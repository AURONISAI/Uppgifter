from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_LEFT

base = Path(r"c:\Users\samij\Desktop\uppgifter\matematik-2")
md_path = base / "Öva-räta_FACIT.md"
pdf_path = base / "Öva-räta_FACIT_print.pdf"

text = md_path.read_text(encoding="utf-8")
lines = text.splitlines()

styles = getSampleStyleSheet()
style_title = ParagraphStyle(
    "TitleSv",
    parent=styles["Heading1"],
    fontName="Helvetica-Bold",
    fontSize=16,
    leading=20,
    spaceAfter=8,
    alignment=TA_LEFT,
)
style_h2 = ParagraphStyle(
    "H2Sv",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=12,
    leading=15,
    spaceBefore=6,
    spaceAfter=4,
)
style_body = ParagraphStyle(
    "BodySv",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=10,
    leading=13,
    spaceAfter=3,
)

story = []

def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )

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

    # normalize markdown emphasis markers for cleaner print text
    clean = line.replace("**", "").replace("`", "")

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
    title="Öva Räta linjens ekvation - Facit",
)

doc.build(story)
print(f"Saved: {pdf_path}")
