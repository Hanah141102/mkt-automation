# Quy Ước Làm Việc Trong Repo

## Cấu trúc chính

Repo này là vault Obsidian PARA + AI Brain của Tony Hoang Company, đồng thời giữ lớp runtime cho xưởng video AI.

- `00. Business Context/` là nguồn sự thật duy nhất về doanh nghiệp.
- `01. Inbox/`, `02. Projects/`, `03. Areas/`, `04. Resources/`, `05. Archive/` là cấu trúc PARA.
- `People/`, `Companies/`, `Meetings/`, `Decisions/`, `Daily/`, `Nhật Ký CEO/` là lớp thực thể và nhật ký.
- `.claude/skills/` chứa 97 skill vận hành đang bật.
- `huong dan/30. Thư Viện Skill/_Kho Skill/` là kho skill dự phòng.
- `02. Projects/Xưởng Video AI/videos/` chứa các dự án HyperFrames; `videos` ở root là liên kết tương thích.
- `04. Resources/Market & Competitor Research/Video AI/` chứa nghiên cứu YouTube; `research` ở root là liên kết tương thích.
- `workspace/` và media sinh ra là đầu ra local, không commit.

## Quy tắc nội dung vault

Đọc `CLAUDE.md` và `00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md` trước mọi khuyến nghị có ngưỡng thời gian, thiết kế phễu hoặc nội dung thương hiệu. Viết note bằng tiếng Việt, dùng wikilink cho liên kết nội bộ, không tạo note mồ côi, không bịa số liệu và không xoá lịch sử; nội dung đã đóng chuyển vào `05. Archive/`.

## Lệnh kỹ thuật

Root không có test suite chung. Cài dependency bằng `npm install`; làm mới thư viện B-roll bằng `npm run broll:seed`. Với dự án HyperFrames:

```bash
cd videos/reactjs-intro-motion
npm run dev
npm run check
npm run render
```

Sau khi sửa HTML HyperFrames, luôn chạy `npm run check`. Giữ nguyên phiên bản HyperFrames đã pin trong từng dự án.

## Phong cách code và bảo mật

Dùng indent hai khoảng trắng cho JSON, JavaScript và HTML. Tên thư mục skill/dự án dùng lowercase kebab-case; nội dung note dùng tên tiếng Việt theo quy ước trong `CLAUDE.md`. Tránh `Date.now()`, `Math.random()` và network call không được kiểm soát trong composition.

Không commit `.env`, API key, credentials, media sinh ra, `workspace/`, `.media-library/`, virtualenv hay `node_modules/`. Các thay đổi hiện có của người dùng phải được giữ nguyên.

## Nguồn tri thức cá nhân

Khi viết nội dung cần trải nghiệm, thế giới quan hoặc giọng riêng của tác giả, đọc `/Users/tonyhoang/Documents/GitHub/Tony Brain/Me.md` trước rồi tìm note liên quan trong `2. Mine/`, `3. Core/Dots/`, `4. Mint/` và các template Brand & Content. Không đưa chi tiết riêng tư hoặc dữ liệu khách hàng vào nội dung công khai nếu chưa được yêu cầu rõ ràng.
