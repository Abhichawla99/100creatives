#!/usr/bin/env python3
"""Pre-flight validator for 100creatives.com pages.

Usage (from the repo root):
    python3 .seo-engine/validate.py page-a.html page-b.html
    python3 .seo-engine/validate.py --all          # every root page + work/*.html

Exit code 1 if any FAIL. WARN lines are advisory.
"""
import glob, html, json, os, re, sys

BASE = "https://www.100creatives.com"
BANNED = [
    (r"one[- ]fifth (of )?the cost", "one fifth the cost"),
    (r"ten times the speed|10x (faster|the speed)", "ten times the speed"),
    (r"\bthe leading\b|\bleading (ai|creative|ad) (product photography |creative |)agency", "leading agency"),
    (r"\bfive years\b|\b5 years in\b", "five years"),
    (r"zero missed deadlines", "zero missed deadlines"),
    (r"NDA[^.<]{0,60}(roster|major brands|brands you have heard)", "NDA roster claim"),
    (r"approved[^.<]{0,40}in writing|signed off explicitly", "approved-in-writing claim"),
    (r"thousands of SKUs", "thousands of SKUs"),
    (r"client work spans|brands we've designed for|brands we have designed for|we have shipped for|our roster spans|"
     r"we have produced for|brands we have produced for|work we do for (Barefoot|Maker)|our friends at Anita Dongre|"
     r"documented case work with|reference case-study anchors", "named-client framing"),
    (r"we work with [^.<]{0,80}(Chobani|ARMRA|Armra|Barefoot|Carbon38|Smackin|Zero Lush|Anita Dongre)", "named-client framing"),
    (r"our work (anchors|for) [^.<]{0,60}(Chobani|Armra|ARMRA|Anita Dongre|Ralph Lauren|Porsche)", "named-client framing"),
    (r"foundingDate\"?\s*:\s*\"20(1\d|2[0-5])", "founding year before 2026"),
    (r"Offer expires in|timer hits zero", "countdown urgency"),
]

def text_of(fragment):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", fragment))).strip()

def check(path):
    fails, warns = [], []
    s = open(path, encoding="utf-8").read()
    slug = path[:-5]
    robots = re.search(r'<meta name="robots" content="([^"]*)"', s)
    noindex = bool(robots and "noindex" in robots.group(1))

    # JSON-LD
    lds = []
    for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            lds.append(json.loads(raw))
        except Exception as ex:
            fails.append(f"JSON-LD does not parse: {ex}")
    flat = json.dumps(lds)
    if re.search(r'"(aggregateRating|review)"\s*:', flat):
        fails.append("AggregateRating/Review markup present")

    # FAQ sync
    faq = [o for o in lds if isinstance(o, dict) and o.get("@type") == "FAQPage"]
    visible = re.findall(r"<summary[^>]*>(.*?)</summary>\s*(?:<div class=\"faq-answer\">\s*)?<p>(.*?)</p>", s, re.S)
    visible = [(text_of(q), text_of(a)) for q, a in visible]
    if faq:
        schema = [(text_of(e.get("name", "")), text_of(e.get("acceptedAnswer", {}).get("text", "")))
                  for e in faq[0].get("mainEntity", [])]
        if not visible:
            fails.append("FAQPage JSON-LD present but no visible FAQ")
        elif schema != visible[:len(schema)] or len(visible) < len(schema):
            bad = [q for (q, a), (vq, va) in zip(schema, visible) if (q, a) != (vq, va)]
            fails.append(f"FAQ visible text differs from JSON-LD ({len(schema)} schema vs {len(visible)} visible; first mismatch: {bad[:1]})")

    # canonical
    canon = re.search(r'<link rel="canonical" href="([^"]*)"', s)
    want = f"{BASE}/" if slug == "index" else f"{BASE}/{slug}"
    if not canon:
        fails.append("no canonical")
    elif canon.group(1) != want:
        fails.append(f"canonical {canon.group(1)} != {want}")
    if "https://100creatives.com" in s:
        fails.append("non-www absolute URL present")

    # internal links
    for href in sorted(set(re.findall(r'href="(/[^"]*)"', s))):
        target = href.split("#")[0].split("?")[0]
        if target in ("", "/"):
            continue
        rel = target.lstrip("/")
        if os.path.exists(rel) or os.path.exists(rel + ".html") or os.path.exists(os.path.join(rel, "index.html")):
            continue
        fails.append(f"broken internal link {href}")
    if re.search(r'href="/[^"]*\.html', s):
        warns.append("internal link uses .html")

    # claims
    body = s[s.find("<body"):] if "<body" in s else s
    for pat, label in BANNED:
        for m in re.finditer(pat, s, re.I):
            ctx = text_of(s[max(0, m.start() - 80):m.end() + 40])
            (warns if noindex else fails).append(f"banned claim [{label}]: ...{ctx}...")
            break

    # basics
    title = re.search(r"<title>(.*?)</title>", s, re.S)
    if not title:
        fails.append("no <title>")
    elif len(html.unescape(title.group(1))) > 60:
        warns.append(f"title {len(html.unescape(title.group(1)))} chars")
    desc = re.search(r'<meta name="description" content="([^"]*)"', s)
    if not desc:
        warns.append("no meta description")
    elif len(html.unescape(desc.group(1))) > 160:
        warns.append(f"meta description {len(html.unescape(desc.group(1)))} chars")
    if "<h1" not in s:
        fails.append("no <h1>")
    if 'class="fade-in' in s or " fade-in" in s:
        if "IntersectionObserver" not in s and "classList.add('visible')" not in s and 'classList.add("visible")' not in s:
            fails.append("fade-in used but IntersectionObserver script missing (content would stay invisible)")
    dashes = text_of(re.sub(r"<script.*?</script>|<style.*?</style>|<footer.*?</footer>", "", body, flags=re.S)).count("—")
    if dashes:
        warns.append(f"{dashes} em dash(es) in body copy")
    if noindex:
        warns.append("page is noindex")
    return fails, warns

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    files = sorted(glob.glob("*.html")) + sorted(glob.glob("work/*.html")) if args == ["--all"] else args
    total_fail = 0
    for f in files:
        if not os.path.exists(f):
            print(f"FAIL {f}: file not found")
            total_fail += 1
            continue
        fails, warns = check(f)
        total_fail += len(fails)
        status = "FAIL" if fails else "ok  "
        print(f"{status} {f}")
        for x in fails:
            print(f"     FAIL {x}")
        if args != ["--all"]:
            for x in warns:
                print(f"     warn {x}")
    print(f"\n{len(files)} file(s), {total_fail} failure(s)")
    sys.exit(1 if total_fail else 0)

if __name__ == "__main__":
    main()
