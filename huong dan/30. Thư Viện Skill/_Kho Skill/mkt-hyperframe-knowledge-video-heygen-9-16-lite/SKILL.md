---
name: mkt-hyperframe-knowledge-video-heygen-9-16-lite
description: Create a cost-efficient 9:16 knowledge or news video with HeyGen only for selected hook/CTA windows, evidence-led Pexels, and readable editorial HyperFrames. Use when the user wants vertical avatar content with reduced HeyGen usage, ElevenLabs or MiniMax audio, storyboard/styleframe approval, familiar visual metaphors, and a validated default-balanced or user-approved readability-first Pexels/HyperFrames mix.
---

# HyperFrame Knowledge Video LITE — HeyGen 30-40% + Editorial HyperFrames/Pexels

Video kiến thức 9:16 dọc (1080×1920): HeyGen avatar full-screen **chỉ trong các window** — hook mở đầu, 1-2 re-hook giữa video, CTA cuối (tổng 30-40% thời lượng). Trong **thời gian không có avatar**, mặc định cân bằng Pexels full-screen và pure HyperFrames; ưu tiên block HyperFrames đủ dài để một visual argument đọc được trọn vẹn. Không dùng PIP, captions vẫn chạy theo layout. Credit HeyGen chỉ tốn cho ~35% audio. Render bằng `npx hyperframes render`.

**APPROVAL GATE:** Khi tạo visual direction mới hoặc đổi nhận diện, phải trình `design.md` + `STORYBOARD.md` + motion board/styleframes thể hiện `start → transformation → proof` cho user duyệt trước khi author scene. Với video kiến thức/kinh doanh, mặc định dựng thêm `storyboard-preview.html`: một proof frame 9:16/scene, có tab chuyển scene, rồi chụp contact sheet. Storyboard phải có visual thesis, scene brief và seam ledger; contact sheet đẹp nhưng không có shared object/carrier vẫn fail. Sau khi user duyệt HTML/styleframe, AUTOPILOT được phép chạy một mạch tới MP4 bằng đúng preset đó.

## Khi nào dùng skill này

- Video knowledge/news **9:16 dọc** có AI avatar nhưng **cần tiết kiệm credit HeyGen** (default cho hầu hết case)
- User có **ảnh/video trám** muốn chèn vào video (bỏ vào `media/`)
- User nói "avatar 50%" hay ratio khác → vẫn skill này, chỉnh `--min-ratio/--max-ratio`

KHÔNG dùng khi:
- User nói rõ muốn avatar dẫn **suốt video** → sibling `mkt-hyperframe-knowledge-video-heygen-9-16`
- 16:9 ngang → `mkt-hyperframe-knowledge-video-heygen-16-9`
- Footage quay sẵn → `mkt-hyperframe-talking-head-video`
- Không cần avatar → `mkt-hyperframe-knowledge-video`

## Khác biệt với sibling 9:16 gốc

| Aspect | Gốc (avatar 100%) | LITE (skill này) |
|---|---|---|
| HeyGen input | full.mp3 (60-120s) | **avatar.mp3 (~30-40%)** — tiết kiệm ~60-65% credit |
| Layout | FULL↔SPLIT height tween + divider | **Avatar window ↔ scene full-canvas**, không split |
| Scene canvas | 1080×960 top half | **1080×1920 full-canvas** |
| Audio spine | `<audio>` từ source.mp4 | **audio/full.mp3** (TTS gốc) |
| Video HeyGen | 1 file source.mp4 | **N clips** avatar-clips/clip-NN.mp4 |
| Presence khi vắng avatar | — | **Không PIP** — dành toàn canvas cho Pexels/HyperFrames |
| Media trám user cung cấp | — | **Có** — tự phân tích + tự gán beat |
| Visual mix khi vắng avatar | Chủ yếu motion graphics | Default **Pexels 50% / HyperFrames 50%**; cho phép approved readability override |
| TOTAL | ffprobe source.mp4 | **ffprobe audio/full.mp3** |

## HARD RULES (NON-NEGOTIABLE)

