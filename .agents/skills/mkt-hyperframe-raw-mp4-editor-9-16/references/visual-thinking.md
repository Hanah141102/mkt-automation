# Visual Thinking — Biến lời nói thành một lập luận bằng hình

Nguồn học: repo `heygen-com/hyperframes-launches`, clone tại commit
`db564381d41bef3d9939bd112c7e76981176ff6f`. Các mẫu đáng học nhất là
`frame-md-launch-storyboard`, `claude-design-send-hyperframes-launch`,
`timeline-launch`, `inspector-launch` và `cloud-render-launch`.

Không sao chép palette, UI hoặc VFX của các launch. Chỉ lấy **cách tư duy hình ảnh** rồi
chuyển sang AI-HUB Blueprint, 9:16, tiếng Việt và pipeline footage thật/Pexels của skill này.

## Khác biệt cốt lõi

Minh họa yếu chỉ đặt một icon, vài card hoặc một sơ đồ cạnh câu nói. Visual thinking mạnh
biến chính mệnh đề thành một hành động nhìn thấy được:

```text
Lời nói nêu nguyên nhân → vật thể chịu tác động → trạng thái thay đổi → frame tự chứng minh kết luận.
```

Ví dụ:

- Yếu: nói “quy trình rời rạc” rồi hiện ba card.
- Mạnh: ba yêu cầu rời rạc va vào cùng một artifact, artifact tái cấu trúc thành gateway,
  luồng chỉ chạy tiếp khi cổng duyệt mở.
- Yếu: nói “hãy nhìn toàn hệ thống” rồi zoom ngẫu nhiên.
- Mạnh: bắt đầu ở một chi tiết gây lỗi, camera lùi ra để lộ quan hệ khiến lỗi đó xảy ra.

## Visual Thinking Contract — bắt buộc cho mọi beat HyperFrames

Trước khi author HTML, mỗi scene brief phải trả lời đủ:

```yaml
claim: "Mệnh đề duy nhất scene phải chứng minh"
noun_verb: "Danh từ + động từ cụ thể trong lời nói"
persuasion: "before-after | cause-effect | comparison | proof | callback | distillation"
source_object: "Một vật thể chính tồn tại xuyên scene"
start_state: "Trạng thái nhìn thấy ở đầu"
transformation: "Thay đổi vật lý/cấu trúc mang ý nghĩa"
end_state: "Trạng thái cuối tự chứng minh claim"
causal_trigger: "Từ được nói, click, flow chạm gate, dữ liệu đến..."
motion_route: "shared-object-morph | camera-reveal | accumulation | causal-chain | semantic-removal | evidence-physicalization"
focal: "Một điểm mắt phải nhìn"
supporting: ["Tối đa hai thành phần hỗ trợ, xuất hiện theo cue"]
scale_plan: "Tương phản tỉ lệ nào làm rõ hierarchy"
vo_cues: [{anchor: "từ/cụm từ", local_s: 0.0, event: "hành động hình ảnh"}]
tail_behavior: "live-resolution | deliberate-stillness"
transition_in: {vector: "left|right|up|down|z|none", carrier: "vật thể nối seam"}
transition_out: {vector: "left|right|up|down|z|none", carrier: "vật thể nối seam"}
exact_copy: ["Mọi chữ trên màn hình, viết nguyên văn"]
```

Nếu thiếu `source_object`, `transformation` hoặc `end_state`, scene chưa có visual argument;
không được chữa bằng card, icon, particles hoặc camera push trang trí.

## Sáu motion route ưu tiên

### 1. Shared-object morph

Cùng một element đổi vai trò nhưng không biến mất: brief → gateway → hệ thống; con số →
progress rail → kết quả; document → workflow map. Đây là route mạnh nhất để tránh slideshow.

Quy tắc: source và destination phải chia sẻ hình học hoặc ý nghĩa. Không crossfade hai object
khác nhau rồi gọi đó là morph.

### 2. Camera reveal — zoom để lộ nguyên nhân

Camera bắt đầu ở chi tiết có ý nghĩa, rồi truck/zoom để tiết lộ quan hệ rộng hơn. Move chỉ hợp
lệ khi frame cuối chứa thông tin mà frame đầu chưa thể thấy. Không pan qua khoảng trống chỉ để
“cinematic”.

### 3. Accumulation / recompose

Không xoá từng ý sau khi đọc. Mỗi cue thêm một phần vào cùng canvas; đến payoff, các phần đã
có tự sắp lại thành kết luận. Phù hợp list, quy trình, nhiều agent và before/after.

### 4. Causal chain

