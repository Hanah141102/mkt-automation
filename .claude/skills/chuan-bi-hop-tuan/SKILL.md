---
name: chuan-bi-hop-tuan
description: "Đọc số liệu kỳ vừa rồi trong vault rồi sinh ra nghị trình họp cụ thể: ba câu đáng bàn nhất, số liệu kèm theo, việc còn treo và đề xuất quyết định. Thay cho nghị trình cố định chung chung. Chạy trước mỗi buổi họp định kỳ."
allowed-tools: Read Write Glob Grep
ten-viet: "Chuẩn Bị Họp Tuần"
nhom: "15. Dữ Liệu & Đo Lường"
ten-goc: "Chuẩn Bị Họp Tuần"
---

# Chuẩn Bị Họp Tuần

## Khi nào dùng skill này

Chạy **trước mỗi buổi họp định kỳ**, khoảng 10 phút trước giờ họp.

**Vấn đề skill này giải quyết:** nghị trình cố định làm buổi họp thành nghi thức — đọc số, gật đầu, tan họp, không quyết gì. Nghị trình sinh từ số liệu thật buộc buổi họp phải bàn đúng chỗ đang có vấn đề.

> **Nhịp họp không cố định.** Đọc `chu-ky-ban-ngay` trong `00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md`: dưới 30 ngày họp tuần · 30–90 ngày họp hai tuần · trên 90 ngày họp tháng. Với chu kỳ dài, **tuần chỉ đọc chỉ số dẫn dắt**, không đọc doanh thu.

---

## Nguyên tắc cốt lõi

BUỔI HỌP TỐT KHÔNG PHẢI BUỔI HỌP ĐỌC HẾT SỐ — MÀ LÀ BUỔI HỌP RA ĐƯỢC QUYẾT ĐỊNH. NGHỊ TRÌNH PHẢI CHỈ THẲNG VÀO **BA THỨ ĐÁNG BÀN NHẤT**, KHÔNG PHẢI LIỆT KÊ MỌI THỨ.

---

## Quy trình

### Bước 1 — Gom số

Đọc từ vault, không hỏi người dùng:

| Nguồn | Lấy gì |
|---|---|
| `03. Areas/Analytics & Reporting/` | Số liệu kỳ này và kỳ trước |
| `Sales Pipeline & CRM/Pipeline Tháng *.md` | Trạng thái deal, giá trị treo, deal quá hạn |
| `Content Đã Đăng/` | Số bài đăng kỳ này, trụ cột nào chạy tốt |
| `Meetings/` | Số cuộc gặp khách |
| `01. Inbox/` | Việc còn treo, yêu cầu chưa xử lý |
| `Decisions/` | Quyết định kỳ trước — đã thực hiện chưa |

Thiếu dữ liệu ở đâu thì **nêu rõ là thiếu**, đừng bỏ qua im lặng. Thiếu dữ liệu cũng là một vấn đề đáng bàn.

### Bước 2 — Chọn ba câu đáng bàn

Không liệt kê hết. Chấm mọi phát hiện theo ba tiêu chí rồi lấy ba cái điểm cao nhất:

| Tiêu chí | Điểm |
|---|---|
| **Có tiền gắn vào không** — quy ra được số tiền đang mất hoặc đang treo | 0–3 |
| **Có làm được gì tuần này không** — hay chỉ để biết | 0–3 |
| **Có bất thường không** — lệch trên 30% so với kỳ trước hoặc so với chuẩn | 0–2 |

Ví dụ: *"15 khách đã báo giá quá hạn theo đuôi, giá trị treo 340 triệu"* — có tiền (3), làm được ngay (3), bất thường (2) = **8 điểm, đưa lên đầu**.

Còn *"lượt tiếp cận Facebook giảm 8%"* — không quy ra tiền (0), khó can thiệp trong tuần (1), không bất thường (0) = **1 điểm, bỏ qua**.

### Bước 3 — Xuất nghị trình

