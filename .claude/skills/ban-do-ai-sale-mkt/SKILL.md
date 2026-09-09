---
name: ban-do-ai-sale-mkt
description: "Đọc mô hình kinh doanh đã có trong `00. Business Context/`, phỏng vấn kỹ từng bước của quy trình Marketing và Sale hiện tại (thu hút, lead vào, tư vấn, chốt, sau bán, đo lường), chấm điểm rồi chỉ ra doanh nghiệp Việt nên đưa AI vào điểm nào trước, điểm nào chưa nên, người vẫn phải duyệt gì. Ghi ra `Bản Đồ Ứng Dụng AI — Sale & Marketing.md`. Dùng sau `/mo-hinh-kinh-doanh` (được gọi tự động ở Giai đoạn 2) hoặc chạy riêng khi đã có MHKD."
ten-viet: "Bản Đồ Ứng Dụng AI — Sale & Marketing"
nhom: "01. Chiến Lược & Điều Hành"
ten-goc: "AI Opportunity Map — Sales & Marketing"
---

# Bản Đồ Ứng Dụng AI — Sale & Marketing

## Skill này trả lời câu hỏi gì

Chủ doanh nghiệp Việt thường hỏi: *"Tôi nên dùng AI vào chỗ nào trong bán hàng và marketing?"* Câu trả lời đúng **không nằm ở danh sách công cụ**, mà nằm ở quy trình thật của họ: lead vào từ đâu, ai trả lời, mất bao lâu, rơi ở bước nào, ai đang làm việc lặp lại mỗi ngày.

Skill này làm ba việc theo thứ tự:

1. **Vẽ lại quy trình Marketing và Sale đang chạy**, từng bước, bằng câu trả lời của người dùng.
2. **Chấm điểm từng điểm chạm** theo khung dành cho doanh nghiệp vừa và nhỏ Việt Nam.
3. **Đề xuất ba tầng**: làm ngay trong 30 ngày, kế tiếp trong 60 đến 90 ngày, và chưa nên làm kèm lý do.

Đầu ra là một file trong `00. Business Context/` mà mọi skill vận hành phía sau đọc trước khi tự động hoá bất cứ thứ gì.

## Phạm vi: chỉ Sale & Marketing, đóng gói thành hệ thống agent

Skill này **chỉ đề xuất trong phạm vi Sale & Marketing**: thu hút, nội dung, quảng cáo, lead, tư vấn, chốt, chăm sóc khách, mua lại, và đo lường của chính các mảng đó. Không đề xuất cho kế toán, nhân sự, kho vận, sản xuất hay pháp lý, kể cả khi phỏng vấn lộ ra điểm đau ở đó. Gặp thì ghi một dòng "ngoài phạm vi, xem `/process-automation-audit`" rồi đi tiếp.

Đề xuất được đóng gói thành **hệ thống agent**, không phải mẹo dùng chatbot lẻ. Một hệ thống agent là một AI làm một việc theo quy trình rõ, đọc dữ liệu của doanh nghiệp, có điểm dừng để người duyệt, và đo được. Tám họ hệ thống agent mà skill này xét, chi tiết trong `references/khung-cham-diem-va-diem-ung-dung.md`:

