# Smoke Test — Use Case 3 — Đăng bài đa nền tảng

- Thư mục test: `/Users/tonyhoang/Documents/GitHub/mkt-automation`
- Ngày test: 2026-08-12

## Skill được kiểm tra

1. `$mkt-multiplatform-content-factory`: chuẩn bị gói nội dung và caption theo kênh; không có quyền xuất bản.
2. `$mkt-blotato-publish-social`: skill xuất bản; ưu tiên Composio, dùng Blotato khi cần.

## Kết quả

| Hạng mục | Kết quả | Bằng chứng |
|---|---|---|
| Publisher CLI khởi động | PASS | `blotato_publish.py --help` trả về đủ 4 lệnh `accounts`, `upload`, `publish`, `status` |
| Cổng bắt buộc Page ID | PASS | Lệnh Facebook thiếu `--page-id` dừng trước khi gọi API |
| Composio đăng nhập | PASS | `composio whoami` thành công |
| Tìm action Facebook thật | PASS | Tìm được `FACEBOOK_UPLOAD_PHOTOS_BATCH` và action kiểm tra liên quan |
| Facebook toolkit | PASS | Toolkit Facebook đang kết nối |
| Blotato account listing | CHƯA SẴN SÀNG | Chưa có `BLOTATO_API_KEY` dùng được trong repo |
| Đăng bài thật | KHÔNG CHẠY | Không phát hành ra kênh thật khi chưa có Content Package và approval của người dùng |

## Kết luận

Nhánh Composio sẵn sàng cho bài thực hành. Nhánh Blotato mới đạt mức kiểm tra CLI; muốn chạy thật phải cấu hình `BLOTATO_API_KEY`. Skill đã chặn đúng trường hợp Facebook thiếu Page ID. Đây là kiểm tra an toàn, không tạo bài đăng bên ngoài.
