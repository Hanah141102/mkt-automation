---
updated: 2026-08-03
status: draft
owner: An
---
> [!warning] ĐÂY LÀ BÀI MẪU — DỮ LIỆU HƯ CẤU
> Toàn bộ tên công ty, tên người, tên miền, số tiền và số liệu trong tài liệu này **đã được thay bằng dữ liệu ví dụ**. Không dùng các con số ở đây làm căn cứ kinh doanh. Giá trị của bộ tài liệu này nằm ở **cấu trúc và cách lập luận**, không nằm ở số liệu.


# 36 — Onboarding 4 bước & Cơ chế lương thưởng KPI

> Dùng cho **một buổi họp 90 phút** đưa cả team vào hệ thống tài liệu. Nguyên tắc: không thuyết trình quá 10 phút liên tục — mỗi bước kết bằng một việc người học **tự làm được ngay tại chỗ**.
>
> Tài liệu này **không thay** [[05-organization-roles-raci]]. RACI vẫn là nguồn chuẩn về vai trò; file này chỉ là cách dạy team dùng nó.

---

## Phần 0 — Chuẩn bị (An làm, trước họp 24h)

| Việc | Chi tiết |
|---|---|
| Gửi 1 link duy nhất | `00-Governance/00-huong-dan-nhanh-cho-doi.md` — yêu cầu đọc trước, 5 phút |
| Kiểm tra máy | Mỗi người đã cài GitHub Desktop, đã Clone repo, đã Fetch thành công |
| Chuẩn bị 6 câu hỏi | Mỗi người 1 câu, dùng ở Bước 1 (xem mục 1.3) |
| In/mở sẵn | Bảng RACI mục 4 và bảng Handoff mục 5 của `05-organization-roles-raci.md` |

**Luật của buổi họp:** ai chưa Fetch được repo thì xử lý trước khi vào — không dừng buổi họp để cài phần mềm.

---

## BƯỚC 1 — Hiểu dự án có những gì (20 phút)

**Mục tiêu ra khỏi bước này:** mỗi người biết *đi tìm* thông tin, không cần *nhớ* thông tin.

### 1.1 Nói một câu về logic của hệ thống (5 phút)

Không đọc từng file. Chỉ nói đúng chuỗi này và chỉ tay vào 9 folder:

```text
Governance → Strategy/Brand → Research → Offer/Funnel → Growth/Content
→ People → Training → Measurement → Campaign → (Retro quay lại đầu)
```

Một câu chốt: **"Mỗi folder trả lời đúng một câu hỏi. Việc của bạn là biết câu hỏi của mình thuộc folder nào."**

### 1.2 Ba luật cứng — viết lên bảng (5 phút)

| Luật | Vì sao |
|---|---|
| **Luôn Fetch trước khi làm** | Tránh sửa trên bản cũ rồi bị đè mất |
| **Không lấy file trong `99-Archive` ra làm theo** | Đã bị thay thế, làm theo là làm sai |
| **Không sửa `00-Governance` và `01-Strategy-Brand`** (trừ An) | Tài liệu nguồn — sai một chỗ, nhiều file trích theo sẽ sai theo |

### 1.3 Bài tập tại chỗ: "60 giây tìm đúng folder" (10 phút)

Đọc to từng câu hỏi, người được gọi tên phải **mở đúng file trên màn hình** trong 60 giây:

| # | Câu hỏi | Đáp án đúng |
|:--:|---|---|
| 1 | Học Viện AI Demo định vị là ai, không phải ai? | `01-Strategy-Brand/02-brand-bible.md` |
| 2 | Khách hàng mục tiêu đau ở đâu? | `02-Research-Insights/07-customer-persona-insight.md` |
| 3 | Chúng ta đang bán gói nào, giá nào? | `03-Offer-Funnel/08-product-offer-map.md` |
| 4 | Tháng này đăng bài gì, ngày nào? | `04-Growth-Content/14-content-calendar-production.md` |
| 5 | Việc này ai duyệt, ai chỉ được thông báo? | `05-People-Operations/05-organization-roles-raci.md` |
| 6 | Tuần này số nào là số sống còn? | `07-Measurement/15-kpi-dashboard-reporting.md` |

> Ai tìm sai không sao — điều cần rút ra là **luôn quay về `00-index.md`** rồi lần theo bảng, đừng đoán theo trí nhớ.

### 1.4 Nói rõ ba thứ team đang nhầm lẫn

