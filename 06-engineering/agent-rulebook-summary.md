# Agent rulebook (summary of draft)

Draft by Linus, 2026-10-17. Full draft: ironblueprint-agent-prep/rulebook-draft.md on the box. Order follows the correction pyramid: fix in code/types first, then lint/CI, then written rules, then human review.

## Cross-repo rules
1. One shared contract (schema) for Node and Nexus requests and results; changes update the schema and both repos.
2. Requested shape equals delivered shape (weeks x days), checked in Nexus and again in Node; mismatch fails the program and refunds the credit.
3. Webhook trust: shared secret from SSM/env on both directions, never from the request body.
4. Shared MongoDB: backend owns every collection; Nexus is read-only.
5. Shared error_code enum, each mapped to a user message and a refund decision.
6. Every frontend URL constant must match a backend route (script check in CI).
7. Agent PRs only against the agreed branches; cross-repo changes link sibling PRs.
8. Changes to athlete/mobile responses need human review until the mobile repo is shared.

## Per-repo patterns
- Backend: auth middleware first on every route; secrets only from SSM; refund AI quota on every failure path.
- Nexus: rules as data (config JSON) plus deterministic checks over prompt text; every client bug gets a test.
- Frontend: API calls through the helper and Redux thunks; V1 editors only.

## Top anti-patterns to stop
Secrets in committed config; commented-out auth checks; routes without auth; loads with no owner scope; swallowed errors; silent defaults (8 or 12 weeks); PII in logs and fixtures; god files.

## Ryne's guardrails on agent coding (2026-10-17)
- No agent writes code until Ryne decides. If ever: small, reversible fixes only (never payments, logins, or customer data), a human reviews and merges every PR, and Linus/Forge explain each change in plain English.

Sources: ironblueprint-agent-prep/rulebook-draft.md (2026-10-17); Chief chat 2026-10-17 (t458).
