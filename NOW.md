# NOW: IronBlueprint (as of 2026-10-17)

Current priorities and live context only. Replace lines as they go stale; history goes in LOG.md and `10-decisions-log/`.

## Launch
- **Public launch: Monday 2026-11-30**, still planned (Ryne, 2026-10-17).
- Ryne's push (2026-09-04): get it into users' hands soon with bugs mostly gone. Quality bar is category-leading.
- Basecamp Growth & Ops launch lists were all at 0% as of 2026-10-16.
- **IB 500**: the team is logging program reviews toward 500 labeled program-feedback loops (quality goal date Oct 29 per bug notes). Forge tallies from Achieve Slack #ironblueprint into the 500 Program Feedback Tracker sheet. Phase Five learning stays gated on about 500 loops.

## Engineering
- **Suffescom does all coding. Bots are read-only.** Linus and Forge read, review and propose; nothing is written, pushed or merged by a bot.
- **Linus reviews every Suffescom PR** on frontend-website, nodejs-backend and nexus-ai-agent for security, bugs and messy code, plus a weekday 9:00am CT backup check, and traces each bug Forge sends. Findings go to Chief; Ryne decides what goes to Suffescom.
- Forge's live routines: IB meeting ingest and IB web/mobile tasks (post in the IronBlueprint room), IB 500 tally and daily pace post, IB Slack bug watcher (#bugs, #web-app, #mobile-app, #nexus-ai), IB dev daily summary (Forge DM).
- Open blocker 2026-10-17: web app "over storage" Network Error, no athletes or programs showing (IB Slack #bugs, sent to Forge).
- **Security:** 7 critical findings are open (see `06-engineering/security-status.md`). Key rotation status is **unknown**; Forge and Linus track it.
- **Ownership:** Ryne owns all accounts (GitHub orgs, AWS, Firebase, database). Flag: Firebase keys sit on a Suffescom-created project, `suffescom-mobiles`; move to IronBlueprint's own project.
- The mobile app repo (`Iron-Blueprint/IronBlueprint-Mobile-App`) is not readable by the Cursor GitHub app yet.

## Business
- Iron Blueprint LLC. Convert to a Delaware C-corp before taking investor money (talk to a CPA first). Fundraising, if any, comes after launch traction, likely early 2027.
- Trademark 99550047: examination suspended 2026-10-07, no deadline. 99383569 is owned by Iron Blueprint LLC.
- Copy default: "AI programming engine for coaches". Never "an app", "software" or "a platform".

## Who to ask
- Forge (PM), Linus (engineering, read-only), Max (sales), Maya (marketing), Chief (routing).

Sources: Chief chat 2026-10-17 (launch date, read-only rule, account ownership, LLC); Forge message to Chief 2026-10-17 (live routines); Linus instructions (2026-10-17); `10-decisions-log/decisions.md`; `06-engineering/security-status.md`; `WS/ironblueprint-agent-prep/bug-triage-state.json`.
