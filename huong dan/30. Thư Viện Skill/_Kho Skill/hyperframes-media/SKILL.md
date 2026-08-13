---
name: hyperframes-media
description: "Tiền xử lý tài nguyên cho video HyperFrames: chuyển văn bản thành giọng đọc, bóc lời thoại từ audio hoặc video, và tách nền để làm lớp phủ trong suốt. Dùng trước khi dựng video."
ten-viet: "Xử Lý Media Cho HyperFrames"
nhom: "16. Xưởng Video AI"
cong-doan: "4. Dựng hình & hiệu ứng"
thu-tu: 3
ten-goc: "HyperFrames Media Preprocessing"
---

# Xử Lý Media Cho HyperFrames

Three CLI commands that produce assets for compositions: `tts` (speech), `transcribe` (timestamps), and `remove-background` (transparent video). Each downloads a model on first run and caches it under `~/.cache/hyperframes/`. Drop the output into the project, then reference it from the composition HTML — see the `hyperframes` skill for the audio/video element conventions.

## Text-to-Speech (`tts`)

Generate speech audio locally with Kokoro-82M. No API key.

```bash
npx hyperframes tts "Text here" --voice af_nova --output narration.wav
npx hyperframes tts script.txt --voice bf_emma --output narration.wav
npx hyperframes tts --list                       # all 54 voices
```

### Voice Selection

Match voice to content. Default is `af_heart`.

| Content type      | Voice                 | Why                           |
| ----------------- | --------------------- | ----------------------------- |
| Product demo      | `af_heart`/`af_nova`  | Warm, professional            |
| Tutorial / how-to | `am_adam`/`bf_emma`   | Neutral, easy to follow       |
| Marketing / promo | `af_sky`/`am_michael` | Energetic or authoritative    |
| Documentation     | `bf_emma`/`bm_george` | Clear British English, formal |
| Casual / social   | `af_heart`/`af_sky`   | Approachable, natural         |

### Multilingual

Voice IDs encode language in the first letter: `a`=American English, `b`=British English, `e`=Spanish, `f`=French, `h`=Hindi, `i`=Italian, `j`=Japanese, `p`=Brazilian Portuguese, `z`=Mandarin. The CLI auto-detects the phonemizer locale from the prefix — no `--lang` needed when the voice matches the text.

```bash
npx hyperframes tts "La reunión empieza a las nueve" --voice ef_dora --output es.wav
npx hyperframes tts "今日はいい天気ですね" --voice jf_alpha --output ja.wav
```

Use `--lang` only to override auto-detection (stylized accents). Valid codes: `en-us`, `en-gb`, `es`, `fr-fr`, `hi`, `it`, `pt-br`, `ja`, `zh`. Non-English phonemization requires `espeak-ng` system-wide (`brew install espeak-ng` / `apt-get install espeak-ng`).

### Speed

- `0.7-0.8` — tutorial, complex content, accessibility
- `1.0` — natural pace (default)
- `1.1-1.2` — intros, transitions, upbeat content
- `1.5+` — rarely appropriate; test carefully

### Long Scripts

For more than a few paragraphs, write to a `.txt` file and pass the path. Inputs over ~5 minutes of speech may benefit from splitting into segments.

### Requirements

Python 3.8+ with `kokoro-onnx` and `soundfile` (`pip install kokoro-onnx soundfile`). Model downloads on first use (~311 MB + ~27 MB voices, cached in `~/.cache/hyperframes/tts/`).

### Alternative TTS: edge-tts (Python)

When Kokoro doesn't support the target language (Vietnamese, Korean, Arabic, Cantonese, etc.) or you need higher-quality neural voices without downloading multi-GB models, use `edge-tts` directly. It wraps Microsoft's online Edge TTS service — no API key, no model download, but requires internet.

```bash
# Install
pip install edge-tts

# List available voices (200+ across 100+ languages)
edge-tts --list-voices

# Find Vietnamese voices
edge-tts --list-voices | grep -i vietnam

# Generate audio + word-level subtitles in one pass
edge-tts \
  --voice vi-VN-HoaiMyNeural \
  --text "$(cat script.txt)" \
  --write-media narration.mp3 \
  --write-subtitles narration.srt

# Common Vietnamese voices
# vi-VN-HoaiMyNeural (female, natural, warm — default recommendation)
# vi-VN-NamMinhNeural (male, clear, professional)
```

**Word-level timing with phrase segments** — for caption overlay, extract word boundaries from the SRT:

