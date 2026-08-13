---
name: nhac-mua-lai-theo-chu-ky
description: "Thiết kế hệ nhắc mua lại đúng thời điểm khách dùng hết sản phẩm hoặc sắp tới kỳ tái quyết định: tính chu kỳ tiêu dùng thật từ dữ liệu, chọn cửa sổ nhắc, viết nội dung cho từng mốc và đo tỷ lệ quay lại. Dùng cho hàng tiêu dùng lặp lại, gói dịch vụ theo kỳ, khoá học có tái ghi danh."
allowed-tools: Read Write Glob
ten-viet: "Nhắc Mua Lại Theo Chu Kỳ"
nhom: "08. Chăm Sóc & Giữ Khách"
ten-goc: "Nhắc Mua Lại Theo Chu Kỳ"
---

# Nhắc Mua Lại Theo Chu Kỳ

## Khi nào dùng skill này

Đọc `00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md`, trường `mo-hinh-mua-lai`. Dùng skill này khi giá trị là **`theo-ky`** — nghĩa là khách không rời từ từ, mà có **một điểm quyết định rời rạc**:

| Ngành | Điểm tái quyết định |
|---|---|
| Mỹ phẩm, thực phẩm chức năng | Lúc dùng hết lọ |
| Trung tâm đào tạo | Hai tuần cuối khoá |
| Dịch vụ định kỳ (spa, bảo trì) | Hết liệu trình, hết hợp đồng |
| Phần mềm trả năm | 30 ngày trước ngày gia hạn |

**KHÁC với `/churn-prevention-playbook`:** skill đó dành cho mô hình `lien-tuc` — khách có thể rời bất cứ lúc nào, nên phải theo dõi sức khoẻ liên tục. Skill này dành cho mô hình có **cửa sổ quyết định hẹp** — toàn bộ trận đánh nằm trong vài ngày.

---

## Nguyên tắc cốt lõi

ĐÚNG THỜI ĐIỂM QUAN TRỌNG HƠN ĐÚNG NỘI DUNG. NHẮN ĐÚNG NGÀY KHÁCH SẮP HẾT HÀNG CÓ THỂ CHO TỶ LỆ QUAY LẠI GẤP NĂM LẦN SO VỚI CÙNG MỘT TIN NHẮN GỬI SAI THỜI ĐIỂM — VÌ LÚC ĐÓ KHÁCH ĐANG THẬT SỰ CẦN, KHÔNG PHẢI ĐANG BỊ LÀM PHIỀN.

---

## Giai đoạn 1: Tìm chu kỳ tiêu dùng thật

Đây là bước quan trọng nhất và hay bị làm ẩu nhất. Đừng lấy con số nhà sản xuất ghi trên bao bì — lấy con số khách dùng thật.

### Ba cách đo, xếp theo độ tin cậy

**Cách 1 — Từ dữ liệu đơn hàng (tốt nhất)**

Lấy các khách đã mua từ 2 lần trở lên, tính khoảng cách giữa hai lần mua, rồi lấy **trung vị** (không phải trung bình — trung bình bị kéo lệch bởi vài khách mua lại rất muộn).

```
Ví dụ 12 khách mua lặp: 38, 42, 45, 47, 48, 50, 52, 55, 58, 71, 95, 120 ngày
Trung bình = 60 ngày  ← sai, bị 3 khách cuối kéo lên
Trung vị   = 51 ngày  ← đúng hơn
```

**Cách 2 — Từ dung tích và liều dùng**

```
Chu kỳ = Dung tích ÷ Lượng dùng mỗi lần ÷ Số lần dùng mỗi ngày
```
Rồi **nhân 1,2** — vì thực tế khách luôn dùng chậm hơn hướng dẫn (quên, đi công tác, dùng gián đoạn).

**Cách 3 — Hỏi thẳng khách**

Thêm một câu vào tin nhắn chăm sóc sau mua: *"Chị dùng khoảng bao lâu thì hết lọ này ạ?"* Gom 20–30 câu trả lời là có con số dùng được.

> Ghi con số tìm được vào `chu-ky-tieu-dung-ngay` trong Hồ Sơ Mô Hình Kinh Doanh.

### Chia nhóm nếu chu kỳ lệch nhiều

Nếu khoảng chu kỳ trải rộng (ví dụ 30–120 ngày), đừng dùng một con số chung. Chia làm 2–3 nhóm theo tần suất dùng và nhắc riêng.

---

## Giai đoạn 2: Cửa sổ nhắc

Không nhắc một lần. Nhắc theo ba mốc quanh thời điểm hết.

### Hai loại chu kỳ — dùng công thức khác nhau

> [!warning] Đây là chỗ hay tính sai nhất
> Công thức 0,8 / 0,95 / 1,15 × C **chỉ đúng cho chu kỳ tiêu dùng** — khách dùng dần tới lúc hết. Với **kỳ hạn cố định** (khoá học 3 tháng, hợp đồng năm, gói thuê bao), phải **tính ngược từ ngày hết hạn**, không nhân theo tỷ lệ.
>
> Ví dụ sai: gói gia hạn hằng năm (365 ngày), áp 0,8 × C ra ngày 292 — nhắc gia hạn từ tháng thứ 10 là quá sớm, khách khó chịu.

**Loại A — Chu kỳ tiêu dùng** (dùng dần tới hết): mỹ phẩm, thực phẩm chức năng, vật tư

