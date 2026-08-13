# Scene Patterns — AI-HUB Blueprint Reference

Scene canvas 1080×1920, avatar không hiện và không PIP. Pattern chỉ là **motion route**, không phải layout template. Chọn route theo điều cần chứng minh; nếu phải bẻ nội dung để khớp card/diagram có sẵn thì invent từ metaphor.

## Quy tắc chung

- Đọc `design.md`, `design-system.md` và `assets/templates/scene-reference-full.html` trước khi author.
- Headline Be Vietnam Pro 68–84px, tối đa 2 dòng/4–8 từ, line-height ≥1.08, tracking ≥−0.015em.
- Content kết thúc trước `y=1480`; caption chiếm vùng dưới.
- Không bokeh, cyberpunk, glassmorphism, neon hoặc `data-layout-allow-overlap` trên text.
- Một scene có một visual anchor và một hero animation.
- Một `source_object` phải đổi trạng thái theo ba nhịp: `start → transformation → proof`.
- Camera chỉ di chuyển để tiết lộ quan hệ, nguyên nhân hoặc thay đổi quy mô; cấm pan/zoom chỉ để frame “có động”.
- Focal phải thắng supporting bằng ít nhất hai tín hiệu: scale, contrast, timing hoặc vị trí. Không để ba card ngang hàng.
- Chuyển cảnh phải dùng `carrier + vector` trong seam ledger; shared object phải thật sự tiếp tục qua seam, không crossfade hai object giống nhau.
- Beat có Pexels che giữa scene: đặt context trước footage, insight/payoff sau footage.

## Chọn pattern theo nội dung

| Nội dung beat | Pattern ưu tiên |
|---|---|
| Cùng một vật đổi vai trò/trạng thái | `shared-object-morph` |
| Cần lùi/gần camera để lộ quan hệ | `camera-reveal` |
| Hành động A gây ra kết quả B | `causal-chain` |
| Nhiều mảnh hợp thành một kết luận | `accumulation` |
| Khái niệm trừu tượng cần thành vật chứng | `evidence-physicalization` |
| Điều bị thiếu/xóa chính là thông điệp | `semantic-removal` |
| Trạng thái cũ → trạng thái mới | `before-after-reframe` |
| Chuỗi bước hoặc quy trình | `blueprint-flow` |
| Nhiều agent/module phối hợp | `module-lock-system` |
| Việc chạy song song | `parallel-lanes` |
| Điểm cần người duyệt | `human-approval-gate` |
| Bằng chứng/screenshot | `evidence-stack` |
| Một con số quan trọng | `single-stat` |
| Một câu kết luận | `editorial-statement` |

## 1. shared-object-morph

- Chọn một artifact có nghĩa: brief, tài liệu, bảng điều khiển, gateway, con dấu duyệt hoặc output.
- Giữ cùng DOM object làm focal trong cả scene; thay nội dung, silhouette, scale hoặc quan hệ xung quanh nó.
- Ba trạng thái phải đọc được ở contact sheet: nguồn → đang biến đổi → bằng chứng cuối.
- Morph phải trả lời “nó đã trở thành gì?”; đổi màu/opacity đơn thuần không đủ.

## 2. camera-reveal — zoom-to-meaning

- Bắt đầu ở crop gần để người xem tin mình đang nhìn một vật riêng lẻ.
- Zoom-out hoặc reframe để lộ vật đó thuộc một hệ thống, tạo ra hệ quả hoặc bị chi phối bởi một nguyên nhân khác.
- Camera dừng khi quan hệ mới đã đọc được; không tiếp tục drift sau insight.
- Hợp với reveal “vấn đề không nằm ở output, mà ở nguồn/brief/quy trình”.

## 3. causal-chain

- Mỗi trigger phải có phản ứng nhìn thấy được: click → đường chạy → gate đổi trạng thái → output xuất hiện.
- Node chỉ phản ứng sau khi tín hiệu thật sự chạm tới; không animate đồng loạt.
- Lời nói là đồng hồ: causal trigger land đúng từ khóa trong `vo_cues`.
- Tail tiếp tục resolve bằng trace/output status; không kết thúc timeline giữa beat.

## 4. accumulation — accumulate/recompose

- Các mảnh bằng chứng xuất hiện tuần tự, giữ lịch sử thay vì biến mất sau mỗi câu.
- Ở payoff, cùng các mảnh đó dịch chuyển/scale để tạo thành một hình hoặc hệ thống mới.
- Không thêm object payoff hoàn toàn mới để giả cảm giác “recompose”.
- Dùng khi kết luận mạnh hơn tổng các ý riêng lẻ.

## 5. evidence-physicalization

