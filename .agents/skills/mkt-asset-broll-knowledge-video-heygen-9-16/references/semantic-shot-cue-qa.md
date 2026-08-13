# Semantic shot, cue và vision QA

Đọc file này trước approval gate, trước khi wire timeline và trước mỗi draft. Mục tiêu là giữ hình sát nghĩa, text xuất hiện đúng lúc và overlay không che chủ thể.

## 1. Quyết định visual bằng danh từ + động từ

Viết claim thành cặp `noun_verb` trước khi tìm media, ví dụ `người ngồi chờ`, `nhiều tác vụ chạy song song`, `dashboard cho thấy tăng trưởng`.

Chỉ dùng Pexels khi cả danh từ và hành động đều nhìn thấy được. Clip laptop, team meeting hoặc code screen chung chung không chứng minh một claim chỉ vì cùng chủ đề AI/công việc.

Router:

```text
asset user chứng minh claim? → user-asset
footage thật khớp noun + verb? → Pexels full-screen riêng
không có hình nhưng cần giải thích cơ chế? → text/chart/flow riêng
không có bằng chứng bắt buộc? → giữ avatar hoặc typography tối giản
```

Không ép quota Pexels. Khi semantic match yếu, ghi override và lý do trong storyboard rồi điều chỉnh validator bounds theo approval.

## 2. Pexels là shot độc lập

- Mount full-canvas ở master, muted, crop 9:16 có chủ đích.
- Ngoài captions, không để text badge, chip, chart, callout, tint note, PIP hoặc ảnh nhỏ trên footage.
- Không chạy text/chart phía dưới Pexels rồi để nó xuất hiện ở trạng thái đã hoàn tất khi footage kết thúc.
- Kết thúc Pexels ở semantic boundary của vế nó minh họa. Bắt đầu visual kế tiếp đúng cùng timestamp; sai lệch tối đa 50ms.
- Nếu câu tiếp theo chuyển từ hành động sang cơ chế, clean-cut sang chart. Không cần freeze + annotation.

Gate Pexels:

1. Tắt captions vẫn nhận ra đúng noun + verb?
2. Footage có đang chứng minh câu nói, không chỉ tạo không khí?
3. Frame có sạch ngoài captions?
4. End của footage có khớp đầu câu/ý tiếp theo?
5. Coverage có gap hoặc overlap dominant quá 50ms?

## 3. Cue ledger cho text/chart

Tạo cue từ `audio/alignment.json`, không nghe ước lượng. Mỗi cue ghi:

```json
{
  "anchor": "lập kế hoạch",
  "absolute_s": 17.717,
  "scene_relative_s": 2.170,
  "target": "#role-plan",
  "event": "reveal"
}
```

Với scene bắt đầu tại `scene_start_s`:

```text
scene_relative_s = absolute_s − scene_start_s
```

Quy tắc author:

- Set mọi node, card, row, connector và verdict về `opacity: 0` trước timeline.
- Có thể reveal container rỗng sớm; nội dung mang nghĩa vẫn phải chờ keyword.
- Reveal từng item tại đúng anchor; connector chỉ hiện sau source node và trước/đúng target node.
- Giữ item đã reveal nếu nó giúp người xem tích lũy mô hình.
- Dùng `fromTo` 0,12–0,28 giây với dịch chuyển 10–22px. Không generic stagger.
- Không cho headline dài và ba card xuất hiện đồng thời.

Ví dụ đúng:

```js
tl.set(['#plan', '#execute', '#check'], { opacity: 0 }, 0);
tl.fromTo('#plan', { opacity: 0, y: 18 },
  { opacity: 1, y: 0, duration: .24, ease: 'power3.out' }, cue.plan);
tl.fromTo('#execute', { opacity: 0, y: 18 },
  { opacity: 1, y: 0, duration: .24, ease: 'power3.out' }, cue.execute);
tl.fromTo('#check', { opacity: 0, y: 18 },
  { opacity: 1, y: 0, duration: .24, ease: 'power3.out' }, cue.check);
```

