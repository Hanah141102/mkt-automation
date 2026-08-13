# Tích hợp runtime với skill Lite

Skill này tái sử dụng pipeline kỹ thuật đã kiểm chứng của `mkt-hyperframe-knowledge-video-heygen-9-16-lite`; không sao chép TTS, HeyGen sync hoặc renderer.

## Scaffold

```bash
PROJECT_ROOT=$(pwd)
BASE_SKILL="$PROJECT_ROOT/.agents/skills/mkt-hyperframe-knowledge-video-heygen-9-16-lite"
THIS_SKILL="$PROJECT_ROOT/.agents/skills/mkt-asset-broll-knowledge-video-heygen-9-16"
OUT="$PROJECT_ROOT/workspace/content/$(date +%Y-%m-%d)/<slug>"

mkdir -p "$OUT"/{audio,scenes,compositions,avatar-clips,broll-clips,media,assets/bgm,assets/sfx,assets/fonts}
cp "$BASE_SKILL/assets/templates/hyperframes.json" "$OUT/"
cp "$BASE_SKILL/assets/templates/package.json" "$OUT/"
cp "$BASE_SKILL/assets/templates/master-index.reference.html" "$OUT/index.html"
cp "$BASE_SKILL/assets/templates/captions.html.template" "$OUT/compositions/captions.html"
cp "$BASE_SKILL/assets/templates/storyboard.reference.md" "$OUT/STORYBOARD.md"
cp "$BASE_SKILL/assets/fonts/"* "$OUT/assets/fonts/"
```

Sửa `package.json` name thành slug. Copy media người dùng vào `media/` mà không đổi file gốc.

## Tái sử dụng script BASE

Dùng trực tiếp:

- `tts.py` hoặc `tts_minimax.py`.
- `validate_tts_alignment.py`.
- `map_beats.py`.
- `cut_avatar_audio.py`.
- `split_avatar_video.sh` + `verify_avatar_sync.py`.
- `prep_broll.sh`.
- captions scripts.

Không dùng `validate_visual_mix.py` của BASE vì nó bắt Pexels 45–55%. Dùng `validate_asset_broll_plan.py` của skill này.

## Pexels resolver

```bash
python3 "$BROLL_SKILL/scripts/resolve_broll.py" \
  --project "$OUT" \
  --needs "$OUT/broll-needs.json" \
  --library "$PROJECT_ROOT/.media-library" \
  --download-missing \
  --max-assets 4
```

Giữ provenance, contact sheet và SQLite usage ledger. Pexels clip phải muted, H.264, 30fps và chỉ mount trong SCENE time.

## Master wiring bổ sung

Từ template BASE:

1. Giữ voice track 1.
2. Thêm BGM track 3 sau voice, trước avatar.
3. Giữ avatar track 10+.
4. Mount user-asset scene track 40+.
5. Mount Pexels track 45+ từ `media-manifest.json`.
6. Giữ captions track 60 và SFX track 70+.
7. Nếu có HeyGen emphasis, mount cue visual với `z-index` dưới captions; captions vẫn mount cuối và `z-index: 100`.
8. Tạo `MOUNTS[]`, `BROLLS[]` và `EMPHASIS[]` từ plan đã duyệt, không tự đoán lại placement.

User image nằm trong scene HTML; Pexels fullscreen nằm ở master. Nếu dùng user video fullscreen, mount master như B-roll nhưng giữ `kind: "user-asset"` trong visual plan.

Pexels không có overlay riêng. Chỉ cho fade/cut ngắn và scale rất nhẹ nếu không làm sai nghĩa. Khi Pexels kết thúc, scene text/chart kế tiếp phải bắt đầu đúng semantic boundary; không để scene chạy ẩn dưới footage.

## Cue wiring

Chuyển absolute cue sang scene-relative cue trước khi author scene. Set item về hidden rồi reveal từng target, không stagger theo index.

```js
const cues = { plan: 2.17, execute: 3.45, check: 4.56 };
tl.set(['#plan', '#execute', '#check'], { opacity: 0 }, 0);
Object.entries(cues).forEach(([id, at]) => {
  tl.fromTo(`#${id}`, { opacity: 0, y: 18 },
    { opacity: 1, y: 0, duration: .24, ease: 'power3.out' }, at);
});
```

Với emphasis trên HeyGen, dùng absolute time và hard-hide tại `end`; giữ tối đa một cue visible:

```js
EMPHASIS.forEach((cue) => {
  tl.fromTo(cue.id, { opacity: 0, x: -18, scale: .96 },
    { opacity: 1, x: 0, scale: 1, duration: .16, ease: 'power3.out' }, cue.start);
  tl.set(cue.id, { opacity: 0 }, cue.end);
});
```

## Approval artifacts

`storyboard-preview.html` phải dùng đúng project-relative asset path và asset thật. Với text/chart, hiển thị các trạng thái reveal tuần tự. Với HeyGen emphasis, dùng frame trích từ clip thật tại cue time và kèm vision audit; không duyệt bằng avatar placeholder.

## Final commands

```bash
python3 "$THIS_SKILL/scripts/validate_asset_broll_plan.py" --project "$OUT"
cd "$OUT"
npm run check
npx hyperframes render -q draft -o _draft-<variant>.mp4
# QA frame/audio xong mới:
npx hyperframes render -q standard -o <slug>.mp4
```

Nếu BGM còn `BGM_NEEDED`, chỉ ở vòng draft được thêm `--draft-allow-missing-bgm` vào validator; final phải chạy lại không có cờ này. Trích frame trước/sau từng cue từ draft và vision-check. `ffprobe` final phải là 1080×1920, duration bằng `audio/full.mp3` ±0,1 giây. BGM không được kéo dài duration composition.
