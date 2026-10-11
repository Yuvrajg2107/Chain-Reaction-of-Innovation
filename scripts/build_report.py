"""Generate planning diagrams and a printable report from the Markdown sources."""
import html
import re
import textwrap
from pathlib import Path

from PIL import Image as PILImage, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Image, Preformatted, KeepTogether, CondPageBreak
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/ChainReaction_Analysis_and_Plan.pdf"
NAVY = "#143449"
TEAL = "#116c71"
SECTIONS = [
    "docs/project-brief.md", "docs/source-review.md",
    "docs/research/novelty-assessment.md", "docs/research/literature-review.md",
    "docs/PRD.md", "docs/architecture.md", "docs/data-contract.md",
    "docs/reasoning-spec.md", "docs/evaluation-plan.md",
    "docs/implementation-plan.md", "docs/team-guide.md",
    "docs/publication-and-ip.md", "docs/decisions-and-risks.md",
    "docs/agent-handoff.md", "docs/research/sources.md", "docs/research/search-log.md"
]


def diagram(name, title, subtitle, boxes, arrows, footer):
    width, height = 1600, 1000
    im = PILImage.new("RGB", (width, height), "#f5f8fa")
    draw = ImageDraw.Draw(im)
    regular = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 27)
    bold = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 30)
    titlefont = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 48)
    small = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 24)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
           '<rect width="1600" height="1000" fill="#f5f8fa"/>',
           '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#116c71"/></marker></defs>']

    def text(x, y, value, font, size, color=NAVY, weight="normal"):
        draw.text((x, y), value, font=font, fill=color)
        svg.append(f'<text x="{x}" y="{y + size}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{html.escape(value)}</text>')

    text(55, 40, title, titlefont, 48, weight="bold")
    text(55, 110, subtitle, regular, 27)
    for x, y, w, h, heading, lines, fill in boxes:
        draw.rounded_rectangle((x, y, x + w, y + h), radius=15, fill=fill, outline="#bbcad3", width=2)
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="{fill}" stroke="#bbcad3" stroke-width="2"/>')
        text(x + 22, y + 18, heading, bold, 30, weight="bold")
        for j, line in enumerate(lines):
            text(x + 22, y + 73 + j * 40, line, regular, 27)
    for x1, y1, x2, y2 in arrows:
        draw.line((x1, y1, x2, y2), fill=TEAL, width=5)
        if y1 == y2:
            sign = 1 if x2 > x1 else -1
            draw.polygon([(x2, y2), (x2 - sign * 15, y2 - 10), (x2 - sign * 15, y2 + 10)], fill=TEAL)
        else:
            sign = 1 if y2 > y1 else -1
            draw.polygon([(x2, y2), (x2 - 10, y2 - sign * 15), (x2 + 10, y2 - sign * 15)], fill=TEAL)
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{TEAL}" stroke-width="5" marker-end="url(#arrow)"/>')
    for j, line in enumerate(footer):
        text(55, 900 + j * 35, line, small, 24)
    svg.append("</svg>")
    base = ROOT / "assets/diagrams" / name
    im.save(base.with_suffix(".png"))
    base.with_suffix(".svg").write_text("\n".join(svg), encoding="utf-8")


def make_diagrams():
    diagram("architecture", "ChainReaction | proposed system", "A shared engine, reviewed domain packs, and conditional engineering outputs.", [
        (55, 185, 450, 220, "1. Evidence and review", ["Permitted sources and exact locators", "Draft claims -> human review", "Source versions and conflicts"], "#e4eff5"),
        (575, 185, 470, 280, "2. Domain pack", ["Product / subsystem / component", "Material / principle / model", "Parameters, units, configurations", "Model bindings and conditions"], "#e3f1ec"),
        (1115, 185, 430, 280, "3. Shared engine", ["Plan relevant mechanisms", "Check context and inputs", "Execute approved models", "Recheck inverse candidates"], "#e9edf9"),
        (55, 570, 450, 230, "Versioned local records", ["SQLite + graph view", "Evidence files and permissions", "Immutable run snapshots"], "#e9edf0"),
        (575, 570, 470, 260, "5. Evaluate", ["Matched baselines and ablations", "Correct paths and false support", "Answer coverage and transfer effort", "Expert review of failures"], "#fbefda"),
        (1115, 570, 430, 260, "4. Inspectable results", ["Conditional supported impacts", "Blocked or unresolved branches", "Evidence and model versions", "Next evidence needed"], "#def1f0")
    ], [(505, 300, 575, 300), (1045, 320, 1115, 320), (1330, 465, 1330, 570), (1115, 700, 1045, 700), (280, 405, 280, 570)],
        ["Planning diagram, 12 October 2026. Components are not implemented.", "The six entity types organize knowledge; they do not impose a linear physical hierarchy."])
    diagram("reasoning", "Forward and backward engineering analysis", "Both directions use the same reviewed models, configuration, evidence, and constraints.", [
        (55, 180, 690, 200, "Forward: specify a change", ["Parameter, product configuration, context", "Find applicable mechanisms and model bindings"], "#e4eff5"),
        (855, 180, 690, 200, "Backward: specify a requirement", ["Target, allowed interventions, hard constraints", "Find upstream controllable variables"], "#e3f1ec"),
        (55, 445, 690, 185, "Check before execution", ["Inputs / units / assumptions / validity ranges", "Unknown conditions create explicit blockers"], "#e9edf9"),
        (855, 445, 690, 185, "Generate bounded candidates", ["Approved inverse model or bounded search", "Forward-check each candidate and constraint"], "#e9edf9"),
        (55, 695, 690, 165, "Report conditional impacts", ["Beneficial, adverse, mixed, or unresolved", "Show intermediate outputs and evidence"], "#def1f0"),
        (855, 695, 690, 165, "Report investigated options", ["Feasible within conditions, blocked, or unresolved", "No automatic novelty or invention certification"], "#fbefda")
    ], [(400, 380, 400, 445), (400, 630, 400, 695), (1200, 380, 1200, 445), (1200, 630, 1200, 695)],
        ["A reverse graph traversal finds relevance. It does not prove that an intervention works.", "New planning diagram based on source text; it does not recover the cropped source image."])


def inline(value):
    # Normalize PDF punctuation while preserving factual source text.
    value = value.replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", " - ").replace("\u2192", "->")
    value = value.replace("\u201c", '"').replace("\u201d", '"').replace("\u2019", "'")
    tokens = []
    def link(match):
        label, url = match.groups()
        safe_label = html.escape(label)
        if url.startswith("http"):
            replacement = f'<link href="{html.escape(url, quote=True)}" color="#116c71">{safe_label}</link>'
        else:
            replacement = safe_label
        tokens.append(replacement)
        return f"ZZLINK{len(tokens)-1}ZZ"
    value = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, value)
    value = html.escape(value)
    value = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    for n, token in enumerate(tokens):
        value = value.replace(f"ZZLINK{n}ZZ", token)
    return value


