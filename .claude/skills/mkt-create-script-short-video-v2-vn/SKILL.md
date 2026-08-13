---
name: mkt-create-script-short-video-v2-vn
description: "Nghiên cứu brand context và Second Brain được người dùng chỉ định rồi tạo gói tiếng Việt gồm video ngắn 30–90 giây và bài Facebook dài đăng kèm. Dùng khi cần biến nhật ký, kiến thức, framework hoặc trải nghiệm của bất kỳ thương hiệu/tác giả nào thành script short có 4S hook, triple hook, proof, một CTA và bài viết sâu hơn mà vẫn đúng brand voice và quyền riêng tư."
---

# MKT Gói Nội Dung Video Ngắn + Facebook

Tạo **một insight — hai tầng chiều sâu**: video giúp người xem dừng lại và hiểu nhanh; bài Facebook giúp họ đổi cách nhìn và biết cách làm. Giữ cùng một thông điệp, lời hứa, proof và hành động tiếp theo ở cả hai đầu ra. Học cơ chế giữ chú ý của Kallaway; không sao chép câu chữ, cá tính hoặc giọng khoe thành tích của người khác.

## Chuẩn đầu ra

Tạo một gói để người đại diện thương hiệu có thể quay, editor có thể dựng và bài Facebook có thể đăng mà không phải viết lại:

1. Nêu nguồn insight và mức được phép công khai.
2. Đưa ba phương án hook chữ–lời–hình, chọn một phương án đề xuất.
3. Viết timeline có lời thoại, text overlay, hình ảnh và bằng chứng cho từng beat.
4. Xuất bản thoại sạch để quay hoặc đưa vào TTS.
5. Viết bài Facebook dài từ cùng Content Seed, bổ sung mindset, cơ chế và cách áp dụng.
6. Viết caption ngắn khi cần đăng trên TikTok/Reels.
7. Chạy quality gate cho từng đầu ra và sự đồng nhất giữa hai đầu ra.

Đọc [references/templates.md](references/templates.md) trước khi soạn đầu ra. Đọc [references/second-brain-routing.md](references/second-brain-routing.md) trước khi tìm nguyên liệu trong Second Brain.

## Nguyên tắc không thương lượng

- Dùng brand voice, đại từ và cách gọi audience từ `$mkt-brand-context-guard`; không mặc định một giọng cá nhân.
- Dùng Kallaway để tổ chức sự chú ý; dùng nguồn của thương hiệu/tác giả để tạo góc nhìn riêng.
- Không biến Literature Note hoặc lời người khác thành trải nghiệm của tác giả.
- Không gọi một kiến thức cũ là “mới” nếu không có thay đổi thật. Có thể đưa ra góc nhìn mới và nói rõ đó là một cách nhìn.
- Không bịa số liệu, case, lời khách, kết quả hoặc urgency. Claim càng mạnh càng cần proof mạnh.
- Mặc định coi dữ liệu gia đình, sức khỏe, tài chính, khách hàng, credentials và chuyện riêng là **không được công khai**.
- Không bắt buộc liệt kê “thứ nhất, thứ hai, thứ ba”. Chỉ dùng danh sách khi nội dung thật sự là quy trình hoặc checklist.
- Không dùng nhiều CTA. Không biến mọi video thành bài bán hàng.
- Không kéo dài bài Facebook bằng cách chép lại transcript. Mỗi đoạn thêm vào phải làm rõ cảnh, cách nhìn, cơ chế, ví dụ, ranh giới hoặc hành động.

## Workflow

### Bước 1 — Chốt brief làm việc

Xác định hoặc suy luận có kiểm soát:

- Người xem chính: lấy từ brand context hoặc brief; không dùng audience của thương hiệu khác.
- Một vấn đề hoặc kết quả mà video xử lý.
- Nền tảng và thời lượng: mặc định 9:16, 45–60 giây.
- Mục tiêu: nhận biết, xây niềm tin, tạo hội thoại hay chuyển sang nội dung tiếp theo.
- CTA duy nhất; mặc định không ép CTA thương mại nếu user chưa cung cấp.
- Nguyên liệu user đã đưa: topic, voice note, bài viết, link hoặc note.

