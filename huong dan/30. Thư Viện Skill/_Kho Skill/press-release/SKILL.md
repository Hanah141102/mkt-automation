---
name: press-release
description: "Viết thông cáo báo chí chuẩn: tiêu đề, dòng địa danh và ngày, đoạn mở, phần thân, đoạn giới thiệu công ty và thông tin liên hệ. Dùng khi ra mắt sản phẩm, công bố hợp tác hoặc có sự kiện đáng đưa tin."
allowed-tools: Read Write Glob
ten-viet: "Thông Cáo Báo Chí"
nhom: "04. Mạng Xã Hội & SEO"
ten-goc: "Press Release"
---

# Thông Cáo Báo Chí

## When to Use This Skill

Use this skill when you need to:
- Announce a product launch, feature release, or service expansion to media outlets
- Share a funding round, revenue milestone, or company achievement with the press
- Publicize a new hire, promotion, or advisory board appointment
- Announce a partnership, acquisition, or strategic alliance
- Promote an event, grand opening, or community initiative
- Distribute an award, certification, or industry recognition

**DO NOT** use this skill for blog posts, social media announcements, internal memos, or marketing copy. This is for structured press releases intended for journalists and media distribution only.

---

## Core Principle

A PRESS RELEASE IS A NEWS DOCUMENT, NOT AN ADVERTISEMENT. EVERY SENTENCE MUST REPORT FACTS A JOURNALIST CAN VERIFY AND PUBLISH WITHOUT REWRITING.

---

## Phase 1: Brief

**Round 1 -- The News:**

| Input | What to Ask | Default |
|-------|------------|---------|
| **The news** | "What is the announcement? One sentence." | No default -- must be provided |
| **Release type** | "Which category: Product Launch, Funding/Milestone, Partnership, Hire/Promotion, Event, or Award?" | Infer from the news |
| **Who is involved** | "Company name, key people, and their titles." | No default -- must be provided |
| **Timing** | "Is this for immediate release, or is there an embargo date?" | For Immediate Release |
| **Quote attribution** | "Who should be quoted in the release? Name, title, company." | Company founder or CEO |

**Round 2 -- Context and Distribution:**

| Input | What to Ask | Default |
|-------|------------|---------|
| **Why it matters** | "Why should a journalist care? What is the impact on customers, the industry, or the community?" | No default -- push for this |
| **Supporting details** | "Any numbers, dates, features, pricing, or availability info to include?" | Include what the user provides |
| **Company boilerplate** | "Do you have an existing 'About [Company]' paragraph?" | Generate from user info |
| **Media contact** | "Name, email, and phone number for the media contact." | No default -- must be provided |
| **Target outlets** | "Which media outlets or journalist types are you targeting?" | General industry and local media |

**GATE: Do not proceed to Phase 2 until the user confirms the brief. Minimum required: the news, a quotable person with their title, company information, and a media contact.**

---

## Phase 2: Write

### Press Release Structure

```
**FOR IMMEDIATE RELEASE**
(or: **EMBARGOED UNTIL [Date], [Time] [Timezone]**)

# [Headline]

## [Subheadline -- optional]

**[CITY, STATE]** -- [Lead paragraph: who, what, when, where, why in 2-3 sentences.]

[Body paragraph 1: supporting details, context, market problem]

"[Quote from primary spokesperson]," said [Full Name], [Title] of [Company].

[Body paragraph 2: additional details — features, pricing, availability, partnerships]

"[Second quote -- optional]," said [Full Name], [Title] of [Company/Organization].

[Closing paragraph: where to learn more, availability, CTA]

### About [Company Name]

[Boilerplate: 2-4 sentences. What the company does, who it serves,
when it was founded, where it is headquartered. End with website URL.]

### Media Contact

[Full Name]
[Title]
[Company]
[Email]
[Phone]

###
```

### Section-by-Section Rules

**Release Line:** "FOR IMMEDIATE RELEASE" in bold, all caps. If embargoed, include exact date, time, and timezone.

**Headline:** Starts with an action verb (Launches, Announces, Secures, Expands, Appoints, Partners). Contains company name. Under 80 characters. Title case. No periods.

**Dateline:** Format: CITY, STATE (abbreviated per AP) followed by an em dash. Use company headquarters city.

**Lead Paragraph:** Answers who, what, when, where, and why in 2-3 sentences. Most important fact in the first sentence. No adjectives like "leading" or "innovative."

**Body Paragraph 1:** Context, market problem with a data point, how the announcement addresses it.

**Primary Quote:** Attributed to most senior relevant person. Forward-looking. Must sound like something a human would say. Format: "Quote text," said Full Name, Title of Company. Use "said" only.

**Body Paragraph 2:** Specific details: features, pricing, availability dates, partner names.

**Second Quote (optional):** External validation from a customer, partner, investor, or industry figure.

