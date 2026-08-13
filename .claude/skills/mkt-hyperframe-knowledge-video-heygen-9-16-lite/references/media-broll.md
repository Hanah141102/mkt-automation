# Media trám (b-roll) — phân tích & đặt vị trí tự động

## Purpose
Trong thời gian không có avatar, video phải dùng **50% footage Pexels full-screen và 50% pure HyperFrames**. Kho SQLite được ưu tiên để tái sử dụng asset có provenance Pexels; thiếu mới tải từ Pexels. Skill `mkt-resolve-broll-media` chịu trách nhiệm reuse/download/materialize. Output là `media-manifest.json` — nguồn duy nhất để Phase 3 wire ảnh vào scene và Pexels b-roll vào master.

## When to Load
Phase 1b sau khi có `beats.json`, và khi wire master/scene có media.

---

## Visual Mix Budget — bắt buộc trước final render

```text
scene_time       = fullTotal − union(avatar windows)
pexels_target_s  = scene_time × 0.50
PASS             = Pexels coverage / scene_time nằm trong 0.45–0.55
HyperFrames      = scene_time − Pexels coverage
```

- Chỉ asset `usage: "broll-fullscreen"` có `source.provider: "pexels"` hoặc `assetId` bắt đầu bằng `pexels-` mới tính vào Pexels coverage. Asset Pexels tái sử dụng từ SQLite vẫn được tính.
- Coverage tính theo **union của placement thực tế**, không cộng trùng các clip overlap. Pexels phải là lớp hình visually dominant; HyperFrames chạy phía sau không được tính đồng thời.
- Captions, screenshot, ảnh tĩnh, footage user tự quay và stock không có provenance Pexels không tính vào quota. Pipeline không dùng PIP.
- Dùng ít nhất 2 Pexels asset khác nhau. Không placement nào được đè lên avatar window.
- Gate chuẩn:

  ```bash
  python3 "$SKILL/scripts/validate_visual_mix.py" --project "$OUT"
  ```

  Exit `0` mới được render final; exit `2` phải sửa asset/placement rồi chạy lại.

## Thuật toán (Phase 1b — chạy song song với TTS)

1. **Lập budget trước khi search** — đọc `avatar-windows.json`, tính `scene_time`, `pexels_target_s` và biên PASS. Từ `script.md` + `beats.json`, chọn đủ beat SCENE có hành động/bằng chứng/bối cảnh cụ thể để phủ target; không chọn `avatar:true`. Viết `broll-needs.json` theo contract của `mkt-resolve-broll-media`, tổng `desired_duration_s` xấp xỉ target.
2. **Inventory media user** — với mỗi file user cung cấp trong `media/`:
   ```bash
   bash $SKILL/scripts/prep_broll.sh probe <file>   # → {type, duration, width, height, orientation}
   ```
3. **Phân tích nội dung user media:**
   - **Ảnh:** Read trực tiếp file → mô tả 1-2 câu: nội dung chính, text trong ảnh, chất lượng, phù hợp dọc/ngang.
   - **Video:** `prep_broll.sh frames <video> <scratch_dir>` → 3 frame (10/50/90%) → Read cả 3 → mô tả nội dung + chọn **bestSegment** 3–6s (đoạn ổn định, chủ thể rõ, không rung/chuyển cảnh giữa chừng — suy từ 3 frame + duration).
4. **Resolve/gán beat:**
   - User chỉ định sẵn ("ảnh dashboard.png cho beat 3") → **chỉ định LUÔN thắng**, `assignedBy: "user"`.
   - Còn lại: gọi `mkt-resolve-broll-media`; thứ tự bắt buộc là user → Pexels có sẵn trong SQLite library → Pexels portrait mới.
   - **Ngưỡng local 0.5**: asset library dưới ngưỡng mới được gọi Pexels. Nếu Pexels sai chủ đề → cho vào `unused`, sửa query cụ thể hơn và rerun đúng 1 lần. Vẫn không đạt semantic QA hoặc coverage gate → BLOCK final render.
   - Mỗi asset dùng 1 lần. Mỗi beat ≤ 2 asset (1 ảnh trong scene + 1 b-roll). Cả video lẫn ảnh cùng match 1 beat → **video thắng** (chuyển động giữ retention tốt hơn), ảnh rơi xuống beat điểm cao kế tiếp.
