"""
Build 3 print-ready PDF layouts matching Publisher specifications:
1. Visitkort  - 90 x 55 mm  (framsida + baksida)
2. Folder     - A4 trifold  (6 paneler)
3. A3 Collage - A3 landscape (reklamfoto)
"""

from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import (
    HexColor, white, black
)
from reportlab.lib.pagesizes import A4, A3, landscape
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUT = r"c:\Users\samij\Desktop\uppgifter\alyaa"

# ─── COLOURS ─────────────────────────────────────────────
ROSE_BG      = HexColor("#E8D5C4")   # warm rosy beige
SAND_DARK    = HexColor("#4A3728")   # dark sand / brown-black
SAND_MID     = HexColor("#C4A882")   # mid sand accent
SCHOOL_BLUE  = HexColor("#1A3A5C")   # deep blue
SCHOOL_YELLOW= HexColor("#F5C842")   # yellow accent
LIGHT_BLUE   = HexColor("#EEF3F8")   # very light blue bg
DARK_GREY    = HexColor("#2C2C2C")
MID_GREY     = HexColor("#666666")
LIGHT_GREY   = HexColor("#F4F4F4")
AD_DARK      = HexColor("#1C1C1C")
AD_ACCENT    = HexColor("#D4AF37")   # gold for ad

# ─── HELPERS ─────────────────────────────────────────────
def draw_rect(c, x, y, w, h, fill, stroke=None):
    c.setFillColor(fill)
    if stroke:
        c.setStrokeColor(stroke)
        c.setLineWidth(0.3*mm)
        c.rect(x, y, w, h, fill=1, stroke=1)
    else:
        c.rect(x, y, w, h, fill=1, stroke=0)

def text(c, txt, x, y, size, color, font="Helvetica", align="left"):
    c.setFont(font, size)
    c.setFillColor(color)
    if align == "center":
        c.drawCentredString(x, y, txt)
    elif align == "right":
        c.drawRightString(x, y, txt)
    else:
        c.drawString(x, y, txt)

def text_bold(c, txt, x, y, size, color, align="left"):
    text(c, txt, x, y, size, color, font="Helvetica-Bold", align=align)

def wrapped_text(c, txt, x, y, max_width, size, color, font="Helvetica", line_height=None):
    """Simple word-wrap for reportlab canvas."""
    if line_height is None:
        line_height = size * 1.5
    c.setFont(font, size)
    c.setFillColor(color)
    words = txt.split()
    line = ""
    cy = y
    for word in words:
        test = (line + " " + word).strip()
        if c.stringWidth(test, font, size) <= max_width:
            line = test
        else:
            if line:
                c.drawString(x, cy, line)
                cy -= line_height
            line = word
    if line:
        c.drawString(x, cy, line)
    return cy - line_height   # return final y

# ═══════════════════════════════════════════════════════════
# 1. VISITKORT  90 x 55 mm
# ═══════════════════════════════════════════════════════════
W = 90*mm
H = 55*mm
MARGIN = 5*mm

cv = canvas.Canvas(
    os.path.join(OUT, "PUBLISHER_visitkort.pdf"),
    pagesize=(W, H)
)

# ── FRAMSIDA ──────────────────────────────────────────────
draw_rect(cv, 0, 0, W, H, ROSE_BG)

# Left colour stripe
draw_rect(cv, 0, 0, 7*mm, H, SAND_DARK)

# Logo box (simple stylised A)
draw_rect(cv, 10*mm, H - 17*mm, 12*mm, 12*mm, SAND_DARK)
text_bold(cv, "A", 10*mm + 6*mm, H - 10*mm, 14, ROSE_BG, align="center")

# Name
text_bold(cv, "Alyaa", 25*mm, H - 10*mm, 16, SAND_DARK)
# Title
text(cv,  "Frilansfotograf", 25*mm, H - 16*mm, 8, SAND_MID)

# Divider line
cv.setStrokeColor(SAND_MID)
cv.setLineWidth(0.3*mm)
cv.line(25*mm, H - 19*mm, W - MARGIN, H - 19*mm)

# Contact info
INFO_Y = H - 25*mm
INFO_X = 25*mm
cv.setFont("Helvetica", 7)
cv.setFillColor(SAND_DARK)
for line in [
    "alyaa@foton.se",
    "+46 70 123 45 67",
    "Storgatan 12, Stockholm",
]:
    cv.drawString(INFO_X, INFO_Y, line)
    INFO_Y -= 5.5*mm

# Tagline bottom
text(cv, "Ditt ögonblick. Mitt hantverk.", W/2, MARGIN + 1*mm, 6.5, SAND_MID, align="center")

