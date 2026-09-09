---
name: mkt-fb-ads-pull-hourly
description: "Kéo số liệu Facebook/Meta Ads theo từng giờ (spend, impression, click, LPV, ATC, checkout, purchase, doanh thu) cho một hoặc nhiều tài khoản quảng cáo qua Composio, chuẩn hoá thành hourly.json để skill phát hiện bất thường đọc. Chỉ đọc, không sửa gì trên Meta. Dùng khi người dùng nói 'kéo số ads theo giờ', 'lấy insight facebook ads', 'cập nhật dữ liệu ads hôm nay', hoặc trước khi chạy mkt-fb-ads-anomaly-detector."
ten-viet: "Kéo Số Facebook Ads Theo Giờ"
nhom: "05. Quảng Cáo Trả Phí"
allowed-tools: Read Write Glob Bash
---

# Kéo Số Facebook Ads Theo Giờ

## Khi nào dùng / Không dùng khi

**Dùng khi**
- Cần dữ liệu theo giờ của 7–14 ngày gần nhất để so sánh cùng khung giờ (đường nền cho `mkt-fb-ads-anomaly-detector`).
- Cập nhật số hôm nay trước một phiên đánh giá theo giờ.
- Người dùng hỏi "tài khoản nào đang chạy", "hôm nay tiêu bao nhiêu đến giờ này".

**Không dùng khi**
- Cần phân tích hoặc ra quyết định → chạy `mkt-fb-ads-anomaly-detector` sau khi đã có `hourly.json`.
- Cần bật/tắt/đổi ngân sách → `mkt-fb-ads-actions`. Skill này **không bao giờ ghi** lên Meta.
- Chỉ cần số theo ngày cho báo cáo tháng → `mkt-marketing-report-writer`.

## Điều kiện bắt buộc

```bash
command -v composio            # CLI có sẵn
composio connections list      # metaads phải ở trạng thái ACTIVE
```

Nếu `metaads` là EXPIRED hoặc không có: dừng, báo người dùng chạy `composio link metaads` rồi thử lại. Không in access token, không lưu token vào vault.

## Đầu vào

| Đầu vào | Bắt buộc | Ghi chú |
|---|---|---|
| `act_id` (một hoặc nhiều) | Có | Dạng `act_123456789`. Không nhớ thì liệt kê bằng bước 1 |
| Số ngày lịch sử | Không | Mặc định 14 (đủ cho median 7–14 ngày) |
| Cấp độ | Không | Mặc định `account,campaign,adset,ad` |
| Thư mục ra | Không | Mặc định `workspace/fb-ads/<act_id>/<YYYY-MM-DD>/hourly.json` |

## Quy trình

### 1. Xác định tài khoản

```bash
composio execute METAADS_GET_AD_ACCOUNTS -d '{ fields: "id,account_id,name,currency,timezone_name,account_status", limit: 100 }'
```

Ghi lại `id` (có tiền tố `act_`), `currency` và `timezone_name` — giờ trong dữ liệu là **giờ theo múi giờ của tài khoản quảng cáo**, không phải giờ máy. Nếu người dùng gọi tên tài khoản, khớp theo `name`; không khớp được thì hỏi lại, không đoán.

### 2. Kéo dữ liệu theo giờ (đường chính — Graph API qua `composio proxy`)

`METAADS_GET_INSIGHTS` không có tham số `time_increment`, nên dòng theo giờ lấy qua Graph API với tài khoản Composio đã kết nối:

```bash
python3 .claude/skills/mkt-fb-ads-pull-hourly/scripts/pull_hourly.py \
  --act act_123456789 --days 14 --levels account,campaign,adset,ad
# thêm --act cho mỗi tài khoản; --out để đổi thư mục
```

Script gọi tuần tự:

```
composio proxy 'https://graph.facebook.com/v23.0/<act_id>/insights?level=<level>&time_increment=1
  &breakdowns=hourly_stats_aggregated_by_advertiser_time_zone
  &fields=spend,impressions,reach,frequency,actions,action_values,campaign_id,campaign_name,adset_id,adset_name,ad_id,ad_name
  &time_range={"since":"YYYY-MM-DD","until":"YYYY-MM-DD"}&limit=500' --toolkit metaads
```

