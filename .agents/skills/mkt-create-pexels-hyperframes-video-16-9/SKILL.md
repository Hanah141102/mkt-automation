---
name: mkt-create-pexels-hyperframes-video-16-9
description: Tạo video giải thích ngang 16:9 từ kịch bản tiếng Việt bằng ElevenLabs, Pexels, HyperFrames và sound effect. Dùng khi cần lọc script TTS, tạo voice MP3, làm storyboard HTML có timeline để duyệt, rồi phối B-roll, motion graphic và SFX theo từng câu hoặc từ khóa, render bản nháp và QA trước bản master.
---

# Tạo video Pexels + HyperFrames 16:9

## Mục tiêu

Biến một kịch bản giáo dục hoặc hướng dẫn dài thành video 1920×1080, 30 fps. Dùng Pexels như cảnh B-roll chính khi hình ảnh đời thực truyền đạt tốt; dùng HyperFrames toàn màn hình cho quy trình, prompt, bảng, sơ đồ và khái niệm trừu tượng; dùng overlay nhẹ khi hai lớp bổ trợ cho nhau.

Giữ đúng hai cổng duyệt của người dùng:

1. Tạo và giao MP3 cùng storyboard HTML để duyệt.
2. Chỉ sau khi được duyệt mới tải media đầy đủ, dựng HyperFrames và render video nháp.

Không tự động vượt qua cổng duyệt dù người dùng đã cung cấp kịch bản hoàn chỉnh.

## Hợp đồng đầu ra

Tạo dự án trong `workspace/content/YYYY-MM-DD/<slug>/` theo cấu trúc ở [production-contract.md](references/production-contract.md). Sản phẩm tối thiểu gồm:

- `script/script-source.md`: bản gốc, không sửa âm thầm.
- `script/script-tts.md`: bản đã lọc để đọc thành tiếng.
- `audio/voiceover.mp3`: voice ElevenLabs.
- `audio/qa/word-timestamps.json`: timestamp theo từ hoặc transcript tương đương.
- `audio/sfx-plan.json`: hiệu ứng âm thanh gắn với từ/cụm từ cần nhấn.
- `storyboard/storyboard.html`: storyboard trực quan, mở độc lập trong trình duyệt.
- `planning/beats.json` và `planning/media-plan.json`: nhịp lời thoại và phương án hình.
- `media/media-manifest.json`: nguồn, tác giả, URL và dấu vết của mọi tài sản.
- `render-draft/<slug>-draft-vN.mp4`: bản nháp có thể duyệt.
- `render-draft/<slug>-draft-vN-contact-sheet.jpg`: ảnh QA tổng quan.

## Trạng thái bắt buộc

Đi theo đúng chuỗi:

`SCRIPT → TTS_REVIEW → STORYBOARD_REVIEW → MEDIA_RESOLUTION → BUILD → DRAFT_REVIEW → MASTER`

Nếu chưa có phản hồi duyệt MP3 và storyboard HTML, dừng ở `STORYBOARD_REVIEW`. Có thể sửa voice/storyboard nhiều vòng nhưng không bắt đầu tải hàng loạt Pexels hoặc render video.

## Quy trình

### 1. Kiểm tra dự án và nguồn

- Đọc kịch bản, yêu cầu về tỉ lệ, giọng đọc, phong cách, logo và tài liệu tham chiếu.
- Nếu dự án đã tồn tại, kiểm tra các thay đổi của người dùng và tái sử dụng phần đã được duyệt.
- Xác nhận mọi tên sản phẩm, dữ liệu riêng tư, câu trích dẫn và tuyên bố có cần kiểm chứng hay không.
- Không đưa dữ liệu bí mật hoặc dữ liệu khách hàng lên dịch vụ AI nếu chưa được phép.

### 2. Lọc script TTS

Gọi `$mkt-elevenlabs-tts-to-mp3` cho bước tạo giọng. Trước khi gửi TTS:

- Bỏ heading Markdown, bullet marker, URL, citation, chú thích nguồn và ký hiệu không cần đọc.
- Giữ nguyên ý nghĩa, số liệu và thứ tự lập luận; không tự rút gọn nội dung.
- Chuyển danh sách thành câu nói tự nhiên, thêm ngắt đoạn hợp lý.
- Chuẩn hóa cách đọc các tên như Zoom, Loom, Fathom, NotebookLM, M4A, MP3 và từ giao diện tiếng Anh.
- Lưu bản đã lọc riêng để người dùng so sánh với bản gốc.

Tạo MP3 và word alignment nếu ElevenLabs trả về. Nếu chỉ có MP3, dùng transcript có timestamp để dựng cue, đồng thời đánh dấu đây là timing suy ra.

### 3. Chia beat theo lời thoại

