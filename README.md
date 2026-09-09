---
title: Template Vận Hành Doanh Nghiệp — Marketing, Sales & Automation
cap-nhat: 2026-08-18
tags: [moc, huong-dan, skill, marketing-automation]
---

# Template Vận Hành Doanh Nghiệp — Marketing, Sales & Automation

Đây là **template mẫu giúp founder và đội ngũ vận hành doanh nghiệp từ Marketing đến Sales Automation** bằng AI Agent. Template kết hợp Business Context, hệ thống quản trị tri thức, quy trình chuẩn và thư viện skill chuyên môn để biến một yêu cầu kinh doanh thành đầu ra có thể triển khai, đo lường và cải tiến.

Template bao phủ toàn bộ hành trình:

`Business Context` → `Nghiên cứu & Chiến lược` → `Thương hiệu & Offer` → `Nội dung & Quảng cáo` → `Lead & Sales` → `CRM & Chăm sóc khách hàng` → `Đo lường & Tối ưu` → `Automation`

Người dùng có thể clone template, điền ngữ cảnh doanh nghiệp một lần, sau đó gọi các skill để thực hiện từng nghiệp vụ hoặc điều phối cả workflow nhiều bước. Mọi kết quả được lưu lại trong vault để đội ngũ và AI tiếp tục sử dụng, thay vì bắt đầu lại từ đầu ở mỗi cuộc hội thoại.

## Template này dành cho ai?

- Founder hoặc chủ doanh nghiệp muốn xây hệ thống Marketing–Sales có thể vận hành cùng AI.
- Đội Marketing, Sales và Customer Success cần dùng chung dữ liệu, quy trình và tiêu chuẩn bàn giao.
- Agency hoặc consultant muốn triển khai một bộ khung có thể nhân bản cho từng doanh nghiệp.
- Nhóm automation muốn nối chiến lược, nội dung, lead, CRM, báo cáo và các công cụ thực thi thành workflow hoàn chỉnh.

## Template giúp vận hành những gì?

| Lớp vận hành | Kết quả chính |
|---|---|
| **Nền tảng doanh nghiệp** | Mô hình kinh doanh, chân dung khách hàng, định vị, Brand Voice và mục tiêu |
| **Marketing** | Nghiên cứu thị trường, chiến lược, nội dung, SEO, social, quảng cáo và campaign |
| **Sales** | Offer, phễu, lead scoring, kịch bản tư vấn, xử lý từ chối và chốt đơn |
| **Customer Success** | Onboarding, CRM lifecycle, chăm sóc, giữ chân, tái mua và giới thiệu |
| **Đo lường** | KPI, tracking, attribution, dashboard, báo cáo và phân tích nguyên nhân gốc |
| **Automation** | SOP, workflow người–AI, email automation, tích hợp công cụ và pipeline xuất bản |
| **Quản trị tri thức** | Lưu quyết định, dữ liệu, bài học và tài sản tái sử dụng trong Obsidian PARA + AI Brain |

## Đào tạo và chuyển giao

📘 **[Giáo Án 5 Buổi Chuyển Giao](Giáo%20Án%205%20Buổi%20Chuyển%20Giao.md)** — giáo án cho lớp có người hướng dẫn ngồi cùng, mỗi buổi có cổng nghiệm thu:

| Buổi | Nội dung |
|:--:|---|
| 1 | Mô hình kinh doanh và tìm điểm nghẽn |
| 2 | Hệ thống marketing tự động — nghiên cứu, nội dung, xưởng video AI (HyperFrames + HeyGen) |
| 3 | Đo hiệu quả social, tạo quảng cáo và hành lang tự bật tắt |
| 4 | Nhân sự AI chăm khách Zalo — phần mềm Zalo CRM chạy trên desktop |
| 5 | Nhân sự AI đa kênh Facebook · WhatsApp · website và luồng giữ khách |

Chạy dài hơi hơn thì đi theo `huong dan/50. Triển Khai 90 Ngày/00 — Lộ Trình 8 Tuần.md`.

## Cách bắt đầu

1. Clone repo và mở thư mục này bằng Codex, Claude Code hoặc agent hỗ trợ `AGENTS.md`/`SKILL.md`.
2. Hoàn thiện `00. Business Context/` để AI hiểu đúng doanh nghiệp, khách hàng, offer và giọng thương hiệu.
3. Chọn category nghiệp vụ trong bảng bên dưới.
4. Gọi một skill đơn lẻ hoặc skill điều phối cho workflow nhiều bước.
5. Duyệt đầu ra quan trọng, lưu kết quả đúng nơi và dùng dữ liệu thực tế để tối ưu vòng tiếp theo.

