#!/usr/bin/env python3
"""Fail-fast gate for asset-led, Pexels, HyperFrames, BGM and SFX coverage."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


EPSILON = 0.05
KINDS = ("user-asset", "pexels", "hyperframes")
MUSIC_RIGHTS = ("user-provided", "licensed-local", "royalty-free-approved")


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


def interval_duration(intervals: list[tuple[float, float]]) -> float:
  return sum(end - start for start, end in intervals)


def overlap_duration(
  left: list[tuple[float, float]], right: list[tuple[float, float]]
) -> float:
  total = 0.0
  for left_start, left_end in left:
    for right_start, right_end in right:
      total += max(0.0, min(left_end, right_end) - max(left_start, right_start))
  return total


def placement_rows(plan: dict) -> list[dict]:
  rows = list(plan.get("placements", []))
  for beat in plan.get("beats", []):
    for placement in beat.get("placements", []):
      row = dict(placement)
      row.setdefault("beat_id", beat.get("id") or beat.get("beat_id"))
      rows.append(row)
  return rows


def project_file_exists(project: Path, file_value: object) -> bool:
  if not isinstance(file_value, str) or not file_value.strip():
    return False
  return (project / file_value).is_file()


def evaluate_visual(
  windows_data: dict,
  visual_plan: dict,
  media_manifest: dict,
  project: Path,
  args: argparse.Namespace,
) -> tuple[dict, list[str]]:
  errors: list[str] = []
  full_total = float(windows_data.get("fullTotal") or visual_plan.get("fullTotal") or 0)
  if full_total <= 0:
    return {}, ["Thiếu fullTotal hợp lệ trong avatar-windows.json hoặc visual-plan.json"]

  avatar_intervals = merge_intervals([
    (
      max(0.0, float(item["start"])),
      min(full_total, float(item["end"])),
    )
    for item in windows_data.get("windows", [])
    if "start" in item and "end" in item
  ])
  avatar_total = interval_duration(avatar_intervals)
  scene_total = full_total - avatar_total
  if scene_total <= 0:
    return {}, ["Không còn scene_time để tính visual mix"]

  intervals: dict[str, list[tuple[float, float]]] = {kind: [] for kind in KINDS}
  asset_ids: dict[str, set[str]] = {kind: set() for kind in KINDS}
  manifest_pexels: dict[str, dict] = {}
  for asset in media_manifest.get("assets", []):
    provider = str(asset.get("source", {}).get("provider", "")).lower()
    asset_id = str(asset.get("assetId", ""))
    if (
      asset.get("usage") == "broll-fullscreen"
      and (provider == "pexels" or asset_id.lower().startswith("pexels-"))
    ):
      manifest_pexels[asset_id] = asset

  for index, placement in enumerate(placement_rows(visual_plan), start=1):
    if placement.get("dominant", True) is False:
      continue
    kind = str(placement.get("kind", ""))
    if kind not in KINDS:
      errors.append(f"Placement #{index} có kind không hợp lệ: {kind or '(trống)'}")
      continue
    try:
      start = max(0.0, float(placement["start_s"]))
      end = min(full_total, start + float(placement["duration_s"]))
    except (KeyError, TypeError, ValueError):
      errors.append(f"Placement #{index} thiếu start_s/duration_s hợp lệ")
      continue
    if end <= start:
      errors.append(f"Placement #{index} có duration không hợp lệ")
      continue

    current = [(start, end)]
    avatar_overlap = overlap_duration(current, avatar_intervals)
    if avatar_overlap > EPSILON:
      errors.append(
        f"Placement #{index} ({kind}) đè avatar {avatar_overlap:.2f}s"
      )

    if kind != "hyperframes" and not args.no_file_check:
      if not project_file_exists(project, placement.get("file")):
        errors.append(
          f"Placement #{index} ({kind}) thiếu file: {placement.get('file') or '(trống)'}"
        )

    if kind == "pexels":
      if placement.get("overlay") != "none":
        errors.append(
          f"Placement #{index} Pexels phải có overlay='none'; "
          "chỉ captions được phép phủ footage"
        )
      placement_asset_id = str(placement.get("asset_id", ""))
      manifest_asset = manifest_pexels.get(placement_asset_id)
      if manifest_asset is None:
        errors.append(
          f"Placement #{index} Pexels không có provenance trong media-manifest: "
          f"{placement_asset_id or '(trống)'}"
        )
      else:
        manifest_placement = manifest_asset.get("placement", {})
        try:
          manifest_start = float(manifest_placement["start_s"])
          manifest_duration = float(manifest_placement["duration_s"])
        except (KeyError, TypeError, ValueError):
          errors.append(
            f"Pexels {placement_asset_id} thiếu placement trong media-manifest"
          )
        else:
          if (
            abs(start - manifest_start) > EPSILON
            or abs((end - start) - manifest_duration) > EPSILON
          ):
            errors.append(
              f"Pexels {placement_asset_id} lệch timing giữa visual-plan và media-manifest"
            )
        if placement.get("file") != manifest_asset.get("trimmed"):
          errors.append(
            f"Pexels {placement_asset_id} phải trỏ tới file trimmed trong media-manifest"
          )

    intervals[kind].append((start, end))
    if kind != "hyperframes":
      asset_id = str(placement.get("asset_id") or placement.get("file") or "")
      if asset_id:
        asset_ids[kind].add(asset_id)

  for kind in KINDS:
    intervals[kind] = merge_intervals(intervals[kind])

  for left_index, left_kind in enumerate(KINDS):
    for right_kind in KINDS[left_index + 1:]:
      overlap = overlap_duration(intervals[left_kind], intervals[right_kind])
      if overlap > EPSILON:
        errors.append(
          f"Dominant placement {left_kind}/{right_kind} overlap {overlap:.2f}s"
        )

  all_intervals = merge_intervals([
    interval for kind in KINDS for interval in intervals[kind]
  ])
  timeline_intervals = merge_intervals(all_intervals + avatar_intervals)
  cursor = 0.0
  visual_gaps: list[tuple[float, float]] = []
  for start, end in timeline_intervals:
    if start - cursor > args.max_visual_gap + 1e-9:
      visual_gaps.append((cursor, start))
    cursor = max(cursor, end)
  if full_total - cursor > args.max_visual_gap + 1e-9:
    visual_gaps.append((cursor, full_total))
  for start, end in visual_gaps:
    errors.append(
      f"Timeline hở {end - start:.2f}s tại {start:.2f}–{end:.2f}s; "
      "căn semantic boundary của hai placement liền nhau"
    )

  avatar_overlap_total = overlap_duration(all_intervals, avatar_intervals)
  covered_total = max(0.0, interval_duration(all_intervals) - avatar_overlap_total)
  coverage_ratio = covered_total / scene_total

  totals = {
    kind: max(
      0.0,
      interval_duration(intervals[kind])
      - overlap_duration(intervals[kind], avatar_intervals),
    )
    for kind in KINDS
  }
  ratios = {kind: totals[kind] / scene_total for kind in KINDS}

  if not args.min_user <= ratios["user-asset"] <= args.max_user:
    errors.append(
      f"User asset {ratios['user-asset']:.1%} ngoài biên "
      f"{args.min_user:.0%}–{args.max_user:.0%}"
    )
  if not args.min_pexels <= ratios["pexels"] <= args.max_pexels:
    errors.append(
      f"Pexels {ratios['pexels']:.1%} ngoài biên "
      f"{args.min_pexels:.0%}–{args.max_pexels:.0%}"
    )
  if ratios["hyperframes"] > args.max_hyperframes + 1e-9:
    errors.append(
      f"Pure HyperFrames {ratios['hyperframes']:.1%} vượt trần "
      f"{args.max_hyperframes:.0%}"
    )
  if coverage_ratio < args.min_coverage:
    missing = scene_total * args.min_coverage - covered_total
    errors.append(
      f"Dominant coverage {coverage_ratio:.1%} dưới {args.min_coverage:.0%}; "
      f"còn thiếu khoảng {max(0.0, missing):.2f}s"
    )
  if len(asset_ids["user-asset"]) < args.min_user_assets:
    errors.append(
      f"Chỉ có {len(asset_ids['user-asset'])} user asset; "
      f"cần ít nhất {args.min_user_assets}"
    )
  if len(asset_ids["pexels"]) < args.min_pexels_assets:
    errors.append(
      f"Chỉ có {len(asset_ids['pexels'])} Pexels asset; "
      f"cần ít nhất {args.min_pexels_assets}"
    )

  metrics = {
    "full_total_s": full_total,
    "avatar_total_s": avatar_total,
    "scene_total_s": scene_total,
    "coverage_ratio": coverage_ratio,
    "user_ratio": ratios["user-asset"],
    "pexels_ratio": ratios["pexels"],
    "hyperframes_ratio": ratios["hyperframes"],
    "user_assets": len(asset_ids["user-asset"]),
    "pexels_assets": len(asset_ids["pexels"]),
  }
  return metrics, errors


def evaluate_audio(
  audio_plan: dict,
  project: Path,
  full_total: float,
  args: argparse.Namespace,
) -> tuple[dict, list[str]]:
  errors: list[str] = []
  voice = audio_plan.get("voice", {})
  try:
    voice_volume = float(voice.get("volume", 0))
  except (TypeError, ValueError):
    voice_volume = 0
  if abs(voice_volume - 1.0) > 1e-9:
    errors.append("Voice volume phải bằng 1.0")
  if not args.no_file_check and not project_file_exists(project, voice.get("file")):
    errors.append(f"Thiếu voice file: {voice.get('file') or '(trống)'}")

  music_rows = audio_plan.get("music", [])
  if isinstance(music_rows, dict):
    music_rows = [music_rows]
  music_intervals: list[tuple[float, float]] = []
  for index, music in enumerate(music_rows, start=1):
    try:
      start = max(0.0, float(music.get("start_s", 0)))
      duration_s = float(music["duration_s"])
      volume = float(music["volume"])
      end = min(full_total, start + duration_s)
    except (KeyError, TypeError, ValueError):
      errors.append(f"Music #{index} thiếu timing/volume hợp lệ")
      continue
    if end <= start:
      errors.append(f"Music #{index} có duration không hợp lệ")
      continue
    if not 0.05 <= volume <= 0.15:
      errors.append(f"Music #{index} volume {volume:.2f} ngoài 0.05–0.15")
    rights = str(music.get("rights", ""))
    if rights not in MUSIC_RIGHTS:
      errors.append(
        f"Music #{index} thiếu rights hợp lệ: "
        f"{rights or '(trống)'}"
      )
    if not args.no_file_check and not project_file_exists(project, music.get("file")):
      errors.append(f"Music #{index} thiếu file: {music.get('file') or '(trống)'}")
    music_intervals.append((start, end))

  music_coverage = (
    interval_duration(merge_intervals(music_intervals)) / full_total
    if full_total > 0 else 0
  )
  if (
    music_coverage < args.min_music_coverage
    and not args.draft_allow_missing_bgm
  ):
    errors.append(
      f"BGM coverage {music_coverage:.1%} dưới {args.min_music_coverage:.0%}"
    )

  sfx_rows = list(audio_plan.get("sfx", []))
  min_sfx = args.min_sfx
  if min_sfx is None:
    min_sfx = 2 if full_total >= 45 else 1
  max_sfx = args.max_sfx
  if max_sfx is None:
    max_sfx = max(2, min(6, math.ceil(full_total / 25)))
  if len(sfx_rows) < min_sfx:
    errors.append(f"Chỉ có {len(sfx_rows)} SFX; cần ít nhất {min_sfx}")
  if len(sfx_rows) > max_sfx:
    errors.append(f"Có {len(sfx_rows)} SFX; vượt trần {max_sfx}")

  starts: list[float] = []
  for index, sfx in enumerate(sfx_rows, start=1):
    try:
      start = float(sfx["start_s"])
      duration_s = float(sfx["duration_s"])
      volume = float(sfx["volume"])
    except (KeyError, TypeError, ValueError):
      errors.append(f"SFX #{index} thiếu timing/volume hợp lệ")
      continue
    if not 0 <= start < full_total or duration_s <= 0:
      errors.append(f"SFX #{index} có placement không hợp lệ")
    if not 0.10 <= volume <= 0.50:
      errors.append(f"SFX #{index} volume {volume:.2f} ngoài 0.10–0.50")
    if not args.no_file_check and not project_file_exists(project, sfx.get("file")):
      errors.append(f"SFX #{index} thiếu file: {sfx.get('file') or '(trống)'}")
    starts.append(start)

  for left, right in zip(sorted(starts), sorted(starts)[1:]):
    if right - left < args.min_sfx_spacing - 1e-9:
      errors.append(
        f"Hai SFX tại {left:.2f}s/{right:.2f}s cách nhau dưới "
        f"{args.min_sfx_spacing:.1f}s"
      )

  metrics = {
    "music_coverage_ratio": music_coverage,
    "music_tracks": len(music_rows),
    "sfx_hits": len(sfx_rows),
    "sfx_max": max_sfx,
  }
  return metrics, errors


def evaluate(
  windows_data: dict,
  visual_plan: dict,
  media_manifest: dict,
  audio_plan: dict,
  project: Path,
  args: argparse.Namespace,
) -> tuple[bool, dict, list[str]]:
  visual_metrics, visual_errors = evaluate_visual(
    windows_data, visual_plan, media_manifest, project, args
  )
  full_total = float(visual_metrics.get("full_total_s", 0))
  audio_metrics, audio_errors = evaluate_audio(
    audio_plan, project, full_total, args
  ) if full_total > 0 else ({}, ["Không thể validate audio khi thiếu fullTotal"])
  metrics = {**visual_metrics, **audio_metrics}
  errors = visual_errors + audio_errors
  return not errors, metrics, errors


def print_result(ok: bool, metrics: dict, errors: list[str]) -> None:
  if metrics:
    print(
      f"{'PASS' if ok else 'FAIL'} asset-broll plan: "
      f"user {metrics.get('user_ratio', 0):.1%}, "
      f"Pexels {metrics.get('pexels_ratio', 0):.1%}, "
      f"HyperFrames {metrics.get('hyperframes_ratio', 0):.1%}, "
      f"coverage {metrics.get('coverage_ratio', 0):.1%}; "
      f"BGM {metrics.get('music_coverage_ratio', 0):.1%}, "
      f"SFX {metrics.get('sfx_hits', 0)}/{metrics.get('sfx_max', 0)}"
    )
  for error in errors:
    print(f"- {error}")


def make_args(**overrides: object) -> argparse.Namespace:
  values = {
    "min_user": 0.40,
    "max_user": 0.75,
    "min_pexels": 0.20,
    "max_pexels": 0.45,
    "max_hyperframes": 0.20,
    "min_coverage": 0.95,
    "max_visual_gap": 0.05,
    "min_user_assets": 2,
    "min_pexels_assets": 2,
    "min_music_coverage": 0.90,
    "min_sfx": None,
    "max_sfx": None,
    "min_sfx_spacing": 1.5,
    "draft_allow_missing_bgm": False,
    "no_file_check": True,
  }
  values.update(overrides)
  return argparse.Namespace(**values)


def self_test() -> int:
  windows = {
    "fullTotal": 60,
    "windows": [{"start": 0, "end": 10}, {"start": 50, "end": 60}],
  }
  visual = {
    "placements": [
      {"kind": "user-asset", "start_s": 10, "duration_s": 11,
       "asset_id": "u1", "file": "media/u1.png"},
      {"kind": "user-asset", "start_s": 21, "duration_s": 11,
       "asset_id": "u2", "file": "media/u2.png"},
      {"kind": "pexels", "start_s": 32, "duration_s": 6,
       "asset_id": "p1", "file": "broll-clips/p1.mp4", "overlay": "none"},
      {"kind": "pexels", "start_s": 38, "duration_s": 6,
       "asset_id": "p2", "file": "broll-clips/p2.mp4", "overlay": "none"},
      {"kind": "hyperframes", "start_s": 44, "duration_s": 6},
    ]
  }
  media_manifest = {
    "assets": [
      {"assetId": "p1", "usage": "broll-fullscreen",
       "trimmed": "broll-clips/p1.mp4",
       "placement": {"start_s": 32, "duration_s": 6},
       "source": {"provider": "pexels"}},
      {"assetId": "p2", "usage": "broll-fullscreen",
       "trimmed": "broll-clips/p2.mp4",
       "placement": {"start_s": 38, "duration_s": 6},
       "source": {"provider": "pexels"}},
    ]
  }
  audio = {
    "voice": {"file": "audio/full.mp3", "volume": 1.0},
    "music": [{"file": "assets/bgm/background.mp3", "start_s": 0,
               "duration_s": 60, "volume": 0.10,
               "rights": "user-provided"}],
    "sfx": [
      {"file": "assets/sfx/flash.mp3", "start_s": 0.2,
       "duration_s": 0.8, "volume": 0.30},
      {"file": "assets/sfx/ting.mp3", "start_s": 24.1,
       "duration_s": 0.7, "volume": 0.28},
    ],
  }
  bad_overlap = json.loads(json.dumps(visual))
  bad_overlap["placements"][2]["start_s"] = 28
  bad_avatar = json.loads(json.dumps(visual))
  bad_avatar["placements"][0]["start_s"] = 5
  bad_provenance = json.loads(json.dumps(visual))
  bad_provenance["placements"][2]["asset_id"] = "missing-pexels"
  bad_rights = json.loads(json.dumps(audio))
  bad_rights["music"][0]["rights"] = ""
  bad_pexels_overlay = json.loads(json.dumps(visual))
  bad_pexels_overlay["placements"][2].pop("overlay")
  bad_gap = json.loads(json.dumps(visual))
  bad_gap["placements"][3]["start_s"] = 38.2
  no_music = json.loads(json.dumps(audio))
  no_music["music"] = []

  cases = [
    ("balanced", visual, audio, True),
    ("dominant-overlap", bad_overlap, audio, False),
    ("avatar-overlap", bad_avatar, audio, False),
    ("missing-provenance", bad_provenance, audio, False),
    ("missing-music-rights", visual, bad_rights, False),
    ("pexels-overlay", bad_pexels_overlay, audio, False),
    ("timeline-gap", bad_gap, audio, False),
  ]
  failed: list[str] = []
  for name, case_visual, case_audio, expected in cases:
    ok, _, _ = evaluate(
      windows, case_visual, media_manifest, case_audio, Path("."), make_args()
    )
    if ok != expected:
      failed.append(name)
  if failed:
    print(f"SELF-TEST FAIL: {', '.join(failed)}")
    return 1
  print(
    "SELF-TEST PASS: balanced, dominant-overlap, avatar-overlap, "
    "missing-provenance, missing-music-rights, pexels-overlay, timeline-gap"
  )
  draft_ok, _, _ = evaluate(
    windows, visual, media_manifest, no_music, Path("."),
    make_args(draft_allow_missing_bgm=True)
  )
  if not draft_ok:
    print("SELF-TEST FAIL: draft-allow-missing-bgm")
    return 1
  print("SELF-TEST PASS: draft-allow-missing-bgm")
  return 0


def main() -> int:
  parser = argparse.ArgumentParser(
    description="Validate asset/Pexels/HyperFrames coverage and BGM/SFX plan."
  )
  parser.add_argument("--project", type=Path)
  parser.add_argument("--min-user", type=float, default=0.40)
  parser.add_argument("--max-user", type=float, default=0.75)
  parser.add_argument("--min-pexels", type=float, default=0.20)
  parser.add_argument("--max-pexels", type=float, default=0.45)
  parser.add_argument("--max-hyperframes", type=float, default=0.20)
  parser.add_argument("--min-coverage", type=float, default=0.95)
  parser.add_argument("--max-visual-gap", type=float, default=0.05)
  parser.add_argument("--min-user-assets", type=int, default=2)
  parser.add_argument("--min-pexels-assets", type=int, default=2)
  parser.add_argument("--min-music-coverage", type=float, default=0.90)
  parser.add_argument("--min-sfx", type=int)
  parser.add_argument("--max-sfx", type=int)
  parser.add_argument("--min-sfx-spacing", type=float, default=1.5)
  parser.add_argument(
    "--draft-allow-missing-bgm",
    action="store_true",
    help="Chỉ dùng cho draft review; final vẫn phải validate không có cờ này.",
  )
  parser.add_argument("--no-file-check", action="store_true")
  parser.add_argument("--self-test", action="store_true")
  args = parser.parse_args()

  if args.self_test:
    return self_test()
  if args.project is None:
    parser.error("--project is required unless --self-test is used")
  if not 0 <= args.min_user <= args.max_user <= 1:
    parser.error("user bounds must satisfy 0 <= min <= max <= 1")
  if not 0 <= args.min_pexels <= args.max_pexels <= 1:
    parser.error("Pexels bounds must satisfy 0 <= min <= max <= 1")
  if not 0 <= args.max_hyperframes <= 1:
    parser.error("--max-hyperframes must be between 0 and 1")
  if not 0 <= args.min_coverage <= 1:
    parser.error("--min-coverage must be between 0 and 1")
  if args.max_visual_gap < 0:
    parser.error("--max-visual-gap must be non-negative")

  try:
    windows_data = json.loads(
      (args.project / "avatar-windows.json").read_text(encoding="utf-8")
    )
    visual_plan = json.loads(
      (args.project / "visual-plan.json").read_text(encoding="utf-8")
    )
    media_manifest = json.loads(
      (args.project / "media-manifest.json").read_text(encoding="utf-8")
    )
    audio_plan = json.loads(
      (args.project / "audio-plan.json").read_text(encoding="utf-8")
    )
  except (OSError, json.JSONDecodeError) as exc:
    print(f"FAIL asset-broll plan: {exc}")
    return 2

  ok, metrics, errors = evaluate(
    windows_data, visual_plan, media_manifest, audio_plan, args.project, args
  )
  print_result(ok, metrics, errors)
  return 0 if ok else 2


if __name__ == "__main__":
  sys.exit(main())
