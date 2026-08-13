---
updated: 2026-07-29
audience: cả đội — không cần biết kỹ thuật
---
> [!warning] ĐÂY LÀ BÀI MẪU — DỮ LIỆU HƯ CẤU
> Toàn bộ tên công ty, tên người, tên miền, số tiền và số liệu trong tài liệu này **đã được thay bằng dữ liệu ví dụ**. Không dùng các con số ở đây làm căn cứ kinh doanh. Giá trị của bộ tài liệu này nằm ở **cấu trúc và cách lập luận**, không nằm ở số liệu.


# Hướng dẫn nhanh: dùng repo này thế nào

> Đọc file này trước khi đụng vào bất cứ file nào khác. 5 phút.

## 1. Mỗi lần bắt đầu làm việc — luôn Fetch trước

Mở **GitHub Desktop** → chọn repo `he-thong-tang-truong-demo` → bấm **Fetch origin** (góc trên bên phải) → nếu có nút **Pull**, bấm luôn.

**Vì sao:** để lấy bản mới nhất người khác vừa đưa lên, tránh sửa trên bản cũ rồi bị đè mất.

## 2. Tìm đúng file — đi theo câu hỏi, không đi theo trí nhớ

| Muốn biết... | Vào folder |
|---|---|
| Hôm nay đọc gì trước, quyết định nào đang chờ chốt | `00-Governance` |
| Học Viện AI Demo là ai, định vị, mục tiêu | `01-Strategy-Brand` |
| Thị trường, khách hàng, đối thủ nói gì | `02-Research-Insights` |
| Bán gì, cho ai, phễu ra sao | `03-Offer-Funnel` |
| Content, kênh, quảng cáo | `04-Growth-Content` |
| Ai làm gì, RACI, nhịp họp | `05-People-Operations` |
| Nội dung đào tạo, ranh giới từng khóa | `06-Training-Delivery` |
| KPI, đo lường, báo cáo | `07-Measurement` |
| Chiến dịch đang chạy (The Tuần Lễ Khởi Nghiệp AI) | `08-Campaigns` |

**Một luật duy nhất cần nhớ: không lấy file trong `99-Archive` để giao việc.** Đó là bản cũ đã bị thay thế, chỉ giữ lại để tra lịch sử.

## 3. Sửa file — ba bước

1. **Mở file trong GitHub Desktop hoặc VS Code**, sửa bình thường như sửa Word.
2. Lưu file lại (Ctrl/Cmd + S).
3. Quay lại GitHub Desktop — sẽ thấy file mình sửa hiện ra ở cột bên trái ("Changes").

## 4. Lưu thay đổi lên chung — Commit rồi Push

Trong GitHub Desktop:

1. Ở góc dưới bên trái, gõ **Summary** — một câu ngắn mô tả mình vừa sửa gì. Ví dụ: *"Cập nhật kịch bản Q&A buổi 3"*. **Không để trống, không gõ đại khái ("sửa", "cập nhật") — người khác đọc lại phải hiểu ngay.**
2. Bấm **Commit to main**.
3. Bấm **Push origin** ở góc trên bên phải.

Xong — người khác Fetch là thấy ngay bản mới.

## 5. Bốn điều KHÔNG làm

| Không làm | Vì sao |
|---|---|
| Không xoá file người khác đang dùng nếu chưa hỏi | Có thể đang có người khác cần |
| Không sửa trực tiếp file trong `00-Governance` hoặc `01-Strategy-Brand` nếu không phải An | Đây là tài liệu nguồn — sửa sai một chỗ, nhiều tài liệu khác trích dẫn theo sẽ sai theo |
| Không lấy file trong `99-Archive` ra làm theo | Đã cũ, đã bị thay bằng bản mới hơn |
| Không Commit mà không viết Summary rõ ràng | Không ai truy lại được ai sửa gì, khi nào |

## 6. Có việc mới muốn thêm, nhưng không chắc nên thêm vào đâu?

Đừng tự tạo file lung tung. Nhắn An một câu, hoặc mang vào **họp thứ Hai hằng tuần** — đó là lúc chốt file mới tạo ở đâu, ai giữ.

## 7. Bị vướng, không biết sửa thế nào?

Hỏi An. Đừng đoán rồi push đại — vì mọi người đang dùng chung một bản.
