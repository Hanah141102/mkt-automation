# Anti-Patterns — Lỗi Thường Gặp

Tổng hợp 24 lỗi đã gặp + cách tránh. SKILL.md tóm tắt HARD RULES; file này chi tiết WHY + cách fix.

## Scene HTML structure

1. **(CORRECTED v1.1)** Scene file load qua `data-composition-src` **ĐƯỢC PHÉP full standalone HTML doc** (`<!doctype html>…<html><head><body>`). Runtime extract element `[data-composition-id]` + scoped style/script — proven render clean. (Inline `<template>` chỉ cần khi embed trực tiếp trong index.html; pipeline này KHÔNG dùng.) Quan trọng: root `<div data-composition-id="scene-N" data-width="1200" data-height="1080">`, CSS scoped, KHÔNG gsap riêng.
2. **anime.js** — hyperframes runtime expect GSAP. Bỏ hoàn toàn anime.js.
3. **CSS `animation: ... infinite`** — banned. Convert sang finite GSAP repeat với yoyo, compute từ DURATION.
4. **`Math.random()`** — banned (non-deterministic). Use seeded mulberry32. Mỗi scene 1 seed unique (vd `0x5cNN`).
5. **`gsap.from()` trong sub-comp** — unreliable vì sub-comps load async. Use `gsap.fromTo()` luôn.
6. **Exit animations trong scene** — banned trừ final scene. Master timeline handles transitions.
7. **`<script src=...gsap...>` trong scene HTML** — master index.html load GSAP. Đừng add lại.
8. **Avatar/footer trong scene HTML** — brand stamp chỉ ở master index.html.

## Asset paths

9. **Path `../../../assets/...`** — không work với hyperframes runtime. Copy asset vào `<project>/assets/`.

## Script writing

10. **Em dash trong VO script** — ElevenLabs đọc em dash sai. Dùng comma / period.

## Pattern selection

11. **Forced fit beat content vào pattern không phù hợp** — invent (Approach C) thay vì ép.
12. **Quá 50% scenes có ảnh** — video trông như slideshow. Mix 60/40 motion graphic vs ảnh.

## Design tokens

13. **Không tạo design.md trước** — sub-agents không có source of truth → palette / typography drift.

## Timing

14. **Hardcoded scene durations** — luôn lấy từ `beats.json` (qua `map_beats.py`). Set TOTAL + data-duration = ffprobe source.mp4 ĐÃ re-encode (không phải alignment.json).
15. **(N/A cho skill này)** Overlap +0.4s crossfade = base-skill only. Skill HeyGen: NO overlap, mount back-to-back, `fromTo opacity 0→1` ở start, scene sau (DOM sau) che scene trước. Overlap + slide-mount width tween = flicker.

## Rendering

16. **Render qua Playwright per-scene + ffmpeg concat** — KHÔNG. Đó là approach v1 cũ đã bỏ. HyperFrames render trên `index.html` xử lý đầy đủ.

## SFX

17. **Quá nhiều SFX** — cap 1 SFX / 30s. Background music không thuộc skill này.
18. **SFX volume = 1.0** — sẽ át voiceover. Stick 0.4-0.5.

## Title card

19. **Title-card slider có wipe bars / flash** — slider 0-5s đã nhỏ, thêm wipe/flash sẽ che ảnh. Chỉ crossfade sạch + ken-burns scale 1.0→1.05. Đặt wipe/flash CHO SCENE BOUNDARIES không phải slider.

## Brand stamp

20. **Brand stamp avatar 56px** — quá nhỏ, viewer không nhìn ra. Default 112px, handle text 30px mono.

## Transitions

21. **Mọi scene boundary đều flash** — flash là cho "loud" moments (premise hit, big stat, finale). Mặc định 5-6/15 boundaries.
22. **Wipe color không xoay vòng** — 15 wipes cùng coral = monotone. Rotate coral/cyan/cream, alternate LTR/RTL.
23. **`gsap.fromTo()` với scene-mount mà không có `overwrite: 'auto'`** — sẽ conflict với scene's own internal animations. Master timeline tween luôn dùng `overwrite: 'auto'`.

## Layout validation

24. **Slider/showcase không có `data-layout-ignore`** — inspect sẽ flag `clipped_text` vì sum của 4 slide labels > showcase width. Mark showcase + slides với `data-layout-ignore` + `data-layout-allow-overflow`.

## HeyGen + master (v1.1 — từ run thật)