Đây là ba khái niệm mới, giải thích một lần cho dứt điểm:

| Khái niệm | Nó là gì | Nó KHÔNG phải là gì |
|---|---|---|
| **File nghiên cứu** (`02-Research-Insights`) | Bằng chứng để ra quyết định. Đọc để lấy *insight*, trích *nguồn*. | Không phải task list. Đọc xong không tự sinh ra việc. |
| **Catalog list** | Bảng liệt kê **tài sản đã có** (bài viết, video, creative, ad, landing) kèm ID, ngày, kết quả — để tái sử dụng thay vì làm lại từ đầu. | Không phải lịch đăng. Catalog nhìn về *quá khứ*; calendar nhìn về *tương lai*. |
| **Dashboard (artifact)** | Trang số liệu sống, mở ra là thấy hiện trạng. Dùng để **ra quyết định trong họp**. | Không phải báo cáo. Dashboard hiện số; báo cáo phải kết bằng *nhận định → hành động → người → deadline*. |

---

## BƯỚC 2 — Hiểu việc cụ thể của mình (25 phút)

**Mục tiêu ra khỏi bước này:** mỗi người tự phát biểu được JD của mình bằng miệng, không nhìn giấy.

### 2.1 Đọc thầm JD của chính mình (7 phút)

Mở `05-organization-roles-raci.md` → mục 3 → phần tên mình. Mỗi người tự trả lời 3 câu ra giấy:

1. **Mục đích vị trí của tôi là gì?** (một câu)
2. **Ba việc tôi là `R` — tức tôi chịu trách nhiệm hoàn thành?**
3. **Ba việc tôi KHÔNG được làm?**

### 2.2 Vòng phát biểu — mỗi người 2 phút (12 phút)

Nói theo đúng khuôn: *"Tôi là R của ___. Tôi được tự quyết ___. Tôi không làm ___. Việc tôi hay bị hiểu nhầm là ___."*

An chỉ can thiệp khi nghe thấy **chồng vai**. Bốn ranh giới hay bị vi phạm nhất:

| Ranh giới | Câu nhắc |
|---|---|
| Hà ≠ Content Planner | Hà **hỗ trợ vận hành kênh**, không sở hữu content plan |
| Anh Thư không setup ads | Anh Thư đưa message/copy; Nguyệt sở hữu ads |
| Duy không tự đổi kịch bản | Sai brief thì **trả lại brief**, không tự sửa claim/CTA |
| Bảo & Chi không mặc định trực workshop miễn phí | Chỉ vào khi có phân ca rõ |

### 2.3 Chốt "một việc R quan trọng nhất tuần này" (6 phút)

Mỗi người ghi **đúng một dòng** vào Checklist công việc hằng ngày (Google Sheet ở `35-checklist-cong-viec-hang-ngay.md`):

> Việc: ___ · Xong nghĩa là gì (bằng số): ___ · Deadline: ___

Không đo được bằng số thì viết lại cho đến khi đo được.

---

## BƯỚC 3 — Hiểu cách phối hợp với nhau (20 phút)

**Mục tiêu ra khỏi bước này:** không ai còn hỏi "cái này của ai?" và "gửi cho nhau thì gửi cái gì?".

### 3.1 Dạy đúng một khái niệm: R–A–C–I (5 phút)

| Chữ | Nghĩa | Câu kiểm tra |
|:--:|---|---|
| **R** | Làm và chịu trách nhiệm xong | "Việc trễ thì hỏi ai?" |
| **A** | Duyệt, chịu trách nhiệm cuối | "Ai nói được câu cuối cùng?" |
| **C** | Được hỏi ý trước khi làm | "Không hỏi người này thì làm sai?" |
| **I** | Chỉ cần biết kết quả | "Người này chỉ cần nhận thông báo" |

**Một luật:** mỗi việc **đúng một R**. Hai R = không ai chịu trách nhiệm.

### 3.2 Diễn thử một chuỗi handoff thật (10 phút)

Lấy chuỗi phổ biến nhất, đi từng chặng, hỏi thẳng người liên quan *"anh/chị nhận được gì, trong bao lâu?"*:

```text
An ──big idea, offer, proof, điều cấm──▶ Anh Thư   (trước khi lập plan)
Anh Thư ──hook, script, reference, format, deadline, CTA──▶ Duy   (≥24h trước edit)
Duy ──preview + tên version──▶ Anh Thư   (trước SLA publish)
Anh Thư ──caption final, kênh, giờ, link/UTM, pin comment──▶ Hà   (≥4h trước đăng)
Hà ──comment quality, inbox, show-up log──▶ Nguyệt   (cuối ngày)
Nguyệt ──winner/loser + lý do + hành động──▶ Team   (hằng ngày khi campaign live)
```

