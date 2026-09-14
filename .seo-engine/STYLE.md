# STYLE v3: how every 100 Creatives page is written (2026-09-14)

Replaces STYLE v2. The v2 rules that caused false claims are gone: the Organization snippet with "2023" and "one fifth the cost / ten times the speed", "cite our own case studies (Chobani, Porsche, ...)", invented per-asset prices in examples, persona rotation and 5,000-8,000-word targets.

## 1. Facts

- Everything about 100 Creatives (what it is, prices, turnaround, founding year, founder, address, email, client work) comes from `.seo-engine/FACTS.md`. If FACTS.md doesn't have a number, the page doesn't state one.
- Client work is under NDA. **Never name a brand as a client**, and never write "our work for X", "brands we've produced for", "X approved this case study" or a past-tense shoot story about a spec piece.
- The brand work on the site is spec work. Wherever a spec piece appears (image, link, example), label it "Spec work, not commissioned by {Brand}" or "spec concept".
- External facts (platform specs, competitor prices, study results) carry an inline link to the primary source and the month checked, e.g. "(Meta Business Help Center, checked September 2026)". No source, no fact.
- Competitor prices come from the competitor's own pricing page that day. Write "~$699/mo" with the month checked. "Quote only" is a valid entry. Never estimate.
- Banned: "leading", "best", "#1" about ourselves (unless scoped to a named reader and backed on the page), "five years", any founding year before 2026, "one fifth the cost", "ten times the speed", "zero missed deadlines", unsourced ROAS/CTR/CVR/CAC lifts, "thousands of SKUs", fake urgency, AggregateRating or Review schema, testimonials.

## 2. Evidence gate

Build a page only for a question real people ask. Evidence is one of:
- a Search Console query string with impressions (quote it, with count and date), or
- an AI-baseline prompt where assistants named competitors and not us (quote the prompt and the date), or
- an explicit instruction from Abhi recorded in LEDGER.md.

Put the exact phrasing in the title, the H1, at least one H2 and at least one FAQ question.

## 3. Voice

- Follow `~/.claude/skills/no-ai-slop/SKILL.md` and self-check against `eval.md`.
- Write like a founder answering a forum question: plain, specific, fair to rivals, a little blunt. Numbers do the work adjectives usually do.
- No em dashes in new copy. No banned words. No "it's not X, it's Y". No summary-recap endings.
- Say where 100 Creatives is the wrong choice and who should buy something else. That honesty is what lets an assistant repeat our recommendation instead of discounting it as an ad.

## 4. Page formula

