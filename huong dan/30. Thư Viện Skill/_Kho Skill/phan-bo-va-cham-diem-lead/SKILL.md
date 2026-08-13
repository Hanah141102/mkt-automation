---
name: phan-bo-va-cham-diem-lead
description: "Thiết kế quy trình tiếp nhận và phân bổ lead: chấm điểm lead nóng lạnh, luật chia lead cho từng người, thời hạn phải liên hệ, quy tắc trả lead về và cách chống tranh khách. Dùng khi lead về nhiều mà rơi rớt, hoặc đội sale từ hai người trở lên."
allowed-tools: Read Write Glob
ten-viet: "Phân Bổ & Chấm Điểm Lead"
nhom: "07. Bán Hàng & Phễu"
ten-goc: "Phân Bổ & Chấm Điểm Lead"
---

# Phân Bổ & Chấm Điểm Lead

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

- Lead về nhiều nhưng không ai biết ai đang chăm khách nào
- Hai người cùng gọi một khách, hoặc không ai gọi
- Sale chỉ nhặt lead dễ, lead khó bỏ đó
- Không biết lead nào đáng đầu tư thời gian
- Đội sale từ **hai người trở lên** — một người thì chưa cần skill này

---

## Nguyên tắc cốt lõi

LEAD KHÔNG PHẢI AI CŨNG NHƯ NHAU, VÀ THỜI GIAN CỦA SALE LÀ NGUỒN LỰC KHAN HIẾM NHẤT. LUẬT PHÂN BỔ TỒN TẠI ĐỂ ĐẢM BẢO **MỌI LEAD ĐỀU ĐƯỢC CHẠM** VÀ **LEAD NÓNG ĐƯỢC CHẠM TRƯỚC**.

---

## Giai đoạn 1: Lấy ngữ cảnh

| Đầu vào | Câu hỏi | Mặc định |
|---|---|---|
| **Số lead mỗi tuần** | "Trung bình một tuần về bao nhiêu lead?" | Chưa đo |
| **Nguồn lead** | "Lead về từ đâu — quảng cáo, livestream, giới thiệu, sự kiện?" | Quảng cáo |
| **Số người bán** | "Mấy người đang trực tiếp bán?" | 2 |
| **Chu kỳ bán** | "Từ lúc khách hỏi tới lúc chốt thường mất bao lâu?" | 3–7 ngày |
| **Giá trị đơn** | "Giá trị trung bình một đơn?" | Đọc `00. Business Context/Sản Phẩm & Dịch Vụ/` |

---

## Giai đoạn 2: Chấm điểm lead

Chấm trên **hai trục**, không phải một. Trục hành vi cho biết khách *sốt sắng* tới đâu; trục phù hợp cho biết khách *đúng người* tới đâu.

### Trục A — Mức độ phù hợp (khách có đúng là người mình bán không)

| Tiêu chí | Điểm |
|---|---|
| Đúng phân khúc trong `MHKD/Phân Khúc Khách Hàng/` | +2 |
| Có khả năng chi trả ở mức giá của mình | +2 |
| Là người có quyền quyết định | +1 |
| Trùng với chân dung ngược (khách không phù hợp) | −3 |

### Trục B — Mức độ sốt sắng (khách đang cần tới đâu)

| Hành vi | Điểm |
|---|---|
| Chủ động hỏi giá | +2 |
| Nêu mốc thời gian cụ thể ("cuối tháng em cần") | +2 |
| Đã xem/tham dự nội dung sâu (webinar, tư vấn, dùng thử) | +2 |
| Được người quen giới thiệu | +1 |
| Chỉ để lại thông tin, chưa tương tác gì thêm | 0 |
| Quá 25% chu kỳ bán không phản hồi | −2 |

### Bảng phân loại

| Tổng điểm | Loại | Cách xử lý |
|---|---|---|
| **≥ 7** | 🔥 Nóng | Liên hệ trong **ngưỡng chạm nóng** (xem công thức trên). Giao cho người bán tốt nhất. |
| **4–6** | 🌤 Ấm | Liên hệ trong **8 × ngưỡng chạm nóng**. Chia đều theo lượt. |
| **1–3** | ❄️ Lạnh | Đưa vào chuỗi nuôi dưỡng tự động, không gọi 1-1. |
| **≤ 0** | ⛔ Loại | Ghi lý do rồi đóng. Không tốn thời gian nữa. |

