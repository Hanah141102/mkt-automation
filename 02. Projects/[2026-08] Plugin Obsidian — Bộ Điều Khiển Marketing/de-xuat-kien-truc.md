---
tags: [du-an, plugin, kien-truc, de-xuat]
type: de-xuat-kien-truc
trang-thai: cho-duyet
ngay-tao: 2026-08-29
lien-quan: ["[[00 — Bản Đồ A-Z]]", "[[Vault SME — Hướng Dẫn]]"]
---

# Đề Xuất Kiến Trúc — Plugin Obsidian "Bộ Điều Khiển Marketing"

> Bản này để anh review. **Chưa code gì.** Cuối bài có 5 câu hỏi cần anh chốt trước khi bắt tay.

## 1. Bài toán

Vault đang có đủ đồ nghề nhưng chỉ dùng được qua terminal:

| Thứ đang có | Số lượng | Vấn đề |
|---|---|---|
| Skill vận hành đã bật | 125 (90 có phân nhóm tiếng Việt) | Phải nhớ tên skill, gõ `/ten-skill` |
| Kho skill dự phòng | 301 | Không biết cái nào có sẵn |
| Khung Vận Hành A-Z | 12 bước, mỗi bước có cổng "Xong" | Không nhìn thấy mình đang đứng ở đâu |
| Nguồn sự thật doanh nghiệp | `00. Business Context/` | Agent đọc được, người thì phải mở từng file |
| Đầu ra | File `.md` rải khắp PARA | Không có chỗ nào nhìn tổng thể |

Cái thiếu **không phải** là thêm trí tuệ AI. Cái thiếu là **mặt kính**: chỗ để nhập liệu có hình có dạng, và chỗ để nhìn kết quả dạng trực quan.

## 2. Năm nguyên tắc — cái này quyết định toàn bộ phần còn lại

**2.1. Markdown vẫn là nguồn sự thật, plugin chỉ là mặt kính.**
Plugin **không** tạo database song song. Mọi thứ agent sinh ra vẫn là file `.md` nằm đúng chỗ theo `CLAUDE.md` mục 3. Gỡ plugin ra thì vault vẫn dùng được 100%, chỉ mất phần đẹp.
*Vì sao:* nếu dữ liệu chui vào database riêng của plugin, vault thành con tin. Plugin hỏng là công ty đứng.

**2.2. Plugin không chứa trí tuệ.**
Không copy prompt, không copy quy trình vào code plugin. Toàn bộ nghiệp vụ nằm trong 125 skill. Sửa skill → plugin đổi theo ngay, không phải build lại.
*Vì sao:* skill là tài sản đã có, viết bằng tiếng Việt, anh sửa được. Code TypeScript thì anh không sửa được.

**2.3. Agent chạy ngoài Obsidian, không chạy trong.**
Job render video 20 phút không được chết khi đóng cửa sổ vault.

**2.4. Người duyệt trước khi ghi vào vùng nhạy cảm.**
`Decisions/`, `00. Business Context/`, mọi thứ dính tới giá — agent chỉ được đề xuất, anh bấm áp dụng. Đúng luật số 5 trong `CLAUDE.md`.

**2.5. Tiếng Việt từ đầu tới cuối.**
Nhãn nút, tên trường, thông báo lỗi, tooltip. Không có chữ "Run", "Submit", "Loading".

## 3. Kiến trúc bốn tầng

```
┌──────────────────────────────────────────────────────────────┐
│ TẦNG 4 — MẶT KÍNH  (plugin Obsidian, TypeScript)             │
│                                                              │
│  Bảng Điều Khiển A-Z │ Ngăn Chạy Skill │ Dòng Chạy Trực Tiếp │
│  Khay Duyệt Thay Đổi │ Khối Visual nhúng thẳng trong note    │
└───────────────────────────┬──────────────────────────────────┘
                            │  HTTP + WebSocket  (127.0.0.1)
┌───────────────────────────┴──────────────────────────────────┐
│ TẦNG 3 — ĐIỀU PHỐI  (sidecar Node, gọi là "mkt-daemon")      │
│                                                              │
│  Hàng đợi 2 làn │ Bộ định tuyến Claude/Codex │ Nhật ký phiên │
│  Bộ gác quyền ghi │ Sinh vùng nháp & diff                    │
└───────────────────────────┬──────────────────────────────────┘
                            │  spawn + stdio (NDJSON)
┌───────────────────────────┴──────────────────────────────────┐
│ TẦNG 2 — TÁC TỬ  (CLI có sẵn trên máy)                       │
│                                                              │
│  claude 2.1.251   →  việc nội dung, phân tích, dùng skill    │
│  codex  0.150.1   →  việc code, pipeline video, sửa lỗi      │
└───────────────────────────┬──────────────────────────────────┘
                            │  đọc / ghi
┌───────────────────────────┴──────────────────────────────────┐
│ TẦNG 1 — TRI THỨC  (vault, không đổi gì)                     │
│                                                              │
│  00. Business Context │ .claude/skills │ PARA │ MOC │ People │
└──────────────────────────────────────────────────────────────┘
```

