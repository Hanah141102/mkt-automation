# Cách dùng thư viện skill

## Skill là gì

Một **skill** là một trợ lý AI chuyên một việc. Gõ `/tên-skill`, nó biết phải hỏi bạn gì, làm theo quy trình nào, và cho ra kết quả gì.

Ví dụ: gõ `/blog-post`, Claude sẽ hỏi từ khoá mục tiêu, dựng dàn ý cho bạn duyệt, viết bài, kèm thẻ mô tả và checklist kiểm tra trước khi đăng. Không cần bạn nhớ quy trình SEO.

Bạn cũng **không bắt buộc phải gõ lệnh**. Cứ mô tả việc muốn làm bằng tiếng Việt — Claude tự nhận skill phù hợp.

## Ba cách tra

| Bạn đang ở đâu | Mở file này |
|---|---|
| Biết mình cần làm gì, không biết gọi skill nào | [[00 — Tôi Muốn Làm Gì]] |
| Muốn xem toàn bộ, có phân nhóm | [[00 — Bảng Tra Toàn Bộ Skill]] |
| Đang làm một bước trong khung A–Z | Mở `Bước NN.md`, mục "Skill dùng ở bước này" |

Hoặc đơn giản nhất: `Ctrl/Cmd + Shift + F` trong Obsidian rồi gõ việc bạn cần bằng tiếng Việt.

## Cấu trúc thư viện

```
30. Thư Viện Skill/
├─ 00 — Cách Dùng Thư Viện.md        ← bạn đang ở đây
├─ 00 — Tôi Muốn Làm Gì.md           ← tra theo tình huống
├─ 00 — Bảng Tra Toàn Bộ Skill.md    ← 282 skill, đủ cả
├─ ⭐ Cốt Lõi/                        ← 34 skill cốt lõi, gắn với 12 bước
├─ 01. Chiến Lược & Điều Hành/       ┐
├─ 02. Thương Hiệu & Thiết Kế/       │
├─ …                                 │ 16 nhóm chức năng
├─ 16. Xưởng Video AI/               ┘
└─ _Kho Skill/                       ← file gốc của cả 282 skill
```

**Các thư mục 01–16 chứa phiếu mô tả tiếng Việt** — mở ra để đọc skill đó làm gì. **`_Kho Skill/` chứa file thật** — chỗ copy đi khi muốn bật thêm skill.

## Ba tầng skill

| Tầng | Số lượng | Trạng thái |
|---|---|---|
| ⭐ **Cốt lõi** | 34 | Đã bật sẵn trong vault, dùng được ngay |
| **Mở rộng** | 245 | Nằm trong `_Kho Skill/`, cần bật thủ công |

34 skill cốt lõi được chọn theo nguyên tắc: **phủ đủ 12 bước của khung A–Z**, mỗi bước có ít nhất một skill. Đây là bộ tối thiểu để một doanh nghiệp chạy được từ định vị tới đo lường.

## Bật thêm skill

1. Tra mã skill (ví dụ `webinar-planner`)
2. Copy thư mục `_Kho Skill/webinar-planner/` vào `10. Hệ Điều Hành/Vault Doanh Nghiệp/.claude/skills/`
3. Khởi động lại Claude

Tắt skill: xoá thư mục đó khỏi `.claude/skills/`. File gốc vẫn còn nguyên trong `_Kho Skill/`.

> [!warning] Đừng bật quá 60 skill
> Mỗi skill bật lên đều nạp mô tả vào bộ nhớ ngữ cảnh của Claude. Bật cả 282 skill cùng lúc sẽ làm Claude chậm, hay nhầm skill và trả lời kém chính xác. Bật khi cần, tắt khi xong việc.

## Về ngôn ngữ

**Tất cả 282 skill đều có tên và mô tả tiếng Việt.** Đó là phần bạn đọc và Claude dùng để nhận diện khi bạn nói tiếng Việt.

Phần hướng dẫn nội bộ bên trong một số skill vẫn còn tiếng Anh — đó là *hướng dẫn cho Claude*, không phải thứ bạn đọc. File `CLAUDE.md` trong vault đã đặt quy tắc bắt buộc: **mọi kết quả Claude tạo ra đều bằng tiếng Việt**, bất kể skill viết bằng ngôn ngữ gì.

Nếu muốn dịch toàn văn một skill cụ thể, nói với Claude: *"Dịch toàn bộ file `.claude/skills/<tên-skill>/SKILL.md` sang tiếng Việt, giữ nguyên phần frontmatter và cấu trúc heading."*

## 16 nhóm chức năng

| Nhóm | Dùng cho ai |
|---|---|
| 01. Chiến Lược & Điều Hành | Chủ doanh nghiệp, ban giám đốc |
| 02. Thương Hiệu & Thiết Kế | Marketing, thiết kế |
| 03. Nội Dung & Sáng Tạo | Người viết nội dung |
| 04. Mạng Xã Hội & SEO | Người phụ trách kênh |
| 05. Quảng Cáo Trả Phí | Người chạy quảng cáo |
| 06. Email & Tự Động Hoá | Marketing automation |
| 07. Bán Hàng & Phễu | Kinh doanh |
| 08. Chăm Sóc & Giữ Khách | Chăm sóc khách hàng |
| 09. Sự Kiện & Ra Mắt | Tổ chức sự kiện, ra mắt sản phẩm |
| 10. Đào Tạo & Sản Phẩm Số | Làm khoá học, coaching |
| 11. Vận Hành & Công Nghệ | Quản lý vận hành |
| 12. Nhân Sự | Nhân sự, quản lý đội ngũ |
| 13. Tài Chính & Giá | Kế toán, tài chính |
| 14. Pháp Lý & Tuân Thủ | Pháp chế, hợp đồng |
| 15. Dữ Liệu & Đo Lường | Phân tích số liệu |
| 16. Xưởng Video AI | Sản xuất video bằng AI (cần tài khoản trả phí) |

## Skill khó nhất và skill dễ nhất

**Bắt đầu bằng skill này nếu bạn hoàn toàn chưa biết gì:** `/fullstack-marketing-operator` — nó phỏng vấn bạn rồi chỉ sang skill phù hợp.

**Ba skill phải chạy đầu tiên, không có ngoại lệ:** `/mo-hinh-kinh-doanh` → `/hoan-tat-business-context` → `/brand-voice-guide`. Chưa xong ba cái này thì mọi skill khác đều cho ra kết quả chung chung.
