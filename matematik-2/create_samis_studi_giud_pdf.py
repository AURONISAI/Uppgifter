from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

base = Path(r"c:\Users\samij\Desktop\uppgifter\matematik-2")
md_path = base / "Samis studi giud.md"
pdf_path = base / "Samis studi giud.pdf"

text = md_path.read_text(encoding="utf-8")
lines = text.splitlines()

styles = getSampleStyleSheet()
style_title = ParagraphStyle(
    "TitleSv",
    parent=styles["Heading1"],
    fontName="Helvetica-Bold",
    fontSize=17,
    leading=21,
    spaceAfter=8,
    alignment=TA_LEFT,
)
style_h2 = ParagraphStyle(
    "H2Sv",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=12,
    leading=16,
    spaceBefore=6,
    spaceAfter=4,
)
style_body = ParagraphStyle(
    "BodySv",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=10.5,
    leading=14,
    spaceAfter=3,
)


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )

story = []
for raw in lines:
    line = raw.rstrip()

    if not line:
        story.append(Spacer(1, 2))
        continue

    if line.startswith("# "):
        story.append(Paragraph(esc(line[2:]), style_title))
        continue

    if line.startswith("## "):
        story.append(Paragraph(esc(line[3:]), style_h2))
        continue

    clean = line.replace("**", "")
    clean = clean.replace("`", "")

    if clean.startswith("- "):
        story.append(Paragraph("• " + esc(clean[2:]), style_body))
    else:
        story.append(Paragraph(esc(clean), style_body))


doc = SimpleDocTemplate(
    str(pdf_path),
    pagesize=A4,
    leftMargin=18 * mm,
    rightMargin=18 * mm,
    topMargin=15 * mm,
    bottomMargin=15 * mm,
    title="Samis studi giud",
)

doc.build(story)
print(f"Saved: {pdf_path}")
