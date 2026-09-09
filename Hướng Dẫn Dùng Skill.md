---
type: huong-dan
cap-nhat: 2026-08-06
tags: [huong-dan, skill]
---

# Hướng Dẫn Dùng Skill — 97 Skill Đang Bật

> Liên quan: [[Vault SME — Hướng Dẫn]] · [[Hồ Sơ Mô Hình Kinh Doanh]]

Cách gọi: gõ `/tên-skill` (ví dụ `/thiet-ke-offer`), **hoặc** chỉ cần mô tả việc muốn làm bằng tiếng Việt — Claude tự chọn skill. Không nhớ nên dùng gì thì gọi `/fullstack-marketing-operator`, skill này điều phối và chỉ sang skill đúng.

---

## 1. Đọc trước khi làm gì cả

Mọi skill đều lấy ngữ cảnh từ `00. Business Context/`. Hiện trạng vault này:

| Đã có | Còn thiếu |
|---|---|
| Hồ Sơ Mô Hình Kinh Doanh (6 tham số) | Chân Dung Doanh Nghiệp |
| Business Model Canvas + sơ đồ | Brand Voice — Giọng Thương Hiệu |
| 4 phân khúc khách (PK1–PK4) | Sản Phẩm & Dịch Vụ (hồ sơ từng gói + giá) |
| 4 giá trị cốt lõi (GT1–GT4) | Chân Dung CEO · AI-Sale-Assistant |

**Ba việc nên làm trước tiên:**

1. **Xác nhận 6 tham số** trong `Hồ Sơ Mô Hình Kinh Doanh.md` — file đang ở trạng thái `cho-xac-nhan`, giá trị do AI đề xuất. `chu-ky-ban-ngay: 60` đang là ước lượng gộp. Con số này điều khiển mọi ngưỡng thời gian của toàn hệ thống (giữ lead 90 ngày, nhắc sau báo giá ngày 3–9–18, đọc số hai tuần một lần). Sai ở đây thì hàng chục khuyến nghị phía sau sai theo.
2. Chạy `/hoan-tat-business-context` để bịt bốn hồ sơ còn thiếu ở cột phải.
3. Chạy `/chan-doan-nhanh` — 12 câu hỏi, chấm điểm 12 bước, chỉ ra 2–3 chỗ yếu nhất nên làm trước. Đây là cách chọn skill đúng thay vì đọc hết 97 cái.

---

## 2. Bản đồ 97 skill theo nhóm

### A. Vận hành vault & điều phối (8)

| Skill | Làm được gì |
|---|---|
| `/mo-hinh-kinh-doanh` | Phỏng vấn 9 ô mô hình kinh doanh, tự sinh toàn bộ file Business Context + sơ đồ, hỏi 6 tham số, rồi vẽ bản đồ nên đưa AI vào điểm nào trong Sale & Marketing |
| `/ban-do-ai-sale-mkt` | Chạy riêng phần bản đồ AI Sale & Marketing khi MHKD đã có: phỏng vấn quy trình thật, chấm điểm, đề xuất hệ thống agent theo 3 tầng |
| `/hoan-tat-business-context` | Quét chỗ còn thiếu trong `00. Business Context/`, hỏi để điền nốt |
| `/chan-doan-nhanh` | Chấm điểm 12 bước, chỉ ra bước yếu nhất — dùng ở buổi đầu tiên |
| `/kiem-tra-cong` | Chấm cổng "Xong" của một bước bằng bằng chứng thật trong vault, chỉ rõ thiếu file nào |
| `/ghi-cuoc-gap` | **Dùng nhiều nhất.** Kể lại cuộc gặp bằng lời, tự tạo biên bản + cập nhật hồ sơ khách + chuyển pipeline + lưu câu khách nói |
| `/chuan-bi-hop-tuan` | Đọc số kỳ vừa rồi, sinh nghị trình họp cụ thể thay vì mẫu chung |
| `/fullstack-marketing-operator` | Điều phối việc nhiều khâu, sắp thứ tự skill, kiểm tra tính nhất quán |
| `/viet-hoa-skill` | Dịch SKILL.md tiếng Anh sang tiếng Việt, giữ nguyên cấu trúc |

### B. Nghiên cứu & chiến lược (10)

