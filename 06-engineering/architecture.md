# Architecture (summary)

- **Web to backend:** REST under /api/v1 with a bearer JWT stored in browser localStorage. Socket.io for generation status and chat.
- **Mobile to backend:** REST athlete routes (mobile repo not visible yet).
- **Backend to Nexus:** HTTPS POST with a program request (weeks, training days, athlete data) and a webhook URL; 600-second timeout. Field names are renamed by hand between the two services.
- **Nexus to backend:** HTTPS webhook back to the backend, which saves the program through an Agenda job. The backend does not check the result's shape.
- **Shared database:** Nexus reads the same MongoDB database the backend writes (exercises, coach settings). No shared schema. Biggest drift risk.
- **AWS:** SSM Parameter Store for secrets, S3 for files, SES for email.
- **Stripe:** checkout plus a signed webhook (signature is checked).
- **Firebase:** push notifications. Backend sends with a Suffescom-created Firebase project (ownership needs a check) ("suffescom-mobiles") while web push is set up on IronBlueprint's own project, so web push may silently fail (inferred, needs a test).
- **Hawkin Dynamics:** REST integration with scheduled jobs.
- **Nexus graph:** feedback_processing > evaluation > periodization > exercise_selection > final_nexus > safety_validation (one retry).
- **Scale:** 74 web routes, about 324 backend endpoints (20 with no auth), 14 Nexus endpoints (none authenticated), 56 data models, 31 features mapped.
- **Tests and lint:** frontend has `next lint` only; backend has neither; Nexus has pytest on AIdevelopment only.
- Leftovers from other Suffescom client projects are in the code (image domains, app name, sender domain), which suggests template reuse.

Sources: ironblueprint-agent-prep/repo-map.md, feature-map.md, rulebook-draft.md (Linus audit 2026-10-17).
