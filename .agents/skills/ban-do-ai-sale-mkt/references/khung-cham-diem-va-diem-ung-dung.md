# Khung chấm điểm và danh mục tám họ hệ thống agent — Sale & Marketing

File này có ba phần: (1) khung chấm điểm 10 điểm và ba điều kiện chặn, (2) danh mục tám họ hệ thống agent với đủ thông tin để viết một đề xuất, (3) bối cảnh doanh nghiệp Việt cần nhớ khi chấm. Chỉ dùng cho phạm vi Sale & Marketing.

---

## Phần 1 — Khung chấm điểm

Mỗi điểm chạm trong bảng quy trình được chấm 5 tiêu chí, mỗi tiêu chí 0, 1 hoặc 2 điểm. Tổng 10.

| # | Tiêu chí | 0 điểm | 1 điểm | 2 điểm |
|:--:|---|---|---|---|
| 1 | **Tác động dòng tiền** | Bước hỗ trợ, không nằm trên đường khách trả tiền | Nằm trên đường trả tiền nhưng chưa thấy rơi rớt rõ | Đang làm mất lead, mất deal hoặc mất khách cũ, người dùng kể được ví dụ |
| 2 | **Độ lặp lại và khối lượng** | Vài lần một tháng, mỗi lần khác nhau | Vài lần một tuần hoặc cách làm giống nhau một phần | Hằng ngày, cách làm giống nhau, người làm thấy nhàm |
| 3 | **Quy trình và dữ liệu đã sẵn** | Không mô tả được, mỗi người một kiểu, dữ liệu rải rác | Có cách làm quen tay nhưng chưa thành văn, dữ liệu gom được trong 1 đến 2 tuần | Có mẫu, có câu trả lời chuẩn, có dữ liệu ở một chỗ đọc được |
| 4 | **Rủi ro thấp khi AI sai** | Sai là tới khách hoặc tới tiền ngay, khó thu hồi | Sai có thể bắt được nếu người duyệt để ý | Sai chỉ tốn thời gian nội bộ, người duyệt bắt được trước khi ra ngoài |
| 5 | **Có người vận hành và duyệt** | Không ai nhận | Có người nhưng chưa có thời gian rõ | Có người cụ thể, có thời gian mỗi ngày, hiểu việc đó |

**Xếp tầng theo tổng điểm**

| Tổng | Tầng | Ý nghĩa |
|:--:|---|---|
| 8 đến 10 | **Làm ngay** trong 30 ngày | Tối đa 3 đề xuất. Nếu nhiều hơn 3 đạt điểm, ưu tiên theo tiêu chí 1, rồi tiêu chí 5. |
| 5 đến 7 | **Kế tiếp** trong 60 đến 90 ngày | Ghi rõ điều kiện phải xong trước khi bắt đầu, thường là gom dữ liệu hoặc viết quy trình. |
| 0 đến 4 | **Chưa nên** | Ghi lý do và điều kiện để xét lại. |

**Ba điều kiện chặn.** Vi phạm một cái là xuống "Chưa nên" bất kể điểm:

1. **Chưa có quy trình mô tả được.** Đánh dấu ⚪ ở bảng quy trình. Đề xuất thay thế là viết quy trình bằng `/sop-builder`.
2. **Dữ liệu cá nhân của khách chưa có cơ sở thu thập hoặc chưa xin đồng ý.** Áp dụng cho mọi việc nhắn tin chủ động, ghi âm cuộc gọi, phân tích hồ sơ khách. Đề xuất thay thế là bổ sung bước xin đồng ý, tham chiếu `/tuan-thu-nganh-vn`.
3. **Không ai nhận vận hành và duyệt.** Bản đồ vẫn viết, tầng làm ngay để trống và nói thẳng lý do.

**Điều chỉnh theo Hồ Sơ Mô Hình Kinh Doanh**

