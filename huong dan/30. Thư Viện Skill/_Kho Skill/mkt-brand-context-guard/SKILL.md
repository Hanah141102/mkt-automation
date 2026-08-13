---
name: mkt-brand-context-guard
description: Nạp và kiểm tra bối cảnh của bất kỳ thương hiệu doanh nghiệp hoặc thương hiệu cá nhân nào trước khi viết, sửa, duyệt hay lập chiến lược content, quảng cáo, video, offer và CTA. Dùng khi cần bảo đảm đúng ICP, định vị, giọng, proof, quyền công bố và trạng thái dữ kiện mà không phụ thuộc một cá nhân hay workspace cố định.
---

# MKT Brand Context Guard

Giữ đầu ra nhất quán với nguồn sự thật của thương hiệu đang được chọn. Không dùng cấu hình, giọng, CTA hay dữ liệu của thương hiệu khác làm mặc định.

## Đầu vào

- `brand_name`: tên thương hiệu hoặc tác giả.
- `brand_context_root`: thư mục chứa business context; mặc định tìm `00. Business Context/` từ workspace hiện hành.
- `creator_context_root`: thư mục nhật ký/Second Brain tùy chọn khi cần trải nghiệm cá nhân.
- `platform`, `audience`, `journey_stage`, `goal` và bản nháp cần kiểm tra.

Nếu workspace có nhiều thương hiệu mà người dùng chưa chọn, dừng và hỏi đúng một câu để xác định thương hiệu. Không tự chọn theo tên file, tài khoản đăng nhập hay dữ liệu lịch sử.

## Nạp nguồn theo thứ tự

1. Hồ sơ mô hình kinh doanh hoặc chiến lược.
2. Chân dung doanh nghiệp, ICP và định vị.
3. Brand voice và quy tắc ngôn ngữ.
4. Trụ cột nội dung, offer, CTA và vai trò từng kênh.
5. Chính sách proof, quyền công bố và danh sách nguồn loại trừ.
6. Lịch nội dung và quyết định đã duyệt gần nhất.
7. `creator_context_root` chỉ khi nhiệm vụ cần câu chuyện hoặc quan điểm cá nhân.

Ưu tiên tài liệu có trạng thái đã duyệt và ngày cập nhật mới hơn. Nêu mâu thuẫn thay vì tự hòa giải. Nếu thiếu nguồn bắt buộc, ghi rõ phần thiếu và chỉ tiếp tục bằng giả định có nhãn.

## Kiểm tra

1. Xác định đúng thương hiệu, audience, stage, mục tiêu và platform.
2. Đối chiếu nội dung với định vị, offer và vai trò kênh.
3. Phân loại claim: dữ kiện, trải nghiệm, suy luận, giả định hoặc dự phóng.
4. Kiểm tra nguồn, proof, quyền công bố, riêng tư và danh sách loại trừ của thương hiệu.
5. Kiểm tra giọng, thuật ngữ, CTA và tính native.
6. Kết luận `PASS`, `PASS CÓ ĐIỀU KIỆN` hoặc `FAIL`.

Không biến proposal, forecast, mục tiêu hoặc demo thành kết quả thật. Không dùng chuyện riêng tư hay dữ liệu khách hàng khi chưa có quyền công bố. Người sở hữu thương hiệu hoặc người được ủy quyền là cổng duyệt cuối.

## Đầu ra

```markdown
## Kết luận
- Thương hiệu:
- Trạng thái: PASS | PASS CÓ ĐIỀU KIỆN | FAIL
- Lý do chính:

## Bảng kiểm
| Lớp | Kết quả | Bằng chứng/lỗi | Cách sửa |

## Claim cần đổi cấp
- Claim:
- Phân loại đúng:
- Cách viết an toàn:

## Quyết định cần người có thẩm quyền duyệt
- ...
```
