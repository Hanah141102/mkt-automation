---
name: youtube-thumbnail
description: "Tạo ba phương án ảnh bìa YouTube tối ưu tỷ lệ nhấp: màu tương phản cao, biểu cảm gương mặt và chữ ngắn gọn trên ảnh. Dùng trước mỗi lần đăng video."
allowed-tools: Read Write Glob mcp__claude_ai_Canva__generate-design mcp__claude_ai_Canva__list-brand-kits mcp__claude_ai_Canva__export-design mcp__claude_ai_Canva__get-export-formats mcp__claude_ai_Canva__get-design-thumbnail mcp__claude_ai_Canva__start-editing-transaction mcp__claude_ai_Canva__perform-editing-operations mcp__claude_ai_Canva__commit-editing-transaction mcp__claude_ai_Canva__cancel-editing-transaction
ten-viet: "Ảnh Bìa YouTube"
nhom: "16. Xưởng Video AI"
cong-doan: "6. Đăng & phân phối"
thu-tu: 3
ten-goc: "YouTube Thumbnail Generator"
---

# Ảnh Bìa YouTube

3 CTR-optimized options per video. 1280x720 JPG export. High-contrast colors, emotional faces, 3 words max. User picks one, refine, deliver.

## When to Use This Skill

Use this skill when you need to:
- Create a click-optimized YouTube thumbnail for an upcoming or published video
- Generate 3 distinct thumbnail concepts to A/B test or pick from
- Apply CTR best practices (contrast, emotion, minimal text) to a thumbnail design
- Refresh an underperforming video's thumbnail with a higher-CTR alternative

**DO NOT** use this skill for YouTube channel art or banners, video editing, or social media graphics for non-YouTube platforms.

---

## Quick Reference: Thumbnail Specifications

| Spec | Value | Why It Matters |
|------|-------|----------------|
| **Dimensions** | 1280 x 720 px | YouTube required minimum; 16:9 aspect ratio |
| **Max file size** | 2 MB | YouTube upload limit |
| **Format** | JPG | Smallest file size at high quality; YouTube standard |
| **Text overlay** | **3 WORDS MAXIMUM** | Must be readable at 168x94 (mobile suggested video) |
| **Font size** | Fills 30-40% of thumbnail width | Legibility at all screen sizes |
| **Safe zone** | Key elements in center 80% | Edges get cropped on some devices |
| **Color contrast** | Minimum 4.5:1 text-to-background | Visibility on white and dark YouTube backgrounds |
| **Faces** | Visible, emotional, eye contact | Faces with strong emotion lift CTR 30-40% on average |

## Quick Reference: CTR Best Practices

| Practice | Impact | Implementation |
|----------|--------|----------------|
| High-contrast colors | CRITICAL | Complementary pairs: yellow/black, red/white, blue/orange |
| Emotional face expression | CRITICAL | Surprise, excitement, shock, curiosity — exaggerated beats subtle |
| 3 words or fewer | CRITICAL | Every extra word reduces readability at small sizes |
| Rule of thirds | HIGH | Face on one third, text on the opposite third |
| No clutter | HIGH | One focal element + one text element maximum |

**THE #1 RULE: IF THE THUMBNAIL IS NOT READABLE AT THE SIZE OF YOUR THUMB, IT WILL NOT GET CLICKED.**

## Quick Reference: Thumbnail Style Types

| Style | Layout | Best For |
|-------|--------|----------|
| **Reaction** | Face on left third, text on right | Commentary, reactions, vlogs |
| **Tutorial** | Step visual on right, text on left | How-to, walkthroughs, guides |
| **Listicle** | Large number left, subject montage right | Top 5, rankings, comparisons |
| **Story** | Dramatic full-bleed image, text overlay | Challenges, experiences, storytime |
| **Before/After** | Split screen, left vs right | Transformations, results, reviews |
| **Bold Text** | Text dominates 60%+ of frame | Hot takes, opinions, announcements |

---

## Core Workflow

GENERATE 3 DISTINCT THUMBNAIL OPTIONS WITH DIFFERENT STYLE APPROACHES — NEVER 3 VARIATIONS OF THE SAME CONCEPT.

### Step 1: Gather Video Details

Collect before generating anything:

1. **Video title** — exact or working title of the video
2. **Topic/subject** — what the video is about in one sentence
3. **Style preference** — preferred style or let the skill pick 3 contrasting styles
4. **Face/person** — include a face? If yes, describe expression and framing
5. **Brand colors** — Canva brand kit or manual hex codes
6. **Competing thumbnails** — thumbnails they want to stand out from (optional)

