---
name: mkt-apify-competitor-social-analyzer
description: Thu thập và so sánh kênh mạng xã hội công khai của đối thủ bằng Apify trên Facebook, Instagram, TikTok và YouTube. Dùng khi cần lấy bài đăng gần đây, lượt xem, thích, bình luận, chia sẻ, nhịp đăng, định dạng nổi bật, chủ đề nội dung và top bài để lập benchmark đối thủ có bằng chứng.
---

# MKT Apify Competitor Social Analyzer

Nhận danh sách đối thủ và URL/handle social, chạy Actor Apify theo từng kênh, chuẩn hóa dữ liệu rồi tạo báo cáo Markdown cùng JSON gốc. Chỉ thu thập dữ liệu công khai.

## Đầu vào

Tạo JSON theo mẫu:

```json
{
  "competitors": [
    {
      "name": "Đối thủ A",
      "channels": {
        "facebook": "https://www.facebook.com/example/",
        "instagram": "https://www.instagram.com/example/",
        "tiktok": "@example",
        "youtube": "https://www.youtube.com/@example"
      }
    }
  ],
  "max_posts": 10,
  "newer_than": "30 days"
}
```

Chấp nhận thiếu một hoặc nhiều nền tảng. Không chạy Actor cho kênh không được cung cấp.

## Chuẩn bị

1. Kiểm tra `APIFY_TOKEN` trong process hoặc `.env` ở workspace.
2. Kiểm tra dependency. Script tự tạo virtualenv local tại `workspace/.venvs/mkt-apify-competitor-social-analyzer`, cài `apify-client` và tự chạy lại; không sửa Python hệ thống:

```bash
python3 scripts/analyze_competitor_social.py --check-deps
```

3. Nếu thiếu token, dừng trước khi phát sinh chi phí và hướng dẫn người dùng thêm:

```text
APIFY_TOKEN=apify_api_...
```

Không in token ra log hoặc báo cáo.

## Chạy

Đọc [actors.md](references/actors.md) trước khi sửa Actor ID hoặc input schema.

Kiểm tra kế hoạch miễn phí trước:

```bash
python3 scripts/analyze_competitor_social.py \
  --input /absolute/path/competitors.json \
  --output-dir /absolute/path/output \
  --dry-run
```

Chạy live sau khi người dùng chấp nhận phạm vi và giới hạn:

```bash
python3 scripts/analyze_competitor_social.py \
  --input /absolute/path/competitors.json \
  --output-dir /absolute/path/output
```

Mặc định lấy tối đa 10 nội dung cho mỗi kênh và đặt trần chi phí 1 USD cho mỗi Actor run khi phiên bản client hỗ trợ. Bắt đầu với giới hạn thấp; chỉ tăng khi người dùng yêu cầu.

## Đầu ra

Script tạo:

- `normalized-data.json`: dữ liệu chuẩn hóa và thống kê.
- `competitor-social-report.md`: bảng benchmark, top nội dung và chủ đề thường gặp.
- `raw/`: dataset gốc của từng Actor live.
- `planned-runs.json`: chỉ có trong `--dry-run`.

Phân biệt rõ:

- **Fact:** số liệu lấy từ dataset tại thời điểm chạy.
- **Suy luận:** lý do một format hoặc chủ đề có thể hiệu quả.
- **Thiếu dữ liệu:** field nền tảng hoặc Actor không trả về; không điền số giả.

Khi lưu vào vault, ưu tiên `04. Resources/Market & Competitor Research/` và tạo wikilink tới đối thủ hoặc dự án liên quan.

## Quy tắc

- Chỉ scrape trang, profile và nội dung công khai.
- Không thu thập dữ liệu cá nhân nhạy cảm, tài khoản riêng tư hoặc nội dung cần đăng nhập.
- Không bật tải video, transcript hoặc comment sâu mặc định vì tăng chi phí.
- Không so trực tiếp follower giữa các nền tảng như cùng một chỉ số.
- Ghi rõ thời điểm thu thập và Actor ID để báo cáo có thể tái lập.
- Nếu Actor đổi schema, chạy `--dry-run`, kiểm tra trang Input chính thức rồi cập nhật [actors.md](references/actors.md) và script cùng lúc.

## Test không tốn phí

Chạy mock fixture để kiểm tra toàn bộ pipeline chuẩn hóa và báo cáo mà không gọi Apify:

```bash
python3 scripts/analyze_competitor_social.py \
  --input /absolute/path/competitors.json \
  --output-dir /absolute/path/output \
  --mock-data /absolute/path/mock-data.json
```
