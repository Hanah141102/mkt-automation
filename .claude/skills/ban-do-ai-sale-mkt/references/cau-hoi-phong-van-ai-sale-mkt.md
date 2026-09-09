# Bộ câu hỏi phỏng vấn — Bản đồ ứng dụng AI vào Sale & Marketing

Sáu lượt, đi theo dòng chảy của khách hàng. Mỗi lượt có **câu hỏi chính** (hỏi cùng lúc trong một lượt), **câu đào sâu** (chỉ dùng khi câu trả lời còn chung chung, tối đa 2 câu mỗi lượt), và **dấu hiệu cần ghi lại** (để Claude tự nhận ra cơ hội, không cần hỏi người dùng).

Không đọc nguyên văn. Dùng làm khung để trò chuyện tự nhiên với chủ doanh nghiệp Việt: câu ngắn, ví dụ gần, gọi "anh chị".

Với **mỗi bước quy trình** người dùng kể ra, cố lấy đủ sáu ô: **ai làm · bao nhiêu lần một tuần · mất bao lâu một lần · dùng gì · hay lỗi ở đâu · để lại dữ liệu gì**. Thiếu ô nào thì hỏi thêm. Người dùng không biết thì ghi "chưa đo", đó là một phát hiện.

---

## Trước khi hỏi: những gì đã có trong vault, không hỏi lại

Từ `Hồ Sơ Mô Hình Kinh Doanh.md`, BMC và MHKD đã biết: loại sản phẩm, chu kỳ bán, người mua có là người dùng, mùa vụ, giao dịch xảy ra ở đâu, mô hình mua lại, phân khúc, kênh, tín hiệu lead tốt, phản đối thường gặp. Tóm tắt lại 8 đến 12 dòng, hỏi "đúng chưa, có gì đổi so với lúc dựng mô hình không?", rồi vào lượt 1.

---

## Lượt 1 — Đội ngũ, công cụ, dữ liệu, ranh giới

Mục tiêu: biết ai đang làm gì, dữ liệu khách nằm ở đâu, có gì không được đụng. Lượt này quyết định tiêu chí "có người vận hành" và điều kiện chặn về dữ liệu cá nhân.

**Câu hỏi chính**

1. Hiện ai lo marketing, ai lo bán hàng, ai lo chăm sóc khách? Bao nhiêu người, có ai kiêm nhiều vai không? Anh chị tự tay làm bước nào?
2. Thông tin khách hàng và lead đang nằm ở đâu? Trong điện thoại nhân viên, trong file bảng tính, trong phần mềm quản lý khách, hay rải ở nhiều chỗ? Nếu một nhân viên nghỉ, dữ liệu khách của người đó có ở lại công ty không?
3. Đội đã dùng AI vào việc gì chưa, dù chỉ là hỏi chatbot? Kết quả thế nào, vì sao dừng hoặc tiếp?
4. Mỗi tháng đang chi bao nhiêu cho công cụ marketing, bán hàng, quảng cáo? Sẵn sàng thêm khoảng bao nhiêu nếu thấy đáng?
5. Ngành của anh chị có quy định gì về quảng cáo, nhắn tin cho khách, hay dữ liệu khách mà mình phải tuân theo không? Khách có từng phàn nàn vì bị nhắn quá nhiều chưa?
6. Có việc nào anh chị nói ngay từ đầu là **không bao giờ** để máy tự làm? Vì sao?

**Câu đào sâu**

- "Nhân viên mới vào, mất bao lâu để họ tự trả lời khách được?" (đo mức độ quy trình đã thành văn)
- "Khách đồng ý cho mình nhắn tin lại bằng cách nào, hay mình cứ nhắn?" (cơ sở thu thập và đồng ý)

**Dấu hiệu cần ghi lại**

- Dữ liệu khách nằm trong điện thoại cá nhân → mọi agent CRM (A4, A7) bị chặn cho tới khi gom dữ liệu về một chỗ; đề xuất đầu tiên có thể là "gom dữ liệu", không phải AI.
- Chủ tự làm bước chốt hoặc bước trả lời inbox → điểm nghẽn năng lực nằm ở chủ; ưu tiên agent giảm việc cho chủ.
- Không có cơ sở đồng ý nhắn tin → mọi đề xuất nhắn tin chủ động (A3, A6) phải kèm bước xin đồng ý trước.
- Ngân sách công cụ hiện tại bằng 0 → tầng làm ngay phải là việc dùng được với chi phí gần 0.

---

## Lượt 2 — Thu hút: nội dung, quảng cáo, kênh

Mục tiêu: tìm việc lặp lại và chỗ tốn thời gian nhất trong marketing. Phục vụ A1 và A2.

**Câu hỏi chính**

