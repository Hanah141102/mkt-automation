# Hợp Đồng Bàn Giao Giữa Các Agent

## Mục lục

1. Quy tắc chung
2. Source analyst
3. Idea strategist
4. Scriptwriter
5. Video producer
6. Publisher
7. Approval package

## 1. Quy tắc chung

Mỗi sub-agent nhận đúng các trường sau:

- Skill bắt buộc phải đọc và dùng.
- File đầu vào tuyệt đối.
- Một file hoặc một tập file output thuộc ownership của agent.
- Artifact version hiện hành.
- Tiêu chí hoàn tất và điều kiện dừng.
- Lệnh cấm side effect ngoài phạm vi.

Mỗi agent trả báo cáo tối đa 150 từ:

```text
Status: DONE | DONE_WITH_CONCERNS | NEEDS_REVIEW | BLOCKED
Output: <absolute path hoặc danh sách path>
Checks: <các gate đã PASS>
Concerns: <không có hoặc mô tả ngắn>
```

Không gửi toàn bộ nội dung artifact qua message nếu đã có file. Orchestrator
phải tự đọc output và xác minh trước khi chuyển stage.

## 2. Source analyst

Skill: `mkt-phan-tich-video-notebooklm`.

Input:

- URL hoặc đường dẫn source.
- Câu hỏi phân tích: hook, tension, cấu trúc, luận điểm, bằng chứng, cơ chế giữ
  người xem và cơ hội tạo góc mới cho thương hiệu.
- Business goal và audience nếu đã biết.

Output `source-analysis.md`:

- Tóm tắt nguồn.
- Cấu trúc và timecode nếu có.
- Hook/pattern đáng học.
- Tuyên bố và bằng chứng trong nguồn.
- Khoảng trống hoặc điểm có thể phản biện.
- Ranh giới chống sao chép.
- Source ID/link hỗ trợ.

Không tạo content cuối và không publish.

## 3. Idea strategist

Skill: `content-ideation`.

Input:

- Business context và brand voice.
- Ý tưởng thô hoặc `source-analysis.md`.
- Mục tiêu, audience, duration và CTA.

Output `idea-review.md`:

```markdown
# Gói Duyệt Ý Tưởng — vN

## Phương án khuyến nghị
- Góc nội dung
- Lời hứa với người xem
- Hook
- Insight/tension
- Proof cần dùng
- Điểm khác biệt
- Rủi ro hoặc giả định

## Creative brief đã đề xuất
- Topic
- Format: short-form 9:16
- Duration
- Audience
- Goal
- Key points theo thứ tự
- CTA duy nhất
- Tone

## Outline để duyệt cùng idea
- Hook
- Beat 1..N
- Re-hook
- CTA

## Hai phương án dự phòng
...

## Khuyến nghị duyệt
...
```

Nếu người dùng chọn phương án dự phòng chưa có full brief/outline, tạo
`idea-review-vN+1.md` cho phương án đó và duyệt lại Gate 1 trước khi viết.

## 4. Scriptwriter

Skill: `video-script`.

Input:

- `idea-review.md` version đã duyệt.
- Approval record cùng version.
- Output path.

Nói rõ rằng Gate 1 đã duyệt cả brief và outline. Agent viết Phase 3–4 của
`video-script`; không mở rộng topic, thêm CTA hoặc đổi audience.

Output `video-script.md`:

- Lời đọc chính xác.
- Timestamp/ước lượng duration mỗi beat.
- `[B-ROLL]`, `[TEXT ON SCREEN]`, `[CUT TO]`, `[SFX]`, `[PAUSE]` phù hợp.
- Shot list.
- Text overlay list.
- Word count và duration estimate.
- Pre-production checklist cần cho video producer.

## 5. Video producer

Skill: `mkt-hyperframe-knowledge-video-heygen-9-16-lite`.

Input:

- Script version đã duyệt.
- Mode của parent.
- Project output directory.
- Media người dùng cung cấp nếu có.

Trong `review`, dừng tại approval gate nội bộ sau khi có:

- `design.md`.
- `STORYBOARD.md` và seam ledger.
- `storyboard-preview.html`.
- Storyboard contact sheet/styleframes.

Sau approval hoặc trong `fast`, chạy đúng fan-out policy của skill video.
Scene agent chỉ sở hữu scene file; parent/video producer giữ index, TTS,
HeyGen, captions, validation và render.

Output cuối:

- MP4 1080×1920.
- Báo cáo duration, avatar ratio, Pexels/HyperFrames ratio.
- Kết quả alignment, sync, visual mix, lint và frame QA.

## 6. Publisher

Skill: `mkt-blotato-publish-social`.

Input:

- Absolute path MP4 đã QA.
- Một danh sách exact target đã preflight.
- `publish_action` và `scheduled_time_utc` nếu có.
- Script/idea để viết caption theo từng nền tảng.

Chỉ một publisher agent xử lý toàn bộ target. Ưu tiên Composio; dùng Blotato
fallback theo skill. Không in credential, không đổi target, không retry mù.

Mỗi target trong state dùng schema:

```json
{
  "platform": "facebook",
  "target_name": "Tên Page/kênh đã đối chiếu",
  "target_id": "page/channel/profile ID",
  "connection": "composio",
  "account_id": null,
  "verified_at": "2026-08-18T10:00:00+07:00"
}
```

`connection` chỉ nhận `composio` hoặc `blotato`. Với Blotato, `account_id` là
bắt buộc ngoài `target_id`. `verified_at` phải được tạo bởi preflight read-only,
không được điền bằng suy đoán.

Output `publish-report.md`:

| Platform | Target name | Target ID | Trạng thái | Submission/Post ID | Public URL | Lỗi |
|---|---|---|---|---|---|---|

`processing` không phải `published`. Với target lỗi sau khi một target khác đã
thành công, báo partial success; không rollback hoặc đăng lại target thành công.

## 7. Approval package

Khi trình gate trong `review`, luôn hiển thị:

- Gate và artifact version.
- Link absolute tới artifact chính và preview.
- Ba lựa chọn bằng lời tự nhiên: duyệt, yêu cầu sửa, hoặc dừng.
- Tác động downstream nếu sửa.

Approval chỉ hợp lệ khi phản hồi có thể gắn rõ với artifact version hiện tại.
Ghi `approved_by: user` và timestamp ISO-8601. Trong `fast`, ghi
`approved_by: orchestrator` và `status: auto_approved`.
