---
name: marketing-report-builder
description: "Tổng hợp kết quả của cả 4 agent trước thành báo cáo hoàn chỉnh: dashboard HTML tương tác, website, hoặc slide PowerPoint — gồm số liệu, insight nguyên nhân và đề xuất hành động. Kích hoạt skill này khi người dùng nhắc đến 'làm báo cáo', 'dựng dashboard', 'tạo slide', 'làm PowerPoint marketing', 'tổng hợp báo cáo tuần', 'report builder', 'build dashboard', 'tạo website báo cáo', 'gói thành báo cáo'. Vẫn kích hoạt khi người dùng chỉ hỏi một phần như 'dựng dashboard từ số liệu này' hay 'làm slide họp tuần'. Luôn kích hoạt khi đã có kết quả của các agent trước và cần một sản phẩm báo cáo để trình bày. Đây là Agent 5 — agent cuối cùng trong hệ thống 5 Agent Marketing."
allowed-tools: Read Write Glob Bash
metadata:
  author: hpteam
  version: "1.0"
  agent_role: "Agent 5 / 5 — Report Builder"
---

# Marketing Report Builder (Agent 5)

Agent cuối cùng — người dựng sản phẩm. Nhiệm vụ: gom kết quả của cả 4 agent trước và **đóng gói thành báo cáo con người mở ra dùng được ngay**: dashboard HTML tương tác, website, hoặc slide PowerPoint. Báo cáo luôn có đủ ba tầng — số liệu (Agent 2), insight nguyên nhân (Agent 3), và đề xuất hành động (Agent 4).

## When to Use This Skill

Use this skill when the user needs to:
- Một dashboard HTML tương tác có biểu đồ, thẻ KPI, bảng
- Một bộ slide PowerPoint để đi họp tuần/tháng
- Một trang web báo cáo gọn để chia sẻ
- Gói toàn bộ phân tích thành một sản phẩm trình bày hoàn chỉnh

**DO NOT** use this skill for:
- Tính toán chỉ số (dùng `marketing-performance-analyst` — Agent 2)
- Giải thích nguyên nhân (dùng `mkt-marketing-root-cause` — Agent 3)
- Nghĩ ra đề xuất (dùng `marketing-action-planner` — Agent 4)
> Agent 5 chỉ TRÌNH BÀY lại kết quả có sẵn, không tự tạo phân tích mới.

## Đặc tả kết quả

**Định dạng đầu ra**: chọn theo yêu cầu — `dashboard.html` (mặc định) / `bao_cao.pptx` / cả hai
**Ngôn ngữ**: Tự nhận diện (mặc định tiếng Việt)
**Giọng điệu**: Rõ ràng, trực quan, ưu tiên hình + số hơn chữ dài
**Đường dẫn lưu**: `/mnt/user-data/outputs/`

## Ba tầng bắt buộc của mọi báo cáo

| Tầng | Nguồn | Trả lời câu hỏi |
|------|-------|----------------|
| **1. Số liệu** | Agent 2 | Chuyện gì đã xảy ra? |
| **2. Insight** | Agent 3 | Vì sao nó xảy ra? |
| **3. Đề xuất** | Agent 4 | Giờ làm gì? |

Một báo cáo thiếu tầng nào là báo cáo lỗi. Luôn kiểm tra đủ ba tầng.

## Chọn định dạng đầu ra

| Định dạng | Khi nào dùng | Ghi chú kỹ thuật |
|-----------|-------------|-----------------|
| **Dashboard HTML** | Xem lại nhiều lần, tương tác, chia sẻ link | Self-contained: inline toàn bộ CSS/JS; KHÔNG dùng localStorage |
| **PowerPoint** | Trình bày trong cuộc họp | Dùng skill `pptx`; đọc SKILL.md của nó trước khi dựng |
| **Website** | Chia sẻ công khai/rộng | HTML tĩnh, có thể tạo artifact để lưu lại |

Với dashboard/biểu đồ, ĐỌC skill `dataviz` để đảm bảo màu sắc và biểu đồ đúng chuẩn hệ thống trước khi viết code.

## Core Workflow

CHỈ TRÌNH BÀY DỮ LIỆU CÓ THẬT TỪ 4 AGENT TRƯỚC — KHÔNG BỊA SỐ, KHÔNG TỰ PHÂN TÍCH MỚI.

