---
name: employee-handbook
description: "Tạo sổ tay nhân viên hoặc cộng tác viên: chính sách công ty, kỳ vọng, phúc lợi, nguyên tắc giao tiếp và quy trình vận hành trình bày chuyên nghiệp. Dùng khi công ty đã đủ đông để cần quy định chung."
allowed-tools: Read Write Glob
ten-viet: "Sổ Tay Nhân Viên"
nhom: "12. Nhân Sự"
ten-goc: "Employee Handbook"
---

# Sổ Tay Nhân Viên

## When to Use This Skill

Use this skill when:
- A user is hiring their first employee or contractor and needs written policies
- A business owner wants to formalize workplace expectations before scaling
- Someone is onboarding remote contractors and needs communication norms, deliverable standards, and payment terms documented
- An existing handbook needs to be rewritten or modernized

**DO NOT** use this skill for employment contracts or legal agreements, job descriptions, SOPs for specific business processes, or independent contractor classification guidance.

---

## Core Principle

A HANDBOOK IS NOT A LEGAL CONTRACT — IT IS AN OPERATIONAL GUIDE THAT SETS CLEAR EXPECTATIONS SO EVERYONE KNOWS HOW WORK GETS DONE, WHAT IS EXPECTED, AND WHERE TO FIND ANSWERS.

---

## Phase 1: Gather

**Group 1 (ask all at once):**
1. What is your company name?
2. How many people are on your team right now?
3. What is your work arrangement? (Remote, hybrid, or in-office?)
4. What industry are you in?
5. Are you hiring employees, contractors, or both?

**Group 2 (ask after Group 1 is answered):**
6. Do you have any existing policies to incorporate?
7. What state or country are your team members based in?
8. What tools does your team use for communication and project management?
9. What are your standard working hours or availability expectations?

### Handbook Type Selection

| Handbook Type | Best For | Typical Length |
|---------------|----------|---------------|
| **Full Employee Handbook** | W-2 employees, businesses with 3+ staff | 15-25 pages |
| **Contractor Handbook** | 1099 contractors, freelancers, remote teams | 5-10 pages |
| **Team Playbook** | Culture-focused teams, early-stage startups | 5-8 pages |

**Default to Contractor Handbook** unless the user's answers clearly indicate otherwise.

**GATE: Do not proceed to Phase 2 until you have the company name, work arrangement, and employee/contractor distinction confirmed.**

---

## Phase 2: Structure

### Section Menu

| # | Section | Employee | Contractor | Playbook |
|---|---------|----------|------------|----------|
| 1 | Welcome and Company Overview | Yes | Yes | Yes |
| 2 | Mission, Vision, and Values | Yes | Optional | Yes |
| 3 | Employment/Engagement Terms | Yes | Yes | No |
| 4 | Work Schedule and Availability | Yes | Yes | Yes |
| 5 | Communication (tools, response times, meeting norms) | Yes | Yes | Yes |
| 6 | Project Management and Deliverables | Optional | Yes | Yes |
| 7 | Time Off and Leave Policies | Yes | No | No |
| 8 | Compensation and Payment | Yes | Yes | No |
| 9 | Equipment and Tools | Yes | Optional | No |
| 10 | Confidentiality and Intellectual Property | Yes | Yes | Optional |
| 11 | Code of Conduct | Yes | Yes | Yes |
| 12 | Performance and Feedback | Yes | Optional | Yes |
| 13 | Termination and Offboarding | Yes | Yes | No |
| 14 | Acknowledgment Page | Yes | Yes | Optional |

**GATE: Do not proceed to Phase 3 until the user approves which sections to include.**

---

## Phase 3: Write

Write each approved section following these rules:

1. **Plain language only.** No legalese. Write like a manager explaining policies to a new team member.
2. **Specific over vague.** "Respond to Slack messages within 4 business hours" beats "Respond to messages promptly."
3. **Flag legal review areas.** Any section touching compliance, termination, non-competes, or benefits must include: **"Have an employment attorney review this section before distributing."**
4. **Consistent tone.** Professional but human. Firm on expectations, warm on culture.
5. **Use the user's actual tools and details.** If they said Slack and Asana, write those in — not generic placeholders.

### Legal Disclaimer (include on page 1 or 2)

```
> **Disclaimer:** This handbook is an internal guide and does not
> constitute a legal contract, guarantee of employment, or binding
> agreement. Policies may be updated at any time with notice.
> Consult a qualified employment attorney to ensure compliance
> with federal, state, and local laws applicable to your business.
```

**GATE: Present the complete handbook for review before saving. If the user requests more than 3 rounds of revisions, ask whether to finalize what exists and mark remaining items for a future version.**

---

## Phase 4: Deliver

After user approval:

1. Save as `[company-name]-handbook.md`
2. Include a table of contents with anchor links at the top
3. Add the legal disclaimer on the first page
4. Include the acknowledgment page as the final section

**Post-delivery advice:**
- "Have an employment attorney review this handbook before distributing, especially termination, leave, confidentiality, and IP sections."
- "Revisit this handbook every 6-12 months as your team and policies evolve."
- "Keep a signed copy of the acknowledgment page for each team member."

---

## Pre-Delivery Checklist

- [ ] Every section uses the user's actual company name, tools, and details
- [ ] Employee vs. contractor language is consistent (no mixing)
- [ ] Compliance-sensitive sections are flagged for attorney review
- [ ] Legal disclaimer appears on the first or second page
- [ ] Acknowledgment page is included as the final section
- [ ] No legalese, no threatening language
- [ ] Table of contents with anchor links is at the top
- [ ] All policies are specific and actionable (no vague "as appropriate" language)

---

## Anti-Patterns

- **DO NOT provide specific legal advice** — flag compliance-sensitive sections for attorney review
- **DO NOT use threatening language** — firm and clear, not hostile
- **DO NOT write vague policies** — "Dress appropriately" tells no one anything
- **DO NOT skip the confidentiality and IP section** — every handbook gets this
- **DO NOT mix employee and contractor terminology** — legally critical distinction
- **DO NOT copy-paste generic templates** — every handbook must reflect the user's actual company
- **DO NOT include policies the user did not confirm** — ask before adding
- **DO NOT assume US-based employment law applies** — always ask location

---

## Recovery

**User cannot articulate their policies:** Ask scenario-based questions ("What happens if someone needs a day off tomorrow?"). Their answer IS the policy. If after 3 attempts they cannot provide input, mark with **"[NEEDS YOUR INPUT]"** and move on.

**Employee vs. contractor confusion:** Do not classify for them — it is a legal determination. Ask: "Which term do you use when you talk about your team? I will write the handbook to match."

**Handbook scope creep:** After the third unplanned addition, pause and ask whether to finalize what exists and create a v2 later.

**User wants legal guarantees:** "I cannot guarantee legal compliance. Have an employment attorney review before distributing."
