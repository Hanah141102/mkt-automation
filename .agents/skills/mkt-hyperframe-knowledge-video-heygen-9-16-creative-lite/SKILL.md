---
name: mkt-hyperframe-knowledge-video-heygen-9-16-creative-lite
description: Create a cost-efficient 9:16 knowledge, business, or AI video with selected HeyGen avatar windows, ElevenLabs v3 narration, contextual Pexels cutaways, captions, sound design, and original HyperFrames art direction invented from each script. Use when the user wants a vertical short video like a premium AI explainer but does not want a fixed palette, stock template, repeated card layout, PIP presenter, or a prescribed HyperFrames style.
---

# Creative HyperFrame Video 9:16 LITE

Tạo video dọc 1080×1920 trong đó HeyGen chỉ xuất hiện ở hook, re-hook và CTA. Dùng ElevenLabs v3 làm audio spine; Pexels làm cutaway có ý nghĩa; HyperFrames do AI tự thiết kế theo nội dung từng kịch bản. Không dùng PIP.

Giữ pipeline kỹ thuật của bản LITE, nhưng trao quyền tự do cao cho art direction. Không mặc định AI-HUB Editorial Explainer, không sao chép visual DNA của video trước và không ép scene vào card/blueprint/flow có sẵn.

## Quyền tự do sáng tạo

AI PHẢI tự quyết định theo kịch bản:

- Visual thesis và metaphor xuyên suốt.
- Palette, typography, chất liệu, độ sáng, mức hiện thực và mật độ hình.
- Hero object, camera language, bố cục, motion route và transition family.
- Scene nào dùng UI thật, logo công cụ, typography kinetic, diagram, vật thể 2.5D hoặc footage.
- Pexels placement theo hành động đang nói, không theo quota máy móc.

Không bắt đầu từ một style preset. Bắt đầu từ `script → meaning → visual verb → proof`. Đọc đầy đủ `references/creative-direction.md` trước khi viết `design.md` hoặc storyboard.

## Hợp đồng kỹ thuật không được phá

1. Tạo project 1080×1920; audio spine là `audio/full.mp3` từ ElevenLabs v3.
2. Chỉ gửi `audio/avatar.mp3` cho HeyGen. Giữ avatar ratio mặc định 0,30–0,42; dùng một look nhất quán và một lần gọi.
3. Giữ mặt avatar full-screen ít nhất 3 giây đầu. Không đặt scene hoặc B-roll đè hook trước mốc 3,0 giây.
4. Không tạo hoặc mount PIP. Avatar chỉ xuất hiện ở các window full-screen.
5. Mỗi scene là một HTML độc lập 1080×1920, load bằng `data-composition-src`.
6. Dùng GSAP timeline `paused:true`; seed mọi randomness; không network call trong composition; không loop vô hạn.
7. Lấy TOTAL từ `ffprobe audio/full.mp3`. Lấy duration avatar clip từ `ffprobe` từng file.
8. Đo sync HeyGen bằng `verify_avatar_sync.py`; dừng nếu `low-confidence` hoặc `stretched`.
9. Mount caption cuối cùng ở track 60, z-index 100; timing lấy từ word-level alignment, không sửa tay timing.
10. Dùng Whisper `--language vi`. Không đưa heading Markdown hoặc nhãn Hook/CTA vào lời đọc.
11. Orchestrator giữ ownership của `index.html`, avatar windows, captions, audio, SFX, validation và render.
12. Fan out một sub-agent cho mỗi scene sau khi storyboard được duyệt. Sub-agent chỉ sửa file scene được giao và không chạy `npx hyperframes`.

## Typography tiếng Việt

