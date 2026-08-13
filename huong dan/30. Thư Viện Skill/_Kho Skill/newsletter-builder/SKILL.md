---
name: newsletter-builder
description: "Tạo newsletter hoàn chỉnh từ brief biên tập đến bản trình bày cuối: lên nội dung rồi xuất bản thiết kế. Dùng khi cần sản xuất bản tin định kỳ gửi cho danh sách email."
allowed-tools: Read Write Glob mcp__claude_ai_Canva__generate-design-structured mcp__claude_ai_Canva__list-brand-kits mcp__claude_ai_Canva__export-design mcp__claude_ai_Canva__get-export-formats mcp__claude_ai_Canva__get-design-thumbnail
ten-viet: "Dựng Newsletter"
nhom: "03. Nội Dung & Sáng Tạo"
ten-goc: "Newsletter Builder"
---

# Dựng Newsletter

## When to Use This Skill

Use this skill when you need to:
- Produce a recurring newsletter issue from topic to send-ready output
- Build a new newsletter from scratch with structure, content, and visual design
- Transform raw notes or ideas into a polished newsletter with a designed layout
- Create both plain-text and visually designed PDF versions of a newsletter

**DO NOT** use for one-off promotional emails, social media content, or blog posts.

---

## Core Principle

EVERY NEWSLETTER EARNS ITS OPEN WITH THE SUBJECT LINE, EARNS ITS READ WITH THE INTRO HOOK, AND EARNS ITS CLICK WITH ONE CLEAR CTA — IF ANY OF THESE THREE FAIL, THE NEWSLETTER FAILS.

---

## Newsletter Structure Template

```
SUBJECT LINE:   [Curiosity gap or specific benefit — under 50 chars]
PREVIEW TEXT:    [Expands on subject — 40-90 chars, visible in inbox]

── HEADER ──        Newsletter name, issue number, date
── INTRO HOOK ──    2-3 sentences. Bold claim, story beat, or question.
── SECTION 1 ──     200-300 words. Primary topic. Deepest value.
── SECTION 2 ──     150-250 words. Supporting angle or practical application.
── SECTION 3 ──     3-5 bullet points. Quick hits, links, tools. (optional)
── CTA ──           One clear ask. Direct sentence, not buried in a paragraph.
── SIGN-OFF ──      1-2 personal sentences. First-name basis.
── FOOTER ──        Unsubscribe placeholder, social links, legal line.
```

---

## Phase 1: Editorial Brief

Collect before writing anything:

1. **Newsletter name** — brand name
2. **Issue topic** — theme for this issue
3. **Target audience** — who reads it and what they care about
4. **Tone** — casual, professional, witty, conversational (default: conversational)
5. **Sections** — how many body sections (default: 2 + quick hits)
6. **Primary CTA** — the one action readers should take
7. **Key links** — any URLs, tools, or resources to include
8. **Recurring elements** — standing segments (e.g., "Tool of the Week")

If the user provides items 1, 2, and 6, proceed with defaults for the rest.

Compile into a structured brief:
```
## Editorial Brief — "The Growth Wire: Why Most Funnels Leak"
Newsletter: The Growth Wire
Audience: Solo founders and early-stage SaaS operators
Tone: Conversational, data-backed
Sections: Intro + 2 body + quick hits + CTA
CTA: Reply with their biggest funnel question
Links: [link1], [link2]
Recurring: "Tool of the Week" in quick hits
```

**GATE: Present the editorial brief. Do not proceed until the user confirms or adjusts.**

---

## Phase 2: Write Content

Write the full newsletter following the structure template.

1. **Subject line and preview text** — provide 2 subject line options. Subject: under 50 chars. Preview: 40-90 chars.

2. **Intro hook (2-3 sentences)** — open with a surprising stat, short story, or direct question. End by telling readers what they get from this issue.

3. **Body sections:**
   - **Section 1 (Primary):** 200-300 words. Must include a specific example, number, or case study.
   - **Section 2 (Supporting):** 150-250 words. Different angle, practical application, or contrarian take.
   - **Section 3 (Quick Hits):** 3-5 bullets with bolded lead-ins. Under 30 seconds to scan.

4. **CTA section** — one sentence, framed as a benefit to the reader.

5. **Sign-off** — 1-2 sentences.

### Save Brief to Obsidian

After writing, call `Glob` for the newsletter name. If found, use `Write` to create or update a Markdown note with title "{Newsletter} — {Topic}", including topic, audience, tone, CTA, subject line, and status "Draft". If no database found, create a standalone page.

**GATE: Present the full newsletter copy. Do not proceed until approved. Maximum 3 revision rounds.**

---

## Phase 3: Design in Canva

### Step 1: Load Brand Kit

Call `list-brand-kits` to retrieve kits. If multiple exist, let user choose. **IF NO BRAND KIT:** Ask for primary color, secondary color, and font preference.

### Step 2: Generate Layout

Build a structured prompt including newsletter name, all section headings and body text, brand colors/fonts, layout (single-column, 600px, mobile-friendly), and CTA styled as button.

Call `generate-design-structured`, then `get-design-thumbnail` to preview.

**Wait for approval before exporting. If design misses: regenerate with adjusted prompt. Maximum 2 attempts.**

---

## Phase 4: Export and Deliver

1. Call `get-export-formats` then `export-design` with format `pdf`
2. Save plain-text markdown to `newsletter-output/{name}-{topic}.md`
3. Update Obsidian status to "Designed"
4. Deliver summary with file paths, export URL, design ID, subject line, and preview text

---

## Anti-Patterns

- **Walls of text** — no paragraph over 4 lines. Readers scan, they do not read newsletters like articles.
- **Skipping the CTA** — every issue needs exactly one clear call to action.
- **Generic subject lines** — "Monthly Update" will not get opened. Create curiosity or promise a specific benefit.
- **Multiple CTAs** — pick one.
- **No preview text** — always write custom preview text.
- **Writing for everyone** — each issue speaks to a specific reader with a specific problem.

---

## Recovery

**Obsidian search finds nothing:** Create a standalone page. Obsidian is for records, not a blocker.

**local Markdown note creation fails:** Save brief locally to `newsletter-output/{name}-brief.md`. Continue to Phase 3.

**No Canva brand kit:** Ask for colors and font. Embed in prompt.

**Canva design generation fails:** Simplify prompt (headline + colors + CTA only), retry once. If 2 attempts fail: deliver plain-text only.

**Canva export fails:** Try PNG instead of PDF. If both fail, provide design ID for manual export from canva.com.

**If 3 attempts at any step fail:** Stop and deliver what is complete, explaining which step failed.

---

## Pre-Delivery Checklist

| Check | Verify |
|-------|--------|
| Subject line under 50 chars | Mobile inboxes truncate aggressively |
| Preview text written | Never blank or defaulted |
| Intro hook 2-3 sentences | Not a paragraph, not a single line |
| Clear heading on every section | Readers scan headings first |
| Section lengths vary | Mix long, medium, scannable |
| Exactly one CTA | Not zero, not three |
| CTA framed as reader benefit | "Get X" not "Help me by doing X" |
| No section over 300 words | Newsletters are not blog posts |
| Plain-text file saved | Pasteable into any email platform |
| Obsidian brief saved | Editorial record for future reference |
| Canva design approved | Thumbnail shown and confirmed |
| PDF exported | Designed version ready for sharing |
