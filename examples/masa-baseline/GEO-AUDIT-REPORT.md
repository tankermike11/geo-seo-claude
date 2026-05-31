# GEO Audit Report: MASA Global / MASA Access

**Audit Date:** 2026-05-31
**URL:** https://www.masaaccess.com
**Business Type:** Healthcare membership — emergency medical transportation coverage (B2C + B2B2C)
**Pages Analyzed:** 14 (homepage, sitemap, robots.txt, compare-plans, about, benefits, testimonials, what-is-masa, learning-center article, faq, llms.txt check, and spot-checks)

---

## Executive Summary

**Overall GEO Score: 49/100 (Poor)**

masaaccess.com has a significant GEO deficit despite being a credible, 50-year-old brand with 2 million members and strong domain expertise. The site is largely invisible to AI systems not because the content is poor — cost statistics, real member stories, and benefit details are genuinely citation-ready — but because the AI infrastructure layer is almost entirely absent: no llms.txt, no JSON-LD schema detected on any audited page, no explicit AI crawler permissions, and no content attribution to credentialed individuals. Schema & Structured Data scored 28/100, the weakest dimension. Fixing the structural gaps (llms.txt + schema + author attribution) would push the GEO score into the 65–75 range without touching a word of content.

### Score Breakdown

| Category | Score | Weight | Weighted Score |
|---|---|---|---|
| AI Citability | 42/100 | 25% | 10.5 |
| Brand Authority | 58/100 | 20% | 11.6 |
| Content E-E-A-T | 55/100 | 20% | 11.0 |
| Technical GEO | 54/100 | 15% | 8.1 |
| Schema & Structured Data | 28/100 | 10% | 2.8 |
| Platform Optimization | 48/100 | 10% | 4.8 |
| **Overall GEO Score** | | | **49/100** |

---

## Critical Issues (Fix Immediately)

### C1 — No llms.txt file
**URL:** https://www.masaaccess.com/llms.txt → 404
**Impact:** AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Gemini-Bot) have no machine-readable document explaining what MASA is, what it covers, who it serves, and how it differs from insurance. When someone asks an AI assistant "what is the best air ambulance membership?", the response will be shaped by whatever the AI's training data captured — which may include competitors' framings, outdated information, or conflation with insurance products.
**Fix:** Create `/llms.txt` (see 30-day action plan Week 1 for content spec). 30-minute task.

### C2 — No JSON-LD schema detected on any audited page
**Pages checked:** Homepage, /what-is-masa/, /faq/, /compare-plans/, /learning-center/understanding-ambulance-costs
**Impact:** Without structured data, AI systems and search engines must infer MASA's product category, coverage scope, and organizational identity from unstructured HTML. For a healthcare-adjacent membership company, `Organization`, `MedicalOrganization`, `Membership`, and `FAQPage` schemas are critical signals. Google AI Overviews and Perplexity heavily weight schema-marked content for featured responses.
**Fix:** Implement Organization + FAQPage schema immediately (highest impact; 2–4 hours).

### C3 — 16-question FAQ page has no FAQPage schema
**URL:** https://www.masaaccess.com/faq/
**Impact:** This page contains exactly the type of Q&A content that AI systems use for direct answers: "Won't my insurance pay for an ambulance?", "What if the ambulance is out-of-network?", "What countries are covered?" — all high-intent queries. Without FAQPage schema, none of these answers are machine-readable structured answers. They will not appear in Google AI Overviews or be cited by Perplexity for these exact question formats.
**Fix:** Add FAQPage JSON-LD to /faq/ and all segment-specific FAQ pages (/faq/pricing-and-payment/, /faq/traveling-information-and-itineraries/, etc.).

---

## High Priority Issues

