# 100 Creatives — 20-Page Build Spec (single source of truth)

This file is the contract every page-build agent follows. It encodes the EXACT
template, SEO rules, copy register, and conventions extracted from the live site
(`fashion-lifestyle-campaign-imagery.html` + `css/article.css`). Static HTML only —
no framework. `vercel.json` has `cleanUrls:true`, so `slug.html` serves at `/slug`.

## Hard rules
- **Domain:** `https://100creatives.com` (NOT `.co`).
- **Stylesheet:** every page links `/css/article.css` — do NOT add page `<style>` unless a
  module needs it; reuse existing classes only (list below). Never invent unstyled classes.
- **Fonts:** Inter + Instrument Serif via the Google Fonts `<link>` (preconnect first). The
  serif italic `<em>` inside headings is the brand signature — every H1/H2 has one `<em>`.
- **Images:** reference ONLY files that exist in `lib/campaign-assets.json`. Every `<img>` gets
  `width`, `height` (intrinsic px from the manifest), `loading="lazy"` (hero may be eager),
  `decoding="async"`, and descriptive `alt` that contains the page's primary keyword **naturally**
  in the hero/first gallery image (not stuffed). NO invented images. If a needed shot does not
  exist, insert `<!-- NEEDS-ASSET: <description> -->` and log it.
- **CTAs (per brief):** book-a-call → `https://tidycal.com/abhixchawla/strategycall` ;
  email → `abhi@paperkites.co`. (⚠ live site chrome uses `/strategy-web`; brief overrides for
  conversion blocks — flagged in gaps.) Nav "Connect" + footer "Contact" keep the site-standard
  `https://tidycal.com/abhixchawla/strategy-web` so chrome matches the other 49 pages.
- **No filler.** No "in today's fast-paced world," no Lorem. Match the house register: specific,
  named real brands, real production economics, persona-locked cold opens, concrete mechanics.
  Body copy 1,500–2,500 words (well above the 600–900 floor — this site IS the portfolio).
- **Keyword placement:** primary keyword must appear in `<title>` (≤60 chars), meta description
  (≤155 chars), `<h1>`, at least one `<h2>`, the first 100 words of the hero body, the hero image
  alt, and the slug.

## Exact page skeleton (fill the ALLCAPS placeholders)
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TITLE_<=60</title>
  <meta name="description" content="META_<=155">
  <meta name="keywords" content="KW1, KW2, ...">
  <meta name="author" content="100 Creatives">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="canonical" href="https://100creatives.com/SLUG.html">
  <meta property="og:type" content="article">
  <meta property="og:title" content="TITLE">
  <meta property="og:description" content="META">
  <meta property="og:url" content="https://100creatives.com/SLUG.html">
  <meta property="og:site_name" content="100 Creatives">
  <meta property="og:image" content="https://100creatives.com/OG_IMAGE">
  <meta property="og:image:width" content="OG_W">
  <meta property="og:image:height" content="OG_H">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="TITLE">
  <meta name="twitter:description" content="META">
  <meta name="twitter:image" content="https://100creatives.com/OG_IMAGE">

  <!-- JSON-LD: BreadcrumbList ALWAYS. Then per page type:
       guides/educational/comparison -> Article ; services -> Service ;
       Canada/money -> Service + LocalBusiness (Calgary, AB, CA). FAQPage if a visible FAQ exists.
       Organization block ALWAYS (copy verbatim from below). -->
  ...JSON-LD blocks...

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/article.css">
</head>
<body>
<header>
<nav>
  <a href="/" class="logo">100</a>
  <div class="nav-right">
    <a href="index.html">Home</a>
    <a href="/#work">Work</a>
    <a href="index.html#services">Services</a>
    <a href="https://tidycal.com/abhixchawla/strategy-web" target="_blank" class="nav-cta">Connect</a>
  </div>
</nav>
</header>
<main>
<nav class="breadcrumb" aria-label="Breadcrumb">
  <a href="index.html">Home</a><span>/</span><a href="apparel-ad-creatives.html">Apparel</a><span>/</span>PAGE NAME
</nav>
<section class="hero">
  <p class="hero-label fade-in">CATEGORY · SUBHEAD</p>
  <h1 class="fade-in">HEADLINE with one <em>serif italic phrase.</em></h1>
  <p class="hero-body fade-in">≥100-word answer that uses the primary keyword in the first 100 words and fully answers the search intent...</p>
  <p class="hero-meta fade-in">By Abhi Chawla, founder · Last updated: 2026-06-19</p>
  <div class="hero-bottom fade-in">
    <a href="https://tidycal.com/abhixchawla/strategycall" target="_blank" class="hero-btn">CTA LABEL
      <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 8h10M9 4l4 4-4 4"/></svg>
    </a>
  </div>
