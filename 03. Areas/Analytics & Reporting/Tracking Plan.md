---
type: tracking-plan
trang-thai: de-xuat
cap-nhat: 2026-08-13
---

# Tracking Plan

## Mục tiêu

Đo số lần người dùng bấm liên kết mời vào nhóm Zalo Agents, phân biệt nguồn
Facebook, TikTok, YouTube và quảng cáo trước khi chuyển người dùng tới Zalo.

Liên kết trung gian dự kiến: `https://tranvanhoang.com/zalo-agents`.

## Kiến trúc đề xuất

1. Mỗi kênh dùng cùng một đường dẫn nhưng có bộ UTM riêng.
2. Route `/zalo-agents` trả một trang chuyển tiếp rất nhẹ.
3. Trình duyệt gửi sự kiện về API cùng tên miền bằng `sendBeacon`.
4. Sau khi gửi sự kiện hoặc hết thời gian chờ ngắn, trang dùng
   `location.replace()` để mở nhóm Zalo.
5. API lưu dữ liệu click tối thiểu và có thể đồng thời gửi sự kiện sang GA4.
6. Bot xem trước liên kết không chạy JavaScript nên không được tính là click
   của người thật; trang vẫn có nút Zalo dự phòng nếu tự động chuyển thất bại.

## Sự kiện

| Tên sự kiện | Ý nghĩa | Thuộc tính |
|---|---|---|
| `zalo_redirect_requested` | Route được gọi, gồm cả crawler và bot xem trước | `source`, `medium`, `campaign`, `content`, `user_agent_class`, `is_bot` |
| `zalo_redirect_clicked` | Người dùng thật kích hoạt chuyển sang Zalo | `source`, `medium`, `campaign`, `content`, `term`, `referrer_host`, `destination`, `click_id` |
| `zalo_redirect_failed` | Không thể gửi sự kiện hoặc mở Zalo | `reason`, `source`, `destination` |

`zalo_redirect_clicked` là chỉ số click sang Zalo, không phải số người đã vào
nhóm. Chỉ coi là thành viên mới khi Zalo cung cấp dữ liệu hoặc cơ chế đối soát.

## Quy ước UTM

| Kênh | `utm_source` | `utm_medium` |
|---|---|---|
| Facebook tự nhiên | `facebook` | `organic_social` |
| TikTok tự nhiên | `tiktok` | `organic_social` |
| YouTube tự nhiên | `youtube` | `organic_video` |
| Meta Ads | nguồn động của Meta | `paid_social` |
| TikTok Ads | `tiktok` | `paid_social` |
| Google/YouTube Ads | `google` hoặc `youtube` | `paid_video` hoặc `cpc` |

Luôn dùng chữ thường. `utm_campaign` mô tả chiến dịch; `utm_content` phân biệt
bài, video hoặc mẫu quảng cáo; `utm_id` giữ ID chiến dịch quảng cáo khi có.

## Báo cáo cần có

- Tổng click và click hợp lệ theo ngày.
- Click theo nguồn, medium, chiến dịch và nội dung.
- Tỷ lệ click hợp lệ sau khi loại bot và lượt lặp kỹ thuật.
- Với quảng cáo: chi phí trên một click sang Zalo sau khi nối dữ liệu chi tiêu.

## Chất lượng dữ liệu và quyền riêng tư

- Không lưu họ tên, số điện thoại, email hoặc nội dung tài khoản Zalo.
- Không nhận URL đích từ query string; URL Zalo phải được cố định phía server để
  tránh tạo open redirect.
- Chỉ nhận các trường UTM có allowlist và giới hạn độ dài.
- Không coi request `HEAD`, bot xem trước liên kết hoặc crawler là click thật.
- Chưa lưu IP thô. Nếu sau này cần ước tính người dùng duy nhất, phải chốt cách
  thông báo, thời hạn lưu và cơ sở xử lý dữ liệu trước khi triển khai.

## Việc cần làm khi nhận source code

- Xác định framework, hosting, GA4/GTM hiện có và nơi lưu dữ liệu.
- Chọn cách lưu sự kiện phù hợp với hạ tầng sẵn có.
- Cài route, API tracking, trang dự phòng và bộ lọc bot.
- Kiểm thử từng URL UTM trên trình duyệt Facebook, TikTok và YouTube.
- Cập nhật bình luận mặc định của skill đăng fanpage sang link tracking chỉ sau
  khi route production đã được kiểm thử thành công.

## Liên kết

- [[Chân Dung Doanh Nghiệp]]
- [[Brand Voice — Giọng Thương Hiệu]]
