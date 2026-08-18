#!/usr/bin/env python3
"""Collect and normalize public competitor social data with Apify Actors."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


ACTORS = {
    "instagram": "apify/instagram-scraper",
    "facebook": "apify/facebook-posts-scraper",
    "tiktok": "clockworks/tiktok-profile-scraper",
    "youtube": "streamers/youtube-channel-scraper",
}
SUPPORTED_PLATFORMS = tuple(ACTORS)
STOPWORDS = {
    "and", "are", "but", "for", "from", "has", "have", "the", "this", "that",
    "with", "you", "your", "our", "was", "were", "will", "video", "https", "www",
    "các", "cho", "của", "được", "giúp", "khi", "không", "là", "một", "này", "những",
    "thì", "trong", "và", "với", "để", "đến", "từ", "có", "sẽ", "đang", "về",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze public competitor social channels with Apify",
    )
    parser.add_argument("--input", help="Competitor config JSON")
    parser.add_argument("--output-dir", help="Directory for report artifacts")
    parser.add_argument("--check-deps", action="store_true", help="Install and verify apify-client")
    parser.add_argument("--dry-run", action="store_true", help="Validate and show Actor calls only")
    parser.add_argument("--mock-data", help="Mock dataset JSON for an offline end-to-end test")
    parser.add_argument("--max-posts", type=int, help="Override max posts per channel")
    parser.add_argument("--max-charge-usd", type=float, default=1.0, help="Cost ceiling per run")
    parser.add_argument("--run-timeout", type=int, default=600, help="Actor timeout in seconds")
    return parser.parse_args()


def project_root() -> Path:
    cwd = Path.cwd().resolve()
    for candidate in (cwd, *cwd.parents):
        if (candidate / ".git").exists():
            return candidate
    return cwd


def ensure_apify_client() -> None:
    if importlib.util.find_spec("apify_client") is not None:
        return
    if os.getenv("MKT_APIFY_BOOTSTRAPPED") == "1":
        raise RuntimeError("apify-client is still unavailable after virtualenv bootstrap")

    venv_dir = project_root() / "workspace" / ".venvs" / "mkt-apify-competitor-social-analyzer"
    python_name = "python.exe" if os.name == "nt" else "python"
    venv_python = venv_dir / ("Scripts" if os.name == "nt" else "bin") / python_name
    if not venv_python.exists():
        subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
    dependency_check = subprocess.run(
        [str(venv_python), "-c", "import apify_client"],
        capture_output=True,
        check=False,
    )
    if dependency_check.returncode != 0:
        subprocess.run(
            [str(venv_python), "-m", "pip", "install", "--disable-pip-version-check", "apify-client"],
            check=True,
        )
    next_env = os.environ.copy()
    next_env["MKT_APIFY_BOOTSTRAPPED"] = "1"
    os.execve(
        str(venv_python),
        [str(venv_python), str(Path(__file__).resolve()), *sys.argv[1:]],
        next_env,
    )


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2, default=str)
        handle.write("\n")


def load_token() -> str | None:
    token = os.getenv("APIFY_TOKEN")
    if token:
        return token

    cwd = Path.cwd().resolve()
    candidates = [candidate / ".env" for candidate in (cwd, *cwd.parents)]
    script_path = Path(__file__).resolve()
    candidates.extend(parent / ".env" for parent in script_path.parents)
    for env_path in candidates:
        if not env_path.is_file():
            continue
        for line in env_path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "=" not in stripped:
                continue
            key, value = stripped.split("=", 1)
            if key.strip() == "APIFY_TOKEN":
                return value.strip().strip('"').strip("'") or None
    return None


def normalize_tiktok_handle(value: str) -> str:
    value = value.strip()
    if "tiktok.com" in value:
        path_parts = [part for part in urlparse(value).path.split("/") if part]
        for part in path_parts:
            if part.startswith("@"):
                return part[1:]
    return value.lstrip("@").strip("/")


def validate_config(config: dict[str, Any], max_posts_override: int | None) -> dict[str, Any]:
    competitors = config.get("competitors")
    if not isinstance(competitors, list) or not competitors:
        raise ValueError("'competitors' must be a non-empty array")

    max_posts = max_posts_override if max_posts_override is not None else config.get("max_posts", 10)
    if not isinstance(max_posts, int) or not 1 <= max_posts <= 500:
        raise ValueError("max_posts must be an integer from 1 to 500")

    clean_competitors = []
    seen_names = set()
    for index, competitor in enumerate(competitors, start=1):
        if not isinstance(competitor, dict):
            raise ValueError(f"competitors[{index}] must be an object")
        name = str(competitor.get("name", "")).strip()
        channels = competitor.get("channels")
        if not name or not isinstance(channels, dict) or not channels:
            raise ValueError(f"competitors[{index}] requires name and channels")
        if name in seen_names:
            raise ValueError(f"duplicate competitor name: {name}")
        seen_names.add(name)

        clean_channels = {}
        for platform, target in channels.items():
            platform = str(platform).lower().strip()
            if platform not in SUPPORTED_PLATFORMS:
                raise ValueError(f"unsupported platform '{platform}' for {name}")
            target = str(target).strip()
            if not target:
                raise ValueError(f"empty {platform} target for {name}")
            clean_channels[platform] = target
        clean_competitors.append({"name": name, "channels": clean_channels})

    overrides = config.get("actor_overrides", {})
    if not isinstance(overrides, dict):
        raise ValueError("actor_overrides must be an object")
    for platform in overrides:
        if platform not in SUPPORTED_PLATFORMS:
            raise ValueError(f"unsupported actor override platform: {platform}")

    older_than_raw = config.get("older_than")
    older_than = str(older_than_raw).strip() if older_than_raw is not None else None

    return {
        "competitors": clean_competitors,
        "max_posts": max_posts,
        "newer_than": str(config.get("newer_than", "30 days")).strip() or "30 days",
        "older_than": older_than or None,
        "actor_overrides": {str(key): str(value) for key, value in overrides.items()},
    }


def date_range_from_newer_than(newer_than: str) -> tuple[str, str]:
    match = re.fullmatch(r"\s*(\d+)\s+days?\s*", newer_than, flags=re.IGNORECASE)
    if not match:
        raise ValueError(
            "api-ninja/facebook-pages-scraper requires newer_than in the form 'N days'"
        )
    end_date = datetime.now(timezone.utc).date()
    start_date = end_date - timedelta(days=int(match.group(1)))
    return start_date.isoformat(), end_date.isoformat()


def actor_input(
    platform: str,
    target: str,
    max_posts: int,
    newer_than: str,
    older_than: str | None,
    actor_id: str,
) -> dict[str, Any]:
    if platform == "instagram":
        return {
            "directUrls": [target],
            "resultsType": "posts",
            "resultsLimit": max_posts,
            "onlyPostsNewerThan": newer_than,
            "addParentData": True,
        }
    if platform == "facebook":
        if older_than and actor_id != ACTORS["facebook"]:
            raise ValueError("older_than is currently supported only by the default Facebook Actor")
        if actor_id == "khadinakbar/facebook-posts-scraper":
            start_date, _ = date_range_from_newer_than(newer_than)
            return {
                "startUrls": [{"url": target}],
                "resultsLimit": max_posts,
                "maxPostsPerSource": max_posts,
                "scrapeDetails": False,
                "fallbackProvider": "auto",
                "onlyPostsNewerThan": start_date,
                "includeRawHtml": False,
                "proxyConfiguration": {
                    "useApifyProxy": True,
                    "apifyProxyGroups": ["RESIDENTIAL"],
                },
            }
        if actor_id == "api-ninja/facebook-pages-scraper":
            start_date, end_date = date_range_from_newer_than(newer_than)
            return {
                "urls": [target],
                "type": "posts",
                # The Actor schema enforces a minimum of 20 even when the
                # requested analysis limit is lower.
                "maxResults": max(20, max_posts),
                "parseAllResults": False,
                "startDate": start_date,
                "endDate": end_date,
            }
        run_input = {
            "startUrls": [{"url": target}],
            "resultsLimit": max_posts,
            "captionText": False,
            "onlyPostsNewerThan": newer_than,
        }
        if older_than:
            run_input["onlyPostsOlderThan"] = older_than
        return run_input
    if platform == "tiktok":
        return {
            "profiles": [normalize_tiktok_handle(target)],
            "profileScrapeSections": ["videos"],
            "profileSorting": "latest",
            "resultsPerPage": max_posts,
            "oldestPostDateUnified": newer_than,
            "excludePinnedPosts": False,
            "shouldDownloadVideos": False,
            "shouldDownloadCovers": False,
            "commentsPerPost": 0,
        }
    if platform == "youtube":
        return {
            "startUrls": [{"url": target}],
            "maxResults": max_posts,
            "maxResultsShorts": 0,
            "maxResultStreams": 0,
            "oldestPostDate": newer_than,
            "sortVideosBy": "NEWEST",
        }
    raise ValueError(f"unsupported platform: {platform}")


def build_plan(config: dict[str, Any]) -> list[dict[str, Any]]:
    plan = []
    for competitor in config["competitors"]:
        for platform, target in competitor["channels"].items():
            actor_id = config["actor_overrides"].get(platform, ACTORS[platform])
            plan.append({
                "competitor": competitor["name"],
                "platform": platform,
                "target": target,
                "actor_id": actor_id,
                "run_input": actor_input(
                    platform,
                    target,
                    config["max_posts"],
                    config["newer_than"],
                    config["older_than"],
                    actor_id,
                ),
            })
    return plan


def numeric(value: Any) -> float:
    if value is None or isinstance(value, bool):
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().lower().replace(",", "")
    match = re.fullmatch(r"(-?\d+(?:\.\d+)?)\s*([kmb])?", text)
    if not match:
        return 0.0
    multiplier = {None: 1, "k": 1_000, "m": 1_000_000, "b": 1_000_000_000}[match.group(2)]
    return float(match.group(1)) * multiplier


def first_value(item: dict[str, Any], keys: tuple[str, ...], default: Any = None) -> Any:
    for key in keys:
        current: Any = item
        for part in key.split("."):
            if not isinstance(current, dict) or part not in current:
                current = None
                break
            current = current[part]
        if current not in (None, "", [], {}):
            return current
    return default


def normalize_item(item: dict[str, Any], run_meta: dict[str, Any]) -> dict[str, Any]:
    likes = numeric(first_value(item, (
        "likesCount", "likeCount", "likes", "diggCount", "stats.diggCount", "reactionsCount",
        "reactions_count",
    )))
    comments = numeric(first_value(item, (
        "commentsCount", "commentCount", "comments", "stats.commentCount", "comments_count",
    )))
    shares = numeric(first_value(item, (
        "sharesCount", "shareCount", "shares", "stats.shareCount", "reshare_count",
    )))
    views = numeric(first_value(item, (
        "viewCount", "viewsCount", "views", "playCount", "videoPlayCount", "stats.playCount",
    )))
    text = str(first_value(item, (
        "caption", "text", "title", "description", "message", "content", "video.text",
    ), ""))
    url = str(first_value(item, (
        "url", "postUrl", "videoUrl", "webVideoUrl", "facebookUrl", "video.url",
    ), ""))
    published_at = first_value(item, (
        "timestamp", "createTimeISO", "publishedAt", "date", "time", "createTime", "video.createTime",
    ))
    author = str(first_value(item, (
        "ownerUsername", "username", "channelName", "author.name", "pageName", "video.author.username",
    ), ""))
    content_type = str(first_value(item, (
        "type", "productType", "mediaType", "video.type",
    ), "unknown"))
    engagement = likes + comments + shares
    engagement_rate = engagement / views * 100 if views > 0 else None
    return {
        "competitor": run_meta["competitor"],
        "platform": run_meta["platform"],
        "actor_id": run_meta["actor_id"],
        "target": run_meta["target"],
        "author": author,
        "content_type": content_type,
        "text": text,
        "url": url,
        "published_at": published_at,
        "views": round(views),
        "likes": round(likes),
        "comments": round(comments),
        "shares": round(shares),
        "engagement": round(engagement),
        "engagement_rate_by_view": round(engagement_rate, 4) if engagement_rate is not None else None,
    }


def is_diagnostic_item(item: dict[str, Any]) -> bool:
    if item.get("error"):
        return True
    text = str(first_value(item, ("text", "message", "errorDescription"), "")).lower()
    return text.startswith("no posts extracted.")


def theme_tokens(records: list[dict[str, Any]], limit: int = 12) -> list[dict[str, Any]]:
    counter: Counter[str] = Counter()
    for record in records:
        words = re.findall(r"[^\W\d_]{3,}", record.get("text", "").lower(), flags=re.UNICODE)
        counter.update(word for word in words if word not in STOPWORDS)
    return [{"term": term, "count": count} for term, count in counter.most_common(limit)]


def summarize(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        groups[(record["competitor"], record["platform"])].append(record)

    summaries = []
    for (competitor, platform), items in sorted(groups.items()):
        total_views = sum(item["views"] for item in items)
        total_engagement = sum(item["engagement"] for item in items)
        top_posts = sorted(items, key=lambda item: (item["views"], item["engagement"]), reverse=True)[:5]
        summaries.append({
            "competitor": competitor,
            "platform": platform,
            "items": len(items),
            "total_views": total_views,
            "average_views": round(total_views / len(items), 2) if items else 0,
            "total_likes": sum(item["likes"] for item in items),
            "total_comments": sum(item["comments"] for item in items),
            "total_shares": sum(item["shares"] for item in items),
            "total_engagement": total_engagement,
            "engagement_rate_by_view": round(total_engagement / total_views * 100, 4) if total_views else None,
            "themes": theme_tokens(items),
            "top_posts": top_posts,
        })
    return summaries


def format_number(value: Any) -> str:
    if value is None:
        return "chưa có"
    if isinstance(value, float) and not value.is_integer():
        formatted = f"{value:,.2f}"
        return formatted.replace(",", "_").replace(".", ",").replace("_", ".")
    return f"{int(value):,}".replace(",", ".")


def markdown_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Báo Cáo Kênh Mạng Xã Hội Đối Thủ",
        "",
        f"- Thu thập lúc: {payload['generated_at']}",
        f"- Số Actor run: {len(payload['runs'])}",
        f"- Tổng bản ghi chuẩn hóa: {len(payload['records'])}",
        "",
        "## Benchmark",
        "",
        "| Đối thủ | Nền tảng | Nội dung | Tổng view | View TB | Tương tác | ER/view |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for summary in payload["summaries"]:
        rate = summary["engagement_rate_by_view"]
        rate_text = f"{rate:.2f}%" if rate is not None else "chưa có"
        lines.append(
            f"| {summary['competitor']} | {summary['platform']} | {summary['items']} | "
            f"{format_number(summary['total_views'])} | {format_number(summary['average_views'])} | "
            f"{format_number(summary['total_engagement'])} | {rate_text} |"
        )

    for summary in payload["summaries"]:
        lines.extend(["", f"## {summary['competitor']} — {summary['platform']}", ""])
        themes = ", ".join(item["term"] for item in summary["themes"]) or "chưa đủ dữ liệu"
        lines.append(f"- Từ khóa xuất hiện nhiều: {themes}")
        lines.append("- Top nội dung theo view, sau đó theo tương tác:")
        for post in summary["top_posts"]:
            title = post["text"].replace("\n", " ").strip()[:100] or "Không có caption/title"
            link = f" — {post['url']}" if post["url"] else ""
            lines.append(
                f"  - {title}: {format_number(post['views'])} view, "
                f"{format_number(post['engagement'])} tương tác{link}"
            )

    lines.extend([
        "",
        "## Lưu ý dữ liệu",
        "",
        "- Đây là snapshot tại thời điểm chạy, không phải dữ liệu lịch sử tăng trưởng.",
        "- Field không được Actor trả về được giữ là `chưa có`, không được suy đoán.",
        "- So sánh chéo nền tảng chỉ mang tính định hướng vì cách tính view và tương tác khác nhau.",
        "",
    ])
    return "\n".join(lines)


def load_mock_runs(path: Path) -> list[dict[str, Any]]:
    payload = read_json(path)
    runs = payload.get("runs") if isinstance(payload, dict) else None
    if not isinstance(runs, list):
        raise ValueError("mock data must contain a 'runs' array")
    for run in runs:
        if not isinstance(run, dict) or not isinstance(run.get("items"), list):
            raise ValueError("each mock run requires an items array")
    return runs


def live_runs(
    plan: list[dict[str, Any]],
    token: str,
    output_dir: Path,
    run_timeout: int,
    max_charge_usd: float,
) -> list[dict[str, Any]]:
    try:
        from apify_client import ApifyClient
    except ImportError as error:
        raise RuntimeError("apify-client is unavailable after dependency bootstrap") from error

    import inspect

    client = ApifyClient(token=token)
    collected = []
    raw_dir = output_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    for index, planned in enumerate(plan, start=1):
        print(
            f"[{index}/{len(plan)}] {planned['competitor']} / {planned['platform']} "
            f"via {planned['actor_id']}",
            file=sys.stderr,
        )
        actor_client = client.actor(planned["actor_id"])
        call_kwargs: dict[str, Any] = {
            "run_input": planned["run_input"],
            "wait_duration": timedelta(seconds=run_timeout),
            "run_timeout": timedelta(seconds=run_timeout),
            "max_items": planned["run_input"].get("resultsLimit")
            or planned["run_input"].get("resultsPerPage")
            or planned["run_input"].get("maxResults"),
        }
        if "max_total_charge_usd" in inspect.signature(actor_client.call).parameters:
            call_kwargs["max_total_charge_usd"] = Decimal(str(max_charge_usd))
        run = actor_client.call(**call_kwargs)
        if run is None:
            raise RuntimeError(f"Actor returned no run: {planned['actor_id']}")
        status = str(run.status)
        if not status.endswith("SUCCEEDED"):
            raise RuntimeError(f"Actor run failed: {planned['actor_id']} status={status}")
        dataset_id = str(run.default_dataset_id or "")
        if not dataset_id:
            raise RuntimeError(f"Actor has no default dataset: {planned['actor_id']}")
        items = list(client.dataset(dataset_id).iterate_items(clean=True))
        raw_name = f"{index:02d}-{planned['competitor']}-{planned['platform']}.json"
        raw_name = re.sub(r"[^A-Za-z0-9._-]+", "-", raw_name)
        write_json(raw_dir / raw_name, items)
        collected.append({**planned, "dataset_id": dataset_id, "items": items})
    return collected


def main() -> int:
    args = parse_args()
    if args.check_deps:
        ensure_apify_client()
        from importlib.metadata import version

        print(json.dumps({"status": "ok", "apify_client_version": version("apify-client")}))
        return 0
    if not args.input or not args.output_dir:
        raise ValueError("--input and --output-dir are required unless --check-deps is used")
    input_path = Path(args.input).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()
    config = validate_config(read_json(input_path), args.max_posts)
    plan = build_plan(config)

    if args.dry_run:
        write_json(output_dir / "planned-runs.json", {"runs": plan})
        print(json.dumps({"status": "dry-run", "runs": len(plan), "output_dir": str(output_dir)}))
        return 0

    if args.mock_data:
        run_results = load_mock_runs(Path(args.mock_data).expanduser().resolve())
    else:
        token = load_token()
        if not token:
            print("Error: APIFY_TOKEN is missing. Add it to the process environment or workspace .env.", file=sys.stderr)
            return 2
        ensure_apify_client()
        run_results = live_runs(plan, token, output_dir, args.run_timeout, args.max_charge_usd)

    records = []
    run_summaries = []
    for run in run_results:
        meta = {
            "competitor": str(run.get("competitor", "Unknown")),
            "platform": str(run.get("platform", "unknown")),
            "actor_id": str(run.get("actor_id", "mock")),
            "target": str(run.get("target", "")),
        }
        raw_items = [item for item in run.get("items", []) if isinstance(item, dict)]
        items = [item for item in raw_items if not is_diagnostic_item(item)]
        records.extend(normalize_item(item, meta) for item in items)
        run_summaries.append({
            **meta,
            "items": len(items),
            "raw_items": len(raw_items),
            "dataset_id": run.get("dataset_id"),
        })

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "config": config,
        "runs": run_summaries,
        "records": records,
        "summaries": summarize(records),
    }
    write_json(output_dir / "normalized-data.json", payload)
    report_path = output_dir / "competitor-social-report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(markdown_report(payload), encoding="utf-8")
    print(json.dumps({
        "status": "ok",
        "runs": len(run_summaries),
        "records": len(records),
        "report": str(report_path),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(1)