- Dùng font local có đủ dấu; ưu tiên Be Vietnam Pro hoặc font được user cung cấp.
- Headline mặc định 64–84px, tối đa 2 dòng khi có thể.
- Dùng line-height 1,14–1,22; không siết letter-spacing quá `-0.04em`.
- Giữ tối thiểu 48px khoảng trống giữa headline và hero visual.
- Giữ vùng `y>=1480` cho caption; không đặt nội dung thiết yếu ở đó.
- Không dùng `data-layout-allow-overlap` để che lỗi chữ.
- Luôn chụp frame có chữ in hoa và dấu Việt. Nếu bounding box, dấu hoặc hai dòng chạm nhau, giảm size/tăng line-height rồi render lại.
- Không đặt “tên video” thành câu voiceover mở đầu. Bắt đầu thẳng từ hook của kịch bản.

## Creative direction gate

Trước khi author scene:

1. Trích `script_fingerprint`: chủ đề, cảm xúc, mức khẩn cấp, danh từ hữu hình, động từ chính, proof cần thấy.
2. Tạo nội bộ ba visual route khác nhau. Không chỉ đổi màu; phải khác metaphor, spatial logic và motion route.
3. Chấm mỗi route theo semantic fit, readability, originality, continuity và feasibility. Chọn route tổng điểm cao nhất.
4. Viết `design.md`, `STORYBOARD.md` và `storyboard-preview.html` bằng route đã chọn.
5. Storyboard preview phải có một proof frame 9:16 cho mỗi scene, tab chuyển scene, timeline Pexels/avatar và vị trí SFX quan trọng.
6. Trình HTML + contact sheet để user duyệt. Chỉ author scene sau khi được duyệt.

Không hỏi user chọn giữa ba route trừ khi hai route dẫn đến trải nghiệm thật sự khác nhau hoặc liên quan nhận diện thương hiệu. Ghi ngắn gọn hai route bị loại và lý do vào `design.md`.

## Visual argument cho mỗi scene

Khai báo trong `STORYBOARD.md`:

```yaml
claim: ""
visual_verb: "split | expose | compress | route | compare | unlock | repair | verify | ..."
source_object: ""
start_state: ""
transformation: ""
end_state: ""
proof: ""
causal_trigger: "cụm từ voiceover + local_s"
focal: ""
supporting: []
motion_route: ""
transition_in: {vector: "", carrier: ""}
transition_out: {vector: "", carrier: ""}
tail_behavior: "live-resolution | deliberate-stillness"
headline: ""
takeaway: ""
proof_hold_s: 0.9
continuous_hf_s: 3.5
```

Scene fail nếu chỉ có các card xuất hiện, nếu hình chỉ “cùng chủ đề”, hoặc nếu không nhìn thấy `start_state → transformation → proof` khi tắt tiếng.

## Pexels và media thật

Đọc `references/media-broll.md`, rồi dùng skill `mkt-resolve-broll-media`.

- Dùng Pexels như cutaway hành động/evidence, không làm wallpaper.
- Mặc định dùng 3–6 clip, mỗi clip 2,6–4,0 giây, phân tán qua video.
- Mục tiêu mặc định là 25–42% non-avatar time để còn đủ thời lượng cho HyperFrames kể trọn visual argument.
- Cho phép thay đổi bounds theo storyboard đã duyệt. Ghi rõ bounds vào frontmatter.
- Không đặt B-roll trên avatar window hoặc giữa causal trigger và proof của HyperFrames.
- Mỗi clip chỉ dùng một lần, muted, re-encode H.264 yuv420p, kiểm tra source và trimmed contact sheet.
- Khi script nói đến thao tác thực tế, ưu tiên close-up tay, màn hình, giấy tờ hoặc hai người cùng kiểm tra.
- Khi script gọi tên ChatGPT, Claude hay công cụ khác, dùng logo chính xác và UI mô phỏng có chủ đích; không dùng logo trang trí ở scene không liên quan.

Chạy gate với bounds của skill:

```bash
python3 "$SKILL/scripts/validate_visual_mix.py" \
  --project "$OUT" --min-pexels 0.25 --max-pexels 0.42 --min-assets 3
```

Nếu video quá ngắn để có 3 clip tốt, ghi override vào storyboard và dùng ít nhất 2 asset.

