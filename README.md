<p align="center">
  <img src="assets/banner.svg" alt="GEO-SEO + AI Marketing Suite for Claude Code" width="900"/>
</p>

<p align="center">
  <strong>GEO-first SEO · AI Marketing Automation — unified in one Claude Code toolkit.</strong><br/>
  Optimize for AI search engines. Audit any website's marketing. Generate copy, emails, social content, and client-ready PDF reports — all from your terminal.
</p>

---

## Why This Suite (2026)

| Metric | Value |
|--------|-------|
| GEO services market | $850M+ (projected $7.3B by 2031) |
| AI-referred traffic growth | +527% year-over-year |
| AI traffic conversion rate vs organic | 4.4x higher |
| Gartner: search traffic drop by 2028 | -50% |
| Brand mentions vs backlinks for AI | 3x stronger correlation |
| Marketers investing in GEO | Only 23% |

---

## Quick Start

### One-Command Install (macOS/Linux)

```bash
git clone https://github.com/zubair-trabzada/geo-seo-claude.git
cd geo-seo-claude
./install.sh
```

### Windows (Git Bash)

Requires [Git for Windows](https://git-scm.com/downloads) which includes Git Bash.

```bash
git clone https://github.com/zubair-trabzada/geo-seo-claude.git
cd geo-seo-claude
./install-win.sh
```

> **Note:** Right-click the folder and select "Open Git Bash here". Do not use PowerShell or Command Prompt.

### Requirements

- Python 3.8+ (on Debian/Ubuntu also `python3-venv`)
- Claude Code CLI
- Git
- Optional: [`uv`](https://docs.astral.sh/uv/) — faster dependency install
- Optional: Playwright (for screenshots)
- Optional: `pip install reportlab` — for PDF reports

### Isolated install

GEO Python dependencies are installed into `~/.claude/skills/geo/.venv/`. Your system Python is not touched. Marketing skills use stdlib with optional `reportlab` for PDFs.

---

## Commands

### GEO-SEO Suite (`/geo`)

| Command | What It Does |
|---------|-------------|
| `/geo audit <url>` | Full GEO + SEO audit with parallel subagents |
| `/geo quick <url>` | 60-second GEO visibility snapshot |
| `/geo citability <url>` | Score content for AI citation readiness |
| `/geo crawlers <url>` | Check AI crawler access (robots.txt) |
| `/geo llmstxt <url>` | Analyze or generate llms.txt |
| `/geo brands <url>` | Scan brand mentions across AI-cited platforms |
| `/geo platforms <url>` | Platform-specific optimization |
| `/geo schema <url>` | Structured data analysis & generation |
| `/geo technical <url>` | Technical SEO audit |
| `/geo content <url>` | Content quality & E-E-A-T assessment |
| `/geo report <url>` | Generate client-ready GEO report |
| `/geo report-pdf` | Generate professional PDF report with charts & visualizations |

### AI Marketing Suite (`/market`)

| Command | What It Does |
|---------|-------------|
| `/market audit <url>` | Full marketing audit with 5 parallel agents |
| `/market quick <url>` | 60-second marketing snapshot |
| `/market copy <url>` | Generate optimized copy with before/after examples |
| `/market emails <topic>` | Generate complete email sequences |
| `/market social <topic>` | 30-day social media content calendar |
| `/market ads <url>` | Ad creative and copy for all platforms |
| `/market funnel <url>` | Sales funnel analysis and optimization |
| `/market competitors <url>` | Competitive intelligence report |
| `/market landing <url>` | Landing page CRO analysis |
| `/market launch <product>` | Product launch playbook |
| `/market proposal <client>` | Client proposal generator |
| `/market report <url>` | Full marketing report (Markdown) |
| `/market report-pdf <url>` | Professional marketing report (PDF) |
| `/market seo <url>` | SEO content audit |
| `/market brand <url>` | Brand voice analysis and guidelines |

---

## Architecture

```
geo-seo-claude/
│
├── geo/                          # GEO skill orchestrator
│   └── SKILL.md
├── market/                       # Marketing skill orchestrator
│   ├── SKILL.md
│   ├── scripts/                  # analyze_page.py, competitor_scanner.py, etc.
│   └── templates/                # Email, proposal, calendar templates
│
├── skills/                       # All sub-skills
│   ├── geo-audit/                # Full GEO audit orchestration & scoring
│   ├── geo-citability/           # AI citation readiness scoring
│   ├── geo-crawlers/             # AI crawler access analysis
│   ├── geo-llmstxt/              # llms.txt analysis & generation
│   ├── geo-brand-mentions/       # Brand presence on AI-cited platforms
│   ├── geo-platform-optimizer/   # Platform-specific AI search optimization
│   ├── geo-schema/               # Structured data for AI discoverability
│   ├── geo-technical/            # Technical SEO foundations
│   ├── geo-content/              # Content quality & E-E-A-T
│   ├── geo-report/               # Client-ready GEO report generation
│   ├── geo-report-pdf/           # Professional PDF report with charts
│   ├── geo-prospect/             # CRM-lite prospect pipeline
│   ├── geo-proposal/             # Auto-generate client proposals
│   ├── geo-compare/              # Monthly delta tracking
│   ├── market-audit/             # Marketing audit orchestration
│   ├── market-copy/              # Copywriting analysis & generation
│   ├── market-emails/            # Email sequence generation
│   ├── market-social/            # Social media content calendar
│   ├── market-ads/               # Ad creative & copy
│   ├── market-funnel/            # Funnel analysis & optimization
│   ├── market-competitors/       # Competitive intelligence
│   ├── market-landing/           # Landing page CRO
│   ├── market-launch/            # Launch playbook generation
│   ├── market-proposal/          # Client proposal generator
│   ├── market-report/            # Marketing report (Markdown)
│   ├── market-report-pdf/        # Marketing report (PDF)
│   ├── market-seo/               # SEO content audit
│   └── market-brand/             # Brand voice analysis
│
├── agents/                       # Parallel subagents
│   ├── geo-ai-visibility.md
│   ├── geo-platform-analysis.md
│   ├── geo-technical.md
│   ├── geo-content.md
│   ├── geo-schema.md
│   ├── market-content.md
│   ├── market-conversion.md
│   ├── market-competitive.md
│   ├── market-technical.md
│   └── market-strategy.md
│
├── scripts/                      # GEO Python utilities
│   ├── fetch_page.py
│   ├── citability_scorer.py
│   ├── brand_scanner.py
│   ├── llmstxt_generator.py
│   └── generate_pdf_report.py
│
├── schema/                       # JSON-LD templates
│   ├── organization.json
│   ├── local-business.json
│   ├── article-author.json
│   ├── software-saas.json
│   ├── product-ecommerce.json
│   └── website-searchaction.json
│
├── install.sh                    # Unified installer
├── uninstall.sh                  # Unified uninstaller
├── requirements.txt              # Python dependencies
└── README.md
```

---

## GEO Scoring Methodology

| Category | Weight |
|----------|--------|
| AI Citability & Visibility | 25% |
| Brand Authority Signals | 20% |
| Content Quality & E-E-A-T | 20% |
| Technical Foundations | 15% |
| Structured Data | 10% |
| Platform Optimization | 10% |

## Marketing Scoring Methodology

| Category | Weight | What It Measures |
|----------|--------|------------------|
| Content & Messaging | 25% | Copy quality, value props, headlines, CTAs |
| Conversion Optimization | 20% | Funnels, forms, social proof, friction, urgency |
| SEO & Discoverability | 20% | On-page SEO, technical SEO, content structure |
| Competitive Positioning | 15% | Differentiation, market awareness, alternatives |
| Brand & Trust | 10% | Design quality, trust signals, authority |
| Growth & Strategy | 10% | Pricing, acquisition channels, retention |

---

## How It Works

Both suites follow the same pattern:

1. **You type a command** — e.g., `/geo audit https://example.com` or `/market audit https://example.com`
2. **Claude reads the skill files** — they define exactly how to analyze the site
3. **5 subagents launch in parallel** — each analyzes a different dimension
4. **Python scripts run** — automated page fetching, scoring, competitor scanning
5. **Results are compiled** — into a scored, prioritized, actionable report
6. **Output is saved** — as a Markdown file or professional PDF

---

## Key Features

### GEO-SEO
- **Citability Scoring** — Optimal AI-cited passages are 134-167 words, self-contained, fact-rich
- **AI Crawler Analysis** — Checks robots.txt for 14+ AI crawlers (GPTBot, ClaudeBot, PerplexityBot, etc.)
- **Brand Mention Scanning** — Scans YouTube, Reddit, Wikipedia, LinkedIn, and 7+ platforms
- **llms.txt Generation** — Generates the emerging llms.txt standard file
- **Platform-Specific Optimization** — Tailored recommendations per AI search platform

### Marketing
- **Full Audit** — 5 parallel agents score messaging, CRO, SEO, competitive position, brand, and growth strategy
- **Copy Generation** — Before/after rewrites with rationale
- **Email Sequences** — Welcome, nurture, and launch sequences
- **Social Calendars** — 30-day content calendars
- **Client-Ready PDFs** — Score gauges, bar charts, color-coded tables, prioritized action plans

---

## Data Storage

GEO prospect/CRM data is stored outside Claude Code at:

```
~/.geo-prospects/
├── prospects.json
├── proposals/
└── reports/
```

This directory is **not removed** by the uninstaller — delete it manually if needed.

---

## Use Cases

- **GEO Agencies** — Run audits, generate deliverables, track clients
- **Marketing Agencies** — Audit prospects before sales calls, deliver PDF reports
- **Marketing Teams** — Monitor AI search visibility and marketing performance
- **Solopreneurs** — Optimize landing pages, generate email sequences and social calendars
- **Content Creators** — Optimize for AI citations, plan launches, analyze funnels
- **Local Businesses** — Get found by AI assistants, improve brand mentions

---

## Uninstall

```bash
./uninstall.sh
```

Or manually:
```bash
rm -rf ~/.claude/skills/geo ~/.claude/skills/geo-* ~/.claude/agents/geo-*.md
rm -rf ~/.claude/skills/market ~/.claude/skills/market-* ~/.claude/agents/market-*.md
```

---

## Want to Turn This Into a Business?

**[Join the AI Workshop Community →](https://skool.com/aiworkshop)**

- Video walkthroughs — setup, running audits, reading results
- Client acquisition playbook — find prospects, pitch services, close deals
- Live office hours
- Agency pricing & proposal templates

GEO agencies charge $2K–$12K/month. Marketing audits add another revenue stream. These tools do the work. The community teaches you how to sell it.

---

## License

MIT License

---

## Contributing

Contributions welcome!

---

Built for the AI search era.
