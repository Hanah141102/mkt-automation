#!/usr/bin/env python3
"""Mix deterministic procedural sound effects into a rendered video."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


SOURCES = {
    "whoosh": "anoisesrc=color=pink:sample_rate=48000:duration=0.36:amplitude=0.65,highpass=f=500,lowpass=f=6500,volume=2,afade=t=in:st=0:d=0.04,afade=t=out:st=0.12:d=0.24",
    "pop": "sine=frequency=620:sample_rate=48000:duration=0.14,volume=8,afade=t=out:st=0.025:d=0.115",
    "click": "sine=frequency=1150:sample_rate=48000:duration=0.075,volume=10,afade=t=out:st=0.01:d=0.065",
    "tick": "sine=frequency=880:sample_rate=48000:duration=0.11,volume=8,afade=t=out:st=0.02:d=0.09",
    "impact": "sine=frequency=150:sample_rate=48000:duration=0.28,volume=8,afade=t=out:st=0.04:d=0.24",
    "warning": "sine=frequency=420:sample_rate=48000:duration=0.22,volume=7,tremolo=f=9:d=0.75,afade=t=out:st=0.08:d=0.14",
    "success": "sine=frequency=1040:sample_rate=48000:duration=0.34,volume=7,afade=t=in:st=0:d=0.015,afade=t=out:st=0.08:d=0.26",
    "shimmer": "sine=frequency=1480:sample_rate=48000:duration=0.24,volume=6,afade=t=in:st=0:d=0.02,afade=t=out:st=0.06:d=0.18",
}

DEFAULT_GAIN_DB = {
    "whoosh": -20.0,
    "pop": -18.0,
    "click": -19.0,
    "tick": -18.0,
    "impact": -17.0,
    "warning": -20.0,
    "success": -20.0,
    "shimmer": -22.0,
}


def probe_duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def load_cues(plan_path: Path, duration: float) -> list[dict[str, Any]]:
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    master_gain_db = plan.get("master_gain_db", 0.0)
    if not isinstance(master_gain_db, (int, float)) or isinstance(master_gain_db, bool):
        raise ValueError("plan.master_gain_db must be a number")
    cues = plan.get("cues")
    if not isinstance(cues, list) or not cues:
        raise ValueError("plan.cues must be a non-empty array")

    checked: list[dict[str, Any]] = []
    for index, cue in enumerate(cues):
        if not isinstance(cue, dict):
            raise ValueError(f"cue[{index}] must be an object")
        cue_type = cue.get("type")
        if cue_type not in SOURCES:
            raise ValueError(f"cue[{index}] has unsupported type {cue_type!r}")
        time_s = cue.get("time_s")
        if not isinstance(time_s, (int, float)) or isinstance(time_s, bool):
            raise ValueError(f"cue[{index}].time_s must be a number")
        if time_s < 0 or time_s >= duration:
            raise ValueError(f"cue[{index}] at {time_s}s falls outside video duration {duration:.3f}s")
        gain_db = cue.get("gain_db", DEFAULT_GAIN_DB[cue_type])
        if not isinstance(gain_db, (int, float)) or isinstance(gain_db, bool):
            raise ValueError(f"cue[{index}].gain_db must be a number")
        gain_db = float(gain_db) + float(master_gain_db)
        if gain_db > -8:
            raise ValueError(f"cue[{index}].gain_db must be <= -8 dB to protect the voice")
        checked.append({**cue, "time_s": float(time_s), "gain_db": gain_db})
    return sorted(checked, key=lambda item: item["time_s"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--video", required=True, help="Rendered MP4 containing the approved voice")
    parser.add_argument("--plan", required=True, help="JSON sound-effect cue plan")
    parser.add_argument("--output", required=True, help="Output MP4")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print cues without rendering")
    args = parser.parse_args()

    for binary in ("ffmpeg", "ffprobe"):
        if not shutil.which(binary):
            print(f"ERROR: {binary} not found", file=sys.stderr)
            return 2

    video = Path(args.video).expanduser().resolve()
    plan = Path(args.plan).expanduser().resolve()
    output = Path(args.output).expanduser().resolve()
    if not video.is_file() or not plan.is_file():
        print("ERROR: video or plan not found", file=sys.stderr)
        return 2

    try:
        duration = probe_duration(video)
        cues = load_cues(plan, duration)
    except (OSError, json.JSONDecodeError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"validated {len(cues)} SFX cue(s) across {duration:.3f}s")
    for cue in cues:
        print(f"  {cue['time_s']:7.2f}s  {cue['type']:<8} {cue['gain_db']:5.1f} dB  {cue.get('label', '')}")
    if args.dry_run:
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    command = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(video)]
    for cue in cues:
        command.extend(["-f", "lavfi", "-i", SOURCES[cue["type"]]])

    filters = ["[0:a]aformat=sample_rates=48000:channel_layouts=stereo[voice]"]
    mix_inputs = ["[voice]"]
    for index, cue in enumerate(cues, start=1):
        delay_ms = round(cue["time_s"] * 1000)
        label = f"sfx{index:03d}"
        filters.append(
            f"[{index}:a]aformat=sample_rates=48000:channel_layouts=stereo,"
            f"volume={cue['gain_db']:.2f}dB,adelay={delay_ms}:all=1[{label}]"
        )
        mix_inputs.append(f"[{label}]")
    filters.append(
        "".join(mix_inputs)
        + f"amix=inputs={len(mix_inputs)}:duration=first:dropout_transition=0:normalize=0,"
        + "alimiter=limit=0.88:attack=5:release=50:level=false[aout]"
    )

    command.extend([
        "-filter_complex", ";".join(filters),
        "-map", "0:v:0", "-map", "[aout]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart", str(output),
    ])
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: ffmpeg failed with exit code {exc.returncode}", file=sys.stderr)
        return exc.returncode

    print(f"video with SFX -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
