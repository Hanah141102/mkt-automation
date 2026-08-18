# SFX design cho raw-footage video

SFX nhấn một thay đổi nhìn thấy hoặc spoken anchor; không phải nhạc nền và không dùng để lấp khoảng trống.

## Kho mặc định

Nguồn thường dùng: `workspace/assets/reels/sfx/`.

| File | Dùng cho |
|---|---|
| `Whoosh sound effect (1).mp3` | major transition hoặc object dịch chuyển |
| `SUDDEN SUSPENSE.mp3` | mở vấn đề/thiếu bằng chứng |
| `búng tay.mp3` | khóa bước, chuyển item, click ngắn |
| `Discord Notification - Sound Effect.mp3` | phản hồi AI/message xuất hiện |
| `ting.mp3` | checkmark, proof, stat tick |
| `lung linh.mp3` | reveal tích cực hoặc knowledge graph |
| `boom.mp3` | premise/CTA punchline, dùng rất nhẹ |
| `camera-flash.mp3` | screenshot/title reveal; trim nếu moment ngắn |
| `Wow.mp3` | payoff lớn, chỉ khi thật sự phù hợp |

## Luật placement

1. Tối đa 6 hit/phút; spacing ≥1,25s.
2. Volume `0.12–0.30`; bắt đầu ở 0.16–0.20 rồi nghe draft.
3. Một loud effect tối đa trong một moment.
4. Không đặt vào câu nhạy cảm, confession, đoạn cảm xúc hoặc giữa từ.
5. `whoosh` chỉ cho transition lớn; không dùng ở mọi cut.
6. `boom` không được làm voice clipping hoặc peak sát 0dBFS.
7. Probe duration từng file; `data-duration` không vượt moment cần nhấn.
8. Mỗi cue ghi `time`, `file`, `volume`, `spoken_anchor`, `visual_action`, `reason`.

## Track và QA

- Source audio nằm trong `rough-cut.mp4`, track 10, volume gốc.
- SFX dùng track 70+ và unique ID.
- Nghe riêng ±2s quanh từng cue, sau đó nghe toàn draft.
- Dùng `volumedetect`/loudness scan để tìm clipping nhưng quyết định cuối bằng tai: voice luôn thắng.
- Nếu cue không có hành động/cụm từ rõ, xóa cue.
