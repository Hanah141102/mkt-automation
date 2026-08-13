---
skill: mkt-apify-competitor-social-analyzer
nhom: "04. Mạng Xã Hội & SEO"
type: huong-dan-skill
trang-thai: ban-nhap-review
cot-loi: true
---

# Research Content Từ Kênh Đối Thủ Bằng Apify

> [!abstract] Mục tiêu
> Thu thập dữ liệu công khai từ Facebook, Instagram, TikTok và YouTube của đối thủ; chuẩn hóa thành một bộ dữ liệu chung; sau đó tìm ra chủ đề, định dạng, nhịp đăng và nội dung nổi bật để hỗ trợ quyết định content.

> [!warning] Ranh giới
> Quy trình này giúp tìm **tín hiệu và mẫu hình**, không chứng minh nguyên nhân khiến một bài thành công. Không sao chép nội dung đối thủ và không coi view cao là bằng chứng duy nhất của chất lượng.

Mã skill: `/mkt-apify-competitor-social-analyzer`

## 1. Framework quy trình tổng quan

![[assets/Research Content Từ Kênh Đối Thủ — Framework Tổng Quan.png]]

### Workflow trực quan

![[assets/Research Content Từ Kênh Đối Thủ — Workflow Trực Quan.png]]

Đọc workflow từ trái sang phải:

```text
Chốt mục tiêu → Nhập đối thủ → Dry-run → Thu thập → Chuẩn hóa
→ Tìm pattern → Thử nghiệm content
```

Sáu lớp bên dưới mô tả **framework tư duy**. Workflow bảy bước tách riêng “chốt mục tiêu” và “nhập đối thủ”, đồng thời thêm bước “thử nghiệm” để biến insight thành hành động thực tế.

Framework gồm sáu lớp:

| Lớp | Câu hỏi cần trả lời | Đầu ra trung gian |
|---|---|---|
| 1. Mục tiêu | Nghiên cứu này phục vụ quyết định nào? | Một câu hỏi nghiên cứu rõ ràng |
| 2. Đầu vào | Phân tích ai, kênh nào và trong phạm vi nào? | Danh sách đối thủ và URL/handle hợp lệ |
| 3. Dry-run | Actor nào sẽ chạy, lấy bao nhiêu dữ liệu và có rủi ro chi phí gì? | `planned-runs.json` |
| 4. Thu thập | Apify trả về những bài đăng công khai nào? | Dataset gốc theo từng Actor run |
| 5. Chuẩn hóa | Làm sao so sánh dữ liệu khác cấu trúc giữa các nền tảng? | `normalized-data.json` |
| 6. Insight | Dữ liệu gợi ý quyết định content nào? | Benchmark, pattern, giả thuyết và hành động thử nghiệm |

Luồng tư duy bắt buộc:

```text
FACT → PATTERN → GIẢ THUYẾT → HÀNH ĐỘNG
```

- **Fact:** dữ liệu Actor thực sự trả về tại thời điểm chạy.
- **Pattern:** điều lặp lại ở nhiều bài, nhiều thời điểm hoặc nhiều đối thủ.
- **Giả thuyết:** cách giải thích có thể đúng nhưng chưa được kiểm chứng.
- **Hành động:** một thử nghiệm content cụ thể, không phải kết luận chung chung.

## 2. Input cần hỏi người dùng

![[assets/Research Content Từ Kênh Đối Thủ — Input Cần Hỏi.png]]

### 2.1. Năm nhóm input nghiệp vụ

| Nhóm | AI cần hỏi | Bắt buộc | Ví dụ câu trả lời tốt |
|---|---|:---:|---|
| Mục tiêu | “Anh/chị muốn dùng nghiên cứu này để quyết định điều gì?” | Có | Chọn ba chủ đề video cho tháng tới |
| Đối thủ | “Tên đối thủ là gì và vì sao chọn họ?” | Có | Hai đối thủ trực tiếp và một kênh đang chiếm sự chú ý của cùng khách hàng |
| Kênh | “Gửi URL hoặc handle công khai của từng kênh.” | Có | URL Facebook, Instagram, TikTok hoặc YouTube |
| Phạm vi | “Phân tích nền tảng nào, khoảng thời gian nào và tối đa bao nhiêu bài mỗi kênh?” | Có | YouTube và TikTok; dữ liệu gần đây; tối đa 10 bài/kênh |
| Đầu ra | “Muốn nhận benchmark, top bài, chủ đề, định dạng hay ý tưởng content?” | Có | Top bài + khoảng trống chủ đề + 10 hướng nội dung để thử |

