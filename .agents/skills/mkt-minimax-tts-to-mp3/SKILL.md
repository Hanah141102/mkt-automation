---
name: mkt-minimax-tts-to-mp3
description: "Convert spoken-only Vietnamese/English narration to MP3 voiceover using MiniMax T2A v2 API (speech-02). Reject production briefs, headings, visual directions, and SFX notes before making a paid request. Drop-in alternative to mkt-elevenlabs-tts-to-mp3 with the same spoken-script input and MP3 output contract."
---

# MiniMax TTS → MP3

Chuyển script text thành file MP3 voiceover bằng MiniMax T2A v2 (`speech-02-hd` /
`speech-02-turbo`). Output là MP3 chuẩn, dùng tiếp được cho `mkt-heygen-mp3-to-mp4`
và các pipeline `mkt-full-video-with-11-hyperframe-heygen*` (thay thế Phase 1
ElevenLabs).

**Input contract:** file đầu vào chỉ được chứa lời narrator nói thành tiếng.
Không đưa production brief, heading beat, visual/camera direction, b-roll,
SFX, music, caption hoặc ghi chú editor vào file TTS. Hãy tách chúng ra khỏi
`voiceover.txt` trước khi gọi MiniMax.

## Env vars (đọc từ `.env` ở project root)

```bash
MINIMAX_API_KEY=        # bắt buộc — https://platform.minimax.io
MINIMAX_GROUP_ID=       # bắt buộc — GroupId của account
MINIMAX_VOICE_ID=       # bắt buộc — system voice hoặc cloned voice id
MINIMAX_MODEL=          # optional — mặc định speech-02-hd (chậm, chất lượng cao);
                        # dùng speech-02-turbo nếu cần nhanh/rẻ
MINIMAX_API_BASE=       # optional — mặc định https://api.minimax.io
                        # (account China dùng https://api.minimaxi.com)
```

## Workflow

0. **Pre-flight verify (BẮT BUỘC trước khi convert)** — chạy:

   ```bash
   python3 <skill_dir>/scripts/minimax_verify.py
   ```

   Script này load `.env`, kiểm tra 3 biến bắt buộc (`MINIMAX_API_KEY`,
   `MINIMAX_GROUP_ID`, `MINIMAX_VOICE_ID`), rồi gọi một request `t2a_v2`
   với câu test ngắn để xác nhận key + group + voice đều hợp lệ. Nếu có
   lỗi, in chính xác biến nào sai để user sửa — KHÔNG nhảy thẳng vào
   convert với script chính rồi debug trên file output thật. Xem
   bảng lỗi bên dưới để map nhanh.

   Lý do: nếu thiếu `MINIMAX_GROUP_ID` thì server trả `2013 invalid params,
   empty field` (không phải "voice id không tồn tại" như bảng lỗi cũ) — nếu
   API key sai thì trả `1004 login fail`. Cả hai đều trông giống nhau nếu
   chỉ nhìn status code; chỉ verify script mới phân biệt được trong 1 lần gọi.

1. **Lấy spoken script**: user đưa text trực tiếp hoặc đường dẫn file. Chỉ
   giữ nội dung narrator nói. Nếu script dài
   hơn ~10.000 ký tự, chia nhỏ theo đoạn và gọi nhiều lần, sau đó nối bằng
   ffmpeg (`concat` demuxer).

   Không dùng trực tiếp file có `## Hook`, `Visual: ...`, `B-roll: ...`,
   `[camera zoom]`, `SFX: ...`, hoặc các đoạn giải thích cho editor.

1.5. **Spoken-script preflight (BẮT BUỘC trước API):**

   ```bash
   python3 <skill_dir>/scripts/validate_spoken_script.py \
     --text-file /path/to/voiceover.txt
   ```

   Helper `minimax_tts.py` cũng chạy cùng kiểm tra và sẽ dừng trước request
   nếu phát hiện nội dung không phải lời đọc.

