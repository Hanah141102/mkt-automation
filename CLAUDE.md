# CLAUDE.md — Quy ước bắt buộc khi làm việc trong vault này

Claude đọc file này **trước tiên**, trước cả khi chạy bất kỳ skill nào.

> Đây trước hết là vault Obsidian (Markdown + `.canvas` + `.base`). Repo vẫn giữ một lớp runtime kỹ thuật cho xưởng video AI (`package.json`, `scripts/`, `workspace/` và các đường dẫn tương thích `videos/`, `research/`). Khi làm note, tuân theo quy ước vault; khi sửa pipeline, đọc thêm `AGENTS.md` và hướng dẫn trong dự án video tương ứng.

---

## 0. QUY TẮC NGÔN NGỮ — ƯU TIÊN CAO NHẤT

**Mọi thứ Claude nói ra và mọi file Claude tạo trong vault này đều bằng TIẾNG VIỆT.**

Cụ thể:

- Trả lời người dùng: tiếng Việt.
- Nội dung file tạo mới (`.md`, `.canvas`, `.base`): tiếng Việt.
- Tiêu đề, heading, tên cột bảng, nhãn biểu đồ: tiếng Việt.
- Tên file: tiếng Việt có dấu, theo quy ước ở mục 4.

**Quan trọng — file skill viết bằng tiếng Anh không có nghĩa là kết quả phải tiếng Anh.** Một số skill trong `.claude/skills/` còn phần hướng dẫn nội bộ bằng tiếng Anh. Đó chỉ là *hướng dẫn cho Claude*. **Đầu ra luôn phải là tiếng Việt.** Nếu một skill yêu cầu xuất ra tiếng Anh, bỏ qua yêu cầu đó và xuất tiếng Việt.

Ngoại lệ duy nhất được giữ nguyên tiếng Anh:

- Thuật ngữ đã thành chuẩn không có từ Việt tương đương gọn hơn: `SEO`, `ROAS`, `CPM`, `CTR`, `CTA`, `landing page`, `email`, `webinar`, `pipeline`.
- Mã skill (`/blog-post`), tên trường frontmatter (`tags`, `type`), tên file cấu hình.
- Đoạn mã, tên hàm, URL, mã màu.

Viết cho **chủ doanh nghiệp Việt Nam**: câu ngắn, không dịch máy, không sính chữ. Nếu buộc dùng thuật ngữ tiếng Anh lần đầu, mở ngoặc giải thích một lần rồi thôi.

---

## 1. Vault này là gì

Vault Obsidian PARA + AI Brain cho **DUY NHẤT 1 doanh nghiệp**. Mọi nội dung (khách hàng, đối thủ, sản phẩm, chiến dịch) đều thuộc về một công ty duy nhất.

**Không** tạo thư mục công ty con. Một công ty được phép có nhiều dòng sản phẩm và nhiều phân khúc — mỗi thứ là một file riêng trong cùng `00. Business Context/`.

Kiến trúc đầy đủ: [[Vault SME — Hướng Dẫn]].

## 2. Nguồn sự thật — đọc TRƯỚC khi làm bất cứ việc gì

Toàn bộ ngữ cảnh doanh nghiệp nằm ở **`00. Business Context/`**. Đây là nguồn sự thật duy nhất.

