"""
Professional print-ready PDF layouts with real photos, real info, 3D shadows/depth effects.
Alyaa Alsharif | Zetterbergsgymnasiet, Eskilstuna
"""

from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.lib.pagesizes import A4, A3, landscape
from reportlab.lib.utils import ImageReader
import os, math, io
from PIL import Image as PILImage

OUT    = r"c:\Users\samij\Desktop\uppgifter\alyaa"
IMGS   = r"c:\Users\samij\Desktop\uppgifter\alyaa\images"

def img(fname):
    return ImageReader(os.path.join(IMGS, fname))

# ── COLOUR PALETTE ──────────────────────────────────────
GOLD       = HexColor("#C9A84C")
GOLD_LIGHT = HexColor("#EDD27A")
DARK       = HexColor("#1A1A1A")
CHARCOAL   = HexColor("#2D2D2D")
BEIGE      = HexColor("#F5EFE6")
CREAM      = HexColor("#FAF7F2")
WARM_GREY  = HexColor("#9E9080")
BLUE_DEEP  = HexColor("#0D2137")
BLUE_MID   = HexColor("#1A3A5C")
BLUE_LIGHT = HexColor("#2C5F8A")
BLUE_PALE  = HexColor("#E8F0F7")
YELLOW_ACC = HexColor("#F4C430")
RED_ACC    = HexColor("#C0392B")

# ── HELPER FUNCTIONS ─────────────────────────────────────
def fill(c, col):
    c.setFillColor(col)

def stroke(c, col, lw=0.3):
    c.setStrokeColor(col)
    c.setLineWidth(lw*mm)

def rect(c, x, y, w, h, fc, sc=None, lw=0.3, r=0):
    c.setFillColor(fc)
    if sc:
        c.setStrokeColor(sc)
        c.setLineWidth(lw*mm)
        if r:
            c.roundRect(x, y, w, h, r, fill=1, stroke=1)
        else:
            c.rect(x, y, w, h, fill=1, stroke=1)
    else:
        if r:
            c.roundRect(x, y, w, h, r, fill=1, stroke=0)
        else:
            c.rect(x, y, w, h, fill=1, stroke=0)

def shadow_rect(c, x, y, w, h, fc, shadow_offset=1.5, r=0):
    """Draw a rectangle with a drop shadow for 3D depth."""
    s = shadow_offset * mm
    c.setFillColor(Color(0, 0, 0, alpha=0.18))
    if r:
        c.roundRect(x + s, y - s, w, h, r, fill=1, stroke=0)
    else:
        c.rect(x + s, y - s, w, h, fill=1, stroke=0)
    rect(c, x, y, w, h, fc, r=r)

def txt(c, text, x, y, size, color, font="Helvetica", align="left"):
    c.setFont(font, size)
    c.setFillColor(color)
    if align == "center":
        c.drawCentredString(x, y, text)
    elif align == "right":
        c.drawRightString(x, y, text)
    else:
        c.drawString(x, y, text)

def txb(c, text, x, y, size, color, align="left"):
    txt(c, text, x, y, size, color, font="Helvetica-Bold", align=align)

def gradient_rect(c, x, y, w, h, color_top, color_bot, steps=30):
    """Simulate vertical gradient by stacking thin rectangles."""
    r1,g1,b1 = color_top.red, color_top.green, color_top.blue
    r2,g2,b2 = color_bot.red, color_bot.green, color_bot.blue
    sh = h / steps
    for i in range(steps):
        t = i / (steps - 1)
        rc = Color(r1 + (r2-r1)*t, g1 + (g2-g1)*t, b1 + (b2-b1)*t)
        c.setFillColor(rc)
        c.rect(x, y + h - (i+1)*sh, w, sh + 0.5, fill=1, stroke=0)

def wrap_text(c, text, x, y, max_w, size, color, font="Helvetica", line_h=None):
    if line_h is None:
        line_h = size * 1.55
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    line = ""
    cy = y
    for word in words:
        test = (line + " " + word).strip()
        if c.stringWidth(test, font, size) <= max_w:
            line = test
        else:
            if line:
                c.drawString(x, cy, line)
                cy -= line_h
            line = word
    if line:
        c.drawString(x, cy, line)
    return cy - line_h

