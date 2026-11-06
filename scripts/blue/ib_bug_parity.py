#!/usr/bin/env python3
"""ib_bug_parity.py: every IronBlueprint bug from Slack #ironblueprint must land in BOTH places.

Ryne's rule (2026-10-22): a bug posted in #ironblueprint gets
  (a) a NEW Basecamp Bugs Triage card (never only a comment on an old card), and
  (b) a NEW top-level post in IB Slack #bugs (C0C8V38T082) so the devs see it,
with every screenshot/video attached to both.

The filing routine appends one JSON line per bug to the ledger (/workspace/ib-bug-ledger.jsonl):
  {source_channel, source_ts, reporter, title, filed_at_ct, card_id, bugs_ts,
   media_expected, media_on_card, media_in_bugs_thread,
   missing_files: [{name, permalink, reason}]}
Program fields (Ryne 2026-10-22, "always pull the program ID"):
  program_related (bool), program_id (24-char lowercase hex), program_id_source
  (text | url | image:<file> | asked_ryne), asked_at (CT time Ryne was asked, required for asked_ryne)
Extra keys (note, related_card_id, ...) are allowed and ignored.

This script never calls Slack or Basecamp. The bot exports what it needs with its own
connectors and passes files in. Offline, standard library only, no secrets.

Checks (one line each):
  MISSING_LEDGER       a source bug ts (--source-bugs) has no ledger row
  MISSING_CARD         ledger row has no card_id
  MISSING_BUGS_POST    ledger row has no bugs_ts
  CARD_NOT_FOUND       card_id is not in --cards-export
  BUGS_POST_NOT_FOUND  bugs_ts is not a top-level post in --bugs-export
  MEDIA_SHORT/EXTRA    media_on_card or media_in_bugs_thread != media_expected. The ONLY pass is
                       both == media_expected (Ryne 2026-10-22: photos and videos are ALWAYS attached).
                       Skipped for a side already flagged MISSING_CARD / MISSING_BUGS_POST. When an
                       export carries attachments_count / files_count, the lower number is used.
  MEDIA_NOT_ATTACHED   any missing_files entry. A permalink is NOT a pass; fix the file with
                       ib_media_fix.sh and attach it, then rewrite the row with missing_files: []
  MISSING_PERMALINK    a missing_files entry also has no permalink
  DUPLICATE            a source_ts appears more than once in the ledger
  PROGRAM_RELATED_UNSET  the row has no program_related true/false
  MISSING_PROGRAM_ID   program_related is true and program_id is empty or not 24-char hex, or the
                       source is asked_ryne without asked_at (a row waiting on Ryne still fails)
  PROGRAM_ID_NOT_IN_POST / _CARD  exports include the post text / card content and it lacks
                       "Program ID: <id>"
Then a totals line, e.g. "OK 3/3 bugs have card + #bugs post, media attached 10/10 (card + #bugs thread)"\n(media counted once per side, so 5 files = 10), or "SUMMARY ..." plus a problem count.

Usage:
  python3 ib_bug_parity.py --ledger /workspace/ib-bug-ledger.jsonl --since 2026-10-21
  options: --bugs-export bugs.json   [{ts, text, thread_ts?, files_count?}]  (or {"messages": [...]})
           --cards-export cards.json [{id, title, attachments_count?}]
           --source-bugs src.json    [{ts, user, text}]  #ironblueprint messages classified as bugs
Exit code: 0 all good, 1 any problem line printed, 2 bad input or usage error.
"""
import argparse, datetime as dt, json, re, sys
from zoneinfo import ZoneInfo

CHI = ZoneInfo("America/Chicago")
BUGS_CHANNEL = "C0C8V38T082"
REQUIRED = ["source_channel", "source_ts", "reporter", "title", "filed_at_ct", "card_id", "bugs_ts",
            "media_expected", "media_on_card", "media_in_bugs_thread", "missing_files"]
PID = re.compile(r"^[0-9a-f]{24}$")
TS_RE = re.compile(r"^\d{9,11}\.\d{1,6}$")


def _norm(t):
    """Lowercase, drop Slack/markdown formatting (` * _ ~) and collapse spaces so 'Program ID: `id`' matches."""
    return re.sub(r"\s+", " ", re.sub(r"[`*_~]", "", str(t))).lower()


class BadInput(Exception):
    pass


def day_of(ts):
    return dt.datetime.fromtimestamp(float(ts), CHI).date().isoformat()


def blank(v):
    return v is None or str(v).strip() in ("", "-", "null", "None")


def as_int(v, field, where):
    if isinstance(v, bool):
        raise BadInput(f"{where}: {field} must be a whole number, got {v!r}")
    if isinstance(v, int):
        n = v
    elif isinstance(v, str) and v.strip().isdigit():
        n = int(v.strip())
    else:
        raise BadInput(f"{where}: {field} must be a whole number, got {v!r}")
    if n < 0:
        raise BadInput(f"{where}: {field} must be >= 0, got {n}")
    return n