1. Khách mới chủ yếu biết đến mình qua đâu? Kể theo thứ tự nhiều tới ít. Kênh nào anh chị chủ động làm, kênh nào tự nhiên đến?
2. Nội dung (bài đăng, video, bài viết dài) ai làm? Một tuần ra bao nhiêu bài, mỗi bài mất bao lâu từ lúc nghĩ ý tới lúc đăng? Ý tưởng lấy từ đâu?
3. Có chạy quảng cáo không? Ai chạy, chi bao nhiêu một tháng, có biết một lead hoặc một đơn từ quảng cáo tốn bao nhiêu tiền không? Bao lâu xem số một lần, và nhìn số nào để quyết định tắt hay tăng?
4. Trước khi một bài quảng cáo chạy, ai duyệt và duyệt theo tiêu chí gì? Đã từng có bài chạy sai, chạy lỗ mà phát hiện muộn chưa?
5. Trong toàn bộ việc marketing, việc nào anh chị hoặc đội thấy **nhàm nhất, lặp lại nhất**? Việc nào **tốn giờ nhất**?

**Câu đào sâu**

- "Bài nào chạy tốt thì có làm lại thành dạng khác không, hay đăng một lần rồi bỏ?" (cơ hội tái sử dụng)
- "Nếu người viết nội dung nghỉ hai tuần, kênh có im không?" (phụ thuộc cá nhân)

**Dấu hiệu cần ghi lại**

- Có trụ cột nội dung và giọng thương hiệu trong vault → A1 sẵn sàng về dữ liệu. Chưa có → đề xuất `/content-pillar-builder` và `/brand-voice-guide` trước A1.
- Quảng cáo không biết chi phí mỗi lead → A2 phần "đo" chưa có dữ liệu để đo; phần "chấm điểm nội dung trước khi chạy" vẫn làm được.
- Xem số quảng cáo theo tuần trong khi chu kỳ bán ngắn dưới 30 ngày → cơ hội cho phần "đọc số theo giờ, cảnh báo bất thường" của A2.
- Nội dung chỉ lấy ý từ đầu người viết, không từ câu hỏi khách → A1 nên nối với dữ liệu inbox và cuộc gọi (A3, A5).

---

## Lượt 3 — Lead vào và phản hồi đầu

Mục tiêu: tốc độ phản hồi, câu hỏi lặp, lead rơi ở cửa. Phục vụ A3 và A4. Đây thường là nơi mất tiền nhiều nhất ở doanh nghiệp Việt bán qua inbox.

**Câu hỏi chính**

1. Một lead mới xuất hiện qua đâu: tin nhắn Facebook, Zalo, bình luận, điền form, gọi điện, inbox trên sàn, người quen giới thiệu? Mỗi kênh khoảng bao nhiêu lead một tuần?
2. Ai trả lời tin nhắn đầu tiên? Trong bao lâu kể từ khi khách nhắn? Buổi tối, cuối tuần, lễ Tết thì sao?
3. Ba câu khách hỏi nhiều nhất là gì? Đội trả lời bằng cách gõ tay, dán mẫu, hay mỗi người một kiểu?
4. Sau khi trả lời, lead được ghi lại ở đâu? Ghi những gì: tên, số điện thoại, nhu cầu, ngân sách, nguồn? Có phân loại nóng lạnh không, dựa vào gì?
5. Ước chừng bao nhiêu phần trăm lead vào là **hỏi cho biết** hoặc rác? Bao nhiêu phần trăm lead tử tế bị **quên trả lời hoặc trả lời chậm** đến mức mất?

**Câu đào sâu**

- "Khách nhắn lúc 10 giờ tối, sáng hôm sau mình trả lời, đã bao giờ khách bảo 'em mua chỗ khác rồi' chưa?" (chi phí của trả lời chậm)
- "Người trả lời inbox có biết khách đó đã từng mua chưa không?" (dữ liệu nối giữa kênh và CRM)

**Dấu hiệu cần ghi lại**

- Có 3 đến 5 câu hỏi lặp chiếm phần lớn inbox → A3 phần "trả lời câu hỏi lặp" điểm cao về độ lặp và dữ liệu sẵn.
- Không ai trả lời ngoài giờ trong khi chu kỳ bán ngắn → A3 phần "giữ khách ngoài giờ, hẹn người thật" là điểm chặn dòng tiền.
- Lead ghi tay hoặc không ghi → A4 phần "điền hồ sơ lead từ hội thoại" giải đúng nỗi đau; nhưng cần chỗ chứa dữ liệu trước.
- Không phân loại nóng lạnh → A4 phần "chấm điểm" dựa vào tín hiệu lead tốt đã có trong PK*.md.
- Ngưỡng chạm lead nóng lấy từ Hồ Sơ MHKD: 15 phút nếu chu kỳ dưới 30 ngày, 4 giờ nếu từ 30 ngày. So với thực tế người dùng kể để chỉ ra khoảng cách.