25. **Không re-encode HeyGen MP4** — HeyGen = 25fps, keyframe ~8s → renderer warn "sparse keyframes → seek failures / frame freezing", avatar đơ frame. Fix: `prep_source_video.sh reencode raw.mp4 source.mp4` (libx264 -r 30 -g 30 -keyint_min 30). LUÔN làm.
26. **Tin sub-agent báo HeyGen "stuck N phút"** — nó bịa elapsed time. HeyGen KHÔNG stuck nếu `failure_code`=null; render 110s/720p ~10-15 phút. Poll `mcp__heygen__get_video` trực tiếp từ orchestrator.
27. **Block chờ HeyGen** — tạo placeholder (`prep_source_video.sh placeholder`) để lint/inspect/draft-render full composition song song, swap avatar thật sau.
28. **Scene meta-badge đè master brand-mark** — cả 2 ở top-left. Scene meta-badge xuống top:92px left:56px; KHÔNG wordmark top-right (avatar ngồi đó).
29. **Lo lắng PIP stretch** — KHÔNG stretch nếu scene content flex-center intrinsic-width: khi slide-mount tween 1200→1920 content chỉ re-center. Đừng dùng block width:100% bên trong scene.
30. **`#avatar-frame > .avatar-breathing/.avatar-punch` thiếu `data-layout-allow-overflow`** — breathing scale 1.025 vượt clip → inspect flag `container_overflow` (vô hại nhưng noise). Thêm attr.
31. **Master select root bằng `[data-composition-id="main"]`** → lint `composition_self_attribute_selector`. Dùng `#root`.
32. **Wipe/flash thiếu hard-kill** → lint `gsap_exit_missing_hard_kill`. Thêm `tl.set('#scene-flash'/'#scene-wipe',{opacity:0}, t)` sau fade.
33. **Mong `npx hyperframes lint` validate scene** — lint CHỈ check index.html, KHÔNG recurse scene mounted, KHÔNG nhận file path ("Not a directory"). Validate scene qua `inspect` + draft-render frame check.
34. **Sub-agent chạy `npx hyperframes`** — concurrent + asset chưa có = false error. Sub-agent author + self-review only; orchestrator validate tập trung.
35. **`gsap.to('#avatar-frame', { top/left: ... })` hoặc `{ bottom: ... }` trên captions** — lint `gsap_non_transform_motion` (device-pixel layout tweens). Hyperframes v0.6.52+ lint reject mọi GSAP prop KHÔNG phải `transform/opacity` trên element có `position: absolute`. Bao gồm: `top`, `left`, `bottom`, `right`, `width`, `height`. SPLIT↔PIP cũ tween `width` của `.slide-mount` (1200→1920) — cũng reject. Fix: wrap avatar frame + slide-mount trong wrapper với `position: absolute; inset: 0; transform: translate(...)`, tween `xPercent` / `scaleX` (transform OK). Captions: dùng `transform: translateY(px)` thay `bottom:`. Master template hiện vẫn dùng `top/bottom` — refactor trước khi render. Đừng patch lint warning, sửa CSS + GSAP.
36. **Burn iterations chờ sub-agent render** — fan out N sub-agents ở Step 8 rồi poll từng cái bằng `process(action='poll')` lặp lần lượt = hết iteration budget. Pattern đúng: spawn tất cả N sub-agents trong **1 message** (parallel), rồi `process(action='wait', timeout=600)` block trên handle cuối cùng. KHÔNG poll từng cái.

37. **Orchestrator viết cùng file scene với sub-agent song song** — nếu orchestrator cũng tự author/sửa 1 scene HTML trong khi fan-out N sub-agents đang chạy, sub-agent có thể overwrite file mid-edit → mất công sửa lại từ đầu. Quy tắc: hoặc (a) orchestrator **KHÔNG tự sửa scene HTML** khi đã fan-out — để sub-agent own file 100%, orchestrator chỉ validate ở Step 9; hoặc (b) split file ownership theo tên (vd orchestrator author `scene-00-hook.html` chỉ định, các scene khác để sub-agent), ghi rõ từng scene cho từng sub-agent, không overlap path. Tương tự cho `index.html` master — orchestrator own một mình, KHÔNG nhờ sub-agent touch.

38. **`onUpdate` / `onComplete` callbacks KHÔNG reliably fire khi master seek timeline** — GSAP paused timeline + seek() (xảy ra khi `npx hyperframes inspect` hoặc draft-render scrub frame) skip callback chain. Count-up numbers, typewriter DOM updates, anything dùng `onUpdate: function(){ el.textContent = ... }` sẽ GIỮ giá trị initial (vd "0") khi seek tới vị trí đó. Fix bắt buộc cho mọi effect DOM-driven: dùng `tl.call(() => { gsap.set(target, { attr: finalValue }); }, null, D - 0.01)` để **hard-set giá trị cuối 10ms trước khi scene kết thúc** + `gsap.set(target, finalValue)` ngay từ đầu để initial state correct. Hoặc explicit `tl.call` tại nhiều checkpoint (25%, 50%, 75%, 100% D) set DOM thẳng. Anti-pattern này đã hit nhiều lần — fix cuối cùng thấy work là per-checkpoint `tl.call` + `gsap.set`, KHÔNG tin tưởng `onUpdate`.

