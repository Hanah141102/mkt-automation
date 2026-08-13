# _MOC 16. Xưởng Video AI

**27 skill** — dây chuyền sản xuất video bằng AI, xếp theo đúng thứ tự công đoạn.

> [!warning] Cần tài khoản trả phí
> Dây chuyền này dùng dịch vụ ngoài có tính phí: **HeyGen** (avatar), **ElevenLabs** hoặc **MiniMax** (giọng đọc), **Blotato** (đăng đa nền tảng). Chuẩn bị tài khoản và khoá API trước khi bật nhóm này.

## Đường đi của một video

```
Ý tưởng  →  Kịch bản  →  Giọng đọc  →  Avatar  →  Dựng hình  →  Đăng
  (1)        (nhóm 03)      (2)          (3)        (4)         (6)
                              └──────── hoặc dùng (5) trọn gói ────────┘
```

**Đi nhanh:** nếu chỉ cần một video, dùng thẳng nhóm **(5) Dây chuyền trọn gói** — một lệnh từ kịch bản ra file MP4. Các nhóm 1–4 dành cho khi cần can thiệp từng công đoạn.

**Kịch bản nằm ở nhóm khác:** `/video-script`, `/mkt-create-script-short-video-v2-vn`, `/mkt-create-script-storytelling-video` thuộc *03. Nội Dung & Sáng Tạo* — vì viết kịch bản là việc nội dung, không phải việc kỹ thuật.


### 1. Nghiên cứu & ý tưởng

| Skill | Mã gọi | Làm gì |
|---|---|---|
| [[Nghiên Cứu Chủ Đề YouTube]] | `/mkt-youtube-topic-researcher` | Nghiên cứu video YouTube theo chủ đề hoặc từ khoá, lọc theo lượt xem, số người đăng ký và tỷ lệ đột phá |
| [[Tìm Video Mới Từ Kênh Theo Dõi]] | `/mkt-youtube-trend-finder` | Lấy video mới nhất từ các kênh YouTube đang theo dõi để phát hiện xu hướng sớm |
| [[Phân Tích Video Bằng NotebookLM]] | `/mkt-phan-tich-video-notebooklm` | Phân tích video YouTube được lưu trong cơ sở dữ liệu bằng NotebookLM: tìm các mục chưa có liên kết, nạp video  |

### 2. Giọng đọc

| Skill | Mã gọi | Làm gì |
|---|---|---|
| [[Chuyển Văn Bản Thành Giọng Đọc]] | `/mkt-minimax-tts-to-mp3` | Chuyển văn bản tiếng Việt hoặc tiếng Anh thành file giọng đọc MP3 |

### 3. Avatar nói

| Skill | Mã gọi | Làm gì |
|---|---|---|
| [[Chuyển Kịch Bản Thành Video Avatar]] | `/mkt-heygen-script-to-mp4` | Chuyển thẳng kịch bản chữ thành video avatar nói khớp khẩu hình, hệ thống tự đọc rồi tự dựng |
| [[Chuyển Giọng Đọc Thành Video Avatar]] | `/mkt-heygen-mp3-to-mp4` | Chuyển một file giọng đọc MP3 thành video avatar nói khớp khẩu hình |
| [[Tạo Clip Avatar Ngắn]] | `/mkt-heygen-short-video` | Tạo các clip avatar nói từ kế hoạch sản xuất và file giọng đọc: cắt audio thành từng đoạn, dựng video khớp khẩ |

### 4. Dựng hình & hiệu ứng

| Skill | Mã gọi | Làm gì |
|---|---|---|
| [[Dựng Video Bằng HyperFrames]] | `/hyperframes` | Tạo bố cục video, hoạt ảnh, thẻ tiêu đề, lớp phủ, phụ đề, thuyết minh, hiệu ứng theo âm thanh và chuyển cảnh b |
| [[Dòng Lệnh HyperFrames]] | `/hyperframes-cli` | Bộ lệnh làm việc với HyperFrames: khởi tạo dự án, kiểm tra lỗi, xem trước, kết xuất video và chẩn đoán môi trư |
| [[Xử Lý Media Cho HyperFrames]] | `/hyperframes-media` | Tiền xử lý tài nguyên cho video HyperFrames: chuyển văn bản thành giọng đọc, bóc lời thoại từ audio hoặc video |
| [[Thư Viện Thành Phần HyperFrames]] | `/hyperframes-registry` | Cài đặt và ghép các khối, thành phần dựng sẵn vào dự án video HyperFrames |
| [[Dựng Video Ngắn Từ Clip Avatar]] | `/heygen-remotion-short-video-editor` | Ghép clip avatar, hình ảnh minh hoạ và hiệu ứng thành video ngắn hoàn chỉnh, tự động kết xuất ra file MP4. Dùn |
| [[Chuyển Remotion Sang HyperFrames]] | `/remotion-to-hyperframes` | Chuyển một dự án video Remotion sang định dạng HyperFrames |
| [[Biến Website Thành Video]] | `/website-to-hyperframes` | Chụp lại một website và tạo video giới thiệu từ đó |

