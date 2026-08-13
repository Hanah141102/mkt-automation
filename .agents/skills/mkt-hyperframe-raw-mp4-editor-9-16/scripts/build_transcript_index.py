#!/usr/bin/env python3
"""Gộp transcript từng clip thành index JSON và Markdown có source time."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def normalize_words(payload: object) -> list[dict]:
  if isinstance(payload, dict):
    payload = payload.get("words") or payload.get("transcript") or payload.get("segments") or []
  if not isinstance(payload, list):
    return []
  words = []
  for item in payload:
    if not isinstance(item, dict):
      continue
    text = str(item.get("text") or item.get("word") or "").strip()
    start = item.get("start")
    end = item.get("end")
    if text and isinstance(start, (int, float)) and isinstance(end, (int, float)):
      words.append({"text": text, "start": float(start), "end": float(end)})
  return words


def phrase_blocks(words: list[dict], gap: float = 0.8, max_words: int = 22) -> list[dict]:
  blocks = []
  current = []
  for word in words:
    should_break = current and (
      word["start"] - current[-1]["end"] > gap
      or len(current) >= max_words
      or current[-1]["text"].rstrip().endswith((".", "?", "!"))
    )
    if should_break:
      blocks.append(current)
      current = []
    current.append(word)
  if current:
    blocks.append(current)
  return [{
    "start": round(block[0]["start"], 3),
    "end": round(block[-1]["end"], 3),
    "text": " ".join(item["text"] for item in block).strip(),
  } for block in blocks]


def main() -> int:
  parser = argparse.ArgumentParser(description="Tạo transcript-index.json và TRANSCRIPT-NGUON.md")
  parser.add_argument("--project", type=Path, required=True)
  args = parser.parse_args()
  project = args.project.resolve()
  inventory_path = project / "clip-inventory.json"
  if not inventory_path.is_file():
    print("FAIL: thiếu clip-inventory.json", file=sys.stderr)
    return 1
  inventory = json.loads(inventory_path.read_text(encoding="utf-8"))

  indexed = []
  markdown = ["# Transcript nguồn", "", "> Timing dưới đây là source time của từng MP4, chưa phải timeline final.", ""]
  missing = []
  for clip in inventory.get("clips", []):
    transcript_path = project / "transcripts" / clip["clip_id"] / "transcript.json"
    if not transcript_path.is_file():
      missing.append(str(transcript_path))
      continue
    payload = json.loads(transcript_path.read_text(encoding="utf-8"))
    words = normalize_words(payload)
    blocks = phrase_blocks(words)
    indexed.append({
      "clip_id": clip["clip_id"],
      "filename": clip["filename"],
      "duration": clip["duration"],
      "words": words,
      "blocks": blocks,
      "text": " ".join(item["text"] for item in words).strip(),
    })
    markdown.extend([
      f'## {clip["clip_id"]} — {clip["filename"]}',
      "",
      f'- Duration: {clip["duration"]:.3f}s',
      "",
    ])
    for block in blocks:
      markdown.append(f'`{block["start"]:.3f}–{block["end"]:.3f}` {block["text"]}')
    markdown.append("")

  if missing:
    for path in missing:
      print(f"FAIL: thiếu {path}", file=sys.stderr)
    return 1
  (project / "transcript-index.json").write_text(
    json.dumps({"version": 1, "clips": indexed}, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
  )
  (project / "TRANSCRIPT-NGUON.md").write_text("\n".join(markdown), encoding="utf-8")
  print(f"PASS: {len(indexed)} transcript → {project / 'TRANSCRIPT-NGUON.md'}")
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
