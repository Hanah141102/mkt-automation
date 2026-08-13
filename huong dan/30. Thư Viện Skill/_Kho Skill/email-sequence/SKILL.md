---
name: email-sequence
description: "Xây chuỗi email tự động hoàn chỉnh: khoảng cách thời gian, điều kiện kích hoạt, tiêu đề để thử nghiệm A/B và ghi chú cài đặt trên từng nền tảng. Dùng khi cần một luồng email chạy tự động."
allowed-tools: Read Write Glob
ten-viet: "Chuỗi Email Tự Động"
nhom: "06. Email & Tự Động Hoá"
ten-goc: "Email Sequence"
---

# Chuỗi Email Tự Động

## When to Use This Skill

Use this skill when you need to:
- Build a welcome series that onboards new subscribers and sets expectations
- Create a nurture sequence that warms leads toward a purchase or action
- Write a launch sequence that drives sales for a product, course, or service drop
- Design a re-engagement campaign that wins back inactive subscribers
- Map out any multi-email automation with timing delays and conditional triggers

**DO NOT** use this skill for one-off email drafts, cold outreach to strangers (use cold-outreach instead), or transactional emails (order confirmations, password resets).

---

## Core Principle

EVERY EMAIL IN THE SEQUENCE MUST EARN THE NEXT OPEN — IF A SUBSCRIBER DOES NOT HAVE A REASON TO OPEN EMAIL 3, EMAILS 4 THROUGH 7 ARE DEAD.

---

## Sequence Type Reference

| Sequence Type | Emails | Duration | Primary Goal | Default Trigger |
|---------------|--------|----------|-------------|----------------|
| **Welcome** | 5 | 14 days | Orient, build trust, deliver lead magnet value | New subscriber opt-in |
| **Nurture** | 7 | 30 days | Educate, build authority, warm toward offer | Completed welcome series |
| **Launch** | 6 | 7 days | Drive purchase during a specific window | Launch date / cart open |
| **Re-engagement** | 3 | 10 days | Reactivate or clean inactive subscribers | No opens in 60+ days |

---

## Phase 1: Strategy

Gather the information needed to build the right sequence:

1. **Sequence type** — welcome, nurture, launch, or re-engagement (ask, no default)
2. **Goal** — what action should the subscriber take by the end?
3. **Audience** — who is receiving this sequence? awareness level?
4. **Number of emails** — use the reference table defaults unless the user overrides
5. **Platform** — một nền tảng gửi email, một nền tảng gửi email, ActiveCampaign, or other (một nền tảng gửi email by default)
6. **Brand voice** — casual, professional, bold, warm (casual-professional by default)
7. **Product or offer** — what are they ultimately selling or promoting?
8. **Lead magnet or entry point** — what did the subscriber opt in for?

**GATE: Do not proceed to Phase 2 until the user confirms or adjusts the strategy brief.**

---

## Phase 2: Map the Flow

Build the sequence map before writing any email copy.

### Sequence Map Format

For each email, define:
1. **Email number and name** — descriptive label
2. **Send timing** — delay from trigger or previous email
3. **Purpose** — one sentence on what this email accomplishes
4. **Conditional trigger** — any branching logic (opened/clicked/purchased)
5. **CTA** — the single action you want the reader to take

### Conditional Branch Patterns

| Trigger | Action | Platform Notes |
|---------|--------|---------------|
| Opened Email X | Send follow-up variant | All platforms support this |
| Clicked link in Email X | Tag subscriber, branch to offer path | một nền tảng gửi email: "Link Trigger" |
| Did NOT open Email X | Resend with new subject line after 48h | một nền tảng gửi email: Visual Automations |
| Purchased product | Remove from sales sequence, add to customer sequence | Requires integration |
| Replied to email | Tag as "engaged," prioritize for personal follow-up | Manual or via helpdesk |

**GATE: Present the full sequence map to the user. Do not write email copy until the map is approved.**

---

## Phase 3: Write the Emails

### Email Format

For every email, deliver:

1. **Subject Line A** — primary subject line
2. **Subject Line B** — A/B test variant (different angle, not just a word swap)
3. **Preview text** — 40-90 characters, complements the subject line
4. **Body** — the full email copy
5. **CTA** — clearly marked in the body
6. **Send timing** — exact delay from previous email or trigger

### Subject Line Rules

- A/B variants must test different angles, not just synonyms
- Keep under 50 characters
- Preview text must complement, not repeat the subject line
- NEVER use ALL CAPS, excessive punctuation, or spam trigger words

### Email Body Rules

- **One CTA per email** — not two, not "also check out"
- **Length varies by purpose:** delivery emails short (100 words), story emails longer (300 words), sales emails 200-400 words
- **Line breaks** — no paragraph longer than 3 sentences
- **Write in second person** ("you") with first person ("I") for personal voice
- **End every email with a P.S. line** — second most-read part of any email

**GATE: Present all emails to the user as a complete sequence. Do not finalize until the user approves the copy, subject lines, and timing.**

---

## Phase 4: Deliver

### Platform Implementation Notes

