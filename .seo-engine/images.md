# Image Inventory — 100 Creatives

The engine consults this file to pick relevant images for each new article. **Only use images listed here — do not invent paths.** All paths are absolute from site root (start with `/images/...` or `/campaigns/web/...`). Use 2–4 images per article when they genuinely fit the topic. Skip images entirely if nothing in the inventory is relevant — empty article > forced bad image.

## Verticals → image folders

### Apparel (luxury, bridal, ethnic, fashion)
- **Anita Dongre** — bridal lehenga collection, AI fashion photography hero work
  - `/images/anitadongre/lehnga-2.jpg` — bridal lehenga, on-model hero
  - `/images/anitadongre/lehnga-3.jpg` — drape detail, fabric fidelity close-up
  - `/images/anitadongre/lehnga-4.jpg` — embellishment close-up, beadwork
  - `/images/anitadongre/lehnga-5.jpg` — editorial/campaign frame
  - `/images/anitadongre/lehnga-7.jpg` — full-look lifestyle context
  - `/images/anitadongre/lehnga-8.jpg` — secondary angle, PDP-grade
  - `/images/anitadongre/anita-web.mp4` — collection motion reel
  - **Use for:** AI fashion photography, luxury apparel, ethnic/bridal wear, fabric fidelity, on-model at scale

### Beauty / Skincare (premium serums, color cosmetics)
- **Golden Rule** — premium beauty/skincare brand
  - `/images/goldenrule/goldenrule-1.png` through `/images/goldenrule/goldenrule-8.png`
  - **Use for:** beauty product photography, skincare PDP, color cosmetics, premium beauty visuals, serum/bottle shots

### Supplements / Wellness
- **Armra** — colostrum supplement brand
  - `/images/armra/armra-1.png` through `/images/armra/armra-9.png`
  - **Use for:** supplements photography, wellness brand visuals, powder/jar product shots, functional health, premium supplement PDP

### Food CPG (snacks, packaged goods)
- **Chobani** — yogurt/dairy CPG flagship work
  - `/images/chobani/chobani-1.png` through `/images/chobani/chobani-10.png`
  - **Use for:** CPG food photography, dairy/yogurt brand visuals, packaged food, retail-shelf imagery, brand campaign work
- **Smackin'** — snack brand (sunflower seeds)
  - `/images/smackin/smackin-1.png` through `/images/smackin/smackin-10.png`
  - **Use for:** snack brand photography, packaged-food CPG, bag/pouch product shots, lifestyle snack imagery

### Beverage (wine, spirits, sparkling, soda)
- **Barefoot Wines** — wine brand campaign
  - `/images/barefootwines/barefoot-1.png` through `/images/barefootwines/barefoot-6.png`
  - **Use for:** wine photography, alcohol brand visuals, bottle product shots, wine campaign
- **Zero Lush** — non-alcoholic sparkling wine (rose + white)
  - `/images/zerolush/sparkling rose 565454.png`
  - `/images/zerolush/sparkling rose 658980.png`
  - `/images/zerolush/sparkling rose b93e-46db2f018d71.png`
  - `/images/zerolush/sparkling white 1.png` through `/images/zerolush/sparkling white 10.png`
  - `/images/zerolush/sparkling white.png`
  - `/images/zerolush/zerolush rose.png`
  - `/images/zerolush/zerolush-editorial-1.png`
  - **Use for:** functional beverage, non-alc, sparkling wine, premium drinks, editorial bottle work
  - **Filename note:** these have spaces — URL-encode as `%20` in href (e.g. `/images/zerolush/sparkling%20rose%20565454.png`)
- **Maker's Mark** — premium bourbon/spirits
  - `/campaigns/web/makers-mark/makers-1.jpg` through `/campaigns/web/makers-mark/makers-4.jpg` (+ matching .mp4 motion)
  - **Use for:** spirits/bourbon photography, premium alcohol, luxury beverage campaign
- **Fizz Soda** — soda can/beverage
  - `/campaigns/web/fizz-soda.jpg` (+ `.mp4` motion)
  - **Use for:** soda/can beverage, beverage product shot, can rendering

### Home / Decor / Luxury Sculpture
- **David Harber** — luxury garden sculpture
  - `/images/davidharber/harber-1.png` through `/images/davidharber/harber-5.png`
  - **Use for:** luxury home goods, garden/outdoor decor, sculpture, architectural product photography, premium home brand visuals

### Auto / Outdoor / Lifestyle Campaigns
- **Ford Bronco** — automotive lifestyle campaign
  - `/campaigns/web/ford-bronco/bronco-1.jpg` through `/campaigns/web/ford-bronco/bronco-3.jpg`
  - `/campaigns/web/ford-bronco/bronco-still.jpg`
  - **Use for:** automotive, outdoor lifestyle, vehicle campaign, adventure/utility brand
- **Porsche** — luxury automotive
  - `/campaigns/web/porsche/porsche-1.jpg` through `/campaigns/web/porsche/porsche-4.jpg`
  - `/campaigns/web/porsche/porsche-hero-1.jpg`
  - **Use for:** luxury automotive, performance vehicle photography, premium campaign work
- **Outdoors / Running / Eyewear** — Shady Rays + Arc'teryx-adjacent
  - `/campaigns/web/outdoors/hero-run.jpg`
  - `/campaigns/web/outdoors/mud-running.jpg`
  - `/campaigns/web/outdoors/shady-rays-arcteryx.jpg`
  - **Use for:** activewear, performance apparel, eyewear, outdoor/sports lifestyle, sunglasses

## Hero/OG image defaults (when nothing vertical-specific fits)
- `/images/chobani/chobani-9.png` — flagship default (already used as site-wide OG)
- `/images/anitadongre/lehnga-2.jpg` — apparel default

## Embedding rules
1. **Picker logic:** Match topic vertical → folder above. If a closer brand fit exists (e.g. article about "supplement product photography" → use Armra), prefer it. Avoid using the same brand twice in 7 days (check MEMORY.md).
2. **Use existing site patterns:** copy the `<figure class="gallery-item">...<figcaption>` markup from `ai-fashion-photography.html` lines 132–140, OR use `<div class="video-block"><video>...</div>` from lines 99–107 for motion.
3. **Alt text is mandatory** and must include the primary keyword + brand context (e.g., `alt="Premium skincare product photography — Golden Rule serum bottle in studio light"`).
4. **OG image:** set `<meta property="og:image">` to the most flagship image used on the page (or default to chobani-9 if none).
5. **Never** invent image paths. **Never** hotlink external images. **Never** reuse the exact same image set as the previous 3 articles (MEMORY.md tracks this).
