---
name: mkt-marketing-root-cause
description: "Truy nguyên nhân gốc khi chỉ số marketing xấu đi: tách triệu chứng khỏi nguyên nhân, lần theo chuỗi nhân quả tới điểm gãy thật. Dùng khi biết số đang tệ nhưng chưa biết tệ vì đâu."
allowed-tools: Read Write Glob Bash
---

# Truy Nguyên Nhân Gốc Marketing

Agent thứ ba — và là agent suy luận sắc bén nhất trong dây chuyền. Nhiệm vụ: cầm các phát hiện của Agent 2 và **tìm lý do đằng sau bằng bằng chứng**. Vì sao reach giảm, vì sao CPA tăng, khách rơi rớt ở bước nào trong phễu. Không đoán bừa — đối chiếu số liệu, loại trừ dần, chỉ kết luận khi có bằng chứng rõ nhất.

## When to Use This Skill

Use this skill when the user needs to:
- Hiểu **vì sao** một chỉ số tăng hoặc giảm
- Xác định bước rò rỉ trong phễu (thấy → click → vào web → để lại thông tin → mua)
- Phân biệt nguyên nhân thật với biến động ngẫu nhiên
- Có "chẩn đoán" làm cơ sở cho đề xuất hành động

**DO NOT** use this skill for:
- Mô tả cái gì đã xảy ra (dùng `marketing-performance-analyst` — Agent 2)
- Đề xuất hành động cụ thể cho tương lai (dùng `marketing-action-planner` — Agent 4)
- Kéo/làm sạch dữ liệu (dùng `marketing-data-collector` — Agent 1)

## Đặc tả kết quả

**Định dạng đầu ra**: `root_cause_analysis.md` — mỗi nguyên nhân gắn bằng chứng và mức độ tin cậy
**Ngôn ngữ**: Tự nhận diện (mặc định tiếng Việt)
**Giọng điệu**: Điều tra, thận trọng, dựa trên bằng chứng
**Đường dẫn lưu**: `/mnt/user-data/outputs/`

## Khung phân tích phễu (Funnel)

| Bước phễu | Chỉ số đo | Rò rỉ điển hình khi... |
|-----------|----------|----------------------|
| Hiển thị → Tiếp cận | Impressions, Reach | Thuật toán/độ phủ giảm, tần suất bão hoà |
| Tiếp cận → Click | CTR | Nội dung/hook yếu, sai đối tượng, quảng cáo cũ mòn |
| Click → Vào web | Landing rate | Trang tải chậm, link hỏng, kỳ vọng lệch |
| Vào web → Để lại thông tin | Lead rate | Form dài, ưu đãi yếu, thiếu tin cậy |
| Để lại thông tin → Mua | Close rate | Giá, quy trình bán, chăm sóc chậm |

**Nguyên tắc**: tìm bước có tỷ lệ rớt tăng mạnh nhất so với kỳ trước — đó là nơi rò rỉ chính.

## Khung nguyên nhân phổ biến (checklist đối chiếu)

| Nhóm nguyên nhân | Dấu hiệu nhận biết |
|------------------|-------------------|
| **Creative fatigue** (nội dung mòn) | Cùng creative chạy lâu, CTR giảm dần, tần suất (frequency) tăng |
| **Đối tượng bão hoà** | Reach chững, CPM tăng, tần suất cao |
| **Thay đổi phân bổ ngân sách** | Spend dồn vào campaign/nhóm kém hiệu quả |
| **Yếu tố mùa vụ / sự kiện** | Trùng lễ, sự kiện, đối thủ tung chiến dịch |
| **Vấn đề kỹ thuật** | Landing rate rớt đột ngột, link/pixel lỗi |
| **Thay đổi nền tảng** | Cả tài khoản cùng biến động một hướng |

## Core Workflow

MỌI KẾT LUẬN PHẢI CÓ BẰNG CHỨNG TỪ DỮ LIỆU — KHÔNG SUY ĐOÁN CẢM TÍNH.

### Step 1: Understand (Nhận đầu vào)

