# Off-site kit: what Abhi does outside the website

Last updated 2026-09-14. The daily engine can't do any of this. It posts nowhere, emails no one and changes no account settings.

**Why this matters more than new pages.** On 2026-09-13, 100 Creatives appeared in 2 of 42 AI answers to buyer questions (both on Perplexity). The agencies that did get recommended (Y'all, Flighted, Darkroom, Common Thread Collective, Brighter Click, inBeat) are named on third-party lists and Clutch profiles that the assistants cite. When asked "is 100 Creatives legit?", ChatGPT and Perplexity both quoted Koolav's review. DialSheet saw the same pattern on 2026-09-08: assistants quote your prices from your own site, but they recommend companies other sites vouch for.

Every description below matches `.seo-engine/FACTS.md`. Don't add claims the site doesn't make.

---

## 1. One-time settings (about 20 minutes total)

1. **Vercel → Domains → 100creatives.com.** Change the apex redirect to www from 307 to **308 (permanent)**. Search Console shows 29 "redirect error" and 55 "page with redirect" URLs from the old apex links, and DialSheet cleared the same pattern this way.
2. **Bing Webmaster Tools.** The verified property is `https://100creatives.com/` (apex). Add or verify `https://www.100creatives.com/`, submit `https://www.100creatives.com/sitemap.xml`, and check AI Performance weekly.
3. **Search Console → Settings.** Confirm the generative AI features control is set to "Include".
4. **LinkedIn company page** (ca.linkedin.com/company/100creatives). The website field points to thealternativestudios.com, which doesn't resolve. Change it to https://www.100creatives.com and paste the copy in section 3.
5. **GitHub repo.** Abhichawla99/100creatives is public, so `.seo-engine/` (including MEMORY.md) is readable on GitHub even though the website no longer serves it. Consider making the repo private. Vercel's Git integration works with private repos, but confirm deploys still trigger afterwards.
6. **Cowork task `100creatives-daily-seo`.** Its prompt (~/Documents/Claude/Scheduled/100creatives-daily-seo/SKILL.md) still describes the retired apparel/persona routine. RUN.md v3 says it overrides that prompt, but replacing the prompt with "Read /Users/home/100creatives/.seo-engine/RUN.md and follow it exactly" removes the conflict.
7. **Name.** Chase Chappell sells a static ad template pack called "100 Creatives™" in the same market. Ask a trademark lawyer whether that affects your use of the name. This isn't legal advice.

## 2. Koolav: ask for a re-evaluation (after the site changes are live)

Koolav's page (koolav.com/agency/100-creatives, evaluated 2026-08-27, 3.0/5, "Conditional") has a "Submit evidence" form. Paste this:

```
Hi, I'm Abhi Chawla, founder of 100 Creatives. Your August 27 review flagged real problems. Here is what we changed on September 14, 2026:

1. Portfolio: every brand piece on the site is now labeled "Spec work, not commissioned by {Brand}". Most of our client work is under NDA, and the homepage, FAQ and About page now say so.
2. Pricing: ad creative is quoted in published budget ranges of $4,000 to $10,000, $10,000 to $25,000, $25,000 to $50,000 and $50,000+ (USD). Product photography starts at $5,000 and workflow builds at $4,000. We don't sell an unlimited plan, and the pages that implied one were rewritten.
3. Terms: the "cancel anytime" wording is gone. Ongoing engagements can be stopped before the next billing date, and fees already paid aren't refunded, which matches our refund policy.
4. Company: a new About page lists the founder, legal entity (2587689 Alberta Ltd.), address and founding year (2026).

About page: https://www.100creatives.com/about

Could you re-evaluate the listing?
```

Koolav also flagged things this sprint did **not** change: no named QC step before client review, source files withheld unless scoped, no multi-language or multi-market delivery, and no reviews. If you have a real QC step, tell me what it is and I'll add it to FACTS.md and the About page before you submit.

## 3. Profile copy (LinkedIn, Clutch, DesignRush, Sortlist)

**Tagline (up to 120 characters):**
AI-made static and video ads for DTC and consumer brands on Meta, TikTok and Google.

**Short description:**
100 Creatives is an AI-powered creative agency in Calgary, Canada. We make static and video ads, and the product imagery behind them, for DTC and consumer brands advertising on Meta, TikTok and Google. There's no studio or shoot to book, so batches come back in 48 hours. Every engagement is quoted in writing, and ad creative budgets start at $4,000 USD.

**Long description:**
100 Creatives makes static ads, AI-made video ads, UGC-style statics and product imagery for brands that need a steady supply of new creative to test. We make the work with AI image and video tools and art-direct every asset against a brand intake covering visual language, model preferences, colorways and export specs. Batches come back in 48 hours, and revisions come back within 48 hours.

We also build brand-trained production workflows that in-house teams can run themselves.

Pricing is quoted per engagement. Ad creative budgets run $4,000 to $10,000, $10,000 to $25,000, $25,000 to $50,000 and $50,000+. Product photography starts at $5,000 per project and workflow builds at $4,000. Most client work is under NDA, so our public portfolio is labeled spec work.

Founded in 2026 by Abhi Chawla. 2587689 Alberta Ltd., #315, 405 64 Ave NE, Calgary, Alberta.

**Services to select:** advertising / ad creative, graphic design, video production, product photography.
**Founded:** 2026. **Location:** Calgary, Alberta, Canada.
**Minimum project size:** $4,000 USD. If the directory only offers fixed brackets, pick the closest one that doesn't overstate it.

## 4. Reviews from NDA clients

A Clutch review reads as independent proof to both buyers and AI answers. Clients under NDA can usually review without naming their company. Check that Clutch's current form still allows it before you send the request. Only ask real clients, never pay for reviews, and don't write the review for them.

Plain-text email, one link:

```
Subject: 5 minutes to review our work together?

Hi {first name},

Thanks again for working with us on {project}. Would you be willing to leave a short review of 100 Creatives on Clutch? You can keep your company name private, so nothing in our NDA gets exposed.

Clutch runs a short form or a 15-minute call, whichever you prefer:
{Clutch review link}

Either way, I appreciate it.

Abhi
```

## 5. Pitching the lists AI assistants cite

These pages were cited when ChatGPT and Perplexity recommended ad creative agencies on 2026-09-13. Most are written by other agencies, so inclusion isn't guaranteed. Pitch the ones that list agencies beyond their own:

- webtonic.io/blog/best-ad-creative-agencies
- webtonic.io/blog/best-creative-strategy-agencies
- webtonic.io/blog/best-meta-ads-fb-ig-agencies
- thesnowmedia.com/resources/best-meta-ads-agencies-dtc-brands/
- wittimarketing.com/blog/10-best-meta-ads-paid-social-agencies-for-dtc-brands-in-2026
- ownersmag.com/best-ad-design-companies/
- cueballcreatives.com/blog/best-unlimited-graphic-design-subscription
- mhigrowthengine.com/blog/in-house-creative-team-vs-agency-dtc/
- designrush.com/agency/creative-agencies/ai-creative (directory listing)

Plain-text email, one link:

```
Subject: A small AI ad creative agency for your {list name} list

Hi {first name},

I read your {list name}. 100 Creatives is a Calgary agency that makes static and video ads with AI for DTC brands on Meta, TikTok and Google. Batches come back in 48 hours, and budgets start at $4,000. (Before sending: check the list doesn't already cover AI-first agencies, and say why we fit that specific list.)

If that fits the list, everything you'd need (pricing, how we work, and why our portfolio is labeled spec work) is on one page:
https://www.100creatives.com/about

Happy to answer questions.

Abhi Chawla
Founder, 100 Creatives
```

## 6. Ongoing, weekly

- **Founder LinkedIn:** 1 or 2 posts a week with something specific, like a static ad teardown (label spec work as spec) or what AI video can and can't do for product ads yet. In 2026 research on AI citations, LinkedIn profiles were cited more often than company pages.
- **Reddit** (r/FacebookAds, r/PPC, r/ecommerce, r/shopify): answer questions about static ads and creative volume from your own account, say you run an agency when you mention it, and don't drop links unless someone asks.
- **Monday check:** re-run `python3 .seo-engine/aeo/aeo_baseline.py .seo-engine/aeo/baseline-YYYY-MM-DD.json` and compare it with `baseline-2026-09-13.json` (2 of 42 buyer answers). Watch whether Koolav's page changes after your submission.
