# Diễn mẫu — một CEO dùng hệ thống từ đầu tới cuối

Tài liệu này theo chân một doanh nghiệp thật-như-thật đi hết 12 bước, để bạn thấy **luồng hỏi đáp diễn ra thế nào** và **kết quả rơi vào đâu**.

> Doanh nghiệp và số liệu dưới đây là hư cấu, dựng cho dễ hình dung.

---

## Bối cảnh

**Xưởng Nội Thất Mộc An** — Hà Nội, làm nội thất gỗ theo yêu cầu.

| | |
|---|---|
| Chủ | Anh Tuấn, 38 tuổi, xuất thân thợ mộc |
| Đội | 6 người: Tuấn (chủ) · Hà (marketing) · Linh (sale, trực inbox) · Bình (thợ cả) · Sơn (thợ) · Mai (kế toán kiêm hành chính) |
| Doanh thu | Trung bình 700 triệu/tháng — tháng cao 1 tỷ, tháng thấp 400 triệu |
| Khách đến từ | Facebook, khách cũ giới thiệu, một ít Google |

**Bốn vấn đề anh Tuấn nói ra khi bắt đầu:**

1. Đơn về không đều, không biết vì sao
2. Anh phải tự chốt tất cả đơn trên 50 triệu
3. Mỗi người báo giá một kiểu, có đơn làm xong mới biết lỗ
4. Đang chạy quảng cáo 15 triệu/tháng nhưng không biết có lãi không

---

## NGÀY 1 — Cài đặt và khai báo doanh nghiệp

Anh Tuấn cài Obsidian, copy vault về máy, mở terminal trong thư mục vault, gõ `claude`.

### Anh gõ lệnh đầu tiên

```
/mo-hinh-kinh-doanh
```

### Claude hỏi lại

> Trước khi bắt đầu, tôi cần hiểu doanh nghiệp của anh. Ta sẽ đi qua 9 ô mô hình kinh doanh, mỗi lần một ô.
>
> **Ô 1 — Phân khúc khách hàng.** Anh mô tả giúp: ai là người trả tiền cho Mộc An? Nếu có nhiều nhóm khác nhau, kể hết ra.

**Anh Tuấn:** *"Chủ yếu là chủ nhà mới xây hoặc mới mua chung cư, cần đóng nội thất trọn gói. Thêm mấy quán cà phê, nhà hàng nhỏ."*

> Anh cho tôi thêm hai chi tiết:
> 1. Trong hai nhóm đó, nhóm nào mang lại nhiều doanh thu hơn, ước chừng bao nhiêu phần trăm?
> 2. Nhóm nào anh thấy **dễ làm việc hơn** — ít sửa đi sửa lại, thanh toán đúng hạn?

**Anh Tuấn:** *"Nhà ở khoảng 75%. Nhưng quán cà phê dễ làm hơn, họ quyết nhanh, không đắn đo từng cái tay nắm."*

> Ghi nhận. Đây là một điểm đáng chú ý: nhóm mang lại nhiều doanh thu **không phải** nhóm dễ làm việc nhất. Ta sẽ quay lại chỗ này ở phần định vị.
>
> **Ô 2 — Giá trị cốt lõi.** Khách chọn Mộc An thay vì xưởng khác vì điều gì? Đừng trả lời "chất lượng tốt, giá hợp lý" — ai cũng nói vậy. Anh nghĩ về lần gần nhất một khách chốt đơn: họ nói câu gì trước khi đồng ý?

**Anh Tuấn:** *"Có chị khách bảo: 'chị đi mấy chỗ rồi, chỉ có em là dám nói cái nào làm được cái nào không, chỗ khác cứ ừ hết rồi làm không ra'."*

> Đó là một giá trị thật và hiếm. Tôi tạm ghi là **"nói thật về giới hạn kỹ thuật trước khi nhận đơn"**. Ta sẽ kiểm chứng lại ở Bước 03 xem đối thủ có làm được điều này không.