```python
import json, re

with open("narration.srt") as f:
    raw = f.read()

# Parse SRT into words with timestamps
# edge-tts --write-subtitles produces phrase-level SRT lines
# Distribute each word evenly across its phrase's time span
segments = []
for block in raw.strip().split("\n\n"):
    lines = block.split("\n")
    if len(lines) < 3:
        continue
    time_match = re.match(r"(\d+:\d+:\d+,\d+) --> (\d+:\d+:\d+,\d+)", lines[1])
    if not time_match:
        continue
    start_s = sum(int(x) * 60 ** i for i, x in enumerate(reversed(time_match[1].replace(",", ".").split(":"))))
    end_s   = sum(int(x) * 60 ** i for i, x in enumerate(reversed(time_match[2].replace(",", ".").split(":"))))
    text = " ".join(lines[2:])
    words = text.split()
    if words:
        seg_dur = (end_s - start_s) / len(words)
        for i, w in enumerate(words):
            w_start = start_s + i * seg_dur
            w_end = w_start + seg_dur
            segments.append({"text": w, "start": round(w_start, 3), "end": round(w_end, 3)})

with open("transcript.json", "w", encoding="utf-8") as f:
    json.dump(segments, f, ensure_ascii=False, indent=2)
```

This produces a flat `transcript.json` compatible with the `hyperframes` caption system. For languages where Whisper struggles with numbers or brand names (common with Vietnamese — e.g. `94%` → `chín mươi tư phần trăm`), edge-tts SRT output gives cleaner text that matches the original script exactly.

**When to use edge-tts vs Kokoro vs ElevenLabs:**

| Tool | Languages | Quality | Cost | Offline | Best for |
|------|-----------|---------|------|---------|----------|
| `npx hyperframes tts` (Kokoro) | EN, ES, FR, JA, ZH, PT-BR, HI, IT | Good neural | Free | ✅ Yes | 8 supported languages, no API needed |
| **edge-tts** (Python) | 100+ languages incl. VI, KO, AR, YUE, TH | Excellent neural | Free | ❌ Internet | Unsupported Kokoro languages, clean script-faithful output |
| ElevenLabs (via pipeline) | 32 languages | Best | Paid API | ❌ Internet | Production polish, voice cloning, audio tags |

### Voiceover replacement (switching TTS provider mid-project)

When regenerating a voiceover with a different TTS provider or voice (e.g., replacing edge-tts with an ElevenLabs voice clone, or Kokoro with edge-tts for a different language), the **new audio will have different duration and pacing** — sometimes dramatically so. Any project timing data keyed to the old voiceover (scene durations, beat/segment triggers, caption boundaries, transition cut points) will be misaligned.

**Workflow:**

