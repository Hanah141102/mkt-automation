#!/usr/bin/env python3
"""Create a labeled contact sheet from beat midpoints in a rendered draft."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def run(command: list[str]) -> None:
    subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--video", required=True)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--columns", type=int, default=4)
    args = parser.parse_args()

    if not shutil.which("ffmpeg"):
        print("ERROR: ffmpeg not found", file=sys.stderr)
        return 2
    if not shutil.which("montage"):
        print("ERROR: ImageMagick montage not found", file=sys.stderr)
        return 2

    video = Path(args.video).expanduser().resolve()
    plan_path = Path(args.plan).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    if not video.is_file():
        print(f"ERROR: video not found: {video}", file=sys.stderr)
        return 2

    try:
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read plan: {exc}", file=sys.stderr)
        return 2

    beats = plan.get("beats", [])
    if not beats:
        print("ERROR: plan has no beats", file=sys.stderr)
        return 2

    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="video-contact-sheet-") as temp_dir:
        frames: list[Path] = []
        for index, beat in enumerate(beats, start=1):
            start = float(beat["start_s"])
            end = float(beat["end_s"])
            midpoint = start + (end - start) * 0.5
            beat_id = str(beat.get("id", f"b{index:03d}"))
            mode = str(beat.get("mode", "UNKNOWN"))
            frame = Path(temp_dir) / f"{index:03d}-{beat_id}-{mode}-{midpoint:.2f}s.jpg"
            run([
                "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                "-ss", f"{midpoint:.3f}", "-i", str(video),
                "-frames:v", "1", "-vf", "scale=480:-2", str(frame),
            ])
            frames.append(frame)

        fonts = [
            Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        ]
        font = next((candidate for candidate in fonts if candidate.is_file()), None)
        command = ["montage", *map(str, frames)]
        if font:
            command.extend(["-font", str(font)])
        command.extend(["-set", "label", "%t"])
        command.extend([
            "-tile", f"{max(1, args.columns)}x",
            "-geometry", "480x270+10+32",
            "-background", "#0b1020",
            "-fill", "white",
            str(output),
        ])
        run(command)

    print(f"contact sheet -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