---

## Lượt 4 — Tư vấn và chốt

Mục tiêu: báo giá, nhắc lại, lý do mất deal, chủ can dự chỗ nào. Phục vụ A4, A5.

**Câu hỏi chính**

1. Từ lúc lead tử tế tới lúc khách trả tiền, đi qua những bước gì? Kể theo thứ tự: gọi, hẹn gặp, demo, báo giá, thương lượng, ký, thanh toán... Bước nào hay tắc?
2. Báo giá làm thế nào, ai làm, mất bao lâu? Giá cố định hay thương lượng từng khách? Ai được quyền giảm giá, giảm tới đâu?
3. Sau khi báo giá, ai nhắc lại khách, nhắc bao nhiêu lần, cách nhau bao lâu? Có bao giờ quên nhắc không? Có bao giờ nhắc quá nhiều khiến khách khó chịu không?
4. Cuộc gọi hoặc buổi gặp tư vấn có ghi âm, ghi chú gì lại không? Ai đọc lại? Nhân viên mới học cách tư vấn bằng cách nào?
5. Ba lý do mất deal hay gặp nhất? Khách từ chối bằng câu gì? Đội trả lời câu đó thế nào, có câu trả lời chuẩn chưa?
6. Bao nhiêu phần trăm lead tử tế thành khách? Bước nào anh chị **phải tự ra tay** thì mới chốt được?

**Câu đào sâu**

- "Tuần này có bao nhiêu deal đang treo mà không ai biết lần cuối chạm là khi nào?" (sức khoẻ pipeline)
- "Nhân viên tư vấn giỏi nhất khác người còn lại ở câu nói nào?" (kiến thức ngầm có thể chuẩn hoá)

**Dấu hiệu cần ghi lại**

- Quên nhắc lại hoặc nhắc không đều → A4 phần "nhắc chạm theo 5%, 15%, 30% chu kỳ bán" điểm cao về dòng tiền.
- Có ghi âm cuộc gọi hoặc sẵn sàng ghi âm với sự đồng ý của khách → A5 khả thi; không có và không thể ghi → A5 xuống tầng chưa nên.
- Báo giá thương lượng từng khách và chủ quyết → AI chỉ nháp báo giá từ mẫu, **không** đề xuất AI quyết giá. Ghi vào "AI không làm".
- Không có câu trả lời chuẩn cho từ chối → đề xuất `/objection-handler` trước, rồi A3/A4 dùng kết quả đó.
- Chủ phải tự chốt mọi deal → nút thắt năng lực; agent nào giảm việc chuẩn bị cho chủ (tóm tắt lead, nháp báo giá) sẽ có tác động lớn nhất.

---

## Lượt 5 — Sau bán và mua lại

Mục tiêu: chăm sóc, khiếu nại, xin giới thiệu, nhắc mua lại. Phục vụ A5, A6, A7. Bỏ lượt này là lỗi phổ biến nhất, vì doanh nghiệp Việt thường dồn sức vào kéo khách mới.

**Câu hỏi chính**

1. Sau khi khách trả tiền, chuyện gì xảy ra trong tuần đầu? Ai liên hệ, hướng dẫn gì, qua kênh nào? Có lộ trình cố định hay tuỳ người?
2. Khách khiếu nại hoặc hỏi hỗ trợ thì nhắn vào đâu, ai xử lý, trong bao lâu? Khiếu nại nào lặp lại nhiều nhất?
3. Có chủ động xin đánh giá, lời chứng thực, hay nhờ khách giới thiệu không? Xin lúc nào, ai xin, tỷ lệ khách đồng ý?
4. Với mô hình mua lại của anh chị (đã có trong Hồ Sơ MHKD), ai nhắc khách mua lại hoặc gia hạn? Nhắc trước bao lâu, dựa vào gì để biết đã đến lúc?
5. Anh chị có biết bao nhiêu phần trăm khách quay lại không? Khách rời đi thường vì lý do gì, và mình biết lý do đó bằng cách nào?
6. Có nhóm khách nào mua nhiều, ở lâu, ít phàn nàn không? Mình có biết họ là ai và họ giống nhau ở điểm gì không?

**Câu đào sâu**

- "Khách mua lần cuối cách đây 6 tháng, hôm nay có ai biết và gọi cho họ không?" (khách ngủ quên)
- "Đánh giá tốt của khách hiện nằm ở đâu, có ai đem vào nội dung bán hàng không?" (nối A6 với A1)

**Dấu hiệu cần ghi lại**

