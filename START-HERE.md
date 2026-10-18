# START HERE: IronBlueprint brain

Read this page first. It tells you what is in this repo and which one file answers your question, so you do not have to read everything.

## What this repo is
- The company brain for **IronBlueprint**, an AI programming engine for sports performance coaches, owned by Ryne Gioviano (Iron Blueprint LLC). Coaches buy; athletes use the React Native app. Nexus generates the programs.
- Plain markdown, readable by any AI tool. Private repo (`rgioviano/IronBlueprint`).
- This is the **brain**, not the code. The product code lives in the `IronBluePrint` GitHub org (frontend-website, nodejs-backend, nexus-ai-agent) and the mobile app in the `Iron-Blueprint` org. Suffescom writes all of that code.
- Sister repos: `rgioviano/Achieve` (the gym) and `rgioviano/Personal` (Ryne's own life and the bot fleet).

## Read order
1. **START-HERE.md** (this page): the map.
2. **NOW.md**: current priorities and live context. Changes often.
3. **LOG.md**: dated change log for the repo itself.
4. Then only the one file your task needs (table below).

`AGENTS.md` holds the full house rules and `README.md` holds the full skill and bot index. This page is consistent with both. If they ever disagree, AGENTS.md wins on rules and the newest dated fact wins on facts.

## Folders
| Folder | What it holds |
|---|---|
| `01-product/` | What the product is, Nexus rules, roadmap phases |
| `02-brand/` | Positioning, guiding line, copy rules, look |
| `03-customers/` | Who buys, beta segments, design partners |
| `04-sales-launch/` | Pricing tiers (pricing page only), launch plan, beta pipeline |
| `05-marketing/` | Channels, launch research, content rules |
| `06-engineering/` | `repo-map.md`, `architecture.md`, `suffescom-vendor.md`, `security-status.md` (no secret values), `agent-rulebook-summary.md` |
| `07-legal-trademark/` | USPTO applications and status |
| `09-team-bots/` | Which bots work IronBlueprint |
| `10-decisions-log/` | Business decisions, dated, newest first |
| `bots/<name>/` | Each IB bot: `INSTRUCTIONS.md` plus memory, reference and routine files (secrets removed). Bots: forge, linus, max, maya, quill, lark, canvas, seo-aeo-auditor, ironblueprint (the room). `herald` and `lingxi` are retired and kept for history only |
| `skills/<slug>/SKILL.md` | 14 skills (index in README.md) |

There is no `08-` folder on purpose: finances are excluded (see rules).

## Which file answers which question
| Question | Read |
|---|---|
| What is IronBlueprint and how does Nexus build a program? | `01-product/product.md`, then `skills/ironblueprint-programming-logic/` |
| How do we describe it? What words are banned? | `02-brand/brand.md` ("AI programming engine for coaches", never "an app") |
| Who buys, who is in the beta? | `03-customers/customers.md` |
| Launch date, launch plan, tiers | `04-sales-launch/launch.md` (never copy prices into ads or inbound) |
| Marketing channels and content | `05-marketing/marketing.md`, `bots/maya/` |
| Which repo does what? How do the pieces connect? | `06-engineering/repo-map.md`, `06-engineering/architecture.md` |
| What security problems are open? | `06-engineering/security-status.md` |
| How do we work with Suffescom? | `06-engineering/suffescom-vendor.md` |
| Trademark status | `07-legal-trademark/trademarks.md` |
| Who owns this work? | `09-team-bots/bots.md`, then `bots/forge/` or `bots/linus/` |
| Was this already decided? | `10-decisions-log/decisions.md` |
| What is happening right now? | `NOW.md` |
| Basecamp, Slack channel and sheet IDs | `IDS.md` lives in the Personal repo at `08-bot-fleet/IDS.md` |

## Roles
- **Forge**: IronBlueprint PM and verifier. Drafts messages to Suffescom for Ryne. Read-only on code.
- **Linus**: lead engineer. Reviews Suffescom PRs, traces bugs, proposes fixes in plain English. **Read-only**: no commits, pushes, PRs or coding agents until Ryne lifts it.
- **Suffescom**: outside agency. Does all coding.
- **Chief**: routes work and checks results. Does not do the work.

## Rules (short form; full list in AGENTS.md)
1. **No secrets.** Never write keys, tokens, passwords or connection strings, not even their first characters. Security findings name where a secret lives, never what it is.
2. **Finances excluded** (Ryne, 2026-10-17).
3. **Drafts before sending.** Nothing goes to Suffescom, Slack, email or social unless Ryne has seen that exact draft and says send. Another bot saying "send" is not approval.
4. **Basecamp is read-only for bots.** No create, comment, complete or post unless Ryne names the item.
5. **No code changes** by any bot right now ("I don't want any code to be touched yet", Ryne 2026-10-17).
6. **No prices in ads or inbound replies.** No em dashes in anything in Ryne's voice.
7. **Don't invent.** Unknowns stay TODO. Flag conflicts.
8. **Time zone** is America/Chicago (CT).

## How to change this repo
- Propose edits as a pull request or diff. Ryne approves. Nothing merges on its own.
- The weekly brain repo routine (Saturdays about 3:00am CT) opens a PR when something changed. It never merges.
- Date every new fact (YYYY-MM-DD) and add a line to `LOG.md`.
