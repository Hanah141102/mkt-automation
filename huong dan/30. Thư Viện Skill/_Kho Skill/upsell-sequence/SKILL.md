---
name: upsell-sequence
description: "Xây chuỗi email bán nâng cấp và bán chéo sau khi mua, tăng giá trị đơn hàng bằng sản phẩm bổ trợ, gói nâng cấp và combo đúng thời điểm. Dùng ngay sau khi khách vừa mua xong."
allowed-tools: Read Write Glob
ten-viet: "Chuỗi Bán Nâng Cấp"
nhom: "06. Email & Tự Động Hoá"
ten-goc: "Upsell Sequence"
---

# Chuỗi Bán Nâng Cấp

## When to Use This Skill

Use this skill when you need to:
- Build a post-purchase email sequence that promotes upgrades, add-ons, or complementary products
- Increase average order value from existing customers without running new ads
- Create a cross-sell flow that pairs related products naturally after a purchase
- Design a bundle or subscription offer triggered by a one-time buy

**DO NOT** use this skill for cold outreach to non-customers, general email sequences for non-buyers, or abandoned cart recovery. This is for people who have already purchased.

---

## Core Principle

UPSELL TO PEOPLE WHO ALREADY TRUST YOU — A CUSTOMER WHO JUST BOUGHT IS 60-70% MORE LIKELY TO BUY AGAIN THAN A NEW PROSPECT IS TO BUY ONCE. EVERY EMAIL MUST DEEPEN THE VALUE OF WHAT THEY ALREADY OWN BEFORE ASKING FOR MORE.

---

## Upsell Type Reference

| Type | Definition | Best For |
|------|-----------|----------|
| **Upsell** | Higher-tier version of what they bought | SaaS, courses, services |
| **Cross-sell** | Complementary product that pairs naturally | E-commerce, digital products |
| **Bundle** | Package deal combining products at a discount | E-commerce, product suites |
| **Upgrade** | Feature unlock or plan change | SaaS, memberships |

## Timing Map

| Timing | Best Upsell Type | Why It Works |
|--------|-----------------|--------------|
| **Immediate (0-1 days)** | Upgrade, Bundle | Buyer is in purchase mode |
| **Short-term (3-5 days)** | Cross-sell | Customer has used the product |
| **Medium-term (7-10 days)** | Upsell | Customer hit the base product's limits |
| **Long-term (30+ days)** | Subscription, Bundle | Proven repeat interest |

---

## Phase 1: Map

Gather inputs before writing any emails:

1. **Initial product purchased** — what did the customer buy?
2. **Initial price point** — how much did they pay?
3. **Upsell candidate(s)** — what product, upgrade, or bundle will you offer?
4. **Upsell price point** — how much is the upsell offer?
5. **Customer segment** — who is this buyer?
6. **Email platform** — ConvertKit, Mailchimp, Klaviyo, ActiveCampaign (ConvertKit by default)

**GATE: Do not proceed until the user confirms the strategy brief. You must have at least one initial product and one upsell candidate before writing.**

---

## Phase 2: Write

Default sequence is 4 emails over 10-14 days. Present all emails together as a complete set.

### Email 1: Thank You + Soft Intro (Day 0-1)

**Goal:** Gratitude, quick-win tip for the product they bought, subtle seed for the next level. No CTA, no link.

**Structure:** (1) Thank them for the specific purchase. (2) Deliver a quick-win tip they can act on immediately. (3) One sentence hinting at a deeper level.

**Length:** 120-180 words. **Subject lines:** "you are in — here is your first step" / "welcome to [product] (and a quick tip)"

### Email 2: Value Bridge (Day 3-5)

**Goal:** Connect the value they are getting from the initial product to a natural next step. Frame the upsell as a logical extension of progress, not a separate purchase.

**Structure:** (1) Check in on their progress. (2) Name the gap — "Now that you have done X, the next challenge is Y." (3) Bridge to the upsell as the thing that closes the gap. (4) No hard CTA — end with a question or teaser.

