---
name: mkt-fb-ads-actions
description: "Thực thi hành động trên Facebook/Meta Ads qua Composio SAU KHI chủ doanh nghiệp xác nhận từng việc: tạm dừng/bật lại campaign, đặt spend cap, tạm dừng ad set hoặc ad, đổi ngân sách ngày ad set trong giới hạn ±10–30% mỗi bước. Luôn xem trước, thực thi, đọc lại để xác minh và ghi vào Decisions/. Dùng khi người dùng nói 'tắt ad set này', 'giảm ngân sách 20%', 'scale campaign', 'bật lại', 'đặt spend cap', hoặc sau khi mkt-fb-ads-anomaly-detector đề xuất hành động và người dùng đồng ý."
ten-viet: "Hành Động Trên Facebook Ads"
nhom: "05. Quảng Cáo Trả Phí"
allowed-tools: Read Write Glob Bash
---

# Hành Động Trên Facebook Ads

Skill duy nhất trong bộ Facebook Ads được phép **ghi** lên Meta. Mọi thứ khác (`mkt-fb-ads-pull-hourly`, `mkt-fb-ads-anomaly-detector`) chỉ đọc.

## Khi nào dùng / Không dùng khi

**Dùng khi** người dùng yêu cầu một hành động cụ thể, hoặc đã đồng ý với đề xuất từ `mkt-fb-ads-anomaly-detector`.

**Không dùng khi**
- Chưa có xác nhận rõ ràng trong chat cho **từng** hành động. "Làm gì thì làm" không phải xác nhận.
- Chưa có bằng chứng số (báo cáo cảnh báo hoặc số người dùng đưa). Không hành động theo cảm xúc — playbook §7.
- Muốn tạo campaign/ad mới → `facebook-ad-campaign` (lập kế hoạch), rồi người dùng tạo trong Ads Manager.

## Điều kiện

```bash
composio connections list   # metaads phải ACTIVE; EXPIRED → composio link metaads
```

Không in access token. Không lưu token vào vault.

## Hành động được phép

| Hành động | Công cụ | Giới hạn |
|---|---|---|
| Tạm dừng / bật lại **campaign** | `METAADS_UPDATE_CAMPAIGN` `{ campaign_id, status: "PAUSED" \| "ACTIVE" }` | — |
| Đặt **spend cap** campaign | `METAADS_UPDATE_CAMPAIGN` `{ campaign_id, spend_cap }` (tiền tệ tài khoản, tối thiểu tương đương 100 USD) | — |
| Tạm dừng / bật lại **ad set** hoặc **ad** | `composio proxy` POST `https://graph.facebook.com/v23.0/<id>` body `status=PAUSED` | Composio không có tool UPDATE_ADSET/AD |
| Đổi **ngân sách ngày ad set** | `composio proxy` POST `.../<adset_id>` body `daily_budget=<đơn vị nhỏ nhất>` | **±10–30% mỗi bước**; scale chỉ 10–20% |

Không được: DELETE/ARCHIVE, đổi targeting, đổi creative, tăng > 30% một lần, tăng liên tiếp trong cùng ngày, tắt toàn bộ campaign khi vẫn có ad đạt target (playbook §6). Bị yêu cầu vượt giới hạn → từ chối, giải thích quy tắc scale §9, đề nghị bước nhỏ hơn.

Đơn vị ngân sách: Graph API nhận **đơn vị nhỏ nhất** của tiền tệ (VND không có phần lẻ → 500000 = 500.000đ; USD → cents). Xác nhận `currency` của tài khoản trước khi tính.

## Quy trình cho MỖI hành động

### 1. Xác định đối tượng và trạng thái hiện tại

```bash
composio execute METAADS_GET_OBJECT -d '{ object_id: "<id>", fields: "id,name,status,effective_status,daily_budget,lifetime_budget,campaign_id" }'
```

Ghi lại giá trị hiện tại (để rollback). Tên trong kết quả phải khớp với tên người dùng nói; lệch → dừng, hỏi lại.

### 2. Tính và nêu rõ thay đổi

Ví dụ: "Ad set *Retarget 7d* (`1234`) đang `daily_budget=1.000.000đ`. Giảm 20% → `800.000đ`. Bằng chứng: CPA rolling 3h 820.000đ vs nền 500.000đ (+64%), kéo dài 3 giờ, đủ mẫu (báo cáo `Cảnh Báo/2026-09-09 16h — …`)."

