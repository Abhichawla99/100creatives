#!/usr/bin/env bash
# Daily SEO publish — stages new HTML + sitemap + state, commits, pushes to main.
# Usage: bash publish.sh "<slug>" "<h1 title>"
set -euo pipefail

SLUG="${1:?slug required}"
TITLE="${2:?title required}"

# Auto-detect repo root: works on macOS (/Users/home/100creatives) and inside the
# Cowork sandbox mount (/sessions/<id>/mnt/100creatives/).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO"

# Sanity check: file must exist
if [ ! -f "${SLUG}.html" ]; then
  echo "ERROR: ${SLUG}.html does not exist. Generate the article first." >&2
  exit 1
fi

# Stage the published artifacts + any engine updates (style, run instructions, queue, state)
git add "${SLUG}.html" sitemap.xml .seo-engine/ .gitignore 2>/dev/null || true

# Bail early if nothing changed
if git diff --cached --quiet; then
  echo "Nothing to commit. Did you forget to write the file?" >&2
  exit 1
fi

# Commit (descriptive, search-engine-friendly message)
COMMIT_MSG="SEO: publish ${TITLE}

Daily SEO post — slug: ${SLUG}
Targets: AI product photography for D2C brands.
Auto-published by SEO engine on $(date +%Y-%m-%d)."

git commit -m "$COMMIT_MSG"

# Push to main (Vercel auto-deploys)
git push origin main

echo ""
echo "✓ Published: https://100creatives.com/${SLUG}"
echo "✓ Vercel will deploy in ~30–60 seconds."
