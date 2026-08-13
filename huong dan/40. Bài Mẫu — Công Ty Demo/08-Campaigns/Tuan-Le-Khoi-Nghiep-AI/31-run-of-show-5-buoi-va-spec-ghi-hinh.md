---
updated: 2026-07-29
status: canonical
tags: [demo-ai, run-of-show, webinar, recording, evergreen]
---
> [!warning] ĐÂY LÀ BÀI MẪU — DỮ LIỆU HƯ CẤU
> Toàn bộ tên công ty, tên người, tên miền, số tiền và số liệu trong tài liệu này **đã được thay bằng dữ liệu ví dụ**. Không dùng các con số ở đây làm căn cứ kinh doanh. Giá trị của bộ tài liệu này nằm ở **cấu trúc và cách lập luận**, không nằm ở số liệu.


# 31 — Run-of-Show 5 buổi & Spec ghi hình tái sử dụng

> **Lưu ý phân vai:** nguồn chuẩn là [[05-organization-roles-raci]] và [[00-TLK-READ-ME-FIRST]]. Mọi ca Bảo/Chi xuất hiện trong tài liệu này là phân công tạm cho campaign, không thay đổi vai trò gốc là hỗ trợ kỹ thuật lớp chuyên sâu.

> Chuỗi 1 An dạy toàn bộ. Nhưng **"An dạy" không được phép biến thành "An làm mọi thứ"**. Tài liệu này tách rành mạch: An chỉ đứng trên sân khấu, mọi thứ khác có tên người khác. Đồng thời đặt spec ghi hình để 5 buổi này trở thành **nguyên liệu evergreen**, thay vì 5 file Zoom bị bỏ quên.

---

## 1. Nguyên tắc phân vai

> **An chịu trách nhiệm từ cửa phòng học trở vào. Đội chịu trách nhiệm tới cửa phòng học và mọi thứ ngoài phòng.** *(doc 24 mục 1.1)*

Cụ thể hóa cho một buổi live:

| An LÀM | An KHÔNG làm |
|---|---|
| Giảng, demo, trả lời Q&A trên sóng | Mở phòng Zoom, admit người vào |
| Ra hiệu chuyển slide | Bấm chia sẻ màn hình cho người khác |
| Đọc 2–3 câu hỏi được lọc sẵn | Đọc chat Zoom |
| Công bố giá và deadline | Trả lời tin nhắn Zalo |
| Quyết định kéo dài/rút ngắn khối | Gửi link thanh toán |
| — | Điểm danh, ghi hình, đối soát đơn |

**Lý do không thỏa hiệp:** mỗi việc An nhặt thêm là một việc không bao giờ chuyển giao được. Chuỗi 1 là lần đầu tiên đội tập chạy — nếu An làm hộ, chuỗi 5 vẫn phải An làm.

---

## 2. Bảng phân vai cố định — 5 buổi

| Vai | Người | Nhiệm vụ trong buổi | Có mặt |
|---|---|---|---|
| **Giảng chính** | **An** | Toàn bộ nội dung trên sóng | 19h45–22h15 |
| **Chủ phòng kỹ thuật** | **Hà** | Mở phòng, admit, ghi hình, poll, thả link, xử lý sự cố, xuất báo cáo attendee | 19h15–22h30 |
| **Trực chat Zoom + nhóm Zalo** | **Chi** | Trả lời chat, lọc câu hỏi cho An, đăng nhóm theo lịch | 19h30–23h00 |
| **Chốt đơn & thanh toán** | **Bảo** | Gửi link thanh toán, xác nhận chuyển khoản, xử lý nâng cấp, bán vé VIP, cập nhật Sheet | 20h30–23h30 |
| **Trực chốt khung Q&A** *(BOD chốt)* | **Hà + Bảo** | 21h35–22h15 — khung sinh 75% đơn. Hà tạm rời vai kỹ thuật, bàn cho người dự phòng | 21h30–23h00 |
| **Số liệu** | **Nguyệt** | Theo dõi số người vào phòng theo phút, báo An nếu rơi bất thường | 20h00–22h15 |
| **Dự phòng** | `[CẦN BỔ SUNG]` | Sẵn sàng thay Hà nếu mất kết nối | 20h00–22h15 |

