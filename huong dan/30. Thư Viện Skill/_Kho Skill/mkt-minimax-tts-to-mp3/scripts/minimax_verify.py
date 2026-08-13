#!/usr/bin/env python3
"""Pre-flight verification for MiniMax TTS env.

Run BEFORE minimax_tts.py to catch the 3 most common misconfigurations
in one shot, instead of debugging them one error message at a time:

  1. Missing MINIMAX_API_KEY / MINIMAX_GROUP_ID / MINIMAX_VOICE_ID in .env
  2. Wrong API key (server returns 1004 login fail)
  3. Missing GroupId (server returns 2013 invalid params, empty field)
     — looks like a "voice id" error but is NOT; do not be fooled.

Usage:
    python3 minimax_verify.py                # uses .env + default base
    python3 minimax_verify.py --base https://api.minimaxi.com

Exits 0 if all 3 vars present and a tiny TTS request succeeds. Exits 1
with a precise one-line error otherwise. Prints a compact JSON status
on success.
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request


def load_env_file(path=".env"):
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key, val = key.strip(), val.strip().strip("'\"")
            if key and val and key not in os.environ:
                os.environ[key] = val


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", default=None,
                   help="Override API base (default from MINIMAX_API_BASE or https://api.minimax.io)")
    p.add_argument("--voice-id", default=None,
                   help="Override MINIMAX_VOICE_ID (otherwise read from env)")
    args = p.parse_args()

    load_env_file()

    api_key = os.environ.get("MINIMAX_API_KEY", "").strip()
    group_id = os.environ.get("MINIMAX_GROUP_ID", "").strip()
    voice_id = (args.voice_id or os.environ.get("MINIMAX_VOICE_ID", "")).strip()
    base = (args.base or os.environ.get("MINIMAX_API_BASE", "https://api.minimax.io")).rstrip("/")

    missing = []
    if not api_key:
        missing.append("MINIMAX_API_KEY")
    if not group_id:
        missing.append("MINIMAX_GROUP_ID")
    if not voice_id:
        missing.append("MINIMAX_VOICE_ID")
    if missing:
        sys.exit(f"Missing env vars: {', '.join(missing)}")

    body = {
        "model": os.environ.get("MINIMAX_MODEL", "speech-02-turbo"),
        "text": "test",
        "stream": False,
        "voice_setting": {
            "voice_id": voice_id,
            "speed": 1.0,
            "vol": 1.0,
            "pitch": 0,
        },
        "audio_setting": {
            "sample_rate": 32000,
            "bitrate": 128000,
            "format": "mp3",
            "channel": 1,
        },
    }
    url = f"{base}/v1/t2a_v2?GroupId={group_id}"
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} from {base}: {e.read().decode('utf-8', 'replace')[:200]}")
    except urllib.error.URLError as e:
        sys.exit(f"Cannot reach {base}: {e.reason}")

    base_resp = payload.get("base_resp") or {}
    status = base_resp.get("status_code")
    if status not in (0, None):
        msg = base_resp.get("status_msg", "")
        # Disambiguate the most common 1004 vs 2013:
        if status == 1004:
            sys.exit(f"1004 login fail — MINIMAX_API_KEY is wrong/expired. server msg: {msg}")
        if status == 2013:
            if "voice" in msg.lower():
                sys.exit(f"2013 — voice id rejected. Check MINIMAX_VOICE_ID. server msg: {msg}")
            sys.exit(f"2013 invalid params — likely missing/wrong MINIMAX_GROUP_ID (NOT voice id). server msg: {msg}")
        sys.exit(f"MiniMax error {status}: {msg}")

    audio_hex = (payload.get("data") or {}).get("audio")
    if not audio_hex:
        sys.exit(f"No audio in verify response: {json.dumps(payload)[:300]}")

    print(json.dumps({
        "ok": True,
        "base": base,
        "voice_id": voice_id,
        "model": body["model"],
        "bytes": len(bytes.fromhex(audio_hex)),
        "group_id_len": len(group_id),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
