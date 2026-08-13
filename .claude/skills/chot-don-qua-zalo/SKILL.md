---
name: chot-don-qua-zalo
description: "Xây kịch bản chốt đơn qua Zalo cho doanh nghiệp Việt Nam: mở lời sau khi khách để lại số, khai thác nhu cầu bằng tin nhắn, báo giá, xử lý im lặng và chốt. Kèm nhịp nhắc lại và quy tắc không làm phiền. Dùng khi khách chủ yếu nhắn Zalo chứ không gọi điện hay email."
allowed-tools: Read Write Glob
ten-viet: "Chốt Đơn Qua Zalo"
nhom: "07. Bán Hàng & Phễu"
ten-goc: "Chốt Đơn Qua Zalo"
---

# Chốt Đơn Qua Zalo

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

- Khách để lại số điện thoại rồi kết bạn Zalo, không nghe máy
- Đội sale đang nhắn tin tuỳ hứng, mỗi người một kiểu
- Tỷ lệ khách "seen không rep" cao mà không biết vì sao
- Muốn người mới vào nhắn được ngay mà không cần kèm

**KHÔNG dùng** cho tin nhắn hàng loạt qua Zalo OA (đó là kênh broadcast, xem `email-sequence` và `drip-campaign` để thiết kế chuỗi). Skill này cho **nhắn 1-1 để chốt một khách cụ thể**.

---

## Nguyên tắc cốt lõi

ZALO KHÔNG PHẢI EMAIL. KHÁCH ĐỌC TRÊN ĐIỆN THOẠI, GIỮA GIỜ LÀM VIỆC, VÀ QUYẾT ĐỊNH TRONG 3 GIÂY CÓ TRẢ LỜI HAY KHÔNG. MỖI TIN NHẮN CHỈ ĐƯỢC HỎI MỘT THỨ VÀ PHẢI DỄ TRẢ LỜI HƠN LÀ DỄ LỜ ĐI.

---

## Giai đoạn 1: Lấy ngữ cảnh

### Đầu vào bắt buộc

| Đầu vào | Câu hỏi | Mặc định |
|---|---|---|
| **Sản phẩm đang bán** | "Khách này đang quan tâm gói nào?" | Đọc `00. Business Context/Sản Phẩm & Dịch Vụ/` |
| **Khách từ đâu ra** | "Khách để lại số từ quảng cáo, livestream, hay người quen giới thiệu?" | Từ quảng cáo |
| **Khách đã biết gì** | "Khách đã xem nội dung nào, đã biết giá chưa?" | Chưa biết giá |
| **Giá và ưu đãi** | "Giá bao nhiêu, có ưu đãi gì đang chạy không?" | Đọc hồ sơ sản phẩm |
| **Ai nhắn** | "Người nhắn xưng là ai — chủ, tư vấn viên, hay trợ lý?" | Tư vấn viên |

Đọc `00. Business Context/Brand Voice — Giọng Thương Hiệu.md` để giữ đúng giọng. Zalo cho phép thân mật hơn website, nhưng không được lệch khỏi tính cách thương hiệu.

**CỔNG: Chưa biết khách từ đâu ra thì chưa viết được câu mở. Hỏi trước.**

---

## Giai đoạn 2: Kịch bản 5 nhịp

Zalo diễn ra theo nhịp, không theo kịch bản một mạch. Mỗi nhịp là **một tin nhắn, một mục đích**.

### Nhịp 1 — Mở lời (trong 5 phút sau khi khách để lại số)

Ba yếu tố bắt buộc: **nhận diện mình là ai · nhắc lại khách vừa làm gì · một câu hỏi dễ trả lời**.

```
Mẫu — khách từ quảng cáo:
Em chào anh/chị [Tên] ạ, em [Tên] bên [Thương hiệu].
Em thấy anh/chị vừa để lại thông tin quan tâm [tên sản phẩm].
Anh/chị đang tìm hiểu cho [tình huống A] hay [tình huống B] ạ?
```