| Mốc | Thời điểm | Mục đích |
|---|---|---|
| Sớm | 0,8 × C | Hỏi thăm kết quả, chưa bán |
| Đúng lúc | 0,95 × C | Mời đặt lại |
| Muộn | 1,15 × C | Cứu vãn |

**Loại B — Kỳ hạn cố định** (có ngày hết hạn rõ): khoá học, hợp đồng, thuê bao

Tính ngược từ ngày kết thúc, **không phụ thuộc độ dài kỳ hạn**:

| Mốc | Thời điểm | Mục đích |
|---|---|---|
| Sớm | 30 ngày trước khi hết hạn *(hoặc 1/4 kỳ hạn nếu kỳ hạn ngắn hơn 60 ngày)* | Cho khách thấy kết quả đã đạt được |
| Đúng lúc | 14 ngày trước | Mời tái ký, ưu đãi cho người quyết sớm |
| Muộn | 3 ngày trước và 7 ngày sau khi hết | Chốt cuối, nêu rõ mất gì nếu dừng |

**Ví dụ Loại A với C = 50 ngày:** nhắc ngày 40 (hỏi thăm) · ngày 48 (mời đặt lại) · ngày 58 (cứu vãn).

**Cách phân biệt:** hỏi *"khách có biết chính xác ngày hết hạn không?"* — biết thì là Loại B, không biết (phải tự cảm nhận sắp hết) thì là Loại A.

---

## Giai đoạn 3: Nội dung từng mốc

### Mốc sớm — không bán

Sai lầm phổ biến: bán ngay từ tin đầu. Khách chưa hết hàng, tin nhắn thành làm phiền.

```
Mẫu — hàng tiêu dùng:
Chị [Tên] ơi, chị dùng [sản phẩm] được hơn tháng rồi ạ.
Da chị thấy đỡ [vấn đề khách từng nói] chưa ạ?
Em hỏi để tư vấn bước tiếp cho đúng ạ.
```

Câu hỏi này còn cho ra **dữ liệu về kết quả sử dụng** — nguyên liệu cho chứng thực sau này. Ghi câu trả lời vào `04. Resources/Feedback & Chứng Thực/`.

### Mốc đúng lúc — bán

Ba yếu tố: **nhắc hết hàng · gỡ ma sát đặt lại · lý do đặt ngay**.

```
Mẫu:
Chị [Tên] ơi, tính theo lịch dùng thì chị sắp hết [sản phẩm] rồi ạ.
Em giữ sẵn một lọ cho chị nhé, chị chỉ cần nhắn "ok" là em gửi,
địa chỉ cũ luôn ạ.
Đặt hôm nay thì thứ 5 chị nhận được, không bị gián đoạn ạ.
```

**Gỡ ma sát là đòn bẩy lớn nhất** — khách không phải nhớ tên sản phẩm, không phải nhập lại địa chỉ, không phải suy nghĩ.

### Mốc muộn — cứu vãn

Chia hai hướng tuỳ tình huống. Nếu khách im lặng hoàn toàn thì hỏi lý do; nếu khách có tương tác nhưng chưa mua thì đưa ưu đãi nhẹ có hạn.

**Đừng giảm giá ở mốc đúng lúc.** Giảm giá lúc khách đang cần sẽ dạy khách chờ giảm giá mới mua.

---

## Giai đoạn 4: Đo

| Chỉ số | Công thức | Ngưỡng tham khảo |
|---|---|---|
| Tỷ lệ mua lại | Số khách mua lần 2 ÷ số khách đã qua mốc chu kỳ | Càng cao càng tốt, so với chính mình tháng trước |
| Độ chính xác chu kỳ | % khách mua lại trong cửa sổ ±20% chu kỳ dự đoán | Trên 60% là chu kỳ ước đúng |
| Hiệu quả từng mốc | Số đơn phát sinh sau mỗi mốc | Nếu mốc sớm ra nhiều đơn → chu kỳ đang ước dài quá |

**Đọc ngược:** nếu phần lớn đơn rơi vào mốc muộn, chu kỳ thật ngắn hơn con số đang dùng — chỉnh xuống. Nếu rơi vào mốc sớm, chu kỳ thật dài hơn — chỉnh lên.

---

## Ghi kết quả vào đâu

| | |
|---|---|
| **Thư mục** | `03. Areas/Customer Success & Retention/` |
| **Tên file** | `Hệ Nhắc Mua Lại — [Sản phẩm/Gói].md` |
| **Bắt buộc** | Ghi `chu-ky-tieu-dung-ngay` vào `00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md`; link tới hồ sơ sản phẩm |

Số liệu đo hằng tháng ghi vào `03. Areas/Analytics & Reporting/Chăm Sóc Khách Hàng/`.

---

## Ràng buộc

- **Không nhắc khi chưa biết chu kỳ thật.** Đoán sai thời điểm biến chăm sóc thành spam.
- **Không giảm giá ở mốc đúng lúc** — dạy hư khách.
- **Không nhắc quá 3 lần** cho một chu kỳ. Không mua thì chuyển sang nuôi dài hạn.
- Với hàng sức khoẻ, không dùng ngôn ngữ hù doạ ("không dùng tiếp sẽ bị lại") — vừa sai đạo đức vừa rủi ro pháp lý. Xem `/tuan-thu-nganh-vn`.
