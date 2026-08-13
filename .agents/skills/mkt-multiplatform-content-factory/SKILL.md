---
name: mkt-multiplatform-content-factory
description: Điều phối dây chuyền content cho bất kỳ thương hiệu nào từ research pack thành lịch và gói nội dung native cho Facebook, TikTok, Reels, Shorts, YouTube hoặc kênh được chọn. Dùng khi lập lịch tuần/tháng, batch production hoặc chuyển một nhóm insight thành nhiều asset theo công suất, trụ cột và CTA của từng thương hiệu.
---

# MKT Multiplatform Content Factory

Tạo một hệ thống nội dung dùng chung topic, take và proof, nhưng mỗi asset phải đứng độc lập và native với kênh.

## Đầu vào

- Kết quả `$mkt-brand-context-guard`.
- Một hoặc nhiều research pack từ `$mkt-kallaway-growth-topic-radar-vn`.
- Proof/story từ `$mkt-proof-story-miner` khi có.
- `platforms`, vai trò từng kênh, kỳ kế hoạch và công suất đã duyệt.
- Trụ cột, audience, stage, offer, CTA và biến cần thử.

Không dùng số lượng bài, vai trò nền tảng, CTA hay tỷ trọng của thương hiệu khác. Nếu chưa có công suất, đề xuất một bản nháp theo nguồn lực được cung cấp và đánh dấu cần duyệt.

## Quy trình

1. Khóa thương hiệu, research pack, pillar, audience, proof và một biến thử nghiệm.
2. Chốt công suất theo từng platform và nguồn lực sản xuất.
3. Vẽ content tree và connective tissue trước khi viết.
4. Dùng `$mkt-kallaway-hook-story-engine-vn` để đóng gói hook và story cho từng nhóm asset.
5. Viết asset theo vai trò kênh; không sao chép cùng caption, intro hay CTA placement.
6. Khi cần bản sản xuất chi tiết, dùng `mkt-create-script-short-video-v2-vn`, `mkt-create-script-storytelling-video`, `$mkt-caption-writer` và `$mkt-content-repurpose`.
7. Gán `content_id`, platform, pillar, stage, proof level, CTA, source pack và trạng thái duyệt.
8. Asset fail quality gate phải sửa hoặc giữ nháp; không publish chỉ để đủ số.

## Quality gate

- Một audience, một vấn đề và một take.
- Hook và body cùng lời hứa.
- Proof đúng cấp, đúng quyền công bố.
- Native với kênh và đúng brand voice.
- Một CTA có destination và tracking phù hợp.
- Có giá trị độc lập và đường sang asset tiếp theo khi cần.

## Đầu ra

1. Tóm tắt research pack.
2. Content tree và connective tissue.
3. Lịch theo kỳ và công suất đã duyệt.
4. Brief theo từng platform.
5. Production sheet có `content_id` và trạng thái.
6. Danh sách proof cần bổ sung và rủi ro claim.

Không tự phát hành hoặc ghi đè lịch nếu người dùng chỉ yêu cầu lập kế hoạch.