Một hành động gây ra hành động kế tiếp: từ khóa bật node, node phát trace, trace chạm gate,
gate mở, output mới xuất hiện. Không cho mọi element animate cùng lúc.

### 5. Evidence physicalization

Biến bằng chứng thành vật liệu của lập luận: tài liệu bị crop cho thấy thiếu context; hàng đợi
dài dần cho thấy bottleneck; hai lane lệch nhịp cho thấy handoff lỗi. Screenshot/Pexels không
đứng làm wallpaper mà bị đóng băng, crop, annotate hoặc nối vào mechanism.

### 6. Semantic removal / silence

Khi lời nói là “loại bỏ”, “tập trung”, “im lặng”, “đơn giản”, hãy bớt visual furniture thật.
Negative space là kết quả của hành động, không phải chỗ trống chưa thiết kế.

## Ba micro-arc thay cho công thức card mặc định

Chọn một, không ép beat nào cũng `context → mechanism → conclusion` giống nhau:

1. **Cause → mechanism → consequence**: nguyên nhân đi vào hệ thống, cơ chế xử lý, hậu quả hiện ra.
2. **Artifact → hidden bias → wrong output → verdict**: dùng cho chẩn đoán sai lầm.
3. **Promise → proof → compression**: claim lớn, bằng chứng vận hành, chốt lại thành một hình/câu ngắn.

## Scale là một phần của tư duy

- Một focal element ở display scale; supporting nhỏ hơn rõ ràng, không phải ba card ngang hàng.
- Dùng crop có chủ đích để nói “quá lớn”, “thiếu góc nhìn” hoặc “còn nằm ngoài frame”.
- Dùng zoom-out để chuyển từ chi tiết sang hệ thống; zoom-in để chuyển từ hệ thống sang quyết định.
- 9:16 ưu tiên trục dọc như một hành trình: input ở trên → mechanism giữa → decision/output trước
  `y=1480`. Không xếp desktop UI thu nhỏ chỉ để chứa đủ chi tiết.

## Seam Ledger — continuity không được giao riêng cho từng scene

Orchestrator lập ledger trước khi fan-out:

| Seam | Exit vector | Entry vector | Carrier | Quan hệ |
|---|---|---|---|---|
| scene-01 → scene-02 | down | down | copper trace | tiếp tục cùng luồng |
| scene-02 → Pexels | z-in | z-in | document frame | từ cơ chế sang bằng chứng |
| Pexels → scene-03 | left | left | thao tác bàn tay/module | hành động thật thành sơ đồ |

- Vector ra/vào phải cùng dấu khi là một chuyển động liên tục.
- Carrier có thể là vật thể, shape, màu, action vector hoặc audio phrase.
- Clean cut được phép khi có lý do: đổi luận điểm, punchline hoặc contrast có chủ đích.
- Avatar seam vẫn ưu tiên opaque clean/masked reveal; không hy sinh quy tắc 3 giây full-face.

## Pexels như một beat điện ảnh

- Chọn clip theo `noun_verb`, không theo chủ đề chung.
- Vào footage bằng match action hoặc carrier; ra bằng freeze + annotation, object continuation
  hoặc cùng vector chuyển động.
- Nếu footage chỉ lấp quota nhưng không làm luận điểm rõ hơn, resolver phải tìm lại.
- Không đặt infographic dày trên footage. Một annotation hoặc một crop có mục đích thường mạnh hơn.

## Contact sheet trước motion

Với pattern mới, tạo 3–5 styleframe thể hiện **trạng thái**, không phải nhiều layout độc lập:

1. start state;
2. causal trigger;
3. transformation peak;
4. proof/end state;
5. seam handoff nếu cần.

User duyệt logic thay đổi trạng thái và hierarchy trước; sau đó mới author timeline. Một contact
sheet đẹp nhưng các frame không chia sẻ object/carrier vẫn fail visual thinking.

## Gate tự review

Scene chỉ PASS khi trả lời “có” cho các câu sau:

1. Tắt toàn bộ text đi, người xem còn đoán đúng quan hệ/hành động không?
2. Có một vật thể hoặc bằng chứng thay đổi trạng thái thật không?
3. Chuyển động có nguyên nhân nhìn thấy hoặc nghe thấy không?
4. Frame cuối có chứng minh claim, thay vì chỉ trang trí cho claim không?
5. Focal có thắng supporting về scale, contrast và timing không?
6. Tail có tiếp tục resolve hoặc cố ý im lặng, thay vì chết vì hết animation không?
7. Scene nối được với beat trước/sau bằng carrier, vector hoặc contrast có chủ đích không?

Fail bất kỳ câu 1–4 → redesign brief trước khi sửa HTML.
