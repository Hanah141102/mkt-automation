---
name: mkt-fb-ads-anomaly-detector
description: "Phát hiện bất thường Facebook Ads theo giờ đúng playbook AI-NEXUS: đường nền median cùng khung giờ 7–14 ngày, rolling 3 giờ, độ lệch 20/30/50%, cổng đủ mẫu, kéo dài ≥2 giờ, pacing, spend multiple theo CPA mục tiêu, tìm điểm gãy trong phễu và đề xuất một trong sáu mức hành động (giữ nguyên / theo dõi / kiểm tra / giảm ngân sách / dừng / scale). Chỉ phân tích, không sửa gì trên Meta. Dùng khi người dùng hỏi 'ads có bất thường không', 'giờ này CPA sao', 'có nên tắt ad này', 'đánh giá ads theo giờ', hoặc sau khi chạy mkt-fb-ads-pull-hourly."
ten-viet: "Phát Hiện Bất Thường Facebook Ads Theo Giờ"
nhom: "05. Quảng Cáo Trả Phí"
allowed-tools: Read Write Glob Bash
---

# Phát Hiện Bất Thường Facebook Ads Theo Giờ

Nguyên tắc: **BẤT THƯỜNG = LỆCH ĐỦ LỚN + ĐỦ DỮ LIỆU + KÉO DÀI ĐỦ LÂU.** Ngoại lệ duy nhất: lỗi website/checkout/link → dừng ngay, không chờ đủ mẫu. Toàn bộ công thức và bảng quyết định nằm ở `references/playbook.md` — đọc trước khi diễn giải kết quả.

## Khi nào dùng / Không dùng khi

**Dùng khi**
- Đã có `hourly.json` (từ `mkt-fb-ads-pull-hourly`) và cần biết chỉ số nào lệch, lệch bao nhiêu, đủ dữ liệu chưa, làm gì tiếp.
- Người dùng lo lắng vì một giờ xấu: skill này ngăn "tối ưu theo cảm xúc".
- Chạy định kỳ mỗi giờ (scheduled) để đưa cảnh báo.

**Không dùng khi**
- Chưa có dữ liệu theo giờ → chạy `mkt-fb-ads-pull-hourly` trước.
- Cần thực thi (tắt, giảm ngân sách, scale) → `mkt-fb-ads-actions`, và chỉ sau khi người dùng xác nhận.
- Muốn phân tích nguyên nhân dài hạn theo tuần/tháng → `ads-performance-diagnostic`, `mkt-marketing-root-cause`.

## Điều kiện

- `python3` (chỉ dùng thư viện chuẩn).
- File `workspace/fb-ads/<act_id>/<YYYY-MM-DD>/hourly.json` với `"hourly": true` và ≥ 7 ngày nền (script cảnh báo nếu ít hơn).
- **Mục tiêu**: CPA mục tiêu, ROAS mục tiêu, ngân sách ngày của cấp đang xét. Thứ tự tìm: (1) người dùng cho trong chat; (2) `03. Areas/Marketing Channels/Facebook Ads/Mục Tiêu.md`; (3) suy từ `00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md` và `Sản Phẩm & Dịch Vụ/` (AOV, biên). Không có thì **hỏi**, tuyệt đối không bịa. Thiếu mục tiêu thì script vẫn chạy nhưng bỏ qua spend multiple và pacing — nói rõ điều đó trong báo cáo.

## Quy trình

### 1. Chạy script

```bash
python3 .claude/skills/mkt-fb-ads-anomaly-detector/scripts/anomaly.py \
  workspace/fb-ads/act_123/2026-09-09/hourly.json \
  --level adset --cpa-target 500000 --roas-target 2.5 --daily-budget 12000000 \
  --md workspace/fb-ads/act_123/2026-09-09/anomaly-16h.md
# --hour 16 --date 2026-09-09 để chọn cửa sổ; --entity <id> để xét một ad set
```

Script làm gì (xem `references/playbook.md` §1–§8):

