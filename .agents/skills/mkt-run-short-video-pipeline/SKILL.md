---
name: mkt-run-short-video-pipeline
description: Điều phối workflow video ngắn 9:16 từ một ý tưởng hoặc video mẫu đến ý tưởng nội dung, kịch bản, storyboard, MP4 và phân phối đa nền tảng bằng các sub-agent chuyên môn. Dùng khi người dùng muốn chạy trọn pipeline content video với ba cổng duyệt idea–script–storyboard hoặc nói fast, fastmode, autopilot để tự duyệt, rồi đăng bằng Composio/Blotato lên đúng Page hoặc kênh đã chọn.
---

# Điều Phối Video Ngắn Đa Kênh

Biến một ý tưởng hoặc video tham chiếu thành video ngắn 9:16 đã kiểm tra và phân
phối lên social. Giữ ownership của trạng thái, phiên bản, cổng duyệt và quyền
publish ở orchestrator; giao từng giai đoạn chuyên môn cho đúng skill con.

## Quy tắc bất biến

1. Đọc `CLAUDE.md`, `00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md`, hồ sơ
   doanh nghiệp, brand voice và phân khúc liên quan trước khi tạo content. Nếu
   nội dung dùng trải nghiệm hoặc giọng riêng của tác giả, đọc thêm nguồn tri
   thức cá nhân theo `AGENTS.md`.
2. Không chép hoặc diễn giải lại logic chi tiết của skill con. Đọc và tuân thủ
   `SKILL.md` của skill con ngay trước khi giao việc.
3. Chạy các stage phụ thuộc theo thứ tự; đóng hoặc chờ agent stage trước hoàn
   tất rồi mới mở stage sau. Chỉ fan-out song song ở nơi skill dựng video yêu
   cầu một agent cho mỗi scene.
4. Orchestrator giữ `workflow-state.json`, kiểm tra artifact, ghi approval và
   vô hiệu đầu ra downstream khi upstream thay đổi. Sub-agent không tự chuyển
   stage hoặc tự ghi approval.
5. `fast` chỉ bỏ các lần chờ duyệt biên tập. Không bỏ validator, QA, xác minh
   tài khoản, quyền công bố, điều kiện an toàn hoặc yêu cầu bằng chứng.
6. Không coi `fast` là quyền đăng. Chỉ publish khi người dùng đã chọn
   `publish_action: now|schedule` và đích cụ thể. Thiếu đích thì dừng ở
   `READY_TO_PUBLISH`.
7. Không retry thao tác publish mù. Luôn xác minh submission/post trước khi
   thử lại vì upload và publish không idempotent.
8. Không để hai agent sửa cùng một file. Mỗi agent chỉ sở hữu artifact được
   giao; orchestrator tích hợp sau khi agent hoàn tất.

## Skill con bắt buộc

| Stage | Skill | Vai trò |
|---|---|---|
| Phân tích video mẫu | `mkt-phan-tich-video-notebooklm` | Trích cấu trúc, luận điểm, hook và insight có nguồn |
| Phát triển ý tưởng | `content-ideation` | Tạo, sàng lọc và chấm điểm góc nội dung |
| Viết kịch bản | `video-script` | Viết lời đọc, production cues, shot list và overlay |
| Dựng video | `mkt-hyperframe-knowledge-video-heygen-9-16-lite` | TTS, storyboard, scene fan-out, QA và render 9:16 |
| Phân phối | `mkt-blotato-publish-social` | Caption theo kênh, publish, verify và báo cáo URL |

Nếu đầu vào là ý tưởng, bỏ qua agent phân tích nguồn. Không thay skill dựng
video bằng sibling khác trừ khi người dùng thay đổi rõ định dạng hoặc yêu cầu
avatar.

## Đầu vào và mặc định

Thu thập hoặc suy ra các trường sau:

- `mode`: `review` mặc định; chuẩn hóa `fastmode` hoặc `autopilot` thành `fast`
  và chỉ dùng khi người dùng nói rõ.
- `input.type`: `idea`, `youtube_url`, `url` hoặc `local_file`.
- `input.value`: ý tưởng, URL hoặc đường dẫn tuyệt đối.
- `duration_s`: mặc định 30–60 giây cho short-form.
- `audience`, `goal`, `cta`, `tone`: ưu tiên nguồn sự thật doanh nghiệp.
- `publish_action`: `prepare_only` mặc định, hoặc `now`, `schedule`.
- `stop_after`: `idea`, `script`, `storyboard`, `video` hoặc `publish`. Mặc
  định `video`; tự đặt `publish` khi user yêu cầu `now|schedule`.
- `publish_targets[]`: platform, tên đích và ID xác định được.
- `scheduled_time_utc`: bắt buộc khi `publish_action=schedule`.

