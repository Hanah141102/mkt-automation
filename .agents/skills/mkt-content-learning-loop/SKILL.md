---
name: mkt-content-learning-loop
description: Phân tích hiệu suất content cho bất kỳ thương hiệu nào theo Content Legos, hành trình khách hàng và tác động kinh doanh để quyết định giữ, sửa, mở rộng hoặc dừng. Dùng cho review định kỳ Facebook, TikTok, YouTube hoặc kênh khác, đọc attribution và chọn thử nghiệm cho vòng nội dung tiếp theo.
---

# MKT Content Learning Loop

Biến dữ liệu thành quyết định cho vòng nội dung kế tiếp. Không lấy view hoặc follower làm kết luận kinh doanh khi thiếu dấu vết tới đúng audience và offer.

## Đầu vào

- Kết quả `$mkt-brand-context-guard`.
- `content_id`, platform, ngày đăng, pillar, topic, take, format, hook, proof và CTA.
- Reach/views, retention và chỉ số tương tác nền tảng cung cấp.
- Tín hiệu audience phù hợp: bình luận, inbox, profile action hoặc returning viewer.
- Lead, conversion, cơ hội và attribution khi có.
- Thời gian, chi phí sản xuất và mức can thiệp của đội/người duyệt.

Để trống metric không có; không thay missing bằng 0.

## Ba tầng đo

1. **Attention:** hook hold, watch time, completion, dwell, save, share và returning viewer.
2. **Trust/fit:** bình luận đúng bài toán, profile action, binge, proof và ngôn ngữ audience nhắc lại.
3. **Demand/business:** lead, hội thoại đủ chuẩn, booking, conversion và cơ hội có attribution.

Nhịp review phải lấy từ business context, chu kỳ bán và tốc độ xuất bản. Nếu chưa có, ghi nhịp đề xuất là giả định cần duyệt.

## Content Legos

So sánh trong nhóm tương đồng theo topic, take, hook/packaging, format, story, proof, visual và CTA. Mỗi thử nghiệm chỉ đổi một biến chính; đổi nhiều biến thì ghi `không xác định nguyên nhân`.

## Ma trận quyết định

| Trạng thái | Điều kiện | Hành động |
|---|---|---|
| Giữ | Đúng audience, chất lượng ổn, chưa đủ mẫu | Tiếp tục thu dữ liệu |
| Mở rộng | Thắng lặp lại ở attention và trust/demand | Tạo series hoặc biến thể |
| Sửa | Topic đúng nhưng một Lego yếu | Chỉ sửa Lego gây nghẽn |
| Dừng | Sai audience, claim rủi ro hoặc thua lặp lại | Ngừng và ghi bài học |

## Quy trình

1. Kiểm tra dữ liệu thiếu, trùng và định nghĩa metric.
2. Nhóm theo platform, pillar, stage và Lego.
3. Tìm thắng/thua lặp lại; tách outlier.
4. Xác định điểm nghẽn lớn nhất.
5. Viết tối đa ba giả thuyết và độ chắc chắn.
6. Chọn một thử nghiệm chính cho mỗi research pack vòng sau.
7. Đề xuất cập nhật tỷ trọng hoặc tracking; không tự đổi nguồn sự thật khi chưa duyệt.

## Đầu ra

```markdown
# Content Learning Review
## Kết luận điều hành
## Dữ liệu và giới hạn
## Keep / Scale / Repair / Stop
## Phát hiện theo Content Legos
## Thử nghiệm vòng sau
## Tracking hoặc business context cần xác nhận
## Quyết định cần người có thẩm quyền duyệt
```

Khi thiếu attribution, ưu tiên sửa tracking trước khi tăng sản lượng hoặc kết luận content không tạo doanh thu.