# Points-to-pixels ratio at 150 DPI for pre-cropping
_DPI = 150
_PT_TO_PX = _DPI / 72.0

# Cache cropped images so we don't re-process the same file+size twice
_img_cache = {}

def _pil_crop(fname, w_pt, h_pt, tint_color=None, tint_alpha=0.0):
    """Use PIL to center-crop + resize image to exact box dimensions.
    Returns an ImageReader ready for reportlab drawImage."""
    px_w = max(1, int(w_pt * _PT_TO_PX))
    px_h = max(1, int(h_pt * _PT_TO_PX))
    key = (fname, px_w, px_h, tint_alpha)
    if key in _img_cache:
        return _img_cache[key]

    src = PILImage.open(os.path.join(IMGS, fname)).convert("RGB")
    src_w, src_h = src.size

    # Scale to cover the box (center crop)
    scale = max(px_w / src_w, px_h / src_h)
    new_w = int(src_w * scale)
    new_h = int(src_h * scale)
    src = src.resize((new_w, new_h), PILImage.LANCZOS)

    # Crop to exact size centered
    left = (new_w - px_w) // 2
    top  = (new_h - px_h) // 2
    src = src.crop((left, top, left + px_w, top + px_h))

    # Apply tint overlay if any
    if tint_color and tint_alpha > 0:
        r = int(tint_color.red   * 255)
        g = int(tint_color.green * 255)
        b = int(tint_color.blue  * 255)
        overlay = PILImage.new("RGB", src.size, (r, g, b))
        src = PILImage.blend(src, overlay, tint_alpha)

    buf = io.BytesIO()
    src.save(buf, format="JPEG", quality=88)
    buf.seek(0)
    ir = ImageReader(buf)
    _img_cache[key] = ir
    return ir

def draw_image_fitted(c, fname, x, y, w, h):
    """Draw image cover-cropped into exact box — no clipPath needed."""
    try:
        ir = _pil_crop(fname, w, h)
        c.drawImage(ir, x, y, w, h)
    except Exception as e:
        print(f"  draw_image_fitted error ({fname}): {e}")

def clip_image(c, fname, x, y, w, h, tint_color=None, tint_alpha=0.0):
    """Draw image cover-cropped with optional tint — no clipPath needed."""
    try:
        ir = _pil_crop(fname, w, h, tint_color, tint_alpha)
        c.drawImage(ir, x, y, w, h)
    except Exception as e:
        print(f"  clip_image error ({fname}): {e}")
        rect(c, x, y, w, h, tint_color if tint_color else CHARCOAL)

def draw_logo_A(c, cx, cy, size, bg_color, letter_color):
    """Draw a stylised A logo."""
    rect(c, cx - size/2, cy - size/2, size, size, bg_color, r=2*mm)
    c.setFont("Helvetica-Bold", size * 0.65)
    c.setFillColor(letter_color)
    c.drawCentredString(cx, cy - size * 0.2, "A")


# ═══════════════════════════════════════════════════════════════════
# 1.  VISITKORT  90 × 55 mm  —  framsida + baksida
# ═══════════════════════════════════════════════════════════════════
W, H = 90*mm, 55*mm

cv = canvas.Canvas(os.path.join(OUT, "PUBLISHER_visitkort.pdf"), pagesize=(W, H))

# ─ FRAMSIDA ────────────────────────────────────────────────────────
# Full background - white
rect(cv, 0, 0, W, H, white)

# Left gold accent strip
rect(cv, 0, 0, 6*mm, H, GOLD)

# Portrait photo — top right quadrant, circular-feel clip
PHOTO_W, PHOTO_H = 22*mm, 26*mm
PHOTO_X = W - PHOTO_W - 5*mm
PHOTO_Y = H - PHOTO_H - 5*mm
# shadow behind photo
cv.setFillColor(Color(0, 0, 0, alpha=0.15))
cv.rect(PHOTO_X + 1.5*mm, PHOTO_Y - 1.5*mm, PHOTO_W, PHOTO_H, fill=1, stroke=0)
clip_image(cv, "portrait.jpg", PHOTO_X, PHOTO_Y, PHOTO_W, PHOTO_H, BLUE_MID, 0.1)
# thin gold border around photo
cv.setStrokeColor(GOLD)
cv.setLineWidth(0.5*mm)
cv.rect(PHOTO_X, PHOTO_Y, PHOTO_W, PHOTO_H, fill=0, stroke=1)

