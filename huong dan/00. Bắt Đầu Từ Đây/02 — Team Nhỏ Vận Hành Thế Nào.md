# Team nhỏ vận hành hệ thống này thế nào

Dành cho chủ doanh nghiệp có đội 3–8 người. Trả lời ba câu: **ai làm gì**, **lúc nào làm**, **dùng chung vault ra sao**.

---

## 1. Sự thật đầu tiên: 3 tuần đầu không giao được cho ai

Đây là chỗ hầu hết chủ doanh nghiệp làm hỏng. Mua hệ thống về, giao cho bạn marketing "em nghiên cứu rồi triển khai đi", ba tuần sau nhận lại một đống tài liệu chung chung.

**Bước 02 (Định vị), Bước 03 (Nghiên cứu), Bước 04 (Offer & Giá) là việc của bạn.** Không phải vì bạn giỏi hơn, mà vì:

- Chỉ bạn biết vì sao khách chọn mình thay vì đối thủ
- Chỉ bạn quyết được giá và biết bán bao nhiêu thì có lãi
- Chỉ bạn biết công ty này thật sự muốn thành cái gì

Nhân viên có thể *hỗ trợ* thu thập dữ liệu, nhưng **người ngồi trả lời câu hỏi của Claude phải là bạn**. Ba tuần này bạn bỏ ra khoảng 12–15 giờ. Đổi lại, 5 tuần sau đội bạn làm việc mà không cần hỏi lại bạn từng câu.

Từ **Bước 05 trở đi** thì giao được, và nên giao.

---

## 2. Phân vai theo quy mô đội

### Đội 3 người (chủ DN + 2)

| Vai | Ai | Phụ trách bước |
|---|---|---|
| **Người giữ hệ thống** | Chủ DN | 01 · giữ vault sạch · duyệt `Decisions/` |
| **Chủ doanh nghiệp** | Bạn | 02 · 03 · 04 · 12 |
| **Marketing kiêm nội dung** | Người 1 | 05 · 06 · 07 · 11 |
| **Sale kiêm chăm sóc** | Người 2 | 08 · 09 · 10 |

### Đội 5 người

| Vai | Phụ trách bước |
|---|---|
| Chủ DN | 01 · 02 · 03 · 04 · duyệt `Decisions/` |
| Marketing/Content | 06 |
| Chạy quảng cáo | 07 · 11 (phần số quảng cáo) |
| Sale | 05 (phễu) · 08 |
| Vận hành/CSKH | 09 · 10 · giữ vault sạch |
| *(luân phiên)* | 12 — mỗi tháng một người chủ trì buổi rút kinh nghiệm |

### Đội 8 người

Giữ nguyên bảng trên, tách thêm:
- Một người **chuyên số liệu** ôm trọn Bước 11
- Một người **giữ hệ thống** toàn thời gian (không kiêm) — dọn Inbox, giữ quy ước đặt tên, nhắc mọi người ghi đúng chỗ

> **Quy tắc bất di bất dịch:** mỗi bước có **đúng một người** chịu trách nhiệm. Hai người cùng chịu trách nhiệm nghĩa là không ai chịu trách nhiệm.

---

## 3. Ai cần tài khoản Claude, ai chỉ cần Obsidian

Đây là câu hỏi tốn tiền nhất, nên trả lời rõ:

| Vai trò | Cần gì | Vì sao |
|---|---|---|
| Chủ DN | **Claude Code + Obsidian** | Chạy các skill nặng ở Bước 02–04 |
| Marketing/Content | **Claude Code + Obsidian** | Chạy skill viết nội dung hằng ngày |
| Sale, CSKH, vận hành | **Chỉ Obsidian** | Chủ yếu đọc kịch bản, ghi biên bản, cập nhật pipeline |

**Đội 3–5 người thường chỉ cần 2 tài khoản Claude.** Người không có tài khoản vẫn đọc được toàn bộ tài liệu, kịch bản, quy trình trong Obsidian — họ chỉ không tự chạy skill được.

Khi họ cần một thứ do AI tạo (ví dụ sale cần thêm kịch bản xử lý một loại từ chối mới), họ ghi yêu cầu vào `01. Inbox/`, người có tài khoản chạy giúp trong buổi họp tuần.

---

## 4. Dùng chung vault thế nào

Chọn **một** trong hai, đừng trộn:

### Cách A — Google Drive / OneDrive (khuyên dùng cho ≤5 người)