| File | Nội dung | Đọc khi |
|---|---|---|
| `Hồ Sơ Mô Hình Kinh Doanh.md` | **6 tham số điều khiển toàn hệ thống** | **ĐỌC ĐẦU TIÊN, trước mọi khuyến nghị có ngưỡng thời gian, nhịp đo, hoặc thiết kế phễu** |
| `Chân Dung Doanh Nghiệp.md` | Định vị, khách hàng lý tưởng | Mọi việc marketing/bán hàng |
| `Brand Voice — Giọng Thương Hiệu.md` | Giọng nói, từ nên/tránh, câu mẫu | Viết content, ads, email |
| `Business Model Canvas — [Tên].md` | 9 khối mô hình kinh doanh | Tư vấn giá, đóng gói offer |
| `MHKD/Phân Khúc Khách Hàng/PK*.md` | Chi tiết từng nhóm khách | Xác định viết cho ai |
| `MHKD/Giá Trị Cốt Lõi/GT*.md` | Chi tiết từng giá trị bán | Làm thông điệp |
| `Sản Phẩm & Dịch Vụ/` | Hồ sơ từng gói: tính năng, **giá**, USP | Báo giá, viết bán hàng |
| `Chân Dung CEO — [Tên].md` | Thương hiệu cá nhân người sáng lập | Khi thương hiệu gắn với CEO |
| `AI-Sale-Assistant.md` | AI được và không được tự làm gì | Trước khi tự động hoá |

**Nếu file nào còn là bản mẫu trống:** báo cho người dùng biết đang thiếu ngữ cảnh gì và gợi ý chạy `/mo-hinh-kinh-doanh` rồi `/hoan-tat-business-context`. **Tuyệt đối không bịa** thông tin về doanh nghiệp.

Khi viết content cho thương hiệu cá nhân: đọc thêm `Nhật Ký CEO/` để lấy chuyện thật và quan điểm riêng. Chỉ dùng mục có `rieng_tu: no`; ưu tiên đoạn gắn `#hat-giong-content`, `#cau-chuyen`, `#quan-diem`.

## 2b. Không dùng ngưỡng cứng

Hệ thống **không có con số thời gian cố định nào**. Mọi ngưỡng tính từ `chu-ky-ban-ngay`:

| Việc | Công thức |
|---|---|
| Giữ lead tối đa | 1,5 × chu kỳ bán |
| Chạm lead nóng | 15 phút nếu chu kỳ < 30 ngày · 4 giờ nếu ≥ 30 ngày |
| Nhắc lại sau báo giá | 5% · 15% · 30% chu kỳ bán |
| Nhịp đọc số | < 30 ngày: tuần · 30–90: hai tuần · > 90: tháng |

Nếu `Hồ Sơ Mô Hình Kinh Doanh.md` chưa được điền, **hỏi người dùng chu kỳ bán trước khi đưa ra bất kỳ ngưỡng nào**. Đừng mặc định 14 ngày.

## 3. Ghi kết quả vào đâu

Đọc ở `00. Business Context/`. **Ghi** vào đúng chỗ dưới đây — không đổ hết vào `01. Inbox/`.

| Loại kết quả | Ghi vào |
|---|---|
| Content đã viết/đăng | `03. Areas/Brand & Content/Content Đã Đăng/` |
| Số liệu, báo cáo đo lường | `03. Areas/Analytics & Reporting/` (chọn đúng miền) |
| Trạng thái deal, pipeline | `03. Areas/Sales Pipeline & CRM/` |
| Kênh marketing đang chạy | `03. Areas/Marketing Channels/` |
| Chăm sóc sau bán | `03. Areas/Customer Success & Retention/` |
| Khách, lead, đối tác (từng người) | `People/` — ghi rõ thuộc phân khúc nào |
| Công ty khách, đối thủ, nhà cung cấp | `Companies/` |
| Biên bản gặp khách | `Meetings/` — bắt buộc link tới `People/` + `Companies/` |
| Quyết định giá, kênh, ngân sách | `Decisions/` — cần chủ doanh nghiệp xác nhận trước |
| Chiến dịch CÓ deadline | `02. Projects/` |
| Nghiên cứu đối thủ, thị trường | `04. Resources/Market & Competitor Research/` |
| Chứng thực, review, case study | `04. Resources/Feedback & Chứng Thực/` |
| Nhật ký cá nhân CEO | `Nhật Ký CEO/` |
| Nhật ký công việc hằng ngày | `Daily/` |
| Việc đã đóng | `05. Archive/` — chuyển vào, **không xoá** |