# Logo
draw_logo_A(cv, 16*mm, H - 13*mm, 10*mm, DARK, GOLD)

# Gold horizontal rule under logo
cv.setStrokeColor(GOLD)
cv.setLineWidth(0.4*mm)
cv.line(11*mm, H - 19*mm, W - PHOTO_W - 8*mm, H - 19*mm)

# Name
txb(cv, "Alyaa Alsharif", 11*mm, H - 26*mm, 13, DARK)
# Title
txt(cv, "Grafisk formgivning  ·  Foto", 11*mm, H - 32*mm, 7.5, WARM_GREY)

# Divider dots
cv.setFillColor(GOLD)
for i in range(3):
    cv.circle(11*mm + i*4*mm, H - 36*mm, 0.8*mm, fill=1, stroke=0)

# Contact info
INFO = [
    ("✉", "alyaa.alsharif@elev.eskilstuna.se"),
    ("✆", "+46 70 000 00 00"),
    ("⌂", "Esbjergatan 1, Eskilstuna"),
]
iy = H - 40*mm
for icon, line in INFO:
    txt(cv, icon,  11*mm, iy, 7, GOLD)
    txt(cv, line,  15*mm, iy, 7, CHARCOAL)
    iy -= 4.8*mm

# Tagline bottom strip - light on white
rect(cv, 0, 0, W, 7*mm, HexColor("#F0F0F0"))
cv.setStrokeColor(HexColor("#DDDDDD"))
cv.setLineWidth(0.3*mm)
cv.line(0, 7*mm, W, 7*mm)
txt(cv, "Ditt ögonblick — mitt hantverk.", W/2, 2.5*mm, 6, WARM_GREY, align="center")

cv.showPage()

# ─ BAKSIDA ────────────────────────────────────────────────────────
rect(cv, 0, 0, W, H, white)
# Outer border
cv.setStrokeColor(GOLD)
cv.setLineWidth(0.5*mm)
cv.rect(1.5*mm, 1.5*mm, W - 3*mm, H - 3*mm, fill=0, stroke=1)

# Large watermark A (ghost)
cv.setFont("Helvetica-Bold", 78)
cv.setFillColor(Color(0, 0, 0, alpha=0.04))
cv.drawCentredString(W/2, 6*mm, "A")

# Gold top band
rect(cv, 0, H - 12*mm, W, 12*mm, GOLD)
txb(cv, "ALYAA ALSHARIF", W/2, H - 7.5*mm, 10, DARK, align="center")

# School info
txt(cv, "Zetterbergsgymnasiet", W/2, H - 20*mm, 8, CHARCOAL, align="center")
txt(cv, "Grafisk kommunikation", W/2, H - 26*mm, 7, WARM_GREY, align="center")

# Tagline
cv.setFont("Helvetica-Oblique", 9.5)
cv.setFillColor(CHARCOAL)
cv.drawCentredString(W/2, H/2 - 2*mm, "Ditt ögonblick.")
cv.setFont("Helvetica-Oblique", 9.5)
cv.setFillColor(GOLD)
cv.drawCentredString(W/2, H/2 - 9*mm, "Mitt hantverk.")

# Bottom strip - light
rect(cv, 0, 0, W, 7*mm, HexColor("#F5F5F5"))
txt(cv, "Eskilstuna  ·  2026", W/2, 2.5*mm, 6, WARM_GREY, align="center")

cv.showPage()
cv.save()
print("✓ PUBLISHER_visitkort.pdf")


# ═══════════════════════════════════════════════════════════════════
# 2.  FOLDER  —  A4 trifold landscape  (210×297, 6 panels)
# ═══════════════════════════════════════════════════════════════════
PW, PH = A4
PNL = PW / 3
M   = 7*mm

fv = canvas.Canvas(os.path.join(OUT, "PUBLISHER_folder_studiero.pdf"), pagesize=A4)

