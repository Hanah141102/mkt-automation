# Script-led creative direction

## Mục lục

1. Mục tiêu
2. Script fingerprint
3. Ba route sáng tạo
4. Chọn visual grammar
5. Thiết kế scene
6. Continuity
7. Pexels, logo và UI
8. Typography tiếng Việt
9. Creative review
10. Ví dụ tham chiếu

## 1. Mục tiêu

Tạo một visual system sinh ra từ nội dung kịch bản, không lấy một design system có sẵn rồi thay chữ. Mỗi quyết định hình ảnh phải trả lời được: “Chi tiết này giúp người xem hiểu câu nói nào nhanh hơn?”

Giữ tự do cao ở palette, typography, metaphor, layout và motion. Giữ ràng buộc thấp ở tính đúng nghĩa, readability, continuity, timing và render safety.

## 2. Script fingerprint

Trích fingerprint trước khi nghĩ đến màu sắc:

```yaml
topic: ""
audience: ""
core_tension: ""
emotional_temperature: "calm | curious | urgent | confrontational | optimistic"
information_density: "low | medium | high"
reality_level: "documentary | hybrid | abstract"
named_entities: []
physical_nouns: []
visual_verbs: []
proof_types: []
brand_constraints: []
```

Ưu tiên danh từ có thể nhìn thấy và động từ có thể animate. Nếu câu nói trừu tượng, physicalize bằng một vật thể quen thuộc: tài liệu, hàng đợi, cánh cửa, bàn cân, dây chuyền, bản đồ, đồng hồ, checklist, hộp thư hoặc màn hình công cụ.

## 3. Ba route sáng tạo

Tạo ba route thật sự khác nhau:

- Route A khác metaphor và không gian chính so với B/C.
- Route B khác mức hiện thực: ví dụ documentary UI thay vì abstract 2.5D.
- Route C khác motion logic: ví dụ semantic removal thay vì accumulation.

Mỗi route ghi:

```yaml
name: ""
one_sentence_thesis: ""
world: ""
hero_object: ""
palette_logic: ""
type_logic: ""
motion_route: ""
persistent_motif: ""
pexels_role: ""
risk: ""
```

Chấm 1–5 theo:

- Semantic fit ×3
- Readability ×3
- Originality ×2
- Continuity ×2
- Feasibility ×2

Chọn route tổng cao nhất. Không chọn route chỉ vì “đẹp” nếu proof khó đọc hoặc cần hiệu ứng quá phức tạp so với thời lượng.

## 4. Chọn visual grammar

Có thể dùng hoặc kết hợp:

- Documentary interface: UI, cursor, prompt, bảng đánh giá, diff.
- Physical metaphor: vật thể đổi trạng thái, lắp ráp, tách lớp, bị kiểm tra.
- Editorial typography: chữ là hành động, từ khóa bị gạch, thay thế, đối chiếu.
- Data physicalization: số liệu thành khối lượng, dòng chảy, khoảng cách hoặc nhịp.
- Diagrammatic world: sơ đồ là không gian có camera, không phải slide phẳng.
- Collage/cutout: footage và graphic tương tác có chủ đích.
- Minimal cinematic: một vật thể lớn, chuyển động ít nhưng có consequence rõ.

Không có grammar mặc định. Không dùng nhiều grammar ngang vai trong một video; chọn một grammar chính và tối đa một grammar phụ.

## 5. Thiết kế scene

Mỗi scene cần:

1. Một claim.
2. Một source object có trạng thái ban đầu.
3. Một visual verb làm object đổi trạng thái.
4. Một end state/proof giữ đủ lâu để hiểu.
5. Một headline cô đọng, không chép lại caption.

Hero animation chỉ có một. Supporting element phải phục vụ cue khác nhau, không xuất hiện cùng lúc như ba card ngang hàng.

Khi script nói về prompt hoặc thao tác AI:

