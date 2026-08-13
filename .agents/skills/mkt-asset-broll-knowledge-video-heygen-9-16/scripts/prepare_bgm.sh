#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 3 || $# -gt 5 ]]; then
  echo "Usage: prepare_bgm.sh INPUT_AUDIO TOTAL_SECONDS OUTPUT_MP3 [FADE_IN_SECONDS] [FADE_OUT_SECONDS]" >&2
  exit 2
fi

input_audio=$1
total_seconds=$2
output_mp3=$3
fade_in_seconds=${4:-1.2}
fade_out_seconds=${5:-2.0}

if [[ ! -f "$input_audio" ]]; then
  echo "Input audio not found: $input_audio" >&2
  exit 2
fi

if ! awk -v total="$total_seconds" -v fade_in="$fade_in_seconds" -v fade_out="$fade_out_seconds" \
  'BEGIN { exit !(total > 0 && fade_in >= 0 && fade_out >= 0 && total > fade_out) }'; then
  echo "Invalid duration/fade values" >&2
  exit 2
fi

fade_out_start=$(awk -v total="$total_seconds" -v fade_out="$fade_out_seconds" \
  'BEGIN { printf "%.3f", total - fade_out }')

mkdir -p "$(dirname "$output_mp3")"

ffmpeg -hide_banner -loglevel error -y \
  -stream_loop -1 -i "$input_audio" \
  -t "$total_seconds" \
  -af "afade=t=in:st=0:d=${fade_in_seconds},afade=t=out:st=${fade_out_start}:d=${fade_out_seconds}" \
  -ar 48000 -ac 2 -c:a libmp3lame -b:a 192k \
  "$output_mp3"

actual_duration=$(ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 "$output_mp3")
echo "Prepared BGM: $output_mp3 (${actual_duration}s)"