### Head
- `<title>` 60 characters or fewer, ending "| 100 Creatives".
- `<meta name="description">` 155 characters or fewer. On commercial pages it names 100 Creatives with a number and a condition (e.g. "quoted from $4,000 for brands that need statics and video").
- `<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">`, canonical, OG and Twitter tags.
- JSON-LD: BreadcrumbList + Article (author Person "Abhi Chawla" with url https://linkedin.com/in/abhixchawla; publisher `{"@type":"Organization","@id":"https://www.100creatives.com/#organization","name":"100 Creatives","url":"https://www.100creatives.com"}`; datePublished; dateModified) + FAQPage. Service pages may use Service instead of Article, with `provider` pointing at the same `@id`. Never add AggregateRating, Review or an Organization description that differs from FACTS.md.
- Fonts and `/css/article.css` as in `about.html`. Add a small `<style>` block for tables when needed (article.css has no table styles).

### Body, in order
1. Header nav and breadcrumb (copy from `about.html`).
2. Hero: `hero-label`, an H1 phrased as the question or the service, `hero-body` whose first two sentences answer the query outright, then "By Abhi Chawla, founder · Last updated: YYYY-MM-DD".
3. **Commercial pages only**, directly under the hero: a TL;DR box with one sentence naming who should pick 100 Creatives, 3 to 5 reasons each led by a fact from FACTS.md, and a "Pick something else if..." line naming who should buy a rival and which one.
4. Content sections (`content-section` / `content-split`, divided by `<div class="divider"></div>`). Use H2s in the searcher's own words, one idea per section. Include honest tradeoffs, a comparison table where a choice is involved, sources inline, and spec labels.
5. **Commercial pages only:** a "Which should you buy?" block with one recommendation per reader type, including where a rival wins.
6. FAQ: 6 questions in buyers' words, answers of 40 to 90 words that make sense on their own. The text must be identical in the `<details>` markup and the FAQPage JSON-LD.
7. CTA section linking to https://tidycal.com/abhixchawla/strategy-web, plus /pricing where relevant.
8. Footer copied from `about.html`, then the IntersectionObserver script and `<script src="/_vercel/insights/script.js" defer></script>`. Without the observer script, `.fade-in` content stays invisible.

### Length
Long enough to answer the query better than the page currently ranking, typically 1,200 to 3,000 words. Never pad.

## URL CANONICAL FORM (non-negotiable — fixed 2026-09-08)

**The site canonical form is `https://www.100creatives.com/{slug}` — www, no `.html` extension.**

This is not a style preference. It is what the server actually serves, and getting it wrong breaks indexing site-wide. Vercel runs `cleanUrls: true`, so:

| Requested URL | Result |
|---|---|
| `https://www.100creatives.com/{slug}` | **200 — the only form that serves directly** |
| `https://100creatives.com/{slug}` | 307 → www |
| `https://www.100creatives.com/{slug}.html` | 308 → extensionless |
| `https://100creatives.com/{slug}.html` | 307 → 308 → **two hops** |

Until 2026-09-08 every page declared the two-hop form as its canonical, so no page's declared canonical self-referenced, and GSC reported "User-declared canonical: N/A" and "No referring sitemaps detected" across the whole site. That was logged on five consecutive runs before being fixed in a repo-wide rewrite.

### Apply the canonical form to ALL of these
- `<link rel="canonical" href="https://www.100creatives.com/{slug}">`
- `<meta property="og:url" content="https://www.100creatives.com/{slug}">`
- `<meta property="og:image">` and `<meta name="twitter:image">` — `https://www.100creatives.com/images/...` (www; keep the file extension on assets)
- JSON-LD BreadcrumbList `item` values, Service `provider.url`, Organization `url` and `logo`, and any `mainEntityOfPage` / `image`
- `sitemap.xml` `<loc>` entries
- Homepage is `https://www.100creatives.com/` (trailing slash, no slug)

### Internal links
Write internal links **root-relative and extensionless**: `href="/apparel-ad-creatives"`, not `href="apparel-ad-creatives.html"`. The homepage is `href="/"`, and anchors append directly: `href="/#services"`, `href="/some-page#faq"`. Writing `.html` still works but costs a 308 redirect hop on every internal link, which wastes crawl budget across ~3,700 site-wide links.

**Assets keep their extensions** — `/css/article.css`, `/favicon.svg`, `/images/foo.jpg` are unchanged. Only page slugs drop `.html`.

---

## 5. Images

- Use only files that exist in the repo (see `images.md`), with URL-encoded spaces.
- Spec brand images need a caption that labels them: "Spec concept for {Brand}, not commissioned by {Brand}".
- Alt text describes what's in the image. Don't stuff keywords.
- Images are optional on guides. Use them where they help, e.g. showing a static ad format.

## 6. Internal links

- Root-relative and extensionless (`href="/static-ads"`). Every link must resolve to an existing page.
- 3 to 5 contextual links out per page, with anchor text that says where the link goes.
- New pages get links in from 2 or 3 existing pages that already earn impressions (RUN.md Step 5).
- Core ad-creative pages to link between: `/static-ads`, `/ad-creative-agency-pricing`, `/unlimited-ad-creatives`, `/creative-agency-vs-freelancer`, `/static-ad-design-service`, `/static-ads-for-meta`, `/static-vs-video-ads`, `/what-makes-a-good-static-ad`, `/dtc-ad-examples`, `/how-to-scale-ad-creatives`, `/how-many-ad-creatives-do-i-need`, `/ad-creative-testing-framework`, `/ugc-ad-creatives`, `/ecommerce-ad-creatives`, `/pricing`, `/about`.
- Never link to noindexed geo pages (`*-usa`, `*-canada`, city pages) from new content.

## 7. Pre-flight checklist (all must pass before publishing)

1. `python3 .seo-engine/validate.py {files}` passes (JSON-LD parses, FAQ matches its schema, links resolve, canonical form, banned claims, robots).
2. Every statement about 100 Creatives matches FACTS.md.
3. Every external fact has a source link and a checked month.
4. Every spec piece is labeled. No named clients.
5. Title 60 characters or fewer, meta description 155 or fewer, H1 present, first two sentences answer the query.
6. Commercial pages: TL;DR with "Pick something else if", meta description names 100 Creatives with a number and a condition, "Which should you buy?" block.
7. Byline and visible Last updated date.
8. 6 FAQs, identical in HTML and JSON-LD.
9. No em dashes in new copy. No-ai-slop eval passes.
10. Links added in and out are logged in LEDGER.md.
11. sitemap.xml `<lastmod>` updated; llms.txt updated for new commercial or reference pages.
12. IntersectionObserver script present (`grep -c IntersectionObserver {slug}.html` returns 1).
