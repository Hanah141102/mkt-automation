---
updated: 2026-07-29
status: canonical
tags: [demo-ai, sales-playbook, closing, objection-handling]
---
> [!warning] ĐÂY LÀ BÀI MẪU — DỮ LIỆU HƯ CẤU
> Toàn bộ tên công ty, tên người, tên miền, số tiền và số liệu trong tài liệu này **đã được thay bằng dữ liệu ví dụ**. Không dùng các con số ở đây làm căn cứ kinh doanh. Giá trị của bộ tài liệu này nằm ở **cấu trúc và cách lập luận**, không nằm ở số liệu.


# 32 — Sales Playbook chuỗi 1: khi An đang dạy thì ai bán

> Hiện trạng BOD xác nhận: **An chốt chính, chưa có sale nào.** Bảo · Hà · Chi chỉ "giải đáp thắc mắc" cho data siêu nóng đã xem webinar. Tài liệu này thừa nhận đúng hiện trạng đó và biến nó thành quy trình chạy được — đồng thời đặt nền để **người thứ hai biết chốt** xuất hiện sau chuỗi 2, gỡ rủi ro lớn nhất mà doc 24 mục 10.10 đã cảnh báo.

> **Lưu ý phân vai:** nguồn chuẩn là [[05-organization-roles-raci]] và [[00-TLK-READ-ME-FIRST]]. Việc trực Q&A/đơn trong file này là `temporary assignment`; Hà vẫn là Support, Bảo/Chi vẫn là kỹ thuật lớp chuyên sâu.

---

## 1. Sự thật cần gọi đúng tên

"Giải đáp thắc mắc cho người đã xem webinar, đã hiểu hết, sắp đăng ký" **chính là khâu chốt sale.** Chỉ là nó đang được gọi bằng tên khác.

Điều này quan trọng vì hai lý do:

1. **Nếu gọi là "giải đáp", đội sẽ không được đào tạo và không được đo.** Ba người đang cầm khúc đắt nhất của phễu mà không ai chấm điểm họ.
2. **Nếu gọi đúng là "chốt", ta đo được và đào tạo được** — và sau 2 chuỗi sẽ biết ai trong ba người có khả năng thành closer thứ hai.

> **Quyết định của tài liệu này:** giữ nguyên cách làm việc hiện tại *(đội không chào bán chủ động, chỉ trả lời người hỏi)*, nhưng **đo và ghi lại như một khâu chốt thật**. Không đổi việc, chỉ đổi cách nhìn và cách đo.

---

## 2. Ranh giới ba người được và không được làm

| Được làm | Không được làm |
|---|---|
| Trả lời mọi câu về **nội dung khóa học** | Tự ý giảm giá, tặng thêm, gia hạn deadline |
| Xác nhận **giá và cơ chế nâng cấp** theo đúng bảng | Cam kết kết quả cụ thể *("chắc chắn anh sẽ ra X đơn")* |
| Gửi **link thanh toán** | Bàn về Solution 100–500tr hoặc Elite |
| Xác nhận **chính sách hoàn tiền, VAT** theo [[33-phap-ly-chinh-sach-ban-hang-va-ban-ghi]] | Trả lời câu hỏi pháp lý ngoài văn bản đã có |
| Hỏi lại để hiểu tình huống khách | Tư vấn khách nên chọn gói nào **khi khách phân vân giữa 12tr và 19tr** → chuyển An |
| Đặt lịch nói chuyện với An | Nhận đặt cọc bằng tài khoản cá nhân |

**Ba lằn ranh phải chuyển lên An ngay:**

1. Khách hỏi về **Solution / cài đặt cho doanh nghiệp / Elite**
2. Khách phân vân giữa **Co-Founder 12tr và Trọn bộ 19tr**
3. Khách đòi **giảm giá hoặc điều kiện đặc biệt**

---

## 3. Luật tốc độ — con số quan trọng nhất của cả tài liệu

