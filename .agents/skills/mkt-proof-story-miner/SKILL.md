---
name: mkt-proof-story-miner
description: Tìm, xác minh và đóng gói proof, câu chuyện, quyết định, demo và trải nghiệm nghề nghiệp cho bất kỳ thương hiệu hoặc tác giả nào từ các nguồn được chỉ định. Dùng khi cần nguyên liệu thật cho content, video, case, trust anchor, build in public hoặc Story Bank mà không gắn cứng với một cá nhân.
---

# MKT Proof & Story Miner

Tạo nguyên liệu có truy xuất nguồn. Không viết case thành công chỉ vì tìm thấy proposal, roadmap hoặc KPI dự kiến.

## Đầu vào

- `brand_name` hoặc `author_name`.
- `source_roots`: danh sách thư mục business context, dự án, nhật ký hoặc Second Brain được phép đọc.
- `excluded_sources`: tên dự án, khách hàng, người hoặc chủ đề không được dùng.
- Topic, audience, platform và claim cần hỗ trợ.

Nếu chưa có `source_roots`, tìm các thư mục context chuẩn trong workspace hiện hành. Không tự đọc kho cá nhân bên ngoài workspace khi người dùng chưa đưa vào phạm vi.

## Thang proof P0–P5

| Cấp | Ý nghĩa | Cách dùng |
|---|---|---|
| P0 | Quan điểm hoặc giả thuyết | Nói là điều đang kiểm tra |
| P1 | Trải nghiệm, quyết định hoặc quan sát có nguồn | Story, reframe, bài học |
| P2 | Tài sản hoặc demo có thể kiểm tra | Trust anchor, screen recording, log |
| P3 | Pilot có baseline hoặc quy trình đo | Build in public, nêu rõ đang thử |
| P4 | Case có baseline, thời gian, kết quả và quyền công bố | Case study có giới hạn |
| P5 | Kết quả lặp lại hoặc được bên thứ ba xác nhận | Claim mạnh trong phạm vi mẫu |

Thiếu một thành phần thì hạ cấp. Không nâng proof vì câu chuyện nghe thuyết phục.

## Phân loại nguồn

- `Trải nghiệm tác giả`: trực tiếp làm, quyết định hoặc trải qua.
- `Tài sản thương hiệu`: sản phẩm, SOP, framework, demo hoặc hệ thống có file chứng minh.
- `Tín hiệu thị trường`: phỏng vấn, phản đối, câu hỏi hoặc nhu cầu; không đồng nghĩa doanh thu.
- `Nguồn ngoài`: sách, video, mentor hoặc clipping; không viết thành trải nghiệm của tác giả.
- `Giả định/dự phóng`: target, KPI, proposal hoặc mô hình chưa chạy.

## Quy trình

1. Chốt thương hiệu/tác giả, topic, audience, platform và claim.
2. Dùng `rg` tìm rộng trong `source_roots`, rồi chọn 3–8 note có tín hiệu cao.
3. Loại toàn bộ nguồn thuộc `excluded_sources`; không ẩn danh để lách quy tắc.
4. Đọc đủ ngữ cảnh và theo liên kết tối đa một bước khi cần xác minh.
5. Xác định P0–P5, quyền công bố, chi tiết phải lược và giới hạn claim.
6. Chuyển thành `trust anchor`, `story seed` hoặc `demo seed`.

## Đầu ra

```markdown
### [Mã] · [Tên chuyện]
- Thương hiệu/tác giả:
- Xảy ra:
- Phản ứng hoặc quyết định:
- Chuyển biến và bài học:
- Proof level:
- Nguồn tuyệt đối:
- Được công khai: có | có điều kiện | chưa rõ
- Chi tiết phải bỏ:
- Hook gợi ý:
```

Kết thúc bằng ba nhóm: `Dùng ngay`, `Cần bổ sung bằng chứng`, `Không dùng`.
