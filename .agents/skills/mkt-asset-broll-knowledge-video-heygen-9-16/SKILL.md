---
name: mkt-asset-broll-knowledge-video-heygen-9-16
description: Dựng video kiến thức, kinh doanh hoặc tin tức dọc 9:16 từ voiceover, avatar HeyGen theo window, ảnh/screenshot do người dùng cung cấp, Pexels B-roll full-screen độc lập, text/chart reveal đúng keyword, emphasis an toàn trên avatar, captions, nhạc nền và SFX. Dùng khi cần phối nhiều loại media trực quan thay vì để HyperFrames tự vẽ toàn bộ scene, đồng thời cần storyboard, vision safe-zone review và draft nhẹ trước bản final.
---

# Asset-led B-roll Knowledge Video — HeyGen 9:16

Tạo video 1080×1920 trong đó asset thật hoặc footage sát nghĩa mang bằng chứng; text/chart giải thích phần không có hình minh họa phù hợp. Dùng HyperFrames để dàn trang, reveal và render, không dùng để phủ đồ họa lên Pexels hay thay bằng một rừng card trang trí.

## Phụ thuộc bắt buộc

Đặt repo root làm `PROJECT_ROOT`, rồi dùng:

```bash
BASE_SKILL="$PROJECT_ROOT/.agents/skills/mkt-hyperframe-knowledge-video-heygen-9-16-lite"
BROLL_SKILL="$PROJECT_ROOT/.agents/skills/mkt-resolve-broll-media"
HEYGEN_SKILL="$PROJECT_ROOT/.agents/skills/mkt-heygen-mp3-to-mp4"
THIS_SKILL="$PROJECT_ROOT/.agents/skills/mkt-asset-broll-knowledge-video-heygen-9-16"
```

Đọc toàn bộ `BASE_SKILL/SKILL.md` trước khi chạy pipeline. Giữ các quy tắc TTS, alignment, avatar window, HeyGen sync, captions, scene HTML, render và cold-seek của BASE, trừ visual mix và audio layer được skill này ghi đè.

Đọc theo phase:

- Trước asset map và storyboard: [references/visual-plan-contract.md](references/visual-plan-contract.md) và [references/asset-motion-patterns.md](references/asset-motion-patterns.md).
- Trước khi duyệt timing, overlay hoặc render draft: [references/semantic-shot-cue-qa.md](references/semantic-shot-cue-qa.md).
- Khi scaffold, wire master hoặc render: [references/runtime-integration.md](references/runtime-integration.md).
- Khi chọn nhạc, SFX và mix audio: [references/audio-layer.md](references/audio-layer.md).

## Contract đầu vào và đầu ra

Yêu cầu:

- `script.md` hoặc brief đủ để viết script.
- Ảnh, screenshot hoặc video người dùng cung cấp trong `media/` nếu có.
- TTS + word-level `audio/alignment.json`.
- Avatar/look đã xác định cho HeyGen.
- Chỉ gọi Pexels khi local library không có asset phù hợp và có `PEXELS_API_KEY` cấu hình sẵn.

Tạo:

- `asset-inventory.json` + contact sheet media người dùng.
- `visual-plan.json`: nguồn sự thật về mode, placement, semantic boundary và coverage.
- Cue ledger cho mọi text/chart có nhiều ý; mỗi cue có anchor, absolute time và scene-relative time.
- `broll-needs.json` + `media-manifest.json` từ resolver Pexels.
- `audio-plan.json`: voice, BGM và SFX.
- `design.md`, `STORYBOARD.md`, `storyboard-preview.html` và contact sheet duyệt theo từng trạng thái.
- Nếu có emphasis trên HeyGen: `heygen-emphasis-review/emphasis-plan.json`, approval board và `VISION-AUDIT.md`.
- `avatar-windows.json`, `avatar-clips/`, `scenes/`, captions, draft nhẹ và MP4 final 1080×1920.

## Hard rules