**Luật giao việc:** thiếu bất kỳ món nào trong gói bàn giao → **người nhận có quyền trả lại**, không bắt đầu làm. Trả lại không phải là gây khó, mà là chặn lỗi từ đầu nguồn.

### 3.3 Escalation — khi nào được làm phiền An (5 phút)

| Tình huống | Xử đầu | Lên An khi |
|---|---|---|
| Content sai format | Anh Thư | Không cần |
| Claim / giá / chính sách | Anh Thư | **Ngay** |
| Ads vượt ngưỡng ngân sách | Nguyệt | **Trước** khi tăng |
| Sự cố Zoom | Hà | Sau 60 giây không xử được |
| Lead hỏi Solution / điều kiện riêng | Hà | Chuyển ngay |
| Lỗi kỹ thuật lớp chuyên sâu | Bảo / Chi | Sau 15 phút, hoặc khi ảnh hưởng nhiều học viên |

### 3.4 Nhịp họp cố định — đọc to, không thảo luận

- **Daily campaign** — 15 phút: chỉ việc chặn, việc tắc, quyết định hôm nay.
- **Weekly growth** — 45 phút: đọc số + research + chọn **một** test.
- **Sau mỗi Zoom** — báo cáo 5 dòng trước khi hết ngày.
- **Sau mỗi campaign** — retro trong 48 giờ.

---

## BƯỚC 4 — Cơ chế lương thưởng KPI (25 phút)

**Mục tiêu ra khỏi bước này:** team hiểu tiền thưởng đến từ đâu, và An chốt được mô hình áp dụng.

Trình bày 3 mô hình ở Phần II, hỏi phản ứng, rồi chốt. **Không chốt được con số trong buổi này cũng được** — nhưng phải chốt được *mô hình* và *ngày công bố số*.

---

## Sau họp — 3 việc trong 48 giờ

| # | Việc | Người | Hạn |
|:--:|---|---|---|
| 1 | Fetch → mở đúng file JD của mình → Commit 1 dòng xác nhận đã đọc vào checklist | Cả team | 24h |
| 2 | Ghi "một việc R quan trọng nhất tuần" vào Google Sheet checklist | Cả team | 24h |
| 3 | Công bố bảng KPI + cơ chế thưởng bản chính thức | An | 48h |

**Cách kiểm tra buổi họp có hiệu quả:** tuần kế tiếp, đếm số lần có người hỏi *"cái này ai làm?"*. Bằng 0 là đạt.

---

# PHẦN II — Lương thưởng KPI: hiểu trước, xây sau

> Đây là **phương pháp**. Bản áp dụng thực tế cho từng người (con số, mốc, đơn giá) nằm ở [[37-co-che-luong-thuong-tung-vi-tri]].

## 1. Hiểu bức tranh trong 2 phút

Thu nhập của một người gồm **hai phần**:

| Phần | Trả cho cái gì | Đặc điểm |
|---|---|---|
| **Lương cứng** | Có mặt, làm đúng vai, đúng chuẩn | Tháng nào cũng như tháng nào |
| **Thưởng KPI** | **Kết quả** làm ra | Làm tốt thì nhiều, làm kém thì ít hoặc không có |

Toàn bộ chuyện "cơ chế lương thưởng KPI" chỉ là trả lời **đúng một câu hỏi**:

> ### Phần thưởng này trả theo cái gì?

Có 3 câu trả lời phổ biến — và đó chính là 3 cách bên dưới:

| Cách | Thưởng trả theo | Ví dụ đời thường |
|---|---|---|
| **1. Chấm điểm** | **Điểm** của cá nhân trên vài tiêu chí | Học sinh: điểm trung bình nhiều môn |
| **2. Ăn theo kết quả** | **Một con số** cá nhân đó làm ra | Tài xế: ăn theo cuốc xe |
| **3. Thưởng đội** | Kết quả **chung** của cả team | Cả quán đạt doanh số thì chia thưởng |

Ba cách này **không loại trừ nhau**. Một công ty có thể dùng cách 1 cho người này, cách 2 cho người kia, rồi phủ cách 3 lên tất cả.

---

## 2. Cách 1 — Chấm điểm (KPI Scorecard)