Chia voice thành các beat ngắn dựa trên ý nghĩa và timestamp, không chia đều theo thời lượng. Một beat thường là một câu hoặc một mệnh đề có hình ảnh riêng.

Với mỗi beat, ghi:

- `start_s`, `end_s`, lời thoại và từ khóa được nhấn.
- `mode`: `BROLL_PRIMARY`, `HYPERFRAME_FULL` hoặc `BROLL_PLUS_OVERLAY`.
- media query, cue xuất hiện chữ/ảnh/logo, SFX và kiểu chuyển cảnh.
- mục đích truyền đạt: vấn đề, hành động, quy trình, bằng chứng hoặc kết quả.

Đọc [visual-routing.md](references/visual-routing.md) để chọn mode. Khi ý nghĩa đổi, ưu tiên đổi cảnh; không kéo một clip chung chung qua nhiều ý chỉ để giảm số asset.

### 4. Tạo storyboard HTML để duyệt

Storyboard phải là một file HTML trực quan 16:9, không chỉ là bảng văn bản. Nó cần:

- Trình phát `voiceover.mp3`, play/pause, scrub timeline và tổng thời lượng.
- Card 16:9 cho từng beat, tự highlight theo thời gian phát.
- Hiển thị câu voice, thời gian, mode, bố cục, Pexels query/thumbnail dự kiến, chữ và logo sẽ xuất hiện.
- Hiển thị tên, loại và timestamp của SFX tại các từ/cụm từ cần nhấn.
- Mô phỏng thứ tự xuất hiện của chữ/card theo cue; không để toàn bộ nội dung hiện ngay từ đầu cảnh.
- Nêu rõ cảnh nào là B-roll toàn màn hình, cảnh nào là HyperFrames toàn màn hình.
- Dùng đường dẫn tương đối để có thể mở local; không nhúng API key.

Ở giai đoạn này chỉ dùng placeholder hoặc thumbnail shortlist. Giao cho người dùng hai link có thể mở/phát: MP3 và `storyboard/storyboard.html`. Yêu cầu duyệt hoặc ghi chú sửa, rồi dừng quy trình tại đây.

### 5. Phân giải Pexels sau khi được duyệt

Sau khi có xác nhận:

- Tìm video Pexels landscape theo ý nghĩa từng beat, không chỉ theo một từ khóa chung của cả đoạn.
- Ưu tiên clip có chủ thể/hành động rõ, khung hình phù hợp vùng đặt overlay và đủ thời lượng để trim.
- Mỗi asset chỉ dùng một lần trong cùng video, trừ khi người dùng yêu cầu motif lặp lại.
- Tăng số clip nếu lời thoại đổi chủ thể, hành động, địa điểm hoặc kết quả.
- Tải bản video từ nguồn Pexels chính thức và lưu URL trang, video ID, tác giả, truy vấn, kích thước, thời lượng và SHA-256 vào manifest.
- Tải logo Zoom, Loom, Fathom hoặc sản phẩm khác từ brand kit/trang chính thức khi kịch bản nhắc đến; giữ tỉ lệ và khoảng thở của logo.

Chuẩn hóa clip về H.264, landscape, 30 fps, có keyframe dày để seek/render ổn định. Loại clip dọc, clip mờ, logo/watermark lạ hoặc nội dung không đúng ngữ cảnh.

### 6. Dựng HyperFrames theo timestamp

Gọi `$hyperframes` và `$hyperframes-cli` cho phần HTML motion và render. Tuân thủ:

- Canvas 1920×1080, 30 fps, deterministic; không dùng `Date.now()` hoặc `Math.random()`.
- B-roll là lớp hình chính ở `BROLL_PRIMARY`; không đặt một UI opaque che kín rồi biến B-roll thành nền trang trí.
- `HYPERFRAME_FULL` dùng trọn màn hình cho flow bốn bước, prompt, bảng nhiệm vụ, dashboard và kho kiến thức.
- `BROLL_PLUS_OVERLAY` chỉ thêm chữ/cards cần thiết, giữ phần lớn khung hình nhìn thấy được.
- Từ khóa, icon, logo và ảnh chỉ đi vào khi voice vừa nhắc đến. Suy ra cue từ word timestamp, không dùng toàn bộ caption như một slide tĩnh.
- Dùng chuyển cảnh push, wipe, zoom, flash hoặc blur có chủ đích; giữ một hệ chuyển cảnh nhất quán và tránh hiệu ứng gây mất khả năng đọc.
- Giữ title/action safe, tương phản tốt và không nhồi chữ.

### 7. Thiết kế sound effect theo từ khóa

Đọc [sound-design.md](references/sound-design.md), rồi tạo `audio/sfx-plan.json` từ word timestamp:

