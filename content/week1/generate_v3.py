#!/usr/bin/env python3
"""V3: Campaign-grade posts. Each one a different world."""
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display as bidi
import os, math

W, H = 1080, 1080
OUT = os.path.dirname(os.path.abspath(__file__))
FONTS = "/tmp/heebo-fonts"
f = lambda w, s: ImageFont.truetype(f"{FONTS}/heebo-{w}.ttf", s)

# Color systems per post
NAVY = (13, 27, 42); GOLD = (212, 168, 67); WHITE = (255,255,255)
BLACK = (0,0,0); CHARCOAL = (30,30,30)

def tc(d, text, y, fnt, fill, w=W, anchor=None):
    bb = d.textbbox((0,0), text, font=fnt)
    x = (w - bb[2] + bb[0]) // 2
    d.text((x, y), text, font=fnt, fill=fill)
    return bb[3] - bb[1]

def tr(d, text, x, y, fnt, fill):
    """Right-aligned text"""
    d.text((x, y), text, font=fnt, fill=fill, anchor="ra")

def tl(d, text, x, y, fnt, fill):
    """Left-aligned text"""
    d.text((x, y), text, font=fnt, fill=fill)

def vgrad(d, c1, c2, y0=0, y1=H):
    for y in range(y0, y1):
        t = (y-y0)/max(y1-y0,1)
        d.line([(0,y),(W,y)], fill=tuple(int(c1[i]+(c2[i]-c1[i])*t) for i in range(3)))

def hgrad(d, c1, c2, x0, x1, y0, y1):
    for x in range(x0, x1):
        t = (x-x0)/max(x1-x0,1)
        c = tuple(int(c1[i]+(c2[i]-c1[i])*t) for i in range(3))
        d.line([(x,y0),(x,y1)], fill=c)

