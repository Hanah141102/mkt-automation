# Sound design theo lời thoại

## Nguyên tắc

- Xem voice là lớp âm thanh chính; SFX chỉ làm rõ từ khóa, hành động UI và chuyển trạng thái.
- Lấy cue từ word timestamp. Đặt transient sát từ đầu của cụm cần nhấn, thường sớm hơn tối đa 2–3 frame.
- Không chèn SFX cho mọi câu. Giữ khoảng nghỉ để người xem không bị mệt.
- Tránh hiệu ứng dài hoặc nhiều bass dưới cảnh có lời dày.
- Mặc định giữ SFX thấp hơn voice; bắt đầu trong khoảng -22 đến -17 dB rồi dùng `master_gain_db` để hiệu chỉnh theo bản mix thật.
- Không dùng hiệu ứng lấy từ nguồn không rõ giấy phép. Ưu tiên SFX tự tổng hợp hoặc thư viện đã xác minh license và ghi vào manifest.

## Ánh xạ ý nghĩa

| Loại | Dùng cho | Tránh dùng cho |
|---|---|---|
| `impact` | con số lớn, lời hứa chính, kết luận mạnh | danh sách lặp lại |
| `pop` | từ khóa/card/logo xuất hiện | cảnh báo nghiêm túc |
| `click` | thao tác giao diện, chọn nút, tên file | tiêu đề cảm xúc |
| `tick` | checklist, bước hoàn tất | vấn đề chưa giải quyết |
| `whoosh` | chuyển section hoặc flow dữ liệu | mọi lần đổi clip |
| `warning` | dữ liệu bí mật, suy đoán, nhiệm vụ chậm | CTA tích cực |
| `success` | xác nhận nguồn, hoàn tất, kết luận tích cực | mở đầu vấn đề |
| `shimmer` | AI/kho kiến thức xuất hiện tinh tế | đoạn cảnh báo |

## Chọn cue

Ưu tiên:

1. Con số hoặc deadline được nhấn: “60 phút”, “bốn bước”, “mười phút”.
2. Ba câu hỏi hoặc các bước đi vào lần lượt.
3. Tên công cụ/logo đi vào đúng lời thoại.
4. Hành động UI: Copy Transcript, Audio File, kiểm tra nguồn.
5. Cảnh báo: đồng ý ghi âm, dữ liệu bí mật, không tự suy đoán.
6. Kết luận và CTA.

Không chèn thêm nếu trong vòng khoảng 0,6 giây đã có một transient khác, trừ khi đó là chuỗi checklist có chủ đích.

## SFX plan

Lưu ở `audio/sfx-plan.json`:

```json
{
  "version": 1,
  "source": "word-timestamps",
  "master_gain_db": 0,
  "cues": [
    {"time_s": 2.30, "type": "impact", "gain_db": -18, "label": "60 phút"},
    {"time_s": 5.58, "type": "pop", "gain_db": -19, "label": "chốt gì"}
  ]
}
```

Dùng `master_gain_db` để tăng hoặc giảm đồng loạt sau khi nghe thử. Với loa laptop, có thể thử từ `+3` đến `+9` dB; vẫn phải giữ gain cuối của từng cue không lớn hơn `-8 dB` và kiểm tra limiter/peak sau khi mix.

Chạy:

```bash
python3 scripts/mix_sfx.py \
  --video /absolute/path/to/draft.mp4 \
  --plan /absolute/path/to/project/audio/sfx-plan.json \
  --output /absolute/path/to/draft-with-sfx.mp4
```

Chạy `--dry-run` trước để kiểm tra toàn bộ cue nằm trong duration.

## Kiểm tra khả năng nghe

Không chỉ xác nhận file có audio stream. Dùng cả phép đo và nghe thật:

1. Chọn tối thiểu ba cue đại diện: một impact, một chuỗi click/tick và một whoosh/warning.
2. Đo cửa sổ 0,3–0,5 giây tại cùng timestamp trên bản baseline và bản có SFX.
3. Nếu chênh peak nhỏ hơn khoảng 1,5 dB và loa laptop không nghe rõ, tăng `master_gain_db` thêm 3 dB rồi render lại.
4. Nếu SFX che phụ âm hoặc làm limiter hoạt động liên tục, giảm cue đó 2–4 dB hoặc bỏ cue.
5. Tắt auto-level của limiter. Với FFmpeg `alimiter`, dùng `level=false`; nếu không, limiter có thể tự nâng toàn bộ âm lượng và làm sai đánh giá.
6. Sau AAC encode, giữ `max_volume` không cao hơn `-1 dB`, nghe đầu/giữa/cuối và decode toàn bộ MP4.

Ví dụ đo một cửa sổ quanh cue tại giây 29,28:

```bash
ffmpeg -hide_banner -ss 29.20 -t 0.40 -i baseline.mp4 \
  -map 0:a:0 -af volumedetect -f null - 2>&1
ffmpeg -hide_banner -ss 29.20 -t 0.40 -i draft-with-sfx.mp4 \
  -map 0:a:0 -af volumedetect -f null - 2>&1
```

Cuối cùng, nghe spot-check trên tai nghe và loa laptop. Phép đo không thay thế việc nghe; nó chỉ phát hiện nhanh trường hợp SFX bị chôn dưới voice.
