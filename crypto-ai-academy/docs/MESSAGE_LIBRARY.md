# CRYPTO × AI — Message Library

These are templates only. Sending is disabled until approved channels are connected.

## Lead — first response
שלום {{first_name}}, תודה על ההתעניינות ב-CRYPTO × AI ACADEMY.
התוכנית כוללת 52 שעות לימוד בקבוצה קטנה, במחיר 13,000 ₪. אין איתותים או הבטחות תשואה — לומדים להבין ולעבוד נכון עם ביטקוין, קריפטו, אבטחה ו-AI.
לבחירת מחזור והרשמה: {{registration_url}}

## Registration started, payment not completed
היי {{first_name}}, ההרשמה שלך למחזור {{cohort_name}} התחילה אך התשלום עדיין לא הושלם. המקום אינו שמור עד לאישור התשלום.
להמשך מאובטח: {{payment_url}}

## Payment success
{{first_name}}, התשלום התקבל בהצלחה ✅
נרשמת למחזור {{cohort_name}}.
שעות: {{time}}
מיקום: Brain Embassy, המלאכה 16, פארק אפק, ראש העין.
אישור מלא ולוח המפגשים נשלחו גם למייל.

## Payment failed
היי {{first_name}}, ניסיון התשלום עבור {{cohort_name}} לא אושר. לא בוצע חיוב מאושר ולא נשמר מקום סופי.
אפשר לנסות שוב כאן: {{payment_url}}
אם הבעיה חוזרת, המערכת תציע דרך טיפול נוספת.

## Threshold reached — cohort confirmed
בשורות טובות — מחזור {{cohort_name}} הגיע למינימום הנדרש ונפתח רשמית ✅
נתראה במפגש הראשון בתאריך {{start_date}} בשעה {{time}}.

## Cohort below minimum
שלום {{first_name}}, מחזור {{cohort_name}} לא הגיע למינימום 5 תלמידים עד מועד ההחלטה.
לא נשאיר אותך בלי פתרון: המערכת תציג לך מחזור חלופי זמין או מסלול החזר בהתאם למדיניות שאושרה בעת ההרשמה.
{{options_url}}

## Sold out
מחזור {{cohort_name}} מלא — 10/10.
אפשר להצטרף לרשימת ההמתנה או לבחור מחזור אחר: {{waitlist_url}}

## 24h reminder
תזכורת למחר 🎓
CRYPTO × AI · {{cohort_name}}
{{date}} · {{time}}
Brain Embassy, המלאכה 16, פארק אפק, ראש העין.

## No-show follow-up
היי {{first_name}}, ראינו שלא הגעת למפגש היום. מקווים שהכול בסדר.
חומרי ההשלמה והנחיות למפגש הבא נמצאים כאן: {{student_portal_url}}

## Automation principles
- Never claim payment succeeded before a verified provider webhook.
- Never claim scarcity unless cohort capacity data supports it.
- 5 = minimum opening threshold; 7 = portfolio target, not hard close; 10 = hard capacity.
- Financial, cancellation and refund messages must reflect the final approved terms.
- No investment recommendations, signals or return promises.