- `chu-ky-ban-ngay` dưới 30 → mọi đề xuất về tốc độ phản hồi (A3, A4) cộng 1 vào tiêu chí 1 nếu chưa đạt 2, vì mỗi giờ chậm đều có giá.
- `mua-vu: co-mua` → đề xuất tầng làm ngay phải hoàn tất trước tháng cao điểm ít nhất 6 tuần; không kịp thì dời sang sau mùa, ghi rõ.
- `so-huu-diem-cham: ban-tren-san` → A3 trọng tâm là inbox sàn và kéo khách về kênh mình sở hữu sau mua; A2 phần đo lấy số từ sàn.
- `mo-hinh-mua-lai: lien-tuc` → A6 phần cảnh báo sắp rời và A7 nhóm khách có nguy cơ được ưu tiên. `theo-ky` → A6 phần nhắc trước điểm tái quyết định.
- `nguoi-mua-la-nguoi-dung: khong` → A3 và A6 phải phân biệt hai nhóm người nhận tin, không dùng một kịch bản chung.

---

## Phần 2 — Danh mục tám họ hệ thống agent

Mỗi họ có: bài toán, các thành phần (có thể chọn một phần), việc agent làm, người vẫn duyệt, dữ liệu cần, chỉ số đo, rủi ro và cách chặn, điều kiện sẵn sàng. Không nêu tên công cụ hay nhà cung cấp. Khi viết đề xuất, chép khung này ra và điền bằng dữ kiện thật của doanh nghiệp.

### A1 — Agent nội dung

**Bài toán.** Nội dung ra không đều, phụ thuộc một người, ý tưởng cạn, giọng lệch giữa các bài, bài tốt đăng một lần rồi bỏ.

**Thành phần**
- Gom ý tưởng từ câu hỏi thật của khách (inbox, cuộc gọi, bình luận) và từ trụ cột nội dung.
- Nháp bài theo giọng thương hiệu, có dẫn bằng chứng từ thư viện lời khách.
- Biến một bài dài thành nhiều định dạng: bài ngắn, kịch bản video, tin nhắn chăm sóc.
- Đề xuất lịch đăng theo mùa vụ và chu kỳ bán.

**Việc agent làm.** Đọc trụ cột, giọng thương hiệu, thư viện câu hỏi khách; nháp bài kèm nguồn; xếp lịch nháp.
**Người vẫn duyệt.** Chủ hoặc người phụ trách nội dung duyệt từng bài trước đăng trong 30 ngày đầu. Mọi con số, cam kết, giá trong bài phải có nguồn trong vault.
**Dữ liệu cần.** `Trụ Cột Nội Dung.md`, `Brand Voice`, thư viện lời khách, danh sách câu hỏi lặp từ lượt 3.
**Chỉ số đo.** Số bài ra mỗi tuần so với kế hoạch; thời gian từ ý tới đăng; tỷ lệ bài được duyệt không sửa lớn; sau 60 ngày, lead đến từ nội dung.
**Rủi ro và cách chặn.** Bịa số liệu hoặc cam kết: bắt buộc dẫn nguồn. Mất giọng: chấm theo Brand Voice trước khi trình duyệt. Trùng lặp: đối chiếu với `Content Đã Đăng/`.
**Điều kiện sẵn sàng.** Đã có trụ cột và giọng thương hiệu. Chưa có thì chạy `/content-pillar-builder`, `/brand-voice-guide` trước.

### A2 — Agent quảng cáo và đo chất lượng quảng cáo

**Bài toán.** Bài quảng cáo chạy theo cảm tính, không ai chấm trước khi chạy, số xem theo tuần trong khi tiền cháy theo giờ, phát hiện lỗ muộn.

**Thành phần**
- Nháp biến thể quảng cáo theo giả thuyết thử nghiệm, từ nội dung đã chạy tốt.
- Chấm điểm nội dung quảng cáo trước khi chạy: đúng phân khúc, đúng giá trị, có bằng chứng, không vi phạm quy định ngành.
- Đọc số theo giờ, so với đường nền, cảnh báo bất thường về chi phí mỗi lead, mỗi đơn.
- Đề xuất một trong các mức hành động: giữ, theo dõi, kiểm tra, giảm ngân sách, dừng, tăng. Người quyết.

