# Kiểm thử hai skill vận hành bằng prompt — Use Case 1

## Kết luận

Hai skill dưới đây không có file chương trình để chạy bằng terminal. Chúng được kích hoạt bằng cách gọi đúng tên skill và cung cấp đầu vào theo biểu mẫu. Kiểm thử này xác nhận tài liệu, điều kiện đầu vào, quy trình và cấu trúc đầu ra hoạt động với dữ liệu giả định.

## 1. `$mkt-phan-tich-doi-thu`

### Kiểu skill

- Skill nghiên cứu và ra quyết định bằng prompt.
- Không có `scripts/`.
- Có `SKILL.md`, mẫu phân tích và tài liệu tham khảo.

### Đầu vào thử

- Công ty: Doanh nghiệp mẫu, không dùng dữ liệu thật.
- Phân khúc: Chủ SME muốn giảm thao tác Marketing thủ công.
- Ba ứng viên:
  - Kênh Mẫu A — đối thủ trực tiếp.
  - Kênh Mẫu B — đối thủ giành sự chú ý.
  - Kênh Mẫu C — kênh chuẩn tham khảo.
- Bằng chứng giả định: URL, phân khúc phục vụ và loại nội dung được gắn nhãn `GIẢ ĐỊNH KIỂM THỬ`.

### Kết quả thử

| Ứng viên | Phân loại đề xuất | Có thể chuyển tiếp? | Việc con người phải làm |
|---|---|---:|---|
| Kênh Mẫu A | Đối thủ trực tiếp | Có điều kiện | Xác minh đúng pháp nhân và URL |
| Kênh Mẫu B | Đối thủ giành sự chú ý | Có điều kiện | Kiểm tra có cùng nhóm khách hàng không |
| Kênh Mẫu C | Kênh chuẩn tham khảo | Có điều kiện | Chỉ rõ định dạng cần học |

### Điểm dừng hoạt động đúng

Skill không được tự khẳng định ba ứng viên là đối thủ thật khi chưa có nguồn công khai. Đầu ra chỉ là danh sách đề xuất; người phụ trách duyệt xong mới điền `competitors.json`.

**Trạng thái kiểm thử:** ĐẠT — quy trình prompt, điểm dừng và cấu trúc bàn giao đều rõ; không có chương trình terminal để chạy.

## 2. `$content-ideation`

### Kiểu skill

- Skill phát triển ý tưởng bằng prompt và checklist.
- Không có `scripts/`.
- Có framework, tiêu chuẩn đầu ra, checklist bảy lớp, mẫu đầu vào và mẫu bàn giao.

### Brief thử

- Trụ cột nội dung: Kiểm soát Marketing Agent.
- Insight: Chủ SME muốn giảm thao tác nhưng sợ AI tự làm sai.
- Nấc nhận thức: Biết vấn đề, chưa biết cách kiểm soát.
- Mục tiêu: Chọn một ý tưởng có thể đăng thử trong tuần.
- Kênh: Facebook.
- Bằng chứng: Ba bản ghi giả trong báo cáo mock Apify.
- Giới hạn: Không tuyên bố giảm chi phí hoặc tăng doanh thu nếu chưa có dữ liệu.

### Đầu ra thử

| Ý tưởng | Hook | Vai trò | Bằng chứng cần dùng | Điểm ưu tiên | Giả thuyết kiểm chứng |
|---|---|---|---|---:|---|
| Ba lần CEO cần kiểm tra trước khi giao việc cho Marketing Agent | “Tự động hóa không có nghĩa là bỏ người chịu trách nhiệm” | Giáo dục vấn đề | Hai nội dung mock cùng nhắc đến kiểm tra và kiểm soát | 8/10 | Bài checklist có thể tạo nhiều lượt lưu hơn bài giới thiệu công cụ |
| AI làm nhanh nhưng ai chịu trách nhiệm khi nội dung sai? | “Sai không nằm ở AI; sai nằm ở chỗ không có người duyệt” | Phản biện | Nội dung mock về kiểm soát nội dung | 7/10 | Góc phản biện có thể tạo nhiều bình luận có nội dung hơn |
| Mẫu phân việc giữa Agent và người phụ trách | “Việc nào giao máy, việc nào CEO vẫn phải ký?” | Hướng dẫn hành động | Báo cáo mock và nguyên tắc phân quyền | 9/10 | Mẫu phân việc có thể tăng lượt tải hoặc yêu cầu nhận tài liệu |

### Tự kiểm bảy lớp

- Dữ kiện và nguồn: dùng dữ liệu giả, đã ghi rõ.
- Giả định: mọi kết quả kỳ vọng đều được gọi là giả thuyết.
- Logic: mỗi ý tưởng có insight, hook, bằng chứng và cách đo.
- Bám yêu cầu: đúng nhóm SME, đúng Facebook, đúng mục tiêu thử trong tuần.
- Khả năng triển khai: có thể bàn giao cho người viết nội dung.
- Rủi ro: không dùng số liệu doanh thu hoặc cam kết không có nguồn.
- Thẩm quyền: người phụ trách vẫn phải chọn ý tưởng và duyệt trước khi đăng.

**Trạng thái kiểm thử:** ĐẠT — đầu vào mẫu đi qua đủ quy trình và tạo được cấu trúc đầu ra đúng checklist; không có chương trình terminal để chạy.
