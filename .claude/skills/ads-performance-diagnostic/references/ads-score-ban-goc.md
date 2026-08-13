---
name: ads-score
description: "Chấm điểm một mẫu quảng cáo theo 6 chiều (1–10) trước khi launch và viết lại phần yếu. Dùng khi người dùng dán một ad (của mình hoặc đối thủ) và muốn chấm điểm ad, ad này ổn chưa, hook mạnh không, đánh giá quảng cáo, score creative, hoặc gõ /ads-score. Chấm hook, copy, CTA, cộng hưởng cảm xúc, cấu trúc offer, ăn khớp hình-copy; chỉ rõ chỗ yếu và vì sao; kèm bản viết lại cho mọi chiều dưới 7."
allowed-tools: Read Write Glob
metadata:
  author: hpteam
  version: "1.0"
---

# Ads Score

## When to Use This Skill

Use this skill when you need to:
- Chấm điểm một creative TRƯỚC khi launch — của mình hay bản nhái từ đối thủ
- Chọn giữa vài biến thể bằng một thang điểm khách quan
- Lọc top mẫu sau `/bulk-creative`
- Gõ `/ads-score` kèm nội dung ad

**DO NOT** use this skill để sản xuất nhiều mẫu (dùng `/bulk-creative`), để audit tài khoản (dùng `/ads-meta-healthcheck`), hay để phân tích nhiều đối thủ (dùng `/competitive-ads-extractor`).

---

## Core Principle

SỬA MỘT HOOK TRÊN GIẤY TỐN 2 PHÚT — PHÁT HIỆN HOOK DỞ SAU KHI CHẠY TỐN CẢ NGÂN SÁCH TEST.

---

## Scoring Quick Reference

| Chiều | Hỏi gì |
|-------|--------|
| Hook strength | Câu đầu có dừng-lướt? Cụ thể, gây tò mò/liên quan? |
| Copy effectiveness | Mạch lạc, thuyết phục, có framework? Lợi ích rõ, xử lý phản đối? |
| CTA clarity | Rõ một hành động? Đúng nhiệt độ khách? Không mơ hồ? |
| Emotional resonance | Chạm pain/mong muốn thật, hay chỉ liệt kê tính năng? |
| Offer structure | Hấp dẫn, dễ hiểu, giảm rủi ro? Có lý do mua ngay? |
| Visual–copy align | Hình và chữ kể cùng câu chuyện? Hook được hình bổ trợ? |

```
9–10 Xuất sắc, launch được | 7–8 Tốt, tinh chỉnh nhẹ | 5–6 Yếu, viết lại | 1–4 Hỏng, làm lại
```

---

## Phase 1: Intake

1. **Nội dung ad** — hook + body + CTA (bắt buộc).
2. **Hình/mô tả visual** — để chấm chiều "ăn khớp hình–copy"; không có thì ghi chiều đó "N/A vì thiếu hình" và chấm 5 chiều còn lại.
3. **Bối cảnh** — sản phẩm, khách hàng mục tiêu, offer (tùy chọn, giúp nhận xét sát hơn).

**GATE: Không sang Phase 2 khi thiếu hook/body/CTA cơ bản.**

---

## Phase 2: Score

Chấm từng chiều 1–10 theo bảng Quick Reference. **Mỗi điểm phải kèm lý do dẫn thẳng từ nội dung ad**, không cho điểm trơ. Cộng tổng /60 và tính trung bình /10.

**GATE: Không có điểm nào được để trống lý do; không nương tay cho điểm cao vô căn cứ.**

---

## Phase 3: Gate Check

Áp quy tắc cổng vì đây là các điểm quyết định phần lớn hiệu quả:
- **Hook strength < 7 → cảnh báo rõ: viết lại hook trước khi tiêu một đồng.** Hook chi phối quyết định dừng-lướt; hook dở kéo mọi chỉ số xuống.
- **Trung bình tổng < 7 → khuyên chưa launch**, ưu tiên sửa các chiều dưới 7.

**GATE: Nếu hook < 7, không kết luận "sẵn sàng launch" dù các chiều khác cao.**

---

## Phase 4: Deliver

```
# ĐIỂM QUẢNG CÁO
Tổng: NN/60  (trung bình N.N/10)

| Chiều                | Điểm | Nhận xét (1 câu) |
| Hook strength        | x/10 | ... |
| Copy effectiveness   | x/10 | ... |
| CTA clarity          | x/10 | ... |
| Emotional resonance  | x/10 | ... |
| Offer structure      | x/10 | ... |
| Visual–copy align    | x/10 | ... |

## Điểm yếu nhất
- <chiều thấp nhất>: vì sao yếu + cách sửa.

## Bản viết lại (cho mọi chiều < 7)
- Hook mới (2–3 phương án nếu hook < 7)
- CTA mới nếu cần
- Đoạn copy chỉnh nếu cần
```

---

## Anti-Patterns

- **Cho điểm cao không giải thích** — vô ích cho việc cải thiện.
- **Viết lại làm lệch brand voice** hoặc vi phạm chính sách Meta (claim tuyệt đối, before/after cá nhân hóa quá đà).
- **Chấm chiều visual khi không có hình** mà không ghi N/A.
- **Điểm ảo, nương tay** — làm hại người dùng khi họ đổ tiền.

---

## Recovery

- **Ad chỉ có hình, ít text:** chấm dựa trên visual + mô tả, nêu rõ giới hạn.
- **Thiếu bối cảnh sản phẩm:** chấm theo chuẩn chung, ghi chú điểm có thể đổi khi biết audience.
- **Người dùng không đồng ý điểm:** giải thích tiêu chí, mời họ đưa dữ liệu test thực tế để hiệu chỉnh.