| # | Hệ thống agent | Phục vụ giai đoạn |
|:--:|---|---|
| A1 | **Agent nội dung** — từ câu hỏi khách và trụ cột ra bài, biến một bài thành nhiều định dạng, đúng giọng thương hiệu | Thu hút |
| A2 | **Agent quảng cáo và đo chất lượng quảng cáo** — nháp biến thể, chấm điểm nội dung trước khi chạy, đọc số theo giờ, cảnh báo bất thường | Thu hút |
| A3 | **Agent nhắn tin đa kênh** — Zalo, Facebook, inbox sàn: trả lời câu hỏi lặp, phân loại, chuyển người đúng lúc | Lead vào |
| A4 | **Agent chấm điểm lead và CRM** — điền hồ sơ lead từ hội thoại, chấm nóng lạnh, nhắc chạm theo chu kỳ bán | Lead vào · Tư vấn |
| A5 | **Agent phân tích cuộc gọi** — nghe lại cuộc gọi tư vấn và chăm sóc, tóm tắt, chấm chất lượng, cập nhật pipeline | Tư vấn · Sau bán |
| A6 | **Agent chăm sóc sau bán và mua lại** — onboarding theo lộ trình, xin đánh giá đúng lúc, nhắc mua lại, cảnh báo khách sắp rời | Sau bán |
| A7 | **Agent phân tích khách hàng và tự đề xuất** — đọc dữ liệu CRM, tìm nhóm khách sinh lời, khách sắp rời, cơ hội bán thêm, và đề xuất việc nên làm tuần này | Sau bán · Đo lường |
| A8 | **Agent báo cáo Sale & Marketing** — gom số từ nhiều nguồn thành báo cáo theo nhịp đọc số, giải thích tăng giảm | Đo lường |

Skill **không** kéo cả tám họ vào đề xuất. Chỉ chọn họ nào khớp với bước thật trong bảng quy trình ở Bước 2 và đủ điểm ở Bước 3.

## Nguyên tắc cốt lõi

**QUY TRÌNH CHƯA MÔ TẢ RÕ THÌ CHƯA GIAO AI. AI CHỈ LÀM TỐT VIỆC MÀ CON NGƯỜI ĐÃ LÀM ĐƯỢC VÀ LÀM LẶP LẠI.**

Hệ quả:

- Nếu người dùng không kể được bước đó diễn ra thế nào, đề xuất đúng là **viết quy trình trước** (`/sop-builder`), không phải đưa AI vào.
- Mỗi đề xuất AI phải ghi rõ **người vẫn duyệt gì**. Không có đề xuất nào để AI tự gửi cho khách trong 30 ngày đầu.
- **Không nêu tên công cụ hay nhà cung cấp.** Mô tả bài toán, việc AI làm, dữ liệu cần, chỉ số đo. Chọn công cụ là việc của doanh nghiệp ở bước sau.
- Tiền tệ là VND. Không bịa số giờ tiết kiệm hay số tiền lợi. Chưa có số thì ghi "chưa có dữ liệu" và nói cách đo.
- Tách rõ **fact** (người dùng nói), **suy luận** (Claude rút ra), **giả định** (chưa kiểm chứng).

## Bước 0 — Đọc vault trước khi hỏi

Đọc theo thứ tự, không bỏ:

| File | Lấy gì |
|---|---|
| `00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md` | 6 tham số: loại sản phẩm, chu kỳ bán, người mua có là người dùng, mùa vụ, sở hữu điểm chạm, mô hình mua lại. **Nếu chưa điền, dừng lại và hướng người dùng chạy `/mo-hinh-kinh-doanh` trước.** |
| `Business Model Canvas — [Tên].md` | Kênh, quan hệ khách hàng, dòng doanh thu, hoạt động chính |
| `MHKD/Phân Khúc Khách Hàng/PK*.md` | Hành vi mua, tín hiệu lead tốt, phản đối thường gặp, KPI |
| `MHKD/Giá Trị Cốt Lõi/GT*.md` | Bằng chứng cần có, phản đối, logic giá |
| `Đánh Giá Mô Hình Kinh Doanh — [Tên].md` | Điểm nghẽn đã phát hiện |
| `AI-Sale-Assistant.md` | Ranh giới AI hiện có, để không đề xuất trái với nó |
| `Sản Phẩm & Dịch Vụ/` | Có bao nhiêu gói, giá đã cố định hay thương lượng |
| `03. Areas/Sales Pipeline & CRM/`, `03. Areas/Marketing Channels/` | Nếu đã có dữ liệu vận hành thật, dùng làm fact |

Sau khi đọc, **tóm tắt cho người dùng những gì đã biết** trong 8 đến 12 dòng và hỏi họ xác nhận hoặc sửa. Những điều đã có trong vault thì **không hỏi lại**.

