# Contract visual plan

Đọc file này trước khi tạo `asset-inventory.json` hoặc `visual-plan.json`.

## Asset inventory

Mỗi media người dùng cung cấp phải có:

```json
{
  "id": "user-dashboard-01",
  "file": "media/dashboard.png",
  "type": "image",
  "width": 1440,
  "height": 2560,
  "orientation": "portrait",
  "description": "Dashboard đơn hàng với biểu đồ tăng trưởng",
  "visible_text": ["Đơn hàng", "Tăng 18%"],
  "safe_crop": "center",
  "proof_value": "Cho thấy số liệu có thể kiểm tra",
  "motion_potential": ["crop-reveal", "callout", "zoom-detail"],
  "privacy": "public-safe"
}
```

Không ghi nội dung riêng tư không cần thiết. Asset user chỉ định phải có `assignedBy: "user"`.

## Chấm điểm asset

```text
score = 0,35 × noun_verb_match
      + 0,25 × proof_value
      + 0,15 × crop_fit_9_16
      + 0,15 × motion_potential
      + 0,10 × readability
      − penalties
```

Penalties gồm trùng asset, mờ, crop mất chủ thể, lộ dữ liệu riêng tư, nhãn hiệu nhạy cảm hoặc chỉ cùng chủ đề. User assignment luôn thắng score.

## visual-plan.json

Mọi placement trong `placements` là lớp visually dominant. Callout, caption, connector và background không ghi thành dominant placement.

```json
{
  "version": "1.0",
  "approved": false,
  "preset": "asset-pexels-balanced",
  "message": "Một câu video phải chứng minh",
  "visual_thesis": "Ảnh thật xây lập luận, motion chỉ dẫn mắt",
  "placements": [
    {
      "beat_id": "scene-01",
      "kind": "user-asset",
      "start_s": 7.2,
      "duration_s": 5.4,
      "asset_id": "user-dashboard-01",
      "file": "media/dashboard.png",
      "pattern": "screenshot-callouts",
      "dominant": true
    },
    {
      "beat_id": "scene-02",
      "kind": "pexels",
      "start_s": 12.6,
      "duration_s": 4.0,
      "asset_id": "pexels-12345",
      "file": "broll-clips/customer-working.mp4",
      "pattern": "full-screen-evidence",
      "overlay": "none",
      "dominant": true
    },
    {
      "beat_id": "scene-02",
      "kind": "hyperframes",
      "start_s": 16.6,
      "duration_s": 2.8,
      "layout": "causal-chain",
      "reveal_mode": "word-aligned",
      "cue_ledger": [
        {
          "anchor": "agent chuyên trách",
          "absolute_s": 17.4,
          "scene_relative_s": 0.8,
          "target": "#specialist"
        }
      ],
      "dominant": true
    }
  ],
  "scene_briefs": [
    {
      "beat_id": "scene-01",
      "claim": "Dashboard làm vấn đề nhìn thấy được",
      "noun_verb": "dashboard cho thấy",
      "hero_asset": "user-dashboard-01",
      "visible_action": "camera crop vào chỉ số tăng",
      "vo_cues": [
        {"anchor": "tăng trưởng", "absolute_s": 9.1, "event": "highlight chỉ số"}
      ],
      "proof_hold_s": 0.9,
      "transition_in": {"vector": "z", "carrier": "khung screenshot"},
      "transition_out": {"vector": "z", "carrier": "khung screenshot"}
    }
  ]
}
```

## Contract semantic boundary và reveal

- Mọi placement Pexels phải có `overlay: "none"` và chỉ đại diện cho vế nó minh họa.
- Khi Pexels chuyển sang text/chart, `pexels.start_s + duration_s` phải bằng `hyperframes.start_s` ±0,05 giây.
- Text/chart nhiều ý phải có `reveal_mode: "word-aligned"` và `cue_ledger` theo `audio/alignment.json`.
- Mỗi cue cần `anchor`, `absolute_s`, `scene_relative_s` và `target`; không suy cue bằng chia đều duration.
- Ghi `layout` rõ như `text-chart-only`, `role-flow-chart`, `three-column-chart`, `human-gate-chart` hoặc `causal-chain`.
- Mọi visual plan phải phủ liên tục scene time. Nếu cắt Pexels ngắn hơn vì semantic match, kéo start của chart kế tiếp về đúng điểm cắt thay vì để gap.

Nếu dùng emphasis trên HeyGen, lưu riêng `heygen-emphasis-review/emphasis-plan.json`; không ghi emphasis thành dominant placement. Mỗi cue phải có window, spoken cue, start/end, text, style, vị trí và proof frame. Approval chỉ hợp lệ khi có `VISION-AUDIT.md` từ frame thật.

## Quy tắc coverage

Tính trên `scene_time = fullTotal − union(avatar windows)`:

- `user-asset`: 40–75% mặc định.
- `pexels`: 20–45% mặc định.
- `hyperframes`: không quá 20% mặc định.
- Tổng dominant coverage: ít nhất 95% scene time.
- Không cho hai dominant placement overlap quá 50ms.
- Không cho dominant placement overlap avatar quá 50ms.

Với video ngắn hoặc thiếu asset thật sự phù hợp, ghi bounds override và lý do trong `STORYBOARD.md`, trình user duyệt rồi truyền cờ tương ứng cho validator. Không tải filler media để đạt quota.

Ví dụ khi không có user asset và phần lớn luận điểm cần chart:

```bash
python3 scripts/validate_asset_broll_plan.py --project "$OUT" \
  --min-user 0 --max-user 0 \
  --min-pexels 0.20 --max-pexels 0.45 \
  --max-hyperframes 0.80 \
  --min-user-assets 0 --min-pexels-assets 2
```

## Đồng bộ media-manifest

Mọi placement `kind: "pexels"` phải trỏ tới đúng `assetId`, `trimmed`, `placement.start_s` và `placement.duration_s` trong `media-manifest.json`. Không tính stock không có provenance Pexels vào coverage Pexels.
