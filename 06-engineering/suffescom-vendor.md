# Suffescom (vendor)

- Outside agency that builds Nexus, the web app, and the mobile app. Ryne accepted the Nexus AI Plan v4 by email on 2026-07-02. (Forge log 2026-09-15)
- People (roles as of Aug 2026): Ajay Chopra (PM, invoices, branching), Pradeep (backend features), Rakesh (mobile APIs), Divesh Soni (program generation, RL), Gaurav Kumar (RL/data/AI phase), Abhishek (UI/mobile), Vishy (program-create API), Prabhjot (QA). (Forge log 2026-08-27)
- Standups: Tue/Thu mornings CT (Forge memory records both about 7:50am and 8:00 to 9:00am; TODO confirm).
- Communication: Ryne's IronBlueprint Slack workspace (#iron-blueprint channel; #bugs). The vendor's own Slack is not connected.
- Invoice on record: Aug 15 to Sep 15 2026, about 188 hours, $3,000. Ryne releases payment himself; bots do not chase.

## Oversight set up 2026-10-17 (read-only, findings go to Chief, Ryne decides what goes to Suffescom)
- "IronBlueprint PR review": on new PRs in the three core repos plus a weekday 9am CT sweep (first Mon 10/19). Linus reviews; nothing is posted on GitHub.
- "IronBlueprint monthly security scan": first weekday of each month (first Mon 11/2), Forge verifies.
- "IronBlueprint bug triage": Forge's direct message when he posts a bug is the main trigger; #bugs listener and weekday 9am sweep of the Basecamp Bugs table are backups. Linus proposes a fix (file, cause, diff, severity, effort).

## Concerns (Ryne and Chief, 2026-10-17)
- Basic security errors (secrets in code, open admin endpoint) that review or secret scanning would catch.
- Firebase admin keys sit on a Suffescom-owned project, so IronBlueprint depends on the vendor for something it should control. Ask: transfer to IronBlueprint's account.
- Agents will not write code until Ryne decides; any future agent code starts small, reversible, human-reviewed.

## TODO
- TODO: Contract terms, rate, IP ownership, and repo/account ownership (who owns the GitHub orgs, AWS, Firebase, Atlas).
- TODO: Whether keys were rotated after April 2026 (asked in the pending Slack draft).

Sources: Forge memory log 2026-08 and 2026-09; Chief chat 2026-10-17 (Linus routine confirmations, Ryne messages t452 to t465); ironblueprint-agent-prep/repo-map.md.
