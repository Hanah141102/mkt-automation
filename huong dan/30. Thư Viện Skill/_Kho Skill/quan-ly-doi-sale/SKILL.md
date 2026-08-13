---
name: quan-ly-doi-sale
description: "Dựng cơ chế quản lý đội bán hàng: chỉ số theo dõi từng người, nhịp họp sale hằng ngày và hằng tuần, cách chấm chất lượng cuộc gọi và tin nhắn, quy trình kèm người mới. Dùng khi có từ hai người bán trở lên và doanh số đang phụ thuộc vào cảm hứng của từng cá nhân."
allowed-tools: Read Write Glob
ten-viet: "Quản Lý Đội Sale"
nhom: "07. Bán Hàng & Phễu"
ten-goc: "Quản Lý Đội Sale"
---

# Quản Lý Đội Sale

> [!important] Đọc `Hồ Sơ Mô Hình Kinh Doanh` trước
> Mọi ngưỡng thời gian trong skill này **không phải con số cứng** — chúng tính từ `chu-ky-ban-ngay` trong `00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md`.
>
> | Việc | Công thức |
> |---|---|
> | Giữ lead tối đa | 1,5 × chu kỳ bán |
> | Chạm lead nóng | 15 phút nếu chu kỳ < 30 ngày · 4 giờ nếu ≥ 30 ngày |
> | Nhắc lại sau báo giá | 5% · 15% · 30% của chu kỳ bán |
>
> Nếu file đó chưa được điền, **hỏi người dùng chu kỳ bán trung bình trước khi đưa bất kỳ ngưỡng nào**. Đừng mặc định 14 ngày — con số đó chỉ đúng với chu kỳ bán ngắn.


## Khi nào dùng skill này

- Có từ 2 người bán trở lên
- Doanh số tháng này tốt, tháng sau tệ, không biết vì sao
- Một người bán giỏi hơn hẳn, nhưng không nhân bản được cách làm
- Người mới vào mất 2–3 tháng mới bán được
- Chủ doanh nghiệp vẫn phải tự chốt các đơn quan trọng

---

## Nguyên tắc cốt lõi

QUẢN ĐỘI SALE KHÔNG PHẢI QUẢN DOANH SỐ — DOANH SỐ LÀ KẾT QUẢ, XUẤT HIỆN QUÁ MUỘN ĐỂ CAN THIỆP. QUẢN **HÀNH VI DẪN TỚI DOANH SỐ**: SỐ LẦN CHẠM, TỐC ĐỘ PHẢN HỒI, CHẤT LƯỢNG CUỘC TRAO ĐỔI.

---

## Giai đoạn 1: Chọn chỉ số

Chia hai loại. Chỉ số dẫn dắt can thiệp được hằng ngày; chỉ số kết quả chỉ đọc được cuối kỳ.

### Chỉ số dẫn dắt — theo dõi hằng ngày

| Chỉ số | Đo gì | Ngưỡng cảnh báo |
|---|---|---|
| Số lead mới nhận | Có việc để làm không | Bằng 0 hai ngày liền |
| Tốc độ chạm lần đầu | Lead nóng có được gọi trong 15 phút không | Quá 30 phút |
| Số lần chạm mỗi lead | Có theo đuổi đủ không | Dưới 3 lần trước khi bỏ |
| Số lead chuyển giai đoạn | Pipeline có chảy không | Đứng yên 3 ngày |
| Số lead quá hạn giữ | Có ôm lead chết không | Trên 20% pipeline |

### Nhịp đọc số — theo chu kỳ bán, không cố định

| Chu kỳ bán | Nhịp đọc chỉ số kết quả | Bắt buộc kèm |
|---|---|---|
| Dưới 30 ngày | Hằng tuần | — |
| 30–90 ngày | Hai tuần một lần | Phân tích theo nhóm khách vào cùng tháng |
| Trên 90 ngày | Hằng tháng | Phân tích theo nhóm + chỉ đọc chỉ số dẫn dắt hằng tuần |

> **Quy tắc quan trọng:** khi chu kỳ bán **dài hơn** nhịp họp, tuyệt đối không đọc doanh thu theo tuần — con số đó là nhiễu ngẫu nhiên, và quyết định dựa vào nó sẽ sai. Tuần chỉ đọc chỉ số dẫn dắt.

### Chỉ số kết quả

| Chỉ số | Công thức |
|---|---|
| Tỷ lệ chốt | Đơn thắng ÷ số lead đã tư vấn |
| Giá trị đơn trung bình | Doanh thu ÷ số đơn |
| Chu kỳ bán | Số ngày trung bình từ chạm đầu tới chốt |
| Tỷ lệ thua theo lý do | Nhóm theo lý do thua trong pipeline |

> **Đừng dựng quá 5 chỉ số dẫn dắt.** Nhiều hơn là không ai nhìn, và bảng số trở thành việc hành chính thay vì công cụ.

---

## Giai đoạn 2: Nhịp quản lý

### Họp đứng hằng ngày — 10 phút, đầu ca

Mỗi người trả lời đúng ba câu, không hơn:

```
1. Hôm qua tôi chốt được gì, mất gì?
2. Hôm nay tôi tập trung vào ba khách nào?
3. Tôi đang tắc ở đâu, cần ai gỡ?
```

Người quản lý **chỉ gỡ tắc**, không giảng bài. Vấn đề cần bàn sâu thì hẹn riêng sau buổi.

### Họp sale hằng tuần — 30 phút

