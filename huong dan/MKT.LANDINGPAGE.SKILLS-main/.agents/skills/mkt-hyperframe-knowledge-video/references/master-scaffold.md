# Master `index.html` Scaffold

Master `index.html` orchestrate toàn bộ composition. Scenes chỉ là `<template>` sub-comp loaded via `data-composition-src`.

## Layer stack (z-index + track-index)

| Element | track-index | z-index | Purpose |
|---|---|---|---|
| `<audio id="vo">` voiceover | 0 | — | ElevenLabs narration, volume 1.0 |
| Title card | 5 | 5 | 5-6s mở đầu (xem `title-card-slider.md`) |
| Scene mounts (#m1..#mN) | 10..10+N | — | Sub-comp loaded via `data-composition-src` |
| Scene wipe overlay | 55 | 50 | Color bar sweep ở scene boundary |
| Scene flash overlay | 56 | 51 | Brief brightness flash ở major boundary |
| Brand stamp | 60 | 100 | Avatar 112px + handle `@tranvanhoang.com` cố định |
| SFX layer | 70..70+M | — | Sound effects (xem `sfx-layer.md`) |

## Scene-mount overlap rule

Mỗi scene `data-duration` = beat duration + 0.4s. Scene kế tiếp `data-start` = beat end nguyên gốc. Overlap 0.4s cho phép transition smooth. Track-index khác nhau cho mỗi scene để có thể overlap.

## Brand stamp (lớn, dễ thấy)

Avatar **112px** không phải 56px. 56px quá nhỏ, viewer không nhìn ra.

```html
<div id="brand-stamp" class="clip brand-stamp"
     data-start="0" data-duration="<total>" data-track-index="60">
  <span class="handle"><span class="at">@</span>tranvanhoang.com</span>
  <div class="avatar">
    <img src="assets/brand/tony-avatar-circle.png" alt="Tony" />
  </div>
</div>
```

```css
#root .brand-stamp {
  position: absolute; bottom: 48px; right: 48px; z-index: 100;
  display: flex; align-items: center; gap: 22px;
  padding: 14px 24px 14px 36px;
  background: rgba(8,12,22,0.62);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 999px;
  backdrop-filter: blur(8px);
}
#root .brand-stamp .handle { font: 600 30px/1 'JetBrains Mono', monospace; color: #faf9f5; letter-spacing: 0.06em; }
#root .brand-stamp .handle .at { color: #d97757; }
#root .brand-stamp .avatar {
  width: 112px; height: 112px; border-radius: 50%;
  overflow: hidden;
  box-shadow: 0 0 0 3px rgba(217,119,87,0.7), 0 0 40px rgba(217,119,87,0.4);
}
```

## Brand asset copy

Path `../../../` KHÔNG work với hyperframes runtime — copy avatar PNG vào `<project>/assets/brand/`:

```bash
mkdir -p $OUT/assets/brand
cp workspace/assets/brand/tony-avatar-circle.png $OUT/assets/brand/
```

Gộp với SFX copy thành 1 parallel bootstrap step.

## Root timeline wiring (master → scene timelines)

Master `index.html` (standalone) KHÔNG phải `<template>`, nó chứa `data-composition-id="root"` div với scenes mounted via `data-composition-src`. Khi muốn root timeline **điều khiển scene timelines** (ví dụ `tl.call(() => sceneTimeline.seek(t))` để đồng bộ transition với scene timeline), cần chú ý:

- Scene `<script>` tags chạy SAU root `<script>` (vì scenes load async qua `data-composition-src`)
- `requestAnimationFrame` (1 tick) → quá sớm, `window.__timelines["scene-NN"]` chưa tồn tại
- `document.addEventListener("DOMContentLoaded")` → cũng quá sớm (scene templates chưa parse xong)
- **Fix**: `setTimeout(() => { ... }, 50)` — empirically đủ để tất cả scene scripts đã register

```js
window.__timelines["root"] = (() => {
  const tl = gsap.timeline({ paused: true });
  // ... tween các mount div opacity cho transitions, brand stamp, v.v.
  tl.to("#m1", { opacity: 0, duration: 0.4 }, 5.8);
  tl.from("#m2", { opacity: 0, duration: 0.4 }, 5.8);
  // ... brand stamp, SFX, v.v.

  // Wire scene timelines SAU khi scripts đã register
  setTimeout(() => {
    const s1 = window.__timelines["scene-01-hook"];
    if (s1) tl.call(() => s1.seek(0), null, 0);
  }, 50);

  return tl;
})();
```

Nếu root timeline chỉ tween opacity của mount divs (không cần reference scene timelines) → KHÔNG cần `setTimeout`, pattern này là optional.
