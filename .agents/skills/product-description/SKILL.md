---
name: product-description
description: "Viết mô tả sản phẩm tối ưu chuyển đổi cho sàn thương mại điện tử: nhấn lợi ích, chèn từ khoá SEO và định dạng đúng chuẩn từng sàn. Dùng khi đăng bán trên Shopee, Lazada, TikTok Shop hoặc website riêng."
allowed-tools: Read Write Glob Grep
ten-viet: "Mô Tả Sản Phẩm"
nhom: "03. Nội Dung & Sáng Tạo"
ten-goc: "Product Description"
---

# Mô Tả Sản Phẩm

## When to Use This Skill

Use this skill when you need to:
- Write a new product listing for Shopify, Amazon, Etsy, or WooCommerce
- Improve existing product copy that is not converting
- Launch a product across multiple e-commerce platforms with tailored descriptions
- Optimize product SEO with keyword-rich titles, bullet points, and meta descriptions

**DO NOT** use this skill for general marketing copy, brand voice development, product photography direction, pricing strategy, or ad copy for paid campaigns.

---

## Quick Reference: Platform Specifications

| Platform | Title | Bullets | Description | Tags/Keywords |
|----------|-------|---------|-------------|---------------|
| Shopify | 255 chars | No limit | No limit | SEO title 70 chars, meta 320 chars |
| Amazon | 200 chars | 5 x 500 chars | 2,000 chars | Backend terms 250 bytes |
| Etsy | 140 chars | N/A | 10,000 chars | 13 tags, 20 chars each |
| WooCommerce | 255 chars | No limit | No limit | SEO title 60 chars, meta 160 chars |

**DEFAULT PLATFORM: Shopify**

## Quick Reference: Description Frameworks

| Framework | Structure | Best For |
|-----------|-----------|----------|
| Feature-Benefit-Outcome | Feature > What it does for the buyer > End result | Physical products with clear specs |
| Problem-Solution | Pain point > How the product solves it > Proof | Products solving a specific frustration |
| Sensory/Lifestyle | Scene-setting > Sensory details > Emotional payoff | Handmade goods, food, candles, apparel |
| Technical Spec | Capability > Integration > Measurable result | SaaS, digital tools, electronics |

**DEFAULT FRAMEWORK: Feature-Benefit-Outcome**

## Quick Reference: Bullet Point Formula

| Position | Purpose | Template |
|----------|---------|----------|
| Bullet 1 | Primary benefit | [BIGGEST BENEFIT] -- [feature that delivers it] |
| Bullet 2 | Differentiator | [WHAT MAKES IT DIFFERENT] -- [specific proof or spec] |
| Bullet 3 | Use case / lifestyle | [WHO IT IS FOR] -- [scenario where it shines] |
| Bullet 4 | Quality / trust signal | [QUALITY INDICATOR] -- [material, process, or certification] |
| Bullet 5 | Risk reducer | [GUARANTEE / EASE] -- [return policy, setup simplicity, or warranty] |

---

## Core Workflow

EVERY PRODUCT DESCRIPTION STARTS WITH UNDERSTANDING THE PRODUCT AND THE BUYER -- NEVER WRITE COPY WITHOUT KNOWING BOTH.

### Step 1: Gather Product Intelligence

1. **Product name** — exact name for the listing
2. **Product category** — candle, software, t-shirt, supplement, etc.
3. **Key features/specs** — dimensions, materials, capabilities, integrations
4. **Target buyer** — who buys this and why
5. **Platform(s)** — Shopify, Amazon, Etsy, WooCommerce
6. **Price point** — calibrates tone (budget vs. premium)
7. **Brand voice** — default: conversational and confident
8. **Existing photos** — what the buyer can see vs. what copy must communicate
9. **Competitor positioning** — what others say, so we say something different
10. **Top objection** — #1 reason someone hesitates to buy

