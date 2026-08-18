#!/usr/bin/env python3
"""Inventory video, image and audio assets under a user-supplied source folder."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


VIDEO_EXTENSIONS = {".mp4", ".mov", ".m4v", ".webm", ".mkv"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".heic"}
AUDIO_EXTENSIONS = {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg"}
SKIP_PARTS = {".git", "node_modules", ".venv", "venv", "renders"}


def ffprobe(path: Path) -> dict:
  result = subprocess.run(
    [
      "ffprobe", "-v", "error", "-show_entries",
      "format=duration:stream=index,codec_type,codec_name,width,height,avg_frame_rate,sample_rate,channels",
      "-of", "json", str(path),
    ],
    check=False,
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
  )
  if result.returncode:
    raise RuntimeError(result.stderr.strip() or "ffprobe failed")
  return json.loads(result.stdout)


def fps(value: str) -> float:
  try:
    numerator, denominator = value.split("/", 1)
    return round(float(numerator) / float(denominator), 3) if float(denominator) else 0.0
  except (AttributeError, ValueError, ZeroDivisionError):
    return 0.0


def media_type(extension: str) -> str | None:
  if extension in VIDEO_EXTENSIONS:
    return "video"
  if extension in IMAGE_EXTENSIONS:
    return "image"
  if extension in AUDIO_EXTENSIONS:
    return "audio"
  return None


def role_hint(path: Path, kind: str) -> str:
  normalized = path.stem.lower().replace("_", " ").replace("-", " ")
  if kind == "audio":
    return "sfx" if any(token in normalized for token in ("sfx", "sound", "whoosh", "boom", "ting")) else "audio"
  if kind == "image":
    return "evidence-image" if any(token in normalized for token in ("obsidian", "graph", "screen", "chat", "dashboard")) else "image"
  if any(token in normalized for token in ("b roll", "broll", "screen record", "ghi nho", "graph")):
    return "user-broll"
  return "review-as-talking-head-or-broll"


def describe(path: Path, root: Path) -> dict:
  kind = media_type(path.suffix.lower())
  if kind is None:
    raise ValueError("unsupported extension")
  payload = ffprobe(path)
  streams = payload.get("streams", [])
  video = next((item for item in streams if item.get("codec_type") == "video"), None)
  audio = next((item for item in streams if item.get("codec_type") == "audio"), None)
  duration_raw = payload.get("format", {}).get("duration")
  duration = round(float(duration_raw), 3) if duration_raw not in (None, "N/A") else None
  width = int(video.get("width") or 0) if video else None
  height = int(video.get("height") or 0) if video else None
  orientation = None
  if width and height:
    orientation = "portrait" if height > width else "landscape" if width > height else "square"
  return {
    "relative_path": str(path.relative_to(root)),
    "absolute_path": str(path.resolve()),
    "type": kind,
    "role_hint": role_hint(path, kind),
    "extension": path.suffix.lower(),
    "size_bytes": path.stat().st_size,
    "duration_s": duration,
    "video": None if not video else {
      "codec": video.get("codec_name"),
      "width": width,
      "height": height,
      "orientation": orientation,
      "fps": fps(str(video.get("avg_frame_rate") or "0/1")),
    },
    "audio": None if not audio else {
      "codec": audio.get("codec_name"),
      "sample_rate": int(audio.get("sample_rate") or 0),
      "channels": int(audio.get("channels") or 0),
    },
  }


def main() -> int:
  parser = argparse.ArgumentParser(description="Kiểm kê đệ quy video, ảnh và audio trong folder nguồn")
  parser.add_argument("--source", type=Path, required=True)
  parser.add_argument("--output", type=Path, required=True)
  args = parser.parse_args()
  source = args.source.resolve()
  if not source.is_dir():
    print(f"FAIL: source không phải folder: {source}", file=sys.stderr)
    return 1

  assets = []
  errors = []
  candidates = sorted(
    path for path in source.rglob("*")
    if path.is_file()
    and media_type(path.suffix.lower())
    and not any(part in SKIP_PARTS for part in path.relative_to(source).parts)
  )
  for path in candidates:
    try:
      assets.append(describe(path, source))
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as error:
      errors.append({"relative_path": str(path.relative_to(source)), "error": str(error)})

  counts = {kind: sum(item["type"] == kind for item in assets) for kind in ("video", "image", "audio")}
  document = {
    "version": 1,
    "source": str(source),
    "counts": counts,
    "assets": assets,
    "errors": errors,
  }
  args.output.parent.mkdir(parents=True, exist_ok=True)
  args.output.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
  print(
    f"PASS: {len(assets)} asset · video={counts['video']} image={counts['image']} "
    f"audio={counts['audio']} error={len(errors)} → {args.output}"
  )
  return 0 if not errors else 2


if __name__ == "__main__":
  raise SystemExit(main())
