---
name: mkt-hyperframe-raw-mp4-editor-9-16
description: "Biên tập end-to-end một folder chứa MP4 thô, B-roll, ảnh/screenshot Obsidian và kho SFX thành video kiến thức/talking-head 9:16 bằng audio gốc. Tự kiểm kê toàn bộ folder, chép lời từng clip, sắp xếp và cắt bằng EDL không phá hủy, tạo storyboard bắt buộc để người dùng duyệt, ưu tiên media người dùng rồi resolve Pexels local-first, dùng HyperFrames tối giản qua sub-agent Luna, tạo caption social, đặt SFX, render draft/final và QA. Dùng khi người dùng muốn chỉ gọi một skill cho toàn bộ quy trình edit raw footage dọc, không dùng HeyGen, ElevenLabs, MiniMax, TTS hay MP3 voice-over."
---

# Raw MP4 Editor 9:16 — one-skill pipeline

Biến toàn bộ folder nguồn thành video 1080×1920 hoàn chỉnh. Dùng giọng thật trong footage làm đồng hồ duy nhất. Giữ nguyên file gốc; mọi quyết định cắt nằm trong JSON và mọi bản dựng là file mới.

## Luật cứng

1. Không gọi HeyGen, ElevenLabs, MiniMax hoặc bất kỳ TTS nào. Không tạo MP3 voice-over.
2. Không sửa, ghi đè hoặc xóa media gốc. Copy MP4 nói vào `raw/`; copy/link media minh họa vào `media/`.
3. Quét đệ quy toàn bộ folder người dùng cung cấp. Không bỏ qua subfolder, ảnh, video B-roll, screenshot hoặc SFX.
4. Transcribe từng MP4 có lời bằng Whisper `--language vi`; sau khi cắt phải transcribe lại `rough-cut.mp4` để lấy timing caption cuối.
5. Không đoán thứ tự chỉ bằng tên file. Ưu tiên: chỉ định của user → số take/part → mạch ý transcript → thời gian quay làm tie-breaker.
6. Chỉ cắt filler/sai/lặp khi không gãy từ, không đổi nghĩa và không tạo audio click. Giữ bản hoàn chỉnh nhất; ghi bằng chứng trong `edit-plan.json`.
7. Ba giây đầu phải giữ mặt thật. Không dùng Pexels hoặc HyperFrame toàn màn hình trước 3,0s.
8. Luôn tạo `STORYBOARD.md`, `storyboard-preview.html` và contact sheet để user review trước khi author scene hoặc render. Chỉ tiếp tục khi user duyệt hoặc yêu cầu render sau khi đã xem storyboard.
9. Thứ tự ưu tiên hình: media user/Obsidian → raw footage → Pexels đúng hành động → HyperFrames. Không biến screenshot thành card nhỏ nếu bằng chứng cần đọc toàn màn hình.
10. Mặc định HyperFrames chiếm không quá 20% video; real media overlay ít nhất 30%. Chỉ vượt khi storyboard ghi lý do và user duyệt.
11. Pexels phải chứng minh đúng `noun + verb`, không làm wallpaper. Mỗi clip chỉ dùng một lần, muted, 2–6s, có provenance và contact sheet.
12. Caption dùng Be Vietnam Pro 800, trắng, viền đen 6px, không hộp nền, căn giữa, tối đa 2 dòng, bottom 300px.
13. SFX tối đa 6 hit/phút, cách nhau ≥1,25s, volume 0.12–0.30. Voice phải luôn thắng.
14. Scene HyperFrame là HTML độc lập 1080×1920, GSAP `paused:true`, deterministic, không network, không loop vô hạn, không exit animation; nội dung thiết yếu ở `y<1460`.
15. Khi có ≥2 scene độc lập và sub-agent khả dụng, fan out một agent/scene. Dùng Luna cho scene đơn giản; mỗi agent chỉ sửa file scene được giao và không chạy HyperFrames. Orchestrator sở hữu EDL, media, captions, master, SFX, validation và render.
16. Bảo vệ quyền riêng tư: cắt lời nhắc lớp/trường/địa chỉ/dữ liệu khách hàng khi không cần; che logo, email, dock, webcam và dữ liệu nhạy cảm trước bản review công khai.

## Output contract

Tạo project tại `workspace/content/YYYY-MM-DD/<slug>/`:

```text
source-assets.json           # kiểm kê toàn bộ folder nguồn
PHAN_TICH_NGUON.md           # vai trò, chất lượng và rủi ro từng asset
raw/                         # bản sao MP4 nói
transcripts/<clip-id>/
clip-inventory.json
TRANSCRIPT-NGUON.md
edit-plan.json
EDIT-REVIEW.md
rough-cut.mp4
edit-map.json
transcript.json
caption-groups.json
beats.json
enhancement-plan.json
design.md
STORYBOARD.md
storyboard-preview.html
storyboard-contact-sheet.png
broll-needs.json
media-manifest.json
media/
broll-clips/
assets/sfx/
scenes/
compositions/captions.html
index.html
renders/<slug>-draft.mp4
renders/<slug>.mp4
RENDER-NOTES.md
```

## Quy trình

### 1. Scaffold và kiểm kê toàn bộ nguồn

Copy templates/fonts từ `assets/` của skill; đổi `name` trong `package.json`. Chạy:

```bash
python3 "$SKILL/scripts/inventory_source_assets.py" \
  --source "$SOURCE_DIR" --output "$OUT/source-assets.json"
```

Đọc `source-assets.json`, sau đó:

- Xem trực tiếp mọi ảnh/screenshot.
- Với mỗi video, lấy frame đầu/giữa/cuối; với raw nói, thêm frame ở các mốc transcript quan trọng.
- Phân loại `talking-head`, `screen-recording`, `user-broll`, `evidence-image`, `sfx`, `unused` trong `PHAN_TICH_NGUON.md`.
- Ghi privacy risk và crop dự kiến. Không đưa asset lạc đề vào timeline.

Copy footage nói vào `raw/` bằng tên an toàn rồi chạy:

```bash
python3 "$SKILL/scripts/inventory_clips.py" --project "$OUT"
```

### 2. Transcript, story order và rough cut

Transcribe trực tiếp từng clip trong `raw/`:

```bash
npx hyperframes transcribe <clip.mp4> --model medium --language vi
python3 "$SKILL/scripts/build_transcript_index.py" --project "$OUT"
```

Đọc toàn bộ `TRANSCRIPT-NGUON.md` và `references/source-editing.md`. Tạo `edit-plan.json`; mỗi segment giữ có `clip_id`, `source_start`, `source_end`, `reason`, `fit`. Mỗi đoạn bỏ có `reason_code` và evidence.

```bash
python3 "$SKILL/scripts/validate_edit_plan.py" --project "$OUT"
python3 "$SKILL/scripts/render_rough_cut.py" --project "$OUT"
```

Nghe/cắt thử mọi seam. Không ép duration storyboard bằng cách cắt cụt chữ; audio thật quyết định duration.

### 3. Transcript cuối và caption

```bash
cd "$OUT"
npx hyperframes transcribe rough-cut.mp4 --model medium --language vi
python3 "$SKILL/scripts/clean_captions.py" transcript.json --output caption-groups.json
python3 "$SKILL/scripts/inject_captions.py" compositions/captions.html caption-groups.json
```

Chỉ sửa lỗi nhận dạng, tên riêng và dấu câu; không tự đổi timing word-level. Đọc `references/caption-style.md`.

### 4. Creative direction và storyboard approval gate

Đọc `references/creative-direction.md`, `references/visual-thinking.md`, `references/editorial-explainer-readability.md`, `references/media-effects.md` và `references/footage-first-media.md`.

1. Trích script fingerprint.
2. Tạo nội bộ ba route khác nhau về metaphor/spatial logic/motion; chấm semantic fit, readability, originality, continuity, feasibility.
3. Chọn route tốt nhất; ghi hai route bị loại vào `design.md`.
4. Chia beat theo output time của `rough-cut.mp4`.
5. Tạo `enhancement-plan.json` gồm `face_moments`, `broll`, `hyperframes`, `sfx`, `text_effects`.
6. Tạo storyboard chi tiết: source time, output time, lời, hình, crop, motion, SFX và privacy.
7. Render `storyboard-preview.html` + contact sheet rồi dừng để user review.

Mỗi HyperFrame brief phải có `claim → source object → transformation → proof`; không dùng nhiều card cùng trọng lượng. Mỗi B-roll/screenshot phải khớp một spoken anchor cụ thể.

```bash
python3 "$SKILL/scripts/validate_enhancement_plan.py" --project "$OUT"
```

### 5. Resolve media user và Pexels trong chính skill