1. **Generate** the replacement audio with your target provider (see the provider-specific commands above).
2. **Swap** the audio file at the same project location, or update `<audio src="...">` in `index.html`.
3. **Re-derive timing data** from the new audio. Every piece of metadata that was tied to the old voiceover needs regeneration:
   - **Word-level transcript** — `npx hyperframes transcribe voiceover.mp3` (or use your provider's native alignment output)
   - **Beat/boundary JSON** — if the project uses `beats.json`, `phrase-segments.json`, or similar for scene-trigger timing
   - **Scene `data-duration` attributes** — especially if total duration shifted by more than ~2s
   - **Caption phrase boundaries** — the new delivery may have different emphasis and pauses
4. **Update scene compositions** for the new pacing. The same script spoken at a different speed changes when each visual element lands.
5. **Lint + inspect + render** as usual:
   ```
   npx hyperframes lint
   npx hyperframes inspect --samples 20
   npx hyperframes render index.html -o output.mp4
   ```

**Common gotchas:**

| Gotcha | Fix |
|--------|-----|
| New voiceover is shorter/longer → scene transitions drift progressively | Always update audio `data-duration` first, then propagate timing to every scene mount and composition clip. |
| Beat/segment JSON still references old word timestamps | Regenerate from the actual new audio. Do NOT scale old beats proportionally — non-linear pacing changes (uneven pauses) don't compress linearly. |
| Caption cut points land mid-word or feel rushed after the swap | Re-run `npx hyperframes transcribe` on the new audio and regenerate captions from fresh word boundaries, not the old script's syllable counts. |
| ElevenLabs voice clone pauses differently than the original script | Use ElevenLabs v3 word-level alignment (returned in the TTS response) as the source of truth; `transcribe` with Whisper as fallback. |
| Scene feels empty after voice swap (speech is faster, gaps between words) | Add breathing/beat animations to fill new dead zones, or use SFX to bridge the timing gap. |

**When to skip this workflow:** if the voiceover duration is identical (e.g., same file re-encoded) or the project's animation is purely time-based with no audio-synced triggers.

## Transcription (`transcribe`)

Produce a normalized `transcript.json` with word-level timestamps.

```bash
npx hyperframes transcribe audio.mp3
npx hyperframes transcribe video.mp4 --model small --language es
npx hyperframes transcribe subtitles.srt          # import existing
npx hyperframes transcribe subtitles.vtt
npx hyperframes transcribe openai-response.json
```

### Language Rule (Non-Negotiable)

**Never use `.en` models unless the user explicitly states the audio is English.** `.en` models (`small.en`, `medium.en`) **translate** non-English audio into English instead of transcribing it. This silently destroys the original language.

1. Language known and non-English → `--model small --language <code>` (no `.en` suffix)
2. Language known and English → `--model small.en`
3. Language unknown → `--model small` (no `.en`, no `--language`) — whisper auto-detects

**Default model is `small`, not `small.en`.**

### Model Sizes

| Model      | Size   | Speed    | When to use                           |
| ---------- | ------ | -------- | ------------------------------------- |
| `tiny`     | 75 MB  | Fastest  | Quick previews, testing pipeline      |
| `base`     | 142 MB | Fast     | Short clips, clear audio              |
| `small`    | 466 MB | Moderate | **Default** — most content            |
| `medium`   | 1.5 GB | Slow     | Important content, noisy audio, music |
| `large-v3` | 3.1 GB | Slowest  | Production quality                    |

Music with vocals: start at `medium` minimum; produced tracks often need manual SRT/VTT import. For caption-quality checks (mandatory after every transcription), the cleaning JS, retry rules, and the OpenAI/Groq API import path, see [hyperframes/references/transcript-guide.md](../hyperframes/references/transcript-guide.md).

### Output Shape

Compositions consume a flat array of word objects. The `id` field (`w0`, `w1`, ...) is added during normalization for stable references in caption overrides; it's optional for backwards compatibility.

```json
[
  { "id": "w0", "text": "Hello", "start": 0.0, "end": 0.5 },
  { "id": "w1", "text": "world.", "start": 0.6, "end": 1.2 }
]
```

## Background Removal (`remove-background`)

Remove the background from a video or image so the subject (typically a person — avatar, presenter, talking head) sits as a transparent overlay in a composition.

```bash
npx hyperframes remove-background subject.mp4 -o transparent.webm  # default: VP9 alpha WebM
npx hyperframes remove-background subject.mp4 -o transparent.mov   # ProRes 4444 (editing)
npx hyperframes remove-background portrait.jpg -o cutout.png       # single-image cutout
npx hyperframes remove-background subject.mp4 -o subject.webm \
  --background-output plate.webm                                   # both layers in one pass
npx hyperframes remove-background subject.mp4 -o transparent.webm --device cpu
npx hyperframes remove-background --info                           # detected providers
```

Uses `u2net_human_seg` (MIT). First run downloads ~168 MB of weights to `~/.cache/hyperframes/background-removal/models/`.

### Layer separation (`--background-output`)

Pass `--background-output` (or `-b`) to emit a **second** transparent video alongside the cutout: same source RGB, alpha is `255 − mask` instead of `mask`. The cutout is the subject with a transparent background; the plate is the original surroundings with a transparent hole where the subject was.

| File                             | Alpha is…                                                 | Use it for                                                      |
| -------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------- |
| `-o subject.webm`                | The mask — subject opaque, background transparent         | Foreground layer, place on top                                  |
| `--background-output plate.webm` | Inverse — surroundings opaque, subject region transparent | Bottom layer; put text or graphics between this and the subject |

Both outputs share the same `--quality` preset and run from a single inference pass — encode cost roughly doubles, segmentation cost stays the same. Only valid for video inputs and `.webm`/`.mov` outputs.

**Hole-cut plate, not an inpainted clean plate.** The subject region in `plate.webm` is fully transparent — composite something opaque under it to fill the hole. The single test for whether `--background-output` is the right tool: _will anything ever be visible through the subject's silhouette where the subject used to be?_

| Use case                                                                            | Right tool                                                                         |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Text/graphics between the cutout and the plate (this command's reason for existing) | **Hole-cut** (`--background-output`)                                               |
| Subject onto an unrelated scene                                                     | Just `subject.webm`; ignore the plate                                              |
| Show the room _without_ the person, alone over no other content                     | **Clean plate** — needs an inpainter (LaMa, ProPainter, E2FGVI). Not this command. |
| Replace the subject with a different subject                                        | **Clean plate** — same as above                                                    |

If a user asks for "the room with the person removed" and intends to display it standalone, do **not** reach for `--background-output`. Tell them they need an inpainter.

Typical layered composition (the canonical hole-cut use case):

```html
<!-- z=1 the inverse-alpha plate fills everything except the subject region -->
<video
  src="plate.webm"
  data-start="0"
  data-duration="6"
  data-track-index="0"
  muted
  playsinline
></video>

<!-- z=2 graphics / text live between the two layers -->
<h1 id="headline" style="z-index:2; ...">MAKE IT IN HYPERFRAMES</h1>

<!-- z=3 the cutout floats the subject back over the headline -->
<div class="cutout-wrap" style="position:absolute;inset:0;z-index:3">
  <video
    src="subject.webm"
    data-start="0"
    data-duration="6"
    data-track-index="1"
    muted
    playsinline
  ></video>
</div>
```

This is functionally equivalent to the text-behind-subject pattern below, but you don't need the original `presenter.mp4` in the project — the plate replaces it. Useful when you want to ship just the two transparent layers and let the user drop arbitrary content between them.

### Output Format

| Format                | When                                                          |
| --------------------- | ------------------------------------------------------------- |
| `.webm` (VP9 + alpha) | Default. Compositions play this directly via `<video>`.       |
| `.mov` (ProRes 4444)  | Editing in DaVinci/Premiere/FCP. Large files.                 |
| `.png`                | Single-image cutout (still subject, layered over a backdrop). |

Chrome decodes VP9 alpha natively, so the `.webm` plugs into a composition like any other muted-autoplay video — see the `hyperframes` skill for the `<video>` track conventions.

### Quality presets

`--quality fast|balanced|best` controls only the VP9 encoder's CRF — segmentation quality is fixed.

| Preset     | CRF | When                                                  |
| ---------- | --- | ----------------------------------------------------- |
| `fast`     | 30  | Iterating, smaller file, looser color match           |
| `balanced` | 18  | Default. Visually identical for most uses             |
| `best`     | 12  | Master / final delivery. Largest file, tightest match |

### Compositing patterns — pick the right one

The cutout webm is a **re-encoded copy** of the source mp4's RGB. That choice has consequences depending on what you put behind it:

| Pattern                                                  | What's behind the cutout                   | Result                                                                                                                                                                                                                            |
| -------------------------------------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cutout over a different scene** (most common)          | Static image, gradient, or unrelated video | Looks great. The cutout's RGB is the only source of the subject — no doubling, no edge halo. This is what `remove-background` is built for.                                                                                       |
| **Cutout over its own source mp4** (text-behind-subject) | Same mp4 the cutout was generated from     | Two RGB sources for the same person. At default `--quality balanced` (crf 18) the doubling is barely visible; at `--quality fast` (crf 30) you'll see a faint color shift / edge halo. Use `--quality best` (crf 12) for masters. |
| **Cutout over a _different_ take of the same person**    | Footage of the same subject                | Will look like two separate people overlapping. Don't do this.                                                                                                                                                                    |

**Text-behind-subject** (headline behind a presenter):

```html
<video
  src="presenter.mp4"
  id="bg"
  data-start="0"
  data-duration="6"
  data-track-index="0"
  muted
  playsinline
></video>
<h1 id="headline" style="z-index:2; ...">MAKE IT IN HYPERFRAMES</h1>
<div class="cutout-wrap" style="position:absolute;inset:0;z-index:3;opacity:0">
  <video
    src="presenter.webm"
    data-start="0"
    data-duration="6"
    data-track-index="1"
    muted
    playsinline
  ></video>
</div>
```

Two key rules:

1. **Wrap the cutout video in a non-timed `<div>`** and animate the wrapper's opacity, not the video element's. The framework forces opacity:1 on active clips (any element with `data-start`/`data-duration`), so animating the video's opacity directly is silently overridden. The wrapper has no `data-*` attributes, so it's owned by your CSS/GSAP.
2. **Both videos use `data-start="0"` and `data-media-start="0"`** so the framework decodes them in sync from t=0. Late-mounting the cutout (`data-start=3.3`) introduces a seek + warm-up that lands a frame off the base mp4 — visible as one frame of misalignment at the cut.

Then GSAP-flip the wrapper opacity at the cut: `tl.set(cutoutWrap, { opacity: 1 }, 3.3)`.

## TTS → Transcribe → Captions

When there's no pre-recorded voiceover, generate one and transcribe it back to get word-level timestamps for captions:

```bash
npx hyperframes tts script.txt --voice af_heart --output narration.wav
npx hyperframes transcribe narration.wav   # → transcript.json
```

Whisper extracts precise word boundaries from the generated audio, so caption timing matches delivery without hand-tuning.
