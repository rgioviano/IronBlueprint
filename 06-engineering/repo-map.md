# Repo map

Read-only audit by Linus, 2026-10-17. Full report: ironblueprint-agent-prep/repo-map.md on the box (ask Chief to attach it).

| Repo (GitHub org IronBluePrint) | What it is | Verdict |
|---|---|---|
| frontend-website | Next.js 14 coach and admin web app (athletes, programs, templates, exercise library, AI generation, billing) | Active, core. `main`; `staging` is ahead |
| nodejs-backend | Express + MongoDB API for web and mobile: auth, programs, Stripe, push, PDFs, Agenda jobs, Nexus client and webhook | Active, core. Team works on `master` |
| nexus-ai-agent | FastAPI + LangGraph (Gemini) service that generates programs and calls back to the backend | Active, core. Live branch inferred to be `AIdevelopment` (confirm with Suffescom) |
| ironblueprint-nexus-ai-agent | First Nexus prototype (2025) | Stale |
| landing-website | Old Next.js marketing page | Stale (check if mobile deep-link files are still served) |
| python-ai-backend | Pre-Nexus Python prototype (2024) | Stale |
| rn-mobile-apps | Empty placeholder | Empty |
| Iron-Blueprint/IronBlueprint-Mobile-App (other org) | The real React Native athlete app | Not accessible to the Cursor GitHub app yet |

- Three repos matter: frontend-website, nodejs-backend, nexus-ai-agent. Plus mobile once shared.
- No CI, no Docker, no deploy config found in any repo. "What runs in prod" is inferred.
- Hostnames: prod web app.iron-blueprint.com, staging staging.iron-blueprint.com, Nexus nexus-api.iron-blueprint.com.
- Local Nexus checkout on Ryne's Mac: ~/Projects/IronBlueprint (per Linus memory).
- Agent PR targets (proposed): frontend-website@staging, nodejs-backend@master, nexus-ai-agent@AIdevelopment. Confirm with Suffescom first.

Sources: ironblueprint-agent-prep/repo-map.md (2026-10-17); Linus memory profile.md (2026-09-04).
