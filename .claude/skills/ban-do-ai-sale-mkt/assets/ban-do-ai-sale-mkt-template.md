---
tags: [identity, ai-roadmap, sales-marketing]
trang-thai: cho-xac-nhan
created: YYYY-MM-DD
cap-nhat: YYYY-MM-DD
chu-ky-ban-ngay: {{lấy từ Hồ Sơ Mô Hình Kinh Doanh}}
so-de-xuat-lam-ngay: {{0 đến 3}}
---

# 🗺️ Bản Đồ Ứng Dụng AI — Sale & Marketing — {{TÊN DOANH NGHIỆP}}

> Bản đồ này trả lời một câu: **nên đưa AI vào điểm nào trong bán hàng và marketing, điểm nào chưa nên, và người vẫn phải duyệt gì.** Phạm vi chỉ Sale & Marketing. Không nêu tên công cụ. Mọi ngưỡng thời gian tính từ chu kỳ bán {{X}} ngày trong [[Hồ Sơ Mô Hình Kinh Doanh]].
>
> Nhãn dùng trong file: **[fact]** người dùng nói · **[suy luận]** Claude rút ra từ fact · **⚠️ giả định** chưa kiểm chứng · **chưa có dữ liệu** cần đo trước.

---

## ⚡ Kết luận nhanh

{{3 đến 5 gạch đầu dòng, viết SAU khi xong các phần dưới: điểm nghẽn lớn nhất, đề xuất số 1, việc phải làm trước khi đụng tới AI, điều không bao giờ giao AI.}}

---

## 1. Bối cảnh lấy từ mô hình kinh doanh

| Tham số | Giá trị | Ảnh hưởng tới bản đồ này |
|---|---|---|
| Loại sản phẩm | {{so / dich-vu / vat-ly / hon-hop}} | {{...}} |
| Chu kỳ bán | {{X}} ngày | Chạm lead nóng trong {{15 phút / 4 giờ}} · nhắc sau báo giá ngày {{5%X}}, {{15%X}}, {{30%X}} · giữ lead tối đa {{1,5X}} ngày · nhịp đọc số {{tuần / hai tuần / tháng}} |
| Người mua có là người dùng | {{co / khong}} | {{một hay hai kịch bản nhắn tin}} |
| Mùa vụ | {{deu / co-mua, tháng ...}} | {{hạn chót triển khai trước mùa}} |
| Giao dịch xảy ra ở đâu | {{co / ban-tren-san / hon-hop}} | {{trọng tâm A3, A2}} |
| Mô hình mua lại | {{khong / lien-tuc / theo-ky}} | {{trọng tâm A6, A7}} |
| Phân khúc ưu tiên | [[PK1 — {{...}}]] | Tín hiệu lead tốt: {{...}} |
| Phản đối thường gặp | {{từ GT*.md}} | Đầu vào cho A3, A5 |

Nguồn: [[Business Model Canvas — {{TÊN}}]] · [[_MHKD {{TÊN}} — Tổng Quan]] · [[Đánh Giá Mô Hình Kinh Doanh — {{TÊN}}]]

---

## 2. Bản đồ quy trình hiện tại

{{Đúng những bước người dùng kể, đã được họ xác nhận. Không thêm bước "chuẩn" mà họ không có. Ký hiệu: 🔴 chặn dòng tiền · 🟠 lặp lại nhiều, tốn giờ · ⚪ chưa có quy trình.}}

### Thu hút

| # | Bước | Ai làm | Lần/tuần | Phút/lần | Dùng gì | Hay lỗi ở đâu | Dữ liệu để lại | Nhãn |
|---|---|---|---|---|---|---|---|---|
| T1 | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} | {{🔴/🟠/⚪}} |

### Lead vào

| # | Bước | Ai làm | Lần/tuần | Phút/lần | Dùng gì | Hay lỗi ở đâu | Dữ liệu để lại | Nhãn |
|---|---|---|---|---|---|---|---|---|
| L1 | {{...}} | | | | | | | |

### Tư vấn và chốt

| # | Bước | Ai làm | Lần/tuần | Phút/lần | Dùng gì | Hay lỗi ở đâu | Dữ liệu để lại | Nhãn |
|---|---|---|---|---|---|---|---|---|
| C1 | {{...}} | | | | | | | |

