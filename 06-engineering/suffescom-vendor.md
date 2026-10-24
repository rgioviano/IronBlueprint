# Suffescom (vendor)

- Outside agency that builds Nexus, the web app, and the mobile app. Ryne accepted the Nexus AI Plan v4 by email on 2026-07-02. (Forge log 2026-09-15)
- People (roles as of Aug 2026): Ajay Chopra (PM, branching), Pradeep (backend features), Rakesh (mobile APIs), Divesh Soni (program generation, RL), Gaurav Kumar (RL/data/AI phase), Abhishek (UI/mobile), Vishy (program-create API), Prabhjot (QA). (Forge log 2026-08-27)
- Standups: Tue/Thu mornings CT (Forge memory records both about 7:50am and 8:00 to 9:00am; TODO confirm).
- Communication: Ryne's IronBlueprint Slack workspace (#iron-blueprint channel; #bugs). The vendor's own Slack is not connected.

## Oversight set up 2026-10-17 (read-only, findings go to Chief, Ryne decides what goes to Suffescom)
- "IronBlueprint PR review": on new PRs in the three core repos plus a weekday 9am CT sweep (first Mon 10/19). Linus reviews; nothing is posted on GitHub.
- "IronBlueprint monthly security scan": first weekday of each month (first Mon 11/2), Forge verifies.
- "IronBlueprint bug triage": Forge's direct message when he posts a bug is the main trigger; #bugs listener and weekday 9am sweep of the Basecamp Bugs table are backups. Linus proposes a fix (file, cause, diff, severity, effort).

## Concerns (Ryne and Chief, 2026-10-17)
- Basic security errors (secrets in code, open admin endpoint) that review or secret scanning would catch.
- Firebase admin keys found in the code sit on a Suffescom-created project ("suffescom-mobiles"). NEEDS A CHECK: confirm whether that project is in an IronBlueprint-owned account or must be moved into one.
- Agents will not write code until Ryne decides; any future agent code starts small, reversible, human-reviewed.

## Account ownership
- Ryne owns all accounts (GitHub orgs, AWS, Firebase, database); IronBlueprint owns them, not Suffescom (Ryne, 2026-10-17). Exception to verify: the "suffescom-mobiles" Firebase project (see above).

## TODO
- TODO: Contract terms and IP assignment.
- TODO: Check the "suffescom-mobiles" Firebase project's ownership.
- Key rotation status: unknown (Ryne, 2026-10-17); Forge and Linus track it (see security-status.md).

Sources: Ryne, 2026-10-17 (account ownership, rotation unknown); Forge memory log 2026-08 and 2026-09; Chief chat 2026-10-17 (Linus routine confirmations, Ryne messages t452 to t465); ironblueprint-agent-prep/repo-map.md.
