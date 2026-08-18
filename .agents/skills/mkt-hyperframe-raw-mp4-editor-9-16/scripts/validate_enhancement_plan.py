#!/usr/bin/env python3
"""Fail-fast gate cho Pexels, HyperFrames, SFX và text effect."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


def overlaps(left: tuple[float, float], right: tuple[float, float], epsilon: float = 0.02) -> bool:
  return min(left[1], right[1]) - max(left[0], right[0]) > epsilon


def interval(item: dict) -> tuple[float, float]:
  return float(item["start"]), float(item["end"])


def merge_intervals(intervals: list[tuple[float, float]]) -> list[tuple[float, float]]:
  merged: list[list[float]] = []
  for start, end in sorted(intervals):
    if end <= start:
      continue
    if not merged or start > merged[-1][1] + 1e-9:
      merged.append([start, end])
    else:
      merged[-1][1] = max(merged[-1][1], end)
  return [(start, end) for start, end in merged]


def covered_duration(intervals: list[tuple[float, float]]) -> float:
  return sum(end - start for start, end in merge_intervals(intervals))


def main() -> int:
  parser = argparse.ArgumentParser(description="Validate enhancement-plan.json")
  parser.add_argument("--project", type=Path, required=True)
  args = parser.parse_args()
  path = args.project.resolve() / "enhancement-plan.json"
  try:
    plan = json.loads(path.read_text(encoding="utf-8"))
  except FileNotFoundError:
    print(f"FAIL: thiếu {path}", file=sys.stderr)
    return 1
  except json.JSONDecodeError as exc:
    print(f"FAIL JSON: {exc}", file=sys.stderr)
    return 1

  errors = []
  try:
    total = float(plan["total_duration"])
  except (KeyError, TypeError, ValueError):
    print("FAIL: total_duration không hợp lệ", file=sys.stderr)
    return 1
  if total <= 0:
    errors.append("total_duration phải > 0")

  face_moments = []
  for index, item in enumerate(plan.get("face_moments", []), start=1):
    try:
      bounds = interval(item)
      if bounds[0] < 0 or bounds[1] <= bounds[0] or bounds[1] > total + 0.05:
        errors.append(f"face_moments[{index}] bounds không hợp lệ")
      face_moments.append(bounds)
    except (KeyError, TypeError, ValueError):
      errors.append(f"face_moments[{index}] thiếu start/end")
  if not any(start <= 0.02 and end >= 3.0 for start, end in face_moments):
    errors.append("face_moments phải bảo vệ full face 0–3s")

  broll_intervals = []
  broll_ids = set()
  for index, item in enumerate(plan.get("broll", []), start=1):
    prefix = f"broll[{index}]"
    try:
      bounds = interval(item)
    except (KeyError, TypeError, ValueError):
      errors.append(f"{prefix}: thiếu start/end")
      continue
    item_id = str(item.get("id") or "")
    if not item_id or item_id in broll_ids:
      errors.append(f"{prefix}: id thiếu hoặc trùng")
    broll_ids.add(item_id)
    if bounds[0] < 3.0 or bounds[1] > total + 0.05 or not 0.8 <= bounds[1] - bounds[0] <= 15.0:
      errors.append(f"{prefix}: phải nằm sau 3s, dài 0.8–15.0s và trong timeline")
    for field in ("intent_vi", "query_en", "noun", "verb", "purpose"):
      if not str(item.get(field) or "").strip():
        errors.append(f"{prefix}: thiếu {field}")
    if any(overlaps(bounds, face) for face in face_moments):
      errors.append(f"{prefix}: đè face moment bắt buộc")
    if any(overlaps(bounds, previous) for previous in broll_intervals):
      errors.append(f"{prefix}: chồng B-roll khác")
    broll_intervals.append(bounds)

  hyperframe_intervals = []
  for index, item in enumerate(plan.get("hyperframes", []), start=1):
    prefix = f"hyperframes[{index}]"
    try:
      bounds = interval(item)
    except (KeyError, TypeError, ValueError):
      errors.append(f"{prefix}: thiếu start/end")
      continue
    if bounds[0] < 3.0 or bounds[1] > total + 0.05 or bounds[1] <= bounds[0]:
      errors.append(f"{prefix}: bounds không hợp lệ hoặc đè 3s hook")
    for field in ("claim", "source_object", "start_state", "transformation", "end_state", "spoken_anchor"):
      if not str(item.get(field) or "").strip():
        errors.append(f"{prefix}: thiếu {field}")
    if any(overlaps(bounds, face) for face in face_moments):
      errors.append(f"{prefix}: đè face moment bắt buộc")
    if any(overlaps(bounds, broll) for broll in broll_intervals):
      errors.append(f"{prefix}: chồng B-roll")
    hyperframe_intervals.append(bounds)

  mix = plan.get("visual_mix", {})
  approved_override = bool(mix.get("approved_override", False))
  try:
    max_hyperframes_ratio = float(mix.get("max_hyperframes_ratio", 0.20))
    min_real_media_ratio = float(mix.get("min_real_media_ratio", 0.30))
  except (TypeError, ValueError):
    errors.append("visual_mix ratio không hợp lệ")
    max_hyperframes_ratio, min_real_media_ratio = 0.20, 0.30
  real_media_ratio = covered_duration(broll_intervals) / total
  hyperframes_ratio = covered_duration(hyperframe_intervals) / total
  if approved_override:
    if not str(mix.get("override_reason") or "").strip():
      errors.append("visual_mix override thiếu override_reason")
  else:
    if hyperframes_ratio > max_hyperframes_ratio + 0.001:
      errors.append(
        f"HyperFrames {hyperframes_ratio:.1%} vượt trần {max_hyperframes_ratio:.0%}; "
        "ưu tiên media user/Pexels hoặc ghi approved_override"
      )
    if real_media_ratio + 0.001 < min_real_media_ratio:
      errors.append(
        f"Real media {real_media_ratio:.1%} dưới mức {min_real_media_ratio:.0%}; "
        "bổ sung media user/Pexels hoặc ghi approved_override"
      )

  sfx = sorted(plan.get("sfx", []), key=lambda item: float(item.get("time", -1)))
  max_hits = max(1, math.ceil(total / 60 * 6))
  if len(sfx) > max_hits:
    errors.append(f"SFX có {len(sfx)} hit; tối đa {max_hits} hit cho {total:.1f}s")
  previous_time = None
  for index, item in enumerate(sfx, start=1):
    prefix = f"sfx[{index}]"
    try:
      timestamp = float(item["time"])
      volume = float(item["volume"])
    except (KeyError, TypeError, ValueError):
      errors.append(f"{prefix}: time/volume không hợp lệ")
      continue
    if not 0 <= timestamp <= total:
      errors.append(f"{prefix}: time ngoài timeline")
    if not 0.12 <= volume <= 0.30:
      errors.append(f"{prefix}: volume phải trong 0.12–0.30")
    if previous_time is not None and timestamp - previous_time < 1.25:
      errors.append(f"{prefix}: cách SFX trước dưới 1.25s")
    previous_time = timestamp
    for field in ("cue", "file", "reason"):
      if not str(item.get(field) or "").strip():
        errors.append(f"{prefix}: thiếu {field}")

  for index, item in enumerate(plan.get("text_effects", []), start=1):
    prefix = f"text_effects[{index}]"
    try:
      bounds = interval(item)
    except (KeyError, TypeError, ValueError):
      errors.append(f"{prefix}: thiếu start/end")
      continue
    text = str(item.get("text") or "").strip()
    if bounds[0] < 0 or bounds[1] <= bounds[0] or bounds[1] > total + 0.05:
      errors.append(f"{prefix}: bounds không hợp lệ")
    if not 1 <= len(text.split()) <= 6:
      errors.append(f"{prefix}: text phải 1–6 từ")
    for field in ("effect", "spoken_anchor", "reason"):
      if not str(item.get(field) or "").strip():
        errors.append(f"{prefix}: thiếu {field}")

  status = "PASS" if not errors else "FAIL"
  print(
    f"{status}: {len(plan.get('broll', []))} B-roll · "
    f"{len(plan.get('hyperframes', []))} HyperFrames · "
    f"{len(sfx)} SFX · {len(plan.get('text_effects', []))} text effects · "
    f"real media {real_media_ratio:.1%} · HyperFrames {hyperframes_ratio:.1%}"
  )
  for error in errors:
    print(f"- {error}")
  return 0 if not errors else 1


if __name__ == "__main__":
  raise SystemExit(main())
