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

## Skills index (18 skills)

Each skill lives in `skills/<slug>/SKILL.md` (some have extra reference files). Synced from Ryne's Grok Bot skill library on 2026-11-05. Em dashes were swapped for hyphens and email addresses that are not Ryne's business addresses were replaced, per the repo rules.

- `knowledge-base-audit`: End-of-day audit that proposes brain edits as a diff for Ryne's approval (the weekly update auto-merges after lint, 2026-11-04).
- `achieve-mail`: Use when Ryne runs /achieve-mail or asks about Achieve/IronBlueprint inbox, triage, leads, or drafting client email. Gmail only (work + contact + IronBlueprint connectors); never Spark.
- `achieve-writing-style`: Use when drafting Achieve or IronBlueprint email or Numa texts, and after Ryne sends so this skill is rewritten from what he actually sent.
- `ad-metrics-decisions`: Use this when auditing Meta or Google ads performance, choosing kill/hold/scale/refresh actions, explaining which metrics matter vs vanity, or updating monthly ads knowledge with metrics decision rules.
- `ads-audit`: Use when the user wants a Google Ads or Meta audit. Propose only. Findings must clear a money bar and read like a decision, not a dashboard.
- `cold-email-reply-rules`: Use when drafting Achieve or IronBlueprint cold first-touch or re-engage sales emails (not booked-eval replies, not pricing replies to inbound questions).
- `design-model-routing`: Use when making a designed file (image, PDF, slide, carousel, lead magnet, pricing sheet, ad static, brand kit) for Achieve or IronBlueprint and deciding whether to stay in chat or launch a CloudAgent, which model, and how to keep the run cheap.
- `email-marketing`: When planning, writing, reviewing, or measuring marketing emails or newsletters (value emails, welcome sequences, list growth, deliverability, copywriting).
- `generate-creative`: Use when the user wants ad creatives or images. Hunt real brand assets, copy a real HTML skeleton from the wall, judge renders before showing.
- `hormozi-grand-slam-offers`: Use when designing or diagnosing a sales offer, package, pricing stack, guarantee, or landing-page offer - Grand Slam / Value Equation mechanics (Hormozi $100M Offers).
- `hormozi-marketing-email-craft`: Use ONLY when drafting a Minute-style marketing email (branded one-idea value email like Acquisition/Mozi Minute) for Achieve Sports Performance or IronBlueprint. Do not use for inquiry replies, ops, nurture sequences, launches, or as the default structure for all marketing emails.
- `ironblueprint-programming-logic`: Use when Strength Coach (or any bot) designs or redesigns a program using IronBlueprint Nexus logic - classify athlete vs general, then apply codebase session order, pairings, overhead, taper, and load rules to make decisions.
- `meta-google-ads-playbook`: Use when building, diagnosing, scaling, killing or rewriting Meta Ads or Google Ads for Achieve Sports Performance or IronBlueprint, when writing Meta ad text fields (Primary, Headline, Description, CTA), or when the monthly meta-ads-knowledge-refresh or google-ads-knowledge-refresh runs.
- `mozi-sales-frameworks`: Use when drafting Achieve or IronBlueprint sales calls, closes, pricing diagnostics, partner offers, pre-call VSLs, or nurture that sits next to 3-7-30 - Mozi standing frameworks including pre-call leverage.
- `sales-nurture-3-7-30`: Use when drafting Achieve or IronBlueprint sales email, Numa, or lead nurture sequences - value sequence, not chase.
- `security-audit`: Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use for security questions, focused reviews, vulnerability research, security audits, or pen tests. Run the complete workflow only for explicit codebase audit or pen-test requests, full/comprehensive/end-to-end reviews, or requested report artifacts.
- `seo-audit`: Use when the user wants an SEO audit: Search Console, indexing, on-page, AI traffic, scored findings delivered like an agency deck - not a dump.
- `van-westendorp-pricing`: Use this when pricing a new offer, program, membership, product, or price change, before picking a number. Runs the four-question Van Westendorp survey (from Alex Hormozi), sliced by customer segment.

## Bots index (11 bots and rooms)

Each bot lives in `bots/<slug>/`: `INSTRUCTIONS.md` (its profile.json instructions) and `ROUTINES.md` (its current schedule map, 2026-11-05). Secrets are never included. Retired bots were removed on 2026-11-05.

- `blue` (Blue): Project manager of the IronBlueprint channel. Owns everything IronBlueprint for Ryne Gioviano (ryne@ironblueprint.app; also ryne@iron-blueprint.com). You run th
- `canvas` (Canvas): ONLY job: for Ryne Gioviano, graphic designer for Achieve Sports Performance and IronBlueprint. Make designed files (image, PDF, slide, simple multi-page). Scop
- `ironblueprint` (IronBlueprint): (no description set)
- `lark` (Lark): ONLY job: Meta Ads and Google Ads platform expert for Ryne Gioviano across Achieve Sports Performance and IronBlueprint. Own everything inside Ads Manager and G
- `linus` (Linus): Expert full-stack software engineer for Ryne Gioviano. Owns anything software: products, apps, backends, frontends, infra, architecture, reviews, debugging, and
- `max` (Max): Sales lead for Ryne Gioviano across Achieve Sports Performance and IronBlueprint. Owns the full customer journey on the sales side: outreach and follow-ups, boo
- `maya` (Maya): ONLY job: master of social media and content strategy/creation for Ryne Gioviano across Achieve Sports Performance and IronBlueprint, plus overarching marketing
- `metric` (Metric): ONLY job: for Ryne Gioviano, deep-dive metric changes, analyze experiments, and visualize data the right way across Achieve Sports Performance and IronBlueprint
- `quill` (Quill): Copy chief for Achieve Sports Performance and IronBlueprint. Rewrites landing pages, ads, emails, and share cards so every line is visual, falsifiable, and only
- `rank` (Rank): Track keyword, technical, AI-prompt, and competitor movement in one place. Surfaces whether you're gaining or losing ground, flags site issues that need a fix, 
- `simon` (Simon): ONLY job: black-box QA for IronBlueprint, for Ryne Gioviano. Acts as your QA on the live deploy: runs the acceptance checklist and says pass or fail before you 