### Vì sao có Tầng 3 — và vì sao nó nhỏ hơn tôi tưởng

**Đã kiểm chứng trên máy anh ngày 29/08/2026.** `claude` 2.1.251 có sẵn chế độ chạy nền có quản lý vòng đời:

```
claude --bg "…"      → chạy nền, trả về id ngay
claude agents        → liệt kê job đang chạy
claude logs <id>     → xem đầu ra
claude attach <id>   → mở lại job trong terminal
claude stop <id>     → dừng, hội thoại vẫn giữ
claude respawn <id>  → chạy lại
claude rm <id>       → xoá hẳn
```

Nghĩa là **lý do lớn nhất tôi đưa ra để có daemon — "đóng Obsidian thì job chết" — đã được CLI làm sẵn.** Bảng dưới là đánh giá lại sau khi kiểm chứng:

| Vấn đề | `claude --bg` giải quyết? | Vẫn cần daemon? |
|---|---|---|
| Đóng Obsidian giữa chừng | ✅ CLI làm sẵn | Không |
| Xem lại phiên hôm qua | ✅ `claude agents` + `logs` | Không |
| Job render video 30 phút | ✅ | Không |
| Hàng đợi, giới hạn 1 job render cùng lúc | ❌ | **Có** |
| Gộp stream để Obsidian không giật | ❌ | Có, nhưng plugin tự làm được |
| Điều khiển từ iPad | ❌ | **Có** |
| Điều phối chung cả `claude` lẫn `codex` | ❌ | Có |

**Khuyến nghị đã sửa: bỏ daemon ở Chặng 0–3.** Plugin gọi thẳng CLI theo hai chế độ:

| Chế độ | Dùng khi | Lệnh |
|---|---|---|
| **Trước mặt** — có stream, hỏi đáp được | Viết content, phân tích, mọi việc anh ngồi xem | `claude -p --output-format stream-json --input-format stream-json` |
| **Chạy nền** — thả ra rồi quên | Render video, nghiên cứu dài, chạy hàng loạt | `claude --bg` rồi theo dõi bằng `agents` / `logs` |

Daemon chỉ dựng ở **Chặng 4** khi thật sự cần hàng đợi và điều khiển từ máy khác. Tiết kiệm khoảng 4–6 ngày công và bớt một thứ để hỏng.

## 4. Tầng 4 — Mặt kính, chi tiết

### 4.1. Bảng Điều Khiển A-Z (màn hình chính)

Một tab riêng trong Obsidian. Mười hai thẻ theo đúng `00 — Bản Đồ A-Z.md`:

```
  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
  │ 01 NỀN MÓNG     │ │ 02 ĐỊNH VỊ      │ │ 03 NGHIÊN CỨU   │
  │ ✅ Qua cổng     │ │ ⚠️ Thiếu 2 mục  │ │ ❌ Chưa bắt đầu │
  │ ▓▓▓▓▓▓▓▓ 100%  │ │ ▓▓▓▓▓░░░  62%   │ │ ░░░░░░░░   0%   │
  │ 3 skill  →      │ │ 8 skill  →      │ │ 6 skill  →      │
  └─────────────────┘ └─────────────────┘ └─────────────────┘
        │ phụ thuộc          │                    │
        └───────────────────►└───────────────────►│
```

- **Trạng thái cổng không phải người tự tick.** Chạy nền skill `/kiem-tra-cong` — nó đi đọc file thật rồi chấm ✅/⚠️/❌. Cache kết quả, làm mới khi vault đổi hoặc anh bấm.
- Bấm vào thẻ → mở danh sách skill thuộc bước đó, kèm mục "còn thiếu gì, chạy skill nào để bịt" lấy thẳng từ đầu ra `/kiem-tra-cong`.
- Bước bị khoá (chưa qua cổng trước) hiện mờ, kèm câu giải thích tại sao — không chặn cứng, anh vẫn bấm được nếu muốn.

### 4.2. Ngăn Chạy Skill (form nhập liệu)

Đây là chỗ thay cho việc gõ `/ten-skill` rồi trả lời 15 câu hỏi trong terminal.