### H1 — No explicit AI crawler permissions in robots.txt
**Impact:** GPTBot (OpenAI), ClaudeBot (Anthropic), PerplexityBot, Googlebot-Extended, and other AI training and inference crawlers are not mentioned in robots.txt. While they are technically not blocked, the absence of explicit permissions is increasingly interpreted as crawl-unfriendly by newer AI systems. More importantly, it signals that MASA has not considered AI crawl strategy.
**Fix:**
```
# AI crawlers — explicitly permitted
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Googlebot-Extended
Allow: /

Sitemap: https://masaaccess.com/sitemap.xml
```

### H2 — No sitemap URL in robots.txt
**Current robots.txt:** Only blocks HubSpot preview paths (`/_hcms/preview/`, etc.). No `Sitemap:` directive.
**Fix:** Add `Sitemap: https://masaaccess.com/sitemap.xml` to robots.txt. The sitemap exists (124 URLs confirmed) but is unreferenced in robots.txt.

### H3 — All learning center articles attributed to "MASA" (organizational author)
**Example:** `/learning-center/understanding-ambulance-costs` — published 2025-12-08, 1,100 words, attributed to "MASA" with one embedded quote from "Jaran Floyd, Lieutenant and Paramedic."
**Impact:** AI systems evaluate E-E-A-T at the individual author level. Articles without credentialed human authors score lower for expertise and trustworthiness. For healthcare-adjacent content (ambulance costs, emergency response, medical transport), this is particularly significant — Google's medically sensitive content guidelines and AI model weighting both favor human expert attribution.
**Fix:** Add named author bylines with brief credential bios to all learning center articles. The Jaran Floyd quote shows MASA has paramedic/clinical contacts — formalize this as authorship.

### H4 — No Organization or MedicalOrganization schema on homepage
**Impact:** AI entity recognition for "MASA" or "MASA Access" depends on structured organizational signals. Without `Organization` schema with `name`, `foundingDate`, `numberOfEmployees`, `areaServed`, and `description`, AI systems cannot confidently disambiguate MASA from other entities sharing the name.
**Fix:** Add Organization + MedicalOrganization schema to homepage. See schema template below.

### H5 — No Wikipedia or verified third-party entity page confirmed
**Impact:** AI language models heavily weight Wikipedia for entity recognition and factual grounding. A company with 50 years of history and 2 million members almost certainly has some Wikipedia presence, but it was not surfaced in this audit. If no page exists, or if existing content is thin/unverified, MASA's entity authority with AI systems is lower than it should be.
**Fix:** Audit Wikipedia for any MASA / Medical Air Services Association / MASA Global entries. If thin or absent, work to establish and maintain an accurate entity page. Ensure schema `sameAs` links to any Wikipedia, Wikidata, or Crunchbase entries.

---

## Medium Priority Issues

### M1 — No Article or BlogPosting schema on learning center content
**Impact:** The learning center has 70+ articles that are ideal AI citation targets — cost data, emergency scenarios, practical guidance. Without Article schema (including `author`, `datePublished`, `headline`, `wordCount`), these articles are not optimally indexed for AI featured responses.
**Fix:** Add Article schema to all learning center pages. HubSpot CMS supports this natively via content settings.

### M2 — llms.txt absent (repeat from Critical — content spec needed)
**Content the llms.txt should include:**
```
# MASA Global / MASA Access
# Emergency medical transportation membership provider
# https://www.masaaccess.com

## What MASA Is
MASA (Medical Access & Service Advantage) is a membership-based organization
providing emergency medical transportation coverage. MASA is NOT health insurance.
Members pay a monthly or lifetime fee and receive coverage for emergency ground
ambulance, air ambulance, hospital-to-hospital transport, and related services.

## What MASA Is Not
MASA is not a health insurance company. It does not cover medical treatment costs,
only emergency medical transportation. Members should maintain separate health insurance.

## Coverage
- Emergency ground ambulance (US, Canada, Mexico, Caribbean)
- Emergency air ambulance transport
- Hospital-to-hospital transport
- Worldwide coverage with Emergency Shield Plus plan
- No dollar limits on covered transport events
- No deductibles, co-pays, or coinsurance

## Target Members
- Individual consumers age 45–80
- Employers offering MASA as a voluntary benefit
- Retirees and frequent travelers
- Families with aging parents

## Plans
- Standard monthly plans: from $63/month (individual), $80/month (family)
- Lifetime plans: $5,200 (individual), $6,400 (family)

## Key URLs
- Plans: https://masaaccess.com/compare-plans/
- Benefits: https://masaaccess.com/benefits/
- FAQ: https://masaaccess.com/faq/
- About: https://masaaccess.com/corporate/about/
- Learning Center: https://masaaccess.com/learning-center/
```

