#!/usr/bin/env python3
"""Kéo insight Facebook Ads theo giờ qua `composio proxy` và ghi hourly.json.

Chỉ đọc. Không in token. Chạy lại cùng ngày sẽ ghi đè file cũ (idempotent).

Ví dụ:
  python3 pull_hourly.py --act act_123 --act act_456 --days 14
  python3 pull_hourly.py --act act_123 --levels account,campaign --out /tmp/h.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
from urllib.parse import quote

GRAPH = "https://graph.facebook.com/v23.0"
LEVELS = ("account", "campaign", "adset", "ad")
FIELDS = (
    "spend,impressions,reach,frequency,actions,action_values,"
    "campaign_id,campaign_name,adset_id,adset_name,ad_id,ad_name,account_name"
)
HOUR_BREAKDOWN = "hourly_stats_aggregated_by_advertiser_time_zone"

ACTION_KEYS = {
    "link_click": "link_clicks",
    "landing_page_view": "lpv",
    "add_to_cart": "atc",
    "initiate_checkout": "checkout",
}
PURCHASE_TYPES = ("omni_purchase", "purchase")


def die(msg: str, code: int = 1) -> None:
    print(f"LỖI: {msg}", file=sys.stderr)
    sys.exit(code)


def proxy(url: str) -> dict:
    """Gọi Graph API qua Composio với tài khoản metaads đã kết nối."""
    cmd = ["composio", "proxy", url, "--toolkit", "metaads"]
    try:
        run = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except FileNotFoundError:
        die("không tìm thấy lệnh `composio`. Cài CLI rồi chạy `composio login`.")
    except subprocess.TimeoutExpired:
        die("Composio không phản hồi sau 120 giây. Thử lại sau.")
    out = run.stdout.strip()
    # CLI có thể in thêm dòng trạng thái; lấy khối JSON đầu tiên từ dấu { đầu.
    start = out.find("{")
    if run.returncode != 0 or start < 0:
        text = (run.stderr or out)[:400]
        if "code=190" in text or '"code":190' in text or "463" in text:
            die("kết nối Meta Ads đã hết hạn (OAuth 190/463). Chạy `composio link metaads` rồi thử lại.")
        if "Missing Permissions" in text or '"code":200' in text:
            die("tài khoản Composio không có quyền đọc ads trên tài khoản này (403 code 200).")
        die(f"composio proxy thất bại: {text}")
    try:
        payload = json.loads(out[start:])
    except json.JSONDecodeError:
        die("không đọc được JSON từ Composio. Chạy lệnh thủ công để xem phản hồi.")
    # Composio bọc phản hồi trong {data: {...}} hoặc trả thẳng.
    if isinstance(payload, dict) and "data" in payload and isinstance(payload["data"], dict) \
            and ("data" in payload["data"] or "error" in payload["data"]):
        payload = payload["data"]
    if isinstance(payload, dict) and "error" in payload:
        err = payload["error"]
        code = err.get("code")
        if code == 190:
            die("kết nối Meta Ads đã hết hạn (OAuth 190). Chạy `composio link metaads`.")
        if code == 100:
            raise ValueError("BREAKDOWN_400")
        die(f"Graph API trả lỗi {code}: {err.get('message', '')[:200]}")
    return payload


def build_url(act: str, level: str, since: str, until: str, with_hours: bool) -> str:
    tr = quote(json.dumps({"since": since, "until": until}, separators=(",", ":")))
    url = (f"{GRAPH}/{act}/insights?level={level}&time_increment=1&fields={FIELDS}"
           f"&time_range={tr}&limit=500&action_attribution_windows=%5B%227d_click%22%5D")
    if with_hours:
        url += f"&breakdowns={HOUR_BREAKDOWN}"
    return url


def fetch_pages(url: str) -> list[dict]:
    rows: list[dict] = []
    while url:
        page = proxy(url)
        rows.extend(page.get("data", []))
        url = (page.get("paging") or {}).get("next")
    return rows


def num(v) -> float:
    try:
        return float(v or 0)
    except (TypeError, ValueError):
        return 0.0


def actions_of(row: dict, key: str) -> dict[str, float]:
    return {a.get("action_type", ""): num(a.get("value")) for a in row.get(key) or []}


def normalise(row: dict, level: str, act: str) -> dict:
    hour = 0
    span = row.get(HOUR_BREAKDOWN)
    if span:
        hour = int(str(span).split(":")[0])
    ids = {
        "account": (act, row.get("account_name") or act),
        "campaign": (row.get("campaign_id"), row.get("campaign_name")),
        "adset": (row.get("adset_id"), row.get("adset_name")),
        "ad": (row.get("ad_id"), row.get("ad_name")),
    }[level]
    acts = actions_of(row, "actions")
    vals = actions_of(row, "action_values")
    purchase = next((acts[t] for t in PURCHASE_TYPES if t in acts), 0.0)
    revenue = next((vals[t] for t in PURCHASE_TYPES if t in vals), 0.0)
    out = {
        "date": row.get("date_start"),
        "hour": hour,
        "level": level,
        "entity_id": ids[0] or "",
        "entity_name": ids[1] or "",
        "spend": num(row.get("spend")),
        "impressions": num(row.get("impressions")),
        "reach": num(row.get("reach")),
        "frequency": num(row.get("frequency")),
        "purchase": purchase,
        "revenue": revenue,
    }
    for action_type, col in ACTION_KEYS.items():
        out[col] = acts.get(action_type, 0.0)
    return out


def pull_account(act: str, days: int, levels: list[str]) -> tuple[list[dict], bool]:
    today = dt.date.today()
    since = (today - dt.timedelta(days=days)).isoformat()
    until = today.isoformat()
    rows: list[dict] = []
    hourly = True
    for level in levels:
        try:
            raw = fetch_pages(build_url(act, level, since, until, with_hours=True))
        except ValueError as e:
            if str(e) != "BREAKDOWN_400":
                raise
            print(f"CẢNH BÁO: {act}/{level}: Meta từ chối breakdown theo giờ (400), "
                  f"chuyển sang số theo ngày (hour=0).", file=sys.stderr)
            hourly = False
            raw = fetch_pages(build_url(act, level, since, until, with_hours=False))
        rows.extend(normalise(r, level, act) for r in raw)
    return rows, hourly


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--act", action="append", required=True, help="act_<id>; lặp lại cho nhiều tài khoản")
    p.add_argument("--days", type=int, default=14, help="số ngày lịch sử (mặc định 14)")
    p.add_argument("--levels", default="account,campaign,adset,ad")
    p.add_argument("--out", help="đường dẫn file JSON (mặc định workspace/fb-ads/<act>/<hôm nay>/hourly.json)")
    a = p.parse_args()

    levels = [l.strip() for l in a.levels.split(",") if l.strip()]
    bad = [l for l in levels if l not in LEVELS]
    if bad:
        die(f"cấp độ không hợp lệ: {', '.join(bad)}. Chọn trong {', '.join(LEVELS)}.")
    if a.days < 3 or a.days > 90:
        die("--days phải trong khoảng 3–90.")
    if len(a.act) > 1 and a.out:
        die("--out chỉ dùng khi kéo MỘT tài khoản; nhiều tài khoản sẽ tự tách thư mục.")

    today = dt.date.today().isoformat()
    summaries = []
    for act in a.act:
        if not act.startswith("act_"):
            die(f"'{act}' phải có tiền tố act_ (ví dụ act_123456789).")
        rows, hourly = pull_account(act, a.days, levels)
        out = a.out or os.path.join("workspace", "fb-ads", act, today, "hourly.json")
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        doc = {
            "act_id": act,
            "pulled_at": dt.datetime.now().isoformat(timespec="seconds"),
            "days": a.days,
            "levels": levels,
            "hourly": hourly,
            "row_count": len(rows),
            "rows": sorted(rows, key=lambda r: (r["level"], r["entity_id"], r["date"] or "", r["hour"])),
        }
        with open(out, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=1)
        by_level = {l: sum(1 for r in rows if r["level"] == l) for l in levels}
        summaries.append(f"{act}: {len(rows)} dòng ({by_level}) {a.days} ngày → {out}"
                         + ("" if hourly else " [KHÔNG có giờ]"))
    print("OK " + " | ".join(summaries))


if __name__ == "__main__":
    main()
