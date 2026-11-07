# Security status (summary, no secret values)

As of 2026-10-17. Found by Linus (read-only audit), verified by Forge. No secret values or prefixes appear here or should ever be added. Full findings: ironblueprint-agent-prep/suggestions.md on the box (it contains truncated prefixes; keep it off GitHub).

## November 2026 monthly scan (Linus, read-only, Mon 2026-11-02)
First saved monthly scan, compared with the 2026-10-17 audit. No code was changed, no key was tested, nothing was sent. Full report stays on the box (`ironblueprint-agent-prep/security-scans/2026-11.md`); it shows cut-down secret prefixes, so keep it off GitHub. Summary only:
- **SEC-18 (Critical, NEW):** live production secrets (database login, live payment keys, cloud and email keys, a Google key) sit in plain view on several current dated backup branches of the backend repo, not just in old history. Other branches hold some of the same cloud and email keys. Cleaning the main branch's history alone will not remove them. Proposed: rotate everything first, then delete or blank those branches before any history purge.
- **SEC-19 (Critical, NEW):** an admin "remove multiple coaches" endpoint has no login check. Anyone with coach IDs could delete coaches and delete or move their athletes, programs, templates and evaluations. It was not on the existing Basecamp card for unauthenticated routes. Proposed: require a logged-in head coach or admin and limit it to that head coach's own coaches.
- **SEC-20 (High, NEW):** the same 2024 keys were put back into a config file in Sep 2026 (removed 8 days later), and a new encryption key was committed in Oct 2026 (later removed). Strong sign the old keys were never rotated. Proposed: rotate, and add a secret scanner on every branch.
- **SEC-21 (Medium, NEW):** the new secret loading from AWS SSM on a feature branch swallows errors and caches a failed lookup until restart, which can lock every user out. Proposed: load secrets at startup and refuse to start if any is missing.
- **Changed:** SEC-6 is worse than recorded (same secrets also on live branch tips and re-committed); SEC-3 has one more Firebase admin key on the automated dependency branches; SEC-16 has one more location; SEC-4 is partly fixed on one feature branch only (signing secret now loaded from SSM; the admin token check is still off and the fix is not on the main branch); SEC-13 was rewritten but is still unsafe; SEC-14 package numbers refreshed.
- **Unchanged:** SEC-7, SEC-2, SEC-9, SEC-3, SEC-12, SEC-14 still open. Nothing is fully fixed.
- **Rotation:** still no evidence any secret was rotated (Blue checked Basecamp and Slack, 2026-11-02: the rotate and close-routes cards are still in Triage with no comments). Developer notes about moving keys to SSM are instructions or partial work, not a confirmed rotation.
- **Ryne's decision (2026-11-02, voice):** HOLD on acting on SEC-18 and SEC-19. He will raise them as a discussion item at the Tue 2026-11-03 IronBlueprint meeting. No rotation, branch cleanup or Suffescom ask until he says otherwise. TODO: record the meeting outcome.
- **Scan gaps:** no full clone was possible (the box has no GitHub login for git), so a full every-commit secret search is still not done; the deployed commit for each service is still unknown.

## Critical (7, from the 2026-10-17 audit; see the November update above)
| ID | Plain English | Status |
|---|---|---|
| SEC-16 | The live database login is written in plain text in the current Nexus code (dev branch). Probably never changed. | Open. Rotate DB user, lock IP access list, remove the hard-coded fallback in the same release |
| SEC-6 | Old code history holds live production credentials (database, AWS, email, Stripe live key and webhook secrets, a Google key, a Hawkin key). Removed from current files in April 2026 but still in history. | Open. Rotate all, then scrub history |
| SEC-7 | Anyone on the internet can create an admin account (an admin route has no login check). | Open. Close today |
| SEC-4 | The login-signing secret is committed and identical in test and live, and the admin token check is switched off, so admin logins can be forged. | Open |
| SEC-3 | Firebase admin private keys are committed; two are on a project created by Suffescom ("suffescom-mobiles"). | Open. Rotate and move to IronBlueprint's project |
| SEC-2 | The webhook that saves AI programs has no authentication and can overwrite any program. | Open. Add a shared-secret/HMAC check |
| SEC-1 | An AWS email key pair is hard-coded (likely dead code). | Open. Rotate anyway |

## High
- SEC-8: about 21 program handlers load by ID with no ownership check (athletes can edit other athletes' programs).
- SEC-9: Nexus API has no auth and open CORS (Critical if publicly reachable).
- SEC-10: CSV import routes and a test-email route have no auth.

## Medium / Low
- SEC-5 Google sign-in secret in frontend env file (Medium). SEC-11 real athlete data in a committed fixture. SEC-12 500 MB body limit and open CORS. SEC-13 regex injection in search. SEC-14 vulnerable dependencies (backend 8 critical / 69 high; frontend 2 critical / 22 high; Nexus pins old langchain/langgraph). SEC-15, SEC-17 low.

## Fix order (Forge)
1. Rotate first: database, Stripe live key and webhook secrets, AWS (S3 and both email keys), Firebase, login secret, Google, Hawkin.
2. Then close holes: admin route, admin token check, webhook auth.
3. Scrub git history last.
- Ryne can rotate the Hawkin key himself (it is an Achieve Hawkin account), then update Hawkin and the Cursor setup.

## Communication
- Forge holds the final Slack draft to Suffescom (#iron-blueprint, IronBlueprint workspace) for Ryne's review. Not sent as of this file.

## Rotation status
- 2026-11-02: still no evidence of any rotation (see November scan above). SEC-18 and SEC-19 on HOLD per Ryne.
- **Unknown.** Ryne does not know whether any of these keys have been rotated (Ryne, 2026-10-17). Forge (PM) and Linus (engineer) track it: record the date each item is rotated or fixed and who confirmed it.

## TODO
- TODO: Fill in rotation and fix dates per item (owner: Forge, with Linus verifying).

Sources: Ryne, 2026-10-17 (rotation status unknown); ironblueprint-agent-prep/suggestions.md (summary table, 2026-10-17); Forge verification messages relayed in Chief chat 2026-10-17; Chief chat 2026-10-17 (Hawkin key, Slack draft owner). `ironblueprint-agent-prep/security-scans/2026-11.md` (Linus, 2026-11-02, summarized with no values or prefixes); Blue reply to Linus 2026-11-02 (rotation evidence); Chief chat 2026-11-02 (Ryne HOLD, voice).