**Vì sao hai lựa chọn:** câu hỏi mở ("anh chị cần gì ạ?") buộc khách phải nghĩ và soạn — phần lớn sẽ lười và bỏ qua. Hai lựa chọn chỉ cần gõ "A" là xong.

> **Tốc độ quan trọng hơn câu chữ.** Với chu kỳ bán ngắn, nhắn trong 5 phút đầu ăn đứt nhắn sau 1 tiếng. Với chu kỳ dài (trên 30 ngày), trong 4 giờ là đủ — nhưng đừng để qua ngày. Nếu ngoài giờ làm việc, vẫn nhắn ngay và ghi rõ "sáng mai em gọi lại anh/chị nhé".

### Nhịp 2 — Khai thác nhu cầu (2–4 tin, mỗi tin một câu hỏi)

Không hỏi dồn. Mỗi tin một câu, đợi trả lời rồi hỏi tiếp.

Thứ tự khai thác:
1. **Tình huống** — "Hiện tại anh/chị đang xử lý việc này thế nào ạ?"
2. **Vướng mắc** — "Chỗ nào làm anh/chị thấy mất thời gian nhất?"
3. **Mốc thời gian** — "Anh/chị định bắt đầu trong tháng này hay còn tham khảo thêm ạ?"
4. **Người quyết định** — "Việc này anh/chị quyết luôn hay cần trao đổi với ai nữa không ạ?"

Câu 3 và 4 là hai câu **sàng lọc quan trọng nhất**. Trả lời xong hai câu này là biết nên đầu tư bao nhiêu công vào khách.

### Nhịp 3 — Đưa giải pháp và báo giá

Chỉ báo giá **sau khi** đã biết vướng mắc. Báo giá sớm quá thì khách chỉ so tiền, không so giá trị.

```
Cấu trúc tin báo giá:
[1 câu tóm lại vướng mắc của khách bằng chính lời họ nói]
[1–2 câu gói giải pháp giải quyết đúng chỗ đó]
[Giá + đang có ưu đãi gì]
[1 câu hỏi chốt bước tiếp — không hỏi "anh chị thấy sao"]
```

Câu chốt bước tiếp phải cụ thể: *"Em giữ suất ưu đãi này tới hết thứ 6 cho anh/chị nhé?"* hoặc *"Anh/chị tiện 15 phút chiều nay hay sáng mai để em gọi trao đổi kỹ hơn ạ?"*

### Nhịp 4 — Xử lý im lặng

Khách "seen không rep" là bình thường, không phải là từ chối. Nhịp nhắc lại:

| Lần | Sau bao lâu | Nội dung |
|---|---|---|
| 1 | **5% chu kỳ bán** | Bổ sung **một thông tin mới có ích**, không hỏi lại "anh/chị xem chưa" |
| 2 | **15% chu kỳ bán** | Gửi bằng chứng: ảnh kết quả khách cũ, review, case study |
| 3 | **30% chu kỳ bán** | Chốt mềm — cho khách một đường lui lịch sự |

*Chu kỳ 20 ngày → nhắc sau 1, 3, 6 ngày. Chu kỳ 75 ngày → nhắc sau 4, 11, 23 ngày. Chu kỳ 3 ngày (bán lẻ) → nhắc sau 4 giờ, 11 giờ, 1 ngày.*

```
Mẫu lần 3 — đường lui lịch sự:
Dạ em hiểu là thời điểm này chưa phù hợp với anh/chị.
Em không làm phiền nữa ạ. Khi nào anh/chị cần thì nhắn em bất cứ lúc nào nhé.
Em gửi anh/chị [tài liệu/checklist] để dùng dần ạ.
```

**Sau 3 lần thì dừng.** Chuyển khách sang trạng thái *Nuôi dài hạn* trong pipeline, đưa vào chuỗi nội dung định kỳ, không nhắn 1-1 nữa.

### Nhịp 5 — Chốt và chuyển giao