| Loại lead | Phải trả lời trong | Vì sao |
|---|---|---|
| Nhắn trong khung Q&A (21h35–22h15) | **≤ 3 phút** | Đây là 20 phút sinh 75% đơn. Chậm 10 phút là mất đơn |
| Nhắn trong buổi, ngoài khung Q&A | ≤ 10 phút | |
| Nhắn sau buổi, trước 24h | ≤ 30 phút *(trong khung 08–23h)* | |
| **Form kim cương** *(form insight tick câu Solution/Elite)* | **≤ 24 giờ — Hà xử lý tạm, book lịch riêng với An** | Doc 17 C2.9: sau 72h lead webinar gần như mất giá trị |
| Người dự ≥3 buổi mà chưa mua, sau chuỗi | ≤ 48 giờ | Nhóm đáng theo đuổi nhất sau chuỗi |

> **Đo được bằng cách nào:** cột `ts_lien_he_dau` trong Sheet, trừ đi `ts_khach_nhan`. Không đo thì luật này chỉ là lời khuyên.

✅ **ĐÃ CHỐT 29/07:** form kim cương → khối Solution *(sẽ có sale riêng)*. Giai đoạn tạm: **Hà care**, nhiệm vụ là book lịch riêng với An. Xem mục 7.

---

## 4. Phân luồng — ai xử lý ai

```
Người nhắn tin
      │
      ├─ Hỏi về nội dung / giá / cách học ──────▶ Chi · Hà · Bảo (theo ca)
      │
      ├─ Đã quyết mua, cần link thanh toán ─────▶ Bảo
      │
      ├─ Muốn nâng cấp gói đã mua ──────────────▶ Bảo (quy trình mục 6)
      │
      ├─ Phân vân 12tr / 19tr ──────────────────▶ AN
      │
      ├─ Hỏi Solution / cài cho DN / Elite ─────▶ AN (qua form kim cương)
      │
      └─ Đòi giảm giá / điều kiện riêng ────────▶ AN
```

### Ca trực *(BOD chốt 29/07: Hà và Bảo trực khung Q&A)*

| Khung | Ai trực | Ghi chú |
|---|---|---|
| Trong buổi 20h00–21h30 | Chi *(chat Zoom + nhóm)* + Bảo *(vé, đơn)* | Hà làm kỹ thuật |
| **Khung Q&A 21h35–22h15** ⭐ | **Hà + Bảo** | **75% đơn rơi vào đây.** ⚠️ Hà đang kiêm kỹ thuật — xem cảnh báo bên dưới |
| 22h15–23h30 | Bảo + Chi | Khung đơn rơi nhiều thứ hai |
| Sáng hôm sau 08h–12h | Hà | |
| Chiều 13h–18h | Chi | |
| Tối ngoài buổi 18h–23h | Bảo | |

> ⚠️ **Xung đột vai:** Hà vừa là Chủ phòng kỹ thuật vừa được giao trực chốt Q&A — hai vai va nhau đúng 40 phút quan trọng nhất. Ba cách gỡ ở [[31-run-of-show-5-buoi-va-spec-ghi-hinh]] mục 2. **Khuyến nghị: Chi chuyển sang kỹ thuật từ 21h30, Hà sang chốt.** `[CHỜ BOD]` chốt trước D−3.

### Bán vé VIP — việc mới của Bảo

BOD chốt bán thêm vé 280k trong buổi 1. Bảo phụ trách:

| Mốc | Việc |
|---|---|
| Buổi 1, phút 8 | Thả link vé vào chat **một lần** |
| Buổi 1, phút 118 | Nhắc lại **một lần** khi phát quà cuối buổi |
| Trong đêm | Xác nhận thanh toán, ghi cột `tang_ve` = `VIP`, `mua_ve_o_dau` = `buoi1` |
| Trong 2 giờ | Gửi bản ghi + workbook + template cho người mua vé |

**Cấm:** nhắc vé quá 2 lần trong buổi 1, hoặc nhắn riêng chào vé cho người chưa hỏi. Buổi 1 là buổi tạo niềm tin, không phải buổi bán.

---

## 5. Kịch bản — bốn tình huống chiếm 80% cuộc trò chuyện

### 5.1 Mở đầu khi khách nhắn "cho em hỏi khóa này..."

