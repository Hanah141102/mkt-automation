# Cẩm nang kiến trúc toàn hệ thống

Tài liệu tham chiếu chính. Đọc một lần để hiểu vì sao hệ thống được xếp như vậy, rồi quay lại tra khi cần.

---

## Phần 1 — Vì sao xếp như thế này

### Ba lớp, không phải sáu thư mục

Sáu thư mục ở tầng gốc thực chất chỉ là **ba loại thứ khác nhau**. Lẫn lộn ba loại này là nguyên nhân của gần như mọi vướng mắc khi dùng.

| Lớp | Thư mục | Bản chất | Tần suất chạm |
|---|---|---|---|
| **Cái máy** | `10. Hệ Điều Hành` | Phần mềm chứa dữ liệu doanh nghiệp | Mỗi ngày |
| **Dụng cụ** | `30. Thư Viện Skill` | 282 trợ lý AI, mỗi cái một việc | Khi cần |
| **Hướng dẫn** | `00` · `20` · `40` · `50` | Bản đồ, khung 12 bước, bài mẫu, lộ trình | Khi bắt đầu và khi bí |

Một cách nhớ: **máy để chạy, dụng cụ để cầm, hướng dẫn để đọc.** Ba thứ này không thay thế cho nhau. Đọc hết hướng dẫn mà không mở máy thì không có gì xảy ra.

### Vì sao xếp theo tầng, không theo phòng ban

Đây là lựa chọn có chủ đích, và nó trả lời một câu hỏi thường gặp: *"sao không xếp Marketing / Kinh doanh / Nhân sự cho dễ?"*

Ba lý do:

1. **Khoá chuyển giao cần thứ tự.** Mở thư mục `Marketing` và `Nhân sự` cạnh nhau, không ai biết làm cái nào trước. Cây theo tầng thì rõ: cài máy → học khung → dùng dụng cụ → nghiệm thu.
2. **Doanh nghiệp nhỏ chưa có phòng ban.** Đội 5 người, một người kiêm ba vai. Cây phòng ban khiến họ thấy hệ thống không dành cho mình.
3. **Nhiều việc xuyên phòng ban.** Một cú ra mắt chạm marketing, bán hàng, vận hành, tài chính cùng lúc.

**Nhưng tư duy phòng ban vẫn hữu ích** — nên nó nằm ở đúng chỗ: **16 nhóm chức năng bên trong `30. Thư Viện Skill`**. Ở đó, người làm marketing mở nhóm 03–06, người làm sale mở nhóm 07–08, kế toán mở nhóm 13. Phòng ban là **lớp chỉ mục**, không phải lớp thư mục gốc.

### Vì sao có cổng "Xong"

Mỗi bước trong khung 12 bước có một cổng. Chưa qua cổng thì chưa sang bước sau.

Cổng tồn tại vì **ràng buộc phụ thuộc là thật**: Bước 06 (nội dung) lấy giọng thương hiệu từ Bước 02; Bước 07 (quảng cáo) lấy offer từ Bước 04; Bước 11 (đo lường) lấy chỉ số từ những bước trước. Bỏ qua một bước không phải là đi nhanh hơn — là xây tiếp trên nền rỗng.

Ba lỗi phổ biến nhất đều là lỗi nhảy cóc:
- Làm content khi chưa biết viết cho ai
- Chạy quảng cáo khi offer chưa ai mua
- Tuyển sale khi chưa có kịch bản để họ đọc

---

## Phần 2 — Bản đồ toàn bộ

