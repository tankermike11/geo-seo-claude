# CLAUDE.md — Unified Site Performance Intelligence Suite
# Project: masaaccess.com GEO + SEO + Marketing Analysis Platform

---

## Project Purpose

This project merges two open-source Claude Code skill repositories into a single, unified site performance intelligence system tailored for **MASA Global / MASA Access** (masaaccess.com).

**Source repos:**
- `geo-seo-claude` — GEO + technical SEO analysis (primary foundation)
- `ai-marketing-claude` — Marketing copy, funnel, email, social, and competitive analysis

The goal is a unified `/site audit <url>` command that produces one composite report
covering GEO visibility, traditional SEO, and marketing performance — with MASA-specific
scoring lenses and branded output.

---

## Current Project State

### Repo Structure (after merge)

```
/
├── CLAUDE.md                   ← You are here
├── geo/                        ← GEO orchestrator skill (from geo-seo-claude)
├── market/                     ← Marketing orchestrator skill (from ai-marketing-claude)
├── site/                       ← NEW: unified /site command (to be built)
├── skills/
│   ├── geo-*/                  ← 13 GEO sub-skills
│   └── market-*/               ← 14 marketing sub-skills
├── agents/
│   ├── geo-*.md                ← 5 GEO subagents
│   └── market-*.md             ← 5 marketing subagents
├── scripts/
│   ├── fetch_page.py
│   ├── citability_scorer.py
│   ├── brand_scanner.py
│   ├── llmstxt_generator.py
│   ├── generate_pdf_report.py
│   ├── analyze_page.py
│   ├── competitor_scanner.py
│   ├── social_calendar.py
│   └── generate_marketing_pdf.py
├── templates/
├── schema/
├── tests/
├── requirements.txt
└── install.sh
```

### What Has Been Done
- [ ] Forked both repos into single workspace ← **START HERE if not yet done**
- [ ] Installed and ran `/geo audit https://www.masaaccess.com` baseline
- [ ] Installed and ran `/market audit https://www.masaaccess.com` baseline
- [ ] Reviewed baseline reports and catalogued scoring gaps

### Active Workstreams (in priority order)
1. **Merge & unify** — single install, single command namespace, no conflicts
2. **MASA-specific tuning** — adjust scoring weights and analysis lenses for MASA's business model
3. **Build `/site audit`** — unified command that orchestrates both skill sets
4. **Improve Python scripts** — error handling, retry logic, test coverage
5. **Brand the reports** — MASA-styled PDF output

---

## About MASA Global

### What MASA Is
MASA Global (masaaccess.com) sells **membership-based emergency medical transportation coverage**.
Core products: air ambulance, ground ambulance transport, extended hospital stay coverage.
B2C and employer/group B2B2C. Membership model (recurring revenue, not claims-based insurance).

### Business Model Implications for Site Analysis
When analyzing masaaccess.com, weight these factors more heavily than generic tools do:

| Factor | Why It Matters for MASA |
|--------|-------------------------|
| Trust & credibility signals | People buy emergency transport coverage from brands they trust with their lives |
| Compliance language clarity | Healthcare-adjacent; must appear legitimate, not aggressive |
| Value prop clarity | "Air ambulance costs $30K–$100K" is the core fear — site must make the ROI obvious |
| Member journey conversion | Homepage → understand benefit → see coverage → join. Friction kills conversion. |
| Employer/HR decision-maker path | B2B2C track is distinct from individual consumer track |
| Geographic coverage clarity | Members travel internationally; coverage geography must be findable |
| Membership vs insurance framing | MASA is NOT insurance — language matters for compliance and clarity |
| Urgency without fear-mongering | Emergency context requires sensitivity — the tone must reassure, not frighten |

### Target Audiences
1. **Individual members** — 45–70, travel-conscious, health-aware, value peace of mind
2. **Employer HR/Benefits managers** — evaluating group membership as an employee benefit
3. **Existing members** — need renewal, usage, and claims support information

### Competitive Landscape
Primary competitors: AirMedCare Network, MASA (itself a legacy brand), Global Rescue, Medjet.
Frame competitive analysis through coverage breadth, pricing transparency, and trust signals.