Không dừng để hỏi nếu có thể suy luận an toàn từ ngữ cảnh. Hỏi lại khi thiếu lựa chọn có thể làm sai đối tượng, sai claim hoặc lộ thông tin riêng tư.

### Bước 2 — Nạp nguồn sự thật

Chạy `$mkt-brand-context-guard` và đọc các nguồn trong `brand_context_root` của thương hiệu đang chọn: mô hình kinh doanh, ICP, định vị, brand voice, trụ cột, offer, CTA và quyền công bố.

Sau đó:

1. Nếu người dùng cung cấp `creator_context_root`, đọc hồ sơ tác giả và tìm note theo [references/second-brain-routing.md](references/second-brain-routing.md).
2. Không tự mở kho cá nhân ngoài workspace khi chưa được đưa vào phạm vi.
3. Đọc toàn bộ 3–8 note có tín hiệu cao nhất; theo wikilink tối đa một bước khi link đó bổ sung proof hoặc bối cảnh cần thiết.
4. Ghi lại đường dẫn nguồn và phân loại `Trải nghiệm tác giả`, `Tri thức đã chắt lọc`, `Nguồn ngoài`, `Giả thuyết` hoặc `Riêng tư`.

Nếu Second Brain không truy cập được, nói rõ giới hạn và dùng nguyên liệu user cung cấp; không giả vờ đã đọc.

### Bước 3 — Chưng cất một insight sở hữu được

Viết nội bộ một Content Seed trước khi viết hook:

```text
Người xem:
Cảnh/điểm đau cụ thể:
Niềm tin cũ:
Góc nhìn thương hiệu/tác giả:
Cơ chế giải thích:
Proof/trust anchor:
Ranh giới của claim:
Cách nhìn cần thay đổi:
Cơ chế/hệ thống cần giải thích sâu:
3–5 bước áp dụng nếu có trình tự thật:
Câu chốt người xem cần nhớ:
Một hành động tiếp theo:
Nguồn + quyền công khai:
```

Ưu tiên insight có đủ ba lớp:

1. Một sự việc hoặc quan sát thật.
2. Một cách nhìn mang dấu vân tay thương hiệu/tác giả.
3. Một hệ quả hữu ích cho đúng ICP.

Nếu chỉ có kiến thức học từ người khác, ghi nguồn và thêm phần tác giả đã áp dụng, phản biện hoặc kết nối vào quy trình thật. Nếu chưa có phần này, không viết như thể đó là phương pháp riêng của thương hiệu.

### Bước 4 — Chọn động cơ câu chuyện

Chọn đúng một cấu trúc:

| Trường hợp | Động cơ |
|---|---|
| Người xem đang tin sai điều gì | **Niềm tin cũ → tương phản → cơ chế mới** |
| Có cảnh vận hành hoặc sai lầm thật | **Cảnh thật → điểm nghẽn → cách sửa** |
| Có demo/quy trình cụ thể | **Kết quả → mổ xẻ → ranh giới** |
| Có bài học từ nhật ký | **Khoảnh khắc → nhận ra → quyết định mới** |
| Có framework/checklist thật | **Kết quả → 2–3 bước → việc làm ngay** |

Viết **câu chốt mang về** trước, rồi mới dựng hook. Dùng cùng động cơ và câu chốt cho video lẫn bài Facebook. Hook phải hứa đúng điều cả hai thân bài sẽ giao.

### Bước 5 — Viết Hook System theo Kallaway

Tạo ba phương án. Mỗi phương án phải trả lời ngay:

- Video nói về gì?
- Xem tiếp thì người xem được gì hoặc tránh mất gì?

Chấm hook theo 4S:

- **Subject:** chủ thể rõ.
- **Stakes:** hệ quả đủ đáng quan tâm với ICP.
- **Speed:** nén ý, không nói quá nhanh.
- **Super clear:** chỉ có một cách hiểu hợp lý.

Với mỗi phương án, thiết kế ba lớp cùng lúc:

| Lớp | Quy chuẩn |
|---|---|
| **Chữ** | 3–8 từ, tối đa hai dòng, giữ khoảng ba giây, không che mắt hoặc miệng |
| **Lời** | Một câu nói được tự nhiên, vào thẳng chủ đề và hệ quả |
| **Hình** | Khung đầu cho thấy chủ thể, vấn đề hoặc bằng chứng; chuyển động vừa đủ, không gimmick |