*…đi tiếp 7 ô còn lại, mất khoảng 80 phút…*

### Claude tạo ra gì

```
00. Business Context/
├─ Chân Dung Doanh Nghiệp.md
├─ Business Model Canvas — Mộc An.md
├─ Business Model Canvas.canvas          ← sơ đồ 9 ô nhìn được
├─ Đánh Giá Mô Hình Kinh Doanh — Mộc An.md
└─ MHKD/
   ├─ Phân Khúc Khách Hàng/
   │  ├─ PK1 — Chủ nhà mới xây, hoàn thiện trọn gói.md
   │  ├─ PK2 — Chủ chung cư mới nhận, làm từng phần.md
   │  └─ PK3 — Quán cà phê, nhà hàng nhỏ.md
   └─ Giá Trị Cốt Lõi/
      ├─ GT1 — Nói thật về giới hạn kỹ thuật trước khi nhận đơn.md
      └─ GT2 — Thợ cả trực tiếp khảo sát, không qua trung gian.md
```

> **Điều đáng chú ý:** anh Tuấn chỉ trả lời câu hỏi. Anh không phải nghĩ ra cấu trúc, không phải biết Business Model Canvas là gì. Cấu trúc do skill lo.

---

## NGÀY 2 — Bịt chỗ thiếu và chốt giọng

```
/hoan-tat-business-context
```

> Tôi vừa quét `00. Business Context/`. Còn thiếu ba thứ:
>
> | Thiếu | Mức quan trọng | Vì sao cần |
> |---|---|---|
> | `Brand Voice — Giọng Thương Hiệu.md` | **Cao** | Chưa có thì mọi content sinh ra sau này sẽ nhạt |
> | `Sản Phẩm & Dịch Vụ/` | **Cao** | Chưa có thì không báo giá tự động được |
> | `Chân Dung CEO` | Trung bình | Chỉ cần nếu anh định lên hình bán hàng |
>
> Ta bắt đầu từ Brand Voice. Anh có sẵn tài liệu nào không, hay tôi phỏng vấn?

**Anh Tuấn:** *"Không có gì cả. Bạn hỏi tôi đi."*

> **Câu 1.** Nếu Mộc An là một người, anh muốn khách nghĩ về người đó thế nào sau lần gặp đầu?

**Anh Tuấn:** *"Như một ông thợ có nghề, nói ít, nói là làm được."*

> **Câu 2.** Có từ nào anh **không muốn** thấy trong bài đăng của Mộc An không?

**Anh Tuấn:** *"Ghét mấy từ 'sang trọng đẳng cấp', 'khẳng định vị thế'. Nghe giả."*

*…10 câu, khoảng 25 phút…*

Kết quả: `Brand Voice — Giọng Thương Hiệu.md` có 12 từ nên dùng (*bền, đúng hẹn, làm được, gỗ thật, thợ cả*), 14 từ cấm (*đẳng cấp, sang trọng, hàng đầu, uy tín số 1*), và 5 câu mẫu lấy từ chính lời anh Tuấn.

> Từ đây, mọi bài viết Claude tạo ra đều đọc file này trước. Anh không phải nhắc lại "đừng viết sáo rỗng" nữa.

---

## TUẦN 2 — Nghiên cứu, và một phát hiện khó chịu

```
/mkt-phan-tich-doi-thu
```

**Anh Tuấn** đưa tên 4 xưởng ở Hà Nội hay bị khách so sánh.

Claude phân tích từng bên bằng dữ liệu công khai — website, fanpage, đánh giá Google, bài đăng, và chấm điểm offer.

### Kết quả làm anh Tuấn khó chịu

