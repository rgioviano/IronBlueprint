# Wave 2 import omissions (2026-11-06)

Archive gzip SHA256: `04647c8348b5335234c9b8190265ae53ac25a409f24a18d61476698b7e654882`

`SHA256SUMS.txt` in this folder matched the archive members before any edit. `COMPLETENESS.md` and `INCLUDED.txt` are those archive files, unchanged. The archive sets `privacy_ready: false`. That flag was not treated as proof. Its skills note and unreadable-skill list are the archive's own disclosure.

`scripts/brain_lint.py` in the archive matches the copy already on main (`f9830b3c4733921d8b221e52053d4424a4c99e11590f47527a236739de3bd9a2`). It was not replaced.

Wave 1 exports were not overwritten: canvas, linus, metric, simon.

## Bots imported
- blue: 451 skills, 8 routines, memories 119 to 116, facts 9 to 8
- lark: 459 skills, 3 routines, memories 38, facts 23 (counts unchanged; locators and two skill lines removed)
- max: 451 skills, 5 routines, memories 143 to 109, facts 33
- maya: 421 skills, 5 routines, memories 125 to 115, facts 10 to 9
- quill: 420 skills, 0 routines, memories 72 to 69, facts 11 to 10
- rank: 366 skills, 0 routines, memories 8, facts 7 (counts unchanged; private project and repo links removed)

## What was removed
Whole memories or facts were dropped when they named an athlete, a lead, or a family event, or when a win-back or re-engage log named people. Public skill text was kept. Two family-specific reply lines were removed from the writing-style skill in each of these six exports.

Private locators were removed from text that was otherwise kept: the prospect spreadsheet link and worksheet id, document links, a payment-page link and its studio and product ids, temporary tunnel links, project and repo links, Basecamp account, project, person, and card ids, and Slack user and channel ids.

One sales schedule note was kept after the client name in it was removed. Caption-format notes were kept after the real names in the examples were removed.

## Committed JSON SHA256
- `bots/blue/export/grok-bot-export-blue.json` `40b5bb9646136f8f374bc72ae541cc9194fcf27bc3bc3519f581233bba10bc06`
- `bots/lark/export/grok-bot-export-lark.json` `25e62bc1c6cea65c35dadbd52f3e635ded177ce9ff3d286748a20dd6a28ca7fb`
- `bots/max/export/grok-bot-export-max.json` `9b45454f50116f2ec12dbe3a79bb545751b0266c7b567231f46fcfe6400c7c74`
- `bots/maya/export/grok-bot-export-maya.json` `e8359d8b68f9b2ca601a1ea214e2df34247e1b46212af2a4649c8284246a19bd`
- `bots/quill/export/grok-bot-export-quill.json` `acf7c959d8f26db4f763879cf9990e5b1924703d534e98426b9a7237c13a9a44`
- `bots/rank/export/grok-bot-export-rank.json` `a3dc235c0775995cfe9e1feb8d72340abff3c759d0f61457e00856b234a277db`

These differ from `SHA256SUMS.txt` because of the removals above.

Sources: wave 2 export archive verified 2026-11-06; review of custom skill bodies, memories, facts, routines, and instructions the same day.