Áp dụng tương tự cho role flow, ba cột, hàng rủi ro, checklist, causal chain và mọi chart nhiều bước.

## 4. Emphasis trên HeyGen

Chỉ thêm khi keyword cần đóng đinh mà captions chưa đủ. Mặc định dùng text badge hoặc micro-icon CSS/vector; không dùng ảnh PIP chung chung.

Mỗi cue cần:

- `start_s`, `end_s` từ alignment.
- `spoken_cue` và text ngắn.
- `window` HeyGen chứa cue.
- vị trí, kích thước, style và mục đích.
- proof frame thật tại cue time.

Giữ tối đa một cue thấy được tại một thời điểm. Cho cue vào bằng fade + dịch 10–18px trong 120–180ms, hold, rồi `gsap.set(..., {opacity: 0})` tại end; không exit animation kéo dài sang từ sau.

Mount emphasis dưới captions về visual stacking. Ví dụ `z-index: 85`; captions mount cuối và `z-index: 100`.

## 5. Vision safe-zone audit

Không có safe zone cố định cho mọi avatar. Trích frame từ chính clip HeyGen tại đầu, giữa và cuối mỗi window, đặc biệt đúng cue time. Đánh dấu:

- mặt, mắt, tóc và vùng head drift;
- tay và vùng gesture;
- caption band;
- brand mark, vật sáng và vùng tương phản thấp;
- rail trống có thể đặt badge.

Một case 9:16 đã kiểm chứng cho thấy các vùng tham khảo sau, nhưng phải đo lại ở video mới:

| Vùng tham khảo | Quyết định |
|---|---|
| mặt/mắt `x 28–72%, y 24–58%` | cấm overlay |
| rail trái `x 5–30%, y 14–28%` | ưu tiên badge ngắn |
| ngực `y 55–66%` | chỉ token ngắn; kiểm tra tay |
| caption `y ≥ 75%` | cấm overlay |
| góc phải trên | kiểm tra đèn, tóc và thái dương |

Nếu proof frame tĩnh không che mắt nhưng badge sát tóc/thái dương, coi là fail vì head drift có thể gây va chạm khi chạy.

## 6. Approval artifacts

Trước khi wire:

1. `storyboard-preview.html` dùng asset thật, không placeholder khi media đã có.
2. Text/chart board hiển thị source → từng keyword reveal → proof; không chỉ final state.
3. HeyGen emphasis board đặt badge lên frame thật tại từng cue.
4. `VISION-AUDIT.md` ghi vùng cấm, vùng ưu tiên, rủi ro và quyết định sửa.
5. `APPROVAL-STATUS.md` ghi rõ `REVIEW_REQUIRED`, `APPROVED` hoặc `NEEDS_PLACEMENT_REVISION`.

## 7. Draft nhẹ và QA sau wire

Render draft mới, không overwrite variant cũ:

```bash
npx hyperframes render -q draft -o _draft-<variant>.mp4
```

Trích frame ngay trước và ngay sau từng cue, cùng frame giữa mỗi Pexels shot. Tạo contact sheet rồi vision-check:

- item chưa hiện trước keyword;
- item mới xuất hiện đúng anchor;
- không có chữ đè nhau;
- Pexels sạch ngoài captions;
- emphasis không che mặt, mắt, tóc, tay, caption hoặc brand;
- transition không lộ chart đã đầy nội dung;
- không có gap/overlap tại semantic boundary.

`npm run check` PASS không thay thế vision QA. Contrast warning có thể được ghi nhận; lỗi layout, overflow, missing asset, cue timing hoặc overlap phải sửa trước final.

Draft review được thiếu BGM khi chưa có track có quyền dùng, nhưng phải ghi `DRAFT · BGM_NEEDED`. Final vẫn bị chặn cho đến khi BGM rights và audio QA PASS.