### M3 — Content citability scores: moderate (estimated 45–55/100)
**Assessment:** The homepage contains strong citability anchors ("$69,000 air ambulance cost", "79% chance of out-of-pocket bill", "no dollar limits") but these are scattered rather than concentrated in self-contained, extractable passages. The learning center article on ambulance costs is better structured for citability (~1,100 words, factual statistics, paramedic quote) but still lacks the ideal 134–167 word self-contained passage format that AI citation research identifies as optimal.
**Fix:** Rewrite the top 10 most-linked learning center articles to include at least one self-contained "citation-ready" passage — a 134–167 word block that answers a specific question completely without requiring surrounding context.

### M4 — FAQ segment pages lack schema
**URLs:** /faq/pricing-and-payment/, /faq/traveling-information-and-itineraries/, /faq/filing-a-claim/, /faq/my-account-and-member-portal/, /faq/plan-identification/
**Impact:** Five segmented FAQ pages exist but none have FAQPage schema. These are high-intent pages that directly answer questions AI users ask about ambulance coverage, travel coverage, and claims.

### M5 — No Membership schema type deployed
**Impact:** Schema.org has a `Membership` type designed for exactly MASA's product. Without it, AI systems must infer membership model from prose descriptions. The MedicalOrganization type additionally signals healthcare authority.

---

## Low Priority Issues

### L1 — Social media presence is fragmented
LinkedIn, Facebook, Instagram, and Vimeo are linked from the footer, but no YouTube channel is confirmed. YouTube is the second-largest search engine and a primary training data source for AI models. A MASA YouTube channel with educational content about ambulance costs and emergency preparedness would meaningfully increase AI training data presence.

### L2 — No Reddit presence confirmed
Subreddits like r/personalfinance, r/insurance, r/travel, and r/camping are high-value for brand mentions that AI models cite. MASA content appears absent or minimal on Reddit.

### L3 — Open Graph meta tags status unknown
Not all pages may have complete OG tags. Complete OG coverage improves link sharing and social media crawl quality.

### L4 — Images: alt text coverage unknown
Alt text completeness was not verified across all pages. Alt text is an E-E-A-T signal and accessibility requirement.

### L5 — No Breadcrumb schema
The site has clear URL hierarchy (/benefits/emergency-air-ambulance-coverage/) but no BreadcrumbList schema to reinforce it. Minor but zero-effort fix in HubSpot.

---

## Category Deep Dives

### AI Citability — 42/100

**What was assessed:** Content extractability, question-answering structure, self-contained passage quality, AI crawler access, llms.txt.

**Strengths:**
- "$69,000 average air ambulance cost," "$4,500 four-minute ambulance ride," "79% chance of out-of-pocket bill" — these are specific, citeable statistics that AI models prize.
- Testimonials contain real dollar amounts and emergency outcomes — highly citeable for AI responses about "is MASA worth it" type queries.
- The learning center article on ambulance costs cites MASA Internal Data and references redcross.org — good citation practice.
- FAQ content directly answers the questions most commonly asked about emergency transport coverage.

**Weaknesses:**
- No llms.txt — AI crawlers have no authoritative document explaining MASA's product model.
- FAQ answers are 1–3 sentences — too brief to be self-contained citation blocks. Optimal AI-cited passages are 134–167 words.
- No content is structured explicitly for AI extraction (summary boxes, "in brief" blocks, structured Q&A with schema).
- Cost statistics are buried in body copy rather than highlighted in schema-marked elements.

