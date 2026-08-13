# B-roll resolver contracts

## Contents

1. `broll-needs.json`
2. `media-manifest.json`
3. SQLite records
4. Scoring and timing
5. Failure behavior

## 1. `broll-needs.json`

Author this file after `beats.json` exists. Include only non-avatar beats where real footage materially improves comprehension or retention.

```json
{
  "version": 1,
  "orientation": "portrait",
  "needs": [
    {
      "beat_id": "scene-03-problem",
      "intent_vi": "Minh họa AI agent nhận mục tiêu rồi phân tích dữ liệu",
      "query_en": "business analyst using AI analytics dashboard",
      "keywords": [
        "AI agent",
        "phân tích dữ liệu",
        "analytics dashboard"
      ],
      "concepts": ["ai_agent", "analytics"],
      "desired_duration_s": 3.5,
      "usage": "broll-fullscreen",
      "exclude_asset_ids": []
    }
  ]
}
```

Optional fields:

- `user_file`: absolute path or path relative to the project. This assignment always wins.
- `description`: literal description supplied by the user or observed from frames.
- `avoid_when`: visual conditions that would make the clip misleading.
- `exclude_asset_ids`: local asset IDs or `pexels-<id>` values rejected during QA.
- `source_start_s`: approved source trim start selected after reading the full-source contact sheet.

Write one need per beat. Default to 2–4 needs for a 30–90 second video. A need is not an instruction to download: it is an instruction to resolve local-first.

## 2. `media-manifest.json`

The resolver emits:

```json
{
  "version": 1,
  "resolver": {
    "library": "/absolute/path/.media-library",
    "threshold": 0.5,
    "counts": {
      "user": 0,
      "library": 2,
      "pexels": 1,
      "unused": 1
    }
  },
  "assets": [
    {
      "assetId": "pexels-38901929",
      "file": "media/pexels-38901929.mp4",
      "type": "video",
      "orientation": "portrait",
      "duration": 23.8,
      "description": "Người dùng tương tác với dashboard tài chính",
      "assignedBeat": "scene-03-problem",
      "assignedBy": "library",
      "score": 0.88,
      "usage": "broll-fullscreen",
      "bestSegment": { "start": 10.15, "dur": 3.5 },
      "trimmed": "broll-clips/scene-03-problem-pexels-38901929.mp4",
      "placement": { "start_s": 11.16, "duration_s": 3.5, "track": 45 },
      "source": {
        "provider": "pexels",
        "url": "https://www.pexels.com/video/...",
        "creator": "Creator Name",
        "creatorUrl": "https://www.pexels.com/@creator",
        "license": "Pexels License",
        "query": "business analytics dashboard"
      }
    }
  ],
  "unused": [
    {
      "beat_id": "scene-04-benefits",
      "reason": "no local match >= 0.50 and Pexels fallback unavailable"
    }
  ]
}
```

All paths inside a project manifest are relative to the project. Resolve them against the project root when wiring.

## 3. SQLite records

Store media files on disk and metadata in `<library>/library.sqlite`. The resolver is compatible with the existing `assets`, `asset_search`, and `asset_usages` tables created by `scripts/pexels/seed-broll-library.mjs`.

Important semantic fields:

- `literal_description`: what visibly happens in the file.
- `communication_purpose`: what idea the footage can communicate.
- `keywords_vi` and `keywords_en`: bilingual retrieval terms.
- `suitable_for`: useful script roles or contexts.
- `avoid_when`: contexts where reuse would mislead.

Use SQLite FTS5 for manual inspection:

```bash
sqlite3 -header -column .media-library/library.sqlite \
  "SELECT asset_id, snippet(asset_search, 2, '[', ']', '…', 12) AS match
   FROM asset_search WHERE asset_search MATCH 'dòng tiền OR doanh thu';"
```

Do not store video bytes as SQLite BLOBs.

## 4. Scoring and timing

Local score combines:

- Best bilingual phrase-token coverage.
- Exact `concepts` ↔ `category` match.
- Requested orientation.
- Favorite/quality metadata.
- A small penalty for previous or same-video reuse.

Require `score >= 0.50`. An exact user assignment bypasses scoring.

For a beat at least 7 seconds long, preserve 2 seconds at both edges. For a 4–7 second beat, preserve 0.8 seconds at both edges and use a 2–3 second clip. Skip beats that cannot hold at least 2 seconds safely.

Choose the middle source segment by default. Read `broll-source-contact-sheet.jpg`; when another interval is better, set `source_start_s` in the need and rerun. Read `broll-contact-sheet.jpg` to verify the exact final trim.

## 5. Failure behavior

- Missing/malformed need: add it to `unused`; continue other needs.
- Avatar beat: reject the need; never mount B-roll.
- Missing Pexels key: continue local-only and log the miss without exposing secrets.
- API/rate/network failure: retry briefly, then retain the motion-graphic scene.
- Invalid media or failed `ffprobe`: do not insert or mount it.
- Horizontal result in a portrait run: reject it rather than relying on destructive center crop.
- Duplicate SHA-256: reuse the canonical SQLite asset.