> **Điểm chung của cả 4 đối thủ:** đều nói "thi công trọn gói, chất lượng cao, giá tốt".
> **Không ai** trong 4 bên có bảng giá công khai.
> **Không ai** nói về giới hạn kỹ thuật của mình.
>
> **Hàm ý:** Giá trị cốt lõi GT1 mà anh nêu ở Ngày 1 — *nói thật về giới hạn* — thật sự là điểm khác biệt, chưa ai chiếm. Nhưng hiện tại **không có chỗ nào trên fanpage hay website của Mộc An thể hiện điều đó**. Anh đang có một lợi thế mà không ai nhìn thấy.

Rồi Claude ghi vào `04. Resources/Market & Competitor Research/Đối Thủ/` — 4 file, mỗi đối thủ một file.

```
/customer-persona
```

Claude dựng 3 chân dung, và thêm một **chân dung ngược**:

> **Khách KHÔNG phù hợp với Mộc An:** người mua theo giá, so 5 chỗ rồi chọn rẻ nhất, đổi ý nhiều lần trong quá trình làm.
>
> **Dấu hiệu nhận ra sớm:** câu hỏi đầu tiên là "bao nhiêu tiền một mét", không hỏi gì về vật liệu hay quy trình.

**Anh Tuấn:** *"Đúng y. Mấy đơn lỗ toàn kiểu đấy."*

---

## TUẦN 3 — Chỗ đau nhất: giá

```
/breakeven-analysis
```

> Để tính điểm hoà vốn, tôi cần bốn con số:
> 1. Chi phí cố định mỗi tháng (mặt bằng, lương cứng, máy móc, điện)
> 2. Giá vốn trung bình trên một đơn
> 3. Giá bán trung bình một đơn
> 4. Số đơn trung bình mỗi tháng

**Anh Tuấn** lấy sổ ra, mất 40 phút mới gom đủ.

### Phát hiện

> Với chi phí cố định 180 triệu/tháng và biên gộp trung bình 35%, anh cần **doanh thu 515 triệu/tháng** mới hoà vốn.
>
> Tháng thấp của anh là 400 triệu. **Những tháng đó anh đang lỗ khoảng 40 triệu**, không phải "hơi ít việc".
>
> Ngoài ra: biên gộp 35% là con số trung bình. Anh có tính riêng biên cho từng loại đơn chưa?

**Anh Tuấn:** *"Chưa. Cứ nghĩ đơn to thì lãi to."*

Chạy `/cost-analysis` trên 12 đơn gần nhất:

| Loại đơn | Số đơn | Giá trung bình | Biên gộp thật |
|---|---|---|---|
| Nhà ở trọn gói | 5 | 210 triệu | **22%** |
| Chung cư từng phần | 4 | 65 triệu | **41%** |
| Quán cà phê | 3 | 95 triệu | **47%** |

> Nhóm chiếm 75% doanh thu (nhà ở trọn gói) lại là nhóm **biên thấp nhất**. Nhóm anh nói "dễ làm hơn" ở Ngày 1 (quán cà phê) là nhóm **lãi nhất**.
>
> Đây là thứ dữ liệu chỉ ra, không phải cảm nhận.

### Quyết định

```
/thiet-ke-offer
```

Claude giúp đóng gói lại thành ba gói có phạm vi rõ, giá rõ, và điều kiện nhận đơn rõ. Kèm điều khoản: **quá 2 lần đổi thiết kế thì tính phí**.

Ghi vào `Decisions/2026-08-20 — Cơ cấu lại 3 gói sản phẩm và điều kiện nhận đơn.md`.

---

## TUẦN 4 — Kéo đội vào

Anh Tuấn họp 60 phút, đọc `Chân Dung Doanh Nghiệp` và `Brand Voice` cho cả đội nghe.

**Chị Hà (marketing):** *"Vậy là từ giờ em không được viết 'sang trọng đẳng cấp' nữa ạ?"*
**Anh Tuấn:** *"Không. Ghét lắm."*
**Chị Hà:** *"Em cũng ghét, nhưng em tưởng anh thích."*