**Một câu:** coi mỗi người như học sinh có vài môn học, mỗi môn một hệ số. Cuối tháng cộng điểm, điểm cao thì thưởng nhiều.

### Làm từng bước

1. Chọn **3–4 việc quan trọng nhất** của vị trí đó → đây là các "môn học".
2. Cho mỗi môn một **trọng số** (%), cộng lại đúng 100%.
3. Cuối tháng, mỗi môn chấm: *đạt bao nhiêu % so với mục tiêu?*
4. Lấy **trọng số × % đạt** = điểm của môn đó.
5. Cộng tất cả → điểm tổng trên 100 → nhân với quỹ thưởng = **tiền**.

### Ví dụ: Anh Thư, quỹ thưởng tháng 3.000.000đ `[GIẢ ĐỊNH]`

| Môn (KPI) | Trọng số | Mục tiêu | Thực tế | % đạt | Điểm |
|---|:--:|---|---|:--:|:--:|
| Data mới từ organic | 40 | 800 | 720 | 90% | 40 × 0,90 = **36** |
| Bài đạt chuẩn Scale | 30 | 4 bài | 5 bài | 125% → tính 120% | 30 × 1,20 = **36** |
| Giao brief đúng hạn cho Duy/Hà | 20 | 100% | 90% | 90% | 20 × 0,90 = **18** |
| Cập nhật objection bank | 10 | 4 lần | 4 lần | 100% | 10 × 1,00 = **10** |
| | **100** | | | | **Tổng 100** |

→ Thưởng = **100/100 × 3.000.000 = 3.000.000đ**

Nếu Anh Thư chỉ được 82 điểm → thưởng = 82/100 × 3.000.000 = **2.460.000đ**.

### Hai cái van an toàn (bắt buộc phải có)

| Van | Luật | Vì sao cần |
|---|---|---|
| **Trần 120%** | Một môn dù vượt bao nhiêu cũng chỉ tính tối đa 120% | Không có van này, người ta dồn hết sức vào 1 môn dễ ăn điểm rồi bỏ mặc 3 môn còn lại |
| **Sàn 70 điểm** | Dưới 70 điểm → thưởng = 0 | Thưởng phải là phần thưởng, không phải khoản mặc định ai cũng có |

### Khi nào dùng cách này

Khi việc của người đó **quan trọng nhưng không ra tiền trực tiếp** — chất lượng và đúng hạn mới là thứ cần đo.

| Ưu | Nhược |
|---|---|
| Áp được cho **mọi vị trí** | Tốn công chấm mỗi tháng |
| Minh bạch, người ta tự tính được thưởng của mình | Người ta chỉ làm những gì được chấm điểm |
| Ép công ty phải có hệ đo | Số liệu bẩn thì cả cơ chế mất uy tín |

---

## 3. Cách 2 — Ăn theo kết quả (Hoa hồng bậc thang)

**Một câu:** không chấm điểm gì cả — chỉ nhìn **một con số đầu ra**. Con số đó tốt tới đâu, thưởng tới đó.

### Làm từng bước

1. Chọn **đúng một con số** mà người đó tự tay tạo ra.
2. Chia thành **các bậc**: chưa đạt → đạt → tốt → xuất sắc.
3. Mỗi bậc gắn một mức tiền, bậc càng cao tỷ lệ càng tăng.
4. **Mỗi bậc phải có 2 điều kiện** — một về *số lượng*, một về *chất lượng*.

### Ví dụ minh hoạ cách chia bậc `[GIẢ ĐỊNH — không phải cơ chế đang áp cho Nguyệt]`

| Bậc | Điều kiện 1 (số lượng) | Điều kiện 2 (chất lượng) | Hoa hồng |
|---|---|---|---|
| Chưa đạt | CPL > 50.000đ | — | **0** |
| Đạt | CPL ≤ 50.000đ | ≥80% target lead tháng | **100%** quỹ |
| Tốt | CPL ≤ 30.000đ | đủ 100% target lead | **130%** |
| Xuất sắc | CPL ≤ 30.000đ | lead → workshop attended ≥30% | **160%** |

### Vì sao bắt buộc phải có 2 điều kiện

Nếu chỉ thưởng theo "lead rẻ", người chạy ads sẽ kéo về **thật nhiều lead rẻ nhưng sai tệp** — đúng kỹ thuật, sai kết quả. Điều kiện thứ hai chính là cái phanh.

Đây là lý do `15-kpi-dashboard-reporting.md` đã ghi sẵn: *"không đánh giá winner chỉ bằng CPL"*.