### 2.2. Input kỹ thuật

| Trường | Quy tắc |
|---|---|
| `APIFY_TOKEN` | Đặt trong biến môi trường hoặc `.env` cục bộ; không dán token vào chat hoặc tài liệu |
| `max_posts` | Số nguyên từ 1–100; bắt đầu nhỏ rồi tăng khi thực sự cần |
| `newer_than` | Khoảng dữ liệu cần quan sát, ví dụ `30 days`; chọn theo câu hỏi nghiên cứu, không mặc định cho mọi dự án |
| `max_charge_usd` | Trần kỹ thuật cho mỗi Actor run khi client hỗ trợ; đơn vị Apify sử dụng là USD, đây không phải dự toán chi phí |
| `actor_overrides` | Chỉ dùng khi đã kiểm tra Actor thay thế và schema đầu vào tương ứng |

### 2.3. Khi nào chưa được chạy

Không chạy live nếu còn một trong các tình trạng sau:

- Chưa biết nghiên cứu để ra quyết định gì.
- Chỉ có tên đối thủ nhưng chưa có URL/handle kênh công khai.
- Người dùng chưa xác nhận phạm vi nền tảng và lượng dữ liệu.
- Chưa chạy dry-run để xem số Actor run dự kiến.
- `APIFY_TOKEN` chưa được cấu hình cục bộ.
- Dữ liệu cần truy cập tài khoản riêng tư hoặc cần đăng nhập.

### 2.4. Prompt thu thập input mẫu

```text
Hãy gửi cho tôi 5 nhóm thông tin:

1. Mục tiêu: nghiên cứu này giúp bạn quyết định điều gì?
2. Đối thủ: tên các đối thủ và lý do chọn họ.
3. Kênh: URL hoặc handle Facebook, Instagram, TikTok, YouTube của từng đối thủ.
4. Phạm vi: nền tảng cần phân tích, khoảng thời gian và số bài tối đa mỗi kênh.
5. Đầu ra: benchmark, top bài, chủ đề, định dạng hay ý tưởng content cần nhận.

Không gửi APIFY_TOKEN trong chat. Token phải được đặt trong môi trường cục bộ.
```

## 3. Chuẩn hóa input thành file cấu hình

Tạo một file JSON cho yêu cầu hiện tại:

```json
{
  "competitors": [
    {
      "name": "Đối thủ A",
      "channels": {
        "facebook": "https://www.facebook.com/example-a/",
        "instagram": "https://www.instagram.com/example-a/",
        "tiktok": "@example-a",
        "youtube": "https://www.youtube.com/@example-a"
      }
    },
    {
      "name": "Đối thủ B",
      "channels": {
        "youtube": "https://www.youtube.com/@example-b"
      }
    }
  ],
  "max_posts": 10,
  "newer_than": "30 days"
}
```

Quy tắc kiểm tra:

- Mỗi đối thủ phải có `name` và ít nhất một channel.
- Không lặp tên đối thủ.
- Chỉ dùng `facebook`, `instagram`, `tiktok`, `youtube`.
- Không thêm nền tảng mà script chưa hỗ trợ.
- Giữ nguyên URL nguồn để có thể truy vết dữ liệu.
- `30 days` và `10 bài` trong ví dụ chỉ là dữ liệu minh họa, không phải mặc định chiến lược.

## 4. Cách làm từng bước

### Bước 1 — Chốt câu hỏi nghiên cứu

Viết câu hỏi theo công thức:

```text
Trong [phạm vi thời gian], các đối thủ [danh sách] đang dùng
[chủ đề/định dạng/cách mở bài] nào tạo ra [tín hiệu cần quan sát],
và thương hiệu có thể thử điều gì mà không sao chép họ?
```

Ví dụ:

> Trong nhóm video YouTube gần đây, định dạng nào thường xuất hiện trong các bài có view và tương tác cao của ba đối thủ, và đâu là khoảng trống chủ đề thương hiệu có thể kiểm thử?

### Bước 2 — Kiểm tra dependency

```bash
SKILL_DIR=".agents/skills/mkt-apify-competitor-social-analyzer"
python3 "$SKILL_DIR/scripts/analyze_competitor_social.py" --check-deps
```

Script tự dùng virtualenv tại `workspace/.venvs/mkt-apify-competitor-social-analyzer` khi cần. Không cài đè Python hệ thống.

### Bước 3 — Chạy dry-run trước

