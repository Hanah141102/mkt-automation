# ElevenLabs v3 — TTS + Forced Alignment

ElevenLabs v3 is the multilingual, expressive voice model with native
character-level alignment timestamps. We use the `with-timestamps`
endpoint to get audio + per-character timing in one call, then collapse
characters into words client-side.

## Endpoint

```
POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/with-timestamps
```

Headers:

```
xi-api-key: <ELEVENLABS_API_KEY>
content-type: application/json
accept: application/json
```

Body:

```json
{
  "text": "Full plain text (markdown stripped). Punctuation matters for prosody.",
  "model_id": "eleven_v3",
  "voice_settings": {
    "stability":         0.5,
    "similarity_boost":  0.75,
    "style":             0.0,
    "use_speaker_boost": true
  },
  "output_format": "mp3_44100_128"
}
```

Response:

```json
{
  "audio_base64": "...",
  "alignment": {
    "characters": ["T", "h", "e", " ", "b", ...],
    "character_start_times_seconds": [0.0, 0.035, 0.07, ...],
    "character_end_times_seconds":   [0.035, 0.07, 0.10, ...]
  },
  "normalized_alignment": { /* same shape, normalized text */ }
}
```

`scripts/tts.py` handles all the marshalling — it decodes the base64
into an MP3, normalizes the alignment into `{characters, words,
duration_ms}` shape, and writes both files.

## Voice IDs

These are well-tested for English knowledge / news narration:

| Voice ID                | Name      | Gender | Tone                       |
|-------------------------|-----------|--------|----------------------------|
| pNInz6obpgDQGcFmaJgB    | Adam      | M      | Baritone, professional (default) |
| ErXwobaYiN019PkySvjV    | Antoni    | M      | Warm, casual               |
| TxGEqnHWrfWFTfGW9XjX    | Josh      | M      | Conversational, confident  |
| EXAVITQu4vr4xnSDxMaL    | Bella     | F      | Soft, narrator             |
| 21m00Tcm4TlvDq8ikWAM    | Rachel    | F      | Neutral, news-anchor       |
| AZnzlk1XvdvUeBnXmlld    | Domi      | F      | Energetic                  |

For Vietnamese, ElevenLabs v3 supports VN via the same voice IDs (the
model handles multilingual). For best VN results, prefer Antoni or
Bella — they pronounce VN diacritics more naturally than the
English-trained voices.

Override via `ELEVENLABS_VOICE_ID` env var or `--voice-id` flag.

## Voice settings tuning

| Setting             | Default | When to adjust                                |
|---------------------|---------|-----------------------------------------------|
| `stability`         | 0.5     | Lower (0.3) for more emotion / energy. Raise (0.7) for consistency on long reads. |
| `similarity_boost`  | 0.75    | Raise (0.9) if voice drifts; lower if it sounds robotic. |
| `style`             | 0.0     | Raise (0.3-0.5) for dramatic / expressive reads. Keep 0 for news. |
| `use_speaker_boost` | true    | Almost always true — improves clarity.        |

## Script prep rules

ElevenLabs reads punctuation as prosody, so script-prep affects output:

- **Commas** = short pause (~150ms)
- **Periods** = full sentence break (~400ms)
- **Semicolons / colons** = medium pause (~250ms)
- **Em dash `—`** = unpredictable, sometimes "hyphen" sometimes pause.
  `tts.py` replaces em dashes with `, ` automatically.
- **Numbers**: write as digits when narrator should read them as digits
  ("32 features"), as words when more natural ("thirty-two").
- **Acronyms**: separate letters with spaces if you want them spelled
  out ("M C P" → "M C P"); leave joined for word-pronounced ("MCP" →
  "mcp" sound). For our domain we usually want spelled-out.
- **Code / paths / URLs**: ElevenLabs reads `claude-code/CHANGELOG.md`
  literally. Pre-process if you want it cleaner — e.g. rewrite to
  "the changelog file in claude-code".
- **Headings**: `tts.py` converts `## Heading` to `Heading.` so the
  narrator says it as a sentence with a period break.

## Cost

Roughly 0.18 credits per character on the standard plan. A 90-second
script (~800 chars) costs ~144 credits = ~$0.05.

## Failure modes & fallback

If the API returns 401 → check `ELEVENLABS_API_KEY` env var.
If it returns 429 → rate-limited, wait 60s and retry.
If alignment array lengths don't match characters → re-run; this is a
transient bug we've seen rarely.

If the API is down entirely, the pipeline can fall back to local TTS
(`say` on macOS for English, or coqui-TTS) but you lose forced alignment
— captions would have to be estimated from word count × average WPM
(~150 WPM English, ~140 WPM Vietnamese). Not implemented in v1 of the
skill.

## Duration impact (v3 vs v2 vs turbo)

`eleven_v3` reads noticeably slower than older models — measured on
Vietnamese (~170 từ, voice Hoàng `K7ewtjKRNtwwt3lKQ6M0`):

| Model | Audio duration | Speed |
|---|---|---|
| `eleven_multilingual_v2` | ~6.7s | ~2.5 từ/s |
| `eleven_v3` (default here) | ~10.9s | ~1.6 từ/s — **~60% slower** |

**Layout implication:** when budgeting video timeline, DON'T assume v3
audio fits the same length as v2. For 60-90s short videos, v3 may push
the total to 100-150s. For 5-9 min long-form, expect ~8-15min render.

**When switching TO v3 mid-session:** re-extend `DURATION` in
`index.html` + re-time keyframe endings in scene timelines (the
`position: "+=N"` references to old ending). See sibling skill
`mkt-elevenlabs-tts-to-mp3` → `references/elevenlabs-model-duration.md`
for the full recipe.

**When switching AWAY from v3** (back to v2 for faster read): audio
shrinks, but `DURATION` in index.html stays the same → video ends with
extra `extend` tail. Re-render usually OK, but if master timeline has
`tl.to(..., { duration: DURATION - 0.5 })` style range locks, check
they don't overflow.
