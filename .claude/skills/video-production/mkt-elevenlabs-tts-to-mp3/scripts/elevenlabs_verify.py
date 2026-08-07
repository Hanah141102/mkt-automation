#!/usr/bin/env python3
"""Pre-flight verification for ElevenLabs TTS.

Loads .env from CWD, checks ELEVENLABS_API_KEY, then calls GET /v1/voices
to confirm: (a) key is valid, (b) ELEVENLABS_VOICE_ID exists in this account.

Usage:
    python3 elevenlabs_verify.py

Exits 0 on success, 1 on failure. Prints JSON one-liner with status.
"""
import json
import os
import sys
from pathlib import Path


def load_env(path: Path) -> dict[str, str]:
    env = {}
    if not path.exists():
        return env
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def main() -> int:
    env = load_env(Path.cwd() / ".env")
    api_key = env.get("ELEVENLABS_API_KEY") or os.environ.get("ELEVENLABS_API_KEY")
    voice_id = env.get("ELEVENLABS_VOICE_ID") or os.environ.get("ELEVENLABS_VOICE_ID", "K7ewtjKRNtwwt3lKQ6M0")
    api_base = env.get("ELEVENLABS_API_BASE") or os.environ.get("ELEVENLABS_API_BASE", "https://api.elevenlabs.io")

    if not api_key:
        print(json.dumps({"ok": False, "error": "ELEVENLABS_API_KEY missing in .env"}))
        return 1

    if len(api_key) < 32:
        print(json.dumps({"ok": False, "error": f"ELEVENLABS_API_KEY too short ({len(api_key)} chars, expected 32+)"}))
        return 1

    # Try GET /v1/voices to verify key + find voice id
    try:
        import urllib.request
        req = urllib.request.Request(
            f"{api_base}/v1/voices",
            headers={"xi-api-key": api_key, "Accept": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        print(json.dumps({"ok": False, "error": f"GET /v1/voices failed: {e}"}))
        return 1

    voices = data.get("voices", [])
    voice_ids = [v.get("voice_id") for v in voices]
    voice_found = voice_id in voice_ids

    if not voice_found:
        # Try EU base if default failed
        if "eu." not in api_base:
            try:
                req = urllib.request.Request(
                    "https://api.eu.elevenlabs.io/v1/voices",
                    headers={"xi-api-key": api_key, "Accept": "application/json"},
                )
                with urllib.request.urlopen(req, timeout=15) as resp:
                    data = json.loads(resp.read())
                    voices = data.get("voices", [])
                    voice_ids = [v.get("voice_id") for v in voices]
                    voice_found = voice_id in voice_ids
                    if voice_found:
                        api_base = "https://api.eu.elevenlabs.io"
            except Exception:
                pass

    result = {
        "ok": voice_found,
        "api_key_valid": True,
        "voice_id": voice_id,
        "voice_found": voice_found,
        "api_base": api_base,
        "voices_in_account": len(voice_ids),
        "error": None if voice_found else f"voice_id {voice_id} not in this account (have {len(voice_ids)} voices)",
    }
    print(json.dumps(result))
    return 0 if voice_found else 1


if __name__ == "__main__":
    sys.exit(main())