```
┌────────────── THIẾT KẾ OFFER ──────────────────────┐
│ Nhóm: 04. Offer & Giá   ·   Bước A-Z: 04           │
│                                                    │
│ Sản phẩm    [ Gói Xây Hệ Thống AI      ▾ ]  ← đọc  │
│                                        từ thư mục  │
│ Phân khúc   [☑ PK1 Chủ DN 10-50 người ]  Sản Phẩm  │
│             [☐ PK2 Freelancer          ]  & Dịch Vụ│
│                                                    │
│ Giá mục tiêu  [ 25.000.000 ] đ                     │
│ Mục đích    ( ) Tăng giá  (•) Đóng gói lại         │
│                                                    │
│ Ghi chú thêm  ┌──────────────────────────────┐     │
│               │                              │     │
│               └──────────────────────────────┘     │
│                                                    │
│ ▸ Xem trước câu lệnh gửi cho agent                 │
│ ▸ Agent sẽ đọc: Hồ Sơ MHKD, Brand Voice, PK1       │
│ ▸ Agent sẽ ghi vào: 00. Business Context/Sản Phẩm  │
│                                                    │
│   [ Chạy với Claude ]  [ Chạy nháp ]  [ Huỷ ]      │
└────────────────────────────────────────────────────┘
```

Ba điểm cần chú ý:

1. **Trường chọn được nạp từ chính vault.** Danh sách phân khúc đọc từ `MHKD/Phân Khúc Khách Hàng/PK*.md`, danh sách sản phẩm đọc từ `Sản Phẩm & Dịch Vụ/`. Không gõ tay, không sai tên.
2. **Luôn nói trước agent sẽ đọc gì, ghi vào đâu.** Không có hộp đen.
3. **"Chạy nháp"** = agent làm nhưng ghi vào vùng nháp, anh xem diff rồi mới áp dụng.

**Form đó lấy từ đâu?** Một file khai báo `.mkt/ui/<ten-skill>.json`:

```json
{
  "skill": "thiet-ke-offer",
  "ten-hien-thi": "Thiết Kế Offer",
  "buoc-az": "04",
  "doc-truoc": ["00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md"],
  "ghi-vao": ["00. Business Context/Sản Phẩm & Dịch Vụ/"],
  "can-duyet": true,
  "truong": [
    { "ma": "san_pham", "nhan": "Sản phẩm", "kieu": "chon-file",
      "nguon": "00. Business Context/Sản Phẩm & Dịch Vụ/*.md" },
    { "ma": "phan_khuc", "nhan": "Phân khúc", "kieu": "chon-nhieu",
      "nguon": "00. Business Context/MHKD/Phân Khúc Khách Hàng/PK*.md" },
    { "ma": "gia_muc_tieu", "nhan": "Giá mục tiêu", "kieu": "tien-vnd" }
  ]
}
```

**Không sửa một dòng nào trong 125 file `SKILL.md`.** File khai báo nằm riêng ở `.mkt/ui/`. Lần đầu chạy một skill chưa có khai báo, plugin nhờ chính Claude đọc `SKILL.md` sinh ra file này rồi lưu lại — anh sửa tay được. Skill nào chưa có khai báo thì rơi về ô nhập tự do, vẫn chạy bình thường.

### 4.3. Dòng Chạy Trực Tiếp (sidebar phải)

Xem agent đang làm gì, theo ngôn ngữ người thường:

```
● Đang chạy · Thiết Kế Offer · 2 phút 14 giây

  ✓ Đọc Hồ Sơ Mô Hình Kinh Doanh
  ✓ Đọc Brand Voice
  ✓ Đọc PK1 — Chủ DN 10-50 người
  ⟳ Đang viết Gói Xây Hệ Thống AI — v2.md
  
  ┌ Agent hỏi ────────────────────────────────┐
  │ Gói này có bảo hành hoàn tiền không?      │
  │ [ Có, 30 ngày ] [ Không ] [ Tự trả lời… ] │
  └───────────────────────────────────────────┘

  [ Dừng ]  [ Xem nhật ký thô ]
```

Điểm khó nhất về kỹ thuật ở đây: agent hỏi lại giữa chừng. Cách đúng là `--input-format stream-json` — **giữ stdin mở** rồi đẩy câu trả lời của anh vào như một tin nhắn mới, phiên không đứt. Thêm `--replay-user-messages` để plugin biết chắc CLI đã nhận. Không dùng `--resume` cho việc này: nó phải giết phiên rồi dựng lại, mất thời gian và mất ngữ cảnh nóng.

### 4.4. Khay Duyệt Thay Đổi

Với các skill có `"can-duyet": true`:

```
Thiết Kế Offer đề xuất 3 thay đổi:

  ● Sửa   00. Business Context/Sản Phẩm & Dịch Vụ/Gói Xây Hệ Thống AI.md
          − Giá: 18.000.000 đ
          + Giá: 25.000.000 đ  · thêm 2 bonus, cam kết 30 ngày
  ● Tạo   Decisions/2026-08-29 — Nâng giá Gói Xây Hệ Thống AI.md
  ● Tạo   03. Areas/Brand & Content/.../Bài giới thiệu gói mới.md

  [ Áp dụng tất cả ]  [ Áp dụng từng cái ]  [ Bỏ hết ]
```

### 4.5. Khối Visual nhúng thẳng trong note — phần quan trọng nhất

Đây là cách plugin cho ra "output visual dễ nhìn" **mà không phá vỡ nguyên tắc 2.1**. Học cách của Dataview: viết một khối trong note, plugin render thành hình.

