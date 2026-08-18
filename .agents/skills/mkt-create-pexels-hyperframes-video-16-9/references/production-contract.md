# Production contract

## Cấu trúc dự án

```text
workspace/content/YYYY-MM-DD/<slug>/
├── script/
│   ├── script-source.md
│   └── script-tts.md
├── audio/
│   ├── voiceover.mp3
│   ├── sfx-plan.json
│   └── qa/word-timestamps.json
├── planning/
│   ├── beats.json
│   └── media-plan.json
├── storyboard/
│   └── storyboard.html
├── media/
│   ├── pexels/
│   ├── logos/
│   ├── trims/
│   └── media-manifest.json
├── render-draft/
│   ├── index.html
│   ├── <slug>-draft-vN.mp4
│   └── <slug>-draft-vN-contact-sheet.jpg
└── design.md
```

Không commit media sinh ra, `workspace/`, API key hoặc credentials.

## Cổng duyệt

### TTS_REVIEW

Giao `script-tts.md` và `voiceover.mp3`. Ghi rõ model/voice đã dùng, duration và mọi cách đọc tên riêng đã chuẩn hóa.

### STORYBOARD_REVIEW

Giao HTML có audio và timeline. Mỗi card phải cho thấy voice, hình chính, lớp motion, SFX cue và transition. Chưa tải video Pexels bản đầy đủ hoặc render tại bước này.

### DRAFT_REVIEW

Giao MP4 draft, contact sheet, storyboard và manifest. Không gọi draft là master.

## Schema media plan

Root tối thiểu:

```json
{
  "version": 1,
  "canvas": {"width": 1920, "height": 1080, "fps": 30},
  "total_duration_s": 12.4,
  "beats": []
}
```

Beat tối thiểu:

```json
{
  "id": "b001",
  "start_s": 0.0,
  "end_s": 4.8,
  "voice": "Anh chị đã bao giờ kết thúc một cuộc họp...",
  "mode": "BROLL_PRIMARY",
  "transition": "push-left",
  "cues": [{"at_s": 0.9, "kind": "text", "value": "CUỘC HỌP 60 PHÚT"}],
  "assets": [{
    "asset_id": "pexels-325185",
    "type": "video",
    "provider": "pexels",
    "pexels_id": "325185",
    "path": "media/trims/b001-pexels-325185.mp4",
    "source_url": "https://www.pexels.com/video/325185/",
    "author": "Tên tác giả",
    "query": "business team video meeting office",
    "width": 1920,
    "height": 1080,
    "start_s": 0.0,
    "end_s": 4.8
  }]
}
```

`start_s` và `end_s` của asset là placement trên timeline tổng. Nếu một beat có nhiều clip, các placement phải phủ beat theo thứ tự, không hở và không chồng quá tolerance.

Mode hợp lệ:

- `BROLL_PRIMARY`: cần ít nhất một video asset.
- `HYPERFRAME_FULL`: không cần video; `assets` nên rỗng.
- `BROLL_PLUS_OVERLAY`: cần video asset và danh sách cue cho overlay.

Cue `at_s` dùng thời gian tuyệt đối trong toàn video và phải nằm trong beat chứa nó.

## Media manifest

Mỗi asset đã tải cần có:

- ID nội bộ và provider ID.
- URL trang nguồn và URL download nếu chính sách cho phép lưu.
- Creator/author, search query và ngày truy cập.
- File gốc, file trim, duration, width, height, codec và fps.
- SHA-256 của file local.
- Beat được gán và placement.
- Ghi chú license/source attribution.

Không tự nhận asset là “royalty-free” nếu chưa xác minh điều khoản hiện hành.

## Storyboard HTML

File phải mở được trực tiếp từ local và vẫn đọc được khi JavaScript lỗi. Tối thiểu có:

- Header dự án, tổng duration và chú giải ba mode.
- Audio player trỏ tới `../audio/voiceover.mp3`.
- Timeline tỷ lệ theo duration.
- Scene card 16:9, timestamp và voice.
- Placeholder/thumbnail, text cue, logo cue, transition.
- JavaScript đồng bộ `audio.currentTime` với active beat.
- Nút nhảy tới beat và indicator phần trăm tiến độ.

Escape nội dung kịch bản trước khi đưa vào HTML. Không nhúng secret vào source.

## QA kỹ thuật

Chạy tối thiểu:

```bash
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate -show_entries format=duration -of json draft.mp4
ffmpeg -v error -i draft.mp4 -f null -
```

Yêu cầu:

- Video H.264, 1920×1080, 30 fps.
- Audio phát đúng, không cắt cuối câu.
- SFX nằm đúng timestamp, thấp hơn voice và không gây clipping.
- Các cue SFX đại diện nghe rõ trên loa laptop; peak sau AAC không cao hơn -1 dB.
- Limiter tắt auto-level để không vô tình nâng toàn bộ chương trình.
- Timeline phủ từ 0 đến duration với sai số tối đa 0,10 giây.
- Không có asset ID trùng hoặc clip portrait.
- Không có màn đen ngoài chủ ý chuyển cảnh.
- Text cue xuất hiện sau hoặc sát từ được nói tới, không đi trước nhiều giây.
