# Visual routing

## Chọn mode

### BROLL_PRIMARY

Dùng khi câu nói mô tả người, hành động hoặc bối cảnh có thể quay thật: cuộc họp, người ghi chú, điện thoại ghi âm, nhóm phối hợp, quản lý kiểm tra hoặc khách hàng phỏng vấn.

B-roll chiếm toàn khung hình. Chỉ thêm nhãn ngắn, con số hoặc callout nhỏ nếu giúp người xem định hướng.

### HYPERFRAME_FULL

Dùng khi nội dung cần nhìn thấy cấu trúc hơn là footage: quy trình nhiều bước, prompt dài, bảng nhiệm vụ, deadline, sơ đồ luồng dữ liệu, dashboard, kho kiến thức hoặc khái niệm trừu tượng.

Cho từng thành phần đi vào theo voice. Nếu voice nói “quyết định”, rồi “nhiệm vụ”, rồi “người phụ trách”, ba card phải xuất hiện lần lượt thay vì hiện đồng thời từ đầu.

### BROLL_PLUS_OVERLAY

Dùng khi hành động thật là trọng tâm nhưng cần minh họa một lớp thông tin ngắn: người họp cùng ba câu hỏi nổi lần lượt; điện thoại ghi âm cùng badge M4A/MP3; hoặc người kiểm tra transcript cùng highlight tên và deadline.

Giữ ít nhất khoảng 65% hình B-roll vẫn đọc được. Nếu overlay cần che phần lớn màn hình, đổi sang `HYPERFRAME_FULL`.

## Mật độ cảnh

Đổi clip khi thay đổi chủ thể, hành động, công cụ, kết quả hoặc sắc thái. Một clip thường giữ 2,5–6 giây. Có thể dài hơn nếu hành động có diễn tiến rõ, hoặc ngắn hơn trong montage. Không cắt chỉ để tăng số lượng nếu hai câu liên tiếp cùng một hành động.

## Truy vấn Pexels

Viết query bằng tiếng Anh theo công thức chủ thể + hành động + bối cảnh + framing, ví dụ:

- `asian business team video conference office wide shot`
- `manager checking project tasks laptop close up`
- `smartphone voice recorder meeting table landscape`
- `sales team customer interview office b roll`

Không dùng một query như `AI meeting` cho cả video. Đánh giá clip bằng frame đầu/giữa/cuối, không chỉ thumbnail.

## Cue theo lời thoại

Ưu tiên word timestamp. Với một cụm từ:

1. Lấy timestamp của từ đầu cụm.
2. Bắt đầu animation sớm hơn tối đa 2–4 frame để cảm giác đồng bộ.
3. Cho animation hoàn thành trong 8–16 frame.
4. Giữ nội dung đủ lâu để đọc, rồi chuyển hoặc thu gọn khi ý tiếp theo bắt đầu.

Nếu timestamp suy ra từ ASR, dùng khoảng an toàn ±0,20 giây và spot-check bằng tai.

## Logo sản phẩm

- Chỉ hiển thị logo khi tên sản phẩm vừa được nhắc hoặc đang được hướng dẫn.
- Dùng nguồn chính thức, nền trong suốt nếu có; không đổi màu hoặc bóp méo.
- Với Zoom, Loom và Fathom, từng logo đi vào đúng thứ tự voice.
- Không dùng logo để ngụ ý tài trợ hoặc hợp tác.

## Chuyển cảnh

- `push-left/right`: sang bước tiếp theo hoặc quay lại bước trước.
- `wipe`: thay đổi công cụ hoặc luồng dữ liệu.
- `zoom`: đi từ tổng quan vào chi tiết.
- `blur-dissolve`: chuyển bối cảnh hoặc thời gian nhẹ.
- `flash`: chỉ dùng cho kết quả hoặc bước ngoặt, thời lượng ngắn.

Giới hạn 2–3 họ chuyển cảnh cho một video. Motion phải phục vụ nhịp giải thích, không làm chữ khó đọc.