Để nguyên thư mục vault trong Drive đã đồng bộ. Mọi người mở cùng một vault.

**Luật tránh xung đột — bắt buộc phổ biến cho cả đội:**
1. **Mỗi người chỉ sửa file thuộc bước mình phụ trách.** Marketing không sửa file trong `Sales Pipeline & CRM/`.
2. **Không hai người mở cùng một file cùng lúc.** Nếu cần, nhắn nhau trước.
3. **`00. Business Context/` chỉ chủ DN được sửa.** Người khác muốn góp ý thì ghi vào `01. Inbox/`.
4. Đợi biểu tượng đồng bộ xong rồi mới tắt máy.

### Cách B — Git + GitHub riêng tư (chuẩn hơn, cần một người biết Git)

Vault đã có sẵn `.gitignore`. Mỗi người `pull` đầu ngày, `push` cuối ngày. Hơn hẳn cách A ở chỗ có lịch sử thay đổi và khôi phục được khi làm hỏng.

Nếu trong đội không ai dùng Git thoải mái, **cứ dùng cách A** — đừng cố cho sang.

---

## 5. Nhịp vận hành

Đây là phần quyết định hệ thống sống hay chết. Không có nhịp thì sau 3 tuần vault thành nghĩa địa tài liệu.

### Hằng ngày — 10 phút/người, cuối ngày

| Ai | Làm gì |
|---|---|
| Tất cả | Ghi việc phát sinh vào `01. Inbox/` — chưa cần gọn, cần ghi |
| Sale | Sau mỗi cuộc gặp khách: `/ghi-cuoc-gap` — kể lại bằng lời, skill tự ghi 4 chỗ |
| Sale | Cập nhật trạng thái deal · gặp khách xong ghi biên bản vào `Meetings/` |
| Marketing | Bài đăng xong lưu vào `Content Đã Đăng/` kèm frontmatter trụ cột, định dạng, câu móc |
| Người giữ hệ thống | Dọn `01. Inbox/` về 0 — chuyển từng note về đúng thư mục |

> `01. Inbox/` cuối ngày phải trống. Đây là chỉ số sức khoẻ số một của hệ thống. Inbox tồn đọng một tuần nghĩa là hệ thống đã ngừng chạy.

### Hằng tuần — họp 45 phút, cố định một khung giờ

**Nghị trình cố định, không đổi:**

| Phút | Nội dung | Ai chủ trì |
|---|---|---|
| −10 | Chạy `/chuan-bi-hop-tuan` — sinh nghị trình từ số liệu thật | Người phụ trách Bước 11 |
| 0–10 | Đọc ba câu đáng bàn nhất | Người phụ trách Bước 11 |
| 10–20 | Chạy `/mkt-marketing-performance-analysis`, đọc kết quả | Người phụ trách Bước 11 |
| 20–35 | Số nào bất thường? Vì sao? Làm gì tuần tới? | Chủ DN |
| 35–42 | Chạy các skill được yêu cầu trong `01. Inbox/` tuần này | Người có tài khoản Claude |
| 42–45 | Chốt việc tuần sau, ai làm gì | Chủ DN |

Quyết định về giá, ngân sách, kênh → ghi ngay vào `Decisions/` trong buổi họp, chủ DN xác nhận.

### Hằng tháng — 90 phút

- Chạy `/retrospective`: bắt đầu gì, dừng gì, tiếp tục gì
- Việc nào làm tốt lặp lại lần hai → chạy `/sop-builder` biến thành quy trình
- Cập nhật backlog cải tiến: mỗi mục có người phụ trách và hạn chót
- Người giữ hệ thống rà: có note nào mồ côi không? có file nào hai bản không?

### Hằng quý — nửa ngày, chỉ chủ DN và 1–2 người chủ chốt

Quay lại Bước 02–04 với dữ liệu thật ba tháng vừa qua:

- Định vị còn đúng không? Khách thật có giống chân dung đã dựng không?
- Offer còn bán được không? Giá còn hợp lý không?
- Đối thủ có gì mới? → chạy lại `/mkt-phan-tich-doi-thu`

---

## 6. Hai tuần đầu — làm gì từng ngày

### Tuần 1 — chỉ mình bạn