```bash
SKILL_DIR=".agents/skills/mkt-apify-competitor-social-analyzer"
INPUT_FILE="/absolute/path/competitors.json"
OUTPUT_DIR="/absolute/path/apify-competitor-research"

python3 "$SKILL_DIR/scripts/analyze_competitor_social.py" \
  --input "$INPUT_FILE" \
  --output-dir "$OUTPUT_DIR" \
  --dry-run
```

Kiểm tra `planned-runs.json`:

- Đúng đối thủ và đúng nền tảng chưa?
- Actor ID có đúng với từng nền tảng không?
- Có run nào không cần thiết không?
- `resultsLimit`, `resultsPerPage` hoặc `maxResults` có đúng phạm vi không?
- Có bật tải video, cover hoặc comment sâu ngoài yêu cầu không?

### Bước 4 — Xác nhận phạm vi và chạy live

Chỉ chạy sau khi người dùng đã thấy số Actor run dự kiến và đồng ý phạm vi:

```bash
python3 "$SKILL_DIR/scripts/analyze_competitor_social.py" \
  --input "$INPUT_FILE" \
  --output-dir "$OUTPUT_DIR"
```

Mặc định script giới hạn tối đa 10 nội dung mỗi kênh nếu input không ghi giá trị khác, đồng thời đặt trần kỹ thuật `1 USD` cho mỗi run khi phiên bản Apify client hỗ trợ. Đây là cơ chế an toàn kỹ thuật, không phải cam kết chi phí thực tế.

### Bước 5 — Kiểm tra dữ liệu sau thu thập

Không đọc báo cáo ngay rồi kết luận. Kiểm tra trước:

1. Mỗi Actor run có dataset tương ứng.
2. Số record chuẩn hóa không vượt quá phạm vi đã duyệt một cách bất thường.
3. `competitor`, `platform`, `actor_id` và `target` có đủ để truy vết.
4. Field thiếu được giữ là `0`, rỗng hoặc “chưa có”, không được AI tự điền.
5. Link top post có mở đúng nội dung công khai.
6. Thời điểm thu thập đã được ghi trong `generated_at`.

### Bước 6 — Đọc benchmark đúng cách

Đọc theo ba tầng:

| Tầng | Đọc gì | Không được kết luận |
|---|---|---|
| Trong cùng một kênh | View, tương tác, ER/view, top bài, chủ đề lặp lại | View cao đồng nghĩa doanh thu cao |
| Giữa các đối thủ trên cùng nền tảng | Khác biệt chủ đề, định dạng, nhịp đăng và mức phân phối | Đối thủ ít follower là làm content kém |
| Chéo nền tảng | Vai trò từng nền tảng và cách tái sử dụng ý tưởng | So follower hoặc view như cùng một thước đo |

### Bước 7 — Chuyển dữ liệu thành hướng content

Với mỗi phát hiện, viết đủ bốn dòng:

```text
FACT: Bài nào, kênh nào, số liệu nào?
PATTERN: Điều gì lặp lại ở ít nhất một nhóm bài có thể so sánh?
GIẢ THUYẾT: Vì sao pattern này có thể hiệu quả với khán giả?
HÀNH ĐỘNG: Thương hiệu sẽ thử chủ đề/định dạng/hook nào và đo bằng gì?
```

Ưu tiên tìm:

- Chủ đề có nhu cầu rõ nhưng ít đối thủ giải thích sâu.
- Định dạng lặp lại trong nhiều bài nổi bật.
- Hook, góc nhìn hoặc cấu trúc dễ chuyển thành thử nghiệm riêng.
- Khoảng trống giữa câu hỏi khách hàng và nội dung đối thủ đang đăng.
- Nội dung có tương tác tốt nhưng chưa có CTA hoặc bước tiếp theo rõ.

Không làm:

- Chép tiêu đề, thumbnail, kịch bản hoặc quan điểm của đối thủ.
- Chỉ lấy một bài viral rồi gọi đó là xu hướng.
- Gộp dữ liệu Facebook, TikTok và YouTube vào một bảng xếp hạng tuyệt đối.
- Suy ra doanh thu, lead hoặc lợi nhuận nếu không có dữ liệu.

## 5. Kết quả nhận được

### 5.1. File do script tạo

| File | Vai trò |
|---|---|
| `planned-runs.json` | Kế hoạch Actor run khi chạy `--dry-run` |
| `raw/` | Dataset gốc của từng Actor live để truy vết |
| `normalized-data.json` | Dữ liệu chuẩn hóa, records, benchmark và top post |
| `competitor-social-report.md` | Báo cáo đọc nhanh theo đối thủ và nền tảng |