| Phút | Nội dung |
|---|---|
| 0–8 | Đọc bảng chỉ số dẫn dắt của từng người |
| 8–18 | Soi 1 deal thắng và 1 deal thua trong tuần — rút ra điều gì |
| 18–25 | Cập nhật sổ tay xử lý từ chối nếu có câu mới |
| 25–30 | Chốt mục tiêu tuần sau cho từng người |

### Rà pipeline hằng tháng — 60 phút

- Lead quá hạn (1,5 × chu kỳ bán) → trả về nhóm chung hoặc chuyển sang nuôi dài hạn
- Chạy `/win-loss-analysis` trên toàn bộ deal thắng và thua trong tháng
- Cập nhật bảng chấm điểm lead nếu quy luật đã đổi
- Ghi quyết định thay đổi vào `Decisions/`

---

## Giai đoạn 3: Chấm chất lượng cuộc trao đổi

Doanh số bằng nhau không có nghĩa cách bán giống nhau. Chấm để biết **ai đang bán bằng kỹ năng, ai đang bán nhờ may**.

Mỗi tuần chọn ngẫu nhiên 2 cuộc trao đổi của mỗi người (ghi âm hoặc lịch sử chat), chấm theo 6 mục:

| # | Tiêu chí | Đạt khi |
|---|---|---|
| 1 | Mở đầu | Xưng danh rõ, nhắc đúng ngữ cảnh khách đến từ đâu |
| 2 | Khai thác | Hỏi ít nhất 3 câu trước khi nói về sản phẩm |
| 3 | Lắng nghe | Nhắc lại đúng vướng mắc bằng chính lời khách |
| 4 | Trình bày | Nối giải pháp vào đúng vướng mắc đã nghe, không đọc thuộc |
| 5 | Xử lý từ chối | Hỏi làm rõ trước khi phản biện |
| 6 | Chốt bước tiếp | Kết thúc bằng một hành động cụ thể có mốc thời gian |

Chấm đạt hoặc không đạt từng mục, không cho điểm số. **Mục nào cả đội cùng trượt là lỗi kịch bản, không phải lỗi người** — quay lại `/sales-script` sửa kịch bản.

---

## Giai đoạn 4: Kèm người mới

Lộ trình 30 ngày, có mốc rõ ràng:

| Tuần | Người mới làm gì | Nghiệm thu |
|---|---|---|
| 1 | Đọc `00. Business Context/` · học hồ sơ sản phẩm và giá · nghe 10 cuộc của người cũ | Trả lời được 10 câu hỏi thường gặp không cần tra |
| 2 | Trực chat cùng người kèm · tự nhắn, người kèm duyệt trước khi gửi | Nhắn được 20 hội thoại, không sai thông tin sản phẩm |
| 3 | Tự chăm lead ấm · người kèm chấm chất lượng 2 cuộc/ngày | Đạt 5/6 mục chấm chất lượng |
| 4 | Nhận lead nóng · làm việc độc lập | Chốt được đơn đầu tiên |

Điều kiện đủ để bắt đầu: **kịch bản bán hàng và sổ tay xử lý từ chối phải có sẵn**. Chưa có thì chạy `/sales-script` và `/objection-handler` trước.

---

## Giai đoạn 5: Trả thưởng

Chỉ thiết kế sau khi đã có chỉ số ổn định ít nhất 2 tháng. Trả thưởng trên số liệu chưa tin được là cách nhanh nhất phá vỡ lòng tin trong đội.

Nguyên tắc:
- **Phần cứng đủ sống** — người bán lo ăn từng bữa sẽ bán kiểu chộp giật
- **Phần mềm gắn với chỉ số kiểm soát được** — tỷ lệ chốt và giá trị đơn, không phải doanh thu công ty
- **Thưởng chất lượng, không chỉ số lượng** — đơn bị hoàn, khách bỏ trong 30 ngày thì trừ lại
- Chi tiết cơ cấu: chạy `/commission-structure`

---

## Ghi vào vault

| Ghi gì | Ghi vào đâu |
|---|---|
| Bảng chỉ số theo tuần | `03. Areas/Analytics & Reporting/Báo Cáo Tuần/` |
| Kết quả chấm chất lượng | `03. Areas/Sales Pipeline & CRM/Chấm Chất Lượng [Tháng].md` |
| Lộ trình kèm người mới | `04. Resources/Playbooks/Kèm Người Mới — Sale.md` |
| Quyết định về luật, thưởng, mục tiêu | `Decisions/` |

---

## Đầu ra

- Bảng 5 chỉ số dẫn dắt + 4 chỉ số kết quả
- Nghị trình họp ngày, họp tuần, rà pipeline tháng
- Bảng chấm chất lượng 6 mục
- Lộ trình kèm người mới 30 ngày

---

## Ràng buộc

- **Không quản bằng doanh số đơn thuần.** Doanh số xuất hiện quá muộn để can thiệp.
- **Không bỏ họp đứng hằng ngày.** Mười phút mỗi sáng rẻ hơn một tháng lệch hướng.
- **Không chấm chất lượng để phạt.** Chấm để sửa kịch bản và để biết kèm ai cái gì.
- **Không thiết kế thưởng khi số liệu chưa đáng tin.** Ít nhất 2 tháng dữ liệu sạch.
- Mọi thay đổi về luật, mục tiêu, thưởng phải ghi vào `Decisions/` và chủ doanh nghiệp xác nhận.