> *"Dạ em chào anh/chị [tên]. Em là [tên] từ chương trình. Trước khi em trả lời, cho em hỏi nhanh: hiện tại anh/chị đang làm gì và điều gì làm anh/chị quan tâm tới khóa này ạ?"*

**Vì sao hỏi trước khi trả lời:** một câu trả lời chung chung cho một câu hỏi chung chung không chốt được ai. Biết bối cảnh mới nói đúng phần khách cần.

**Cấm:** dán một đoạn giới thiệu khóa học dài. Người ta vừa nghe 2 tiếng rồi.

### 5.2 Khi khách hỏi giá

> *"Dạ Cấp {N} là {giá}. Và có một điều quan trọng anh/chị nên biết trước khi quyết: bất cứ lúc nào anh/chị muốn lên gói cao hơn, chỉ trả phần chênh — không mất đồng nào của hôm nay. Hiệu lực tới 48 giờ sau buổi cuối."*

**Luôn nói cơ chế nâng cấp cùng lúc với giá.** Doc 17 C2: người mua sớm mà không biết có combo sẽ thành nhóm khách hối tiếc — đúng nhóm mua nhanh nhất.

**Cách nói combo — dùng cộng dồn, không dùng phần trăm** *(doc 17 C1)*:

| ❌ Không nói | ✅ Nói |
|---|---|
| "Combo 2 khóa giảm 10%" | **"Khóa thứ hai chỉ thêm 5,6 triệu"** |
| "Combo 3 khóa giảm 20%" | **"Khóa thứ ba chỉ thêm 2,8 triệu"** |
| "Trọn bộ giảm 5,6 triệu" | **"Thêm Co-Founder chỉ 11 triệu thay vì 12"** |

### 5.3 Năm phản đối chắc chắn xuất hiện

Doc 17 C3.3 yêu cầu viết trước. Đây là bản viết trước.

| Phản đối | Đừng nói | Nói |
|---|---|---|
| **"Đắt quá"** | *"Không đắt đâu anh, so với giá trị thì..."* | *"Dạ em hiểu. Cho em hỏi để tư vấn đúng: hiện mỗi tháng anh/chị đang mất bao nhiêu giờ cho việc [X] mà agent làm được? Nếu con số đó nhỏ thì thật sự chưa cần khóa này ạ."* — **Chuyển từ giá sang chi phí của việc không làm gì. Và dám nói "chưa cần"** |
| **"Tôi không biết công nghệ"** | *"Dễ lắm anh, ai cũng làm được"* | *"Dạ đúng phần lớn học viên cũng vậy. Anh/chị có thấy phần demo tối nay em dựng agent trong 8 phút không ạ? Toàn bộ là gõ tiếng Việt, không có dòng code nào. Cái khó không phải công nghệ, là biết giao việc gì cho nó."* — **Chỉ vào bằng chứng vừa xảy ra** |
| **"Cần bàn với vợ / BOD"** | *"Anh cứ quyết đi ạ"* | *"Dạ hoàn toàn nên ạ. Để em gửi anh/chị bản tóm tắt 1 trang có phạm vi, lộ trình và chi phí để anh/chị trao đổi cho dễ. Anh/chị dự định trao đổi khi nào để em nhắc lại đúng lúc ạ?"* — **Trang bị cho họ + đặt mốc thời gian, không ép** |
| **"Tôi từng mua khóa rồi không làm"** | *"Khóa này khác lắm ạ"* | *"Dạ em nghe câu này nhiều, và thường lý do giống nhau: học xong không có ai theo và không có gì buộc phải nộp. Ở đây mỗi buổi anh/chị phải ra được một tài sản dùng được — không phải ghi chép. Anh/chị kể em nghe lần trước tắc ở đâu ạ?"* — **Đồng ý với họ trước, rồi chỉ vào cơ chế** |
| **"Team tôi không dùng được"** | *"Team sẽ quen thôi"* | *"Dạ đây là lo lắng đúng. Cho em hỏi team anh/chị bao nhiêu người và ai sẽ là người cầm phần này? Nếu chưa có ai cầm thì thật ra anh/chị cần một hướng khác chứ không phải khóa này."* — **Hỏi để chẩn đoán, và nếu không phù hợp thì nói thật** |

