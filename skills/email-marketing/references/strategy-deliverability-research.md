# Email and newsletter marketing research
Prepared 2026-10-14. General research for IronBlueprint marketing email. Every number below links to its source. Where no source was found, there is no number.

House rules: no prices in emails, no em dashes, and Ryne approves every draft before it sends.

## 1. Cadence, frequency, and send timing
- **Mailchimp's send-time research:** Across Mailchimp's whole data set, weekdays do best and about 10 AM local time is the broadest peak. But 10 AM is the best time for only a small share of recipients (about 6 to 7 percent), so there is no single best time. Sources: [Mailchimp send-time insights](https://mailchimp.com/resources/insights-from-mailchimps-send-time-optimization-system/), [analysis of that data](https://jacobfilipp.com/maildata/insights-from-mailchimps-send-time-optimization-system/index.html).
- **Send Time Optimization:** Mailchimp's feature delivers each email within 24 hours of the date you pick, at the time that contact usually engages. It needs the Standard plan or higher, enough engagement history, and scheduling at least 48 hours ahead. Source: [Mailchimp help](https://mailchimp.com/help/use-send-time-optimization/).
- **What the experts do:** Ben Settle sends one short plain-text email every day and sells in every one ([Ben Settle](https://bensettle.com/blog/how-to-make-6-figures-per-year-writing-one-email-per-day/)). Ann Handley's Total Annarchy goes out every two weeks and is personal and built on stories ([Campaign Monitor case study](https://www.campaignmonitor.com/blog/email-marketing/how-ann-handley-grew-her-newsletter/)). What they share is a fixed, predictable schedule. How often you send matters less than sending on schedule.

## 2. List growth and lead magnets
- **Hormozi ($100M Leads):** A lead magnet should fully solve one narrow problem and, in doing so, reveal the next problem, which the paid offer solves. He names three types: reveal a problem (a diagnosis), give a sample or trial, or give one step of a multi-step process. Make it good enough that you could charge for it, and end with one clear call to action. Source: [$100M Leads summary](https://lythrumpress.com.au/chapter/100m-leads-by-alex-hormozi-section-2/).
- **Ramit Sethi:** Go for quality subscribers over raw numbers. Solve an urgent pain, promote the lead magnet where the audience already spends time, and make signing up easy. Source: [I Will Teach You To Be Rich](https://www.iwillteachyoutoberich.com/how-to-build-an-email-list/).
- **Morning Brew's referral program:** Referrals are widely reported to have driven a large share of its growth. Second-hand reports put the referral share of growth anywhere from about 30 percent to as high as 80 percent in early periods. Source: [Referral Rock](https://referralrock.com/blog/morning-brew-referral-program/). Their setup used personal referral links and rewards that grew at each milestone.

## 3. Segmentation
Tag contacts by role (coach, staff), product interest, and status (lead, customer, former). Send one core email and vary the P.S. by segment. Do not collect a child's email. See the legal section.

## 4. Welcome and nurture sequence
New subscribers are most engaged when they first sign up, so a short sequence works:
1. Day 0: Deliver the lead magnet.
2. Next: one proof point Ryne has approved. Do not invent results.
3. Next: how the offer works, in plain language.
4. Next: one real story, used with permission.
5. Then hand off to the regular send.
Every sequence email goes to Ryne for approval before it is turned on.

## 5. Deliverability
- **Gmail and Yahoo rules (in force since 2024):** Bulk senders must have SPF, DKIM, and DMARC (p=none at minimum), with the From domain aligned. Marketing email must support one-click unsubscribe, and unsubscribes must be honored within 2 days (48 hours). Keep spam complaints under 0.3 percent, ideally under 0.1 percent. Sources: [Gmail sender guidelines](https://support.google.com/mail/answer/81126), [Gmail FAQ](https://support.google.com/a/answer/14229414?hl=en), [Yahoo Sender Hub](https://senders.yahooinc.com/best-practices/).
- **Mailchimp setup:** Authenticate the sending domain (DKIM and DMARC). Validation can take up to 48 hours. Send from your own domain, never from a free webmail address. Source: [Mailchimp domain authentication](https://mailchimp.com/help/set-up-email-domain-authentication/).
- **Plain vs designed, and image-to-text ratio:** Mailchimp advises keeping text above 20 percent of the email and using several content blocks instead of one large image. Source: [Mailchimp content for deliverability](https://mailchimp.com/resources/email-content-for-deliverability/). A marketing email should look like a personal letter, with mostly text, at most one image, and few links. Key copy should be live text, not baked into an image.
- **List hygiene:** Use double opt-in for public forms. Never import scraped or purchased lists or team rosters that didn't opt in. Remove hard bounces.

## 6. Subject lines and preview text
Mailchimp allows subject lines up to 150 characters but recommends 60 or fewer ([Mailchimp](https://mailchimp.com/help/create-ab-tests/)). Subject lines should be specific and concrete. Always write preview text that continues the subject line instead of repeating it. CAN-SPAM bans misleading subject lines ([FTC](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)). Stick to one consistent From name.

## 7. Benchmarks (use with caution)
| Source | Category | Open | Click | Unsub |
|---|---|---|---|---|
| [Mailchimp](https://mailchimp.com/resources/email-marketing-benchmarks/) (data last updated Dec 2023) | Education + Training | 35.64% | 3.02% | 0.18% |
| Mailchimp | All users | 35.63% | 2.62% | 0.22% |
| [SaaS Scored](https://saasscored.com/blog/email-marketing-benchmarks-by-industry), compiling MailerLite/ActiveCampaign/Moosend data | Health & Fitness | 47.81% | 1.45% | 0.29% |
| SaaS Scored | Sports & Recreation | 47.69% | 1.27% | 0.16% |

**Apple MPP:** Apple Mail Privacy Protection loads emails automatically, which records "opens" nobody made. Litmus reports Apple (including MPP) at roughly half of all tracked opens (49.79 percent in March 2025) and says MPP-affected opens can exceed 50 percent of opens. Sources: [Litmus market share](https://www.litmus.com/email-client-market-share/), [Litmus MPP center](https://www.litmus.com/apple-mail-privacy-protection-resources). Treat open rate as a rough trend signal only, useful mainly for spotting a sudden drop that points to a deliverability problem.

## 8. Measuring what matters
Track these each month in a simple sheet:
1. **Replies** per send. The P.S. asks for a reply, so replies are the main signal.
2. **Outcomes booked** that can be traced back to an email (ask how they heard about it).
3. **Click rate** on the single link.
4. **Unsubscribes and spam complaints** (complaints must stay under 0.1 percent).
5. **List growth** net of unsubscribes.
Opens are tracked only to spot deliverability trends.

## 9. A/B testing in Mailchimp
Mailchimp A/B tests one variable at a time (subject line, From name, content, or send time) with up to 3 variations. The test must go to at least 10 percent of the list, and Mailchimp recommends at least 5,000 contacts per variation for reliable results. Send-time tests go to 100 percent of the list. Multivariate tests allow up to 8 combinations. Sources: [Create A/B test](https://mailchimp.com/help/create-ab-tests/), [About A/B tests](https://mailchimp.com/help/about-ab-tests/), [Multivariate](https://mailchimp.com/help/create-multivariate-tests/).
Small lists are far below 5,000 contacts per variation, so treat test results as directional only. Pick winners by clicks, not opens, because MPP inflates opens. Test one thing per month.

## 10. Re-engagement and sunsetting
Mailchimp can find inactive contacts (contact rating or no recent engagement). Send them a re-engagement campaign, then archive those who still don't respond. Archiving removes them from the audience but keeps their data. Sources: [Identify inactive](https://mailchimp.com/help/identify-inactive-subscribers/), [Re-engage](https://mailchimp.com/help/re-engage-inactive-subscribers/), [Archive](https://mailchimp.com/help/remove-inactive-contacts/).
Every quarter, find contacts with no clicks for 6 months (judge by clicks, because MPP opens can't be trusted). Send them 2 short emails, for example "Still want these? Reply yes." Archive anyone who doesn't respond.

## 11. Legal
- **CAN-SPAM (FTC):** No false headers or misleading subject lines. Identify the email as an ad where that applies. Include a valid physical address. Include a clear opt-out that keeps working for 30 days after sending. Honor opt-outs within 10 business days (Gmail and Yahoo require 2 days, so in practice the deadline is 2 days). Being a member doesn't exempt someone from these protections. Sources: [FTC compliance guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business), [FTC 2023 blog](https://www.ftc.gov/business-guidance/blog/2023/08/when-sending-commercial-email-businesses-cant-unsubscribe-can-spam-compliance).
- **Consent:** Use an explicit opt-in checkbox, not pre-checked, and keep a record of it (Mailchimp logs signup source and time). Clients aren't on the marketing list automatically just because they are clients.
- **Minors / COPPA:** COPPA generally requires verifiable parental consent before collecting personal information, including an email address, from a child under 13. The amended rule took effect June 23, 2025, with compliance required by April 22, 2026. Sources: [eCFR 16 CFR 312](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312), [Federal Register 2025](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule), [FTC press release](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-changes-childrens-privacy-rule-limiting-companies-ability-monetize-kids-data). Collect a parent email only for anyone under 13. Get written permission before naming or showing a minor. This is general research, not legal advice.

## 12. Expert frameworks, condensed
- **Hormozi:** Lead magnets that reveal the next problem. Give, give, give, then ask. Source above.
- **Ben Settle:** Send daily, keep it short and in plain text, show personality, and sell in every email. A small sell in every email can live in the P.S.
- **Ramit Sethi:** Quality list, solve an urgent pain, earn the right to sell.
- **Morning Brew:** Referral loop with personal links and milestone rewards. A referral P.S. needs a real reward. Do not invent one.
- **Justin Welsh:** Saturday Solopreneur goes out every week at the same time and has reportedly grown without a referral program ([Newsletter Engines](https://mikeromaine.com/referral-systems-newsletters/)). Lesson: being consistent beats gimmicks.
- **Ann Handley:** Write to one person, tell stories, keep a personal voice. Grew from 0 to 42,000 subscribers ([Campaign Monitor](https://www.campaignmonitor.com/blog/email-marketing/how-ann-handley-grew-her-newsletter/)).
- **Mailchimp / Litmus research:** Authenticate the domain, keep plenty of real text in the email, judge by clicks over opens, and archive inactive contacts.