> Buổi họp này thường lộ ra vài hiểu lầm đã tồn tại nhiều năm. Đó là giá trị của việc viết ra thay vì để trong đầu.

Chốt phân vai, ghi vào `Decisions/`:

| Vai | Ai | Bước phụ trách |
|---|---|---|
| Chủ DN | Tuấn | 01 · 02 · 03 · 04 · 12 · duyệt giá và ngân sách |
| Marketing | Hà | 06 · 11 |
| Sale kiêm inbox | Linh | 05 · 08 |
| Vận hành sản xuất | Bình | 09 · 10 |

Tài khoản Claude: **anh Tuấn và chị Hà**. Linh, Bình, Mai chỉ dùng Obsidian.

---

## TUẦN 5 — Chị Hà tự chạy

Chị Hà gõ:

```
/content-pillar-builder
```

Claude đọc `Chân Dung Doanh Nghiệp`, `Brand Voice`, 3 chân dung khách, và hồ sơ đối thủ — **không hỏi lại chị Hà bất kỳ thông tin nền nào**. Nó chỉ hỏi:

> Anh chị muốn nội dung phục vụ mục tiêu nào trong 3 tháng tới: tăng số người hỏi giá, tăng chất lượng người hỏi giá, hay tăng độ nhận diện?

**Chị Hà:** *"Tăng chất lượng. Giờ hỏi giá nhiều mà toàn khách hỏi xong biến."*

Claude dựng 4 trụ cột, trụ cột số 1 là **"Nói thật về giới hạn"** — đúng cái điểm khác biệt phát hiện ở Tuần 2:

| Trụ cột | Tỷ trọng | Mục đích |
|---|---|---|
| Nói thật về giới hạn kỹ thuật | 30% | Sàng lọc khách sai từ đầu |
| Hậu trường xưởng, thợ cả làm việc | 30% | Tạo tin |
| Bóc giá — vì sao đắt, vì sao rẻ | 25% | Chuẩn bị tâm lý giá |
| Công trình đã bàn giao | 15% | Bằng chứng |

Rồi `/content-plan-builder` ra lịch 30 ngày. Chị Hà viết bài đầu bằng `/content-copywriter`.

**Bài đầu tiên đăng:** *"Ba loại tủ bếp Mộc An không nhận làm — và lý do"*.

Kết quả sau 1 tuần: ít lượt thích hơn bài cũ, nhưng **6 người inbox, cả 6 đều hỏi về vật liệu chứ không hỏi "bao nhiêu tiền một mét"**.

---

## TUẦN 6 — Sale: chỗ thay đổi rõ nhất

Vấn đề của Linh: inbox về nhiều, em trả lời tuỳ hứng, khách hỏi giá là em xin số điện thoại — và mất khách.

Anh Tuấn chạy:

```
/chot-don-qua-inbox
```

Claude đọc hồ sơ sản phẩm, giá, brand voice, rồi ra kịch bản. Một đoạn:

> **Luật số một: trả lời trước, xin thông tin sau.**
>
> ```
> Khách: "Tủ bếp bao nhiêu tiền shop?"
>
> SAI:   "Chị để lại sđt em tư vấn ạ"
> ĐÚNG:  "Dạ tủ bếp gỗ công nghiệp nhà em từ 4,5 triệu/mét dài,
>         gỗ tự nhiên từ 8,5 triệu/mét ạ.
>         Bếp nhà chị dài khoảng bao nhiêu mét để em tính giúp ạ?"
> ```

Rồi:

```
/phan-bo-va-cham-diem-lead
```

Claude dựng bảng chấm 2 trục và **8 trạng thái pipeline**. Anh Tuấn chốt luật: lead nóng phải chạm trong 15 phút, lead giữ quá 14 ngày trả về.

Linh mở `03. Areas/Sales Pipeline & CRM/[Mẫu] Pipeline Tháng.md`, copy ra, bắt đầu điền.

