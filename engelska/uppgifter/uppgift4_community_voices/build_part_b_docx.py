"""Build Part B Literary Analysis First Draft as a .docx file."""
from docx import Document
from docx.shared import Pt, RGBColor
from pathlib import Path

SRC = Path(__file__).parent / "submit" / "PartB_LiteraryAnalysis_FirstDraft.md"
OUT = Path(__file__).parent / "FINAL_SUBMISSION" / "Assignment4_PartB_LiteraryAnalysis_FirstDraft_MohammadSamiAlsharef.docx"
OUT.parent.mkdir(parents=True, exist_ok=True)

doc = Document()

style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)

for raw in SRC.read_text(encoding="utf-8").splitlines():
    line = raw.rstrip()
    if not line:
        doc.add_paragraph("")
        continue
    if line.startswith("# "):
        h = doc.add_heading(line[2:].strip(), level=1)
    elif line.startswith("## "):
        h = doc.add_heading(line[3:].strip(), level=2)
    elif line.startswith("> "):
        p = doc.add_paragraph()
        run = p.add_run(line[2:].strip())
        run.italic = True
        run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    elif line.startswith("---"):
        doc.add_paragraph("")
    elif line.startswith("- "):
        doc.add_paragraph(line[2:].strip(), style="List Bullet")
    else:
        # handle simple bold **...**
        p = doc.add_paragraph()
        parts = line.split("**")
        for i, chunk in enumerate(parts):
            if not chunk:
                continue
            run = p.add_run(chunk)
            run.bold = (i % 2 == 1)

doc.save(OUT)
print(f"Wrote: {OUT}")