Nếu file `Bản Đồ Ứng Dụng AI — Sale & Marketing.md` đã tồn tại và có nội dung thật, cho người dùng biết, hỏi họ muốn cập nhật hay làm mới. Không ghi đè âm thầm.

## Bước 1 — Phỏng vấn 6 lượt theo quy trình thật

Mở `references/cau-hoi-phong-van-ai-sale-mkt.md`. Bộ câu hỏi chia 6 lượt, mỗi lượt 4 đến 6 câu, đi theo dòng chảy của khách hàng:

| Lượt | Chủ đề | Mục tiêu |
|:--:|---|---|
| 1 | Đội ngũ, công cụ, dữ liệu, ranh giới | Biết ai đang làm gì, dữ liệu khách nằm ở đâu, có gì không được đụng |
| 2 | Thu hút: nội dung, quảng cáo, kênh | Việc lặp lại trong marketing, chỗ tốn thời gian nhất |
| 3 | Lead vào và phản hồi đầu | Tốc độ phản hồi, câu hỏi lặp, lead rơi ở cửa |
| 4 | Tư vấn và chốt | Báo giá, nhắc lại, lý do mất deal, chủ can dự chỗ nào |
| 5 | Sau bán và mua lại | Chăm sóc, khiếu nại, xin giới thiệu, nhắc mua lại |
| 6 | Đo lường, quyết định, lo ngại | Báo cáo, con số chủ xem, điều không bao giờ giao AI |

**Cách hỏi:**

- Hỏi **từng lượt một**. Trình bày các câu của một lượt cùng lúc, để người dùng kể tự do bằng đoạn văn. Chờ trả lời xong lượt này rồi mới sang lượt sau.
- Sau mỗi lượt, **phản hồi lại 3 đến 5 dòng** những gì vừa nghe được và hỏi thêm **tối đa 2 câu đào sâu** nếu câu trả lời còn chung chung. Ví dụ "có người trả lời inbox" chưa đủ, cần biết ai, trong bao lâu, ngoài giờ thì sao.
- Với mỗi bước quy trình người dùng kể, cố lấy đủ 6 thông tin: **ai làm · bao nhiêu lần một tuần · mất bao lâu một lần · dùng gì để làm · hay lỗi ở đâu · để lại dữ liệu gì**. Thiếu thông tin nào thì hỏi, người dùng không biết thì ghi "chưa đo".
- Chấp nhận "chưa biết" và "chưa đo". Đừng ép người dùng đoán số. Ghi lại là chỗ cần đo, đó cũng là một phát hiện.
- Nếu người dùng là chủ doanh nghiệp một mình hoặc đội dưới 5 người, nhiều bước sẽ do cùng một người làm. Vẫn hỏi đủ 6 lượt nhưng gọn hơn, và chú ý câu "nếu anh chị nghỉ một tuần thì bước nào dừng".

Toàn bộ phỏng vấn thường mất 25 đến 40 phút trò chuyện. Đó là mức đầu tư đúng, vì bản đồ này quyết định vài chục triệu đồng ngân sách công cụ và hàng trăm giờ của đội về sau.

## Bước 2 — Dựng bản đồ quy trình và xác nhận

Từ câu trả lời, dựng bảng quy trình hiện tại theo 5 giai đoạn: **Thu hút → Lead vào → Tư vấn & chốt → Sau bán → Đo lường**. Mỗi dòng là một bước với 6 cột thông tin ở trên.

Đưa bảng này cho người dùng xem **trước khi chấm điểm**. Hỏi: "Có bước nào tôi ghi sai, thiếu, hoặc anh chị thấy không đúng thực tế?" Bước này bắt được rất nhiều lỗi hiểu nhầm, và người dùng thường nhớ thêm 1 đến 2 bước họ quên kể.

Đánh dấu ngay trên bảng:

- 🔴 bước **chặn dòng tiền**: lead không được trả lời, báo giá gửi chậm, quên nhắc lại, khách cũ không được gọi lại.
- 🟠 bước **lặp lại nhiều, tốn giờ**: viết nội dung, trả lời câu hỏi giống nhau, gom số làm báo cáo.
- ⚪ bước **chưa có quy trình**: người dùng không mô tả được, hoặc mỗi người làm một kiểu.

## Bước 3 — Chấm điểm từng điểm chạm

Mở `references/khung-cham-diem-va-diem-ung-dung.md`. Khung có 5 tiêu chí, mỗi tiêu chí 0 đến 2 điểm, tổng 10:

1. **Tác động dòng tiền** — bước này có nằm trên đường khách trả tiền không, có đang làm mất lead hoặc mất deal không.
2. **Độ lặp lại và khối lượng** — làm nhiều lần một tuần, cách làm giống nhau.
3. **Quy trình và dữ liệu đã sẵn** — có mẫu, có câu trả lời chuẩn, có dữ liệu để AI đọc.
4. **Rủi ro thấp khi AI sai** — AI sai thì người duyệt bắt được trước khi tới khách hay tới tiền.
5. **Có người vận hành và duyệt** — có người cụ thể sẽ dùng và kiểm mỗi ngày.

Có ba **điều kiện chặn**, vi phạm một cái là xuống tầng "Chưa nên" bất kể điểm:

- Bước đó chưa có quy trình mô tả được (điểm ⚪ ở Bước 2).
- Liên quan tới dữ liệu cá nhân của khách mà doanh nghiệp chưa có cơ sở thu thập và chưa xin đồng ý.
- Không ai trong đội nhận duyệt đầu ra.

Xếp tầng: **8 đến 10 điểm** làm ngay · **5 đến 7** kế tiếp · **0 đến 4** chưa nên. Tầng làm ngay giữ **tối đa 3 đề xuất**. Nhiều hơn là không ai làm nổi.

Tham chiếu danh mục tám họ hệ thống agent trong file khung để đặt tên đề xuất cho đúng, nhưng **chỉ chọn những agent khớp với bước thật** trong bảng quy trình. Không kéo cả danh mục vào. Một đề xuất có thể là một agent trọn họ (ví dụ A3 cho toàn bộ inbox) hoặc một phần của họ (ví dụ chỉ phần "chấm điểm nội dung trước khi chạy" của A2) nếu quy trình hiện tại chỉ sẵn tới đó.

## Bước 4 — Tóm tắt đề xuất và xác nhận

Trước khi ghi file, trình bày cho người dùng:

- Bảng chấm điểm.
- Ba tầng đề xuất, mỗi đề xuất 2 dòng: điểm chạm và việc AI làm, người duyệt gì.
- Danh sách "AI không làm" rút từ lượt 6.

Hỏi họ hai câu: "Có đề xuất nào anh chị thấy không hợp thực tế?" và "Thứ tự tầng làm ngay đã đúng ý chưa?" Sửa theo ý họ. Đây là bản đồ của họ, không phải của Claude.

## Bước 5 — Ghi file

### File chính

Đường dẫn: `00. Business Context/Bản Đồ Ứng Dụng AI — Sale & Marketing.md`

Copy `assets/ban-do-ai-sale-mkt-template.md` và điền. Quy tắc điền:

- Mỗi đề xuất theo đúng khung 9 mục trong template: điểm chạm, hiện trạng, việc AI làm, người vẫn duyệt, dữ liệu cần, chỉ số đo, ngưỡng thời gian áp dụng, rủi ro và cách chặn, chi phí ước tính.
- Chi phí ước tính ghi theo khoảng VND một tháng và gắn `⚠️ giả định` nếu người dùng chưa khảo giá. Không có cơ sở thì ghi "chưa có dữ liệu".
- Ngưỡng thời gian **tính từ `chu-ky-ban-ngay`** trong Hồ Sơ Mô Hình Kinh Doanh, không dùng con số cứng. Ví dụ nhắc lại sau báo giá ở 5%, 15%, 30% chu kỳ.
- Mục "Chưa nên" phải có lý do và điều kiện để xét lại.
- Phần "Dữ liệu cần gom trước" liệt kê những chỗ người dùng trả lời "chưa đo", kèm cách đo đơn giản nhất.

