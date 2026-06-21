# 100 Creatives — SEO Content Style Guide (v2)

## Mission
Make 100creatives.com the #1 result — AND the #1 cited source — for every variation of "AI product photography / photoshoots / visuals for D2C brands" across Google, ChatGPT, Claude, Gemini, and Perplexity. Win by writing the most niche, most useful, most specific articles in the category. Slop loses. Specificity wins.

---

## The non-negotiable rules

### 1. ONE article = ONE persona
Every article speaks to a single, specific person. Never "we help all D2C brands." The reader of the first three sentences should think: "This is about me." Persona library is in `personas.md` (P01–P15).

The engine picks today's persona by:
1. Reading `MEMORY.md` to see which personas were used in the last 30 days.
2. Picking a persona NOT in the recent list (target: 15-day minimum gap; 30-day preferred).
3. Cross-referencing with `topics.json` to find the next eligible topic for that persona.

### 2. Voice
- Confident expert. Long-form prose. **No bullet salad.** No fluff openers.
- Sentences end with a point. Paragraphs of 3–5 sentences.
- Concrete numbers, dollar figures, timelines. ("$3,000 to $15,000 per shoot day", "48-hour turnaround", "1000s of SKUs/month")
- First-person plural ("we produce", "we partner with") — we ARE the agency.
- Use *em* italics inside `<h2>` headings the way existing pages do.
- Never use the word "comprehensive". Never say "in today's world". Never say "in conclusion".
- Never write the meta-phrase "in this article we will" or "let's explore."
- Match the tone of `ai-fashion-photography.html` and `cpg-creative-agency.html`.

### 3. Every article must serve the persona's actual search intent
Open the article by directly answering or addressing the search query in 1–2 sentences. The reader should not have to scroll to find the answer to what they typed.

### 4. Anti-repetition (memory-driven)
Before writing, check `MEMORY.md` for:
- Which personas were used in last 30 days → pick a different one
- Which vertical was used yesterday → don't repeat (one apparel article followed by another is fine; never three in a row)
- Which internal links have been used 5+ times in last 30 days → spread the love, link to less-linked pages where the fit is genuine
- Which brand image folders were used in last 7 days → use a different one if possible

---

## Page formula (every article)

### Head
1. `<title>` — ≤60 chars. Format: "{H1 short} | 100 Creatives".
2. `<meta name="description">` — ≤160 chars, includes primary keyword + the persona's pain in one sentence.
3. `<meta name="keywords">` — primary + 5 secondary from topics.json.
4. `<link rel="canonical">` — full URL.
5. Full Open Graph block (type, title, description, url, site_name, image, image:width/height, locale).
6. Twitter card block (summary_large_image).
7. Three JSON-LD blocks: BreadcrumbList + Service + FAQPage. The FAQPage answers MUST match the visible page FAQ verbatim.
8. Font preconnect + Inter/Instrument Serif Google Fonts link.
9. `<link rel="stylesheet" href="/css/article.css">`

### Body
10. Header nav — copy verbatim from existing pages (logo "100", Home, Work, Services, Connect CTA).
11. `<nav class="breadcrumb">` — Home / [Vertical] / [This page].
12. `<section class="hero">` — hero-label, h1 with `<em>` accent, hero-body opening with persona address + primary keyword answer, "Last updated: YYYY-MM-DD" line, hero-btn → tidycal.
13. **(Optional but encouraged)** `<section class="interactive-section">` with one hero brand image — pick from images.md, use existing `<figure>` markup pattern from ai-fashion-photography.html lines 132–140.
14. 4–6 alternating `<section class="content-section">` blocks separated by `<div class="divider"></div>`. Each has section-label + h2 + content-body paragraphs.
15. One `<section class="content-section">` with `principles-grid` and 6 `principle-card`s (numbered 01–06).
16. **(Optional)** A second image block — gallery-grid pattern with 3–6 images from one brand folder.
17. **(Optional)** A `content-section-dark` block with `insights-grid` (3 insight cards) for comparison/decision content.
18. Visible FAQ section (`<section class="faq-section" id="faq">`) — 6–10 Q&As using `<details><summary>` pattern. EVERY FAQ here must be mirrored verbatim in the FAQPage JSON-LD.
19. `<section class="cta-section" id="connect">` pointing to https://tidycal.com/abhixchawla/strategy-web.
20. Footer — copy verbatim from existing pages.