def fold_guides(c):
    c.setStrokeColor(Color(0, 0, 0, alpha=0.08))
    c.setLineWidth(0.2*mm)
    c.setDash(3, 4)
    c.line(PNL,   0, PNL,   PH)
    c.line(PNL*2, 0, PNL*2, PH)
    c.setDash()

# ── PAGE 1 (outside: left-inner-flap | cover | back) ──────────────

# Back panel (left on page 1 = panel 0)
rect(fv, 0, 0, PNL, PH, white)

# School logo area
rect(fv, M, PH - 30*mm, PNL - 2*M, 22*mm, GOLD)
txb(fv, "ZETTERBERGSGYMNASIET", PNL/2, PH - 14*mm, 7, DARK, align="center")
txt(fv, "Eskilstuna kommun", PNL/2, PH - 21*mm, 6.5, CHARCOAL, align="center")

# Rotated identifier
fv.saveState()
fv.translate(PNL/2, PH/2)
fv.rotate(90)
fv.setFont("Helvetica", 7)
fv.setFillColor(Color(0,0,0,alpha=0.2))
fv.drawCentredString(0, 0, "Studiero för alla  ·  Zetterbergsgymnasiet  ·  2026")
fv.restoreState()

# Contact at bottom of back - light box
rect(fv, 0, 0, PNL, 28*mm, HexColor("#F5F5F5"))
fv.setStrokeColor(HexColor("#DDDDDD"))
fv.setLineWidth(0.3*mm)
fv.line(0, 28*mm, PNL, 28*mm)
txb(fv, "Kontakt", M, 24*mm, 8, BLUE_MID)
for i, line in enumerate([
    "Köpmangatan 8, 632 20 Eskilstuna",
    "Tel: 016-710 10 00",
    "info@eskilstuna.se",
    "www.eskilstuna.se/zetterbergsgymnasiet",
]):
    txt(fv, line, M, 18*mm - i*5*mm, 6.5, CHARCOAL)

# Cover panel (middle = panel 1) — white bg with photo at top half only
rect(fv, PNL, 0, PNL, PH, white)

# Photo top half
clip_image(fv, "classroom.jpg", PNL + M, PH - 18*mm - 90*mm, PNL - 2*M, 88*mm, BLUE_DEEP, 0.05)
fv.setStrokeColor(HexColor("#DDDDDD"))
fv.setLineWidth(0.3*mm)
fv.rect(PNL + M, PH - 18*mm - 90*mm, PNL - 2*M, 88*mm, fill=0, stroke=1)

# Gold bar top
rect(fv, PNL, PH - 18*mm, PNL, 18*mm, GOLD)
txb(fv, "ZETTERBERGSGYMNASIET", PNL + PNL/2, PH - 11*mm, 7.5, DARK, align="center")

# Big title
fv.setFont("Helvetica-Bold", 30)
fv.setFillColor(BLUE_MID)
fv.drawCentredString(PNL + PNL/2, PH/2 + 5*mm, "STUDIERO")
fv.setFont("Helvetica-Bold", 22)
fv.setFillColor(GOLD)
fv.drawCentredString(PNL + PNL/2, PH/2 - 10*mm, "FÖR ALLA")

# Thin rule
fv.setStrokeColor(GOLD)
fv.setLineWidth(0.8*mm)
fv.line(PNL + M*2, PH/2 - 16*mm, PNL*2 - M*2, PH/2 - 16*mm)

# Sub-text
txt(fv, "Tillsammans skapar vi en skola", PNL + PNL/2, PH/2 - 24*mm, 8, WARM_GREY, align="center")
txt(fv, "där alla kan lära sig och trivas.", PNL + PNL/2, PH/2 - 30*mm, 8, WARM_GREY, align="center")

# Bottom badge
rect(fv, PNL + PNL/2 - 18*mm, 8*mm, 36*mm, 12*mm, GOLD, r=2*mm)
txb(fv, "Läsåret 2025–2026", PNL + PNL/2, 12.5*mm, 7, DARK, align="center")

# Right inner-flap (panel 2)
rect(fv, PNL*2, 0, PNL, PH, white)
rect(fv, PNL*2, PH - 20*mm, PNL, 20*mm, BLUE_MID)
txb(fv, "Mer information", PNL*2 + PNL/2, PH - 11*mm, 9, white, align="center")
txt(fv, "& resurser", PNL*2 + PNL/2, PH - 17*mm, 8, GOLD_LIGHT, align="center")

