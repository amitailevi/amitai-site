#!/usr/bin/env python3
"""V5c: TRUMP ENERGY. Raw. Aggressive. Slogan. ALL CAPS feel. Meme-grade."""
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display as bidi
import os, math

W, H = 1080, 1080
OUT = os.path.dirname(os.path.abspath(__file__))
FONTS = "/tmp/heebo-fonts"
f = lambda w, s: ImageFont.truetype(f"{FONTS}/heebo-{w}.ttf", s)

WHITE = (255,255,255); BLACK = (10,10,10); GOLD = (220,180,40)
DARKGOLD = (180,145,25); OFFWHITE = (250,248,242)

def tc(d, text, y, fnt, fill, w=W):
    bb = d.textbbox((0,0), text, font=fnt)
    d.text(((w-bb[2]+bb[0])//2, y), text, font=fnt, fill=fill)

def slogan_bar(d, y=H-100):
    """Repeating slogan — like MAGA. Every post."""
    d.rectangle([0, y, W, H], fill=BLACK)
    d.rectangle([0, y, W, y+4], fill=GOLD)
    d.text((W//2, y+28), bidi("חינוך עושים בשטח."), font=f(900,38), fill=GOLD, anchor="mm")
    d.text((W//2, y+72), bidi("אמיתי לוי | amitailevi.com"), font=f(300,20), fill=(120,120,120), anchor="mm")

# ══════════════════════════════════════
# 01: The provocation — "כולם מדברים"
# ══════════════════════════════════════
def p01():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    # No decoration. Just words hitting you.
    tc(d, bidi("כולם"), 60, f(900,140), (200,200,200))
    tc(d, bidi("מדברים."), 210, f(900,140), (200,200,200))
    # The counter
    tc(d, bidi("אני"), 430, f(900,140), BLACK)
    tc(d, bidi("נכנס"), 580, f(900,140), GOLD)
    tc(d, bidi("לגן."), 730, f(900,140), BLACK)
    slogan_bar(d)
    return img

# ══════════════════════════════════════
# 02: The number — raw power
# ══════════════════════════════════════
def p02():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    # Number SO big it barely fits
    d.text((W//2, 20), "612", font=f(900,400), fill=BLACK, anchor="mt")
    # One line under
    d.rectangle([150, 440, 930, 446], fill=GOLD)
    tc(d, bidi("ילדים."), 470, f(900,80), BLACK)
    tc(d, bidi("קייטנה אחת."), 570, f(900,60), GOLD)
    tc(d, bidi("שואלים למה? תשאלו את ההורים."), 680, f(400,30), (150,150,150))
    slogan_bar(d)
    return img

# ══════════════════════════════════════
# 03: Chazal — raw and sharp
# ══════════════════════════════════════
def p03():
    img = Image.new("RGB", (W,H), BLACK)
    d = ImageDraw.Draw(img)
    # White on black — dramatic
    tc(d, bidi("חז״ל אמרו"), 50, f(300,30), (60,60,60))
    tc(d, bidi("לא המדרש"), 120, f(900,100), WHITE)
    tc(d, bidi("אלא"), 240, f(900,100), (60,60,60))
    tc(d, bidi("המעשה."), 360, f(900,120), GOLD)
    # Sharp divider
    d.rectangle([200, 510, 880, 514], fill=GOLD)
    # The translation
    tc(d, bidi("אני תרגמתי:"), 550, f(400,30), (80,80,80))
    tc(d, bidi("תפסיק"), 610, f(900,90), WHITE)
    tc(d, bidi("לדבר."), 720, f(900,90), GOLD)
    # Slogan bar
    d.rectangle([0, H-100, W, H], fill=GOLD)
    d.rectangle([0, H-100, W, H-96], fill=WHITE)
    d.text((W//2, H-72), bidi("חינוך עושים בשטח."), font=f(900,38), fill=BLACK, anchor="mm")
    d.text((W//2, H-28), bidi("אמיתי לוי | amitailevi.com"), font=f(300,20), fill=(100,80,10), anchor="mm")
    return img

for name, func in [
    ("test-01.png", p01),
    ("test-02.png", p02),
    ("test-03.png", p03),
]:
    img = func()
    path = f"{OUT}/{name}"
    img.save(path, "PNG", optimize=True)
    print(f"  {name} ({os.path.getsize(path)//1024}KB)")
print("\nV5c — Trump energy.")
