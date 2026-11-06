# Import redactions (2026-11-06)

Archive SHA256 (gzip): `4665844a0e47f5f0e351fff2d287662b4feb769cb2cb8aa3e40d2727504e780b`

`SHA256SUMS.txt` in this folder matches the archive members. Those checksums were verified before copy. Paths inside `SHA256SUMS.txt`, `INCLUDED.txt`, and `COMPLETENESS.md` are unchanged.

Three committed exports differ from those checksums because obvious leaks were removed before commit:

- `bots/canvas/export/grok-bot-export-canvas.json`: one memory that named an athlete and that athlete's training numbers was replaced with a redaction line. A second memory lost the clause that named the same athlete. The Prospect Tracking spreadsheet URL was removed.
- `bots/linus/export/grok-bot-export-linus.json`: the Prospect Tracking spreadsheet URL was removed.
- `bots/metric/export/grok-bot-export-metric.json`: the Prospect Tracking spreadsheet URL was removed.

The spreadsheet is a lead list. The URL is not in this repo.

Committed SHA256 after those removals:

- `bots/canvas/export/grok-bot-export-canvas.json` `830ad1a5e56749fab01ccaed6896e7dc12ca04a10c365d9c0375dce6a479b66e`
- `bots/linus/export/grok-bot-export-linus.json` `9b099c7bbc718fe4f0da887f6e975c4076d9e8c06deb3c88431c72d095e4aaeb`
- `bots/metric/export/grok-bot-export-metric.json` `9003ff85ace0a6a56b5f8e691bc28664f7ae9b986c49c6ad93a486c58fc36119`

These committed files still match the archive checksums:

- `bots/simon/export/grok-bot-export-simon.json` `a2efa6a5031ead5fad7f37accc50e3596f6308ceac0134cae13963c15439bb18`
- `scripts/brain_lint.py` `f9830b3c4733921d8b221e52053d4424a4c99e11590f47527a236739de3bd9a2`
- `exports/2026-11-06/COMPLETENESS.md` `6353dfade7623365bd27135d6d7d0e3e65e2949c3ee74fac44b885e5cb51da97`

`COMPLETENESS.md` is the archive disclosure, including the skills note. It was not rewritten.

Sources: scrubbed IronBlueprint export archive verified 2026-11-06; import review the same day.