lx = PNL*2 + M
ly = PH - 32*mm
for heading_t, lines in [
    ("Elevhälsa", ["Må bra i skolan? Prata med", "skolkuratorn eller sköterskan."]),
    ("Studiehandledning", ["Vi hjälper dig planera dina", "studier och nå dina mål."]),
    ("Biblioteket", ["Lugn och ro för läsning,", "studier och reflektion."]),
]:
    fv.setFont("Helvetica-Bold", 8)
    fv.setFillColor(BLUE_MID)
    fv.drawString(lx, ly, heading_t)
    ly -= 5.5*mm
    for ln in lines:
        fv.setFont("Helvetica", 7.5)
        fv.setFillColor(CHARCOAL)
        fv.drawString(lx + 3*mm, ly, ln)
        ly -= 4.5*mm
    ly -= 4*mm

# School URL bottom flap
rect(fv, PNL*2, 0, PNL, 12*mm, HexColor("#F0F0F0"))
fv.setStrokeColor(HexColor("#DDDDDD"))
fv.setLineWidth(0.3*mm)
fv.line(PNL*2, 12*mm, PNL*3, 12*mm)
txt(fv, "eskilstuna.se/zetterbergsgymnasiet", PNL*2 + PNL/2, 4*mm, 6, BLUE_MID, align="center")

fold_guides(fv)
fv.showPage()

# ── PAGE 2 (inside: panel 3 | 4 | 5) ─────────────────────────────
# Panel 3 — Vad är studiero?
rect(fv, 0, 0, PNL, PH, white)
rect(fv, 0, PH - 22*mm, PNL, 22*mm, BLUE_MID)
txb(fv, "Vad är studiero?", PNL/2, PH - 13*mm, 10.5, white, align="center")
cv2_line_y = PH - 24*mm
fv.setStrokeColor(GOLD)
fv.setLineWidth(0.6*mm)
fv.line(M, cv2_line_y, PNL - M, cv2_line_y)

paras_1 = [
    ("", "Studiero innebär att alla elever och\nlärare har möjlighet att fokusera,\nlyssna och lära sig — utan störningar."),
    ("", "Det börjar med dig. Varje val du gör\ni klassrummet, korridoren eller på\nrasten påverkar alla omkring dig."),
    ("✦ Vad säger forskningen?", ""),
    ("", "Elever som upplever god studiero\nfår högre betyg, mår bättre och\ntrivs mer i skolan."),
]
py = PH - 32*mm
for heading_t, body_t in paras_1:
    if heading_t:
        fv.setFont("Helvetica-Bold", 8)
        fv.setFillColor(GOLD)
        fv.drawString(M, py, heading_t)
        py -= 6*mm
    if body_t:
        for ln in body_t.split("\n"):
            fv.setFont("Helvetica", 7.5)
            fv.setFillColor(CHARCOAL)
            fv.drawString(M + 2*mm, py, ln)
            py -= 5*mm
        py -= 3*mm

# Illustration photo in panel 3
clip_image(fv, "library.jpg", M, 22*mm, PNL - 2*M, 52*mm, BLUE_DEEP, 0.1)
fv.setStrokeColor(GOLD)
fv.setLineWidth(0.4*mm)
fv.rect(M, 22*mm, PNL - 2*M, 52*mm, fill=0, stroke=1)

# Panel 4 — Regler
rect(fv, PNL, 0, PNL, PH, white)
rect(fv, PNL, PH - 22*mm, PNL, 22*mm, YELLOW_ACC)
txb(fv, "Våra gemensamma regler", PNL + PNL/2, PH - 13*mm, 9, DARK, align="center")

rx = PNL + M
ry = PH - 30*mm
rules = [
    "1.  Kom i tid och var förberedd.",
    "2.  Ha mobilen tyst – eller stängd.",
    "3.  Lyssna när det talas.",
    "4.  Störs du, säg till snällt.",
    "5.  Jobba med egna uppgifter.",
    "6.  Prata lugnt i korridorerna.",
    "7.  Visa respekt för allas utrymme.",
    "8.  Ta ansvar för klassrumsmiljön.",
]
for rule in rules:
    shadow_rect(fv, rx, ry, PNL - 2*M, 8*mm, white, shadow_offset=0.5, r=1.5*mm)
    fv.setFont("Helvetica", 7.5)
    fv.setFillColor(BLUE_MID)
    fv.drawString(rx + 2*mm, ry + 2.5*mm, rule)
    ry -= 10.5*mm

