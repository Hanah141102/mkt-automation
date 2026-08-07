# Anti-Patterns — Lỗi Thường Gặp

Tổng hợp 26 lỗi đã gặp + cách tránh. SKILL.md tóm tắt HARD RULES; file này chi tiết WHY + cách fix.

## Scene HTML structure

1. **`<html>/<head>/<body>` wrapper trong scene HTML** — sub-comp loaded via `data-composition-src` phải là `<template>` only. Standalone HTML = broken in runtime.
2. **anime.js** — hyperframes runtime expect GSAP. Bỏ hoàn toàn anime.js.
3. **CSS `animation: ... infinite`** — banned. Convert sang finite GSAP repeat với yoyo, compute từ DURATION.
4. **`Math.random()`** — banned (non-deterministic). Use seeded mulberry32. Mỗi scene 1 seed unique (vd `0x5cNN`).
5. **`gsap.from()` trong sub-comp** — unreliable vì sub-comps load async. Use `gsap.fromTo()` luôn.
6. **Exit animations trong scene** — banned trừ final scene. Master timeline handles transitions.
7. **`<script src=...gsap...>` trong scene HTML** — master index.html load GSAP. Đừng add lại.
8. **Avatar/footer trong scene HTML** — brand stamp chỉ ở master index.html.

## Asset paths

9. **Path `../../../assets/...`** — không work với hyperframes runtime. Copy asset vào `<project>/assets/`.

## Script writing

10. **Em dash trong VO script** — ElevenLabs đọc em dash sai. Dùng comma / period.

## Pattern selection

11. **Forced fit beat content vào pattern không phù hợp** — invent (Approach C) thay vì ép.
12. **Quá 50% scenes có ảnh** — video trông như slideshow. Mix 60/40 motion graphic vs ảnh.

## Design tokens

13. **Không tạo design.md trước** — sub-agents không có source of truth → palette / typography drift.

## Timing

14. **Hardcoded scene durations** — luôn lấy từ `beats.json` (sau alignment).
15. **Không extend scene-mount duration cho crossfade** — scenes back-to-back = jump cut. Extend mỗi scene duration +0.4s để overlap với scene kế tiếp, sau đó tween opacity ở master timeline.

## Rendering

16. **Render qua Playwright per-scene + ffmpeg concat** — KHÔNG. Đó là approach v1 cũ đã bỏ. HyperFrames render trên `index.html` xử lý đầy đủ.

## SFX

17. **Quá nhiều SFX** — cap 1 SFX / 30s. Background music không thuộc skill này.
18. **SFX volume = 1.0** — sẽ át voiceover. Stick 0.4-0.5.

## Title card

19. **Title-card slider có wipe bars / flash** — slider 0-5s đã nhỏ, thêm wipe/flash sẽ che ảnh. Chỉ crossfade sạch + ken-burns scale 1.0→1.05. Đặt wipe/flash CHO SCENE BOUNDARIES không phải slider.

## Brand stamp

20. **Brand stamp avatar 56px** — quá nhỏ, viewer không nhìn ra. Default 112px, handle text 30px mono.

## Transitions

21. **Mọi scene boundary đều flash** — flash là cho "loud" moments (premise hit, big stat, finale). Mặc định 5-6/15 boundaries.
22. **Wipe color không xoay vòng** — 15 wipes cùng coral = monotone. Rotate coral/cyan/cream, alternate LTR/RTL.
23. **`gsap.fromTo()` với scene-mount mà không có `overwrite: 'auto'`** — sẽ conflict với scene's own internal animations. Master timeline tween luôn dùng `overwrite: 'auto'`.

## Layout validation

24. **Slider/showcase không có `data-layout-ignore`** — inspect sẽ flag `clipped_text` vì sum của 4 slide labels > showcase width. Mark showcase + slides với `data-layout-ignore` + `data-layout-allow-overflow`.

## Paused timeline seek + callback skipping

25. **Callbacks `onUpdate`/`onComplete`/`t.call()` không chạy khi seek paused timeline** — GSAP paused timeline SKIPS mọi callback khi playhead bị seek (qua `time()`, `progress()`, hoặc master timeline seeking qua scenes). Điều này ảnh hưởng đến:
    - **Count-up**: proxy object + `onUpdate` → DOM không update khi seek
    - **Typewriter / cmdText**: `t.call()` không chạy → text không hiển thị
    - **Bất kỳ DOM mutation nào** thông qua callback

    **Fix**: dùng `tl.set()` tại explicit timeline positions. `tl.set()` dùng GSAP property rendering engine, chạy được cả khi paused seek (không phụ thuộc vào callbacks).

    ```javascript
    // Scene HTML pattern
    // window.__timelines["scene-NN"] = (() => {
    //   const tl = gsap.timeline({ paused: true });
    
    // Bad — callbacks không chạy khi seek
    const proxy = { val: 0 };
    tl.to(proxy, {
      val: 100, duration: 3,
      onUpdate: () => { document.querySelector("#stat").textContent = Math.round(proxy.val); }
    });
    
    // Good — thêm tl.set() tại các positions cần render đúng
    tl.to(proxy, {
      val: 100, duration: 3,
      onUpdate: () => { document.querySelector("#stat").textContent = Math.round(proxy.val); }
    });
    tl.set("#stat", { textContent: "100" }, 3);      // render khi seek đến cuối
    tl.set("#stat", { textContent: "0" }, 0.01);       // render khi seek về đầu

    // Typewriter cmdText — tương tự
    const cmdTextEl = document.querySelector("#cmdText");
    tl.to(cmdTextEl, { duration: 3, ease: "none", onUpdate: ... });
    tl.set(cmdTextEl, { textContent: "" }, 0);          // empty at t=0
    tl.set(cmdTextEl, { textContent: "Final command" }, 3); // final at t=3
    // ```

    **Rule of thumb**: mỗi proxy-driven animation cần ít nhất 1 `tl.set()` cho giá trị mục tiêu, và 1 `tl.set()` cho giá trị khởi tạo. Kiểm tra mọi seek position (0, middle, end) trong console để verify.

## Master timeline wiring

26. **Root timeline reference scene timelines trong `requestAnimationFrame` hoặc `DOMContentLoaded`** — khi master `index.html` (standalone, không phải `<template>`) chứa root timeline cần `tl.call(() => sceneTimeline.seek(...))` để interlock với scene timelines loaded via `data-composition-src`, scene `<script>` tags chạy SAU root `<script>`. Cả `requestAnimationFrame` (1 tick) và `DOMContentLoaded` đều quá sớm — `window.__timelines["scene-NN"]` chưa tồn tại.

    **Fix**: `setTimeout(() => { ... }, 50)` sau khi root timeline tạo xong. Empirically đủ để tất cả scene scripts register trước khi code chạy.

    ```js
    window.__timelines["root"] = (() => {
      const tl = gsap.timeline({ paused: true });
      // tweens ...

      setTimeout(() => {
        const s1 = window.__timelines["scene-01-hook"];
        if (s1) tl.call(() => s1.seek(0), null, 0);
      }, 50);

      return tl;
    })();
    ```

    Nếu root timeline chỉ tween opacity của mount divs (không reference scene timelines) → KHÔNG cần `setTimeout`. Pattern này chỉ cần khi muốn scene-level sync.
