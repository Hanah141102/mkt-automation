#!/usr/bin/env python3
"""Validate a 16:9 Pexels + HyperFrames media plan before rendering."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any


ALLOWED_MODES = {"BROLL_PRIMARY", "HYPERFRAME_FULL", "BROLL_PLUS_OVERLAY"}
TOLERANCE = 0.10


def is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, help="Path to media-plan.json")
    parser.add_argument("--project", help="Project root used to resolve asset paths")
    parser.add_argument("--require-files", action="store_true", help="Fail when local assets do not exist")
    args = parser.parse_args()

    plan_path = Path(args.plan).expanduser().resolve()
    project = Path(args.project).expanduser().resolve() if args.project else plan_path.parent.parent
    errors: list[str] = []
    warnings: list[str] = []

    try:
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read plan: {exc}", file=sys.stderr)
        return 2

    canvas = plan.get("canvas", {})
    if canvas.get("width") != 1920 or canvas.get("height") != 1080:
        errors.append("canvas must be 1920x1080")
    if canvas.get("fps") != 30:
        errors.append("canvas fps must be 30")

    total = plan.get("total_duration_s")
    if not is_number(total) or total <= 0:
        errors.append("total_duration_s must be a positive number")
        total = 0.0

    beats = plan.get("beats")
    if not isinstance(beats, list) or not beats:
        errors.append("beats must be a non-empty array")
        beats = []

    beat_ids: set[str] = set()
    asset_ids: set[str] = set()
    provider_ids: set[tuple[str, str]] = set()
    previous_end = 0.0

    for index, beat in enumerate(beats):
        label = f"beat[{index}]"
        if not isinstance(beat, dict):
            errors.append(f"{label} must be an object")
            continue

        beat_id = beat.get("id")
        if not isinstance(beat_id, str) or not beat_id.strip():
            errors.append(f"{label}.id must be a non-empty string")
        elif beat_id in beat_ids:
            errors.append(f"duplicate beat id: {beat_id}")
        else:
            beat_ids.add(beat_id)
            label = beat_id

        start, end = beat.get("start_s"), beat.get("end_s")
        if not is_number(start) or not is_number(end) or start < 0 or end <= start:
            errors.append(f"{label}: invalid start_s/end_s")
            continue
        if index == 0 and abs(start) > TOLERANCE:
            errors.append(f"{label}: timeline must start at 0s, got {start:.3f}s")
        elif index > 0:
            delta = start - previous_end
            if delta > TOLERANCE:
                errors.append(f"{label}: gap of {delta:.3f}s before beat")
            elif delta < -TOLERANCE:
                errors.append(f"{label}: overlap of {-delta:.3f}s with previous beat")
        previous_end = end

        mode = beat.get("mode")
        if mode not in ALLOWED_MODES:
            errors.append(f"{label}: unsupported mode {mode!r}")

        assets = beat.get("assets", [])
        if not isinstance(assets, list):
            errors.append(f"{label}.assets must be an array")
            assets = []
        if mode in {"BROLL_PRIMARY", "BROLL_PLUS_OVERLAY"} and not assets:
            errors.append(f"{label}: {mode} requires at least one asset")
        if mode == "HYPERFRAME_FULL" and assets:
            warnings.append(f"{label}: HYPERFRAME_FULL normally has no video assets")

        cues = beat.get("cues", [])
        if not isinstance(cues, list):
            errors.append(f"{label}.cues must be an array")
            cues = []
        for cue_index, cue in enumerate(cues):
            at = cue.get("at_s") if isinstance(cue, dict) else None
            if not is_number(at) or at < start - TOLERANCE or at > end + TOLERANCE:
                errors.append(f"{label}.cues[{cue_index}]: at_s must fall inside its beat")

        asset_previous_end = start
        for asset_index, asset in enumerate(assets):
            asset_label = f"{label}.assets[{asset_index}]"
            if not isinstance(asset, dict):
                errors.append(f"{asset_label} must be an object")
                continue

            asset_id = asset.get("asset_id")
            if not isinstance(asset_id, str) or not asset_id:
                errors.append(f"{asset_label}.asset_id must be a non-empty string")
            elif asset_id in asset_ids:
                errors.append(f"asset reused: {asset_id}")
            else:
                asset_ids.add(asset_id)

            provider = str(asset.get("provider", ""))
            provider_value = asset.get("pexels_id") or asset.get("provider_id")
            if provider_value is not None:
                provider_id = (provider, str(provider_value))
                if provider_id in provider_ids:
                    errors.append(f"provider asset reused: {provider}:{provider_value}")
                else:
                    provider_ids.add(provider_id)

            width, height = asset.get("width"), asset.get("height")
            if is_number(width) and is_number(height) and width <= height:
                errors.append(f"{asset_label}: video must be landscape, got {width}x{height}")
            elif width is None or height is None:
                warnings.append(f"{asset_label}: width/height missing; verify landscape")

            asset_start, asset_end = asset.get("start_s"), asset.get("end_s")
            if not is_number(asset_start) or not is_number(asset_end) or asset_end <= asset_start:
                errors.append(f"{asset_label}: invalid start_s/end_s")
            else:
                if asset_start < start - TOLERANCE or asset_end > end + TOLERANCE:
                    errors.append(f"{asset_label}: placement must stay inside beat {label}")
                delta = asset_start - asset_previous_end
                if delta > TOLERANCE:
                    errors.append(f"{asset_label}: asset gap of {delta:.3f}s")
                elif delta < -TOLERANCE:
                    errors.append(f"{asset_label}: asset overlap of {-delta:.3f}s")
                asset_previous_end = asset_end

            path_value = asset.get("path")
            if not isinstance(path_value, str) or not path_value:
                errors.append(f"{asset_label}.path must be a non-empty string")
            elif args.require_files:
                asset_path = Path(path_value)
                if not asset_path.is_absolute():
                    asset_path = project / asset_path
                if not asset_path.is_file():
                    errors.append(f"{asset_label}: file not found: {asset_path}")

        if assets and abs(asset_previous_end - end) > TOLERANCE:
            errors.append(f"{label}: assets do not cover beat end ({asset_previous_end:.3f}s vs {end:.3f}s)")

    if beats and is_number(total) and abs(previous_end - total) > TOLERANCE:
        errors.append(f"timeline ends at {previous_end:.3f}s but total_duration_s is {total:.3f}s")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"OK: {len(beats)} beat(s), {len(asset_ids)} unique asset(s), {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
