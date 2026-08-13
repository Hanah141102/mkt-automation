#!/usr/bin/env python3
"""Fail-fast gate for the LITE video's approved Pexels/HyperFrames scene mix."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


EPSILON = 0.05


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


def duration(intervals: list[tuple[float, float]]) -> float:
  return sum(end - start for start, end in intervals)


def overlap_duration(
  left: list[tuple[float, float]], right: list[tuple[float, float]]
) -> float:
  total = 0.0
  for left_start, left_end in left:
    for right_start, right_end in right:
      total += max(0.0, min(left_end, right_end) - max(left_start, right_start))
  return total


def is_pexels(asset: dict) -> bool:
  provider = str(asset.get("source", {}).get("provider", "")).lower()
  asset_id = str(asset.get("assetId", "")).lower()
  return provider == "pexels" or asset_id.startswith("pexels-")


def evaluate_mix(
  windows_data: dict,
  manifest: dict,
  project: Path | None,
  min_pexels: float,
  max_pexels: float,
  min_assets: int,
  check_files: bool = True,
) -> tuple[bool, dict, list[str]]:
  errors: list[str] = []
  full_total = float(windows_data.get("fullTotal", 0))
  if full_total <= 0:
    return False, {}, ["avatar-windows.json thiếu fullTotal hợp lệ"]

  avatar_intervals = merge_intervals([
    (max(0.0, float(item["start"])), min(full_total, float(item["end"])))
    for item in windows_data.get("windows", [])
    if "start" in item and "end" in item
  ])
  avatar_total = duration(avatar_intervals)
  scene_total = full_total - avatar_total
  if scene_total <= 0:
    return False, {}, ["Không còn thời lượng SCENE để tính visual mix"]

  pexels_intervals: list[tuple[float, float]] = []
  pexels_assets: set[str] = set()
  for index, asset in enumerate(manifest.get("assets", []), start=1):
    if asset.get("usage") != "broll-fullscreen" or not is_pexels(asset):
      continue
    placement = asset.get("placement", {})
    if "start_s" not in placement or "duration_s" not in placement:
      errors.append(f"Pexels asset #{index} thiếu placement.start_s/duration_s")
      continue
    start = max(0.0, float(placement["start_s"]))
    end = min(full_total, start + float(placement["duration_s"]))
    if end <= start:
      errors.append(f"Pexels asset #{index} có placement không hợp lệ")
      continue

    trimmed = asset.get("trimmed")
    if check_files and project is not None:
      if not trimmed or not (project / trimmed).is_file():
        errors.append(f"Pexels asset #{index} thiếu file trimmed: {trimmed or '(trống)'}")
        continue

    pexels_intervals.append((start, end))
    pexels_assets.add(str(asset.get("assetId") or trimmed or index))

  pexels_intervals = merge_intervals(pexels_intervals)
  avatar_overlap = overlap_duration(pexels_intervals, avatar_intervals)
  if avatar_overlap > EPSILON:
    errors.append(
      f"Pexels đang đè lên avatar {avatar_overlap:.2f}s; chỉ đặt trong thời gian SCENE"
    )

  pexels_total = max(0.0, duration(pexels_intervals) - avatar_overlap)
  pexels_ratio = pexels_total / scene_total
  hyperframes_ratio = max(0.0, 1.0 - pexels_ratio)

  if len(pexels_assets) < min_assets:
    errors.append(
      f"Chỉ có {len(pexels_assets)} Pexels asset; cần ít nhất {min_assets} asset khác nhau"
    )
  if not min_pexels <= pexels_ratio <= max_pexels:
    target_ratio = (min_pexels + max_pexels) / 2
    target_seconds = scene_total * target_ratio
    delta = target_seconds - pexels_total
    action = "thêm" if delta > 0 else "bớt"
    errors.append(
      f"Pexels {pexels_ratio:.1%} ngoài biên {min_pexels:.0%}–{max_pexels:.0%}; "
      f"{action} khoảng {abs(delta):.2f}s để về mục tiêu {target_ratio:.0%}"
    )

  metrics = {
    "full_total_s": full_total,
    "avatar_total_s": avatar_total,
    "scene_total_s": scene_total,
    "pexels_total_s": pexels_total,
    "hyperframes_total_s": max(0.0, scene_total - pexels_total),
    "pexels_ratio": pexels_ratio,
    "hyperframes_ratio": hyperframes_ratio,
    "pexels_assets": len(pexels_assets),
  }
  return not errors, metrics, errors


def print_result(ok: bool, metrics: dict, errors: list[str]) -> None:
  if metrics:
    print(
      f"{'PASS' if ok else 'FAIL'} visual mix: "
      f"Pexels {metrics['pexels_ratio']:.1%} / "
      f"HyperFrames {metrics['hyperframes_ratio']:.1%} "
      f"trên {metrics['scene_total_s']:.2f}s SCENE "
      f"({metrics['pexels_assets']} Pexels assets)"
    )
  for error in errors:
    print(f"- {error}")


def self_test() -> int:
  windows = {
    "fullTotal": 60,
    "windows": [{"start": 0, "end": 10}, {"start": 50, "end": 60}],
  }
  pass_manifest = {
    "assets": [
      {
        "assetId": "pexels-1",
        "usage": "broll-fullscreen",
        "placement": {"start_s": 10, "duration_s": 10},
        "source": {"provider": "pexels"},
      },
      {
        "assetId": "pexels-2",
        "usage": "broll-fullscreen",
        "placement": {"start_s": 30, "duration_s": 10},
        "source": {"provider": "pexels"},
      },
    ]
  }
  low_manifest = {"assets": pass_manifest["assets"][:1]}
  overlap_manifest = {
    "assets": [
      pass_manifest["assets"][0],
      {
        "assetId": "pexels-3",
        "usage": "broll-fullscreen",
        "placement": {"start_s": 5, "duration_s": 10},
        "source": {"provider": "pexels"},
      },
    ]
  }
  cases = [
    ("exact-50", pass_manifest, 0.45, 0.55, 2, True),
    ("too-low-default", low_manifest, 0.45, 0.55, 2, False),
    ("readability-25", low_manifest, 0.20, 0.30, 1, True),
    ("avatar-overlap", overlap_manifest, 0.45, 0.55, 2, False),
  ]
  failed = []
  for name, manifest, min_ratio, max_ratio, min_assets, expected in cases:
    ok, _, _ = evaluate_mix(
      windows, manifest, None, min_ratio, max_ratio, min_assets, False
    )
    if ok != expected:
      failed.append(name)
  if failed:
    print(f"SELF-TEST FAIL: {', '.join(failed)}")
    return 1
  print("SELF-TEST PASS: exact-50, too-low-default, readability-25, avatar-overlap")
  return 0


def main() -> int:
  parser = argparse.ArgumentParser(
    description=(
      "Validate the approved Pexels/HyperFrames mix during non-avatar time. "
      "Defaults to balanced 45%-55%; pass explicit bounds only for an approved "
      "readability override documented in STORYBOARD.md."
    )
  )
  parser.add_argument("--project", type=Path)
  parser.add_argument("--min-pexels", type=float, default=0.45)
  parser.add_argument("--max-pexels", type=float, default=0.55)
  parser.add_argument("--min-assets", type=int, default=2)
  parser.add_argument("--self-test", action="store_true")
  args = parser.parse_args()

  if args.self_test:
    return self_test()
  if args.project is None:
    parser.error("--project is required unless --self-test is used")
  if not 0 <= args.min_pexels <= args.max_pexels <= 1:
    parser.error("ratio bounds must satisfy 0 <= min <= max <= 1")

  windows_path = args.project / "avatar-windows.json"
  manifest_path = args.project / "media-manifest.json"
  try:
    windows_data = json.loads(windows_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
  except (OSError, json.JSONDecodeError) as exc:
    print(f"FAIL visual mix: {exc}")
    return 2

  ok, metrics, errors = evaluate_mix(
    windows_data,
    manifest,
    args.project,
    args.min_pexels,
    args.max_pexels,
    args.min_assets,
  )
  print_result(ok, metrics, errors)
  return 0 if ok else 2


if __name__ == "__main__":
  sys.exit(main())