cv.showPage()

# ── BAKSIDA ───────────────────────────────────────────────
draw_rect(cv, 0, 0, W, H, SAND_DARK)

# Gold accent band
draw_rect(cv, 0, H - 10*mm, W, 10*mm, SAND_MID)
text_bold(cv, "ALYAA PHOTOGRAPHY", W/2, H - 7*mm, 9, ROSE_BG, align="center")

# Large A logo
cv.setFont("Helvetica-Bold", 38)
cv.setFillColor(ROSE_BG)
cv.setFillAlpha(0.15)
cv.drawCentredString(W/2, 10*mm, "A")
cv.setFillAlpha(1.0)

# Tagline
text(cv, "Ditt ögonblick.", W/2, H/2 + 3*mm, 10, ROSE_BG, align="center")
text(cv, "Mitt hantverk.", W/2, H/2 - 5*mm, 10, SAND_MID, align="center")

# Bottom band
draw_rect(cv, 0, 0, W, 7*mm, SAND_MID)
text(cv, "www.alyaa.se", W/2, 2*mm, 6, SAND_DARK, align="center")

cv.showPage()
cv.save()
print("Saved: PUBLISHER_visitkort.pdf")


# ═══════════════════════════════════════════════════════════
# 2. FOLDER — A4 trifold (6 paneler)
#    Portrait A4 = 210 x 297 mm
#    Each panel = 70 mm wide
# ═══════════════════════════════════════════════════════════
PW, PH = A4   # 595.27 x 841.89 pt
PANEL_W = PW / 3
MARGINS = 8*mm
FOLD_COLOR = HexColor("#CCCCCC")

def fold_lines(cv, pw, ph):
    cv.setStrokeColor(FOLD_COLOR)
    cv.setLineWidth(0.2*mm)
    cv.setDash(2, 3)
    cv.line(PANEL_W, 0, PANEL_W, ph)
    cv.line(PANEL_W*2, 0, PANEL_W*2, ph)
    cv.setDash()

fv = canvas.Canvas(
    os.path.join(OUT, "PUBLISHER_folder_studiero.pdf"),
    pagesize=A4
)

# ── SIDA 1 (utsida: panel 1=rygg, 2=framsida, 3=innerflik) ─
# Panel 1 (Left) — rygg / back inside
draw_rect(fv, 0, 0, PANEL_W, PH, LIGHT_BLUE)
fv.setFont("Helvetica-Bold", 9)
fv.setFillColor(SCHOOL_BLUE)
# Rotated text on spine area
fv.saveState()
fv.translate(PANEL_W/2, PH/2)
fv.rotate(90)
fv.drawCentredString(0, 0, "Zetterbergsgymnasiet – Studiero för alla")
fv.restoreState()

draw_rect(fv, 0, 0, PANEL_W, 18*mm, SCHOOL_BLUE)
text(fv, "Zetterbergsgymnasiet", PANEL_W/2, 8*mm, 7, white, align="center")

# Panel 2 (Middle) — FRAMSIDA
draw_rect(fv, PANEL_W, 0, PANEL_W, PH, SCHOOL_BLUE)
# Top image area placeholder
draw_rect(fv, PANEL_W + MARGINS, PH - 90*mm, PANEL_W - 2*MARGINS, 80*mm, HexColor("#0E2A45"))
text(fv, "[ FOTO ]", PANEL_W + PANEL_W/2, PH - 55*mm, 10, HexColor("#4A7FA5"), align="center")

# Title block
text_bold(fv, "STUDIERO", PANEL_W + PANEL_W/2, PH - 105*mm, 26, SCHOOL_YELLOW, align="center")
text_bold(fv, "FÖR ALLA", PANEL_W + PANEL_W/2, PH - 118*mm, 26, white, align="center")

# Divider
fv.setStrokeColor(SCHOOL_YELLOW)
fv.setLineWidth(1.5)
fv.line(PANEL_W + MARGINS, PH - 125*mm, PANEL_W*2 - MARGINS, PH - 125*mm)

# Subtext
text(fv, "Tillsammans skapar vi en skola", PANEL_W + PANEL_W/2, PH - 133*mm, 8, HexColor("#B0C4D8"), align="center")
text(fv, "där alla kan lära sig.", PANEL_W + PANEL_W/2, PH - 141*mm, 8, HexColor("#B0C4D8"), align="center")

# School logo area bottom
draw_rect(fv, PANEL_W, 0, PANEL_W, 22*mm, HexColor("#0E2A45"))
text(fv, "Zetterbergsgymnasiet", PANEL_W + PANEL_W/2, 8*mm, 8, white, align="center")

