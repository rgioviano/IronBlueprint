# NOW: IronBlueprint (as of 2026-10-24)

Current priorities and live context only. Replace lines as they go stale; history goes in LOG.md and `10-decisions-log/`.

## Launch
- **Public launch: Monday 2026-11-30**, still planned (Ryne, 2026-10-17; reconfirmed 2026-10-22). Older references to a Nov 1 launch are outdated.
- Ryne's push (2026-09-04): get it into users' hands soon with bugs mostly gone. Quality bar is category-leading.
- Basecamp Growth & Ops launch lists were all at 0% as of 2026-10-16.
- Launch-readiness audit (Blue, read-only, 2026-10-19): the production outage was the top launch risk at the time. Full report on the box (`WS/ib-launch-readiness-2026-10-19.md`).
- **IB 500**: the team is logging program reviews toward 500 labeled program-feedback loops (quality goal date Oct 29). Blue tallies from Achieve Slack #ironblueprint into the 500 Program Feedback Tracker sheet; the nightly pace post uses the `ib500_recount.py` check (live from 2026-10-21). Phase Five learning stays gated on about 500 loops. Ryne's top priority for Mon 2026-10-26 is keeping this pace.

## Engineering
- **Suffescom does all coding. Bots are read-only.** Linus, Blue and Simon read, test, review and propose; nothing is written, pushed or merged by a bot.
- **Linus reviews every Suffescom PR** on frontend-website, nodejs-backend and nexus-ai-agent for security, bugs and messy code, plus a weekday 9:00am CT backup check, and traces each bug Blue sends. Findings go to Chief; Ryne decides what goes to Suffescom.
- **Simon** (QA, reports to Blue) tests the live coach web app from the outside like a coach would, writes repro steps, re-tests after fixes, and gives pass/fail. Fails also go to Linus. Never trusts "fixed" until it works live. Uses a dedicated test coach login only.
- Blue's live routines: IB meeting ingest and IB web/mobile tasks (post in the IronBlueprint room), IB 500 tally and nightly pace post, IB Slack bug watcher (#bugs, #web-app, #mobile-app, #nexus-ai), IB dev daily summary.
- **Outage resolved:** 2026-10-17 about 3:45pm CT to 2026-10-20 about 9:50am CT (about 66 hours). Cause: the MongoDB cluster hit its storage cap. Suffescom's DevOps engineer was out for a day. Prevention items still open: MongoDB Atlas storage alerts at 75% and 90%, log retention and purge (BUG-16), API uptime check with alerts to Ryne, DevOps backup coverage, and confirming which cluster prod runs on. Suffescom write-up not received yet. Log: `WS/ib-outage-log.md`.
- **Security:** 7 critical findings are open (see `06-engineering/security-status.md`). Key rotation status is **unknown**; Blue and Linus track it. The 2026-10-19 audit also flagged that the outage fix involved sharing Ryne's own database login with Suffescom; suggested fix is a least-privilege member invite, then a password change and session review.
- **Ownership:** Ryne owns all accounts (GitHub orgs, AWS, Firebase, database). Flag: Firebase keys sit on a Suffescom-created project, `suffescom-mobiles`; move to IronBlueprint's own project.
- The mobile app repo (`Iron-Blueprint/IronBlueprint-Mobile-App`) is not readable by the Cursor GitHub app yet.

## Business
- Iron Blueprint LLC. Convert to a Delaware C-corp before taking investor money (talk to a CPA first). Fundraising, if any, comes after launch traction, likely early 2027.
- Trademark 99550047: examination suspended 2026-10-07, no deadline (not an Office Action). 99383569 is owned by Iron Blueprint LLC.
- Copy default: "AI programming engine for coaches". Never "an app", "software" or "a platform".

## Who to ask
- Blue (PM, formerly Forge), Linus (engineering, read-only), Simon (QA), Max (sales), Maya (marketing), Chief (routing). Max and Maya report through Blue for IronBlueprint work (2026-10-21). Blue and Red share the HQ room (created 2026-10-20).

Sources: Chief TEAM.md and IDS.md (2026-10-21 renames, reporting lines, HQ room, ib500 script); shared memory 2026-10-22 (Nov 30 launch) and 2026-10-13 (trademark suspension); `WS/ib-launch-readiness-2026-10-19.md`; `WS/ib-outage-log.md`; Simon profile.json; Chief tomorrow-priorities.md (2026-10-23); Chief chat 2026-10-17; `06-engineering/security-status.md`.
