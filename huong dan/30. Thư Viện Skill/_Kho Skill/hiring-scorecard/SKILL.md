---
name: hiring-scorecard
description: "Tạo phiếu chấm phỏng vấn có cấu trúc: đánh giá theo năng lực, ngân hàng câu hỏi và thang chấm. Dùng khi muốn tuyển dụng khách quan thay vì cảm tính."
allowed-tools: Read Write Glob
ten-viet: "Phiếu Chấm Ứng Viên"
nhom: "12. Nhân Sự"
ten-goc: "Hiring Scorecard"
---

# Phiếu Chấm Ứng Viên

## When to Use This Skill

Use this skill when you need to:
- Create a structured scorecard for evaluating job candidates consistently
- Define competency ratings and evaluation criteria for a specific role
- Build question banks aligned to role requirements
- Remove bias from hiring decisions with objective scoring

**DO NOT** use this skill for writing job descriptions, sourcing candidates, or building interview question banks. This is for the evaluation scorecard used during and after interviews.

---

## Core Principle

HIRING WITHOUT A SCORECARD IS HIRING ON VIBES — A STRUCTURED SCORECARD FORCES OBJECTIVE EVALUATION AGAINST ROLE-SPECIFIC CRITERIA, REDUCING BIAS AND BAD HIRES.

---

## Phase 1: Role Requirements

### Required Inputs

| Input | What to Ask | Default |
|-------|------------|---------|
| **Role title** | "What role are you hiring for?" | No default |
| **Employment type** | "Full-time, part-time, or contractor?" | Contractor |
| **Top 3 outcomes** | "What does this person need to achieve in the first 90 days?" | No default |
| **Must-have skills** | "What skills are non-negotiable?" | No default |
| **Nice-to-have skills** | "What skills would be a bonus but not required?" | No default |
| **Culture traits** | "What working style or personality traits matter for this role?" | Self-starter, communicative |

### Competency Framework

```
## Role Competencies: [Role Title]

### Must-Have (Weighted 70%)
| Competency | Description | How to Assess |
|-----------|-------------|---------------|
| [Skill 1] | [What good looks like] | [Interview question / portfolio / test] |
| [Skill 2] | [What good looks like] | [Assessment method] |

### Nice-to-Have (Weighted 20%)
| Competency | Description | How to Assess |
|-----------|-------------|---------------|
| [Skill 3] | [What good looks like] | [Assessment method] |

### Culture Fit (Weighted 10%)
| Trait | Description | How to Assess |
|-------|-------------|---------------|
| [Trait 1] | [Observable behavior] | [Behavioral question] |
```

**GATE: Confirm competencies before building the scorecard.**

---

## Phase 2: Build Scorecard

### Scorecard Template

```
## Hiring Scorecard: [Role Title]

**Candidate:** _______________
**Interviewer:** _______________
**Date:** _______________
**Interview stage:** [Screen / Technical / Final]

### Competency Ratings

| # | Competency | Weight | Score (1-5) | Weighted Score | Notes / Evidence |
|---|-----------|--------|-------------|---------------|-----------------|
| 1 | [Must-have 1] | [%] | [ ] | [ ] | |
| 2 | [Must-have 2] | [%] | [ ] | [ ] | |
| 3 | [Nice-to-have] | [%] | [ ] | [ ] | |
| 4 | [Culture trait] | [%] | [ ] | [ ] | |

### Scoring Guide

| Score | Definition |
|-------|-----------|
| 1 | No evidence of competency — significant concern |
| 2 | Below expectations — gaps in critical areas |
| 3 | Meets expectations — adequate for the role |
| 4 | Above expectations — strong evidence of competency |
| 5 | Exceptional — among the best candidates seen |

### Overall Assessment

**Total weighted score:** _____ / 5.0

**Recommendation:** [ ] Strong Hire  [ ] Hire  [ ] No Hire  [ ] Strong No Hire

**Top strengths:** 1. / 2.
**Top concerns:** 1. / 2.
```

### Red Flag Checklist

```
## Automatic Disqualifiers

- [ ] Cannot verify claimed experience or credentials
- [ ] Disrespectful to interviewer or staff
- [ ] Scores 1 on any must-have competency
- [ ] [Role-specific red flag]
```

**GATE: Present scorecard for review before adding interview questions.**

---

## Phase 3: Align Questions

### Question-Competency Map

```
| Competency | Question | What to Listen For | Red Flag |
|-----------|---------|-------------------|----------|
| [Skill 1] | "Tell me about a time you [relevant scenario]" | [Specific evidence] | [Vague or evasive answer] |
| [Skill 2] | "How would you approach [role-specific challenge]?" | [Structured thinking] | [No framework, just buzzwords] |
| [Culture] | "Describe your ideal working relationship with a manager" | [Alignment with your style] | [Misalignment on communication] |
```

### Scoring During Interview

- Write notes as the candidate speaks, not after
- Score each competency immediately after the relevant question
- Record specific examples and quotes, not general impressions
- Do not discuss scores with other interviewers until all scorecards are complete

---

## Phase 4: Decision Framework

### Decision Matrix

| Weighted Score | Recommendation | Action |
|---------------|---------------|--------|
| 4.5-5.0 | Strong Hire | Make an offer quickly |
| 3.5-4.4 | Hire | Solid candidate — proceed with offer |
| 2.5-3.4 | Maybe | Additional assessment needed |
| Below 2.5 | No Hire | Pass — do not lower the bar |

### Multi-Interviewer Calibration

1. Each interviewer completes their scorecard independently
2. Compare scores — discuss any competency where scores differ by 2+ points
3. Average the final scores
4. The hiring manager makes the final call

### Post-Hire Validation

At 90 days, compare the scorecard predictions to actual performance. Use this data to calibrate future scorecards.

---

## Anti-Patterns

- **No evidence, just feelings** — "I liked them" is not a hiring decision. Every score needs a specific example.
- **Halo effect** — one strong answer biases all other scores upward. Score each competency independently.
- **Lowering the bar** — if no candidate scores above 3.0, the role is unclear or the pipeline needs improvement.
- **Ignoring red flags** — a 4.5 score with one automatic disqualifier is still a no hire.
- **Skipping the scorecard for "obvious" hires** — even obvious candidates should be scored. It validates the decision.

---

## Recovery

- **User has never used a scorecard:** Start simple — 3 must-have competencies scored 1-5. Add complexity after the first hire.
- **All candidates score similarly:** The questions may not be differentiating enough. Add a practical test or more specific behavioral questions.
- **Interviewer bias suspected:** Require written evidence for every score.
- **Candidate scored well but is underperforming:** Review which competencies were misjudged and refine the assessment methods.
