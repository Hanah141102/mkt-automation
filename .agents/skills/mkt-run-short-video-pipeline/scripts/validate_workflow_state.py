#!/usr/bin/env python3
"""Validate short-video pipeline state without modifying it or using network."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


WORKFLOW = "mkt-run-short-video-pipeline"
MODES = {"review", "fast"}
INPUT_TYPES = {"idea", "youtube_url", "url", "local_file"}
APPROVAL_STATUSES = {"pending", "approved", "auto_approved", "changes_requested", "invalidated"}
PUBLISH_ACTIONS = {"prepare_only", "now", "schedule"}
PUBLISH_CONNECTIONS = {"composio", "blotato"}
STOP_AFTER_VALUES = {"idea", "script", "storyboard", "video", "publish"}
STAGES = [
    "INTAKE",
    "SOURCE_ANALYSIS",
    "IDEA",
    "IDEA_REVIEW",
    "SCRIPT",
    "SCRIPT_REVIEW",
    "STORYBOARD",
    "STORYBOARD_REVIEW",
    "VIDEO",
    "READY_TO_PUBLISH",
    "PUBLISH",
    "DONE",
]
SPECIAL_STAGES = {"BLOCKED"}
MAX_STAGE_BY_STOP = {
    "idea": "IDEA_REVIEW",
    "script": "SCRIPT_REVIEW",
    "storyboard": "STORYBOARD_REVIEW",
    "video": "READY_TO_PUBLISH",
    "publish": "DONE",
}
FORBIDDEN_KEY_PARTS = {"token", "api_key", "apikey", "password", "credential", "cookie", "secret"}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def nested_get(data: dict[str, Any], *keys: str) -> Any:
    value: Any = data
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return None
        value = value[key]
    return value


def reject_secret_keys(value: Any, path: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            lowered = str(key).lower()
            if any(part in lowered for part in FORBIDDEN_KEY_PARTS):
                errors.append(f"Không lưu credential trong state: {path}.{key}")
            reject_secret_keys(child, f"{path}.{key}", errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            reject_secret_keys(child, f"{path}[{index}]", errors)


def valid_iso8601(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def approval_is_valid(data: dict[str, Any], name: str, errors: list[str]) -> bool:
    approval = nested_get(data, "approvals", name)
    version = nested_get(data, "versions", name)
    if not isinstance(approval, dict):
        errors.append(f"Thiếu approvals.{name}")
        return False

    status = approval.get("status")
    require(status in APPROVAL_STATUSES, f"approvals.{name}.status không hợp lệ", errors)
    require(approval.get("version") == version, f"Approval {name} không khớp artifact version", errors)

    accepted = status in {"approved", "auto_approved"}
    if accepted:
        require(isinstance(version, int) and version > 0, f"Không thể duyệt {name} version 0", errors)
        require(valid_iso8601(approval.get("approved_at")), f"Approval {name} thiếu approved_at ISO-8601", errors)
        require(approval.get("approved_by") in {"user", "orchestrator"}, f"Approval {name} thiếu approved_by hợp lệ", errors)
        if data.get("mode") == "review":
            require(status == "approved" and approval.get("approved_by") == "user", f"Review mode không chấp nhận auto-approval cho {name}", errors)
        if data.get("mode") == "fast":
            require(
                (status == "approved" and approval.get("approved_by") == "user")
                or (status == "auto_approved" and approval.get("approved_by") == "orchestrator"),
                f"Fast mode có cặp status/approved_by sai cho {name}",
                errors,
            )
    return accepted


def require_artifact(data: dict[str, Any], name: str, errors: list[str], check_files: bool) -> None:
    value = nested_get(data, "artifacts", name)
    require(isinstance(value, str) and bool(value.strip()), f"Thiếu artifacts.{name}", errors)
    if isinstance(value, str) and value.strip():
        require(os.path.isabs(value), f"artifacts.{name} phải là absolute path", errors)
        if check_files:
            require(Path(value).exists(), f"Artifact không tồn tại: {value}", errors)


def validate_targets(data: dict[str, Any], errors: list[str], require_exact: bool) -> None:
    publish = data.get("publish")
    if not isinstance(publish, dict):
        errors.append("Thiếu publish object")
        return

    action = publish.get("action")
    require(action in PUBLISH_ACTIONS, "publish.action không hợp lệ", errors)
    targets = publish.get("targets")
    require(isinstance(targets, list), "publish.targets phải là list", errors)
    if not isinstance(targets, list):
        return

    if require_exact and action in {"now", "schedule"}:
        require(bool(targets), "Publish now/schedule cần ít nhất một target", errors)
    if require_exact and action == "schedule":
        require(valid_iso8601(publish.get("scheduled_time_utc")), "Schedule cần scheduled_time_utc ISO-8601", errors)

    seen: set[tuple[str, str]] = set()
    for index, target in enumerate(targets):
        prefix = f"publish.targets[{index}]"
        if not isinstance(target, dict):
            errors.append(f"{prefix} phải là object")
            continue
        platform = target.get("platform")
        target_name = target.get("target_name")
        target_id = target.get("target_id")
        require(isinstance(platform, str) and bool(platform.strip()), f"{prefix}.platform còn thiếu", errors)
        require(isinstance(target_name, str) and bool(target_name.strip()), f"{prefix}.target_name còn thiếu", errors)
        require(isinstance(target_id, str) and bool(target_id.strip()), f"{prefix}.target_id còn thiếu", errors)
        if require_exact:
            connection = target.get("connection")
            require(connection in PUBLISH_CONNECTIONS, f"{prefix}.connection chưa được preflight", errors)
            require(valid_iso8601(target.get("verified_at")), f"{prefix}.verified_at không hợp lệ", errors)
            if connection == "blotato":
                account_id = target.get("account_id")
                require(isinstance(account_id, str) and bool(account_id.strip()), f"{prefix}.account_id bắt buộc với Blotato", errors)
        if isinstance(platform, str) and isinstance(target_id, str) and platform and target_id:
            key = (platform.lower(), target_id)
            require(key not in seen, f"Target bị trùng: {platform}/{target_id}", errors)
            seen.add(key)


def stage_at_least(stage: str, threshold: str) -> bool:
    if stage in SPECIAL_STAGES:
        return False
    return STAGES.index(stage) >= STAGES.index(threshold)


def validate(data: dict[str, Any], next_stage: str | None, check_files: bool) -> list[str]:
    errors: list[str] = []
    reject_secret_keys(data, "$", errors)

    require(data.get("schema_version") == 1, "schema_version phải bằng 1", errors)
    require(data.get("workflow") == WORKFLOW, f"workflow phải là {WORKFLOW}", errors)
    require(data.get("mode") in MODES, "mode phải là review hoặc fast", errors)
    require(isinstance(data.get("run_id"), str) and bool(data.get("run_id", "").strip()), "run_id còn trống", errors)
    require(data.get("stop_after") in STOP_AFTER_VALUES, "stop_after không hợp lệ", errors)

    stage = data.get("current_stage")
    require(stage in set(STAGES) | SPECIAL_STAGES, "current_stage không hợp lệ", errors)
    effective_stage = next_stage or stage
    require(effective_stage in set(STAGES) | SPECIAL_STAGES, "next-stage không hợp lệ", errors)
    if effective_stage not in set(STAGES) | SPECIAL_STAGES:
        return errors
    stop_after = data.get("stop_after")
    if effective_stage not in SPECIAL_STAGES and stop_after in MAX_STAGE_BY_STOP:
        max_stage = MAX_STAGE_BY_STOP[stop_after]
        require(
            STAGES.index(effective_stage) <= STAGES.index(max_stage),
            f"Không được vượt stop_after={stop_after} (tối đa {max_stage})",
            errors,
        )

    source_type = nested_get(data, "input", "type")
    source_value = nested_get(data, "input", "value")
    require(source_type in INPUT_TYPES, "input.type không hợp lệ", errors)
    require(isinstance(source_value, str) and bool(source_value.strip()), "input.value còn trống", errors)
    if source_type == "local_file" and isinstance(source_value, str) and source_value:
        require(os.path.isabs(source_value), "input.value của local_file phải là absolute path", errors)
        if check_files:
            require(Path(source_value).exists(), f"Input file không tồn tại: {source_value}", errors)

    duration_s = nested_get(data, "brief", "duration_s")
    require(isinstance(duration_s, (int, float)) and duration_s > 0, "brief.duration_s phải > 0", errors)

    versions = data.get("versions")
    require(isinstance(versions, dict), "Thiếu versions object", errors)
    if isinstance(versions, dict):
        for name in ("idea", "script", "storyboard", "video"):
            value = versions.get(name)
            require(isinstance(value, int) and value >= 0, f"versions.{name} phải là số nguyên >= 0", errors)

    dependencies = data.get("dependencies")
    require(isinstance(dependencies, dict), "Thiếu dependencies object", errors)

    approvals_ok = {
        name: approval_is_valid(data, name, errors)
        for name in ("idea", "script", "storyboard")
    }
    require_exact_target = effective_stage in {"PUBLISH", "DONE"}
    validate_targets(data, errors, require_exact_target)
    publish_action = nested_get(data, "publish", "action")
    if stop_after == "publish":
        require(publish_action in {"now", "schedule"}, "stop_after=publish cần action now hoặc schedule", errors)
    if publish_action in {"now", "schedule"}:
        require(stop_after == "publish", "action now/schedule cần stop_after=publish", errors)

    if effective_stage == "SOURCE_ANALYSIS":
        require(source_type != "idea", "Idea input không cần SOURCE_ANALYSIS", errors)

    if stage_at_least(effective_stage, "IDEA_REVIEW"):
        idea_version = nested_get(data, "versions", "idea")
        require(isinstance(idea_version, int) and idea_version >= 1, "Idea artifact phải có version >= 1", errors)
        require_artifact(data, "idea_review", errors, check_files)
    if stage_at_least(effective_stage, "SCRIPT"):
        require(approvals_ok["idea"], "Chưa duyệt idea version hiện tại", errors)
    if stage_at_least(effective_stage, "SCRIPT_REVIEW"):
        script_version = nested_get(data, "versions", "script")
        require(isinstance(script_version, int) and script_version >= 1, "Script artifact phải có version >= 1", errors)
        require(
            nested_get(data, "dependencies", "script", "idea_version") == nested_get(data, "versions", "idea"),
            "Script không trỏ đúng idea version hiện tại",
            errors,
        )
        require_artifact(data, "script", errors, check_files)
    if stage_at_least(effective_stage, "STORYBOARD"):
        require(approvals_ok["script"], "Chưa duyệt script version hiện tại", errors)
    if stage_at_least(effective_stage, "STORYBOARD_REVIEW"):
        storyboard_version = nested_get(data, "versions", "storyboard")
        require(isinstance(storyboard_version, int) and storyboard_version >= 1, "Storyboard artifact phải có version >= 1", errors)
        require(
            nested_get(data, "dependencies", "storyboard", "script_version") == nested_get(data, "versions", "script"),
            "Storyboard không trỏ đúng script version hiện tại",
            errors,
        )
        for artifact in ("design", "storyboard", "storyboard_preview", "storyboard_contact_sheet"):
            require_artifact(data, artifact, errors, check_files)
    if stage_at_least(effective_stage, "VIDEO"):
        require(approvals_ok["storyboard"], "Chưa duyệt storyboard version hiện tại", errors)
    if stage_at_least(effective_stage, "READY_TO_PUBLISH"):
        video_version = nested_get(data, "versions", "video")
        require(isinstance(video_version, int) and video_version >= 1, "Video artifact phải có version >= 1", errors)
        require(
            nested_get(data, "dependencies", "video", "script_version") == nested_get(data, "versions", "script"),
            "Video không trỏ đúng script version hiện tại",
            errors,
        )
        require(
            nested_get(data, "dependencies", "video", "storyboard_version") == nested_get(data, "versions", "storyboard"),
            "Video không trỏ đúng storyboard version hiện tại",
            errors,
        )
        require_artifact(data, "video", errors, check_files)
    if effective_stage == "PUBLISH":
        require(nested_get(data, "publish", "action") in {"now", "schedule"}, "PUBLISH cần action now hoặc schedule", errors)
    if effective_stage in {"PUBLISH", "DONE"} and nested_get(data, "publish", "action") in {"now", "schedule"}:
        require(
            nested_get(data, "dependencies", "publish", "video_version") == nested_get(data, "versions", "video"),
            "Publish không trỏ đúng video version hiện tại",
            errors,
        )
    if effective_stage == "DONE" and nested_get(data, "publish", "action") in {"now", "schedule"}:
        require_artifact(data, "publish_report", errors, check_files)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", required=True, help="Đường dẫn workflow-state.json")
    parser.add_argument("--next-stage", choices=STAGES + sorted(SPECIAL_STAGES))
    parser.add_argument("--check-files", action="store_true", help="Xác minh artifact và local input tồn tại")
    args = parser.parse_args()

    state_path = Path(args.state)
    if not state_path.is_file():
        print(f"FAIL: Không tìm thấy state: {state_path}", file=sys.stderr)
        return 2

    try:
        data = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: Không đọc được JSON: {exc}", file=sys.stderr)
        return 2

    if not isinstance(data, dict):
        print("FAIL: Root JSON phải là object", file=sys.stderr)
        return 2

    errors = validate(data, args.next_stage, args.check_files)
    if errors:
        print("FAIL:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    target = args.next_stage or data.get("current_stage")
    print(f"PASS: workflow-state hợp lệ cho stage {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