5. **Chuẩn bị b-roll video:** resolver tự hard-link/copy source vào `media/`, trim/re-encode vào `broll-clips/`, tạo `broll-contact-sheet.jpg`, ghi provenance và usage ledger SQLite. Với media xử lý thủ công, dùng:
   ```bash
   bash $SKILL/scripts/prep_broll.sh trim <video> <bestSegment.start> <bestSegment.dur> broll-clips/<slug>.mp4
   ```
   Luôn re-encode chuẩn hoá (H.264 30fps keyframe dày, **strip audio** — voiceover là spine). Video >10s chỉ lấy bestSegment, phần còn lại bỏ.
6. **Đặt coverage và gate** — phân tán Pexels qua nhiều beat, ghi `placement.start_s` + `placement.duration_s`, rồi chạy `validate_visual_mix.py`. Nếu thấp hơn 45%, thêm placement phù hợp; nếu cao hơn 55%, rút ngắn/bỏ clip. Không render final cho tới khi PASS.

## media-manifest.json schema

```json
{
  "assets": [
    { "file": "media/dashboard.png", "type": "image", "orientation": "landscape",
      "description": "Screenshot dashboard doanh thu, số 128M nổi bật",
      "assignedBeat": "scene-03-how", "assignedBy": "user",
      "usage": "evidence-screenshot" },
    { "file": "media/factory.mp4", "type": "video", "duration": 22.4,
      "description": "Cảnh xưởng sản xuất góc rộng, ánh sáng tốt",
      "bestSegment": { "start": 6.5, "dur": 4.5 },
      "trimmed": "broll-clips/factory.mp4",
      "assignedBeat": "scene-01-problem", "assignedBy": "auto", "score": 0.87,
      "usage": "broll-fullscreen" }
  ],
  "unused": [
    { "file": "media/random-cat.jpg", "reason": "không liên quan beat nào (max score 0.21)" }
  ]
}
```

## Quy tắc đặt vị trí

| usage | Loại | Đặt ở đâu | Cách wire |
|---|---|---|---|
| `evidence-screenshot` | Ảnh dọc / screenshot | Trong scene HTML | Sub-agent prompt kèm abs path + mô tả; card nghiêng nhẹ + border + shadow, pattern theo `image-thumbnail-overlay.md`; LUÔN `onerror` ẩn container |
| `hero-kenburns` | Ảnh ngang chất lượng cao | Trong scene HTML | Nền full pane + gradient tối + hero text đè; GSAP scale 1.0→1.08 chậm |
| `broll-fullscreen` | Video trám | **MASTER** track 45+, z25 | `<video class="clip broll-clip">` `data-start` giữa beat, 3–6s, muted; BROLLS[] wiring (fade + ken-burns + #broll-shade) đã có trong template |

Timing b-roll trong beat: đặt ở **giữa beat**. Ưu tiên clip 2–6s. Beat ≥7s giữ trống 1–2s đầu/cuối khi budget cho phép. Beat 4–7s giữ trống 0.5–0.8s đầu/cuối và dùng clip 2–4s. Beat không chứa được ít nhất 2s an toàn → chuyển coverage sang beat SCENE khác. Sub-agent của beat đó được báo khoảng bị che (`b-roll covers 30.0–34.5s`) để không đặt nhịp nội dung quan trọng vào khoảng đó.

## Fallback & edge cases

- Beat không có asset → scene pure HyperFrames, miễn tổng coverage toàn video vẫn PASS 45–55%.
- Không có media user → vẫn phải resolve Pexels. Ưu tiên Pexels đã có trong SQLite nếu match ≥0.5; thiếu mới tải.
- Không có beat phù hợp với query đầu tiên → chuyển lời thoại thành hành động/bối cảnh nhìn thấy được và rerun 1 lần. Vẫn không đủ footage đúng chủ đề để PASS → BLOCK final render; không dùng 100% HyperFrames làm fallback.
- Video orientation ngang trên canvas dọc: object-fit cover tự crop center — nếu 3 frame cho thấy chủ thể lệch mép, hạ cấp thành ảnh (`hero-kenburns` với frame đẹp nhất).
- Ảnh quá nhỏ (<600px cạnh dài) → chỉ dùng `evidence-screenshot` cỡ nhỏ, không phóng to làm nền.
- Asset trùng nội dung nhau → giữ cái chất lượng cao hơn, cái kia vào `unused` ("duplicate of X").
