#!/usr/bin/env python3
"""Fail-fast check that beat headings did not enter the spoken alignment.

Usage:
  python validate_tts_alignment.py --script <OUT>/script.md \
      --alignment <OUT>/audio/alignment.json

The script may use Markdown headings to organize beats. Those headings are
metadata, not narration. This check compares heading phrases against the
alignment text and fails only when a heading appears in the spoken text but
does not appear in the non-heading body. Run it before cutting avatar audio or
submitting anything to HeyGen.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


WORD_RE = re.compile(r"[^\wÀ-ỹ]+", re.UNICODE)
HEADING_RE = re.compile(r"^[ \t]*#{1,6}(?:[ \t]+(.*?))?[ \t]*$", re.MULTILINE)


def tokens(text: str) -> list[str]:
    return [part for part in WORD_RE.sub(" ", text).lower().split() if part]


def contains_sequence(haystack: list[str], needle: list[str]) -> bool:
    if not needle or len(needle) > len(haystack):
        return False
    width = len(needle)
    return any(haystack[i:i + width] == needle for i in range(len(haystack) - width + 1))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", required=True, help="Markdown source script")
    ap.add_argument("--alignment", required=True, help="TTS alignment JSON")
    args = ap.parse_args()

    script_path = Path(args.script)
    alignment_path = Path(args.alignment)
    raw = script_path.read_text(encoding="utf-8")
    alignment = json.loads(alignment_path.read_text(encoding="utf-8"))

    headings = [match.group(1).strip() for match in HEADING_RE.finditer(raw) if match.group(1)]
    if not headings:
        print("[tts-check] PASS: script has no Markdown headings")
        return 0

    body = HEADING_RE.sub("", raw)
    body_words = tokens(body)
    spoken_words = tokens(str(alignment.get("text", "")))
    leaked: list[str] = []
    for heading in headings:
        heading_words = tokens(heading)
        if contains_sequence(spoken_words, heading_words) and not contains_sequence(body_words, heading_words):
            leaked.append(heading)

    if leaked:
        print("[tts-check] FAIL: heading text found in spoken alignment:", file=sys.stderr)
        for heading in leaked:
            print(f"  - {heading}", file=sys.stderr)
        print("[tts-check] Stop before cut_avatar_audio.py / HeyGen.", file=sys.stderr)
        return 1

    print(f"[tts-check] PASS: {len(headings)} heading(s) are absent from spoken alignment")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
