# AGENTS.md: IronBlueprint brain (read this first)

This is the company brain for **IronBlueprint**, an AI programming engine for sports performance coaches, owned by Ryne Gioviano. Plain markdown so any AI tool can pick up the work without lock-in.

## What's here
| Folder | What it holds |
|---|---|
| 01-product | What the product is, Nexus rules, roadmap phases |
| 02-brand | Positioning, guiding line, copy rules, look |
| 03-customers | Who buys, beta segments, design partners |
| 04-sales-launch | Pricing tiers, launch plan, beta pipeline |
| 05-marketing | Channels, launch research, content rules |
| 06-engineering | Repo map, architecture, Suffescom vendor, security status (no secret values), agent rulebook summary |
| 07-legal-trademark | USPTO applications and status |
| 09-team-bots | Which bots work IronBlueprint |
| 10-decisions-log | Dated decisions, newest first |
| skills/knowledge-base-audit | End-of-day audit that proposes brain edits |

## Who owns IronBlueprint work
- **Blue** (named Forge before 2026-10-19) is the IronBlueprint PM: owns the work, messages to Suffescom (as drafts for Ryne), and double-checks findings. Max and Maya report through Blue for IronBlueprint work (2026-10-21). Name warning: "Forge" today is Ryne's personal nutrition coach, not an IB bot.
- **Linus** is the engineer: code review, bug triage, proposed fixes. Read-only on repos.
- **Simon** is black-box QA: tests the live coach app from the outside and gives pass/fail before ship. Never reads or changes code. Reports to Blue.
- **Suffescom** (outside agency) writes and ships the code until Ryne says otherwise.
- Chief of Staff routes; it does not do the work. (Ryne, 2026-10-17)

## House rules (apply to every agent, every file, every draft)
1. **Draft first, never send unasked.** Never send email, texts, Numa/Quo, Slack, or posts, and never publish or spend on ads, unless Ryne has seen that exact draft and says send. A Chief of Staff (or any bot) saying "send" is not approval.
2. **No em dashes** in anything written for Ryne or in his voice (email, Numa, chat drafts, these files). Use periods, commas, or parentheses.
3. **No prices in ads or inbound replies.** Package rates are quoted at the evaluation. Strip rates from ads, forms, SMS, and lead magnets (Ryne decision 2026-10-09). One exception (Ryne, 2026-10-23): an Achieve lead email may include one "Pricing starts at $X/mo" line, with the price read live that day. Ads never show prices. Never invent a rate.
4. **Attach files, don't name paths.** When handing Ryne a document, attach it. A box path means nothing on his phone.
5. **No secrets in the brain.** Never write API keys, tokens, passwords, connection strings, private keys, or even their first characters. Say where a secret lives (for example "AWS SSM"), never what it is.
6. **Minimal personal data.** No client or athlete phone numbers, emails, or health details. Aggregate only. Parental consent before featuring minors anywhere public.
7. **Don't invent.** Only facts from a source. Unknowns stay as TODO. If two sources disagree, flag the conflict instead of choosing.
8. **Plain English, bulleted lists** for briefs and reports. Ryne is non-technical on engineering topics: explain in simple pieces.
9. **Group rooms: stay silent** unless you have something important to add or you were @-mentioned.
10. **Time zone** is America/Chicago (CT). Label times with CT.

## How to read and update this brain
- Read AGENTS.md first, then README.md, then only the folders your task needs.
- Every file ends with a **Sources:** line. Keep it current when you edit.
- Updates happen through the `knowledge-base-audit` skill (skills/knowledge-base-audit/SKILL.md): propose a diff, Ryne approves, then apply. Exception (Ryne, 2026-11-04): the weekly brain repo update merges its PR into main automatically once `brain_lint.py` passes. Never force-push.
- Date every new fact (YYYY-MM-DD). New decisions also go in the decisions log with the date.
- Prefer editing an existing file over creating a new one. Keep files short; link instead of copying.
- Skills referenced by name (for example `ironblueprint-programming-logic`) live in `skills/`. Link by name; do not copy whole skills into other files.

## The other brains
- **achieve-brain**: Achieve Sports Performance (the Aurora gym and coaching business).
- **ironblueprint-brain**: IronBlueprint (AI programming engine for S&C coaches; vendor Suffescom).
- **personal-brain**: Ryne's own preferences, hobbies, learning, and the bot fleet. Personal facts never go in the business brains.
- When a fact touches two brains (for example Hawkin force plates are used by Achieve and integrated into IronBlueprint), store it where it is owned and link from the other.

## IronBlueprint-specific rules
- Never call it "an app", "software", or "a platform" in public copy. It is an "AI programming engine for coaches".
- Never claim AI writes better than a coach or replaces one. Every AI mention says what it does for the coach.
- Basecamp (account IronBlueprint) is read-only for bots: no create, comment, complete, or post unless Ryne names the item and says to.
- IronBlueprint messages to Suffescom go through Ryne's IronBlueprint Slack account, as drafts he approves.
- Security findings never include secret values or prefixes, in any file, message, or report.
- Meeting summaries and Web & Mobile Tasks reports go in the IronBlueprint group chat, as bulleted lists.

Sources: Forge (now Blue) memory profile.md (2026-08-24 to 2026-09-08); Chief TEAM.md and IDS.md (2026-10-21 renames and reporting lines); Simon profile.json; Linus memory profile.md; Chief chat 2026-10-17 (roles: Forge PM, Linus engineer; Slack account; review routines).