> **Nguyên tắc chung của cả năm:** không phản bác. Đồng ý với phần đúng trong phản đối, rồi hỏi một câu để chẩn đoán. **Người dám nói "cái này chưa hợp với anh" bán được nhiều hơn người luôn nói có.**

### 5.4 Khi khách im sau khi hỏi giá

Chờ 20 phút, rồi nhắn **một** lần:

> *"Dạ em để anh/chị suy nghĩ ạ. Em chỉ nhắc một điều: cơ chế nâng cấp hết hạn 48 giờ sau buổi cuối, sau đó mua lẻ từng khóa sẽ đắt hơn. Anh/chị cần em làm rõ thêm gì không ạ?"*

**Không nhắn lần thứ hai trong cùng ngày.** Ngày hôm sau, nếu người đó có dự buổi tiếp theo → nhắn lại một lần nữa với nội dung mới, không lặp lại.

---

## 6. Quy trình nâng cấp — khâu dễ vỡ nhất chưa ai thiết kế

Doc 17 C2.3 liệt kê đây vào **nhóm chặn**: bậc thang 5→9→11→19 đòi khách trả **phần chênh**, mà không cổng thanh toán VN nào làm việc này mặc định.

### 6.1 Ba đường nâng cấp và số tiền chênh

| Đã mua | Muốn lên | Trả thêm |
|---|---|---:|
| Cấp bất kỳ (5tr) | Gói 2 khóa (9tr) | **4tr** |
| Gói 2 khóa (9tr) | Gói 3 khóa (11tr) | **2tr** |
| Gói 3 khóa (11tr) | TRỌN BỘ (19tr) | **8tr** |
| Cấp bất kỳ (5tr) | Co-Founder (12tr) | **7tr** |
| Co-Founder (12tr) | TRỌN BỘ (19tr) | **7tr** |
| Chưa mua gì | TRỌN BỘ (19tr) | **19tr** |

**Kiểm tra:** mọi đường đều về đúng **19tr**. Không ai bị phạt vì mua sớm, không ai được thưởng vì chờ. Đây là điều kiện bắt buộc *(doc 17 B3-V2)*.

### 6.2 Quy trình thu tiền chênh — làm tay, nhưng có quy trình

| Bước | Việc | Ai | Thời gian |
|:--:|---|---|---|
| 1 | Khách nhắn muốn nâng cấp | — | — |
| 2 | Bảo **tra Sheet** cột `goi_mua` xác nhận đã mua gì, ngày nào | Bảo | 2 phút |
| 3 | Bảo tính chênh theo bảng 6.1, **đọc lại thành lời**: *"Anh đã trả 5tr, lên Trọn bộ là thêm 14tr, tổng đúng 19tr như bảng"* | Bảo | 1 phút |
| 4 | Gửi **link thanh toán tạo tay** đúng số tiền chênh, ghi rõ nội dung `NANGCAP-{sđt}-{gói mới}` | Bảo | 3 phút |
| 5 | Nhận tiền → cập nhật cột `goi_mua`, `da_nang_cap`, `doanh_thu` | Bảo | 2 phút |
| 6 | **Thêm khách vào nhóm/lớp của gói mới trong 2 giờ** | Bảo | — |

**Luật:** bước 3 không được bỏ. Đọc lại phép tính thành lời là thứ chặn khiếu nại "sao tôi trả nhiều hơn người kia".

**Rủi ro cần canh:** Bảo làm một mình cả thanh toán lẫn nâng cấp lẫn cập nhật Sheet. Ở buổi 5 với hàng chục đơn, đây là **điểm nghẽn chắc chắn xảy ra**. Phải có người thứ hai.

---

## 7. Form kim cương — đường đi của tiền lớn

Form insight phát ở **buổi 2 và buổi 4** *(doc 16 mục 7.2)*, đóng gói tên **"Bản đồ AI hóa doanh nghiệp của bạn"**.

