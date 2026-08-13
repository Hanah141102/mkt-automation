# ElevenLabs model duration — v3 vs v2 differences

Quantitative data + workflow recipe khi switch model giữa các phiên và cần
re-time toàn bộ video timeline để khớp audio mới.

## Dữ liệu tham khảo với một voice tiếng Việt

| Model | Cùng script ~170 từ VN | Audio duration | Tốc độ đọc |
|---|---|---|---|
| `eleven_multilingual_v2` (default) | ~170 từ | **~6.73s** | ~2.5 từ/s — nhanh, gọn |
| `eleven_v3` | ~170 từ | **~10.88s** | ~1.6 từ/s — chậm hơn ~60%, nhiều pause tự nhiên |

**Key insight:** v3 không phải chỉ "thêm SSML pause" — nó đọc chậm hơn across
the board với nhiều breath pause tự nhiên. Khoảng cách tỉ lệ gần như constant
~60% trong mọi test, không phụ thuộc độ dài script (cần verify thêm với script
>500 từ, nhưng pattern đã rõ).

## Tại sao đây là pitfall (không phải edge case)

- API contract không đổi — MP3 vẫn được ghi đúng bytes, ffprobe vẫn đọc được
  duration chính xác. Vấn đề là downstream pipeline assume audio duration
  trùng với `DURATION` mặc định trong `index.html`.
- Nếu không re-time: video dài 11s nhưng audio kéo 11s → audio bị cắt nửa chừng
  hoặc video đen 0.5s ở cuối. Subtitle timing trong `alignment.json` cũng lệch.
- Scene timelines có `position: "+=N"` references to old ending → render ra
  effects rỗng vì timeline đã kết thúc trước khi keyframe chạy.

## Workflow khi switch model (recipe thực tế)

### 1. Re-run TTS với model mới

```bash
ELEVENLABS_MODEL_ID=eleven_v3 python3 <skill_dir>/scripts/elevenlabs_tts.py \
  --text-file script.txt --out audio/full.mp3
```

### 2. Đo duration mới

```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio/full.mp3
```

### 3. Update master `index.html` DURATION

3 chỗ cần sửa (regex-friendly):

```bash
# data-duration của audio clip
sed -i '' 's/data-duration="[0-9.]\+"/data-duration="11.0"/' index.html

# JS const DURATION
sed -i '' 's/const DURATION = [0-9.]\+/const DURATION = 11.0/' index.html

# audio/alignment.json — duration_ms field
python3 -c "
import json
p='audio/alignment.json'
d=json.load(open(p))
d['duration_ms']=10880  # 10.88s * 1000
json.dump(d, open(p,'w'), indent=2)
"
```

### 4. Re-time keyframes ending trong scene timelines

Vấn đề: mỗi scene timeline có các keyframe ở cuối dùng `position: "+=N"` relative
to old DURATION. Khi DURATION đổi, "ending" dịch chuyển → các keyframe cần dời
về cuối mới.

Pattern: scan tất cả `position: "+=..."` trong scene HTML, tính lại offset dựa
trên difference (new_DURATION - old_DURATION).

```bash
# Ví dụ: old_DURATION=7.0, new_DURATION=11.0, delta=4.0
# Tất cả position: "+=6.5" → "+=10.5" (giữ relative offset within scene)
# NHƯNG các keyframe ở scene boundary (where timeline ends) cần absolute new end

# Practical recipe: dùng awk thay vì sed vì quote hell
awk -v old_end=7.0 -v new_end=11.0 '
  /position: "+=/ {
    # Nếu absolute position > old_end (i.e. near end), shift by delta
    match($0, /"\+=[0-9.]+"/)
    if (RSTART) {
      val = substr($0, RSTART+4, RLENGTH-5) + 0
      if (val >= old_end - 0.5) {
        # near-end keyframe: shift by delta
        new_val = val + (new_end - old_end)
        gsub(/"\+=[0-9.]+"/, "\"+=" new_val "\"")
      }
    }
  }
  { print }
' scenes/scene-01-*.html > scenes/scene-01-*.html.tmp && mv scenes/scene-01-*.html.tmp scenes/scene-01-*.html
```

### 5. Re-render + verify

```bash
npx hyperframes render -q standard -o final.mp4
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 final.mp4
# Phải khớp audio duration ±0.2s
```

## Anti-patterns

- **Hardcode `DURATION = 11.0` without measuring**: nếu script dài hơn,
  audio có thể 12.5s. Luôn `ffprobe` trước khi set.
- **Quên update `alignment.json`**: subtitles sẽ drift khỏi audio mới.
- **Chỉ update master, quên scene timelines**: effects gần cuối sẽ không chạy
  (timeline đã paused).
- **Dùng `eleven_v3` mặc định cho podcasts/keynote**: v3 chậm hơn 60% → video
  ngắn content dài sẽ thành video dài nhàm. Default vẫn nên là v2 trừ khi user
  muốn giọng đọc chậm/pause tự nhiên.

## Khi nào nào dùng v3

- Video có narrative pacing chậm (meditation, deep-dive)
- Khi user explicitly nói "đọc chậm lại" / "có pause tự nhiên"
- Audiobook/long-form explainer (>3 phút)
- Khi content nặng về emotion (testimonial, storytelling)

## Khi nào KHÔNG dùng v3

- Video TikTok/Reels ngắn (60-90s) — v3 sẽ kéo dài thành 100-150s
- Content tactical/listicle (tips, how-to) — cần tempo nhanh
- Khi đã render xong scene timelines với DURATION cũ (không muốn re-time)