If the user provides items 1-5, proceed with defaults for the rest. If they have an existing listing, read it with `Read`, identify weaknesses, rewrite with improvements flagged.

### Step 2: Write the Listing

Generate every element in this order:

1. **Title** — keyword-optimized, primary keyword first, within platform character limit
2. **Bullet points** — 5 bullets using the bullet formula (benefit first, then feature)
3. **Short description** — 2-3 sentences for search previews and quick scanning
4. **Long description** — storytelling paragraph + specs section + social proof cues + CTA
5. **SEO meta** — meta title, meta description, URL slug, alt text suggestions, backend keywords if Amazon
6. **Tags** — platform-appropriate (13 tags for Etsy, backend terms for Amazon)

**WRITING RULES:**
- **LEAD EVERY BULLET WITH A BENEFIT, THEN THE FEATURE** — not "Made with organic cotton" but "Softer on your skin -- 100% GOTS-certified organic cotton"
- Sensory language for physical products; technical precision for SaaS
- Address the top objection in the long description
- Include social proof — stats if available; credibility cues if not
- End with a specific CTA — "Light it tonight" beats "Buy now"
- 8th-grade reading level — short sentences, common words, active voice
- **NEVER use unsubstantiated superlatives** — no "best", "#1", "world-class" without proof

### Step 3: Present and Verify

1. Show the complete listing with all elements labeled
2. Display character counts next to every limited field: `Title: "..." (63/200 chars)`
3. Flag elements within 10% of the limit
4. Multiple platforms: show each version separately
5. **GATE: Ask the user to approve before saving**

### Step 4: Deliver

Save as `{product-name}-{platform}.md`. Multiple platforms: separate files. Include a copy-paste section at the end with raw text for pasting into the platform editor.

---

## Pre-Delivery Checklist

| Check | What to Verify |
|-------|----------------|
| Benefits lead bullets | Every bullet starts with what the buyer gets, not what the product has |
| Character limits met | Title, meta description, tags, and bullets all within platform limits |
| Top objection addressed | Long description directly neutralizes the #1 purchase hesitation |
| No unproven superlatives | Zero instances of "best", "#1", "world-class" without evidence |
| Sensory or technical language | Physical products use texture/scent/feel; digital products use speed/metrics/outcomes |
| Social proof present | Customer count, rating, certification, or credibility statement included |
| CTA at the end | Long description ends with a clear call to action |
| SEO complete | Title keywords, meta description, URL slug, alt text, and tags all present |
| Reading level appropriate | Short sentences, common words, no unexplained jargon |

---

## Recovery and Troubleshooting

**User provides minimal product information:** Ask the 7-question brief. **NEVER fabricate features, specs, or claims.** If 3 clarification rounds fail, write with confirmed details and flag gaps with `[NEEDS: specific missing info]`.

**Existing listing needs improvement:** Read with `Read`, identify top 3 weaknesses (feature-first bullets, missing SEO, wall of text). Present before/after comparison with improvements flagged.

**Writing for multiple platforms:** Write Shopify version first, adapt to each platform's limits. Save separate files. **DO NOT copy-paste across platforms.**

**Character limit exceeded:** Cut filler words first (very, really, just, that, actually). Prioritize: primary keyword > main benefit > secondary details.

**User disagrees with copy direction:** Ask what feels off — tone, angle, or specific words. Present 2 alternative approaches using a different framework. After 3 revision rounds, ask the user for a sentence they like.

---

## Anti-Patterns

- **DO NOT** list features without benefits
- **DO NOT** exceed platform character limits
- **DO NOT** use superlatives without proof
- **DO NOT** copy competitor language
- **DO NOT** write walls of text — use bullets, headers, line breaks
- **DO NOT** use jargon without explanation
- **DO NOT** skip the objection
- **DO NOT** write generic CTAs
- **DO NOT** stuff keywords
- **DO NOT** fabricate reviews or statistics
