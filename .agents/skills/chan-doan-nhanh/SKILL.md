---
name: chan-doan-nhanh
description: "Chẩn đoán sức khoẻ 12 bước bằng 12 câu hỏi, chấm điểm từng bước rồi chỉ ra 2–3 bước yếu nhất nên làm trước. Dành cho doanh nghiệp đã chạy nhiều năm, không cần đi lại toàn bộ khung từ đầu. Dùng ở buổi đầu tiên thay cho việc bắt đầu tuần tự từ Bước 01."
allowed-tools: Read Write Glob Grep
ten-viet: "Chẩn Đoán Nhanh"
nhom: "01. Chiến Lược & Điều Hành"
ten-goc: "Chẩn Đoán Nhanh"
---

# Chẩn Đoán Nhanh

## Khi nào dùng skill này

- Doanh nghiệp **đã chạy từ 2 năm trở lên**, có doanh thu, có đội ngũ
- Không muốn bỏ 3 tuần đi lại từ Bước 01 những thứ đã ổn
- Đang có một vấn đề cụ thể nhưng chưa rõ gốc nằm ở bước nào
- Chuẩn bị rà quý ở Bước 12

**KHÔNG dùng cho doanh nghiệp mới** — dưới 1 năm thì chưa có gì để chẩn đoán, cứ đi tuần tự từ Bước 01.

---

## Nguyên tắc cốt lõi

DOANH NGHIỆP ĐÃ CHẠY 5 NĂM KHÔNG CẦN LÀM LẠI 12 BƯỚC — HỌ CẦN BIẾT **HAI BƯỚC NÀO ĐANG HỎNG**. BẮT HỌ ĐI TUẦN TỰ LÀ CÁCH NHANH NHẤT ĐỂ HỌ BỎ CUỘC Ở TUẦN THỨ HAI.

---

## Quy trình

### Bước 1 — Quét vault trước khi hỏi

Nếu vault đã có dữ liệu, chạy `/kiem-tra-cong tất cả` trước. Bước nào đã có bằng chứng thì **không hỏi lại**, chỉ hỏi các bước còn trống.

### Bước 2 — Mười hai câu hỏi

Hỏi từng câu một. Mỗi câu tương ứng một bước. Người dùng trả lời tự do; skill tự chấm.

| Bước | Câu hỏi | Chấm 0 điểm nếu | Chấm 2 điểm nếu |
|:--:|---|---|---|
| 01 | "Quyết định về giá và ngân sách, ai là người chốt cuối?" | "Tuỳ lúc" · nhiều người cùng chốt | Một người rõ ràng, có ghi lại |
| 02 | "Anh chị nói trong một câu: bán gì, cho ai, khác đối thủ chỗ nào?" | Ấp úng hoặc dài dòng | Trả lời gọn, cụ thể, có điểm khác biệt thật |
| 03 | "Ba đối thủ gần nhất mạnh yếu ở đâu? Khách chọn mình vì gì?" | "Chắc là giá" · không kể được | Kể được cụ thể, có dẫn chứng từ khách |
| 04 | "Bán bao nhiêu đơn một tháng thì hoà vốn?" | Không biết | Biết con số, biết biên từng dòng sản phẩm |
| 05 | "Từ lúc người lạ biết đến mình tới lúc mua, họ đi qua những bước nào?" | Không mô tả được | Mô tả được từng bước, biết chỗ rơi nhiều nhất |
| 06 | "Nội dung tháng này đăng theo kế hoạch hay tới đâu nghĩ tới đó?" | Tới đâu nghĩ tới đó | Có trụ cột, có lịch, có người phụ trách |
| 07 | "Đang chi bao nhiêu quảng cáo? Một khách mới tốn bao nhiêu?" | Không biết chi phí mỗi khách | Biết, và biết ngưỡng dừng |
| 08 | "Người mới vào bán hàng, mất bao lâu để chốt được đơn đầu?" | Trên 2 tháng, hoặc phải chủ tự chốt | Dưới 1 tháng, có kịch bản để đọc |
| 09 | "Nếu người giỏi nhất nghỉ một tuần, chất lượng có tụt không?" | Tụt rõ | Không tụt, có quy trình |
| 10 | "Bao nhiêu phần trăm khách quay lại? Anh chị có biết vì sao khách rời không?" | Không đo | Biết số, biết lý do |
| 11 | "Tháng trước doanh thu tăng hay giảm, và **vì sao**?" | Biết tăng giảm nhưng không biết vì sao | Giải thích được bằng số |
| 12 | "Ba tháng qua có quy trình nào mới được viết ra không?" | Không có | Có, và đang được dùng |

Chấm **1 điểm** cho các câu trả lời ở giữa.