> **Cơ chế thật của Nguyệt đã đi xa hơn bảng này.** Thay vì bậc thang hai điều kiện, file 37 gộp cả số lượng và chất lượng vào **một công thức duy nhất**: đếm *lead thực sự vào Zoom* thay vì đếm lead. Khi làm được vậy thì không cần bậc, không cần điều kiện phụ — chất lượng đã nằm trong chính đơn vị đo. Đó là dạng tốt nhất của Cách 2, nhưng chỉ dựng được khi có tracking nối tới bước sau. Bảng bậc thang ở trên vẫn hữu ích khi chưa nối được.

### Khi nào dùng cách này

Khi người đó **tự tay tạo ra một con số ra tiền** và **tự tác động được** vào con số đó.

| Ưu | Nhược |
|---|---|
| Động lực rất mạnh | Chỉ áp được cho vài vị trí |
| Chi phí tự cân bằng theo kết quả | Dễ sinh hành vi ăn xổi nếu thiếu điều kiện chất lượng |
| Ít cần giám sát | **Bắt buộc phải có tracking sạch** |

> ⚠️ Hiện Học Viện AI Demo **chưa nối được** `source → lead → attendance → buyer`. Áp cách này bây giờ sẽ dẫn đến cãi nhau về số liệu chứ không phải về công việc.

---

## 4. Cách 3 — Thưởng đội (OKR / Team Bonus)

**Một câu:** đặt vài mục tiêu chung cho cả công ty theo quý. Cả team đạt thì cả team có thưởng, không đạt thì không ai có.

### Ví dụ: quý T8–T10 `[GIẢ ĐỊNH]`

| Mốc | Điều kiện | Thưởng |
|---|---|---|
| Mốc 1 | Đạt mục tiêu T8 (700tr) | Trích x% phần vượt chia cho team |
| Mốc 2 | Đạt lũy kế cả quý (700 + 1.000 + 1.300 = 3.000tr) | Trích x% + 1 tháng lương thứ 13 |
| **Mốc chặn cửa** | Lead gắn đúng tag = 100% **và** có ≥3 case study | **Không đạt mốc này thì không mở quỹ, dù doanh thu đạt** |

Chia theo hệ số đóng góp: Trưởng khối ×1,5 · Nhân sự chính thức ×1,0 · Hỗ trợ theo ca ×0,5 `[GIẢ ĐỊNH]`

### Khi nào dùng

Khi cần cả team **nhìn chung một số** và ngừng đổ lỗi chéo. Không nên dùng một mình.

| Ưu | Nhược |
|---|---|
| Giảm bệnh "việc của tôi xong rồi" | Người giỏi và người kém nhận gần bằng nhau |
| Hợp giai đoạn cần phối hợp chặt | Quý mới thấy tiền → động lực hằng ngày yếu |
| Ít tốn công chấm | Dễ gây ấm ức nếu team không đạt vì lỗi một người |

---

## 5. Chọn cách nào cho vị trí nào — chỉ cần hỏi 1 câu

> ### "Người này có tự tay tạo ra một con số ra tiền không, và có tự tác động được vào con số đó không?"

| Trả lời | Dùng cách |
|---|---|
| **Có** — tự tay làm ra, tự tác động được | **Cách 2** (hoa hồng) |
| **Có ảnh hưởng nhưng gián tiếp**, hoặc chất lượng quan trọng hơn số lượng | **Cách 1** (chấm điểm) |
| **Không tách được** đóng góp riêng của người này | Dựa vào **Cách 3** (thưởng đội) |

### Áp cho 6 vị trí Học Viện AI Demo

> Bảng này khớp với bản chốt ở [[37-co-che-luong-thuong-tung-vi-tri]] (cập nhật 2026-08-03). Nếu hai bảng lệch nhau, **file 37 là bản đúng**.