1. **Fan out parallel LLM sub-agents** — 1 sub-agent / scene. KHÔNG dùng Python template generator.
2. **Scene HTML = standalone full HTML doc 1080×1920 FULL-CANVAS**, load qua `data-composition-src`. Root `<div data-composition-id="scene-NN-slug" data-width="1080" data-height="1920">`, CSS scoped.
3. **GSAP only**, seeded mulberry32 PRNG (seed 0x5cNN), `window.__timelines[...] = gsap.timeline({paused:true})`, entrances `gsap.fromTo()`, no exit anims, scene KHÔNG load gsap riêng.
4. **HeyGen CHỈ nhận `audio/avatar.mp3`** (output `cut_avatar_audio.py`) — gửi nhầm `full.mp3` là mất toàn bộ khoản tiết kiệm. 1 lần gọi duy nhất (1 avatar look nhất quán).
4a. **TTS source contract:** Markdown headings (`# Title`, `## Hook`, `## Problem`...) chỉ là metadata để map beat, KHÔNG phải lời đọc. Viết narration ở các dòng bên dưới heading; `tts.py` và `tts_minimax.py` tự loại toàn bộ dòng heading trước khi gọi TTS. Sau TTS phải chạy `validate_tts_alignment.py`; nếu fail thì dừng trước khi cắt audio hoặc gọi HeyGen.
5. **Budget guard 0.30–0.42**: `cut_avatar_audio.py` fail sớm nếu ratio avatar ngoài khoảng — sửa window TRƯỚC khi tốn credit. User yêu cầu ratio khác → truyền `--min-ratio/--max-ratio`.
6. **TOTAL + mọi data-duration overlay = ffprobe `audio/full.mp3`** — KHÔNG phải video HeyGen. Avatar mount `data-duration` = ffprobe từng clip.
6b. **Vị trí cắt clip phải ĐO, không được đoán.** `split_avatar_video.sh` luôn chạy `verify_avatar_sync.py` trước: nó dò từng chunk `avatar.mp3` trong audio HeyGen trả về (tương quan envelope) để biết HeyGen dịch/padding bao nhiêu, và đo cả **drift nội bộ** (miệng khớp đầu clip nhưng lệch dần về cuối — một điểm cắt không sửa được). Cắt theo offset đã gửi (hoặc rescale theo tỉ lệ duration) là sai khi HeyGen padding — test cho thấy lệch tới 360ms, quá ngưỡng cảm nhận ~80ms. Xử lý theo status: `stretched` (exit 4) → split tự dừng, chạy lại Phase 2 hoặc chẻ window dài thành 2 beat ngắn; `low-confidence` (exit 3) → dừng kiểm tra file, đừng render.
7. **3 giây đầu LUÔN full face** — window hook start=0; scene mount đầu tiên không start trước 3.0s và không được opacity-overlay lên mặt trước mốc này.
8. **Ranh giới avatar↔scene**: mount đầu segment thường start = `window.end − 0.25`; riêng hook ngắn phải dùng `max(3.0, window.end − 0.10)` để giữ đủ 3 giây full-face. Mount cuối segment end = ĐÚNG `nextWindow.start`. Mặc định clean cut hoặc masked reveal opaque; cấm translucent crossfade làm hai lớp hình chồng nhau. Flash tối đa 1 `loud moment`.
9. **Scene full-canvas vùng cấm**: không content dưới `y≈1480` (caption safe zone). Không cần chừa góc trên bên phải vì pipeline **không dùng PIP**. Headline tiếng Việt 68–84px, tối đa 2 dòng/4–8 từ, line-height 1.08–1.15, letter-spacing ≥−0.015em. Text trong hero visual tối thiểu 28px; 18–20px chỉ cho micro status/mã rất ngắn. Cấm `data-layout-allow-overlap` cho text.
10. **AI-HUB Editorial Explainer là mặc định cho knowledge/business**: warm ivory `#F7F3EE`, graphite `#1F2430`, copper `#C96A2B`, orange `#E07A3B`, sand `#E9DED2`, glow `#F2B277`. Dùng headline lớn + một vật thể quen thuộc ở display scale + takeaway; blueprint/flow chỉ giải thích cơ chế bên trong. Cấm cyberpunk blue, starfield, neon, glassmorphism đại trà và particle bokeh. Đọc `references/design-system.md` và `references/editorial-explainer-readability.md`.
11. **Motion phải có nghĩa**: mỗi beat khai báo `motion_intent`, `visual_anchor`, `transition_in`, `transition_out`, `sound_cue`. Một beat chỉ có 1 hero animation; cả video tối đa 2 họ transition. Không dùng bounce/back/elastic trừ `back.out(1.15)` cho một module-lock nhỏ.
11a. **Mỗi scene là một visual argument, không phải slide minh họa**: bắt buộc khai báo `claim`, `persuasion`, `source_object`, `start_state`, `transformation`, `end_state`, `causal_trigger`, `motion_route`, `focal`, `supporting`, `scale_plan`, `vo_cues`, `tail_behavior`. Thiếu `source_object + transformation + end_state` → redesign brief, không chữa bằng card/icon/VFX. Đọc `references/visual-thinking.md`.
11b. **Continuity do orchestrator sở hữu**: trước fan-out phải có `STORYBOARD.md` + seam ledger `{exit_vector, entry_vector, carrier, relationship}`. Scene ra/vào cùng một chuyển động phải match vector và dùng carrier thật; clean cut chỉ khi có contrast/punchline có chủ đích. Sub-agent không tự phát minh seam riêng.
11c. **Voiceover là đồng hồ**: focal và supporting land theo `vo_cues` lấy từ word-level alignment. Causal trigger phải xảy ra đúng từ/cụm từ được nói. Scene phải tiếp tục `live-resolution` tới hết beat hoặc khai báo `deliberate-stillness`; cấm tail chết vì timeline hết sớm.
11d. **Proof-frame readability**: mỗi scene khai báo `headline`, `familiar_object`, `visible_action`, `takeaway`, `proof_hold_s`, `continuous_hf_s`. Hero chiếm 55–65% vùng nội dung; proof giữ ≥0,90s; một visual argument HyperFrames nên có block liên tục ≥3,5s. Không đặt Pexels giữa `trigger → transformation → proof`. Tắt tiếng và freeze proof frame vẫn phải hiểu claim.
12. **Root `#root` PHẢI có `data-duration`** + mọi loop hữu hạn tính từ TOTAL. Background chỉ được có glow/line drift tinh tế; không sinh hàng chục particles để “lấp chỗ trống”.
13. **Captions mount CUỐI, track 60, z-index 100**, `.caption-stage` bottom:220–280, timing từ word-level transcript của **full.mp3**, KHÔNG hand-edit timing. Caption Be Vietnam Pro 44–50px, tối đa 2 dòng, nền graphite 88%; không che headline/diagram.
14. **Visual mix mặc định 50/50, readability được ưu tiên khi user duyệt**: `scene_time = fullTotal − union(avatar windows)`. Default gate là Pexels 45–55%. Nếu quota làm hero transformation bị cắt hoặc `continuous_hf_s < 3.5`, trình user một readability override trong `STORYBOARD.md` gồm lý do, min/max Pexels và thời lượng HF liên tục từng scene. Chỉ dùng override sau approval; vẫn cần ít nhất 2 Pexels evidence asset. Chỉ footage `usage:"broll-fullscreen"` có provenance Pexels mới được tính.
14a. **Pexels là bằng chứng/hành động, không phải wallpaper**: footage phải khớp danh từ + động từ của câu nói. Ưu tiên close-up thao tác, người chờ, viết brief, giao việc, làm song song; cấm clip “văn phòng đẹp” không liên quan. Dùng ít nhất 2 asset, không đặt trên `avatar:true`, mỗi asset 1 lần, muted + re-encode.
14b. **Fail-fast trước render**: luôn chạy `validate_visual_mix.py` sau khi chốt placement và ngay trước final. Default không truyền bounds. Với override đã duyệt, truyền đúng `--min-pexels/--max-pexels` đã ghi trong storyboard; không được bỏ validator. Exit khác 0 → sửa placement/assets; KHÔNG render final.
15. **Text–Speech–Image Gate**: tại từng beat, headline/diagram/Pexels phải diễn đạt cùng một ý với voiceover; không lặp nguyên caption thành headline. Fail nếu hình chỉ “cùng chủ đề” nhưng không thể hiện đúng hành động/hệ quả.
16. **Sub-agents KHÔNG chạy `npx hyperframes`** — orchestrator validate tập trung.
17. **Không PIP**: không tạo, không mount và không animate `pip-still`; avatar chỉ xuất hiện trong các avatar window full-screen.
18. **Whisper LUÔN `--language vi`** cho audio Việt.

