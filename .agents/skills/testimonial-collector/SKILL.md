---
name: testimonial-collector
description: "Dựng hệ thống thu thập lời chứng thực hoàn chỉnh: mẫu email xin nhận xét, chuỗi nhắc lại, biểu mẫu ghi nhận có cấu trúc và hướng dẫn đặt ở đâu cho hiệu quả. Dùng khi cần chứng thực dùng cho bán hàng."
allowed-tools: Read Write Glob
ten-viet: "Hệ Thu Thập Chứng Thực"
nhom: "06. Email & Tự Động Hoá"
ten-goc: "Testimonial Collector"
---

# Hệ Thu Thập Chứng Thực

## When to Use This Skill

Use this skill when:
- A user wants to systematically collect testimonials from clients or customers
- Someone needs social proof for a website, sales page, or marketing materials
- A business owner has happy customers but no documented testimonials
- A user wants to turn client results into case studies

**DO NOT** use for writing fake testimonials, reputation management, third-party platform reviews (Google, Google Maps), or NPS/survey systems.

---

TESTIMONIALS THAT TELL A STORY OUTSELL TESTIMONIALS THAT GIVE PRAISE. "THEY WERE GREAT!" IS WORTHLESS. "I WAS STUCK AT 130 nghìn đK/MONTH, TRIED THREE OTHER COACHES, AND HIT 390 nghìn đK WITHIN 90 DAYS" IS PROOF.

---

## Testimonial Prompt Framework

| # | Question | Extracts |
|---|----------|----------|
| 1 | What was your situation before working with us? | "Before" state — pain, frustration |
| 2 | What had you already tried that was not working? | Failed alternatives — you as the solution |
| 3 | What specific results have you seen? | Concrete outcomes — numbers, timelines |
| 4 | What surprised you most about the experience? | Emotional detail — feels real |
| 5 | Who would you recommend this to, and why? | Reader self-identifies |

**DEFAULT: All 5 questions.** If fewer requested, keep 1, 3, and 5 at minimum.

---

## Step 1: Understand

1. **Business type** — what they sell and to whom
2. **Testimonial types** — written, video, case study, screenshot (default: written)
3. **Where used** — homepage, sales page, email, social, proposals, ads
4. **Current state** — existing testimonials? Clients served?
5. **Communication channel** — email, Slack, DM, in-person
6. **Client results** — measurable outcomes they deliver

**GATE: Do not proceed until you have: business type, placement, and client results.**

---

## Step 2: Build

### 2A: Request Email Templates

**Email 1 — Initial Ask** (1-3 days after milestone or praise): Lead with gratitude. Include all 5 prompt questions. Offer reply or form option. Under 150 words before questions.

**Email 2 — Follow-Up** (5-7 days later, no response): Acknowledge they are busy. Include only questions 1, 3, 5. Add one example of a good testimonial.

**Email 3 — Thank You** (after receiving): Thank specifically. Explain where it will be used. Ask permission for name/photo. Offer to share final version before publishing.

### 2B: Capture Format

```
## Your Experience with [Business Name]

1. What was your situation before working with us?
2. What had you already tried that was not working?
3. What specific results have you seen since working with us?
4. What surprised you most about the experience?
5. Who would you recommend this to, and why?

- May we use your full name? [ ] Yes [ ] First name only [ ] Anonymous
- May we use your photo/logo? [ ] Yes [ ] No
- Open to a 5-min video call? [ ] Yes [ ] Maybe later [ ] No
```

### 2C: Timing Guide

| Trigger | Ask Within |
|---------|------------|
| Client hits a measurable result | 1-3 days |
| Unsolicited praise (email, DM) | Same day |
| Project delivery or completion | 1-5 days |
| Repeat purchase or renewal | Within 1 week |
| Client refers someone to you | Same day |

**DEFAULT: Strongest trigger is unsolicited praise.** Respond immediately: "That means a lot — would you mind if I shared that?"

### 2D: Follow-Up Sequence

```
Day 1:  Email 1 (Initial Ask)
Day 7:  No response → Email 2 (Follow-Up, questions 1/3/5 only)
Day 14: No response → Short DM: "No pressure — just bumping this."
Day 21: No response → Stop. Re-ask after next milestone.
```

**NEVER more than 3 touchpoints per request.**

---

## Step 3: Present

Show the complete system for approval: all three email templates, capture format, timing guide, and follow-up sequence — all customized with the user's business details.

**GATE: Do not write files until the user approves.**

---

## Step 4: Deliver

Write to `testimonial-system/` (or user-specified path):

```
testimonial-system/
├── request-emails.md        # 3 email templates
├── capture-format.md        # 5-question form
├── timing-and-followup.md   # Timing triggers + follow-up cadence
└── placement-guide.md       # Where to display testimonials
```

**Placement guide:**

| Placement | What Works Best |
|-----------|----------------|
| **Homepage** | 2-3 short quotes with names/photos near hero CTA |
| **Sales page** | Full story testimonials near pricing section |
| **Email** | One-line quotes in P.S. lines of nurture sequences |
| **Social media** | Screenshot testimonials or quote graphics |
| **Proposals** | 1-2 testimonials from similar-industry clients |
| **Ads** | Video clips or short quotes overlaid on imagery |

Suggest: "Send Email 1 to your 3-5 happiest clients this week."

---

## Anti-Patterns

- **DO NOT** beg or over-apologize in templates. You are offering a chance to share success.
- **DO NOT** ask mid-project before results are achieved.
- **DO NOT** exceed 7 questions. Five is the default.
- **DO NOT** reuse one testimonial everywhere without matching it to placement purpose.
- **DO NOT** skip the permission step for name, photo, and usage.
- **DO NOT** edit testimonials to change meaning. Typos and trim only.

---

## Recovery

- **Zero clients:** Build the system now. Collect screenshot praise as interim social proof.
- **Cannot identify who to ask:** Filter for referrers, renewals, unsolicited praise, strongest results. Start with top 5.
- **Vague praise received:** Follow up: "Could you share one specific result? Even a sentence makes a big difference."
- **Client never submits:** 3-touch sequence, then stop. Wait for next trigger.
- **Video reluctance:** Offer a 5-minute Zoom call instead of solo recording.
- **3 failed requirement attempts:** Ask for their website and reverse-engineer what testimonials they need.

---

## Ghi kết quả vào đâu

> [!important] Không ghi vào vault thì coi như chưa làm
> Kết quả chỉ hiện trong khung chat sẽ mất khi đóng phiên. Hệ thống chỉ thông minh bằng đúng dữ liệu được ghi lại.

| | |
|---|---|
| **Thư mục** | `04. Resources/Feedback & Chứng Thực/` |
| **Tên file** | `[Loại] — [Tên khách] (PK<số>).md` |
| **Bắt buộc** | Ảnh, video để `Media/` cùng thư mục; link tới sản phẩm và `People/` |

Sau khi ghi xong, báo lại cho người dùng **đường dẫn đầy đủ** của file vừa tạo để họ mở kiểm tra.
