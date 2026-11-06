# Import redactions (2026-11-06)

Archive SHA256 (gzip): `4665844a0e47f5f0e351fff2d287662b4feb769cb2cb8aa3e40d2727504e780b`

`SHA256SUMS.txt` in this folder matches the archive members. Those checksums were verified before copy. Paths inside `SHA256SUMS.txt`, `INCLUDED.txt`, and `COMPLETENESS.md` are unchanged.

Three committed exports differ from those checksums because obvious leaks were removed before commit:

- `bots/canvas/export/grok-bot-export-canvas.json`: one memory that named an athlete and that athlete's training numbers was replaced with a redaction line. A second memory lost the clause that named the same athlete. The Prospect Tracking spreadsheet URL was removed.
- `bots/linus/export/grok-bot-export-linus.json`: the Prospect Tracking spreadsheet URL was removed.
- `bots/metric/export/grok-bot-export-metric.json`: the Prospect Tracking spreadsheet URL was removed.

The spreadsheet is a lead list. The URL is not in this repo.

A second pass the same day read every custom skill body and the personal fields (instructions, memories, facts, routines), including text past the lint script's 5 MB read. More was removed from the canvas and linus exports:

- The prospect-tracking run log that named leads, including the appended heartbeat log
- The prospect-tracking worksheet id
- One writing-style entry about an athlete injury and that session
- Two writing-style entries about one family's account change

The same injury entry and family entries were removed from `skills/achieve-writing-style/SKILL.md`. Nonpublic email literals in that file and in `skills/achieve-mail/SKILL.md` were replaced with `[REDACTED email]`. `scripts/brain_lint.py` was not changed.

Committed SHA256 after those removals:

- `bots/canvas/export/grok-bot-export-canvas.json` `423f62727d6d0cbd1a623d52752c4609be45b7293829921de079f903102f6565`
- `bots/linus/export/grok-bot-export-linus.json` `39032d6ac88aef34cc376d4ce28ff42685efb58afed1e1371bc9d828a2fe1456`
- `bots/metric/export/grok-bot-export-metric.json` `9003ff85ace0a6a56b5f8e691bc28664f7ae9b986c49c6ad93a486c58fc36119`

These committed files still match the archive checksums:

- `bots/simon/export/grok-bot-export-simon.json` `a2efa6a5031ead5fad7f37accc50e3596f6308ceac0134cae13963c15439bb18`
- `scripts/brain_lint.py` `f9830b3c4733921d8b221e52053d4424a4c99e11590f47527a236739de3bd9a2`
- `exports/2026-11-06/COMPLETENESS.md` `6353dfade7623365bd27135d6d7d0e3e65e2949c3ee74fac44b885e5cb51da97`

`COMPLETENESS.md` is the archive disclosure, including the skills note (`skills: non-Chief incomplete/unverified; only full-text skills after Chief fill kept`). It was not rewritten. Its `privacy_ready: true` line is the archive's claim. The committed tree had more identifiers removed after that claim.

Sources: scrubbed IronBlueprint export archive verified 2026-11-06; import review the same day.