#### một nền tảng gửi email
- Create a Visual Automation with the opt-in form as the trigger
- Add each email as an "Email" step with "Delay" steps between them
- Use "Conditions" for branching (clicked link, tag applied, purchased)
- A/B subject lines: use the built-in "A/B" toggle on each email step

#### một nền tảng gửi email
- Build the sequence as a "Customer Journey" (not a classic automation)
- Use "If/Else" branches for conditional logic
- A/B subject lines: toggle "A/B Test," select "Subject Line," set sample size to 50%

#### ActiveCampaign
- Create an Automation with the trigger as "Subscribes to list" or "Tag is added"
- Branching: "If/Else" blocks based on "Has opened email," "Has clicked link," or "Has tag"
- A/B: use the "Split Action" for 50/50 splits

### A/B Testing Defaults

| Parameter | Default |
|-----------|---------|
| Split ratio | 50/50 |
| Wait time before picking winner | 4 hours |
| Winning metric | Open rate (subject lines), Click rate (body variants) |
| Minimum sample size | 100 subscribers (below this, skip A/B) |

### Pre-Delivery Checklist

```
- [ ] Every email has a single, clear CTA
- [ ] Subject lines are under 50 characters
- [ ] Preview text does not repeat the subject line
- [ ] A/B subject lines test different angles, not word swaps
- [ ] No email sends less than 24 hours after the previous one
- [ ] Conditional branches are clearly labeled
- [ ] P.S. line included on every email
- [ ] Personalization tokens are correct for the platform
- [ ] Purchase / goal exit points are defined
- [ ] Tone is consistent across all emails
- [ ] No spam trigger words in subject lines
```

---

## Anti-Patterns

- **Sending daily emails in a nurture sequence** — subscribers feel bombarded. Minimum 2-day gaps for welcome/nurture.
- **Clickbait subject lines** — erodes trust and trains subscribers to ignore you.
- **Burying the CTA** — the CTA should be visible without excessive scrolling.
- **Multiple CTAs per email** — one email, one ask.
- **No clear reason to open the next email** — each email should tease or set up the next one.
- **Skipping the welcome email** — sending a nurture or pitch email first breaks trust.
- **Identical A/B subject lines** — variants must represent different hooks or angles.
- **Walls of text** — no paragraph longer than 3 sentences.

---

## Recovery

- **User unsure which sequence type:** Ask what triggered the request. If they just launched a lead magnet → welcome series. Engaged list + product to sell → launch sequence. Dropping open rates → re-engagement.
- **User wants more emails than recommended:** Flag the risk of drop-off after the midpoint. Front-load the most important content.
- **User has no lead magnet or entry point:** Help them define one before building the welcome sequence.
- **List under 100 subscribers:** Skip A/B testing. Start A/B when they cross 500 subscribers.
- **If 3 revision rounds produce no approval:** Ask the user to share an email they admire so you can match the voice and structure.

---

## Quick Reference: Timing Defaults by Sequence Type

### Welcome Series (5 Emails / 14 Days)

| Email | Name | Delay | Purpose |
|-------|------|-------|---------|
| 1 | The Welcome | Immediate | Deliver lead magnet, set expectations |
| 2 | The Quick Win | +2 days | Help them get a fast result |
| 3 | The Story | +2 days | Build trust through narrative |
| 4 | The Deeper Problem | +3 days | Name the obstacle, position solution |
| 5 | The Invitation | +7 days | Present the paid offer |

### Launch Series (6 Emails / 7 Days)

| Email | Name | Delay | Purpose |
|-------|------|-------|---------|
| 1 | The Announcement | Day 1 | Reveal the offer, generate excitement |
| 2 | The Deep Dive | Day 2 | Explain what is included and who it is for |
| 3 | The Social Proof | Day 3 | Share testimonials, results, case studies |
| 4 | The Objection Handler | Day 5 | Address the top 1-2 reasons people hesitate |
| 5 | The Deadline Warning | Day 6 | Remind them the window is closing |
| 6 | The Final Call | Day 7 | Last chance, cart closes tonight |

### Re-engagement Series (3 Emails / 10 Days)

| Email | Name | Delay | Purpose |
|-------|------|-------|---------|
| 1 | The Check-In | Day 1 | Acknowledge the silence, offer value |
| 2 | The Best-Of | +5 days | Share your top-performing content they missed |
| 3 | The Farewell | +4 days | Let them self-select: stay or unsubscribe |

---

## Ghi kết quả vào đâu

> [!important] Không ghi vào vault thì coi như chưa làm
> Kết quả chỉ hiện trong khung chat sẽ mất khi đóng phiên. Hệ thống chỉ thông minh bằng đúng dữ liệu được ghi lại.

| | |
|---|---|
| **Thư mục** | `03. Areas/Marketing Channels/` |
| **Tên file** | `Chuỗi Email — [Mục đích].md` |
| **Bắt buộc** | Link tới offer và giai đoạn phễu tương ứng |

Sau khi ghi xong, báo lại cho người dùng **đường dẫn đầy đủ** của file vừa tạo để họ mở kiểm tra.