### Sau bán

| # | Bước | Ai làm | Lần/tuần | Phút/lần | Dùng gì | Hay lỗi ở đâu | Dữ liệu để lại | Nhãn |
|---|---|---|---|---|---|---|---|---|
| S1 | {{...}} | | | | | | | |

### Đo lường

| # | Bước | Ai làm | Lần/tuần | Phút/lần | Dùng gì | Hay lỗi ở đâu | Dữ liệu để lại | Nhãn |
|---|---|---|---|---|---|---|---|---|
| D1 | {{...}} | | | | | | | |

**Ngoài phạm vi, ghi lại không chấm:** {{điểm đau về kho, kế toán, nhân sự nếu có, mỗi cái một dòng, kèm gợi ý `/process-automation-audit`}}

---

## 3. Ba điểm nghẽn theo dòng tiền

{{Xếp theo mức mất tiền. Mỗi điểm: bước nào, chuyện gì xảy ra, bằng chứng người dùng kể [fact], Claude suy ra gì [suy luận], còn giả định gì.}}

1. **{{Bước}}** — {{...}}
2. **{{Bước}}** — {{...}}
3. **{{Bước}}** — {{...}}

---

## 4. Bảng chấm điểm cơ hội

{{Chỉ chấm những bước có nhãn 🔴 hoặc 🟠. Bước ⚪ ghi thẳng "chưa có quy trình" và không chấm. Khung điểm ở `references/khung-cham-diem-va-diem-ung-dung.md`.}}

| Bước | Họ agent | Dòng tiền | Lặp lại | Quy trình & dữ liệu | Rủi ro thấp | Người vận hành | Tổng /10 | Điều kiện chặn | Tầng |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|---|---|
| {{L1}} | {{A3}} | {{0-2}} | {{0-2}} | {{0-2}} | {{0-2}} | {{0-2}} | {{...}} | {{không / số 1, 2, 3}} | {{Làm ngay / Kế tiếp / Chưa nên}} |

---

## 5. Đề xuất

### Tầng 1 — Làm ngay trong 30 ngày {{(tối đa 3)}}

{{Nếu tầng này trống vì điều kiện chặn số 3, viết rõ: "Chưa có người nhận vận hành và duyệt. Tầng này để trống cho tới khi có." Không bịa đề xuất cho đầy.}}

#### Đề xuất 1 — {{Tên ngắn, ví dụ "Agent nhắn tin giữ lead ngoài giờ trên Facebook và Zalo"}}

| Mục | Nội dung |
|---|---|
| **Họ agent** | {{A1 đến A8, có thể chỉ một thành phần}} |
| **Điểm chạm** | {{bước nào trong bảng quy trình, mã T/L/C/S/D}} |
| **Hiện trạng** | {{[fact] ai làm, mất bao lâu, lỗi gì}} |
| **Việc agent làm** | {{mô tả bằng động từ, không nêu công cụ}} |
| **Người vẫn duyệt** | {{vai trò cụ thể duyệt gì, ở mức nào: từng tin / theo mẫu / xem báo cáo}} |
| **Dữ liệu cần có trước** | {{liệt kê, đánh dấu cái nào đã có, cái nào phải gom}} |
| **Chỉ số đo** | {{1 đến 3 chỉ số, ghi giá trị hiện tại nếu biết, "chưa có dữ liệu" nếu không}} |
| **Ngưỡng thời gian áp dụng** | {{tính từ chu kỳ bán, ví dụ "gọi lại lead ngoài giờ trong 4 giờ làm việc kế tiếp"}} |
| **Rủi ro và cách chặn** | {{2 đến 3 rủi ro, mỗi cái kèm cách chặn}} |
| **Chi phí ước tính** | {{khoảng VND/tháng, ⚠️ giả định nếu chưa khảo giá, hoặc "chưa có dữ liệu"}} |
| **Bước đầu tiên tuần này** | {{một việc làm được trong 1 đến 2 giờ}} |
| **Skill tiếp theo** | {{ví dụ `/chot-don-qua-inbox`}} |

#### Đề xuất 2 — {{...}}

{{cùng khung}}

#### Đề xuất 3 — {{...}}

{{cùng khung}}

### Tầng 2 — Kế tiếp trong 60 đến 90 ngày