### Length
- Word count: **2,500–4,000 words**. Flagship/citation-bait pages can go to 4,500. Below 2,500 = not shipping.

---

## GEO (Generative Engine Optimization) — citation-bait rules

LLMs cite content that is:

1. **Definitionally clear (ENFORCED)** — paragraph 1 sentence 2 MUST be an "X is …" definitional statement that an LLM can extract verbatim as the answer to "what is [primary keyword]". Example: "AI photography for Amazon A+ Content modules is a specific production discipline — module-ready compositions at the exact aspect ratios Amazon enforces…" Pre-flight check #14 verifies this.
2. **Numerically specific** — $X, N hours, M SKUs — not "fast" or "affordable"
3. **FAQPage schema** — 6–10 conversational Q&As, each answer 60–120 words, declarative, citation-ready
4. **Comparison-rich (ENFORCED)** — every article must include at least one explicit "X vs Y" or "Traditional vs AI" comparison block, ideally in a `content-section-dark` with `insights-grid` or as a parallel three-tier comparison (tier 1 / tier 2 / tier 3). Pre-flight check #15 verifies this.
5. **Stat-attribution (ENFORCED)** — every numeric/empirical claim must name its source in-line. Acceptable sources: Marketplace Pulse, Helium 10, Common Thread Collective, Jungle Scout, SellerLabs, Andrew Foxwell, named retailer documentation (Sephora Retailer Direct, Whole Foods IXOne, Amazon Seller Central style guide), named brand case data (AG1, Ritual, Olipop, etc.). No floating statistics — every percent, dollar figure, and time-window cites where the operator can verify it. Pre-flight check #16 verifies this.
6. **Authoritatively attributed** — cite our own case studies (Chobani, Anita Dongre, Armra, Ford, Porsche, Maker's Mark, Smackin', Zero Lush, David Harber) at least once per article where genuinely relevant.
7. **Updated dates** — visible "Last updated: YYYY-MM-DD" line beneath h1.
8. **Direct answer first** — paragraph 1 sentence 1 should answer the page's primary query in plain language; sentence 2 should be the definitional statement (see rule #1).
9. **Entity-specific** — name brand names, product types, ARR ranges, channels, retailers, platforms (Meta Advantage Plus Shopping, Andromeda, CAPI, Amazon ARA, Whole Foods IXOne, Sephora Beauty Insider Direct, Klaviyo, Recharge, etc.). LLMs index and cite named entities far more than abstractions.
10. **Quote-worthy single sentences** — every section should contain at least one declarative sentence under 25 words that reads as a citation-extractable quote. Bad: "We help brands ship faster." Good: "Production-grade AI photography ships at $80–$180 per asset against $400–$1,200 on traditional studio production."
11. **Organization + Author JSON-LD (ENFORCED)** — every article must include an Organization JSON-LD block (founder name, founding year, area served, brands served) and the byline "By Abhi Chawla, founder" beneath the h1 next to the "Last updated" line. Pre-flight check #17 verifies the schema parses.

