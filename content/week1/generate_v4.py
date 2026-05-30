#!/usr/bin/env python3
"""V4: Presidential narrative. Story of a leader. Jewish connection. Political edge."""
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display as bidi
import os, math

W, H = 1080, 1080
OUT = os.path.dirname(os.path.abspath(__file__))
FONTS = "/tmp/heebo-fonts"
f = lambda w, s: ImageFont.truetype(f"{FONTS}/heebo-{w}.ttf", s)

BLACK = (0,0,0); WHITE = (255,255,255); GOLD = (212,168,67)
NAVY = (13,27,42); BLUE = (26,58,92); CHARCOAL = (25,25,25)
CREAM = (250,245,235); DARKGOLD = (170,130,40)

def tc(d, text, y, fnt, fill, w=W):
    bb = d.textbbox((0,0), text, font=fnt)
    d.text(((w-bb[2]+bb[0])//2, y), text, font=fnt, fill=fill)
    return bb[3]-bb[1]

def brand(d, y=H-50, c=GOLD):
    d.text((W//2, y), "amitailevi.com", font=f(700,18), fill=c, anchor="mm")

def vgrad(d, c1, c2, y0=0, y1=H):
    for y in range(y0, y1):
        t = (y-y0)/max(y1-y0,1)
        d.line([(0,y),(W,y)], fill=tuple(int(c1[i]+(c2[i]-c1[i])*t) for i in range(3)))

# ══════════════════════════════════════
# 01: "שליחות" — Melbourne story
# ══════════════════════════════════════
def p01():
    img = Image.new("RGB", (W,H), BLACK)
    d = ImageDraw.Draw(img)
    vgrad(d, (5,5,5), (20,15,10))
    # Top — location
    d.text((W//2, 80), "MELBOURNE, AUSTRALIA", font=f(300,24), fill=(60,60,60), anchor="mm")
    d.rectangle([400, 110, 680, 112], fill=GOLD)
    # Main word
    tc(d, bidi("שליחות."), 180, f(900,120), WHITE)
    # Story text
    lines = [
        bidi("עמדתי מול ילדים יהודים בקצה העולם"),
        bidi("ולימדתי אותם מה זה להיות ישראלי."),
        "",
        bidi("הם לא ידעו עברית."),
        bidi("הם לא הכירו את ההמנון."),
        bidi("אבל הם ידעו דבר אחד —"),
        bidi("שמישהו בא מישראל בשבילם."),
    ]
    y = 380
    for l in lines:
        if l:
            tc(d, l, y, f(400,28), (160,160,160))
        y += 42
    # Bottom quote
    d.rectangle([300, 720, 780, 722], fill=GOLD)
    tc(d, bidi("ואז הבנתי: חינוך זו לא מקצוע."), 750, f(700,30), WHITE)
    tc(d, bidi("חינוך זו שליחות."), 800, f(900,36), GOLD)
    brand(d)
    return img

# ══════════════════════════════════════
# 02: "אני מאמין" — values statement
# ══════════════════════════════════════
def p02():
    img = Image.new("RGB", (W,H), BLACK)
    d = ImageDraw.Draw(img)
    # Bold opening
    tc(d, bidi("אני"), 60, f(300,40), (80,80,80))
    tc(d, bidi("מאמין."), 110, f(900,100), WHITE)
    d.rectangle([200, 230, 880, 233], fill=GOLD)
    # Beliefs
    beliefs = [
        bidi("שחינוך הוא הכלי הכי חזק לשנות חברה."),
        bidi("שילד שמרגיש בטוח — ילמד הכל."),
        bidi("שמנהיגות נמדדת במה שעושים"),
        bidi("כשאף אחד לא מסתכל."),
        bidi("שהקשר בין ישראל ליהודי התפוצות"),
        bidi("עובר דרך החינוך."),
    ]
    y = 290
    for b in beliefs:
        tc(d, b, y, f(400,30), (180,180,180))
        y += 48
    y += 20
    d.rectangle([350, y, 730, y+2], fill=GOLD)
    y += 30
    tc(d, bidi("ולכן אני בשטח. כל יום. כבר עשור."), y, f(700,32), GOLD)
    brand(d)
    return img

# ══════════════════════════════════════
# 03: "612 — הם בחרו" — mandate framing
# ══════════════════════════════════════
def p03():
    img = Image.new("RGB", (W,H), WHITE)
    d = ImageDraw.Draw(img)
    d.rectangle([0,0,W,6], fill=NAVY)
    # Small context
    tc(d, bidi("קייטנת פסח. מועצה אזורית באר טוביה."), 50, f(300,22), (150,150,150))
    # Giant number
    tc(d, "612", 100, f(900,280), NAVY)
    d.rectangle([250, 400, 830, 404], fill=GOLD)
    # Not just kids — families who CHOSE
    tc(d, bidi("משפחות שבחרו."), 430, f(900,56), NAVY)
    tc(d, bidi("לא בגלל פרסום. לא בגלל מחיר."), 510, f(400,28), (130,130,130))
    tc(d, bidi("בגלל שהיינו בשטח. כל יום. שנה שלמה."), 555, f(400,28), (130,130,130))
    # Bottom
    d.rectangle([0, 700, W, H], fill=NAVY)
    tc(d, bidi("זו לא סטטיסטיקה."), 730, f(700,36), WHITE)
    tc(d, bidi("זו הצבעת אמון."), 785, f(900,42), GOLD)
    brand(d, H-30, WHITE)
    return img

# ══════════════════════════════════════
# 04: "מלבורן → באר טוביה" — the journey
# ══════════════════════════════════════
def p04():
    img = Image.new("RGB", (W,H), CHARCOAL)
    d = ImageDraw.Draw(img)
    vgrad(d, (10,10,10), CHARCOAL)
    # Journey line
    d.line([(100, 540),(980, 540)], fill=(40,40,40), width=2)
    # Dots on timeline
    stops = [
        (150, "MELBOURNE", bidi("שליחות")),
        (370, bidi("רעננה"), bidi("מכרז ראשון")),
        (590, bidi("נס ציונה"), bidi("התרחבות")),
        (810, bidi("באר טוביה"), bidi("612 ילדים")),
    ]
    for x, top, bot in stops:
        d.ellipse([x-10, 530, x+10, 550], fill=GOLD)
        d.text((x, 505), top, font=f(700,22), fill=WHITE, anchor="mb")
        d.text((x, 570), bot, font=f(300,18), fill=(120,120,120), anchor="mt")
    # Above timeline
    tc(d, bidi("מלבורן"), 100, f(900,80), (50,50,50))
    d.text((W//2, 200), "→", font=f(300,60), fill=GOLD, anchor="mm")
    tc(d, bidi("באר טוביה."), 240, f(900,80), WHITE)
    tc(d, bidi("המסע של עשור."), 360, f(400,30), (100,100,100))
    # Bottom
    d.rectangle([350, 680, 730, 682], fill=GOLD)
    tc(d, bidi("לא התחלתי גדול."), 710, f(700,32), (160,160,160))
    tc(d, bidi("התחלתי עם אמונה."), 760, f(900,36), GOLD)
    brand(d)
    return img

# ══════════════════════════════════════
# 05: "ברגע אמת" — wartime, dramatic
# ══════════════════════════════════════
def p05():
    img = Image.new("RGB", (W,H), BLACK)
    d = ImageDraw.Draw(img)
    # Date
    d.text((W//2, 80), bidi("אפריל 2026"), font=f(300,28), fill=(50,50,50), anchor="mm")
    d.text((W//2, 130), bidi("המלחמה בעיצומה."), font=f(300,28), fill=(50,50,50), anchor="mm")
    # Center focus
    d.rectangle([0, 250, W, 700], fill=(10,10,10))
    d.rectangle([0, 250, 8, 700], fill=GOLD)
    tc(d, bidi("הורים מקבלים הודעה:"), 290, f(400,30), (120,120,120))
    tc(d, bidi("״כל חיובי אפריל"), 370, f(900,60), WHITE)
    tc(d, bidi("יבוטלו.״"), 450, f(900,60), GOLD)
    tc(d, bidi("לא חיכינו שיתלוננו."), 560, f(400,28), (120,120,120))
    tc(d, bidi("לא חיכינו להנחיה."), 600, f(400,28), (120,120,120))
    tc(d, bidi("עשינו את הדבר הנכון."), 650, f(700,30), WHITE)
    # Bottom
    d.rectangle([300, 770, 780, 772], fill=GOLD)
    tc(d, bidi("כי מנהיגות נמדדת"), 800, f(700,30), (140,140,140))
    tc(d, bidi("ברגעי אמת."), 845, f(900,36), GOLD)
    brand(d)
    return img

# ══════════════════════════════════════
# 06: "לא המדרש" — his real quote
# ══════════════════════════════════════
def p06():
    img = Image.new("RGB", (W,H), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([0,0,W,10], fill=NAVY)
    # Quote marks
    d.text((120, 100), "״", font=f(900,200), fill=GOLD)
    # Quote text
    tc(d, bidi("לא המדרש"), 200, f(900,72), NAVY)
    tc(d, bidi("הוא העיקר,"), 290, f(900,72), NAVY)
    tc(d, bidi("אלא המעשה."), 400, f(900,72), GOLD)
    d.text((900, 440), "״", font=f(900,120), fill=GOLD)
    # Context
    d.rectangle([200, 540, 880, 543], fill=NAVY)
    tc(d, bidi("פרקי אבות א׳, י״ז"), 570, f(300,24), (140,130,120))
    tc(d, bidi("העיקרון שמנחה אותי כל יום."), 620, f(400,28), (100,90,80))
    # Personal application
    d.rectangle([0, 730, W, H], fill=NAVY)
    tc(d, bidi("הרבה מדברים על חינוך."), 760, f(400,28), (180,180,180))
    tc(d, bidi("אני מגיע לגן ב-7 בבוקר."), 810, f(700,32), GOLD)
    brand(d, H-30, GOLD)
    return img

# ══════════════════════════════════════
# 07: "חינוך דרך הרגליים" — philosophy
# ══════════════════════════════════════
def p07():
    img = Image.new("RGB", (W,H), NAVY)
    d = ImageDraw.Draw(img)
    vgrad(d, NAVY, (8,16,30))
    tc(d, bidi("חינוך"), 100, f(900,100), WHITE)
    tc(d, bidi("עושים"), 220, f(900,100), WHITE)
    tc(d, bidi("דרך"), 340, f(900,100), (80,80,80))
    tc(d, bidi("הרגליים."), 460, f(900,100), GOLD)
    d.rectangle([200, 590, 880, 593], fill=GOLD)
    # Actions
    items = [
        bidi("נכנס לגנים. יושב עם צוותים."),
        bidi("כותב דוחות צפייה. מלווה גננות."),
        bidi("יש מפעילים שנעלמים אחרי החוזה."),
        bidi("אני נשאר."),
    ]
    y = 620
    for i, item in enumerate(items):
        c = GOLD if i == 3 else (150,150,150)
        fn = f(700,30) if i == 3 else f(400,26)
        tc(d, item, y, fn, c)
        y += 44
    brand(d)
    return img

# ══════════════════════════════════════
# 08: "הם בחרו בי" — the mandate
# ══════════════════════════════════════
def p08():
    img = Image.new("RGB", (W,H), BLACK)
    d = ImageDraw.Draw(img)
    tc(d, bidi("הם"), 80, f(300,36), (70,70,70))
    tc(d, bidi("בחרו"), 130, f(900,90), WHITE)
    tc(d, bidi("בי."), 240, f(900,90), GOLD)
    d.rectangle([380, 350, 700, 352], fill=GOLD)
    # Who chose
    choosers = [
        (bidi("מועצה אזורית באר טוביה"), bidi("מכרז 16/2025")),
        (bidi("עיריית רעננה"), bidi("צהרונים דתיים וחרדים")),
        (bidi("עיריית אריאל"), bidi("קייטנות חינוכיות")),
        (bidi("עיריית ראש העין"), bidi("רשת גנים")),
    ]
    y = 400
    for name, desc in choosers:
        d.ellipse([W//2-4, y+14, W//2+4, y+22], fill=GOLD)
        d.text((W//2-20, y+8), name, font=f(700,26), fill=WHITE, anchor="ra")
        d.text((W//2+20, y+10), desc, font=f(300,22), fill=(100,100,100))
        y += 55
    d.rectangle([200, 660, 880, 662], fill=(30,30,30))
    tc(d, bidi("לא קשרים. לא פרוטקציה."), 690, f(400,26), (120,120,120))
    tc(d, bidi("עבודה בשטח. שנה אחרי שנה."), 740, f(700,28), (160,160,160))
    tc(d, bidi("כשבוחרים בך ארבע פעמים — זה כבר מנדט."), 800, f(700,28), GOLD)
    brand(d)
    return img

# ══════════════════════════════════════
# 09: "הגשר" — Israel ↔ Diaspora
# ══════════════════════════════════════
def p09():
    img = Image.new("RGB", (W,H), NAVY)
    d = ImageDraw.Draw(img)
    # Two sides connected
    d.rectangle([0,0,W,4], fill=GOLD)
    tc(d, bidi("ישראל"), 80, f(900,70), WHITE)
    d.text((W//2, 180), "—", font=f(900,60), fill=GOLD, anchor="mm")
    tc(d, bidi("התפוצות."), 220, f(900,70), GOLD)
    d.rectangle([300, 320, 780, 323], fill=GOLD)
    # The bridge story
    lines = [
        bidi("למדתי ילדים יהודים באוסטרליה."),
        bidi("היום אני מחנך ילדים בישראל."),
        "",
        bidi("הקשר בין שני העולמות האלה"),
        bidi("הוא מה שמגדיר אותי."),
        "",
        bidi("כי ילד יהודי במלבורן וילד יהודי בבאר שבע"),
        bidi("ראויים לאותו חינוך, לאותה שליחות,"),
        bidi("לאותו מישהו שבא בשבילם."),
    ]
    y = 370
    for l in lines:
        if l:
            tc(d, l, y, f(400,26), (170,170,170))
        y += 40
    d.rectangle([350, y+10, 730, y+12], fill=GOLD)
    tc(d, bidi("חינוך בלי גבולות."), y+40, f(700,34), GOLD)
    brand(d)
    return img

# ══════════════════════════════════════
# 10: "וזו רק ההתחלה" — future
# ══════════════════════════════════════
def p10():
    img = Image.new("RGB", (W,H), BLACK)
    d = ImageDraw.Draw(img)
    # Diagonal gold
    for i in range(12):
        d.line([(0, 150+i), (150+i, 0)], fill=GOLD, width=1)
    for i in range(12):
        d.line([(W-150-i, H), (W, H-150-i)], fill=GOLD, width=1)
    # Past
    tc(d, bidi("אתמול:"), 120, f(300,28), (50,50,50))
    tc(d, bidi("שליח צעיר במלבורן."), 165, f(400,30), (80,80,80))
    # Present
    tc(d, bidi("היום:"), 260, f(300,28), (80,80,80))
    tc(d, bidi("מערכת חינוך ב-4 ערים."), 305, f(700,34), WHITE)
    tc(d, bidi("מאות צוותים. אלפי ילדים."), 355, f(400,28), (140,140,140))
    # Divider
    d.rectangle([300, 430, 780, 433], fill=GOLD)
    # Future
    tc(d, bidi("מחר:"), 480, f(300,28), GOLD)
    tc(d, bidi("וזו רק"), 550, f(900,90), WHITE)
    tc(d, bidi("ההתחלה."), 660, f(900,90), GOLD)
    # Sign off
    d.rectangle([380, 800, 700, 802], fill=GOLD)
    tc(d, bidi("אמיתי לוי"), 830, f(700,28), WHITE)
    brand(d)
    return img

# ─── Generate ───
for name, func in [
    ("01-shlichut.png", p01),
    ("02-believe.png", p02),
    ("03-mandate.png", p03),
    ("04-journey.png", p04),
    ("05-crisis.png", p05),
    ("06-quote.png", p06),
    ("07-feet.png", p07),
    ("08-chose-me.png", p08),
    ("09-bridge.png", p09),
    ("10-beginning.png", p10),
]:
    img = func()
    path = f"{OUT}/{name}"
    img.save(path, "PNG", optimize=True)
    print(f"  {name} ({os.path.getsize(path)//1024}KB)")
print("\nV4 — Presidential narrative. 10 posts ready.")