Anti-patterns chung: `references/anti-patterns.md`.

## MODEL ROUTING & SUB-AGENT POLICY

Mặc định dùng **GPT-5.6-Luna** cho các scene độc lập và hiệu ứng HyperFrames đơn giản. Luna phù hợp với công việc có scope rõ, chỉ sở hữu một file scene, không cần quyết định timing liên scene và không tạo external side effects.

| Model / role | Phạm vi được giao | Không giao |
|---|---|---|
| `gpt-5.6-luna` · `thinking=low` | Author scene HTML 1080×1920; blueprint line, module-lock, flow-trace, keyword reveal; self-review cục bộ | `index.html`, avatar windows, captions, HeyGen, dependency, render |
| `gpt-5.6-terra` · `thinking=medium` | Scene có visual metaphor phức tạp, nhiều lớp layout, media/b-roll hoặc cần quyết định hierarchy | TTS alignment, HeyGen sync và final render |
| `gpt-5.6-sol` · `thinking=high` | Review chéo khi scene fail lint/inspect, lỗi timing, CSS scope, loop hoặc lỗi tích hợp nhiều scene | Viết thay toàn bộ pipeline nếu chỉ là lỗi cục bộ |
| Orchestrator | Tạo scaffold, chia scene, giữ ownership của master, xử lý TTS/HeyGen/captions/SFX, lint/inspect/render/QA | Giao quyền sửa `index.html` hoặc render cho sub-agent |