### 3. Xin xác nhận

Hỏi đúng một câu, chờ người dùng trả lời **có/đồng ý/ok** cho hành động này. Không gộp nhiều hành động vào một câu hỏi. Không có xác nhận → không chạy bước 4.

### 4. Xem trước rồi thực thi

Campaign:

```bash
composio execute METAADS_UPDATE_CAMPAIGN --dry-run -d '{ campaign_id: "<id>", status: "PAUSED" }'
composio execute METAADS_UPDATE_CAMPAIGN           -d '{ campaign_id: "<id>", status: "PAUSED" }'
```

Ad set / ad (echo lệnh đầy đủ cho người dùng thấy trước khi chạy):

```bash
composio proxy 'https://graph.facebook.com/v23.0/<adset_id>' --toolkit metaads -X POST \
  -H 'content-type: application/x-www-form-urlencoded' -d 'daily_budget=800000'
# tạm dừng: -d 'status=PAUSED' ; bật lại: -d 'status=ACTIVE'
```

Phản hồi `{"success": true}` mới là thành công. Lỗi 190 → kết nối hết hạn; lỗi 100 → tham số/đơn vị sai; lỗi 200 → thiếu quyền `ads_management`.

### 5. Đọc lại để xác minh

```bash
composio execute METAADS_GET_OBJECT -d '{ object_id: "<id>", fields: "id,name,status,effective_status,daily_budget" }'
```

Giá trị phải bằng giá trị mong muốn. Không khớp → báo ngay, không thử lại tự động quá 1 lần.

### 6. Ghi vào Decisions

File `Decisions/YYYY-MM-DD — Facebook Ads — <hành động ngắn>.md`, theo mẫu `[Mẫu] Quyết Định.md`, thêm các mục:

| Mục | Nội dung |
|---|---|
| Quyết định gì | Một câu: đối tượng, thay đổi, giá trị trước → sau |
| Bối cảnh | Số liệu: baseline, rolling 3h, độ lệch, kéo dài mấy giờ, spend multiple; link báo cáo `[[YYYY-MM-DD HHh — tài khoản]]` |
| Ai chốt · ai thực hiện | Người chốt: tên người dùng xác nhận trong chat; thực hiện: agent; thời điểm (giờ máy + múi giờ tài khoản) |
| Điều kiện xem lại | Sau 24 giờ: CPA/ROAS cần đạt gì; nếu CPA tăng > 30% sau scale → quay về mức trước |
| Rollback | Lệnh chính xác để trả về giá trị cũ (xem dưới) |

Frontmatter: `type: quyet-dinh`, `linh-vuc: Ngân sách`, `tai-khoan`, `doi-tuong: <id>`, `tags: [facebook-ads]`.

### 7. Báo lại

Ba dòng: đã làm gì (trước → sau), đã xác minh chưa, đường dẫn đầy đủ file Decisions và giờ cần xem lại.

## Rollback

Mỗi hành động có một lệnh đảo ngược; ghi sẵn vào Decisions và chạy khi người dùng yêu cầu hoặc khi điều kiện xem lại kích hoạt:

| Đã làm | Rollback |
|---|---|
| `status=PAUSED` | `status=ACTIVE` (cùng endpoint/tool) |
| `daily_budget` A → B | `daily_budget=A` |
| `spend_cap` đặt mới | `METAADS_UPDATE_CAMPAIGN { campaign_id, spend_cap: <giá trị cũ> }`; nếu trước đó không có cap, ghi rõ trong Decisions rằng không thể xoá cap qua Composio — người dùng gỡ trong Ads Manager |

Rollback cũng là một hành động: đi qua đúng 7 bước trên (xác nhận, dry-run, thực thi, xác minh, ghi Decisions).

## Không bao giờ

- Không hành động khi Meta chưa có đơn nhưng backend có đơn — đó là lỗi tracking, giữ ads (playbook §4).
- Không scale từ một giờ đẹp; cần 2–3 ngày ổn định và backend xác nhận lãi (§9).
- Không chạy nhiều thay đổi trên cùng đối tượng trong một giờ.