Khi khách đồng ý:
1. Xác nhận lại **bằng văn bản trong Zalo**: gói gì, giá bao nhiêu, gồm những gì, khi nào bắt đầu
2. Gửi thông tin thanh toán
3. Xác nhận đã nhận tiền
4. Giới thiệu người sẽ tiếp nhận tiếp theo, kèm mốc thời gian đầu tiên

> Bước xác nhận bằng văn bản là chỗ hay bị bỏ. Nó ngăn tranh cãi "em tưởng gói đó có cả…" về sau.

---

## Giai đoạn 3: Bộ câu trả lời từ chối trong chat

Từ chối qua chat khác từ chối qua điện thoại — ngắn hơn, mơ hồ hơn, và thường là cách nói lịch sự của "chưa đủ tin".

| Khách nhắn | Ý thật thường là | Trả lời theo hướng |
|---|---|---|
| "Để em suy nghĩ thêm" | Chưa thấy đủ giá trị, hoặc chưa tin | Hỏi lại đúng một câu: điều gì làm anh/chị còn phân vân nhất ạ? |
| "Đắt quá" | So với thứ họ đang hình dung, không phải so với ngân sách | Quy giá về đơn vị nhỏ nhất (mỗi ngày, mỗi buổi) và đối chiếu với chi phí của việc không làm gì |
| "Để em hỏi ý kiến..." | Không phải người quyết | Đề nghị gửi tài liệu tóm tắt để khách chuyển tiếp, hoặc xin nói chuyện trực tiếp với người quyết |
| Seen không rep | Chưa cấp thiết | Không hỏi lại, gửi thêm một thông tin có ích |
| "Bên kia rẻ hơn" | Đang so sai thứ | Chỉ ra khác biệt cụ thể ảnh hưởng tới kết quả, không nói xấu đối thủ |
| "Có giảm thêm không" | Đang thử | Không giảm giá — đổi sang tặng thêm giá trị hoặc chia nhỏ đợt thanh toán |

Nếu đã chạy `/objection-handler` thì lấy nội dung từ sổ tay đó và rút gọn về độ dài tin nhắn.

---

## Giai đoạn 4: Ghi vào vault

Mỗi khách Zalo được chốt hoặc mất đều phải để lại dấu vết:

| Ghi gì | Ghi vào đâu |
|---|---|
| Hồ sơ khách (tên, nguồn, phân khúc, trạng thái) | `People/[Tên] — [Nguồn] (PK<số>).md` |
| Tóm tắt cuộc trao đổi, khách nói gì bằng chính lời họ | `Meetings/YYYY-MM-DD — Zalo — [Tên khách].md` |
| Trạng thái deal | `03. Areas/Sales Pipeline & CRM/Pipeline Tháng [MM-YYYY].md` |
| Câu từ chối mới chưa có trong sổ tay | `01. Inbox/` để tuần sau bổ sung vào `/objection-handler` |

**Lời khách nói nguyên văn là tài sản.** Chúng là nguyên liệu tốt nhất cho content và quảng cáo sau này — chép nguyên, đừng viết lại cho hay.

---

## Đầu ra

- Bộ kịch bản 5 nhịp, viết sẵn để copy dán
- Bảng câu trả lời từ chối rút gọn cho chat
- Nhịp nhắc lại 3 lần kèm nội dung từng lần
- Checklist chuyển giao sau khi chốt

Lưu vào `04. Resources/Playbooks/Kịch Bản Chốt Đơn Qua Zalo.md`.

---

## Ràng buộc

- **Không spam.** Tối đa 3 lần nhắc, sau đó dừng. Danh tiếng thương hiệu đắt hơn một deal.
- **Không bịa cam kết.** Chỉ hứa những gì có trong `00. Business Context/Sản Phẩm & Dịch Vụ/`.
- **Không tự ý giảm giá.** Mức giảm tối đa phải do chủ doanh nghiệp chốt và ghi trong `Decisions/`.
- **Không copy nguyên kịch bản cho mọi khách.** Kịch bản là khung, tên riêng và tình huống phải thật.
- Tin nhắn dài quá 4 dòng trên điện thoại là khách lướt qua. Tách thành nhiều tin.