| Khối | Hiện ra cái gì | Đọc dữ liệu từ đâu |
|---|---|---|
| ` ```mkt-canvas ` | Business Model Canvas 9 ô, màu theo độ đầy đủ | `Business Model Canvas — *.md` |
| ` ```mkt-phao ` | Sơ đồ phễu có số ở từng tầng, chỗ rơi rớt tô đỏ | `03. Areas/Sales Pipeline & CRM/` |
| ` ```mkt-lich ` | Lịch content dạng tháng, màu theo trụ cột & kênh | frontmatter trong `Content Đã Đăng/` |
| ` ```mkt-kpi ` | Hàng thẻ số: lead, tỷ lệ chốt, doanh thu, xu hướng | `03. Areas/Analytics & Reporting/` |
| ` ```mkt-cong ` | Thanh tiến độ 12 bước A-Z | cache của `/kiem-tra-cong` |
| ` ```mkt-pipeline ` | Bảng kanban deal theo giai đoạn | frontmatter `People/` + `Companies/` |
| ` ```mkt-tru-cot ` | Vòng tròn tỷ trọng trụ cột nội dung thực tế vs kế hoạch | đếm bài đã đăng |

Nguyên tắc bắt buộc cho mọi khối: **bên dưới khối luôn có bảng markdown thô**. Không có plugin thì vẫn đọc được số, chỉ mất phần đồ hoạ. Người khác mở vault bằng Obsidian trắng, hoặc xem trên GitHub, vẫn hiểu.

## 5. Tầng 3 — Daemon, chi tiết

### 5.1. Giao diện lập trình

```
POST   /viec              tạo việc mới → { id }
GET    /viec/:id          trạng thái
WS     /dong/:id          stream sự kiện
POST   /viec/:id/tra-loi  trả lời câu hỏi của agent
POST   /viec/:id/dung     dừng
GET    /cong              trạng thái 12 cổng A-Z (có cache)
POST   /duyet/:id         áp dụng thay đổi từ vùng nháp
```

Nghe trên `127.0.0.1` thôi, không mở ra mạng. Token ngẫu nhiên lưu ở `.mkt/token`, đã gitignore.

### 5.2. Hai làn hàng đợi

| Làn | Việc | Đồng thời tối đa |
|---|---|---|
| **Nhanh** | Viết content, phân tích, kiểm tra cổng, nghiên cứu | 3 |
| **Nặng** | Render video HyperFrames, HeyGen, ElevenLabs, Apify | 1 |

Vì sao tách: một lệnh render chiếm hết CPU thì mọi việc viết lách đứng theo. Hai làn cho phép vừa render video vừa viết caption.

### 5.3. Bộ định tuyến Claude / Codex

| Loại việc | Giao cho | Lý do |
|---|---|---|
| Chạy skill vault, viết nội dung, phân tích kinh doanh | **Claude CLI** | Skill viết cho Claude, tiếng Việt tốt hơn |
| Sửa script trong `scripts/`, `videos/`, debug lỗi render | **Codex CLI** | Mạnh về code, đã có sẵn agent `codex:rescue` |
| Việc dài, nhiều bước, cần đọc nhiều file | **Claude CLI** | Cửa sổ ngữ cảnh lớn |
| Việc lặp máy móc, rẻ | **Codex CLI** | Tiết kiệm |

Mặc định theo bảng, nhưng nút "Chạy với…" luôn cho anh đổi.

### 5.4. Bộ gác quyền ghi

Ba vòng bảo vệ, xếp từ ngoài vào:

1. **Whitelist thư mục theo skill** — khai báo trong `"ghi-vao"`. Agent chạy với hook `PreToolUse` chặn mọi lệnh ghi ra ngoài danh sách.
2. **Vùng nhạy cảm luôn qua duyệt** — `Decisions/`, `00. Business Context/`, bất cứ file nào chứa giá.
3. **Không bao giờ xoá** — hook chặn `rm`, chặn Write đè file có sẵn ngoài danh sách. Đúng luật 4 trong `CLAUDE.md`.

### 5.5. Nhật ký phiên

```
.mkt/
├── token                       ← bí mật cục bộ
├── ui/<skill>.json             ← khai báo form (nên commit)
├── cache/cong.json             ← trạng thái 12 cổng
└── runs/2026-08-29-1432-thiet-ke-offer/
    ├── viec.json               ← form đã nhập, skill, agent nào
    ├── cau-lenh.txt            ← prompt gửi đi, để anh kiểm chứng
    ├── tho.ndjson              ← stream gốc
    ├── file-cham-vao.json
    └── ket-qua.md
