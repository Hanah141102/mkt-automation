# Listicle / Tips Video Recipe — Proven Composition Sequence

Concrete, proven-working scene sequence for "N tips for X" / "M mistakes to avoid" / "K bước để Y" knowledge shorts (9:16, with HeyGen avatar). Captured from a real end-to-end build (6-scene SME tips video, 1450 frames @ 1080×1920, 0 lint errors, render time 55.6s).

Use this as a starting template when the user says "tạo video 6 tips / 5 mẹo / top 7 ..." and wants HeyGen avatar + slides.

## Beat → Pattern mapping (default 6 scenes, ~60-75s)

| # | Beat | Duration | Pattern | Notes |
|---|------|----------|---------|-------|
| 0 | Hook / cold open | 0-3.0s | (full face, no scene) | Always full avatar for first 3s. No scene. |
| 1 | Hook scene (title slam + stat) | 3.0-8.5s (~5.5s) | `hero` | Brand title + 1 big stat. Mount via `data-start=3.0 data-duration=4.0` (mount ends before brollEnd to let avatar expand for "breath"). |
| 2 | Tip 1+2 (early spotlight) | 8.5-15.5s (~7s) | `listicle-stack` variant A spotlight | 4-6 items, only current at 100% opacity. Items 1 & 2 surface in this window. |
| 3 | Tip 3+4 (middle) | 15.5-23s (~7.5s) | `listicle-stack` variant A | Items 3 & 4. Use different accent rotation than scene 2. |
| 4 | Tip 5+6 (late) | 23-30.5s (~7.5s) | `listicle-stack` variant A or B | Items 5 & 6. Last item can stay full opacity longer (the "memory anchor"). |
| 5 | CTA / recap | 30.5-37s (~6.5s) | `cta-outro` | Recap command (`$ bắt đầu ngay`) + 3 social CTAs. |
| (6) | Final breath | 37-40s (~3s) | (full face) | Avatar full + closing tagline, no scene. Master auto-mounts avatar full after brollEnd. |

**Total ~40s.** Adjust beat durations to match actual voiceover length. If script is longer, add a 7th tip scene rather than stretching durations (entrances get cramped past 9s).

## Scene canvas & content rules (9:16 top half 1080×960)

- Hero text 64-84px, NOT 124px (pane is short)
- Card stack: 6 cards × ~120px each = 720px, fits comfortably with title above
- Meta-badge top:92px left:48px (DO NOT collide with master brand-mark top-left)
- No element below y≈900px (will clip the divider between slide and avatar bottom half)
- All accent colors come from design.md palette — rotate cyan → coral → amber → mint → violet → pink across the 6 cards. **Never repeat the same accent for 2 consecutive items.**
- 9:16 full canvas is 1080×1920: scene mounts in top half (1080×960), avatar takes bottom half (1080×960) when in SPLIT mode. Master transitions to FULL (avatar entire 1080×1920) at brollEnd of each beat.

## Listicle spotlight mechanics (the secret to retention)

The "spotlight" variant is the workhorse for tips. Pattern:

1. All N items are positioned in the stack with `gsap.set()` from the start (initial state).
2. The "active" item (current tip) has opacity 1, others 0.35-0.5.
3. `tl.call(() => setActive(N), null, t)` at scheduled times — toggle which item is the spotlight.
4. Each spotlight toggle also animates: previous fades to 0.4, new scales 0.92→1 + opacity 0.35→1 over 0.4s `power2.out`.
5. Last item (tip N) gets an extra settle: stays full opacity for the remaining 1.5s, no further switches.

`tl.call` is required (NOT `tl.to` on opacity 1, NOT `onUpdate`) — see anti-patterns #38: GSAP `onUpdate`/`onComplete` callbacks don't reliably fire when master seeks the timeline, so DOM-state-changing effects (active-item toggle, count-up, typewriter) MUST use `tl.call` checkpoints at known times.

**Time budget per item (spotlight mode):**
- Item appears: 0.3s (scale + opacity entrance)
- Item holds as "current": 1.0s
- Item transitions to "previous" (fades to 0.4): 0.3s
- Total per item: ~1.6s, with 0.4s lead-in for first item

For 6 items: 6×1.6s = 9.6s. Plus 1.0s scene entrance + 1.0s CTA chip = ~12s scene budget.

## Master wiring (key bits)

Each listicle scene mounts with:
- `data-start = beat.start` (e.g. 8.5)
- `data-duration = beat.brollEnd - beat.start` (mount window — scene ends, avatar expand "breath" begins)
- `data-width="1080" data-height="960"`

Internal scene duration (the GSAP timeline length) = mount window. The last item's settle + CTA chip finish by `D - 0.5` to give the viewer ≥500ms of settled state before transition. See anti-patterns #39.

## Accent rotation (across the 3 listicle scenes)

Recommended palette flow (from design.md):
- Scene 2 (tips 1-2): cyan → coral
- Scene 3 (tips 3-4): amber → mint
- Scene 4 (tips 5-6): violet → pink

If using only 2 listicle scenes: 6 colors still rotate, but 3 per scene.

## When NOT to use this recipe

- N > 7 tips → use `card-grid-3x2` (parallel scan, not progressive)
- 16:9 canvas → see `mkt-hyperframe-knowledge-video-heygen-16-9` skill
- Pure editorial/news beat (single insight, not a list) → `hero` or `card-grid-2x2`
- B2B enterprise audience expecting a "whitepaper" tone → use `card-grid-3x2` instead (less "influencer", more "report")
- Footage talking-head instead of HeyGen avatar → `mkt-hyperframe-talking-head-video`