> ⚠️ **Xung đột vai phát sinh từ quyết định BOD.** BOD chốt **Hà và Bảo trực chốt khung Q&A**. Nhưng Hà cũng là Chủ phòng kỹ thuật — **hai vai này va nhau đúng 40 phút quan trọng nhất của buổi.** Từ 21h35 Hà không thể vừa canh Zoom vừa trả lời hàng chục tin nhắn.
>
> **Ba cách gỡ, theo thứ tự khuyến nghị:**
> 1. **Có người thứ tư làm kỹ thuật từ 21h30** — Chi chuyển sang kỹ thuật, Hà sang chốt. Nhóm Zalo lúc này chỉ cần ghim link, ít việc.
> 2. Hà giữ kỹ thuật, **Chi + Bảo trực chốt**. Đơn giản nhất nhưng Chi chưa được giao vai này.
> 3. Giữ nguyên BOD chốt, chấp nhận Hà phản hồi chậm trong khung Q&A. **Không khuyến nghị** — đây là khung sinh 75% đơn.
>
> `[CHỜ BOD]` Chọn một trong ba. **Phải chốt trước D−3.**

**Cảnh báo công suất:** Bảo một mình xử lý đơn của 300–800 người dự là không khả thi ở buổi 5. Xem mục 6.

---

## 3. Rundown chuẩn một buổi — 120 phút

Áp dụng cho cả 5 buổi. Phần khác nhau ghi ở mục 4.

| Giờ | Phút | Khối | Ai chạy | Ghi chú vận hành |
|---|---:|---|---|---|
| 19h15 | T−45 | Hà mở phòng, bật ghi hình thử 2 phút, kiểm âm thanh + chia sẻ màn hình | Hà | Xem checklist mục 5 |
| 19h30 | T−30 | Chi đăng link phòng lên 4 nhóm Zalo + ghim | Chi | |
| 19h45 | T−15 | **An vào phòng, thử demo sẽ dùng tối nay** | An + Hà | Demo hỏng phát hiện lúc này còn sửa được |
| 19h50 | T−10 | Mở phòng chờ, phát nhạc + slide đếm ngược | Hà | Người vào sớm không thấy phòng trống |
| 19h55 | T−5 | Chi đăng "đang mở phòng" + SMS *(buổi 1 và 5)* | Chi + Nguyệt | |
| **20h00** | **0–5** | **Mở:** điểm danh bằng chat, xin cam kết ở lại, **công bố tên quà cuối buổi** | An | Quà cuối buổi là đòn giữ người mạnh nhất ([[30-show-up-engine-khong-co-zalo-oa]] mục 5) |
| 20h05 | 5–20 | **Origin story** *(buổi 1)* / **Nhắc lại 60 giây + kết quả người học** *(buổi 2–5)* | An | Buổi 1 là bản gốc để quay lại — xem mục 7 |
| 20h20 | 20–35 | **Niềm tin #1 — Phương tiện:** AI là nhân sự, không phải công cụ | An | Trial close: *"thấy quen thì gõ CÓ vào chat"*. Chi đếm số CÓ, báo An |
| 20h35 | 35–50 | **Niềm tin #2 — Bản thân:** không cần biết code. **DEMO LIVE 8 phút** | An | **Khoảnh khắc quyết định. Demo phải chạy thật.** Hà chuẩn bị bản ghi dự phòng — xem mục 6 |
| 20h50 | 50–65 | **Niềm tin #3 — Ngoại cảnh:** hệ 5 lớp Business Brain → Dashboard | An | |
| 21h05 | 65–75 | **Case study có số** | An | Mỗi buổi một case khác nhau — xem mục 4 |
| 21h15 | 75–90 | **Stack:** trình từng cấu phần, mỗi cấu phần gắn một phản đối | An | **Không báo giá trước phút 90** |
| 21h30 | 90–95 | **Báo giá + deadline + cơ chế nâng cấp** | An | Bảo bật link thanh toán đúng phút này |
| 21h35 | 95–115 | **Q&A có kịch bản:** 8–10 câu mồi xen câu thật | An + Chi lọc | **75% đơn rơi vào đây.** Bảo + Chi chốt song song trên Zalo |
| 21h55 | 115–120 | **Phát quà cuối buổi + hé buổi sau + nhắc điểm danh cộng dồn** | An | Không kết thúc bằng bán. Kết thúc bằng cho |
| 22h00 | T+0 | Dừng ghi hình, cảm ơn, đóng phòng | Hà | |
| 22h05 | T+5 | Hà xuất attendee → dán Sheet | Hà | [[29-tracking-measurement-spec]] mục 6 |
| 22h15 | T+15 | Chi đăng tóm tắt 3 gạch + hé buổi sau lên nhóm | Chi | |
| 22h30 | T+30 | Bảo đối soát đơn, cập nhật Sheet, gửi xác nhận | Bảo | |
| 23h00 | T+60 | Nguyệt chốt số buổi, gửi 5 dòng vào nhóm nội bộ | Nguyệt | Xem mẫu mục 8 |

