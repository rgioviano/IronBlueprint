# NOW: IronBlueprint (as of 2026-11-18)

Current priorities and live context only. Replace lines as they go stale; history goes in LOG.md and `10-decisions-log/`.


## Status as of 2026-11-16 (Blue's outcome file; added 2026-11-18)
- **Launch target is still Mon 2026-11-30** (Launch Page, set by Ryne 2026-10-22). It is a target, not proven readiness. No later change is recorded.
- Dev-reported, not independently verified (Nov 10 meeting): coach and athlete creation, invites, onboarding and program validation pass the devs' checks.
- **New-account registration (Stripe) was blocked:** the devs needed Stripe Sandbox Mode enabled. A Sandbox was created 2026-11-16 (Chief promises watch, 2026-11-17); the live registration test result is not recorded yet.
- Staging to production: several frontend-website and nodejs-backend PRs merged Nov 10 to Nov 13. Merges are not production verification; nothing is confirmed live by QA or Ryne yet.
- App Store policy terms accepted by Ryne (2026-11-16 and again 2026-11-17).
- **New security issue (2026-11-15 to 11-16):** a frontend-website commit went straight to main without a PR and hardcodes the invite decryption key and secret in the sign-up page. Ryne asked the devs (2026-11-16) to move decryption to the backend, rotate the key and secret, use PRs, and confirm whether it reached production. No dev reply recorded as of 2026-11-16. See `06-engineering/security-status.md`.
- `PROGRAMMING_RULES_ENABLED` is still off in production per the Launch Page; it blocks BUG-23, 29, 30, 31 and 36. SEC-18 and SEC-19 remain on Ryne's HOLD (since 2026-11-02).
- New feature request (Ryne, 2026-11-14 to 11-15): make the evaluation optional for AI programming; to be scoped with the devs.
- Coach test posts (Ryne, 2026-11-10): list only what is ready to test now; no "Coming soon" section (`scripts/blue/ib_coach_test_lint.py` enforces it).
- IB 500 means 500 Nexus-generated programs reviewed with coach feedback (an internal RL-labeling goal), not users or revenue.

Sources: `shared/chief/ib-outcome-context.md` (Blue, 2026-11-16 about 10:35am CT); Chief notes TEAM.md promises watch 2026-11-16 and 2026-11-17; `ib_coach_test_lint.py` docstring.

