#!/usr/bin/env python3
"""Phát hiện bất thường Facebook Ads theo giờ — cài đặt playbook AI-NEXUS (references/playbook.md).

Đọc hourly.json từ mkt-fb-ads-pull-hourly, tính baseline (median cùng giờ 7–14 ngày),
rolling 3h, độ lệch, cổng đủ mẫu, độ bền 2 giờ, pacing, spend multiple, điểm gãy,
và mức hành động. In JSON (stdout) và bảng markdown tiếng Việt (--md).

Ví dụ:
  python3 anomaly.py workspace/fb-ads/act_1/2026-09-09/hourly.json \
      --cpa-target 500000 --roas-target 2.5 --daily-budget 12000000 \
      --level adset --hour 16 --md report.md
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import statistics
import sys
from collections import defaultdict

# ---- Ngưỡng theo playbook (guardrail ban đầu; hiệu chỉnh sau 4–8 tuần) ----
BANDS = ((50, "do"), (30, "cam"), (20, "vang"))          # > 50 đỏ, 30–50 cam, 20–30 vàng
ALERT_DEVIATION = 30.0
PERSIST_HOURS = 2
MIN_SAMPLE = {"impressions": 1000, "link_clicks": 30, "lpv_atc": 50, "lpv_cvr": 100}
PACING_HOT = 1.3
SPEND_MULTIPLE = {"warn": 1.0, "reduce": 2.0, "stop": 3.0}
BASELINE_DAYS = (7, 14)

# metric -> (tử số, mẫu số, hệ số, hướng: 'lower' = càng thấp càng tốt)
RATES = {
    "cpm": ("spend", "impressions", 1000, "lower"),
    "ctr": ("link_clicks", "impressions", 100, "higher"),
    "cpc": ("spend", "link_clicks", 1, "lower"),
    "lpv_rate": ("lpv", "link_clicks", 100, "higher"),
    "atc_rate": ("atc", "lpv", 100, "higher"),
    "checkout_rate": ("checkout", "atc", 100, "higher"),
    "purchase_rate": ("purchase", "checkout", 100, "higher"),
    "cvr": ("purchase", "lpv", 100, "higher"),
    "cpa": ("spend", "purchase", 1, "lower"),
    "roas": ("revenue", "spend", 1, "higher"),
}
SUMS = ("spend", "impressions", "reach", "link_clicks", "lpv", "atc", "checkout", "purchase", "revenue")
LABEL = {"cpm": "CPM", "ctr": "CTR link", "cpc": "CPC link", "lpv_rate": "LPV Rate", "atc_rate": "ATC Rate",
         "checkout_rate": "Checkout Rate", "purchase_rate": "Purchase Rate", "cvr": "CVR", "cpa": "CPA", "roas": "ROAS"}


def rate(sums: dict, m: str):
    num, den, k, _ = RATES[m]
    return sums[num] / sums[den] * k if sums.get(den) else None


def deviation(m: str, cur, base):
    """Độ lệch tự nhiên (hiện tại − nền)/nền × 100; dấu giữ nguyên để hiển thị."""
    if cur is None or base in (None, 0):
        return None
    return (cur - base) / base * 100


def badness(m: str, dev):
    """Mức xấu đi: với chỉ số càng thấp càng tốt = độ lệch; càng cao càng tốt = mức suy giảm."""
    if dev is None:
        return None
    return dev if RATES[m][3] == "lower" else -dev


def band(dev):
    if dev is None:
        return "khong_du_du_lieu"
    for th, name in BANDS:
        if dev > th:
            return name
    return "binh_thuong"


def enough_sample(m: str, sums: dict) -> bool:
    if m in ("cpm", "ctr", "cpc"):
        return sums["impressions"] >= MIN_SAMPLE["impressions"]
    if m == "lpv_rate":
        return sums["link_clicks"] >= MIN_SAMPLE["link_clicks"]
    if m in ("atc_rate", "checkout_rate", "purchase_rate"):
        return sums["lpv"] >= MIN_SAMPLE["lpv_atc"]
    if m == "cvr":
        return sums["lpv"] >= MIN_SAMPLE["lpv_cvr"]
    return True  # cpa/roas dùng spend multiple, không dùng cổng mẫu


def window_sums(rows_by_hour: dict, hour: int, width: int = 3) -> dict:
    s = {k: 0.0 for k in SUMS}
    for h in range(hour - width + 1, hour + 1):
        for k in SUMS:
            s[k] += rows_by_hour.get(h, {}).get(k, 0.0)
    return s


def median_or_none(vals):
    vals = [v for v in vals if v is not None]
    return statistics.median(vals) if vals else None


def analyse_entity(day_rows: dict, today: str, hour: int, cpa_target, roas_target, daily_budget) -> dict:
    """day_rows: {date: {hour: row}} cho một entity."""
    base_days = sorted(d for d in day_rows if d < today)[-BASELINE_DAYS[1]:]
    cur = window_sums(day_rows.get(today, {}), hour)
    prev = window_sums(day_rows.get(today, {}), hour - 1)
    metrics = {}
    bad_flags = []
    for m in RATES:
        cur_v = rate(cur, m)
        base_v = median_or_none(rate(window_sums(day_rows[d], hour), m) for d in base_days)
        dev = deviation(m, cur_v, base_v)
        bad = badness(m, dev)
        prev_bad = badness(m, deviation(m, rate(prev, m), median_or_none(rate(window_sums(day_rows[d], hour - 1), m) for d in base_days)))
        sample_ok = enough_sample(m, cur)
        persistent = bad is not None and bad >= ALERT_DEVIATION and prev_bad is not None and prev_bad >= ALERT_DEVIATION
        real_alert = bool(bad is not None and bad >= ALERT_DEVIATION and sample_ok and persistent)
        metrics[m] = {"label": LABEL[m], "baseline": base_v, "rolling_3h": cur_v, "deviation_pct": dev, "bad_pct": bad,
                      "band": band(bad), "sample_ok": sample_ok, "persistent_2h": persistent, "alert": real_alert}
        if real_alert:
            bad_flags.append(m)

    # Pacing: tỷ trọng tích luỹ lịch sử đến giờ H (median các ngày nền)
    pacing = None
    if daily_budget and base_days:
        shares = []
        for d in base_days:
            tot = sum(r.get("spend", 0) for r in day_rows[d].values())
            upto = sum(r.get("spend", 0) for h, r in day_rows[d].items() if h <= hour)
            if tot > 0:
                shares.append(upto / tot)
        share = median_or_none(shares)
        spent = sum(r.get("spend", 0) for h, r in day_rows.get(today, {}).items() if h <= hour)
        if share:
            expected = daily_budget * share
            pacing = {"share_to_hour": share, "expected_spend": expected, "actual_spend": spent,
                      "ratio": spent / expected if expected else None}

    # Spend multiple: spend tích luỹ từ lần mua gần nhất hôm nay
    spend_since, signals = 0.0, {"atc": 0.0, "checkout": 0.0}
    for h in sorted(day_rows.get(today, {})):
        if h > hour:
            break
        r = day_rows[today][h]
        if r.get("purchase", 0) > 0:
            spend_since, signals = 0.0, {"atc": 0.0, "checkout": 0.0}
        else:
            spend_since += r.get("spend", 0)
            signals["atc"] += r.get("atc", 0)
            signals["checkout"] += r.get("checkout", 0)
    spend_multiple = spend_since / cpa_target if cpa_target else None
    has_buy_signal = signals["atc"] > 0 or signals["checkout"] > 0

    breakpoint_, action, reason = decide(metrics, bad_flags, pacing, spend_multiple, has_buy_signal,
                                         cur, cpa_target, roas_target)
    return {"window": {"date": today, "hour": hour, "sums_3h": cur}, "metrics": metrics, "pacing": pacing,
            "spend_multiple": {"value": spend_multiple, "spend_without_purchase": spend_since,
                               "atc": signals["atc"], "checkout": signals["checkout"]},
            "breakpoint": breakpoint_, "action": action, "reason": reason, "alerts": bad_flags}


def decide(mt, flags, pacing, sm, buy_signal, cur, cpa_target, roas_target):
    """Cây quyết định §4, §5, §7, §11. Trả (điểm gãy, mức hành động, lý do)."""
    a = lambda m: mt[m]["alert"]  # noqa: E731
    b = lambda m: mt[m]["band"]   # noqa: E731
    # Lỗi kỹ thuật nghi ngờ: click tốt nhưng LPV gãy; checkout tốt nhưng purchase gãy
    if a("lpv_rate") and not a("ctr"):
        return ("landing_page", "kiem_tra",
                "Click bình thường nhưng LPV Rate giảm ≥30%, đủ mẫu, kéo dài 2 giờ → nghi trang chậm/sai link/lỗi mobile. "
                "Kiểm tra web ngay; nếu xác minh lỗi thật thì DỪNG traffic bị ảnh hưởng (không chờ đủ mẫu).")
    if a("purchase_rate") and not a("checkout_rate"):
        return ("thanh_toan_tracking", "kiem_tra",
                "Checkout bình thường nhưng Purchase Rate gãy → nghi thanh toán, tồn kho hoặc Purchase Event. "
                "Đối chiếu backend: backend có đơn → giữ ads, sửa Pixel/CAPI; lỗi thật → dừng ngay.")
    if a("checkout_rate") and not a("atc_rate"):
        return ("checkout", "giam_ngan_sach",
                "ATC tốt nhưng Checkout Rate giảm → phí ship, giá cuối hoặc UX checkout. Giảm ngân sách 20–30% và sửa phễu.")
    if a("atc_rate") and not a("lpv_rate"):
        return ("offer_san_pham", "kiem_tra", "LPV tốt nhưng ATC Rate giảm → sản phẩm, giá, niềm tin hoặc offer. Kiểm tra offer/trang sản phẩm.")
    # Spend multiple (§5)
    if sm is not None and sm >= SPEND_MULTIPLE["stop"]:
        return ("khong_co_don", "dung", f"Spend chưa có đơn = {sm:.1f}x CPA mục tiêu (>3x). Chỉ giữ nếu backend xác nhận có đơn; nếu không → dừng ad/ad set.")
    if sm is not None and sm >= SPEND_MULTIPLE["reduce"]:
        if buy_signal:
            return ("attribution_offer", "kiem_tra", f"Spend chưa có đơn = {sm:.1f}x CPA mục tiêu nhưng có ATC/Checkout → kiểm tra attribution và offer trước khi dừng.")
        return ("khong_co_don", "dung", f"Spend chưa có đơn = {sm:.1f}x CPA mục tiêu, không có ATC/Checkout → dừng ad/ad set.")
    # Creative mỏi (§4 dòng 2): CTR giảm + CPC tăng (≥ 2 điều kiện xấu)
    if a("ctr") and a("cpc"):
        return ("creative_audience", "giam_ngan_sach",
                "CTR giảm và CPC tăng ≥30%, đủ impression, kéo dài 2 giờ → creative mỏi hoặc audience bão hoà. "
                "Tắt mẫu yếu, thay creative; giảm ngân sách 20–30% nếu CPA xấu thêm 2 giờ.")
    if a("cpa") and (pacing and pacing.get("ratio") and pacing["ratio"] > PACING_HOT):
        return ("tieu_nhanh_cpa_xau", "giam_ngan_sach", f"CPA lệch xấu kéo dài và pacing {pacing['ratio']:.2f} (>1,3) → giảm ngân sách 20–30%.")
    if a("cpa"):
        return ("cpa", "giam_ngan_sach", "CPA xấu ≥30% kéo dài 2–3 giờ → giảm ngân sách 20–30%, xem breakdown creative.")
    if sm is not None and sm >= SPEND_MULTIPLE["warn"]:
        return ("cho_du_lieu", "theo_doi" if buy_signal else "kiem_tra",
                f"Spend chưa có đơn = {sm:.1f}x CPA mục tiêu (1–2x). " + ("Có tín hiệu mua → chờ, kiểm tra checkout." if buy_signal else "Không có tín hiệu mua → giảm hoặc tắt creative yếu."))
    if a("cpm") and not a("ctr") and not a("cpa"):
        return ("dau_gia", "giu_nguyen", "CPM tăng nhưng CTR và CPA vẫn tốt → đấu giá đắt hơn, traffic vẫn chất lượng. Giữ nguyên.")
    # Cơ hội scale — chỉ là ứng viên; §9 yêu cầu 2–3 ngày ổn định, script không thấy đủ ngày nên chỉ gắn cờ
    cpa_now, roas_now = rate(cur, "cpa"), rate(cur, "roas")
    if cpa_target and roas_target and cpa_now is not None and roas_now is not None \
            and cur["purchase"] >= 2 and cpa_now <= cpa_target * 0.8 and roas_now >= roas_target * 1.2:
        return ("co_hoi_scale", "theo_doi",
                "CPA thấp hơn target ≥20% và ROAS cao hơn target ≥20% trong 3 giờ này. CHƯA scale từ một cửa sổ giờ: "
                "xác nhận ổn định 2–3 ngày và backend có lãi rồi mới tăng 10–20% (mkt-fb-ads-actions).")
    yellow = [m for m in mt if b(m) in ("vang", "cam", "do") and not a(m)]
    if yellow:
        return ("chua_du_bang_chung", "theo_doi", "Có chỉ số lệch 20%+ nhưng chưa đủ mẫu hoặc chưa kéo dài 2 giờ: " + ", ".join(LABEL[m] for m in yellow) + ". Theo dõi thêm, không chỉnh theo cảm xúc.")
    return ("khong", "giu_nguyen", "Mọi chỉ số trong ngưỡng bình thường. Giữ nguyên.")


def fmt(v, m=None):
    if v is None:
        return "—"
    if m in ("ctr", "lpv_rate", "atc_rate", "checkout_rate", "purchase_rate", "cvr"):
        return f"{v:.2f}%"
    if m == "roas":
        return f"{v:.2f}"
    return f"{v:,.0f}".replace(",", ".")


BAND_VI = {"binh_thuong": "Bình thường", "vang": "Vàng", "cam": "Cam", "do": "Đỏ", "khong_du_du_lieu": "Thiếu dữ liệu"}
ACTION_VI = {"giu_nguyen": "Giữ nguyên", "theo_doi": "Theo dõi", "kiem_tra": "Kiểm tra", "giam_ngan_sach": "Giảm ngân sách",
             "dung": "Dừng", "scale": "Scale"}


def to_markdown(result: dict) -> str:
    out = [f"# Bất thường Facebook Ads — {result['act_id']} — {result['date']} {result['hour']:02d}h (rolling 3h, cấp {result['level']})", ""]
    for e in result["entities"]:
        out.append(f"## {e['entity_name']} (`{e['entity_id']}`) → **{ACTION_VI[e['action']]}**")
        out.append(f"Điểm gãy: `{e['breakpoint']}` — {e['reason']}")
        out.append("")
        out.append("| Chỉ số | Baseline | Rolling 3h | Độ lệch | Mức | Đủ mẫu | ≥2h |")
        out.append("|---|---|---|---|---|---|---|")
        for m, v in e["metrics"].items():
            dev = "—" if v["deviation_pct"] is None else f"{v['deviation_pct']:+.1f}%"
            out.append(f"| {v['label']} | {fmt(v['baseline'], m)} | {fmt(v['rolling_3h'], m)} | {dev} | {BAND_VI[v['band']]} | "
                       f"{'✓' if v['sample_ok'] else '✗'} | {'✓' if v['persistent_2h'] else '✗'} |")
        p, s = e["pacing"], e["spend_multiple"]
        if p:
            out.append(f"\nPacing: thực tế {fmt(p['actual_spend'])} / kỳ vọng {fmt(p['expected_spend'])} "
                       f"(tỷ trọng đến giờ {p['share_to_hour']*100:.0f}%) → **{p['ratio']:.2f}**")
        if s["value"] is not None:
            out.append(f"Spend Multiple: {fmt(s['spend_without_purchase'])} chưa có đơn = **{s['value']:.1f}x** CPA mục tiêu "
                       f"(ATC {s['atc']:.0f}, Checkout {s['checkout']:.0f})")
        out.append("")
    return "\n".join(out)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("hourly_json")
    p.add_argument("--level", default="adset", choices=("account", "campaign", "adset", "ad"))
    p.add_argument("--date", help="ngày đánh giá (mặc định: ngày mới nhất trong file)")
    p.add_argument("--hour", type=int, help="giờ đánh giá 0–23 (mặc định: giờ mới nhất có dữ liệu)")
    p.add_argument("--cpa-target", type=float)
    p.add_argument("--roas-target", type=float)
    p.add_argument("--daily-budget", type=float, help="ngân sách ngày của cấp đang xét (dùng cho pacing)")
    p.add_argument("--entity", action="append", help="chỉ xét entity_id này (lặp lại được)")
    p.add_argument("--md", help="ghi bảng markdown tiếng Việt ra file này")
    a = p.parse_args()

    try:
        with open(a.hourly_json, encoding="utf-8") as f:
            doc = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"LỖI: không đọc được {a.hourly_json}: {e}")
    if not doc.get("hourly", True):
        sys.exit("LỖI: file này không có cột giờ (Meta từ chối breakdown). Playbook theo giờ không áp dụng; dùng số theo ngày.")

    rows = [r for r in doc.get("rows", []) if r.get("level") == a.level and r.get("date")]
    if a.entity:
        rows = [r for r in rows if r["entity_id"] in a.entity]
    if not rows:
        sys.exit(f"LỖI: không có dòng nào ở cấp {a.level}.")
    by_entity: dict = defaultdict(lambda: defaultdict(dict))
    names = {}
    for r in rows:
        by_entity[r["entity_id"]][r["date"]][int(r["hour"])] = r
        names[r["entity_id"]] = r.get("entity_name") or r["entity_id"]
    today = a.date or max(r["date"] for r in rows)
    hour = a.hour if a.hour is not None else max((int(r["hour"]) for r in rows if r["date"] == today), default=0)
    if not 0 <= hour <= 23:
        sys.exit("LỖI: --hour phải trong 0–23.")

    entities = []
    for eid, day_rows in by_entity.items():
        if today not in day_rows:
            continue
        res = analyse_entity(day_rows, today, hour, a.cpa_target, a.roas_target, a.daily_budget)
        entities.append({"entity_id": eid, "entity_name": names[eid], **res})
    order = {"dung": 0, "giam_ngan_sach": 1, "kiem_tra": 2, "theo_doi": 3, "giu_nguyen": 4}
    entities.sort(key=lambda e: order[e["action"]])
    result = {"act_id": doc.get("act_id"), "date": today, "hour": hour, "level": a.level,
              "baseline_days": sorted(d for d in {r["date"] for r in rows} if d < today)[-BASELINE_DAYS[1]:],
              "targets": {"cpa": a.cpa_target, "roas": a.roas_target, "daily_budget": a.daily_budget},
              "generated_at": dt.datetime.now().isoformat(timespec="seconds"), "entities": entities}
    if len(result["baseline_days"]) < BASELINE_DAYS[0]:
        result["warning"] = f"Chỉ có {len(result['baseline_days'])} ngày nền (<7). Baseline chưa đáng tin — coi mọi cảnh báo là 'theo dõi'."
    print(json.dumps(result, ensure_ascii=False, indent=1))
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write(to_markdown(result))
        print(f"Đã ghi bảng markdown: {a.md}", file=sys.stderr)


if __name__ == "__main__":
    main()
