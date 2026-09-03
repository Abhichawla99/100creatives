# Unpushed backlog — needs a manual `git push`

**Last updated:** 2026-09-03 (auto-written by the daily run)

## Status: 2 articles written + validated locally, BLOCKED on git auth (day 2)

`origin/main` is still at `c0a00b6`. Neither article below is live. Vercel has not deployed them.

### What's ready but not on origin

1. `eyewear-and-sunglasses-brand-campaign-and-editorial-imagery.html` — 2026-09-02, P25 (DTC Eyewear Founder), apparel/eyewear sub-segment, ~10,470 words.
2. `size-inclusive-apparel-brand-campaign-and-editorial-imagery.html` — 2026-09-03, P26 (Extended-Range / Size-Inclusive Head of Brand), apparel/size-inclusive sub-segment, 5,889 wc -w (~3,800 visible words).
   - Pre-flight: 4/4 JSON-LD blocks valid, title 59 chars, meta description 145 chars, 12/12 internal links resolve, 4/4 image paths resolve, 8/8 FAQ answers match FAQPage JSON-LD verbatim (86–105 words each), IntersectionObserver present, sitemap.xml parses at 169 URLs.

`sitemap.xml`, `.seo-engine/state.json` (next_index 24), `.seo-engine/topics.json` (extended 23 → 28), and `.seo-engine/MEMORY.md` are all updated and consistent with both articles.

### The two blockers (unchanged from 2026-09-02)

1. **No git push credentials.** `remote.origin.url` is the bare
   `https://github.com/Abhichawla99/100creatives.git`. No PAT, no credential helper, no
   `~/.netrc`, no `GITHUB_TOKEN`/`GH_TOKEN`, no `gh` CLI. Clone and fetch work (public repo);
   push fails with `could not read Username for 'https://github.com'`.
2. **Stuck `.git/index.lock`** in the local clone at `/Users/home/100creatives`. `rm` returns
   `Operation not permitted` from the sandbox mount, so even a local commit can't be made there.
   (The `/tmp` clone fallback in `publish.sh` routes around this — it only fails on blocker #1.)

## Recovery — run from Terminal on the Mac

```bash
cd /Users/home/100creatives

# 1. Clear the stuck lock (needs a real shell, not the sandbox)
rm -f .git/index.lock .git/HEAD.lock .git/refs/remotes/origin/main.lock

# 2. Restore push auth with a fresh GitHub PAT (repo scope)
git remote set-url origin "https://Abhichawla99:NEW_TOKEN@github.com/Abhichawla99/100creatives.git"

# 3. Commit + push both articles
git add -A
git commit -m "SEO: publish eyewear (P25) and size-inclusive (P26) apparel campaign articles"
git push origin main
```

## After the push

Vercel auto-deploys in 30–60s. Then:

```bash
sleep 45
curl -sS -X POST https://api.indexnow.org/IndexNow \
  -H 'Content-Type: application/json' \
  -d '{"host":"100creatives.com","key":"e6baf767262d12f58083a712d380812b","keyLocation":"https://100creatives.com/e6baf767262d12f58083a712d380812b.txt","urlList":["https://100creatives.com/eyewear-and-sunglasses-brand-campaign-and-editorial-imagery.html","https://100creatives.com/size-inclusive-apparel-brand-campaign-and-editorial-imagery.html","https://100creatives.com/sitemap.xml"]}' -w '\nHTTP %{http_code}\n'
```

Then request indexing for both URLs in Google Search Console → URL Inspection.

## Fixed in this run

`publish.sh` had a bug that made it print `✓ Published via fallback` even when the push failed —
which is why the 2026-09-02 run looked successful. Two changes:

- The fallback path now checks the exit status of `git push` and returns failure loudly instead of
  claiming success.
- The fallback `/tmp` clone now sweeps in any repo-root `.html` article that isn't already on
  origin, so once auth is restored a single run ships the whole backlog rather than only that
  day's article.

**Until the PAT is restored, every daily run will hit this same wall and the backlog will keep
growing.** Fixing step 2 once unblocks the whole engine.
