# Email design research

Researched 2026-10-14. Every figure below was read in the linked source. Where a source gave no number, none is given here.

## 1. Layout and width
- Mailchimp: "Set email width to 600px or less. Most people view messages in their preview panes, which are narrow and small." Its templates are "never more than 600 pixels wide, or they're fluid-width." https://mailchimp.com/help/about-html-email/
- Mailchimp templates are "designed to be no greater than 600px wide." https://mailchimp.com/help/about-template-widths/
- Mailchimp's HTML email basics: 600 to 800px maximum, "Design for simplicity," avoid floats/positioning, and do not build an email that is "one large, sliced-up image." https://templates.mailchimp.com/getting-started/html-email-basics/
- Takeaway: one single column, 600px max, fluid on phones.

## 2. Mobile and responsive
- Mailchimp: use media queries to increase text size on small screens and give links "thumb-sized (~46x46px) hit areas." https://templates.mailchimp.com/getting-started/html-email-basics/
- Mailchimp accessibility guide: buttons "at least 44 by 44 pixels" with space around them. https://mailchimp.com/resources/accessibility-in-email-marketing/
- WCAG 2.2 Target Size (Minimum) SC 2.5.8 sets 24x24 CSS px as the AA floor; 44x44 is the stronger AAA (2.5.5) target. https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html

## 3. Dark mode
- Litmus: optimize logos for both modes, use transparent PNGs, and "add a slight white shadow to images with dark text to keep them readable in Dark Mode." Use high-contrast text/background so partial and full color inverts stay readable. https://www.litmus.com/blog/new-in-litmus-extended-dark-mode-testing
- Litmus developer tips: design with midtones, use a glow or stroke, or put the logo on a shape/background; add `@media (prefers-color-scheme: dark)` styles and duplicate for Outlook with `[data-ogsc]`/`[data-ogsb]`. https://www.litmus.com/blog/coding-emails-for-dark-mode
- Litmus: dark-mode meta tags must be included or the media queries have no effect; image swap mostly works in Apple Mail clients (and Outlook.com only with linked images). https://www.litmus.com/blog/ama-email-developer-tips
- Full guide: https://www.litmus.com/blog/the-ultimate-guide-to-dark-mode-for-email-marketers

## 4. Images and alt text
- Mailchimp: "Assume images will be initially blocked." Use absolute image URLs on a reliable host. https://templates.mailchimp.com/getting-started/html-email-basics/
- Mailchimp alt text: keep it to 1 or 2 sentences, do not repeat captions, mark purely decorative images, and test with images off. https://mailchimp.com/help/add-alt-text-to-images/
- Mailchimp accessibility: keep alt text "under 150 characters"; "Important information should always be in actual text, not embedded in graphics." https://mailchimp.com/resources/accessibility-in-email-marketing/

## 5. Image-to-text ratio
- I found no authoritative source in this pass that publishes a specific ratio, so none is cited. The sourced principle: do not send an all-image email (Mailchimp basics link above) and keep key info in live text (Mailchimp accessibility link above).
- HubSpot's analysis of over half a billion customer emails found even a single image reduced click rate. https://blog.hubspot.com/marketing/plain-text-vs-html-emails-data

## 6. Fonts and fallbacks
- Webmail clients strip head/body tags in some cases; Mailchimp advises inline CSS. https://mailchimp.com/help/about-html-email/
- Litmus's own production code uses a stack ending in `Helvetica, Arial, sans-serif`. https://www.litmus.com/blog/the-ultimate-guide-to-dark-mode-for-email-marketers
- Mailchimp accessibility: body text "at least 14 pixels"; avoid all caps beyond short headings. https://mailchimp.com/resources/accessibility-in-email-marketing/
- Inter is not installed on most recipients' devices, so it lives only inside images (header and card). Body is live text in `Helvetica, Arial, sans-serif`.