### 5. Dây chuyền trọn gói

| Skill | Mã gọi | Làm gì |
|---|---|---|
| [[Dây Chuyền Video Dọc Trọn Gói]] | `/mkt-full-video-with-11-hyperframe-heygen` | Dây chuyền trọn gói làm video dọc 9:16 cho TikTok và Reels: từ kịch bản chữ, tự đọc thành giọng, dựng avatar n |
| [[Dây Chuyền Video Ngang Trọn Gói]] | `/mkt-full-video-with-11-hyperframe-heygen-16-9` | Dây chuyền trọn gói làm video ngang 16:9 kiểu podcast keynote: avatar nói cạnh slide động, từ kịch bản chữ ra  |
| [[Video Kiến Thức 16:9]] | `/mkt-hyperframe-knowledge-video` | Tạo video chia sẻ kiến thức 16:9 bằng slide động và giọng đọc tự động, khớp chữ với lời nói |
| [[Video Kiến Thức Có Avatar 16:9]] | `/mkt-hyperframe-knowledge-video-heygen-16-9` | Tạo video kiến thức 16:9 kiểu podcast keynote: slide động bên trái, avatar nói trong khung nổi bên phải, có ch |
| [[Video Kiến Thức Có Avatar 9:16]] | `/mkt-hyperframe-knowledge-video-heygen-9-16` | Tạo video kiến thức dọc 9:16 cho TikTok, Reels và Shorts: avatar nói toàn màn hình khi giảng, thu nhỏ xuống nử |
| [[Video Kiến Thức 9:16 Tiết Kiệm Credit]] | `/mkt-hyperframe-knowledge-video-heygen-9-16-lite` | Tạo video kiến thức dọc 9:16 với avatar chỉ xuất hiện ở phần mở, phần chuyển và lời kêu gọi để tiết kiệm khoản |
| [[Video Người Nói 9:16]] | `/mkt-hyperframe-talking-head-video` | Dựng video dọc 9:16 từ một clip quay sẵn có người nói: bóc lời thoại tiếng Việt, tự sửa lỗi nhận dạng và tạo p |
| [[Video Người Nói 16:9]] | `/mkt-hyperframe-talking-head-video-16-9` | Dựng video ngang 16:9 từ một clip quay sẵn có người nói: bóc lời thoại tiếng Việt, tạo phụ đề khớp lời và bố c |

### 6. Đăng & phân phối

| Skill | Mã gọi | Làm gì |
|---|---|---|
| [[Đăng Bài Đa Nền Tảng]] | `/mkt-blotato-publish-social` | Đăng nội dung (video, ảnh, chữ) lên nhiều nền tảng cùng lúc: Facebook, TikTok, Instagram, YouTube, Threads, X, |
| [[SEO YouTube]] | `/youtube-seo` | Tối ưu video YouTube cho tìm kiếm: tiêu đề, mô tả, thẻ, chương và khuyến nghị ảnh bìa |
| [[Ảnh Bìa YouTube]] | `/youtube-thumbnail` | Tạo ba phương án ảnh bìa YouTube tối ưu tỷ lệ nhấp: màu tương phản cao, biểu cảm gương mặt và chữ ngắn gọn trê |
| [[Chiến Lược Kênh YouTube]] | `/youtube-strategy` | Lập chiến lược kênh YouTube: trụ cột nội dung, lịch đăng, nguyên tắc ảnh bìa và các mốc tăng trưởng |
| [[Kịch Bản Quảng Cáo YouTube]] | `/youtube-ad-script` | Viết kịch bản quảng cáo YouTube cho các định dạng chèn đầu, chèn giữa và bumper, kèm câu móc, thông điệp và cá |