---
name: mkt-hyperframe-raw-mp4-editor-9-16
description: "Biên tập một hoặc nhiều MP4 thô thành video kiến thức/talking-head dọc 9:16 bằng audio gốc: chép lời từng clip, xác định đúng thứ tự nội dung, loại im lặng/ậm ừ/nói sai/lặp ý bằng EDL không phá hủy, dựng rough cut, đề xuất và tải Pexels để che jump cut hoặc làm bằng chứng, thêm SFX/text effect có chủ đích, tạo subtitle trắng đậm viền đen giống video social mẫu, rồi dựng HyperFrames và render MP4. Dùng khi người dùng đã cung cấp footage MP4 quay sẵn và không muốn HeyGen, TTS hoặc MP3 voice-over."
---

# Biên tập MP4 thô 9:16 bằng HyperFrames

Biến nhiều clip quay thật thành một video 1080×1920 hoàn chỉnh. Audio trong footage là đồng hồ duy nhất. Mọi cắt ghép phải không phá hủy: giữ nguyên file gốc, lưu quyết định trong `edit-plan.json`, rồi tạo `rough-cut.mp4` mới.

## Luật cứng

1. Không gọi HeyGen, ElevenLabs, MiniMax hoặc TTS khác.
2. Không tạo `full.mp3`, `avatar.mp3` hay MP3 voice-over. SFX `.wav/.mp3` được phép vì không phải voice-over.
3. Không ghi đè, cắt trực tiếp hoặc xóa MP4 gốc. Copy vào `raw/`; mọi bản dựng là file mới.
4. Transcribe trực tiếp từng MP4 bằng Whisper với `--language vi`. Sau rough cut, transcribe lại `rough-cut.mp4`; timing caption cuối chỉ lấy từ transcript này.
5. Không đoán thứ tự theo tên file nếu tên không mang số thứ tự rõ. Ưu tiên: thứ tự user chỉ định → số take/part trong tên → mạch ý transcript → thời gian quay chỉ làm tie-breaker.
6. Chỉ bỏ filler khi cô lập được mà không làm gãy từ, đổi nghĩa hoặc tạo âm thanh cụt. Giữ nhịp nghỉ có dụng ý. Nói sai/lặp take: giữ bản hoàn chỉnh cuối cùng, ghi rõ bằng chứng trong EDL.
7. Ba giây đầu phải là face hook từ footage thật. Có thể lấy hook ở clip sau và đưa lên đầu, nhưng không dùng Pexels/HyperFrames toàn màn hình trước mốc 3,0s.
8. Pexels là bằng chứng hoặc lớp che jump cut, không phải wallpaper. Mỗi placement phải khớp danh từ + động từ của câu đang nói và không che biểu cảm/punchline cần thấy mặt.
9. Subtitle cố định theo preset `social-outline`: Be Vietnam Pro 800, trắng, viền đen, không hộp nền, căn giữa, tối đa 2 dòng; marker như `#1` đứng riêng phía trên. Đọc `references/caption-style.md`.
10. SFX tối đa 6 hit/phút, cách nhau tối thiểu 1,25s, volume 0.12–0.30. Không đặt SFX vào câu nhạy cảm, đoạn cảm xúc hoặc chỉ để lấp trống.
11. Text effect không lặp nguyên cả caption. Chỉ dùng cho con số, từ khóa, đối lập, bước hoặc kết luận cần neo trí nhớ.
12. Captions mount cuối, track 60, z-index 100. SFX dùng track 70+. Source face track 10; HyperFrames/Pexels track 40–49.
13. Scene HyperFrames là standalone HTML 1080×1920, GSAP paused timeline, root có `data-duration`, không exit animation. Nội dung quan trọng không xuống dưới `y=1460` vì subtitle ở vùng `y≈1500–1660`.
14. Nếu có từ 2 scene HyperFrames độc lập và công cụ sub-agent khả dụng, fan out một sub-agent/scene; mỗi agent chỉ sửa một file scene và không chạy HyperFrames. Orchestrator sở hữu EDL, master, captions, media, lint và render.

## Đầu vào và đầu ra

Đầu vào bắt buộc: một hoặc nhiều MP4 có lời nói. Ảnh, video minh họa và transcript tham chiếu là tùy chọn.

Tạo project tại `workspace/content/YYYY-MM-DD/<slug>/`:

```text
raw/                         # bản sao MP4 gốc, không sửa
transcripts/<clip-id>/       # transcript từng clip
clip-inventory.json
transcript-index.json
TRANSCRIPT-NGUON.md
edit-plan.json               # thứ tự + đoạn giữ/bỏ + lý do
EDIT-REVIEW.md
rough-cut.mp4                # audio gốc đã cắt, không có TTS
edit-map.json                # source time → output time
transcript.json              # transcript lại rough-cut
caption-groups.json
enhancement-plan.json        # Pexels/SFX/text effects
design.md
STORYBOARD.md
media-manifest.json
broll-clips/
scenes/
compositions/captions.html
index.html
<slug>.mp4
```

## Quy trình

### 1. Scaffold và kiểm kê MP4

Copy templates/fonts, gồm `caption-overrides.json` rỗng vào root project, đổi `name` trong `package.json`, rồi copy footage vào `raw/` bằng tên an toàn. Chạy:

```bash
python3 "$SKILL/scripts/inventory_clips.py" --project "$OUT"
```

Đọc `clip-inventory.json`; xác nhận file có video + audio, duration hợp lệ. Footage không phải 9:16 vẫn dùng được nhưng phải ghi `fit: "contain-blur"` hoặc crop có chủ đích trong EDL.

### 2. Chép lời từng clip và xác định thứ tự