## Launch
- **Public launch: Monday 2026-11-30**, still planned (Ryne, 2026-10-17; reconfirmed 2026-10-22). Older references to a Nov 1 launch are outdated.
- Ryne's push (2026-09-04): get it into users' hands soon with bugs mostly gone. Quality bar is category-leading.
- Basecamp Growth & Ops launch lists were all at 0% as of 2026-10-16.
- Launch-readiness audit (Blue, read-only, 2026-10-19): the production outage was the top launch risk at the time. Full report on the box (`WS/ib-launch-readiness-2026-10-19.md`).
- **IB 500 goal hit: 500 of 500 program reviews logged on 2026-10-29**, the goal date (Blue's tally log; final nightly pace post the same evening). Phase Five learning was gated on about 500 loops. Devs' plan from the 2026-10-27 standup: feed the reviews to the model, train for a couple of days, then test program generation. Whether training has started is not confirmed.
- Project Pages (2026-10-30): Blue owns the IronBlueprint Launch Page (weekday heartbeat about 8:10am CT) and the USPTO IRONBLUEPRINT Page (about 8:15am CT). Bots read the Page before work and update it after; Ryne hears only about blockers, overdue items, decisions and status changes.

## Engineering
- **Suffescom does all coding. Bots are read-only.** Linus, Blue and Simon read, test, review and propose; nothing is written, pushed or merged by a bot.
- **Linus reviews every Suffescom PR** on frontend-website, nodejs-backend and nexus-ai-agent for security, bugs and messy code, plus a weekday 9:00am CT backup check, and traces each bug Blue sends. Findings go to Chief; Ryne decides what goes to Suffescom.
- **Simon** (QA, reports to Blue) tests the live coach web app from the outside like a coach would, writes repro steps, re-tests after fixes, and gives pass/fail. Fails also go to Linus. Never trusts "fixed" until it works live. Uses a dedicated test coach login only.
- Blue's live routines: IB meeting ingest and IB web/mobile tasks (post in the IronBlueprint room), IB 500 tally and nightly pace post, IB bug sweep, IB dev daily summary.
- Bug sweeps stay manual: Ryne wants Blue to keep doing manual bug sweeps and not switch to an hourly Slack poll of #web-app, #mobile-app and #nexus-ai (2026-10-27).
- Meeting transcripts: Blue can get IronBlueprint meeting transcripts through the Spark connection (2026-10-27). The ingest fails when Ryne's Mac is offline, and Blue then runs a catch-up (ingest log, 2026-10-20 to 2026-10-29).
- **QA to-dos for Ryne** (2026-10-27): after each standup or ship, and whenever the devs write what they fixed, Blue creates one Basecamp QA to-do per Ready-to-test item assigned to Ryne, with what to test. Blue does this before, or instead of, waiting on coach-test Slack approval. Bundled notes alone are not enough. Coach-test Slack posts still need Ryne's approval before posting.
- **Standup 2026-10-27 (summary):** devs reported fixes live for progression editing, training variables save and delete, pick-list loading, editing a program while another generates, and a profile notification setting. Open at the time: sign-up, invites and email were down pending an ops config change (target 2026-10-28; current status not checked in this audit); a duplicate core category in one workout (fix in progress); a possible power pairing bug (needs a program ID). The security blockers (secret rotation, unauthenticated admin endpoints) were still in Triage and not discussed.
- **Outage resolved:** 2026-10-17 about 3:45pm CT to 2026-10-20 about 9:50am CT (about 66 hours). Cause: the MongoDB cluster hit its storage cap. Suffescom's DevOps engineer was out for a day. Prevention items still open: MongoDB Atlas storage alerts at 75% and 90%, log retention and purge (BUG-16), API uptime check with alerts to Ryne, DevOps backup coverage, and confirming which cluster prod runs on. Suffescom write-up not received yet. Log: `WS/ib-outage-log.md`.
- **Security:** 7 critical findings are open (see `06-engineering/security-status.md`). Key rotation status is **unknown**; Blue and Linus track it. The 2026-10-19 audit also flagged that the outage fix involved sharing Ryne's own database login with Suffescom; suggested fix is a least-privilege member invite, then a password change and session review.
- **Ownership:** Ryne owns all accounts (GitHub orgs, AWS, Firebase, database). Flag: Firebase keys sit on a Suffescom-created project, `suffescom-mobiles`; move to IronBlueprint's own project.
- The mobile app repo (`Iron-Blueprint/IronBlueprint-Mobile-App`) is not readable by the Cursor GitHub app yet.

## Business
- Iron Blueprint LLC. Convert to a Delaware C-corp before taking investor money (talk to a CPA first). Fundraising, if any, comes after launch traction, likely early 2027.
- Trademark 99550047: examination suspended 2026-10-07, no deadline (not an Office Action). 99383569 is owned by Iron Blueprint LLC.
- Copy default: "AI programming engine for coaches". Never "an app", "software" or "a platform".

## Who to ask
- Blue (PM, formerly Forge), Linus (engineering, read-only), Simon (QA), Max (sales), Maya (marketing), Chief (routing). Max and Maya report through Blue for IronBlueprint work (2026-10-21). The HQ room Blue and Red shared (created 2026-10-20) is gone (Ryne, 2026-11-05).

Sources: `WS/ib-500-tally-log.md` (2026-10-29); `WS/ib-project-pulse-2026-10-27.md`; `WS/ib-meeting-ingest-heartbeat.log`; Chief memory 2026-10-27 (Blue QA to-dos, Spark transcripts, manual bug sweeps); Chief TEAM.md (Page-based project management, 2026-10-30); Chief TEAM.md and IDS.md (2026-10-21 renames, reporting lines, HQ room, ib500 script); shared memory 2026-10-22 (Nov 30 launch) and 2026-10-13 (trademark suspension); `WS/ib-launch-readiness-2026-10-19.md`; `WS/ib-outage-log.md`; Simon profile.json; Chief tomorrow-priorities.md (2026-10-23); Chief chat 2026-10-17; `06-engineering/security-status.md`.