Ba lớp phải cùng hướng về một ý. Nếu tắt âm vẫn đoán được chủ đề; nếu chỉ nghe vẫn hiểu đúng lời hứa; nếu chỉ đọc text không được hiểu sang chủ đề khác.

### Bước 6 — Xây Lock-in Zone từ giây 3–10

Viết 2–4 câu để làm hai việc:

1. Xác nhận ngay claim của hook, không bait-and-switch.
2. Cho người xem một lý do tin người nói hoặc thương hiệu sẽ không làm phí thời gian của họ.

Ưu tiên trust anchor theo thứ tự:

1. Cảnh hoặc kết quả tác giả đã trực tiếp trải qua và được phép kể.
2. Demo, ảnh màn hình, sơ đồ, log hoặc quy trình thật.
3. Case tương đồng đã ẩn danh và có quyền công bố.
4. Nguồn ngoài đáng tin, được diễn đạt đúng phạm vi.

Không có proof thì thu hẹp lời hứa thành quan sát, giả thuyết hoặc cách thương hiệu đang thử.

### Bước 7 — Viết thân bài và kết

Giữ nhịp mặc định:

```text
0–3s    Hook: chủ đề + stakes
3–10s   Lock-in: xác nhận + trust anchor
10–35s  Một cơ chế; tối đa ba ý hỗ trợ
35–50s  Ví dụ/demo + ranh giới
50–60s  Câu chốt + một CTA
```

Để chủ đề quen thuộc trở nên đáng xem một cách có trách nhiệm:

- Tìm một góc mới thật hoặc một cách gọi rõ hơn.
- Nối góc đó với outcome người xem muốn.
- Đặt niềm tin cũ cạnh cơ chế mới để tạo tương phản thật.
- Chỉ dùng tính thời điểm khi có sự kiện hoặc cửa sổ thời gian xác thực.
- Đưa proof gần với đời sống ICP nhất có thể.

Sau mỗi khái niệm trừu tượng, thêm cảnh, ví dụ, thao tác hoặc cách kiểm tra. Nêu nơi AI không nên làm hoặc điều kiện khiến phương pháp thất bại khi điều đó quan trọng.

### Bước 8 — Mở rộng thành bài Facebook dài

Dùng framework xuất bản nội bộ **CẢNH → NGHẼN → ĐỔI → HỆ → LÀM → CHỐT**. Đây là framework kết hợp cơ chế kể chuyện Kallaway, brand voice và nguồn trải nghiệm; không gọi nó là framework nguyên bản của Kallaway.

| Nhịp | Chức năng |
|---|---|
| **CẢNH** | Mở bằng một tình huống, quan sát hoặc quyết định thật đủ cụ thể để người đọc thấy mình trong đó. |
| **NGHẼN** | Chỉ ra điểm nghẽn thật hoặc niềm tin cũ khiến cách làm hiện tại không hiệu quả. |
| **ĐỔI** | Đổi cách nhìn; nói rõ tác giả đã nhận ra điều gì và vì sao cách nhìn mới hợp lý hơn. |
| **HỆ** | Giải thích cơ chế hoặc hệ thống phía sau bằng ngôn ngữ đơn giản, có ví dụ và ranh giới. |
| **LÀM** | Đưa 3–5 bước, câu hỏi tự kiểm hoặc việc áp dụng cụ thể; chỉ đánh số khi có trình tự thật. |
| **CHỐT** | Gói lại một câu đáng nhớ và dùng đúng CTA đã chọn cho video. |

Giữ mặc định 600–1.000 từ; thay đổi khi user yêu cầu hoặc nguồn không đủ sâu. Không viết cho đủ chữ. Bài phải đứng độc lập khi người đọc chưa xem video và phải sâu hơn video ở hai lớp: **mindset** và **cách làm**.

Viết theo nhịp đọc Facebook:

- Mở bằng một câu hoặc một cảnh cụ thể, không mở bằng lời dẫn chung chung.
- Dùng đoạn ngắn 1–3 câu, khoảng trắng tự nhiên và câu chuyển ý rõ.
- Không để nhãn `CẢNH`, `NGHẼN`, `ĐỔI`, `HỆ`, `LÀM`, `CHỐT` trong bản đăng.
- Không dùng tiêu đề Markdown, bảng hoặc hashtag trong phần copy sẵn đăng trừ khi user yêu cầu.
- Không đưa claim, ví dụ hoặc chi tiết riêng tư mới chỉ để làm bài dài hơn.
- Giữ cùng lời hứa, proof, ranh giới và CTA với video; không để bài Facebook hứa lớn hơn.

### Bước 9 — Việt hóa theo brand voice

- Tuân theo đại từ, nhịp câu, từ nên dùng/tránh và mức trang trọng trong brand context.
- Viết để nói thành tiếng; không thêm từ đệm trái với giọng thương hiệu.
- Phản biện cách làm, không hạ thấp con người.
- Giảm hype; tăng quy trình, quyết định, demo, giới hạn và một việc làm ngay.
- Không mở bằng “Xin chào” hoặc “Hôm nay tôi sẽ…”.
- Không dùng câu hỏi giật gân khi một tuyên bố rõ sẽ mạnh hơn.

### Bước 10 — Lập storyboard chữ–lời–hình

Dùng bảng timeline trong [references/templates.md](references/templates.md). Với mỗi beat, kiểm tra:

- Chữ bổ sung hoặc nén lời, không tạo một thông điệp thứ hai.
- Hình chứng minh, minh họa hoặc làm rõ đúng câu đang nói; không dùng B-roll trang trí không liên quan.
- Bằng chứng xuất hiện tại đúng claim nó hỗ trợ.
- Text overlay nằm trong vùng an toàn và đủ lâu để đọc.
- Một cảnh không giữ quá lâu nếu không có thay đổi thông tin hoặc cảm xúc.

### Bước 11 — Chạy quality gate trước khi bàn giao

Chỉ đánh dấu `PASS` khi tất cả điều kiện đúng:

- [ ] Một ICP, một thông điệp, một outcome và một CTA.
- [ ] Hook đạt đủ 4S.
- [ ] Chữ–lời–hình đầu video cùng một ý.
- [ ] Giây 3–10 xác nhận lời hứa và có trust anchor phù hợp.
- [ ] Thân bài giao đúng điều hook đã hứa.
- [ ] Claim, số liệu và case có nguồn; giả thuyết được gắn nhãn.
- [ ] Không có chi tiết riêng tư hoặc dữ liệu khách chưa được phép.
- [ ] Đúng đại từ, cách gọi audience và brand voice đã chọn.
- [ ] Có ví dụ/demo/việc làm ngay, không chỉ có lý thuyết.
- [ ] Thời lượng thoại phù hợp; mặc định 130–160 từ/phút.
- [ ] Video và bài Facebook cùng big idea, lời hứa, proof, ranh giới và CTA.
- [ ] Bài Facebook có đủ CẢNH–NGHẼN–ĐỔI–HỆ–LÀM–CHỐT nhưng không lộ nhãn framework trong bản đăng.
- [ ] Bài Facebook giải thích sâu mindset và cách làm, không phải transcript được kéo dài.
- [ ] Phần mở rộng không tạo claim hoặc câu chuyện mới thiếu nguồn.
- [ ] Bản Facebook sạch, dễ đọc và sẵn sàng sao chép để đăng.

Dùng `REVISE` nếu cần sửa chất lượng. Dùng `BLOCK` nếu thiếu nguồn cho claim mạnh hoặc quyền công khai chưa rõ; nêu chính xác thứ cần user xác nhận.

## Điều cấm

- Không sao chép hook, framework hoặc câu cửa miệng của Kallaway.
- Không đưa chi tiết nhạy cảm từ `Me.md`, nhật ký hoặc note khách hàng vào script hay bài Facebook chỉ vì chúng tạo cảm xúc mạnh.
- Không dùng “10x”, “thay đổi tất cả”, “không thể bỏ qua”, “khoa học chứng minh” nếu nguồn không đủ.
- Không lấy view hoặc viral làm mục tiêu duy nhất; ưu tiên giữ đúng ICP và tạo tin cậy.
- Không xuất bản hoặc tự động đăng nội dung nếu user chỉ yêu cầu viết.
