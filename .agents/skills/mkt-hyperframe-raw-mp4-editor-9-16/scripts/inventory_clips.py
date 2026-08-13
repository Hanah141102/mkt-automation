#!/usr/bin/env python3
"""Kiểm kê MP4 thô bằng ffprobe và tạo clip-inventory.json."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


def natural_key(path: Path) -> list[object]:
  return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", path.name)]


def probe(path: Path) -> dict:
  command = [
    "ffprobe", "-v", "error", "-show_entries",
    "format=duration,format_name:stream=index,codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels",
    "-of", "json", str(path),
  ]
  try:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
  except FileNotFoundError as exc:
    raise RuntimeError("Không tìm thấy ffprobe trong PATH") from exc
  except subprocess.CalledProcessError as exc:
    raise RuntimeError(f"ffprobe lỗi với {path.name}: {exc.stderr.strip()}") from exc
  return json.loads(result.stdout)


def parse_fps(value: str | None) -> float:
  if not value or value == "0/0":
    return 0.0
  if "/" in value:
    left, right = value.split("/", 1)
    return float(left) / float(right) if float(right) else 0.0
  return float(value)


def main() -> int:
  parser = argparse.ArgumentParser(description="Tạo inventory cho raw/*.mp4")
  parser.add_argument("--project", type=Path, required=True)
  args = parser.parse_args()

  project = args.project.resolve()
  raw_dir = project / "raw"
  if not raw_dir.is_dir():
    print(f"FAIL: thiếu thư mục {raw_dir}", file=sys.stderr)
    return 1

  files = sorted(
    (path for path in raw_dir.iterdir() if path.is_file() and path.suffix.lower() == ".mp4"),
    key=natural_key,
  )
  if not files:
    print(f"FAIL: không có MP4 trong {raw_dir}", file=sys.stderr)
    return 1

  clips = []
  errors = []
  for index, path in enumerate(files, start=1):
    try:
      data = probe(path)
    except RuntimeError as exc:
      errors.append(str(exc))
      continue
    streams = data.get("streams", [])
    video = next((item for item in streams if item.get("codec_type") == "video"), None)
    audio = next((item for item in streams if item.get("codec_type") == "audio"), None)
    duration = float(data.get("format", {}).get("duration") or 0)
    clip_id = f"clip-{index:03d}"
    if not video:
      errors.append(f"{path.name}: thiếu video stream")
    if not audio:
      errors.append(f"{path.name}: thiếu audio stream")
    if duration <= 0:
      errors.append(f"{path.name}: duration không hợp lệ")
    clips.append({
      "clip_id": clip_id,
      "filename": path.name,
      "path": str(path.relative_to(project)),
      "duration": round(duration, 3),
      "video": {
        "codec": video.get("codec_name") if video else None,
        "width": int(video.get("width") or 0) if video else 0,
        "height": int(video.get("height") or 0) if video else 0,
        "fps": round(parse_fps(video.get("r_frame_rate") if video else None), 3),
      },
      "audio": {
        "codec": audio.get("codec_name") if audio else None,
        "sample_rate": int(audio.get("sample_rate") or 0) if audio else 0,
        "channels": int(audio.get("channels") or 0) if audio else 0,
      },
      "filename_order": index,
    })

  output = {
    "version": 1,
    "project": project.name,
    "clips": clips,
    "raw_total_duration": round(sum(item["duration"] for item in clips), 3),
    "ordering_note": "filename_order chỉ là thứ tự tự nhiên của tên file; phải xác minh bằng transcript",
  }
  output_path = project / "clip-inventory.json"
  output_path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

  for clip in clips:
    shape = f'{clip["video"]["width"]}x{clip["video"]["height"]}'
    print(f'{clip["clip_id"]}: {clip["filename"]} · {clip["duration"]:.2f}s · {shape}')
  if errors:
    for error in errors:
      print(f"FAIL: {error}", file=sys.stderr)
    return 1
  print(f"PASS: {len(clips)} clip · {output['raw_total_duration']:.2f}s → {output_path}")
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