# Quote box panel 4
rect(fv, PNL + M, 15*mm, PNL - 2*M, 20*mm, BLUE_MID, r=2*mm)
fv.setFont("Helvetica-Oblique", 8)
fv.setFillColor(white)
fv.drawCentredString(PNL + PNL/2, 28*mm, '"Respekt är grunden för')
fv.setFillColor(GOLD_LIGHT)
fv.drawCentredString(PNL + PNL/2, 22*mm, 'allt lärande."')

# Panel 5 — Tillsammans
rect(fv, PNL*2, 0, PNL, PH, white)

# Header
rect(fv, PNL*2, PH - 22*mm, PNL, 22*mm, BLUE_MID)
txb(fv, "Tillsammans kan vi", PNL*2 + PNL/2, PH - 12*mm, 10, white, align="center")
txb(fv, "göra skillnad!", PNL*2 + PNL/2, PH - 19*mm, 10, GOLD, align="center")

# Photo
clip_image(fv, "classroom.jpg", PNL*2 + M, PH - 80*mm, PNL - 2*M, 52*mm, BLUE_DEEP, 0.2)
fv.setStrokeColor(GOLD)
fv.setLineWidth(0.4*mm)
fv.rect(PNL*2 + M, PH - 80*mm, PNL - 2*M, 52*mm, fill=0, stroke=1)

ty = PH - 90*mm
tx = PNL*2 + M
tips = [
    ("Tänk på:", True),
    ("Ditt beteende smittar av sig.", False),
    ("Positiva val skapar positiv miljö.", False),
    ("", False),
    ("Vad KAN du göra?", True),
    ("Uppmuntra en klasskamrat.", False),
    ("Välj en lugn plats att studera.", False),
    ("Säg till om något stör dig.", False),
    ("Hjälp till att hålla det rent.", False),
]
for line, bold in tips:
    if not line:
        ty -= 3*mm
        continue
    fv.setFont("Helvetica-Bold" if bold else "Helvetica", 7.5)
    fv.setFillColor(BLUE_MID if bold else CHARCOAL)
    fv.drawString(tx, ty, line)
    ty -= 5.5*mm

# Bottom stamp
rect(fv, PNL*2 + M, 10*mm, PNL - 2*M, 14*mm, HexColor("#F0F0F0"), r=2*mm)
fv.setStrokeColor(HexColor("#CCCCCC"))
fv.setLineWidth(0.3*mm)
fv.roundRect(PNL*2 + M, 10*mm, PNL - 2*M, 14*mm, 2*mm, fill=0, stroke=1)
txt(fv, "Zetterbergsgymnasiet", PNL*2 + PNL/2, 17*mm, 7, BLUE_MID, align="center")
txt(fv, "Eskilstuna  ·  2026", PNL*2 + PNL/2, 12*mm, 6.5, WARM_GREY, align="center")

fold_guides(fv)
fv.showPage()
fv.save()
print("✓ PUBLISHER_folder_studiero.pdf")


# ═══════════════════════════════════════════════════════════════════
# 3.  A3 COLLAGE  —  Reklamfoto (landscape)
# ═══════════════════════════════════════════════════════════════════
A3W, A3H = landscape(A3)
GM = 12*mm    # global margin
STRIP = 115*mm

av = canvas.Canvas(os.path.join(OUT, "PUBLISHER_A3_collage_reklamfoto.pdf"), pagesize=landscape(A3))

# ── Background — white ─────────────────────────────────────────────
rect(av, 0, 0, A3W, A3H, white)

# ── Top title bar ──────────────────────────────────────────────────
TB_H = 28*mm
rect(av, 0, A3H - TB_H, A3W, TB_H, BLUE_MID)
# Gold accent line
av.setStrokeColor(GOLD)
av.setLineWidth(1.2*mm)
av.line(GM, A3H - TB_H + 0.6*mm, A3W - GM, A3H - TB_H + 0.6*mm)

