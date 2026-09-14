"""One-off AI answer baseline for 100 Creatives.

Asks ChatGPT (OpenAI web search), Perplexity Sonar and Gemini (web plugin) the
questions a buyer would type, via OpenRouter, the same way the DialSheet
citation check does. Nothing is saved outside the scratchpad. The API key is
read from DialSheet's .env.local and never printed.
"""
import json, re, sys, time, urllib.request, concurrent.futures as cf
from urllib.parse import urlparse

ENV = "/Users/home/dialsheet/.env.local"
OUT = sys.argv[1]
KEY = None
for line in open(ENV):
    if line.startswith("OPENROUTER_API_KEY="):
        KEY = line.split("=", 1)[1].strip().strip('"').strip("'")
if not KEY:
    sys.exit("no OPENROUTER_API_KEY")

MODELS = {
    "chatgpt": "openai/gpt-5.4-mini",
    "perplexity": "perplexity/sonar",
    "gemini": "google/gemini-3.8-flash",
}
JUDGE = "google/gemini-3.8-flash"

PROMPTS = [
    # ad creative lane (where GSC impressions are)
    ("static-ad-agency", "What are the best agencies for static ad creatives for Meta ads for DTC brands? Name specific companies."),
    ("unlimited-subscription", "Which companies offer unlimited ad creatives on a flat monthly subscription? Name specific companies and prices."),
    ("dtc-50k-meta", "I run a DTC brand spending $50k a month on Meta and need 30+ new static ads a month. Who should I hire? Name specific companies."),
    ("static-ad-service", "What is a good static ad design service for ecommerce brands? Name specific companies."),
    ("scale-creative-agency", "What are the best creative agencies for scaling ad creative production for paid social in 2026? Name specific agencies."),
    ("static-ad-examples", "Where can I find good examples of high-converting DTC static ads?"),
    ("agency-vs-freelancer", "Should a DTC brand hire a creative agency, a freelancer, or an in-house designer for ad creatives? Name options."),
    # AI product / fashion photography lane (where most pages are)
    ("ai-photo-agency", "What are the best done-for-you AI product photography agencies (not self-serve tools) for ecommerce brands? Name specific companies."),
    ("ai-fashion-onmodel", "Which companies do AI fashion photography for clothing brands, turning flat lays into on-model images? Name specific companies and prices."),
    ("ai-photo-cost", "How much does AI product photography cost in 2026 compared with a traditional studio shoot? Name specific providers and prices."),
    ("apparel-500-skus", "I have 500 apparel SKUs and no budget for a studio shoot. Which service should I use for on-model photos? Name specific companies."),
    # wellness / CPG lane (homepage positioning)
    ("wellness-agency", "What are the best creative agencies for health and wellness brands like supplements and skincare? Name specific agencies."),
    ("supplement-creative", "Which creative agency should a supplement brand hire for ad creative and product imagery? Name specific agencies."),
    # workflows lane
    ("brand-trained-pipeline", "Which agencies build custom brand-trained AI image generation workflows for in-house creative teams? Name specific companies."),
    # entity checks
    ("entity-what", "What is 100 Creatives (100creatives.com)? What do they do, who runs it, and what do they charge?"),
    ("entity-legit", "Is 100 Creatives (100creatives.com) a legitimate creative agency? What do reviews say?"),
]

def post(payload):
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://www.100creatives.com",
            "X-Title": "100 Creatives AEO baseline",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())

URL_RE = re.compile(r"https?://[^\s)\]>\"']+")

def ask(engine, prompt):
    payload = {"model": MODELS[engine], "messages": [{"role": "user", "content": prompt}],
               "max_tokens": 1100, "temperature": 0.3}
    if engine != "perplexity":
        payload["plugins"] = [{"id": "web"}]
    res = post(payload)
    if res.get("error"):
        raise RuntimeError(res["error"].get("message", str(res["error"])))
    msg = res["choices"][0]["message"]
    text = msg.get("content") or ""
    cites = [a["url_citation"]["url"] for a in (msg.get("annotations") or [])
             if a.get("type") == "url_citation" and a.get("url_citation", {}).get("url")]
    cites += res.get("citations") or []
    cites += URL_RE.findall(text)
    clean = []
    for u in cites:
        u = re.sub(r"[?&]utm_source=[^&]*", "", u).rstrip(".,;")
        if u not in clean:
            clean.append(u)
    return text, clean

def judge(text):
    sys_prompt = ("You grade an AI assistant's answer to a buyer's question about creative agencies, ad creative "
                  "services or AI photography. Return ONLY a JSON object: "
                  '{"verdict":"recommended"|"mentioned"|"absent","named":["Company", ...],"describes_100_creatives_as":"short phrase or empty"} '
                  'verdict is about "100 Creatives" (also written 100creatives): "recommended" if presented as an option to '
                  'consider, "mentioned" if only in passing or with a caveat, "absent" if not present. named: the companies or '
                  "products the answer recommends, in order, up to 10, excluding 100 Creatives.")
    res = post({"model": JUDGE, "temperature": 0, "max_tokens": 1500,
                "messages": [{"role": "system", "content": sys_prompt}, {"role": "user", "content": text[:7000]}]})
    raw = res["choices"][0]["message"].get("content") or ""
    s, e = raw.find("{"), raw.rfind("}")
    j = json.loads(raw[s:e + 1]) if s >= 0 else {"verdict": "absent", "named": []}
    if j.get("verdict") == "absent" and re.search(r"100\s?creatives", text, re.I):
        j["verdict"] = "mentioned"
    return j

def cell(engine, pid, prompt):
    for attempt in range(2):
        try:
            text, cites = ask(engine, prompt)
            j = judge(text)
            return {"engine": engine, "prompt_id": pid, "prompt": prompt, "answer": text, "citations": cites, **j}
        except Exception as ex:
            err = str(ex)
            time.sleep(3)
    return {"engine": engine, "prompt_id": pid, "prompt": prompt, "error": err}

jobs = [(e, pid, p) for pid, p in PROMPTS for e in MODELS]
rows = []
with cf.ThreadPoolExecutor(max_workers=6) as pool:
    for r in pool.map(lambda a: cell(*a), jobs):
        rows.append(r)
        mark = r.get("verdict", "ERR")[:3].upper()
        print(f"{mark:4} {r['engine']:10} {r['prompt_id']:24} {', '.join((r.get('named') or [])[:5]) if 'error' not in r else r['error'][:80]}", flush=True)

json.dump(rows, open(OUT, "w"), indent=1)
print(f"\nsaved {len(rows)} cells -> {OUT}")
