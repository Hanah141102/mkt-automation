# Nghiên cứu: Dùng Claude Design/Claude Code để build website (video >20K views)

**Notebook NotebookLM:** https://notebooklm.google.com/notebook/b448841e-c4dd-4068-9d93-8b6e1fe138dc

## Nguồn video đã đưa vào NotebookLM (YouTube Data API, min 20K views, trong năm)

| # | Title | Kênh | Views | Ratio | URL |
|---|-------|------|-------|-------|-----|
| 1 | Claude Design = Easy Websites for Beginners | Kyle Skelly | 1.1M | 20.3x | youtu.be/rJtF32LTX8U |
| 2 | Introducing Claude Design by Anthropic Labs | Claude (official) | 856.5K | 1.7x | youtu.be/t_LBECIQQqs |
| 3 | Build $10,000 Websites using Claude Code (Ultimate Guide) | Metics Media | 831.6K | 1.3x | youtu.be/VMvZuhcDdnw |
| 4 | Building Beautiful Websites with Claude Code Is Too Easy | Nate Herk \| AI Automation | 519.9K | 0.6x | youtu.be/86HM0RUWhCk |
| 5 | Claude Design: Everything You Can Build in 16 Minutes (5 Real Use Cases) | Peter Yang | 392.6K | 3.9x | youtu.be/WMnk1LFBMqA |
| 6 | CLAUDE CODE FULL COURSE 4 HOURS: Build & Sell (2026) | Nick Saraev | 2.2M | 4.5x | youtu.be/QoQBzR1NIqI |
| 7 | I Tested Figma and Sketch for Website UI Design Here's What's BEST | Code with Me | 1.6M | 50.0x | youtu.be/yVXsS59LYJ0 |

Danh sách raw đầy đủ (nhiều video khác cùng chủ đề, đã lọc >20K views) nằm ở:
- `research/youtube/topics/claude-code-build-website/videos.json`
- `research/youtube/topics/claude-ai-web-design/videos.json`
- `research/youtube/topics/claude-design-website-tutorial/videos.json`

---

## PHƯƠNG PHÁP tổng hợp từ NotebookLM (phân tích 5 video có trích dẫn nhiều nhất)

### 1. Chuẩn bị prompt & brief hiệu quả
- **Trực quan hóa bằng ảnh tham chiếu** thay vì mô tả bằng lời: chụp screenshot các site truyền cảm hứng từ Dribbble, Awwwards, Godly.website, Pinterest. Mẹo: F12 → Console → full-size screenshot, copy luôn CSS của trang tham chiếu rồi dán cùng ảnh vào Claude để nó học bố cục/font/màu.
- **Prompt pattern "Ask me clarifying questions"**: luôn kết câu brief bằng "Hãy hỏi tôi các câu hỏi để làm rõ yêu cầu" — Claude sẽ hỏi ngược về phong cách, khách hàng mục tiêu, công nghệ, mức độ chuyển động trước khi làm (Claude Design đã tích hợp sẵn bước này).
- **File `claude.md`** ở root project — "bộ não" system prompt Claude đọc trước mỗi phiên. Dùng lệnh `/init` để tự sinh. Giữ ngắn (200–500 dòng), không nhồi tài liệu API dài để tránh tốn token và giảm độ chính xác.
- **Brand assets**: thư mục `brand_assets/` (logo, brand guideline) + tag `@` trực tiếp trong IDE để Claude bám đúng nhận diện thương hiệu.