## SFX theo nghĩa và hành động

Đọc `references/sfx-layer.md` trước khi wire master.

- Gắn SFX vào từ/cụm từ hoặc hành động nhìn thấy được.
- Dùng keyboard typing trong đúng khoảng prompt hiện dần.
- Dùng click khi gửi prompt/chọn lựa; whoosh ở chuyển cảnh; boom ở punchline; ting/success ở proof hoặc reveal.
- Không rải SFX theo nhịp cố định. Không dùng quá một loud effect trong cùng một khoảnh khắc.
- Giữ SFX thấp hơn voiceover và kiểm tra bằng tai ở bản draft.

## Pipeline

### 1. Scaffold

```bash
PROJECT_ROOT=$(pwd)
OUT=$PROJECT_ROOT/workspace/content/$(date +%Y-%m-%d)/<slug>
SKILL=<absolute path to this skill>
mkdir -p "$OUT"/{audio,scenes,assets/sfx,compositions,avatar-clips,broll-clips,media}
cp "$SKILL/assets/templates/hyperframes.json" "$OUT/"
cp "$SKILL/assets/templates/package.json" "$OUT/"
cp "$SKILL/assets/templates/master-index.reference.html" "$OUT/index.html"
cp "$SKILL/assets/templates/captions.html.template" "$OUT/compositions/captions.html"
cp "$SKILL/assets/templates/caption-overrides.json" "$OUT/"
cp "$SKILL/assets/templates/storyboard.reference.md" "$OUT/STORYBOARD.md"
cp "$SKILL/assets/fonts/"* "$OUT/assets/fonts/"
```

### 2. Script, TTS và beat map

- Viết hook thẳng vào vấn đề; không đọc tiêu đề video.
- Đánh dấu avatar ở hook/re-hook/CTA trong `beats-spec.json`.
- Tạo TTS ElevenLabs v3 và validate trước mọi bước tốn phí:

```bash
python3 "$SKILL/scripts/tts.py" --script script.md --out-audio audio/full.mp3 --out-alignment audio/alignment.json
python3 "$SKILL/scripts/validate_tts_alignment.py" --script script.md --alignment audio/alignment.json
python3 "$SKILL/scripts/map_beats.py" --project "$OUT"
python3 "$SKILL/scripts/cut_avatar_audio.py" --project "$OUT"
```

### 3. Creative storyboard và approval

- Đọc `references/creative-direction.md` và `references/visual-thinking.md`.
- Dùng `assets/templates/storyboard.reference.md` làm contract, không làm style preset.
- Tạo `design.md`, `STORYBOARD.md`, `storyboard-preview.html` và contact sheet.
- Chờ user duyệt. Sau approval, giữ nguyên visual thesis nhưng cho từng scene tự sáng tạo trong cùng grammar.

### 4. Pexels, HeyGen và captions

- Resolve Pexels, ghi placement vào `media-manifest.json`, chạy visual-mix gate.
- Chỉ gửi `audio/avatar.mp3` cho `mkt-heygen-mp3-to-mp4`.
- Chạy `split_avatar_video.sh` và đọc toàn bộ báo cáo sync.
- Transcribe `audio/full.mp3`, clean, fix typo và inject captions.

### 5. Fan-out scene authoring

Spawn scene agents trong cùng một đợt khi có slot. Dùng Luna cho scene đơn giản, Terra cho metaphor/layout phức tạp. Prompt mỗi agent phải chứa:

- Output file tuyệt đối và composition id.
- Voiceover beat + cue time local.
- Scene brief nguyên văn từ storyboard.
- `design.md`, seam ledger và Pexels interval che scene.
- Yêu cầu đọc `assets/templates/scene-reference-full.html` chỉ như technical scaffold, không sao chép màu/bố cục.
- Quy tắc typography tiếng Việt, caption safe zone, GSAP paused timeline, seeded randomness.
- Cấm sửa master, cấm render, cấm tạo visual khác direction đã duyệt.