| Ngày | Việc | Thời gian |
|---|---|---|
| T2 | Cài Obsidian + Claude Code, mở vault, sao lưu | 60 phút |
| T3 | Chạy `/mo-hinh-kinh-doanh` — trả lời hết 9 ô | 90 phút |
| T4 | Chạy `/hoan-tat-business-context` — điền nốt chỗ thiếu | 60 phút |
| T5 | Chạy `/brand-positioning-builder` + `/brand-voice-guide` | 90 phút |
| T6 | Đọc lại toàn bộ `00. Business Context/`, sửa chỗ chưa đúng | 45 phút |

> Không biết trả lời? Nói với Claude **"bạn hỏi tôi đi"** — nó sẽ phỏng vấn từng câu một.

### Tuần 2 — kéo đội vào

| Ngày | Việc | Ai |
|---|---|---|
| T2 | Họp 60 phút: đọc `Chân Dung Doanh Nghiệp` và `Brand Voice` cho cả đội nghe. Hỏi: có chỗ nào thấy không đúng thực tế không? | Cả đội |
| T2 | Chốt phân vai theo bảng ở Mục 2. Ghi vào `Decisions/` | Chủ DN |
| T3 | Cài Obsidian cho từng người, phổ biến 4 luật tránh xung đột ở Mục 4 | Người giữ hệ thống |
| T4 | Chạy `/mkt-phan-tich-doi-thu` cho 3 đối thủ gần nhất | Chủ DN |
| T5 | Họp tuần đầu tiên theo nghị trình ở Mục 5 — kể cả khi chưa có số liệu gì | Cả đội |

Hết tuần 2, đội bạn phải làm được ba việc: **mở vault**, **biết ghi vào thư mục nào**, **biết họp tuần diễn ra thế nào**.

---

## 7. Bảng phân quyền sửa file

In ra dán lên tường, hoặc lưu vào `Decisions/`:

| Thư mục | Ai được sửa | Ai chỉ đọc |
|---|---|---|
| `00. Business Context/` | Chủ DN | Tất cả |
| `01. Inbox/` | Tất cả | — |
| `02. Projects/` | Người phụ trách dự án đó | Tất cả |
| `03. Areas/Brand & Content/` | Marketing/Content | Tất cả |
| `03. Areas/Analytics & Reporting/` | Người phụ trách Bước 11 | Tất cả |
| `03. Areas/Sales Pipeline & CRM/` | Sale | Tất cả |
| `03. Areas/Customer Success & Retention/` | CSKH | Tất cả |
| `People/` `Companies/` `Meetings/` | Người trực tiếp gặp khách | Tất cả |
| `Decisions/` | Chủ DN (người khác đề xuất qua Inbox) | Tất cả |
| `Nhật Ký CEO/` | Chỉ chủ DN | Chỉ chủ DN |
| `.claude/skills/` | Người giữ hệ thống | Tất cả |

---

## 8. Bốn thứ làm hỏng hệ thống nhanh nhất

**1. Giao Bước 02–04 cho nhân viên.** Kết quả sẽ chung chung, và mọi thứ xây trên đó cũng chung chung theo.

**2. Bỏ họp tuần.** Bỏ hai tuần liên tiếp là hệ thống chết. Thà họp 20 phút còn hơn không họp.

**3. Để Inbox tồn đọng.** Note không được dọn về đúng chỗ thì Claude không tìm thấy, và AI trả lời như chưa từng biết doanh nghiệp bạn.

**4. Bật hết 282 skill "cho đủ bộ".** Claude sẽ chậm, hay nhầm skill và trả lời kém chính xác. Giữ dưới 60 skill hoạt động.

---

## 9. Bạn đang ở đâu — bảng tự chấm

Sau mỗi tháng, tự chấm:

| Dấu hiệu | Tốt | Đang hỏng |
|---|---|---|
| `01. Inbox/` cuối ngày | Trống | Tồn đọng nhiều ngày |
| Họp tuần | Diễn ra đều, có quyết định ghi vào `Decisions/` | Bỏ, hoặc họp mà không quyết gì |
| Khi cần thông tin về khách | Mở vault ra tra | Nhắn hỏi nhau qua Zalo |
| Người mới vào | Đọc vault là làm được | Phải có người kèm giải thích |
| Bạn nghỉ một tuần | Việc vẫn chạy | Mọi thứ đứng lại |

Ba dòng cuối là mục tiêu thật của cả hệ thống này: **kiến thức nằm trong vault, không nằm trong đầu bạn.**

---

→ Tiếp theo: [[00 — Bản Đồ A-Z]] để bắt đầu Bước 01 · [[00 — Lộ Trình 8 Tuần]] để xem toàn cảnh 8 tuần.