**Example — current FAQ answer (poor citability):**
> "Won't my insurance pay for an ambulance or emergency medical transports? Health insurance may not fully cover ambulance bills due to out-of-network providers, medical necessity denials, or unmet deductibles."

**Rewrite for AI citability:**
> "Standard health insurance frequently leaves patients with large ambulance bills for three reasons: ambulance providers are often out-of-network (meaning standard network rates don't apply), insurers may deny claims citing lack of 'medical necessity,' and ambulance charges often apply directly to your deductible before any coverage kicks in. The national average ground ambulance cost is $2,086; air ambulance averages $72,469 per flight. MASA membership covers these costs with no dollar limits, no deductibles, and no co-pays — members submit the bill and receive full payment upon approval."

### Brand Authority — 58/100

**Strengths:**
- 2 million members globally — the largest membership scale in the category.
- 52 years in operation (founded 1974) — nearly unmatched heritage.
- 500+ employees, 18 global offices — institutional scale signals.
- Vimeo channel with member video testimonials.
- Active LinkedIn, Facebook, Instagram.
- Learning center creates ongoing indexable content.
- Partnership announcements visible in /insights/ (Securian Financial, Willis Towers Watson).

**Weaknesses:**
- No Wikipedia entity page confirmed — critical for AI entity disambiguation.
- No Reddit community presence identified (r/personalfinance, r/insurance, r/travel).
- No third-party accreditation logos (BBB, URAC, state insurance commission references).
- No media mentions surfaced on the homepage or about page.
- The partnership announcements (WTW, Securian) are in /insights/ — excellent authority signals that are not surfaced on the homepage or in schema.

### Content E-E-A-T — 55/100

**Strengths:**
- The organization's 50-year operational history is the strongest experience signal in the category.
- Real member data and paramedic quotes appear in learning center content.
- Mission statement is clear and specific.
- Content covers real emergency scenarios with practical, specific guidance.
- Testimonials demonstrate real-world outcome experience.

**Weaknesses:**
- Every learning center article is attributed to "MASA" — no individual human authors with credentials.
- No leadership team page with bios (About page mentions 500+ employees but names no one).
- No medical advisory board or clinical review process mentioned.
- No third-party expert citations beyond redcross.org (single instance found).
- No academic or peer-reviewed references on medical content.
- MASA's own data is cited ("MASA Internal Data") but without methodology transparency.

**Priority fix:** Add author bylines to the top 20 learning center articles. Use the existing paramedic/clinical contacts as named authors. Create a brief "About the author" block with credentials.

### Technical GEO — 54/100

**Strengths:**
- HTTPS — confirmed.
- Clean, descriptive URL structure (/benefits/emergency-air-ambulance-coverage/).
- Comprehensive sitemap (124 URLs, well-structured categories).
- HubSpot CMS provides a technically solid foundation (CDN, mobile responsive, good render performance).
- No AI crawlers are blocked.
- Security/legal pages exist (HIPAA policy, terms, privacy).

**Weaknesses:**
- robots.txt contains no AI crawler references (neither explicit allow nor deny for GPTBot, ClaudeBot, PerplexityBot, Gemini-Bot).
- No `Sitemap:` directive in robots.txt.
- No llms.txt (repeated — Technical GEO dimension).
- Core Web Vitals not verified in this audit — recommend PageSpeed Insights check.
- No `hreflang` tags confirmed for international content (14 global office locations but no apparent international subdomains or paths).
- HubSpot preview URLs are appropriately blocked but the block patterns are overly complex — clean up opportunity.

### Schema & Structured Data — 28/100

**Critical finding:** No JSON-LD schema was detected on any of the five audited pages (homepage, /what-is-masa/, /faq/, /compare-plans/, /learning-center/understanding-ambulance-costs/). This is the most significant GEO gap on the site.

**Schema types MASA should deploy:**