**Việc agent làm.** Chấm và ghi lý do cho từng bài; kéo số theo nhịp; so với ngưỡng đã thống nhất; đề xuất hành động kèm bằng chứng.
**Người vẫn duyệt.** Người chạy quảng cáo quyết mọi thay đổi ngân sách. Chủ duyệt mức chi mỗi tháng. Agent không tự tắt, tự tăng trong 30 ngày đầu.
**Dữ liệu cần.** Chi phí mục tiêu mỗi lead hoặc mỗi đơn; số theo giờ ít nhất 7 ngày để có đường nền; danh sách quy định ngành về quảng cáo.
**Chỉ số đo.** Chi phí mỗi lead theo tuần; số giờ từ lúc bất thường tới lúc có người xử lý; tỷ lệ bài bị chấm rớt trước khi chạy.
**Rủi ro và cách chặn.** Tắt nhầm quảng cáo đang tốt: chỉ đề xuất, không thực thi. Cảnh báo giả khi mẫu ít: có cổng đủ mẫu, kéo dài ít nhất 2 giờ mới báo.
**Điều kiện sẵn sàng.** Đang chạy quảng cáo có ngân sách đều và biết hoặc sẵn sàng đặt chi phí mục tiêu. Không biết chi phí mỗi lead → chỉ làm phần chấm điểm trước khi chạy.

### A3 — Agent nhắn tin đa kênh

**Bài toán.** Lead nhắn qua Facebook, Zalo, inbox sàn ngoài giờ không ai trả lời; ba câu hỏi lặp chiếm phần lớn inbox; mỗi nhân viên trả lời một kiểu; khách cũ nhắn nhưng người trả lời không biết họ là ai.

**Thành phần**
- Trả lời câu hỏi lặp bằng câu chuẩn đã duyệt, có nhãn là trợ lý.
- Giữ khách ngoài giờ: ghi nhu cầu, hẹn người thật liên hệ trong ngưỡng chạm lead nóng.
- Phân loại tin: mua ngay, hỏi thông tin, khiếu nại, rác; chuyển đúng người.
- Gợi ý câu trả lời cho nhân viên với các tin ngoài mẫu, người gửi.

**Việc agent làm.** Nhận tin từ các kênh, đối chiếu câu hỏi lặp, trả lời hoặc gợi ý, gắn nhãn, chuyển người khi khách hỏi giá thương lượng, khiếu nại, hoặc yêu cầu người thật.
**Người vẫn duyệt.** Bộ câu trả lời chuẩn được chủ duyệt trước. Nhân viên duyệt từng gợi ý ngoài mẫu. Không tự hứa giá, thời hạn, cam kết.
**Dữ liệu cần.** Danh sách câu hỏi lặp và câu trả lời chuẩn; thông tin gói và giá niêm yết; cơ sở đồng ý nhận tin của khách.
**Chỉ số đo.** Thời gian phản hồi đầu tiên theo giờ trong ngày; tỷ lệ lead ngoài giờ được người thật gọi lại trong ngưỡng; tỷ lệ tin cần chuyển người; số lời phàn nàn về trả lời máy.
**Rủi ro và cách chặn.** Giả người: luôn có nhãn, chuyển người khi được hỏi. Nói sai giá: chỉ dùng giá niêm yết, giá thương lượng chuyển người. Nhắn quá nhiều: chỉ trả lời khi khách nhắn trước, nhắn chủ động thuộc A6 và cần đồng ý.
**Điều kiện sẵn sàng.** Có ít nhất 5 câu hỏi lặp với câu trả lời chuẩn được duyệt. Chưa có thì viết bộ câu trả lời trước, dùng `/chot-don-qua-inbox`.

### A4 — Agent chấm điểm lead và CRM

**Bài toán.** Lead ghi tay hoặc không ghi, không phân loại nóng lạnh, nhắc lại tuỳ trí nhớ, deal treo không ai biết lần cuối chạm, dữ liệu rời theo nhân viên.

**Thành phần**
- Điền hồ sơ lead từ hội thoại: tên, nhu cầu, ngân sách, nguồn, phân khúc.
- Chấm điểm nóng lạnh theo tín hiệu lead tốt đã có trong PK*.md.
- Nhắc chạm theo ngưỡng từ Hồ Sơ MHKD: chạm lead nóng, nhắc sau báo giá ở 5%, 15%, 30% chu kỳ bán, trả lead về nhóm chung sau 1,5 chu kỳ.
- Cảnh báo deal trễ hạn và lead sắp hết hạn giữ.