```
AI Business OS — Khóa Chuyển Giao/
│
├─ README.md                          ← tóm tắt 1 trang
│
├─ 00. Bắt Đầu Từ Đây/                ← ĐỌC TRƯỚC TIÊN
│   ├─ 00 — Bạn Đang Cầm Gì           ← 6 thư mục dùng để làm gì
│   ├─ 01 — Đi Theo Thứ Tự Nào        ← ngày đầu, tuần đầu, 8 tuần
│   ├─ 02 — Team Nhỏ Vận Hành Thế Nào ← phân vai, nhịp họp, quyền sửa file
│   └─ 03 — Cẩm Nang Kiến Trúc        ← bạn đang ở đây
│
├─ 10. Hệ Điều Hành/                  ← CÁI MÁY
│   ├─ 00 — Hướng Dẫn Cài Đặt         ← 30 phút, 6 bước
│   └─ Vault Doanh Nghiệp/            ← copy về máy, mở bằng Obsidian
│       ├─ CLAUDE.md                  ← quy tắc bắt buộc, AI đọc đầu tiên
│       ├─ .claude/skills/            ← 35 trợ lý đang bật
│       ├─ 00. Business Context/      ← HỒ SƠ DOANH NGHIỆP (nền, ít đổi)
│       ├─ 01. Inbox/                 ← ghi thô, cuối ngày dọn về 0
│       ├─ 02. Projects/              ← việc CÓ deadline
│       ├─ 03. Areas/                 ← VẬN HÀNH HẰNG NGÀY
│       ├─ 04. Resources/             ← tái sử dụng: playbook, nghiên cứu
│       ├─ 05. Archive/               ← đã đóng, không xoá
│       ├─ People/ Companies/         ← khách và công ty thật
│       ├─ Meetings/ Decisions/       ← biên bản và quyết định
│       ├─ Daily/ Nhật Ký CEO/        ← nhật ký công việc và cá nhân
│       └─ MOC/                       ← mục lục sống
│
├─ 20. Khung Vận Hành A-Z/            ← HƯỚNG DẪN: LÀM GÌ TRƯỚC
│   ├─ 00 — Bản Đồ A-Z                ← 12 bước + luồng phụ thuộc
│   └─ 01…12/ Bước NN.md              ← mỗi bước: đầu vào · việc · skill · đầu ra · cổng Xong
│
├─ 30. Thư Viện Skill/                ← DỤNG CỤ
│   ├─ 00 — Cách Dùng Thư Viện
│   ├─ 00 — Tôi Muốn Làm Gì           ← tra theo tình huống
│   ├─ 00 — Bảng Tra Toàn Bộ Skill    ← 282 skill, có phân nhóm
│   ├─ viet-hoa-hang-loat.sh          ← dịch thân skill sang tiếng Việt
│   ├─ ⭐ Cốt Lõi/                     ← 34 skill đã bật sẵn
│   ├─ 01…15/                         ← 16 nhóm chức năng (lớp "phòng ban")
│   └─ _Kho Skill/                    ← file gốc 282 skill
│
├─ 40. Bài Mẫu — Công Ty Demo/        ← HƯỚNG DẪN: "XONG" TRÔNG THẾ NÀO
│   ├─ 00 — Đọc Trước                 ← cảnh báo dữ liệu hư cấu
│   └─ 00…99/                         ← 50 tài liệu theo đúng 12 bước
│
└─ 50. Triển Khai 90 Ngày/            ← HƯỚNG DẪN: THEO DÕI VÀ NGHIỆM THU
    ├─ 00 — Lộ Trình 8 Tuần
    ├─ 01 — Checklist Nghiệm Thu      ← 40 mục, chấm điểm
    └─ 02 — Biên Bản Bàn Giao
```

---

## Phần 3 — Luồng dữ liệu: điều làm nó thành một hệ điều hành

Đây là phần quan trọng nhất của cẩm nang. Một thư mục chứa tài liệu thì không phải hệ điều hành. Cái làm nó thành hệ điều hành là **dữ liệu chảy thành vòng khép kín**.