av.setFont("Helvetica-Bold", 38)
av.setFillColor(white)
av.drawString(GM, A3H - 19*mm, "REKLAMFOTO")
av.setFont("Helvetica", 12)
av.setFillColor(GOLD_LIGHT)
txt_sub = "Bildtyp inom grafisk kommunikation  ·  Alyaa Alsharif  ·  Zetterbergsgymnasiet"
av.drawRightString(A3W - GM, A3H - 19*mm, txt_sub)

# ── Collage image grid  (left 2/3 minus strip) ─────────────────────
CX = GM
CY = GM
CW = A3W - STRIP - 2*GM
CH = A3H - TB_H - 2*GM
GAP = 4*mm

# 4 images: top-left, top-right, bottom-left, bottom-right
# top row: taller, bottom row: shorter
TOP_H  = CH * 0.58
BOT_H  = CH - TOP_H - GAP
HALF_W = (CW - GAP) / 2

SLOTS = [
    (CX,               CY + BOT_H + GAP, HALF_W, TOP_H, "ad_fashion.jpg",   "Modefoto",    "Kläder, AccessoArer, Kosmetika"),
    (CX + HALF_W + GAP, CY + BOT_H + GAP, HALF_W, TOP_H, "ad_product.jpg",   "Produktfoto", "Elektronik, Livsmedel, Varor"),
    (CX,               CY,               HALF_W, BOT_H, "ad_lifestyle.jpg", "Livsstilsfoto","Produkt i Verklig Miljö"),
    (CX + HALF_W + GAP, CY,               HALF_W, BOT_H, "ad_food.jpg",      "Matfoto",     "Restauranger & Livsmedel"),
]

LABEL_H = 16*mm   # height reserved at bottom of each tile for label

for sx, sy, sw, sh, fname, cat_title, cat_desc in SLOTS:
    photo_h = sh - LABEL_H
    photo_y = sy + LABEL_H

    # Drop shadow (solid, no alpha — reportlab compatible)
    av.setFillColor(HexColor("#DDDDDD"))
    av.rect(sx + 2*mm, sy - 2*mm, sw, sh, fill=1, stroke=0)

    # Photo — full width, reduced height (top portion of tile)
    clip_image(av, fname, sx, photo_y, sw, photo_h)

    # Label strip at bottom — white background
    rect(av, sx, sy, sw, LABEL_H, white)
    av.setStrokeColor(HexColor("#EEEEEE"))
    av.setLineWidth(0.3*mm)
    av.line(sx, sy + LABEL_H, sx + sw, sy + LABEL_H)

    # Gold accent bar at top of label strip
    rect(av, sx, sy + LABEL_H - 2*mm, sw, 2*mm, GOLD)

    # Category label text
    av.setFont("Helvetica-Bold", 9.5)
    av.setFillColor(BLUE_MID)
    av.drawString(sx + 3*mm, sy + LABEL_H - 8*mm, cat_title)
    av.setFont("Helvetica", 7)
    av.setFillColor(WARM_GREY)
    av.drawString(sx + 3*mm, sy + 2.5*mm, cat_desc)

    # Gold corner bracket on photo (top-left)
    av.setStrokeColor(GOLD)
    av.setLineWidth(0.7*mm)
    blen = 7*mm
    av.line(sx, photo_y + photo_h, sx + blen, photo_y + photo_h)
    av.line(sx, photo_y + photo_h, sx, photo_y + photo_h - blen)
    # Bottom-right bracket of photo
    av.line(sx + sw, photo_y, sx + sw - blen, photo_y)
    av.line(sx + sw, photo_y, sx + sw, photo_y + blen)

    # Border around entire tile
    av.setStrokeColor(HexColor("#CCCCCC"))
    av.setLineWidth(0.3*mm)
    av.rect(sx, sy, sw, sh, fill=0, stroke=1)

# ── Right info strip ────────────────────────────────────────────────
SX = A3W - STRIP
SY = 0
SH = A3H - TB_H

rect(av, SX, SY, STRIP, SH, HexColor("#F7F7F7"))
# Separator line
av.setStrokeColor(GOLD)
av.setLineWidth(0.8*mm)
av.line(SX, SY, SX, SH)

