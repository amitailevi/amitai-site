#!/usr/bin/env python3
"""V5: White+Yellow. Campaign grade. Signature. Bibi+Trump energy."""
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display as bidi
import os

W, H = 1080, 1080
OUT = os.path.dirname(os.path.abspath(__file__))
FONTS = "/tmp/heebo-fonts"
f = lambda w, s: ImageFont.truetype(f"{FONTS}/heebo-{w}.ttf", s)

WHITE = (255,255,255); BLACK = (20,20,20); YELLOW = (240,190,50)
DARKYELLOW = (200,160,30); LIGHTYELLOW = (255,245,200)
GRAY = (140,140,140); LIGHTGRAY = (245,245,245)

def tc(d, text, y, fnt, fill, w=W):
    bb = d.textbbox((0,0), text, font=fnt)
    d.text(((w-bb[2]+bb[0])//2, y), text, font=fnt, fill=fill)
    return bb[3]-bb[1]

def signature(d, y=H-120):
    """Campaign signature block"""
    d.rectangle([350, y, 730, y+2], fill=YELLOW)
    d.text((W//2, y+25), bidi("אמיתי לוי"), font=f(900,36), fill=BLACK, anchor="mm")
    d.text((W//2, y+65), bidi("מחנך | יזם | שליח"), font=f(300,20), fill=GRAY, anchor="mm")
    d.text((W//2, y+95), "amitailevi.com", font=f(700,16), fill=DARKYELLOW, anchor="mm")

# ══════════════════════════════════════
# 01: Bold statement — "אני מאמין"
# ══════════════════════════════════════
def p01():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    # Yellow accent top
    d.rectangle([0,0,W,12], fill=YELLOW)
    # Personal & bold
    tc(d, bidi("הלל הזקן אמר:"), 70, f(300,26), GRAY)
    tc(d, bidi("״אם אין אני לי, מי לי.״"), 120, f(700,40), BLACK)
    d.rectangle([250, 185, 830, 188], fill=YELLOW)
    # The twist
    tc(d, bidi("אני אומר:"), 230, f(300,28), GRAY)
    tc(d, bidi("אם אתה לא"), 290, f(900,80), BLACK)
    tc(d, bidi("בגן ב-7"), 390, f(900,80), YELLOW)
    tc(d, bidi("בבוקר —"), 490, f(900,80), BLACK)
    # Punchline in yellow box
    d.rounded_rectangle([100, 610, W-100, 720], 20, fill=YELLOW)
    tc(d, bidi("אל תקרא לעצמך מחנך."), 640, f(900,44), WHITE)
    signature(d)
    return img

# ══════════════════════════════════════
# 02: The 612 = mitzvot joke
# ══════════════════════════════════════
def p02():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    d.rectangle([0,0,W,12], fill=YELLOW)
    # Fun fact badge
    d.rounded_rectangle([340, 50, 740, 100], 25, fill=YELLOW)
    tc(d, bidi("עובדה מעניינת"), 58, f(900,28), WHITE)
    # Number
    tc(d, "612", 130, f(900,240), BLACK)
    d.rectangle([250, 390, 830, 394], fill=YELLOW)
    tc(d, bidi("ילדים נרשמו לקייטנת פסח."), 415, f(700,36), BLACK)
    tc(d, bidi("באר טוביה."), 465, f(400,26), GRAY)
    # The joke
    d.rounded_rectangle([120, 530, W-120, 690], 16, fill=LIGHTYELLOW)
    tc(d, bidi("רגע — 612?"), 550, f(700,32), BLACK)
    tc(d, bidi("זה גם מספר המצוות בתורה."), 595, f(400,28), (80,80,80))
    tc(d, bidi("צירוף מקרים? 😏 גם אנחנו עושים את הכל."), 645, f(700,26), DARKYELLOW)
    signature(d)
    return img

# ══════════════════════════════════════
# 03: "לא המדרש" — sharp & clean
# ══════════════════════════════════════
def p03():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    d.rectangle([0,0,W,12], fill=YELLOW)
    # Quote
    d.text((80, 50), "״", font=f(900,180), fill=YELLOW)
    tc(d, bidi("לא המדרש"), 130, f(900,72), BLACK)
    tc(d, bidi("הוא העיקר,"), 220, f(900,72), BLACK)
    tc(d, bidi("אלא המעשה."), 320, f(900,72), YELLOW)
    d.text((940, 340), "״", font=f(900,120), fill=YELLOW)
    d.rectangle([200, 460, 880, 463], fill=YELLOW)
    tc(d, bidi("פרקי אבות"), 480, f(300,22), GRAY)
    # Translation
    tc(d, bidi("בתרגום חופשי:"), 540, f(700,26), GRAY)
    tc(d, bidi("תפסיק לדבר. תיכנס לגן."), 590, f(900,40), BLACK)
    # Yellow box punchline
    d.rounded_rectangle([100, 670, W-100, 770], 20, fill=YELLOW)
    tc(d, bidi("זה מה שאני עושה. כל בוקר. 🌅"), 695, f(900,38), WHITE)
    signature(d)
    return img

# ─── Generate ───
for name, func in [
    ("test-01.png", p01),
    ("test-02.png", p02),
    ("test-03.png", p03),
]:
    img = func()
    path = f"{OUT}/{name}"
    img.save(path, "PNG", optimize=True)
    print(f"  {name} ({os.path.getsize(path)//1024}KB)")
print("\nV5 — 3 test posts ready.")