---

## 4. Điểm khác biệt từng buổi

| Buổi | Chủ đề | Chốt | Case study dùng | Điểm vận hành đặc biệt |
|:--:|---|---|---|---|
| **1** | Foundation — AI Agent đã làm được gì, mô hình thế giới, AI Agent tạo mô hình KD mới | **KHÔNG chốt khóa · CÓ bán vé VIP/VVIP** *(BOD chốt lượt 2)* | demo tự thân: Genful + đội agent | Buổi đông nhất → **ghi hình cẩn thận nhất**. Nêu outline 4 buổi sau. Công bố điểm danh cộng dồn. **Chào vé VIP ở phút 5–8** — xem 4.0 |
| **2** | Ứng dụng AI Agent trong KD/Marketing/Sales | **Cấp 1 — AI Agent for Business, 5tr** | Case DN giảm việc lặp, có số trước–sau | **Bắt buộc công bố cơ chế nâng cấp TRƯỚC khi báo giá** *(doc 17 C2)*. Phát **form insight #1** ở phút 60 |
| **3** | Xây mô hình KD sản phẩm số | **Cấp 2 — AI Builder Bootcamp, 5tr** + Gói 2 khóa **9tr** | Case chuyên gia đóng gói sản phẩm số, có doanh thu | Nói *"khóa thứ hai chỉ thêm 5,6 triệu"*, **không nói phần trăm** |
| **4** | Xây kênh AI bán hàng & affiliate | **Cấp 3 — 5tr** + Gói 3 khóa **11tr** | Case xây kênh AI làm affiliate, có số | Buổi rơi mạnh nhất → tăng liều quà + đọc tên người dự đủ. **Form insight #2** ở phút 55 |
| **5** | Hệ thống AI Agent vận hành một mô hình KD + Bản đồ 90 ngày | **Cấp 4 — The Agentic Co-Founder 12tr** + **TRỌN BỘ 19tr** | Case anh Hưng (CEO) — case mạnh nhất để cuối | **DEMO CO-FOUNDER AGENT LIVE.** Buổi đắt nhất. Cần ≥3 người trực chốt. Mời ngày offline |

### 4.0 Bán vé VIP trong buổi 1 — cách làm không phá không khí

BOD chốt bán thêm vé trong buổi 1. Đây là **lần chốt đầu tiên của cả chuỗi** — làm sai thì mất niềm tin ngay từ đầu, làm đúng thì tạo thói quen mua hàng *(doc 17 B1)*.