# Panel 3 (Right) — innerflik
draw_rect(fv, PANEL_W*2, 0, PANEL_W, PH, LIGHT_GREY)
draw_rect(fv, PANEL_W*2, PH - 22*mm, PANEL_W, 22*mm, SCHOOL_BLUE)
text_bold(fv, "Kontakt & Info", PANEL_W*2 + PANEL_W/2, PH - 13*mm, 9, white, align="center")

IY = PH - 35*mm
IX = PANEL_W*2 + MARGINS
fv.setFont("Helvetica-Bold", 8)
fv.setFillColor(SCHOOL_BLUE)
fv.drawString(IX, IY, "Rektorsexpedition")
fv.setFont("Helvetica", 7.5)
fv.setFillColor(DARK_GREY)
for ln in ["info@zetterbergs.se", "08-123 456 78", "Skolvägen 1, Stockholm", "", "Läs mer på vår hemsida:"]:
    IY -= 6.5*mm
    fv.drawString(IX, IY, ln)

IY -= 4*mm
fv.setFont("Helvetica-Bold", 8)
fv.setFillColor(SCHOOL_BLUE)
fv.drawString(IX, IY, "www.zetterbergsgymnasiet.se")

fold_lines(fv, PW, PH)
fv.showPage()

# ── SIDA 2 (insida: 3 paneler med innehåll) ──────────────
# Panel 1 — Vad är studiero?
draw_rect(fv, 0, 0, PANEL_W, PH, white)
draw_rect(fv, 0, PH - 28*mm, PANEL_W, 28*mm, SCHOOL_BLUE)
text_bold(fv, "Vad är studiero?", PANEL_W/2, PH - 17*mm, 10, white, align="center")

content_1 = [
    ("", "Studiero handlar om att alla i skolan"),
    ("", "ska ha möjlighet att fokusera och lära"),
    ("", "sig — utan onödiga störningar."),
    ("", ""),
    ("", "Det är ett gemensamt ansvar. Varje"),
    ("", "elev bidrar till stämningen i klassrum"),
    ("", "och korridorer varje dag."),
    ("", ""),
    ("", "En bra studiemiljö leder till:"),
    ("•", "Bättre koncentration"),
    ("•", "Tryggare klassrumsklimat"),
    ("•", "Högre motivation"),
    ("•", "Bättre studieresultat"),
]
cy = PH - 42*mm
for bullet, line in content_1:
    fv.setFont("Helvetica", 7.5)
    fv.setFillColor(DARK_GREY)
    fv.drawString(MARGINS + (4*mm if bullet == "•" else 0), cy, (bullet + " " if bullet else "") + line)
    cy -= 5.5*mm

# Illustration placeholder
draw_rect(fv, MARGINS, 20*mm, PANEL_W - 2*MARGINS, 45*mm, LIGHT_BLUE)
fv.setFont("Helvetica", 7)
fv.setFillColor(HexColor("#888888"))
fv.drawCentredString(PANEL_W/2, 43*mm, "[ ILLUSTRATION ]")

# Panel 2 — Våra regler
draw_rect(fv, PANEL_W, 0, PANEL_W, PH, LIGHT_GREY)
draw_rect(fv, PANEL_W, PH - 28*mm, PANEL_W, 28*mm, SCHOOL_YELLOW)
text_bold(fv, "Våra regler", PANEL_W + PANEL_W/2, PH - 17*mm, 10, SCHOOL_BLUE, align="center")

RULES = [
    "1. Kom i tid till lektionen.",
    "2. Ha mobilen tyst eller i fickan.",
    "3. Lyssna när läraren – eller en",
    "   klasskamrat – pratar.",
    "4. Jobba med egna uppgifter under",
    "   lektionen.",
    "5. Prata lugnt i korridorerna.",
    "6. Respektera andras arbetsro i",
    "   biblioteket.",
    "7. Ta ansvar för ditt beteende.",
]
ry = PH - 40*mm
for rule in RULES:
    fv.setFont("Helvetica", 7.5)
    fv.setFillColor(DARK_GREY)
    fv.drawString(PANEL_W + MARGINS, ry, rule)
    ry -= 6*mm

draw_rect(fv, PANEL_W + MARGINS, 20*mm, PANEL_W - 2*MARGINS, 35*mm, HexColor("#D8E6F0"))
fv.setFont("Helvetica-Oblique", 7.5)
fv.setFillColor(SCHOOL_BLUE)
fv.drawCentredString(PANEL_W + PANEL_W/2, 38*mm, '"Respekt är grunden')
fv.drawCentredString(PANEL_W + PANEL_W/2, 31*mm, 'för allt lärande."')