def check_ts(v, field, where):
    s = str(v).strip()
    if not TS_RE.match(s):
        raise BadInput(f"{where}: {field} {v!r} is not a Slack ts like 1792603801.673819")
    return s


def load_ledger(path):
    rows = []
    try:
        fh = open(path, encoding="utf-8")
    except OSError as e:
        raise BadInput(f"ledger: cannot open {path}: {e.strerror}")
    with fh:
        for i, line in enumerate(fh, 1):
            if not line.strip():
                continue
            where = f"ledger line {i}"
            try:
                r = json.loads(line)
            except json.JSONDecodeError as e:
                raise BadInput(f"{where}: not valid JSON ({e.msg})")
            if not isinstance(r, dict):
                raise BadInput(f"{where}: must be a JSON object")
            miss = [k for k in REQUIRED if k not in r]
            if miss:
                raise BadInput(f"{where}: missing field(s) {', '.join(miss)}")
            r["source_ts"] = check_ts(r["source_ts"], "source_ts", where)
            if not blank(r["bugs_ts"]):
                r["bugs_ts"] = check_ts(r["bugs_ts"], "bugs_ts", where)
            for k in ("media_expected", "media_on_card", "media_in_bugs_thread"):
                r[k] = as_int(r[k], k, where)
            if not isinstance(r["missing_files"], list) or not all(isinstance(m, dict) for m in r["missing_files"]):
                raise BadInput(f"{where}: missing_files must be a list of objects")
            r["_line"] = i
            rows.append(r)
    return rows


