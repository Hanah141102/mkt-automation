# AI-HUB Blueprint Motion System — 9:16

Nguồn nhận diện: `<brand_context_root>/brand-design-system.md`.

## Ý niệm trung tâm

Mỗi video trông như **một bản vẽ doanh nghiệp đang được tái cấu trúc**. HeyGen tạo tin cậy, Pexels cho thấy hành động thật, HyperFrames giải thích cơ chế phía sau. Motion không phải trang trí; mọi chuyển động phải làm rõ trạng thái, quan hệ, luồng hoặc quyết định.

## Palette khóa cứng

```css
--ivory: #F7F3EE;
--sand: #E9DED2;
--graphite: #1F2430;
--graphite-2: #2A303D;
--copper: #C96A2B;
--orange: #E07A3B;
--bronze: #A85B2A;
--glow: #F2B277;
--success: #56735F;
--danger: #A84F45;
```

- 70–80% frame là ivory/graphite.
- Copper là màu điều hướng và quyết định, không phủ cả frame.
- Tối đa 2 accent semantic trong một scene.
- Cấm cyan/pink neon, starfield, rainbow gradient và cyberpunk blue.

## Typography tiếng Việt

- Primary: `Be Vietnam Pro`, fallback `Inter`, sans-serif.
- Mono label: `JetBrains Mono`, chỉ dùng cho số bước/mã trạng thái rất ngắn.
- Orbitron chỉ dành cho logo hoặc micro-label đã kiểm tra dấu; không dùng cho câu tiếng Việt.

| Vai trò | Cỡ | Weight | Line-height | Tracking |
|---|---:|---:|---:|---:|
| Headline | 68–84px | 800 | 1.08–1.15 | −0.015em → 0 |
| Section title | 42–54px | 700 | 1.16 | 0 |
| Body | 28–36px | 500–650 | 1.35 | 0 |
| Micro-label | 15–20px | 600 | 1.2 | 0.08em max |
| Caption | 44–50px | 700 | 1.28–1.35 | 0 |

Headline tối đa 2 dòng, 4–8 từ. Không dùng ALL CAPS cho câu dài. Cấm `data-layout-allow-overlap` trên text. Content phải kết thúc trước `y=1480`; caption chiếm vùng dưới.

## Visual primitives

1. **Blueprint Draw** — SVG stroke được vẽ dần để giới thiệu cấu trúc.
2. **Module Lock** — module trượt ngắn 18–32px, scale 0.97→1 rồi khóa bằng click/pulse nhẹ.
3. **Flow Trace** — một vệt copper chạy qua node theo đúng thứ tự lời nói.
4. **Human Approval Gate** — luồng dừng ở cổng, label người duyệt hiện sau khi luồng chạm cổng.
5. **Before/After Reframe** — phần tử rời rạc được sắp lại thành một hệ thống rõ ràng.
6. **Freeze + Annotation** — dừng Pexels và thêm một annotation copper có mục đích.
7. **Evidence Stack** — screenshot/tài liệu xếp lớp với depth 2.5D rất nhẹ.
8. **Match Motion** — nối hai medium bằng cùng hướng chuyển động, hình dạng hoặc hành động.
9. **Kinetic Keyword** — chỉ reveal 1–3 từ khóa, không lặp nguyên caption.
10. **Persistent Artifact Morph** — một artifact sống xuyên scene và đổi vai trò từ nguồn → cơ chế → bằng chứng.
11. **Zoom-to-Meaning** — camera đổi tỷ lệ để lộ quan hệ nhân quả hoặc bối cảnh ẩn, không dùng để “tăng năng lượng”.
12. **Accumulate + Recompose** — dữ kiện tích lũy rồi chính các mảnh đó tái cấu trúc thành kết luận.
13. **Semantic Removal** — xóa/che một thành phần có kỳ vọng rõ để khoảng trống trở thành thông điệp.
14. **Carrier Handoff** — artifact, đường trace, mask edge hoặc hành động thật tiếp tục qua seam với cùng vector.
15. **Environmental Response** — grid/đường blueprint phản ứng rất nhẹ khi có trigger nhân quả; không tự drift liên tục.

## Visual hierarchy và density