### Routing sau khi khách nộp

> ✅ **BOD chốt 29/07:** form kim cương **chuyển sang khối Solution, sẽ có sale riêng của Solution.** Trong lúc chờ set xong khối Solution, **Hà care tạm** — nhiệm vụ duy nhất là **book lịch riêng với An**, không bán gì.

| Trả lời "mức sẵn sàng" | Đi đâu | Ai xử *(giai đoạn tạm)* | Ai xử *(khi có khối Solution)* | Trong |
|---|---|---|---|---|
| Tự làm theo hướng dẫn | Ở lại khóa · gợi ý lên Co-Founder | Bảo | Bảo | 24h |
| **Muốn được cài giúp** | **Solution** — book lịch riêng với An | **Hà → An** | Sale Solution | **24h** |
| **Muốn đội ngũ vận hành cùng** | **Solution cao cấp / Managed** | **Hà → An** | Sale Solution | **24h** |
| Tick câu Elite + đạt tiêu chí | Elite — phỏng vấn 1-1 | **An** | **An** | 48h |

**Việc của Hà với nhóm Solution — chỉ ba câu, không bán:**

> *"Dạ em đã đọc bản anh/chị điền. Có mấy chỗ em nghĩ anh An nên xem trực tiếp. Anh/chị sắp xếp được 30 phút vào [2 khung giờ cụ thể] không ạ?"*

**Cấm:** báo giá Solution, mô tả phạm vi, hứa gì. Nhiệm vụ duy nhất là **book được lịch riêng với An**.

> **Vì sao đây là phần đáng tiền nhất của cả chuỗi:** một deal Solution 100–500tr bằng 5–25 người mua Trọn bộ. Và nó chỉ xảy ra nếu có người book lịch trong 24h.

**Ba việc phải có trước chuỗi 1 để đường này chạy:**

| # | Việc | Ai | Hạn |
|:--:|---|---|---|
| 1 | An **chặn sẵn 4 khung 30 phút/tuần** trong lịch riêng cho discovery Solution | An | D−5 |
| 2 | Hà có **quyền xem và đặt vào lịch đó** *(link Calendly hoặc quyền Google Calendar)* | Hà | D−5 |
| 3 | Kịch bản 3 câu ở trên **in ra, dán chỗ Hà ngồi** | Hà | D−3 |

> **Rủi ro giai đoạn tạm:** Hà đang giữ 3 vai *(kỹ thuật Zoom · trực chốt Q&A · care form kim cương)*. Đây là người quá tải nhất trong chuỗi 1. **Khi khối Solution có sale riêng, chuyển ngay** — và ghi mốc đó vào roadmap chuỗi 2.

---

## 8. Sau khi mua — bàn giao học viên

Doc 24 mục 10.7: *"học viên trả tiền rồi bị bỏ rơi giữa hai khâu"*. Quy trình chặn:

| Mốc | Việc | Ai |
|---|---|---|
| Trong 15 phút | Tin nhắn xác nhận: đã nhận tiền, gói gì, bước tiếp theo là gì, ngày nào | Bảo |
| Trong 2 giờ | Thêm vào nhóm học viên của gói đúng | Bảo |
| Trong 24 giờ | Gửi bộ tài liệu khởi động + lịch buổi đầu | Bảo |
| Trong 72 giờ | **Một tin nhắn hỏi thăm cá nhân** — không bán gì | Chi |
| Sau 7 ngày | Hỏi đã làm được bước 1 chưa; nếu chưa, hỏi vướng ở đâu | Chi |

**Tin nhắn 72 giờ là khoản đầu tư rẻ nhất vào tỷ lệ hoàn tiền và testimonial.** Người vừa trả 5–19tr mà 3 ngày không ai nhắn sẽ bắt đầu nghi ngờ quyết định của mình.

---

## 9. Đo và chấm — nền để có closer thứ hai

### 9.1 Chỉ số theo người *(tối đa 4 chỉ số/người — luật doc 24 mục 4.1)*