Đọc `references/broll-contracts.md`. Viết `broll-needs.json` từ các beat đã duyệt. User assignment luôn thắng. Resolve theo thứ tự user → SQLite local → Pexels portrait:

```bash
python3 "$SKILL/scripts/resolve_broll.py" \
  --project "$OUT" \
  --needs "$OUT/broll-needs.json" \
  --library "$PROJECT_ROOT/.media-library" \
  --download-missing \
  --max-assets 8
```

Không in hoặc ghi `PEXELS_API_KEY`; script đọc từ `<repo>/.env` hoặc environment. Đọc `broll-source-contact-sheet.jpg` trước, rồi `broll-contact-sheet.jpg`. Sai interval thì chỉnh `source_start_s`; sai asset thì thêm `exclude_asset_ids`, cụ thể hóa query và rerun đúng một lần. Vẫn sai thì bỏ asset.

Ảnh/screenshot Obsidian phải có placement trong `enhancement-plan.json` và `media-manifest.json`, kể cả khi không đi qua resolver video. Crop theo một mục tiêu đọc: title, prompt, verdict hoặc node trung tâm; bỏ sidebar/dock/webcam không cần thiết.

### 6. Author HyperFrames bằng Luna

Chỉ chạy sau approval. Đọc `references/scene-patterns.md`, `references/design-system.md` và `references/raw-video-anti-patterns.md`.

Prompt mỗi scene agent gồm:

- Absolute output file, composition id, duration và local cue time.
- Voice beat nguyên văn; scene brief + proof frame từ storyboard.
- `design.md`, persistent motif, seam ledger và khoảng B-roll che scene.
- Typography tiếng Việt, caption-safe zone, `fromTo`, cold-seek safety, seeded randomness.
- Cấm sửa master/caption/media, cấm render và cấm đổi visual thesis.

Không tạo thêm HyperFrame chỉ để lấp khoảng trống. Nếu ảnh Obsidian hoặc Pexels đã chứng minh được câu nói, dùng media thật.

### 7. Wire master, SFX và draft

Copy `assets/templates/master-index.reference.html` thành `index.html`. Source video giữ audio; mọi B-roll `muted`. Track: source 10, scene 40+, media 45+, caption 60, SFX 70+.

Đọc `references/sfx-design.md`. Copy kho SFX người dùng vào `assets/sfx/`, probe duration, viết cue sheet và chỉ đặt hit ở spoken/visual anchor. Không thêm nhạc nền nếu user không yêu cầu.

```bash
cd "$OUT"
npm run check
npx hyperframes render --no-browser-gpu --workers 2 -q draft \
  -o renders/<slug>-draft.mp4
```

Nếu auto GPU treo sau calibration, chuyển ngay sang `--no-browser-gpu --workers 2`; không chờ vô hạn.

### 8. QA và final

Tạo contact sheet 10–12 mốc và frame tại hook, mọi seam, proof, SFX, CTA. Kiểm tra:

- 3 giây đầu là face thật; không lộ dữ liệu riêng tư hoặc logo cần che.
- Không thiếu/chặt chữ ở mọi EDL seam; không click, clipping hoặc duplicate take.
- Screenshot đọc được trên điện thoại; Pexels đúng noun + verb; không frame đen.
- Caption đúng text/timing/safe zone; SFX không lấn voice.
- `npm run check` không có error; cảnh báo phải được review và ghi vào `RENDER-NOTES.md`.
- `ffprobe`: H.264, 1080×1920, 30fps, AAC 48kHz, duration khớp `rough-cut.mp4` ±0,10s.

Sau khi user duyệt draft:

```bash
npm run check || exit 1
npx hyperframes render -q standard -o renders/<slug>.mp4
ffprobe renders/<slug>.mp4
```

## Tài nguyên cần đọc theo giai đoạn

- Cắt nguồn: `references/source-editing.md`.
- Caption: `references/caption-style.md`.
- Storyboard: `references/creative-direction.md`, `references/visual-thinking.md`.
- Readability: `references/editorial-explainer-readability.md`.
- Enhancement/media: `references/media-effects.md`, `references/footage-first-media.md`, `references/broll-contracts.md`.
- HyperFrames: `references/scene-patterns.md`, `references/design-system.md`, `references/raw-video-anti-patterns.md`.
- SFX: `references/sfx-design.md`.
- Scripts: inventory, transcript index, EDL/rough cut, media resolver, validators và caption injector.

**Spec 2.0 — one skill, raw footage, original audio, storyboard-first, footage-first.**
