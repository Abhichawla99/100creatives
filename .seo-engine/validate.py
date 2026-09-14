#!/usr/bin/env python3
"""Pre-flight validator for 100creatives.com pages.

Usage (from the repo root):
    python3 .seo-engine/validate.py page-a.html page-b.html
    python3 .seo-engine/validate.py --all          # every root page + work/*.html
    python3 .seo-engine/validate.py --changed      # pages changed vs origin/main

Exit code 1 if any FAIL. WARN lines are advisory.
"""
import glob, html, json, os, re, sys

BASE = "https://www.100creatives.com"
BANNED = [
    (r"one[- ]fifth (of )?the (per[- ]\w+ )?cost", "one fifth the cost"),
    (r"ten times the speed|10x (faster|the speed)", "ten times the speed"),
    (r"\bthe leading (ai|creative|ad|agency|product|photography|studio)|\bleading (ai|creative|ad) (product photography |creative |)agency", "leading agency"),
    (r"\b(after|over the (last|past)|for the (last|past)) five years\b|five years in the category|onboarded over the last five years", "five years"),
    (r"zero missed deadlines", "zero missed deadlines"),
    (r"\bNDA\b[^.<]{0,60}(roster|major brands|brands you have heard)", "NDA roster claim"),
    (r"approved case-study treatment|explicitly approved[^.<]{0,40}in writing|signed off explicitly", "approved-in-writing claim"),
    (r"thousands of SKUs (a|per) month|(ship|shipped|produce|produced) thousands of SKUs", "thousands of SKUs"),
    (r"client work spans|brands we've designed for|brands we have designed for|we have shipped for|our roster spans|"
     r"we have produced for|brands we have produced for|work we do for (Barefoot|Maker)|our friends at Anita Dongre|"
     r"documented case work with|reference case-study anchors", "named-client framing"),
    (r"we work with [^.<]{0,80}(Chobani|ARMRA|Armra|Barefoot|Carbon38|Smackin|Zero Lush|Anita Dongre)", "named-client framing"),
    (r"our work (anchors|for) [^.<]{0,60}(Chobani|Armra|ARMRA|Anita Dongre|Ralph Lauren|Porsche)", "named-client framing"),
    (r"\b(we|our team) (hold|offer|provide|give)[^.<]{0,40}(pixel|product)[- ]accuracy guarantee|\bwe redo (it )?at no cost|product accuracy guaranteed", "accuracy guarantee"),
    (r"foundingDate\"?\s*:\s*\"20(1\d|2[0-5])", "founding year before 2026"),
    (r"Offer expires in|timer hits zero", "countdown urgency"),
]


from html.parser import HTMLParser

class _FAQParser(HTMLParser):
    """Collects visible Q&A pairs from <details><summary> blocks and from
    elements whose class contains faq-question / faq-answer."""
    VOID = {"br", "img", "hr", "input", "meta", "link", "source", "path", "line", "circle", "rect"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # (tag, role)
        self.skip = 0
        self.pairs, self.q, self.a = [], None, None
        self.mode = None         # "q" | "a" | "details-a"

    def _role(self, tag, attrs):
        cls = dict(attrs).get("class", "") or ""
        if tag == "summary":
            return "q"
        if "faq-question" in cls:
            return "q"
        if "faq-answer" in cls:
            return "a"
        return None

    def handle_starttag(self, tag, attrs):
        if tag in ("svg", "script", "style"):
            self.skip += 1
        if tag in self.VOID:
            return
        role = self._role(tag, attrs)
        if tag == "details":
            role = "details"
        self.stack.append((tag, role))
        if role == "q":
            self.mode, self.q = "q", ""
        elif role == "a":
            self.mode, self.a = "a", ""

    def handle_endtag(self, tag):
        if tag in ("svg", "script", "style"):
            self.skip = max(0, self.skip - 1)
        if tag in self.VOID:
            return
        while self.stack:
            t, role = self.stack.pop()
            if role == "q":
                self.mode = "details-a" if any(r == "details" for _, r in self.stack) else None
                if self.mode == "details-a":
                    self.a = ""
            elif role == "a":
                self._flush()
            elif role == "details":
                if self.mode == "details-a":
                    self._flush()
                self.mode = None
            if t == tag:
                break

    def _flush(self):
        if self.q is not None and self.a is not None and self.a.strip():
            self.pairs.append((self.q, self.a))
        self.q, self.a, self.mode = (None, None, None)

    def handle_data(self, data):
        if self.skip:
            return
        if self.mode == "q" and self.q is not None:
            self.q += data
        elif self.mode in ("a", "details-a") and self.a is not None:
            self.a += data

def extract_faq(s):
    p = _FAQParser()
    try:
        p.feed(s[s.find("<body"):] if "<body" in s else s)
    except Exception:
        return []
    return [(re.sub(r"\s*[+\u2212\u00d7\u2013-]\s*$", "", text_of(q)), text_of(a)) for q, a in p.pairs]

def text_of(fragment):
    t = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", fragment))).strip()
    # tags replaced by spaces leave "pricing ." after a closing </a>; normalise before comparing
    return re.sub(r"\s+([.,;:!?)])", r"\1", re.sub(r"\(\s+", "(", t))

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
    visible = extract_faq(s)
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
    if args == ["--all"]:
        files = sorted(glob.glob("*.html")) + sorted(glob.glob("work/*.html"))
    elif args == ["--changed"]:
        import subprocess
        out = subprocess.run(["git", "diff", "--name-only", "origin/main", "--", "*.html", "work/*.html"],
                             capture_output=True, text=True).stdout.split()
        new = subprocess.run(["git", "ls-files", "--others", "--exclude-standard", "--", "*.html"],
                             capture_output=True, text=True).stdout.split()
        files = sorted(set(f for f in out + new if os.path.exists(f)))
    else:
        files = args
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
        if args not in (["--all"], ["--changed"]):
            for x in warns:
                print(f"     warn {x}")
    print(f"\n{len(files)} file(s), {total_fail} failure(s)")
    sys.exit(1 if total_fail else 0)

if __name__ == "__main__":
    main()
