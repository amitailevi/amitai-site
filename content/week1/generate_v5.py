#!/usr/bin/env python3
"""V5b: Trump method. Name=brand. Massive. Few words. Gold on white. Stars."""
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display as bidi
import os, math

W, H = 1080, 1080
OUT = os.path.dirname(os.path.abspath(__file__))
FONTS = "/tmp/heebo-fonts"
f = lambda w, s: ImageFont.truetype(f"{FONTS}/heebo-{w}.ttf", s)

WHITE = (255,255,255); BLACK = (15,15,15); GOLD = (218,175,50)
DARKGOLD = (180,140,30); LIGHTGOLD = (255,240,180)
GRAY = (160,160,160)

def tc(d, text, y, fnt, fill, w=W):
    bb = d.textbbox((0,0), text, font=fnt)
    d.text(((w-bb[2]+bb[0])//2, y), text, font=fnt, fill=fill)

def star(d, cx, cy, r, fill):
    """5-point star"""
    pts = []
    for i in range(10):
        a = math.pi/2 + i * math.pi/5
        rad = r if i%2==0 else r*0.4
        pts.append((cx+rad*math.cos(a), cy-rad*math.sin(a)))
    d.polygon(pts, fill=fill)

def name_badge(d, y):
    """Trump-style name in box with stars"""
    bw, bh = 700, 90
    bx = (W-bw)//2
    # Box
    d.rectangle([bx, y, bx+bw, y+bh], fill=GOLD)
    # Name
    d.text((W//2, y+bh//2), bidi("אמיתי לוי"), font=f(900,52), fill=WHITE, anchor="mm")
    # 5 stars above
    for i in range(5):
        sx = bx + 100 + i * 130
        star(d, sx, y-25, 14, GOLD)
    # Subtitle below
    d.text((W//2, y+bh+20), bidi("מחנך · יזם · שליח"), font=f(300,22), fill=GRAY, anchor="mm")
    d.text((W//2, y+bh+50), "amitailevi.com", font=f(700,18), fill=DARKGOLD, anchor="mm")

# ══════════════════════════════════════
# 01: "בגן ב-7 בבוקר" — billboard style
# ══════════════════════════════════════
def p01():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    # Gold top bar
    d.rectangle([0,0,W,16], fill=GOLD)
    # One statement. Massive.
    tc(d, bidi("בגן."), 100, f(900,180), BLACK)
    tc(d, bidi("ב-7 בבוקר."), 300, f(900,120), GOLD)
    # Thin gold line
    d.rectangle([300, 460, 780, 464], fill=GOLD)
    # Short punch
    tc(d, bidi("כל יום. כבר עשור."), 500, f(700,40), BLACK)
    tc(d, bidi("בזמן שאחרים עוד ישנים."), 560, f(400,32), GRAY)
    # Badge
    name_badge(d, 740)
    # Bottom bar
    d.rectangle([0,H-16,W,H], fill=GOLD)
    return img

# ══════════════════════════════════════
# 02: "612" — one number, one fact
# ══════════════════════════════════════
def p02():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    d.rectangle([0,0,W,16], fill=GOLD)
    # MASSIVE number
    tc(d, "612", 30, f(900,350), BLACK)
    # Gold underline
    d.rectangle([200, 400, 880, 406], fill=GOLD)
    # One line
    tc(d, bidi("ילדים. קייטנה אחת. בחירה אחת."), 430, f(900,40), BLACK)
    # Cheeky line
    d.rounded_rectangle([180, 530, W-180, 610], 16, fill=LIGHTGOLD)
    tc(d, bidi("גם מספר המצוות. צירוף מקרים? 😏"), 550, f(700,30), DARKGOLD)
    # Badge
    name_badge(d, 740)
    d.rectangle([0,H-16,W,H], fill=GOLD)
    return img

# ══════════════════════════════════════
# 03: "לא המדרש" — quote as brand
# ══════════════════════════════════════
def p03():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    d.rectangle([0,0,W,16], fill=GOLD)
    # Big bold quote — fewer words
    tc(d, bidi("דיבורים?"), 100, f(900,120), GRAY)
    tc(d, bidi("תעזוב."), 240, f(900,140), BLACK)
    # Gold line
    d.rectangle([250, 410, 830, 416], fill=GOLD)
    # Action
    tc(d, bidi("תיכנס לגן."), 450, f(900,100), GOLD)
    # Small source
    tc(d, bidi("— פרקי אבות, בתרגום שלי"), 580, f(300,24), GRAY)
    # Badge
    name_badge(d, 740)
    d.rectangle([0,H-16,W,H], fill=GOLD)
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
print("\nV5b — Trump method. 3 posts.")
