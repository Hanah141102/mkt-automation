---
title: Hướng Dẫn Agent Cài Đặt Skills và ENV
tags: [huong-dan, agent, skill, env, github]
---

# Hướng Dẫn Agent Cài Đặt Skills và ENV

Tài liệu này dành cho agent hoặc thành viên mới cần lấy toàn bộ hệ thống từ GitHub, nhận đúng bộ skill và cấu hình biến môi trường mà không làm lộ API key. Sau khi cài xong, đọc tiếp [[Hướng Dẫn Dùng Skill]] và [[Vault SME — Hướng Dẫn]].

## 1. Lấy toàn bộ repo từ GitHub

Yêu cầu tối thiểu: Git, Node.js, npm và một agent hỗ trợ đọc file `AGENTS.md` hoặc `CLAUDE.md`.

```bash
git clone https://github.com/Freedombuiders/mkt-automation.git
cd mkt-automation
npm install
```

Nếu máy đã có repo:

```bash
cd /duong-dan/toi/mkt-automation
git pull --ff-only origin main
npm install
```

Không tải riêng từng file bằng giao diện GitHub. Clone toàn bộ repo để giữ đủ script, reference, asset mẫu, wikilink và symlink tương thích.

## 2. Agent lấy skill ở đâu

| Nền tảng | Thư mục cần dùng | Cách dùng |
|---|---|---|
| Codex và agent theo chuẩn `AGENTS.md` | `.agents/skills/` | Mở chính thư mục repo làm workspace; skill cấp dự án được nhận từ đây. |
| Claude Code | `.claude/skills/` | Mở chính thư mục repo; Claude nhận skill cấp dự án từ đây. |
| Agent chưa hỗ trợ tự nhận skill | `.agents/skills/<ten-skill>/SKILL.md` | Yêu cầu agent đọc `AGENTS.md`, rồi đọc trọn file `SKILL.md` của skill cần chạy. |
| Kho đầy đủ để tra cứu/bật thêm | `huong dan/30. Thư Viện Skill/_Kho Skill/` | Đây là kho dự phòng; chỉ copy skill thật sự cần dùng vào thư mục hoạt động. |

Hai thư mục `.agents/skills/` và `.claude/skills/` phục vụ hai runtime khác nhau. Không xoá một thư mục chỉ vì thấy nhiều skill trùng tên.

Để mang toàn bộ skill sang một repo khác mà không mang vault và dữ liệu doanh nghiệp:

```bash
mkdir -p /duong-dan/repo-moi/.agents/skills
mkdir -p /duong-dan/repo-moi/.claude/skills
rsync -a .agents/skills/ /duong-dan/repo-moi/.agents/skills/
rsync -a .claude/skills/ /duong-dan/repo-moi/.claude/skills/
```

Sau khi copy, khởi động lại agent hoặc mở task mới để agent nạp lại danh sách skill. Khi chỉ cần một vài skill, nên copy đúng các thư mục đó để giảm nhiễu ngữ cảnh.

## 3. Thứ tự agent phải đọc

Khi làm việc trong repo này, agent đọc theo thứ tự:

1. `AGENTS.md` — quy ước Git, code, bảo mật và cấu trúc repo.
2. `CLAUDE.md` — quy tắc tiếng Việt, vault, nguồn sự thật và nơi ghi kết quả.
3. `00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md` — trước khuyến nghị có ngưỡng thời gian hoặc thiết kế phễu.
4. File `SKILL.md` của skill được gọi; phải đọc hết file và các reference bắt buộc trước khi chạy.

Agent không được bịa số liệu, không đưa dữ liệu khách hàng vào nội dung công khai và không commit secret hay media sinh ra.

## 4. Tạo file `.env`

Tại root repo, chạy:

```bash
cp .env.example .env
chmod 600 .env
```

Mở `.env` và chỉ điền các biến cần cho pipeline đang dùng. Không sửa `.env.example` bằng key thật.

### Nhóm biến phổ biến

| Pipeline | Biến thường cần |
|---|---|
| HeyGen avatar/lip-sync | `HEYGEN_API_KEY`, `HEYGEN_AVATAR_LOOKS`, đôi khi `HEYGEN_VOICE_ID` |
| ElevenLabs TTS | `ELEVENLABS_API_KEY`, `ELEVENLABS_VOICE_ID`; model và API base là tuỳ chọn |
| MiniMax TTS | `MINIMAX_API_KEY`, `MINIMAX_GROUP_ID`, `MINIMAX_VOICE_ID`; model và API base là tuỳ chọn |
| Nghiên cứu YouTube | `YOUTUBE_API_KEY` |
| B-roll Pexels | `PEXELS_API_KEY` |
| Phân tích đối thủ Apify | `APIFY_TOKEN` |
| Đăng mạng xã hội Blotato | `BLOTATO_API_KEY` |
| Tạo hình/phiên âm tuỳ chọn | `GEMINI_API_KEY`, `GOOGLE_API_KEY`, `OPENAI_API_KEY` hoặc `GROQ_API_KEY` tuỳ skill |

Không phải skill nào cũng cần API key. Chỉ cấp credential tối thiểu cho công việc đang chạy.

Module landing page BIZ.MKT.OS có danh sách Supabase, SePay, SMTP, Telegram và OpenRouter riêng. Tạo env theo mẫu:

```bash
cp 'huong dan/MKT.LANDINGPAGE.SKILLS-main/.env.example' \
  'huong dan/MKT.LANDINGPAGE.SKILLS-main/.env'
```

## 5. Kiểm tra an toàn trước khi dùng hoặc commit

Xác nhận `.env` đang bị Git bỏ qua:

```bash
git check-ignore -v .env
git ls-files .env
```

Lệnh đầu phải in ra quy tắc trong `.gitignore`. Lệnh thứ hai phải không có kết quả. Có thể liệt kê tên biến mà không lộ giá trị bằng:

```bash
awk -F= '/^[A-Za-z_][A-Za-z0-9_]*=/{print $1}' .env
```

Trước mỗi commit:

```bash
git status --short
git diff --cached --check
```

Không dùng `git add -f` với `.env`. Không dán API key vào chat, log, issue, commit message hoặc ảnh chụp màn hình. Nếu một key từng được commit hoặc chia sẻ, phải thu hồi và tạo key mới tại nhà cung cấp; xoá file ở commit mới không xoá key khỏi lịch sử Git.

## 6. Cập nhật skill về sau

Trong repo chính:

```bash
git pull --ff-only origin main
npm install
```

Nếu đã copy skill sang repo khác, chạy lại hai lệnh `rsync` ở mục 2 rồi khởi động lại agent. Trước khi đồng bộ, kiểm tra thay đổi local ở repo đích để tránh ghi đè bản skill đang tự chỉnh sửa.

## 7. Checklist bàn giao cho agent mới

- Clone đúng repo và checkout nhánh `main`.
- Đọc `AGENTS.md`, `CLAUDE.md` và nguồn Business Context phù hợp.
- Xác nhận thấy skill trong `.agents/skills/` hoặc `.claude/skills/`.
- Tạo `.env` từ `.env.example`, chỉ điền key cần thiết.
- Chạy `git check-ignore -v .env` và xác nhận `git ls-files .env` không có kết quả.
- Không commit `workspace/`, `.media-library/`, media, virtualenv, `node_modules/` hoặc credential.
- Chạy kiểm tra riêng của dự án/skill trước khi bàn giao kết quả.
