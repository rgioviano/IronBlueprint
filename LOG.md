# LOG: IronBlueprint brain repo

Dated changes to this repo and to the fleet facts it depends on. Newest first. One line per change. Business decisions go in `10-decisions-log/decisions.md`; this file tracks the repo itself.

## 2026-10-31
- Weekly brain audit (second run). Covered 2026-10-24 to 2026-10-31. Branch `brain-audit-2026-10-31` is built on `brain-v1`, so it also carries the 2026-10-24 audit commit, which reached `brain-v1` (PR #2) after PR #1 had already merged into `main`. Opened as a PR into `main`. Not merged.
- NOW.md: IB 500 goal hit (500 on 2026-10-29); project Pages for Blue; manual bug sweeps; Spark transcripts; Basecamp QA to-do rule; 2026-10-27 standup summary.
- `09-team-bots/bots.md`: Blue's new duties and Pages; Chief router-only.
- `10-decisions-log/decisions.md`: 2026-10-27 and 2026-10-30 decisions; open questions updated.

## 2026-10-24
- Weekly brain audit (first run). Covered 2026-10-17 to 2026-10-24. Opened as a PR into `brain-v1`. Not merged.
- Renamed the IronBlueprint PM from Forge to Blue in AGENTS.md, START-HERE.md, NOW.md, `04-sales-launch/launch.md`, `09-team-bots/bots.md` and the decisions log, with a name warning (Forge is now Ryne's nutrition coach). The `bots/forge/` folder name is unchanged.
- Added Simon (black-box QA, reports to Blue) to AGENTS.md, START-HERE.md, NOW.md, launch.md and bots.md.
- NOW.md: the 2026-10-17 "over storage" blocker is replaced with the resolved outage summary (about 66 hours, MongoDB storage cap) and its open prevention items; added the 2026-10-19 launch-readiness audit summary, the IB 500 recount script, and the Max and Maya reporting line.
- launch.md: Nov 30 launch reconfirmed (Nov 1 is outdated); Simon's launch acceptance pass.
- AGENTS.md house rule 3: added the Achieve lead-email pricing line exception so all three brains match.
- Decisions log: added 2026-10-19 to 2026-10-22 entries and an open question about Simon's test login.

## 2026-10-19
- Removed the Suffescom invoice (hours and amount) and other company finance figures (vendor rate, USPTO fee amount, model spend figures, "spend is high"). Public pricing tiers stay in `04-sales-launch/launch.md`.
- Removed Achieve-only material: Max, Maya, Quill, and Lark memory and reference files (including both $100M Leads PDFs), the SEO bot folder, `achieve-mail`, `achieve-writing-style`, and the Achieve Minute template. Short IronBlueprint instructions remain for Max, Maya, Quill, and Lark.
- Scrubbed email addresses and phone numbers from the tree.

## 2026-10-17
- Repo `rgioviano/IronBlueprint` created by Ryne (private, personal account). First content opened as PR #1 from branch `brain-v1`. Not merged.
- Scope set to "everything included" (Ryne): all IB skills and every IB bot's instructions, memory, reference and routine files. Secret values are always redacted; security findings carry no values or prefixes.
- Finances left out entirely. `08-finance/` from the first draft is deleted in the PR.
- Ryne's gap answers recorded: launch still Nov 30; Ryne owns all accounts; key rotation status unknown (Forge and Linus track it); `suffescom-mobiles` Firebase project flagged.
- Roles set: Forge is PM and verifier, Linus is lead engineer, Chief routes only, Suffescom does all coding.
- **Linus set to read-only** (Ryne: "I don't want any code to be touched yet"). His instructions were rewritten: no commits, pushes, PRs or coding agents until Ryne lifts it.
- Forge confirmed none of his 6 live routines post to the deleted IronBlueprint room `0382da49-...`. Live room is `8857ae2a-0e5d-4af3-be8a-5ee7f2b04e50`.
- Lingxi (PR supervisor) and Herald (X launch) retired; their folders stay under `bots/` for history only.
- `bots/` and `skills/` added: 11 bot folders and 14 skills.
- Hormozi "$100M Leads" PDF split into two files (about 10 MB each, 385 pages total) and added to `bots/maya/reference/`.
- Read-only repo audit of the IronBluePrint code org written up in `06-engineering/repo-map.md` and `security-status.md`.
- Added START-HERE.md, NOW.md and LOG.md (this file) so any AI reads one or two pages instead of the whole repo.
- Weekly brain repo update routine set: Saturdays about 3:00am CT, opens PRs, never merges. First run 2026-10-24.

Sources: Chief TEAM.md and IDS.md (2026-10-21); shared memory 2026-10-22; `WS/ib-outage-log.md`; `WS/ib-launch-readiness-2026-10-19.md`; Simon profile.json; Chief chat 2026-10-17; Forge message to Chief 2026-10-17; `WS/brains-push/ironblueprint-DELETIONS.txt`; `WS/fleet/IDS.md`.