Nếu dữ kiện thương hiệu còn ở trạng thái đề xuất/chờ xác nhận, gắn nhãn giả
định. Trong `fast`, dừng khi giả định đó có thể tạo tuyên bố công khai sai về
giá, kết quả, khách hàng, pháp lý hoặc cam kết thương hiệu.

`prepare_only` nghĩa là vẫn tạo và QA MP4 nhưng không publish. Nếu người dùng
chỉ muốn chuẩn bị idea, script hoặc storyboard, dùng `stop_after` tương ứng.

## Hai chế độ

### `review` — ba cổng duyệt

1. `IDEA_REVIEW`: trình `idea-review.md` rồi dừng.
2. `SCRIPT_REVIEW`: trình `video-script.md` rồi dừng.
3. `STORYBOARD_REVIEW`: trình `design.md`, `STORYBOARD.md`,
   `storyboard-preview.html` và contact sheet rồi dừng.

Không thêm gate duyệt MP4 thứ tư. Sau khi storyboard được duyệt, tự render,
QA và publish tới các đích đã được cấp quyền ở intake. Nếu QA buộc phải đổi
thông điệp, lời đọc hoặc visual thesis đã duyệt, quay lại gate tương ứng.

Để giữ đúng gate của `video-script` mà không phát sinh thêm lần chờ, gói
`idea-review.md` phải chứa creative brief và outline hoàn chỉnh. Approval Gate
1 đồng thời xác nhận topic, format, duration, key points, CTA, tone, audience,
hook và outline. Agent viết script nhận chính artifact đã được duyệt này.

### `fast` — tự duyệt có dấu vết

Orchestrator chọn phương án đạt điểm cao nhất, tự kiểm rồi ghi
`auto_approved` cho idea, script và storyboard. Vẫn tạo đủ artifact review để
có thể audit. Chỉ hỏi người dùng khi gặp hard block: nguồn không truy cập được,
thiếu credential, TTS/visual/lip-sync validator fail, target mơ hồ, tuyên bố
không có bằng chứng hoặc thay đổi cần chủ thương hiệu quyết định.

## Khởi tạo run và trạng thái

Tạo thư mục:

```text
workspace/content/YYYY-MM-DD/<slug>/
```

Copy `assets/workflow-state.template.json` thành `workflow-state.json`, điền
đường dẫn tuyệt đối và không lưu token/credential. Đọc
`references/handoff-contracts.md` để dùng đúng schema artifact và prompt giao
việc.

Chạy validator trước khi resume, trước mỗi stage có side effect và trước khi
publish:

```bash
python3 <skill-dir>/scripts/validate_workflow_state.py \
  --state <run-dir>/workflow-state.json
```

Để kiểm tra có được chuyển sang stage kế tiếp hay không:

```bash
python3 <skill-dir>/scripts/validate_workflow_state.py \
  --state <run-dir>/workflow-state.json --next-stage VIDEO
```

Exit khác 0 nghĩa là dừng và sửa trạng thái/artifact; không bỏ qua validator.

## Workflow

### 1. Preflight

1. Chuẩn hóa đầu vào, mode, duration, mục tiêu và CTA.
2. Nếu user muốn đăng, kiểm tra read-only kết nối và đối chiếu target ngay từ
   đầu; chưa upload hoặc publish.
3. Khởi tạo state ở `INTAKE` và ghi mọi giả định.
4. Nếu source là video mẫu, chuyển sang `SOURCE_ANALYSIS`; nếu không, chuyển
   thẳng `IDEA`.

### 2. Phân tích video mẫu

Spawn một source analyst dùng `mkt-phan-tich-video-notebooklm`. Yêu cầu phân
tích pattern, không sao chép câu chữ, sequence độc đáo hoặc tuyên bố không có
nguồn. Ghi `source-analysis.md`, kết thúc agent, rồi chuyển artifact cho idea
agent.

### 3. Tạo idea package

Spawn một idea strategist dùng `content-ideation`. Tạo một phương án khuyến
nghị và hai phương án dự phòng. Phương án khuyến nghị phải có đủ creative brief
và outline để thỏa Phase 1–2 của `video-script`.

Ghi `idea-review.md`. Trong `review`, chuyển `IDEA_REVIEW`, trình link và dừng.
Trong `fast`, tự chấm bảy lớp, ghi `auto_approved` rồi tiếp tục.
Nếu `stop_after=idea`, bàn giao package và không gọi scriptwriter.

### 4. Viết script

Chỉ chạy khi idea version hiện tại đã được `approved` hoặc `auto_approved`.
Spawn một scriptwriter dùng `video-script`; truyền nguyên brief + outline đã
duyệt và chỉ định output `video-script.md`. Bắt buộc kiểm tra word count, thời
lượng, hook, một CTA, lời nói tự nhiên và visual cue.