# Panel 3 — Tillsammans kan vi
draw_rect(fv, PANEL_W*2, 0, PANEL_W, PH, SCHOOL_BLUE)
draw_rect(fv, PANEL_W*2, PH - 28*mm, PANEL_W, 28*mm, HexColor("#0E2A45"))
text_bold(fv, "Tillsammans kan vi", PANEL_W*2 + PANEL_W/2, PH - 15*mm, 9, white, align="center")
text_bold(fv, "göra skillnad!", PANEL_W*2 + PANEL_W/2, PH - 23*mm, 9, SCHOOL_YELLOW, align="center")

TIPS = [
    ("Tänk på:", True),
    ("", False),
    ("Ditt beteende påverkar alla", False),
    ("runt om kring dig i skolan.", False),
    ("", False),
    ("Om du ser att någon stör", False),
    ("arbetsron – säg till snällt,", False),
    ("eller prata med en lärare.", False),
    ("", False),
    ("Positiv stämning smittar!", True),
    ("", False),
    ("Hjälp till att hålla skolan", False),
    ("till en plats där alla trivs", False),
    ("och kan växa.", False),
]
ty = PH - 42*mm
for line, bold in TIPS:
    fv.setFont("Helvetica-Bold" if bold else "Helvetica", 7.5 if bold else 7.5)
    fv.setFillColor(SCHOOL_YELLOW if bold else HexColor("#C8D8E8"))
    fv.drawString(PANEL_W*2 + MARGINS, ty, line)
    ty -= 5.5*mm

# Photo placeholder
draw_rect(fv, PANEL_W*2 + MARGINS, 18*mm, PANEL_W - 2*MARGINS, 40*mm, HexColor("#0E2A45"))
fv.setFont("Helvetica", 7)
fv.setFillColor(HexColor("#4A7FA5"))
fv.drawCentredString(PANEL_W*2 + PANEL_W/2, 38*mm, "[ FOTO ]")

fold_lines(fv, PW, PH)
fv.showPage()
fv.save()
print("Saved: PUBLISHER_folder_studiero.pdf")


# ═══════════════════════════════════════════════════════════
# 3. A3 COLLAGE — Reklamfoto (landscape)
# ═══════════════════════════════════════════════════════════
A3W, A3H = landscape(A3)   # 1190 x 841 pt  (approx)
MARG = 15*mm

av = canvas.Canvas(
    os.path.join(OUT, "PUBLISHER_A3_collage_reklamfoto.pdf"),
    pagesize=landscape(A3)
)

# Background
draw_rect(av, 0, 0, A3W, A3H, AD_DARK)

# Top title band
draw_rect(av, 0, A3H - 32*mm, A3W, 32*mm, black)
# Title
av.setFont("Helvetica-Bold", 36)
av.setFillColor(AD_ACCENT)
av.drawString(MARG, A3H - 23*mm, "REKLAMFOTO")
av.setFont("Helvetica", 14)
av.setFillColor(white)
av.drawString(MARG, A3H - 30*mm, "Bildtyp inom grafisk kommunikation")

# Right info strip
STRIP_W = 110*mm
draw_rect(av, A3W - STRIP_W, 0, STRIP_W, A3H - 32*mm, HexColor("#111111"))
av.setStrokeColor(AD_ACCENT)
av.setLineWidth(1.5)
av.line(A3W - STRIP_W, 0, A3W - STRIP_W, A3H - 32*mm)

# Collage image slots (left 2/3)
SLOT_MARGIN = 6*mm
COL_W = (A3W - STRIP_W - 2*MARG - 3*SLOT_MARGIN) / 2
ROW1_H = (A3H - 32*mm - 2*MARG - 2*SLOT_MARGIN) * 0.55
ROW2_H = (A3H - 32*mm - 2*MARG - 2*SLOT_MARGIN) * 0.39

SLOT_COLORS = [HexColor("#1E2A38"), HexColor("#1A1A1A"), HexColor("#0E1C28"), HexColor("#181818")]
SLOT_LABELS = [
    "Modefoto / Fashion",
    "Produktfoto / Product",
    "Livsstilsfoto / Lifestyle",
    "Matfoto / Food",
]

positions = [
    (MARG,                   MARG + ROW2_H + SLOT_MARGIN, COL_W, ROW1_H),
    (MARG + COL_W + SLOT_MARGIN, MARG + ROW2_H + SLOT_MARGIN, COL_W, ROW1_H),
    (MARG,                   MARG, COL_W, ROW2_H),
    (MARG + COL_W + SLOT_MARGIN, MARG, COL_W, ROW2_H),
]