**Length:** 150-200 words. **Subject lines:** "where most [customer type] get stuck after [product]"

### Email 3: The Offer (Day 7)

**Goal:** Direct upsell offer with a clear benefit, social proof, and a reason to act now.

**Structure:** (1) Callback to the gap from Email 2. (2) Present the upsell — what it is, what it includes, what outcome it delivers. (3) Social proof — one specific result (name, situation, outcome). (4) Incentive — limited-time bonus or exclusive add-on. (5) Single clear CTA.

**Length:** 200-300 words. **Subject lines:** "an upgrade for [product] customers only"

### Email 4: Last Chance (Day 10-14)

**Goal:** Real deadline, restate the core benefit, final nudge, graceful close.

**Structure:** (1) State the deadline. (2) Restate the single strongest benefit. (3) Address the most common hesitation. (4) Final CTA. (5) Graceful close — no guilt.

**Length:** 100-150 words. **Subject lines:** "last call — [bonus] expires [day]"

**GATE: Present the full 4-email sequence. Do not finalize until the user approves the copy, tone, timing, and offer framing.**

---

## Phase 3: Sequence Map

```
TRIGGER: Customer completes purchase of [initial product]
  |
EMAIL 1: "Thank You + Soft Intro" (Day 0-1) — No CTA
  |  [Wait 3 days]
EMAIL 2: "Value Bridge" (Day 3-5) — Soft reply/teaser
  +--- IF purchased upsell ---> EXIT, move to upsell onboarding
EMAIL 3: "The Offer" (Day 7) — Buy/upgrade link
  +--- IF purchased upsell ---> EXIT
EMAIL 4: "Last Chance" (Day 10-14) — Final CTA
  +--- IF purchased ---> Move to upsell onboarding
  +--- IF no purchase ---> Tag "upsell-declined," move to nurture
```

### Conditional Exit Rules

- **Customer buys the upsell:** immediately remove from remaining emails
- **Customer opens a support ticket:** pause until resolved
- **Customer requests a refund:** cancel the upsell sequence permanently
- **Full sequence, no purchase:** tag "upsell-passed," do not re-send the same offer

---

## Phase 4: Deliver

### Pre-Send Checklist

```
- [ ] Email 1 sends gratitude and value — no pitch, no CTA link
- [ ] Email 2 names a real gap, not a manufactured one
- [ ] Email 3 has one specific social proof story (name, situation, outcome)
- [ ] Email 4 has a real deadline that you will actually enforce
- [ ] Every email has exactly one CTA (Emails 1-2: soft/none; Emails 3-4: buy link)
- [ ] Subject lines are under 50 characters
- [ ] Conditional exit removes buyers from remaining upsell emails immediately
- [ ] Support ticket pause is configured
- [ ] Refund trigger cancels the upsell sequence permanently
- [ ] The upsell offer is genuinely complementary — not a random product
- [ ] No email sends within 24 hours of the purchase confirmation email
- [ ] The incentive has a real expiration
```

---

## Anti-Patterns

- **Upselling in the order confirmation email** — pitch separately, at least a few hours later.
- **Pitching before the customer has received the product** — wait until they have it in hand.
- **Offering discounts on premium upsells** — use bonuses instead (extra session, exclusive resource).
- **Sending upsells to customers with open support tickets** — resolve the issue first.
- **Stacking upsells** — one upsell per sequence.
- **Fake scarcity** — if you use scarcity, it must be real.
- **More than 4 emails** — if they did not buy after 4 touches, move on.

---

## Recovery

- **No upsell candidate:** Ask what customers most commonly ask about after purchasing. Suggest the logical next step.
- **Only one product:** Help design one — premium version, complementary download, subscription, or service add-on.
- **Low email engagement (under 20% open rate):** Clean the list first. Only send to customers who opened at least 1 of their last 3 emails.
- **High refund rate (over 10%) on initial product:** Fix the initial experience before adding upsells.