### MASA Brand System
Brand colors (use in all generated reports and outputs):
- **Horizon** `#230871` — primary dark (navy/purple); headings, panels, CTAs
- **Tide** `#0071CE` — electric blue; accents, buttons, highlights
- **Flare** `#E64B38` — alert red; urgent CTAs, warnings (use sparingly)
- **Shine** `#FFD040` — gold; achievements, highlights (use sparingly)
- **Harbor** `#968694` — muted gray; secondary text, dividers
- **Harbor tint** `#E8E3E8` — light bg; card fills, table rows

Fonts: **Poppins** (headings/CTAs, Bold 700 / SemiBold 600) + **Open Sans** (body, Regular 400)

---

## Unified Command Design

### Target: `/site audit <url>`

When implemented, this command should:

1. Run all 10 parallel subagents (5 GEO + 5 marketing) simultaneously
2. Produce a **composite Site Performance Score** (0–100) from both scoring models
3. Output a single unified report with four sections:
   - Executive Summary (composite score, top 3 wins, top 3 critical gaps)
   - GEO & Technical (AI visibility, crawlers, schema, E-E-A-T)
   - Marketing Performance (messaging, conversion, competitive position)
   - Prioritized Action Plan (quick wins < 1 week, medium-term 1–4 weeks, strategic 1–3 months)

### Proposed Composite Scoring Model

| Dimension | Source | Weight |
|-----------|--------|--------|
| AI Citability & Visibility | GEO | 20% |
| Brand Authority Signals | GEO | 15% |
| Content Quality & E-E-A-T | GEO | 10% |
| Technical Foundations | GEO | 10% |
| Structured Data | GEO | 5% |
| Content & Messaging | Marketing | 15% |
| Conversion Optimization | Marketing | 10% |
| Competitive Positioning | Marketing | 10% |
| Brand & Trust | Marketing | 5% |
| **TOTAL** | | **100%** |

---

## MASA-Specific Scoring Adjustments

Apply these adjustments when analyzing masaaccess.com specifically
(or any healthcare-adjacent membership company):

### Boost Weight For:
- **Social proof with specificity** — member testimonials with real emergency stories score higher than generic reviews
- **Pricing transparency** — clear cost of membership and clear contrast to uninsured transport costs
- **Coverage geography** — is it findable without 3 clicks?
- **Mobile-first navigation** — members may need the site in an actual emergency
- **Trust badge prominence** — accreditations, BBB, partner logos above the fold
- **E-E-A-T depth** — authored content from credentialed sources (medical directors, insurance experts)

### Penalize More Heavily For:
- **Ambiguous membership vs insurance language** — compliance risk
- **Fear-based CTAs without reassurance** — "You could die without this" without warm framing damages trust
- **Buried pricing or coverage limitations** — creates distrust
- **No employer/HR landing page** — B2B2C channel is under-leveraged without it
- **llms.txt absent** — AI crawlers won't understand the membership model without explicit guidance
- **Schema gaps** — Organization, MedicalOrganization, and FAQPage schemas are critical

---

## Python Script Standards

All scripts in `/scripts/` must meet these standards before shipping:

### Error Handling
```python
# Always wrap network calls:
try:
    response = requests.get(url, timeout=15, headers=HEADERS)
    response.raise_for_status()
except requests.exceptions.Timeout:
    logger.warning(f"Timeout fetching {url} — returning partial result")
    return {"error": "timeout", "url": url}
except requests.exceptions.HTTPError as e:
    logger.error(f"HTTP {e.response.status_code} for {url}")
    return {"error": f"http_{e.response.status_code}", "url": url}
```

### Output Contract
Every script must return a dict with at minimum:
```python
{
    "url": str,
    "timestamp": str,   # ISO 8601
    "success": bool,
    "score": int | None,  # 0–100, None if unable to score
    "findings": list[str],
    "recommendations": list[str],
    "error": str | None
}
```

### Test Coverage
Every script must have a corresponding test in `/tests/` using pytest.
Test with at minimum: masaaccess.com, a competitor (airmedcarenetwork.com), and a malformed URL.

---

## Report Output Requirements