```
        ┌─────────────────────────────────────────────────────┐
        │                                                     │
        ▼                                                     │
┌───────────────────┐                                         │
│ 00. Business      │  Ai mình là · bán cho ai · giọng gì      │
│    Context        │  ← NỀN, ít đổi, mọi thứ đọc ngược về đây │
└─────────┬─────────┘                                         │
          │ AI đọc để có ngữ cảnh                             │
          ▼                                                   │
┌───────────────────┐                                         │
│  Skill            │  282 trợ lý, mỗi cái một việc            │
│  (.claude/skills) │                                         │
└─────────┬─────────┘                                         │
          │ tạo ra kết quả                                    │
          ▼                                                   │
┌───────────────────┐                                         │
│ 03. Areas         │  Content đã đăng · pipeline · CSKH       │
│ People/Meetings   │  ← VẬN HÀNH, đổi hằng ngày               │
└─────────┬─────────┘                                         │
          │ sinh ra số liệu                                   │
          ▼                                                   │
┌───────────────────┐                                         │
│ Analytics &       │  Bài nào chạy tốt · kênh nào ra đơn      │
│ Reporting         │  · khách rơi ở khúc nào                  │
└─────────┬─────────┘                                         │
          │ phân tích → kết luận                              │
          ▼                                                   │
┌───────────────────┐                                         │
│ Decisions/        │  Đổi giá · đổi kênh · đổi thông điệp     │
└─────────┬─────────┘                                         │
          │ cập nhật ngược lại nền                            │
          └─────────────────────────────────────────────────────┘
```

**Đọc vòng này theo một ví dụ thật:**

1. Bạn khai báo trong `00. Business Context/` rằng khách chính là phụ nữ 25–40 đi làm, giọng thương hiệu ấm áp và gần gũi.
2. Marketing gõ `/blog-post`. AI đọc hai file đó, viết bài đúng đối tượng và đúng giọng — **không phải hỏi lại bạn**.
3. Bài đăng xong lưu vào `03. Areas/Brand & Content/Content Đã Đăng/` kèm ghi chú trụ cột và câu móc.
4. Cuối tuần ghi số vào `Analytics & Reporting/`. Thấy bài dạng "kể chuyện khách" có lượt tương tác gấp ba bài dạng "giới thiệu sản phẩm".
5. Ghi vào `Decisions/`: chuyển 60% ngân sách nội dung sang dạng kể chuyện.
6. Cập nhật `00. Business Context/` — trụ cột nội dung đổi. Từ đây mọi bài viết sau đều theo hướng mới.

**Vòng này khép kín là lúc hệ thống bắt đầu tự tốt lên.** Vòng hở ở bất kỳ chỗ nào thì nó chỉ còn là một thư mục chứa file.

### Ba chỗ vòng hay bị đứt

| Đứt ở đâu | Triệu chứng | Sửa bằng |
|---|---|---|
| Không khai báo Business Context | AI hỏi lại mọi thứ, kết quả chung chung | `/mo-hinh-kinh-doanh` + `/hoan-tat-business-context` |
| Làm xong không ghi vào Areas | Không biết tháng trước đã làm gì | Kỷ luật ghi cuối ngày, Inbox về 0 |
| Có số nhưng không ai đọc | Số liệu nằm đó, quyết định vẫn theo cảm tính | Họp tuần 45 phút, nghị trình cố định |

---

## Phần 4 — Quy ước bắt buộc

### Đọc ở đâu, ghi vào đâu

| Việc | Đọc từ | Ghi vào |
|---|---|---|
| Viết content, quảng cáo, email | `Brand Voice` + `Chân Dung Doanh Nghiệp` | `03. Areas/Brand & Content/Content Đã Đăng/` |
| Báo giá, đóng gói offer | `Sản Phẩm & Dịch Vụ/` + `Business Model Canvas` | `00. Business Context/Sản Phẩm & Dịch Vụ/` |
| Bán hàng, chăm khách | `04. Resources/Playbooks/` (kịch bản) | `People/` · `Meetings/` · `Sales Pipeline & CRM/` |
| Nghiên cứu đối thủ, thị trường | Nguồn công khai | `04. Resources/Market & Competitor Research/` |
| Ghi số liệu | Nền tảng quảng cáo, web, chat | `03. Areas/Analytics & Reporting/` (chọn đúng miền) |
| Quyết định giá, ngân sách, kênh | Số liệu + phân tích | `Decisions/` — chủ DN xác nhận trước |
| Việc đã đóng | | `05. Archive/` — chuyển vào, **không xoá** |