rồi đi theo `paging.next` cho đến hết, chuẩn hoá mỗi dòng thành:

```json
{ "date": "2026-09-09", "hour": 14, "level": "adset", "entity_id": "…", "entity_name": "…",
  "spend": 0, "impressions": 0, "reach": 0, "link_clicks": 0, "lpv": 0, "atc": 0,
  "checkout": 0, "purchase": 0, "revenue": 0, "frequency": 0 }
```

`actions`/`action_values` được tách theo `action_type`: `link_click`, `landing_page_view`, `add_to_cart`, `initiate_checkout`, `purchase` (ưu tiên `omni_purchase` nếu có). Chạy lại cùng ngày sẽ ghi đè file cũ — an toàn, không nhân đôi dữ liệu.

Script in đúng một dòng tóm tắt: số dòng, khoảng ngày, đường dẫn file. Báo lại dòng đó cho người dùng.

### 3. Đường phụ — `METAADS_GET_INSIGHTS` (khi chỉ cần số theo ngày hoặc proxy lỗi)

```bash
composio execute METAADS_GET_INSIGHTS -d '{
  object_id: "act_123456789", level: "campaign",
  fields: ["spend","impressions","clicks","reach","frequency","actions","action_values","campaign_id","campaign_name"],
  time_range: { since: "2026-09-01", until: "2026-09-09" },
  action_attribution_windows: ["7d_click"]
}'
```

Lưu ý: `time_range` phải là object (không phải chuỗi JSON); không gửi cùng lúc `date_preset`; phân trang bằng `after`. Kết quả không có cột giờ — chỉ dùng để đối chiếu tổng ngày hoặc khi người dùng chấp nhận số theo ngày.

### 4. Bổ sung tên và trạng thái (tuỳ chọn)

Khi dòng insight thiếu tên hoặc cần trạng thái ACTIVE/PAUSED:

```bash
composio execute METAADS_READ_ADSETS -d '{ account_id: "act_123456789", fields: "id,name,status,daily_budget,campaign_id" }'
composio execute METAADS_LIST_ADS   -d '{ account_id: "act_123456789", fields: "id,name,status,adset_id" }'   # fields là MỘT chuỗi
composio execute METAADS_GET_OBJECT -d '{ object_id: "<id>", fields: "id,name,status,daily_budget" }'
```

Muốn xem schema chính xác: `composio execute <SLUG> --get-schema`; muốn xem trước không gọi thật: thêm `--dry-run`.

## Lỗi hay gặp

| Triệu chứng | Nguyên nhân | Xử lý |
|---|---|---|
| 401 `OAuthException` code 190 subcode 463 | Kết nối Meta hết hạn | `composio link metaads`, chạy lại |
| 403 code 200 "Missing Permissions" | Tài khoản Composio không có quyền `ads_read` trên act đó | Kết nối lại bằng user có quyền, hoặc bỏ act đó |
| 400 code 100 khi có `breakdowns` | Breakdown không được hỗ trợ cho level/field đó | Script tự thử lại không breakdown và báo "chỉ có số theo ngày" |
| Lỗi validate `time_range` | Gửi chuỗi thay vì object | Dùng `{ since, until }` dạng object |
| Dữ liệu rỗng cho hôm nay | Meta trễ 15–60 phút | Chờ, không kết luận |

## Ghi kết quả vào đâu

| | |
|---|---|
| Dữ liệu thô | `workspace/fb-ads/<act_id>/<YYYY-MM-DD>/hourly.json` (không commit — `workspace/` đã gitignore) |
| Danh sách tài khoản đang theo dõi | `03. Areas/Marketing Channels/Facebook Ads/Tài Khoản Quảng Cáo.md` — bảng `act_id · tên · tiền tệ · múi giờ · ngày cập nhật` |

Không ghi số liệu thô vào vault; vault chỉ giữ báo cáo do `mkt-fb-ads-anomaly-detector` viết.

## Báo lại người dùng

Một đoạn ngắn: tài khoản đã kéo, khoảng ngày, số dòng theo cấp độ, đường dẫn `hourly.json`, và gợi ý bước tiếp theo (`/mkt-fb-ads-anomaly-detector`).
