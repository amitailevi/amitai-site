# CODEX MASTER PROMPT

You are the lead engineer for CRYPTO × AI ACADEMY. Build a production-ready system inside this workspace. Preserve the existing Amitai visual language: RTL, Heebo, premium, concise, strong hierarchy. For the academy use black/white/gold and avoid crypto-hype aesthetics.

## Fixed rules
- Price: 13,000 ILS/student.
- 52 hours/student; 13 meetings × 4 hours.
- Minimum 5, target 7, maximum 10 per cohort.
- 10 = SOLD OUT + waitlist.
- Payment success reserves a seat only after a verified server webhook.
- No individualized investment advice or return promises.

## Build
1. Premium RTL landing page, mobile first.
2. Cohort catalogue with live availability.
3. Registration and checkout flow.
4. Payment provider abstraction; webhook verification, idempotency and sandbox mode.
5. CRM database and lead lifecycle.
6. Admin dashboard: leads, paid, failed, occupancy, cohort state, revenue, outstanding balance, next action.
7. Email and WhatsApp template engine.
8. Cohort state machine implementing 0–4 / 5–6 / 7 / 8–9 / 10.
9. Waitlist and alternative-cohort offers.
10. CSV export and immutable audit trail.
11. Calendar invitations after confirmed payment.
12. Reminder and payment-failure recovery jobs.
13. Analytics events for landing → registration → checkout → paid.
14. Tests for seat race conditions, duplicate webhooks, payment failure and sold-out transitions.

## Security and money
Never trust price, cohort capacity or payment state from the browser. Look up price server-side. Verify webhook signatures. Use idempotency keys. Never store card data. Keep secrets in environment/secret manager. Protect admin routes with authentication and roles. Log every money/cohort state transition.

## Deployment
Create staging first. Production remains disabled until provider credentials, domain, legal/refund policy and first outbound templates are approved.

## Definition of done before GO LIVE
A new lead can choose a cohort, submit details, complete a sandbox payment, be atomically assigned, receive a test confirmation, appear in CRM/dashboard, affect 5/7/10 state, receive calendar data, and be handled correctly for failed payment/waitlist — with no manual Amitai action.