- Cho prompt xuất hiện dần theo phrase, không paste cả đoạn cùng lúc.
- Giữ cursor/typing state thật.
- Chỉ dùng logo đúng công cụ đang có vai trò trong câu.
- Sau khi gửi prompt, hình phải cho thấy output hoặc consequence, không dừng ở màn hình gõ.

## 6. Continuity

Orchestrator chọn một persistent motif và tối đa hai transition family. Scene agents không tự thay đổi.

Một seam hợp lệ cần ít nhất một dạng liên tục:

- Shared object.
- Shared vector.
- Shared color/shape carrier.
- Cause ở scene trước, effect ở scene sau.
- Clean cut có punchline hoặc contrast rõ.

Không crossfade hai scene bán trong suốt. Không dùng flash ở mọi seam.

## 7. Pexels, logo và UI

Pexels phải chứng minh noun + verb của câu nói. Ví dụ:

- “soạn bản nháp” → tay gõ trên laptop.
- “rà soát” → người đọc và đánh dấu tài liệu.
- “sửa theo góp ý” → checklist hoặc chỉnh tài liệu.
- “kiểm tra chéo” → hai người cùng xem một hồ sơ.

Không dùng “người làm việc trong văn phòng” chung chung khi câu nói có hành động cụ thể hơn.

Logo và UI làm tăng tính thật khi script gọi tên công cụ. Dùng asset rõ nguồn, không kéo logo mờ, không bóp tỷ lệ. UI mô phỏng phải đủ quen để hiểu nhưng không cần sao chép toàn bộ sản phẩm.

## 8. Typography tiếng Việt

Dấu tiếng Việt làm glyph vượt ascender/descender Latin. Vì vậy:

- Bắt đầu line-height 1,18 cho headline in hoa.
- Giảm font-size trước khi ép tracking quá chặt.
- Dùng 2 dòng có khoảng cách thị giác rõ; không để dấu dòng dưới chạm thân chữ dòng trên.
- Kiểm tra frame sau khi font local đã load; browser fallback có metrics khác.
- Giữ headline trong một box riêng, hero visual bắt đầu sau box ít nhất 48px.
- Dùng `getBoundingClientRect()` hoặc frame QA để phát hiện box cắt/chồng; không tin duy nhất vào CSS lint.

## 9. Creative review

Review storyboard theo hai pass:

Pass 1 — Meaning:

- Tắt toàn bộ text, còn hiểu hành động chính không?
- Source object có thay đổi thật hay chỉ crossfade?
- Proof có nhìn thấy consequence không?
- Pexels có đúng noun + verb không?

Pass 2 — Craft:

- Headline có chồng dấu hoặc sát hero không?
- Focal có thắng về scale, contrast và timing không?
- Hai scene liền nhau có lặp layout không?
- Motion có land đúng spoken cue không?
- Sound cue có một lý do rõ không?

Nếu pass 1 fail, redesign visual argument. Không chữa bằng thêm icon, glow hoặc card. Nếu pass 2 fail, sửa hierarchy, spacing, timing hoặc transition.

## 10. Ví dụ tham chiếu

Với kịch bản “ChatGPT viết, Claude phản biện, ChatGPT sửa”:

- Fingerprint: công cụ AI, tài liệu công việc, kiểm tra chéo, energy phân tích.
- Route phù hợp: control room tài liệu tối màu; xanh/đào phân vai; UI prompt và bảng lỗi là evidence; một document là shared carrier.
- HyperFrames: tài liệu đi từ draft → critic flags → accepted/rejected feedback → revised version → cross-check loop.
- Pexels: gõ laptop, đọc tài liệu, checklist, hai người cùng review.
- SFX: typing lúc prompt hiện, click khi gửi, notification lúc phản biện tới, success lúc bản sửa hoàn thành.

Đây là kết quả của fingerprint trên, không phải preset. Với kịch bản logistics, giáo dục, tài chính hoặc sức khỏe, phải tạo route mới từ noun + verb tương ứng; không tái dùng control room AI chỉ vì nó trông hiện đại.