**Việc agent làm.** Đọc hội thoại và biên bản, đề xuất cập nhật hồ sơ, tính điểm, tạo nhắc việc cho đúng người, báo danh sách deal treo mỗi ngày.
**Người vẫn duyệt.** Nhân viên xác nhận hồ sơ trước khi lưu. Người quản lý bán hàng quyết chuyển lead. Agent không nhắn khách trực tiếp.
**Dữ liệu cần.** Một chỗ chứa hồ sơ lead mà cả đội dùng chung (`People/`, `Sales Pipeline & CRM/` hoặc phần mềm của doanh nghiệp); tín hiệu lead tốt từ MHKD; 6 tham số.
**Chỉ số đo.** Tỷ lệ lead có hồ sơ đủ 6 trường; tỷ lệ lead nóng được chạm trong ngưỡng; số deal treo quá hạn; tỷ lệ chốt theo nhóm điểm.
**Rủi ro và cách chặn.** Chấm sai làm bỏ lead tốt: so tỷ lệ chốt giữa các nhóm điểm mỗi tháng, chỉnh tiêu chí. Dữ liệu cá nhân: chỉ lưu trường cần cho bán hàng, có cơ sở thu thập.
**Điều kiện sẵn sàng.** Dữ liệu lead đã hoặc sẽ gom về một chỗ trong 2 tuần. Còn trong điện thoại cá nhân → đề xuất bước gom trước, dùng `/ghi-cuoc-gap` để giảm ma sát ghi.

### A5 — Agent phân tích cuộc gọi

**Bài toán.** Cuộc gọi tư vấn và chăm sóc không được ghi lại, kiến thức nằm trong đầu người giỏi nhất, không biết vì sao mất deal, nhân viên mới học bằng cách nghe lỏm, chất lượng chăm sóc qua điện thoại không đo được.

**Thành phần**
- Chuyển lời cuộc gọi thành văn bản và tóm tắt: nhu cầu, phản đối, cam kết, bước tiếp.
- Cập nhật pipeline và hồ sơ khách từ tóm tắt, người xác nhận.
- Chấm chất lượng cuộc gọi theo bảng tiêu chí đã thống nhất: mở đầu, hỏi nhu cầu, xử lý từ chối, chốt bước tiếp, thái độ.
- Gom mẫu câu tốt của người giỏi thành tài liệu đào tạo; gom lý do mất deal thành danh sách phản đối cho A3 và `/objection-handler`.

**Việc agent làm.** Xử lý bản ghi âm đã có sự đồng ý, tạo tóm tắt và điểm chất lượng, đề xuất cập nhật hồ sơ, tổng hợp theo tuần.
**Người vẫn duyệt.** Nhân viên xác nhận tóm tắt trước khi lưu. Quản lý xem điểm chất lượng và quyết việc huấn luyện. Điểm chất lượng không dùng để phạt trong 60 ngày đầu.
**Dữ liệu cần.** Bản ghi âm có thông báo và đồng ý của khách; bảng tiêu chí chất lượng cuộc gọi; danh sách phản đối thường gặp từ MHKD.
**Chỉ số đo.** Tỷ lệ cuộc gọi có tóm tắt trong ngày; thời gian nhân viên mới đạt điểm trung bình đội; số phản đối mới phát hiện mỗi tháng; tỷ lệ chốt theo điểm chất lượng.
**Rủi ro và cách chặn.** Ghi âm không đồng ý: điều kiện chặn số 2, bắt buộc thông báo đầu cuộc gọi. Nhận dạng sai tiếng Việt vùng miền và thuật ngữ ngành: người xác nhận tóm tắt, xây từ điển thuật ngữ. Nhân viên thấy bị giám sát: công bố tiêu chí trước, dùng để huấn luyện.
**Điều kiện sẵn sàng.** Đã hoặc có thể ghi âm hợp lệ, và có ít nhất 20 cuộc gọi một tuần để đáng công.

### A6 — Agent chăm sóc sau bán và mua lại

**Bài toán.** Sau khi trả tiền khách bị bỏ quên, không ai hướng dẫn, không xin đánh giá, không nhắc mua lại, khách rời đi không ai biết.