### Routing rules

1. Fan out **một sub-agent cho mỗi scene** trong cùng một message; mỗi agent chỉ được sở hữu file output của scene đó.
2. Gắn `model: "gpt-5.6-luna"` và `thinking: "low"` cho scene đơn giản. Không dùng Luna cho task có nhiều file hoặc phụ thuộc trạng thái HeyGen.
3. Nếu scene có visual metaphor mới, nhiều media hoặc logic timing phức tạp, dùng Terra ngay từ đầu.
4. Nếu Luna fail gate lần đầu, cho Luna sửa lỗi cục bộ một lần. Nếu lỗi liên quan master, timing hoặc nhiều scene, chuyển Sol/orchestrator.
5. Sub-agent chỉ author và self-review; **không chạy `npx hyperframes`**. Orchestrator luôn chạy lint, inspect, draft render và frame QA tập trung.
6. Không để orchestrator sửa cùng file scene trong lúc agent đang chạy. Chỉ sửa sau khi agent hoàn tất hoặc sau khi đóng agent đó.

### Luna effect brief mặc định

Khi beat chỉ cần một hiệu ứng minh họa đơn giản: dùng 1 metaphor vật lý, ví dụ đường blueprint được vẽ → 3 module khóa vào vị trí → một flow-trace chạy qua. Nền ivory/graphite sạch, tối đa 1 glow copper tinh tế, không bokeh. Timeline `paused:true`, không exit animation, giữ `y≥1480` trống cho captions.

## Pipeline overview

```
Phase 1a ── TTS (tts.py | tts_minimax.py) ───────────────► audio/full.mp3 + alignment.json
         ── beats-spec.json (avatar:true cho hook/re-hook/CTA) → map_beats.py → beats.json
         ── cut_avatar_audio.py ─────────────────────────► audio/avatar.mp3 + avatar-windows.json
Phase 1b ── budget default 50% hoặc approved bounds → SQLite Pexels ► media-manifest.json + broll-clips/
Phase 2  ── mkt-heygen-mp3-to-mp4 (avatar.mp3, background) ──► avatar_heygen_raw.mp4
         ── split_avatar_video.sh ───────────────────────► avatar-clips/clip-NN.mp4
Phase 3  ── design.md + STORYBOARD.md + seam ledger + styleframes (song song Phase 2)
         ── transcribe audio/full.mp3 + clean + captions
         ── fan out N sub-agents ────────────────────────► scenes/scene-N.html (1080×1920)
         ── wire master: avatar clips + scene mounts + b-roll + SFX + captions
         ── lint + inspect + draft render + frame QA
         ── npx hyperframes render -q standard ──────────► <slug>.mp4 (1080×1920)
```

**Resume mode:** `audio/full.mp3` + `avatar-clips/` đủ clip khớp `avatar-windows.json` → skip Phase 1a+2, vào thẳng Phase 3.

## Step 0 — Scaffold project

```bash
PROJECT_ROOT=$(pwd)
OUT=$PROJECT_ROOT/workspace/content/$(date +%Y-%m-%d)/<slug>
SKILL=<abs path to this skill dir>
mkdir -p $OUT/audio $OUT/scenes $OUT/assets/sfx $OUT/compositions $OUT/avatar-clips $OUT/broll-clips $OUT/media
cp $SKILL/assets/templates/hyperframes.json $OUT/
cp $SKILL/assets/templates/package.json $OUT/          # sửa "name" → slug
cp $SKILL/assets/templates/master-index.reference.html $OUT/index.html   # replace markers [1]..[9]
cp $SKILL/assets/templates/captions.html.template $OUT/compositions/captions.html
cp $SKILL/assets/templates/storyboard.reference.md $OUT/STORYBOARD.md
cp $SKILL/assets/fonts/* $OUT/assets/fonts/
# SFX: copy từ mkt-hyperframe-talking-head-video/assets/sfx/ (6 file chuẩn)
# Media user đưa (nếu có): để nguyên/copy vào $OUT/media/
```

## Step 1-4 — Script, beats, TTS