</section>
<!-- hero gallery (interactive-section + gallery-grid) -->
<!-- 4-7 content-section blocks (content-split: left H2, right content-body <p>s w/ contextual internal links) -->
<!-- ONE differentiating module per page (see module menu) -->
<!-- principles-grid (6 cards) OR insights-grid dark (3 tiers) where it fits -->
<!-- faq-section#faq with <details> mirrored into FAQPage JSON-LD -->
<!-- cta-section#connect -->
</main>
<footer> ...standard footer (copy from reference)... </footer>
<script> IntersectionObserver fade-in + smooth-scroll (copy verbatim) </script>
<script src="/_vercel/insights/script.js" defer></script>
</body>
</html>
```

## Available CSS classes (use ONLY these)
nav, logo, nav-right, nav-cta · breadcrumb · hero, hero-label, hero-body, hero-meta, hero-bottom,
hero-btn · divider · content-section, content-section-dark, section-label, section-label-dark,
content-split, content-body · principles-grid, principle-card, principle-number ·
insights-grid, insight-card, insight-tier · interactive-section, interactive-label,
interactive-title, interactive-sub · gallery-wrap, gallery-grid, gallery-item, gallery-caption ·
video-block, video-frame, video-caption · calc-* (cost calculator) · timeline-* · checklist-* ·
funnel-* · ba-* (before/after slider) · faq-section, faq-list, section-title, details/summary ·
cta-section, cta-label, cta-title, cta-body, cta-btn · footer-grid, footer-brand, footer-brand-sub,
footer-col, footer-bottom, footer-left, footer-right · fade-in (+ .visible toggled by JS).

## Differentiating module menu (pick ONE per page so pages don't feel stamped)
- **Guides (3,13,15,16):** `timeline-*` (5-step process) or `checklist-*` (readiness checklist) — needs inline JS.
- **Money/service (9,10,14,18,19,20):** `calc-*` cost calculator or `funnel-*` asset-funnel — needs inline JS.
- **Comparisons (5,6,11,12):** `ba-*` before/after slider or a 2-column `insights-grid` (dark tiers) — slider needs JS.
- **Authority/educational (1,2,7,8,17):** `principles-grid` (6 cards) or dark `insights-grid`.
JS for each interactive module must be added inline before the closing scripts; keep it minimal and
self-contained. If unsure, fall back to `principles-grid` (no JS) + `gallery-grid`.

## Organization JSON-LD (paste verbatim into every page)
```
{"@context":"https://schema.org","@type":"Organization","name":"100 Creatives","url":"https://100creatives.com","logo":"https://100creatives.com/favicon.svg","founder":{"@type":"Person","name":"Abhi Chawla","url":"https://linkedin.com/in/abhixchawla"},"foundingDate":"2023","description":"A brand-world studio and AI product photography agency for apparel brands — campaigns, lookbooks, editorial and brand identity at one fifth the cost and ten times the speed of traditional studios.","areaServed":"Worldwide","sameAs":["https://linkedin.com/in/abhixchawla"]}
```

## LocalBusiness JSON-LD (Canada/money pages 4,7,9,10,15 — per brief)
```
{"@context":"https://schema.org","@type":"LocalBusiness","name":"100 Creatives","url":"https://100creatives.com","image":"https://100creatives.com/OG_IMAGE","description":"...","address":{"@type":"PostalAddress","addressLocality":"Calgary","addressRegion":"AB","addressCountry":"CA"},"areaServed":["Canada","Worldwide"],"founder":{"@type":"Person","name":"Abhi Chawla"}}
```
(No street/postal/phone — not fabricated. Flagged: add real address for full rich-result eligibility.)

## Footer (paste verbatim)
Standard 4-column footer from the reference page (brand blurb + Apparel / Compare / Company columns +
footer-bottom). Company column "Contact" link uses `/strategy-web` (site chrome standard).

## Closing scripts (paste verbatim)
IntersectionObserver toggling `.visible` on `.fade-in` (threshold 0.15) + smooth-scroll for `a[href^="#"]`,
then `<script src="/_vercel/insights/script.js" defer></script>`.
