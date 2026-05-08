# Daily SEO Run — Procedure (v2)

This is the canonical procedure the scheduled task fires every morning at 6 AM PT. Follow it exactly. Do not skip steps. Do not cut corners. The user explicitly asked for niche, persona-driven articles — not slop.

---

## STEP 1 — Load context (read everything below before writing anything)

Read these files end to end, in order:

1. `/Users/home/100creatives/.seo-engine/MEMORY.md` — what's been published, which personas are recently used, which links/images are saturated. **This is the most important file.**
2. `/Users/home/100creatives/.seo-engine/personas.md` — the 15 personas you can target.
3. `/Users/home/100creatives/.seo-engine/STYLE.md` — voice, formula, GEO rules, image rules, link rules, pre-flight checklist.
4. `/Users/home/100creatives/.seo-engine/images.md` — image inventory by vertical/brand.
5. `/Users/home/100creatives/.seo-engine/topics.json` — the queue.
6. `/Users/home/100creatives/.seo-engine/state.json` — `next_index` pointer.

---

## STEP 2 — Pick today's topic + persona

1. Read `state.json.next_index`. Tentatively pick `topics[next_index]`.
2. Cross-check the topic's `persona` against MEMORY.md "Personas used" stats.
   - If that persona was used within the **last 15 days**, ADVANCE: try `topics[next_index + 1]`, then `+2`, etc., until you find one whose persona has the longest gap (or has never been used).
   - Update `next_index` to whichever index you actually picked (skipped indexes are fine — go back to them later).
3. Cross-check the topic's `vertical` against MEMORY.md "Verticals used (last 7 days)".
   - If the same vertical was used **yesterday AND the day before** (3-in-a-row), advance further to a different vertical.
4. Verify the chosen topic's slug doesn't already exist as `/Users/home/100creatives/{slug}.html`. If it does, advance by 1 and re-verify.

---

## STEP 3 — Inspect site to mirror voice and structure

1. Read `/Users/home/100creatives/index.html` lines 1–100 (head + nav).
2. Read ONE existing page in the same vertical:
   - apparel → `ai-fashion-photography.html`
   - beauty → `beauty-ad-creatives.html`
   - food-bev or supplements → `cpg-creative-agency.html`
   - geo/comparison → `best-ai-product-photography-agency-for-dtc-brands.html`
3. Note the section structure and copy verbatim where instructed (header nav, footer, scripts).

---

## STEP 4 — Pick internal links (3+ minimum)

1. From the topic's `suggested_internal_links`, **verify each file exists** in the repo:
   ```bash
   ls /Users/home/100creatives/{filename}.html
   ```
2. From MEMORY.md "Internal links — link counts", check each candidate's recent count.
   - If a candidate has 5+ links in last 30 days, find a similar-but-less-linked alternative.
3. ALWAYS include a link UP to `best-ai-product-photography-agency-for-dtc-brands.html` (the anchor) where genuinely relevant.
4. Final list: 3–6 links woven into the prose (not a footer dump).

---

## STEP 5 — Pick images (0–4)

1. From the topic's `image_hints`, identify the relevant brand folder(s) per `images.md`.
2. Check MEMORY.md "Brand images used (last 7 days)" — avoid same folder twice in 7 days unless no alternative fits.
3. Select 2–4 specific files. **Verify each exists**:
   ```bash
   ls "/Users/home/100creatives/images/{folder}/{filename}"
   ```
4. URL-encode any spaces in filenames as `%20` when writing the `src` attribute.
5. If no inventory image fits the topic, ship without images. Empty > forced.

---

## STEP 6 — Write the article

Create `/Users/home/100creatives/{slug}.html` following the page formula in STYLE.md exactly. Hard requirements (also in the pre-flight checklist):

- **2,500–4,000 words** of long-form prose (4,500 OK for flagship/citation-bait).
- **Persona-first opening**: paragraph 1 addresses the persona's pain in their language and answers the primary keyword query directly.
- **`<head>` block**: title ≤60 chars, meta description ≤160 chars, keywords, canonical, OG, Twitter, BreadcrumbList JSON-LD, Service JSON-LD, FAQPage JSON-LD.
- **Hero**: `<section class="hero">` with hero-label, h1 with `<em>`, hero-body, "Last updated: YYYY-MM-DD" line, hero-btn → tidycal.
- **(Optional) Image hero**: one image in `<section class="interactive-section">` after hero.
- **4–6 content-sections** with section-label + h2 + 3-5 paragraph content-body, separated by `<div class="divider"></div>`.
- **One principles-grid** with 6 numbered cards (01–06).
- **(Optional) Image gallery** mid-article: 3–6 images in gallery-grid pattern.
- **(Optional) content-section-dark** with insights-grid for comparison/decision content.
- **FAQ section**: 6–10 `<details><summary>` Q&As. EACH answer must match the FAQPage JSON-LD answer verbatim, 60–120 words each, declarative.
- **CTA section** → tidycal.
- **Footer** copied verbatim.
- **3+ internal links** to existing pages, woven into prose.
- **2–4 images** if relevant, with descriptive alt text containing primary keyword.

