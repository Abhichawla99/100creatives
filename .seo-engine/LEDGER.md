# LEDGER: v3 runs (from 2026-09-14)

Short log of every v3 run. Read all of it at the start of each run (RUN.md Step 1). The v2 archive is MEMORY.md; don't read that end to end.

---

## Baseline, 2026-09-13 (before the repositioning)

**Search Console, 3 months to 2026-09-11:** 61 clicks, about 5K impressions, average position 49.6. **0 external links.**

| Page group | URLs with impressions | Clicks | Impressions |
|---|---|---|---|
| Ad creative / static ads / agency | 27 | 30 | 4,475 (87%) |
| Apparel photography articles | 53 | 1 | 301 |
| Spec brand pages | 11 | 0 | 218 |
| Homepage | 2 | 32 | 171 |

- **Top queries:** static advertising 257 · what is a static ad 195 · what are static ads 185 · scaling strategies for creative agencies 159 · static ad design services 120 · dtc branding agency 120 · what is a static advertisement 107 · scale ad creative without breaking brand systems 97 · ad creative scaling 93 · scaling creative production 88 · dtc marketing agency 80.
- **Google generative AI report:** 112 impressions in 3 months, rising. Top pages: unlimited-ad-creatives 40, homepage 25, creative-agency-vs-freelancer 13, health-and-wellness-ad-creatives 10.
- **Indexing:** 55 indexed, 179 not. Not indexed breaks down as: page with redirect 55, crawled but not indexed 39, alternate canonical 33, redirect error 29 (old apex `.html` URLs), 404 17, noindex 6.
- **Bing AI Performance, 7 days:** 20 citations in Copilot and partners. Grounding query "static ads examples", 13.4% citation share.
- **AI answer baseline** (`aeo/baseline-2026-09-13.json`, ChatGPT web, Perplexity Sonar and Gemini web, 14 buyer prompts × 3 engines): named in **2 of 42** answers, both Perplexity, both ad creative. For "is 100 Creatives legit?", ChatGPT and Perplexity quoted koolav.com (3.0/5, "portfolio fraud red flag").

---

## 2026-09-14, run 0: repositioning sprint (Claude Code with Abhi, not the scheduled task)

- **Decisions from Abhi:**
  - Positioning: AI static and video ad creative agency.
  - Pricing: publish the existing buckets and ranges.
  - Spec work: label everywhere and noindex the brand pages.
  - Founded 2026. Client work is under NDA. Keep abhi@paperkites.co.
  - Ship everything once validation passes.
  - Leave the 88 older long-form apparel/photography articles as they are (no noindex, no further cleanup).
- **Safety:**
  - `.vercelignore` stops `.seo-engine/`, `lib/` and `.claude/` from being served.
  - `publish.sh` fallback pushes only named files and accepts extra files.
- **Entity:**
  - New `/about`.
  - Homepage, `/pricing`, `/faq` and `llms.txt` rewritten from FACTS.md.
  - One Organization schema sitewide (foundingDate 2026, one address).
  - AggregateRating 5.0/42 removed.
- **Trust:**
  - Every homepage work card and all 34 spec pages labeled "Spec work, not commissioned by {Brand}".
  - Named-client claims, "leading", "five years", "one fifth the cost", "zero missed deadlines" and "thousands of SKUs a month" removed from 51 pages.
  - Contractual accuracy guarantee claims (not in the terms) removed from 9 pages.
  - "Cancel anytime" aligned with the refund policy.