- Script: hook mạnh → 3-7 beats → CTA. Câu ngắn, KHÔNG em dash. ~60-120s.
  **Đoạn AVATAR (hook / re-hook / CTA) viết kiểu nói thẳng camera; đoạn SCENE viết dẫn chuyện có số liệu/ví dụ** (chất liệu visual cho scene).
- `beats-spec.json`: mỗi beat `{id, slug, pattern, anchor[]}` + **`"avatar": true`** cho hook, re-hook, CTA (thêm `"role": "hook"|"rehook"|"cta"` cho rõ). Video ≤60s: 1 re-hook; >75s: 2 re-hook, đặt tại câu chuyển mạnh nhất vùng 40-60%.
- `script.md` có thể dùng heading để tổ chức beat, nhưng heading chỉ là metadata. Không đặt các nhãn như `Hook`, `Problem`, `Benefits`, `CTA` trên cùng dòng narration để “đánh dấu” beat; đặt chúng sau `##` và để lời nói ở dòng kế tiếp.
- TTS provider (ElevenLabs mặc định | MiniMax qua `TTS_PROVIDER=minimax` hoặc user nói): giống skill gốc —
  `python3 $SKILL/scripts/tts.py --script script.md --out-audio audio/full.mp3 --out-alignment audio/alignment.json`
  (MiniMax: `tts_minimax.py ... --lang vi`, tự Whisper lại để dựng alignment — anchor phải là từ thường).
- TTS preflight bắt buộc, trước `map_beats.py`, `cut_avatar_audio.py` và HeyGen:
  `python3 $SKILL/scripts/validate_tts_alignment.py --script script.md --alignment audio/alignment.json`
  Nếu thấy `FAIL` hoặc alignment có chữ heading, sửa script/TTS rồi chạy lại; không dùng MP3 đó để tiếp tục.
- `python3 $SKILL/scripts/map_beats.py --project $OUT` → beats.json (carry cờ avatar/role).

## Step 4.6 — Visual thinking + storyboard gate

Đọc `references/visual-thinking.md`, `references/editorial-explainer-readability.md`, `references/scene-patterns.md` và `references/design-system.md`, rồi hoàn tất `$OUT/STORYBOARD.md` trước khi chọn Pexels hoặc author scene:

1. Chốt một `message`, `arc`, `visual_thesis`, `persistent_motif` và tối đa hai transition families cho cả video.
2. Với mỗi beat SCENE, viết visual argument đầy đủ: `claim → source_object → transformation → proof`. Copy mọi cue time từ `audio/alignment.json`; không đoán timing.
3. Chọn một motion route chính: `shared-object-morph`, `camera-reveal`, `accumulation`, `causal-chain`, `evidence-physicalization` hoặc `semantic-removal`.
4. Lập seam ledger cho avatar↔scene, scene↔Pexels và scene↔scene. Match exit/entry vector; ghi rõ carrier hoặc lý do clean cut.
5. Điền proof-frame contract: headline, familiar object, visible action, takeaway, proof hold và continuous HF block.
6. Pattern mới phải có 3–5 styleframe cùng một object. Với knowledge/business, tạo `storyboard-preview.html` có một proof frame 9:16/scene và tab chuyển scene; chụp contact sheet rồi trình cùng `design.md`.
7. Chỉ sau approval mới fan-out. Preset đã duyệt được resume/autopilot nhưng không được đổi visual thesis giữa chừng.

## Step 4.5 — Cắt avatar windows

```bash
python3 $SKILL/scripts/cut_avatar_audio.py --project $OUT
# → audio/avatar.mp3 + avatar-windows.json; fail nếu ratio ngoài 0.30-0.42 (kèm gợi ý sửa)
# User yêu cầu ratio khác: --min-ratio 0.45 --max-ratio 0.55
```

## Step 4.7 — Phase 1b: Pexels evidence + visual-mix budget

Đọc `references/media-broll.md`, rồi dùng skill `mkt-resolve-broll-media`:

1. Tính `scene_time = fullTotal − union(avatar windows)` từ `avatar-windows.json`; mặc định đặt `pexels_target_s = scene_time × 0.50`, biên PASS là `scene_time × 0.45..0.55`.
2. Từ `script.md` + `beats.json`, chọn đủ beat SCENE để footage Pexels phủ mục tiêu trên; không chọn beat `avatar:true`. Dùng ít nhất 2 clip khác nhau, ưu tiên clip 2–6s và phân tán qua các beat thay vì một clip dài chiếm toàn bộ.
3. Viết `broll-needs.json` với `intent_vi`, `query_en`, `keywords`, `concepts`, `desired_duration_s`; tổng `desired_duration_s` phải xấp xỉ `pexels_target_s`. Asset user chỉ định vẫn được dùng theo yêu cầu, nhưng chỉ tính vào quota nếu provenance gốc là Pexels.
4. Chạy resolver với `--library "$PROJECT_ROOT/.media-library" --download-missing` và `--max-assets` đủ cho budget (thường 3–6). Resolver ưu tiên asset Pexels đã có trong SQLite, rồi mới tải Pexels portrait mới; output `media-manifest.json`, `broll-clips/`, source/final contact sheets và usage ledger.
5. Read `broll-source-contact-sheet.jpg` rồi `broll-contact-sheet.jpg` đúng 1 vòng QA. Đúng asset nhưng sai đoạn → đặt `source_start_s` và rerun không tải lại. Clip lạc đề/nhãn hiệu nhạy cảm → thêm ID vào `exclude_asset_ids`, làm query cụ thể hơn và rerun 1 lần.
6. Không đặt footage giữa trigger và proof; ưu tiên evidence block riêng trước/sau hero transformation. Nếu mỗi HyperFrames block <3,5s, quay lại approval gate và đề xuất readability override.
7. Ghi `placement.start_s` + `placement.duration_s` cho mọi Pexels clip rồi chạy gate:

```bash
python3 "$SKILL/scripts/validate_visual_mix.py" --project "$OUT"
```

Với override đã duyệt: thêm `--min-pexels <min> --max-pexels <max>`. Gate fail → tăng/giảm thời lượng hoặc đổi footage và chạy lại. Không có đủ Pexels phù hợp sau 1 vòng sửa query → báo BLOCKED; **không được render final bằng 100% HyperFrames**.

## Step 5 — Phase 2: HeyGen (background) + split

Delegate skill `mkt-heygen-mp3-to-mp4` qua sub-agent `run_in_background: true`, **INPUT = `audio/avatar.mp3`**, portrait 720×1280. Orchestrator poll `mcp__codex_apps__heygen_get_video` TRỰC TIẾP (audio ngắn → ~4-6 phút). Download xong:

```bash
bash $SKILL/scripts/split_avatar_video.sh $OUT/avatar_heygen_raw.mp4 $OUT
# tự chạy verify_avatar_sync.py trước → cut-plan.json (offset ĐO ĐƯỢC + confidence)
# → avatar-clips/clip-NN.mp4 (cắt theo offset đo, re-encoded)
```

Đọc bảng lag script in ra: `corr` gần 1.0 = định vị chắc chắn; `lag` là lượng HeyGen đã dịch nội dung (đã được tự bù). Nếu có dòng `low-confidence` → file raw không phải lip-sync của `avatar.mp3` này, hoặc audio bị lỗi — dừng, đừng render.

Trong lúc chờ: placeholder clips per window (xem `references/heygen-integration.md`) để lint/draft sớm.

## Step 6 — Captions

```bash
cd $OUT && npx hyperframes transcribe audio/full.mp3 --model medium --language vi
python3 $SKILL/scripts/clean_transcript.py transcript.json          # → caption-groups.json
python3 $SKILL/scripts/fix_caption_typos.py caption-groups.json script.txt
python3 $SKILL/scripts/inject_captions.py compositions/captions.html caption-groups.json
```

## Step 7 — Master wiring

Từ template `master-index.reference.html`, replace markers [1]..[9]:
- [2]+[8]: TOTAL = **ffprobe audio/full.mp3**
- [4]: avatar clips từ `avatar-windows.json` — `data-start = window.start`, `data-duration = ffprobe clip`, track 10+
- [5]: scene mounts full-canvas track 40+ (đầu segment overlap −0.25s, cuối segment end đúng nextWindow.start); [5b]: Pexels b-roll mounts track 45+ từ media-manifest, visually dominant đúng placement đã qua visual-mix gate
- [6]: `WINDOWS[]`; [7]: `MOUNTS[]` + `BROLLS[]`; [3]: SFX chỉ tại insight/major transition (`references/sfx-layer.md`); không tạo marker/DOM/GSAP cho PIP

Geometry + timing rules: `references/avatar-windows-layout.md` (ĐỌC khi wire).

## Step 8 — Fan out sub-agents (scene HTML 1080×1920)

Spawn N sub-agents trong **1 message**. Mặc định dùng `gpt-5.6-luna` với `thinking=low` cho scene đơn giản; chọn Terra/Sol theo policy ở trên. Prompt template (per scene):