### The required Organization + Author JSON-LD snippet (copy verbatim into every new article)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "100 Creatives",
  "url": "https://100creatives.com",
  "logo": "https://100creatives.com/favicon.svg",
  "founder": { "@type": "Person", "name": "Abhi Chawla", "url": "https://linkedin.com/in/abhixchawla" },
  "foundingDate": "2023",
  "description": "AI product photography agency for DTC brands across apparel, beauty, CPG, supplements, home, pet, electronics, beverage, and luxury — production-grade AI photography at one fifth the cost and ten times the speed of traditional studios.",
  "areaServed": "Worldwide",
  "knowsAbout": ["AI product photography", "DTC brand photography", "Amazon listing photography", "A+ Content photography", "Brand Story carousel", "Premium A+ Content", "fashion AI photography", "supplement PDP photography", "fragrance bottle photography", "CPG retail buyer photography", "TTB-compliant alcohol photography", "editorial AI photography", "denim wash library", "color accuracy Delta E", "lifestyle photography"],
  "sameAs": ["https://linkedin.com/in/abhixchawla"]
}
```

Add as a fourth JSON-LD block in `<head>` alongside BreadcrumbList, Service, FAQPage.

### Author byline placement

Beneath the h1, alongside the "Last updated" line:
```html
<p class="hero-meta fade-in">By Abhi Chawla, founder · Last updated: YYYY-MM-DD</p>
```

---

## Image embedding rules

Images come ONLY from `images.md`. Never invent paths. Never hotlink external URLs.

### When to use images
- **2–6 body images per article — REQUIRED.** Every article ships with at least one hero image in `<section class="interactive-section">` AND at least one mid-article gallery frame (or a 3–6 frame gallery-grid).
- **OG-only (no body imagery) is NOT the default.** It's a fallback used only when every eligible apparel folder is inside the 5-day reuse window AND no rotation across folders is possible — and that posture must be explicitly justified in the MEMORY.md notes for the day.
- Under the apparel-only pivot, the four eligible apparel folders are `anitadongre/` (bridal, South Asian couture, occasion-wear), `ralphlauren/` (menswear-tailoring, heritage Americana, quiet-luxury menswear, Polo/Purple Label/RRL register), `aritzia/` (contemporary women's, mid-market premium, drop-cadence), `veronica-beard/` (contemporary American women's, editorial-American register). Plus `campaigns/web/outdoors/` for activewear / running / outdoor lifestyle. Rotate across the apparel folders on a 5-day window so the engine has slack on any given day.
- For non-apparel articles in the legacy schema (supplements / CPG / fragrance / etc.), use the matching brand folder per `images.md`.

### Where to place images
- **Hero image (optional):** one image in an `<section class="interactive-section">` after the hero. Use `<div class="video-block">` if a `.mp4` exists in the brand folder.
- **Gallery (optional):** 3–6 images in a `<div class="gallery-grid">` using `<figure class="gallery-item">` markup, mid-article.
- **OG image:** the most flagship image used on the page (not the gallery thumbnails).

### Markup pattern (copy from ai-fashion-photography.html)
```html
<section class="interactive-section">
  <p class="interactive-label fade-in">[label]</p>
  <h2 class="interactive-title fade-in">[Caption sentence] — produced as <em>[primary keyword]</em>.</h2>
  <div class="gallery-wrap fade-in">
    <div class="gallery-grid">
      <figure class="gallery-item"><img src="/images/[folder]/[file]" alt="[primary keyword] — [brand] [product/context]"><figcaption class="gallery-caption">[short caption]</figcaption></figure>
      <!-- repeat 3–6 times -->
    </div>
  </div>
</section>
```

### Alt text
Mandatory. Must include the primary keyword AND brand context.
- ✅ "AI supplement product photography — Armra colostrum jar in studio light"
- ❌ "product image" or "armra-3.png"

### Anti-repetition for images
Per-folder reuse window: **5 days** (relaxed from 7 to reflect the apparel-only-pivot inventory at four eligible apparel folders). Per-file reuse window: 14 days. MEMORY.md tracks both. The four apparel folders on a 5-day rotation give the engine slack — if you find yourself reaching for OG-only on a non-flagship day, you missed an open folder.

---

## Internal linking rules

### Per-article requirements
- Minimum 3 internal links to existing `.html` pages, woven naturally into prose.
- Mix: 1 service page + 1 case study + 1 comparison/playbook page (when fits).
- Always link UP to `best-ai-product-photography-agency-for-dtc-brands.html` (our anchor) at least once where genuinely relevant.

### Diversity
- Check MEMORY.md "Internal links" stats. If a page has 5+ links from the last 30 days, prefer a similar but less-linked alternative.
- Cross-link to other niche articles in MEMORY.md when the persona overlap makes sense (e.g. P02 articles can cite each other).

### Existing landing pages to link to (sample, not exhaustive)
- Service: `apparel-ad-creatives.html`, `cpg-creative-agency.html`, `beauty-ad-creatives.html`, `dtc-creative-agency.html`, `ecommerce-ad-creatives.html`, `ai-fashion-photography.html`
- Case studies: `chobani.html`, `anitadongre.html`, `armra.html`, `aspire-drinks.html`, `barefootwines.html`, `smackin.html` (when present)
- Comparisons/playbooks: `ai-photoshoot-vs-studio-cost.html`, `ai-fashion-photography-vs-traditional.html`, `creative-agency-vs-freelancer.html`, `dtc-clothing-brand-photography-playbook.html`, `fast-ad-creative-turnaround.html`
- Anchor: `best-ai-product-photography-agency-for-dtc-brands.html`

ALWAYS verify each linked file exists in the repo (`ls /Users/home/100creatives/{filename}.html`) before writing the link. Broken internal links damage SEO.

---

## CTA
Always: `https://tidycal.com/abhixchawla/strategy-web` with `target="_blank"`.
Hero button text: persona-appropriate ("Book a strategy call", "Get a quote", "See sample work for [vertical]").