| Bước | Cách tính |
|---|---|
| Baseline | Median cùng khung giờ (rolling 3h) của tối đa 14 ngày trước, không tính hôm nay |
| Rolling 3h | Cộng tử số và mẫu số 3 giờ rồi tính lại tỷ lệ (CTR, LPV/ATC/Checkout/Purchase Rate, CVR); CPM, CPC, CPA, ROAS từ tổng |
| Độ lệch | `(hiện tại − nền)/nền`; với chỉ số càng cao càng tốt dùng mức suy giảm. Dương = xấu |
| Mức | < 20% bình thường · 20–30% vàng · 30–50% cam · > 50% đỏ |
| Đủ mẫu | CPM/CTR/CPC ≥ 1.000 impression · LPV Rate ≥ 30 click · ATC/Checkout/Purchase Rate ≥ 50 LPV · CVR ≥ 100 LPV |
| Kéo dài | Lệch ≥ 30% ở cả cửa sổ giờ H và H−1 |
| Cảnh báo thật | `|lệch| ≥ 30% AND đủ mẫu AND ≥ 2 giờ` |
| Pacing | Ngân sách ngày × median tỷ trọng tích luỹ đến giờ H của các ngày nền; > 1,3 và CPA xấu mới đáng lo |
| Spend multiple | Spend tích luỹ từ lần mua gần nhất hôm nay / CPA mục tiêu; 1x cảnh báo, 2x giảm, 3x dừng (tuỳ có ATC/Checkout hay không) |
| Điểm gãy | Bảng chẩn đoán §4: đấu giá · creative/audience · landing page · offer · checkout · thanh toán/tracking · không có đơn |
| Hành động | `giu_nguyen` / `theo_doi` / `kiem_tra` / `giam_ngan_sach` / `dung`; cơ hội `scale` chỉ được gắn cờ, không đề xuất từ một giờ |

Đầu ra: JSON ở stdout (mỗi entity có `metrics`, `pacing`, `spend_multiple`, `breakpoint`, `action`, `reason`) và bảng markdown tiếng Việt ở `--md`. Entity xếp theo mức khẩn: dừng → giảm → kiểm tra → theo dõi → giữ.

### 2. Diễn giải — tách fact / suy luận / giả định

- **Fact**: số trong JSON (baseline, rolling 3h, độ lệch, cờ đủ mẫu).
- **Suy luận**: điểm gãy và hành động script chọn. Kiểm tra lại bằng bảng §4: điểm gãy ở web/checkout thì đổi creative không giải quyết được.
- **Giả định**: mục tiêu CPA/ROAS/ngân sách lấy từ đâu; dữ liệu Meta trễ 15–60 phút; attribution 7d_click.
- Chỉ nâng lên cảnh báo mạnh khi **≥ 2 điều kiện xấu cùng xuất hiện** (CTR giảm + CPC tăng; CPA tăng + spend multiple vượt ngưỡng).
- Meta không có đơn nhưng backend có đơn → điểm gãy là tracking, **giữ ads**. Luôn nhắc người dùng đối chiếu backend trước khi tin Meta.
- Có `warning` "< 7 ngày nền" → hạ mọi hành động xuống tối đa `theo_doi`, trừ lỗi kỹ thuật đã xác minh.

### 3. Ghi báo cáo vào vault

> Không ghi vào vault thì coi như chưa làm.

| | |
|---|---|
| Thư mục | `03. Areas/Marketing Channels/Facebook Ads/Cảnh Báo/` |
| Tên file | `YYYY-MM-DD HHh — <tên tài khoản>.md` |
| Frontmatter | `type: canh-bao-ads`, `tai-khoan`, `ngay`, `gio`, `cap-do`, `hanh-dong` (mức cao nhất), `tags: [facebook-ads, canh-bao]` |

Cấu trúc bắt buộc:

1. **Tình trạng** — một câu: mấy entity cần dừng/giảm/kiểm tra, còn lại ổn.
2. **Bảng chỉ số** — copy bảng markdown của script (baseline / rolling 3h / độ lệch / mức / đủ mẫu / ≥2h) cho các entity có cảnh báo; entity bình thường gom một dòng.
3. **Điểm gãy** — theo bảng §4, kèm bằng chứng số.
4. **Hành động đề xuất** — mức hành động + việc cụ thể (tắt creative nào, giảm bao nhiêu %, kiểm tra gì). Ghi rõ: *chưa thực hiện; cần chủ doanh nghiệp xác nhận, thực thi bằng `/mkt-fb-ads-actions`.*
5. **Checklist kiểm tra** (§10) — backend có đơn? Pixel/CAPI? tự mở ad trên mobile? test ATC/mã giảm giá/ship/thanh toán? đủ impression/click/spend multiple? breakdown theo creative? ghi lại thời điểm hành động.
6. **Xem lại sau 24 giờ** — chỉ số nào cần đạt gì để kết luận hành động đúng; nếu CPA tăng > 30% sau khi đổi → quay về mức trước.

Link về `[[Tài Khoản Quảng Cáo]]` và, nếu có hành động được duyệt, về file trong `Decisions/`.

### 4. Trả lời người dùng

Tối đa ~10 dòng tiếng Việt: tình trạng, 1–3 entity đáng chú ý với số cụ thể (baseline → hiện tại, lệch %), điểm gãy, hành động đề xuất và câu hỏi xác nhận ("Anh/chị duyệt giảm 20% ad set X không?"). Đường dẫn đầy đủ của file báo cáo ở cuối.

## Không bao giờ

- Không dừng vì ROAS của một giờ xấu. Không scale vì một giờ đẹp.
- Không gọi công cụ ghi lên Meta trong skill này.
- Không bịa mục tiêu, không bịa số backend.