STYLES = getSampleStyleSheet()
STYLES.add(ParagraphStyle(name="BodyCR", fontName="Helvetica", fontSize=9.5, leading=14.3, textColor=colors.HexColor(NAVY), spaceAfter=7))
STYLES.add(ParagraphStyle(name="TitleCR", fontName="Helvetica-Bold", fontSize=25, leading=30, textColor=colors.HexColor(NAVY), spaceBefore=12, spaceAfter=16, keepWithNext=True))
STYLES.add(ParagraphStyle(name="H2CR", fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=colors.HexColor(TEAL), spaceBefore=13, spaceAfter=7, keepWithNext=True))
STYLES.add(ParagraphStyle(name="H3CR", fontName="Helvetica-Bold", fontSize=10.5, leading=14, textColor=colors.HexColor(NAVY), spaceBefore=8, spaceAfter=5, keepWithNext=True))
STYLES.add(ParagraphStyle(name="CellCR", fontName="Helvetica", fontSize=8, leading=11, textColor=colors.HexColor(NAVY)))
STYLES.add(ParagraphStyle(name="CaptionCR", fontName="Helvetica-Oblique", fontSize=8, leading=11, textColor=colors.HexColor(TEAL), spaceAfter=9))
STYLES.add(ParagraphStyle(name="CodeCR", fontName="Courier", fontSize=7.3, leading=10))


