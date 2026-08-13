---
name: content-calendar
description: "Tạo lịch nội dung 30 ngày, mỗi bài gắn với trụ cột nội dung, nền tảng và ngày đăng, kèm mẫu thiết kế khởi điểm cho từng trụ cột. Dùng khi cần một lịch đăng bài cụ thể thay vì làm tới đâu nghĩ tới đó."
allowed-tools: Read Write Glob mcp__claude_ai_Canva__generate-design mcp__claude_ai_Canva__list-brand-kits mcp__claude_ai_Canva__create-folder mcp__claude_ai_Canva__move-item-to-folder mcp__claude_ai_Canva__get-design-thumbnail
ten-viet: "Lịch Nội Dung 30 Ngày"
nhom: "03. Nội Dung & Sáng Tạo"
ten-goc: "Content Calendar"
---

# Lịch Nội Dung 30 Ngày

## When to Use This Skill

Use this skill when the user needs to:
- Plan 30 days of content across one or more platforms
- Build a structured posting schedule mapped to content pillars and post types
- Create a local Markdown tracker to track content status from idea through published
- Generate starter Canva graphic templates for each content pillar
- Batch-plan content for Instagram, LinkedIn, X/Twitter, YouTube, TikTok, newsletter, or podcast

**DO NOT** use this skill for:
- Writing full-length blog posts or articles (use a content writing skill)
- Creating individual social media graphics on demand (use social-media-graphics)
- Managing an existing content calendar that already lives in Obsidian
- One-off post creation with no broader monthly plan

---

## Content Pillar Framework

Every calendar is built on 3-5 content pillars. Pillars prevent random posting and make batching possible.

| Pillar Type | Purpose | Example (Fitness Coach) | Example (SaaS Founder) |
|-------------|---------|------------------------|----------------------|
| **Education** | Teach your audience something actionable | "3 exercises for desk workers" | "How to reduce churn with onboarding emails" |
| **Authority** | Showcase expertise, results, credentials | "Client transformation: 12 weeks" | "We hit $50K MRR — here's what worked" |
| **Connection** | Build trust through personality and story | "Why I became a trainer after burnout" | "The worst bug I shipped and what it taught me" |
| **Promotion** | Drive sales, signups, or conversions | "Spots open for 1:1 coaching" | "Try our free plan — no credit card needed" |
| **Community** | Engage and involve the audience | "What's your biggest gym struggle?" | "Poll: What feature should we build next?" |

**DEFAULT: 4 pillars** — Education, Authority, Connection, Promotion.

---

## Common Posting Frequencies

| Schedule | Posts/Week | Best For | Monthly Total |
|----------|-----------|----------|---------------|
| Light | 3 | Solopreneurs with limited time, B2B LinkedIn-only | 12-13 |
| Standard | 5 | Most creators, coaches, consultants | 21-22 |
| Active | 7 | Full-time creators, brand accounts | 30 |
| Aggressive | 10-14 | Multi-platform creators, agencies | 42-60 |

**DEFAULT: 5 posts/week (Standard)**

---

## Post Type Reference

| Post Type | Platform Fit | Engagement Level | Production Effort |
|-----------|-------------|-----------------|-------------------|
| Carousel | Instagram, LinkedIn | High | Medium |
| Reel/Short | Instagram, TikTok, YouTube Shorts | Very High | High |
| Story | Instagram, Facebook | Medium | Low |
| Text post | X/Twitter, LinkedIn | Medium | Low |
| Thread | X/Twitter | High | Medium |
| Image post | Instagram, LinkedIn, Facebook | Medium | Medium |
| Newsletter | Email | High | High |

---

## Core Workflow

EVERY CALENDAR STARTS WITH CONTENT PILLARS — NEVER GENERATE POST IDEAS WITHOUT ESTABLISHING PILLARS FIRST.

### Step 1: Understand

Gather these inputs from the user before generating anything:

1. **Business/niche** — what they do and who they serve
2. **Content pillars** — their 3-5 core topics (offer the framework table if they are unsure)
3. **Target platforms** — which platforms they post on
4. **Posting frequency** — how many posts per week (offer the frequency table if unsure)
5. **Audience** — who they are trying to reach
6. **Upcoming events** — product launches, sales, holidays, or milestones in the next 30 days
7. **Brand voice** — tone descriptors (professional, casual, witty, motivational, direct)

