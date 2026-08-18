# Actor Apify Và Input Schema

Xác minh lần cuối: 2026-08-10. Luôn kiểm tra lại trang Input trước khi thay đổi production vì Actor có thể cập nhật schema và giá.

| Nền tảng | Actor ID | Input chính | Actor |
|---|---|---|---|
| Instagram | `apify/instagram-scraper` | `directUrls`, `resultsType`, `resultsLimit`, `onlyPostsNewerThan` | https://apify.com/apify/instagram-scraper/input-schema |
| Facebook | `apify/facebook-posts-scraper` | `startUrls`, `resultsLimit`, `captionText`, `onlyPostsNewerThan`, `onlyPostsOlderThan` | https://apify.com/apify/facebook-posts-scraper/input-schema |
| TikTok | `clockworks/tiktok-profile-scraper` | `profiles`, `profileScrapeSections`, `profileSorting`, `resultsPerPage`, `oldestPostDateUnified` | https://apify.com/clockworks/tiktok-profile-scraper/input-schema |
| YouTube | `streamers/youtube-channel-scraper` | `startUrls`, `maxResults`, `maxResultsShorts`, `maxResultStreams`, `oldestPostDate`, `sortVideosBy` | https://apify.com/streamers/youtube-channel-scraper/input-schema |

## Actor thay thế đã kiểm tra

| Nền tảng | Actor ID | Input chính | Giá tham khảo | Actor |
|---|---|---|---|---|
| Facebook | `api-ninja/facebook-pages-scraper` | `urls`, `type`, `maxResults`, `parseAllResults`, `startDate`, `endDate` | từ 5 USD/1.000 kết quả | https://apify.com/api-ninja/facebook-pages-scraper |
| Facebook | `khadinakbar/facebook-posts-scraper` | `startUrls`, `resultsLimit`, `maxPostsPerSource`, `scrapeDetails`, `fallbackProvider`, `onlyPostsNewerThan`, `proxyConfiguration` | 0,0035 USD/bài + 0,00005 USD/lượt | https://apify.com/khadinakbar/facebook-posts-scraper |

Actor Facebook thay thế chỉ được dùng qua `actor_overrides` khi người dùng chấp nhận. Với yêu cầu lấy bài gần đây, đặt `type: posts`, `parseAllResults: false`, giới hạn bằng `maxResults` và chuyển cửa sổ `N days` thành `startDate`/`endDate` theo UTC. Schema live yêu cầu `maxResults` tối thiểu là 20, kể cả khi giới hạn phân tích mong muốn thấp hơn.

`khadinakbar/facebook-posts-scraper` hỗ trợ Page lẫn Profile và dùng Residential Proxy cho HTML fallback. Giữ `scrapeDetails: false`, `includeRawHtml: false`, giới hạn đồng thời bằng `resultsLimit` và `maxPostsPerSource`, rồi chuyển cửa sổ `N days` thành ngày ISO cho `onlyPostsNewerThan`.

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
  "onlyPostsNewerThan": "30 days",
  "onlyPostsOlderThan": "2026-08-01T00:00:00Z"
}
```

`onlyPostsOlderThan` là tùy chọn. Chỉ đặt trường này khi cần chia một cửa sổ dài thành nhiều run không chồng lấn.

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