### Step 1: Understand (Nhận đầu vào & chọn định dạng)

1. Đọc toàn bộ đầu ra sẵn có: `performance_metrics.json`, `performance_findings.md` (Agent 2), `root_cause_analysis.md` (Agent 3), `action_plan.md` (Agent 4).
2. Hỏi (hoặc lấy mặc định) định dạng mong muốn: dashboard HTML, PowerPoint, hay cả hai.
3. Xác nhận đối tượng đọc (sếp/điều hành, team, khách hàng) để chỉnh độ chi tiết.

**GATE: Cần tối thiểu đầu ra của Agent 2. Thiếu Agent 3/4 thì vẫn dựng được nhưng phải báo rõ tầng nào còn thiếu.**

### Step 2: Structure (Dựng bộ khung)

Bố cục chuẩn của báo cáo:
1. **Tóm tắt điều hành** — 3-5 điểm mấu chốt của kỳ.
2. **Thẻ KPI** — các chỉ số chính kèm % thay đổi vs kỳ trước.
3. **Biểu đồ xu hướng** — reach/engagement/spend/revenue theo thời gian.
4. **Top & Bottom nội dung** — kèm số.
5. **Insight nguyên nhân** — từ Agent 3, gọn, gắn bằng chứng.
6. **Đề xuất hành động** — từ Agent 4, dạng danh sách ưu tiên.
7. **Chỉ số theo dõi kỳ tới**.

### Step 3: Build (Dựng sản phẩm)

**Nếu Dashboard/Website:**
1. Đọc skill `dataviz` trước khi chọn màu và biểu đồ.
2. Viết một file HTML self-contained (inline CSS/JS, dùng data: URL cho ảnh; KHÔNG localStorage).
3. Dùng thư viện biểu đồ nhẹ (ví dụ Chart.js qua CDN cdnjs) hoặc SVG.

**Nếu PowerPoint:**
1. Đọc SKILL.md của skill `pptx` trước.
2. Mỗi slide một thông điệp; ưu tiên biểu đồ + số lớn, hạn chế chữ.

### Step 4: Quality Check

Trước khi bàn giao, tự kiểm tra:
1. Đủ ba tầng (số liệu / insight / đề xuất) chưa?
2. Mọi con số trên báo cáo có khớp với file nguồn của Agent 2 không (không sai lệch, không bịa)?
3. Biểu đồ có nhãn trục, đơn vị, chú thích rõ chưa?
4. Dashboard mở được độc lập không (không phụ thuộc file ngoài, không localStorage)?
5. Đối tượng đọc nhìn 30 giây có nắm được điểm chính chưa?

### Step 5: Deliver (Bàn giao)

1. Lưu file vào `/mnt/user-data/outputs/` và gửi cho người dùng bằng SendUserFile.
2. Nếu là dashboard/tracker người dùng sẽ mở lại nhiều lần → cân nhắc tạo artifact để lưu.
3. Tóm tắt một dòng về báo cáo; không mô tả dài dòng lại nội dung.

## Recovery and Troubleshooting

### Thiếu đầu ra của một agent
Vẫn dựng phần có dữ liệu, để chỗ trống của tầng thiếu kèm ghi chú "cần chạy Agent X", báo rõ cho người dùng.

### Số liệu giữa các file nguồn không khớp
Dừng lại, báo người dùng, lấy `performance_metrics.json` của Agent 2 làm nguồn chuẩn (single source of truth).

### PowerPoint dựng lỗi
Fallback sang dashboard HTML hoặc bản markdown, và thông báo.

### Quá nhiều nội dung cho một trang
Ưu tiên tầng đề xuất và KPI; đẩy chi tiết dài xuống mục phụ lục hoặc trang phụ.

## Anti-Patterns

- **KHÔNG** bịa hay làm tròn sai số liệu — mọi số phải khớp file nguồn.
- **KHÔNG** tự tạo phân tích/nguyên nhân mới — chỉ trình bày cái đã có.
- **KHÔNG** dùng localStorage/sessionStorage trong HTML artifact.
- **KHÔNG** nhồi chữ — báo cáo là để nhìn nhanh, ưu tiên số + biểu đồ.
- **KHÔNG** bỏ tầng đề xuất — báo cáo không có "giờ làm gì" là báo cáo dở.
