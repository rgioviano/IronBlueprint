#!/usr/bin/env bash
# ib_media_fix.sh: check (and if needed fix) one downloaded bug screenshot/video before attaching it
# to the Basecamp card and the #bugs thread. Offline: ffmpeg/ffprobe only, no network, no secrets.
#
# Usage: ib_media_fix.sh <file> [out_dir]      (out_dir defaults to the file's folder)
#   image (png/jpg/jpeg/gif/webp/heic): verified with `file` (falls back to magic bytes + ffprobe
#         when `file` is not installed). Prints the path to attach.
#   video: verified with ffprobe (duration + video stream) and a full decode. If it is .mov or
#         over 10 MB it is transcoded to H.264/AAC .mp4 under 10 MB (two-pass, bitrate from the
#         duration, scaled down to 720p when taller). Prints the path to attach.
# Last line of stdout on success is always: ATTACH <path>
# Exit: 0 ready to attach, 2 usage / file missing or empty, 3 corrupt (re-download it),
#       4 transcode failed or could not get under 10 MB.
set -uo pipefail
LIMIT=10000000                   # 10 MB hard limit (decimal, safe for Slack and Basecamp)
TARGET=9000000                   # aim for 9 MB
die() { echo "$2" >&2; exit "$1"; }

[[ $# -ge 1 && "$1" != "-h" && "$1" != "--help" ]] || { sed -n '2,15p' "$0" | sed 's/^# \{0,1\}//'; [[ $# -ge 1 ]] && exit 0; exit 2; }
f="$1"; [[ -f "$f" ]] || die 2 "NOT FOUND: $f"
[[ -s "$f" ]] || die 2 "EMPTY: $f is 0 bytes (download failed, re-download)"
command -v ffprobe >/dev/null && command -v ffmpeg >/dev/null || die 2 "ffmpeg/ffprobe not installed"
out_dir="${2:-$(dirname "$f")}"; mkdir -p "$out_dir"
name="$(basename "$f")"; base="${name%.*}"; ext="$(echo "${name##*.}" | tr 'A-Z' 'a-z')"
size=$(stat -c %s "$f")

case "$ext" in
  png|jpg|jpeg|gif|webp|heic)
    if command -v file >/dev/null; then
      desc=$(file -b "$f")
      echo "$desc" | grep -qiE 'image|bitmap|PNG|JPEG|GIF|Web/P|HEIF' || die 3 "CORRUPT image: $f ($desc)"
    else
      magic=$(head -c 12 "$f" | od -An -tx1 | tr -d ' \n')
      case "$magic" in
        89504e47*|ffd8ff*|47494638*|52494646????????57454250*|????????66747970*) ;;
        *) die 3 "CORRUPT image: $f (bad header $magic)";;
      esac
      ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$f" >/dev/null 2>&1 \
        || [[ "$ext" == heic ]] || die 3 "CORRUPT image: $f (ffprobe cannot read it)"
    fi
    echo "OK image $f ($size bytes)"
    echo "ATTACH $f"; exit 0;;
esac

# video (or anything else ffprobe can read)
dur=$(ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$f" 2>/dev/null | head -1)
vh=$(ffprobe -v error -select_streams v:0 -show_entries stream=height -of default=nw=1:nk=1 "$f" 2>/dev/null | head -1)
[[ -n "$vh" && "$dur" =~ ^[0-9.]+$ ]] || die 3 "CORRUPT video: $f (ffprobe finds no readable video stream/duration; re-download the original)"
errs=$(ffmpeg -v error -xerror -i "$f" -f null - 2>&1 | head -5)
[[ -z "$errs" ]] || die 3 "CORRUPT video: $f (decode errors: $(echo "$errs" | head -1))"
has_audio=$(ffprobe -v error -select_streams a:0 -show_entries stream=index -of csv=p=0 "$f" 2>/dev/null | head -1)

if [[ "$ext" != "mov" && $size -le $LIMIT ]]; then
  echo "OK video $f ($size bytes, ${dur}s), no transcode needed"
  echo "ATTACH $f"; exit 0
fi

out="$out_dir/$base.mp4"; [[ "$(realpath -m "$out")" == "$(realpath "$f")" ]] && out="$out_dir/$base-fixed.mp4"
scale=(); [[ "$vh" -gt 720 ]] && scale=(-vf "scale=-2:720")
abr=0; aopt=(-an); [[ -n "$has_audio" ]] && { abr=96; aopt=(-c:a aac -b:a 96k); }
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
factor=100
for try in 1 2 3; do
  vbr=$(awk -v t=$TARGET -v d="$dur" -v a=$abr -v k=$factor 'BEGIN{v=int((t*8/d/1000 - a)*k/100); if(v<100)v=100; print v}')
  ffmpeg -y -v error -i "$f" "${scale[@]}" -c:v libx264 -preset medium -b:v ${vbr}k -pass 1 -passlogfile "$tmp/p" -an -f mp4 /dev/null \
   && ffmpeg -y -v error -i "$f" "${scale[@]}" -c:v libx264 -preset medium -b:v ${vbr}k -pass 2 -passlogfile "$tmp/p" \
        -pix_fmt yuv420p "${aopt[@]}" -movflags +faststart "$out" \
   || die 4 "TRANSCODE FAILED: $f"
  osize=$(stat -c %s "$out")
  if [[ $osize -lt $LIMIT ]]; then
    ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of csv=p=0 "$out" | grep -q h264 || die 4 "TRANSCODE FAILED: $out is not H.264"
    echo "FIXED video $f ($size bytes, .$ext) -> $out ($osize bytes, H.264 ${vbr}k, ${dur}s$([[ ${#scale[@]} -gt 0 ]] && echo ', scaled to 720p'))"
    echo "ATTACH $out"; exit 0
  fi
  factor=$((factor*80/100))
done
die 4 "TOO BIG: could not get $f under 10 MB after 3 tries (last $osize bytes)"
