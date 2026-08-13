---
name: mkt-elevenlabs-tts-to-mp3
description: "Convert Vietnamese/English script text to MP3 voiceover using ElevenLabs Text-to-Speech API (eleven_multilingual_v2). Default voice is Hoàng's brand voice (K7ewtjKRNtwwt3lKQ6M0). Same input (script text) and output (MP3 file) contract as mkt-minimax-tts-to-mp3 — downstream skills (heygen-mp3-to-mp4, mkt-full-video-with-11-hyperframe-heygen*, mkt-hyperframe-knowledge-video*) work unchanged. Reads ELEVENLABS_API_KEY, ELEVENLABS_VOICE_ID, ELEVENLABS_MODEL_ID, ELEVENLABS_API_BASE from .env. Includes an mp3 → aiff converter for HeyGen workflows. USE WHEN user says 'tạo mp3 elevenlabs', 'elevenlabs tts', 'tạo voiceover elevenlabs', 'text to speech elevenlabs', 'đọc text bằng giọng Hoàng', 'giọng elevenlabs', 'elevenlabs script to mp3', 'tạo voiceover brand voice', or wants a voiceover MP3 and ElevenLabs is the chosen TTS provider (default for Hoàng's content)."
---

# ElevenLabs TTS → MP3

Chuyển script text thành file MP3 voiceover bằng ElevenLabs Text-to-Speech API
(voice `K7ewtjKRNtwwt3lKQ6M0` — Hoàng's brand voice, model `eleven_multilingual_v2`).
Output là MP3 chuẩn, dùng tiếp được cho `heygen-mp3-to-mp4` và các pipeline
`mkt-full-video-with-11-hyperframe-heygen*` (Phase 1) và `mkt-hyperframe-knowledge-video*`
(Phase 1). **Day-style parity với `mkt-minimax-tts-to-mp3`** — same input/output
contract, downstream skills không phân biệt được MP3 từ provider nào.

## Env vars (đọc từ `.env` ở project root)

```bash
ELEVENLABS_API_KEY=        # bắt buộc — https://elevenlabs.io — Settings → API Keys
ELEVENLABS_VOICE_ID=       # optional — mặc định K7ewtjKRNtwwt3lKQ6M0 (Hoàng's brand voice)
                           # có thể override bằng cloned voice id khác
ELEVENLABS_MODEL_ID=       # optional — mặc định eleven_multilingual_v2
                           # alternatives: eleven_turbo_v2_5, eleven_flash_v2_5
ELEVENLABS_API_BASE=       # optional — mặc định https://api.elevenlabs.io
                           # (EU residency dùng https://api.eu.elevenlabs.io)

# Voice settings (optional override)
ELEVENLABS_STABILITY=          # optional — mặc định 0.35 (0.0–1.0)
ELEVENLABS_SIMILARITY_BOOST=   # optional — mặc định 0.75 (0.0–1.0)
ELEVENLABS_STYLE=              # optional — mặc định 0.0 (0.0–1.0, càng cao càng expressive)
ELEVENLABS_USE_SPEAKER_BOOST=  # optional — mặc định true
```

## Default voice settings (Hoàng brand voice)

| Param | Default | Lý do |
|---|---|---|
| `model_id` | `eleven_multilingual_v2` | Hỗ trợ tiếng Việt tốt nhất, chậm hơn turbo nhưng chất lượng tự nhiên hơn |
| `stability` | 0.35 | Vừa phải — quá cao (>0.7) sẽ đơ, quá thấp (<0.2) sẽ lặp từ |
| `similarity_boost` | 0.75 | Giữ đặc trưng giọng Hoàng nhưng không quá sát để tránh artifact |
| `style` | 0.0 | Mặc định — nếu cần kịch tính tăng 0.2–0.4, podcast tăng 0.1 |
| `use_speaker_boost` | true | Cải thiện clarity |

## Workflow

0. **Pre-flight verify (BẮT BUỘC trước khi convert)** — chạy:

   ```bash
   python3 <skill_dir>/scripts/elevenlabs_verify.py
   ```

   Script load `.env`, kiểm tra `ELEVENLABS_API_KEY` (format: 32+ chars), gọi 1
   request nhỏ tới `GET /v1/voices` để xác nhận key hợp lệ + voice id tồn tại
   trong account. Nếu lỗi, in chính xác biến nào sai để user sửa — KHÔNG nhảy
   thẳng vào convert với script chính rồi debug trên file output thật.

   **Lý do:** ElevenLabs trả 401 khi key sai, 404 khi voice id không thuộc
   account này, 422 khi text quá dài. Cả 3 đều trông giống nhau nếu chỉ nhìn
   status code — chỉ verify script mới phân biệt được trong 1 lần gọi.

1. **Lấy script**: user đưa text trực tiếp hoặc đường dẫn file. ElevenLabs
   `/v1/text-to-speech` chấp nhận tối đa **5000 ký tự** mỗi request. Nếu script
   dài hơn, **chia theo câu** (boundary = dấu chấm/xuống dòng) rồi gọi nhiều
   lần, ghép MP3 bằng ffmpeg `concat` demuxer.

2. **Chạy helper script** (nằm trong `scripts/` của skill này):

   ```bash
   python3 <skill_dir>/scripts/elevenlabs_tts.py \
     --text-file /path/to/script.txt \
     --out /path/to/voiceover.mp3
   ```

   Tham số optional: `--voice-id <id>` (override env), `--model eleven_turbo_v2_5`,
   `--stability 0.5`, `--similarity-boost 0.8`, `--style 0.2`, `--api-base https://api.eu.elevenlabs.io`.

   Script tự load `.env` từ thư mục hiện hành, gọi
   `POST {API_BASE}/v1/text-to-speech/{voice_id}` với header `xi-api-key`,
   body `{"text": ..., "model_id": ..., "voice_settings": {...}}`, ghi MP3
   bytes từ response. Stdout là JSON một dòng:
   `{out, bytes, duration_ms, voice_id, model, chars_used}`.

3. **Validate output** — kiểm tra:

   ```bash
   ffprobe -v quiet -show_entries format=duration,bit_rate -of csv=p=0 voiceover.mp3
   ```

   Duration hợp lý ~150 từ/phút tiếng Việt. Nghe thử nếu user yêu cầu — gửi
   file cho user duyệt trước khi đưa vào bước HeyGen.

4. **Optional: convert sang AIFF cho HeyGen** — HeyGen upload API khuyến nghị
   AIFF/WAV. Nếu pipeline kế tiếp là `heygen-mp3-to-mp4` thì MP3 vẫn OK,
   nhưng nếu cần AIFF:

   ```bash
   python3 <skill_dir>/scripts/mp3_to_aiff.py \
     --in voiceover.mp3 --out voiceover.aiff
   ```

   Helper dùng `ffmpeg` (subprocess, không cần pydub). Sample rate 44100 Hz,
   PCM 16-bit, mono — chuẩn cho HeyGen upload.

5. **Báo kết quả**: đường dẫn MP3 + duration + số ký tự đã dùng (ElevenLabs
   tính phí theo ký tự).

## Lỗi thường gặp

| Lỗi | Nguyên nhân thật / xử lý |
|-----|-------------------------|
| `401 Unauthorized` | API key sai / hết hạn / thuộc account khác. Verify bằng `GET /v1/voices` — nếu cả `api.elevenlabs.io` và `api.eu.elevenlabs.io` đều trả 401 thì key sai, đừng đổi base URL nữa. |
| `404 voice_not_found` | Voice id không thuộc account này (thường là cloned voice từ account khác). Verify bằng `GET /v1/voices` xem voice id có trong list không. |
| `422 unprocessable_entity` | Text quá 5000 chars, hoặc model không hỗ trợ giọng này. Chia nhỏ text hoặc đổi `model_id`. |
| `429 too_many_requests` | Vượt quota character/giờ. Đợi hoặc upgrade plan. |
| MP3 nghe rỗng/0 bytes | Voice id đúng nhưng account hết credit. Check quota qua `GET /v1/user/subscription`. |
| Tiếng Việt đọc lỗ (phát âm sai dấu) | Dùng `eleven_multilingual_v2` (không phải turbo), viết số/từ viết tắt thành chữ đầy đủ, escape ký tự đặc biệt. |
| `style=0.5` nghe quá kịch tính | Style mặc định 0.0 — chỉ tăng 0.1–0.3 cho podcast/kịch. Style cao + low stability = bùng nổ. |
| Connection timeout | `eleven_multilingual_v2` chậm cho text dài (3–8s). Tăng timeout lên 60s hoặc split thành nhiều request nhỏ. |

## Ghi chú

- ElevenLabs trả audio dạng **MP3 bytes trực tiếp** (binary response) — KHÔNG
  phải hex string trong JSON như MiniMax. Helper script ghi thẳng `response.content`
  ra file, KHÔNG cần decode hex.
- Vietnamese: `eleven_multilingual_v2` hỗ trợ tiếng Việt tốt nhất hiện tại.
  `eleven_turbo_v2_5` nhanh hơn ~2x nhưng chất lượng tiếng Việt kém hơn.
- **Model-speed pitfall (v3 vs v2)**: `eleven_v3` đọc Vietnamese chậm hơn đáng kể
  so với `eleven_multilingual_v2` — cùng 1 script ~170 từ tiếng Việt, v2 ra ~6.7s
  audio thì v3 ra ~10.9s (chậm hơn ~60%, nhiều pause tự nhiên hơn). Nếu switch
  model giữa chừng, PHẢI re-extend `DURATION` master `index.html` (data-duration
  + JS const + `duration_ms` trong alignment.json) VÀ re-time keyframes ending
  trong các scene timelines (offset `position: "+=N"` references to old ending).
  Xem chi tiết + recipe: `references/elevenlabs-model-duration.md`.
- Voice cloning: tạo Instant Voice Clone trên elevenlabs.io (cần ≥ 1 phút
  audio sample) → dùng voice id đó trong `ELEVENLABS_VOICE_ID`. Hoàng's brand
  voice `K7ewtjKRNtwwt3lKQ6M0` đã được clone sẵn.
- Same contract với `mkt-minimax-tts-to-mp3`: text in → MP3 out. Pipeline
  cha (`mkt-full-video-with-11-hyperframe-heygen*`) gọi Phase 1 dùng thẳng
  helper script này, không cần đổi gì ở Phase 2/3.
- **DURATION-SYNC PITFALL (rất hay gặp):** Sau khi tạo MP3, PHẢI sync
  `data-duration` của audio clip và `DURATION` biến trong `index.html` +
  `audio/alignment.json` + tất cả scene timeline GSAP keyframes cho khớp
  với audio duration thật (đo bằng `ffprobe`). Sai số 0.5s là audio bị
  cắt giữa chừng hoặc video đen ở cuối. Helper `sync_audio_duration.py`
  trong `scripts/` tự động update tất cả chỗ.
- **Workflow style:** khi user yêu cầu test giọng mới, chạy probe + verify
  script trước rồi mới hỏi user. Đừng hỏi "bạn muốn thử API base nào?"
  trước khi đã thử cả 2 — chỉ tốn 2 curl calls và trả lời được câu hỏi
  "key có hợp lệ không?" / "voice id có tồn tại không?" trong vòng 1 phút.
  Chỉ clarify khi 2 base URL cho kết quả khác nhau (key có thể region-specific).

## References

- ElevenLabs API docs: https://elevenlabs.io/docs/api-reference/text-to-speech
- Default voice: `K7ewtjKRNtwwt3lKQ6M0` (Hoàng's brand voice, Vietnamese-friendly)
- Sibling skill: `mkt-minimax-tts-to-mp3` (alternative TTS provider, same contract)
- Downstream skill: `heygen-mp3-to-mp4` (consumes MP3 output)
