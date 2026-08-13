---
name: viet-hoa-skill
description: "Dịch toàn văn một hoặc nhiều file SKILL.md từ tiếng Anh sang tiếng Việt, giữ nguyên frontmatter, cấu trúc heading, bảng biểu và mã lệnh. Dùng khi muốn đọc hoặc chỉnh sửa được phần hướng dẫn bên trong một skill, hoặc khi bàn giao cho đội không đọc được tiếng Anh."
allowed-tools: Read Write Edit Glob Grep Bash
ten-viet: "Việt Hoá Skill"
nhom: "11. Vận Hành & Công Nghệ"
ten-goc: "Việt Hoá Skill"
---

# Việt Hoá Skill

## Khi nào dùng

- Muốn đọc hiểu phần hướng dẫn bên trong một skill để chỉnh cho hợp doanh nghiệp mình
- Bàn giao cho đội không đọc được tiếng Anh
- Chuẩn hoá toàn bộ thư viện về một ngôn ngữ

**Không cần dùng khi** chỉ muốn *kết quả* bằng tiếng Việt — quy tắc trong `CLAUDE.md` đã bắt buộc mọi đầu ra là tiếng Việt rồi, kể cả khi skill viết bằng tiếng Anh.

## Nguyên tắc bắt buộc

1. **Giữ nguyên `name:` trong frontmatter.** Đây là mã gọi skill, đổi là hỏng.
2. **Giữ nguyên cấu trúc heading** — số lượng và cấp độ `#`, `##`, `###` phải khớp bản gốc. Skill hoạt động dựa vào cấu trúc này.
3. **Giữ nguyên khối mã, tên file, đường dẫn, biến, URL, mã màu.**
4. **Giữ nguyên bảng** — số cột, số dòng, thứ tự. Chỉ dịch nội dung ô.
5. **Không rút gọn, không tóm tắt, không bỏ mục.** Dịch đủ.
6. **Không dịch máy.** Viết như người Việt viết cho người Việt đọc.

## Từ điển thuật ngữ — dùng thống nhất

| Tiếng Anh | Tiếng Việt |
|---|---|
| offer | offer (giữ nguyên) |
| funnel | phễu |
| lead | lead (giữ nguyên) |
| lead magnet | mồi thu lead |
| landing page | landing page (giữ nguyên) |
| copy / copywriting | nội dung / viết nội dung |
| hook | câu móc |
| CTA / call to action | lời kêu gọi hành động |
| social proof | bằng chứng xã hội |
| testimonial | lời chứng thực |
| objection | phản đối / từ chối |
| churn | rời bỏ |
| retention | giữ chân |
| onboarding | đón khách mới / làm quen |
| persona | chân dung khách hàng |
| ICP / ideal customer | khách hàng lý tưởng |
| pain point | điểm đau |
| value proposition | giá trị cốt lõi |
| brand voice | giọng thương hiệu |
| pillar | trụ cột |
| repurpose | tái chế |
| SOP | quy trình chuẩn |
| stakeholder | bên liên quan |
| deliverable | hạng mục bàn giao |
| benchmark | so chuẩn |
| KPI, ROAS, CPM, CTR, CPA, LTV, CAC, SEO, GA4, UTM, A/B test | giữ nguyên |

**Tiền tệ:** nếu bản gốc dùng USD cho ví dụ, quy đổi sang VND theo mức hợp lý ở Việt Nam và ghi rõ đơn vị. Định dạng số kiểu Việt Nam: `1.000.000 đ`.

**Ví dụ thị trường:** nếu bản gốc lấy ví dụ Mỹ (Shopify, Amazon, Yelp), thay bằng tương đương Việt Nam (Shopee, Lazada, TikTok Shop, Google Maps) khi việc thay không làm sai ý.

## Quy trình

### Bước 1 — Xác định phạm vi

Hỏi người dùng dịch cái gì, nếu chưa nói rõ:

- Một skill cụ thể → hỏi mã skill
- Cả một nhóm → hỏi nhóm nào trong 17 nhóm
- Toàn bộ → cảnh báo: 556 skill, khoảng 4 MB, nên chia lô 20–30 skill mỗi lần

### Bước 2 — Kiểm tra trước khi dịch

```bash
head -20 "30. Thư Viện Skill/_Kho Skill/<mã-skill>/SKILL.md"
```

Nếu phần thân đã là tiếng Việt → báo người dùng, không dịch lại.

### Bước 3 — Dịch

Đọc toàn bộ file, dịch phần thân (sau frontmatter), giữ nguyên:

```
---
name: <giữ nguyên>
description: <giữ nguyên nếu đã tiếng Việt>
ten-viet: <giữ nguyên>
nhom: <giữ nguyên>
---
```

Nếu skill có thư mục `references/`, dịch luôn các file trong đó.

### Bước 4 — Kiểm tra sau khi dịch

Đối chiếu bản dịch với bản gốc:

- [ ] Số lượng heading khớp
- [ ] Số bảng và số cột mỗi bảng khớp
- [ ] Khối mã giữ nguyên, không bị dịch
- [ ] `name:` không đổi
- [ ] Không mục nào bị bỏ

### Bước 5 — Đồng bộ sang vault nếu skill đang bật

```bash
ls "10. Hệ Điều Hành/Vault Doanh Nghiệp/.claude/skills/<mã-skill>"
```

Nếu có → copy bản đã dịch đè lên, để bản đang chạy và bản trong kho không lệch nhau.

## Đầu ra

- File `SKILL.md` đã dịch, ghi đè bản cũ
- Bản gốc tiếng Anh lưu tại `references/<mã-skill>-ban-goc-en.md` (tạo nếu chưa có)
- Báo cáo ngắn: đã dịch bao nhiêu file, còn bao nhiêu skill chưa dịch trong phạm vi

## Ranh giới

- Không đổi logic skill, không thêm bớt bước trong quy trình gốc
- Không đổi `name:` — sẽ làm hỏng lệnh gọi
- Không dịch các skill kỹ thuật thuần (`obsidian-cli`, `json-canvas`, `hyperframes-*`) trừ khi người dùng yêu cầu rõ — phần lớn nội dung là cú pháp lệnh, dịch xong khó dùng hơn
