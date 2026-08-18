#!/usr/bin/env python3
"""Resolve script B-roll needs against a shared SQLite library, then Pexels."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
REPO_ROOT = SKILL_DIR.parents[2]
STOPWORDS = {
    "a", "an", "and", "at", "for", "in", "of", "on", "the", "to", "with",
    "bị", "các", "cho", "của", "đang", "để", "là", "một", "những", "trong", "và"
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def normalize_text(value: str) -> str:
    return unicodedata.normalize("NFKC", value or "").lower()


def tokens(value: str) -> set[str]:
    return {
        token for token in re.findall(r"[^\W_]+", normalize_text(value), flags=re.UNICODE)
        if len(token) > 1 and token not in STOPWORDS
    }


def slugify(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", ascii_value.lower()).strip("-")[:64] or "broll"


def read_env(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    result: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.lstrip().startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        result[key.strip()] = value.strip()
    return result


def run(args: list[str], capture: bool = False) -> str:
    result = subprocess.run(
        args,
        check=False,
        text=True,
        stdout=subprocess.PIPE if capture else subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise RuntimeError(f"{args[0]} failed: {result.stderr.strip()}")
    return result.stdout or ""


def probe_video(path: Path) -> dict[str, Any]:
    raw = run([
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height,avg_frame_rate:format=duration",
        "-of", "json", str(path)
    ], capture=True)
    data = json.loads(raw)
    stream = data.get("streams", [{}])[0]
    width = int(stream.get("width") or 0)
    height = int(stream.get("height") or 0)
    duration = float(data.get("format", {}).get("duration") or 0)
    rate = str(stream.get("avg_frame_rate") or "0/1").split("/")
    fps = float(rate[0]) / float(rate[1]) if len(rate) == 2 and float(rate[1]) else 0.0
    if not width or not height or duration <= 0:
        raise ValueError(f"invalid video: {path}")
    return {
        "width": width,
        "height": height,
        "duration": duration,
        "duration_ms": round(duration * 1000),
        "fps": fps,
        "orientation": "portrait" if height > width else "landscape"
    }


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def initialize_database(connection: sqlite3.Connection) -> None:
    connection.executescript("""
        PRAGMA journal_mode=WAL;
        CREATE TABLE IF NOT EXISTS assets (
          id TEXT PRIMARY KEY,
          media_type TEXT NOT NULL,
          file_path TEXT NOT NULL,
          thumbnail_path TEXT,
          provider TEXT NOT NULL,
          provider_asset_id TEXT NOT NULL,
          source_url TEXT NOT NULL,
          creator_name TEXT,
          creator_url TEXT,
          query TEXT,
          category TEXT,
          literal_description TEXT NOT NULL,
          communication_purpose TEXT NOT NULL,
          suitable_for TEXT,
          avoid_when TEXT,
          keywords_vi TEXT,
          keywords_en TEXT,
          orientation TEXT,
          width INTEGER,
          height INTEGER,
          duration_ms INTEGER,
          fps REAL,
          sha256 TEXT UNIQUE,
          license TEXT NOT NULL,
          favorite INTEGER DEFAULT 0,
          quality_score REAL DEFAULT 0,
          active INTEGER DEFAULT 1,
          created_at TEXT NOT NULL,
          updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS asset_usages (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          asset_id TEXT NOT NULL,
          project_name TEXT,
          scene_id TEXT,
          script_excerpt TEXT,
          intended_purpose TEXT,
          suggestion_score REAL,
          accepted INTEGER,
          used_at TEXT NOT NULL,
          FOREIGN KEY(asset_id) REFERENCES assets(id)
        );
        CREATE VIRTUAL TABLE IF NOT EXISTS asset_search USING fts5(
          asset_id UNINDEXED,
          literal_description,
          communication_purpose,
          keywords_vi,
          keywords_en,
          suitable_for,
          avoid_when
        );
    """)
    columns = {row[1] for row in connection.execute("PRAGMA table_info(assets)")}
    for name, definition in (
        ("favorite", "INTEGER DEFAULT 0"),
        ("quality_score", "REAL DEFAULT 0"),
        ("active", "INTEGER DEFAULT 1"),
    ):
        if name not in columns:
            connection.execute(f"ALTER TABLE assets ADD COLUMN {name} {definition}")
    connection.commit()


def resolve_asset_path(raw_path: str, library_root: Path) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        return path
    candidates = [REPO_ROOT / path, library_root / path, Path.cwd() / path]
    return next((candidate.resolve() for candidate in candidates if candidate.exists()), candidates[0].resolve())


def phrase_coverage(need: dict[str, Any], row: sqlite3.Row) -> float:
    corpus = tokens(" ".join(str(row[key] or "") for key in (
        "literal_description", "communication_purpose", "keywords_vi",
        "keywords_en", "suitable_for", "category"
    )))
    def coverage(phrase: str) -> float:
        phrase_tokens = tokens(phrase)
        return len(phrase_tokens & corpus) / len(phrase_tokens) if phrase_tokens else 0.0

    intent_score = coverage(str(need.get("intent_vi", "")))
    query_score = coverage(str(need.get("query_en", "")))
    keyword_scores = [coverage(str(value)) for value in need.get("keywords", [])]
    keyword_score = sum(keyword_scores) / len(keyword_scores) if keyword_scores else 0.0
    return 0.30 * intent_score + 0.45 * query_score + 0.25 * keyword_score


def local_score(need: dict[str, Any], row: sqlite3.Row, orientation: str, usage_count: int) -> float:
    coverage = phrase_coverage(need, row)
    concepts = {normalize_text(str(item)).replace("-", "_").replace(" ", "_") for item in need.get("concepts", [])}
    category = normalize_text(str(row["category"] or "")).replace("-", "_").replace(" ", "_")
    concept_bonus = 0.18 if category and category in concepts else 0.0
    orientation_bonus = 0.12 if row["orientation"] == orientation else 0.0
    favorite_bonus = 0.06 if int(row["favorite"] or 0) else 0.0
    quality_bonus = min(0.08, max(0.0, float(row["quality_score"] or 0)) * 0.08)
    reuse_penalty = min(0.12, usage_count * 0.02)
    return max(0.0, min(1.0, 0.72 * coverage + concept_bonus + orientation_bonus + favorite_bonus + quality_bonus - reuse_penalty))


def choose_local_asset(
    connection: sqlite3.Connection,
    need: dict[str, Any],
    orientation: str,
    used: set[str],
    threshold: float,
    library_root: Path,
) -> tuple[sqlite3.Row, Path, float] | None:
    excluded = {str(item) for item in need.get("exclude_asset_ids", [])}
    usage_counts = dict(connection.execute("SELECT asset_id, COUNT(*) FROM asset_usages GROUP BY asset_id"))
    candidates = []
    for row in connection.execute("SELECT * FROM assets WHERE COALESCE(active, 1)=1 AND media_type='video'"):
        if row["id"] in used or row["id"] in excluded:
            continue
        path = resolve_asset_path(row["file_path"], library_root)
        if not path.exists():
            continue
        score = local_score(need, row, orientation, int(usage_counts.get(row["id"], 0)))
        candidates.append((score, row, path))
    if not candidates:
        return None
    score, row, path = max(candidates, key=lambda item: item[0])
    return (row, path, score) if score >= threshold else None


def api_json(url: str, api_key: str, attempts: int = 3) -> dict[str, Any]:
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"Authorization": api_key, "User-Agent": "mkt-broll-resolver/1.0"})
            with urllib.request.urlopen(request, timeout=20) as response:
                return json.load(response)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
            last_error = error
            if attempt + 1 < attempts:
                time.sleep(0.75 * (attempt + 1))
    raise RuntimeError(f"Pexels request failed after {attempts} attempts: {last_error}")


def download(url: str, destination: Path, attempts: int = 3) -> None:
    if destination.exists() and destination.stat().st_size:
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + ".part")
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "mkt-broll-resolver/1.0"})
            with urllib.request.urlopen(request, timeout=30) as response, temporary.open("wb") as handle:
                shutil.copyfileobj(response, handle)
            temporary.replace(destination)
            return
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            last_error = error
            temporary.unlink(missing_ok=True)
            if attempt + 1 < attempts:
                time.sleep(0.75 * (attempt + 1))
    raise RuntimeError(f"download failed after {attempts} attempts: {last_error}")


def choose_pexels_video(videos: list[dict[str, Any]], desired: float, excluded: set[str]) -> tuple[dict[str, Any], dict[str, Any]] | None:
    ranked = []
    for rank, video in enumerate(videos):
        asset_id = f"pexels-{video.get('id')}"
        if asset_id in excluded:
            continue
        files = [item for item in video.get("video_files", []) if item.get("file_type") == "video/mp4" and item.get("height", 0) > item.get("width", 0)]
        if not files:
            continue
        selected = min(files, key=lambda item: abs(item.get("height", 0) - 1280) + 2 * abs(item.get("width", 0) - 720))
        duration = float(video.get("duration") or 0)
        duration_fit = 1.0 if duration >= desired else max(0.0, duration / max(desired, 0.1))
        technical = 1 / (1 + abs(selected.get("height", 0) - 1280) / 1280)
        score = 0.55 * (1 / (1 + rank)) + 0.25 * duration_fit + 0.20 * technical
        ranked.append((score, video, selected))
    if not ranked:
        return None
    _, video, selected = max(ranked, key=lambda item: item[0])
    return video, selected


def portable_library_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path.resolve())


def upsert_downloaded_asset(
    connection: sqlite3.Connection,
    library_root: Path,
    need: dict[str, Any],
    video: dict[str, Any],
    selected_file: dict[str, Any],
) -> tuple[sqlite3.Row, Path]:
    asset_id = f"pexels-{video['id']}"
    existing = connection.execute("SELECT * FROM assets WHERE id=?", (asset_id,)).fetchone()
    if existing:
        path = resolve_asset_path(existing["file_path"], library_root)
        if path.exists():
            return existing, path

    page_slug = Path(urllib.parse.urlparse(video.get("url", "")).path).name
    page_slug = re.sub(rf"-{video['id']}$", "", page_slug) or need.get("query_en", "broll")
    category = str((need.get("concepts") or ["general"])[0])
    destination = library_root / "assets" / "videos" / f"{slugify(category)}-{slugify(page_slug)}-pexels-{video['id']}.mp4"
    thumbnail = library_root / "thumbnails" / f"{slugify(category)}-{slugify(page_slug)}-pexels-{video['id']}.jpg"
    download(selected_file["link"], destination)
    if video.get("image"):
        download(video["image"], thumbnail)
    probe = probe_video(destination)
    if probe["orientation"] != "portrait":
        raise ValueError(f"Pexels {video['id']} is not portrait")
    digest = file_sha256(destination)
    description = need.get("description") or page_slug.replace("-", " ")
    purpose = need["intent_vi"]
    keywords = ", ".join(str(item) for item in need.get("keywords", []))
    timestamp = now_iso()
    user = video.get("user") or {}
    connection.execute("""
        INSERT INTO assets (
          id, media_type, file_path, thumbnail_path, provider, provider_asset_id,
          source_url, creator_name, creator_url, query, category, literal_description,
          communication_purpose, suitable_for, avoid_when, keywords_vi, keywords_en,
          orientation, width, height, duration_ms, fps, sha256, license,
          favorite, quality_score, active, created_at, updated_at
        ) VALUES (?, 'video', ?, ?, 'pexels', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                  ?, ?, ?, ?, ?, ?, 'Pexels License', 0, 0, 1, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
          file_path=excluded.file_path, thumbnail_path=excluded.thumbnail_path,
          literal_description=excluded.literal_description,
          communication_purpose=excluded.communication_purpose,
          keywords_vi=excluded.keywords_vi, keywords_en=excluded.keywords_en,
          sha256=excluded.sha256, updated_at=excluded.updated_at
    """, (
        asset_id, portable_library_path(destination), portable_library_path(thumbnail), str(video["id"]),
        video.get("url", ""), user.get("name", ""), user.get("url", ""), need["query_en"],
        category, description, purpose, need.get("usage", "broll-fullscreen"), need.get("avoid_when", ""),
        keywords, f"{need['query_en']}, {keywords}", probe["orientation"], probe["width"], probe["height"],
        probe["duration_ms"], probe["fps"], digest, timestamp, timestamp
    ))
    connection.execute("DELETE FROM asset_search WHERE asset_id=?", (asset_id,))
    connection.execute("INSERT INTO asset_search VALUES (?, ?, ?, ?, ?, ?, ?)", (
        asset_id, description, purpose, keywords, f"{need['query_en']}, {keywords}",
        need.get("usage", "broll-fullscreen"), need.get("avoid_when", "")
    ))
    connection.commit()
    return connection.execute("SELECT * FROM assets WHERE id=?", (asset_id,)).fetchone(), destination


def ingest_user_asset(connection: sqlite3.Connection, library_root: Path, project: Path, need: dict[str, Any]) -> tuple[sqlite3.Row, Path]:
    source = Path(need["user_file"])
    if not source.is_absolute():
        source = project / source
    source = source.resolve()
    if not source.exists():
        raise FileNotFoundError(f"user_file not found: {source}")
    probe = probe_video(source)
    digest = file_sha256(source)
    existing = connection.execute("SELECT * FROM assets WHERE sha256=?", (digest,)).fetchone()
    if existing:
        return existing, resolve_asset_path(existing["file_path"], library_root)
    asset_id = f"user-{digest[:12]}"
    destination = library_root / "assets" / "videos" / f"{asset_id}-{slugify(source.stem)}{source.suffix.lower()}"
    materialize(source, destination)
    timestamp = now_iso()
    description = need.get("description") or source.stem.replace("-", " ").replace("_", " ")
    purpose = need["intent_vi"]
    keywords = ", ".join(str(item) for item in need.get("keywords", []))
    connection.execute("""
        INSERT INTO assets (
          id, media_type, file_path, thumbnail_path, provider, provider_asset_id,
          source_url, creator_name, creator_url, query, category, literal_description,
          communication_purpose, suitable_for, avoid_when, keywords_vi, keywords_en,
          orientation, width, height, duration_ms, fps, sha256, license,
          favorite, quality_score, active, created_at, updated_at
        ) VALUES (?, 'video', ?, NULL, 'user', ?, '', '', '', ?, ?, ?, ?, ?, ?, ?, ?,
                  ?, ?, ?, ?, ?, ?, 'User supplied', 1, 1, 1, ?, ?)
    """, (
        asset_id, portable_library_path(destination), digest[:12], need.get("query_en", ""),
        str((need.get("concepts") or ["user"])[0]), description, purpose,
        need.get("usage", "broll-fullscreen"), need.get("avoid_when", ""), keywords,
        f"{need.get('query_en', '')}, {keywords}", probe["orientation"], probe["width"], probe["height"],
        probe["duration_ms"], probe["fps"], digest, timestamp, timestamp
    ))
    connection.execute("INSERT INTO asset_search VALUES (?, ?, ?, ?, ?, ?, ?)", (
        asset_id, description, purpose, keywords, f"{need.get('query_en', '')}, {keywords}",
        need.get("usage", "broll-fullscreen"), need.get("avoid_when", "")
    ))
    connection.commit()
    return connection.execute("SELECT * FROM assets WHERE id=?", (asset_id,)).fetchone(), destination


def materialize(source: Path, destination: Path) -> None:
    if destination.exists() and destination.stat().st_size:
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        os.link(source, destination)
    except OSError:
        shutil.copy2(source, destination)


def timing_for_beat(beat: dict[str, Any], requested: float) -> tuple[float, float] | None:
    beat_duration = float(beat["duration_s"])
    guard = 2.0 if beat_duration >= 7.0 else 0.8
    available = beat_duration - 2 * guard
    if available < 2.0:
        return None
    duration = min(6.0, max(2.0, requested), available)
    start = float(beat["start_s"]) + guard + max(0.0, (available - duration) / 2)
    return round(start, 3), round(duration, 3)


def trim_video(source: Path, destination: Path, source_start: float, duration: float) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-ss", f"{source_start:.3f}", "-i", str(source), "-t", f"{duration:.3f}",
        "-c:v", "libx264", "-r", "30", "-g", "30", "-keyint_min", "30",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", str(destination)
    ])
    probe = probe_video(destination)
    if abs(probe["duration"] - duration) > 0.25:
        raise ValueError(f"trim duration mismatch for {destination}")


def resolve_pexels(
    connection: sqlite3.Connection,
    library_root: Path,
    need: dict[str, Any],
    api_key: str,
    desired: float,
    used: set[str],
) -> tuple[sqlite3.Row, Path, float] | None:
    query = urllib.parse.urlencode({
        "query": need["query_en"], "orientation": "portrait", "size": "medium", "per_page": 12
    })
    data = api_json(f"https://api.pexels.com/v1/videos/search?{query}", api_key)
    excluded = {str(item) for item in need.get("exclude_asset_ids", [])} | used
    selected = choose_pexels_video(data.get("videos", []), desired, excluded)
    if not selected:
        return None
    video, selected_file = selected
    row, path = upsert_downloaded_asset(connection, library_root, need, video, selected_file)
    return row, path, 0.75


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--needs", default="broll-needs.json")
    parser.add_argument("--library", default=str(REPO_ROOT / ".media-library"))
    parser.add_argument("--threshold", type=float, default=0.50)
    parser.add_argument("--max-assets", type=int, default=4)
    parser.add_argument("--download-missing", action="store_true")
    parser.add_argument("--local-only", action="store_true")
    args = parser.parse_args()

    if args.download_missing and args.local_only:
        parser.error("--download-missing and --local-only are mutually exclusive")
    if not shutil.which("ffprobe") or not shutil.which("ffmpeg"):
        raise SystemExit("ffprobe and ffmpeg are required")

    project = Path(args.project).resolve()
    needs_path = Path(args.needs)
    if not needs_path.is_absolute():
        needs_path = project / needs_path
    library_root = Path(args.library).resolve()
    library_root.mkdir(parents=True, exist_ok=True)
    needs_doc = json.loads(needs_path.read_text(encoding="utf-8"))
    beats_doc = json.loads((project / "beats.json").read_text(encoding="utf-8"))
    beats = {item["id"]: item for item in beats_doc.get("beats", [])}
    orientation = needs_doc.get("orientation", "portrait")

    connection = sqlite3.connect(library_root / "library.sqlite")
    connection.row_factory = sqlite3.Row
    initialize_database(connection)

    env = {**read_env(REPO_ROOT / ".env"), **os.environ}
    api_key = env.get("PEXELS_API_KEY", "")
    used: set[str] = set()
    assets: list[dict[str, Any]] = []
    unused: list[dict[str, Any]] = []
    counts = {"user": 0, "library": 0, "pexels": 0, "unused": 0}

    for need in needs_doc.get("needs", [])[: max(0, args.max_assets)]:
        beat_id = need.get("beat_id")
        beat = beats.get(beat_id)
        if not beat:
            unused.append({"beat_id": beat_id, "reason": "beat not found"})
            continue
        if beat.get("avatar"):
            unused.append({"beat_id": beat_id, "reason": "avatar beat cannot receive B-roll"})
            continue
        if not need.get("intent_vi") or not need.get("query_en"):
            unused.append({"beat_id": beat_id, "reason": "intent_vi and query_en are required"})
            continue
        connection.execute(
            "DELETE FROM asset_usages WHERE project_name=? AND scene_id=?",
            (project.name, beat_id),
        )
        connection.commit()
        requested = float(need.get("desired_duration_s") or 3.5)
        placement = timing_for_beat(beat, requested)
        if not placement:
            unused.append({"beat_id": beat_id, "reason": "beat cannot fit a safe B-roll interval >=2s"})
            continue
        placement_start, placement_duration = placement

        try:
            if need.get("user_file"):
                row, source = ingest_user_asset(connection, library_root, project, need)
                score, assigned_by = 1.0, "user"
            else:
                local = choose_local_asset(connection, need, orientation, used, args.threshold, library_root)
                if local:
                    row, source, score = local
                    assigned_by = "library"
                elif args.download_missing and api_key:
                    remote = resolve_pexels(connection, library_root, need, api_key, placement_duration, used)
                    if not remote:
                        unused.append({"beat_id": beat_id, "reason": "Pexels returned no usable portrait video"})
                        continue
                    row, source, score = remote
                    assigned_by = "pexels"
                else:
                    reason = "no local match >= threshold"
                    if args.download_missing and not api_key:
                        reason += "; PEXELS_API_KEY is missing"
                    unused.append({"beat_id": beat_id, "reason": reason})
                    continue

            asset_id = row["id"]
            if asset_id in used:
                unused.append({"beat_id": beat_id, "reason": f"asset {asset_id} already used in this video"})
                continue
            source_probe = probe_video(source)
            if orientation == "portrait" and source_probe["orientation"] != "portrait":
                unused.append({"beat_id": beat_id, "reason": f"asset {asset_id} is not portrait"})
                continue

            project_source = project / "media" / f"{asset_id}{source.suffix.lower()}"
            materialize(source, project_source)
            default_source_start = max(0.0, (source_probe["duration"] - placement_duration) / 2)
            source_start = float(need.get("source_start_s", default_source_start))
            source_start = min(max(0.0, source_start), max(0.0, source_probe["duration"] - placement_duration))
            trimmed = project / "broll-clips" / f"{slugify(beat_id)}-{asset_id}.mp4"
            trim_video(source, trimmed, source_start, placement_duration)
            used.add(asset_id)

            source_meta = {
                "provider": row["provider"], "url": row["source_url"],
                "creator": row["creator_name"], "creatorUrl": row["creator_url"],
                "license": row["license"], "query": row["query"]
            }
            assets.append({
                "assetId": asset_id,
                "file": str(project_source.relative_to(project)),
                "type": "video",
                "orientation": source_probe["orientation"],
                "duration": round(source_probe["duration"], 3),
                "description": row["literal_description"],
                "assignedBeat": beat_id,
                "assignedBy": assigned_by,
                "score": round(float(score), 3),
                "usage": need.get("usage", "broll-fullscreen"),
                "bestSegment": {"start": round(source_start, 3), "dur": placement_duration},
                "trimmed": str(trimmed.relative_to(project)),
                "placement": {"start_s": placement_start, "duration_s": placement_duration, "track": 45},
                "source": source_meta
            })
            connection.execute("""
                INSERT INTO asset_usages (
                  asset_id, project_name, scene_id, script_excerpt,
                  intended_purpose, suggestion_score, accepted, used_at
                ) VALUES (?, ?, ?, ?, ?, ?, 1, ?)
            """, (
                asset_id, project.name, beat_id, beat.get("anchor_context", ""),
                need["intent_vi"], score, now_iso()
            ))
            connection.commit()
            counts[assigned_by] += 1
            print(f"{assigned_by:7s} {beat_id} <- {asset_id} score={score:.2f}")
        except Exception as error:
            unused.append({"beat_id": beat_id, "reason": str(error)})

    counts["unused"] = len(unused)
    manifest = {
        "version": 1,
        "resolver": {
            "library": str(library_root),
            "threshold": args.threshold,
            "counts": counts,
            "generated_at": now_iso()
        },
        "assets": assets,
        "unused": unused
    }
    manifest_path = project / "media-manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    connection.close()

    if assets:
        contact = subprocess.run([
            sys.executable, str(SCRIPT_DIR / "make_contact_sheet.py"),
            "--project", str(project), "--manifest", str(manifest_path)
        ], check=False, text=True, capture_output=True)
        if contact.stdout.strip():
            print(contact.stdout.strip())
        if contact.returncode:
            print(f"contact-sheet warning: {contact.stderr.strip()}", file=sys.stderr)

    print(f"manifest -> {manifest_path}")
    print("counts " + " ".join(f"{key}={value}" for key, value in counts.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