> [!tip] Bắt đầu trong 30 giây
> Nếu Business Context đã hoàn chỉnh: chọn category → gọi tên skill → cung cấp dữ liệu nguồn → xác định đầu ra và nơi lưu → duyệt trước khi xuất bản, chạy quảng cáo hoặc dùng ngân sách.

## 1. Chọn category trước

Đây là bản đồ định tuyến nhanh. Các skill được liên kết là điểm bắt đầu tiêu biểu, không phải toàn bộ thư viện. Xem tất cả skill đang có tại [`.agents/skills/`](./.agents/skills/).

| Category | Dùng khi cần | Skill nên bắt đầu |
|---|---|---|
| **01. Chiến Lược & Điều Hành** | Chẩn đoán doanh nghiệp, chọn ưu tiên, lập chiến lược hoặc điều phối bài toán nhiều khâu | [`fullstack-marketing-operator`](./.agents/skills/fullstack-marketing-operator/SKILL.md) · [`chan-doan-nhanh`](./.agents/skills/chan-doan-nhanh/SKILL.md) · [`marketing-strategy-planner`](./.agents/skills/marketing-strategy-planner/SKILL.md) |
| **02. Thương Hiệu & Thiết Kế** | Định vị, giọng thương hiệu, nhận diện, tên gọi hoặc brief hình ảnh | [`brand-positioning-builder`](./.agents/skills/brand-positioning-builder/SKILL.md) · [`brand-voice-guide`](./.agents/skills/brand-voice-guide/SKILL.md) · [`visual-concept-builder`](./.agents/skills/visual-concept-builder/SKILL.md) |
| **03. Nội Dung & Sáng Tạo** | Lên trụ cột, ý tưởng, brief, viết bài, landing page hoặc kịch bản video | [`content-plan-builder`](./.agents/skills/content-plan-builder/SKILL.md) · [`content-copywriter`](./.agents/skills/content-copywriter/SKILL.md) · [`video-script`](./.agents/skills/video-script/SKILL.md) |
| **04. Mạng Xã Hội & SEO** | Lập lịch social, TikTok, Instagram, local SEO, keyword hoặc audit SEO | [`social-media-strategy`](./.agents/skills/social-media-strategy/SKILL.md) · [`social-media-calendar`](./.agents/skills/social-media-calendar/SKILL.md) · [`technical-seo-checklist`](./.agents/skills/technical-seo-checklist/SKILL.md) |
| **05. Quảng Cáo Trả Phí** | Lập chiến lược ads, tính ngân sách, viết quảng cáo, thiết kế test hoặc chẩn đoán hiệu suất | [`ads-strategy-planner`](./.agents/skills/ads-strategy-planner/SKILL.md) · [`ad-spend-calculator`](./.agents/skills/ad-spend-calculator/SKILL.md) · [`ads-performance-diagnostic`](./.agents/skills/ads-performance-diagnostic/SKILL.md) |
| **06. Email & Tự Động Hoá** | Welcome, nurture, launch, win-back, abandoned cart hoặc workflow email | [`email-sequence`](./.agents/skills/email-sequence/SKILL.md) · [`welcome-sequence`](./.agents/skills/welcome-sequence/SKILL.md) · [`automation-workflow`](./.agents/skills/automation-workflow/SKILL.md) |
| **07. Bán Hàng & Phễu** | Thiết kế offer, phễu, sales script, xử lý từ chối, báo giá hoặc chốt đơn | [`thiet-ke-offer`](./.agents/skills/thiet-ke-offer/SKILL.md) · [`sales-funnel-builder`](./.agents/skills/sales-funnel-builder/SKILL.md) · [`sales-script`](./.agents/skills/sales-script/SKILL.md) |
| **08. Chăm Sóc & Giữ Khách** | Onboarding, CRM, customer success, churn, khiếu nại hoặc hỗ trợ khách hàng | [`crm-lifecycle-builder`](./.agents/skills/crm-lifecycle-builder/SKILL.md) · [`customer-success-playbook`](./.agents/skills/customer-success-playbook/SKILL.md) · [`churn-prevention-playbook`](./.agents/skills/churn-prevention-playbook/SKILL.md) |
| **09. Sự Kiện & Ra Mắt** | Lên kế hoạch event, webinar, launch sản phẩm, trang đăng ký hoặc run of show | [`event-planner`](./.agents/skills/event-planner/SKILL.md) · [`product-launch-plan`](./.agents/skills/product-launch-plan/SKILL.md) · [`launch-checklist`](./.agents/skills/launch-checklist/SKILL.md) |
| **10. Đào Tạo & Sản Phẩm Số** | Xây khoá học, giáo án, workshop, cohort, ebook hoặc membership | [`course-outline`](./.agents/skills/course-outline/SKILL.md) · [`lesson-plan`](./.agents/skills/lesson-plan/SKILL.md) · [`workshop-builder`](./.agents/skills/workshop-builder/SKILL.md) |
| **11. Vận Hành & Công Nghệ** | SOP, automation, quản lý dự án, AI use case, knowledge base hoặc chọn tech stack | [`sop-builder`](./.agents/skills/sop-builder/SKILL.md) · [`process-automation-audit`](./.agents/skills/process-automation-audit/SKILL.md) · [`tech-stack-recommendation`](./.agents/skills/tech-stack-recommendation/SKILL.md) |
| **12. Nhân Sự** | Tuyển dụng, onboarding nhân viên, lương thưởng, đánh giá hiệu suất hoặc đào tạo | [`hiring-scorecard`](./.agents/skills/hiring-scorecard/SKILL.md) · [`onboarding-checklist`](./.agents/skills/onboarding-checklist/SKILL.md) · [`performance-review`](./.agents/skills/performance-review/SKILL.md) |
| **13. Tài Chính & Giá** | Định giá, dự báo doanh thu, cash flow, P&L, ROI hoặc điểm hoà vốn | [`pricing-analysis`](./.agents/skills/pricing-analysis/SKILL.md) · [`financial-projection`](./.agents/skills/financial-projection/SKILL.md) · [`unit-economics`](./.agents/skills/unit-economics/SKILL.md) |
| **14. Pháp Lý & Tuân Thủ** | Soạn hợp đồng, chính sách, điều khoản, NDA hoặc rà tuân thủ ngành tại Việt Nam | [`contract-writer`](./.agents/skills/contract-writer/SKILL.md) · [`privacy-policy`](./.agents/skills/privacy-policy/SKILL.md) · [`tuan-thu-nganh-vn`](./.agents/skills/tuan-thu-nganh-vn/SKILL.md) |
| **15. Dữ Liệu & Đo Lường** | Thiết kế KPI, tracking, attribution, cohort, dashboard, A/B test hoặc báo cáo | [`mkt-marketing-measurement-designer`](./.agents/skills/mkt-marketing-measurement-designer/SKILL.md) · [`do-luong-tracking`](./.agents/skills/do-luong-tracking/SKILL.md) · [`mkt-marketing-report-writer`](./.agents/skills/mkt-marketing-report-writer/SKILL.md) |
| **16. Nghiên Cứu Kênh & Đối Thủ** | Thu thập social, phân tích đối thủ, tìm chủ đề YouTube hoặc khai thác insight nội dung | [`mkt-apify-competitor-social-analyzer`](./.agents/skills/mkt-apify-competitor-social-analyzer/SKILL.md) · [`mkt-phan-tich-doi-thu`](./.agents/skills/mkt-phan-tich-doi-thu/SKILL.md) · [`mkt-youtube-topic-researcher`](./.agents/skills/mkt-youtube-topic-researcher/SKILL.md) |
| **17. Video AI & Media** | Tạo kịch bản, TTS, avatar, B-roll, storyboard, HyperFrames, render hoặc publish video | [`mkt-run-short-video-pipeline`](./.agents/skills/mkt-run-short-video-pipeline/SKILL.md) · [`mkt-hyperframe-knowledge-video-heygen-9-16-lite`](./.agents/skills/mkt-hyperframe-knowledge-video-heygen-9-16-lite/SKILL.md) · [`mkt-hyperframe-raw-mp4-editor-9-16`](./.agents/skills/mkt-hyperframe-raw-mp4-editor-9-16/SKILL.md) |
| **18. Web, App & Thanh Toán** | Dựng landing page, chatbot, i18n, auth, Supabase, SePay, Telegram hoặc deploy Vercel | [`biz-sales-page-layout`](./.agents/skills/biz-sales-page-layout/SKILL.md) · [`biz-nextjs-chatbot-openrouter`](./.agents/skills/biz-nextjs-chatbot-openrouter/SKILL.md) · [`biz-setup-sepay-payment`](./.agents/skills/biz-setup-sepay-payment/SKILL.md) |