- Dùng `impact` cho con số hoặc kết luận mạnh; `pop` cho keyword/card/logo; `click` cho thao tác UI; `tick` cho checklist; `warning` cho cảnh báo; `success` cho xác nhận; `whoosh` cho chuyển section.
- Đặt transient sát từ đầu của cụm được nhấn, thường sớm hơn không quá 2–3 frame.
- Không chèn hiệu ứng vào mọi câu. Ưu tiên điểm ngoặt, số liệu, tên công cụ, thao tác và kết luận.
- Giữ SFX thấp hơn voice; tránh bass hoặc whoosh dài che phụ âm tiếng Việt.
- Ghi nguồn/license vào manifest nếu dùng SFX bên ngoài. Ưu tiên SFX tự tổng hợp để có kết quả deterministic.
- Không xem việc có cue trong JSON là bằng chứng SFX nghe được. Phải kiểm tra bản mix thật trên loa laptop.

Kiểm tra plan và mix sau khi đã có draft hình:

```bash
python3 scripts/mix_sfx.py --video draft.mp4 --plan audio/sfx-plan.json --output draft-with-sfx.mp4 --dry-run
python3 scripts/mix_sfx.py --video draft.mp4 --plan audio/sfx-plan.json --output draft-with-sfx.mp4
```

Sau lần mix đầu:

- Nghe spot-check quanh `impact`, một chuỗi `tick/click`, một `whoosh`, một `warning` và cue kết bằng cả tai nghe lẫn loa laptop.
- So sánh cửa sổ 0,3–0,5 giây quanh ít nhất ba cue với draft không SFX. Nếu peak thay đổi dưới khoảng 1,5 dB và hiệu ứng không nghe rõ, tăng `master_gain_db` theo nấc 3 dB rồi mix lại.
- Giữ gain cuối của từng cue không lớn hơn `-8 dB`. Nếu voice bị che, giảm hoặc bỏ cue thay vì tăng toàn bộ mix.
- Dùng limiter với auto-level tắt (`level=false`) để tránh limiter tự nâng toàn bộ chương trình.
- Sau mã hóa AAC, yêu cầu `max_volume <= -1 dB`; decode lại toàn bộ video.

### 8. Kiểm tra media plan trước render

Chạy:

```bash
python3 scripts/validate_media_plan.py \
  --plan /absolute/path/to/project/planning/media-plan.json \
  --project /absolute/path/to/project \
  --require-files
```

Sửa mọi lỗi về timeline, mode, media bị dùng lại, clip dọc, asset thiếu hoặc cue nằm ngoài beat. Không render khi validator còn lỗi.

### 9. Render nháp và QA

- Chạy `npm run check` sau mỗi thay đổi HTML HyperFrames.
- Render draft MP4 trước, chưa xuất bản master.
- Kiểm tra `ffprobe`, decode toàn bộ bằng `ffmpeg -f null -`, độ phân giải, fps, audio và duration.
- Tạo contact sheet bằng:

```bash
python3 scripts/make_video_contact_sheet.py \
  --video /absolute/path/to/draft.mp4 \
  --plan /absolute/path/to/project/planning/media-plan.json \
  --output /absolute/path/to/contact-sheet.jpg
```

- Xem contact sheet và spot-check đầu/giữa/cuối mỗi cảnh quan trọng.
- Giao MP4 nháp, contact sheet, storyboard và manifest để người dùng duyệt.
- Chỉ render hoặc đổi tên thành master sau khi người dùng chấp thuận draft.

## Tiêu chí đạt

- MP3 và storyboard HTML đã được duyệt trước khi dựng.
- Hình đổi theo ý nghĩa từng câu; không lặp một B-roll quá lâu.
- Không dùng Pexels như nền phụ ở mọi cảnh.
- Toàn bộ chữ, ảnh, logo và card xuất hiện đúng nhịp được nói tới.
- Có cả B-roll chính lẫn HyperFrames toàn màn hình khi nội dung cần.
- Không tái sử dụng asset ngoài chủ đích; mọi nguồn có manifest.
- Không có frame đen, media hỏng, timeline hở/chồng, clip dọc hoặc chữ ngoài safe area.
- Draft decode được hoàn toàn, 1920×1080, 30 fps và audio rõ.
- SFX xuất hiện đúng cụm từ, không lấn voice, không dày đặc và không vượt peak an toàn.
- Các cue đại diện nghe rõ trên loa laptop; không chấp nhận bản chỉ có SFX về mặt kỹ thuật nhưng không cảm nhận được.

## Tài liệu đi kèm

- Đọc [production-contract.md](references/production-contract.md) khi tạo cấu trúc dự án và JSON.
- Đọc [visual-routing.md](references/visual-routing.md) khi chia beat, chọn B-roll/HyperFrames và thiết kế cue.
- Đọc [sound-design.md](references/sound-design.md) khi chọn, căn timing và mix SFX.
- Dùng [media-plan.example.json](references/media-plan.example.json) làm mẫu tối thiểu cho validator.