### Bước 3 — Bảng điểm và chẩn đoán

```
CHẨN ĐOÁN — [Tên doanh nghiệp]                    Tổng: 14/24

Bước 01 Nền móng      ●●  2  ✓
Bước 02 Định vị       ●●  2  ✓
Bước 03 Nghiên cứu    ●   1  ⚠
Bước 04 Offer & Giá   ○   0  ✗  ← YẾU NHẤT
Bước 05 Phễu          ●   1  ⚠
Bước 06 Nội dung      ●●  2  ✓
Bước 07 Quảng cáo     ○   0  ✗  ← YẾU NHÌ
...
```

### Bước 4 — Chọn thứ tự làm, không phải làm hết

Đây là phần quan trọng nhất. **Không đề xuất làm tất cả các bước 0 điểm.** Áp ba luật:

**Luật 1 — Bước nền hỏng thì sửa nền trước.** Nếu 02 hoặc 04 điểm thấp, sửa chúng trước mọi bước khác, kể cả khi bước khác thấp hơn. Bước 06–08 xây trên nền của 02 và 04.

**Luật 2 — Tối đa 3 bước một đợt.** Nhiều hơn là không ai làm nổi.

**Luật 3 — Ưu tiên bước chặn dòng tiền.** Nếu 04 hoặc 08 hỏng thì tiền đang chảy ra ngoài mỗi ngày; các bước khác chờ được.

```
ĐỀ XUẤT — làm theo thứ tự này, khoảng 3 tuần

1. Bước 04 — Offer & Giá        (tuần 1)  /breakeven-analysis → /thiet-ke-offer
   Vì sao trước: chưa biết hoà vốn thì quảng cáo ở Bước 07 có thể đang lỗ mà không biết.

2. Bước 07 — Quảng cáo          (tuần 2)  /ads-strategy-planner → /ads-performance-diagnostic
   Vì sao sau 04: phải biết chi phí tối đa mỗi khách rồi mới đặt được ngưỡng dừng.

3. Bước 03 — Nghiên cứu         (tuần 3)  /mkt-phan-tich-doi-thu
   Vì sao cuối: cần thiết nhưng không chặn dòng tiền ngay.

TẠM BỎ QUA: 01, 02, 06 đang ổn — quay lại rà ở kỳ sau.
```

---

## Đọc ngược từ triệu chứng

Nếu người dùng mô tả một vấn đề cụ thể thay vì muốn chẩn đoán tổng thể:

| Triệu chứng | Bước hay hỏng thật sự |
|---|---|
| "Quảng cáo tốn tiền không ra đơn" | 04 (offer) hoặc 05 (phễu) — hiếm khi là 07 |
| "Content viết ra không ai tương tác" | 02 (định vị) — không phải 06 |
| "Khách hỏi giá xong biến mất" | 04 (giá không khớp giá trị cảm nhận) hoặc 08 (không theo đuôi) |
| "Đơn về không đều" | 05 (phễu không liên tục) hoặc 06 (đăng bài không đều) |
| "Tuyển sale mãi không được người tốt" | 08 (chưa có kịch bản để người mới đọc) |
| "Tôi phải làm mọi thứ" | 01 (chưa phân quyền) và 12 (chưa có quy trình) |
| "Doanh thu ổn nhưng không có lãi" | 04 (chưa tính biên từng dòng sản phẩm) |
| "Khách mua một lần rồi thôi" | 10 (chưa có cơ chế giữ) hoặc 09 (giao hàng chưa đủ tốt) |

**Quy tắc chung:** triệu chứng hiện ở bước sau, nguyên nhân thường nằm ở bước trước.

---

## Ghi kết quả vào đâu

| | |
|---|---|
| **Thư mục** | `50. Triển Khai 90 Ngày/` |
| **Tên file** | `Chẩn Đoán — YYYY-MM-DD.md` |
| **Bắt buộc** | Ghi thứ tự bước đã chọn vào `Decisions/` để cả đội biết đợt này tập trung vào đâu |

Chạy lại mỗi quý và so điểm với lần trước — đây là cách đo hệ thống có tốt lên không.

---

## Ràng buộc

- **Không đề xuất làm cả 12 bước.** Tối đa 3 bước một đợt.
- **Không bỏ qua Bước 02 và 04 khi chúng điểm thấp**, kể cả khi người dùng muốn nhảy thẳng vào quảng cáo.
- **Không chấm điểm dựa trên lời tự đánh giá** khi vault đã có dữ liệu — ưu tiên bằng chứng từ `/kiem-tra-cong`.
- Nói rõ với người dùng: chẩn đoán này dựa trên câu trả lời của họ, độ chính xác phụ thuộc mức độ thành thật.