{{Mỗi đề xuất 4 dòng: họ agent và điểm chạm · việc agent làm · điều kiện phải xong trước (gom dữ liệu gì, viết quy trình gì) · chỉ số đo.}}

- **{{Tên}}** ({{A?}}, bước {{...}}) — {{...}}. *Điều kiện trước:* {{...}}. *Đo bằng:* {{...}}.

### Tầng 3 — Chưa nên, và vì sao

{{Mỗi dòng: tên · lý do (điểm thấp ở tiêu chí nào, hoặc điều kiện chặn nào) · điều kiện để xét lại.}}

- **{{Tên}}** — {{lý do}}. *Xét lại khi:* {{...}}.

---

## 6. Ranh giới: AI không làm

{{Rút từ lượt 6 và từ các đề xuất. Đối chiếu với mục "Không được tự quyết" trong [[AI-Sale-Assistant]]; điểm nào mới thì đề xuất người dùng cập nhật file đó, không tự sửa.}}

- Không quyết giá, chiết khấu, cam kết thời hạn với khách.
- Không tự gửi tin cho khách trong 30 ngày đầu; sau đó chỉ gửi tin theo mẫu đã duyệt, có nhãn là trợ lý.
- Không giả người thật; khách hỏi thì chuyển người ngay.
- Không nhắn chủ động cho khách chưa có cơ sở đồng ý.
- Không dùng dữ liệu cá nhân ngoài phạm vi bán hàng và chăm sóc.
- {{thêm từ câu trả lời của người dùng}}

---

## 7. Dữ liệu cần gom trước khi bắt đầu

{{Tất cả chỗ người dùng trả lời "chưa đo" hoặc "chưa biết" mà đề xuất Tầng 1 và 2 cần. Mỗi dòng kèm cách đo đơn giản nhất và ai làm.}}

| Dữ liệu | Cần cho đề xuất | Cách đo đơn giản nhất | Ai làm | Bao lâu có |
|---|---|---|---|---|
| {{ví dụ: thời gian phản hồi inbox theo giờ}} | {{Đề xuất 1}} | {{ghi tay 20 tin gần nhất: giờ khách nhắn, giờ trả lời}} | {{...}} | {{1 tuần}} |

---

## 8. Kế hoạch 30 ngày đầu

{{Chỉ cho Tầng 1. Nếu `mua-vu: co-mua`, kiểm tra 30 ngày này không rơi vào 6 tuần trước mùa cao điểm; nếu rơi, dời và ghi rõ.}}

| Tuần | Việc | Ai | Kết quả nhìn thấy |
|---|---|---|---|
| 1 | {{gom dữ liệu, viết bộ câu trả lời chuẩn, chốt người duyệt}} | | |
| 2 | {{chạy thử nội bộ, chưa tới khách}} | | |
| 3 | {{chạy với khách, người duyệt từng tin}} | | |
| 4 | {{đọc số, quyết giữ hay dừng}} | | |

**Chỉ số thành công sau 30 ngày** (đúng câu người dùng trả lời ở lượt 6, không thay bằng chỉ số khác): {{...}}

---

## 9. Việc tiếp theo

- {{Đề xuất 1}} → chạy `/{{skill}}`
- {{Điểm chưa có quy trình}} → chạy `/sop-builder`
- Quyết định ngân sách công cụ và thay đổi cách phản hồi khách → ghi vào `Decisions/` sau khi chủ doanh nghiệp xác nhận
- Rà lại bản đồ này sau {{nhịp đọc số × 4, ví dụ 2 tháng}} hoặc khi đổi mô hình kinh doanh

---

## 🔗 Kết nối với

- [[Hồ Sơ Mô Hình Kinh Doanh]] — 6 tham số điều khiển mọi ngưỡng trong file này
- [[Business Model Canvas — {{TÊN}}]] · [[_MHKD {{TÊN}} — Tổng Quan]]
- [[Đánh Giá Mô Hình Kinh Doanh — {{TÊN}}]]
- [[AI-Sale-Assistant]] — ranh giới AI, cần khớp với mục 6
- [[Chân Dung Doanh Nghiệp]] · [[Brand Voice — Giọng Thương Hiệu]]
- [[_MOC 03. Areas]] — nơi ghi kết quả vận hành khi các đề xuất chạy thật