**Thành phần**
- Gửi lộ trình sau bán theo mốc: xác nhận, hướng dẫn, kiểm tra hài lòng, xin đánh giá.
- Nhắc mua lại hoặc gia hạn theo `mo-hinh-mua-lai` và `chu-ky-tieu-dung-ngay`; với `theo-ky` dồn vào cửa sổ trước điểm tái quyết định.
- Cảnh báo khách sắp rời theo dấu hiệu: im lặng lâu, khiếu nại, giảm dùng.
- Phân loại và nháp trả lời khiếu nại, người gửi.

**Việc agent làm.** Theo dõi mốc thời gian từng khách, nháp tin theo mẫu đã duyệt, gắn cờ cần người, tổng hợp danh sách nên gọi trong tuần.
**Người vẫn duyệt.** Bộ tin mẫu do chủ duyệt. Tin khiếu nại và tin cho khách giá trị cao do người gửi. Không hứa đền bù, giảm giá.
**Dữ liệu cần.** Ngày mua, sản phẩm, giá trị, kênh liên hệ, đồng ý nhận tin; lộ trình sau bán đã viết; 6 tham số.
**Chỉ số đo.** Tỷ lệ khách nhận đủ lộ trình; tỷ lệ mua lại hoặc gia hạn; số đánh giá thu về mỗi tháng; thời gian xử lý khiếu nại; số khách được gọi trước khi rời.
**Rủi ro và cách chặn.** Nhắn quá nhiều thành làm phiền: tần suất tối đa ghi trong mẫu, khách từ chối là dừng ngay. Nhắn sai người khi người mua khác người dùng: tách hai kịch bản.
**Điều kiện sẵn sàng.** Có lộ trình sau bán thành văn. Chưa có thì `/onboarding-flow`, `/customer-success-playbook` trước.

### A7 — Agent phân tích khách hàng và tự đề xuất

**Bài toán.** Không biết nhóm khách nào sinh lời, khách nào sắp rời, ai nên được mời mua thêm; quyết định marketing dựa vào cảm giác; dữ liệu có nhưng không ai đọc.

**Thành phần**
- Phân nhóm khách theo giá trị, tần suất, thời gian từ lần mua cuối, sản phẩm, kênh.
- Tìm điểm chung của nhóm khách tốt để quay lại chỉnh phân khúc và nội dung.
- Tìm khách có dấu hiệu rời và cơ hội bán thêm, bán chéo.
- Mỗi tuần đề xuất 3 việc nên làm kèm bằng chứng, người quyết.

**Việc agent làm.** Đọc dữ liệu khách đã gom, tính nhóm, so với kỳ trước, viết bản đề xuất tuần bằng tiếng Việt dễ hiểu, tách fact và suy luận.
**Người vẫn duyệt.** Chủ quyết việc nào làm. Mọi thay đổi giá, ưu đãi, phân khúc ghi vào `Decisions/` sau khi chủ xác nhận.
**Dữ liệu cần.** Tối thiểu 4 trường cho mỗi giao dịch: ngày, khách, giá trị, sản phẩm; tốt hơn nếu có kênh và phân khúc; ít nhất 3 tháng dữ liệu hoặc 100 giao dịch.
**Chỉ số đo.** Số đề xuất được thực hiện mỗi tháng; kết quả của đề xuất so với kỳ vọng; tỷ lệ khách sắp rời được giữ lại; doanh thu từ bán thêm.
**Rủi ro và cách chặn.** Kết luận từ mẫu nhỏ: ghi rõ số quan sát, gắn `⚠️ giả định` khi dưới ngưỡng. Phân biệt đối xử theo dữ liệu cá nhân nhạy cảm: không dùng trường không liên quan tới hành vi mua.
**Điều kiện sẵn sàng.** Dữ liệu giao dịch đã gom ở một chỗ. Chưa có thì đề xuất đầu tiên là bảng 4 trường, không phải agent.

### A8 — Agent báo cáo Sale & Marketing

**Bài toán.** Báo cáo gom tay từ nhiều nguồn, mất nhiều giờ, ra muộn, đọc xong không biết vì sao tăng giảm, chủ không có ba con số để nhìn mỗi tuần.

