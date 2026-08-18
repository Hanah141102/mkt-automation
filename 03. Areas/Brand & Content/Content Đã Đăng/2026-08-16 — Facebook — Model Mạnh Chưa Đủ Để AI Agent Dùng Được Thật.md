---
content_pillar: "AI Marketing–Sales Closed-Loop"
format: "Facebook research digest kết hợp framework"
hook: "Model mạnh chưa đủ để AI Agent làm việc đáng tin cậy."
audience: "Chủ doanh nghiệp và người phụ trách vận hành tại SME Việt Nam"
funnel_stage: "Xây nhận thức và niềm tin"
cta: "Kiểm tra một AI Agent hiện có bằng năm câu hỏi vận hành"
trang-thai: da-dang
created: 2026-08-16
cap-nhat: 2026-08-16
published_at: "2026-08-16T20:51:00+07:00"
facebook_page: "Tony Hoàng Learn AI Automation"
facebook_post_id: "704841222706761_122226581036900113"
facebook_comment_id: "122226581036900113_1379442567487449"
facebook_url: "https://www.facebook.com/61577003393729/posts/122226581036900113/"
image_asset: "03. Areas/Brand & Content/Assets/2026-08-16-harness-engineering-infographic.png"
---

# Model mạnh chưa đủ để AI Agent dùng được thật

Liên kết: [[Chân Dung Doanh Nghiệp]] · [[Brand Voice — Giọng Thương Hiệu]] · [[Trụ Cột Nội Dung]] · [[2026-08-16 — 48 bài Nguyễn Tiệp có thể viết lại cho Tony]]

## Bản nội dung chính

**Model mạnh chưa đủ để AI Agent làm việc đáng tin cậy.**

Một paper mới có tên *Agent Systems with Harness Engineering* chỉ ra phần nhiều đội ngũ thường bỏ quên khi xây AI Agent: **hệ thống vận hành bao quanh model**.

Nhóm tác giả gọi lớp này là **harness**.

Model cung cấp khả năng suy luận và tạo nội dung. Harness quyết định Agent nhận mục tiêu thế nào, dùng công cụ gì, ghi nhớ điều gì, xử lý lỗi ra sao và khi nào phải dừng.

Đây là khác biệt giữa một bản demo chạy được và một hệ thống có thể đưa vào công việc thật.

Paper mô tả bốn nhóm thành phần chính:

1. Agent workflow — luồng công việc của Agent.
2. Memory system — hệ thống bộ nhớ.
3. Skill library — thư viện kỹ năng.
4. Multi-agent orchestration — cách nhiều Agent phối hợp.

Nhưng với một chủ doanh nghiệp, tôi nghĩ có thể chuyển nghiên cứu này thành **5 câu hỏi vận hành** dễ kiểm tra hơn.

### 1. Agent có biết khi nào công việc hoàn thành?

Một mục tiêu như “chăm sóc khách hàng tốt hơn” không đủ rõ.

Agent cần đầu vào, các bước xử lý, đầu ra và tiêu chí hoàn thành. Nếu mục tiêu mơ hồ, model càng mạnh chỉ càng tạo ra câu trả lời thuyết phục hơn cho một công việc chưa được định nghĩa.

### 2. Agent đang dùng nguồn dữ liệu nào?

Chính sách, bảng giá, hồ sơ khách hàng và lịch sử xử lý phải có nguồn chuẩn.

Nếu ba phòng ban đang dùng ba phiên bản tài liệu, AI không thể tự quyết định phiên bản nào đại diện cho doanh nghiệp.

Quản trị ngữ cảnh không phải nhồi thêm thật nhiều tài liệu.

Đó là đưa đúng thông tin vào đúng thời điểm.

### 3. Agent được phép làm gì?

Đọc dữ liệu khác với cập nhật dữ liệu.

Tạo bản nháp khác với tự gửi cho khách hàng.

Mỗi công cụ cần có phạm vi quyền, điều kiện kích hoạt và giới hạn rõ. Những việc liên quan đến giá, hoàn tiền, pháp lý hoặc cam kết nên có cổng phê duyệt của người phụ trách.

### 4. Agent có học được từ lần sửa trước không?

Nếu nhân viên sửa cùng một lỗi mỗi ngày nhưng bài học chỉ nằm trong đoạn chat, hệ thống chưa thật sự học.

Các lỗi lặp lại cần được chưng cất thành quy tắc, ví dụ, test case hoặc Skill có thể gọi lại. Bộ nhớ chỉ có giá trị khi nó làm lần thực thi sau tốt hơn và vẫn có người quản lý phiên bản.

### 5. Khi Agent không chắc, công việc được chuyển cho ai?

Một hệ thống đáng tin không phải hệ thống không bao giờ sai.

Đó là hệ thống phát hiện được tình huống vượt phạm vi, lưu lại quá trình xử lý và chuyển ngoại lệ tới đúng người.

Ví dụ, một Agent chăm sóc khách hàng không nên chỉ được đánh giá bằng câu trả lời có tự nhiên hay không.