## 7. Color, contrast, accessibility
- WCAG 2.2 SC 1.4.3 Contrast (Minimum, AA): 4.5:1 for normal text, 3:1 for large text (18pt, or 14pt bold). https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- WCAG SC 1.4.1 Use of Color: do not rely on color alone to identify links. https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
- Mailchimp: avoid "click here" link text; use descriptive links. https://mailchimp.com/resources/accessibility-in-email-marketing/

Computed contrast (WCAG relative luminance formula, run 2026-10-14):
| Pair | Ratio | AA normal text (4.5) |
|---|---|---|
| #c82536 on #ffffff | 5.56:1 | Pass |
| #ffffff on #c82536 | 5.56:1 | Pass |
| #222222 on #ffffff | 15.91:1 | Pass |
| #333333 on #ffffff | 12.63:1 | Pass |
| #666666 on #ffffff | 5.74:1 | Pass |
| #c82536 on #121212 (dark mode) | 3.37:1 | Fails normal, passes large only |

## 8. Buttons vs text links
- Campaign Monitor: a CTA button instead of a text link gave them "a 28% increase in click-throughs" (their own test). Image buttons are risky because many clients block images. https://www.campaignmonitor.com/email/use-buttons-in-email-campaigns/
- Bulletproof buttons are HTML/CSS (VML for Outlook) with live text. https://www.emailonacid.com/blog/article/email-development/how-to-make-your-emails-bulletproof/ and generator https://www.buttons.cm/

## 9. Gmail clipping
- Gmail clips HTML over 102 KB (102,000 bytes) and shows "View entire message." Hosted image file size does not count; the code does. https://docs.aweber.com/message-editors/messages/why-is-my-message-clipped-in-gmail
- Clipping can hide the unsubscribe link and tracking pixel. https://help.activecampaign.com/hc/en-us/articles/115001060524-Why-is-Gmail-clipping-my-email
- Klaviyo: mobile limits can be lower, around 20 KB on iOS (applied inconsistently) and around 75 KB on other mobile devices. https://help.klaviyo.com/hc/en-us/articles/115000591251
- A one-tip email is far below this; just avoid pasting bloated code.

## 10. Mailchimp tips
- Width cannot be changed in the builder; wider than 600px needs custom code. https://mailchimp.com/help/about-template-widths/
- Merge tags such as `*|FNAME|*` personalize; set a default value for missing names. https://mailchimp.com/help/getting-started-with-merge-tags/ and https://mailchimp.com/help/all-the-merge-tags-cheat-sheet/
- Preview text: set it in the campaign field; in custom code use `*|MC_PREVIEW_TEXT|*`. https://mailchimp.com/help/edit-your-emails-subject-preview-text-from-name-or-from-email-address/
- Test with live merge tag info or a small live segment; normal tests do not fill contact merge tags. https://mailchimp.com/help/preview-and-test-your-email-campaign/
- Recommendation: the drag-and-drop builder is enough (Image, Text, Button blocks). No custom code needed.

## 11. Plain text vs designed: evidence
- HubSpot A/B tests: plain text beat a GIF version with 42% more clicks; an HTML template with images got 51% fewer clicks than plain text; a simple HTML template beat an HTML-heavy one with 30% more clicks. https://blog.hubspot.com/marketing/plain-text-vs-html-emails-data
- HubSpot 2014 survey: 64% said they prefer HTML emails; 79% of ages 30 to 44 vs 49% of those over 60. Stated preference and observed clicks disagree. https://cdn2.hubspot.net/hub/53/file-2191769206-pdf/Science_of_Email_Marketing_2014.pdf
- Litmus test: plain text style won with customers, but they note the first test was flawed (messaging differed too); for non-customers format did not seem to matter. https://www.litmus.com/blog/the-results-are-in-a-b-testing-html-vs-plain-text-emails
- Takeaway: light design, mostly live text, few images. That is exactly "simple, professional."

---