```
Author HyperFrames sub-composition for scene-NN (FULL-CANVAS 1080×1920, LITE pipeline).
# Model routing
- SIMPLE SCENE: use gpt-5.6-luna with low reasoning; COMPLEX SCENE: use gpt-5.6-terra.
- Do not edit files outside OUTPUT. Do not run npx hyperframes or any render command.
# Files
- OUTPUT: <abs>/scenes/scene-NN-slug.html
- REFERENCE (READ FIRST): $SKILL/assets/templates/scene-reference-full.html
- DESIGN: <abs>/design.md
- STORYBOARD (READ SHARED DIRECTION + SEAM LEDGER): <abs>/STORYBOARD.md
- VISUAL THINKING CONTRACT: $SKILL/references/visual-thinking.md
- EDITORIAL READABILITY: $SKILL/references/editorial-explainer-readability.md
- PATTERNS: $SKILL/references/scene-patterns.md
# Context
- Composition id: scene-NN-slug · Duration: <beat duration> s (phủ CẢ beat)
- Avatar KHÔNG trên màn hình — master không dùng PIP.
# Visual argument (copy NGUYÊN scene brief từ STORYBOARD.md)
- claim + persuasion + noun_verb
- source_object: <one persistent object>
- start_state → transformation → end_state/proof
- causal_trigger + motion_route
- focal + supporting[] + scale_plan
- vo_cues[]: <anchor + local_s + visual event>
- transition_in/out: <vector + carrier>; KHÔNG tự đổi seam ledger
- exact_copy[] quoted; tail_behavior: live-resolution | deliberate-stillness
# Hard rules: (copy hard rules từ SKILL.md, nhấn: headline 68-84px, vùng cấm y>=1480,
  không cần chừa góc phải, seed 0x5cNN, AI-HUB Editorial Explainer, không bokeh,
  một hero transformation/beat, một focal ở display scale, tối đa 2 supporting,
  hero visual 55–65%, hero text >=28px, proof hold >=0.90s,
  không `data-layout-allow-overlap`, scene chứng minh claim bằng thay đổi trạng thái,
  KHÔNG chạy npx hyperframes)
# Media (nếu beat có): <abs path ảnh + mô tả + usage pattern>; b-roll che <t1>-<t2>s
  — không đặt moment quan trọng vào khoảng đó. <img> LUÔN có onerror ẩn container.
# Content brief: <beat summary + voiceover đoạn đó + accent colors>
# Process: Read reference → visual-thinking.md → design.md → STORYBOARD scene brief → write →
  self-review bằng 7 câu gate → report <150 words,
  Status: DONE/DONE_WITH_CONCERNS/BLOCKED
```

## Step 9 — Validate (orchestrator, central)

```bash
python3 "$SKILL/scripts/validate_visual_mix.py" --project "$OUT"  # PASS 45–55% Pexels trong scene time
cd $OUT && npm run check                         # pinned: lint + validate + inspect
npx hyperframes render -q draft -o _draft.mp4
for t in <sample times>; do ffmpeg -y -ss $t -i _draft.mp4 -frames:v 1 qa_$t.png; done
```

Frame QA bắt buộc soi:
- `window.start + 1s` mỗi window: avatar hiện, miệng khớp caption
- Giữa mỗi segment: không có PIP; captions hiển thị và Pexels/HyperFrames phủ full-canvas
- ±0.3s quanh mỗi ranh giới: không hở frame đen/đứng hình
- 3s đầu full face; scene không có content vào vùng cấm
- Không chồng chữ/dấu tiếng Việt; không có `data-layout-allow-overlap` trên text
- Palette AI-HUB đạt: ivory/graphite/copper; không neon/cyberpunk/bokeh
- Mỗi hiệu ứng có thể giải thích bằng một câu “giúp hiểu điều gì”
- Tắt text vẫn đọc được quan hệ/hành động chính; frame cuối tự chứng minh claim
- Có source object đổi trạng thái thật; không phải hai object crossfade giả morph
- Focal thắng supporting về scale/contrast/timing; không có 3 card ngang hàng
- Cue hình land đúng spoken anchor; tail còn resolve hoặc cố ý im lặng
- Mỗi seam tuân thủ vector + carrier trong ledger; không có scene tự phát minh transition
- Freeze proof frame: headline + familiar object + visible action + takeaway đọc được ngay
- Hero visual chiếm 55–65%; text trong UI/diagram >=28px trừ micro status
- Soi class/state motion ở frame giữa; không để GSAP className làm mất class geometry

## Step 10-11 — Render (AUTOPILOT)

