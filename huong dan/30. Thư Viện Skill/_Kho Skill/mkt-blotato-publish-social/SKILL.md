---
name: mkt-blotato-publish-social
description: >-
  Đăng content (MP4 video, ảnh, text) lên nhiều nền tảng social. Ưu tiên
  Composio khi CLI và kết nối nền tảng đã tồn tại; dùng Blotato API làm
  fallback — Facebook Page (feed/reel/story), TikTok, Instagram, YouTube,
  Threads, X/Twitter, LinkedIn. USE WHEN user nói "đăng video lên fanpage",
  "post lên tiktok", "đăng đa nền tảng", "publish lên facebook và tiktok",
  "blotato", "composio", "đăng reel", "phân phối video lên social", "đăng
  mp4 vừa render lên fb", "share video lên các kênh", hoặc sau khi một video
  skill render xong MP4 và user muốn đăng nó lên mạng xã hội.
---

# Composio-first Multi-Platform Publisher

Đăng 1 content lên mạng xã hội bằng Composio nếu có thể; Blotato là đường dự
phòng. Không tự in hoặc lưu access token trong log, file output hay báo cáo.

## Composio-first policy

1. Chạy `command -v composio`. Nếu có, ưu tiên Composio.
2. Kiểm tra toolkit và account bằng `composio whoami`; dùng `composio search
   "<platform> upload"` rồi `composio execute <SLUG> --get-schema` nếu chưa
   biết action hoặc schema.
3. Xác minh đúng đích theo tên/ID user yêu cầu trước khi upload. Không suy đoán
   từ account cá nhân và không đăng sang Page/kênh khác.
4. Dùng action native của nền tảng và truyền file local qua `--file` khi schema
   hỗ trợ; không upload video lên Blotato trước nếu Composio đã có action.
5. Sau khi đăng, lấy ID/permalink từ response và gọi action verify tương ứng.
   Không retry mù vì upload là thao tác không idempotent.
6. Chỉ dùng Blotato khi `composio` không tồn tại, toolkit đích chưa kết nối
   sau khi đã báo lỗi, hoặc Composio không hỗ trợ nền tảng user yêu cầu.

Composio command mẫu cho Page đã được người dùng chọn:

```bash
composio execute FACEBOOK_CREATE_VIDEO_POST \
  --file /absolute/path/video.mp4 \
  -d '{"page_id":"<FACEBOOK_PAGE_ID>","title":"Tiêu đề video","description":"Caption ở đây...","published":true}'
```

Nếu chưa biết slug hoặc schema, dùng `composio search`, sau đó
`composio execute <SLUG> --get-schema`; không đoán input.

### YouTube / YouTube Shorts bằng Composio

Khi user nói “đăng lên YouTube Short”, “đăng YouTube” hoặc chỉ rõ tên kênh:

1. Xác minh channel đang được kết nối, không dùng handle đoán mò:

```bash
composio execute YOUTUBE_GET_CHANNEL_STATISTICS \
  -d '{"mine":true,"part":"snippet,statistics"}'
```

Đối chiếu `snippet.localized.title` (và `id`) với tên kênh user yêu cầu. Nếu
không khớp hoặc chưa đăng nhập, dừng và báo user; không upload nhầm kênh.

2. Dùng `YOUTUBE_MULTIPART_UPLOAD_VIDEO`. Với `--file`, không thêm
`videoFile` vào JSON vì CLI sẽ inject path vào field file uploadable:

```bash
composio execute YOUTUBE_MULTIPART_UPLOAD_VIDEO \
  --file /absolute/path/video.mp4 \
  -d '{"title":"CEO đừng ngồi đợi AI: Thiết kế hệ thống thay vì canh từng việc #Shorts","description":"CEO đừng ngồi đợi AI.\n\nKhi chỉ giao từng việc một, AI có thể chạy nhanh hơn nhưng hàng đợi vẫn còn đó. Hãy chuyển vai: chốt đầu ra, tiêu chí xong và cổng duyệt để agent tự phối hợp.\n\n#AI #Automation #AIWorkflow #CEO #Shorts","categoryId":"28","privacyStatus":"public","tags":["AI Automation","AI workflow","CEO","agent AI","tự động hóa"]}'
```