### Markdown Reports
- Section hierarchy: H1 title → H2 dimensions → H3 sub-findings
- Score display: emoji traffic light (🔴 < 50, 🟡 50–74, 🟢 75+) next to every scored dimension
- Action items must be tagged: `[QUICK WIN]`, `[MEDIUM TERM]`, or `[STRATEGIC]`
- Always include a "MASA-Specific Observations" section with membership-model-specific findings

### PDF Reports
- MASA branded: Horizon `#230871` header panel, Tide `#0071CE` accent bars
- Font: Poppins for headings (embed or substitute Helvetica-Bold), Open Sans for body
- Must include: score gauge visualization, dimension bar chart, color-coded priority table
- Footer: "Prepared for MASA Global | masaaccess.com | [date]"
- Target: client-ready without post-processing

---

## Session Protocols

### Starting a New Session
At the start of each Claude Code session, run:
```
Read CLAUDE.md, then list the current state of each active workstream.
```

### Before Editing Any Skill File
1. Read the existing SKILL.md fully
2. Note what the skill currently does, inputs, and outputs
3. Make changes incrementally — do not rewrite from scratch unless the file is fundamentally broken
4. Test the changed skill against masaaccess.com before committing

### Before Editing Any Python Script
1. Run the existing script against masaaccess.com and capture current output
2. Make changes
3. Run again and diff the output
4. Run `/tests/` to confirm no regressions

### Committing Changes
Commit messages follow: `[scope] brief description`
Scopes: `geo`, `market`, `site`, `scripts`, `tests`, `reports`, `docs`
Example: `[site] add unified /site audit orchestrator skill`

---

## Known Issues and Tech Debt

Track discovered issues here as you work:

| Issue | Location | Priority | Status |
|-------|----------|----------|--------|
| `ai-marketing-claude` Python scripts have no error handling | `/scripts/analyze_page.py` etc. | High | Open |
| No unified install.sh for merged repo | `/install.sh` | High | Open |
| PDF reports use plain ReportLab styling — not MASA branded | `/scripts/generate_pdf_report.py` | Medium | Open |
| No test suite for `ai-marketing-claude` scripts | `/tests/` | Medium | Open |
| `/geo prospect` data stored in `~/.geo-prospects/` — no masaaccess.com pipeline seeded | `~/.geo-prospects/` | Low | Open |
| Schema templates are generic — need MedicalOrganization and Membership types | `/schema/` | Medium | Open |

---

## Useful Reference Commands

```bash
# Run GEO audit on MASA
/geo audit https://www.masaaccess.com

# Run marketing audit on MASA
/market audit https://www.masaaccess.com

# Run quick GEO snapshot
/geo quick https://www.masaaccess.com

# Check AI crawler access
/geo crawlers https://www.masaaccess.com

# Generate llms.txt
/geo llmstxt https://www.masaaccess.com

# Run a competitor comparison
/geo audit https://www.airmedcarenetwork.com
/market competitors https://www.masaaccess.com

# Test a specific Python script
python3 scripts/citability_scorer.py --url https://www.masaaccess.com
python3 scripts/analyze_page.py --url https://www.masaaccess.com

# Run tests
pytest tests/ -v
```

---

## Next Actions (in order)

- [ ] 1. Fork both repos; create single working directory
- [ ] 2. Run baseline audits on masaaccess.com from both tools; save raw outputs to `/examples/masa-baseline/`
- [ ] 3. Create `/site/SKILL.md` — unified command router that calls both orchestrators
- [ ] 4. Merge `install.sh` scripts into one
- [ ] 5. Add MASA-specific scoring adjustments to GEO audit sub-skill
- [ ] 6. Add `MedicalOrganization` and `Membership` schema templates to `/schema/`
- [ ] 7. Harden Python scripts with error handling (start with `analyze_page.py` and `citability_scorer.py`)
- [ ] 8. Add pytest tests for all scripts
- [ ] 9. Rebrand PDF reports with MASA color system
- [ ] 10. Run final unified `/site audit masaaccess.com` and compare to baseline

---

*Last updated: May 2026 | Maintained by: Mike @ MASA Global*
