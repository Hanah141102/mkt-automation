#!/usr/bin/env python3
"""Inject caption-groups.json vào template mà không hand-edit JS timing."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def main() -> int:
  parser = argparse.ArgumentParser(description="Inject subtitle social-outline")
  parser.add_argument("html", type=Path)
  parser.add_argument("groups", type=Path)
  args = parser.parse_args()
  if not args.html.is_file() or not args.groups.is_file():
    print("FAIL: thiếu captions HTML hoặc caption-groups JSON", file=sys.stderr)
    return 1
  groups = json.loads(args.groups.read_text(encoding="utf-8"))
  if not isinstance(groups, list) or not groups:
    print("FAIL: caption groups phải là mảng không rỗng", file=sys.stderr)
    return 1
  for index, group in enumerate(groups):
    if not all(key in group for key in ("text", "start", "end")) or float(group["end"]) <= float(group["start"]):
      print(f"FAIL: group #{index + 1} không hợp lệ", file=sys.stderr)
      return 1
  html = args.html.read_text(encoding="utf-8")
  array_literal = "const CAPTION_GROUPS = " + json.dumps(groups, ensure_ascii=False, indent=2) + ";"
  pattern = re.compile(r"const CAPTION_GROUPS\s*=\s*\[.*?\];", re.DOTALL)
  if not pattern.search(html):
    print("FAIL: không tìm thấy CAPTION_GROUPS trong template", file=sys.stderr)
    return 1
  html = pattern.sub(array_literal, html, count=1)
  total = max(float(item["end"]) for item in groups)
  html = re.sub(
    r'(<div id="captions"[^>]*data-duration=")[^"]+("[^>]*>)',
    rf'\g<1>{total:.3f}\2',
    html,
    count=1,
  )
  args.html.write_text(html, encoding="utf-8")
  print(f"PASS: inject {len(groups)} groups → {args.html} · duration {total:.3f}s")
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