| Phút | Việc | Cách nói |
|---|---|---|
| **5–8** | Chào vé **một lần duy nhất**, trước khi vào nội dung | *"Buổi học này miễn phí và anh chị cứ học hết. Có một thứ em muốn nói trước rồi thôi không nhắc lại: ai muốn giữ bản ghi trọn đời, workbook và bộ template thì có vé VIP 280k. Link ở chat. Còn không có vé thì vẫn học đầy đủ như nhau. Giờ ta vào bài."* |
| 8 | Bảo thả link vào chat **một lần** | Không nhắc lại giữa buổi |
| 115–120 | Nhắc lại **một lần** khi phát quà cuối buổi | *"Ai muốn giữ lại bản ghi thì link vé vẫn còn trong chat tới hết đêm nay."* |

**Ba luật:**

1. **Tối đa 2 lần nhắc trong cả buổi 1.** Nhắc lần thứ ba là biến buổi học thành buổi bán hàng.
2. **Luôn nói rõ "không có vé vẫn học đầy đủ".** Nếu người ta ngờ nội dung bị giấu sau vé, họ rời phòng.
3. **Bán bằng quyền sở hữu, không bán bằng nội dung.** Vé bán bản ghi + workbook + template — thứ họ giữ lại được, không phải thứ họ được nghe.

> **Vì sao 280k mà không cao hơn ở buổi 1:** VVIP 700k nên để trên landing, nơi người ta có thời gian đọc. Trong buổi, một mức giá duy nhất quyết định nhanh hơn hai mức.

### Bốn thứ phải chuẩn bị riêng cho buổi 5

> 🔴 **BOD xác nhận ngày 29/07: Co-Founder Agent ĐANG BUILD, chưa xong.** Chuỗi 1 chạy trong ~2 tuần. Đây là **rủi ro số một còn lại của cả chuỗi** — buổi 5 là buổi đắt nhất (12tr và 19tr) và nó phụ thuộc hoàn toàn vào một demo chưa tồn tại.
>
> **Ba mốc cứng, không lùi:**
>
> | Mốc | Điều kiện | Nếu không đạt |
> |---|---|---|
> | **D−10** | Agent chạy được một luồng đầu-cuối, dù thô | **Báo BOD ngay.** Còn 10 ngày để quyết |
> | **D−7** | Demo 8 phút chạy mượt 3 lần liên tiếp | Quay **bản ghi demo dự phòng** và dùng bản ghi ở buổi 5 |
> | **D−5** | Đã chạy thử trước 20 người group Cơm AI Lo | Hoãn phần demo, đổi buổi 5 sang case study + lộ trình 90 ngày |
>
> **Phương án lùi nếu D−7 không đạt:** buổi 5 vẫn bán được bằng **case anh Hưng có số + Bản đồ 90 ngày cá nhân hóa từ form insight**, không nhất thiết phải demo live. Nhưng phải quyết ở D−7, không phải quyết vào tối buổi 5.

| # | Việc | Vì sao | Ai | Hạn |
|:--:|---|---|---|---|
| 1 | **Demo Co-Founder Agent chạy được thật** | Doc 17 C2.1 gọi đây là rủi ro lớn nhất còn lại. **BOD xác nhận đang build** | An | **D−7** |
| 2 | **Chạy thử demo trước 20 người trong group Cơm AI Lo** | Nếu không thuyết phục được 20 người quen thì sẽ không thuyết phục được 500 người lạ | An | D−5 |
| 3 | **Bảng giá 5 tầng in sẵn trên slide** — 5 / 9 / 11 / 12 / 19 | Ba đường nâng cấp phải về cùng 19tr, không ai thấy mình mua hớ | Anh Thư | D−3 |
| 4 | **Tăng lên ≥3 người trực chốt** | Bảo một mình không kham nổi đơn buổi 5 | An | D−3 |

> ✅ **ĐÃ CHỐT 29/07:** BOD duyệt sửa đụng giá — **combo 3 khóa hạ xuống 11tr**, tách khỏi Co-Founder 12tr. Bậc thang chính thức: **5 / 9 / 11 / 12 / 19tr**, mọi đường nâng cấp về cùng 19tr *(doc 17 B3-V2)*. Slide giá phải in đúng bộ số này.

---