def markdown_story(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    story = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith("```"):
            code = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code.extend(textwrap.wrap(lines[i], 88, replace_whitespace=False, drop_whitespace=False) or [""])
                i += 1
            story.append(Preformatted("\n".join(code), STYLES["CodeCR"]))
            story.append(Spacer(1, 8))
            i += 1
            continue
        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                raw = [x.strip() for x in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", x.replace(" ", "")) for x in raw):
                    rows.append(raw)
                i += 1
            count = len(rows[0])
            width = 175 * mm
            weights = {2: [0.25, 0.75], 3: [0.23, 0.38, 0.39], 4: [0.17, 0.28, 0.28, 0.27], 5: [0.16, 0.17, 0.25, 0.22, 0.20]}.get(count, [1/count]*count)
            cells = [[Paragraph(inline(x), STYLES["CellCR"]) for x in row] for row in rows]
            table = Table(cells, colWidths=[width * x for x in weights], repeatRows=1, hAlign="LEFT")
            table.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#e1edf0")),
                ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f4f7f8")]),
                ("VALIGN", (0,0), (-1,-1), "TOP"),
                ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
                ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6),
                ("LINEBELOW", (0,0), (-1,0), .6, colors.HexColor("#aec6ce"))]))
            story.extend([table, Spacer(1, 11)])
            continue
        image_match = re.fullmatch(r"!\[([^\]]*)\]\(([^)]+)\)", line)
        if image_match:
            caption, target = image_match.groups()
            file = (path.parent / target).resolve()
            with PILImage.open(file) as image_data:
                w, h = image_data.size
            scale = min(175 * mm / w, 110 * mm / h)
            story.append(KeepTogether([Image(str(file), width=w*scale, height=h*scale), Paragraph(inline(caption), STYLES["CaptionCR"])]))
            i += 1
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            style = {1: "TitleCR", 2: "H2CR", 3: "H3CR"}[level]
            story.append(Paragraph(inline(heading.group(2)), STYLES[style]))
            i += 1
            continue
        bullet = re.match(r"^([-*]|\d+\.)\s+(.+)$", line)
        if bullet:
            marker = bullet.group(1) if bullet.group(1)[0].isdigit() else "-"
            story.append(Paragraph(inline(bullet.group(2)), STYLES["BodyCR"], bulletText=marker))
            i += 1
            continue
        para = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||!\[|```|[-*] |\d+\. )", lines[i].strip()):
            para.append(lines[i].strip())
            i += 1
        story.append(Paragraph(inline(" ".join(para)), STYLES["BodyCR"]))
    return story


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#bbcad3"))
    canvas.line(17.5*mm, 16*mm, 192.5*mm, 16*mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor(NAVY))
    canvas.drawString(17.5*mm, 11*mm, "ChainReaction | Research and implementation plan | 12 October 2026")
    canvas.drawRightString(192.5*mm, 11*mm, str(doc.page))
    canvas.restoreState()


def main():
    make_diagrams()
    doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=17.5*mm, rightMargin=17.5*mm,
                            topMargin=18*mm, bottomMargin=22*mm, title="ChainReaction: Analysis and Plan",
                            author="ChainReaction project planning")
    story = [Spacer(1, 35*mm), Paragraph("CHAIN REACTION<br/>OF INNOVATION", STYLES["TitleCR"]),
             Paragraph("Source review, research assessment, product requirements, and implementation plan", STYLES["H2CR"]),
             Spacer(1, 12*mm), Paragraph("12 October 2026 | Planning version 0.1", STYLES["BodyCR"]),
             Paragraph("The project is a proposed engineering decision-support framework. This report contains recommendations and prospective experiments. It does not claim a working application, proven novelty, patent eligibility, publication acceptance, or institutional approval.", STYLES["BodyCR"]),
             Spacer(1, 7*mm), Paragraph("Recommendation: implement one complete, reviewed forward-and-backward workflow in an extensible domain-pack architecture. Establish comparative evidence before expanding coverage or asserting a research contribution.", STYLES["BodyCR"]), PageBreak(),
             Paragraph("Reading guide", STYLES["TitleCR"]),
             Paragraph("The editable Markdown files in docs/ are the source of truth. Each section below reproduces its corresponding planning document. Direct research links appear in the source register; access limitations are recorded. Local cross-references in the PDF refer to the companion repository.", STYLES["BodyCR"])]
    for n, name in enumerate(SECTIONS, 1):
        heading = (ROOT / name).read_text(encoding="utf-8").splitlines()[0].removeprefix("# ")
        story.append(Paragraph(f"{n}. {html.escape(heading)}", STYLES["BodyCR"]))
    story.append(PageBreak())
    for index, name in enumerate(SECTIONS):
        if index:
            story.extend([Spacer(1, 6*mm), CondPageBreak(45*mm)])
        story.extend(markdown_story(ROOT / name))
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"Built {OUT.name} and two diagrams (PNG + SVG).")


if __name__ == "__main__":
    main()
