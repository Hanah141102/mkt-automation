# AI Business OS — Khoá Chuyển Giao & BIZ.MKT.OS

Hệ điều hành kinh doanh chạy bằng AI, đóng gói để chuyển giao cho doanh nghiệp — tích hợp sẵn **BIZ.MKT.OS** (Pipeline tự động hoá dựng Landing Page, Thanh toán VietQR & Sales Funnel toàn diện).

**Bắt đầu:** mở [`00. Bắt Đầu Từ Đây/00 — Bạn Đang Cầm Gì.md`](00.%20Bắt%20Đầu%20Từ%20Đây/00%20—%20Bạn%20Đang%20Cầm%20Gì.md)

---

## 📂 Cấu trúc thư mục hệ thống

| Thư mục | Nội dung & Vai trò | Quy mô |
|---|---|---|
| **00. Bắt Đầu Từ Đây** | Bạn đang cầm gì · thứ tự triển khai · quy trình vận hành team nhỏ · cẩm nang kiến trúc · demo CEO thực chiến · 3 ngành thử nghiệm + Kaizen | 6 tài liệu |
| **10. Hệ Điều Hành** | Vault Obsidian chuẩn hoá "cài là chạy", 35 skill bật sẵn, pipeline mẫu & hồ sơ khách hàng | ~17 MB |
| **20. Khung Vận Hành A-Z** | 12 bước từ định vị thương hiệu tới cải tiến liên tục, cổng kiểm soát chất lượng | 13 tài liệu |
| **30. Thư Viện Skill** | 282 trợ lý AI, 16 nhóm chức năng (marketing, sales, HR, xưởng video AI...), 100% tiếng Việt | ~7 MB |
| **40. Bài Mẫu — Công Ty Demo** | Doanh nghiệp mẫu đã dựng đủ hệ thống thực tế (dữ liệu hư cấu) | 49 tài liệu |
| **50. Triển Khai 90 Ngày** | Lộ trình 8 tuần, checklist nghiệm thu 40 mục, biên bản bàn giao | 3 tài liệu |
| 🚀 **[MKT.LANDINGPAGE.SKILLS-main](MKT.LANDINGPAGE.SKILLS-main)** | **BIZ.MKT.OS**: Pipeline 13+1 Skill dựng Landing Page, Thanh toán VietQR, Email, Admin CRM & Affiliate | Full Source & Docs |

---

## 🛠️ Chi tiết Module mới: BIZ.MKT.OS (Marketing & Sales Funnel)

Nằm tại thư mục [`MKT.LANDINGPAGE.SKILLS-main/`](MKT.LANDINGPAGE.SKILLS-main/), đây là bộ công cụ chuyên dụng đóng gói sản phẩm số từ **Ý tưởng → Landing Page Live → Nhận tiền thật qua VietQR**.

### 🌟 Pipeline 13 + 1 Skill chuyên biệt

1. `/market-research` — Nghiên cứu thị trường & validate nhu cầu (Niche Score /100).
2. `/biz-offer-alex-hormozi` — Đóng gói Grand Slam Offer & xuất `offer.json`.
3. `/biz-sales-page-copy` — Viết Sales Copy chốt đơn + A/B Testing Variants.
4. `/ui-ux-pro-max` — Thiết kế & lập trình Landing Page Next.js Production (Mobile-first).
5. `/biz-setup-sepay-payment` — Tích hợp VietQR (SePay) & lưu trữ Lead/Order (Supabase / KV).
6. `/biz-nextjs-chatbot-openrouter` — Dựng AI Chatbot widget hỗ trợ khách hàng 24/7.
7. `/biz-email-setup` — Hệ thống Email Auto-responder qua SMTP Nodemailer.
8. `/biz-telegram-payment-notify` — Báo đơn hàng đã thanh toán tức thì qua Telegram Bot.
9. `/biz-admin-leads-dashboard` — Trình quản trị CRM `/admin` trên Supabase.
10. `/biz-deploy-vercel` — Deploy 1-click lên Vercel Production.
11. `/biz-admin-google-auth` ⭐ — Bảo mật trang Admin với Google OAuth & Allowlist.
12. `/biz-affiliate-system` ⭐ — Hệ thống Affiliate (`?aff=`), portal đối tác, tính hoa hồng & leaderboard.
13. `/biz-i18n-landing-page` ⭐ — Đa ngôn ngữ cho Landing Page.