---

## STEP 7 — Pre-flight validation

Run all 12 checks from STYLE.md "Pre-flight checklist". Programmatic where possible:

```bash
cd /Users/home/100creatives

# 1. Word count
wc -w {slug}.html

# 2. JSON-LD validity
python3 -c "
import re, json, sys
html = open('{slug}.html').read()
blocks = re.findall(r'<script type=\"application/ld\+json\">(.*?)</script>', html, re.DOTALL)
print(f'{len(blocks)} JSON-LD blocks')
for i, b in enumerate(blocks):
    json.loads(b)
print('All valid')
"

# 4. Internal links exist
grep -oE 'href=\"[a-z0-9-]+\.html\"' {slug}.html | sed 's/href=\"//;s/\"//' | sort -u | while read f; do
  [ -f \"$f\" ] && echo \"✓ $f\" || echo \"✗ MISSING: $f\"
done

# 5. Image src files exist
grep -oE 'src=\"/images/[^\"]+\"|src=\"/campaigns/[^\"]+\"' {slug}.html | sed 's/src=\"//;s/\"//' | while read p; do
  decoded=$(printf '%b' \"${p//%/\\x}\")
  [ -f \".$decoded\" ] && echo \"✓ $p\" || echo \"✗ MISSING: $p\"
done
```

If ANY check fails, fix the article. Do not push broken pages.

---

## STEP 8 — Update sitemap.xml

Edit `/Users/home/100creatives/sitemap.xml`. Insert this block immediately before `</urlset>`:
```xml
  <url>
    <loc>https://100creatives.com/{slug}.html</loc>
    <lastmod>{TODAY YYYY-MM-DD}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
```

---

## STEP 9 — Update state.json

```json
{
  "next_index": [the index AFTER the one you used + 1],
  "last_published_slug": "{slug}",
  "last_published_date": "{TODAY YYYY-MM-DD}",
  "history": [...existing, {"date": "...", "slug": "...", "h1": "..."}]
}
```

If you skipped indexes in STEP 2, those topics are still in queue — they'll come up later when the engine cycles back. Don't try to be clever.

---

## STEP 10 — Append to MEMORY.md

Add a new dated section at the bottom of MEMORY.md (above the "Rolling stats" section). Use exactly this format:

```markdown
## YYYY-MM-DD
- **slug:** {slug}
- **h1:** {full h1}
- **persona:** {Pxx} ({short label})
- **vertical:** {vertical}
- **angle:** {one-sentence angle}
- **intent:** {intent}
- **primary_keyword:** {exact phrase}
- **internal_links_used:** {comma-separated .html files}
- **images_used:** {comma-separated paths or "none"}
- **word_count:** {n}
- **notes:** {1-2 sentences on what makes this article niche/specific}
```

THEN update the "Rolling stats" section:
- "Personas used" — set this persona's last-use date to today
- "Verticals used (last 7 days)" — append today's entry; trim entries older than 7 days
- "Internal links — link counts" — increment count for each link used; add new entries if the page wasn't tracked yet
- "Brand images used (last 7 days)" — append today's entry; trim entries older than 7 days

---

## STEP 11 — Commit + push (+ IndexNow ping)

```bash
bash /Users/home/100creatives/.seo-engine/publish.sh "{slug}" "{full h1}"
```

The script auto-stages: `{slug}.html`, `sitemap.xml`, the entire `.seo-engine/` directory (including state.json, MEMORY.md, topics.json updates), and `.gitignore`. It commits with a descriptive message and pushes to `main`. Vercel auto-deploys in 30–60 seconds.

**Then it auto-pings IndexNow** (Bing, Yandex, Seznam, Naver) with the new URL + sitemap. The script waits 45s for Vercel to deploy first, then POSTs to `api.indexnow.org/IndexNow` with our key (`e6baf767262d12f58083a712d380812b`, hosted at `https://100creatives.com/e6baf767262d12f58083a712d380812b.txt`). HTTP 200 or 202 = accepted. Non-200 is logged but non-fatal — IndexNow rate-limits and re-tries are not necessary for daily cadence.

**Google note.** Google doesn't participate in IndexNow and has no public per-URL submission API for general pages (the Indexing API is restricted to JobPosting and BroadcastEvent). For Google we use **STEP 11b** below — Chrome MCP automates the same "Request Indexing" button a human would click in GSC.

---

## STEP 11b — Request indexing in Google Search Console (via Chrome MCP)