Nếu yêu cầu chạm nhiều category hoặc chưa biết bắt đầu ở đâu, dùng [`fullstack-marketing-operator`](./.agents/skills/fullstack-marketing-operator/SKILL.md). Skill này chẩn đoán bài toán, chọn chuỗi skill tối thiểu và xác định điểm duyệt giữa các bước.

## 2. Cách gọi một skill

### Cách 1 — Gọi đích danh

Đây là cách rõ nhất và dễ kiểm soát nhất.

```text
Dùng skill content-copywriter để viết một bài Facebook về AI automation.
Đối tượng: chủ doanh nghiệp dịch vụ 5–20 nhân sự.
Mục tiêu: kéo người đọc đăng ký buổi tư vấn.
Đầu vào: [đường dẫn note/brief].
Giữ đúng Brand Voice và lưu bản nháp vào 01. Inbox/.
```

- Với Codex hoặc agent đọc `AGENTS.md`: viết `Dùng skill <tên-skill>...`; nếu giao diện hỗ trợ thì có thể dùng `$<tên-skill>`.
- Với Claude Code: gọi `/<tên-skill>` hoặc mô tả rõ tên skill trong yêu cầu.
- Tên skill chính là tên thư mục, viết lowercase-kebab-case, ví dụ `content-copywriter` hoặc `mkt-run-short-video-pipeline`.

