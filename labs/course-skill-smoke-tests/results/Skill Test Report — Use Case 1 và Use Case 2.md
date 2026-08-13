# Báo cáo kiểm thử skill — Use Case 1 và Use Case 2

Ngày kiểm thử: 2026-08-12

## Use Case 1 — Nghiên cứu kênh đối thủ bằng Apify

| Tên gọi chính xác | Vai trò | Cách chạy | Kết quả kiểm thử |
|---|---|---|---|
| `$mkt-phan-tich-doi-thu` | Xác minh và phân loại đối thủ | Gọi bằng prompt | ĐẠT với brief mẫu; không có script |
| `$mkt-apify-competitor-social-analyzer` | Lập kế hoạch, thu thập và chuẩn hóa dữ liệu mạng xã hội công khai | Chạy chương trình Python | ĐẠT `--help`, `--check-deps`, `--dry-run` và dữ liệu mock |
| `$content-ideation` | Biến báo cáo và khoảng trống thành ý tưởng có thể kiểm chứng | Gọi bằng prompt | ĐẠT với brief mẫu và checklist bảy lớp; không có script |

### Bằng chứng Apify

- Dependency: `apify-client 3.1.2`.
- Dry run: tạo 2 kế hoạch trong `planned-runs.json`.
- Mock run: chuẩn hóa 3 bản ghi thành 2 nhóm kênh.
- Tạo được `normalized-data.json` và `competitor-social-report.md`.
- Không gọi Actor thật và không phát sinh phí.
- Máy chưa có `APIFY_TOKEN`; vì vậy chưa xác nhận live run với Actor thật.

## Use Case 2 — Nghiên cứu báo và YouTube

| Tên gọi chính xác | Vai trò | Cách chạy | Kết quả kiểm thử |
|---|---|---|---|
| `$mkt-youtube-topic-researcher` | Tìm và xếp hạng video theo chủ đề | Chạy chương trình Python bằng `uv run` | ĐẠT với API thật, truy vấn 3 video |
| `$mkt-phan-tich-video-notebooklm` | Nạp nguồn vào NotebookLM và tổng hợp có dẫn chứng | Skill điều phối CLI `nlm` | ĐẠT end-to-end với 2 nguồn văn bản mẫu |

### Bằng chứng YouTube

- Từ khóa thử: `AI marketing automation`.
- Phạm vi: tối đa 3 video, trong một năm, ngưỡng lượt xem bằng 0.
- API trả về 3 video, có thống kê kênh và mức vượt trội.
- Lưu đúng `uc2-youtube/youtube-videos.json`.

### Bằng chứng NotebookLM

- CLI: `nlm 0.5.26`.
- Đăng nhập: hợp lệ.
- Notebook thử: `4c4fb126-9c4e-42ac-a82f-536bc15ff71a`.
- Nạp thành công 2 nguồn văn bản mẫu và kiểm tra lại đủ 2 nguồn.
- Query trả về câu trả lời tiếng Việt có dẫn chứng `[1]`, `[2]`.
- Notebook không bị xóa sau kiểm thử theo quy tắc an toàn của skill.

## Kết luận chung

Năm tên skill trong giáo án đều trùng với tên thư mục và trường `name` trong `SKILL.md`. Hai chương trình Python và luồng NotebookLM chạy được trên máy hiện tại. Hai skill prompt của Use Case 1 có đầy đủ tài liệu để vận hành, nhưng không nên mô tả cho học viên như một lệnh terminal.
