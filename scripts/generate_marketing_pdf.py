#!/usr/bin/env python3
"""
Marketing Audit Report PDF Generator
Generates MASA-branded, client-ready PDF marketing reports with charts,
score visualizations, and prioritized action plans.

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
    "highlight":  HexColor("#E64B38"),  # Flare — alerts, high-severity findings
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
    t = Table([["MASA GLOBAL  |  MARKETING AUDIT REPORT"]], colWidths=[width], rowHeights=[56])
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
    """Circular score gauge using MASA colors."""
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
    """Generate a MASA-branded marketing audit PDF report."""
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
    elements.append(Paragraph("Marketing Audit Report", title_style))
    elements.append(Paragraph(url, subtitle_style))
    elements.append(Paragraph(f"Prepared: {date_str}", subtitle_style))
    elements.append(Spacer(1, 0.5 * inch))

    overall_score = data.get("overall_score", 0)
    elements.append(draw_score_gauge(overall_score, size=100))
    elements.append(Spacer(1, 0.3 * inch))

    grade = "A+" if overall_score >= 90 else "A" if overall_score >= 80 else "B" if overall_score >= 70 else "C" if overall_score >= 60 else "D" if overall_score >= 50 else "F"
    elements.append(Paragraph(f"Overall Marketing Score: {int(overall_score)}/100 (Grade: {grade})", heading_style))

    exec_summary = data.get("executive_summary", (
        "This report provides a comprehensive analysis of the website's marketing effectiveness "
        "across content, conversion, SEO, competitive positioning, brand trust, and growth strategy."
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
        "Content & Messaging", "Conversion Optimization", "SEO & Discoverability",
        "Competitive Positioning", "Brand & Trust", "Growth & Strategy"
    ]
    cat_scores = [categories.get(c, {}).get("score", 50) for c in cat_names] if categories else [65, 58, 72, 55, 68, 60]

    elements.append(create_bar_chart(cat_names, cat_scores))
    elements.append(Spacer(1, 0.3 * inch))

    score_data = [["Category", "Score", "Weight", "Status"]]
    weights = ["25%", "20%", "20%", "15%", "10%", "10%"]
    for i, (name, score) in enumerate(zip(cat_names, cat_scores)):
        status = "Strong" if score >= 75 else "Needs Work" if score >= 50 else "Critical"
        score_data.append([name, f"{int(score)}/100", weights[i] if i < len(weights) else "—", status])

    score_table = Table(score_data, colWidths=[180, 70, 60, 90])
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
        {"severity": "Critical", "finding": "Homepage headline lacks clarity — visitors can't understand the value proposition in under 5 seconds"},
        {"severity": "High",     "finding": "No social proof on homepage — missing testimonials, member logos, and trust badges"},
        {"severity": "High",     "finding": "Primary CTA uses generic text ('Get Started') instead of value-driven copy"},
        {"severity": "Medium",   "finding": "Missing meta descriptions on key landing pages"},
        {"severity": "Medium",   "finding": "No email capture mechanism or lead magnet visible"},
        {"severity": "Low",      "finding": "Blog content lacks internal linking to membership and coverage pages"},
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
        "Rewrite homepage headline to be specific and benefit-driven",
        "Add 3–5 member testimonials or trust badges above the fold",
        "Change primary CTA to value-driven text (e.g., 'Protect My Family — Join MASA')",
        "Add meta descriptions to top 5 landing pages",
    ]), 1):
        elements.append(Paragraph(f"{i}. {win}", body_style))

    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("[MEDIUM TERM] Medium-Term — 1–3 Months", subheading_style))
    for i, action in enumerate(data.get("medium_term", [
        "Build email capture funnel with lead magnet (e.g., emergency planning checklist)",
        "Create comparison pages vs. AirMedCare, Global Rescue, and Medjet",
        "Develop 3 member stories with real emergency scenarios and outcomes",
        "Build employer/HR landing page with group membership pitch and ROI framing",
    ]), 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph("[STRATEGIC] Strategic — 3–6 Months", subheading_style))
    for i, action in enumerate(data.get("strategic", [
        "Launch referral program with member incentives",
        "Build content authority hub: air ambulance cost, coverage gaps, international travel safety",
        "Implement full-funnel retargeting across Meta and Google",
        "Develop pricing transparency page contrasting membership cost vs. uninsured transport costs",
    ]), 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(PageBreak())

    # === COMPETITOR SNAPSHOT ===
    if data.get("competitors"):
        elements.append(draw_section_bar("Competitive Landscape"))
        elements.append(Spacer(1, 0.2 * inch))

        comp_data = [[""] + [c.get("name", f"Competitor {i+1}") for i, c in enumerate(data["competitors"][:3])]]
        for row_name in ["Positioning", "Pricing", "Social Proof", "Content"]:
            row = [row_name]
            for comp in data["competitors"][:3]:
                row.append(comp.get(row_name.lower().replace(" ", "_"), "—"))
            while len(row) < len(comp_data[0]):
                row.append("—")
            comp_data.append(row)

        col_count = len(comp_data[0])
        comp_table = Table(comp_data, colWidths=[470 / col_count] * col_count)
        comp_table.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (-1, 0),  COLORS["primary"]),
            ("TEXTCOLOR",     (0, 0), (-1, 0),  COLORS["white"]),
            ("FONTNAME",      (0, 0), (-1, 0),  "Helvetica-Bold"),
            ("FONTSIZE",      (0, 0), (-1, -1), 8),
            ("GRID",          (0, 0), (-1, -1), 0.5, COLORS["border"]),
            ("ROWBACKGROUNDS",(0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING",    (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("FONTNAME",      (0, 1), (0, -1),  "Helvetica-Bold"),
        ]))
        elements.append(comp_table)
        elements.append(PageBreak())

    # === METHODOLOGY ===
    elements.append(draw_section_bar("Methodology"))
    elements.append(Spacer(1, 0.2 * inch))
    elements.append(Paragraph(
        "This audit evaluates six key dimensions of marketing effectiveness. "
        "Each category is scored 0–100 based on industry best practices and competitive benchmarks.",
        body_style
    ))

    method_data = [
        ["Category", "Weight", "What We Measure"],
        ["Content & Messaging",    "25%", "Copy quality, value proposition clarity, CTA effectiveness"],
        ["Conversion Optimization","20%", "Funnel design, forms, social proof, friction reduction"],
        ["SEO & Discoverability",  "20%", "On-page SEO, technical SEO, content structure"],
        ["Competitive Positioning","15%", "Market differentiation, pricing, alternatives strategy"],
        ["Brand & Trust",          "10%", "Design quality, trust signals, authority indicators"],
        ["Growth & Strategy",      "10%", "Pricing strategy, acquisition channels, retention"],
    ]
    method_table = Table(method_data, colWidths=[140, 50, 280])
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
            "overall_score": 62,
            "executive_summary": (
                "This marketing audit of masaaccess.com reveals high-impact opportunities in conversion "
                "optimization and competitive positioning. The site has solid content foundations but "
                "is underperforming on trust signals, pricing transparency, and the employer/HR channel."
            ),
            "categories": {
                "Content & Messaging":    {"score": 68, "weight": "25%"},
                "Conversion Optimization":{"score": 52, "weight": "20%"},
                "SEO & Discoverability":  {"score": 74, "weight": "20%"},
                "Competitive Positioning":{"score": 48, "weight": "15%"},
                "Brand & Trust":          {"score": 70, "weight": "10%"},
                "Growth & Strategy":      {"score": 55, "weight": "10%"},
            },
            "competitors": [
                {"name": "AirMedCare",   "positioning": "Largest US network", "pricing": "$99–249/yr",   "social_proof": "Network coverage map", "content": "Active blog"},
                {"name": "Global Rescue","positioning": "Adventure/travel",   "pricing": "$119–329/yr",  "social_proof": "Member stories",       "content": "Travel advisories"},
                {"name": "Medjet",       "positioning": "Hospital-to-hospital","pricing": "$295–415/yr", "social_proof": "Forbes mention",       "content": "Resource hub"},
            ],
            "brand_name": "MASA Access"
        }
        output = "MARKETING-REPORT-sample.pdf"
        generate_report(sample_data, output)
        print(f"Sample report generated: {output}")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "MARKETING-REPORT.pdf"
    with open(input_file, "r") as f:
        data = json.load(f)
    generate_report(data, output_file)
    print(f"Report generated: {output_file}")


if __name__ == "__main__":
    main()
