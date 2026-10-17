# ironblueprint-brain

Company brain for IronBlueprint. Start with **AGENTS.md**.

- 01-product/product.md
- 02-brand/brand.md
- 03-customers/customers.md
- 04-sales-launch/launch.md
- 05-marketing/marketing.md
- 06-engineering/repo-map.md
- 06-engineering/architecture.md
- 06-engineering/suffescom-vendor.md
- 06-engineering/security-status.md
- 06-engineering/agent-rulebook-summary.md
- 07-legal-trademark/trademarks.md
- 09-team-bots/bots.md
- 10-decisions-log/decisions.md
- skills/knowledge-base-audit/SKILL.md

Status: local draft built 2026-10-17. Not yet a GitHub repo.

Sources: this folder.

## Skills index (14 skills)

Each skill lives in `skills/<slug>/SKILL.md` (some have extra reference files). Copied unchanged from Ryne's Grok Bot skill library on 2026-10-17.

- `knowledge-base-audit`: End-of-day audit that proposes brain edits as a diff for Ryne's approval; never auto-commits.
- `achieve-mail`: Use when Ryne runs /achieve-mail or asks about Achieve/IronBlueprint inbox, triage, leads, or drafting client email. Gmail only (work + contact + IronBlueprint connectors); never Spark.
- `achieve-writing-style`: Use when drafting Achieve or IronBlueprint email or Numa texts, and after Ryne sends so this skill is rewritten from what he actually sent.
- `ad-metrics-decisions`: Use this when auditing Meta or Google ads performance, choosing kill/hold/scale/refresh actions, explaining which metrics matter vs vanity, or updating monthly ads knowledge with metrics decision rules.
- `ads-audit`: Use when the user wants a Google Ads or Meta audit. Propose only. Findings must clear a money bar and read like a decision, not a dashboard.
- `email-marketing`: When planning, writing, reviewing, or measuring marketing emails or newsletters (value emails, welcome sequences, list growth, deliverability, copywriting).
- `generate-creative`: Use when the user wants ad creatives or images. Hunt real brand assets, copy a real HTML skeleton from the wall, judge renders before showing.
- `hormozi-grand-slam-offers`: Use when designing or diagnosing a sales offer, package, pricing stack, guarantee, or landing-page offer: Grand Slam / Value Equation mechanics (Hormozi $100M Offers).
- `hormozi-marketing-email-craft`: Use ONLY when drafting a Minute-style marketing email (branded one-idea value email like Acquisition/Mozi Minute) for Achieve Sports Performance or IronBlueprint. Do not use for inquiry replies, ops, nurture sequences, launches, or as the default structure for all marketing emails.
- `ironblueprint-programming-logic`: Use when Strength Coach (or any bot) designs or redesigns a program using IronBlueprint Nexus logic: classify athlete vs general, then apply codebase session order, pairings, overhead, taper, and load rules to make decisions.
- `mozi-sales-frameworks`: Use when drafting Achieve or IronBlueprint sales calls, closes, pricing diagnostics, partner offers, pre-call VSLs, or nurture that sits next to 3-7-30: Mozi standing frameworks including pre-call leverage.
- `sales-nurture-3-7-30`: Use when drafting Achieve or IronBlueprint sales email, Numa, or lead nurture sequences: value sequence, not chase.
- `seo-audit`: Use when the user wants an SEO audit: Search Console, indexing, on-page, AI traffic, scored findings delivered like an agency deck: not a dump.
- `van-westendorp-pricing`: Use this when pricing a new offer, program, membership, product, or price change, before picking a number. Runs the four-question Van Westendorp survey (from Alex Hormozi), sliced by customer segment.

## Bots index (11 bots)

Each bot lives in `bots/<slug>/`: `INSTRUCTIONS.md` (its full instructions) plus any memory, reference, and routine (automation) files, copied 2026-10-17. Secrets are never included.

- `canvas` (Canvas): ONLY job: for Ryne Gioviano, graphic designer for Achieve Sports Performance and IronBlueprint. Make designed files (image, PDF, slide, simple multi-page). Scop
- `forge` (Forge): Project manager of the IronBlueprint channel. Owns everything IronBlueprint for Ryne Gioviano (ryne@ironblueprint.app; also ryne@iron-blueprint.com). You run th
- `herald` (Herald): Helps founders launch products on X. Studies similar launches, sharpens your launch post and materials, then tracks engagement and the conversation in real time
- `ironblueprint` (IronBlueprint): (no description set)
- `lark` (Lark): ONLY job: Meta Ads and Google Ads platform expert for Ryne Gioviano across Achieve Sports Performance and IronBlueprint. Own everything inside Ads Manager and G
- `lingxi` (Lingxi): A hands-off engineering supervisor. It boards work, launches cloud agents, watches PRs on a 30-minute cadence, and only asks you to merge. For anyone who wants 
- `linus` (Linus): Expert full-stack software engineer for Ryne Gioviano. Owns anything software: products, apps, backends, frontends, infra, architecture, reviews, debugging: a
- `max` (Max): Sales lead for Ryne Gioviano across Achieve Sports Performance and IronBlueprint. Owns the full customer journey on the sales side: outreach and follow-ups, boo
- `maya` (Maya): ONLY job: master of social media and content strategy/creation for Ryne Gioviano across Achieve Sports Performance and IronBlueprint: plus overarching marketin
- `quill` (Quill): Copy chief for Achieve Sports Performance and IronBlueprint. Rewrites landing pages, ads, emails, and share cards so every line is visual, falsifiable, and only
- `seo-aeo-auditor` (SEO / AEO Auditor): Track keyword, technical, AI-prompt, and competitor movement in one place. Surfaces whether you're gaining or losing ground, flags site issues that need a fix, 
