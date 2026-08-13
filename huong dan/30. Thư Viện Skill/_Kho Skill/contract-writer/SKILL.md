---
name: contract-writer
description: "Soạn hợp đồng dịch vụ, hợp đồng freelance và thoả thuận hợp tác với các điều khoản chuẩn kèm chú thích giải thích từng phần bằng ngôn ngữ dễ hiểu. Dùng khi cần văn bản ràng buộc với đối tác hoặc khách."
allowed-tools: Read Write Glob
ten-viet: "Soạn Hợp Đồng"
nhom: "14. Pháp Lý & Tuân Thủ"
ten-goc: "Contract Writer"
---

# Soạn Hợp Đồng

## When to Use This Skill

Use this skill when:
- A user needs a service agreement, freelance contract, retainer agreement, partnership agreement, or NDA
- Someone wants to formalize a client or vendor relationship before starting work
- A freelancer, consultant, or agency owner needs a contract template for a new engagement
- A user asks for a starting point to send to their attorney for review

**DO NOT** use this skill for employment contracts, real estate, securities, regulatory filings, or contracts involving litigation or settlements.

---

## Legal Disclaimer

**THIS SKILL GENERATES CONTRACT TEMPLATES FOR INFORMATIONAL PURPOSES ONLY. IT DOES NOT PROVIDE LEGAL ADVICE. EVERY CONTRACT PRODUCED BY THIS SKILL MUST BE REVIEWED BY A QUALIFIED ATTORNEY BEFORE SIGNING OR ENFORCEMENT.**

This disclaimer MUST appear at the top of every generated contract document.

---

## Core Principle

EVERY CONTRACT MUST PROTECT BOTH PARTIES FAIRLY, USE PLAIN LANGUAGE WHEREVER POSSIBLE, AND BE TREATED AS A STARTING TEMPLATE FOR ATTORNEY REVIEW — NEVER AS A FINAL LEGAL DOCUMENT.

---

## Contract Type Quick Reference

| Type | Best For | Typical Length |
|------|----------|---------------|
| **Freelance Service** | One-time projects (design, dev, copywriting) | 2-4 pages |
| **Retainer** | Ongoing monthly engagements | 2-4 pages |
| **Partnership** | Co-ventures, revenue shares, joint projects | 3-5 pages |
| **NDA** | Pre-engagement confidentiality | 1-2 pages |

Default to **Freelance Service Agreement** if the user does not specify.

---

## Phase 1: Gather Contract Details

**Group 1 — Parties and Purpose:**
1. What type of contract do you need?
2. Who are the two parties?
3. What is the service or relationship being formalized?

**Group 2 — Commercial Terms:**
4. What is the total price or compensation structure?
5. What is the payment schedule?
6. What are the specific deliverables or services?
7. What is the project timeline or contract duration?

**Group 3 — Protections:**
8. Who owns the intellectual property after delivery?
9. Is a confidentiality clause needed? (default yes)
10. What are the termination terms?
11. Preferred governing law state or jurisdiction?

### Defaults for Unanswered Questions

| Question | Default |
|----------|---------|
| IP ownership | Client owns all deliverables upon full payment |
| Confidentiality | Mutual, 2-year duration |
| Termination notice | 30 days written notice by either party |
| Governing law | User's state if known, otherwise `[STATE]` |
| Dispute resolution | Mediation first, then binding arbitration |
| Late payment | 1.5% monthly interest on overdue balances |
| Limitation of liability | Capped at total contract value |

**GATE: Do not proceed to Phase 2 until you have answers to at least questions 1-7.** Apply defaults and flag them with `[DEFAULT — confirm with your attorney]`.

---

## Phase 2: Draft the Contract

Include these 12 sections with plain-language annotations:

**1. Scope of Work** — *"This defines exactly what work is being done. If it is not listed here, it is not included."*

**2. Deliverables** — Table: Deliverable | Description | Due Date

**3. Payment Terms** — *"How much is owed, when payments are due, and what happens if late."*

**4. Timeline and Milestones** — Table: Milestone | Target Date | Notes

**5. Intellectual Property** — *"Who owns the work product after the project is complete."*

**6. Confidentiality** — *"Both parties agree not to share private business information with outsiders."*

**7. Termination** — *"The exit clause — how to end the contract, notice required, what happens to payments."*

**8. Limitation of Liability** — *"Caps the maximum amount either party could owe if something goes wrong."*

**9. Dispute Resolution** — *"How to resolve disagreements without going to court."*

**10. Governing Law** — *"Which state's laws apply to this contract."*

**11. General Provisions** — Entire agreement, amendments, severability, force majeure, notices.

**12. Signatures** — Signature lines, printed names, dates for both parties.

### Drafting Rules

- **Plain language always.** "The client pays $5,000 within 10 days of signing" not legal jargon.
- **Never leave a critical term blank.** Use defaults and flag them.
- **Keep under 5 pages** for freelance/retainer.
- **Adapt sections to the contract type.** An NDA skips Deliverables. A retainer adds Term and Renewal.

**GATE: Present the complete draft to the user before saving to file.**

---

## Phase 3: Review with User

Present the full draft and ask:
1. "Does this accurately reflect the terms you described?"
2. "Are you comfortable with the default terms used? (Flagged with [DEFAULT] markers.)"
3. "Do you want to adjust any financial terms, timelines, or IP ownership?"

**If more than 3 revision rounds:** "Would you like to finalize the current version and let your attorney handle the remaining adjustments?"

**GATE: Do not save to file until the user explicitly approves.**

---

## Phase 4: Deliver to File

Save to: `contracts/[party-b-name]-[contract-type]-agreement.md`

Always end with: "Send this document to a qualified attorney for review before either party signs."

---

## Pre-Delivery Checklist

- [ ] Legal disclaimer appears at the top of the document
- [ ] Both parties named correctly throughout
- [ ] Payment amount, schedule, and late-payment terms explicitly stated
- [ ] Every deliverable has a description and due date
- [ ] IP ownership clause matches user's specification
- [ ] Termination clause includes notice period and payment handling
- [ ] All `[DEFAULT]` flags present where defaults were applied
- [ ] Plain-language annotations included for every section
- [ ] No internal contradictions between sections
- [ ] Signature block includes both parties with date

---

## Anti-Patterns

- **Overly complex legalese** — plain language is not less enforceable.
- **Skipping or vague payment terms** — specify exact amount, exact due date, and late-payment consequences.
- **Promising enforceability** — NEVER say "legally binding" or "compliant." Always recommend attorney review.
- **Inserting unflagged clauses** — flag any clause the user did not request.
- **Omitting the legal disclaimer** — every generated contract must include it.

---

## Recovery

**User cannot provide key details:** Offer common defaults. If 3 attempts fail on basic terms, stop: "Finalize these terms with your client first. Once you know the scope, price, and timeline, we can draft this in minutes."

**Contract type outside scope:** "I can help with service agreements, freelance contracts, retainers, partnerships, and NDAs. That type requires specialized legal expertise."

**File write fails:** Report error and present contract in chat for manual copying.
