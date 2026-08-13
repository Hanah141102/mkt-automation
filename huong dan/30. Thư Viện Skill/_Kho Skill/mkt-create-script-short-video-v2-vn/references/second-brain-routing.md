# Định Tuyến Second Brain Cho Content

## Phạm vi

Chỉ đọc `creator_context_root` hoặc `source_roots` mà người dùng đã cung cấp. Không mặc định một đường dẫn, tác giả hay vault cá nhân cụ thể.

## Thứ tự đọc

1. Hồ sơ tác giả hoặc tài liệu bản sắc.
2. Nhật ký gần đây để lấy cảnh thật, quyết định và từ ngữ tự nhiên.
3. Statements/frameworks đã chắt lọc.
4. Dự án, thử nghiệm và sản phẩm đang diễn ra.
5. Literature notes để lấy kiến thức và nguồn ngoài.
6. Raw/Inbox chỉ khi thiếu nguồn đã xử lý; coi là nguyên liệu chưa xác nhận.

Ưu tiên note mới khi nói về công cụ, dự án hoặc quyết định thay đổi. Ưu tiên nhật ký khi cần trải nghiệm; ưu tiên nguồn đã chắt lọc khi cần nguyên lý.

## Cách tìm

1. Rút 3–6 từ khóa từ brief: chủ thể, nỗi đau, kết quả và từ đồng nghĩa.
2. Dùng `rg --files <source_roots>` để tìm tên file.
3. Dùng `rg -l -i --glob '*.md' '<keywords>' <source_roots>` để tìm nội dung.
4. Đọc toàn bộ 3–8 note có tín hiệu cao nhất; không kết luận chỉ từ đoạn khớp.
5. Theo wikilink tối đa một bước khi cần xác minh proof hoặc quyết định mới hơn.

## Phân loại nguồn

| Loại | Có thể dùng | Không được làm |
|---|---|---|
| Trải nghiệm tác giả | Kể ngôi “tôi” khi được phép | Tổng quát thành chân lý phổ quát |
| Statement/Framework | Dùng làm nguyên lý | Coi là bằng chứng nếu không có dữ liệu |
| Literature Note | Ghi nguồn, diễn giải | Nhận là phát minh/trải nghiệm tác giả |
| Project/Pilot | Dùng demo và bài học | Gọi là case thành công khi thiếu baseline |
| Nhật ký | Lấy câu chữ và quyết định | Công khai chi tiết riêng tư |
| Raw/Inbox | Gợi câu hỏi hoặc giả thuyết | Dùng như dữ kiện đã xác nhận |

## Bảo mật

Không đọc secret, `.env`, credential, dữ liệu xác thực hoặc thư mục bị brand policy loại trừ. Không công khai dữ liệu gia đình, sức khỏe, tài chính, khách hàng hay thông tin nhận dạng khi chưa được phép.

Gắn trạng thái `Public`, `Anonymize`, `Need approval` hoặc `Private` cho từng nguồn. `Need approval` phải để placeholder và chuyển cho người có thẩm quyền duyệt.