Chạy `npx hyperframes transcribe <mp4> --model medium --language vi` trong từng thư mục `transcripts/<clip-id>/`, để mỗi nơi tạo `transcript.json`. Sau đó:

```bash
python3 "$SKILL/scripts/build_transcript_index.py" --project "$OUT"
```

Đọc toàn bộ `TRANSCRIPT-NGUON.md` và `references/source-editing.md`. Lập `edit-plan.json` theo schema trong reference. Mỗi segment giữ phải có `clip_id`, `source_start`, `source_end`, `reason`, `fit`; thứ tự mảng `sequence` chính là thứ tự video cuối. Mọi đoạn bỏ phải nằm trong `removed` với `reason_code` và câu/âm thanh làm bằng chứng.

Nếu có hai thứ tự hợp lý nhưng làm đổi lập luận, dừng trước khi cắt và đưa user hai phương án ngắn. Nếu mạch ý rõ, tự chọn và ghi lý do.

Chạy gate và dựng rough cut:

```bash
python3 "$SKILL/scripts/validate_edit_plan.py" --project "$OUT"
python3 "$SKILL/scripts/render_rough_cut.py" --project "$OUT"
```

Script render chuẩn hóa 1080×1920, 30fps, H.264/AAC nhưng giữ giọng thật trong MP4. Không xuất audio rời.

### 3. Transcript tổng và subtitle

Transcribe lại timeline sau cắt:

```bash
cd "$OUT"
npx hyperframes transcribe rough-cut.mp4 --model medium --language vi
python3 "$SKILL/scripts/clean_captions.py" transcript.json --output caption-groups.json
```

Chỉ sửa text khi Whisper sai; không sửa `start/end`. Với marker danh sách, thêm `label: "#1"` vào group chứa câu đầu mục và bỏ chữ “số một/thứ nhất” khỏi phần `text` nếu tự nhiên. Inject vào template:

```bash
python3 "$SKILL/scripts/inject_captions.py" compositions/captions.html caption-groups.json
```

### 4. Phân tích toàn transcript và đề xuất enhancement

Đọc `references/media-effects.md`. Tạo `enhancement-plan.json` gồm:

- `broll`: khoảng output time, ý câu nói, `intent_vi`, `query_en`, `noun`, `verb`, lý do che jump cut/bổ sung bằng chứng.
- `hyperframes`: khoảng thời gian cần giải thích cơ chế bằng `start → transformation → proof`.
- `sfx`: timestamp, cue, file, volume, lý do.
- `text_effects`: khoảng thời gian, copy ngắn, kiểu effect, spoken anchor, lý do.
- `face_moments`: hook, punchline, cảm xúc hoặc CTA bắt buộc giữ mặt.

Chạy:

```bash
python3 "$SKILL/scripts/validate_enhancement_plan.py" --project "$OUT"
```

Viết `EDIT-REVIEW.md`, `design.md`, `STORYBOARD.md` và `storyboard-preview.html`. Preview phải thể hiện ít nhất một frame cho face, Pexels, HyperFrames, text effect và subtitle preset. Đây là approval gate trước khi tải Pexels hoặc author scene. Sau khi user duyệt, chạy AUTOPILOT đến MP4, không đổi visual thesis.

### 5. Resolve Pexels và author scene

Dùng `mkt-resolve-broll-media` với các nhu cầu đã duyệt. Tải clip portrait, re-encode, giữ provenance trong `media-manifest.json`, đọc source/final contact sheet. Clip đúng chủ đề nhưng sai khoảnh khắc thì chỉnh `source_start_s` rồi resolve lại; asset lạc đề thì exclude ID và đổi query một lần.

Đọc `references/visual-thinking.md`, `references/editorial-explainer-readability.md`, `references/scene-patterns.md`, `references/design-system.md` trước khi author scene. Không đặt Pexels giữa causal trigger và proof của một HyperFrames argument.

### 6. Wire master và render

Copy `assets/templates/master-index.reference.html` thành `index.html`. Thay marker bằng duration `rough-cut.mp4`, B-roll, scene mounts, SFX và text effects đã duyệt. Source video phải có audio; không thêm audio voice-over khác. B-roll luôn `muted`.

```bash
cd "$OUT"
npm run check
npx hyperframes render -q draft -o _draft.mp4
npx hyperframes render -q standard -o <slug>.mp4
```

QA tối thiểu:

- So timeline `edit-map.json`: không thiếu từ đầu/cuối mỗi cut, không audio click, không lặp take.
- Ba giây đầu full face; mọi Pexels đúng câu và che jump cut sạch.
- Subtitle đúng preset ảnh mẫu, không nền hộp, không chồng dấu, không quá 2 dòng.
- Caption khớp word-level; mọi SFX/text effect land đúng spoken anchor.
- Không black frame quanh cut; mặt không bị crop sai; B-roll muted; audio gốc rõ và không clipping.
- Output 1080×1920, 30fps, duration khớp `rough-cut.mp4` ±0,10s.

## Tài nguyên

- `references/source-editing.md`: thứ tự semantic, ngưỡng cut và schema EDL.
- `references/caption-style.md`: preset subtitle theo ảnh user cung cấp.
- `references/media-effects.md`: cách đặt Pexels, HyperFrames, SFX và text effect.
- `references/visual-thinking.md`: visual argument và seam ledger.
- `references/editorial-explainer-readability.md`: proof-frame và readability.
- `assets/templates/`: master, captions, storyboard và scene reference.
- `scripts/`: inventory, transcript index, validators, rough-cut renderer và caption injector.

**Spec 1.0 — Raw MP4, original-audio spine, non-destructive EDL.**
