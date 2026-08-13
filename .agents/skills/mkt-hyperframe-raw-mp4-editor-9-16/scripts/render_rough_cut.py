#!/usr/bin/env python3
"""Render edit-plan.json thành rough-cut.mp4 giữ audio nói thật trong MP4."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


def run(command: list[str]) -> None:
  try:
    subprocess.run(command, check=True)
  except FileNotFoundError as exc:
    raise RuntimeError(f"Không tìm thấy lệnh: {command[0]}") from exc
  except subprocess.CalledProcessError as exc:
    raise RuntimeError(f"Lệnh lỗi ({exc.returncode}): {' '.join(command[:6])} …") from exc


def filter_graph(fit: str, duration: float) -> tuple[str, str]:
  fade_out = max(0.0, duration - 0.008)
  audio = f"[0:a:0]aresample=48000,afade=t=in:st=0:d=0.008,afade=t=out:st={fade_out:.6f}:d=0.008[a]"
  if fit == "contain-blur":
    video = (
      "[0:v:0]split=2[bg][fg];"
      "[bg]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=28:8[bgv];"
      "[fg]scale=1080:1920:force_original_aspect_ratio=decrease[fgv];"
      "[bgv][fgv]overlay=(W-w)/2:(H-h)/2,fps=30,setsar=1,format=yuv420p[v]"
    )
  else:
    video = "[0:v:0]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,format=yuv420p[v]"
  return f"{video};{audio}", "[v]"


def main() -> int:
  parser = argparse.ArgumentParser(description="Dựng rough-cut.mp4 từ EDL")
  parser.add_argument("--project", type=Path, required=True)
  parser.add_argument("--output", default="rough-cut.mp4")
  args = parser.parse_args()
  project = args.project.resolve()

  validator = Path(__file__).with_name("validate_edit_plan.py")
  validation = subprocess.run([sys.executable, str(validator), "--project", str(project)])
  if validation.returncode:
    return validation.returncode

  inventory = json.loads((project / "clip-inventory.json").read_text(encoding="utf-8"))
  plan = json.loads((project / "edit-plan.json").read_text(encoding="utf-8"))
  clips = {item["clip_id"]: item for item in inventory["clips"]}
  output_path = project / args.output
  edit_map = []
  output_cursor = 0.0

  try:
    with tempfile.TemporaryDirectory(prefix="raw-mp4-edl-") as temp_name:
      temp_dir = Path(temp_name)
      segment_paths = []
      for index, segment in enumerate(plan["sequence"], start=1):
        source = project / clips[segment["clip_id"]]["path"]
        start = float(segment["source_start"])
        end = float(segment["source_end"])
        duration = end - start
        target = temp_dir / f"segment-{index:04d}.mp4"
        graph, video_map = filter_graph(segment.get("fit", "cover"), duration)
        command = [
          "ffmpeg", "-y", "-v", "error", "-ss", f"{start:.6f}", "-t", f"{duration:.6f}",
          "-i", str(source), "-filter_complex", graph, "-map", video_map, "-map", "[a]",
          "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-g", "30", "-keyint_min", "30",
          "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-movflags", "+faststart", str(target),
        ]
        run(command)
        segment_paths.append(target)
        edit_map.append({
          "segment_id": segment["segment_id"],
          "clip_id": segment["clip_id"],
          "source_start": round(start, 3),
          "source_end": round(end, 3),
          "output_start": round(output_cursor, 3),
          "output_end": round(output_cursor + duration, 3),
        })
        output_cursor += duration

      concat_path = temp_dir / "concat.txt"
      concat_path.write_text("".join(f"file '{path.as_posix()}'\n" for path in segment_paths), encoding="utf-8")
      temp_output = project / f".{output_path.name}.tmp.mp4"
      run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(concat_path), "-c", "copy", "-movflags", "+faststart", str(temp_output)])
      os.replace(temp_output, output_path)
  except RuntimeError as exc:
    print(f"FAIL: {exc}", file=sys.stderr)
    return 1

  (project / "edit-map.json").write_text(
    json.dumps({"version": 1, "duration": round(output_cursor, 3), "segments": edit_map}, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
  )
  print(f"PASS: {len(edit_map)} segment → {output_path} ({output_cursor:.2f}s)")
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
