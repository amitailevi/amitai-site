#!/usr/bin/env python3
"""V5d: PRESIDENT. No kindergartens. Big vision. Winner. Leader."""
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display as bidi
import os

W, H = 1080, 1080
OUT = os.path.dirname(os.path.abspath(__file__))
FONTS = "/tmp/heebo-fonts"
f = lambda w, s: ImageFont.truetype(f"{FONTS}/heebo-{w}.ttf", s)

WHITE = (255,255,255); BLACK = (10,10,10); GOLD = (220,180,40)

def tc(d, text, y, fnt, fill, w=W):
    bb = d.textbbox((0,0), text, font=fnt)
    d.text(((w-bb[2]+bb[0])//2, y), text, font=fnt, fill=fill)

def brand(d):
    d.rectangle([0, H-80, W, H], fill=BLACK)
    d.rectangle([0, H-80, W, H-76], fill=GOLD)
    d.text((W//2, H-50), bidi("אמיתי לוי"), font=f(900,32), fill=GOLD, anchor="mm")

# ══════════════════════════════════════
# 01: "אמרו שזה בלתי אפשרי"
# ══════════════════════════════════════
def p01():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    tc(d, bidi("אמרו"), 80, f(900,130), (190,190,190))
    tc(d, bidi("שזה בלתי"), 220, f(900,130), (190,190,190))
    tc(d, bidi("אפשרי."), 370, f(900,130), (190,190,190))
    d.rectangle([200, 530, 880, 536], fill=GOLD)
    tc(d, bidi("עשיתי."), 570, f(900,160), BLACK)
    brand(d)
    return img

# ══════════════════════════════════════
# 02: "4 ערים. מנדט."
# ══════════════════════════════════════
def p02():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    d.text((W//2, 50), "4", font=f(900,400), fill=BLACK, anchor="mt")
    d.rectangle([200, 460, 880, 466], fill=GOLD)
    tc(d, bidi("ערים בחרו בי."), 490, f(900,80), BLACK)
    tc(d, bidi("לא ביקשתי. לא התחנפתי."), 610, f(400,30), (150,150,150))
    tc(d, bidi("הם ראו תוצאות."), 660, f(700,36), GOLD)
    brand(d)
    return img

# ══════════════════════════════════════
# 03: Chazal — presidential
# ══════════════════════════════════════
def p03():
    img = Image.new("RGB", (W,H), BLACK)
    d = ImageDraw.Draw(img)
    tc(d, bidi("אם אין"), 80, f(900,110), WHITE)
    tc(d, bidi("אני לי —"), 210, f(900,110), GOLD)
    d.rectangle([250, 350, 830, 354], fill=GOLD)
    tc(d, bidi("מי לי."), 390, f(900,140), WHITE)
    tc(d, bidi("הלל הזקן ידע."), 580, f(400,30), (80,80,80))
    tc(d, bidi("גם אני."), 640, f(900,60), GOLD)
    d.rectangle([0, H-80, W, H], fill=GOLD)
    d.text((W//2, H-50), bidi("אמיתי לוי"), font=f(900,32), fill=BLACK, anchor="mm")
    return img

for name, func in [("test-01.png",p01),("test-02.png",p02),("test-03.png",p03)]:
    img = func()
    img.save(f"{OUT}/{name}", "PNG", optimize=True)
    print(f"  {name}")
print("V5d ready.")
