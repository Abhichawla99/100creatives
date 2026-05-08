#!/usr/bin/env bash
# Daily SEO publish — pulls latest, stages, commits, pushes to main.
# Usage: bash publish.sh "<slug>" "<h1 title>"
#
# Resilience: if the local clone has stuck .git/*.lock files (Cowork sandbox
# mount issue), this script falls back to a fresh clone in /tmp, copies the
# article and engine state into it, and pushes from there. Either way the
# article ends up on origin/main and Vercel deploys.

set -euo pipefail

SLUG="${1:?slug required}"
TITLE="${2:?title required}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/.." && pwd)"

ARTICLE="${REPO}/${SLUG}.html"
SITEMAP="${REPO}/sitemap.xml"

# Sanity: the article must exist
if [ ! -f "$ARTICLE" ]; then
  echo "ERROR: $ARTICLE does not exist. Generate the article first." >&2
  exit 1
fi

COMMIT_MSG="SEO: publish ${TITLE}

Daily SEO post — slug: ${SLUG}
Targets: AI product photography for D2C brands.
Auto-published by SEO engine on $(date +%Y-%m-%d)."

# ----- PRIMARY PATH: commit + push from the original repo -----
push_from_repo() {
  cd "$REPO"
  echo "→ Trying primary path (push from local clone)…"

  # Pull latest first so we don't get rejected on non-fast-forward
  git pull --rebase origin main 2>&1 | tail -3

  # Stage everything the engine touches
  git add "${SLUG}.html" sitemap.xml .seo-engine/ .gitignore 2>/dev/null || true

  if git diff --cached --quiet; then
    echo "Nothing staged. Did the article get written?"
    return 1
  fi

  git commit -m "$COMMIT_MSG"
  git push origin main
  return 0
}

# ----- FALLBACK PATH: fresh /tmp clone, copy files in, push -----
push_via_tmp_clone() {
  echo "→ Primary failed. Falling back to /tmp clone path…"

  local TMPDIR="/tmp/100creatives-publish-$$"
  rm -rf "$TMPDIR" 2>/dev/null || true

  # Pull the remote URL (with embedded token) from the local repo's git config
  local REMOTE_URL
  REMOTE_URL="$(cd "$REPO" && git config --get remote.origin.url)"

  git clone "$REMOTE_URL" "$TMPDIR" >/dev/null 2>&1
  cd "$TMPDIR"

  git config user.name "100Creatives SEO Bot"
  git config user.email "abhixchawla@gmail.com"

  # Copy the article + sitemap + entire .seo-engine/ + .gitignore
  cp "$ARTICLE" "$TMPDIR/${SLUG}.html"
  cp "$SITEMAP" "$TMPDIR/sitemap.xml"
  mkdir -p "$TMPDIR/.seo-engine"
  cp -r "$REPO/.seo-engine/." "$TMPDIR/.seo-engine/"
  [ -f "$REPO/.gitignore" ] && cp "$REPO/.gitignore" "$TMPDIR/.gitignore"

  git add -A
  if git diff --cached --quiet; then
    echo "Nothing changed vs origin. Aborting fallback path."
    rm -rf "$TMPDIR"
    return 1
  fi

  git commit -m "$COMMIT_MSG"
  git push origin main

  # Clean up
  rm -rf "$TMPDIR"
  return 0
}

# Try primary, fall back, error if both fail
if push_from_repo 2>&1; then
  echo ""
  echo "✓ Published: https://100creatives.com/${SLUG}"
  echo "✓ Vercel will deploy in ~30–60 seconds."
elif push_via_tmp_clone 2>&1; then
  echo ""
  echo "✓ Published via fallback: https://100creatives.com/${SLUG}"
  echo "✓ Vercel will deploy in ~30–60 seconds."
  echo "ℹ Local clone at $REPO may be behind origin — run 'git pull' there to sync."
else
  echo "" >&2
  echo "✗ Both publish paths failed. Token may be expired, or git auth is broken." >&2
  echo "  Check: cd $REPO && git remote -v && git push origin main" >&2
  exit 1
fi
