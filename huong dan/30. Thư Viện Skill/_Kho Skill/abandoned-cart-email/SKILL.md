---
name: abandoned-cart-email
description: "Viết chuỗi email nhắc khách bỏ giỏ hàng: thời điểm gửi, tiêu đề, mức ưu đãi tăng dần và ghi chú ảnh sản phẩm. Dùng khi muốn cứu lại các đơn khách đã bỏ dở."
allowed-tools: Read Write Glob
ten-viet: "Email Nhắc Bỏ Giỏ Hàng"
nhom: "06. Email & Tự Động Hoá"
ten-goc: "Abandoned Cart Email"
---

# Email Nhắc Bỏ Giỏ Hàng

## When to Use This Skill

Use this skill when you need to:
- Write an abandoned cart email sequence (2-4 emails) to recover lost sales
- Create subject lines, timing, and incentive escalation strategies
- Design emails with product image placement and urgency elements
- Build a cart recovery system for an e-commerce or digital product business

**DO NOT** use this skill for general promotional emails, welcome sequences, or newsletters. This is specifically for cart abandonment recovery.

---

## Core Principle

ABANDONED CART EMAILS WORK BECAUSE THE CUSTOMER ALREADY WANTED THE PRODUCT — YOUR JOB IS TO REMOVE THE FRICTION THAT STOPPED THEM, NOT TO SELL FROM SCRATCH.

---

## Phase 1: Brief

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Product type** | "What was abandoned? Physical product, digital product, course, subscription?" | No default — must be provided |
| **Average cart value** | "What is the typical cart value?" | No default — must be provided |
| **Common objections** | "Why do customers typically abandon? Price, shipping, comparison shopping?" | Price and distraction |
| **Incentive budget** | "Can you offer a discount, free shipping, or bonus to recover carts?" | 10% discount available |
| **Email platform** | "What email tool do you use?" | Any (will provide generic templates) |
| **Number of emails** | "How many emails in the sequence? (2-4 recommended)" | 3 emails |

**GATE: Confirm brief before writing the sequence.**

---

## Phase 2: Outline

### Sequence Architecture

```
## Abandoned Cart Sequence

**Email 1:** Reminder (1 hour after abandonment)
- Tone: Helpful, not pushy
- Purpose: Remind them their cart is waiting
- No incentive yet

**Email 2:** Objection Buster (24 hours after abandonment)
- Tone: Reassuring, social proof
- Purpose: Address the reason they hesitated
- Light incentive (optional)

**Email 3:** Last Chance (48-72 hours after abandonment)
- Tone: Urgency + incentive
- Purpose: Create urgency and offer the strongest incentive
- Full incentive deployed
```

**GATE: Approve sequence timing and structure before writing.**

---

## Phase 3: Write

### Email 1: The Reminder (1 hour after abandonment)

```
## Email 1: Gentle Reminder

**Send time:** 1 hour after cart abandonment
**Subject line options:**
1. "You left something behind"
2. "Still thinking it over?"
3. "Your cart is waiting for you"

**Preview text:** "Your [product name] is reserved — complete your order before it's gone."

**Body:**

Hey [Name],

Looks like you left [product name] in your cart.

[PRODUCT IMAGE: Show the exact item(s) they abandoned]

No worries — it happens. Your cart is saved and ready when you are.

[CTA BUTTON: "Complete My Order →"]

If you ran into any issues at checkout, just reply to this email and I'll help.

**Design notes:**
- Product image prominently displayed
- Single CTA button
- Clean, minimal layout
- Mobile-optimized
```

### Email 2: Objection Buster (24 hours)

```
## Email 2: Address the Hesitation

**Send time:** 24 hours after abandonment
**Subject line options:**
1. "Still on the fence about [product]?"
2. "Here's what [product] customers are saying"
3. "Quick question about your order"

**Preview text:** "[Social proof snippet — e.g., '500+ happy customers and counting']"

**Body:**

Hey [Name],

I noticed you haven't completed your order yet. Totally understand — here's what might help:

[TESTIMONIAL: "Quote about the specific product from a real customer" — Name, Location]

[Address top objection:]
- If price: "This is an investment that pays for itself in [timeframe/savings]"
- If shipping: "Free shipping on orders over $[X]" or "Ships within 24 hours"
- If trust: "[Guarantee] — try it risk-free for [X] days"

[PRODUCT IMAGE]

[CTA BUTTON: "Complete My Order →"]

[Optional light incentive: "Use code SAVE10 for 10% off — just for you."]
```