- `categoryId: "28"` phù hợp nội dung Science & Technology; đổi khi chủ đề
  khác.
- Chỉ dùng `privacyStatus: "public"` khi user đã yêu cầu đăng/xuất bản công
  khai (ví dụ “đăng lên YouTube”); nếu user chỉ nói upload, hỏi lại hoặc dùng
  `unlisted` theo chỉ dẫn.
- Shorts nên là MP4 dọc 9:16, thời lượng ngắn (dự án này giữ dưới 60 giây),
  title có hook và thêm `#Shorts` trong title/description.

3. Verify bằng video ID trả về:

```bash
composio execute YOUTUBE_GET_VIDEO_DETAILS_BATCH \
  -d '{"id":["<VIDEO_ID>"],"parts":["snippet","status","contentDetails"]}'
```

Kiểm tra `snippet.channelTitle`, `status.privacyStatus`,
`status.uploadStatus`, `contentDetails.duration` và tạo permalink dạng
`https://youtube.com/shorts/<VIDEO_ID>`. Báo user channel, title, trạng thái và
URL; nếu upload thành công nhưng đang xử lý, nói rõ trạng thái đó.

## Blotato fallback

Khi Composio không khả dụng, đăng content qua [Blotato](https://blotato.com)
bằng helper script `scripts/blotato_publish.py` (python3 stdlib, không cần pip).

## Prerequisites

- `BLOTATO_API_KEY` trong `.env` ở project root (script tự walk-up tìm). Đã set sẵn.
- Tài khoản social phải được kết nối trước trong Blotato dashboard
  (https://my.blotato.com → Accounts). API **không** kết nối account mới được.

## Xác định tài khoản đích

- Nhận `platform`, `account_id`, `page_id` hoặc tên kênh từ người dùng/brand context.
- Liệt kê tài khoản đang kết nối rồi đối chiếu cả tên và ID trước khi đăng.
- Không dùng Page, profile hoặc kênh từng dùng ở lần chạy trước làm mặc định.
- Nếu có nhiều đích trùng tên hoặc người dùng chưa chọn rõ, dừng và hỏi xác nhận.
- Có thể lưu mapping theo từng thương hiệu trong file cấu hình local không chứa token; không hard-code vào skill.

```bash
SKILL_DIR="$(pwd)/.agents/skills/mkt-blotato-publish-social"
python3 "$SKILL_DIR/scripts/blotato_publish.py" accounts
```

## Workflow

### Bước 0 — Có MP4 chưa?
Nếu user muốn "tạo video rồi đăng": chạy video skill phù hợp trước
(`mkt-hyperframe-*`, `mkt-full-video-*`) ra MP4, rồi quay lại đây.

### Bước 1 — Viết caption per-platform (đừng dùng 1 caption cho mọi nền tảng)
- **Facebook**: caption dài hơn, hook dòng đầu, 3-5 hashtag cuối, tiếng Việt tự nhiên.
- **TikTok**: `--text` ngắn + hashtags; `--title` ≤ 90 ký tự (hook chính).
- **YouTube Shorts**: title có hook (nên thêm `#Shorts`), description 2-4 câu
  giải thích lợi ích + 3-5 hashtag; giữ tiếng Việt tự nhiên và kiểm tra đúng
  channel trước khi upload.
- Tự viết từ nội dung video nếu user không đưa caption. Không hỏi lại.

### Bước 2 — Publish

**Ưu tiên Composio nếu CLI và toolkit đích đã kết nối:**

```bash
composio execute FACEBOOK_CREATE_VIDEO_POST \
  --file /absolute/path/video.mp4 \
  -d '{"page_id":"<FACEBOOK_PAGE_ID>","title":"Tiêu đề video","description":"Caption ở đây...","published":true}'
```

Lưu `data.id` trả về, không retry mù vì thao tác này không idempotent. Verify
bằng `FACEBOOK_GET_PAGE_POSTS` hoặc `FACEBOOK_GET_PAGE_VIDEOS`; nếu cần
permalink, dùng `FACEBOOK_GET_POST` với composite ID mà bước verify trả về.

**YouTube Shorts (Composio):** dùng quy trình xác minh channel →
`YOUTUBE_MULTIPART_UPLOAD_VIDEO` → `YOUTUBE_GET_VIDEO_DETAILS_BATCH` ở trên.
Lưu `data.video.id` (hoặc video ID tương đương) và chỉ báo đã publish sau khi
verify trả về đúng `channelTitle` + `privacyStatus`.

**Blotato fallback (script tự upload media local qua presigned flow):**

Facebook Reel lên fanpage đã xác minh:
```bash
python3 "$SKILL_DIR/scripts/blotato_publish.py" publish \
  --platform facebook --account-id <ACCOUNT_ID> --page-id <PAGE_ID> \
  --fb-media-type reel \
  --media /absolute/path/video.mp4 \
  --text "Caption tiếng Việt ở đây..." \
  --wait 300
```
- Bỏ `--fb-media-type` → post feed thường. `story` cũng hợp lệ.

TikTok (sau khi đã kết nối, lấy accountId từ `accounts`):
```bash
python3 "$SKILL_DIR/scripts/blotato_publish.py" publish \
  --platform tiktok --account-id <TIKTOK_ACCOUNT_ID> \
  --media /absolute/path/video.mp4 \
  --text "Caption + #hashtags" --title "Hook ngắn ≤90 ký tự" \
  --wait 300
```
- Video HeyGen/AI mặc định được gắn nhãn AI (`isAiGenerated: true`). Chỉ thêm
  `--no-ai-label` khi video là footage quay thật.
- Privacy mặc định `PUBLIC_TO_EVERYONE`; test thì dùng `--tiktok-privacy SELF_ONLY`.

Đăng cùng 1 video lên nhiều nền tảng: **upload 1 lần, tái dùng URL** —
```bash
BLOTATO_URL=$(python3 "$SKILL_DIR/scripts/blotato_publish.py" upload /absolute/path/video.mp4)
# rồi publish nhiều lần với --media "$BLOTATO_URL" (script nhận diện URL blotato, không upload lại)
```

Lên lịch thay vì đăng ngay: thêm `--scheduled-time 2026-06-11T09:00:00Z` (UTC; giờ VN = UTC+7).

### Bước 3 — Verify + báo cáo
- `--wait` đã poll sẵn: exit 0 + JSON có `publicUrl` = published; exit 2 = failed
  (đọc `errorMessage`, fix rồi thử lại — lỗi thường gặp: video quá dài/quá nặng
  cho platform, thiếu quyền page).
- Check lại sau: `python3 .../blotato_publish.py status <postSubmissionId>`
- Báo cáo cho user: mỗi platform 1 dòng — tên page/kênh + public URL (hoặc lý do fail).
- Log hive mind (action `published_social`) theo quy tắc agent.

## Gotchas

- `mediaUrls` phải là URL thuộc domain blotato — script tự lo việc này, đừng đưa
  thẳng URL ngoài vào content khi tự gọi API tay.
- Rate limit: 30 posts/phút, 120 presigned uploads/phút.
- TikTok bắt buộc đủ bộ flags (privacy/duet/stitch/AI) — script đã set default đúng.
- `presignedUrl` hết hạn nhanh — script PUT ngay sau khi tạo, đừng tách 2 bước thủ công.
- Nền tảng chưa kết nối → API trả lỗi account không tồn tại: nhắc user vào
  my.blotato.com kết nối, KHÔNG tự retry vô ích.
- MP4 > giới hạn plan của Blotato → upload fail; báo size + path cho user.
