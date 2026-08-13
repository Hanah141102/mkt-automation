#!/usr/bin/env python3
"""Fail-fast validator cho edit-plan.json."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ALLOWED_FITS = {"cover", "contain-blur"}
ALLOWED_REASONS = {"silence", "filler", "false-start", "mistake", "duplicate", "off-topic", "technical", "other"}


def main() -> int:
  parser = argparse.ArgumentParser(description="Kiểm tra bounds, ID và overlap trong edit-plan.json")
  parser.add_argument("--project", type=Path, required=True)
  args = parser.parse_args()
  project = args.project.resolve()

  try:
    inventory = json.loads((project / "clip-inventory.json").read_text(encoding="utf-8"))
    plan = json.loads((project / "edit-plan.json").read_text(encoding="utf-8"))
  except FileNotFoundError as exc:
    print(f"FAIL: thiếu {exc.filename}", file=sys.stderr)
    return 1
  except json.JSONDecodeError as exc:
    print(f"FAIL JSON: {exc}", file=sys.stderr)
    return 1

  clips = {item["clip_id"]: item for item in inventory.get("clips", [])}
  errors = []
  segment_ids = set()
  intervals: dict[str, list[tuple[float, float, str]]] = {}
  kept = 0.0

  sequence = plan.get("sequence")
  if not isinstance(sequence, list) or not sequence:
    errors.append("sequence phải là mảng không rỗng")
    sequence = []
  for index, segment in enumerate(sequence, start=1):
    prefix = f"sequence[{index}]"
    segment_id = str(segment.get("segment_id") or "")
    clip_id = str(segment.get("clip_id") or "")
    if not segment_id or segment_id in segment_ids:
      errors.append(f"{prefix}: segment_id thiếu hoặc trùng")
    segment_ids.add(segment_id)
    if clip_id not in clips:
      errors.append(f"{prefix}: clip_id không tồn tại: {clip_id}")
      continue
    try:
      start = float(segment["source_start"])
      end = float(segment["source_end"])
    except (KeyError, TypeError, ValueError):
      errors.append(f"{prefix}: source_start/source_end không hợp lệ")
      continue
    duration = float(clips[clip_id]["duration"])
    if start < 0 or end > duration + 0.03 or end - start < 0.08:
      errors.append(f"{prefix}: bounds {start:.3f}–{end:.3f} ngoài clip 0–{duration:.3f}")
    fit = segment.get("fit", "cover")
    if fit not in ALLOWED_FITS:
      errors.append(f"{prefix}: fit phải là cover hoặc contain-blur")
    if not str(segment.get("reason") or "").strip():
      errors.append(f"{prefix}: thiếu reason")
    kept += max(0.0, end - start)
    intervals.setdefault(clip_id, []).append((start, end, segment_id))

  for clip_id, items in intervals.items():
    ordered = sorted(items)
    for left, right in zip(ordered, ordered[1:]):
      if right[0] < left[1] - 0.03:
        errors.append(f"{clip_id}: source overlap giữa {left[2]} và {right[2]}")

  for index, removed in enumerate(plan.get("removed", []), start=1):
    prefix = f"removed[{index}]"
    clip_id = str(removed.get("clip_id") or "")
    if clip_id not in clips:
      errors.append(f"{prefix}: clip_id không tồn tại")
      continue
    try:
      start = float(removed["source_start"])
      end = float(removed["source_end"])
    except (KeyError, TypeError, ValueError):
      errors.append(f"{prefix}: bounds không hợp lệ")
      continue
    if start < 0 or end <= start or end > float(clips[clip_id]["duration"]) + 0.03:
      errors.append(f"{prefix}: bounds ngoài clip")
    if removed.get("reason_code") not in ALLOWED_REASONS:
      errors.append(f"{prefix}: reason_code không hợp lệ")
    if not str(removed.get("evidence") or "").strip():
      errors.append(f"{prefix}: thiếu evidence")

  raw_total = float(inventory.get("raw_total_duration") or 0)
  status = "PASS" if not errors else "FAIL"
  print(f"{status}: {len(sequence)} segment · giữ {kept:.2f}s / raw {raw_total:.2f}s")
  if plan.get("open_issues"):
    print(f"WARN: còn {len(plan['open_issues'])} open issue cần nêu trong EDIT-REVIEW.md")
  for error in errors:
    print(f"- {error}")
  return 0 if not errors else 1


if __name__ == "__main__":
  raise SystemExit(main())
