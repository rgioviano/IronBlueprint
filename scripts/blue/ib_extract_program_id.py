#!/usr/bin/env python3
"""ib_extract_program_id.py: pull IronBlueprint program IDs (24-char hex Mongo ObjectIds) out of a bug
report's Slack text, its URLs, and OCR of its screenshots. Offline: no network, no secrets.

Sources, in order:
  url           an ID inside a link, e.g. app.iron-blueprint.com/programs/view/6ad8f20fe2a7801835f5b603
  text          an ID typed in the message text
  image:<file>  an ID read by OCR from a screenshot. Pass 1 crops the browser address bar (top 4, 6, 8,
                10 and 12% of the height), upscales it 4x in grayscale and looks only for the
                ".../program(s)/[view/]<id>" URL. Pass 2 (only if pass 1 confirms nothing) reads the
                whole page at 2x grayscale, then 3x. If the same screenshot is given at two sizes
                (shot.png + shot-full.png, or a preview and the original) only the largest is read.
                Common OCR swaps are fixed (O/o -> 0, l/I/| -> 1) only when the fixed string is valid
                24-char hex AND its ObjectId timestamp (first 8 hex) falls between 2025-01-01 and now.
                An OCR ID is reported only when at least 2 reads agree exactly. Anything else goes to
                stderr as "UNCERTAIN <id> image:<file>" and does NOT count as found: small or blurry
                screenshots misread f/1 and a/3, so a guessed ID must never go on a card. An image under
                1600 px wide with no confirmed ID also prints "LOW_RES ..." to stderr: Slack's
                preview copies are 1024x576 and their address bar cannot be read reliably.

Usage:
  python3 ib_extract_program_id.py --text "<slack message text>" shot1.png shot2.png
  python3 ib_extract_program_id.py --text-file msg.txt --image shot.png --json
Output: one line per ID and source: "<id> <source>" (or JSON {found, uncertain} with --json). The same ID found in
several sources is printed once per source; IDs are lowercased.
Exit: 0 at least one ID found, 4 none found, 2 bad input (missing image, tesseract not installed).
tesseract: uses $IB_TESSERACT, else `tesseract` on PATH, else /home/box/.local/bin/tesseract
(user-space install of tesseract 5.5.0 on the box).
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile

HEX24 = re.compile(r"(?<![0-9A-Za-z])[0-9a-fA-F]{24}(?![0-9A-Za-z])")
# OCR candidates: hex plus the characters OCR commonly swaps in for 0 and 1
OCR_CAND = re.compile(r"(?<![0-9A-Za-z])[0-9a-fA-FOoIl|]{24}(?![0-9A-Za-z])")
SWAPS = str.maketrans({"O": "0", "o": "0", "I": "1", "l": "1", "|": "1"})
URL = re.compile(r"<?(?:https?://|www\.)[^\s<>|]+|[\w.-]+\.[a-z]{2,}/[^\s<>|]+|/programs?/[^\s<>|]+", re.I)


class BadInput(Exception):
    pass


def find_tesseract():
    for c in (os.environ.get("IB_TESSERACT"), shutil.which("tesseract"), "/home/box/.local/bin/tesseract"):
        if c and os.path.exists(c) and os.access(c, os.X_OK):
            return c
    raise BadInput("tesseract not installed (expected on PATH or /home/box/.local/bin/tesseract)")


def from_text(text):
    out = []
    urls = [m.group(0) for m in URL.finditer(text or "")]
    for u in urls:
        out += [(m.group(0).lower(), "url") for m in HEX24.finditer(u)]
    rest = URL.sub(" ", text or "")
    out += [(m.group(0).lower(), "text") for m in HEX24.finditer(rest)]
    return out


def fix_ocr(token):
    fixed = token.translate(SWAPS)
    return fixed.lower() if re.fullmatch(r"[0-9a-fA-F]{24}", fixed) else None


OCR_WHITELIST = "tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789./-:_|"
# Pass 1, address bar (Ryne 2026-10-22: the program ID is always in the browser URL of a full screenshot):
# crop the top strip (4-12% of the height, so it works with and without a tab/bookmarks bar), upscale 4x,
# grayscale, and look ONLY for the ".../program(s)/[view/]<id>" pattern.
BAR_PCTS = (4, 6, 8, 10, 12)
BAR_PSMS = ("6", "7", "11")
# Pass 2, whole page (used only if pass 1 confirms nothing): 2x grayscale first, then 3x re-reads.
PAGE_VARIANTS = [(2, "3", False), (2, "11", False), (3, "6", False), (3, "11", True)]
MIN_VOTES = 2   # an OCR ID is reported only when at least 2 independent reads agree exactly
EARLIEST = 1735689600  # 2025-01-01 UTC: an IronBlueprint ObjectId's first 8 hex are its creation time
LOW_RES_W = 1600  # Slack's preview copies are 1024 wide; a Retina original is 2048+ wide
PROGRAM_URL = re.compile(r"programs?[/y]?(?:view[/y]?)?([0-9A-Za-z|]{24})(?![0-9A-Za-z])", re.I)
SIZE_TAGS = re.compile(r"[-_. ](?:full|orig|original|preview|thumb|small|\d{3,4}(?:x\d{3,4})?)$", re.I)


def plausible(oid, now=None):
    """Mongo ObjectIds start with a 4-byte creation timestamp; reject OCR garbage outside IB's lifetime."""
    import time
    t = int(oid[:8], 16)
    return EARLIEST <= t <= (now or time.time()) + 86400