def load_list(path, label, need):
    try:
        data = json.load(open(path, encoding="utf-8"))
    except OSError as e:
        raise BadInput(f"{label}: cannot open {path}: {e.strerror}")
    except json.JSONDecodeError as e:
        raise BadInput(f"{label}: not valid JSON ({e.msg})")
    if isinstance(data, dict):
        data = data.get("messages") or data.get("cards") or data.get("data") or []
    if not isinstance(data, list):
        raise BadInput(f"{label}: must be a JSON list")
    for i, x in enumerate(data):
        if not isinstance(x, dict) or any(k not in x for k in need):
            raise BadInput(f"{label} item {i}: needs {', '.join(need)}")
    return data


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="ib_bug_parity.py",
        description="IB bug parity: every #ironblueprint bug has a new Basecamp Bugs Triage card AND a new "
                    "#bugs post, with all media on both. Exported files in, no API calls.",
        epilog="Exit code: 0 all good, 1 problem lines printed, 2 bad input or usage error.")
    ap.add_argument("--ledger", required=True, help="JSONL ledger, one row per filed bug")
    ap.add_argument("--bugs-export", help="#bugs messages JSON: [{ts, text, thread_ts?, files_count?}]")
    ap.add_argument("--cards-export", help="Basecamp Bugs cards JSON: [{id, title, attachments_count?}]")
    ap.add_argument("--source-bugs", help="#ironblueprint messages classified as bugs: [{ts, user, text}]")
    ap.add_argument("--since", help="YYYY-MM-DD (CT). Only bugs whose source_ts is on or after this day. Default: all")
    a = ap.parse_args(argv)

    if a.since:
        try:
            dt.date.fromisoformat(a.since)
        except ValueError:
            raise BadInput(f"--since {a.since!r} is not YYYY-MM-DD")
    keep = (lambda ts: day_of(ts) >= a.since) if a.since else (lambda ts: True)

    ledger = [r for r in load_ledger(a.ledger) if keep(r["source_ts"])]
    source = None
    if a.source_bugs:
        source = load_list(a.source_bugs, "source-bugs", ["ts"])
        for i, m in enumerate(source):
            m["ts"] = check_ts(m["ts"], "ts", f"source-bugs item {i}")
        source = [m for m in source if keep(m["ts"])]
    bugs = load_list(a.bugs_export, "bugs-export", ["ts"]) if a.bugs_export else None
    cards = load_list(a.cards_export, "cards-export", ["id"]) if a.cards_export else None

    problems = []
    seen = {}
    for r in ledger:
        seen.setdefault(r["source_ts"], []).append(r["_line"])
    for ts, lines in seen.items():
        if len(lines) > 1:
            problems.append(f"DUPLICATE source_ts {ts}: ledger lines {', '.join(map(str, lines))}")

    if source is not None:
        for m in source:
            if m["ts"] not in seen:
                txt = re.sub(r"\s+", " ", str(m.get("text", "")))[:80]
                problems.append(f"MISSING_LEDGER source_ts {m['ts']} ({m.get('user', '?')}): \"{txt}\"")

    top_level, thread_files, post_text = set(), {}, {}
    if bugs is not None:
        for m in bugs:
            ts = str(m["ts"]).strip()
            parent = str(m.get("thread_ts") or ts).strip()
            if parent == ts:
                top_level.add(ts)
                post_text[ts] = str(m.get("text") or "")
            if "files_count" in m:
                thread_files[parent] = thread_files.get(parent, 0) + as_int(m["files_count"], "files_count", f"bugs-export ts {ts}")
    card_ids, card_files, card_text = set(), {}, {}
    if cards is not None:
        for c in cards:
            cid = str(c["id"]).strip()
            card_ids.add(cid)
            if c.get("content") or c.get("description"):
                card_text[cid] = str(c.get("content") or c.get("description"))
            if "attachments_count" in c:
                card_files[cid] = as_int(c["attachments_count"], "attachments_count", f"cards-export id {cid}")

    complete = media_total = media_ok = 0
    for r in ledger:
        tag = f"source_ts {r['source_ts']} \"{str(r['title'])[:60]}\""
        has_card, has_post = not blank(r["card_id"]), not blank(r["bugs_ts"])
        row_bad = False
        if not has_card:
            problems.append(f"MISSING_CARD {tag}: no Basecamp Bugs Triage card_id"); row_bad = True
        if not has_post:
            problems.append(f"MISSING_BUGS_POST {tag}: no #bugs ({BUGS_CHANNEL}) post ts"); row_bad = True
        cid = str(r["card_id"]).strip() if has_card else None
        if cid and cards is not None and cid not in card_ids:
            problems.append(f"CARD_NOT_FOUND {tag}: card {cid} not in cards export"); row_bad = True
        if has_post and bugs is not None and r["bugs_ts"] not in top_level:
            problems.append(f"BUGS_POST_NOT_FOUND {tag}: {r['bugs_ts']} is not a top-level post in the #bugs export"); row_bad = True

        exp = r["media_expected"]
        on_card = r["media_on_card"]
        if cid and cid in card_files:
            on_card = min(on_card, card_files[cid])
        in_thread = r["media_in_bugs_thread"]
        if has_post and r["bugs_ts"] in thread_files:
            in_thread = min(in_thread, thread_files[r["bugs_ts"]])
        for side, got, present in (("card", on_card, has_card), ("#bugs thread", in_thread, has_post)):
            if present and got != exp:
                kind = "MEDIA_SHORT" if got < exp else "MEDIA_EXTRA"
                problems.append(f"{kind} {tag}: {side} has {got}, expected exactly {exp}"); row_bad = True
        for f in r["missing_files"]:
            problems.append(f"MEDIA_NOT_ATTACHED {tag}: {f.get('name', '?')!r} ({f.get('reason') or 'no reason given'}); "
                            f"a permalink is not a pass, attach the file"); row_bad = True
            if blank(f.get("permalink")):
                problems.append(f"MISSING_PERMALINK {tag}: missing file {f.get('name', '?')!r} has no permalink"); row_bad = True
        # program ID (Ryne 2026-10-22: always pull the program ID)
        if "program_related" not in r:
            problems.append(f"PROGRAM_RELATED_UNSET {tag}: set program_related true/false"); row_bad = True
        elif r["program_related"] is True:
            pid = str(r.get("program_id") or "").strip()
            src = str(r.get("program_id_source") or "").strip()
            asked = not blank(r.get("asked_at"))
            if not PID.match(pid):
                why = f"waiting on Ryne since {r['asked_at']}" if src == "asked_ryne" and asked else \
                      ("not asked yet: run ib_extract_program_id.py, then ask Ryne" if not pid else f"{pid!r} is not 24-char hex")
                problems.append(f"MISSING_PROGRAM_ID {tag}: {why}"); row_bad = True
            elif src == "asked_ryne" and not asked:
                problems.append(f"MISSING_PROGRAM_ID {tag}: program_id_source asked_ryne needs asked_at"); row_bad = True
            elif not (src in ("text", "url", "asked_ryne") or src.startswith("image:")):
                problems.append(f"MISSING_PROGRAM_ID {tag}: program_id_source {src!r} must be text, url, image:<file> or asked_ryne"); row_bad = True
            else:
                need_line = f"program id: {pid}"
                if has_post and r["bugs_ts"] in post_text and need_line not in _norm(post_text[r["bugs_ts"]]):
                    problems.append(f"PROGRAM_ID_NOT_IN_POST {tag}: #bugs post lacks \"Program ID: {pid}\""); row_bad = True
                if cid and cid in card_text and need_line not in _norm(re.sub(r"<[^>]+>", " ", card_text[cid])):
                    problems.append(f"PROGRAM_ID_NOT_IN_CARD {tag}: card lacks \"Program ID: {pid}\""); row_bad = True
        elif r["program_related"] is not False:
            raise BadInput(f"ledger line {r['_line']}: program_related must be true or false")
        media_total += 2 * exp
        media_ok += (min(on_card, exp) if has_card else 0) + (min(in_thread, exp) if has_post else 0)
        if not row_bad:
            complete += 1

    for p in problems:
        print(p)
    n = len(ledger)
    print(f"{'OK' if not problems else 'SUMMARY'} {complete}/{n} bugs have card + #bugs post, media attached {media_ok}/{media_total} (card + #bugs thread)"
          + (f", {len(source)} source bug(s) checked" if source is not None else "")
          + (f" (since {a.since} CT)" if a.since else ""))
    if problems:
        print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except BadInput as e:
        print(f"ib_bug_parity bad input: {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"ib_bug_parity error: {e}", file=sys.stderr)
        sys.exit(2)
