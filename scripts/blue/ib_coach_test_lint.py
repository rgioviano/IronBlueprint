#!/usr/bin/env python3
"""ib_coach_test_lint.py: check the draft #ironblueprint (Achieve Slack) coach test post written
after an IronBlueprint dev meeting, before it goes to Ryne and again right before posting.

Checks (one line each, "CODE line N: detail"):
  NO_CHANNEL_TAG          first non-empty line does not start with <!channel>
  MISSING_SECTION         "Ready to test now" or "Coming soon, don't test yet" missing, or out of order
  EMPTY_SECTION           a section has no bullets (the bullet "None this time" counts)
  NO_PASS_CRITERIA        a Ready bullet has no "should" / "you should see" / "pass:"
  EMOJI                   emoji character or :shortcode: (times like 9:30 are fine)
  EM_DASH                 U+2014 em dash
  DEV_NAME                Divesh, Pradeep, Abhishek, Prabhjot, Ritik, Ajay, Suffescom (whole word)
  BASECAMP_LINK           "basecamp" / 3.basecamp.com
  SECRET_LIKE             xox[bpa]-, sk-, AKIA, or 32+ char base64/hex runs (24-char program IDs ok).
                          Only the first 4 characters are printed.
  NO_CLOSING              last line does not tell coaches to post broken items in #ironblueprint
                          with a screenshot or video, plus mention "program ID" (Ryne 2026-10-22)
  CHANGED_SINCE_APPROVAL  --approved given and draft differs (trailing whitespace ignored); short diff

Usage: ib_coach_test_lint.py <draft.md> [--approved <approved.md>]
Offline, standard library only, never posts.
Exit code: 0 good ("OK coach test post: N ready, M coming soon"), 1 problem lines, 2 bad input.
"""
import argparse, difflib, re, sys

READY = "ready to test now"
SOON_RE = re.compile(r"coming soon,\s*don['\u2019]t test yet", re.I)
BULLET = re.compile(r"^\s*(?:[-*\u2022]|\d+[.)])\s+(.*)$")
PASS_RX = re.compile(r"\bshould\b|you should see|pass:", re.I)
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u200D\u2300-\u23FF]")
SHORTCODE = re.compile(r"(?<![\w/]):[a-z0-9_+\-]*[a-z_][a-z0-9_+\-]*:(?![\w/])", re.I)
DEVS = re.compile(r"\b(divesh|pradeep|abhishek|prabhjot|ritik|ajay|suffescom)\b", re.I)
BASECAMP = re.compile(r"basecamp", re.I)
SECRET_RX = re.compile(r"xox[bpa]-[\w-]*|\bsk-[\w-]{4,}|\bAKIA[0-9A-Z]{4,}|(?<![A-Za-z0-9+/=])[A-Za-z0-9+/=]{32,}")
CLOSING = re.compile(r"#ironblueprint", re.I)
PROGID = re.compile(r"program id", re.I)
MEDIA = re.compile(r"screenshot|video|recording", re.I)


class BadInput(Exception):
    pass


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except (OSError, UnicodeDecodeError) as e:
        raise BadInput(f"cannot read {path}: {e}")
    if not text.strip():
        raise BadInput(f"{path} is empty")
    return text


def lint(text):
    lines = text.splitlines()
    probs = []
    add = lambda code, n, msg: probs.append((n, code, msg))
    nonempty = [(i + 1, l) for i, l in enumerate(lines) if l.strip()]
    first_n, first = nonempty[0]
    if not first.strip().startswith("<!channel>"):
        add("NO_CHANNEL_TAG", first_n, "first line must start with <!channel>")
    last_n, last = nonempty[-1]
    closing_ok = bool(CLOSING.search(last) and MEDIA.search(last) and PROGID.search(last))
    if not closing_ok:
        add("NO_CLOSING", last_n, "last line must ask coaches to post broken items in #ironblueprint with a screenshot or video, and to include the program ID when the screenshot lacks the web address")

    ready_n = soon_n = None
    section = None
    bullets = {"ready": [], "soon": []}
    for n, l in nonempty:
        if ready_n is None and READY in l.lower():
            ready_n, section = n, "ready"; continue
        if soon_n is None and SOON_RE.search(l):
            soon_n, section = n, "soon"; continue
        m = BULLET.match(l)
        if m and section and not (n == last_n and closing_ok):
            bullets[section].append((n, m.group(1).strip()))
    if ready_n is None:
        add("MISSING_SECTION", 0, 'missing "Ready to test now"')
    if soon_n is None:
        add("MISSING_SECTION", 0, "missing \"Coming soon, don't test yet\"")
    if ready_n and soon_n and soon_n < ready_n:
        add("MISSING_SECTION", soon_n, '"Coming soon" appears before "Ready to test now"')
    for key, hn, name in (("ready", ready_n, "Ready to test now"), ("soon", soon_n, "Coming soon")):
        if hn and not bullets[key]:
            add("EMPTY_SECTION", hn, f'"{name}" has no bullets (use "None this time")')
    for n, b in bullets["ready"]:
        if b.rstrip(". ").lower() != "none this time" and not PASS_RX.search(b):
            add("NO_PASS_CRITERIA", n, "bullet needs a pass condition (should / you should see / pass:)")

    for i, l in enumerate(lines, 1):
        if EMOJI.search(l) or SHORTCODE.search(l):
            add("EMOJI", i, "remove emoji / :shortcode:")
        if "\u2014" in l:
            add("EM_DASH", i, "replace em dash")
        for m in DEVS.finditer(l):
            add("DEV_NAME", i, f"remove dev/vendor name {m.group(1)}")
        if BASECAMP.search(l):
            add("BASECAMP_LINK", i, "remove Basecamp reference")
        for m in SECRET_RX.finditer(l):
            add("SECRET_LIKE", i, f"token-like string starting {m.group(0)[:4]}...")
    probs.sort(key=lambda p: p[0])
    return probs, len(bullets["ready"]), len(bullets["soon"]), bullets


def main(argv=None):
    ap = argparse.ArgumentParser(description="Offline lint for the IB coach test post draft. Never posts.",
                                 epilog="Exit: 0 good, 1 problems, 2 bad input.")
    ap.add_argument("draft")
    ap.add_argument("--approved", help="text Ryne approved; draft must match exactly (trailing whitespace ignored)")
    a = ap.parse_args(argv)
    text = load(a.draft)
    probs, nr, ns, bullets = lint(text)
    if a.approved:
        appr = load(a.approved)
        norm = lambda t: [l.rstrip() for l in t.rstrip().splitlines()]
        if norm(text) != norm(appr):
            diff = list(difflib.unified_diff(norm(appr), norm(text), "approved", "draft", lineterm="", n=0))
            first = next((i + 1 for i, (x, y) in enumerate(zip(norm(appr) + [None] * 999, norm(text))) if x != y), 0)
            probs.append((first, "CHANGED_SINCE_APPROVAL", "draft differs from approved text"))
            a._diff = diff[2:14]
    for n, code, msg in probs:
        print(f"{code} line {n}: {msg}")
    for d in getattr(a, "_diff", []):
        print("  " + d)
    if probs:
        print(f"SUMMARY {len(probs)} problem(s)")
        return 1
    real = lambda k: sum(1 for _, b in bullets[k] if b.rstrip(". ").lower() != "none this time")
    print(f"OK coach test post: {real('ready')} ready, {real('soon')} coming soon")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BadInput as e:
        print(f"ERROR {e}", file=sys.stderr)
        sys.exit(2)