def image_size(path):
    try:
        from PIL import Image
        with Image.open(path) as im:
            return im.size
    except ImportError:
        p = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                            "stream=width,height", "-of", "csv=p=0", path], capture_output=True, text=True)
        try:
            w, h = p.stdout.strip().split(",")[:2]
            return int(w), int(h)
        except ValueError:
            raise BadInput(f"cannot read image {path}")
    except Exception as e:
        raise BadInput(f"cannot read image {path}: {e}")


def prefer_full_size(paths):
    """Same screenshot given more than once (e.g. shot.png and shot-full.png, or the Slack preview and the
    original)? Keep only the version with the most pixels. Returns [(path, (w, h), [skipped paths])]."""
    groups = {}
    for p in paths:
        stem = SIZE_TAGS.sub("", os.path.splitext(os.path.basename(p))[0]).lower()
        groups.setdefault(stem, []).append((p, image_size(p)))
    out = []
    for items in groups.values():
        items.sort(key=lambda x: -(x[1][0] * x[1][1]))
        out.append((items[0][0], items[0][1], [x[0] for x in items[1:]]))
    return out


def load_gray(path):
    try:
        from PIL import Image
    except ImportError:
        return None
    try:
        with Image.open(path) as im:
            return im.convert("L")
    except Exception as e:
        raise BadInput(f"cannot read image {path}: {e}")


