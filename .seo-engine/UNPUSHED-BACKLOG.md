# Unpushed backlog — needs a manual `git push` on next opportunity

**Last updated:** 2026-05-26 (auto-written by the daily run on this date)

## What happened

The 2026-05-26 scheduled run wrote today's article, validated it, and updated state.json / MEMORY.md / sitemap.xml correctly — but the **git push step could not complete** because the sandbox shell hit a persistent `no space left on device` error on the host coordination filesystem (`/etc/srt-settings`). The local clone at `/Users/home/100creatives` also has the documented stuck `.git/*.lock` files (sandbox mount permission issue), so the primary push path was unavailable too. The fallback `/tmp clone` path could not run because every shell invocation died on the same RPC error.

Same root cause appears to have hit the 2026-05-24 and 2026-05-25 runs — both wrote articles locally that never reached origin/main.

## What's on local mount but not on origin

Three article HTML files are written, validated, and registered in `sitemap.xml` + `state.json` + `MEMORY.md`, but missing from `origin/main`:

1. `color-accuracy-in-ai-product-photography-pantone-and-pdp-trust.html` — 2026-05-24, P03, beauty/cross-vertical
2. `ai-vs-3d-rendering-for-cpg-and-beverage-brands.html` — 2026-05-25, P04, food-bev
3. `lifestyle-photography-without-the-location-scout.html` — 2026-05-26, P05, geo (today's run)

The `.seo-engine/` files (`state.json`, `MEMORY.md`, `topics.json`) all reflect the post-2026-05-26 state. `sitemap.xml` includes all three new `<url>` entries.

## Recovery procedure

Run this from a working shell (Cowork or local) when the sandbox infrastructure recovers. The local-clone primary path will probably still fail on the `.git/*.lock` issue, so go straight to the `/tmp` fallback clone approach. The repo's GitHub auth token is embedded in `.git/config` — read it from there, never hard-code it:

```bash
REPO=/Users/home/100creatives
TMPDIR=/tmp/100c-publish-recovery
REMOTE_URL=$(cd $REPO && git config --get remote.origin.url)

rm -rf $TMPDIR
git clone "$REMOTE_URL" $TMPDIR
cd $TMPDIR
git config user.name "100Creatives SEO Bot"
git config user.email "abhixchawla@gmail.com"

# Copy the three backlog articles
cp $REPO/color-accuracy-in-ai-product-photography-pantone-and-pdp-trust.html $TMPDIR/
cp $REPO/ai-vs-3d-rendering-for-cpg-and-beverage-brands.html $TMPDIR/
cp $REPO/lifestyle-photography-without-the-location-scout.html $TMPDIR/

# Copy updated sitemap and entire .seo-engine/
cp $REPO/sitemap.xml $TMPDIR/sitemap.xml
mkdir -p $TMPDIR/.seo-engine
cp -r $REPO/.seo-engine/. $TMPDIR/.seo-engine/

# .gitignore if it exists
[ -f $REPO/.gitignore ] && cp $REPO/.gitignore $TMPDIR/.gitignore

git add -A
git commit -m "SEO: catch-up publish — 2026-05-24, 2026-05-25, 2026-05-26 articles

Publishes three articles that were written locally but never reached origin
due to sandbox infrastructure failures:
  - color-accuracy-in-ai-product-photography-pantone-and-pdp-trust (2026-05-24, P03)
  - ai-vs-3d-rendering-for-cpg-and-beverage-brands (2026-05-25, P04)
  - lifestyle-photography-without-the-location-scout (2026-05-26, P05)

Also updates sitemap.xml and the .seo-engine/ state files."

git push origin main

# Then ping IndexNow for the three URLs:
curl -s -X POST "https://api.indexnow.org/IndexNow" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d '{
    "host": "100creatives.com",
    "key": "e6baf767262d12f58083a712d380812b",
    "keyLocation": "https://100creatives.com/e6baf767262d12f58083a712d380812b.txt",
    "urlList": [
      "https://100creatives.com/color-accuracy-in-ai-product-photography-pantone-and-pdp-trust.html",
      "https://100creatives.com/ai-vs-3d-rendering-for-cpg-and-beverage-brands.html",
      "https://100creatives.com/lifestyle-photography-without-the-location-scout.html",
      "https://100creatives.com/sitemap.xml"
    ]
  }'

rm -rf $TMPDIR
```

## Once recovery is done

Delete this file (`/Users/home/100creatives/.seo-engine/UNPUSHED-BACKLOG.md`) and request GSC indexing for the three URLs (only ~10–20 requests/day allowed, so submit all three).

## Pre-flight validation already passed for 2026-05-26 article

- Word count: 3,968 (visible body) — within 2,500–4,000 ✓
- All 3 JSON-LD blocks parse as valid JSON ✓
- 10 FAQ Q&As — visible markup matches FAQPage JSON-LD verbatim ✓
- All 13 internal links resolve to existing `.html` files in the repo ✓
- All 5 image src files exist (`/campaigns/web/ford-bronco/*` and `/campaigns/web/outdoors/*`) ✓
- Every image has descriptive alt text with the primary keyword ✓
- Persona P05 unused for 15 days (last 2026-05-11) — at boundary, eligible ✓
- Vertical `geo` — yesterday was `food-bev`, no 3-in-a-row violation ✓
- "Last updated: 2026-05-26" visible on page ✓
- Sitemap.xml updated with new `<url>` entry ✓
- MEMORY.md appended with full entry + rolling-stat updates ✓

The article is shippable. It's only the network push that didn't run.
