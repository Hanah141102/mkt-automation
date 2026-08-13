#!/usr/bin/env python3
"""Convert MP3 to AIFF (PCM 16-bit, 44100 Hz, mono) for HeyGen upload.

Usage:
    python3 mp3_to_aiff.py --in voiceover.mp3 --out voiceover.aiff

Uses ffmpeg via subprocess. No third-party deps.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="src", required=True, help="Input MP3 path")
    parser.add_argument("--out", dest="dst", required=True, help="Output AIFF path")
    parser.add_argument("--sample-rate", type=int, default=44100)
    parser.add_argument("--channels", type=int, default=1, help="1=mono, 2=stereo")
    args = parser.parse_args()

    src = Path(args.src)
    dst = Path(args.dst)
    if not src.exists():
        print(json.dumps({"ok": False, "error": f"input not found: {src}"}))
        return 1
    dst.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "ffmpeg", "-y", "-i", str(src),
        "-acodec", "pcm_s16be",
        "-ar", str(args.sample_rate),
        "-ac", str(args.channels),
        "-f", "aiff",
        str(dst),
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, timeout=60)
    except subprocess.CalledProcessError as e:
        print(json.dumps({"ok": False, "error": e.stderr.decode() if e.stderr else "ffmpeg failed"}))
        return 1
    except FileNotFoundError:
        print(json.dumps({"ok": False, "error": "ffmpeg not found in PATH"}))
        return 1

    size = dst.stat().st_size
    print(json.dumps({"ok": True, "src": str(src), "dst": str(dst), "bytes": size}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