Trong `review`, chuyển `SCRIPT_REVIEW`, trình link và dừng. Trong `fast`, tự
kiểm rồi ghi `auto_approved`.
Nếu `stop_after=script`, bàn giao script package và không gọi video skill.

### 5. Tạo storyboard và dựng video

Chạy `mkt-hyperframe-knowledge-video-heygen-9-16-lite` bằng script version đã
duyệt. Orchestrator giữ quyền tích hợp master; skill video sở hữu TTS alignment,
avatar windows, storyboard, Pexels, scene fan-out, captions, lint, render và QA.

Ở `review`, yêu cầu skill video dừng sau khi tạo đủ approval package và chuyển
state sang `STORYBOARD_REVIEW`. Chỉ sau approval mới cho skill video fan-out
scene và render. Ở `fast`, ghi `auto_approved`, nhưng vẫn chạy toàn bộ approval
artifact và validator của skill video.

Nếu `stop_after=storyboard`, bàn giao approval package và không author scene.

Sau render, xác minh MP4 tồn tại, 1080×1920, duration đúng và các quality gate
PASS. Ghi absolute path vào state rồi chuyển `READY_TO_PUBLISH`.
Nếu `stop_after=video`, dừng tại đây dù `publish_action` đang là
`prepare_only`.

### 6. Publish và verify

Nếu `publish_action=prepare_only`, dừng ở `READY_TO_PUBLISH` và giao MP4 cùng
caption package. Nếu là `now|schedule`, validator phải xác nhận video và target
đã đủ.

Spawn đúng một publisher agent dùng `mkt-blotato-publish-social` cho toàn bộ
platform để giữ upload reuse và tránh đăng trùng. Truyền exact MP4 path,
platform, account/page/channel ID, publish action và scheduled time. Agent phải
verify từng kết quả, ghi `publish-report.md`, submission ID và public URL. Chỉ
chuyển `DONE` sau khi trạng thái từng target đã được báo rõ thành công hoặc lỗi.

## Approval, revision và resume

- Chỉ chấp nhận approval cho đúng artifact version đang hiện hành.
- Khi tạo artifact lần đầu, đặt version của artifact đó thành `1`; version `0`
  nghĩa là artifact chưa tồn tại và không thể được duyệt.
- Mỗi artifact ghi dependency version trong `dependencies`; validator phải xác
  nhận script trỏ đúng idea, storyboard trỏ đúng script, video trỏ đúng script
  + storyboard và publish trỏ đúng video.
- Sửa idea: tăng `versions.idea`; đặt approval idea mới về `pending`; đặt
  approval downstream thành `invalidated`, xóa active pointers của script,
  storyboard và video rồi quay lại `IDEA_REVIEW`.
- Sửa script trong phạm vi brief/outline đã duyệt: tăng `versions.script`, đặt
  approval script mới về `pending`; giữ idea approval, đặt storyboard approval
  thành `invalidated`, xóa active pointers của storyboard/video và quay lại
  `SCRIPT_REVIEW`. Nếu đổi topic, audience, CTA, key points hoặc outline, coi là
  sửa idea và quay lại `IDEA_REVIEW`.
- Sửa storyboard: tăng `versions.storyboard`, đặt approval mới về `pending`,
  xóa active video pointer và quay lại `STORYBOARD_REVIEW`.
- Khi invalidated, giữ counter của artifact cũ và archive file `-vN`; chỉ tăng
  counter khi artifact thay thế thực sự được tạo. Vô hiệu toàn bộ TTS,
  alignment, beats, avatar windows, B-roll placement, scene và captions phụ
  thuộc script/storyboard cũ.
- Không xóa artifact cũ; giữ lịch sử bằng suffix `-vN` hoặc chuyển bản đóng vào
  thư mục archive của run.
- Nếu phiên bản cũ đã publish, không xóa submission ID, URL hoặc bài live. Lưu
  chúng vào publish report lịch sử, đặt run mới về `prepare_only` và chỉ repost
  khi người dùng cấp quyền publish mới.
- Agent trả một trong `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_REVIEW`, `BLOCKED`.
  `DONE_WITH_CONCERNS` không được tự vượt gate nếu concern ảnh hưởng claim,
  brand, timing, visual thesis hoặc publish target.
- Khi resume, đọc state + kiểm tra file thật trên disk; không dựa vào hội thoại
  cũ hoặc suy đoán stage.

## Bàn giao cuối

Báo ngắn gọn:

1. Idea, script và storyboard version đã dùng.
2. Absolute path MP4, duration, ratio avatar và visual mix.
3. Mỗi nền tảng: Page/kênh, trạng thái, submission ID và public URL.
4. Target lỗi hoặc đang xử lý; không gọi là published nếu verify chưa thành
   công.
5. Các giả định, concern hoặc việc người dùng còn phải xử lý.