> Điểm số chỉ để **xếp thứ tự làm việc**, không phải để bỏ khách. Lead lạnh vẫn được chăm — chỉ bằng chuỗi tự động thay vì bằng người.

---

## Giai đoạn 3: Luật phân bổ

Chọn **một** luật và ghi vào `Decisions/`. Đổi luật giữa chừng là nguồn gốc của mọi tranh cãi.

| Luật | Cách chạy | Hợp khi |
|---|---|---|
| **Chia vòng tròn** | Lead về lần lượt cho từng người theo thứ tự | Đội đồng đều, lead nhiều |
| **Chia theo nguồn** | Mỗi người ôm trọn một nguồn (quảng cáo / giới thiệu / sự kiện) | Mỗi nguồn cần cách bán khác nhau |
| **Chia theo sản phẩm** | Mỗi người chuyên một dòng sản phẩm | Sản phẩm phức tạp, cần chuyên môn |
| **Ai nhanh tay** | Lead vào nhóm chung, ai nhận trước người đó chăm | Đội ≤3 người, tin nhau |

**Luật bổ sung bắt buộc, áp cho mọi phương án:**

1. **Thời hạn nhận việc.** Lead nóng chưa được ai nhận trong ngưỡng chạm nóng → tự động chuyển sang người thứ hai.
2. **Thời hạn chăm.** Sale giữ lead tối đa **1,5 × chu kỳ bán**. Quá hạn không chuyển trạng thái → lead trả về nhóm chung.
   *Ví dụ: chu kỳ 21 ngày → giữ 32 ngày. Chu kỳ 75 ngày → giữ 113 ngày.*
3. **Chống tranh khách.** Khách đã có trong `People/` thì thuộc về người đang chăm, kể cả khi khách nhắn lại qua kênh khác.
4. **Ghi ngay.** Nhận lead xong phải tạo file trong `People/` trong ngày. Không ghi = không tính là đã nhận.

---

## Giai đoạn 4: Trạng thái pipeline

Dùng đúng bộ trạng thái này, không tự đặt thêm:

```
1. Mới          → vừa về, chưa ai liên hệ
2. Đã liên hệ   → đã chạm lần đầu, chưa khai thác được nhu cầu
3. Đang tư vấn  → đã biết nhu cầu, đang trao đổi
4. Đã báo giá   → khách đã biết giá, đang cân nhắc
5. Chờ quyết    → khách nói sẽ quyết, đang đợi
6. Thắng        → đã thanh toán
7. Thua         → không mua, ghi rõ lý do
8. Nuôi dài hạn → chưa phải lúc, đưa vào chuỗi nội dung
```

**Bắt buộc ghi lý do khi vào trạng thái 7 (Thua).** Lý do thua là dữ liệu quý nhất trong toàn bộ hệ thống — nó nói cho bạn biết offer sai chỗ nào, giá sai chỗ nào, hoặc mình đang thu hút sai khách. Chạy `/win-loss-analysis` hằng quý trên dữ liệu này.

---

## Giai đoạn 5: Ghi vào vault

| Ghi gì | Ghi vào đâu |
|---|---|
| Luật phân bổ đã chốt | `Decisions/YYYY-MM-DD — Luật phân bổ lead.md` |
| Bảng chấm điểm | `04. Resources/Playbooks/Chấm Điểm Lead.md` |
| Từng lead | `People/[Tên] — [Nguồn] (PK<số>).md` |
| Pipeline theo tháng | `03. Areas/Sales Pipeline & CRM/Pipeline Tháng [MM-YYYY].md` |
| Số liệu chuyển đổi từng giai đoạn | `03. Areas/Analytics & Reporting/` |

---

## Đầu ra

- Bảng chấm điểm lead hai trục, điền được ngay
- Luật phân bổ đã chọn, kèm 4 luật bổ sung
- Bộ 8 trạng thái pipeline
- Mẫu pipeline tháng để copy dùng

---

## Ràng buộc

- **Không đổi luật phân bổ giữa tháng.** Chốt đầu tháng, chạy hết tháng, rà lại cuối tháng.
- **Không để lead nóng chờ quá ngưỡng chạm nóng.** Đây là chỗ mất tiền nhiều nhất trong toàn bộ phễu.
- **Không xoá lead thua.** Chuyển sang trạng thái Thua kèm lý do, giữ nguyên trong vault.
- Điểm số là công cụ xếp thứ tự, không phải phán quyết. Sale vẫn được quyền đề xuất nâng hạng một lead nếu có lý do.
