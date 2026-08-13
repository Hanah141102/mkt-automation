#!/usr/bin/env python3
"""Sync audio duration across all hyperframes project files.

Read audio duration from MP3 (ffprobe), then update:
  - index.html: any `data-duration="X"` attributes
  - audio/alignment.json: top-level "duration" field
  - All scene-*.html files: any `data-duration` attributes, GSAP timeline
    durations, and JS `DURATION` constants

Usage:
    python3 sync_audio_duration.py --audio voiceover.mp3 --project-root .
    python3 sync_audio_duration.py --audio voiceover.mp3 --project-root . --old 10.0

By default, --old is auto-detected from the first `data-duration="N.N"` found
in the project (most likely the audio clip in index.html). The --new value
defaults to the measured audio duration (rounded to 1 decimal).

Exits 0 on success, 1 if no changes applied or audio missing.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


def get_audio_duration_seconds(path: Path) -> float:
    out = subprocess.check_output(
        [
            "ffprobe", "-v", "quiet", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(path),
        ],
        stderr=subprocess.DEVNULL, timeout=10,
    )
    return float(out.decode().strip())


def find_files(project_root: Path) -> list[Path]:
    files = []
    idx = project_root / "index.html"
    if idx.exists():
        files.append(idx)
    align = project_root / "audio" / "alignment.json"
    if align.exists():
        files.append(align)
    for f in sorted(project_root.rglob("scene-*.html")):
        files.append(f)
    return files


def patch_text(text: str, old: float, new: float) -> tuple[str, int]:
    """Replace `old` with `new` in known contexts. Returns (new_text, n_changes)."""
    n = 0
    old_str = str(old)
    new_str = str(new)

    # 1. data-duration="OLD" — replace with NEW
    def repl_attr(m):
        nonlocal n
        val = m.group(1)
        if val == old_str:
            n += 1
            return f'data-duration="{new_str}"'
        return m.group(0)
    text = re.sub(r'data-duration="([\d.]+)"', repl_attr, text)

    # 2. JSON "duration": OLD
    def repl_json(m):
        nonlocal n
        val = m.group(2)
        if val == old_str:
            n += 1
            return f'{m.group(1)}{new_str}'
        return m.group(0)
    text = re.sub(r'("duration"\s*:\s*)([\d.]+)', repl_json, text)

    # 3. JS const/let/var DURATION = OLD;
    def repl_const(m):
        nonlocal n
        val = m.group(2)
        if val == old_str:
            n += 1
            return f'{m.group(1)}{new_str}'
        return m.group(0)
    text = re.sub(
        r'((?:const|let|var)\s+DURATION\s*=\s*)([\d.]+)',
        repl_const, text,
    )

    # 4. Standalone number `OLD` (word-boundary) — covers GSAP from/to/duration
    #    values like `tl.to(..., { duration: 6.73 })` or `tl.call(..., 6.73)`.
    #    Only replace if exact match to avoid touching other numbers like 6.15.
    def repl_num(m):
        nonlocal n
        val = m.group(0)
        if val == old_str:
            n += 1
            return new_str
        return m.group(0)
    text = re.sub(r'\b\d+\.\d+\b', repl_num, text)

    return text, n


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio", required=True, help="MP3 file to measure duration from")
    parser.add_argument("--project-root", default=".", help="Project root containing index.html / scenes")
    parser.add_argument("--old", type=float, help="Override old duration (else auto-detect)")
    parser.add_argument("--new", type=float, help="Override new duration (else use measured audio)")
    args = parser.parse_args()

    audio = Path(args.audio)
    if not audio.exists():
        print(json.dumps({"ok": False, "error": f"audio not found: {audio}"}))
        return 1

    measured = get_audio_duration_seconds(audio)
    new = args.new if args.new is not None else round(measured, 1)

    root = Path(args.project_root)
    files = find_files(root)
    if not files:
        print(json.dumps({"ok": False, "error": f"no project files found in {root}"}))
        return 1

    # Auto-detect old duration if not provided
    old = args.old
    if old is None:
        for f in files:
            text = f.read_text(encoding="utf-8")
            m = re.search(r'data-duration="([\d.]+)"', text)
            if m:
                old = float(m.group(1))
                break
        if old is None:
            print(json.dumps({"ok": False, "error": "could not auto-detect old duration; pass --old"}))
            return 1

    total_changes = 0
    updated_files = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        new_text, changes = patch_text(text, old, new)
        if changes > 0 and new_text != text:
            f.write_text(new_text, encoding="utf-8")
            updated_files.append(str(f))
            total_changes += changes

    result = {
        "ok": True,
        "audio": str(audio),
        "audio_duration_s": measured,
        "old_duration": old,
        "new_duration": new,
        "files_updated": updated_files,
        "total_changes": total_changes,
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
