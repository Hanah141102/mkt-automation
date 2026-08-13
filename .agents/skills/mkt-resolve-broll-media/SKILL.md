---
name: mkt-resolve-broll-media
description: Resolve reusable B-roll for Vietnamese or English marketing video scripts and timed beats. Search the shared SQLite media library first, fetch portrait Pexels videos only when no local asset clears the relevance threshold, materialize muted clips into a HyperFrames project, and emit media-manifest.json plus a review contact sheet. Use for 9:16 knowledge videos, AI-agent/business content, automatic filler-footage suggestions, B-roll reuse, or the Phase 1b media step of mkt-hyperframe-knowledge-video-heygen-9-16-lite.
---

# Resolve reusable B-roll media

Turn script beats into a small, traceable set of B-roll clips. Reuse the shared library before making any Pexels request. Never download media merely to decorate every beat.

## Contract

Require:

- A HyperFrames project containing `beats.json` and usually `script.md`.
- A shared library at `<repo>/.media-library/library.sqlite`.
- `PEXELS_API_KEY` in `<repo>/.env` only when network fallback is allowed.
- `ffprobe` and `ffmpeg`; ImageMagick `montage` is optional but recommended.

Produce:

- `<project>/broll-needs.json`: AI-authored semantic needs.
- `<project>/media-manifest.json`: source of truth consumed by the LITE master.
- `<project>/media/`: project-local full source via hard link or copy.
- `<project>/broll-clips/`: muted, trimmed H.264 clips.
- `<project>/broll-source-contact-sheet.jpg`: early/middle/late frames of each full source.
- `<project>/broll-contact-sheet.jpg`: early/middle/late frames of each final trimmed clip.
- SQLite usage rows and newly downloaded Pexels assets.

Read [references/contracts.md](references/contracts.md) before authoring `broll-needs.json` or consuming the manifest.

## Workflow

### 1. Select B-roll opportunities

Read `script.md`, `beats.json`, and any user media instructions. Select only 2–4 strong SCENE beats by default:

- Exclude every beat with `avatar: true`.
- Prefer concrete actions, evidence, environments, customer activity, money, dashboards, and workflows.
- Skip abstract claims already communicated better by motion graphics.
- Preserve user asset assignments exactly; represent them with `user_file`.
- Do not request more than one fullscreen B-roll clip per beat.

Write `<project>/broll-needs.json`. Supply bilingual terms: `intent_vi` describes the communication purpose, while `query_en` describes a literal searchable shot. Make `query_en` concrete, such as `customer support agent working at office`, not `great customer experience`.

### 2. Resolve local-first

Run:

```bash
python3 "$BROLL_SKILL/scripts/resolve_broll.py" \
  --project "$OUT" \
  --needs "$OUT/broll-needs.json" \
  --library "$PROJECT_ROOT/.media-library" \
  --download-missing \
  --max-assets 4
```

Resolution order is strict:

1. User-assigned file.
2. Active local SQLite asset scoring at least `0.50`.
3. Pexels portrait-video search using `query_en`.
4. No asset; retain the motion-graphic scene and log the miss.

Use `--local-only` when network access is forbidden. Do not combine it with `--download-missing`.

### 3. Inspect once

Read `<project>/broll-source-contact-sheet.jpg` first, then `<project>/broll-contact-sheet.jpg`. The first sheet reveals whether another source interval is better; the second verifies the exact rendered clip.

- If every clip is relevant and visually safe, continue.
- If the asset is right but the interval is wrong, set `source_start_s` from the source sheet and rerun without downloading.
- If the asset itself is wrong, add its ID to `exclude_asset_ids`, make `query_en` more literal, and rerun once.
- If the rerun still misses, remove that need and use motion graphics. Never force a weak match.
- Treat visible brands, sensitive people, private data, or misleading financial imagery as a mismatch.

### 4. Hand off to HyperFrames

Use `media-manifest.json` as the only wiring source. Mount `trimmed` clips in the master at track 45+, muted, using the emitted `placement.start_s` and `placement.duration_s`. Tell each scene author the covered interval so it does not place essential content underneath.

After the final video succeeds, retain the usage ledger. The next project should see the same asset as a reusable candidate rather than download it again.

## Non-negotiable rules

- Never print, copy into source, or commit `PEXELS_API_KEY`.
- Never scrape Pexels or prefetch large collections. Download at most the requested missing clips.
- Prefer portrait MP4 near 720×1280 for the 9:16 pipeline.
- Use each asset at most once per video.
- Keep user assignment above automatic scoring.
- Require score `>=0.50` for local automatic reuse.
- Strip B-roll audio and re-encode H.264/30fps before mounting.
- Keep Pexels URL, creator, query, license, and SHA-256 in SQLite/manifest.
- Do not place B-roll on avatar windows.
- Do not use B-roll shorter than 2 seconds; skip beats that cannot fit a safe interval.

## Commands

```bash
# Normal LITE pipeline usage
python3 scripts/resolve_broll.py --project "$OUT" --needs "$OUT/broll-needs.json" \
  --library "$PROJECT_ROOT/.media-library" --download-missing

# Offline reuse only
python3 scripts/resolve_broll.py --project "$OUT" --needs "$OUT/broll-needs.json" \
  --library "$PROJECT_ROOT/.media-library" --local-only

# Rebuild the visual review artifact
python3 scripts/make_contact_sheet.py --project "$OUT"
```

Report counts for user-assigned, library-reused, Pexels-downloaded, and unused needs. Do not report a successful media phase until every selected file passes `ffprobe` and the contact sheet has been inspected.