| Vị trí | Tự tạo ra con số ra tiền? | → Cách |
|---|---|---|
| **Nguyệt** — Ads | Có. Chi tiền → ra lead → ra người vào Zoom | **Cách 1 + 2** — quỹ 4tr chấm điểm, cộng hoa hồng theo *lead có vào Zoom* |
| **Anh Thư** — Content & Social | Có ảnh hưởng lớn nhưng gián tiếp qua nhiều khâu | **Cách 1 + 2** — quỹ 4tr chấm điểm, cộng hoa hồng lead organic vượt mốc 700 |
| **Duy** — Video | Không. Duy làm ra *chất lượng*, không làm ra *lượt mua* | **Cách 1 + 2** — quỹ 4tr chấm điểm, cộng thưởng sản lượng vượt định mức 40 điểm |
| **Hà** — Trợ lý lớp & Trợ giảng | Có, ở phần chốt sale sau buổi | **Cách 1 + 2** — 2 cục thưởng cố định (quy trình 1,5tr + hài lòng 1tr/khóa), cộng hoa hồng sale 2%/3% |
| **Bảo** — Trợ giảng & Kỹ thuật học viên | Có, ở phần chốt sale và lead page | **Cách 2 chủ đạo** — thưởng hài lòng 1tr/khóa, hoa hồng sale, lead page, affiliate 5%. Tag lead ≥95% là **chặn cửa** |
| **Chi** — Kỹ thuật Genful | Có: user Genful ở lại, và mini app giao được | **Cách 2** — affiliate Genful 10% recurring + chia mini app 40/60 |
| **Cả team** | — | Phủ thêm **Cách 3** theo quý |

> **Điều thay đổi so với bản đầu:** không vị trí nào còn dùng thuần Cách 1. Lý do: quỹ chấm điểm đơn thuần tạo trần thu nhập, mà cả sáu vị trí đều có ít nhất một con số họ tự đẩy lên được. Cách 1 giờ chỉ dùng cho **phần sàn** — giữ chất lượng và quy trình; phần vượt luôn là Cách 2.

---

## 6. Sáu câu hỏi để xây KPI cho MỘT vị trí

Ngồi 1-1 với từng người, hỏi đúng 6 câu này **theo thứ tự**. Trả lời xong 6 câu là có KPI.

### Câu 1 — "Nếu người này nghỉ một tháng, cái gì hỏng đầu tiên?"

→ Câu trả lời chính là **KPI sống còn** của vị trí đó.

*Nguyệt nghỉ → không có lead từ ads → KPI sống còn là lead & CPL.*
*Duy nghỉ → creative không kịp giao → KPI sống còn là giao đúng hạn, đúng brief.*

> **Nếu câu trả lời là "chẳng hỏng gì rõ ràng"** → vị trí đó chưa rõ vai. Quay lại sửa JD trong `05-organization-roles-raci.md` trước, đừng sửa KPI.

### Câu 2 — "Con số đó lấy ở đâu ra? Ai là người mở file lấy số?"

→ Ra **nguồn dữ liệu** và **người chịu trách nhiệm lấy số**.

> **Luật cứng:** không chỉ ra được file hoặc màn hình cụ thể → **bỏ KPI đó**. Không đo được thì không thưởng được, và cuối tháng sẽ cãi nhau.

### Câu 3 — "Người này có tự làm con số đó tăng lên được không, hay phải chờ người khác?"

→ Kiểm tra **tính công bằng** của KPI.

*Bắt Duy chịu KPI "lượt xem video" là sai: Duy không chọn kênh, không chọn giờ đăng, không chạy ads. Duy chỉ tự quyết được chất lượng và tiến độ.*

> **Luật cứng:** người không tự tác động được thì không chịu KPI đó. KPI sai người sẽ giết động lực nhanh hơn là không có KPI.

### Câu 4 — "Nếu người này chỉ chăm chăm chạy con số đó, họ có thể phá cái gì?"

→ Ra **chỉ số chặn cửa** (chỉ số chất lượng).

| Nếu chỉ chạy... | Có thể phá... | Chỉ số chặn cửa |
|---|---|---|
| CPL rẻ | Chất lượng lead | Lead → workshop attended |
| Số bài đăng nhiều | Chất lượng nội dung | Số bài đạt chuẩn Scale |
| Video giao nhanh | Đúng brief | Tỷ lệ bị trả lại |
| Số lead nhiều | Dữ liệu sạch | Tỷ lệ gắn đúng tag |

> Đây là **câu quan trọng nhất** và cũng là câu hay bị bỏ qua nhất. Mọi cơ chế KPI hỏng đều hỏng ở đây.

### Câu 5 — "Hôm nay con số đó đang là bao nhiêu?"

→ Ra **baseline** — điểm xuất phát.

> **Luật cứng:** chưa biết baseline thì **đo 2–4 tuần rồi mới đặt mục tiêu**. Đặt mục tiêu khi chưa biết điểm xuất phát là đoán, và người bị áp sẽ biết ngay đó là đoán.

