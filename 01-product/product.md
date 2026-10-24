# Product

## What it is
- AI programming engine for sports performance coaches. Coaches buy; athletes use the React Native mobile app. (Forge 2026-08-24)
- Coach uses the web app: AI philosophy settings, generate, edit, review, grant autonomy. Athlete uses mobile: assigned program, log sessions, progress.
- **Nexus** (FastAPI + LangGraph + Gemini, MongoDB exercise DB) generates individualized programs. Built by Suffescom.
- Public site promise: individualized programs in 30 to 60 seconds instead of 20 to 30 minutes per athlete; every program editable. (X launch research, 2026-10-10)
- Hawkin force plates are integrated. Asymmetry is never auto-applied.

## Core rules (authoritative: Nexus AI RL Technical Plan v3.0, 2026-06-30)
- "The LLM proposes; a validation gate disposes." Nothing reaches an athlete unvalidated at any autonomy level.
- Always coach approval: injury/return-to-play, first program for a new athlete, anything set Manual Only, Hawkin asymmetry. Layer 1 safety violations are blocked, not routed.
- Autonomy is per coach per decision category (Suggest > Auto-draft > Auto-adjust with notify > Autonomous with audit), always reversible.
- Day-one personalization from Head Coach AI Settings. Preference learning from edits takes weeks (about 30 days). Outcome learning (1RM, Hawkin) is capture-only until month 18+.
- Workout completion is not a quality signal. RPE vs prescribed is a load-calibration signal.

## Programming logic
- Session order: SMR > Breathing > Warm-up > (athletes: Speed/Agility > Power) > Strength > Core > Tertiary. About 1 hour. Adults get no speed/power unless the coach asks.
- No true overhead press for overhead sports. Pairings are non-competing (never two lowers, two pushes, or two pulls).
- Failed sets do not update 1RM (Epley from last successful set).
- Taper: start 2 to 3 weeks out, cut volume 40 to 60% gradually, no new exercises, last S&C 5 days before.
- Team programs stay uniform; coaches adjust per athlete. Adult phases: GPP, foundation, hypertrophy.
- Skill: `ironblueprint-programming-logic`.

## Status and phases
- Program generation deployed to live 2026-06-25; Sep 8 2026 standup: AI generation live-only. Mobile store builds uploaded around Sep 8. (Forge log)
- Phase Five (RL) gated on about 500 labeled program-feedback loops. The team "IB 500" tally was 246/500 on 2026-10-16. (ib-500-tally-log)
- Open bug themes (Linus audit 2026-10-17): wrong program shape (4 weeks instead of 5), swaps resetting sets/reps, RPE lost on swap, credits not refunded on failed generations. Root cause: nothing checks the generated shape matches the request. See 06-engineering.

## Model policy (2026-09-08)
- Gemini 3.1 Pro is the orchestration baseline. Chinese-origin open weights allowed only with no data path to China (self-host or US-pinned hosting). DeepSeek's China API is a hard no. DGX Spark is for dev, soak, and A/B only. Any model swap needs a coach-scored staging A/B on 10 to 20 real athletes.

## TODO
- TODO: Which Nexus branch runs in production (ask Suffescom).
- TODO: Mobile app repo access (separate GitHub org, not shared yet).
- TODO: Current phase status (Phase 3 edits/approvals, Phase 4 safety gate) as of October.

Sources: Forge memory profile.md and log 2026-08/2026-09; ironblueprint-x-launch-research.md; ib-500-tally-log.md; ironblueprint-agent-prep/suggestions.md and repo-map.md (Linus audit 2026-10-17).