```

`.mkt/` vào `.gitignore`, trừ `.mkt/ui/` nên commit vì đó là cấu hình chung.

### 5.6. Lệnh gọi CLI — đã chạy thử thật, không phải lý thuyết

**Claude — chế độ trước mặt:**

```bash
claude -p "/thiet-ke-offer Sản phẩm: Gói Xây Hệ Thống AI · Phân khúc: PK1 · Giá: 25.000.000đ" \
  --session-id 8f3a1c02-…                    # plugin tự sinh UUID, biết trước id
  --output-format stream-json --verbose      # dòng sự kiện
  --input-format  stream-json                # để trả lời agent giữa chừng
  --include-partial-messages                 # chữ hiện dần
  --permission-mode acceptEdits              # acceptEdits|auto|manual|dontAsk|plan|bypassPermissions
  --allowedTools Read Edit Write Glob Grep "Bash(npx hyperframes *)"
  --disallowedTools "Bash(rm *)" "Bash(git push*)"
  --add-dir "/Users/tonyhoang/Documents/GitHub/Tony Brain"
  --settings .mkt/settings-plugin.json       # hook gác quyền ghi, không đụng settings vault
  --append-system-prompt "Trả lời và tạo file bằng tiếng Việt."
  --max-budget-usd 2                         # trần chi phí một việc
  --model opus
```

Bốn flag đáng tiền:

| Flag | Vì sao quan trọng cho plugin |
|---|---|
| `--session-id <uuid>` | Plugin sinh UUID **trước** khi chạy → thư mục `.mkt/runs/<uuid>/` khớp ngay, không phải chờ parse id trả về |
| `--json-schema '{…}'` | Bắt agent trả JSON đúng khuôn. **Đây là cách nuôi khối visual** — `/kiem-tra-cong` trả thẳng JSON 12 cổng thay vì plugin phải đọc văn xuôi |
| `-w, --worktree` | Chạy trong git worktree tách riêng. **Chính là "vùng nháp" cho Khay Duyệt** — CLI làm sẵn, plugin chỉ cần `git diff` |
| `--settings <file>` | Nạp hook gác quyền riêng của plugin mà **không sửa** `.claude/settings.local.json` của vault |

**Dạng sự kiện thật** (chạy thử lúc 14:32 ngày 29/08, đã rút gọn):

```jsonc
{"type":"system","subtype":"init","session_id":"51ecc744…","model":"claude-haiku-4-5","tools":[…]}
{"type":"system","subtype":"thinking_tokens","estimated_tokens":180}
{"type":"rate_limit_event","rate_limit_info":{"unifiedWindows":{"five_hour":{"utilization":0.03}}}}
{"type":"assistant","message":{"content":[{"type":"thinking",…},{"type":"text",…}]}}
{"type":"result","subtype":"success","total_cost_usd":…}
```

Chú ý `rate_limit_event`: plugin hiện được đồng hồ *"đã dùng 3% hạn 5 giờ"* — rất cần khi chạy hàng loạt video, để biết lúc nào nên dừng.

**Codex — cho việc code và pipeline video:**

```bash
codex exec --json \
  -C "/Users/tonyhoang/Documents/GitHub/mkt-automation" \
  -s workspace-write \                       # read-only | workspace-write | danger-full-access
  --add-dir videos \
  --output-schema .mkt/schema/ket-qua.json \
  -o .mkt/runs/<id>/ket-qua.md \
  "Sửa lỗi render trong videos/…"

