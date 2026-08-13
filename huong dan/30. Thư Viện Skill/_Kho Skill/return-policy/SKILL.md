---
name: return-policy
description: "Viết chính sách đổi trả và hoàn tiền rõ ràng, thân thiện với khách cho cửa hàng trực tuyến, sản phẩm số và doanh nghiệp dịch vụ, diễn đạt dễ hiểu. Dùng khi cần công bố chính sách trên website."
allowed-tools: Read Write Glob
ten-viet: "Chính Sách Đổi Trả"
nhom: "14. Pháp Lý & Tuân Thủ"
ten-goc: "Return Policy Generator"
---

# Chính Sách Đổi Trả

## When to Use This Skill

Use this skill when:
- A user needs a return and refund policy for an e-commerce store (Shopify, WooCommerce, Etsy)
- Someone is launching a new online store and needs return terms before going live
- A user sells digital products (courses, templates, software) and needs refund terms
- A service provider needs a cancellation and refund policy
- A user runs a subscription business and needs cancellation and prorated refund terms

**DO NOT** use this skill for terms of service, privacy policies, individual refund disputes, or warranty documents.

---

## Legal Disclaimer

**THIS SKILL GENERATES RETURN POLICY TEMPLATES FOR INFORMATIONAL PURPOSES ONLY. IT DOES NOT PROVIDE LEGAL ADVICE. CONSULT WITH A QUALIFIED ATTORNEY TO ENSURE COMPLIANCE WITH YOUR JURISDICTION'S CONSUMER PROTECTION LAWS.** This disclaimer MUST appear at the bottom of every generated policy.

---

## Core Principle

EVERY RETURN POLICY MUST BE WRITTEN IN PLAIN LANGUAGE A CUSTOMER CAN UNDERSTAND IN UNDER 60 SECONDS, MAKE RETURNS AS EASY AS PURCHASING, AND PROTECT THE BUSINESS WITHOUT PUNISHING THE BUYER.

## Policy Types

### Physical Products (Default)
- Return window: 30 days from delivery date
- Condition: Unused, unworn, in original packaging with tags attached
- Return shipping: Customer pays unless item is defective
- Refund method: Original payment method within 5-10 business days

### Digital Products
- Refund window: 14-day satisfaction guarantee (or no refunds per user preference)
- Access revocation: Refund triggers immediate access removal
- Exception: Technical issues preventing access are always refunded

### Services (Coaching, Consulting, Agency)
- Cancellation notice: Minimum notice period before scheduled session
- Completed work: No refund for work already delivered and approved
- Unused prepaid sessions: Refundable minus cancellation fee

### Subscriptions
- Monthly: Cancel anytime, access continues through current billing period
- Annual: Cancel anytime, prorated refund for remaining months (or no refund per user preference)

Default to **Physical Products with 30-day return window** unless user specifies otherwise.

---

## Core Workflow

### Step 1: Gather Business Details

Ask all at once:
1. What do you sell? (physical products, digital products, services, subscriptions, or a mix)
2. What platform? (Shopify, WooCommerce, Etsy, Squarespace, custom site, or N/A)
3. What return window? (default: 30 days physical, 14 days digital)
4. How do you want to issue refunds? (original payment, store credit, exchange, or customer's choice)
5. Who pays for return shipping? (you, customer, or free for defective only)
6. Any non-returnable items or situations?
7. What is your return email or contact method?

**Defaults for unanswered questions:**

| Question | Default |
|----------|---------|
| Return window | 30 days from delivery |
| Refund method | Original payment method |
| Processing time | 5-10 business days |
| Return shipping | Customer pays; free for defective |
| Exchanges | Available for size/color swaps |
| Non-returnable items | Gift cards, final sale, personalized orders |
| Contact | `returns@yourbrand.com` [DEFAULT — update before publishing] |

**GATE: Do not proceed without what they sell (question 1) and their preferred return window (question 3).**

### Step 2: Draft the Policy

Write these 10 sections in order:
1. **Overview Statement** — friendly, confidence-building, 1-2 sentences
2. **Return Window** — specific days and what triggers the clock
3. **Eligibility** — two clear lists: what can and cannot be returned
4. **How to Start a Return** — numbered step-by-step process
5. **Refund Method and Processing Time** — specific business days
6. **Shipping Costs** — who pays and whether labels are provided
7. **Exchanges** — whether available, how to request, limitations
8. **Damaged or Defective Items** — separate, faster, no-cost process
9. **Exceptions** — bulleted list of non-returnable items
10. **Contact Information** — email, response time

Formatting rules: H2 for title, H3 for sections, numbered lists for processes, bullets for exceptions, plain language at an 8th-grade reading level, under 800 words (physical) or 400 words (digital).

**GATE: Present the complete draft before saving to file.**

### Step 3: Review with User

1. "Does this accurately reflect your return terms?"
2. "Are the default terms acceptable? (Marked with [DEFAULT] flags.)"
3. "Is the tone right — or should it be more formal or more casual?"

**If more than 3 revision rounds:** "Would you like to finalize and adjust the remaining details yourself?"

**GATE: Do not save to file until the user explicitly approves.**

### Step 4: Deliver to File

Default path: `policies/return-policy.md`

Always end with: "Have a qualified attorney review this policy for compliance with your jurisdiction's consumer protection laws before publishing."

---

## Anti-Patterns

- **Aggressive or punitive language** — "ALL SALES ARE FINAL" destroys trust and increases chargebacks.
- **Hiding the return process** — steps must be a numbered list, visible in under 10 seconds.
- **Making returns harder than purchasing** — match the effort.
- **Vague processing times** — state a specific number of business days.
- **Contradicting platform policies** — Etsy, Shopify, and Amazon have mandatory buyer protections.
- **Legalese and jargon** — plain language is not less enforceable.
- **Omitting the legal disclaimer** — every generated policy must include it.

---

## Recovery

**User does not know what terms to set:** Present common defaults by business type. If still unsure: "Start with 30 days and original payment method. You can tighten the policy later once you see your return rate."

**User wants no returns:** Explain chargebacks risk. Offer 14-day window with conditions as a middle ground. If they insist, write the policy clearly and add exceptions for defective items (most jurisdictions require this).

**User sells multiple product types:** Write one policy with clearly labeled sections for each product type.

**File save fails:** Output the complete policy in chat so the user can copy-paste it.
