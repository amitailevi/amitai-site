#!/usr/bin/env python3
"""V2: Elite-level posts built from real email data."""
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display as bidi
import os

W, H = 1080, 1080
OUT = os.path.dirname(os.path.abspath(__file__))
FONTS = "/tmp/heebo-fonts"
f = lambda w, s: ImageFont.truetype(f"{FONTS}/heebo-{w}.ttf", s)

NAVY = (13, 27, 42); BLUE = (26, 58, 92); GOLD = (212, 168, 67)
WHITE = (255, 255, 255); BLACK = (0, 0, 0); LIGHT = (248, 249, 250)
DARKGOLD = (180, 140, 50); CREAM = (255, 248, 235)

def tc(d, text, y, fnt, fill, w=W):
    bb = d.textbbox((0, 0), text, font=fnt)
    d.text(((w - bb[2] + bb[0]) // 2, y), text, font=fnt, fill=fill)
    return bb[3] - bb[1]

def gold_line(d, y, w=120, h=3):
    d.rectangle([(W - w) // 2, y, (W + w) // 2, y + h], fill=GOLD)

def vgrad(d, c1, c2, y0=0, y1=H):
    for y in range(y0, y1):
        t = (y - y0) / max(y1 - y0, 1)
        d.line([(0, y), (W, y)], fill=tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3)))

def footer(d):
    d.rectangle([0, H - 70, W, H], fill=NAVY)
    tc(d, "amitailevi.com", H - 50, f(700, 24), GOLD)

def badge(d, text, y, bg=GOLD, fg=WHITE):
    fnt = f(700, 24)
    bb = d.textbbox((0, 0), text, font=fnt)
    bw = bb[2] - bb[0] + 40
    bx = (W - bw) // 2
    d.rounded_rectangle([bx, y, bx + bw, y + 40], 20, fill=bg)
    tc(d, text, y + 6, fnt, fg)

# ─── 01: TENDER WIN ───
def p01():
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    vgrad(d, (5, 12, 25), NAVY)
    y = 80
    badge(d, bidi("מכרז 16/2025"), y, GOLD, WHITE)
    y += 80
    tc(d, bidi("מועצה אזורית"), y, f(400, 36), (160, 160, 160))
    y += 50
    tc(d, bidi("באר טוביה"), y, f(900, 72), WHITE)
    y += 100
    gold_line(d, y, 200, 3)
    y += 45
    tc(d, bidi("בחרה בכפיר צהרונים."), y, f(900, 52), GOLD)
    y += 90
    # Stats row
    stats = [
        ("6", bidi("ישובים")),
        ("4", bidi("בתי ספר")),
        ("30+", bidi("גנים")),
    ]
    sx = 140
    for num, label in stats:
        d.rounded_rectangle([sx, y, sx + 220, y + 120], 12, fill=(20, 40, 65))
        tc(d, num, y + 10, f(900, 50), GOLD, 220)
        fnt = f(400, 22)
        bb = d.textbbox((0, 0), label, font=fnt)
        d.text((sx + (220 - bb[2] + bb[0]) // 2, y + 72), label, font=fnt, fill=(180, 180, 180))
        sx += 270
    footer(d)
    return img

# ─── 02: THE MOMENT ───
def p02():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    vgrad(d, NAVY, (10, 20, 35))
    y = 120
    tc(d, bidi("הרגע"), y, f(900, 80), GOLD)
    y += 110
    tc(d, bidi("שהמועצה שלחה"), y, f(700, 44), (180, 180, 180))
    y += 60
    tc(d, bidi("את ההודעה."), y, f(700, 44), (180, 180, 180))
    y += 90
    gold_line(d, y, 160, 2)
    y += 50
    # Quote box
    d.rounded_rectangle([80, y, W - 80, y + 140], 16, fill=(20, 40, 65))
    d.rectangle([W - 86, y + 20, W - 80, y + 120], fill=GOLD)
    tc(d, bidi("״תודה רבה."), y + 20, f(700, 38), WHITE)
    tc(d, bidi("מתרגש נורא.״"), y + 70, f(700, 38), GOLD)
    y += 180
    tc(d, bidi("— אמיתי לוי, 30 ביולי 2025"), y, f(300, 26), (120, 120, 120))
    footer(d)
    return img

# ─── 03: 612 DATA ───
def p03():
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)
    y = 60
    badge(d, bidi("קייטנת פסח תשפ״ו"), y, NAVY, GOLD)
    y += 70
    tc(d, "612", y, f(900, 160), NAVY)
    y += 170
    tc(d, bidi("ילדים נרשמו"), y, f(700, 44), NAVY)
    y += 70
    gold_line(d, y, 200, 3)
    y += 35
    # Data grid
    rows = [
        (bidi("בתי ספר"), "370", bidi("גני ילדים"), "242"),
        (bidi("צהרון קבוע"), "297", bidi("נרשמים חדשים"), "315"),
    ]
    for label1, num1, label2, num2 in rows:
        # Left box
        d.rounded_rectangle([60, y, 520, y + 65], 10, fill=(240, 245, 250))
        d.text((80, y + 18), label1, font=f(400, 22), fill=(100, 100, 100))
        fnt = f(900, 28)
        bb = d.textbbox((0, 0), num1, font=fnt)
        d.text((500 - bb[2], y + 16), num1, font=fnt, fill=NAVY)
        # Right box
        d.rounded_rectangle([560, y, 1020, y + 65], 10, fill=(240, 245, 250))
        d.text((580, y + 18), label2, font=f(400, 22), fill=(100, 100, 100))
        bb = d.textbbox((0, 0), num2, font=fnt)
        d.text((1000 - bb[2], y + 16), num2, font=fnt, fill=NAVY)
        y += 80
    y += 10
    schools = [
        (bidi("שדות"), "112"), (bidi("מבואות"), "107"),
        (bidi("רגבים"), "105"), (bidi("יד חזון"), "46"),
    ]
    sx = 60
    for name, num in schools:
        d.rounded_rectangle([sx, y, sx + 225, y + 55], 8, fill=NAVY)
        tc(d, f"{name} | {num}", y + 12, f(700, 22), WHITE, 225)
        sx += 245
    footer(d)
    return img

# ─── 04: MULTI-CITY ───
def p04():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    vgrad(d, (5, 12, 25), NAVY)
    y = 100
    tc(d, bidi("נוכחות ארצית."), y, f(900, 60), GOLD)
    y += 90
    gold_line(d, y, 160, 2)
    y += 50
    cities = [
        (bidi("רעננה"), bidi("צהרונים | דתי + חרדי")),
        (bidi("באר טוביה"), bidi("צהרונים + קייטנות | 6 ישובים")),
        (bidi("אריאל"), bidi("קייטנות חינוכיות")),
        (bidi("ראש העין"), bidi("רשת גנים")),
    ]
    for city, desc in cities:
        d.rounded_rectangle([80, y, W - 80, y + 90], 12, fill=(20, 40, 65))
        d.rectangle([W - 86, y + 15, W - 80, y + 75], fill=GOLD)
        d.text((W - 120, y + 15), city, font=f(700, 32), fill=WHITE, anchor="ra")
        d.text((W - 120, y + 55), desc, font=f(300, 22), fill=(160, 160, 160), anchor="ra")
        y += 105
    y += 10
    tc(d, bidi("כפיר צהרונים | למעלה מעשור בשטח"), y, f(400, 26), GOLD)
    footer(d)
    return img

# ─── 05: LEADERSHIP IN CRISIS ───
def p05():
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    y = 100
    tc(d, bidi("אפריל 2026."), y, f(900, 52), (100, 100, 100))
    y += 70
    tc(d, bidi("המלחמה בעיצומה."), y, f(900, 52), (100, 100, 100))
    y += 90
    gold_line(d, y, 160, 2)
    y += 50
    tc(d, bidi("ההורים קיבלו"), y, f(700, 46), WHITE)
    y += 60
    tc(d, bidi("הודעה אישית:"), y, f(700, 46), WHITE)
    y += 80
    # Quote box
    d.rounded_rectangle([60, y, W - 60, y + 110], 14, fill=(15, 25, 40))
    d.rectangle([60, y, 66, y + 110], fill=GOLD)
    tc(d, bidi("כל חיובי חודש אפריל יבוטלו."), y + 15, f(700, 34), GOLD)
    tc(d, bidi("לא תראו חיוב בפועל בחשבונכם."), y + 60, f(400, 28), (180, 180, 180))
    y += 150
    tc(d, bidi("כי מנהיגות נמדדת ברגעי אמת."), y, f(900, 38), GOLD)
    footer(d)
    return img

# ─── 06: PEDAGOGICAL AUTHORITY ───
def p06():
    img = Image.new("RGB", (W, H), LIGHT)
    d = ImageDraw.Draw(img)
    y = 80
    badge(d, bidi("ליווי פדגוגי"), y, NAVY, GOLD)
    y += 75
    tc(d, bidi("לא רק מפעיל."), y, f(900, 56), NAVY)
    y += 75
    tc(d, bidi("מנחה פדגוגי וארגוני."), y, f(700, 40), GOLD)
    y += 80
    gold_line(d, y, 140, 3)
    y += 40
    items = [
        bidi("דוחות צפייה מקצועיים לכל גן"),
        bidi("ישיבות מעקב שבועיות עם הצוותים"),
        bidi("עבודה ישירה עם אגף גיל הרך"),
        bidi("הטמעת כלים פדגוגיים בשטח"),
    ]
    for item in items:
        d.rounded_rectangle([80, y, W - 80, y + 55], 10, fill=WHITE)
        d.rectangle([W - 86, y + 10, W - 80, y + 45], fill=GOLD)
        d.text((W - 100, y + 14), item, font=f(400, 24), fill=(60, 60, 60), anchor="ra")
        y += 65
    y += 10
    tc(d, bidi("שזה ההבדל בין קבלן לבין מנהיג חינוכי."), y, f(700, 28), NAVY)
    footer(d)
    return img

# ─── 07: SYSTEM LAUNCH ───
def p07():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    vgrad(d, NAVY, BLUE)
    y = 80
    tc(d, "72", y, f(900, 140), GOLD)
    y += 150
    tc(d, bidi("שעות"), y, f(700, 44), (180, 180, 180))
    y += 70
    gold_line(d, y, 200, 3)
    y += 45
    tc(d, "184", y, f(900, 80), WHITE)
    y += 90
    tc(d, bidi("משפחות נרשמו"), y, f(700, 40), (180, 180, 180))
    y += 70
    # Stats
    d.rounded_rectangle([120, y, 500, y + 70], 12, fill=(20, 40, 65))
    tc(d, bidi("שיא: 138 ביום אחד"), y + 18, f(700, 26), GOLD, 380)
    d.rounded_rectangle([560, y, 960, y + 70], 12, fill=(20, 40, 65))
    tc(d, bidi("שיא: 36 בשעה"), y + 18, f(700, 26), GOLD, 400)
    y += 100
    tc(d, bidi("מערכת הרשמה דיגיטלית | kfir-p.co.il"), y, f(300, 24), (120, 120, 120))
    footer(d)
    return img

# ─── 08: DR. REGINA ───
def p08():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    y = 100
    badge(d, bidi("מינוי חדש"), y, GOLD, WHITE)
    y += 75
    tc(d, bidi("ד״ר רגינה חסון"), y, f(900, 60), WHITE)
    y += 90
    gold_line(d, y, 160, 2)
    y += 45
    tc(d, bidi("מנהלת פדגוגית"), y, f(700, 48), GOLD)
    y += 65
    tc(d, bidi("כפיר צהרונים"), y, f(400, 36), (160, 160, 160))
    y += 80
    # What she does
    roles = [
        bidi("ניהול פדגוגי מקצועי"),
        bidi("הדרכת צוותים בשטח"),
        bidi("בקרת איכות חינוכית"),
    ]
    for r in roles:
        d.rounded_rectangle([180, y, W - 180, y + 50], 8, fill=(20, 40, 65))
        tc(d, r, y + 10, f(400, 26), (200, 200, 200), W - 360)
        y += 60
    y += 15
    tc(d, bidi("כי חינוך מתחיל מלמעלה."), y, f(700, 32), GOLD)
    footer(d)
    return img

# ─── 09: THE TEAM ───
def p09():
    img = Image.new("RGB", (W, H), LIGHT)
    d = ImageDraw.Draw(img)
    y = 70
    tc(d, bidi("הצוות"), y, f(900, 60), NAVY)
    y += 75
    tc(d, bidi("שמאחורי ההצלחה."), y, f(700, 38), GOLD)
    y += 65
    gold_line(d, y, 200, 3)
    y += 35
    team = [
        (bidi("מירי לוי"), bidi("עו״ד | מנהלת המשרד")),
        (bidi("מרים כוכב"), bidi("מנהלת כספים ורישום")),
        (bidi("שלומית צוקר"), bidi("מנהלת משאבי אנוש")),
        (bidi("ד״ר רגינה חסון"), bidi("מנהלת פדגוגית")),
    ]
    for name, role in team:
        d.rounded_rectangle([80, y, W - 80, y + 85], 12, fill=WHITE)
        d.rectangle([W - 86, y + 15, W - 80, y + 70], fill=GOLD)
        d.text((W - 110, y + 15), name, font=f(700, 28), fill=NAVY, anchor="ra")
        d.text((W - 110, y + 50), role, font=f(300, 22), fill=(100, 100, 100), anchor="ra")
        y += 95
    y += 5
    tc(d, bidi("בלעדיהן — אין קייטנה, אין צהרון, אין חינוך."), y, f(700, 26), GOLD)
    footer(d)
    return img

# ─── 10: DECADE ───
def p10():
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    vgrad(d, BLACK, (10, 18, 30))
    y = 100
    tc(d, bidi("למעלה מ"), y, f(400, 36), (100, 100, 100))
    y += 55
    tc(d, bidi("עשור"), y, f(900, 100), GOLD)
    y += 120
    tc(d, bidi("בחינוך."), y, f(900, 60), WHITE)
    y += 100
    gold_line(d, y, 200, 3)
    y += 50
    milestones = [
        (bidi("שליחות במלבורן"), bidi("אוסטרליה")),
        (bidi("זכייה במכרזים עירוניים"), bidi("רעננה | נס ציונה | קרית אונו")),
        (bidi("מועצה אזורית באר טוביה"), bidi("6 ישובים | 612 ילדים בקייטנה")),
    ]
    for title, sub in milestones:
        d.rounded_rectangle([80, y, W - 80, y + 75], 10, fill=(15, 25, 40))
        d.rectangle([W - 86, y + 12, W - 80, y + 63], fill=GOLD)
        d.text((W - 100, y + 12), title, font=f(700, 24), fill=WHITE, anchor="ra")
        d.text((W - 100, y + 44), sub, font=f(300, 20), fill=(140, 140, 140), anchor="ra")
        y += 85
    footer(d)
    return img

# ─── Generate all ───
for name, func in [
    ("01-tender-win.png", p01),
    ("02-the-moment.png", p02),
    ("03-612-data.png", p03),
    ("04-multi-city.png", p04),
    ("05-crisis-leadership.png", p05),
    ("06-pedagogical.png", p06),
    ("07-system-launch.png", p07),
    ("08-dr-regina.png", p08),
    ("09-team.png", p09),
    ("10-decade.png", p10),
]:
    img = func()
    path = f"{OUT}/{name}"
    img.save(path, "PNG", optimize=True)
    print(f"  {name} ({os.path.getsize(path) // 1024}KB)")
print("\n10 elite posts ready!")