codex exec resume <session-id> "Chạy lại phần render"
```

`-s workspace-write` là sandbox có sẵn — thành vòng gác quyền ghi thứ tư, khỏi tự viết.

**Rủi ro đã giảm:** vì cả hai CLI đều có `--json`/`stream-json` và đều có cơ chế resume, lớp adapter trong plugin chỉ cần dịch về một dạng sự kiện chung `{loai: 'chu'|'cong-cu'|'file'|'hoi'|'xong'|'loi'}`. Plugin chỉ hiểu một giao thức.

## 6. Bản đồ đầy đủ: 12 bước → skill → nhập gì → hiện gì

| Bước A-Z | Skill chính đã có | Nhập vào | Nhìn ra |
|---|---|---|---|
| 01 Nền Móng | `kiem-tra-cong` | — | Thanh 12 cổng |
| 02 Định Vị | `mo-hinh-kinh-doanh`, `hoan-tat-business-context`, `brand-positioning-builder`, `brand-voice-guide`, `customer-persona` | Phỏng vấn 9 ô dạng nhiều bước | Canvas 9 ô tương tác |
| 03 Nghiên Cứu | `nghien-cuu-thi-truong`, `mkt-phan-tich-doi-thu`, `voice-of-customer`, `swot-analysis` | Ngách, đối thủ, nguồn | Điểm ngách 100, ma trận SWOT |
| 04 Offer & Giá | `thiet-ke-offer`, `pricing-strategy`, `breakeven-analysis`, `bundle-creator`, `unit-economics` | Sản phẩm, giá, phân khúc | Bậc thang giá, biểu đồ hoà vốn |
| 05 Phễu | `sales-funnel-builder`, `customer-journey-map`, `lead-magnet` | Kênh, tầng phễu | Sơ đồ phễu có số |
| 06 Nội Dung | `content-pillar-builder`, `content-plan-builder`, `content-copywriter`, `hook-generator`, `blog-post`, `social-media-calendar` | Trụ cột, kênh, nhịp đăng | Lịch content, vòng tròn trụ cột |
| 07 Quảng Cáo | `ads-strategy-planner`, `ads-copywriting`, `facebook-ad-campaign`, `media-buy-plan`, `ads-performance-diagnostic` | Ngân sách, mục tiêu, đối tượng | Phân bổ ngân sách, bảng ngưỡng dừng |
| 08 Bán Hàng | `sales-script`, `objection-handler`, `chot-don-qua-zalo`, `ghi-cuoc-gap`, `phan-bo-va-cham-diem-lead` | Kể lại cuộc gặp bằng lời | Kanban pipeline, hồ sơ khách |
| 09 Giao Hàng | `onboarding-flow`, `sop-builder`, `training-manual` | Gói đã bán | Sơ đồ quy trình |
| 10 Giữ Khách | `churn-prevention-playbook`, `customer-health-score`, `win-back-campaign`, `nhac-mua-lai-theo-chu-ky` | Danh sách khách | Bảng sức khoẻ khách, cảnh báo rời bỏ |
| 11 Đo Lường | `mkt-kpi-dashboard`, `mkt-marketing-report-writer`, `attribution-model`, `cohort-analysis` | Kỳ báo cáo | Thẻ KPI, biểu đồ xu hướng |
| 12 Kaizen | `retrospective`, `process-automation-audit`, `thu-nghiem-ab` | Kỳ rà soát | Danh sách cải tiến có chủ |

**Nhánh sản xuất video** (`mkt-hyperframe-*`, `mkt-heygen-*`, `mkt-elevenlabs-*`) nằm ngoài 12 bước, gắn vào Bước 06. Đây là nhóm chạy làn "nặng", cần thanh tiến độ render và ô xem trước MP4 ngay trong plugin.

**Nhánh đăng bài** (`mkt-blotato-publish-social`, MCP Composio/Blotato) nối vào cuối Bước 06 → đẩy số đo về Bước 11.


## 6b. Xưởng Nội Dung — tạo nhiều dạng, đăng nhiều kênh

Đây là phần chạy hằng ngày, nên đáng thiết kế kỹ nhất.

### 6b.1. Các dạng nội dung và skill tương ứng

| Dạng nội dung | Skill đã có | Kênh đích | Làn |
|---|---|---|:--:|
| Bài Facebook dài | `content-copywriter`, `mkt-create-script-short-video-v2-vn` | FB | nhanh |
| Caption ngắn + hook | `hook-generator`, `mkt-caption-writer`, `mkt-kallaway-hook-story-engine-vn` | FB · IG · Threads | nhanh |
| Bài blog SEO | `blog-post`, `seo-competitor-analysis` | Website | nhanh |
| Trang bán hàng | `landing-page-copy`, `sales-page` | Web | nhanh |
| Chuỗi email | `email-sequence`, `win-back-campaign`, `nhac-mua-lai-theo-chu-ky` | Email | nhanh |
| Mồi thu lead | `lead-magnet` | PDF · Web | nhanh |
| Kịch bản video ngắn | `mkt-create-script-short-video-v2-vn`, `video-script` | — | nhanh |
| **Video 9:16 avatar** | `mkt-hyperframe-knowledge-video-heygen-9-16` · bản `-lite` tiết kiệm HeyGen | TikTok · Reels · Shorts | **nặng** |
| **Video 9:16 từ face-cam** | `mkt-hyperframe-talking-head-video` | TikTok · Reels | **nặng** |
| **Video 16:9 keynote** | `mkt-hyperframe-knowledge-video-heygen-16-9`, `mkt-hyperframe-knowledge-video` | YouTube | **nặng** |
| **Motion graphic không lời** | `motion-graphics`, `general-video` | Overlay · IG | **nặng** |
| **Giọng đọc MP3** | `mkt-elevenlabs-tts-to-mp3` | — | **nặng** |
| Poster · ảnh bài viết | Kie.ai GPT Image 2, `example-skills:canvas-design` | FB · IG | trung |
| Nội dung quảng cáo | `ads-copywriting`, `facebook-ad-campaign`, `google-ads-campaign` | Ads | nhanh |
| **Tái chế 1 → N** | `mkt-content-repurpose`, `mkt-multiplatform-content-factory` | tất cả | nhanh |

### 6b.2. Màn hình Xưởng Nội Dung — một ý tưởng, nhiều đầu ra

Đây là chỗ ăn tiền nhất: **một lần nhập, ra đủ bộ.**

```
Ý tưởng gốc                    Chọn format cần            Sinh song song
┌──────────────┐              ┌──────────────────┐        ┌─────────────┐
│ Nguồn:       │              │ ☑ Bài FB dài     │───────►│ ● xong  2p  │
│ ( ) Gõ tay   │              │ ☑ Video 9:16     │───────►│ ⟳ render 8p │
│ (•) Nhật Ký  │              │ ☑ 5 caption      │───────►│ ● xong  1p  │
│ ( ) Ý tưởng  │─────────────►│ ☐ Blog SEO       │        │             │
│ ( ) Bài cũ   │              │ ☑ Ảnh bìa        │───────►│ ● xong  40s │
│ ( ) Đối thủ  │              │ ☐ Email          │        │             │
└──────────────┘              └──────────────────┘        └─────────────┘
                                                                 │
      Trụ cột: [Quy trình ▾]  Phân khúc: [PK1 ▾]                 ▼
      Tầng phễu: [Nhận biết ▾]  Kênh: [FB][TikTok][IG]      Xem trước & duyệt