1. Giữ HeyGen theo window: hook 3 giây đầu, re-hook và CTA; mặc định 30–42% tổng thời lượng. Chỉ gửi `audio/avatar.mp3` cho HeyGen.
2. Ưu tiên nguồn hình: user chỉ định → user media tự khớp → local Pexels → Pexels mới → text/chart HyperFrames.
3. Dùng `visual-plan.json` làm nguồn duy nhất cho scene mode và dominant placement. Không author motion trước approval gate.
4. Chọn theo semantic match, không theo quota. Target mix chỉ là mặc định; nếu hình không khớp đúng danh từ + động từ, dùng bounds override có lý do và trình user duyệt.
5. Pexels là shot full-screen độc lập. Ngoài captions, không đặt badge, callout, chart, infographic, tint note hoặc ảnh nhỏ lên footage.
6. Không cho Pexels và text/chart cùng hiển thị. Cắt footage tại semantic boundary rồi bắt đầu chart ở đúng mốc đó, không để hở coverage hoặc để chart chạy ẩn bên dưới.
7. Khi không có hình minh họa sát nghĩa, dùng text, chart, flow hoặc biểu đồ riêng; không chèn filler footage chỉ “cùng ngành”.
8. Mọi node/card/row của text/chart phải ẩn ban đầu và chỉ reveal khi đúng keyword được nói theo `audio/alignment.json`. Cấm stagger nhanh làm cả sơ đồ hiện sớm.
9. Mỗi beat chỉ có một hero, một visible action và tối đa ba callout. Asset thật phải thắng text/graphics về scale và contrast.
10. Emphasis trên HeyGen là tùy chọn, tối đa một cue thấy được tại một thời điểm. Mặc định chỉ dùng text badge + CSS/vector micro-icon; không dùng PIP hoặc ảnh minh họa chung chung.
11. Trước khi wire emphasis, trích frame thật tại cue time và vision-audit mặt, mắt, tóc, tay, caption, brand và head drift. Không suy safe zone từ layout tĩnh.
12. BGM final bắt buộc, có quyền sử dụng đã xác nhận, volume 0.08–0.12, hard cap 0.15, fade-in/out. Draft review được thiếu BGM nhưng phải ghi rõ `DRAFT · BGM_NEEDED`; không được giao như final.
13. Dùng 2–5 SFX cho video 60–120 giây, cách nhau ít nhất 1,5 giây; không đặt whoosh ở mọi scene. Không lấy audio từ B-roll.
14. Captions lấy từ `audio/full.mp3`, mount cuối, không hand-edit timing. Voiceover volume luôn 1.0.
15. Chỉ dùng hai họ transition: clean/opaque reset và directional mask/match-action. Flash tối đa một loud moment.

## Visual router

Chọn mode cho từng beat:

| Mode | Điều kiện | Vai trò HyperFrames |
|---|---|---|
| `user-asset` | Ảnh/screenshot chứng minh claim | crop, callout, compare, stack |
| `pexels` | Footage khớp đúng hành động/bối cảnh | mount full-screen sạch; không annotation |
| `hybrid` | Asset và footage hỗ trợ hai vế liên tiếp | nối bằng semantic boundary; không overlap |
| `hyperframes` | Không có asset hợp lệ | text/chart/flow riêng, reveal theo keyword |
| `avatar` | Hook, re-hook, CTA | full-screen; emphasis nhỏ chỉ sau vision audit |

Nếu user chỉ định asset cho beat, không đổi mode hoặc gán sang beat khác khi chưa báo.

## Pipeline

### 1. Scaffold và audio spine

Scaffold từ BASE theo [references/runtime-integration.md](references/runtime-integration.md). Viết script, TTS, validate alignment, map beats và cắt avatar window bằng script BASE.

### 2. Inventory media người dùng

Probe từng file. Với video, trích frame 10/50/90%; với ảnh, đọc nội dung, chữ, kích thước và safe crop. Tạo contact sheet và `asset-inventory.json`. Không công khai dữ liệu riêng tư ngoài mục đích dựng video.

### 3. Lập visual plan theo nghĩa

Với từng SCENE beat:

1. Chốt `claim`, `noun_verb`, spoken cue và visual job.
2. Chấm asset theo semantic match, proof value, crop fit, readability và motion potential.
3. Chọn mode/pattern; ghi semantic start/end và dominant placement không overlap.
4. Nếu chọn text/chart, lập cue ledger theo word alignment trước khi thiết kế layout.
5. Đánh dấu `ASSET_NEEDED` nếu user cần cung cấp bằng chứng; nếu không cần bằng chứng ảnh, dùng chart riêng.

### 4. Resolve Pexels evidence

Viết `broll-needs.json` chỉ cho beat cần hành động thật. Dùng `mkt-resolve-broll-media`, local-first, tối đa một Pexels clip/beat. Chỉ nhận clip khi noun + verb khớp claim. Ghi placement cuối vào `media-manifest.json` và `visual-plan.json` với `overlay: "none"`.

### 5. Approval gate

Trình user trước khi author motion:

- Contact sheet media dùng/bỏ và lý do.
- `STORYBOARD.md` có asset map, visual argument, semantic boundary và seam ledger.
- `storyboard-preview.html` dùng proof frame thật.
- Với text/chart: board trạng thái source → từng keyword reveal → proof; không chỉ gửi final frame đã đầy chữ.
- Với HeyGen emphasis: frame avatar thật tại từng cue, badge đề xuất và vision safe-zone audit.
- Tỷ lệ dự kiến user asset/Pexels/HyperFrames, nhạc nền và SFX dự kiến.

Chỉ tiếp tục sau khi user duyệt. Direction đã duyệt cho cùng series được resume, nhưng không tự đổi visual thesis hoặc safe-zone decision.

### 6. HeyGen, emphasis và captions

Tạo `audio/avatar.mp3`, gọi HeyGen một lần, đo sync offset/drift rồi split clip bằng BASE. Nếu cần emphasis, tạo approval board và `emphasis-plan.json`, vision-audit rồi mới wire cue theo absolute alignment. Transcribe `audio/full.mp3` với `--language vi`, clean và inject captions.

### 7. Author theo cue ledger

Mỗi scene là standalone HTML 1080×1920. Dùng project-relative path; mọi `<img>` có `onerror` ẩn container. Set tất cả item tuần tự về hidden trước timeline, rồi dùng `gsap.fromTo()` tại cue-relative time; hard-hide cue ngắn ở end, không exit animation. Không dùng generic stagger thay word cues.

### 8. BGM và SFX

Chọn một BGM theo arc; chỉ dùng hai track khi có mood shift rõ. Chuẩn hóa BGM đủ TOTAL bằng `scripts/prepare_bgm.sh`, ghi `audio-plan.json`, rồi wire voice track 1, BGM track 3, SFX track 70+.

### 9. Validate và render draft nhẹ

```bash
python3 "$THIS_SKILL/scripts/validate_asset_broll_plan.py" --project "$OUT" <approved-bound-overrides>
cd "$OUT" && npm run check
npx hyperframes render -q draft -o _draft-<variant>.mp4
```

Nếu chỉ cần draft review và BGM chưa có quyền sử dụng, thêm `--draft-allow-missing-bgm` vào lệnh validator rồi ghi `BGM_NEEDED`; không bỏ các lỗi visual/timing khác. Trích frame ngay trước/sau từng cue, tạo QA contact sheet và vision-check Pexels sạch, cue đúng lời, không che mặt/mắt/tay/caption và không có gap tại semantic boundary. Dùng tên output mới, không overwrite draft cũ.

### 10. Render final

Chỉ render `-q standard` khi validator, `npm run check`, frame QA, vision QA, sync và audio rights đều PASS. `ffprobe` phải cho 1080×1920 và duration bằng `audio/full.mp3` ±0,1 giây.

## Báo cáo hoàn tất

Báo absolute path MP4, draft hay final, kích thước, duration, ratio avatar/user asset/Pexels/HyperFrames, asset dùng/bỏ/tải mới, BGM rights, số SFX và kết quả cue/vision QA.