| Skill | Làm được gì |
|---|---|
| `/nghien-cuu-thi-truong` | Đo cầu thật cho sản phẩm số/dịch vụ tại VN, chấm điểm ngách 100, khuyến nghị làm hay không |
| `/mkt-phan-tich-doi-thu` | Phân tích đối thủ chỉ bằng dữ liệu công khai, không cần công cụ trả phí |
| `/seo-competitor-analysis` | Từ khoá trùng lặp, khoảng trống nội dung, backlink, so thứ hạng |
| `/brand-positioning-builder` | Định vị: cho ai, khác gì, hứa gì, tin được vì sao |
| `/customer-persona` | Chân dung khách chi tiết — nhân khẩu, tâm lý, hành vi mua |
| `/customer-journey-map` | Hành trình từ chưa biết tới giới thiệu, chỉ ra chỗ rơi rớt |
| `/voice-of-customer` | Chương trình lắng nghe khách, khung phân tích insight |
| `/win-loss-analysis` | Vì sao thắng, vì sao mất thương vụ |
| `/swot-analysis` | SWOT có đối chiếu chéo, ra hành động cụ thể |
| `/decision-matrix` | Ma trận quyết định có trọng số — chọn kênh, vendor, sản phẩm ưu tiên |

### C. Offer & giá (8)

| Skill | Làm được gì |
|---|---|
| `/thiet-ke-offer` | Xếp chồng giá trị, bonus, bảo đảm, cấp thiết, đặt tên gói, cấu trúc thanh toán |
| `/offer-message-audit` | Chấm độ rõ / phù hợp / khác biệt / đáng tin của offer trước khi tung |
| `/pricing-strategy` | Định giá lần đầu hoặc chuẩn bị tăng giá |
| `/bundle-creator` | Combo + biên lợi nhuận + câu chữ bán |
| `/tripwire-offer` | Offer mồi giá thấp, lộ trình bán lên gói cao |
| `/service-guarantee` | Cam kết dịch vụ, điều khoản loại trừ, quy trình bồi hoàn |
| `/unit-economics` | Biên đóng góp, thời gian hoàn vốn, LTV/CAC |
| `/breakeven-analysis` | Điểm hoà vốn, mô phỏng kịch bản |

### D. Nội dung & thương hiệu (12)

| Skill | Làm được gì |
|---|---|
| `/brand-voice-guide` | Cẩm nang giọng: thuộc tính, từ nên/tránh, điều chỉnh theo kênh |
| `/content-pillar-builder` | Trụ cột nội dung có vai trò, tỷ trọng, chỉ số |
| `/content-ideation` | Ngân hàng ý tưởng bám trụ cột |
| `/content-plan-builder` | Kế hoạch đa kênh: nhịp, phụ thuộc, người làm, cách đo |
| `/content-copywriter` | Viết & biên tập theo nấc nhận thức và yêu cầu từng kênh |
| `/blog-post` | Bài blog dài chuẩn SEO, duyệt dàn ý trước |
| `/mkt-caption-writer` | Caption theo từng nền tảng, kèm CTA + hashtag |
| `/hook-generator` | Câu mở đầu chặn ngón tay lướt, nhiều phương án |
| `/video-script` | Kịch bản quay được ngay: móc, phân đoạn, chữ màn hình, danh sách cảnh |
| `/social-media-calendar` | Lịch đăng riêng từng nền tảng, khung giờ tốt |
| `/mkt-content-repurpose` | Một nội dung gốc → nhiều định dạng sẵn đăng |
| `/lead-magnet` | Mồi thu lead + landing page quảng bá |

### E. Phễu & trang chuyển đổi (6)

| Skill | Làm được gì |
|---|---|
| `/sales-funnel-builder` | Vẽ toàn bộ phễu: giai đoạn, điểm chuyển đổi, nội dung tương ứng |
| `/conversion-funnel-analysis` | Tìm chỗ rơi rớt, xếp thứ tự tối ưu, mức so chuẩn |
| `/conversion-system-optimizer` | Rà landing page, form, CTA, điểm bàn giao sang sale |
| `/landing-page-copy` | Nội dung landing hướng chuyển đổi |
| `/sales-page` | Trang bán dài theo khung Vấn đề – Khoét sâu – Giải pháp |
| `/email-sequence` | Chuỗi email tự động: khoảng cách, trigger, tiêu đề A/B |

### F. Quảng cáo trả phí (9)

| Skill | Làm được gì |
|---|---|
| `/ads-strategy-planner` | Vai trò quảng cáo, cấu trúc phễu, phân bổ ngân sách, nguyên tắc quyết định |
| `/ad-spend-calculator` | Từ mục tiêu doanh thu ngược ra ngân sách cần chi |
| `/media-buy-plan` | Phân bổ ngân sách đa kênh, ROAS kỳ vọng, lộ trình thử |
| `/ads-copywriting` | Bộ nội dung quảng cáo theo tầng phễu + giả thuyết thử nghiệm |
| `/ads-testing-designer` | Ma trận thử nghiệm có biến kiểm soát và quy tắc quyết định |
| `/ads-performance-diagnostic` | Chẩn đoán nghẽn từ phân phối tới doanh thu |
| `/facebook-ad-campaign` | Chiến dịch Meta: nhắm đối tượng, brief creative, ngân sách |
| `/google-ads-campaign` | Chiến dịch Search: nhóm từ khoá, câu chữ, đấu giá |
| `/retargeting-strategy` | Chia nhóm tiếp thị lại, thông điệp theo tầng, giới hạn tần suất |

