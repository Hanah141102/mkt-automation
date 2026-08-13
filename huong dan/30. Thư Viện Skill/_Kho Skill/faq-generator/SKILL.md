---
name: faq-generator
description: "Tạo bộ câu hỏi thường gặp phân theo nhóm, trả lời ngắn gọn rõ ràng, tối ưu cho website, trang bán hàng và trung tâm hỗ trợ. Dùng khi cần phần FAQ hoặc muốn giảm số câu hỏi lặp lại của khách."
allowed-tools: Read Write Glob Grep
ten-viet: "Tạo Bộ Câu Hỏi Thường Gặp"
nhom: "03. Nội Dung & Sáng Tạo"
ten-goc: "FAQ Generator"
---

# Tạo Bộ Câu Hỏi Thường Gặp

## When to Use This Skill

Use this skill when the user needs to:
- Create an FAQ section for a sales page, landing page, or product page
- Build a dedicated FAQ or help center page for their website
- Preempt common customer objections before they reach support
- Generate structured FAQ content with SEO-friendly schema markup
- Organize scattered customer questions into a clean, categorized format

**DO NOT** use this skill for:
- Building an internal customer support knowledge base (use customer-support-kb)
- Writing long-form help documentation or user guides
- Creating chatbot scripts or automated response flows
- Answering a single specific customer question on the spot

---

## FAQ Category Framework

| Category | What It Covers | Typical For |
|----------|---------------|-------------|
| **Getting Started** | How to buy, sign up, access, get started | All businesses |
| **Product/Service Details** | What is included, how it works, features, specs | All businesses |
| **Pricing & Payment** | Costs, plans, refunds, payment methods, billing | All businesses |
| **Shipping & Delivery** | Timelines, tracking, international, packaging | E-commerce, physical products |
| **Support & Troubleshooting** | How to get help, common issues, account problems | SaaS, courses, memberships |
| **Trust & Credibility** | Guarantees, certifications, testimonials, track record | All businesses |

**DEFAULT: Use all 6 categories.** Drop Shipping & Delivery for purely digital products. Drop Support & Troubleshooting for simple one-time purchases with no account.

---

## Answer Writing Rules

EVERY FAQ ANSWER MUST LEAD WITH THE DIRECT ANSWER — NEVER OPEN WITH FILLER, PLEASANTRIES, OR A RESTATEMENT OF THE QUESTION.

| Rule | Correct | Incorrect |
|------|---------|-----------|
| Direct answer first | "Yes, we offer a 30-day money-back guarantee." | "Great question! We understand that making a purchase decision can be difficult..." |
| 2-4 sentences max | Concise paragraph with one follow-up detail | Multi-paragraph essay covering every edge case |
| Specific, not vague | "Refunds are processed within 5-7 business days." | "Refunds are handled on a case-by-case basis." |
| Action-oriented endings | "Visit your account dashboard to update your plan." | "Feel free to reach out if you have any questions." |
| No invented policies | Only include details the user has confirmed | Making up refund windows, shipping times, or guarantees |

---

## Core Workflow

### Step 1: Understand

Gather these inputs from the user before generating any questions or answers:

1. **Product or service description** — what they sell and how it works
2. **Target audience** — who buys this
3. **FAQ context type** — sales page, service page, SaaS landing page, e-commerce FAQ, or course/program FAQ
4. **Pricing details** — price points, plans, tiers
5. **Refund/guarantee policy**
6. **Shipping/delivery details** (if applicable)
7. **Existing customer questions** (read files with `Read` or `Glob` if paths are provided)
8. **Common objections** — what stops people from buying

**If the user provides items 1-3, proceed with reasonable defaults for the rest.**

**GATE: Do not proceed to Step 2 until you have at minimum: product/service description, target audience, and FAQ context type.**

---

### Step 2: Extract

Generate 15-25 FAQ questions across the relevant categories (3-5 per active category).

- **Phrase questions the way a real buyer would ask**, not in formal corporate language.
- **Write answers following the Answer Writing Rules** — direct answer first, 2-4 sentences, specific details, action-oriented ending.
- **Include at least 2 objection-handling questions** in Trust & Credibility.
- **Verify completeness:** every active category has 3-5 questions, total 15-25, no answer exceeds 4 sentences, no filler openers, pricing and refund questions always included.

---

### Step 3: Present

Show the complete FAQ draft organized by category:

```
## FAQ Draft — [Product/Service Name]

### Getting Started
**Q: How do I sign up?**
A: [answer]

### Pricing & Payment
**Q: How much does it cost?**
A: [answer]
...
```

Include the Schema.org FAQ structured data snippet below the markdown version:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I sign up?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Visit our website and click the Get Started button..."
      }
    }
  ]
}
</script>
```

Present a summary with question count by category, schema note, and estimated read time.

**GATE: Do not proceed to Step 4 until the user reviews and approves the FAQ content.**

---

### Step 4: Deliver

Save to `faq/faq.md` (markdown) and `faq/faq.html` (HTML with schema markup). Suggest placement:

- **Sales page:** Above the final CTA, after testimonials and pricing
- **Dedicated FAQ page:** Linked from footer, nav, and contact page
- **Product listing:** Top 5-8 most relevant questions on the product page

---

## Anti-Patterns

- **DO NOT** start any answer with "Great question!" "Absolutely!" or any filler — lead with the direct answer
- **DO NOT** write answers longer than 4 sentences
- **DO NOT** invent policies the user has not confirmed — ask if information is missing
- **DO NOT** skip Pricing & Payment — always address cost and refund questions
- **DO NOT** use corporate jargon in answers — write plainly
- **DO NOT** duplicate questions across categories
- **DO NOT** present the FAQ without the Schema.org structured data
- **DO NOT** save files before the user has reviewed and approved the content

---

## Recovery and Troubleshooting

### User Cannot Describe Their Product Clearly
Ask for a link to their website or sales page. If no URL, ask the three minimum questions one at a time.

### User Has No Existing Customer Questions
Generate based on product type using common objection patterns for their niche:
- Digital products: "Is this a scam?" "Will I actually get results?" "Is there a guarantee?"
- E-commerce: "What if it doesn't fit?" "How long does shipping take?" "What's the return policy?"
- Services: "How long does this take?" "What's included?" "Do you offer a free consultation?"
- SaaS: "Is there a free trial?" "Can I cancel anytime?" "Is my data secure?"

### User Wants More Than 25 Questions
Offer to split: concise FAQ for the sales page (15-20 questions) and a separate help center document with the rest, with a table of contents and anchor links.

### File Save Fails
Output the complete FAQ content directly in the conversation for the user to copy-paste.