| Chỉ số | Cách tính | Ngưỡng chuỗi 1 |
|---|---|---|
| **Tốc độ phản hồi trung bình** trong khung Q&A | Trung bình `ts_lien_he_dau − ts_khach_nhan` | `[PHẢI ĐO]` — đề xuất ≤5 phút |
| **Số cuộc trò chuyện xử lý** | Đếm | Baseline |
| **Tỷ lệ trò chuyện → đơn** | Đơn ÷ số cuộc | `[PHẢI ĐO]` — đây là chỉ số phát hiện closer |
| **Tỷ lệ chuyển đúng tuyến** | Số ca chuyển An đúng ÷ tổng ca đáng chuyển | 100% |

> Chỉ số thứ 3 là thứ sẽ trả lời câu hỏi lớn: **ai trong ba người có khả năng thành closer thứ hai.** Không đo ở chuỗi 1 thì chuỗi 3 vẫn phải An chốt.

### 9.2 Việc bắt buộc sau chuỗi 1

| # | Việc | Ai | Ra cái gì |
|:--:|---|---|---|
| 1 | Xuất toàn bộ hội thoại Zalo của 3 người | Bảo | Kho nguyên liệu |
| 2 | Chọn **10 cuộc thắng và 10 cuộc thua**, đọc cùng nhau 90 phút | An + 3 người | Biết chỗ mất đơn thật |
| 3 | Viết bổ sung **5 phản đối mới** thực sự xuất hiện | Chi | Bản v2 của mục 5.3 |
| 4 | Chấm 3 người theo mục 9.1, chọn **1 người vào lộ trình closer** | An | Gỡ rủi ro doc 24 mục 10.10 |

---

## 10. Checklist trước chuỗi

| # | Việc | Hạn | Ai | ✅ |
|:--:|---|---|---|:--:|
| 1 | Chốt **tên người** xử lý form kim cương ≤24h | D−7 | An | ⬜ |
| 2 | Chốt ≥2 người trực chốt thêm cho buổi 5 | D−3 | An | ⬜ |
| 3 | In bảng 6 đường nâng cấp, dán chỗ Bảo ngồi | D−3 | Bảo | ⬜ |
| 4 | Tạo sẵn mẫu link thanh toán cho 6 mức chênh | D−3 | Bảo | ⬜ |
| 5 | Ba người học thuộc 5 kịch bản phản đối, **diễn thử với nhau 60 phút** | D−2 | Chi · Hà · Bảo | ⬜ |
| 6 | Chốt ca trực và dán lịch | D−2 | Chi | ⬜ |
| 7 | Tạo cột `ts_lien_he_dau` trong Sheet | D−2 | Bảo | ⬜ |
| 8 | Xác nhận chính sách hoàn tiền + VAT đã có văn bản ([[33-phap-ly-chinh-sach-ban-hang-va-ban-ghi]]) | D−3 | BOD | ⬜ |

---

## Khối bàn giao

**Dùng ngay:** ranh giới (mục 2) · luật tốc độ (mục 3) · phân luồng (mục 4) · 5 kịch bản phản đối (mục 5.3) · bảng nâng cấp (mục 6.1) · routing form kim cương (mục 7).

**`[CẦN BỔ SUNG]`:** tên người xử lý form kim cương · tên 2 người trực chốt thêm buổi 5 · người thứ hai hỗ trợ Bảo khâu thanh toán.

**`[PHẢI ĐO]`:** tốc độ phản hồi · tỷ lệ trò chuyện→đơn từng người · tỷ lệ mua combo · tỷ lệ nâng cấp *(chỉ số số một của doc 17 B5)*.

**Không được làm:** đội tự giảm giá · đội báo giá Solution · để Bảo một mình xử lý thanh toán buổi 5 · nhắn theo đuổi 2 lần trong cùng ngày.

*Tài liệu 32 · playbook vận hành · 29/07/2026 · phái sinh từ [[08-product-offer-map]] mục 5, [[16-webinar-funnel-blueprint]] mục 7.2, [[17-chuong-trinh-webinar-5-ngay]] B+C, [[24-he-thong-van-hanh-jd-kpi-quy-trinh]] mục 10.*