```
HỌP TUẦN 34 · 45 phút · [ngày]
Nhịp: hằng tuần (chu kỳ bán 21 ngày)

━━━ BA CÂU ĐÁNG BÀN ━━━

1. [8đ] 15 khách đã báo giá quá hạn theo đuôi — treo 340 triệu
   Số: báo giá 19 · theo đuôi 4 · quá hạn 15 (hạn: 6 ngày = 30% chu kỳ)
   Ai: Linh
   Cần quyết: chia lại lead hay bổ sung người theo đuôi?

2. [7đ] Tốc độ phản hồi inbox tụt 62% → 41%
   Số: thứ 3 và thứ 5 tệ nhất (28% và 31%)
   Ai: Linh, Hà
   Cần quyết: ai trực hai ngày đó?

3. [6đ] Trụ cột "Bóc giá" tương tác gấp 2,3 lần nhưng chỉ chiếm 15% lịch
   Số: 6 bài · trung bình 340 tương tác · các trụ cột khác 148
   Ai: Hà
   Cần quyết: tăng tỷ trọng lên 30% không?

━━━ SỐ LIỆU KỲ NÀY ━━━
[bảng gọn, chỉ chỉ số chính, so với kỳ trước]

━━━ VIỆC TỪ KỲ TRƯỚC ━━━
✓ Đặt tin nhắn tự động ngoài giờ — xong
✗ Viết 2 bài trụ cột Bóc giá — chưa, Hà bận chiến dịch
⏳ SOP khảo sát tại nhà — đang làm, còn 1 mục

━━━ CHƯA CÓ DỮ LIỆU ━━━
⚠️ Chưa ghi số phễu chat tuần này → không biết inbox có tăng không

━━━ KHÔNG BÀN TUẦN NÀY ━━━
Lượt tiếp cận Facebook giảm 8% — trong biên dao động bình thường
```

### Bước 4 — Sau họp

Nhắc người chủ trì ghi lại:
- Quyết định → `Decisions/`
- Việc tuần sau + người + hạn → phần "Việc từ kỳ trước" của buổi sau

---

## Chỉ số dẫn dắt theo loại hình

Đọc `loai-san-pham` để biết đọc chỉ số nào. Không dùng chung một bộ cho mọi ngành.

| Loại | Ba chỉ số dẫn dắt quan trọng nhất |
|---|---|
| **Sản phẩm số**, chu kỳ dài | Số buổi tư vấn đặt được · số người xem hết webinar · số câu hỏi về giá |
| **Dịch vụ** | Số buổi trải nghiệm/học thử · tỷ lệ hoàn thành dịch vụ · điểm hài lòng giữa kỳ |
| **Hàng vật lý**, bán sàn | Tốc độ phản hồi inbox · số ngày tồn kho còn lại · tỷ lệ đánh giá 5 sao |

**Chỉ số dẫn dắt đọc hằng tuần kể cả khi chỉ số kết quả đọc theo tháng** — đó là cách theo dõi doanh nghiệp chu kỳ dài mà không bị nhiễu.

---

## Ghi kết quả vào đâu

| | |
|---|---|
| **Thư mục** | `03. Areas/Analytics & Reporting/Báo Cáo Tuần/` |
| **Tên file** | `Nghị Trình Tuần [NN-YYYY].md` |
| **Bắt buộc** | Sau họp, cập nhật kết quả vào chính file này; quyết định chép sang `Decisions/` |

---

## Ràng buộc

- **Tối đa ba câu đáng bàn.** Nhiều hơn là buổi họp không quyết được gì.
- **Mỗi câu phải có một quyết định cần chốt**, không chỉ thông tin để biết.
- **Không giấu chỗ thiếu dữ liệu.** Thiếu số là một vấn đề, phải nêu.
- **Không đọc doanh thu theo tuần khi chu kỳ bán dài hơn một tuần** — con số đó là nhiễu ngẫu nhiên.
- Nêu rõ mục "không bàn tuần này" để mọi người biết đã cân nhắc rồi bỏ qua, không phải quên.
