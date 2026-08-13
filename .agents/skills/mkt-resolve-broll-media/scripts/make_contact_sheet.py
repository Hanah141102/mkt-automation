#!/usr/bin/env python3
"""Create an early/middle/late contact sheet from media-manifest.json."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def run(args: list[str]) -> None:
    subprocess.run(args, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--manifest", default="media-manifest.json")
    args = parser.parse_args()

    project = Path(args.project).resolve()
    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = project / manifest_path
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    if not shutil.which("ffmpeg"):
        print("contact-sheet skipped: ffmpeg not found", file=sys.stderr)
        return 0

    assets = [item for item in manifest.get("assets", []) if item.get("type") == "video"]
    if not assets:
        print("contact-sheet skipped: no video assets")
        return 0

    frames_root = project / "broll-review" / "frames"
    frames_root.mkdir(parents=True, exist_ok=True)
    fonts = [
        Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    ]
    font = next((candidate for candidate in fonts if candidate.exists()), None)

    modes = (
        ("source", "file", "duration", (0.10, 0.50, 0.90), project / "broll-source-contact-sheet.jpg"),
        ("trimmed", "trimmed", None, (0.15, 0.50, 0.85), project / "broll-contact-sheet.jpg"),
    )
    for mode, path_key, duration_key, ratios, output in modes:
        mode_dir = frames_root / mode
        mode_dir.mkdir(parents=True, exist_ok=True)
        frames: list[Path] = []
        for item in assets:
            clip = project / item[path_key]
            duration = float(item.get(duration_key) if duration_key else item.get("placement", {}).get("duration_s") or item.get("bestSegment", {}).get("dur") or 3)
            for label, ratio in zip(("early", "middle", "late"), ratios):
                frame = mode_dir / f"{item['assignedBeat']}--{item['assetId']}--{mode}-{label}.jpg"
                run([
                    "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
                    "-ss", f"{max(0, duration * ratio):.3f}", "-i", str(clip),
                    "-frames:v", "1", "-vf", "scale=270:-2", str(frame)
                ])
                frames.append(frame)

        if not shutil.which("montage"):
            print(f"{mode} contact-sheet frames -> {mode_dir}")
            continue
        montage = ["montage", *map(str, frames)]
        if font:
            montage.extend(["-font", str(font), "-label", "%t"])
        montage.extend([
            "-tile", "3x", "-geometry", "270x480+8+24",
            "-background", "#101418", "-fill", "white", str(output)
        ])
        run(montage)
        print(f"{mode} contact-sheet -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