- **Indexing:** noindex, follow on 35 spec pages (incl. /campaigns) and 14 city/country apparel pages, all removed from the sitemap.
- **New pages:**
  - `/static-ads` (definition, specs checked 2026-09-14)
  - `/ad-creative-agency-pricing` (21 services, every price checked on the vendor's page 2026-09-14)
- **Rebuilt:**
  - `/unlimited-ad-creatives`, `/creative-agency-vs-freelancer`, `/static-ad-design-service`
  - `/dtc-ad-examples`, `/what-makes-a-good-static-ad`, `/static-vs-video-ads`, `/static-ads-for-meta`
  - Accuracy fixes on `/ecommerce-ad-creatives` and `/fast-ad-creative-turnaround`
- **Engine v3:** FACTS.md, RUN.md, STYLE.md, topics.json (9 jobs), validate.py, OFFSITE.md, aeo baseline script.
- **Validation:** `validate.py --changed` passes except 34 FAQ visible/JSON-LD mismatches that were already live on origin/main before today (see debt).
- **Shipped:** origin/main `3e7e523`, verified live 2026-09-14. New pages return 200 with self-referencing canonicals. `/.seo-engine/*`, `/lib/*` and `/.claude/*` return 404. Spec and geo pages serve `noindex, follow`. The live sitemap has 134 URLs.
- **IndexNow:** HTTP 200 for 70 URLs (every page with a visible change, plus the sitemap).
- **Search Console:** `/static-ads` inspected as "URL is unknown to Google". Request indexing returned "Quota Exceeded", because the 09-14 v2 run had already used the quota, so nothing was requested. The whole indexing debt list below is still open.
- **Links added:**
  - /static-ads ← what-makes-a-good-static-ad, dtc-ad-examples, static-ads-for-meta, static-vs-video-ads, ecommerce-ad-creatives, fast-ad-creative-turnaround, index, about
  - /ad-creative-agency-pricing ← unlimited-ad-creatives, creative-agency-vs-freelancer, static-ad-design-service, static-ads-for-meta, pricing, faq, about, index
  - /about ← index (nav and footer), faq (nav)

---

## 2026-09-15, run 1: fix

- **Signal (28 days, GSC Performance):** 20 clicks, 1.48K impressions, 1.4% avg CTR, avg position 53.1. Top queries: static advertising 77 · scaling strategies for creative agencies 54 · what is a static ad 52 · what are static ads 45 · ad creative scaling 30 · scale ad creative without breaking brand systems 29 · scaling creative production 22 · "when should a dtc ecommerce brand hire a google ads agency instead of a freelancer?" 21 · health and wellness cpg branding agency 17. Top pages by impressions: what-makes-a-good-static-ad 368+53, how-to-scale-ad-creatives 284, static-ads-for-meta 136+27, unlimited-ad-creatives 150+10. No query or page surfaced that isn't already covered by a queued topics.json job.
- **Indexing:** 55 indexed / 179 not indexed, unchanged from the 2026-09-13 baseline (page with redirect 55, crawled-not-indexed 39, alternate canonical 33, redirect error 29, 404 17, noindex 6). No drop since last run, so a new page was not ruled out on that basis, but a Fix job took priority per Step 3.1.
- **URL:** https://www.100creatives.com/how-many-ad-creatives-do-i-need
- **Evidence:** LEDGER 2026-09-14 "Known debt" note: page still said "unlimited"/"$5M+" and contradicted FACTS.md's quoted-project pricing model; explicitly queued as "next run should start with" this fix.
- **Changed:**
  - Hero subtitle: removed the unsourced "$5M+ in revenue" framing and "every brand we work with" claim; reframed to the article's own $30K-$100K spend-tier language.
  - Removed two "unlimited ad creatives" self-claims (mid-article and CTA). 100 Creatives quotes fixed-total project batches per FACTS.md, it does not sell an unlimited/flat-monthly plan (confirmed against the live /unlimited-ad-creatives page, which says the same).
  - CTA line rewritten to "quotes static and video ad creative batches with a 48-hour turnaround... a fixed total before work starts" (both claims sourced from FACTS.md).
  - Added byline "By Abhi Chawla, founder" + visible "Last updated: September 15, 2026" under the hero (was missing).
  - Fixed FAQ markup: added `faq-question` / `faq-answer` classes so validate.py's parser can read the visible Q&A (it already matched the JSON-LD word for word, but the generic `.faq-item h3/p` markup wasn't recognized). Removed 2 stray em dashes from FAQ answers (visible + JSON-LD, kept identical).
  - Shortened title (64 → 49 chars) and meta/OG/Twitter description (207 → 137 chars) to pass STYLE.md length limits; updated `dateModified` to 2026-09-15.
  - sitemap.xml `<lastmod>` bumped to 2026-09-15 for this URL.