### Đặt tên file

| Loại | Mẫu |
|---|---|
| Content đã đăng | `YYYY-MM-DD — [Kênh] — [Tên bài].md` |
| Biên bản | `YYYY-MM-DD — [Kênh] — [Tên khách].md` |
| Quyết định | `YYYY-MM-DD — [Nội dung].md` |
| Dự án | `[YYYY-MM] [Tên chiến dịch].md` |
| Người | `[Họ Tên] — [Nguồn] (PK<số>).md` |
| Mục lục thư mục | `_MOC [Tên].md` |
| Bản mẫu | Tiền tố `[Mẫu]` — copy ra rồi bỏ tiền tố |

### Năm nguyên tắc không được phá

1. **Không note mồ côi.** Mọi note link ra ít nhất một note khác.
2. **Không bịa số liệu.** Không có dữ liệu thì ghi "chưa có dữ liệu".
3. **Tách fact / suy luận / giả định** khi phân tích.
4. **Không xoá.** Chuyển sang `05. Archive/`.
5. **Quyết định về tiền phải có xác nhận của chủ doanh nghiệp** trước khi ghi vào `Decisions/`.

---

## Phần 5 — 12 bước: ai làm, vào ra cái gì

| Bước | Ai chủ trì | Đầu vào | Đầu ra chính | Cổng "Xong" |
|:--:|---|---|---|---|
| 01 | **Chủ DN** | Quyết định của chủ DN | Phân quyền, sổ `Decisions/` | Không còn hai file cùng tự nhận là bản chuẩn |
| 02 | **Chủ DN** | Hiểu biết về ngành và khách | `Chân Dung DN`, `Brand Voice`, BMC | Đọc là biết bán gì cho ai |
| 03 | **Chủ DN** | Định vị + nguồn công khai | Báo cáo thị trường, hồ sơ đối thủ | Mỗi kết luận có ≥3 nguồn |
| 04 | **Chủ DN** | Chân dung khách + năng lực thật | Hồ sơ sản phẩm có giá | Biết bán bao nhiêu thì hoà vốn |
| 05 | Chủ DN + Sale | Offer + kênh đang có | Sơ đồ phễu, mồi thu lead, landing page | Mỗi bước phễu có 1 người + 1 chỉ số |
| 06 | Marketing | Định vị + brand voice | Trụ cột nội dung, lịch 30 ngày | Mọi bài gắn được phân khúc, tầng phễu, CTA |
| 07 | Marketing | Phễu đã chạy tự nhiên | Kế hoạch quảng cáo, bộ creative | Có ngưỡng dừng viết sẵn **trước khi** bật |
| 08 | Sale | Lead + offer | Kịch bản 3 kênh, luật phân bổ, pipeline | Chủ DN không còn phải tự chốt đơn thường |
| 09 | Vận hành | Đơn đã chốt | Quy trình giao hàng, luồng đón khách | Người khác làm thay mà chất lượng không tụt |
| 10 | CSKH | Khách đã dùng sản phẩm | Vòng đời khách, kho chứng thực | Biết dấu hiệu khách sắp rời |
| 11 | Người phụ trách số | Toàn bộ hoạt động 05–10 | Tracking, dashboard, báo cáo | Nối được nguồn → lead → khách → doanh thu |
| 12 | **Chủ DN** | Dữ liệu + phản hồi | Backlog cải tiến, quy trình mới | Kiến thức nằm trong vault, không trong đầu ai |

**Bốn bước in đậm là việc của chủ doanh nghiệp, không giao được.** Bước 01–04 vì chỉ bạn biết công ty này là gì; Bước 12 vì chỉ bạn quyết được thay đổi gì cho chu kỳ sau.