### 📐 Sơ đồ thuật toán & Kiến trúc kĩ thuật
- 📜 [`so-do-thuat-toan-landing-page-supabase.md`](MKT.LANDINGPAGE.SKILLS-main/so-do-thuat-toan-landing-page-supabase.md): Luồng xử lý Landing Page → VietQR Webhook → Supabase → Telegram Notify.
- 📜 [`so-do-thuat-toan-affiliate.md`](MKT.LANDINGPAGE.SKILLS-main/so-do-thuat-toan-affiliate.md): Luồng theo dõi chuyển đổi & đối soát hoa hồng Affiliate.
- 📜 [`so-do-thuat-toan-revit-license-supabase.md`](MKT.LANDINGPAGE.SKILLS-main/so-do-thuat-toan-revit-license-supabase.md): Sơ đồ quản lý bản quyền phần mềm (Add-in Revit & Web Admin License).

---

## 💡 Các lớp vận hành — Đừng lẫn lộn

- **Hệ điều hành** (`10`) & **Landing Page Pipeline** (`MKT.LANDINGPAGE.SKILLS-main`) là *cái máy*. Cài đặt và sử dụng để tự động hoá công việc.
- **Thư viện skill** (`30`) là *bộ dụng cụ*. Rút ra dùng đúng lúc đúng việc.
- **Khung A–Z, Bài mẫu & Sơ đồ thuật toán** (`20`, `40`, `MKT.LANDINGPAGE.SKILLS-main/*.md`) là *hướng dẫn sử dụng & sơ đồ kiến trúc*.

---

## 🎯 Nguyên tắc thiết kế cốt lõi

1. **Thư mục xếp theo tầng bàn giao, không theo phòng ban:** Giúp quá trình bàn giao và tiếp nhận có thứ tự rõ ràng.
2. **Một việc — Một skill:** Mỗi bước thực hiện 1 nhiệm vụ rõ ràng, output bước trước là input bước sau.
3. **Cắt giảm nhiễu:** Đã tinh chỉnh loại bỏ các skill dư thừa không phù hợp với SME Việt Nam.
4. **Tối ưu cho thị trường Việt Nam:** Ngôn ngữ tiếng Việt thuần, xưng hô chuẩn mực, giao diện Mobile-First, tích hợp ngân hàng Việt Nam (VietQR/SePay) và thông báo qua Telegram.
5. **Local-first → Deploy 1-click:** Phát triển và kiểm thử toàn bộ ở Localhost trước khi Deploy live.

---

## ⚡ Cần gì để vận hành

- **Phần mềm:** Obsidian (miễn phí), Node.js, Claude Code / Antigravity Agent.
- **Tài khoản hỗ trợ:** Claude API / Gemini API, Supabase (Database & Auth), Vercel (Hosting), SePay (VietQR Webhook).
- **Nhân sự:** Một người chịu trách nhiệm chính trong doanh nghiệp (CEO / Operations Lead).

Chi tiết cài đặt: [`10. Hệ Điều Hành/00 — Hướng Dẫn Cài Đặt.md`](10.%20Hệ%20Điều%20Hành/00%20—%20Hướng%20Dẫn%20Cài%20Đặt.md) và [`MKT.LANDINGPAGE.SKILLS-main/README.md`](MKT.LANDINGPAGE.SKILLS-main/README.md).

---

## ⚠️ Lưu ý về dữ liệu bài mẫu

Toàn bộ thông tin doanh nghiệp, số điện thoại, tên miền và số liệu trong `40. Bài Mẫu — Công Ty Demo/` và tài liệu mẫu là **dữ liệu hư cấu** nhằm mục đích minh hoạ cấu trúc và tư duy vận hành.