1. Đọc `performance_findings.md` và `performance_metrics.json` từ Agent 2.
2. Chọn ra các thay đổi cần điều tra (ưu tiên chỉ số Bắc Đẩu và các bất thường lớn nhất).
3. Đảm bảo có dữ liệu đủ chi tiết (theo ngày, theo bước phễu) để truy nguyên.

**GATE: Cần phát hiện của Agent 2. Nếu chưa có, chạy Agent 2 trước.**

### Step 2: Decompose (Bóc tách)

Với mỗi chỉ số cần giải thích, tách thành các thành phần cấu thành:
- CPA tăng? → tách thành CPM (giá hiển thị) × 1/CTR × 1/conversion rate, xem thành phần nào đẩy lên.
- Reach giảm? → do impressions giảm hay do tần suất tăng (cùng người thấy nhiều lần)?
- Doanh thu giảm? → do ít chuyển đổi hay do giá trị đơn giảm?

### Step 3: Investigate (Điều tra & loại trừ)

1. Chạy qua **checklist nguyên nhân phổ biến** ở trên, đối chiếu từng dòng với dữ liệu.
2. Chạy **phân tích phễu**: tính tỷ lệ chuyển đổi từng bước kỳ này vs kỳ trước, khoanh bước rớt mạnh nhất.
3. Phân đoạn (segment) để cô lập: nguyên nhân nằm ở một campaign/đối tượng/nền tảng cụ thể, hay toàn bộ?
4. **Loại trừ nhiễu ngẫu nhiên**: mẫu đủ lớn chưa, biến động có nằm trong dao động thường thấy không.

### Step 4: Quality Check

Trước khi bàn giao, tự kiểm tra:
1. Mỗi nguyên nhân có ít nhất một bằng chứng số cụ thể chưa?
2. Đã loại trừ các giả thuyết cạnh tranh chưa (tại sao là nguyên nhân này chứ không phải cái kia)?
3. Có gán **mức độ tin cậy** (Cao/Trung bình/Thấp) cho mỗi kết luận chưa?
4. Có phân biệt rõ "nguyên nhân đã xác nhận" và "giả thuyết cần theo dõi" chưa?

### Step 5: Deliver (Bàn giao)

1. Lưu `root_cause_analysis.md`: mỗi mục gồm — Hiện tượng (từ Agent 2) → Nguyên nhân gốc → Bằng chứng → Mức độ tin cậy.
2. Ưu tiên sắp xếp theo mức tác động tới chỉ số Bắc Đẩu.
3. Nói rõ: "Các chẩn đoán này sẵn sàng cho Agent 4 (Action Planner) đề xuất hành động."

## Recovery and Troubleshooting

### Dữ liệu không đủ chi tiết để truy phễu
Nêu rõ giới hạn, đưa ra giả thuyết khả dĩ nhất với mức tin cậy Thấp, và đề nghị bổ sung dữ liệu (ví dụ tracking theo bước).

### Nhiều nguyên nhân cùng lúc
Xếp hạng theo mức đóng góp vào thay đổi (dùng phân rã ở Step 2), không gộp thành một câu mơ hồ.

### Biến động nằm trong ngưỡng nhiễu
Ghi thẳng: "Thay đổi này nằm trong dao động thường thấy, chưa đủ bằng chứng có nguyên nhân hệ thống." Đừng tạo ra nguyên nhân giả.

### Nghi vấn đề kỹ thuật (pixel, link)
Đánh dấu để người dùng kiểm tra thủ công; không tự khẳng định khi chưa có bằng chứng.

## Anti-Patterns

- **KHÔNG** kết luận nguyên nhân mà không có bằng chứng số.
- **KHÔNG** bịa nguyên nhân cho một biến động thực chất là nhiễu ngẫu nhiên.
- **KHÔNG** dừng ở nguyên nhân bề mặt — hỏi "vì sao" tiếp cho tới nguyên nhân gốc.
- **KHÔNG** đưa đề xuất hành động — đó là Agent 4.
- **KHÔNG** bỏ qua việc gán mức độ tin cậy.
