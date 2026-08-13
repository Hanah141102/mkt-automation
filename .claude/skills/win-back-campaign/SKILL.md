---
name: win-back-campaign
description: "Xây chuỗi email và tin nhắn kéo lại khách đã rời bỏ hoặc lâu không mua, có điều kiện kích hoạt cá nhân hoá và chiến lược ưu đãi. Dùng khi muốn hồi sinh tệp khách cũ."
allowed-tools: Read Write Glob
ten-viet: "Chiến Dịch Kéo Khách Quay Lại"
nhom: "06. Email & Tự Động Hoá"
ten-goc: "Win-Back Campaign"
---

# Chiến Dịch Kéo Khách Quay Lại

## When to Use This Skill

Use this skill when you need to:
- Re-engage email subscribers who have gone silent (no opens or clicks in 30+ days)
- Win back lapsed customers who stopped buying from an e-commerce store or service
- Recover churned users from a SaaS tool, membership, or subscription
- Build a segmented re-engagement sequence that treats at-risk, lapsed, and churned contacts differently
- Create a graceful exit path that cleans your list of people who no longer want to hear from you

**DO NOT** use this skill for welcome sequences, cold outreach to strangers, or subscribers who never engaged in the first place.

---

## Core Principle

WIN-BACK IS NOT BEGGING — IT IS REMINDING PEOPLE WHY THEY CARED IN THE FIRST PLACE AND GIVING THEM A CLEAR REASON TO COME BACK OR A CLEAN WAY TO LEAVE.

---

## Phase 1: Segment

Before writing any email, define who you are writing to and why they went quiet.

### Gather These Inputs

1. **Business type** — SaaS, e-commerce, service, membership, newsletter, course
2. **Product or service** — what the person was buying or using
3. **Why people churn** — main reason people disengage, if known (unknown)
4. **Incentive budget** — discount, bonus, or free trial available? (yes, up to 15%)
5. **Email platform** — ConvertKit, Mailchimp, ActiveCampaign, Klaviyo
6. **Inactive list size** — rough count for segmentation

### Inactivity Segments

| Segment | Inactivity Period | Strategy | Incentive Level |
|---------|------------------|----------|----------------|
| **At-Risk** | 30-60 days | Gentle nudge, value reminder | None needed |
| **Lapsed** | 60-120 days | Value reminder + soft incentive | Soft (free resource, small bonus) |
| **Churned** | 120+ days | Strong incentive or graceful goodbye | Strong (discount, free month) |

**GATE: Do not proceed to Phase 2 until the user confirms the business type and at least one segment is defined.**

---

## Phase 2: Write

Write email templates for each segment.

### Email A: "We miss you" (At-Risk — Day 1)

**Purpose:** Personal, value-focused nudge. No discount, no pressure. Remind them why they signed up.

**Subject line formulas:** "it's been a while, {first_name}" / "still growing?" / "your {product} misses you"

**Structure:** (1) Acknowledge the gap. (2) Show what's new or what they've earned. (3) Soft CTA. (4) Invite a reply.

### Email B: "Here's what you're missing" (Lapsed — Day 5)

**Purpose:** Social proof, new features, FOMO. Show them the world moved forward.

**Subject line formulas:** "here's what changed since you left" / "{first_name}, you missed this" / "3 things that happened while you were away"

**Structure:** (1) Lead with a number (1,400 teams joined, 3 new features). (2) List specific improvements. (3) Soft invite back. (4) P.S. with a social proof moment.

### Email C: "Come back for X% off" (Lapsed — Day 10)

**Purpose:** Incentive offer with a clear deadline. First email with a discount.

**Subject line formulas:** "a little something to welcome you back" / "{first_name}, this is just for you" / "come back — this one's on us"

**Structure:** (1) Brief, direct. (2) State the offer and code. (3) Set expiry date. (4) Link to shop/platform. (5) P.S. with the expiry date again.

### Email D: "Should we part ways?" (Churned — Day 14)

**Purpose:** Honest, respectful final email. Clear choice: come back or unsubscribe cleanly.