## 5. Checklist kỹ thuật — Hà chạy mỗi buổi

### T−45 phút

| # | Việc | ✅ |
|:--:|---|:--:|
| 1 | Vào phòng Zoom bằng tài khoản host, kiểm tài khoản còn hạn | ⬜ |
| 2 | **Bật ghi hình thử 2 phút → mở file kiểm âm thanh và hình** | ⬜ |
| 3 | Kiểm micro An: không rè, không vọng, không tiếng quạt | ⬜ |
| 4 | Kiểm chia sẻ màn hình: slide + trình duyệt demo, chuyển qua lại mượt | ⬜ |
| 5 | Kiểm mạng: có mạng dự phòng 4G sẵn sàng chuyển | ⬜ |
| 6 | Đặt sẵn 3 poll, 5 tin nhắn mẫu để thả link | ⬜ |
| 7 | Tắt hết thông báo trên máy An *(tin nhắn hiện lên khi chia sẻ màn hình là mất chuyên nghiệp)* | ⬜ |
| 8 | Đặt phòng chờ ON, chat ON, cho phép đổi tên OFF | ⬜ |

### T−10 phút

| # | Việc | ✅ |
|:--:|---|:--:|
| 9 | Mở phòng chờ, bật slide đếm ngược + nhạc | ⬜ |
| 10 | Xác nhận Chi, Bảo, Nguyệt đã vào phòng | ⬜ |
| 11 | **Bật ghi hình chính thức** *(bật sớm, thà thừa 10 phút còn hơn thiếu 30 giây)* | ⬜ |

### T+5 phút sau buổi

| # | Việc | ✅ |
|:--:|---|:--:|
| 12 | Dừng ghi, chờ file render xong mới tắt máy | ⬜ |
| 13 | **Đổi tên file theo quy ước** — mục 7.2 | ⬜ |
| 14 | Tải lên Drive `AFW_C1_RECORDINGS` ngay trong đêm | ⬜ |
| 15 | Xuất báo cáo attendee → dán vào Sheet | ⬜ |

---

## 6. Kịch bản sự cố — quyết định trong 30 giây

| Sự cố | Ai xử | Hành động ngay | Câu An nói trên sóng |
|---|---|---|---|
| **Demo live không chạy** | Hà | Bật **bản ghi demo dự phòng** đã quay sẵn *(bắt buộc có)* | *"Cái này em quay lại lúc chạy thật tuần trước, để anh chị xem cho rõ hơn."* — **không xin lỗi, không giải thích lỗi** |
| **An rớt mạng** | Hà | Chuyển sang video chèn đã chuẩn bị · Chi đăng nhóm Zalo trấn an | Hà lên tiếng: *"Anh An đang chuyển mạng, ta xem tiếp phần này 2 phút."* |
| **Zoom sập / quá tải** | Hà | Mở link phòng dự phòng đã tạo sẵn · Chi đăng link mới lên 4 nhóm Zalo + SMS | — |
| **Hà mất kết nối** | Người dự phòng | Người dự phòng đã là co-host, tiếp quản ngay | — |
| **Chat bị spam / phá** | Chi | Tắt chat công khai, chuyển sang chat riêng với host | — |
| **Cổng thanh toán lỗi** | Bảo | Chuyển sang số tài khoản chuyển khoản + ghi nhận tay vào Sheet | *"Anh chị chuyển khoản theo thông tin bên dưới, bên em xác nhận trong 15 phút."* |
| **Số người tụt bất thường >30% trong 10 phút** | Nguyệt | Báo An qua tin nhắn riêng | An chuyển ngay sang khối tương tác/demo, bỏ phần lý thuyết |

### Ba thứ phải chuẩn bị trước để kịch bản trên chạy được

1. **Bản ghi demo dự phòng** cho cả 5 buổi — quay trước D−3, mỗi bản 5–8 phút.
2. **Link phòng Zoom dự phòng** đã tạo, đã dán sẵn trong tin nhắn nháp của Chi.
3. **Người dự phòng đã được set co-host từ đầu buổi**, không phải lúc sự cố mới thêm.