### G. Bán hàng & chốt đơn (9)

| Skill | Làm được gì |
|---|---|
| `/phan-bo-va-cham-diem-lead` | Chấm lead nóng lạnh, luật chia lead, thời hạn liên hệ, chống tranh khách |
| `/discovery-call-script` | Khung buổi tư vấn đầu: sàng lọc, khai thác đau, chốt bước tiếp |
| `/sales-script` | Kịch bản gọi điện / video call / tin nhắn |
| `/chot-don-qua-zalo` | Kịch bản Zalo: mở lời, khai thác, báo giá, xử lý im lặng, nhịp nhắc |
| `/chot-don-qua-inbox` | Kịch bản inbox FB/IG/TikTok Shop, kéo bình luận về inbox, bàn giao ca |
| `/objection-handler` | Sổ tay xử lý từ chối theo nhóm phản đối |
| `/sales-battlecard` | Bảng đấu khi cạnh tranh trực tiếp với một đối thủ cụ thể |
| `/proposal-writer` | Đề xuất dự án chỉn chu cho khách lớn |
| `/quan-ly-doi-sale` | Chỉ số từng người, nhịp họp, chấm chất lượng cuộc gọi, kèm người mới |

### H. Giữ khách & doanh thu lặp lại (12)

| Skill | Làm được gì |
|---|---|
| `/crm-lifecycle-builder` | Thiết kế CRM + vòng đời: dữ liệu, phân nhóm, trạng thái, luồng chăm sóc |
| `/onboarding-flow` | Luồng đón khách mới, mốc kích hoạt, điểm kiểm tra |
| `/customer-success-playbook` | Nhịp chạm sau bán và nhận diện cơ hội bán thêm |
| `/customer-health-score` | Chấm sức khoẻ khách, ngưỡng kích hoạt can thiệp |
| `/churn-prevention-playbook` | Cảnh báo sớm + chuỗi can thiệp giữ chân |
| `/win-back-campaign` | Kéo lại khách đã rời hoặc lâu không mua |
| `/nhac-mua-lai-theo-chu-ky` | Nhắc đúng lúc khách sắp hết hàng / tới kỳ tái quyết định |
| `/loyalty-program` | Hạng, tích điểm, đổi thưởng |
| `/referral-program` | Bậc thưởng, theo dõi, thông điệp giới thiệu |
| `/nps-survey` | Đo mức sẵn sàng giới thiệu + kế hoạch hành động theo nhóm |
| `/testimonial-collector` | Hệ thống xin chứng thực: email, nhắc lại, biểu mẫu, chỗ đặt |
| `/complaint-resolution` | Kịch bản đồng cảm, đường leo thang, phương án bù đắp |

### I. Đo lường, phân tích & báo cáo (9)

| Skill | Làm được gì |
|---|---|
| `/mkt-marketing-measurement-designer` | Thiết kế hệ đo **trước khi** phân tích: cây mục tiêu, KPI, công thức, ngưỡng |
| `/do-luong-tracking` | GA4, GTM, kế hoạch tracking, UTM — có mẫu sự kiện bấm gọi / Zalo / Messenger + lưu ý Nghị định 13/2023 |
| `/mkt-kpi-dashboard` | Bảng chỉ số, mục tiêu, trạng thái, xu hướng |
| `/attribution-model` | Kênh nào thật sự tạo ra đơn |
| `/mkt-marketing-performance-analysis` | Phân tích theo phễu, thời gian, phân khúc — tìm driver |
| `/mkt-marketing-root-cause` | Số xấu đi nhưng chưa biết vì đâu → lần tới điểm gãy thật |
| `/mkt-marketing-report-writer` | Báo cáo trả lời trước, có số, nguyên nhân, hành động, người chịu trách nhiệm |
| `/cohort-analysis` | Nhóm khách theo kỳ: giữ chân, doanh thu, hành vi theo thời gian |
| `/thu-nghiem-ab` | Giả thuyết, cỡ mẫu, ý nghĩa thống kê — có cảnh báo traffic tối thiểu |

### J. Vận hành nội bộ & tuân thủ (9)

