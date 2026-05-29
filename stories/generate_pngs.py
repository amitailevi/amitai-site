#!/usr/bin/env python3
"""Generate story PNG images (1080x1920) with proper RTL Hebrew."""
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display
import os

W, H = 1080, 1920
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
FONTS = "/tmp/heebo-fonts"

def f(weight, size):
    return ImageFont.truetype(f"{FONTS}/heebo-{weight}.ttf", size)

def bidi(text):
    return get_display(text)

# Colors
NAVY = (13, 27, 42)
BLUE = (26, 58, 92)
GOLD = (212, 168, 67)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DIM_WHITE = (191, 191, 191)
GRAY = (140, 140, 140)
LIGHT_GRAY = (153, 153, 153)
MID_GRAY = (178, 178, 178)
HALF_WHITE = (128, 128, 128)

def tc(draw, text, y, fnt, fill):
    """Text centered. Returns height."""
    bb = draw.textbbox((0, 0), text, font=fnt)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    draw.text(((W - tw) // 2, y), text, font=fnt, fill=fill)
    return th

def gold_line(d, y, w=120, h=3):
    x = (W - w) // 2
    d.rectangle([x, y, x + w, y + h], fill=GOLD)

def vgradient(d, c1, c2, y0=0, y1=H):
    for y in range(y0, y1):
        t = (y - y0) / (y1 - y0)
        c = tuple(int(c1[i] + (c2[i]-c1[i])*t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)

# ─── STORIES ───

def s01():
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    fnt = f(700, 64)
    lines = [bidi("היום יוצא משהו"), bidi("שחיכיתי לו.")]
    y = H // 2 - 100
    for l in lines:
        tc(d, l, y, fnt, WHITE); y += 105
    return img

def s02():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    vgradient(d, NAVY, BLUE, 0, int(H*0.6))
    vgradient(d, BLUE, NAVY, int(H*0.6), H)
    y = H // 2 - 150
    tc(d, bidi("שנים בשטח."), y, f(700, 72), DIM_WHITE)
    gold_line(d, y + 100)
    tc(d, bidi("עכשיו הסיפור"), y + 155, f(700, 56), GOLD)
    tc(d, bidi("יוצא החוצה."), y + 240, f(700, 56), GOLD)
    gold_line(d, y + 340, 80, 2)
    return img

def s03():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    y = H // 2 - 280
    tc(d, bidi("ראיון בלעדי"), y, f(700, 42), GOLD)
    gold_line(d, y + 65, 200, 2)
    tc(d, bidi("הבלוף של התעשייה"), y + 120, f(900, 72), WHITE)
    tc(d, bidi("נחשף"), y + 215, f(900, 72), WHITE)
    gold_line(d, y + 310, 200, 2)
    tc(d, bidi("עיתון Talk | סיוון תשפ״ו"), y + 365, f(300, 36), GRAY)
    tc(d, bidi("הסיפור המלא בלינק"), y + 430, f(700, 38), GOLD)
    return img

def s04():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    qf = f(700, 54)
    y = H // 2 - 230
    # Big quote mark
    tc(d, bidi("״"), y - 140, f(900, 160), GOLD)
    lines = [
        bidi("אני לא יושב במשרד ממוזג."),
        bidi("המשרד שלי הוא"),
        bidi("אשכולות הגנים.")
    ]
    for l in lines:
        tc(d, l, y, qf, WHITE); y += 90
    gold_line(d, y + 30, 140, 3)
    tc(d, bidi("— אמיתי לוי, עיתון Talk"), y + 80, f(400, 34), GOLD)
    return img

def s05():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)
    qf = f(700, 52)
    lines = [
        bidi("כשסייעת שמחה — הילד שמח."),
        bidi("כשהיא עצובה — הילד עצוב."),
        bidi("לכן אצלנו"),
        bidi("הסייעת היא המלכה.")
    ]
    y = H // 2 - 200
    for l in lines:
        tc(d, l, y, qf, NAVY); y += 95
    gold_line(d, y + 20, 160, 4)
    tc(d, bidi("— אמיתי לוי"), y + 70, f(400, 34), GOLD)
    return img

def s07():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    vgradient(d, NAVY, BLUE)
    y = H // 2 - 280
    tc(d, bidi("השקנו אתר חדש"), y, f(700, 48), WHITE)
    y += 100
    # White card
    cw, ch = 700, 260
    cx = (W - cw) // 2
    d.rounded_rectangle([cx, y, cx+cw, y+ch], 28, fill=WHITE, outline=GOLD, width=4)
    tc(d, bidi("אמיתי לוי"), y + 50, f(900, 56), NAVY)
    tc(d, bidi("מחזירים את החיוך לחינוך"), y + 140, f(700, 36), GOLD)
    y += ch + 55
    tc(d, "amitailevi.com", y, f(900, 52), GOLD)
    tc(d, bidi("לינק בביו"), y + 80, f(400, 38), MID_GRAY)
    return img

def s08():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    sf = f(900, 110)
    lines = [bidi("מחזירים"), bidi("את החיוך"), bidi("לחינוך")]
    y = H // 2 - 250
    gold_line(d, y - 30, 360, 3)
    for l in lines:
        tc(d, l, y, sf, GOLD); y += 155
    gold_line(d, y + 10, 360, 3)
    tc(d, "amitailevi.com", y + 70, f(300, 34), LIGHT_GRAY)
    return img

def s09():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)
    y = H // 2 - 250
    tc(d, bidi("תשתפו."), y, f(700, 56), NAVY)
    y += 90
    tc(d, bidi("תגיבו."), y, f(700, 66), NAVY)
    y += 100
    tc(d, bidi("תתייגו הורה שצריך לדעת."), y, f(900, 60), NAVY)
    y += 130
    # Gold button
    bw, bh = 600, 100
    bx = (W - bw) // 2
    d.rounded_rectangle([bx, y, bx+bw, y+bh], 50, fill=GOLD)
    tc(d, "amitailevi.com", y + 18, f(900, 44), WHITE)
    tc(d, bidi("מחזירים את החיוך לחינוך"), y + bh + 30, f(400, 30), BLUE)
    return img

def s10():
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    y = H // 2 - 100
    tc(d, bidi("תודה לכל מי ששלח, שיתף, כתב."), y, f(700, 50), WHITE)
    tc(d, bidi("הדרך רק מתחילה."), y + 110, f(700, 52), GOLD)
    tc(d, bidi("שבת שלום"), y + 230, f(300, 36), HALF_WHITE)
    return img

# ─── Generate ───
stories = [
    ("story-01-teaser.png", s01),
    ("story-02-hint.png", s02),
    ("story-03-article-reveal.png", s03),
    ("story-04-quote1.png", s04),
    ("story-05-quote2.png", s05),
    ("story-07-website.png", s07),
    ("story-08-slogan.png", s08),
    ("story-09-cta.png", s09),
    ("story-10-thanks.png", s10),
]

os.makedirs(OUT, exist_ok=True)
for name, func in stories:
    img = func()
    path = f"{OUT}/{name}"
    img.save(path, "PNG", optimize=True)
    print(f"  {name} ({os.path.getsize(path)//1024}KB)")
print(f"\n{len(stories)} images -> {OUT}")