### Cách 2 — Chỉ mô tả kết quả cần có

```text
Hãy phân tích vì sao quảng cáo Meta có nhiều click nhưng ít đơn,
dùng dữ liệu trong báo cáo tuần này và đề xuất ba thử nghiệm ưu tiên.
```

Agent sẽ tự chọn skill phù hợp. Nếu muốn kiểm soát quy trình, yêu cầu agent **nêu skill sẽ dùng và đầu ra của từng bước trước khi chạy**.

### Cách 3 — Gọi một workflow nhiều skill

```text
Dùng mkt-run-short-video-pipeline để biến video tham chiếu này thành video 9:16.
Chế độ review. Dừng để tôi duyệt ở idea, script và storyboard.
Chưa được publish nếu tôi chưa xác nhận kênh đích.
```

Với workflow nhiều bước, nên gọi skill điều phối thay vì tự gọi tất cả skill con cùng lúc. Skill điều phối sẽ giữ thứ tự phụ thuộc, trạng thái, validator và các cổng duyệt.

## 3. Mẫu prompt dùng chung

Copy mẫu này rồi điền phần còn thiếu:

```text
Dùng skill: <tên-skill>

Mục tiêu:
Đối tượng:
Đầu vào / nguồn dữ liệu:
Đầu ra mong muốn:
Kênh hoặc định dạng:
Ràng buộc về giọng, độ dài, ngân sách, deadline:
Điểm cần tôi duyệt:
Nơi lưu kết quả:
```

Một prompt tốt không cần dài, nhưng nên trả lời được bốn câu: **làm cho ai, để đạt gì, dựa trên dữ liệu nào và bàn giao ở đâu**.

## 4. Agent sẽ xử lý skill như thế nào

Khi một skill được gọi, agent phải:

1. Đọc toàn bộ file `.agents/skills/<tên-skill>/SKILL.md` hoặc file tương ứng trong `.claude/skills/`.
2. Đọc các reference, template hoặc script bắt buộc mà `SKILL.md` chỉ định.
3. Kiểm tra đầu vào; nêu rõ dữ kiện, giả định và phần còn thiếu.
4. Thực hiện đúng quy trình, chạy validator hoặc QA nếu skill có cung cấp.
5. Xin duyệt trước các quyết định chiến lược, ngân sách, giá, tuyên bố thương hiệu và thao tác xuất bản.
6. Bàn giao đầu ra, đường dẫn file và giới hạn còn lại.

Người dùng không cần tự đọc hết `SKILL.md`, nhưng nên cung cấp dữ liệu thật. Skill phân tích tài chính, quảng cáo, cohort, attribution hoặc hiệu suất sẽ không tự bịa số khi dữ liệu còn thiếu.

## 5. Các workflow thường dùng

### Hoàn thiện nền tảng doanh nghiệp

`mo-hinh-kinh-doanh` → `hoan-tat-business-context` → `chan-doan-nhanh` → `fullstack-marketing-operator`

### Xây chiến dịch marketing

`nghien-cuu-thi-truong` → `customer-persona` → `brand-positioning-builder` → `thiet-ke-offer` → `campaign-planner` → `mkt-marketing-measurement-designer`

### Làm hệ thống nội dung

`content-pillar-builder` → `content-plan-builder` → `content-ideation` → `content-copywriter` → `social-media-calendar` → `mkt-content-performance-optimizer`

