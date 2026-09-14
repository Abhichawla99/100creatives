# Daily SEO + AEO run: procedure v3 (2026-09-14)

**This file replaces RUN v2 and overrides the scheduled task prompt wherever the two disagree.** The persona rotation, the apparel sub-niche queue, "one article a day", 5,000-8,000-word citation-bait articles, personas.md and "cite our own case studies" are retired. Abhi repositioned 100 Creatives on 2026-09-14 after Search Console showed 87% of impressions came from static-ad and ad-creative pages, while ~100 apparel articles had earned about 20 impressions in three months.

## What 100 Creatives is

100 Creatives is an AI-powered creative agency in Calgary, Canada, that makes static and video ads, and the product imagery behind them, for DTC and consumer brands advertising on Meta, TikTok and Google.

`.seo-engine/FACTS.md` is the source of truth for every claim, price and name. When a page and FACTS.md disagree, the page is wrong.

## Goal

Rank in Google and get cited, then recommended, by ChatGPT, Perplexity, Gemini, Copilot and Google AI Overviews for the questions ad-creative buyers ask: what static ads are, what ad creative agencies cost, unlimited ad creative subscriptions, agency vs freelancer, AI video ads, UGC-style ads, and ad creative for specific categories.

Fewer, better pages. Google's 2026 spam policies target mass-produced AI content and self-serving "best of" lists. Assistants lift checkable facts from vendor pages, but they recommend brands that other sites vouch for. So the daily run improves pages that already earn impressions, adds a new page only when real search evidence supports it, and never invents proof.

---

## Step 0: sync

```bash
cd /Users/home/100creatives && git pull --rebase origin main
```

If it fails on a stuck `.git/index.lock`: run `pgrep -fl "git "`. If no git process is running, `rm -f .git/index.lock` and retry once. If `rm` isn't permitted in this sandbox, continue anyway. `publish.sh`'s fallback pushes only the files you name, so a stale checkout can't overwrite newer work.

## Step 1: read, in this order

1. `.seo-engine/FACTS.md`, all of it
2. `.seo-engine/STYLE.md`, all of it
3. `.seo-engine/LEDGER.md`, all of it (short: v3 runs only)
4. `.seo-engine/topics.json` and `.seo-engine/state.json`

Do **not** read `.seo-engine/MEMORY.md` end to end. It's the 740KB v2 archive (through 2026-09-14). Grep it only when you need a specific past fact.

## Step 2: gather signal (about 15 minutes)

Use Claude in Chrome, where the user is logged in. Read only; never change settings.

1. **Search Console Performance**, property `sc-domain:100creatives.com`, last 28 days: `https://search.google.com/search-console/performance/search-analytics?resource_id=sc-domain%3A100creatives.com&num_of_days=28&breakdown=query`. Record the top 30 queries by impressions, then open the Pages breakdown (`&breakdown=page`) and record pages at average position 8 to 40 with 30+ impressions.
2. **Indexing counts**: `https://search.google.com/search-console/index?resource_id=sc-domain%3A100creatives.com`. Record indexed and not indexed, and the "Crawled, currently not indexed" count.
3. **Mondays only:**
   - Search Console, Performance, Generative AI report: impressions by page.
   - Bing Webmaster Tools, AI Performance, site 100creatives.com: citations, grounding queries, citation share.
   - The AI answer baseline, if `/Users/home/dialsheet/.env.local` is readable: `python3 .seo-engine/aeo/aeo_baseline.py .seo-engine/aeo/baseline-$(date +%F).json`. Never print the API key. If the file isn't reachable from this sandbox, skip it and log "baseline skipped: no key access".

Write a short "Signal" block for today in LEDGER.md (numbers only, no prose).

## Step 3: pick exactly one job

Work down this list and take the first job that applies.

1. **Fix.** Any live page that contradicts FACTS.md, found in Step 2 or on a page you opened: a named client, a banned claim, a price that doesn't match, a missing spec label. Fix up to five pages in one run.
2. **Strengthen.** A `strengthen` topic in topics.json, or any ad-creative page from Step 2 at position 8 to 40, that hasn't been strengthened in the last 14 days (check LEDGER.md). Take the one with the most impressions and bring it up to the page spec in STYLE.md. Keep its URL.
3. **New page.** The next `new` topic with `"status": "queued"`, but only if its evidence still holds: the quoted query appears in Search Console, or the quoted prompt is in the baseline. Never start more than one new page per run. Skip this option entirely if indexed pages dropped since the last run.
4. **Nothing qualifies.** Ship no new page. Run the fact patrol (open 3 live pages, compare them with FACTS.md, fix drift) and log it. That counts as a successful run.

