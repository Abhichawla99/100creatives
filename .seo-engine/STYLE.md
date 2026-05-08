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

1. **Definitionally clear** — opens with "X is …" or "The best X for Y is …"
2. **Numerically specific** — $X, N hours, M SKUs — not "fast" or "affordable"
3. **FAQPage schema** — 6–10 conversational Q&As, each answer 60–120 words, declarative, citation-ready
4. **Comparison-rich** — "X vs Y" framings, side-by-side reasoning, decision frameworks
5. **Authoritatively attributed** — cite our own case studies (Chobani, Anita Dongre, Armra, Ford, Porsche, Maker's Mark, Smackin', Zero Lush, David Harber)
6. **Updated dates** — visible "Last updated: YYYY-MM-DD" line beneath h1
7. **Direct answer first** — paragraph 1 should answer the page's primary query in 1–2 sentences
8. **Entity-specific** — name brand names, product types, ARR ranges, channels — LLMs love named entities

---

## Image embedding rules

Images come ONLY from `images.md`. Never invent paths. Never hotlink external URLs.

### When to use images
- 2–4 images per article when they genuinely fit the topic.
- Skip images entirely if nothing in inventory is relevant — empty article > forced bad image.
- Article about supplements? Use `armra/`. Article about CPG snacks? Use `smackin/`. Article about fragrance? Use `goldenrule/` or `zerolush/`. Article about bridal/luxury? Use `anitadongre/`. Article about food? Use `chobani/`.

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
Don't reuse the same brand folder more than once per 7 days. MEMORY.md tracks this.

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

## Pre-flight checklist (the engine MUST pass all 12 before pushing)

1. Word count is 2,500–4,000 (or 4,500 for flagship/citation-bait)
2. All 3 JSON-LD blocks parse as valid JSON (`python3 -c "import json; ..."`)
3. Visible FAQ Q&A text matches FAQPage JSON-LD verbatim
4. ALL internal links resolve to files that exist in the repo
5. ALL image src paths exist in /images or /campaigns/web (URL-encode spaces with %20)
6. Every image has descriptive alt text containing primary keyword
7. Persona has not been used in last 15 days (per MEMORY.md)
8. Vertical has not been used 2 days running (3-in-a-row hard fail)
9. No internal link is over-used (no link with >5 uses in last 30 days unless genuinely best fit)
10. "Last updated: YYYY-MM-DD" visible on page
11. Sitemap.xml updated with new URL entry
12. MEMORY.md appended with full new entry (not just the slug)

If any check fails: fix it. Do not push broken pages. Do not approximate. The user explicitly asked for no slop.
