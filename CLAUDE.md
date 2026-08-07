# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **Claude Code skills pack** for an AI-driven Vietnamese-language marketing video pipeline — not a conventional application. There is no app to build/lint/test; the "product" is a set of `.claude/skills/*/SKILL.md` definitions (plus helper scripts) that Claude Code loads and invokes to turn a topic/script into a published short-form or landscape video, and the `research/` and `workspace/` directories those skills read from and write to.

The only tracked dependency is `puppeteer` (root `package.json`) used by some skill helper scripts for browser automation/screenshots. There is no build step, linter, or test suite for the repo itself.

## Environment setup

- Copy `.env.example` → `.env` and fill in API keys. `.env` is gitignored; never commit real keys.
- Key vars: `HEYGEN_API_KEY` / `HEYGEN_AVATAR_LOOKS` / `HEYGEN_VOICE_ID` (avatar lip-sync), `ELEVENLABS_API_KEY` / `ELEVENLABS_VOICE_ID` (default TTS), `MINIMAX_API_KEY` / `MINIMAX_VOICE_ID` (alternate TTS, selected via `TTS_PROVIDER=minimax`), `BLOTATO_API_KEY` (multi-platform publishing), `YOUTUBE_API_KEY` (trend/topic research), `DOWNSUB_API_KEY` (YouTube transcript fetch).
- `workspace/` (generated content) and all `*.mp4/*.mov/*.mp3/*.wav/*.webm` are gitignored — treat them as build output, not source.

## Repository layout

- `.claude/skills/` — the skill definitions Claude Code loads. This is the actual "codebase."
- `workspace/content/<YYYY-MM-DD>/<slug>/` — per-video working directories produced by the pipelines (audio/, scenes/, compositions/, design.md, script.md, alignment.json, final `<slug>.mp4`). Generated, gitignored.
- `workspace/assets/` — reusable brand assets (avatar images, SFX) referenced by skills across projects.
- `videos/<project-name>/` — standalone HyperFrames composition projects that *are* committed (e.g. `videos/reactjs-intro-motion/`). Each has its own `package.json` with an exact pinned `hyperframes@X.Y.Z` version and its own `CLAUDE.md`/`AGENTS.md` describing the HyperFrames skill/workflow router (`/hyperframes`, `/product-launch-video`, `/faceless-explainer`, etc.). Treat these as a separate tool ecosystem from the marketing skills above — read the project's own CLAUDE.md when working inside one.
- `research/` — YouTube topic/trend research outputs (`research/youtube/topics/<topic>/`, `research/reports/`) produced by the research skills.

## Skill architecture

Skills fall into a few layers; understand the layering before editing or adding one:

1. **Atomic producers** — single input → single output, no orchestration:
   - `mkt-elevenlabs-tts-to-mp3`, `mkt-minimax-tts-to-mp3` — script text → MP3 voiceover.
   - `heygen-mp3-to-mp4` — one MP3 → one HeyGen avatar lip-sync MP4. Uses a **hybrid** call pattern: REST (`scripts/upload_asset.py` against `upload.heygen.com`) for asset upload since the HeyGen MCP server has no upload tool, then MCP (`mcp__heygen__*`) for video creation/polling/download. Reuse this pattern for any future HeyGen asset work.
   - `heygen-script-to-mp4` — script text → HeyGen MP4, letting HeyGen's own TTS speak (no ElevenLabs step).
   - `youtube-transcript`, `youtube-trend-finder`, `mkt-youtube-topic-researcher` — YouTube research, independent of the video pipeline.

2. **HyperFrames core** — `hyperframes`, `hyperframes-cli`, `hyperframes-core`, `hyperframes-animation`, `hyperframes-creative`, `hyperframes-keyframes`, `hyperframes-media`, `hyperframes-registry`. These are the generic HyperFrames authoring/rendering skills (composition HTML contract, GSAP animation patterns, CLI commands like `init/check/render/preview/publish`, TTS/transcribe/background-removal preprocessing, registry component installs). They apply both to ad-hoc `/hyperframes` work in `videos/` and as building blocks the marketing pipelines below call into.