2. **Chạy helper script** (nằm trong `scripts/` của skill này):

   ```bash
   python3 <skill_dir>/scripts/minimax_tts.py \
     --text-file /path/to/script.txt \
     --out /path/to/voiceover.mp3
   ```

   Tham số optional: `--voice-id <id>` (override env), `--model speech-02-turbo`,
   `--speed 1.1` (0.5–2.0).

   Script tự load `.env` từ thư mục hiện hành, gọi `POST /v1/t2a_v2?GroupId=...`,
   decode hex audio trong JSON response và ghi MP3. Stdout là JSON một dòng:
   `{out, bytes, duration_ms, usage_characters, voice_id, model}`.

3. **Validate output**: kiểm tra file tồn tại và `duration_ms` hợp lý so với độ
   dài script (~150 từ/phút tiếng Việt). Nghe thử nếu user yêu cầu — gửi file
   cho user duyệt trước khi đưa vào bước HeyGen.

4. **Báo kết quả**: đường dẫn MP3 + duration + số ký tự đã dùng (tính phí theo
   ký tự).

## Lỗi thường gặp

| Lỗi | Nguyên nhân thật / xử lý |
|-----|-------------------------|
| `1004 login fail: Please carry the API secret key in the 'Authorization' field` | API key sai / hết hạn / thuộc account khác region. Verify bằng cách gọi 1 request nhỏ — nếu cả `api.minimax.io` và `api.minimaxi.com` đều trả 1004 thì key sai, đừng đổi base URL nữa. |
| `2013 invalid params, empty field` | Thường là `MINIMAX_GROUP_ID` trống, **KHÔNG PHẢI** voice id. Server yêu cầu GroupId là query param bắt buộc. Nếu chắc chắn GroupId có rồi mà vẫn 2013 thì mới nghi voice id. |
| `2013 invalid voice_id` / voice-not-found | Voice id không thuộc account này — kiểm tra lại `MINIMAX_VOICE_ID` (system voice vs cloned voice) |
| `invalid GroupId` | `MINIMAX_GROUP_ID` sai format hoặc sai account — lấy lại từ platform.minimax.io account settings |
| `voice/list` returns 404 | Endpoint này KHÔNG TỒN TẠI trên MiniMax. Đừng dùng làm probe "verify key" — hãy gọi thẳng `t2a_v2` với text ngắn. |
| Cả 2 base URL (`api.minimax.io` và `api.minimaxi.com`) đều phản hồi cùng lỗi | Key sai, không phải vấn đề region/routing. Cả hai server đều live, đều trả 1004 với key rác. |
| Response không có `data.audio` | In nguyên payload ra để debug; thường do text rỗng, model name sai, hoặc account hết quota |
| Tiếng Việt đọc sai | Thử `speech-02-hd` thay vì turbo; viết số/từ viết tắt thành chữ đầy đủ trong script |

## Ghi chú

- MiniMax trả audio dạng **hex string trong JSON** (non-streaming) — không phải
  bytes trực tiếp như ElevenLabs. Helper script đã xử lý, đừng tự curl rồi ghi
  thẳng response ra file.
- Voice cloning: tạo cloned voice trên platform.minimax.io rồi dùng voice id đó
  trong `MINIMAX_VOICE_ID` — giống pattern brand voice của ElevenLabs.
- Contract giống `mkt-elevenlabs-tts-to-mp3`: text in → MP3 out. Khi pipeline
  cha (`mkt-full-video-with-11-hyperframe-heygen*`) gọi Phase 1, có thể dùng
  skill này thay thế mà không đổi gì ở Phase 2/3.
- **Workflow style**: khi user yêu cầu test một provider mới, ưu tiên chạy
  probe + verify script rồi mới hỏi user. Đừng hỏi "bạn muốn thử base URL
  nào?" trước khi đã thử cả 2 — chỉ tốn 2 curl calls và trả lời được câu
  hỏi "key có hợp lệ không?" / "GroupId có cần không?" trong vòng 1 phút.
  Chỉ clarify khi 2 base URL cho kết quả khác nhau (key có thể region-specific).
- **SPOKEN-CONTENT PITFALL:** TTS sẽ đọc mọi chữ được truyền vào. Luôn
  validate file trước; MP3 skill không tự đoán hay tự diễn giải phần nào là
  lời thoại.
