# Biên tập nguồn MP4 và EDL

## 1. Xác định đúng thứ tự

Ưu tiên bằng chứng theo thứ tự:

1. User chỉ định thứ tự cụ thể.
2. Prefix rõ trong filename: `01`, `part-1`, `take-03`.
3. Quan hệ ngôn ngữ: hook → đặt vấn đề → giải thích → ví dụ → kết luận/CTA.
4. Cụm nối: “tiếp theo”, “ý thứ hai”, “vì vậy”, “tóm lại”.
5. Thời gian tạo file chỉ là tie-breaker; copy/AirDrop có thể làm sai timestamp.

Không buộc giữ nguyên clip theo block. Có thể dùng một câu hook từ clip sau ở đầu rồi quay lại mạch chính, nhưng phải ghi `reason: "hook relocation"`.

## 2. Quy tắc cắt

- Trim im lặng đầu/cuối nếu không chứa hít vào có chủ đích. Giữ handle 80–160ms quanh phụ âm đầu/cuối.
- Pause nội bộ trên 0,65s là candidate, không phải lệnh cắt tự động. Giữ pause làm nhịp nhấn hoặc chuyển cảm xúc.
- Cắt `ừm`, `ờ`, `à`, `kiểu là` khi đứng riêng và hai phía nối tự nhiên. Không cắt filler dính vào âm đầu của từ kế tiếp.
- False start: bỏ mệnh đề bỏ dở, giữ lần nói hoàn chỉnh gần nhất.
- Lặp take: giữ take rõ, đúng và giàu năng lượng nhất; không mặc định take cuối nếu take trước tốt hơn.
- Nói sai fact hoặc phát âm sai: nếu có take sửa đúng, dùng take sửa. Nếu không có, flag `needs_user_decision`; không dùng text/Pexels để che một phát biểu sai.
- Off-topic chỉ cắt khi không tạo lỗ logic. Ghi lại câu nối trước/sau trong `evidence`.
- Không time-stretch giọng để vá cut. Không synthesize từ bị thiếu.

## 3. Schema `edit-plan.json`

```json
{
  "version": 1,
  "output": {"width": 1080, "height": 1920, "fps": 30},
  "sequence": [
    {
      "segment_id": "seg-001",
      "clip_id": "clip-001",
      "source_start": 1.24,
      "source_end": 6.82,
      "fit": "cover",
      "reason": "Hook hoàn chỉnh, bỏ im lặng đầu clip"
    }
  ],
  "removed": [
    {
      "clip_id": "clip-001",
      "source_start": 0.00,
      "source_end": 1.24,
      "reason_code": "silence",
      "evidence": "Không có từ; chỉ room tone"
    }
  ],
  "open_issues": []
}
```

`fit` nhận `cover` hoặc `contain-blur`. `sequence` có thể đổi thứ tự clip; script dùng đúng thứ tự mảng. Không để cùng một khoảng source xuất hiện hai lần trừ khi có lý do “callback” rõ.

`reason_code`: `silence`, `filler`, `false-start`, `mistake`, `duplicate`, `off-topic`, `technical`, `other`.

Nếu `open_issues` không rỗng hoặc có `reason_code: mistake` mà không có take sửa đúng, phải nêu cho user trước final.

## 4. Review EDL

`EDIT-REVIEW.md` phải có:

- Thứ tự clip/segment sau sắp xếp và lý do.
- Bảng đoạn giữ/bỏ theo source time.
- Tổng raw duration, kept duration, removed duration.
- Danh sách cut khó: phụ âm sát biên, room tone thay đổi, jump cut lớn, câu có thể đổi nghĩa.
- Mọi `open_issues` cần user quyết định.

Raw files là nguồn sự thật; không xóa dù final đã render.