Nó cần được kiểm tra thêm:

- Có dùng đúng chính sách hiện hành không?
- Có dẫn được nguồn cho câu trả lời không?
- Có tạo ticket và cập nhật đúng trạng thái không?
- Có dừng trước yêu cầu hoàn tiền ngoài thẩm quyền không?
- Có chuyển đầy đủ ngữ cảnh cho nhân viên tiếp nhận không?

Đây là lý do tôi không bắt đầu một dự án AI bằng câu hỏi:

**“Nên chọn model nào?”**

Tôi bắt đầu bằng các câu hỏi khác:

**Quy trình nào đang cần sửa? Dữ liệu chuẩn nằm ở đâu? AI nhận phần việc nào? Ngoại lệ giao cho ai? Kết quả được kiểm tra bằng gì?**

Model tạo ra khả năng.

Harness tạo ra độ tin cậy.

Quy trình mới biến khả năng đó thành kết quả kinh doanh.

### Ví dụ trong Marketing

Giả sử doanh nghiệp xây một AI Agent để hỗ trợ sản xuất nội dung Marketing.

Nếu chỉ đưa cho nó một câu lệnh như “hãy viết bài Facebook”, Agent có thể tạo nội dung nhanh. Nhưng đó mới là khả năng của model, chưa phải một hệ thống Marketing.

Một harness đủ rõ cần tổ chức công việc như sau:

1. **Workflow:** nhận mục tiêu chiến dịch → chọn insight → tạo concept → viết bản nháp → chờ duyệt → xuất bản → đọc kết quả.
2. **Dữ liệu:** chỉ dùng chân dung khách hàng, Brand Voice, offer và bằng chứng đã được doanh nghiệp xác nhận.
3. **Quyền hành động:** được tạo bản nháp và đề xuất hình ảnh, nhưng không tự đăng bài, thay đổi ngân sách hoặc công bố giá.
4. **Bộ nhớ:** lưu lại hook bị loại, chỉnh sửa của người duyệt và kết quả nội dung để lần sau không lặp lại cùng một lỗi.
5. **Bàn giao:** nội dung có cam kết, số liệu, thông tin khách hàng hoặc vấn đề nhạy cảm phải chuyển cho người phụ trách quyết định.

Khi đó, AI không chỉ viết nhanh hơn.

Nó trở thành một phần của vòng vận hành Marketing có nguồn, có kiểm duyệt và có khả năng học từ phản hồi.

Nếu anh/chị đang thử một AI Agent, hãy dùng năm câu hỏi trên để kiểm tra hệ thống trước khi mua thêm một model hoặc công cụ mới.

#AIAgent #HarnessEngineering #AIForBusiness #BusinessProcess #HumanInTheLoop #ContextEngineering #AIGovernance

## Gợi ý hình ảnh

- **Tên sơ đồ:** 5 lớp để AI Agent dùng được thật.
- **Tỷ lệ:** 1:1 cho Facebook.
- **Bố cục:** năm lớp xếp chồng từ dưới lên.
- **Các lớp:** Quy trình rõ → Dữ liệu chuẩn → Quyền hành động → Bộ nhớ & Skills → Kiểm tra & Bàn giao.
- **Kết quả trên cùng:** Dùng được thật trong doanh nghiệp.
- **Headline:** “Model tạo khả năng. Hệ thống tạo độ tin cậy.”
- Không dùng logo model hoặc hình robot; ưu tiên sơ đồ vận hành đơn giản.

## Nguồn và giới hạn

- Nguồn chính: [Agent Systems with Harness Engineering — OpenReview](https://openreview.net/pdf?id=nM5tDHrQsx).
- Kho tài liệu chính thức của nhóm tác giả: [RUCAIBox/awesome-agent-harness](https://github.com/RUCAIBox/awesome-agent-harness).
- Paper xác định bốn nhóm thành phần của harness: workflow, memory, skill library và multi-agent orchestration.
- Khung “5 câu hỏi vận hành cho SME” là phần diễn giải và ứng dụng của bài viết này, không phải taxonomy nguyên văn của paper.
- Bài không khẳng định mọi doanh nghiệp cần multi-agent hoặc phải tự xây hạ tầng riêng.
- Cần điều chỉnh quyền, kiểm thử và cổng phê duyệt theo mức rủi ro của từng quy trình.

## Checklist tự kiểm

- [x] Mở bằng kết luận rõ và trái với thói quen chạy theo model.
- [x] Dùng nghiên cứu gốc làm lý do tin.
- [x] Phân biệt taxonomy của paper với diễn giải của Tony.
- [x] Chuyển thuật ngữ kỹ thuật thành năm câu hỏi vận hành.
- [x] Có ví dụ chăm sóc khách hàng và điểm bàn giao cho người.
- [x] Không bịa số liệu hoặc case triển khai.
- [x] Một CTA: kiểm tra Agent bằng năm câu hỏi.
- [ ] Tony duyệt câu chữ trước khi đăng.
