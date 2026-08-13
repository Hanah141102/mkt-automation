# Audio layer: voice, nhạc nền và SFX

Voiceover là spine. BGM tạo nhịp cảm xúc; SFX chỉ nhấn một số peak moment.

## Track map

| Layer | Track | Volume |
|---|---:|---:|
| Voice `audio/full.mp3` | 1 | 1.00 cố định |
| BGM đã chuẩn hóa | 3 | 0.08–0.12, tối đa 0.15 |
| Avatar video | 10+ | muted |
| Scene | 40+ | — |
| Pexels | 45+ | muted |
| Captions | 60 | — |
| SFX | 70+ | 0.20–0.45 |

Không lấy tiếng từ HeyGen clip hoặc B-roll. Chỉ `audio/full.mp3` chứa lời.

## Chọn BGM

Ưu tiên theo thứ tự:

1. Track người dùng cung cấp và xác nhận quyền sử dụng.
2. Track trong thư viện local `workspace/assets/reels/background music/` nếu thư mục tồn tại và provenance đã được ghi.
3. Track royalty-free được user duyệt nguồn/license trước khi tải.

Không dùng các file nhạc nằm trong repo tham khảo hoặc project khác nếu chưa xác định quyền sử dụng. Nếu chưa có track hợp lệ, ghi `BGM_NEEDED` trong approval package. Được render draft nhẹ để review visual bằng validator flag `--draft-allow-missing-bgm`, nhưng phải dừng trước final render và chạy lại validator không có flag này.

Chọn mood theo nội dung: ambient/reflective cho giải thích; restrained tension cho pain point; cinematic wonder cho demo; uplifting cho payoff/CTA. Dùng một track mặc định. Chỉ dùng hai track khi arc có chuyển mood rõ; crossfade audio 1–2 giây, không hard cut.

Chuẩn hóa track đủ TOTAL:

```bash
bash "$THIS_SKILL/scripts/prepare_bgm.sh" \
  "workspace/assets/reels/background music/<licensed-track>.mp3" \
  "$TOTAL" "$OUT/assets/bgm/background.mp3" 1.2 2.0
```

## audio-plan.json

```json
{
  "voice": {"file": "audio/full.mp3", "volume": 1.0},
  "music": [
    {
      "file": "assets/bgm/background.mp3",
      "start_s": 0,
      "duration_s": 75.4,
      "volume": 0.10,
      "fade_in_s": 1.2,
      "fade_out_s": 2.0,
      "mood": "reflective",
      "rights": "user-provided"
    }
  ],
  "sfx": [
    {
      "file": "assets/sfx/camera-flash.mp3",
      "start_s": 0.20,
      "duration_s": 0.8,
      "volume": 0.30,
      "intent": "hook asset reveal"
    },
    {
      "file": "assets/sfx/ting.mp3",
      "start_s": 24.10,
      "duration_s": 0.7,
      "volume": 0.28,
      "intent": "hero stat"
    }
  ]
}
```

`rights` chỉ nhận `user-provided`, `licensed-local` hoặc `royalty-free-approved`. Không bỏ trống trường này.

## SFX decision rules

- `camera-flash`: screenshot hoặc contact-sheet reveal mạnh.
- `ting`: một stat/checkmark quan trọng nhất.
- `whoosh`: tối đa 1–2 major transition.
- `suspense`: câu chuyển sang vấn đề.
- `boom` hoặc `wow`: payoff hoặc CTA, không dùng cả hai nếu cùng chức năng.

Video 60–120 giây dùng 2–5 hit. Cách nhau ít nhất 1,5 giây. Không đặt SFX lên mọi callout; animation nhẹ không cần âm thanh.

## Wire master

```html
<audio id="bgm" class="clip"
  data-start="0" data-duration="75.400" data-track-index="3"
  data-volume="0.10" src="assets/bgm/background.mp3"></audio>
```

Wire mỗi SFX theo `audio-plan.json` ở track 70+. Không sửa voice volume để “nhường” BGM; hạ BGM/SFX.

## QA tai nghe

Nghe ba đoạn: hook, scene dày lời và CTA. Voice phải rõ trên loa điện thoại. Nếu nghe thấy BGM trước khi hiểu lời, hạ BGM. Nếu SFX gây giật hoặc che phụ âm đầu câu, dịch hit 0,15–0,30 giây hoặc hạ volume.
