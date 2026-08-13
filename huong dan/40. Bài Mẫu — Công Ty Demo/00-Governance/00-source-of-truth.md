---
updated: 2026-07-29
status: canonical
owner: An
---
> [!warning] ĐÂY LÀ BÀI MẪU — DỮ LIỆU HƯ CẤU
> Toàn bộ tên công ty, tên người, tên miền, số tiền và số liệu trong tài liệu này **đã được thay bằng dữ liệu ví dụ**. Không dùng các con số ở đây làm căn cứ kinh doanh. Giá trị của bộ tài liệu này nằm ở **cấu trúc và cách lập luận**, không nằm ở số liệu.


# Source of Truth & Quy tắc quản trị tài liệu

## 1. Thứ tự ưu tiên khi hai tài liệu mâu thuẫn

| Ưu tiên | Loại tài liệu | Cách dùng |
|:--:|---|---|
| 1 | Quyết định BOD đã ghi ngày + tài liệu `status: canonical` | Dùng để quyết định và giao việc |
| 2 | Tài liệu campaign đang hoạt động | Dùng trong phạm vi campaign đó |
| 3 | Tài liệu chức năng: Strategy, Offer, Growth, Operations, Measurement | Dùng như chính sách dài hạn |
| 4 | Master research | Dùng để chọn pattern và giả thuyết test |
| 5 | `Source-Research` | Dùng để tra bằng chứng/link, không phải quyết định |
| 6 | `99-Archive` | Chỉ tra lịch sử |

Nếu vẫn mâu thuẫn: dừng giao việc, ghi câu hỏi vào Decision Log và để An chốt.

## 2. Quyết định vai trò hiện hành

| Người | Vai trò nguồn chuẩn | Không được hiểu sai |
|---|---|---|
| **An** | Founder, chiến lược, offer, giảng chính, duyệt cuối quyết định lớn | Không phải người điều phối mọi task hằng ngày |
| **Anh Thư** | Content Planner và quản lý social | Hà không thay Anh Thư làm content owner |
| **Nguyệt** | Ads Performance | Không tự đổi offer, giá hoặc big message |
| **Duy** | Video Editor | Không tự đổi kịch bản/claim |
| **Hà** | Support; kỹ thuật lớp; truyền thông nội bộ nhóm trước–trong–sau Zoom; hỗ trợ vận hành kênh cho Anh Thư | Không phải Content Planner; không phải Ads Performance |
| **Bảo, Chi** | Hỗ trợ kỹ thuật khi học viên vào lớp chuyên sâu | Không mặc định là người vận hành toàn bộ workshop miễn phí |

Phân ca tạm thời trong một campaign không làm thay đổi JD gốc. Phải ghi rõ `temporary assignment`.

## 3. Nhãn trạng thái

| Nhãn | Nghĩa | Có dùng giao việc không? |
|---|---|:--:|
| `canonical` | Nguồn chuẩn đang hiệu lực | Có |
| `active-campaign` | Hiệu lực cho campaign ghi trong file | Có |
| `reference` | Tham khảo, framework, nghiên cứu | Không trực tiếp |
| `draft` | Chờ duyệt | Không |
| `superseded` | Đã bị thay thế | Không |
| `archive` | Lưu lịch sử | Không |

## 4. Quy tắc chống trùng

1. Một chủ đề chỉ có một file `canonical`.
2. File nghiên cứu giữ evidence; file master giữ conclusion/action.
3. Không copy cùng một bảng RACI vào nhiều file. Campaign index dẫn link về RACI chuẩn.
4. Không copy KPI vào checklist. Checklist chỉ dẫn tới KPI.
5. Không copy offer/giá vào content plan nếu có thể dẫn link; nếu bắt buộc phải lặp, ghi ngày chốt.
6. Khi một file bị thay thế: chuyển vào `99-Archive/Superseded`, không xóa.

## 5. Quy tắc tên file

- Dùng chữ thường, không dấu cho file mới.
- Tên nói đúng output: `tracking-spec`, `sales-playbook`, `run-of-show`.
- Không đặt `final`, `final-v2`, `new-final`.
- Phiên bản nằm trong front matter: `updated`, `status`, `owner`.
- Campaign nằm trong `08-Campaigns/<campaign-name>`.

## 6. Definition of Done cho tài liệu vận hành

Một tài liệu chưa được coi là xong nếu thiếu một trong các mục:

- Mục đích và phạm vi.
- Input và output.
- Một người owner.
- Quy trình/bảng quyết định.
- KPI hoặc điều kiện đạt.
- Exception/escalation.
- Ngày cập nhật.
- Link tới tài liệu phụ thuộc.

## 7. Decision Log

| Ngày | Quyết định | Owner | Tài liệu bị ảnh hưởng |
|---|---|---|---|
| 29/07/2026 | Dùng repository riêng, private, làm nguồn cộng tác | An | Toàn hệ |
| 29/07/2026 | Tách Strategy/Research/Offer/Growth/People/Training/Measurement/Campaign | An | Cấu trúc repository |
| 29/07/2026 | Anh Thư giữ Content Plan + Social; Hà là Support và hỗ trợ kênh | An | `05-organization-roles-raci` |
| 29/07/2026 | Nguyệt giữ Ads Performance; Duy giữ Edit | An | `05-organization-roles-raci` |
| 29/07/2026 | Bảo, Chi tập trung kỹ thuật lớp chuyên sâu | An | `05-organization-roles-raci` |
| 29/07/2026 | Gộp research trùng thành 2 master: Organic và Paid; raw source giữ riêng | An | `02-Research-Insights` |

## 8. Cách cập nhật

1. Pull bản mới nhất.
2. Sửa đúng file canonical.
3. Nếu quyết định đổi: cập nhật Decision Log và mọi campaign chịu ảnh hưởng.
4. Commit với Summary mô tả kết quả, không mô tả thao tác.
5. Push và thông báo link file cho người liên quan.

