---
tags: [template, brand-system, design-handoff]
created: 2026-08-07
cap-nhat: 2026-08-07
trang-thai: dang-su-dung
phien-ban: 1.0
---

# README — Brand Template Kit — Tony Hoang

> [!success] Đã duyệt v1.0 — 2026-08-07
> Đây là bộ template chính thức theo hướng “Bản Vẽ Tái Cấu Trúc”. Mỗi nội dung cụ thể vẫn cần được duyệt trước khi phát hành.

## Xem nhanh

Mở `index.html` để xem contact sheet của toàn bộ template.

## Cấu trúc

```text
Brand System — Tony Hoang/
├── index.html
├── assets/
│   ├── brand-tokens.css
│   ├── logo-mark-dark.svg
│   ├── logo-mark-dark.png
│   ├── logo-mark-light.svg
│   ├── logo-mark-light.png
│   ├── logo-mark-mono.svg
│   └── logo-mark-mono.png
├── templates/
│   ├── short-video-9x16.html
│   ├── youtube-thumbnail-16x9.html
│   ├── social-carousel-4x5.html
│   ├── framework-slide-16x9.html
│   └── quote-cover-1x1.html
└── previews/
```

## Cách sử dụng

1. Nhân bản đúng file theo định dạng cần dùng.
2. Thay headline, nhãn và sơ đồ; không thay token màu trực tiếp trong từng file.
3. Nếu cần đổi màu hệ thống, sửa `assets/brand-tokens.css`.
4. Giữ tối đa một điểm Ember trong một vùng nhìn.
5. Sau khi thay nội dung, kiểm tra chữ không tràn và CTA chỉ có một hành động.

## Quy tắc nội dung

- Headline 3–12 từ, kết luận lên trước.
- Một thiết kế chỉ nói với một nhóm chính.
- Dùng từ của Brand Voice: điểm nghẽn, quy trình thật, người phụ trách, đầu ra, dùng được thật.
- Không dùng tuyên bố thiếu bằng chứng, lời hứa 100% hoặc “AI thay thế con người”.

## Thay ảnh chân dung

Hai template có ảnh đang đọc từ:

`workspace/assets/brand/tony-avatar.jpg`

Đổi đường dẫn `src` nếu di chuyển bộ template ra khỏi repository. Không phủ màu lên toàn bộ khuôn mặt; giữ da tự nhiên và vùng mắt rõ.

## Xuất ảnh

Kích thước gốc:

| Template | Kích thước |
|---|---:|
| Short video | 1080 × 1920 |
| YouTube thumbnail | 1280 × 720 |
| Carousel | 1080 × 1350 |
| Framework slide | 1920 × 1080 |
| Quote cover | 1080 × 1080 |

Có thể mở từng HTML bằng trình duyệt rồi chụp đúng viewport hoặc chuyển cấu trúc sang Figma/Canva.

## Checklist bàn giao

- [ ] Đúng font Archivo / Inter / JetBrains Mono.
- [ ] Chỉ dùng màu trong `brand-tokens.css`.
- [ ] Body text đạt tương phản và đọc được trên điện thoại.
- [ ] Sơ đồ có điểm bắt đầu, owner hoặc output rõ.
- [ ] Ember có ý nghĩa, không chỉ để trang trí.
- [ ] Không dùng robot, não AI, mạch điện hoặc glow neon chung chung.
- [ ] Tony duyệt bản cuối trước khi đăng.

## Liên kết

- [[Brand System — Tony Hoang]]
- [[Brand Voice — Giọng Thương Hiệu]]
- [[Brand Kit — Trần Văn Hoàng · FreedomBuilders]]