```

Ba điều bắt buộc:

1. **Sinh song song, không xếp hàng.** Bài FB và caption chạy làn nhanh; video chạy làn nặng. Anh đọc bài trong khi video còn đang render.
2. **Mọi đầu ra đều gắn được ba nhãn**: phân khúc nào · tầng phễu nào · kêu gọi làm gì. Đây đúng là cổng "Xong" của Bước 06 trong Khung A-Z.
3. **Xem trước đúng hình dạng kênh** — bài FB xem như trên FB, video 9:16 xem trong khung dọc. Không xem markdown thô rồi đoán.

### 6b.3. Bàn Đăng Bài — kanban vòng đời

```
Ý TƯỞNG   →  ĐANG VIẾT  →  CHỜ DUYỆT  →  ĐÃ LÊN LỊCH  →  ĐÃ ĐĂNG  →  ĐANG ĐO
   12           3              5              8             34         34
```

- Kéo thẻ sang cột là chạy hành động tương ứng, không phải sửa frontmatter tay.
- Nguồn dữ liệu vẫn là file `.md` trong `Content Đã Đăng/` + frontmatter `trang-thai`. Plugin **không** giữ trạng thái riêng — kéo thẻ = sửa một dòng frontmatter.
- Dùng chung được với plugin Kanban đang cài, không đá nhau.

### 6b.4. Đăng bài

Skill `mkt-blotato-publish-social` đã có, và **ưu tiên Composio trước, Blotato làm dự phòng**. Kênh phủ được: Facebook Page (feed · reel · story), TikTok, Instagram, YouTube, Threads, X, LinkedIn.

```
┌──── XẾP LỊCH ĐĂNG ──────────────────────────────────┐
│ Nội dung: "Sáu trường hợp AI làm sai"               │
│                                                     │
│  Kênh          Dạng        Thời điểm                │
│  ☑ FB Page     Bài + ảnh   [30/08  08:00]           │
│  ☑ TikTok      Video 9:16  [30/08  19:30]  ← giờ tốt│
│  ☑ Instagram   Reel        [30/08  19:30]           │
│  ☐ YouTube     Shorts                               │
│  ☑ Threads     Bài ngắn    [31/08  08:00]           │
│                                                     │
│  ⚠ TikTok chưa nối tài khoản — [ Nối ngay ]         │
│                                                     │
│    [ Xếp lịch ]   [ Đăng ngay ]   [ Lưu nháp ]      │
└─────────────────────────────────────────────────────┘
```

Nguyên tắc: **đăng là hành động ra ngoài, luôn hỏi xác nhận.** Không có chế độ tự đăng ngầm. Trước khi gửi, plugin hiện đúng nội dung sẽ lên từng kênh.

### 6b.5. Vòng khép kín — đăng xong phải học được gì

```
Đăng  →  3 ngày sau kéo số về  →  7 ngày sau đối chiếu  →  cập nhật ngân hàng hook
        mkt-facebook-list-comments   mkt-content-              mkt-content-
        Blotato analytics            performance-optimizer     learning-loop