### 5.2. Kết quả nghiệp vụ cần tổng hợp thêm

Một research pack hoàn chỉnh nên có:

1. Câu hỏi nghiên cứu và phạm vi.
2. Danh sách đối thủ, kênh và thời điểm thu thập.
3. Bảng benchmark trong cùng từng nền tảng.
4. Top nội dung kèm link nguồn.
5. Ba đến năm pattern đáng chú ý.
6. Khoảng trống content có bằng chứng.
7. Danh sách giả thuyết cần kiểm thử.
8. Hành động content ưu tiên, người phụ trách và chỉ số đo.
9. Danh sách field thiếu hoặc giới hạn dữ liệu.

Khi lưu vào vault, đặt research pack tại:

```text
04. Resources/Market & Competitor Research/
```

Sau đó có thể dùng:

- `/mkt-kallaway-growth-topic-radar-vn` để xếp hạng chủ đề.
- `/mkt-kallaway-hook-story-engine-vn` để phát triển hook và góc kể riêng.
- `/mkt-caption-writer` để viết caption theo từng nền tảng.
- `/mkt-content-learning-loop` để đưa kết quả đăng thật quay lại vòng học.
- `/mkt-phan-tich-doi-thu` nếu cần mở rộng sang website, offer, review và vị thế cạnh tranh.

## 6. Checklist vận hành

### Trước khi chạy

- [ ] Có một quyết định content cụ thể cần hỗ trợ.
- [ ] Đã phân loại đối thủ trực tiếp, gián tiếp hoặc đối thủ nội dung.
- [ ] Có URL/handle công khai cho từng kênh.
- [ ] Người dùng đã xác nhận nền tảng, thời gian và số bài tối đa.
- [ ] `APIFY_TOKEN` được cấu hình cục bộ và không xuất hiện trong chat.
- [ ] Đã chạy `--check-deps` thành công.
- [ ] Đã chạy dry-run và kiểm tra `planned-runs.json`.
- [ ] Người dùng đã đồng ý phạm vi live run.

### Trong khi chạy

- [ ] Không mở rộng Actor hoặc lượng dữ liệu ngoài phạm vi đã duyệt.
- [ ] Không bật download video, transcript hoặc comment sâu mặc định.
- [ ] Không thu thập tài khoản riêng tư hoặc dữ liệu cá nhân nhạy cảm.
- [ ] Ghi lại Actor ID và lỗi của từng run.
- [ ] Nếu một kênh lỗi, báo rõ; không âm thầm bỏ qua.

### Sau khi chạy

- [ ] Có `normalized-data.json` và `competitor-social-report.md`.
- [ ] Có thể truy vết mỗi kết luận về đối thủ, nền tảng và link nguồn.
- [ ] Fact, pattern, giả thuyết và hành động được tách riêng.
- [ ] Không so sánh follower/view chéo nền tảng như cùng một chỉ số.
- [ ] Không bịa field mà Actor không trả về.
- [ ] Mỗi đề xuất content gắn với ít nhất một bằng chứng và một phép đo.
- [ ] Báo cáo ghi rõ đây là snapshot tại thời điểm chạy.
- [ ] Research pack được liên kết với dự án hoặc MOC liên quan, không thành note mồ côi.

## 7. Tiêu chí hoàn thành

Quy trình chỉ được xem là hoàn thành khi:

- Người đọc biết dữ liệu đến từ đâu và thu thập lúc nào.
- Người đọc phân biệt được số liệu thật với suy luận.
- Có ít nhất một quyết định content rõ ràng được hỗ trợ bởi dữ liệu.
- Có hành động thử nghiệm tiếp theo thay vì chỉ có báo cáo đẹp.
- Không phát sinh thu thập ngoài phạm vi hoặc chi phí ngoài kiểm soát.

## 8. Gọi skill nhanh

```text
Dùng /mkt-apify-competitor-social-analyzer để nghiên cứu content từ các kênh
đối thủ tôi cung cấp. Hãy hỏi đủ 5 nhóm input trước, chạy dry-run để tôi duyệt
phạm vi, sau đó mới chạy live. Kết quả phải tách Fact → Pattern → Giả thuyết
→ Hành động và không so sánh tuyệt đối giữa các nền tảng.
```

## Liên kết

[[_MOC 04. Mạng Xã Hội & SEO]] · [[Rà Soát Mạng Xã Hội]] · [[Phân Tích Đối Thủ]] · [[00 — Tôi Muốn Làm Gì]]