def prep(path, gray, scale, top_pct, out):
    """Grayscale + upscale (Pillow, else ffmpeg). top_pct: crop the top strip of that % first."""
    if gray is not None:
        from PIL import Image
        im = gray.crop((0, 0, gray.width, max(1, gray.height * top_pct // 100))) if top_pct else gray
        im.resize((im.width * scale, im.height * scale), Image.LANCZOS).save(out)
        return out
    if not shutil.which("ffmpeg"):
        raise BadInput("need Pillow or ffmpeg to preprocess images")
    vf = (f"crop=iw:ih*{top_pct}/100:0:0," if top_pct else "") + f"scale=iw*{scale}:ih*{scale}:flags=lanczos,format=gray"
    p = subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", path, "-vf", vf, out], capture_output=True, text=True)
    if p.returncode:
        raise BadInput(f"cannot read image {path}: {p.stderr.strip()[:120]}")
    return out


def clean_lines(text):
    for line in text.splitlines():
        line = re.sub(r"\s*/\s*", "/", line)
        # OCR sometimes drops a space inside a long ID ("6ad0dc947 6ebc30afff85e66"); also try with
        # single spaces between hex-like characters removed. A hit still has to be exactly 24 chars.
        yield line
        yield re.sub(r"(?<=[0-9a-fA-FOoIl|]) (?=[0-9a-fA-FOoIl|])", "", line)


def ids_in_url_text(text):
    found = []
    for line in clean_lines(text):
        for m in PROGRAM_URL.finditer(line):
            f = fix_ocr(m.group(1))
            if f and plausible(f) and f not in found:
                found.append(f)
    return found


def ids_in_ocr_text(text):
    found = []
    for line in clean_lines(text):
        for m in OCR_CAND.finditer(line):
            f = fix_ocr(m.group(0))
            if f and plausible(f) and f not in found:
                found.append(f)
    return found


def tally(votes):
    """IDs read identically by >= MIN_VOTES reads. Near-identical rivals with equal votes cancel out."""
    ranked = sorted(votes.items(), key=lambda kv: -kv[1])
    keep = []
    for i, v in ranked:
        if v < MIN_VOTES:
            continue
        close = [k for k in keep if sum(a != b for a, b in zip(i, k)) <= 6]
        if close:
            if v == votes[close[0]]:
                keep.remove(close[0])
            continue
        keep.append(i)
    return keep, [i for i, _ in ranked if i not in keep]


def run_tess(tess, img, psm, wl):
    cmd = [tess, img, "stdout", "--psm", psm, "-l", "eng"] + (["-c", OCR_WHITELIST] if wl else [])
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else ""


def from_image(path, tess, tmpdir):
    """Return (confirmed_ids, uncertain_ids, pass_name)."""
    gray = load_gray(path)
    base = os.path.basename(path)
    # pass 1: address bar
    votes = {}
    for pct in BAR_PCTS:
        img = prep(path, gray, 4, pct, os.path.join(tmpdir, f"bar{pct}-{base}.png"))
        for psm in BAR_PSMS:
            for i in ids_in_url_text(run_tess(tess, img, psm, True)):
                votes[i] = votes.get(i, 0) + 1
    ok, unsure = tally(votes)
    if ok:
        return ok, unsure, "address-bar"
    # pass 2: whole page
    pvotes = {}
    for n, (scale, psm, wl) in enumerate(PAGE_VARIANTS):
        img = prep(path, gray, scale, 0, os.path.join(tmpdir, f"page{n}-{base}.png"))
        for i in ids_in_ocr_text(run_tess(tess, img, psm, wl)):
            pvotes[i] = pvotes.get(i, 0) + 1
    ok2, unsure2 = tally(pvotes)
    return ok2, unsure + [u for u in unsure2 if u not in unsure], "page" if ok2 else "none"


def main(argv=None):
    ap = argparse.ArgumentParser(prog="ib_extract_program_id.py",
                                 description="Find IronBlueprint program IDs (24-char hex) in bug text, URLs and screenshot OCR. Offline.",
                                 epilog="Exit: 0 found, 4 none found, 2 bad input.")
    ap.add_argument("images", nargs="*", help="screenshot paths")
    ap.add_argument("--text", default="", help="Slack message text")
    ap.add_argument("--text-file", help="file holding the message text")
    ap.add_argument("--image", action="append", default=[], help="screenshot path (repeatable)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    text = a.text
    if a.text_file:
        try:
            text += "\n" + open(a.text_file, encoding="utf-8").read()
        except OSError as e:
            raise BadInput(f"cannot open {a.text_file}: {e.strerror}")
    images = a.images + a.image
    if not text.strip() and not images:
        ap.error("give --text/--text-file and/or image paths")
    for im in images:
        if not os.path.isfile(im):
            raise BadInput(f"image not found: {im}")

    hits, uncertain, low_res = from_text(text), [], []
    if images:
        tess = find_tesseract()
        with tempfile.TemporaryDirectory(prefix="ibpid-") as td:
            for im, size, skipped in prefer_full_size(images):
                for sk in skipped:
                    print(f"SKIPPED {os.path.basename(sk)}: a larger copy ({os.path.basename(im)}, {size[0]}x{size[1]}) was given",
                          file=sys.stderr)
                ok, unsure, _ = from_image(im, tess, td)
                hits += [(i, f"image:{os.path.basename(im)}") for i in ok]
                uncertain += [(i, f"image:{os.path.basename(im)}") for i in unsure]
                if not ok and size[0] < LOW_RES_W:
                    low_res.append(f"LOW_RES {os.path.basename(im)} is {size[0]}x{size[1]}, likely Slack's downscaled "
                                   f"preview; the address bar is too small to read. Get the full-size original.")
    seen, uniq = set(), []
    for h in hits:
        if h not in seen:
            seen.add(h); uniq.append(h)
    if a.json:
        print(json.dumps({"found": [{"program_id": i, "source": s} for i, s in uniq],
                          "uncertain": [{"program_id": i, "source": s} for i, s in uncertain],
                          "low_res": low_res}))
    else:
        for i, s in uniq:
            print(f"{i} {s}")
        for line in low_res:
            print(line, file=sys.stderr)
        for i, s in uncertain:
            print(f"UNCERTAIN {i} {s} (OCR reads disagree; do not use, read the screenshot or ask Ryne)", file=sys.stderr)
        if not uniq:
            print("NO_PROGRAM_ID found in text, URLs or images", file=sys.stderr)
    return 0 if uniq else 4


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except BadInput as e:
        print(f"ib_extract_program_id bad input: {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"ib_extract_program_id error: {e}", file=sys.stderr)
        sys.exit(2)
