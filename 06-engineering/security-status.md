# Security status (summary, no secret values)

As of 2026-10-17. Found by Linus (read-only audit), verified by Forge. No secret values or prefixes appear here or should ever be added. Full findings: ironblueprint-agent-prep/suggestions.md on the box (it contains truncated prefixes; keep it off GitHub).

## Critical (7)
| ID | Plain English | Status |
|---|---|---|
| SEC-16 | The live database login is written in plain text in the current Nexus code (dev branch). Probably never changed. | Open. Rotate DB user, lock IP access list, remove the hard-coded fallback in the same release |
| SEC-6 | Old code history holds live production credentials (database, AWS, email, Stripe live key and webhook secrets, a Google key, a Hawkin key). Removed from current files in April 2026 but still in history. | Open. Rotate all, then scrub history |
| SEC-7 | Anyone on the internet can create an admin account (an admin route has no login check). | Open. Close today |
| SEC-4 | The login-signing secret is committed and identical in test and live, and the admin token check is switched off, so admin logins can be forged. | Open |
| SEC-3 | Firebase admin private keys are committed; two are on a Suffescom-owned project. | Open. Rotate and move to IronBlueprint's project |
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

## TODO
- TODO: Record date each item is rotated or fixed, and who confirmed it.

Sources: ironblueprint-agent-prep/suggestions.md (summary table, 2026-10-17); Forge verification messages relayed in Chief chat 2026-10-17; Chief chat 2026-10-17 (Hawkin key, Slack draft owner).