---

## Phần 6 — CEO và team kết hợp thế nào

### Ba chế độ làm việc

Hệ thống chạy ở ba chế độ khác nhau tuỳ giai đoạn. Nhầm chế độ là nguồn gốc của hầu hết trục trặc.

**Chế độ 1 — CEO độc thoại với AI (tuần 1–3)**

Bạn ngồi một mình với Claude. AI phỏng vấn, bạn trả lời, AI ghi vào `00. Business Context/`.

Không có team trong chế độ này. Nếu không biết trả lời, nói **"bạn hỏi tôi đi"** — AI sẽ hỏi từng câu một.

**Chế độ 2 — CEO đối thoại với team, AI ghi biên (tuần 4 trở đi)**

Đây là chế độ chính khi vận hành. Cách chạy trong buổi họp:

```
CEO hỏi team:      "Tuần rồi lead về bao nhiêu, chốt được mấy?"
Team trả lời:      số liệu từ pipeline
CEO hỏi tiếp:      "Sao tỷ lệ chốt tụt so với tháng trước?"
Team đưa giả thuyết
→ Người có tài khoản Claude gõ: /mkt-marketing-performance-analysis
→ AI đọc số trong vault, đưa phân tích và các nguyên nhân khả dĩ
CEO quyết:         chọn một hướng
→ Gõ: ghi quyết định này vào Decisions/
```

**Điểm mấu chốt:** AI không thay CEO quyết định, và không thay team làm việc. Nó **rút ngắn khoảng cách từ câu hỏi tới dữ liệu**. Việc trước đây mất ba ngày tổng hợp báo cáo giờ mất ba phút.

**Chế độ 3 — Team tự chạy, CEO chỉ duyệt (từ tháng 3)**

Team gõ skill trực tiếp, làm ra kết quả, CEO chỉ duyệt những thứ chạm vào tiền và thương hiệu. Đây là đích đến.

### Bảng phân quyền quyết định

| Loại việc | Team tự làm | Cần CEO duyệt |
|---|---|---|
| Viết bài, caption, email | ✓ | |
| Đăng nội dung theo lịch đã duyệt | ✓ | |
| Nhắn khách, chốt đơn theo bảng giá | ✓ | |
| Cập nhật pipeline, ghi biên bản | ✓ | |
| Đổi giá, giảm giá ngoài khung | | ✓ |
| Tăng hoặc dừng ngân sách quảng cáo | | ✓ |
| Đổi thông điệp chính, đổi định vị | | ✓ |
| Ra sản phẩm mới, đóng gói lại offer | | ✓ |
| Tuyển, cho nghỉ, đổi cơ chế thưởng | | ✓ |
| Cam kết với khách ngoài phạm vi hợp đồng | | ✓ |

Bảng này nên được copy vào `Decisions/` ngay tuần 2, có chữ ký của cả đội.

### Bốn câu CEO nên hỏi mỗi tuần

Không cần hỏi nhiều. Bốn câu này phủ hết:

1. **"Tuần rồi số nào tốt lên, số nào xấu đi?"** → team đọc từ `Analytics & Reporting/`
2. **"Cái xấu đi đó do đâu?"** → gõ `/mkt-marketing-root-cause` nếu chưa rõ
3. **"Tuần này ba việc quan trọng nhất là gì?"** → team đề xuất, CEO chốt
4. **"Có gì đang tắc mà cần tôi gỡ không?"** → thường là quyết định về tiền

---

## Phần 7 — Chẩn đoán khi hệ thống trục trặc