### Câu 6 — "Đạt thì được bao nhiêu tiền? Không đạt thì sao?"

→ Ra **cơ chế**. Phải nói được **bằng con số**.

Nói *"làm tốt công ty sẽ xem xét"* thì không phải cơ chế — đó là lời hứa, và lời hứa không tạo động lực.

---

## 7. Ví dụ điền đủ 6 câu — vị trí Nguyệt (Ads)

| Câu hỏi | Trả lời |
|---|---|
| **1.** Nghỉ 1 tháng thì hỏng gì? | Không có lead trả phí → hai phễu CEO và Builder đứng |
| **2.** KPI sống còn | **Số người từ Link B thực sự vào Zoom** trên mỗi đồng chi (chuẩn: 133.000đ/người vào phòng) |
| **3.** Số lấy ở đâu, ai lấy | Meta Ads Manager + Link B + Zoom log · Nguyệt tự lấy, Bảo đối chiếu |
| **4.** Tự tác động được? | Có — Nguyệt tự chọn tệp, ngân sách, creative test |
| **5.** Chạy theo số này phá gì? | Ít hơn hẳn so với đo CPL đơn thuần, vì chất lượng đã nằm trong công thức. Vẫn giữ **chặn cửa: attended ≥25%** làm sàn an toàn |
| **6.** Baseline hôm nay | `[CẦN BỔ SUNG]` — chưa nối được Link B → Zoom log ở mức từng người. Phải dựng trước, rồi đo 2 tuần |
| **7.** Cơ chế + tiền | Quỹ 4tr chấm điểm + hoa hồng `(attended thực tế − attended chuẩn) × 16.700đ`, không trần |

> **Vì sao đổi KPI sống còn của Nguyệt từ "CPL" sang "người vào Zoom":** Nguyệt nêu đúng một điểm — nếu mua lead đắt hơn nhưng tỉ lệ vào Zoom cao gấp đôi thì sao? Với công thức đo CPL, lead 45.000đ chốt gấp đôi vẫn ăn 0đ, tức cơ chế đang **phạt việc mua lead tốt**. Đổi đơn vị đếm sang "người thực sự vào phòng học" gỡ được đúng chỗ đó. Đây là ví dụ mẫu cho Câu 4 ở mục 6 — chỉ số nào cũng có mặt trái, và mặt trái của CPL là nó thưởng cho lead rẻ bất kể chất lượng.

---

## 8. Phiếu trống — copy và điền cho từng vị trí

```text
VỊ TRÍ: ______________     NGƯỜI: ______________

1. Nghỉ 1 tháng thì hỏng gì đầu tiên?
   →

2. KPI SỐNG CÒN (chỉ một):
   →

3. Số lấy ở file/màn hình nào? Ai lấy?
   →   (không trả lời được → bỏ KPI này)

4. Người này tự tác động được không?   [ ] Có   [ ] Không
   →   (Không → đổi KPI khác)

5. Chạy theo số này có thể phá gì?
   → CHỈ SỐ CHẶN CỬA:

6. Baseline hôm nay:            (chưa có → đo 2–4 tuần trước)
   Mục tiêu:

7. Cơ chế:   [ ] Cách 1 chấm điểm   [ ] Cách 2 hoa hồng   [ ] Cách 3 đội
   Đạt thì được:
   Không đạt thì:
```

---

## 9. Gợi ý câu trả lời mồi cho 6 vị trí

Đây là bản đã chốt cùng file 37. Vẫn giữ lại mục này để thấy **logic phía sau** từng lựa chọn.

| Vị trí | KPI sống còn | Chỉ số chặn cửa | Nguồn số |
|---|---|---|---|
| **Anh Thư** — Content & Social | Data organic mới qua **Link A** (mốc 700/tháng) | Zalo → workshop attended **≥25%** để lĩnh hoa hồng | Link A + Zoom log |
| **Nguyệt** — Ads | **Số người từ Link B thực sự vào Zoom** trên mỗi đồng chi | Lead ads → attended **≥25%** để lĩnh hoa hồng | Meta + Link B + Zoom log |
| **Duy** — Video | % creative giao đúng SLA và đúng brief | Tỷ lệ creative bị trả lại **>20%** → mất thưởng sản lượng | Bảng log sản xuất |
| **Hà** — Trợ lý lớp & Trợ giảng | Quy trình truyền thông trước–trong–sau đủ 13 bước | Quy trình ≥70% **và** hài lòng ≥7,0/10 → mới lĩnh hoa hồng sale | Checklist buổi + khảo sát cuối khóa |
| **Bảo** — Trợ giảng & Kỹ thuật học viên | Tỷ lệ lead gắn đúng tag = **100%** | Tag **<95%** → mất toàn bộ phần thưởng tháng đó | CRM |
| **Chi** — Kỹ thuật Genful | Tỷ lệ giữ chân user Genful (đo gián tiếp qua affiliate recurring) | SLA ticket ≥90% **và** first-contact ≥70% → mới lĩnh phần mini app | Ticket log + Genful |

