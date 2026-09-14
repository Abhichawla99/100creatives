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
- **Links added:**
  - /static-ads ← what-makes-a-good-static-ad, dtc-ad-examples, static-ads-for-meta, static-vs-video-ads, ecommerce-ad-creatives, fast-ad-creative-turnaround, index, about
  - /ad-creative-agency-pricing ← unlimited-ad-creatives, creative-agency-vs-freelancer, static-ad-design-service, static-ads-for-meta, pricing, faq, about, index
  - /about ← index (nav and footer), faq (nav)

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

- **Legacy FAQ mismatches.** 34 pages have visible FAQ text that differs from their FAQPage JSON-LD, all present before today. Core ad pages in that list (apparel, beauty, skincare, supplement, health-and-wellness and food-and-beverage ad creatives, ad-creative-testing-framework, cpg-creative-agency) get fixed when their strengthen job comes up.
- **`/what-to-look-for-in-an-ai-product-photography-agency`** tells buyers that capped revisions and no contractual accuracy guarantee are red flags. Our own terms cap revision rounds and offer no such guarantee. Rewrite before strengthening anything else in the photography lane.
- **Four core ad pages still say "unlimited", "flat monthly" or "$5M+":** how-many-ad-creatives-do-i-need, ad-creative-testing-framework, ugc-ad-creatives, performance-creative-agency. Fix-first priority (RUN.md Step 3.1), one per run.
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

**Next run should start with:** RUN.md Step 3.1 fix job on `/how-many-ad-creatives-do-i-need` (remove "unlimited"/"flat monthly"/"$5M+" claims, align with FACTS.md), then spend the Search Console quota on the indexing debt list above.
