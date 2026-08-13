#!/usr/bin/env python3
"""Convert script text to MP3 voiceover using ElevenLabs Text-to-Speech API.

Usage:
    python3 elevenlabs_tts.py --text-file script.txt --out voiceover.mp3
    python3 elevenlabs_tts.py --text "Đọc câu này" --out voiceover.mp3 --voice-id <id>
    python3 elevenlabs_tts.py --text-file script.txt --out voiceover.mp3 --stability 0.5 --style 0.3

Stdout: JSON one-liner with {out, bytes, duration_ms, voice_id, model, chars_used}.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
import urllib.error
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


def get_audio_duration_ms(path: Path) -> int:
    """Use ffprobe to get duration in ms."""
    try:
        out = subprocess.check_output(
            [
                "ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1", str(path),
            ],
            stderr=subprocess.DEVNULL,
            timeout=10,
        )
        return int(float(out.decode().strip()) * 1000)
    except Exception:
        return 0


def tts_request(api_base: str, api_key: str, voice_id: str, text: str,
                model_id: str, stability: float, similarity_boost: float,
                style: float, use_speaker_boost: bool, timeout: int = 60) -> bytes:
    url = f"{api_base}/v1/text-to-speech/{voice_id}"
    body = json.dumps({
        "text": text,
        "model_id": model_id,
        "voice_settings": {
            "stability": stability,
            "similarity_boost": similarity_boost,
            "style": style,
            "use_speaker_boost": use_speaker_boost,
        },
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        try:
            err_body = json.loads(e.read())
        except Exception:
            err_body = {"raw": "non-json error body"}
        raise RuntimeError(f"ElevenLabs HTTP {e.code}: {json.dumps(err_body)}") from e


def split_text(text: str, max_chars: int = 5000) -> list[str]:
    """Split text into chunks of <= max_chars at sentence boundaries."""
    if len(text) <= max_chars:
        return [text]
    chunks = []
    # Split on sentence-ending punctuation or newline
    sentences = re.split(r'(?<=[.!?。！？])\s+|\n+', text)
    buf = ""
    for s in sentences:
        if not s.strip():
            continue
        if len(buf) + len(s) + 1 > max_chars and buf:
            chunks.append(buf.strip())
            buf = s
        else:
            buf = (buf + " " + s).strip() if buf else s
    if buf:
        chunks.append(buf.strip())
    return chunks


def concat_mp3(parts: list[Path], out: Path) -> None:
    """Concatenate MP3 files using ffmpeg concat demuxer."""
    list_file = out.parent / f".concat_{out.stem}.txt"
    list_file.write_text("\n".join(f"file '{p.resolve()}'" for p in parts))
    try:
        subprocess.run(
            [
                "ffmpeg", "-y", "-f", "concat", "-safe", "0",
                "-i", str(list_file), "-c", "copy", str(out),
            ],
            check=True, capture_output=True, timeout=120,
        )
    finally:
        list_file.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", help="Inline text (use instead of --text-file)")
    parser.add_argument("--text-file", help="Path to script text file")
    parser.add_argument("--out", required=True, help="Output MP3 path")
    parser.add_argument("--voice-id", help="Override ELEVENLABS_VOICE_ID")
    parser.add_argument("--model", help="Override ELEVENLABS_MODEL_ID")
    parser.add_argument("--api-base", help="Override ELEVENLABS_API_BASE")
    parser.add_argument("--stability", type=float, help="Voice settings: stability")
    parser.add_argument("--similarity-boost", type=float, help="Voice settings: similarity_boost")
    parser.add_argument("--style", type=float, help="Voice settings: style")
    parser.add_argument("--max-chars", type=int, default=5000, help="Max chars per request (ElevenLabs limit)")
    args = parser.parse_args()

    if not args.text and not args.text_file:
        print(json.dumps({"ok": False, "error": "must provide --text or --text-file"}))
        return 1

    # Load env
    env = load_env(Path.cwd() / ".env")
    api_key = env.get("ELEVENLABS_API_KEY") or os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print(json.dumps({"ok": False, "error": "ELEVENLABS_API_KEY missing in .env"}))
        return 1

    voice_id = args.voice_id or env.get("ELEVENLABS_VOICE_ID") or os.environ.get("ELEVENLABS_VOICE_ID", "K7ewtjKRNtwwt3lKQ6M0")
    model_id = args.model or env.get("ELEVENLABS_MODEL_ID") or os.environ.get("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2")
    api_base = args.api_base or env.get("ELEVENLABS_API_BASE") or os.environ.get("ELEVENLABS_API_BASE", "https://api.elevenlabs.io")
    stability = args.stability if args.stability is not None else float(env.get("ELEVENLABS_STABILITY", "0.35"))
    similarity_boost = args.similarity_boost if args.similarity_boost is not None else float(env.get("ELEVENLABS_SIMILARITY_BOOST", "0.75"))
    style = args.style if args.style is not None else float(env.get("ELEVENLABS_STYLE", "0.0"))
    use_speaker_boost = env.get("ELEVENLABS_USE_SPEAKER_BOOST", "true").lower() != "false"

    # Get text
    if args.text:
        text = args.text
    else:
        text = Path(args.text_file).read_text(encoding="utf-8").strip()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    # Split if needed
    chunks = split_text(text, max_chars=args.max_chars)
    print(f"[elevenlabs] text={len(text)} chars, chunks={len(chunks)}, voice={voice_id}, model={model_id}", file=sys.stderr)

    if len(chunks) == 1:
        audio = tts_request(api_base, api_key, voice_id, chunks[0], model_id,
                            stability, similarity_boost, style, use_speaker_boost)
        out.write_bytes(audio)
    else:
        part_paths = []
        for i, ch in enumerate(chunks):
            part_out = out.parent / f".{out.stem}_part{i}.mp3"
            audio = tts_request(api_base, api_key, voice_id, ch, model_id,
                                stability, similarity_boost, style, use_speaker_boost)
            part_out.write_bytes(audio)
            part_paths.append(part_out)
        concat_mp3(part_paths, out)
        for p in part_paths:
            p.unlink(missing_ok=True)

    # Stats
    bytes_out = out.stat().st_size
    duration_ms = get_audio_duration_ms(out)
    result = {
        "ok": True,
        "out": str(out),
        "bytes": bytes_out,
        "duration_ms": duration_ms,
        "voice_id": voice_id,
        "model": model_id,
        "chars_used": len(text),
        "chunks": len(chunks),
        "stability": stability,
        "similarity_boost": similarity_boost,
        "style": style,
    }
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