**If the user provides items 1-3, proceed with defaults for items 4-7.**

**GATE: Do not proceed to Step 2 until you have at minimum: business/niche, platforms, and either user-provided or default-assigned content pillars.**

---

### Step 2: Generate

Build 30 days of content ideas mapped to pillars, platforms, post types, and dates.

1. **Assign pillar distribution** — for 5 posts/week with 4 pillars:
   - Education: 2x/week (40%)
   - Authority: 1x/week (20%)
   - Connection: 1x/week (20%)
   - Promotion: 1x/week (20%)

   Education always gets the highest share. Promotion never exceeds 25%.

2. **Map post types to platforms:**
   - Instagram: carousel (2x), reel (1x), image (1x), story (bonus)
   - LinkedIn: text post (2x), carousel (1x), link post (1x), image (1x)
   - X/Twitter: text post (2x), thread (1x), link post (1x), image (1x)

3. **Generate 30 days of post ideas** with these fields per entry:
   - Date, Platform, Content Pillar, Post Type, Caption Idea, Status (default: "Idea")

4. **Weave in any upcoming events** — place promotional posts 3 days before, day-of, and 1 day after.

5. **Verify balance** — each pillar appears at least once per week; no more than 2 promotional posts in a row; post types vary within each week.

---

### Step 3: Present

Show the full calendar to the user for approval before creating anything in Obsidian or Canva.

Present a summary table showing the first 7 days in detail, then ask for approval:

```
Does this direction look right? I can:
- Swap any pillar assignments
- Change post types for specific days
- Add or remove platforms
- Adjust the posting frequency

Once approved, I'll create the full local Markdown tracker and Canva pillar templates.
```

**GATE: Do not proceed to Step 4 until the user approves the calendar direction.**

---

### Step 4: Act

Create the local Markdown tracker and Canva starter templates.

#### 4A: Create the Markdown tracker

1. Call `Glob` to check for existing content-related pages
2. Use `Write` to create or update a Markdown note with these properties:

   | Property | Type |
   |----------|------|
   | Post Title | Title |
   | Date | Date |
   | Platform | Select |
   | Pillar | Select |
   | Post Type | Select |
   | Status | Select (Idea, Drafting, Ready, Scheduled, Published) |
   | Canva Link | URL |
   | Notes | Rich text |

   Database title: `Content Calendar — [Month Year]`

3. Call `Write` to add all 30 days as individual entries. All entries default to "Idea" status.

#### 4B: Create Canva Starter Templates

1. Call `list-brand-kits` to load the user's brand colors and fonts
2. Call `create-folder` with the name: `Content Calendar — [Month Year]`
3. Generate one template per pillar using `generate-design` (1080x1080 square):

   | Pillar | Template Direction |
   |--------|-------------------|
   | Education | Clean numbered list or tip format |
   | Authority | Bold headline with metric/testimonial space |
   | Connection | Casual story-style layout |
   | Promotion | CTA-focused design with urgency element |
   | Community | Question-centered with engagement prompt |

4. Call `get-design-thumbnail` to verify quality
5. Call `move-item-to-folder` for each template
6. Deliver the complete package with Obsidian link, Canva folder link, and suggested workflow

---

## Recovery and Troubleshooting

### Markdown tracker Creation Fails
Inform the user and fall back to generating the full 30-day calendar as a markdown table for manual import.

### Canva Design Generation Fails
1. Simplify the prompt and retry once
2. If still failing, skip that template and deliver the others with manual specs (dimensions, colors, layout description)

### Brand Kit Not Found in Canva
Ask for primary/secondary color hex codes and font preference, then proceed with manual values.

### User Has No Content Pillars
Present the Content Pillar Framework table and recommend the default 4. Do not proceed without at least 3 defined pillars.

### Calendar Feels Repetitive
- Check if any post type appears more than 3 times in one week
- Vary caption angles within the same pillar (problem-focused, story, data, how-to)
- Alternate platforms day by day instead of clustering

---

## Anti-Patterns

- **DO NOT** generate post ideas without establishing content pillars first
- **DO NOT** schedule more than 25% promotional content
- **DO NOT** assign the same post type to the same platform 3+ days in a row
- **DO NOT** create Canva templates before the user approves the calendar
- **DO NOT** front-load promotional posts in week 1 — warm the audience first
