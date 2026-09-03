# Unpushed backlog

**Last updated:** 2026-09-03

## Status: EMPTY — nothing pending

Both backlogged articles (eyewear 09-02, size-inclusive 09-03) shipped on 2026-09-03 in commit `89765b4`. Push auth now comes from `GITHUB-TOKEN.txt` (gitignored) via `publish.sh`.

Optional cleanup from Terminal to restore the primary (non-/tmp) publish path:

```bash
cd /Users/home/100creatives && rm -f .git/index.lock .git/HEAD.lock && git reset -q && git pull --rebase origin main
```
