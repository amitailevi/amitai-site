#!/usr/bin/env python3
"""Generate posts 07-10 from real email data."""
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display as bidi
import os

W, H = 1080, 1080
OUT = os.path.dirname(os.path.abspath(__file__))
FONTS = "/tmp/heebo-fonts"
def f(w, s): return ImageFont.truetype(f"{FONTS}/heebo-{w}.ttf", s)

NAVY = (13, 27, 42); BLUE = (26, 58, 92); GOLD = (212, 168, 67)
WHITE = (255, 255, 255); BLACK = (0, 0, 0); LIGHT = (248, 249, 250)

def tc(d, text, y, fnt, fill, w=W):
    bb = d.textbbox((0,0), text, font=fnt)
    tw = bb[2]-bb[0]
    d.text(((w-tw)//2, y), text, font=fnt, fill=fill)
    return bb[3]-bb[1]

def gold_line(d, y, w=120, h=3):
    x = (W-w)//2
    d.rectangle([x, y, x+w, y+h], fill=GOLD)

def footer(d):
    d.rectangle([0, H-80, W, H], fill=NAVY)
    tc(d, "amitailevi.com", H-60, f(700, 28), GOLD)
    gold_line(d, H-80, 60, 2)

def vgradient(d, c1, c2):
    for y in range(H):
        t = y/H
        c = tuple(int(c1[i]+(c2[i]-c1[i])*t) for i in range(3))
        d.line([(0,y),(W,y)], fill=c)

# ─── 07: 184 families in 72 hours ───
def p07():
    img = Image.new("RGB", (W,H), NAVY)
    d = ImageDraw.Draw(img)
    vgradient(d, NAVY, BLUE)
    y = 100
    tc(d, bidi("72 שעות."), y, f(900, 70), GOLD)
    y += 100
    tc(d, bidi("184 משפחות."), y, f(900, 70), WHITE)
    y += 100
    gold_line(d, y, 200, 3)
    y += 50
    tc(d, bidi("מערכת הרשמה חדשה."), y, f(700, 42), (191,191,191))
    y += 60
    tc(d, bidi("הורה סוגר הרשמה ותשלום"), y, f(400, 36), (153,153,153))
    y += 50
    tc(d, bidi("ב-5 דקות מהסלון."), y, f(700, 40), GOLD)
    y += 80
    tc(d, bidi("שיא: 138 הרשמות ביום אחד"), y, f(300, 30), (140,140,140))
    y += 40
    tc(d, bidi("שיא שעתי: 36 הרשמות בשעה"), y, f(300, 30), (140,140,140))
    footer(d)
    return img

# ─── 08: 612 kids Passover camp ───
def p08():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    y = 100
    bw, bh = 400, 50
    bx = (W-bw)//2
    d.rounded_rectangle([bx, y, bx+bw, y+bh], 25, fill=GOLD)
    tc(d, bidi("קייטנת פסח תשפ״ו"), y+8, f(700, 28), WHITE)
    y += 100
    tc(d, "612", y, f(900, 140), NAVY)
    y += 150
    tc(d, bidi("ילדים נרשמו"), y, f(700, 48), NAVY)
    y += 80
    gold_line(d, y, 160, 3)
    y += 40
    tc(d, bidi("4 בתי ספר | 6 ישובים | 30+ גנים"), y, f(400, 30), (100,100,100))
    y += 50
    tc(d, bidi("מועצה אזורית באר טוביה"), y, f(400, 30), GOLD)
    y += 50
    tc(d, bidi("כפיר צהרונים"), y, f(700, 34), NAVY)
    footer(d)
    return img

# ─── 09: Dr. Regina Hason ───
def p09():
    img = Image.new("RGB", (W,H), NAVY)
    d = ImageDraw.Draw(img)
    y = 130
    tc(d, bidi("מינוי חדש"), y, f(900, 52), GOLD)
    y += 80
    gold_line(d, y, 160, 2)
    y += 40
    tc(d, bidi("ד״ר רגינה חסון"), y, f(900, 60), WHITE)
    y += 85
    tc(d, bidi("מנהלת פדגוגית"), y, f(700, 44), GOLD)
    y += 70
    tc(d, bidi("כפיר צהרונים"), y, f(400, 36), (191,191,191))
    y += 80
    gold_line(d, y, 100, 2)
    y += 40
    lines = [
        bidi("כי חינוך מתחיל מלמעלה."),
        bidi("ניהול פדגוגי מקצועי,"),
        bidi("בגובה העיניים של הצוותים."),
    ]
    for l in lines:
        tc(d, l, y, f(400, 32), (153,153,153))
        y += 48
    footer(d)
    return img

# ─── 10: The team ───
def p10():
    img = Image.new("RGB", (W,H), LIGHT)
    d = ImageDraw.Draw(img)
    y = 90
    tc(d, bidi("הצוות שמאחורי ההצלחה"), y, f(900, 48), NAVY)
    y += 75
    gold_line(d, y, 200, 3)
    y += 40
    team = [
        (bidi("מירי לוי"), bidi("עו״ד, מנהלת המשרד")),
        (bidi("מרים כוכב"), bidi("מנהלת כספים ורישום")),
        (bidi("שלומית צוקר"), bidi("מנהלת משאבי אנוש")),
        (bidi("ד״ר רגינה חסון"), bidi("מנהלת פדגוגית")),
    ]
    for name, role in team:
        tc(d, name, y, f(700, 36), NAVY)
        y += 42
        tc(d, role, y, f(300, 28), (100,100,100))
        y += 55
    y += 10
    gold_line(d, y, 140, 3)
    y += 35
    lines = [
        bidi("בלעדיהן — אין קייטנה,"),
        bidi("אין צהרון, אין חינוך."),
    ]
    for l in lines:
        tc(d, l, y, f(700, 34), GOLD)
        y += 48
    footer(d)
    return img

for name, func in [
    ("07-system-launch.png", p07),
    ("08-passover-camp.png", p08),
    ("09-regina.png", p09),
    ("10-team.png", p10),
]:
    img = func()
    path = f"{OUT}/{name}"
    img.save(path, "PNG", optimize=True)
    print(f"  {name} ({os.path.getsize(path)//1024}KB)")
print("4 extra posts ready!")