### Chẩn đoán traffic có nhưng ít đơn

`conversion-funnel-analysis` → `mkt-marketing-root-cause` → `conversion-system-optimizer` → `offer-message-audit` → `thu-nghiem-ab`

### Sản xuất video ngắn hoàn chỉnh

`mkt-run-short-video-pipeline` điều phối: phân tích nguồn → phát triển idea → viết script → dựng video → QA → chuẩn bị phân phối. Publish chỉ được thực hiện khi người dùng xác nhận hành động và kênh đích.

### Vận hành hằng tuần

`ghi-cuoc-gap` sau cuộc gặp → `chuan-bi-hop-tuan` trước buổi họp → `weekly-report` cuối kỳ → `retrospective` cuối chiến dịch.

## 6. Chuẩn bị workspace và dữ liệu

### Nguồn skill theo runtime

Tại thời điểm cập nhật README này:

| Runtime | Thư mục | Số skill |
|---|---|---:|
| Codex và agent theo chuẩn `AGENTS.md` | `.agents/skills/` | 311 |
| Claude Code | `.claude/skills/` | 125 |
| Kho dự phòng | `huong dan/30. Thư Viện Skill/_Kho Skill/` | Chỉ bật khi cần |

Kiểm tra số lượng hiện tại bằng:

```bash
find .agents/skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l
find .claude/skills -mindepth 2 -maxdepth 2 -name SKILL.md | wc -l
```

Hai runtime có thể có số lượng và phiên bản skill khác nhau. Luôn dùng skill trong đúng thư mục mà agent hiện tại hỗ trợ.

### Nguồn ngữ cảnh cần đọc

- `AGENTS.md` — quy ước repo, code, bảo mật và cách làm việc.
- `CLAUDE.md` — quy tắc vault, ngôn ngữ, nguồn sự thật và nơi lưu đầu ra.
- `00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md` — bắt buộc trước thiết kế phễu hoặc khuyến nghị có ngưỡng thời gian.
- `00. Business Context/Chân Dung Doanh Nghiệp.md` và Brand Voice — đọc trước khi viết nội dung thương hiệu.

Xem hướng dẫn cài đặt đầy đủ tại [[Hướng Dẫn Agent Cài Đặt Skills và ENV]].

### API key và `.env`

Một số pipeline video, nghiên cứu hoặc publish cần API key. Tạo file local từ `.env.example`, chỉ điền biến thật sự cần và không bao giờ commit `.env`.

```bash
cp .env.example .env
chmod 600 .env
git check-ignore -v .env
```

## 7. Bản đồ vault

- [[_MOC 00. Business Context|00. Business Context]] — nguồn sự thật duy nhất về doanh nghiệp.
- [[_MOC 01. Inbox|01. Inbox]] — thông tin thô và bản nháp chưa phân loại.
- [[_MOC 02. Projects|02. Projects]] — chiến dịch và công việc có deadline.
- [[_MOC 03. Areas|03. Areas]] — trách nhiệm vận hành liên tục.
- [[_MOC 04. Resources|04. Resources]] — tài liệu, nghiên cứu và tài sản tái sử dụng.
- [[_MOC 05. Archive|05. Archive]] — việc đã đóng; lưu lịch sử thay vì xoá.
- [[_MOC Daily|Daily]] · [[_MOC Nhật Ký CEO|Nhật Ký CEO]] — nhật ký vận hành và chất liệu cá nhân.
- [[Vault SME — Hướng Dẫn]] — kiến trúc vault đầy đủ.

Xưởng video AI nằm trong `02. Projects/Xưởng Video AI/`. Nghiên cứu video nằm trong `04. Resources/Market & Competitor Research/Video AI/`. Hai đường dẫn `videos/` và `research/` ở root là liên kết tương thích cho các lệnh cũ.

## 8. Nguyên tắc an toàn

- Không bịa số liệu, benchmark, bằng chứng, feedback khách hàng hoặc kết quả chiến dịch.
- Không đưa dữ liệu riêng tư và dữ liệu khách hàng vào nội dung công khai nếu chưa được yêu cầu rõ ràng.
- Không publish, gửi email, chạy quảng cáo, thanh toán hoặc deploy production khi chưa có phạm vi và quyền phù hợp.
- Không commit `.env`, API key, credential, `workspace/`, media sinh ra, virtualenv hoặc `node_modules/`.
- Sau khi sửa HTML HyperFrames, luôn chạy `npm run check` trong đúng dự án trước khi bàn giao.