If the user provides items 1-2, proceed with defaults for the rest.

### Step 2: Load Brand Kit from Canva

1. Call `list-brand-kits` to retrieve available brand kits
2. Note brand colors, fonts, and logo references for generation prompts

**IF NO BRAND KIT EXISTS:** Ask for primary color, secondary color, and preferred font weight. **DEFAULT PALETTE:** Yellow (#FFD700) text on dark navy (#0A0E27) background with white (#FFFFFF) stroke.

### Step 3: Generate 3 Thumbnail Options

Option selection logic (when no user preference):
- Commentary/opinion videos: Reaction + Bold Text + Story
- How-to/educational videos: Tutorial + Listicle + Bold Text
- Challenge/experience videos: Story + Reaction + Before/After
- Review/comparison videos: Listicle + Before/After + Tutorial

For each option:
1. Condense the video title to **3 words or fewer** for overlay text
2. Build generation prompt with: overlay text, brand colors, style layout, 1280x720 landscape, high-contrast treatment, text stroke/outline
3. Call `generate-design` with the prompt
4. Call `get-design-thumbnail` to preview

Present all 3 options with style name, layout description, design ID, and thumbnail preview. **Wait for the user to pick a favorite before proceeding.**

**IF THE USER DISLIKES ALL 3:** Ask what element was closest, generate 2 new options. After 5 total attempts, stop and provide specs for manual Canva creation.

### Step 4: Refine the Selected Thumbnail

Once the user picks a favorite:

1. Ask if refinements are needed
2. If yes: call `start-editing-transaction` > `perform-editing-operations` > `get-design-thumbnail` > if approved: `commit-editing-transaction`; if not: `cancel-editing-transaction` and repeat
3. **REFINEMENT LIMIT:** Maximum 3 rounds. After 3, regenerate from scratch with all feedback in the prompt.

### Step 5: Export at 1280x720 as JPG

1. Call `get-export-formats` to confirm JPG availability
2. Call `export-design` with: design ID, format `jpg`, dimensions 1280x720
3. Verify: file under 2 MB, dimensions exactly 1280x720
4. Present the final export with file name, dimensions, format, size, and export URL

**FILE NAMING:** `youtube-thumbnail-{topic-slug}.jpg`

---

## Pre-Delivery Checklist

| # | Check | Verify |
|---|-------|--------|
| 1 | **Text readable at thumb size** | Legible at 168x94 px |
| 2 | **3 words or fewer** | Count overlay words |
| 3 | **Face visible and emotional** | Expression obvious at small sizes (if face included) |
| 4 | **High contrast** | 4.5:1+ text-to-background ratio |
| 5 | **No clutter** | Max 2 focal elements |
| 6 | **Rule of thirds** | Key elements on thirds grid intersections |
| 7 | **Safe zone** | All key content within center 80% of frame |
| 8 | **1280 x 720 px** | Exact dimensions verified in export |
| 9 | **Under 2 MB** | JPG file size within YouTube limit |
| 10 | **No title duplication** | Thumbnail text complements, not duplicates, video title |

---

## Recovery and Troubleshooting

**Brand Kit Not Found:** Ask for primary color, secondary color, font weight. Apply default palette if no preference.

**All 3 Options Rejected:** Ask which was closest and what feels wrong. Generate 2 new options. After 5 total options, provide text specs for manual Canva creation.

**Editing Transaction Fails:** Call `cancel-editing-transaction` to clean up. Retry with one change at a time. If still failing, regenerate from scratch.

**Export Fails:** Try PNG instead of JPG. If both fail, provide design ID for manual export.

**Text Overlay Exceeds 3 Words:** Extract 1-3 most powerful words. Present condensed options to user before generating.

---

## Anti-Patterns

- **DO NOT** put the full video title on the thumbnail — 3 words maximum
- **DO NOT** use low-contrast combinations (gray/gray, light yellow/white, navy/black)
- **DO NOT** generate 3 variations of the same concept — each must be a different style
- **DO NOT** export before the user picks and approves a favorite
- **DO NOT** crowd with multiple text elements, logos, and imagery
- **DO NOT** export as PNG by default — JPG is the YouTube thumbnail standard
- **DO NOT** duplicate the video title word-for-word on the thumbnail