Mỗi agent tự review bảy câu: claim có nhìn thấy không; object có đổi trạng thái không; focal có thắng không; cue có đúng VO không; dấu Việt có thoáng không; proof giữ đủ lâu không; seam có match không.

### 6. Master wiring

Wire theo `references/avatar-windows-layout.md`:

- Avatar track 10+, scene track 40+, B-roll track 45+, caption track 60, SFX track 70+.
- B-roll full-screen nằm trên scene, dưới captions; dùng fade 0,18–0,28 giây và push-in nhẹ.
- Dùng clean cut hoặc opaque masked reveal; không crossfade hai hình bán trong suốt.
- Khi prompt được đọc/gõ, reveal theo word/phrase và đồng bộ keyboard SFX.

### 7. Validate, draft và QA

```bash
python3 "$SKILL/scripts/validate_visual_mix.py" --project "$OUT" --min-pexels 0.25 --max-pexels 0.42 --min-assets 3
cd "$OUT"
npm run check
npx hyperframes render -q draft -o _draft.mp4
```

Chụp frame bằng `ffmpeg -i _draft.mp4 -ss <time> -frames:v 1 ...` tại:

- Mỗi headline sau entrance.
- Causal trigger, giữa transformation và proof của từng scene.
- Giữa từng B-roll.
- ±0,3 giây quanh mọi avatar↔scene↔B-roll seam.
- Prompt typing, CTA và frame cuối.

Tạo contact sheet. Soi chữ chồng, dấu Việt, caption safe zone, logo/UI, Pexels relevance, frame đen, lip-sync và audio balance. Nếu có lỗi, sửa rồi render lại; không bàn giao bản chưa xem frame.

### 8. Final render

```bash
python3 "$SKILL/scripts/validate_visual_mix.py" --project "$OUT" --min-pexels 0.25 --max-pexels 0.42 --min-assets 3 || exit 1
npm run check || exit 1
npx hyperframes render -q standard -o <slug>.mp4
ffprobe <slug>.mp4
```

Báo đường dẫn tuyệt đối, duration, resolution, ratio avatar, ratio Pexels/HyperFrames và số Pexels asset đã dùng/bỏ.

## Quality gate

- Video mở thẳng bằng hook, không có title narration thừa.
- 3 giây đầu full face; không PIP.
- HyperFrames có art direction riêng phù hợp kịch bản, không giống template được đổi màu.
- Mỗi scene có một hero transformation và proof rõ.
- Các scene khác bố cục nhưng cùng visual grammar/persistent motif.
- Headline không chồng dấu; caption không che nội dung chính.
- B-roll thực sự mô tả hành động đang nói và xuất hiện đủ thường xuyên.
- Logo/UI chỉ xuất hiện khi có vai trò trong ý nghĩa.
- Prompt typing hiện dần đúng nhịp và có keyboard SFX khi kịch bản yêu cầu.
- SFX khớp câu nói/hành động, không lấn voice.
- `npm run check`, visual-mix validator, frame QA và ffprobe đều pass.

## Tài nguyên cần đọc theo giai đoạn

- Creative storyboard: `references/creative-direction.md`, `references/visual-thinking.md`.
- Typography/layout QA: `references/editorial-explainer-readability.md` chỉ dùng phần readability; không kế thừa palette/preset.
- Media: `references/media-broll.md`.
- Avatar: `references/heygen-integration.md`, `references/avatar-windows-layout.md`.
- Audio: `references/elevenlabs-v3.md`, `references/sfx-layer.md`.
- Failure modes: `references/anti-patterns.md`.
- Technical HTML scaffold: `assets/templates/scene-reference-full.html`.

Skill không chứa design system hoặc scene-pattern cố định. Luôn sinh style và visual route từ script fingerprint.

---

Spec version 1.0 — adaptive script-led creative direction, HeyGen LITE, no PIP, contextual Pexels, Vietnamese-safe typography.
