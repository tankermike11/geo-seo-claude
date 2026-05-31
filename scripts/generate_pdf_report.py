#!/usr/bin/env python3
"""
GEO + SEO Audit Report PDF Generator
Generates MASA-branded, client-ready PDF reports for GEO and technical SEO audits.

Requires: reportlab (pip install reportlab)
"""

import sys
import json
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                     TableStyle, PageBreak, HRFlowable)
    from reportlab.graphics.shapes import Drawing, Rect, Circle, String
    from reportlab.graphics import renderPDF
except ImportError:
    print("Error: reportlab is required. Install with: pip install reportlab")
    sys.exit(1)


# MASA Global brand palette
COLORS = {
    "primary":    HexColor("#230871"),  # Horizon — headings, panels, CTAs
    "accent":     HexColor("#0071CE"),  # Tide — accent bars, buttons, highlights
    "highlight":  HexColor("#E64B38"),  # Flare — alerts, critical findings
    "success":    HexColor("#0071CE"),  # Tide for strong scores
    "warning":    HexColor("#FFD040"),  # Shine — caution scores
    "danger":     HexColor("#E64B38"),  # Flare — critical scores
    "light_bg":   HexColor("#E8E3E8"),  # Harbor tint — card fills, row alternation
    "text":       HexColor("#262626"),  # 85% black — body copy
    "text_light": HexColor("#968694"),  # Harbor — captions, secondary text
    "border":     HexColor("#E8E3E8"),  # Harbor tint — table borders, dividers
    "white":      white,
    "black":      black,
}


def score_color(score):
    if score >= 75:
        return COLORS["success"]
    elif score >= 50:
        return COLORS["warning"]
    else:
        return COLORS["danger"]


def draw_cover_header(width=510):
    """Horizon-colored header panel for cover page (MASA Layout B)."""
    t = Table([["MASA GLOBAL  |  GEO + SEO AUDIT REPORT"]], colWidths=[width], rowHeights=[56])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), COLORS["primary"]),
        ("TEXTCOLOR",     (0, 0), (-1, -1), COLORS["white"]),
        ("FONTNAME",      (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 13),
        ("ALIGN",         (0, 0), (-1, -1), "LEFT"),
        ("LEFTPADDING",   (0, 0), (-1, -1), 18),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
    ]))
    return t


