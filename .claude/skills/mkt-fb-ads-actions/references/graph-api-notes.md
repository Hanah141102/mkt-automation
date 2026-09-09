# Ghi chú Graph API cho hành động Meta Ads qua Composio

- Phiên bản: `v23.0`. Endpoint cập nhật: `POST https://graph.facebook.com/v23.0/<object_id>`.
- Trường ghi được: `status` (`ACTIVE` | `PAUSED`), `daily_budget`, `lifetime_budget` (đơn vị nhỏ nhất tiền tệ), `name`.
- Không đổi `daily_budget` và `lifetime_budget` trên cùng ad set; ad set chạy lifetime budget thì chỉ đổi lifetime.
- Campaign dùng CBO (Advantage+ campaign budget): ngân sách nằm ở campaign, `daily_budget` của ad set không có tác dụng — dùng `METAADS_UPDATE_CAMPAIGN` hoặc proxy tới `<campaign_id>` với `daily_budget`.
- `effective_status` khác `status`: ad set có thể `ACTIVE` nhưng `effective_status=CAMPAIGN_PAUSED`. Đọc cả hai khi xác minh.
- Quyền cần có trên kết nối Composio: `ads_management` (ghi) ngoài `ads_read`.
- Mã lỗi thường gặp: 190 (token hết hạn → `composio link metaads`), 100 (tham số sai/đơn vị sai), 200 (thiếu quyền), 17/32 (rate limit → chờ 5 phút).
- Meta có thể mất tới vài phút để `effective_status` cập nhật; nếu đọc lại vẫn cũ, chờ 60 giây rồi đọc lại một lần.