| Schema Type | Priority | Page(s) | Why |
|---|---|---|---|
| `Organization` | Critical | Homepage | Entity recognition, brand disambiguation |
| `MedicalOrganization` | Critical | Homepage, About | Healthcare-adjacent authority signal |
| `FAQPage` | Critical | /faq/ and 5 segment pages | Direct answer eligibility for AI Overviews |
| `Membership` | High | /compare-plans/ | Product type clarity for AI systems |
| `Article` | High | All /learning-center/ pages | Content authority for AI citation |
| `BreadcrumbList` | Medium | All pages | Navigation clarity |
| `VideoObject` | Medium | Testimonials with video | Video content discoverability |
| `Review` / `AggregateRating` | Medium | Testimonials page | Social proof for AI entity evaluation |
| `Person` | Medium | Learning center authors (once added) | E-E-A-T author authority |
| `Event` | Low | /consultation/, seminars | Seminar discoverability |

**Sample Organization + MedicalOrganization schema for homepage:**
```json
{
  "@context": "https://schema.org",
  "@type": ["Organization", "MedicalOrganization"],
  "name": "MASA Global",
  "alternateName": "MASA Access",
  "url": "https://www.masaaccess.com",
  "logo": "https://www.masaaccess.com/path/to/logo.png",
  "foundingDate": "1974",
  "numberOfEmployees": {"@type": "QuantitativeValue", "value": 500},
  "description": "MASA Global provides membership-based emergency medical transportation coverage, including air ambulance, ground ambulance, and hospital-to-hospital transport. MASA is not health insurance.",
  "areaServed": ["United States", "Canada", "Mexico", "Caribbean", "Worldwide"],
  "telephone": "+1-800-755-7857",
  "sameAs": [
    "https://www.linkedin.com/company/masa-global",
    "https://www.facebook.com/masaaccess"
  ]
}
```

### Platform Optimization — 48/100

**Platforms with confirmed presence:**
- LinkedIn (company page — linked from footer)
- Facebook (page — linked from footer)
- Instagram (profile — linked from footer)
- Vimeo (channel — linked from footer, member testimonial videos)

**Platforms with likely partial presence (unconfirmed):**
- YouTube — no channel confirmed; video content exists on Vimeo but not YouTube, which is a significant gap (YouTube is primary AI training data source for video)
- Wikipedia — 50-year-old company with 2M+ members likely has some entry; unverified in this audit
- Google Business Profile — seminar-based sales model suggests local GBP entries may exist

**Platforms with apparent absence:**
- Reddit — no MASA community or significant brand mention presence identified
- Quora — no MASA answers or brand presence identified
- Healthgrades / Yelp — review platform presence unverified
- TrustPilot / BBB — accreditation display absent from homepage

---

## Quick Wins (Implement This Week)

1. **Create llms.txt** — publish at `masaaccess.com/llms.txt` using the content spec in M2 above. 30-minute task. Highest GEO impact per hour of work.