Google's only fast path to indexing for general pages is the "Request Indexing" button inside GSC's URL Inspection tool. There's no API, but the user is already logged into Google Search Console in their default Chrome profile, so we drive the UI via the Chrome MCP. Run this **after** the publish.sh push succeeds and after waiting ~60s for Vercel to deploy.

```python
# Pseudocode for the engine — actual calls use mcp__Claude_in_Chrome__* tools
1. tabs_context_mcp(createIfEmpty=true) → get a tabId
2. navigate(tabId, "https://search.google.com/search-console")
   wait 4s, screenshot
   - If GSC overview shows "100creatives.com" in the property switcher (top-left), proceed.
   - If a Google account picker / login screen appears, STOP. Report to user:
     "GSC needs you to log in. After login, re-run this skill."
3. For each URL to submit (today's new article + sitemap.xml):
   left_click(tabId, [600, 25])     # the top inspect-URL search bar
   type(tabId, full_url)            # e.g. https://www.100creatives.com/{slug}.html
   key(tabId, "Return")
   wait 8s
   screenshot                        # confirm "URL Inspection" page rendered
   left_click(tabId, [1226, 295])    # "REQUEST INDEXING" button
   wait 60s                          # Google runs a live crawlability test
   screenshot                        # confirm "Indexing requested" green banner
   left_click(tabId, [960, 442])     # Dismiss
4. Report each URL submitted in STEP 12.
```

**What to submit.** Just the new article. Don't re-submit old URLs — Google's quota is "a few dozen URLs per day per property" and burning it on yesterday's articles wastes the limit. The sitemap is auto-fetched by Google on its own cadence, so no need to inspect it through the URL tool.

**Quota gotchas.**
- Google rate-limits to roughly 10–20 Request Indexing clicks per property per day. We only submit 1 URL/day so we're nowhere near the limit, but if the engine ever back-fills missed days it should cap at 5/day.
- "URL is not on Google" → expected for fresh URLs; click Request Indexing.
- "URL is on Google" → already indexed, no need to request.
- "URL is on Google, but has issues" → log to MEMORY.md notes, don't auto-fix; surface to user.

**Login failure.** If GSC redirects to accounts.google.com instead of showing the dashboard, the user's Google session has expired in this Chrome profile. STOP the engine and report. Never attempt to log in on the user's behalf — credentials must be entered by the user.

**Coordinate drift.** GSC layout occasionally moves. If `screenshot` after the click doesn't show "Testing if live URL can be indexed" or "Indexing requested", fall back to `find(tabId, "Request Indexing button")` to get the live element ref, then click via `ref`.

---

## STEP 12 — Report (one line)

```
✓ Published "{h1}" → https://100creatives.com/{slug} (persona {Pxx}, {vertical}, {word_count} words). Vercel deploying. IndexNow pinged. GSC Request Indexing submitted.
```

---

## Edge cases

### Queue exhaustion
If `next_index >= topics.length` (or all remaining topics have personas used too recently):
1. Read MEMORY.md to identify uncovered persona × intent × vertical combinations.
2. Extend `topics.json` with 20–40 new briefs filling those gaps. Each new topic gets the same schema as existing topics (persona, vertical, angle, intent, primary_keyword, secondary_keywords, suggested_internal_links, image_hints).
3. Set `next_index` to the first new topic's index.
4. Then proceed with STEP 6.

### Stuck git locks
If `.git/*.lock` files exist and block commit:
1. Try `rm -f /Users/home/100creatives/.git/index.lock /Users/home/100creatives/.git/HEAD.lock /Users/home/100creatives/.git/refs/remotes/origin/main.lock`.
2. If `rm` fails with "Operation not permitted" (sandbox mount issue): report to user with the exact command — they can run it from Terminal.
3. Never use `sudo`.

### Auth failure on push
Report to user: "GitHub PAT in .git/config may have expired or been rotated. Reset with: `cd /Users/home/100creatives && git remote set-url origin "https://Abhichawla99:NEW_TOKEN@github.com/Abhichawla99/100creatives.git"`". **NEVER echo or log the existing token.**

### Sitemap parse failure
Validate sitemap.xml after edit. If parse fails, revert the change and stop. Do not push partial state.

### Slug collision
If `{slug}.html` already exists in the repo (e.g. you generated it before but state wasn't updated): advance `next_index` and pick the next eligible topic.

---

## What "no slop" looks like (read this last, before writing)

The user explicitly asked for niche, persona-driven articles — not "we help every D2C brand under the sun" generic content. Before writing each section, ask yourself:

- Would the persona recognize their own situation in this paragraph?
- Is there a specific number, name, or detail that proves we know the niche?
- Could a competitor write this exact paragraph? If yes, rewrite.
- Does the article help the persona make a decision today, or just describe the category?

If you finish a draft and it could be re-titled for any other persona without much change — STOP, rewrite. The whole point is sharpness.
