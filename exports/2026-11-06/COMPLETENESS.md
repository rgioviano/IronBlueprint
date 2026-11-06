# IronBlueprint export checkpoint completeness

privacy_ready: true
semantic_review: full re-scan of memories, user_facts, instructions, routine instructions;
known client/athlete identifiers and personal-health clinical content removed when present;
brain_lint secrets/pii/emdash exit 0; scan.py empty.
skills: non-Chief incomplete/unverified; only full-text skills after Chief fill kept.

## Bots
- canvas
- linus
- metric
- simon

## Files
- `bots/canvas/export/grok-bot-export-canvas.json` bytes=10174073
- `bots/linus/export/grok-bot-export-linus.json` bytes=9621019
- `bots/metric/export/grok-bot-export-metric.json` bytes=9447666
- `bots/simon/export/grok-bot-export-simon.json` bytes=28700
- `scripts/brain_lint.py` bytes=9117