### Email 3: Last Chance (48-72 hours)

```
## Email 3: Urgency + Best Offer

**Send time:** 48-72 hours after abandonment
**Subject line options:**
1. "Last chance: [X]% off your cart (expires tonight)"
2. "Your cart expires soon — [incentive] inside"
3. "Final reminder + a special offer just for you"

**Preview text:** "Your [incentive] expires at midnight."

**Body:**

Hey [Name],

This is my last reminder about your cart — after today, [incentive expires / cart clears / price goes back up].

[PRODUCT IMAGE]

**Your cart:**
- [Product name] — $[price]
- [Discount applied]: -$[amount]
- **Your price: $[final price]**

[CTA BUTTON: "Get [X]% Off Now →"]

[Urgency element: "This offer expires at midnight tonight."]

If [product name] is not right for you, no hard feelings. But if you were planning to buy, now is the best time.

P.S. [Restate the guarantee or key benefit one more time]
```

### Timing & Incentive Escalation

```
## Sequence Timing

| Email | Timing | Incentive | Tone |
|-------|--------|-----------|------|
| 1 | 1 hour after abandonment | None | Helpful reminder |
| 2 | 24 hours | Light (10% off or free shipping) | Reassuring + social proof |
| 3 | 48-72 hours | Full (best discount + urgency) | Urgency + last chance |

**If only 2 emails:** Send Email 1 at 1 hour, Email 3 at 48 hours.
**If 4 emails:** Add a "product education" email between Email 2 and 3.
```

---

## Phase 4: Polish

### 1. Sequence Checklist

```
## Abandoned Cart Sequence Checklist

- [ ] Email 1 sends within 1 hour of abandonment
- [ ] Subject lines are A/B testable (provide 2-3 options per email)
- [ ] Product image is prominently displayed in every email
- [ ] Incentive escalates across the sequence (none → light → full)
- [ ] Each email has a single CTA button
- [ ] Social proof appears in at least one email
- [ ] Guarantee or risk-reversal is mentioned
- [ ] P.S. line is included in the final email
- [ ] Urgency element has a real deadline
- [ ] Emails are mobile-friendly (short paragraphs, large CTA button)
- [ ] Unsubscribe link is included (compliance)
```

### 2. Recovery Rate Benchmarks

- Industry average cart recovery rate: 5-15%
- Good recovery rate with this sequence: 10-20%
- Track: open rates, click rates, and recovered revenue per email
- Test subject lines with A/B splits on Email 1 (highest volume)

---

## Anti-Patterns

- **Leading with the discount in Email 1** — trains customers to abandon carts for a discount. Always start with a no-incentive reminder.
- **No product image** — the customer needs to see what they left behind. Always show the product.
- **Too many emails** — more than 4 cart recovery emails feels aggressive. 3 is the sweet spot.
- **Generic subject lines** — "Complete your purchase" is forgettable. Include the product name or incentive.
- **No urgency in the final email** — set a real deadline.
- **Sending Email 1 too late** — after 4+ hours, purchase intent fades fast. Send within 1 hour.

---

## Recovery

- **Email platform does not support cart triggers:** Use a manual process — export abandoned carts daily and send a batch email.
- **No testimonials available:** Replace the social proof email with a product benefits email highlighting the top 3 outcomes.
- **Cannot offer discounts:** Replace the incentive with a bonus (free template, extra module, extended trial) or emphasize the guarantee.
- **Low open rates:** Test subject lines aggressively. Try personalization (include the product name), curiosity, or urgency.
- **Customers say they abandoned due to a bug:** Fix the checkout flow first. No email sequence overcomes a broken cart.