---

## 7. Spec ghi hình — biến chuỗi 1 thành nguyên liệu evergreen

> **Đây là phần dễ bỏ qua nhất và đắt nhất nếu bỏ qua.** BOD đã chốt chuỗi 1 chỉ ghi Zoom, quay chỉn chu ở chuỗi 2–3. Nhưng bản ghi chuỗi 1 vẫn phải **dùng được** — làm bản nháp dựng kịch bản, cắt clip social, và làm mốc so sánh. Không có spec, 5 buổi này thành 5 file 2GB không ai mở lại.

### 7.1 Cấu hình Zoom bắt buộc

| Cài đặt | Giá trị | Vì sao |
|---|---|---|
| Chế độ ghi | **Cloud + Local đồng thời** | Cloud để chia sẻ nhanh, Local để phòng cloud lỗi |
| Bố cục ghi | **Ghi riêng: màn hình chia sẻ + camera diễn giả thành 2 file** | Dựng lại được, đổi bố cục được. Ghi gộp là mất khả năng biên tập |
| Âm thanh | **Ghi thêm audio riêng của từng người nói** | Tách được tiếng An khỏi tiếng ồn/chat |
| Độ phân giải | 1080p | 720p không cắt clip social được |
| Ghi chat | **BẬT** — xuất file chat | Chat là kho câu hỏi thật, dùng làm FAQ và hook cho chuỗi sau |
| Phụ đề tự động | **BẬT** | Có transcript → chuyển thành SOP, bài viết, script chuỗi sau |

> **Kiểm ngay hôm nay:** tài khoản Zoom hiện tại có hỗ trợ ghi tách file và audio riêng không. Gói Pro cơ bản có thể không có. `[PHẢI KIỂM]`

### 7.2 Quy ước đặt tên file

```
AFW-C1-B{số buổi}-{loại}-{ngày}.{đuôi}

Ví dụ:
AFW-C1-B01-manhinh-20260805.mp4
AFW-C1-B01-camera-20260805.mp4
AFW-C1-B01-audio-thang-20260805.m4a
AFW-C1-B01-chat-20260805.txt
AFW-C1-B01-transcript-20260805.txt
AFW-C1-B01-attendee-20260805.csv
```

**Sáu file mỗi buổi × 5 buổi = 30 file.** Thiếu bất kỳ file nào thì buổi đó không dùng lại được đầy đủ.

### 7.3 Ba việc phải làm với bản ghi trong 48 giờ sau chuỗi

| # | Việc | Ai | Ra cái gì |
|:--:|---|---|---|
| 1 | **Đánh dấu mốc thời gian** mọi khối trong mỗi bản ghi | Hà | File `AFW-C1-timecode.md` — biết phần nào ở phút nào |
| 2 | **Chấm điểm từng khối** *(1–5)* dựa trên số người ở lại theo phút | Nguyệt + An | Biết khối nào giữ người, khối nào làm rơi — **đây là dữ liệu quý nhất của cả chuỗi** |
| 3 | **Cắt 10 clip 30–60 giây** từ khối điểm cao nhất | Duy | Nguyên liệu organic + paid creative cho chuỗi 2, chi phí bằng 0 |

> Việc số 2 là thứ biến chuỗi 1 thành bài học thật. Nếu không chấm khối, chuỗi 2 sẽ lặp lại đúng những khối làm người ta rời phòng.

### 7.4 Nếu có khách mời ở chuỗi sau

Chuỗi 1 chỉ An dạy nên **không vướng bản quyền**. Nhưng từ chuỗi 2, nếu thầy Tony hoặc thầy Khoa tham gia, **phải có thoả thuận quyền dùng bản ghi ký trước khi bấm ghi**. Mẫu ở [[33-phap-ly-chinh-sach-ban-hang-va-ban-ghi]] mục 4.

**Luật cứng: không có thoả thuận → không ghi hình → không có evergreen.** Doc 24 mục 10.2 đã cảnh báo; đây là nơi biến nó thành quy trình.