3. **Orchestrator pipelines** — multi-phase skills that chain the atomic producers into a finished MP4, e.g.:
   - `mkt-full-video-with-11-hyperframe-heygen[-16-9]` — script → TTS → HeyGen lip-sync → HyperFrames scene packaging → rendered MP4 (9:16 or 16:9).
   - `mkt-hyperframe-knowledge-video[-heygen-16-9|-heygen-9-16]` — knowledge/news video with a slide motion-graphic pane, optionally with a HeyGen avatar in a SPLIT↔PIP or FULL↔SPLIT layout.
   - `mkt-hyperframe-talking-head-video[-16-9]` — packages a pre-recorded talking-head MP4 (not HeyGen-generated) with captions/b-roll/SFX.
   - These run **autopilot**: no mid-pipeline checkpoints or preview gates, sensible defaults chosen for missing info, and the final response is the absolute path to the rendered MP4. When editing or extending a pipeline skill, preserve this autopilot contract unless the user asks otherwise.
   - Phase 3 (scene authoring) in these pipelines typically fans out **parallel sub-agents**, one per scene, each producing a standalone composition HTML file — sub-agents author and self-review only; they never run `npx hyperframes` themselves (that's centralized in the orchestrator to avoid false errors from concurrent renders against not-yet-complete assets).

4. **Distribution** — `mkt-blotato-publish-social` posts a finished MP4/image/text to multiple platforms (Facebook, TikTok, Instagram, YouTube, Threads, X, LinkedIn) via the Blotato API, typically invoked after a pipeline finishes rendering.

Sibling skills with near-identical names differ on one axis — check the aspect ratio (9:16 vs 16:9), presence of a HeyGen avatar, or footage-provided-vs-generated — before assuming two are interchangeable; each skill's SKILL.md states explicitly when *not* to use it in favor of a sibling.

## Nguồn chất liệu content — Tony Brain vault

Khi viết script/content cần **giọng văn thật, insight thật, hoặc framework** (không phải content chung chung), đọc thêm kho second-brain cá nhân của Hoàng tại `/Users/tonyhoang/Documents/GitHub/Tony Brain` (repo Obsidian riêng, **không phải** thư mục con của repo này — private, đừng copy nguyên văn ra ngoài nơi public). Vault này vận hành theo 4 tầng RAW → MINE → CORE → MINT (chi tiết trong `README.md` của vault đó); các điểm vào hữu ích cho việc viết content:

- `Me.md` — Hoàng là ai, đang ở đâu, văn phong/quan điểm cá nhân. Đọc trước khi viết bất cứ content nào cần đúng "giọng" của Hoàng.
- `2. Mine/Daily Notes/` và `2. Mine/Weekly Notes/` — nhật ký hàng ngày/tuần, nguồn chuyện thật/case thật để làm ví dụ, hook, hoặc mở bài cho video.
- `3. Core/Dots/Statements/` (prefix `PN —`) — các insight đã chắt lọc thành câu khẳng định có quan điểm; dùng làm luận điểm cốt lõi cho script thay vì phát biểu chung chung.
- `3. Core/Dots/Frameworks/` — các framework đã hệ thống hoá (nội dung, kinh doanh, tư duy); tra trước khi cần dựng script theo một framework có sẵn thay vì bịa cấu trúc mới.
- `4. Mint/Background/Brand Kit — Trần Văn Hoàng · FreedomBuilders.md` — brand voice/định vị cá nhân dùng khi content cần nhất quán thương hiệu.
- `5. Toolbox/Templates/` — có sẵn template content đã proven (`Template - 10X Fanpage post v6.md`, `Template - 10X short Video.md`, `Template - Prompt - 10X Fanpage Post V6.md`...).

Vault đó có CLAUDE.md riêng — nếu phải thao tác sâu trong vault (không chỉ đọc tham khảo), mở project đó và đọc CLAUDE.md của nó trước.

## Working conventions

- Skills are Vietnamese-first in their SKILL.md instructions (the target audience/output language is Vietnamese); code/scripts inside them are in English.
- When a skill needs a Python helper, it's invoked via `uv run .claude/skills/<skill>/scripts/<name>.py` — there's no repo-wide virtualenv contract beyond that.
- HyperFrames render commands are version-pinned per project (`npx --yes hyperframes@X.Y.Z ...`) inside `videos/*/package.json` so renders stay reproducible; don't casually bump the pin without checking `npx hyperframes@latest upgrade --project . --check` first.