- Biến khái niệm thành vật có hành vi: “độ trễ” thành khoảng cách kéo dài, “thiên kiến” thành lớp mực phủ, “chi phí” thành khối nặng kéo flow xuống.
- Vật chứng phải tương tác với source object và làm thay đổi kết quả.
- Annotation chỉ gọi tên điều mắt đã thấy; không gánh phần giải thích chính.

## 6. semantic-removal

- Một phần tử có nghĩa bị xóa, che, bỏ trống hoặc không phản hồi để diễn đạt thiếu vắng/silence.
- Sau hành động xóa, dành 0.35–0.7s deliberate stillness để người xem nhận ra khoảng trống.
- Khoảng trống phải nằm tại nơi trước đó có kỳ vọng rõ; trống ngẫu nhiên không tạo nghĩa.

## 7. before-after-reframe

- Context: 3–5 task slips/module rời rạc, không dùng card grid đều nhau.
- Mechanism: các phần tử dịch chuyển theo cùng hướng và khóa thành một brief/system.
- Conclusion: một câu ngắn mô tả thay đổi vai trò hoặc cách vận hành.
- Animation: `power3.out`; module lock được phép `back.out(1.15)` một lần.

## 8. blueprint-flow

- SVG path được vẽ theo thứ tự lời nói.
- Node chỉ hiện khi đường chạm tới node.
- Một copper trace chạy qua sau khi cấu trúc đã rõ.
- Không dùng dash-flow loop vô hạn.

## 9. module-lock-system

- 2–4 module có khác biệt vai trò, một module là focal point.
- Module trượt 18–32px, scale 0.97→1; không bounce.
- Sau khi khóa đủ module, reveal kết luận hoặc trạng thái `SYSTEM READY` bằng tiếng Việt dễ hiểu.

## 10. parallel-lanes

- Hai hoặc ba lane dùng cùng trục thời gian.
- Dùng copper trace để cho thấy việc chạy đồng thời.
- Nếu có quyết định/chi tiền/nhắn khách, lane phải dừng ở approval gate chứ không chạy xuyên qua.

## 11. human-approval-gate

- Gate là cấu trúc kiến trúc, không phải popup đỏ/neon.
- Flow chạm gate rồi dừng; sau đó label “Người duyệt” xuất hiện.
- Màu copper biểu thị quyền quyết định, graphite biểu thị hệ thống.

## 12. evidence-stack

- Ảnh/screenshot là focal point; chỉ thêm 1–2 annotation copper.
- Depth 2.5D rất nhẹ: rotate ≤1.5°, translate ≤24px, scale ≤1.03.
- Không đặt nhiều khung mockup chồng nhau nếu không giúp chứng minh ý nói.

## 13. single-stat

- Một con số lớn, một đơn vị, một câu giải thích.
- Chỉ count-up khi sự thay đổi giá trị có ý nghĩa; nếu không, reveal trực tiếp.
- Không text glow hoặc halo neon.

## 14. editorial-statement

- Một statement 4–10 từ với nhiều whitespace.
- Có thể dùng một đường copper hoặc dấu ngoặc kiến trúc làm anchor.
- Không biến toàn bộ caption thành headline.

## Nhịp animation theo voiceover

Không áp một nhịp cố định cho mọi scene. Lấy mốc từ word-level alignment rồi map thành bốn loại cue:

| Cue | Hành động |
|---|---|
| `setup` | Source object hiện đủ sớm để người xem nhận dạng |
| `trigger` | Click, va chạm, xóa, nối hoặc camera move bắt đầu đúng spoken anchor |
| `transformation` | Vật thể đổi trạng thái; supporting chỉ phản ứng theo sau |
| `proof` | End state land và giữ đủ lâu để đọc; phần còn lại là live-resolution hoặc deliberate stillness |

Không để conclusion mặc định xuất hiện ở `D−1.2s` nếu câu kết được nói sớm hơn. Không để timeline chết sau mốc proof; trạng thái cuối có thể tiếp tục xử lý một cách có nghĩa.

## Seam handoff

- `carrier`: source object, đường copper, mask edge, camera direction hoặc hành động Pexels.
- `exit_vector` phải khớp `entry_vector` nếu muốn tạo cảm giác liên tục.
- Background có thể dẫn transition sớm khoảng 0.1s, foreground theo sau cùng vector.
- Clean cut chỉ dùng cho punchline/contrast có chủ đích và vẫn phải ghi trong seam ledger.

## Text–Speech–Image self-review

Ghi một câu trước khi bàn giao:

```text
Voiceover nói [ý] → scene cho thấy [cơ chế] → text chốt [kết luận].
```

Nếu không cùng một mệnh đề, status là `DONE_WITH_CONCERNS` hoặc `BLOCKED`.