39. **Final composition KHÔNG hold ≥500ms trước scene kế tiếp** — `scene-patterns.md` đã nói "hold final ≥500ms" nhưng quên enforce ở timeline math. Khi duration D gần bằng `end - start` (mount window), entrance cuối (vd subtitle, closing tagline) phải xon trước `D - 0.5` để viewer nhìn thấy settled state ≥500ms. Pattern: `const ENTRANCE_END = D - 0.5;` rồi schedule mọi entrance sao cho entry cuối `≤ ENTRANCE_END`. Nếu pattern có minimum duration dài hơn (terminal-typewriter cần ≥9s cho command gõ xong), phải **tăng scene D** thay vì cắt settle time.

40. **Drift giữa `DURATION` trong scene HTML và `data-duration` của `.slide-mount` trong `index.html`** — `index.html` khai báo `<div class="clip slide-mount" data-duration="5.292">` cho scene-04, nhưng scene-04 HTML nội bộ đặt `const DURATION = 6.792` cho timeline GSAP. Hai con số lệch 1.5s → render vẫn chạy nhưng (a) master timeline mount/unmount scene lệch nhịp với internal timeline, (b) khi scene kế tiếp bắt đầu, scene cũ GSAP vẫn đang chạy → có thể xuất hiện "scene overlap glitch" hoặc entrance cuối scene-04 bị scene-05 che mất. Fix: scene HTML viết `const DURATION = N.NNN;` đúng bằng `data-duration` của `.slide-mount` trong `index.html`. Cách tốt nhất: orchestrator viết `index.html` (own file 100%), sau đó dùng 1 sed/awk pass copy từng `data-duration` xuống scene HTML tương ứng (`sed -i "s/const DURATION = .*/const DURATION = <N.NNN>;/" scenes/scene-N-*.html`) trước khi render. Hoặc: scene HTML tự compute `DURATION = <attr from data-composition-id's parent data-duration>` — phức tạp hơn, chỉ làm khi authoring programmatic.

41. **Render output verification pattern** — sau `npx hyperframes render -q standard -o final.mp4`, LUÔN verify bằng 3 check trước khi báo "done":
    ```bash
    # 1. duration phải ≈ source.mp4 (audio sync check)
    ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 final.mp4
    # expect: 48.333 (match source.mp4 ±0.05s)
    # 2. frames × fps = duration (sanity check no dropped frames)
    ffprobe -v error -select_streams v:0 -count_packets -show_entries stream=nb_read_packets -of csv=p=0 final.mp4
    # expect: 1450 packets × 30fps = 48.333s
    # 3. bitrate + size reasonable
    ls -lh final.mp4  # 30-50MB cho 48s 1080p standard
    ```
    Nếu duration lệch >0.5s so với source.mp4 → render bị trim/cut ở đâu đó (thường do scene timeline chạy quá DURATION, hoặc data-duration của `<video>`/`<audio>` ngắn hơn thực tế). KHÔNG báo done nếu 3 check fail.

42. **Sub-agent race khi render đồng thời** — khi fan-out N scene sub-agents ở Step 8, KHÔNG đợi tất cả xong mới render. Pattern đúng: (a) sau khi spawn N sub-agents ở 1 message, (b) `process(action='wait', timeout=600)` block trên handle cuối cùng, (c) check mtime của từng scene file (`stat -f "%Sm %N" scenes/scene-*.html`) — nếu có scene vẫn older > spawn-time → scene đó bị sub-agent bỏ/stuck, KHÔNG render (gate). Nếu tất cả mtime > spawn-time → render OK. Trong run thật, dispatch 1 scene redo sub-agent giữa chừng, scene đó vẫn ở mtime cũ khi render bắt đầu → render dùng bản valid trước đó, kết quả vẫn đúng. Sub-agent redo chạy xong có thể ghi đè nhưng render đã xong. Kết luận: render KHÔNG nên gate 100% vào sub-agent completion nếu file hiện tại đã pass lint + inspect.

43. **`npx hyperframes lint` warnings KHÔNG block render** — output `0 errors, 8 warnings` (vd `google_fonts_import`, `text_fit_margin`) là chấp nhận được. Render env có mạng → Google Fonts load OK, fonts render đúng. Chỉ FAIL khi `errors > 0`. Warnings mở rộng thêm `google_fonts_import` (lesson #12 đã ghi) — generalize thành "mọi warning ngoại trừ `gsap_exit_missing_hard_kill` + `composition_self_attribute_selector` + `gsap_non_transform_motion` (3 loại này fix) là OK". Nếu muốn fail trên warnings → dùng `--strict-all` (per `hyperframes-cli`).