- Mỗi frame có **một focal ở display scale**, tối đa hai supporting có vai trò khác nhau.
- Ưu tiên bố cục bất đối xứng khoảng 60/40; crop và negative space phải dẫn mắt hoặc tạo kỳ vọng.
- Focal phải lớn hơn supporting rõ rệt, không chỉ khác 4–8px.
- Supporting không được xuất hiện đồng thời nếu logic là tuần tự; để chuyển động tạo hierarchy theo thời gian.
- Contact sheet phải cho thấy 3–5 trạng thái của cùng visual argument, không phải 3–5 layout độc lập.
- Tắt headline/caption, người xem vẫn phải nhận ra danh từ chính và động từ chính.

## Motion grammar

- Một beat = một source object + một hero transformation.
- Dựng theo grammar: `claim → cause → transformation → proof`.
- Source object phải giữ danh tính qua các trạng thái; đổi opacity giữa hai object giống nhau không phải morph.
- Motion bắt đầu từ nguyên nhân nhìn thấy được và supporting phản ứng sau focal.
- Camera chỉ dùng để tiết lộ quan hệ, nguyên nhân hoặc quy mô.
- Chỉ dùng hai họ transition trong một video: `clean/masked reveal` và `match-motion`.
- `power3.out`: module/headline reveal.
- `sine.inOut`: flow trace, glow chậm, avatar push.
- `expo.out`: chỉ cho insight lớn, tối đa 1–2 lần/video.
- `back.out(1.15)`: chỉ cho module-lock nhỏ; cấm bounce/elastic.
- Không auto flash; tối đa một flash ở loud moment.
- Không auto punch-zoom xen kẽ scene.
- Cuối beat phải là `live-resolution` hoặc `deliberate-stillness`; cấm giữ frame chết vì timeline kết thúc sớm.

## Background

Nền mặc định sạch, ấm và có cấu trúc:

```css
background:
  linear-gradient(rgba(31,36,48,.035) 1px, transparent 1px),
  linear-gradient(90deg, rgba(31,36,48,.035) 1px, transparent 1px),
  radial-gradient(circle at 78% 16%, rgba(242,178,119,.20), transparent 34%),
  #F7F3EE;
background-size: 72px 72px, 72px 72px, auto, auto;
```

Scene graphite được phép dùng khi cần tương phản, nhưng vẫn giữ copper/ivory. Không bokeh, dust, stars hoặc noise động. Nền chỉ chuyển động nếu đang mang carrier qua seam hoặc phản ứng với causal trigger; không “thở” mặc định chỉ để lấp khoảng trống.

## Pexels treatment

- Footage phải thể hiện đúng hành động đang nói.
- Dùng object-fit cover, ưu tiên portrait và chủ thể ở center safe zone.
- Chỉ dùng Ken Burns 1.00→1.025; không 1.06 mặc định.
- Overlay graphite đáy chỉ đủ để caption đọc được.
- Editorial annotation tối đa 1 cụm/clip; không phủ infographic lên toàn bộ footage.

## Brand marks

- Micro brand mark: `BRAND · KNOWLEDGE SYSTEM`, graphite/copper, top-left.
- Logo/gateway chỉ xuất hiện ở intro/outro hoặc khi metaphor thật sự cần.
- Không watermark avatar, không PIP và không wordmark neon.

## Text–Speech–Image Gate

Với mỗi beat, ghi một câu:

```text
Voiceover nói [ý] → hình cho thấy [hành động/cơ chế] → text chốt [kết luận ngắn].
```

Nếu ba phần không cùng một mệnh đề, scene fail. Hình “cùng chủ đề” nhưng sai hành động cũng fail.

## Cấm

- Bokeh/particle field bắt buộc.
- Cyberpunk blue, neon cyan/pink, glassmorphism đại trà.
- 3–5 card cùng trọng lượng thị giác.
- Headline 90–124px với tracking âm mạnh.
- Flash/SFX ở mọi boundary.
- Scale/bounce/rotation chỉ để tạo cảm giác “động”.
- B-roll văn phòng chung chung không liên quan động từ của câu nói.
- Fake morph bằng crossfade hai object giống nhau.
- Camera move không tiết lộ thêm thông tin.
- Contact sheet gồm nhiều layout đẹp nhưng không có state progression.