### Sau 2 tuần dùng pipeline

**Anh Tuấn:** *"Linh, tháng này bao nhiêu khách hỏi mà mình không trả lời trong ngày?"*
**Linh:** *(mở pipeline)* *"Bảy ạ. Toàn khách nhắn sau 9 giờ tối."*
**Anh Tuấn:** *"Bảy khách. Trung bình đơn 65 triệu. Mình đang bỏ rơi 450 triệu vì không ai trực buổi tối."*

Trước khi có pipeline, con số này **không tồn tại** — không ai biết nó.

Quyết định ghi vào `Decisions/`: đặt tin nhắn tự động hẹn giờ trả lời, Linh trực thêm 30 phút buổi tối, có phụ cấp.

---

## TUẦN 8 — Buổi họp tuần đầu tiên có số

45 phút, nghị trình cố định.

**Phút 0–10 — Hà ghi số vào `Analytics & Reporting/`**

| Chỉ số | Tuần này | Tuần trước |
|---|---|---|
| Inbox mới | 34 | 28 |
| Trả lời dưới 5 phút | 21 (62%) | 11 (39%) |
| Được báo giá | 19 | 14 |
| Chốt | 4 | 3 |
| Doanh thu | 268 triệu | 195 triệu |

**Phút 10–20 — chạy `/mkt-marketing-performance-analysis`**

> Tỷ lệ chốt trên số được báo giá là 21%, tăng từ 21% tuần trước — **không đổi**.
> Doanh thu tăng chủ yếu do **số inbox tăng** và **tốc độ phản hồi cải thiện**, không phải do bán giỏi hơn.
>
> Điểm nghẽn hiện tại nằm ở khúc **báo giá → chốt**: 15 người nhận báo giá rồi không quay lại. Tôi đề xuất kiểm tra ba giả thuyết:
> 1. Giá cao hơn kỳ vọng của nhóm khách đang tới
> 2. Báo giá chưa đủ rõ để khách so sánh
> 3. Không có ai theo đuôi sau khi báo giá

**Phút 20–35 — bàn**

**Linh:** *"Cái số 3 đúng ạ. Em báo giá xong là thôi, đợi khách nhắn lại."*

**Phút 35–42 — chạy skill được yêu cầu**

Anh Tuấn gõ `/chot-don-qua-zalo`. Claude ra **nhịp nhắc lại 3 lần**: sau 1 ngày bổ sung thông tin có ích, sau 3 ngày gửi ảnh công trình tương tự, sau 7 ngày chốt mềm và cho đường lui.

**Phút 42–45 — chốt việc**

Linh áp nhịp nhắc lại cho 15 khách đang treo. Hà viết 2 bài trụ cột "Bóc giá". Bình dựng SOP khảo sát tại nhà.

---

## THÁNG 3 — Trạng thái

| Trước | Sau |
|---|---|
| Đơn về không đều, không biết vì sao | Biết đúng khúc rơi: báo giá → chốt |
| Anh Tuấn tự chốt mọi đơn trên 50 triệu | Linh chốt được tới 120 triệu theo bảng giá đã duyệt |
| Mỗi người báo giá một kiểu | Ba gói, giá rõ, điều kiện nhận đơn rõ |
| Quảng cáo 15 triệu/tháng không biết lãi hay lỗ | Biết chi phí trên mỗi khách mới và ngưỡng dừng |
| Tháng thấp 400 triệu — tưởng "ít việc" | Biết đó là **lỗ 40 triệu**, và đã đặt sàn nhận đơn |

**Điều anh Tuấn nói ở buổi nghiệm thu:**

> *"Cái tôi được không phải là mấy cái file. Là lần đầu tiên tôi hỏi 'tháng này sao thế' mà đội trả lời được bằng số chứ không phải bằng cảm giác."*

---

## Đánh giá thẳng: khung này đủ A–Z chưa?