**Ba điều đáng chú ý trong bảng này:**

1. **Chi không còn chịu KPI doanh thu Genful.** Đó là vị trí kỹ thuật. Cơ chế affiliate 10% recurring đã tự động gắn thu nhập của Chi với việc user ở lại — không cần thêm KPI doanh thu.
2. **Bảo không còn quỹ chấm điểm**, nên "tag lead 100%" được nâng thành **chặn cửa cho toàn bộ phần thưởng**. Đây là việc load-bearing: lương của Anh Thư, Nguyệt và Hà đều cần tag sạch mới tính được.
3. **Hà chấm theo *bước*, không theo *buổi*.** Thiếu một bước nhỏ mà mất trắng cả buổi thì quá nặng; chấm theo bước cho mỗi thiếu sót một cái giá đúng bằng sức nặng của nó.

> KPI nào chưa có baseline thì ghi `[CẦN BỔ SUNG]` — **không bịa số để có cái mà chấm**. Chấm điểm trên số bịa sẽ phá niềm tin vào cả cơ chế, và niềm tin đó rất khó lấy lại.

---

## 10. Năm lỗi hay gặp nhất

| Lỗi | Hậu quả | Cách sửa |
|---|---|---|
| Đặt 8–10 KPI cho một người | Không ai nhớ nổi, cuối tháng chấm lấy lệ | Tối đa 4, trong đó **đúng 1 cái sống còn** |
| KPI không có nguồn số rõ ràng | Cuối tháng cãi nhau về con số | Bỏ KPI đó, hoặc dựng tracking trước |
| Chỉ đo số lượng | Người ta chạy theo số, phá chất lượng | Luôn kèm **1 chỉ số chặn cửa** |
| Đặt mục tiêu khi chưa có baseline | Số trên trời, nhân sự mất niềm tin ngay tháng đầu | Đo 2–4 tuần trước |
| Áp tiền ngay tháng đầu tiên | Sai số một lần là cơ chế mất uy tín vĩnh viễn | **Tháng 1 chạy thử, chấm điểm nhưng không tính tiền** |

---

## 11. Lộ trình 4 tuần để chốt xong

| Tuần | Việc | Ai |
|:--:|---|---|
| **1** | Họp 1-1 từng người, hỏi 6 câu, điền phiếu ở mục 8 | An + từng người |
| **2** | Dựng nguồn số cho các KPI đang thiếu (ưu tiên: gắn tag lead) | Bảo + Nguyệt |
| **3–4** | Chạy thử: chấm điểm thật, cho mỗi người thấy bảng điểm của mình, **nhưng chưa tính tiền** | Cả team |
| **5** | Chốt tỷ lệ và con số, công bố chính thức, ghi vào Decision Log `00-source-of-truth.md` | An |

---

## 12. Việc An cần tự chốt (không ai chốt thay được)

| # | Cần chốt | Ghi chú |
|:--:|---|---|
| 1 | Tỷ lệ lương cứng / thưởng từng vị trí | Đang để `[GIẢ ĐỊNH]` 80/20 cho Cách 1, 65/35 cho Cách 2 |
| 2 | Quỹ thưởng tháng bằng tiền tuyệt đối | Đối chiếu quỹ lương thực tế |
| 3 | Baseline cho KPI đang `[CẦN BỔ SUNG]` | Đo 2–4 tuần rồi mới đặt target |
| 4 | Ngày bắt đầu áp dụng | Đề xuất: tháng 1 chạy thử không tính tiền |
| 5 | Có phủ Cách 3 (thưởng đội) theo quý không | Nếu có, chốt mốc chặn cửa là gì |

> **Nhớ một điều:** cơ chế thưởng chỉ tốt bằng chất lượng dữ liệu phía sau nó. `15-kpi-dashboard-reporting.md` đang ghi *"tỷ lệ lead được gắn đúng tag: chưa có"*. Sửa cái đó trước, rồi hãy công bố cơ chế tiền.