**Subject line formulas:** "should we stop emailing you?" / "one last thing, {first_name}" / "stay or go — totally your call"

**Structure:** (1) Acknowledge no response. (2) OPTION A: reactivate link. (3) OPTION B: unsubscribe link. (4) Auto-suppress notice. (5) P.S. asking for feedback.

**GATE: Present all four email templates. Do not finalize until the user approves the tone, incentive levels, and personalization approach.**

---

## Phase 3: Sequence

### Default Sequence: 4 Emails Over 14 Days

```
TRIGGER: Contact meets inactivity threshold for any segment
  |
EMAIL 1: "We miss you" (Day 1) — Segments: All
  +--- IF re-engaged (opened + clicked) ---> EXIT, tag "won-back"
  |  [Wait 4 days]
EMAIL 2: "Here's what you're missing" (Day 5) — Segments: Lapsed + Churned
  +--- IF re-engaged ---> EXIT, tag "won-back"
  |  [Wait 5 days]
EMAIL 3: "Come back for X% off" (Day 10) — Segments: Lapsed + Churned
  +--- IF re-engaged ---> EXIT, tag "won-back"
  |  [Wait 4 days]
EMAIL 4: "Should we part ways?" (Day 14) — Segments: Churned only
  +--- IF clicked reactivate ---> EXIT, tag "won-back"
  +--- IF clicked unsubscribe ---> Remove from all lists
  +--- IF no action in 7 days ---> Auto-suppress
```

### Conditional Logic Rules

| Condition | Action |
|-----------|--------|
| Re-engaged (opened + clicked) | Exit sequence, apply "won-back" tag |
| Used discount code / reactivated | Exit sequence, tag "won-back" |
| Clicked unsubscribe in Email 4 | Remove from all marketing lists immediately |
| No action after Email 4 + 7 days | Auto-suppress, keep in database for annual re-check only |
| Hard bounce on any email | Remove immediately, stop remaining emails |

**GATE: Present the complete sequence map. Do not finalize until the user confirms the flow, timing, and platform.**

---

## Phase 4: Deliver

### Pre-Send Checklist

```
- [ ] Cleaned hard bounces BEFORE sending (critical for deliverability)
- [ ] Segmented contacts into At-Risk, Lapsed, and Churned tiers
- [ ] Personalization tokens are mapped correctly in the platform
- [ ] Incentive codes are created, tested, and set to expire on the correct date
- [ ] Unsubscribe link works and is clearly visible in every email
- [ ] Sequence exit conditions are configured
- [ ] Auto-suppress is set for non-responders after Email 4 + 7 days
- [ ] Subject lines are under 50 characters
- [ ] Emails render correctly on mobile
- [ ] Reply-to address is monitored by a real person
```

---

## Anti-Patterns

- **Emailing people who never engaged** — they are uninterested, not lapsed. Clean them off the list.
- **Offering a discount in the first email** — leads with discounts trains people to wait for them.
- **Guilt-tripping language** — "We're sad you left" is manipulative. Be honest, be helpful.
- **Skipping the unsubscribe option in the final email** — no exit means spam complaints.
- **No segmentation** — a 35-day-inactive subscriber needs different messaging than a 150-day-inactive one.
- **Ignoring hard bounces before sending** — clean BEFORE sending.
- **More than 4 emails to non-responders** — four ignored emails means move on.

---

## Recovery

- **Unknown churn reason:** Use a "life got busy" angle and include a reply-to question in Email 1. Replies reveal churn reasons for future iterations.
- **No incentive budget:** Replace Email 3 with a "what's changed" email using social proof. Converts at 3-5% instead of 8-12%, but still works.
- **Inactive list under 100 contacts:** Skip segmentation. Send a single 3-email sequence to everyone.
- **No purchase or login data to segment by:** Segment by email engagement. At-Risk = opened but no clicks. Lapsed = no opens in 60-120 days. Churned = no opens 120+ days.
- **Domain reputation already damaged:** Fix deliverability first. Clean hard bounces, warm up by sending to engaged subscribers only for 2-4 weeks.
