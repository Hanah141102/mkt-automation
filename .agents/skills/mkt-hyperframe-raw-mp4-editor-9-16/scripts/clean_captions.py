#!/usr/bin/env python3
"""Nhóm word-level transcript thành subtitle; không thay đổi timing nguồn."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


NUMBER_WORDS = {
  "một": "1", "hai": "2", "ba": "3", "bốn": "4", "tư": "4",
  "năm": "5", "sáu": "6", "bảy": "7", "tám": "8", "chín": "9", "mười": "10",
}


def normalize_words(payload: object) -> list[dict]:
  if isinstance(payload, dict):
    payload = payload.get("words") or payload.get("transcript") or payload.get("segments") or []
  if not isinstance(payload, list):
    return []
  words = []
  for item in payload:
    if not isinstance(item, dict):
      continue
    text = str(item.get("text") or item.get("word") or "").strip().replace("�", "")
    if not text:
      continue
    start, end = item.get("start"), item.get("end")
    if isinstance(start, (int, float)) and isinstance(end, (int, float)) and end >= start:
      words.append({"text": text, "start": float(start), "end": float(end)})
  return words


def apply_corrections(text: str, corrections: dict[str, str]) -> str:
  for source, target in corrections.items():
    text = re.sub(rf"(?<!\w){re.escape(source)}(?!\w)", target, text, flags=re.IGNORECASE)
  return re.sub(r"\s+([,.!?;:])", r"\1", re.sub(r"\s+", " ", text)).strip()


def extract_label(text: str) -> tuple[str | None, str]:
  pattern = re.compile(r"^(?:số|thứ)\s+(\d+|một|hai|ba|bốn|tư|năm|sáu|bảy|tám|chín|mười)\b[\s,:-]*", re.IGNORECASE)
  match = pattern.match(text)
  if not match:
    return None, text
  token = match.group(1).lower()
  return f"#{NUMBER_WORDS.get(token, token)}", text[match.end():].strip()


def group_words(words: list[dict], corrections: dict[str, str]) -> list[dict]:
  raw_groups: list[list[dict]] = []
  current: list[dict] = []
  for word in words:
    next_chars = len(" ".join(item["text"] for item in current + [word]))
    current_text = " ".join(item["text"] for item in current)
    marker_prefix = re.match(
      r"^(?:số|thứ)\s+(?:\d+|một|hai|ba|bốn|tư|năm|sáu|bảy|tám|chín|mười)\b",
      current_text,
      flags=re.IGNORECASE,
    )
    max_words = 8 if marker_prefix else 6
    should_break = current and (
      word["start"] - current[-1]["end"] > 0.45
      or len(current) >= max_words
      or next_chars > 34
      or current[-1]["text"].rstrip().endswith((".", "?", "!", ";", ":"))
    )
    if should_break:
      raw_groups.append(current)
      current = []
    current.append(word)
  if current:
    raw_groups.append(current)

  groups = []
  pending_label = None
  for raw in raw_groups:
    text = apply_corrections(" ".join(item["text"] for item in raw), corrections)
    label, cleaned = extract_label(text)
    label = label or pending_label
    if label and not cleaned:
      pending_label = label
      continue
    pending_label = None
    item = {
      "text": cleaned or text,
      "start": round(raw[0]["start"], 3),
      "end": round(raw[-1]["end"], 3),
    }
    if label:
      item["label"] = label
    groups.append(item)
  return groups


def main() -> int:
  parser = argparse.ArgumentParser(description="Tạo caption-groups.json theo preset social-outline")
  parser.add_argument("transcript", type=Path)
  parser.add_argument("--output", type=Path, default=Path("caption-groups.json"))
  parser.add_argument("--corrections", type=Path)
  args = parser.parse_args()
  if not args.transcript.is_file():
    print(f"FAIL: thiếu {args.transcript}", file=sys.stderr)
    return 1
  corrections = {}
  if args.corrections:
    corrections = json.loads(args.corrections.read_text(encoding="utf-8"))
    if not isinstance(corrections, dict):
      print("FAIL: corrections phải là JSON object source→target", file=sys.stderr)
      return 1
  words = normalize_words(json.loads(args.transcript.read_text(encoding="utf-8")))
  if not words:
    print("FAIL: transcript không có word-level timing", file=sys.stderr)
    return 1
  groups = group_words(words, corrections)
  args.output.write_text(json.dumps(groups, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
  print(f"PASS: {len(words)} từ → {len(groups)} caption groups · timing giữ nguyên")
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