### 2. Quy trình từ ý tưởng → website hoàn chỉnh
1. **Wireframe & UI độ phân giải cao (Claude Design)** — kéo thả tạo nhanh, chọn biến thể ưng ý, nâng lên high-fidelity, tinh chỉnh màu/font trên toolbar.
2. **Tạo tài nguyên hình ảnh/video**: Midjourney/DALL·E cho ảnh; nhờ chính Claude viết prompt ảnh khớp phong cách dự án. Video nền: ảnh tĩnh → Veo 3.1/Luma tạo loop, upscale 4K (Astra/Topaz), nén tối ưu cho web.
3. **Hand off sang Claude Code**: khi hết hạn mức Claude Design hoặc cần code sâu, bấm "Hand off to Claude Code", copy lệnh vào terminal để kéo toàn bộ source về local.
4. **Vòng lặp kiểm thử trực quan tự động**: cấu hình Puppeteer qua `claude.md` để Claude tự chụp screenshot local server, so với ảnh gốc, tự sửa lỗi bố cục qua nhiều vòng lặp.
5. **Mobile responsive pass riêng biệt**: không để Claude tự co giao diện desktop — yêu cầu tối ưu riêng (ẩn phần thừa, thu gọn spacing, menu → hamburger).
6. **Micro-interactions & content polish**: đổi font mặc định "Inter" (dễ lộ AI) sang Geist/serif sang trọng; thêm hover, parallax theo cursor, hiệu ứng glow lag nhẹ; copywriting ngắn gọn, gợi cảm giác thay vì liệt kê tính từ kiểu AI.
7. **Deploy**: site tĩnh → zip nội dung *bên trong* thư mục dự án (không zip cả thư mục cha) → Hostinger; site động (React/Node/Supabase/Stripe) → GitHub → Vercel/Netlify/Cloudflare.

### 3. Pattern lặp lại giữa nhiều video
- **"AI làm 90%, người làm 10%"**: AI đưa bạn đến 80–90% kết quả trong vài phút; 10% còn lại (gu thẩm mỹ, spacing, vị trí ảnh, trải nghiệm thật) cần con người để tránh "AI slop".
- **Cài Design Skills nâng cao**: skill chính thức "Front End Design" của Anthropic + skill cộng đồng "UI UX Pro Max" (bảng màu, font pairing, style) qua NPM — ép Claude bỏ default xấu, hướng tới thiết kế táo bạo hơn.
- **21st.dev**: kho component (buttons, scroll effects, shaders) do dev thật viết — copy prompt của component rồi dán vào Claude Code thay vì bắt AI tự viết từ đầu (dễ lỗi).
- **Quản lý context chủ động**: `/context` để xem dung lượng, `/compact` để nén lịch sử chat dài, giữ Claude "tỉnh táo" và tiết kiệm chi phí.

### 4. Sai lầm cần tránh
- Đưa app "vibe-coded" (có login, Stripe...) lên production mà không có dev thật kiểm tra bảo mật — rất dễ dính lỗ hổng, prompt injection, rò rỉ DB.
- Nhồi tài liệu API/style guide khổng lồ vào `claude.md` — tốn token mỗi lần chat, giảm độ chính xác do "quên" giữa ngữ cảnh; nên tách thành file Skill/Rule riêng, load theo yêu cầu.
- Để Puppeteer tự chụp so sánh với component có animation/canvas động — dễ chụp nhầm ảnh mờ và khiến Claude ghi đè code tốt thành hỏng; cần dặn rõ "đây là thành phần chuyển động, đừng dùng screenshot để so sánh".
- Bật "Bypass Permissions" mà không giám sát — tăng tốc độ nhưng có rủi ro chạy nhầm lệnh phá hoại hoặc sinh rác file; luôn ngồi cạnh máy khi bật.

### 5. Ứng dụng kiếm tiền thực tế
- **Nhận thầu website cao cấp ($10K)**: code tùy chỉnh hoàn toàn thay vì template Wix/Squarespace, chi phí vận hành cực thấp (~$20/tháng Claude Pro + ~$43/năm hosting/domain).
- **Lead magnet tự động**: dùng custom skill cào danh sách leads (vd phòng khám nha khoa kèm SĐT/địa chỉ) → chạy subagents song song tự tạo mockup website cá nhân hóa cho từng lead trong ~30s → gửi mockup làm mồi chào hàng thiết kế web, tạo hàng ngàn mockup trong vài giờ.
- **SaaS/internal tools nhanh**: hệ thống báo giá tích hợp Stripe + chữ ký điện tử (kiểu PandaDoc), bot phân loại email/gửi welcome email tự động — không cần thuê team dev riêng.

---

*Nguồn: NotebookLM phân tích trực tiếp 5/7 video (2 video còn lại — Nick Saraev 4h course và Code with Me Figma/Sketch — đã được thêm vào notebook nhưng chưa được trích dẫn trong câu trả lời này; có thể hỏi thêm NotebookLM để khai thác riêng nếu cần).*