- **Links added:** none new (page already carries 5 contextual outbound links: /unlimited-ad-creatives, /fast-ad-creative-turnaround, /ecommerce-ad-creatives, /performance-creative-agency, /ad-creative-testing-framework). No inbound-link step required for a fix job.
- **Validation:** `python3 .seo-engine/validate.py how-many-ad-creatives-do-i-need.html` → `ok`, 0 failures, 0 warnings (was 1 failure + 3 warnings before the fix).
- **IndexNow:** HTTP 200, accepted (Bing/Yandex/Seznam/Naver notified for this URL + sitemap.xml).
- **GSC:** URL Inspection showed "URL is not on Google" (unknown to Google, no referring sitemap/page detected yet). Request Indexing → "Indexing requested, added to priority crawl queue." No quota error today (unlike 09-14, which had already burned the day's quota).
- **New signal noticed, not acted on:** GSC Overview recommendation flagged `https://www.100creatives.com/static-ads-for-meta.html` (the old `.html` URL form) down 93% in impressions recently. That's expected decay of the deprecated non-canonical URL now that `/static-ads-for-meta` (extensionless) is live and 308-redirecting it; flagging here in case it's actually a canonicalization problem worth checking next run.
- **Local checkout note:** `.git/index.lock` and `.git/ORIG_HEAD.lock` in the local sandbox mount are not removable (`Operation not permitted`), so `git pull`/`git stash` fail there. Read every engine file via `git show origin/main:...` instead of trusting the local working tree, and synced `.seo-engine/{LEDGER.md,state.json,topics.json}` and `sitemap.xml` from `origin/main` before editing them, per RUN.md Step 0's guidance to continue rather than abort. Published through publish.sh's fallback path.
- **Next run should start with:** the next item on the "Four core ad pages" debt list — `ad-creative-testing-framework` (remove the unsourced "20-40% CAC reduction" claim per its topics.json S7 angle, and check it for the same "unlimited"/"$5M+" language), then spend the Search Console quota on the indexing debt list below.

---

## 2026-09-16, run 2: fix

- **Signal:** not re-pulled from Search Console this run (Claude in Chrome signal-gathering step skipped; see note below). Indexing last confirmed 2026-09-15: 55 indexed / 179 not indexed, unchanged from the 2026-09-13 baseline.
- **URL:** https://www.100creatives.com/ad-creative-testing-framework
- **Evidence:** LEDGER 2026-09-15 run 1 "Next run should start with" note: fix `ad-creative-testing-framework` — remove the unsourced "20-40% CAC reduction" claim per its topics.json S7 angle, and check it for the same "unlimited"/"$5M+" language flagged in the 2026-09-14 Known Debt list. Confirmed directly on the page (opened and read the live copy).
- **Changed:**
  - Removed the unsourced "typically see a 20-40% reduction in customer acquisition cost within the first 60 days" claim (banned per FACTS.md: no unsourced CAC/ROAS/CTR/CVR lift stat). Replaced with a claim-free sentence about what a testing system does mechanically.
  - Removed "DTC brands doing $5M+ per year" framing about our client base (same unsourced-scale claim the 2026-09-15 fix removed from `how-many-ad-creatives-do-i-need`).
  - Rewrote "Our clients typically test 15-25 new ad creatives per week... competitors who are still waiting two weeks for their agency" (unsourced client-behavior stat, competitor jab, and an implied unlimited/continuous creative stream that contradicts FACTS.md's fixed-quote project model) into a sentence about the 48-hour turnaround and fixed-total quoting, both sourced from FACTS.md. Dropped the anchor link to `/unlimited-ad-creatives` since the sentence no longer describes unlimited velocity.
  - Fixed the Article JSON-LD `author` from `Organization` to `Person` "Abhi Chawla" (linkedin.com/in/abhixchawla) per STYLE.md; added `publisher.@id`; bumped `dateModified` to 2026-09-16.
  - Added the missing byline "By Abhi Chawla, founder" + visible "Last updated: September 16, 2026" under the hero (STYLE.md pre-flight checklist item 7 — page had neither).
  - Shortened the meta/OG/Twitter/JSON-LD description from 182 to 139 characters (STYLE.md caps it at 155).
  - Fixed a pre-existing FAQ visible/JSON-LD text mismatch (curly quotes in the visible HTML vs straight quotes in the JSON-LD, in the "angles vs variations" answer) that was failing `validate.py`. This page was on the "Legacy FAQ mismatches" Known Debt list; removed from that list below.
  - `sitemap.xml` `<lastmod>` bumped to 2026-09-16 for this URL.
- **Links added:** none new. No inbound-link step required for a fix job.
- **Validation:** `python3 .seo-engine/validate.py ad-creative-testing-framework.html` → `ok`, 0 failures (1 advisory warning: 5 pre-existing em dashes in body copy I did not touch; no em dashes in the new copy).
- **IndexNow:** see publish step below.
- **GSC:** URL Inspection for `/ad-creative-testing-framework` showed "URL is not on Google" (unknown to Google, no referring sitemap/page detected yet — expected for a page that was live before today but is only now picking up a fresh `<lastmod>`). Request Indexing → **Quota Exceeded** ("Sorry, we couldn't process this request because you've exceeded your quota. Please try submitting this again tomorrow."). Also observed on the Overview/Indexing panel while there: 74 indexed / 191 not indexed pages (up from the 55/179 baseline tracked since 2026-09-13 through 2026-09-15 — real movement, not re-verified against the Pages breakdown this run, so treat as a signal to confirm next run rather than a confirmed trend). The `static-ads-for-meta.html` (old non-canonical URL) impressions-drop recommendation flagged on 2026-09-15 is still showing on the Overview page.
- **Local checkout note:** same sandbox-mount issue as 2026-09-15 — local `.git` had stuck lock files and 14 commits of stale local history behind `origin/main`, plus leftover uncommitted working-tree changes from a prior aborted run (already superseded by what's on origin). Synced `.seo-engine/{LEDGER.md,state.json,topics.json,FACTS.md,STYLE.md,RUN.md,validate.py}` and `sitemap.xml` from `origin/main` via `git show` before editing, confirmed local `LEDGER.md`/`state.json` already matched origin byte-for-byte, then edited the working tree directly. Did not attempt `git reset --hard`/`git clean` with elevated permissions after it failed once with `Operation not permitted`; left recovery to `publish.sh`'s fallback path per RUN.md Step 0.
- **Next run should start with:** the remaining "unlimited"/"flat monthly"/"$5M+" Known Debt items — `ugc-ad-creatives` and `performance-creative-agency` — then a full Step 2 Search Console pull (this run only opened Overview + one URL Inspection, not the full Performance/Pages breakdown) once the indexing quota resets. Indexing-debt list below still open; today's quota was spent on `/ad-creative-testing-framework` itself (Quota Exceeded on the first request of the day, so the list below got none of today's quota — investigate whether another process used it earlier today).

---

## 2026-09-17, run 3: fix

- **Signal (28 days, GSC Performance):** 23 clicks, 1.52K impressions, 1.5% avg CTR, avg position 51. Top queries: static advertising 77 · what is a static ad 54 · scaling strategies for creative agencies 53 · what are static ads 46 · ad creative scaling 30 · scale ad creative without breaking brand systems 29 · scaling creative production 23 · "when should a dtc ecommerce brand hire a google ads agency instead of a freelancer?" 22 · static ad 18. No new query or page surfaced outside topics.json's queued jobs.
- **Indexing:** 74 indexed / 191 not indexed (page with redirect 68, crawled-not-indexed 42, alternate canonical 28, redirect error 29, 404 17, noindex 7). Confirms the 74/191 movement run 2 flagged as "not re-verified" — same count today, so treat as the new stable baseline rather than a one-off blip.
- **Job:** `run_count` was 2 (2 % 3 == 2), so this run is fix/strengthen only per RUN.md Step 3. Took the fix-first Known Debt item queued by run 2's "Next run should start with": `ugc-ad-creatives`.
- **URL:** https://www.100creatives.com/ugc-ad-creatives
- **Evidence:** LEDGER 2026-09-16 run 2 "Next run should start with" note, and the Known Debt "Core ad pages still say unlimited/flat monthly/$5M+" line naming `ugc-ad-creatives` and `performance-creative-agency`. Confirmed directly on the page (opened and read the live copy).
- **Changed:**
  - Removed the unsourced "Data from hundreds of DTC campaigns shows... 15 to 30 percent lower CPAs" claim (banned: unsourced CAC/CPA lift stat) and the duplicate "consistently see 15 to 30 percent lower cost per acquisition" claim in the insights grid. Rewrote both sentences around mechanics (why the format earns attention, why it fits cold prospecting) instead of an invented number.
  - Removed "We have designed UGC ad creatives for DTC brands doing five million dollars a year and up" (the same unsourced-scale "$5M+" claim already removed from `how-many-ad-creatives-do-i-need` and `ad-creative-testing-framework`). Replaced with the FACTS.md-sourced brand-intake process (visual language, model preferences, colorways, export specs).
  - Fixed the footer tagline "High-converting static ad creatives for DTC brands doing $5M+ a year" to match the current sitewide copy ("AI-made static and video ads for DTC and consumer brands. Calgary, Canada.", per `about.html`/`index.html`).
  - Added the missing byline "By Abhi Chawla, founder" + visible "Last updated: September 17, 2026" under the hero (STYLE.md checklist item 7 — page had neither).
  - Fixed all 5 FAQ visible/JSON-LD text mismatches (visible HTML had extra "Learn more about..." link sentences and straight punctuation that the JSON-LD `text` fields didn't carry, plus em-dash list formatting in the JSON-LD that the visible copy didn't use). Unified both to the same plain text per question, added to the "Legacy FAQ mismatches" Known Debt list's implicit scope even though this page wasn't named on it.
  - Shortened the title (63 → 53 chars) and meta/OG/Twitter description (166 → 141/130/91 chars) to pass STYLE.md's 60/155-char limits; new meta description names 100 Creatives with the $4,000 starting quote per STYLE.md item 6.
  - Fixed the Service JSON-LD `offers` block: replaced the vague "Flat, transparent pricing" description (which implied a flat-rate/monthly plan FACTS.md doesn't support) with the same quoted-budget-range wording used on `static-ad-design-service`, and added `priceCurrency`/`priceSpecification` (minPrice 4000) to match.
  - `meta name="author"` changed from "100 Creatives" to "Abhi Chawla" to match the new visible byline.
  - `sitemap.xml` `<lastmod>` bumped to 2026-09-17 for this URL.
- **Links added:** none new. No inbound-link step required for a fix job; page already carries contextual outbound links to /static-ads-for-meta, /how-to-scale-ad-creatives, /ecommerce-ad-creatives, /how-many-ad-creatives-do-i-need, /skincare-ad-creatives, /supplement-ad-creatives, /food-and-beverage-ad-creatives, /creative-agency-vs-freelancer, /dtc-ad-examples, /what-makes-a-good-static-ad, /performance-creative-agency, /static-ads-for-meta, /fast-ad-creative-turnaround, /dtc-creative-agency.
- **Validation:** `python3 .seo-engine/validate.py ugc-ad-creatives.html` → `ok`, 0 failures, 0 warnings. Manual no-ai-slop check: 0 banned words, 0 em dashes in the file.
- **IndexNow:** see publish step below.
- **GSC:** see publish step below.
- **Local checkout note:** same sandbox-mount issue as runs 1 and 2 — `.git/index.lock` in the local mount is not removable (`Operation not permitted`), and `git pull --rebase` fails on it even though the branch was already up to date with `origin/main` (only local diff was an irrelevant `.claude/settings.local.json` change plus a stray untracked temp file). Edited the working tree directly since RUN.md Step 0 says continue rather than abort; left recovery to `publish.sh`'s fallback path.
- **Next run should start with:** the last remaining "unlimited"/"flat monthly"/"$5M+" Known Debt item — `performance-creative-agency` — then a full Step 2 pull including the Pages breakdown (this run only pulled the Queries breakdown and the Indexing overview, not per-page positions) once that's done. Indexing debt list below still open; spend today's quota on it after `ugc-ad-creatives`.

---

## Indexing debt (request in Search Console in this order, about 3 a day)

1. https://www.100creatives.com/static-ads
2. https://www.100creatives.com/ad-creative-agency-pricing
3. https://www.100creatives.com/about
4. https://www.100creatives.com/
5. https://www.100creatives.com/unlimited-ad-creatives
6. https://www.100creatives.com/creative-agency-vs-freelancer
7. https://www.100creatives.com/pricing
8. https://www.100creatives.com/what-makes-a-good-static-ad
9. https://www.100creatives.com/static-ad-design-service
10. https://www.100creatives.com/dtc-ad-examples

## Known debt (not fixed on 2026-09-14)

- **Legacy FAQ mismatches.** 33 pages have visible FAQ text that differs from their FAQPage JSON-LD, all present before 2026-09-14. Core ad pages still in that list (apparel, beauty, skincare, supplement, health-and-wellness and food-and-beverage ad creatives, cpg-creative-agency) get fixed when their strengthen job comes up. (`ad-creative-testing-framework` fixed 2026-09-16, see run 2 above.)
- **`/what-to-look-for-in-an-ai-product-photography-agency`** tells buyers that capped revisions and no contractual accuracy guarantee are red flags. Our own terms cap revision rounds and offer no such guarantee. Rewrite before strengthening anything else in the photography lane.
- **Core ad pages still say "unlimited", "flat monthly" or "$5M+":** performance-creative-agency. Fix-first priority (RUN.md Step 3.1), one per run. (`how-many-ad-creatives-do-i-need` fixed 2026-09-15, `ad-creative-testing-framework` fixed 2026-09-16, `ugc-ad-creatives` fixed 2026-09-17, see runs 1-3 above.)
- **The 88 older apparel/photography articles** still contain unsourced third-party attributions (Andrew Foxwell, Common Thread Collective, BoF, Vogue), guarantees and prices that aren't on /pricing. Abhi chose to leave them as they are on 2026-09-14, so don't bulk-edit them. Touch one only when it's the target of a fix or strengthen job.
- **`images/barefootwines/barefoot-2.png`** prints its subline twice. It's used on dtc-ad-examples.
- **Titles ending "| 100"** on 43 older pages. Change to "| 100 Creatives" when a page is touched.

## Corroboration queue (Abhi's actions; details in OFFSITE.md)

- [ ] Vercel apex redirect 307 → 308
- [ ] Bing Webmaster Tools: add/verify www property, submit sitemap
- [ ] LinkedIn company page: fix the website field (currently thealternativestudios.com) and paste the profile copy
- [ ] Koolav "Submit evidence" after the deploy is live
- [ ] Clutch profile, plus review requests to NDA clients
- [ ] Pitch the cited lists (OFFSITE.md section 5)
- [ ] Cowork task prompt → "Read RUN.md and follow it exactly"
- [ ] Trademark question on "100 Creatives™" (lawyer)

**Next run should start with:** see the 2026-09-17 run 3 entry above — `performance-creative-agency` fix, then a full Step 2 Pages-breakdown pull, then the indexing debt list.
