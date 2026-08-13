#!/usr/bin/env python3
"""Validate that an input file contains spoken narration only."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ANNOTATION_PREFIX = re.compile(
    r"^\s*(?:visual|visuals|b-roll|broll|on[- ]screen|text on screen|sfx|sound fx|"
    r"music|scene|shot|camera|cảnh|hình ảnh|hình minh họa|chữ trên màn hình|"
    r"âm thanh|nhạc nền|ghi chú|note|voiceover|voice-over|vo|narrator|narration|"
    r"lời dẫn|lời thoại)\s*:",
    re.IGNORECASE,
)
HEADING = re.compile(r"^\s*#{1,6}(?:\s+.*)?$")
FULL_BRACKET_NOTE = re.compile(r"^\s*(?:\[[^\]]+\]|\([^\)]+\))\s*$")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")


def find_violations(text: str) -> list[tuple[int, str, str]]:
    violations: list[tuple[int, str, str]] = []
    for line_no, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        if HEADING.match(line):
            violations.append((line_no, "heading", line))
        elif ANNOTATION_PREFIX.match(line):
            violations.append((line_no, "production note", line))
        elif FULL_BRACKET_NOTE.match(line):
            violations.append((line_no, "bracketed note", line))
        elif TABLE_ROW.match(line):
            violations.append((line_no, "table row", line))
    return violations


def validate_or_report(text: str, source: str = "script") -> bool:
    violations = find_violations(text)
    if not violations:
        return True
    print(f"[spoken-script] FAIL: {source} must contain spoken narration only", file=sys.stderr)
    for line_no, kind, line in violations[:20]:
        print(f"  line {line_no} ({kind}): {line}", file=sys.stderr)
    if len(violations) > 20:
        print(f"  ... and {len(violations) - 20} more line(s)", file=sys.stderr)
    print("[spoken-script] Remove headings/visual directions/SFX notes and retry; no TTS request was made.", file=sys.stderr)
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate spoken-only TTS input")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--text")
    src.add_argument("--text-file")
    args = ap.parse_args()
    text = args.text if args.text is not None else Path(args.text_file).read_text(encoding="utf-8")
    return 0 if validate_or_report(text, args.text_file or "inline text") else 2


if __name__ == "__main__":
    raise SystemExit(main())