## 3b. Ghi nhanh — dùng skill thay vì gõ tay bốn chỗ

Sau mỗi lần trao đổi với khách, **đừng bắt người dùng gõ bốn chỗ**. Gợi ý họ dùng `/ghi-cuoc-gap` — kể lại bằng lời tự nhiên, skill tự tạo biên bản, cập nhật hồ sơ khách, chuyển trạng thái pipeline và lưu câu khách nói vào thư viện.

Ma sát ghi chép là nguyên nhân số một khiến hệ thống chết. Luôn chọn đường ít gõ nhất cho người dùng.

## 4. Quy ước đặt tên file

- Content đã đăng: `YYYY-MM-DD — [Kênh] — [Tên bài].md`
- Biên bản họp: `YYYY-MM-DD — [Loại] — [Đối tượng].md`
- Quyết định: `YYYY-MM-DD — [Nội dung quyết định].md`
- Dự án: `[YYYY-MM] [Tên chiến dịch].md`
- Người: `[Họ Tên] — [Vai trò] (PK<số>).md`
- Mục lục của thư mục: `_MOC [Tên thư mục].md`
- Bản mẫu: đặt tiền tố `[Mẫu]` — copy ra rồi bỏ tiền tố khi dùng thật

## 5. Nguyên tắc bắt buộc

1. **Không note mồ côi.** Mọi note phải link ra ít nhất một note khác. Biên bản `Meetings/` phải link tới `People/` + `Companies/` + dự án liên quan.
2. **Không bịa số liệu.** Không có dữ liệu thì ghi rõ "chưa có dữ liệu" và hỏi người dùng. Không tự chế con số cho đẹp báo cáo.
3. **Tách fact / suy luận / giả định.** Khi phân tích, đánh dấu rõ đâu là số liệu thật, đâu là suy luận của Claude, đâu là giả định chưa kiểm chứng.
4. **Không xoá.** Việc đã xong thì chuyển sang `05. Archive/`.
5. **Quyết định về giá, ngân sách, cam kết với khách** — luôn hỏi xác nhận chủ doanh nghiệp trước khi ghi vào `Decisions/`.
6. **Tiền tệ mặc định là VND.** Nếu skill gốc dùng USD, quy đổi hoặc ghi rõ đơn vị. Định dạng số theo kiểu Việt Nam (1.000.000 đ).

## 6. Skill

97 skill vận hành đã bật sẵn trong `.claude/skills/`. Gọi bằng `/tên-skill`, hoặc chỉ cần mô tả việc muốn làm bằng tiếng Việt — Claude tự nhận skill phù hợp.

Không chắc dùng skill nào? Gọi `/fullstack-marketing-operator` — skill này điều phối và chỉ đường sang skill đúng.

**Kho dự phòng hiện có 301 skill** tại `huong dan/30. Thư Viện Skill/_Kho Skill/`. Muốn bật thêm: copy thư mục skill đó vào `.claude/skills/` rồi khởi động lại Claude. Tra skill bằng tiếng Việt: mở `huong dan/30. Thư Viện Skill/00 — Bảng Tra Toàn Bộ Skill.md`.

> Đừng bật thêm hàng loạt. Mỗi skill hoạt động đều chiếm bộ nhớ ngữ cảnh; chỉ bật skill bổ sung khi có nhu cầu rõ ràng.

## 7. Nếu skill yêu cầu file không tồn tại

Vài skill nhập từ thư viện nước ngoài sẽ tìm file kiểu `.agents/product-marketing.md`. Vault này **không dùng đường dẫn đó**. Khi gặp, đọc thay bằng `00. Business Context/Chân Dung Doanh Nghiệp.md` + `Business Model Canvas — [Tên].md` và coi là tương đương. Đừng hỏi lại người dùng thông tin đã có sẵn trong đó.
