# Smoke Test — Use Case 5 — Đo hiệu quả Facebook

- Thư mục test: `/Users/tonyhoang/Documents/GitHub/mkt-automation`
- Ngày test: 2026-08-12
- Dữ liệu: `facebook-posts-clean-sample.csv`, 12 bài demo, không có dữ liệu thật của giảng viên hay học viên.

## Skill theo đúng thứ tự

1. `$data-preparation`: làm sạch, đối soát và ghi giới hạn dữ liệu.
2. `$mkt-marketing-measurement-designer`: định nghĩa KPI trước khi tính.
3. `$mkt-marketing-performance-analysis`: mô tả kết quả, không tự bịa nguyên nhân.
4. `$mkt-content-performance-optimizer`: chia Giữ / Sửa / Mở rộng / Dừng và thiết kế thử nghiệm.

## Kết quả

| Hạng mục | Kết quả |
|---|---|
| Bốn `SKILL.md` tồn tại và đọc được | PASS |
| File mẫu đúng schema 16 cột | PASS |
| 12 `post_id` không trùng | PASS |
| Không có mẫu số reach bằng 0 | PASS |
| KPI có tử số, mẫu số và kỳ đo | PASS |
| Tách nhóm theo objective trước so sánh | PASS |
| Sites/Artifact | KHÔNG DỰNG trong smoke test; đây chỉ là lớp giao diện sau khi số liệu đã được kiểm tra |

## Kết luận

Dây chuyền skill chạy được ở mức phương pháp và dữ liệu mẫu. Bài lab có thể dùng file này để học viên thử prompt mà không chạm dữ liệu riêng tư. Việc dựng dashboard tương tác được thực hiện trên ChatGPT Sites hoặc Claude Artifact trong lớp.
