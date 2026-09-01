# CRYPTO × AI ACADEMY — Product Spec

## Operating principle
Amitai teaches only. The system owns lead → registration → payment → assignment → messaging → cohort opening/closing → reminders → payment failure handling → waitlist.

## Cohort rules
- 0–4: waiting for opening.
- 5–6: approved to open.
- 7: optimal target.
- 8–9: continue selling when demand exists.
- 10: SOLD OUT; new leads go to waitlist.

## Commercial
- Price: 13,000 ILS/student.
- 52 hours/student.
- 250 ILS/student-hour.
- 13 meetings × 4 hours.
- Target: 6 cohorts × 7 = 42 students = 546,000 ILS.
- Maximum capacity: 60 students = 780,000 ILS.

## Required states
lead, contacted, interested, payment_pending, paid, assigned, waitlist, payment_failed, cancelled, refunded.

## Automation rules
- Never reserve a seat on client-side payment success alone.
- Only a verified payment webhook can mark PAID.
- Seat assignment must be atomic and idempotent.
- At 4 paid students: internal alert — one more required to open.
- At 5: cohort becomes OPEN.
- At 7: TARGET_REACHED; do not block sales.
- At 10: SOLD_OUT and activate waitlist.
- Payment failure: seat is not reserved; send recovery flow.
- If a cohort fails to reach 5 by its decision deadline: offer approved alternative cohort or process according to the accepted cancellation/refund policy.

## Human approval boundary
No first live outbound campaign, payment capture, refund, or production WhatsApp send before owner approval of connected accounts/templates. Everything else should be buildable and testable in staging.