| Triệu chứng | Nguyên nhân thật | Sửa ở đâu |
|---|---|---|
| AI trả lời chung chung, không giống công ty mình | `00. Business Context/` chưa điền hoặc điền hời hợt | Bước 02 — chạy lại `/hoan-tat-business-context` |
| AI trả lời bằng tiếng Anh | `CLAUDE.md` bị xoá hoặc đứng ngoài thư mục vault | Kiểm tra file `CLAUDE.md`, chạy `claude` **trong** vault |
| Gõ `/tên-skill` không nhận | Skill chưa bật, hoặc đứng sai thư mục | Copy skill từ `_Kho Skill/` vào `.claude/skills/` |
| AI chậm, hay nhầm skill | Bật quá nhiều skill | Giữ dưới 60 skill trong `.claude/skills/` |
| Không biết tháng trước làm gì | Không ghi vào `03. Areas/` | Kỷ luật ghi cuối ngày |
| Có số nhưng quyết định vẫn cảm tính | Không họp tuần, hoặc họp mà không quyết | Nghị trình họp tuần 45 phút |
| Hai người cùng gọi một khách | Chưa có luật phân bổ lead | Bước 08 — `/phan-bo-va-cham-diem-lead` |
| Người mới mất 3 tháng mới bán được | Chưa có kịch bản và lộ trình kèm | Bước 08 — `/sales-script` + `/quan-ly-doi-sale` |
| Content viết ra không ai nhớ | Làm Bước 06 khi chưa xong Bước 02 | Quay lại Bước 02 |
| Quảng cáo càng chạy càng lỗ | Làm Bước 07 khi chưa xong Bước 04 | Quay lại Bước 04 |
| CEO nghỉ một tuần là mọi thứ đứng | Kiến thức nằm trong đầu, không trong vault | Bước 12 — `/sop-builder` |

---

## Phần 8 — Bảng tra nhanh: tôi đang ở đâu, mở file nào

| Tình huống | Mở file |
|---|---|
| Chưa biết gì, mới nhận bộ này | [[00 — Bạn Đang Cầm Gì]] |
| Muốn biết làm gì trước, làm gì sau | [[01 — Đi Theo Thứ Tự Nào]] |
| Có team, muốn biết phân vai và nhịp họp | [[02 — Team Nhỏ Vận Hành Thế Nào]] |
| Muốn thấy một CEO dùng thật trông thế nào | [[04 — Diễn Mẫu Một CEO Dùng Hệ Thống]] |
| Chuẩn bị cài lên máy | `10. Hệ Điều Hành/00 — Hướng Dẫn Cài Đặt` |
| Đang làm một bước, không rõ phải ra cái gì | `20. Khung Vận Hành A-Z/…/Bước NN.md` |
| Cần một việc cụ thể, không biết dùng skill nào | [[00 — Tôi Muốn Làm Gì]] |
| Muốn xem toàn bộ skill có gì | [[00 — Bảng Tra Toàn Bộ Skill]] |
| Không hình dung được "xong" trông thế nào | `40. Bài Mẫu — Công Ty Demo/00 — Đọc Trước` |
| Muốn theo dõi tiến độ 8 tuần | [[00 — Lộ Trình 8 Tuần]] |
| Chuẩn bị nghiệm thu, bàn giao | [[01 — Checklist Nghiệm Thu]] |
| Hệ thống trục trặc | Phần 7 của chính tài liệu này |

---

## Phần 9 — Mục tiêu cuối cùng

Toàn bộ kiến trúc này phục vụ đúng một mục tiêu, và nó không phải "có nhiều tài liệu hơn":

> **Kiến thức vận hành doanh nghiệp nằm trong hệ thống, không nằm trong đầu một người.**

Ba dấu hiệu cho biết đã đạt:

1. Khi cần thông tin về khách, cả đội **mở vault ra tra** thay vì nhắn hỏi nhau.
2. Người mới vào **đọc vault là làm được**, không cần ai kèm giải thích.
3. **Chủ doanh nghiệp nghỉ một tuần, việc vẫn chạy.**

Nếu sau 90 ngày ba điều này chưa đúng, hệ thống chưa hoàn thành nhiệm vụ — dù tài liệu có đầy đủ tới đâu.