---

## 8. Báo cáo 5 dòng sau mỗi buổi — Nguyệt gửi trước 23h

```
BUỔI {N} — {ngày}
1. Vào phòng: {số} người · đỉnh {số} lúc {phút} · còn lại lúc kết thúc: {số}
2. Rơi mạnh nhất ở phút {số} — khối "{tên khối}"
3. Đơn: {số} đơn · {số} tiền · gói bán chạy nhất: {tên}
4. Nhận định: {một câu, không phải liệt kê số}
5. Sửa gì ở buổi mai: {đúng MỘT thứ}
```

> **Luật của doc 15: báo cáo kết bằng hành động, cấm liệt kê số suông.** Và dòng 5 chỉ được ghi **một** thứ — sửa hai thứ cùng lúc thì không biết cái nào có tác dụng.

---

## 9. Checklist tổng trước chuỗi

| # | Việc | Hạn | Ai | ✅ |
|:--:|---|---|---|:--:|
| 1 | Kiểm gói Zoom có ghi tách file + audio riêng không | **D−12** | Hà | ⬜ |
| 2 | Chốt người dự phòng vai Chủ phòng kỹ thuật | D−10 | An | ⬜ |
| 3 | Demo Co-Founder Agent chạy được | **D−7** | An | ⬜ |
| 4 | Quay 5 bản ghi demo dự phòng | D−5 | An + Duy | ⬜ |
| 5 | Chạy thử demo trước 20 người group Cơm AI Lo | D−5 | An | ⬜ |
| 6 | Tạo phòng Zoom dự phòng + soạn tin nháp | D−5 | Hà | ⬜ |
| 7 | ~~BOD chốt bảng giá 5 tầng~~ ✅ **ĐÃ CHỐT 29/07: 5/9/11/12/19tr** | — | BOD | ✅ |
| 7b | **Gỡ xung đột vai Hà** *(kỹ thuật vs chốt Q&A — mục 2)* | **D−3** | An | ⬜ |
| 8 | Slide bảng giá + 8–10 câu Q&A mồi mỗi buổi | D−3 | Anh Thư | ⬜ |
| 8b | **Slide + kịch bản chào vé VIP buổi 1** (mục 4.0) | D−3 | Anh Thư | ⬜ |
| 9 | Chốt ≥3 người trực chốt buổi 5 | D−3 | An | ⬜ |
| 10 | Chạy thử toàn bộ rundown 30 phút với cả đội | **D−2** | Cả đội | ⬜ |
| 11 | Chốt danh sách quà cuối buổi cho cả 5 buổi | D−3 | An | ⬜ |
| 12 | Tạo thư mục Drive `AFW_C1_RECORDINGS`, phân quyền | D−2 | Hà | ⬜ |

---

## Khối bàn giao

**Dùng ngay:** phân vai (mục 2) · rundown 120 phút (mục 3) · khác biệt từng buổi (mục 4) · checklist kỹ thuật (mục 5) · kịch bản sự cố (mục 6) · spec ghi hình (mục 7).

**`[PHẢI KIỂM HÔM NAY]`:** gói Zoom có ghi tách file + audio riêng + transcript không. Nếu không, phải nâng gói **trước** khi chạy — không sửa được sau.

**`[CHỜ BOD]`:** bảng giá 5 tầng đã sửa đụng giá 12tr chưa · ai là người dự phòng kỹ thuật · ai là 2 người trực chốt thêm ở buổi 5.

**Không được làm:** để An đọc chat Zoom · bắt đầu buổi khi chưa bật ghi hình · chạy demo live buổi 5 mà chưa có bản ghi dự phòng · ghi hình người khác khi chưa có thoả thuận.

*Tài liệu 31 · spec vận hành · 29/07/2026 · phái sinh từ [[16-webinar-funnel-blueprint]] mục 6, [[17-chuong-trinh-webinar-5-ngay]] mục 1 + B, [[24-he-thong-van-hanh-jd-kpi-quy-trinh]] mục 1.1 và 7.*
