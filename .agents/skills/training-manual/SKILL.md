---
name: training-manual
description: "Viết cẩm nang đào tạo: hướng dẫn từng bước, hình minh hoạ, câu hỏi kiểm tra kiến thức và phần tra cứu. Dùng khi cần tài liệu để người mới tự học một công việc."
allowed-tools: Read Write Glob
ten-viet: "Cẩm Nang Đào Tạo"
nhom: "12. Nhân Sự"
ten-goc: "Training Manual"
---

# Cẩm Nang Đào Tạo

## When to Use This Skill

Use this skill when you need to:
- Write a training manual for employees, clients, or program participants
- Create step-by-step instructions for processes and procedures
- Include knowledge checks that verify comprehension
- Build reference sections for ongoing use after training

**DO NOT** use this skill for SOPs, user documentation, or API documentation. This is for training materials designed to teach someone how to do something.

---

## Core Principle

A TRAINING MANUAL IS NOT A REFERENCE BOOK — IT IS A GUIDED LEARNING EXPERIENCE THAT TAKES SOMEONE FROM "I DO NOT KNOW HOW" TO "I CAN DO THIS ON MY OWN" THROUGH STRUCTURED, SEQUENTIAL INSTRUCTION.

---

## Phase 1: Manual Brief

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Subject** | "What skill or process does this manual teach?" | No default — must be provided |
| **Audience** | "Who is the learner — new employee, client, general public?" | New team member |
| **Prior knowledge** | "What should the reader already know before starting?" | No prior knowledge assumed |
| **Format** | "Digital PDF, printed manual, or online wiki?" | Digital PDF |
| **Estimated length** | "How many sections or chapters?" | 5-8 sections |

**GATE: Confirm subject, audience, and scope before outlining the manual.**

---

## Phase 2: Manual Structure

### Outline Template

```
## [Manual Title] — Training Manual

### Front Matter
- Title page
- Table of contents
- How to use this manual
- Prerequisites (if any)

### Section 1: Foundation / Overview
- What is [subject] and why it matters
- Key concepts and terminology

### Section 2: Core Process / Skill — Part 1
- Step-by-step instructions
- Visual aids and screenshots
- Common mistakes to avoid
- Knowledge check

### Section 3: Core Process / Skill — Part 2
- Step-by-step instructions
- Tips and best practices
- Troubleshooting guide
- Knowledge check

### Section 4: Advanced Topics
- Building on the basics
- Edge cases and exceptions
- When to escalate or ask for help

### Section 5: Practice Exercises
- Hands-on scenarios with guided steps
- Independent practice with answer keys

### Reference Section
- Quick reference card (1-page summary)
- Glossary of terms
- FAQ
- Resource links and contacts
```

---

## Phase 3: Writing Guidelines

### Step-by-Step Instruction Format

```
## [Task Name]

**Purpose:** [Why this task matters — 1 sentence]
**Time required:** [Estimate]
**Tools needed:** [List]

### Steps:

1. **[Action verb] + [specific action]**
   - [Additional detail]
   - [Visual placeholder: describe what the reader should see]

2. **[Action verb] + [specific action]**
   - [Additional detail]
   - ⚠️ **Note:** [Important warning or tip placed BEFORE the step that could cause issues]

3. **[Action verb] + [specific action]**
   - ✓ **Result:** [What the reader should see when done correctly]
```

### Writing Rules

1. **One action per step** — do not combine two actions into one step
2. **Use imperative voice** — "Click the button" not "The button should be clicked"
3. **Include visual checkpoints** — tell the reader what they should see after each major step
4. **Warn before errors** — place caution notes BEFORE the step that could cause issues
5. **Define terms on first use** — bold and briefly explain any jargon
6. **Keep paragraphs to 2-3 sentences**
7. **Number all steps**

### Knowledge Check Format

After each section, include 3-5 questions:

```
## Knowledge Check — Section [X]

1. [Question — multiple choice, true/false, or short answer]
   a) [Option A]
   b) [Option B]
   **Answer: [Correct answer with brief explanation]**

2. [Scenario-based question]
   "You encounter [situation]. What should you do?"
   **Answer: [Correct action and why]**
```

---

## Phase 4: Supplementary Materials

### Quick Reference Card

```
## [Subject] — Quick Reference

### Key Steps
1. [Step 1 — condensed]
2. [Step 2 — condensed]

### Troubleshooting
- [Problem]: [Quick fix]
- [Problem]: [Quick fix]

### Need Help?
Contact: [Name/Team] at [email/phone]
```

### Manual Quality Checklist

- [ ] Table of contents matches actual section headers
- [ ] Every section has a clear learning objective
- [ ] Step-by-step instructions use numbered lists with one action per step
- [ ] Visual aids or screenshot placeholders are included for complex steps
- [ ] Knowledge checks appear after each major section
- [ ] Answers are provided for all knowledge check questions
- [ ] Quick reference card summarizes the key process on one page
- [ ] Glossary defines all technical terms
- [ ] Manual has been tested by someone unfamiliar with the process
- [ ] Version number and last-updated date are included

---

## Anti-Patterns

- **Assuming knowledge** — explain everything from the beginning.
- **Walls of text** — use lists, tables, headers, and white space.
- **No practice opportunities** — reading without doing results in poor retention.
- **Outdated screenshots** — visuals that do not match what the reader sees erode trust.
- **No troubleshooting section** — anticipate common problems and provide solutions.
- **Writing for experts** — use plain language, not industry shorthand.

---

## Recovery

- **Manual is too long:** Split into a quick-start guide and a comprehensive manual.
- **Learners still confused after reading:** Add more examples, simplify language, and test with a fresh reader.
- **Process changes frequently:** Version the manual and maintain a changelog with a designated owner.
- **No visuals available:** Use descriptive text placeholders and add screenshots later.
- **Multiple audiences:** Create role-specific sections or separate manuals rather than one document for everyone.