- Không có lộ trình sau bán → A6 phần "onboarding theo lộ trình" cần viết lộ trình trước, `/onboarding-flow`, rồi mới giao agent gửi nhắc.
- Không nhắc mua lại trong khi `mo-hinh-mua-lai` là `theo-ky` hoặc `lien-tuc` → A6 phần "nhắc mua lại, cảnh báo sắp rời" là điểm chặn dòng tiền rõ nhất.
- Không biết tỷ lệ quay lại và không biết nhóm khách tốt → A7 có bài toán rõ nhưng thiếu dữ liệu; đề xuất bước gom dữ liệu tối thiểu: ngày mua, giá trị, sản phẩm, kênh.
- Khiếu nại lặp lại một kiểu → vừa là đầu vào cho A3 (trả lời chuẩn), vừa là tín hiệu cho A7 (nguyên nhân gốc).
- Có nhiều đánh giá tốt chưa dùng → A1 có nguồn bằng chứng, nối với `/testimonial-collector`.

---

## Lượt 6 — Đo lường, quyết định, lo ngại

Mục tiêu: báo cáo, con số chủ xem, điều không bao giờ giao AI, người vận hành. Phục vụ A8 và phần "Ranh giới" của bản đồ.

**Câu hỏi chính**

1. Hiện có báo cáo marketing và bán hàng định kỳ không? Ai làm, mất bao lâu, gom số từ mấy nguồn? Anh chị có đọc không, đọc xong có làm gì khác đi không?
2. Nếu chỉ được xem **ba con số** mỗi tuần để biết bán hàng và marketing đang ổn hay không, anh chị chọn ba số nào? Hiện có số đó không?
3. Khi doanh thu tháng lên hoặc xuống, anh chị có giải thích được vì sao không? Thường mất bao lâu để tìm ra?
4. Điều gì làm anh chị **lo nhất** khi để AI tham gia vào bán hàng và chăm khách: nói sai thông tin, lộ dữ liệu khách, mất giọng của mình, khách biết là máy, hay tốn tiền không ra kết quả?
5. Nếu triển khai, ai trong đội sẽ là người **vận hành và kiểm tra mỗi ngày**? Người đó có thời gian không? Anh chị muốn duyệt ở mức nào: duyệt từng tin, duyệt theo mẫu, hay chỉ xem báo cáo?
6. Sau 30 ngày, anh chị muốn nhìn thấy điều gì thay đổi để nói "đáng"? Một con số, hay một cảm giác?

**Câu đào sâu**

- "Việc nào anh chị làm mỗi tuần mà thấy 'đáng lẽ máy làm được' nhưng chưa dám giao?" (cơ hội bị kìm bởi niềm tin)
- "Có quyết định nào trong 3 tháng qua mà nếu có số sớm hơn một tuần thì đã khác?" (giá trị của A8)

**Dấu hiệu cần ghi lại**

- Báo cáo gom tay từ 3 nguồn trở lên mất trên 2 giờ mỗi kỳ → A8 điểm cao về độ lặp; nhịp đọc số lấy từ Hồ Sơ MHKD, không bịa.
- Không chọn được ba con số → chưa nên làm A8; đề xuất `/mkt-kpi-dashboard` để chốt chỉ số trước.
- Lo "khách biết là máy" → mọi đề xuất A3, A6 phải ghi rõ nguyên tắc **minh bạch**: máy trả lời có nhãn, chuyển người khi khách hỏi, không giả người.
- Lo "nói sai thông tin" → tầng làm ngay giới hạn ở việc AI **nháp và gợi ý**, người gửi; đưa vào phần "Người vẫn duyệt".
- Không có người vận hành → điều kiện chặn thứ ba; bản đồ vẫn viết ra nhưng tầng làm ngay để trống và nói thẳng vì sao.
- Câu trả lời câu 6 là **chỉ số thành công** của kế hoạch 30 ngày trong file đầu ra. Không tự thay bằng chỉ số Claude nghĩ hay hơn.

---

## Sau sáu lượt: kiểm tra trước khi dựng bảng

- Mỗi giai đoạn (thu hút, lead vào, tư vấn chốt, sau bán, đo lường) có ít nhất một bước được mô tả đủ sáu ô chưa? Giai đoạn nào trống hoàn toàn, hỏi thêm một câu: "Giai đoạn này hiện gần như không có gì, đúng không?" Người dùng xác nhận thì ghi "chưa có quy trình", đừng tự lấp.
- Có bước nào người dùng kể hai lần với hai cách khác nhau không? Hỏi lại cho rõ.
- Có điểm đau nào nằm ngoài Sale & Marketing (kho, kế toán, nhân sự) không? Ghi một dòng "ngoài phạm vi", không đưa vào chấm điểm.
