---
name: payment-terms-policy
description: "Soạn chính sách thanh toán và thu hồi công nợ: thời hạn thanh toán, mức phạt trả chậm và quy trình đòi nợ theo cấp độ. Dùng khi cần quy định rõ khách phải trả khi nào và thế nào."
allowed-tools: Read Write Glob
ten-viet: "Chính Sách Điều Khoản Thanh Toán"
nhom: "14. Pháp Lý & Tuân Thủ"
ten-goc: "Payment Terms Policy"
---

# Chính Sách Điều Khoản Thanh Toán

## When to Use This Skill

Use this skill when you need to:
- Establish standard payment terms for your business
- Create a late payment and collections escalation policy
- Draft payment terms language for contracts and invoices
- Design early payment incentives or late fee structures

**DO NOT** use this skill for creating invoices, pricing strategies, or full client agreements. This is specifically for the payment terms and collections process.

---

## Core Principle

CLEAR PAYMENT TERMS PREVENT 90% OF COLLECTIONS ISSUES — STATE THE RULES UPFRONT, ENFORCE THEM CONSISTENTLY, AND ESCALATE PREDICTABLY.

---

## Phase 1: Business Context

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Business type** | "What type of business? (freelance, agency, SaaS, product)" | Service-based |
| **Average invoice amount** | "What is your typical invoice size?" | $1,000-5,000 |
| **Current terms** | "What payment terms do you currently use?" | Net 30 |
| **Payment methods accepted** | "How can clients pay? (credit card, ACH, wire, check)" | Credit card + ACH |
| **Client type** | "B2B or B2C? Large companies or small businesses?" | B2B small businesses |

**GATE: Do not proceed without business type and typical invoice size.**

---

## Phase 2: Payment Terms Design

### Standard Terms Options

| Term Type | When to Use | Risk Level |
|-----------|------------|-----------|
| Due on receipt | Small projects, new clients, under $1,000 | Lowest |
| Net 15 | Standard services, retainer invoices | Low |
| Net 30 | Established clients, B2B standard | Medium |
| Net 45-60 | Enterprise clients only | Higher |
| 50% upfront / 50% on delivery | Projects, custom work | Lowest |
| Monthly retainer (due 1st of month) | Ongoing services | Low |

### Late Fee Structure

```
### Late Payment Fees

| Days Past Due | Action | Fee |
|--------------|--------|-----|
| 1-7 days | Courtesy reminder email | None |
| 8-15 days | Late notice + late fee applied | [1.5% per month or $X flat] |
| 16-30 days | Second notice, phone call | Additional interest accrues |
| 31-60 days | Final notice, work paused | Services suspended |
| 61-90 days | Collections warning letter | Formal demand |
| 90+ days | Collections agency or legal | External collections |

**Late fee rate:** 1.5% per month / 18% annually (check state usury laws)
**Grace period:** 7 days from due date
**Compounding:** Simple interest, not compounding
```

---

## Phase 3: Collections Process

### Escalation Email Templates

```
### Courtesy Reminder (Day 1-7)
Subject: Friendly reminder — Invoice #[X] due [date]

Invoice #[X] for $[amount] was due on [date]. If you have already sent payment, please disregard.
Pay here: [payment link]

---

### Late Notice (Day 8-15)
Subject: Past due — Invoice #[X] ($[amount])

Invoice #[X] for $[amount] is now [X] days past due. A late fee of $[X] has been applied per our payment terms.
Please remit by [new date] to avoid additional fees. Pay here: [link]

---

### Final Notice (Day 31-60)
Subject: Final notice — Invoice #[X] past due

Invoice #[X] for $[amount] is now [X] days past due. Services have been paused until the balance is resolved.
Total due (including late fees): $[X]
Please remit within 7 days or we will proceed with formal collections.
```

---

## Phase 4: Policy Document

### Invoice Language

```
Payment is due within [X] days of invoice date. A late fee of [1.5%] per month will be applied to balances outstanding beyond the [7]-day grace period. Client is responsible for all costs of collection, including reasonable attorney fees. [Business Name] reserves the right to suspend services on accounts more than [30] days past due.
```

### Implementation Checklist

```
- [ ] Payment terms added to contract template
- [ ] Late fee language added to invoice template
- [ ] Payment link included on every invoice
- [ ] Auto-reminder set up in invoicing software (Day 1, 7, 14, 30)
- [ ] Collections escalation process documented
- [ ] Late fee rate compliant with state usury laws
```

---

## Anti-Patterns

- **No written terms** — verbal agreements lead to disputes. Put terms in writing on every contract and invoice.
- **Terms but no enforcement** — if you never charge late fees, your terms are suggestions.
- **Net 60+ for small businesses** — only enterprise clients justify long terms.
- **No upfront payment on projects** — always collect 30-50% before starting custom work.
- **Emotional collections** — follow the escalation process mechanically.

---

## Recovery

- **Currently owed money with no terms:** Implement terms going forward. For existing overdue invoices, send a professional reminder and offer a payment plan.
- **Client refuses late fees:** Waive once for valuable clients but communicate terms apply going forward.
- **State restricts late fee rates:** Research state usury laws. Most states allow 1-1.5% per month for commercial transactions.
- **Client disputes the invoice:** Pause collections. Resolve the dispute first, then restart the clock.