### Chỗ chạy trơn

**Luồng hỏi đáp thật sự hoạt động.** CEO không cần biết Business Model Canvas là gì, không cần biết cách tính điểm hoà vốn. Anh chỉ cần **trả lời trung thực về doanh nghiệp mình**. Cấu trúc, khung phân tích, cách trình bày — skill lo hết.

**Ngữ cảnh chỉ khai báo một lần.** Sau Ngày 1–2, chị Hà chạy skill content mà không phải nhập lại thông tin gì về công ty. Đây là điểm khác biệt lớn nhất so với dùng ChatGPT rời rạc — ở đó mỗi lần lại phải kể lại từ đầu.

**Cổng "Xong" chặn được lỗi nhảy cóc.** Anh Tuấn ban đầu muốn làm content ngay tuần 1. Cổng Bước 02 buộc anh chốt định vị trước — và chính nhờ đó trụ cột nội dung số 1 mới ra được đúng điểm khác biệt.

**Dữ liệu chảy thành vòng.** Nghiên cứu Tuần 2 → trụ cột nội dung Tuần 5 → số liệu Tuần 8 → quyết định. Mỗi vòng hệ thống biết nhiều hơn về chính doanh nghiệp.

### Chỗ vẫn khó — nói thật

**1. Bước 04 đòi số liệu mà nhiều doanh nghiệp không có sẵn.** Anh Tuấn mất 40 phút lục sổ để có bốn con số cho điểm hoà vốn. Doanh nghiệp không ghi chép gì sẽ tắc ở đây. **Cách gỡ:** ước lượng thô trước, ghi rõ là ước lượng, rồi chỉnh dần khi có dữ liệu thật — đừng dừng cả quá trình vì thiếu số.

**2. Ba tuần đầu là công việc một mình, và nó chán.** Không có kết quả nhìn thấy được, không có gì để khoe. Đây là chỗ phần lớn người bỏ cuộc. **Cách gỡ:** chia nhỏ, mỗi buổi 60–90 phút, và mở bài mẫu ra xem để biết đích đến trông thế nào.

**3. Kỷ luật ghi chép là điểm yếu nhất.** Hệ thống chỉ thông minh bằng đúng dữ liệu được đưa vào. Tuần nào Linh quên cập nhật pipeline thì tuần đó buổi họp không có gì để bàn. **Không có cách nào tự động hoá chỗ này** — nó là thói quen, không phải công nghệ.

**4. CEO vẫn phải quyết.** AI chỉ ra được ba giả thuyết cho việc khách không quay lại, nhưng chọn giả thuyết nào để thử là quyết định kinh doanh. Hệ thống **rút ngắn khoảng cách từ câu hỏi tới dữ liệu**, không thay người ra quyết định.

### Trả lời câu hỏi gốc

> *CEO chỉ cần hỏi đáp cùng team là ra được toàn bộ quy trình vận hành — đúng hay sai?*

**Đúng, với một điều kiện.** Hỏi đáp là đủ để **dựng ra** toàn bộ quy trình — 12 bước, mọi tài liệu, mọi kịch bản đều sinh ra từ đối thoại, không cần ai biết lý thuyết quản trị.

Nhưng hỏi đáp **không đủ để vận hành**. Vận hành cần ba thứ mà không đối thoại nào thay được: **ghi chép hằng ngày**, **họp tuần đều đặn**, và **CEO chịu ngồi ba tuần đầu**.

Có đủ ba thứ đó thì đây là một hệ điều hành. Thiếu một trong ba thì nó quay về thành một thư mục chứa tài liệu đẹp.

---

→ Bắt đầu: [[01 — Đi Theo Thứ Tự Nào]] · Phân vai đội: [[02 — Team Nhỏ Vận Hành Thế Nào]] · Kiến trúc: [[03 — Cẩm Nang Kiến Trúc Toàn Hệ Thống]]