def draw_section_bar(title, width=510):
    """Tide-colored section accent bar."""
    t = Table([[title]], colWidths=[width], rowHeights=[28])
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), COLORS["accent"]),
        ("TEXTCOLOR",     (0, 0), (-1, -1), COLORS["white"]),
        ("FONTNAME",      (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 11),
        ("LEFTPADDING",   (0, 0), (-1, -1), 12),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return t


def draw_score_gauge(score, size=80):
    """Circular score gauge."""
    d = Drawing(size + 20, size + 30)
    d.add(Circle(size / 2 + 10, size / 2 + 15, size / 2,
                 fillColor=COLORS["light_bg"], strokeColor=COLORS["border"], strokeWidth=2))
    inner_r = size / 2 - 8
    d.add(Circle(size / 2 + 10, size / 2 + 15, inner_r,
                 fillColor=score_color(score), strokeColor=None))
    d.add(Circle(size / 2 + 10, size / 2 + 15, inner_r - 10,
                 fillColor=COLORS["white"], strokeColor=None))
    d.add(String(size / 2 + 10, size / 2 + 10, str(int(score)),
                 fontSize=20, fillColor=COLORS["primary"],
                 textAnchor="middle", fontName="Helvetica-Bold"))
    return d


def create_bar_chart(categories, scores, width=450, height=180):
    """Horizontal bar chart using MASA palette."""
    d = Drawing(width, height)
    bar_height = 20
    gap = 8
    max_bar_width = width - 180
    start_y = height - 30
    label_x = 5
    bar_x = 160

    for i, (cat, score) in enumerate(zip(categories, scores)):
        y = start_y - i * (bar_height + gap)
        d.add(String(label_x, y + 5, cat[:22],
                     fontSize=9, fillColor=COLORS["text"],
                     textAnchor="start", fontName="Helvetica"))
        d.add(Rect(bar_x, y, max_bar_width, bar_height,
                   fillColor=COLORS["light_bg"], strokeColor=None))
        d.add(Rect(bar_x, y, (score / 100) * max_bar_width, bar_height,
                   fillColor=score_color(score), strokeColor=None))
        d.add(String(bar_x + max_bar_width + 10, y + 5, f"{int(score)}",
                     fontSize=10, fillColor=COLORS["text"],
                     textAnchor="start", fontName="Helvetica-Bold"))
    return d


def generate_report(data, output_path):
    """Generate a MASA-branded GEO + SEO audit PDF report."""
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=50, leftMargin=50,
        topMargin=50, bottomMargin=50
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "MASATitle", parent=styles["Title"],
        fontSize=26, textColor=COLORS["primary"],
        spaceAfter=6, fontName="Helvetica-Bold"
    )
    subtitle_style = ParagraphStyle(
        "MASASubtitle", parent=styles["Normal"],
        fontSize=13, textColor=COLORS["text_light"],
        spaceAfter=20, fontName="Helvetica"
    )
    heading_style = ParagraphStyle(
        "MASAHeading", parent=styles["Heading1"],
        fontSize=16, textColor=COLORS["primary"],
        spaceBefore=16, spaceAfter=8, fontName="Helvetica-Bold"
    )
    subheading_style = ParagraphStyle(
        "MASASubheading", parent=styles["Heading2"],
        fontSize=12, textColor=COLORS["accent"],
        spaceBefore=12, spaceAfter=6, fontName="Helvetica-Bold"
    )
    body_style = ParagraphStyle(
        "MASABody", parent=styles["Normal"],
        fontSize=10, textColor=COLORS["text"],
        spaceAfter=6, fontName="Helvetica", leading=14
    )
    footer_style = ParagraphStyle(
        "MASAFooter", parent=styles["Normal"],
        fontSize=8, textColor=COLORS["text_light"], fontName="Helvetica"
    )

    elements = []
    url = data.get("url", "masaaccess.com")
    date_str = data.get("date", datetime.now().strftime("%B %d, %Y"))

    # === COVER PAGE ===
    elements.append(draw_cover_header())
    elements.append(Spacer(1, 0.8 * inch))
    elements.append(Paragraph("GEO + SEO Audit Report", title_style))
    elements.append(Paragraph(url, subtitle_style))
    elements.append(Paragraph(f"Prepared: {date_str}", subtitle_style))
    elements.append(Spacer(1, 0.5 * inch))

    overall_score = data.get("overall_score", 0)
    elements.append(draw_score_gauge(overall_score, size=100))
    elements.append(Spacer(1, 0.3 * inch))

    grade = "A+" if overall_score >= 90 else "A" if overall_score >= 80 else "B" if overall_score >= 70 else "C" if overall_score >= 60 else "D" if overall_score >= 50 else "F"
    elements.append(Paragraph(f"Overall GEO Score: {int(overall_score)}/100 (Grade: {grade})", heading_style))

    exec_summary = data.get("executive_summary", (
        "This GEO + SEO audit evaluates AI visibility, brand authority, content quality, "
        "technical foundations, and structured data — the five dimensions that determine whether "
        "AI systems and search engines discover, understand, and cite this site."
    ))
    elements.append(Paragraph(exec_summary, body_style))

    elements.append(Spacer(1, 1.2 * inch))
    elements.append(HRFlowable(width="100%", thickness=1, color=COLORS["accent"]))
    elements.append(Spacer(1, 0.1 * inch))
    elements.append(Paragraph(
        f"Prepared for MASA Global  |  masaaccess.com  |  {date_str}", footer_style
    ))
    elements.append(PageBreak())

    # === SCORE BREAKDOWN ===
    elements.append(draw_section_bar("Score Breakdown"))
    elements.append(Spacer(1, 0.2 * inch))

    categories = data.get("categories", {})
    cat_names = list(categories.keys()) if categories else [
        "AI Citability & Visibility", "Brand Authority Signals",
        "Content Quality & E-E-A-T", "Technical Foundations", "Structured Data"
    ]
    cat_scores = [categories.get(c, {}).get("score", 50) for c in cat_names] if categories else [55, 60, 65, 70, 45]

    elements.append(create_bar_chart(cat_names, cat_scores))
    elements.append(Spacer(1, 0.3 * inch))

    score_data = [["Category", "Score", "Weight", "Status"]]
    weights = ["20%", "15%", "10%", "10%", "5%"]
    for i, (name, score) in enumerate(zip(cat_names, cat_scores)):
        status = "Strong" if score >= 75 else "Needs Work" if score >= 50 else "Critical"
        score_data.append([name, f"{int(score)}/100", weights[i] if i < len(weights) else "—", status])

    score_table = Table(score_data, colWidths=[200, 65, 55, 90])
    score_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  COLORS["primary"]),
        ("TEXTCOLOR",     (0, 0), (-1, 0),  COLORS["white"]),
        ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("ALIGN",         (1, 0), (-1, -1), "CENTER"),
        ("GRID",          (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    elements.append(score_table)
    elements.append(PageBreak())

    # === KEY FINDINGS ===
    elements.append(draw_section_bar("Key Findings"))
    elements.append(Spacer(1, 0.2 * inch))

    findings = data.get("findings", [
        {"severity": "Critical", "finding": "No llms.txt file — AI crawlers cannot understand the membership model or coverage scope"},
        {"severity": "High",     "finding": "MedicalOrganization and Membership schema types absent — structured data gap for AI and search"},
        {"severity": "High",     "finding": "E-E-A-T signals weak — no authored content from credentialed medical or insurance professionals"},
        {"severity": "Medium",   "finding": "Content passages lack self-containment and specificity preferred by AI citation models"},
        {"severity": "Medium",   "finding": "Coverage geography not in structured data — international members can't confirm via AI"},
        {"severity": "Low",      "finding": "robots.txt does not explicitly permit GPTBot, ClaudeBot, or PerplexityBot"},
    ])

    findings_data = [["Severity", "Finding"]]
    for f in findings:
        findings_data.append([f.get("severity", "Medium"), Paragraph(f.get("finding", ""), body_style)])

    severity_colors = {
        "Critical": COLORS["danger"],
        "High":     COLORS["highlight"],
        "Medium":   COLORS["warning"],
        "Low":      COLORS["accent"],
    }
    table_cmds = [
        ("BACKGROUND",    (0, 0), (-1, 0),  COLORS["primary"]),
        ("TEXTCOLOR",     (0, 0), (-1, 0),  COLORS["white"]),
        ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("GRID",          (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("ALIGN",         (0, 0), (0, -1),  "CENTER"),
    ]
    for i, f in enumerate(findings, 1):
        c = severity_colors.get(f.get("severity", "Medium"), COLORS["warning"])
        table_cmds += [("TEXTCOLOR", (0, i), (0, i), c), ("FONTNAME", (0, i), (0, i), "Helvetica-Bold")]

    findings_table = Table(findings_data, colWidths=[70, 400])
    findings_table.setStyle(TableStyle(table_cmds))
    elements.append(findings_table)
    elements.append(PageBreak())

    # === ACTION PLAN ===
    elements.append(draw_section_bar("Prioritized Action Plan"))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph("[QUICK WIN] Quick Wins — This Week", subheading_style))
    for i, win in enumerate(data.get("quick_wins", [
        "Create and publish llms.txt describing membership model, coverage scope, and target audiences",
        "Add Organization and FAQPage schema to the homepage",
        "Update robots.txt to explicitly permit GPTBot, ClaudeBot, PerplexityBot, Googlebot-Extended",
        "Add author bylines with credentials to all informational content pages",
    ]), 1):
        elements.append(Paragraph(f"{i}. {win}", body_style))

    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("[MEDIUM TERM] Medium-Term — 1–4 Weeks", subheading_style))
    for i, action in enumerate(data.get("medium_term", [
        "Implement MedicalOrganization and Membership schema types site-wide",
        "Rewrite key content passages to be self-contained and citation-ready (134–167 word target)",
        "Build coverage geography FAQ page with structured data markup",
        "Add E-E-A-T author profiles: medical director, claims specialists, compliance team",
    ]), 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("[STRATEGIC] Strategic — 1–3 Months", subheading_style))
    for i, action in enumerate(data.get("strategic", [
        "Build GEO content hub: pillar pages on air ambulance cost, coverage gaps, emergency travel planning",
        "Monitor AI citation share across ChatGPT, Perplexity, Claude, and Gemini monthly",
        "Develop employer/HR landing page with schema and llms.txt entry",
        "Commission third-party trust signals: accreditation badges, BBB rating, media mentions",
    ]), 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(PageBreak())

    # === METHODOLOGY ===
    elements.append(draw_section_bar("Methodology"))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph(
        "This audit evaluates five GEO dimensions that determine AI discoverability and citation readiness. "
        "Each dimension is scored 0–100 against current AI and search engine best practices.",
        body_style
    ))

    method_data = [
        ["Dimension", "Weight", "What We Measure"],
        ["AI Citability & Visibility", "20%", "Citation-ready content, AI crawler access, llms.txt presence"],
        ["Brand Authority Signals",    "15%", "Mentions, backlinks, E-E-A-T, third-party trust signals"],
        ["Content Quality & E-E-A-T",  "10%", "Author credentials, factual density, content depth"],
        ["Technical Foundations",      "10%", "Core Web Vitals, crawlability, robots.txt, sitemaps"],
        ["Structured Data",            "5%",  "Schema.org coverage, MedicalOrganization, FAQPage, Membership"],
    ]
    method_table = Table(method_data, colWidths=[170, 50, 290])
    method_table.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0),  COLORS["primary"]),
        ("TEXTCOLOR",     (0, 0), (-1, 0),  COLORS["white"]),
        ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("GRID",          (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    elements.append(method_table)

    elements.append(Spacer(1, 0.5 * inch))
    elements.append(HRFlowable(width="100%", thickness=1, color=COLORS["accent"]))
    elements.append(Spacer(1, 0.1 * inch))
    elements.append(Paragraph(
        f"Prepared for MASA Global  |  masaaccess.com  |  {date_str}", footer_style
    ))

    doc.build(elements)
    return output_path


def main():
    if len(sys.argv) < 2:
        sample_data = {
            "url": "https://www.masaaccess.com",
            "date": datetime.now().strftime("%B %d, %Y"),
            "overall_score": 58,
            "executive_summary": (
                "This GEO + SEO audit of masaaccess.com reveals significant opportunities to improve "
                "AI visibility and citation readiness. The site lacks llms.txt, key schema types, and "
                "E-E-A-T signals that would help AI systems understand and recommend MASA's emergency "
                "medical transportation coverage to prospective members."
            ),
            "categories": {
                "AI Citability & Visibility": {"score": 45, "weight": "20%"},
                "Brand Authority Signals":    {"score": 62, "weight": "15%"},
                "Content Quality & E-E-A-T":  {"score": 58, "weight": "10%"},
                "Technical Foundations":      {"score": 71, "weight": "10%"},
                "Structured Data":            {"score": 38, "weight": "5%"},
            },
        }
        output = "GEO-REPORT-sample.pdf"
        generate_report(sample_data, output)
        print(f"Sample report generated: {output}")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "GEO-REPORT.pdf"
    with open(input_file, "r") as f:
        data = json.load(f)
    generate_report(data, output_file)
    print(f"Report generated: {output_file}")


if __name__ == "__main__":
    main()