```

Kết quả đổ về `03. Areas/Analytics & Reporting/` và hiện lên khối ` ```mkt-kpi ` + ` ```mkt-tru-cot `. Đây là thứ nối Bước 06 với Bước 11 — phần hầu hết mọi người bỏ dở.


## 7. Lộ trình — làm gì trước

| Chặng | Nội dung | Xong khi | Ước lượng |
|---|---|---|---|
| **0. Xương sống** | Plugin gọi `claude -p --output-format stream-json`, hiện dòng chạy, ghi file thật | Bấm nút trong Obsidian, `thiet-ke-offer` chạy, file hiện ra | 3–4 ngày |
| **1. Bảng điều khiển** | Màn hình 12 bước + `/kiem-tra-cong` chạy nền + form cho 10 skill lõi | Mở vault thấy ngay đang đứng ở bước nào | 1 tuần |
| **2. Xưởng Nội Dung** | Một ý tưởng → nhiều format song song + xem trước theo kênh + làn nặng cho video | Một lần nhập ra bài FB + 5 caption + 1 video 9:16 | 1,5 tuần |
| **3. Khối visual** | `mkt-canvas`, `mkt-lich`, `mkt-kpi`, `mkt-cong`, `mkt-tru-cot` | Note có hình, gỡ plugin vẫn đọc được | 1 tuần |
| **4. Bàn Đăng Bài** | Kanban vòng đời + xếp lịch + đăng qua Composio/Blotato + xác nhận trước khi ra ngoài | Đăng đa kênh từ trong Obsidian | 1 tuần |
| **5. An toàn** | Khay duyệt + `--worktree` làm vùng nháp + bộ gác quyền ghi | Không skill nào ghi lén vào `Decisions/` | 4–5 ngày |
| **6. Vòng khép kín** | Kéo số về + `mkt-content-learning-loop` + daemon (nếu lúc đó thật sự cần hàng đợi/iPad) | Đăng xong 7 ngày tự có báo cáo | 1 tuần |

**Đề nghị: chốt xong Chặng 0 rồi mới bàn tiếp.** Chặng 0 trả lời câu hỏi khó nhất — vòng đời agent chạy được hay không. Mọi thứ sau đó chỉ là giao diện.

## 8. Rủi ro đã thấy trước

| Rủi ro | Mức | Cách xử |
|---|---|---|
| Obsidian không có API chính thức để spawn tiến trình | Cao | Dùng `child_process` của Electron, đặt `isDesktopOnly: true`. Đổi lại: **không chạy trên iPad/điện thoại**. |
| Flag CLI đổi giữa các phiên bản (`claude`, `codex`) | Cao | Viết lớp adapter riêng cho từng CLI, kiểm tra phiên bản lúc khởi động, báo rõ nếu lệch |
| Đường dẫn có dấu tiếng Việt và khoảng trắng | Trung bình | Luôn truyền tham số dạng mảng, không nối chuỗi shell |
| Stream dày làm Obsidian giật | Trung bình | Daemon gộp 100ms một lần, danh sách ảo hoá, chỉ giữ 500 dòng gần nhất |
| 125 skill × mỗi cái một form = quá nhiều việc | Trung bình | Sinh tự động bằng Claude, chỉ làm tay 15–20 skill hay dùng, còn lại ô nhập tự do |
| Agent ghi sai chỗ, phá vault | Cao | Ba vòng gác ở mục 5.4 + `git` là lưới an toàn cuối |
| Plugin phình ra thành ứng dụng thứ hai | Trung bình | Nguyên tắc 2.1 và 2.2 là luật, review mỗi chặng |

## 9. Cái này **không** làm

Nói trước để khỏi hiểu nhầm phạm vi:

- Không chạy trên Obsidian mobile (bản chất kỹ thuật, không phải lười)
- Không tự viết lại 125 skill — plugin đọc chúng như đang có
- Không thay Dataview, Kanban, Excalidraw — plugin dùng chung, không cạnh tranh
- Không gọi thẳng API Anthropic/OpenAI — đi qua CLI để dùng đúng gói thuê bao và đúng skill đã cài
- Không đồng bộ lên đám mây

## 10. Năm câu hỏi cần anh chốt

1. **Daemon — hoãn hay làm ngay?** Sau khi kiểm chứng `claude --bg`, tôi **đổi khuyến nghị: hoãn tới Chặng 6.** Gọi thẳng CLI đã đủ cho job dài. Daemon chỉ thêm giá trị khi anh cần hàng đợi giới hạn đồng thời (vd: cấm 2 job render video chạy cùng lúc) hoặc muốn bấm chạy từ iPad. Anh có cần hai thứ đó sớm không?

2. **Code plugin để đâu?** Nằm trong vault ở `.obsidian/plugins/mkt-control/` (tiện, nhưng lẫn code vào vault) hay repo riêng rồi symlink vào (sạch hơn, thêm một bước cài)?

3. **Thứ tự Chặng 1 và 2?** Lộ trình đang để Bảng Điều Khiển trước Xưởng Nội Dung. Nếu việc hằng ngày của anh là ra content thì nên đảo lại — Xưởng Nội Dung trước, bảng điều khiển sau. Anh chọn thứ tự nào?

4. **Mức tự động mặc định?** Agent tự ghi thẳng rồi báo (nhanh, hợp khi anh tin), hay luôn qua Khay Duyệt (chậm hơn một nhịp, an toàn)? Có thể đặt khác nhau theo từng nhóm skill.

5. **Có cần nhiều người dùng chung không?** Nếu chỉ mình anh thì bỏ được toàn bộ phần xác thực và khoá file, tiết kiệm khá nhiều.

---

*Bản đề xuất, chưa code. Sửa thẳng vào file này hoặc ghi chú bên dưới, tôi cập nhật rồi mới bắt đầu Chặng 0.*