def brand(d, y=H-55):
    d.text((W//2, y), "amitailevi.com", font=f(700,20), fill=GOLD, anchor="mm")

# ══════════════════════════════════════
# 01: THE BIG NUMBER — 612 billboard
# ══════════════════════════════════════
def p01():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    # Gold accent bar top
    d.rectangle([0,0,W,8], fill=GOLD)
    # Giant number
    tc(d, "612", 80, f(900,340), NAVY)
    # Underline
    d.rectangle([200, 430, 880, 434], fill=GOLD)
    # Text
    tc(d, bidi("ילדים נרשמו לקייטנת פסח."), 470, f(700,46), NAVY)
    tc(d, bidi("מועצה אזורית באר טוביה."), 540, f(400,34), (120,120,120))
    # Bottom data strip
    d.rectangle([0, 680, W, H], fill=NAVY)
    cols = [
        ("4", bidi("בתי ספר")),
        ("6", bidi("ישובים")),
        ("30+", bidi("גנים")),
        ("315", bidi("חדשים")),
    ]
    cw = W // 4
    for i, (num, label) in enumerate(cols):
        cx = i * cw + cw // 2
        d.text((cx, 720), num, font=f(900,60), fill=GOLD, anchor="mm")
        d.text((cx, 780), label, font=f(300,22), fill=(180,180,180), anchor="mm")
        if i < 3:
            d.line([(cw*(i+1), 700),(cw*(i+1), 800)], fill=(40,60,80), width=1)
    brand(d, H-40)
    return img

# ══════════════════════════════════════
# 02: SPLIT — "בחרה בכפיר"
# ══════════════════════════════════════
def p02():
    img = Image.new("RGB", (W,H), BLACK)
    d = ImageDraw.Draw(img)
    # Left half gold, right half black
    d.rectangle([0, 0, 420, H], fill=GOLD)
    # Vertical text on gold side
    d.text((210, 200), bidi("מכרז"), font=f(900,70), fill=WHITE, anchor="mm")
    d.text((210, 290), "16/2025", font=f(900,50), fill=(180,140,40), anchor="mm")
    d.text((210, 400), bidi("מועצה"), font=f(400,32), fill=WHITE, anchor="mm")
    d.text((210, 445), bidi("אזורית"), font=f(400,32), fill=WHITE, anchor="mm")
    d.text((210, 490), bidi("באר טוביה"), font=f(700,36), fill=WHITE, anchor="mm")
    # Right side
    d.text((750, 280), bidi("בחרה"), font=f(900,80), fill=WHITE, anchor="mm")
    d.text((750, 390), bidi("בכפיר"), font=f(900,80), fill=GOLD, anchor="mm")
    d.text((750, 480), bidi("צהרונים."), font=f(900,60), fill=GOLD, anchor="mm")
    # Bottom quote
    d.rectangle([420, 680, W, 682], fill=GOLD)
    d.text((750, 730), bidi("זו לא רק זכייה במכרז."), font=f(400,28), fill=(140,140,140), anchor="mm")
    d.text((750, 775), bidi("זו הצבעת אמון."), font=f(700,32), fill=WHITE, anchor="mm")
    brand(d, H-40)
    return img

# ══════════════════════════════════════
# 03: RAW EMOTION — "מתרגש נורא"
# ══════════════════════════════════════
def p03():
    img = Image.new("RGB", (W,H), CHARCOAL)
    d = ImageDraw.Draw(img)
    vgrad(d, (15,15,15), (35,35,35))
    # Date stamp
    d.text((W//2, 120), "30.07.2025", font=f(300,30), fill=(70,70,70), anchor="mm")
    # The email
    d.rectangle([100, 200, W-100, 420], outline=(50,50,50), width=1)
    d.rectangle([100, 200, W-100, 250], fill=(40,40,40))
    d.text((W-120, 218), bidi("הודעת מועצה — מכרז צהרונים"), font=f(400,22), fill=(120,120,120), anchor="ra")
    d.text((W-120, 280), bidi("אמיתי שלום רב,"), font=f(400,26), fill=(160,160,160), anchor="ra")
    d.text((W-120, 320), bidi("מצורף מכתב החלטת המועצה"), font=f(400,26), fill=(160,160,160), anchor="ra")
    d.text((W-120, 360), bidi("בנושא מכרז הצהרונים. בהצלחה."), font=f(400,26), fill=(160,160,160), anchor="ra")
    # The response - BIG
    d.text((W//2, 550), bidi("״תודה רבה."), font=f(900,72), fill=WHITE, anchor="mm")
    d.text((W//2, 660), bidi("מתרגש נורא.״"), font=f(900,72), fill=GOLD, anchor="mm")
    # Subtle
    d.rectangle([380, 780, 700, 782], fill=GOLD)
    d.text((W//2, 820), bidi("יש רגעים שמסכמים שנים של עבודה"), font=f(400,24), fill=(100,100,100), anchor="mm")
    d.text((W//2, 855), bidi("במשפט אחד."), font=f(700,26), fill=(140,140,140), anchor="mm")
    brand(d)
    return img

# ══════════════════════════════════════
# 04: MAP PRESENCE — 4 cities
# ══════════════════════════════════════
def p04():
    img = Image.new("RGB", (W,H), (248,248,248))
    d = ImageDraw.Draw(img)
    d.rectangle([0,0,W,8], fill=NAVY)
    tc(d, bidi("נוכחות ארצית."), 50, f(900,56), NAVY)
    tc(d, bidi("לא חברת ענק. יזם אחד. צוות מסור."), 125, f(400,26), (130,130,130))
    # 4 city cards in 2x2
    cities = [
        (NAVY, GOLD, bidi("רעננה"), bidi("צהרונים"), bidi("דתי + חרדי")),
        ((26,58,92), WHITE, bidi("באר טוביה"), bidi("צהרונים + קייטנות"), bidi("6 ישובים")),
        ((40,40,40), GOLD, bidi("אריאל"), bidi("קייטנות"), bidi("חינוכיות")),
        (GOLD, WHITE, bidi("ראש העין"), bidi("רשת גנים"), ""),
    ]
    positions = [(50,200), (555,200), (50,560), (555,560)]
    for (bg, fg, city, line1, line2), (x, y) in zip(cities, positions):
        d.rounded_rectangle([x, y, x+475, y+310], 20, fill=bg)
        d.text((x+237, y+70), city, font=f(900,56), fill=fg, anchor="mm")
        d.rectangle([x+160, y+120, x+315, y+123], fill=fg if bg!=GOLD else WHITE)
        d.text((x+237, y+165), line1, font=f(400,30), fill=(*fg[:3],) if isinstance(fg,tuple) else fg, anchor="mm")
        if line2:
            d.text((x+237, y+210), line2, font=f(300,24), fill=tuple(min(c+60,255) for c in bg), anchor="mm")
    brand(d, H-40)
    return img

# ══════════════════════════════════════
# 05: CRISIS — wartime leadership
# ══════════════════════════════════════
def p05():
    img = Image.new("RGB", (W,H), BLACK)
    d = ImageDraw.Draw(img)
    # Dramatic top
    tc(d, bidi("אפריל 2026."), 100, f(300,36), (60,60,60))
    tc(d, bidi("המלחמה בעיצומה."), 155, f(300,36), (60,60,60))
    # Center focus
    tc(d, bidi("הודעה"), 300, f(900,90), WHITE)
    tc(d, bidi("להורים."), 410, f(900,90), GOLD)
    # The message box
    d.rounded_rectangle([80, 560, W-80, 730], 16, fill=(18,18,18))
    d.rectangle([W-86, 580, W-80, 710], fill=GOLD)
    tc(d, bidi("כל חיובי אפריל יבוטלו."), 585, f(700,36), WHITE)
    tc(d, bidi("לא תראו חיוב בפועל."), 635, f(400,30), (160,160,160))
    tc(d, bidi("לא חיכינו. עשינו."), 680, f(700,28), GOLD)
    # Bottom
    d.rectangle([400, 790, 680, 792], fill=GOLD)
    tc(d, bidi("מנהיגות נמדדת ברגעי אמת."), 820, f(700,28), (100,100,100))
    brand(d)
    return img

# ══════════════════════════════════════
# 06: PEDAGOGICAL — clean, professional
# ══════════════════════════════════════
def p06():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    # Left gold bar
    d.rectangle([0, 0, 12, H], fill=GOLD)
    # Right-aligned content
    tr(d, bidi("לא רק"), W-60, 80, f(900,70), NAVY)
    tr(d, bidi("מפעיל."), W-60, 165, f(900,70), GOLD)
    d.rectangle([500, 260, W-60, 263], fill=NAVY)
    tr(d, bidi("מנחה פדגוגי וארגוני."), W-60, 290, f(700,36), (80,80,80))
    # Checklist items
    items = [
        bidi("דוחות צפייה מקצועיים"),
        bidi("ישיבות מעקב שבועיות"),
        bidi("עבודה עם אגף גיל הרך"),
        bidi("הטמעת כלים בשטח"),
    ]
    y = 400
    for item in items:
        # Gold dot
        d.ellipse([W-80, y+10, W-60, y+30], fill=GOLD)
        tr(d, item, W-100, y+5, f(400,30), (60,60,60))
        y += 65
    # Bottom dark section
    d.rectangle([0, 730, W, H], fill=NAVY)
    d.text((W//2, 790), bidi("ההבדל בין קבלן"), font=f(700,34), fill=WHITE, anchor="mm")
    d.text((W//2, 840), bidi("לבין מנהיג חינוכי."), font=f(700,34), fill=GOLD, anchor="mm")
    brand(d, H-35)
    return img

# ══════════════════════════════════════
# 07: SYSTEM — 72 hours, digital
# ══════════════════════════════════════
def p07():
    img = Image.new("RGB", (W,H), NAVY)
    d = ImageDraw.Draw(img)
    vgrad(d, (8,16,30), NAVY)
    # Giant 72
    d.text((W//2, 100), "72", font=f(900,200), fill=GOLD, anchor="mt")
    d.text((W//2, 310), bidi("שעות."), font=f(700,50), fill=(160,160,160), anchor="mm")
    # Divider
    d.rectangle([350, 380, 730, 383], fill=GOLD)
    # 184
    d.text((W//2, 440), "184", font=f(900,120), fill=WHITE, anchor="mt")
    d.text((W//2, 580), bidi("משפחות נרשמו."), font=f(700,40), fill=(160,160,160), anchor="mm")
    # Progress bar visual
    bar_y = 670
    d.rounded_rectangle([100, bar_y, W-100, bar_y+50], 25, fill=(20,35,55))
    d.rounded_rectangle([100, bar_y, 850, bar_y+50], 25, fill=GOLD)
    d.text((475, bar_y+25), bidi("מהסלון. 5 דקות. בלי טפסים."), font=f(700,22), fill=NAVY, anchor="mm")
    # Records
    d.text((350, 780), bidi("שיא יומי"), font=f(300,22), fill=(100,100,100), anchor="mm")
    d.text((350, 815), "138", font=f(900,40), fill=GOLD, anchor="mm")
    d.text((730, 780), bidi("שיא שעתי"), font=f(300,22), fill=(100,100,100), anchor="mm")
    d.text((730, 815), "36", font=f(900,40), fill=GOLD, anchor="mm")
    d.line([(540, 770),(540, 860)], fill=(30,50,70), width=1)
    brand(d)
    return img

# ══════════════════════════════════════
# 08: REGINA — appointment card
# ══════════════════════════════════════
def p08():
    img = Image.new("RGB", (W,H), (245,245,245))
    d = ImageDraw.Draw(img)
    # Top accent
    d.rectangle([0,0,W,160], fill=NAVY)
    d.text((W//2, 80), bidi("מינוי חדש"), font=f(900,52), fill=GOLD, anchor="mm")
    # Card
    d.rounded_rectangle([80, 200, W-80, 850], 24, fill=WHITE)
    d.rectangle([80, 200, W-80, 210], fill=GOLD)
    # Name
    d.text((W//2, 310), bidi("ד״ר רגינה חסון"), font=f(900,58), fill=NAVY, anchor="mm")
    d.rectangle([300, 390, 780, 393], fill=GOLD)
    d.text((W//2, 430), bidi("מנהלת פדגוגית"), font=f(700,42), fill=GOLD, anchor="mm")
    d.text((W//2, 495), bidi("כפיר צהרונים"), font=f(400,30), fill=(130,130,130), anchor="mm")
    # Role items
    roles = [
        bidi("ניהול פדגוגי מקצועי"),
        bidi("הדרכת צוותים בשטח"),
        bidi("בקרת איכות חינוכית"),
    ]
    y = 570
    for r in roles:
        d.rounded_rectangle([160, y, W-160, y+50], 8, fill=(248,248,248))
        d.text((W//2, y+25), r, font=f(400,24), fill=(80,80,80), anchor="mm")
        y += 60
    # Footer text
    d.text((W//2, 800), bidi("כי חינוך מתחיל מלמעלה."), font=f(700,28), fill=NAVY, anchor="mm")
    brand(d, H-40)
    return img

# ══════════════════════════════════════
# 09: TEAM — modern horizontal cards
# ══════════════════════════════════════
def p09():
    img = Image.new("RGB", (W,H), NAVY)
    d = ImageDraw.Draw(img)
    d.text((W//2, 70), bidi("הצוות"), font=f(900,64), fill=GOLD, anchor="mm")
    d.text((W//2, 140), bidi("שמאחורי ההצלחה."), font=f(400,30), fill=(140,140,140), anchor="mm")
    d.rectangle([380, 190, 700, 192], fill=GOLD)
    team = [
        (bidi("מירי לוי"), bidi("עו״ד | מנהלת המשרד"), (212,168,67)),
        (bidi("מרים כוכב"), bidi("מנהלת כספים ורישום"), (100,180,220)),
        (bidi("שלומית צוקר"), bidi("מנהלת משאבי אנוש"), (180,130,200)),
        (bidi("ד״ר רגינה חסון"), bidi("מנהלת פדגוגית"), (130,200,150)),
    ]
    y = 230
    for name, role, accent in team:
        d.rounded_rectangle([60, y, W-60, y+110], 14, fill=(20,35,55))
        # Accent left bar
        d.rounded_rectangle([60, y, 72, y+110], 6, fill=accent)
        d.text((W-90, y+25), name, font=f(700,34), fill=WHITE, anchor="ra")
        d.text((W-90, y+68), role, font=f(300,24), fill=(150,150,150), anchor="ra")
        # Initial circle
        d.ellipse([90, y+20, 160, y+90], fill=accent)
        initial = name[-1] if name else "?"
        d.text((125, y+55), initial, font=f(900,32), fill=WHITE, anchor="mm")
        y += 125
    y += 15
    d.text((W//2, y+10), bidi("בלעדיהן — אין כפיר."), font=f(700,30), fill=GOLD, anchor="mm")
    brand(d)
    return img

# ══════════════════════════════════════
# 10: CLOSING — decade + bold statement
# ══════════════════════════════════════
def p10():
    img = Image.new("RGB", (W,H), BLACK)
    d = ImageDraw.Draw(img)
    # Diagonal gold accent
    for i in range(8):
        d.line([(0, 200+i), (200+i, 0)], fill=GOLD, width=1)
    for i in range(8):
        d.line([(W-200-i, H), (W, H-200-i)], fill=GOLD, width=1)
    # Main content
    d.text((W//2, 160), bidi("למעלה מ"), font=f(300,32), fill=(80,80,80), anchor="mm")
    d.text((W//2, 260), bidi("עשור"), font=f(900,120), fill=GOLD, anchor="mm")
    d.text((W//2, 380), bidi("בחינוך."), font=f(900,60), fill=WHITE, anchor="mm")
    d.rectangle([350, 460, 730, 463], fill=GOLD)
    # Timeline dots
    milestones = [
        (bidi("מלבורן, אוסטרליה"), bidi("שליחות")),
        (bidi("רעננה | נס ציונה | קרית אונו"), bidi("מכרזים עירוניים")),
        (bidi("מועצה אזורית באר טוביה"), bidi("612 ילדים בקייטנה")),
    ]
    y = 510
    for main, sub in milestones:
        # Dot
        d.ellipse([W//2-6, y+8, W//2+6, y+20], fill=GOLD)
        if y < 510 + 2*80:
            d.line([(W//2, y+20),(W//2, y+80)], fill=(40,40,40), width=1)
        d.text((W//2-25, y+5), main, font=f(700,24), fill=WHITE, anchor="ra")
        d.text((W//2+25, y+5), sub, font=f(300,22), fill=(120,120,120))
        y += 80
    # Bold close
    y += 30
    d.text((W//2, y), bidi("וזו רק ההתחלה."), font=f(900,48), fill=GOLD, anchor="mm")
    brand(d)
    return img

# ─── Generate ───
for name, func in [
    ("01-612.png", p01),
    ("02-tender.png", p02),
    ("03-moment.png", p03),
    ("04-cities.png", p04),
    ("05-crisis.png", p05),
    ("06-pedagogy.png", p06),
    ("07-system.png", p07),
    ("08-regina.png", p08),
    ("09-team.png", p09),
    ("10-decade.png", p10),
]:
    img = func()
    path = f"{OUT}/{name}"
    img.save(path, "PNG", optimize=True)
    print(f"  {name} ({os.path.getsize(path)//1024}KB)")
print("\nV3 — 10 campaign-grade posts ready.")