Every third run (`state.json` `run_count % 3 == 2`) is strengthen or fix only.

Write the chosen job and its evidence into LEDGER.md **before** writing any copy. Evidence means the exact query or prompt string, where it came from, the impression count and the date. Never build on a phrase you invented.

## Step 4: write to the page spec

Follow STYLE.md exactly. The short version:

- Answer the query in the first two sentences.
- Commercial pages get a TL;DR under the hero that names who should pick 100 Creatives, with 3 to 5 concrete reasons, plus "Pick something else if" naming who should buy a rival and which one.
- Every fact about 100 Creatives comes from FACTS.md. Every external fact carries its source link and the month you checked it.
- Spec work is always labeled. Never name a client.
- Six FAQs, identical in the HTML and the FAQPage JSON-LD.
- Byline "By Abhi Chawla, founder" and a visible "Last updated" date (change the date only when the content changed).

## Step 5: links in and out

- **New page:** add a sentence-level link to it from 2 or 3 existing ad-creative pages that already earn impressions (from Step 2). A page linked only from the sitemap tends to sit at "Discovered, currently not indexed".
- **Every page you touch:** link out to 3 to 5 related pages with descriptive anchor text.
- Record every link you add in LEDGER.md as `from -> to`.

## Step 6: validate (everything must pass)

Run from the repo root, passing every HTML file you touched:

```bash
python3 .seo-engine/validate.py about.html static-ads.html   # replace with the files you touched
```

`validate.py` checks: JSON-LD parses; the FAQ matches its JSON-LD word for word; every internal link resolves; the canonical is `https://www.100creatives.com/{slug}`; no banned claims (named clients, "leading", "five years", "one fifth the cost", "zero missed deadlines", AggregateRating); the page isn't noindex unless intended. It also counts em dashes in the body. Then run the no-ai-slop eval (`~/.claude/skills/no-ai-slop/eval.md`) on the new copy yourself and fix any failure.

## Step 7: sitemap and llms.txt

- New page: add a `<url>` block to `sitemap.xml` with today's `<lastmod>`.
- Strengthened or fixed page: update that page's `<lastmod>` to today.
- New commercial or reference page: add one line to `llms.txt` under the right heading. Keep llms.txt consistent with FACTS.md.

## Step 8: publish

```bash
bash /Users/home/100creatives/.seo-engine/publish.sh "{slug}" "{short description of the change}" [other files you edited...]
```

Pass every other file you edited (pages you added links to, llms.txt) as extra arguments. The fallback path pushes only the named files plus the sitemap entry and engine state.

## Step 9: verify live and request indexing

1. Wait about 60 seconds, then curl the page: HTTP 200, the `<h1>` is present, and the canonical is correct.
2. publish.sh pings IndexNow. Confirm HTTP 200 or 202 in its output.
3. In Search Console, use URL Inspection → Request indexing for the new or strengthened URL. The quota is about 3 a day, so spend it on today's URL first, then the "Indexing debt" list in LEDGER.md. When you see "Quota exceeded", stop and add the rest to the debt list.

## Step 10: log and close

Append today's entry to LEDGER.md:

```
## YYYY-MM-DD, run {n}: {fix | strengthen | new | patrol}
- URL:
- Evidence: "{exact query or prompt}", {source}, {impressions}, {date}
- Signal: indexed {n} / not indexed {n}; top ad-lane page positions
- Changed: (3-6 short bullets)
- Links added: from -> to
- Validation: pass/fail details
- IndexNow: {status}; GSC: {verdict}
- Next run should start with:
```

Update `state.json`: increment `run_count`, and set `last_run`, `last_job` and the `strengthened` map (slug → date). Mark a new topic's status as `"published"`. Close any Chrome tabs you opened.

---

## Never

- Name a brand as a client, or describe spec work as a real shoot or campaign.
- Invent statistics, prices, reviews, ratings, testimonials or quotes.
- Publish self-ranking "best agencies" lists that put 100 Creatives first.
- Add city or country landing pages for places where 100 Creatives has no presence.
- Change FACTS.md. Only Abhi changes positioning, prices or client facts. If you think something in it is wrong, say so in LEDGER.md.
- Enter credentials, post anywhere, email anyone, or change Search Console or Bing settings.
