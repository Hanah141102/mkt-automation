# Đề xuất Pexels, SFX và text effect

## Pexels

Mỗi B-roll phải trả lời đủ bốn câu:

1. Câu nói nào đang phát?
2. Danh từ cụ thể là gì?
3. Hành động/động từ cần thấy là gì?
4. Clip giúp chứng minh ý hay che jump cut nào?

Ưu tiên placement 2–5s: thao tác tay, hành động thật, close-up vật thể hoặc bối cảnh có quan hệ nhân quả. Tránh “văn phòng đẹp”, người gõ laptop chung chung, logo/brand nhạy cảm và footage không có hành động đúng câu.

Không đặt B-roll:

- Trong 3 giây đầu.
- Trên punchline/câu thú nhận/cảm xúc cần thấy mặt.
- Chồng hai asset hoặc chèn giữa trigger → proof của một HyperFrames scene.
- Dài hơn phần transcript mà nó chứng minh.

Schema item:

```json
{
  "id": "br-01",
  "start": 8.4,
  "end": 12.2,
  "intent_vi": "Cho thấy chủ doanh nghiệp giao việc và phản hồi ngay",
  "query_en": "business owner assigning task close up vertical",
  "noun": "chủ doanh nghiệp",
  "verb": "giao việc",
  "purpose": "evidence",
  "source_type": "user | pexels | library | screen-recording",
  "covers_cut": "seg-003→seg-004",
  "status": "proposed"
}
```

`purpose`: `evidence`, `jump-cut-cover`, `context`. Chỉ tải asset sau approval; sau resolve đổi `status` thành `resolved` và thêm asset/provenance.

## HyperFrames

Dùng khi câu nói cần giải thích cơ chế, so sánh, chuỗi nguyên nhân hoặc số liệu mà footage thật/Pexels không chứng minh được. Mỗi scene có `claim`, `source_object`, `start_state`, `transformation`, `end_state`, `spoken_anchor`, `proof_hold_s`. Ưu tiên block liên tục ≥3,5s.

## SFX

SFX phải đồng bộ một thay đổi nhìn thấy hoặc spoken anchor:

- `whoosh`: cut/reveal lớn, volume 0.12–0.20.
- `snap/click`: marker/bước khóa vào, 0.15–0.24.
- `impact`: con số hoặc kết luận chính, 0.18–0.30.
- `notification`: CTA liên quan comment/message, 0.15–0.24.

Tối đa 6 hit/phút, cách nhau ≥1,25s. Không auto gắn SFX vào mọi cut.

## Text effect

Copy 1–6 từ; không chép lại cả caption. Các kiểu được phép:

- `number-punch`: số liệu/chỉ số.
- `keyword-lock`: từ khóa chốt.
- `contrast-swap`: A → B.
- `step-marker`: `#1`, `#2`, `#3`.
- `quote-pin`: câu trích cực ngắn.

Text effect phải có `spoken_anchor` và xuất hiện trong ±0,12s quanh từ/cụm được nói. Không đặt vào vùng subtitle `y≥1460`.

## Schema `enhancement-plan.json`

```json
{
  "version": 1,
  "total_duration": 42.8,
  "visual_mix": {
    "min_real_media_ratio": 0.30,
    "max_hyperframes_ratio": 0.20,
    "approved_override": false,
    "override_reason": ""
  },
  "face_moments": [{"start": 0, "end": 3.2, "reason": "hook"}],
  "broll": [],
  "hyperframes": [],
  "sfx": [],
  "text_effects": []
}
```

Mọi timestamp dùng output time của `rough-cut.mp4`, không dùng source time.