**Closing Paragraph:** Where to find more info, availability date or how to sign up. No new information.

**Boilerplate:** 2-4 sentences, present tense. No superlatives. End with company website URL.

**Media Contact:** Full name, title, company, email, phone — each on its own line.

**End Marker:** Three hash marks centered: ###

### AP Style Quick Reference

| Rule | Correct | Incorrect |
|------|---------|-----------|
| Headline case | Title Case for Headlines | title case for headlines |
| Oxford comma | red, white and blue | red, white, and blue |
| Numbers under 10 | spelled out: "five locations" | 5 locations |
| Numbers 10+ | numerals: "12 employees" | twelve employees |
| Percent | 8% (numeral + symbol) | eight percent |
| Dates | March 15 (no "th" or "st") | March 15th |
| States | abbreviated in datelines: Colo. | Colorado (in dateline) |
| Titles after names | Jordan Reeves, founder and CEO | Jordan Reeves, Founder and CEO |

**Length Target:** 400-600 words total.

**GATE: Do not save to file until the user explicitly approves. If more than 3 rounds of revisions, pause and ask whether to finalize or keep refining.**

---

## Phase 3: Review Checklist (internal)

1. FOR IMMEDIATE RELEASE or embargo notice at the top
2. Headline starts with action verb, contains company name, under 80 characters
3. Dateline format correct
4. Lead paragraph answers who, what, when, where, why
5. At least one attributed quote using "said"
6. Boilerplate with company description and URL
7. Media contact with name, email, phone
8. End marker (###) present
9. Total word count 400-600
10. No marketing superlatives

---

## Phase 4: Deliver

**Filename:** `[company-name]-[topic-keyword]-press-release.md`

After writing the file, confirm delivery and suggest distribution channels by release type:

| Release Type | Recommended Channels |
|-------------|---------------------|
| Product Launch | PR Newswire/Business Wire, industry trade publications, product review blogs, LinkedIn |
| Funding/Milestone | TechCrunch/Crunchbase, local business journal, LinkedIn post by founder |
| Partnership | Both companies' newsrooms, shared LinkedIn, industry trade press |
| Hire/Promotion | Local business journal "People on the Move," LinkedIn, industry associations |
| Event | Local newspaper event calendars, community groups, Eventbrite, industry newsletters |
| Award | Award-granting organization's press list, local media, industry trade publications |

Offer next steps: "Would you like me to write a pitch email to send to journalists alongside this release?"

---

## Anti-Patterns

- **DO NOT use marketing superlatives.** "Revolutionary," "game-changing," "world-class" are advertising words, not news words.
- **DO NOT bury the news.** The announcement must appear in the first sentence.
- **DO NOT write quotes no human would say.** Read the quote out loud — if it sounds like a corporate chatbot, rewrite it.
- **DO NOT skip the boilerplate.** Journalists use it to fact-check your company description.
- **DO NOT skip the media contact.** A press release without contact information is a dead end.
- **DO NOT use exclamation marks.** Not anywhere in the document.
- **DO NOT include an Oxford comma.** AP style omits the serial comma.
- **DO NOT exceed 600 words.**
- **DO NOT use first person** outside of direct quotes.

---

## Recovery

**User cannot articulate the news:**
Ask: "If a journalist wrote one sentence about your company tomorrow, what would it say?" Then: "What changed? A new product? A new number? A new person? A new relationship?" After 3 attempts: explain that a press release needs a concrete, specific piece of news.

**No quotable person available:**
Explain every press release needs at least one attributed quote. Write it and have them approve it. If truly no one available, use a placeholder: "[SPOKESPERSON NAME], [TITLE]" and flag it.

**No boilerplate exists:**
Ask: what the company does, who the customers are, where based. Write from those answers. Tell the user to save it for reuse.

**Announcement is not news:**
Be direct: "Journalists publish stories with a clear news hook — a launch date, a number, a name, or a milestone." Suggest a blog post or social media update if no hook can be found.

**File write fails:**
Present the complete press release in chat. Tell the user: "I was unable to save the file. The complete press release is above — you can copy it directly."

---

## Pre-Delivery Checklist

- [ ] "FOR IMMEDIATE RELEASE" or embargo notice at top
- [ ] Headline starts with action verb, contains company name, under 80 characters, title case
- [ ] Dateline uses correct AP state abbreviation
- [ ] Lead paragraph answers who, what, when, where, why
- [ ] At least one attributed quote using "said"
- [ ] Quote sounds like something the person would actually say
- [ ] Boilerplate describes company without superlatives and ends with URL
- [ ] Media contact includes name, email, and phone
- [ ] End marker (###) present
- [ ] Total word count 400-600
- [ ] No marketing language, exclamation marks, Oxford commas, or first-person outside quotes
- [ ] Numbers under 10 spelled out; 10+ use numerals
- [ ] All dates use AP format (March 15, not March 15th)