for i, (sx, sy, sw, sh) in enumerate(positions):
    draw_rect(av, sx, sy, sw, sh, SLOT_COLORS[i])
    av.setStrokeColor(AD_ACCENT)
    av.setLineWidth(0.5)
    av.rect(sx, sy, sw, sh, fill=0, stroke=1)
    av.setFont("Helvetica", 8)
    av.setFillColor(HexColor("#555555"))
    av.drawCentredString(sx + sw/2, sy + sh/2 + 4*mm, "[ BILD ]")
    av.setFont("Helvetica-Bold", 8.5)
    av.setFillColor(AD_ACCENT)
    av.drawCentredString(sx + sw/2, sy + sh/2 - 5*mm, SLOT_LABELS[i])

# ── Right strip — text content ────────────────────────────
TX = A3W - STRIP_W + 8*mm
TW = STRIP_W - 16*mm

def rtext(txt, y, size=8, color=white, bold=False):
    font = "Helvetica-Bold" if bold else "Helvetica"
    av.setFont(font, size)
    av.setFillColor(color)
    av.drawString(TX, y, txt)

def rwrap(txt, y, size=7.5, color=HexColor("#BBBBBB")):
    av.setFont("Helvetica", size)
    av.setFillColor(color)
    words = txt.split()
    line = ""
    cy = y
    for word in words:
        test = (line + " " + word).strip()
        if av.stringWidth(test, "Helvetica", size) <= TW:
            line = test
        else:
            av.drawString(TX, cy, line)
            cy -= size * 1.5
            line = word
    if line:
        av.drawString(TX, cy, line)
    return cy - size * 1.8

# Section: Vad är reklamfoto?
y = A3H - 47*mm
rtext("Vad är reklamfoto?", y, size=11, color=AD_ACCENT, bold=True)
y -= 7*mm
y = rwrap("Reklamfoto är bilder som skapats för att sälja, informera eller skapa en känsla kring en produkt, tjänst eller ett varumärke.", y)
y -= 2*mm
y = rwrap("Till skillnad från reportagefoto är allt i bilden noggrant planerat – ljuset, kompositionen, modellen och miljön.", y)

y -= 8*mm
rtext("Hur används det?", y, size=11, color=AD_ACCENT, bold=True)
y -= 7*mm
for ex in [
    "• Tidningsannonser och affischer",
    "• Webbutiker och hemsidor",
    "• Sociala medier (Instagram, etc.)",
    "• Förpackningsdesign",
    "• Kataloger och broschyrer",
]:
    rtext(ex, y, size=7.5, color=HexColor("#CCCCCC"))
    y -= 5.5*mm

y -= 5*mm
rtext("Syfte", y, size=11, color=AD_ACCENT, bold=True)
y -= 7*mm
y = rwrap("Syftet är alltid att påverka betraktaren — att köpa, klicka, lita på eller minnas ett varumärke.", y)
y -= 2*mm
y = rwrap("Fotografen arbetar nära art directors och marknadsförare för att bilden ska matcha varumärkets identitet.", y)

y -= 8*mm
rtext("Fyra vanliga underkategorier:", y, size=9, color=white, bold=True)
y -= 6*mm
CATS = [
    ("Modefoto",    "Kläder, accessoarer, kosmetika"),
    ("Produktfoto", "Elektronik, mat, industrivaror"),
    ("Livsstil",    "Produkt i verklig vardagsmiljö"),
    ("Matfoto",     "Restauranger och livsmedel"),
]
for cat, desc in CATS:
    av.setFont("Helvetica-Bold", 7.5)
    av.setFillColor(AD_ACCENT)
    av.drawString(TX, y, cat + ":")
    av.setFont("Helvetica", 7.5)
    av.setFillColor(HexColor("#AAAAAA"))
    av.drawString(TX + 22*mm, y, desc)
    y -= 5.5*mm

# Bottom credit bar
draw_rect(av, 0, 0, A3W, 10*mm, black)
av.setFont("Helvetica", 7)
av.setFillColor(HexColor("#666666"))
av.drawString(MARG, 3.5*mm, "Grafisk kommunikation  ·  Alyaa  ·  Zetterbergsgymnasiet  ·  2026")
av.drawRightString(A3W - MARG, 3.5*mm, "Bildtyp: Reklamfoto")

av.showPage()
av.save()
print("Saved: PUBLISHER_A3_collage_reklamfoto.pdf")

print("\nAlla Publisher-liknande filer klara!")
