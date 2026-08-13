# Smoke Test — Use Case 4 — Video HeyGen + HyperFrames Lite

- Thư mục test: `/Users/tonyhoang/Documents/GitHub/mkt-automation`
- Ngày test: 2026-08-12
- Skill: `$mkt-hyperframe-knowledge-video-heygen-9-16-lite`

## Kết quả tiền kiểm

| Hạng mục | Kết quả |
|---|---|
| `cut_avatar_audio.py --help` | PASS |
| `verify_avatar_sync.py --help` | PASS |
| `validate_visual_mix.py --help` | PASS |
| `map_beats.py --help` | PASS |
| FFmpeg | PASS |
| HyperFrames CLI | PASS |
| `ELEVENLABS_API_KEY` | CHƯA CẤU HÌNH trong shell test |
| `HEYGEN_API_KEY` | CHƯA CẤU HÌNH trong shell test |
| `PEXELS_API_KEY` | CHƯA CẤU HÌNH trong shell test |

## Kết luận

Các bộ kiểm tra cốt lõi và công cụ render đều chạy được trong repo. Chưa chạy end-to-end vì ba khóa dịch vụ chưa hiện diện trong shell test; chạy thật còn tiêu tốn voice/avatar credit và cần script, avatar identity cùng storyboard đã duyệt. Giáo án phải dạy đây là **preflight đạt, production chưa chạy**, không được nói đã tạo MP4.
