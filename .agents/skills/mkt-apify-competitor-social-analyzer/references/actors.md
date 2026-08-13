# Actor Apify Và Input Schema

Xác minh lần cuối: 2026-08-10. Luôn kiểm tra lại trang Input trước khi thay đổi production vì Actor có thể cập nhật schema và giá.

| Nền tảng | Actor ID | Input chính | Actor |
|---|---|---|---|
| Instagram | `apify/instagram-scraper` | `directUrls`, `resultsType`, `resultsLimit`, `onlyPostsNewerThan` | https://apify.com/apify/instagram-scraper/input-schema |
| Facebook | `apify/facebook-posts-scraper` | `startUrls`, `resultsLimit`, `captionText`, `onlyPostsNewerThan` | https://apify.com/apify/facebook-posts-scraper/input-schema |
| TikTok | `clockworks/tiktok-profile-scraper` | `profiles`, `profileScrapeSections`, `profileSorting`, `resultsPerPage`, `oldestPostDateUnified` | https://apify.com/clockworks/tiktok-profile-scraper/input-schema |
| YouTube | `streamers/youtube-channel-scraper` | `startUrls`, `maxResults`, `maxResultsShorts`, `maxResultStreams`, `oldestPostDate`, `sortVideosBy` | https://apify.com/streamers/youtube-channel-scraper/input-schema |

## Input mặc định

### Instagram

```json
{
  "directUrls": ["https://www.instagram.com/example/"],
  "resultsType": "posts",
  "resultsLimit": 10,
  "onlyPostsNewerThan": "30 days",
  "addParentData": true
}
```

### Facebook

```json
{
  "startUrls": [{"url": "https://www.facebook.com/example/"}],
  "resultsLimit": 10,
  "captionText": false,
  "onlyPostsNewerThan": "30 days"
}
```

### TikTok

```json
{
  "profiles": ["example"],
  "profileScrapeSections": ["videos"],
  "profileSorting": "latest",
  "resultsPerPage": 10,
  "oldestPostDateUnified": "30 days",
  "excludePinnedPosts": false,
  "shouldDownloadVideos": false,
  "shouldDownloadCovers": false,
  "commentsPerPost": 0
}
```

### YouTube

```json
{
  "startUrls": [{"url": "https://www.youtube.com/@example"}],
  "maxResults": 10,
  "maxResultsShorts": 0,
  "maxResultStreams": 0,
  "oldestPostDate": "30 days",
  "sortVideosBy": "NEWEST"
}
```

## Chính sách chọn Actor

- Ưu tiên Actor do Apify hoặc đội được Apify duy trì.
- Không tự chuyển sang Actor cộng đồng chỉ vì run lỗi; schema, giá và dữ liệu có thể khác.
- Cho phép override bằng `actor_overrides` trong config sau khi người dùng chấp nhận Actor thay thế.
- Giữ `max_posts` thấp trong lần chạy đầu để kiểm tra chất lượng và chi phí.