### Cập nhật file liên quan

- `AI-Sale-Assistant.md`: đối chiếu mục "Không được tự quyết" với danh sách "AI không làm" vừa chốt. Nếu có điểm mới, **đề xuất sửa và hỏi trước**, không tự ghi.
- `_MOC 00. Business Context.md`: thêm dòng cho file mới nếu chưa có.
- Nếu tầng làm ngay kéo theo ngân sách công cụ hoặc thay đổi cách phản hồi khách, nhắc người dùng đây là quyết định cần ghi vào `Decisions/` sau khi họ xác nhận. Không tự tạo file quyết định.

## Bước 6 — Việc tiếp theo

Chỉ gợi ý, không tự chạy. Với mỗi đề xuất tầng làm ngay, chỉ đúng skill vận hành:

| Đề xuất thuộc nhóm | Skill tiếp theo |
|---|---|
| Bước chưa có quy trình | `/sop-builder` |
| Phân loại và chấm điểm lead, nhắc chạm lead | `/phan-bo-va-cham-diem-lead` |
| Trả lời inbox, chốt qua chat | `/chot-don-qua-inbox` · `/chot-don-qua-zalo` |
| Xử lý từ chối, kịch bản tư vấn | `/objection-handler` · `/sales-script` |
| Nội dung theo trụ cột, biến một bài thành nhiều bài | `/content-pillar-builder` · `/mkt-content-repurpose` |
| Quảng cáo và thử nghiệm | `/ads-copywriting` · `/thu-nghiem-ab` |
| Chăm sóc sau bán, nhắc mua lại | `/customer-success-playbook` · `/nhac-mua-lai-theo-chu-ky` |
| Ghi cuộc gặp, cập nhật pipeline | `/ghi-cuoc-gap` |
| Báo cáo và chỉ số | `/mkt-kpi-dashboard` · `/do-luong-tracking` |
| Tuân thủ dữ liệu cá nhân, quảng cáo | `/tuan-thu-nganh-vn` |

Kết thúc bằng một câu: đề xuất số 1 ở tầng làm ngay là gì, và bước đầu tiên trong tuần này là gì.

## Những lỗi hay gặp và cách tránh

- **Đề xuất theo danh mục thay vì theo quy trình thật.** Nếu bảng quy trình không có bước "viết quảng cáo" thì không đề xuất AI viết quảng cáo.
- **Nhét quá nhiều vào tầng làm ngay.** Tối đa 3. Chủ doanh nghiệp Việt thường kiêm nhiều vai, họ chỉ đủ sức thử một hai thứ mỗi tháng.
- **Bỏ qua người duyệt.** Đề xuất nào không ghi tên vai trò duyệt thì chưa xong.
- **Bịa giờ tiết kiệm.** Chỉ ghi khi người dùng đã nói mất bao lâu một lần và bao nhiêu lần một tuần. Còn lại ghi "chưa có dữ liệu" và cách đo.
- **Quên mùa vụ.** Nếu `mua-vu: co-mua`, tầng làm ngay phải xong trước mùa cao điểm ít nhất 6 tuần, hoặc dời sang sau mùa.
- **Trôi ra ngoài Sale & Marketing.** Điểm đau về kho, kế toán, nhân sự ghi một dòng ngoài phạm vi, không chấm điểm, không đề xuất.
- **Nêu tên công cụ.** Người dùng hỏi "dùng phần mềm nào" thì trả lời: bản đồ này mô tả bài toán, việc chọn công cụ làm ở bước sau khi đã có bài toán rõ. Có thể liệt kê **tiêu chí chọn** thay vì tên.