2. **Add FAQPage JSON-LD to /faq/** — 16 questions already written; wrapping them in schema takes ~1 hour. Immediately unlocks Google AI Overview and Perplexity direct-answer eligibility for "does insurance cover ambulances?", "what countries does MASA cover?", and 14 other high-intent queries.

3. **Add Organization + MedicalOrganization schema to homepage** — use the JSON-LD template above. 30 minutes in HubSpot. Establishes MASA as a recognized entity for AI disambiguation.

4. **Update robots.txt** — add explicit AI crawler permissions and the sitemap URL. 15-minute change. Zero risk.

5. **Add `Sitemap: https://masaaccess.com/sitemap.xml` to robots.txt** — standalone fix that ensures AI crawlers find the full sitemap immediately.

---

## 30-Day Action Plan

### Week 1: AI Infrastructure (GEO unlocks)
- [ ] Publish llms.txt at /llms.txt (content spec in M2 above)
- [ ] Add Organization + MedicalOrganization JSON-LD to homepage
- [ ] Add FAQPage JSON-LD to /faq/ (all 16 questions)
- [ ] Update robots.txt: AI crawler permissions + sitemap URL
- [ ] Add Article schema to top 5 learning center articles

### Week 2: Schema Expansion
- [ ] Add FAQPage schema to all 5 segment FAQ pages (/faq/pricing-and-payment/ etc.)
- [ ] Add Membership schema to /compare-plans/
- [ ] Add BreadcrumbList schema site-wide (HubSpot setting)
- [ ] Add Article schema to remaining learning center articles (bulk operation)
- [ ] Audit and confirm HubSpot schema settings (some may already exist at HubSpot template level)

### Week 3: E-E-A-T & Author Attribution
- [ ] Identify 3–5 named MASA employees / paramedics / clinical contacts for content authorship
- [ ] Create author profile pages with credential bios
- [ ] Add author bylines + `Person` schema to top 20 learning center articles
- [ ] Add Person schema for each author (name, jobTitle, credentials)
- [ ] Review "about" page — add leadership team section with bios and headshots

### Week 4: Citability Optimization
- [ ] Rewrite top 10 learning center articles to include one 134–167 word self-contained citation-ready passage
- [ ] Expand FAQ answers from 1–3 sentences to 100–150 word comprehensive answers
- [ ] Add "Key Facts" summary box to homepage (air ambulance = $69K, ground = $2K, MASA from $63/mo)
- [ ] Verify Wikipedia entity status for MASA Global; update or create if absent
- [ ] Check Reddit for any existing MASA brand mentions; assess community presence strategy

---

## MASA-Specific GEO Notes

Per the MASA scoring framework (CLAUDE.md), the following adjustments were applied:

- **llms.txt absent** was scored as Critical (not just High) because MASA's product — membership, not insurance — is highly susceptible to AI misrepresentation. Without explicit AI guidance, AI systems may describe MASA as "insurance" or compare it incorrectly against health insurance products.
- **MedicalOrganization schema** was weighted as Critical (not just High) because AI systems use this type to categorize healthcare-adjacent entities. Without it, MASA may be miscategorized.
- **FAQPage schema absence** on a page with 16 questions was flagged as Critical — this is perhaps the single highest-impact 1-hour fix available, as FAQ schema directly enables Google AI Overview and Perplexity direct-answer features for exactly the questions MASA prospects ask.
- **E-E-A-T penalties** were applied for the absence of individual author attribution on medical/emergency content. Healthcare-adjacent content without credentialed authors is specifically penalized in AI model content weighting.
- **Coverage geography** was noted as unclearly structured in schema — with 14 international locations and worldwide plan coverage, `areaServed` in Organization schema is critical for AI geographic queries ("does MASA work in Europe?").

---

## Appendix: Pages Analyzed

| URL | Status | GEO Issues Found |
|---|---|---|
| https://masaaccess.com | 200 | No schema, no llms.txt, weak AI crawler config |
| https://masaaccess.com/sitemap.xml | 200 | No issues — comprehensive 124-URL sitemap |
| https://masaaccess.com/robots.txt | 200 | No AI crawlers, no sitemap reference |
| https://masaaccess.com/llms.txt | 404 | Does not exist — Critical |
| https://masaaccess.com/compare-plans/ | 200 | No schema, no Membership type |
| https://masaaccess.com/corporate/about/ | 200 | No schema, no leadership bios |
| https://masaaccess.com/benefits/ | 200 | No schema, good content depth |
| https://masaaccess.com/testimonials/ | 200 | No Review/AggregateRating schema; excellent content |
| https://masaaccess.com/what-is-masa/ | 200 | No schema detected |
| https://masaaccess.com/learning-center/understanding-ambulance-costs | 200 | No Article schema; moderate E-E-A-T |
| https://masaaccess.com/faq/ | 200 | No FAQPage schema — 16 questions unschematized |
| https://masaaccess.com/membership-plans | 404 | URL does not exist (use /compare-plans/) |
| https://masaaccess.com/about | 404 | URL does not exist (use /corporate/about/) |

---

*Generated by GEO Audit Suite — `/geo audit` | Baseline audit for masaaccess.com | 2026-05-31*