TX2 = SX + 8*mm
TW2 = STRIP - 16*mm

# Section heading helper
def strip_heading(c, text, y):
    c.setFillColor(BLUE_MID)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(TX2, y, text)
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.3*mm)
    c.line(TX2, y - 2*mm, TX2 + TW2, y - 2*mm)
    return y - 7*mm

def strip_body(c, text, y, size=7.5, col=HexColor("#444444")):
    c.setFont("Helvetica", size)
    c.setFillColor(col)
    words = text.split()
    line = ""
    cy = y
    for w in words:
        test = (line + " " + w).strip()
        if c.stringWidth(test, "Helvetica", size) <= TW2:
            line = test
        else:
            if line:
                c.drawString(TX2, cy, line)
                cy -= size * 1.5
            line = w
    if line:
        c.drawString(TX2, cy, line)
    return cy - size * 2.2

y = SH - 12*mm

y = strip_heading(av, "Vad är reklamfoto?", y)
y = strip_body(av, "Reklamfoto är professionellt planerade bilder vars syfte är att marknadsföra en produkt, tjänst eller ett varumärke.", y)
y -= 2*mm
y = strip_body(av, "Till skillnad från ett dokumentärfoto är ingenting slumpmässigt — belysning, komposition, modell och miljö är alla noggrant styrda.", y)

y -= 6*mm
y = strip_heading(av, "Hur används det?", y)
for item in [
    "• Tidningsannonser & affischer",
    "• E-handel & produktsidor",
    "• Sociala medier (Instagram, TikTok)",
    "• Förpackningsdesign & kataloger",
    "• Outdoor-reklam & skyltar",
]:
    av.setFont("Helvetica", 7.5)
    av.setFillColor(CHARCOAL)
    av.drawString(TX2, y, item)
    y -= 5.5*mm

y -= 4*mm
y = strip_heading(av, "Syfte", y)
y = strip_body(av, "Reklambildens primära syfte är kommersiellt — att påverka betraktaren att köpa, välja eller minnas ett varumärke.", y)
y -= 2*mm
y = strip_body(av, "Fotografen samarbetar nära art directors för att säkerställa att bilden matchar varumärkets identitet och målgruppens förväntningar.", y)

y -= 6*mm
y = strip_heading(av, "De fyra underkategorierna", y)
categories = [
    ("Modefoto",     "Kläder, accessoarer och kosmetika."),
    ("Produktfoto",  "Elektronik, mat och industriprodukter."),
    ("Livsstilsfoto","Produkten visas i en verklig vardagsmiljö."),
    ("Matfoto",      "Restauranger, livsmedel och dryck."),
]
for cat, desc in categories:
    av.setFont("Helvetica-Bold", 8)
    av.setFillColor(BLUE_MID)
    av.drawString(TX2, y, cat + ":")
    av.setFont("Helvetica", 7.5)
    av.setFillColor(CHARCOAL)
    av.drawString(TX2 + 22*mm, y, desc)
    y -= 6*mm

y -= 4*mm
y = strip_heading(av, "Tekniska aspekter", y)
y = strip_body(av, "Studio- eller naturligt ljus används beroende på stil. Retuschering i Photoshop är standard för att uppnå det perfekta slutresultatet.", y)

# ── Bottom bar ─────────────────────────────────────────────────────
rect(av, 0, 0, A3W, 9*mm, HexColor("#F0F0F0"))
av.setStrokeColor(HexColor("#CCCCCC"))
av.setLineWidth(0.3*mm)
av.line(0, 9*mm, A3W, 9*mm)
av.setFont("Helvetica", 6.5)
av.setFillColor(HexColor("#777777"))
av.drawString(GM, 3*mm, "Alyaa Alsharif  ·  Grafisk kommunikation  ·  Zetterbergsgymnasiet, Köpmangatan 8, 632 20 Eskilstuna  ·  2026")
av.drawRightString(A3W - GM, 3*mm, "Bildtyp: Reklamfoto  ·  Uppgift A3 collage")

av.showPage()
av.save()
print("✓ PUBLISHER_A3_collage_reklamfoto.pdf")

print("\n✅ Alla tre filer klara med riktiga foton och riktig information!")