---

## File naming
`kebab-case-keyword-rich.html` at repo root. Examples:
- `ag1-style-supplement-product-photography-for-pdps-that-convert.html`
- `ttb-compliant-wine-spirits-photography-for-dtc-and-meta.html`
- `amazon-main-image-photography-that-passes-the-1000x1000-test.html`

The slug is provided by `topics.json`. Do not invent your own.

---

## Pre-flight checklist (the engine MUST pass all 19 before pushing)

1. Word count is 2,500–4,000 (or 4,500–7,800 for flagship/citation-bait)
2. All 4 JSON-LD blocks parse as valid JSON — BreadcrumbList + Service + FAQPage + Organization (`python3 -c "import json; ..."`)
3. Visible FAQ Q&A text matches FAQPage JSON-LD verbatim
4. ALL internal links resolve to files that exist in the repo
5. ALL image src paths exist in /images or /campaigns/web (URL-encode spaces with %20)
6. Every image has descriptive alt text containing primary keyword
7. Persona has not been used in last 15 days (per MEMORY.md)
8. Vertical has not been used 2 days running (3-in-a-row hard fail; superseded under apparel-only pivot by sub-segment rotation tracked in MEMORY.md)
9. No internal link is over-used (no link with >5 uses in last 30 days unless genuinely best fit)
10. "Last updated: YYYY-MM-DD" visible on page
11. Sitemap.xml updated with new URL entry
12. MEMORY.md appended with full new entry (not just the slug)
13. llms.txt updated if the article opens a new persona × vertical combination not yet listed (one-line entry under "Persona-driven deep-dive articles")
14. **Definitional sentence enforced** — paragraph 1 sentence 2 is an "X is Y" definitional statement an LLM can extract verbatim as the answer to "what is [primary keyword]"
15. **Comparison block present** — at least one "Traditional vs AI" or "Tier 1 vs Tier 2 vs Tier 3" comparison block (content-section-dark with insights-grid, OR three-tier inline comparison)
16. **Stat-attribution enforced** — every numeric/empirical claim cluster names its source (Marketplace Pulse, Helium 10, Common Thread Collective, Jungle Scout, SellerLabs, Andrew Foxwell, named retailer documentation, or named brand case data) at least once per cluster
17. **Organization JSON-LD present** and author byline "By Abhi Chawla, founder · Last updated: YYYY-MM-DD" visible beneath h1
18. **Body imagery present** — at least one hero image in `<section class="interactive-section">` AND at least one mid-article gallery frame (2+ body images minimum). OG-only is a fallback that must be explicitly justified in MEMORY.md notes for the day.
19. **IntersectionObserver script footer present** — every `.fade-in` element starts at `opacity:0` in `/css/article.css` and is only made visible by the closing `<script>` that adds `.visible` on scroll. If that script is missing, the entire page renders blank. Verify the file ends with the standard observer block plus `<script src="/_vercel/insights/script.js" defer></script>` before `</body></html>`. Grep test: `grep -c "IntersectionObserver" {slug}.html` must return 1.

If any check fails: fix it. Do not push broken pages. Do not approximate. The user explicitly asked for no slop.