| Skill | Làm được gì |
|---|---|
| `/sop-builder` | Phỏng vấn cách bạn đang làm → xuất quy trình người khác làm được |
| `/delegation-framework` | Ma trận trách nhiệm, mẫu bàn giao, theo dõi cam kết, leo thang |
| `/training-manual` | Cẩm nang đào tạo để người mới tự học |
| `/quality-assurance-checklist` | Tiêu chí đạt / không đạt, quy trình duyệt |
| `/process-automation-audit` | Nên tự động hoá khâu nào trước, công cụ gì |
| `/ai-use-case-finder` | Cơ hội đưa AI vào quy trình, khả thi và lợi ích |
| `/retrospective` | Rút kinh nghiệm sau chiến dịch (Bắt đầu/Dừng/Tiếp tục, 4L, Thuyền buồm) |
| `/ke-hoach-hang-hoa` | Nối marketing với tồn kho — chỉ dùng nếu bán hàng vật lý |
| `/tuan-thu-nganh-vn` | Rà rủi ro câu chữ quảng cáo theo ngành có quản lý (mỹ phẩm, TPCN, y tế, giáo dục, BĐS, tài chính) |

### K. Đào tạo & sự kiện (5)

| Skill | Làm được gì |
|---|---|
| `/course-outline` | Chương trình khoá học: mô-đun, bài học, mục tiêu, bài tập |
| `/lesson-plan` | Giáo án một buổi cụ thể |
| `/workshop-builder` | Nghị trình, bài tập, tài liệu phát, cẩm nang điều phối |
| `/webinar-planner` | Webinar trọn gói: dàn ý, slide, email quảng bá, trang đăng ký, theo đuôi |
| `/webinar-sales-script` | Kịch bản webinar bán hàng: dạy → chuyển → chào bán |

---

## 3. Bốn lộ trình thường dùng

**Mới mở vault, chưa có gì**
`/mo-hinh-kinh-doanh` → `/hoan-tat-business-context` → `/chan-doan-nhanh` → làm theo 2–3 bước yếu nhất nó chỉ ra.

**Ra mắt một sản phẩm hoặc gói dịch vụ mới**
`/nghien-cuu-thi-truong` → `/mkt-phan-tich-doi-thu` → `/thiet-ke-offer` → `/pricing-strategy` → `/unit-economics` → `/offer-message-audit` → `/sales-funnel-builder` → `/landing-page-copy` → `/ads-strategy-planner` → `/ad-spend-calculator` → `/do-luong-tracking`.

**Có traffic nhưng ít đơn**
`/conversion-funnel-analysis` → `/mkt-marketing-root-cause` → `/conversion-system-optimizer` → `/offer-message-audit` → `/thu-nghiem-ab`.

**Vận hành hằng tuần**
Sau mỗi lần gặp khách: `/ghi-cuoc-gap`. Trước mỗi buổi họp: `/chuan-bi-hop-tuan`. Cuối chiến dịch: `/mkt-marketing-report-writer` rồi `/retrospective`.

Với `chu-ky-ban-ngay: 60`, nhịp đọc số của công ty này là **hai tuần một lần**, không phải hằng tuần.

---

## 4. Bốn điều cần biết trước khi dùng

**Đang bật 97 skill — vượt ngưỡng khuyến nghị 60.** Mỗi skill bật lên chiếm bộ nhớ ngữ cảnh, bật quá nhiều làm Claude chậm và kém chính xác. Nhóm ít dùng nhất với mô hình hiện tại (B2B phần mềm, chu kỳ 60 ngày): `/ke-hoach-hang-hoa` (chỉ cho hàng vật lý), `/loyalty-program`, `/lesson-plan`, `/course-outline`, `/tripwire-offer`, `/bundle-creator`. Muốn tắt thì chuyển thư mục skill đó ra khỏi `.claude/skills/` rồi khởi động lại.

**Các thư mục ghi kết quả đã được tạo đủ.** `01. Inbox/`, `02. Projects/`, `03. Areas/`, `04. Resources/`, `05. Archive/`, `Daily/` và `Nhật Ký CEO/` đã sẵn sàng. Khi tạo note mới, đặt đúng thư mục theo bảng trong [[CLAUDE]].

**Có kho 301 skill dự phòng.** Kho nằm tại `huong dan/30. Thư Viện Skill/_Kho Skill/`; chỉ copy skill cần dùng vào `.claude/skills/`, không bật hàng loạt.

**Skill không bịa số.** Skill nào cần dữ liệu thật (`/cohort-analysis`, `/mkt-marketing-performance-analysis`, `/attribution-model`, `/unit-economics`) sẽ hỏi bạn con số. Chưa có dữ liệu thì nó ghi "chưa có dữ liệu" chứ không tự chế cho đẹp báo cáo.
