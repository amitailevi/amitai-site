#!/usr/bin/env python3
"""V5e: WITH HIS FACE. Presidential. Personal. Real."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from bidi.algorithm import get_display as bidi
import os

W, H = 1080, 1080
OUT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(os.path.dirname(OUT))
FONTS = "/tmp/heebo-fonts"
f = lambda w, s: ImageFont.truetype(f"{FONTS}/heebo-{w}.ttf", s)

WHITE = (255,255,255); BLACK = (10,10,10); GOLD = (220,180,40)
DARKGOLD = (180,145,25)

def tc(d, text, y, fnt, fill, w=W):
    bb = d.textbbox((0,0), text, font=fnt)
    d.text(((w-bb[2]+bb[0])//2, y), text, font=fnt, fill=fill)

def load_face():
    """Load and prepare the headshot"""
    img = Image.open(f"{SITE}/amitai.jpg").convert("RGBA")
    return img

# ══════════════════════════════════════
# 01: Face + "אמרו בלתי אפשרי. עשיתי."
# ══════════════════════════════════════
def p01():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    # Photo on left side, large
    face = load_face().resize((500, 500), Image.LANCZOS)
    img.paste(face, (-50, 50), face)
    # Text on right
    d.text((750, 100), bidi("אמרו"), font=f(900,70), fill=(190,190,190), anchor="mm")
    d.text((750, 180), bidi("שזה בלתי"), font=f(900,55), fill=(190,190,190), anchor="mm")
    d.text((750, 250), bidi("אפשרי."), font=f(900,70), fill=(190,190,190), anchor="mm")
    d.rectangle([600, 310, 900, 314], fill=GOLD)
    d.text((750, 370), bidi("עשיתי."), font=f(900,90), fill=BLACK, anchor="mm")
    # Bottom bar
    d.rectangle([0, 600, W, H], fill=BLACK)
    d.rectangle([0, 600, W, 604], fill=GOLD)
    tc(d, bidi("אמיתי לוי"), 650, f(900,60), GOLD)
    tc(d, bidi("מחנך · יזם · מנהיג"), 730, f(300,26), (140,140,140))
    tc(d, "amitailevi.com", 780, f(700,20), DARKGOLD)
    return img

# ══════════════════════════════════════
# 02: Face center + "4 ערים בחרו בי"
# ══════════════════════════════════════
def p02():
    img = Image.new("RGB", (W,H), BLACK)
    d = ImageDraw.Draw(img)
    # Photo - centered, cropped tighter
    face = load_face().resize((600, 600), Image.LANCZOS)
    img.paste(face, (240, 30), face)
    # Gradient overlay at bottom
    for y in range(400, H):
        alpha = min(255, int((y-400)/200 * 255))
        d.line([(0,y),(W,y)], fill=(10,10,10))
    # Text over dark area
    d.rectangle([200, 640, 880, 644], fill=GOLD)
    tc(d, bidi("4 ערים בחרו בי."), 670, f(900,60), WHITE)
    tc(d, bidi("לא ביקשתי. הם ראו תוצאות."), 750, f(400,28), (160,160,160))
    # Name
    d.rectangle([300, 830, 780, 832], fill=GOLD)
    tc(d, bidi("אמיתי לוי"), 850, f(900,36), GOLD)
    return img

# ══════════════════════════════════════
# 03: Split — face + chazal
# ══════════════════════════════════════
def p03():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    # Left half — photo
    face = load_face().resize((540, 540), Image.LANCZOS)
    img.paste(face, (0, 0), face)
    # Gold vertical divider
    d.rectangle([540, 0, 548, H], fill=GOLD)
    # Right half — quote
    rx = 810  # center of right half
    d.text((rx, 100), bidi("אם אין"), font=f(900,55), fill=BLACK, anchor="mm")
    d.text((rx, 170), bidi("אני לי —"), font=f(900,55), fill=GOLD, anchor="mm")
    d.rectangle([600, 220, W-60, 223], fill=GOLD)
    d.text((rx, 280), bidi("מי לי."), font=f(900,70), fill=BLACK, anchor="mm")
    d.text((rx, 390), bidi("הלל הזקן"), font=f(300,22), fill=(150,150,150), anchor="mm")
    d.text((rx, 440), bidi("ידע."), font=f(700,36), fill=(150,150,150), anchor="mm")
    # Bottom full width — black
    d.rectangle([0, 560, W, H], fill=BLACK)
    d.rectangle([0, 560, W, 564], fill=GOLD)
    tc(d, bidi("גם אני."), 600, f(900,80), GOLD)
    tc(d, bidi("אמיתי לוי"), 720, f(900,40), WHITE)
    tc(d, bidi("מחנך · יזם · מנהיג"), 780, f(300,22), (120,120,120))
    tc(d, "amitailevi.com", 820, f(700,18), DARKGOLD)
    return img

for name, func in [("test-01.png",p01),("test-02.png",p02),("test-03.png",p03)]:
    img = func()
    img.save(f"{OUT}/{name}", "PNG", optimize=True)
    print(f"  {name}")
print("V5e — WITH FACE.")
