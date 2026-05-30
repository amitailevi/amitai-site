#!/usr/bin/env python3
"""Generate week 1 social media post images (1080x1080 feed format)."""
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display as bidi
import os

W, H = 1080, 1080
OUT = os.path.dirname(os.path.abspath(__file__))
FONTS = "/tmp/heebo-fonts"

def f(weight, size):
    return ImageFont.truetype(f"{FONTS}/heebo-{weight}.ttf", size)

NAVY = (13, 27, 42)
BLUE = (26, 58, 92)
GOLD = (212, 168, 67)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT = (248, 249, 250)

def tc(d, text, y, fnt, fill, w=W):
    bb = d.textbbox((0, 0), text, font=fnt)
    tw = bb[2] - bb[0]
    d.text(((w - tw) // 2, y), text, font=fnt, fill=fill)
    return bb[3] - bb[1]

def gold_line(d, y, w=120, h=3):
    x = (W - w) // 2
    d.rectangle([x, y, x + w, y + h], fill=GOLD)

def vgradient(d, c1, c2, y0=0, y1=H):
    for y in range(y0, y1):
        t = (y - y0) / max(y1 - y0, 1)
        c = tuple(int(c1[i] + (c2[i]-c1[i])*t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)

def footer(d, y=None):
    """Brand footer bar."""
    fy = y or H - 80
    d.rectangle([0, fy, W, H], fill=NAVY)
    tc(d, "amitailevi.com", fy + 20, f(700, 28), GOLD)
    gold_line(d, fy, 60, 2)

# ─── יום א׳ — תודה + גל ראשון ───
def post_sunday():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    vgradient(d, NAVY, BLUE)
    y = 160
    tc(d, bidi("תודה על הגל!"), y, f(900, 72), GOLD)
    y += 110
    gold_line(d, y, 200, 3)
    y += 50
    lines = [
        bidi("השבוע השקנו אתר,"),
        bidi("פרסמנו כתבה,"),
        bidi("וקיבלנו אהבה שלא ציפיתי לה."),
    ]
    for l in lines:
        tc(d, l, y, f(400, 42), WHITE)
        y += 65
    y += 40
    tc(d, bidi("זו רק ההתחלה."), y, f(900, 56), GOLD)
    footer(d)
    return img

# ─── יום ב׳ — ציטוט חינוכי ───
def post_monday():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)
    y = 140
    tc(d, bidi("״"), y, f(900, 140), GOLD)
    y += 140
    lines = [
        bidi("חינוך לא עושים"),
        bidi("מהמשרד."),
        bidi("עושים אותו"),
        bidi("דרך הרגליים."),
    ]
    for l in lines:
        tc(d, l, y, f(900, 64), NAVY)
        y += 85
    y += 20
    gold_line(d, y, 140, 4)
    y += 40
    tc(d, bidi("— אמיתי לוי"), y, f(400, 32), GOLD)
    footer(d)
    return img

# ─── יום ג׳ — מאחורי הקלעים ───
def post_tuesday():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    y = 120
    # Top badge
    bw, bh = 360, 50
    bx = (W - bw) // 2
    d.rounded_rectangle([bx, y, bx+bw, y+bh], 25, fill=GOLD)
    tc(d, bidi("מאחורי הקלעים"), y + 8, f(700, 28), WHITE)
    y += 100
    tc(d, bidi("07:00 בבוקר."), y, f(900, 60), WHITE)
    y += 85
    tc(d, bidi("סיור באשכולות הגנים."), y, f(700, 46), (191,191,191))
    y += 80
    tc(d, bidi("כי הרמטכ״ל נמצא"), y, f(700, 46), (191,191,191))
    y += 65
    tc(d, bidi("בחוד החנית,"), y, f(900, 52), GOLD)
    y += 75
    tc(d, bidi("לא במגדל השן."), y, f(900, 52), GOLD)
    y += 100
    gold_line(d, y, 100, 2)
    y += 30
    tc(d, bidi("מ-1 ביולי, בשיא החום,"), y, f(300, 32), (153,153,153))
    y += 45
    tc(d, bidi("גן-גן. כיתה-כיתה. 7:00 עד 16:00."), y, f(300, 32), (153,153,153))
    footer(d)
    return img

# ─── יום ד׳ — הסיפור של בנג׳י ───
def post_wednesday():
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    y = 130
    tc(d, bidi("הסיפור של בנג׳י"), y, f(900, 56), GOLD)
    y += 90
    gold_line(d, y, 160, 2)
    y += 40
    lines = [
        bidi("בן 24 נכנס לבית המדרש"),
        bidi("במלבורן ואמר:"),
    ]
    for l in lines:
        tc(d, l, y, f(400, 38), (191,191,191))
        y += 55
    y += 15
    tc(d, bidi("״גיליתי אתמול שאני יהודי."), y, f(700, 44), WHITE)
    y += 65
    tc(d, bidi("מה זה אומר?״"), y, f(700, 44), WHITE)
    y += 90
    gold_line(d, y, 100, 2)
    y += 40
    tc(d, bidi("עד היום אנחנו חברים."), y, f(400, 36), GOLD)
    y += 50
    tc(d, bidi("ב-7 באוקטובר הוא היה"), y, f(400, 36), GOLD)
    y += 50
    tc(d, bidi("הראשון שהתקשר."), y, f(700, 36), GOLD)
    footer(d)
    return img

# ─── יום ה׳ — טיפ להורים ───
def post_thursday():
    img = Image.new("RGB", (W, H), LIGHT)
    d = ImageDraw.Draw(img)
    y = 100
    # Top badge
    bw, bh = 320, 50
    bx = (W - bw) // 2
    d.rounded_rectangle([bx, y, bx+bw, y+bh], 25, fill=NAVY)
    tc(d, bidi("טיפ להורים"), y + 8, f(700, 28), GOLD)
    y += 100
    tc(d, bidi("איך בוחרים צהרון?"), y, f(900, 56), NAVY)
    y += 90
    gold_line(d, y, 140, 3)
    y += 40
    tips = [
        (bidi("תסתכלו לצוות בעיניים."), f(700, 38), NAVY),
        ("", f(400, 20), NAVY),
        (bidi("שידוך בין גננת לסייעת"), f(400, 36), (100,100,100)),
        (bidi("הוא קריטי."), f(400, 36), (100,100,100)),
        ("", f(400, 20), NAVY),
        (bidi("אם אין כימיה —"), f(700, 38), NAVY),
        (bidi("הילדים ירגישו מיד."), f(700, 38), NAVY),
    ]
    for text, fnt, fill in tips:
        if text:
            tc(d, text, y, fnt, fill)
        y += 50
    y += 10
    gold_line(d, y, 100, 2)
    y += 30
    tc(d, bidi("מתוך ראיון בעיתון Talk"), y, f(300, 26), GOLD)
    footer(d)
    return img

# ─── יום ו׳ — שבת שלום ───
def post_friday():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    vgradient(d, NAVY, BLUE)
    y = 250
    tc(d, bidi("שבת שלום"), y, f(900, 90), GOLD)
    y += 130
    gold_line(d, y, 200, 3)
    y += 50
    tc(d, bidi("מחזירים את החיוך"), y, f(700, 46), WHITE)
    y += 65
    tc(d, bidi("לחינוך"), y, f(700, 46), WHITE)
    y += 100
    tc(d, "amitailevi.com", y, f(300, 30), (153,153,153))
    return img

# ─── Generate all ───
posts = [
    ("01-sunday-thanks.png", "יום א׳", post_sunday),
    ("02-monday-quote.png", "יום ב׳", post_monday),
    ("03-tuesday-bts.png", "יום ג׳", post_tuesday),
    ("04-wednesday-benji.png", "יום ד׳", post_wednesday),
    ("05-thursday-tip.png", "יום ה׳", post_thursday),
    ("06-friday-shabbat.png", "יום ו׳", post_friday),
]

for name, day, func in posts:
    img = func()
    path = f"{OUT}/{name}"
    img.save(path, "PNG", optimize=True)
    print(f"  {day}: {name} ({os.path.getsize(path)//1024}KB)")

print(f"\n{len(posts)} posts ready!")