**Thành phần**
- Gom số từ các nguồn theo nhịp đọc số của Hồ Sơ MHKD: tuần, hai tuần, hoặc tháng.
- Trình bày ba con số chủ đã chọn ở lượt 7, so kỳ trước.
- Giải thích tăng giảm bằng cách nối với sự kiện: chiến dịch, mùa, thay đổi giá, sự cố.
- Cảnh báo khi một chỉ số lệch khỏi đường nền.

**Việc agent làm.** Kéo số, kiểm tra khớp giữa nguồn, viết báo cáo ngắn theo mẫu `Analytics & Reporting/`, nêu 1 đến 2 câu hỏi cần chủ trả lời.
**Người vẫn duyệt.** Người phụ trách đối chiếu số trước khi gửi trong 30 ngày đầu. Chủ quyết hành động.
**Dữ liệu cần.** Ba chỉ số đã chốt; nguồn số có thể truy cập; lịch sự kiện marketing và bán hàng để giải thích.
**Chỉ số đo.** Giờ làm báo cáo mỗi kỳ; ngày báo cáo ra so với kế hoạch; số quyết định trích dẫn báo cáo.
**Rủi ro và cách chặn.** Số lệch giữa nguồn: ghi rõ nguồn nào, không tự làm tròn. Giải thích suy diễn: gắn nhãn suy luận, không viết như fact.
**Điều kiện sẵn sàng.** Đã chốt ba chỉ số. Chưa có thì `/mkt-kpi-dashboard` trước.

---

## Phần 3 — Bối cảnh doanh nghiệp Việt cần nhớ khi chấm

- **Bán qua inbox là chuẩn.** Phần lớn lead đến qua tin nhắn Facebook, Zalo, sàn thương mại điện tử, và khách kỳ vọng trả lời trong vài phút kể cả buổi tối. Trả lời chậm là mất khách sang người bán kế bên. A3 vì thế thường có tác động dòng tiền cao ở doanh nghiệp bán lẻ và dịch vụ cá nhân.
- **Chủ kiêm nhiều vai.** Ở đội dưới 10 người, chủ thường tự chốt, tự duyệt nội dung, tự xem quảng cáo. Agent giảm việc chuẩn bị cho chủ có giá trị hơn agent thay nhân viên.
- **Dữ liệu nằm trong điện thoại cá nhân.** Đây là điểm chặn phổ biến nhất cho A4 và A7. Đề xuất đầu tiên thường là gom dữ liệu, không phải AI. Nói thẳng điều này, người dùng sẽ cảm ơn.
- **Giá thường thương lượng.** Nhiều ngành B2B và dịch vụ báo giá theo từng khách. AI nháp từ mẫu, người quyết. Không đề xuất AI quyết giá trong bất kỳ tầng nào.
- **Tết và mùa vụ.** Nhu cầu nhiều ngành dồn vào vài tháng. Triển khai giữa mùa cao điểm là thất bại chắc chắn. Đọc `mua-vu` và `thang-cao-diem` trước khi xếp lịch 30 ngày.
- **Nhắn tin hàng loạt gây khó chịu và có quy định.** Khách Việt nhạy với tin nhắn quảng cáo không xin phép. Mọi đề xuất nhắn chủ động phải có cơ sở đồng ý và tần suất tối đa. Không nêu tên nền tảng nhắn tin hay quy định cụ thể trong bản đồ; tham chiếu `/tuan-thu-nganh-vn` để kiểm tra.
- **Khách muốn biết đang nói với người hay máy.** Máy có nhãn, chuyển người ngay khi được hỏi, không dùng tên người thật cho máy.
- **Ngân sách công cụ tính bằng vài trăm nghìn tới vài triệu đồng một tháng.** Đề xuất phải có mức thử với chi phí gần 0 trước khi khuyên chi. Ghi chi phí theo khoảng VND và gắn `⚠️ giả định` khi chưa khảo giá.
- **Tiếng Việt vùng miền và thuật ngữ ngành.** A3 và A5 sẽ hiểu sai một phần. Người xác nhận và từ điển thuật ngữ là bắt buộc trong 30 ngày đầu.
- **Đo lường thường chưa có.** Nhiều câu hỏi về tỷ lệ sẽ nhận câu trả lời "chưa đo". Đừng coi là thiếu sót của người dùng, coi là phát hiện, và mục "Dữ liệu cần gom trước" của bản đồ là nơi ghi lại.