```bash
# Default balanced:
python3 "$SKILL/scripts/validate_visual_mix.py" --project "$OUT" || exit 1
# Hoặc readability override đã được user duyệt và ghi trong STORYBOARD.md:
python3 "$SKILL/scripts/validate_visual_mix.py" --project "$OUT" --min-pexels <min> --max-pexels <max> || exit 1
cd $OUT && npm run check && rm -f _draft.mp4 qa_*.png && npx hyperframes render -q standard -o <slug>.mp4
ffprobe ...  # verify duration == TOTAL(full.mp3) ±0.1s và 1080×1920
```

Báo user: absolute path MP4 + size + **ratio avatar** (từ avatar-windows.json) + **Pexels/HyperFrames ratio trong scene time** + số Pexels asset đã dùng/bỏ. Log hive_mind sau khi xong.

## Quality Criteria

- 3s đầu full face; avatar quay lại mỗi ≤20s (re-hook đặt đúng)
- Ranh giới avatar↔scene sạch, theo cùng hướng chuyển động hoặc masked reveal; không hở seam
- Không có PIP hoặc thumbnail presenter trong scene segment
- Captions sync word-level, không bị che; headline tiếng Việt không chồng dấu
- Text–speech–image đồng nhất; một beat chỉ có một hero animation
- Mỗi proof frame tự giải thích claim: headline lớn + vật thể quen thuộc + hành động + takeaway
- Hero visual 55–65%, text hero >=28px, proof giữ ≥0,90s và HF block liên tục ≥3,5s khi khả thi
- Mỗi scene có visual argument `start → transformation → proof`; tắt text vẫn hiểu hành động chính
- Shared object/carrier và seam ledger tạo continuity; video không đọc như chuỗi slide độc lập
- Motion do lời nói/hành động kích hoạt; không có camera/VFX trang trí hoặc tail đứng hình ngoài ý đồ
- Đúng AI-HUB Editorial Explainer; blueprint chỉ hỗ trợ cơ chế; không cyberpunk, particle bokeh hay flash lặp lại
- Pexels full-screen đúng chủ đề; default 45–55% hoặc đúng bounds của readability override đã duyệt
- Ít nhất 2 Pexels asset khác nhau; không footage nào đè avatar window
- Render duration == TOTAL; ratio avatar trong khoảng cam kết

## References & Scripts

- `references/avatar-windows-layout.md` — geometry + timing + master JS (ĐỌC khi wire master)
- `references/media-broll.md` — thuật toán media trám + manifest schema (ĐỌC trong Phase 1b)
- `mkt-resolve-broll-media` — skill resolver SQLite/Pexels; tạo `broll-needs.json`, materialize media và ghi usage ledger
- `references/heygen-integration.md` — Phase 2 lite (avatar.mp3 → clips)
- `references/visual-thinking.md` — visual argument, motion routes, seam ledger và 7 câu gate (ĐỌC trước storyboard + author scene)
- `references/editorial-explainer-readability.md` — layout proof-frame, vật thể quen thuộc, HTML approval preview, minimum timing/text và QA class-state (ĐỌC cho knowledge/business hoặc khi user nói khó hiểu/quá ngắn)
- `references/scene-patterns.md` (canvas note lite), `references/sfx-layer.md`, `references/anti-patterns.md`, `references/design-system.md`, `references/elevenlabs-v3.md`, `references/image-thumbnail-overlay.md`
- `scripts/cut_avatar_audio.py`, `scripts/split_avatar_video.sh`, `scripts/verify_avatar_sync.py` (đo lip-sync offset thật), `scripts/prep_broll.sh` — MỚI của lite
- `scripts/tts.py`, `scripts/tts_minimax.py`, `scripts/map_beats.py` (carry avatar/role), `scripts/prep_source_video.sh`, captions scripts — như sibling
- `scripts/validate_tts_alignment.py` — fail-fast kiểm tra heading metadata không lọt vào alignment sau TTS
- `scripts/validate_visual_mix.py` — fail-fast coverage; default 45–55% hoặc bounds của readability override đã duyệt
- `assets/templates/master-index.reference.html` — master lite (markers [1]..[9])
- `assets/templates/scene-reference-full.html` — DNA scene 1080×1920
- `assets/templates/storyboard.reference.md` — visual thesis, scene brief và seam ledger
- `assets/templates/captions.html.template` — captions sub-comp proven

---

**Spec version 1.5 (AI-HUB Editorial Visual Thinking)** — avatar windows 30–40%, không PIP, default-balanced hoặc approved readability mix, proof-frame HTML approval, familiar hero object, visual argument `start → transformation → proof`, shared carrier/seam ledger và VO-cued motion.
