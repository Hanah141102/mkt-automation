# Bộ câu hỏi phỏng vấn — Bản đồ ứng dụng AI vào Sale & Marketing

Bảy lượt, đi theo dòng chảy của khách hàng. Mỗi lượt có **câu hỏi chính** (hỏi cùng lúc trong một lượt), **câu đào sâu** (chỉ dùng khi câu trả lời còn chung chung, tối đa 2 đến 3 câu mỗi lượt), **bảng kiểm Người / Công cụ / Tự động / Không làm** (điền cùng người dùng ở cuối lượt), và **dấu hiệu cần ghi lại** (để Claude tự nhận ra cơ hội và nối sang đúng họ agent).

Không đọc nguyên văn. Dùng làm khung để trò chuyện tự nhiên với chủ doanh nghiệp Việt: câu ngắn, ví dụ gần, gọi "anh chị".

Với **mỗi bước quy trình** người dùng kể ra, cố lấy đủ sáu ô: **ai làm · bao nhiêu lần một tuần · mất bao lâu một lần · dùng gì · hay lỗi ở đâu · để lại dữ liệu gì**. Thiếu ô nào thì hỏi thêm. Người dùng không biết thì ghi "chưa đo", đó là một phát hiện.

## Bảng kiểm Người / Công cụ / Tự động / Không làm

Cuối mỗi lượt từ 2 đến 6, đọc danh sách việc của lượt đó và hỏi người dùng xếp từng việc vào một trong bốn ô:

| Ký hiệu | Nghĩa |
|:--:|---|
| 👤 **Người** | Người làm tay từ đầu tới cuối, không công cụ nào hỗ trợ ngoài gõ chữ |
| 🔧 **Công cụ** | Người làm, có công cụ hỗ trợ một phần (mẫu, bảng tính, phần mềm, chatbot hỏi nhanh) |
| ⚙️ **Tự động** | Chạy không cần người trong đa số trường hợp, người chỉ xem kết quả |
| ⛔ **Không làm** | Biết là nên nhưng hiện không ai làm |

Bảng này quan trọng hơn mọi câu hỏi khác vì nó cho thấy ngay **khoảng trống**: việc ở ô 👤 lặp lại nhiều là ứng viên cho agent, việc ở ô ⛔ nằm trên đường tiền là điểm chặn dòng tiền, việc ở ô ⚙️ cần hỏi thêm "có ai kiểm không". Kết quả ghi vào mục 2b của file đầu ra.

---

## Trước khi hỏi: những gì đã có trong vault, không hỏi lại

Từ `Hồ Sơ Mô Hình Kinh Doanh.md`, BMC và MHKD đã biết: loại sản phẩm, chu kỳ bán, người mua có là người dùng, mùa vụ, giao dịch xảy ra ở đâu, mô hình mua lại, phân khúc, kênh, tín hiệu lead tốt, phản đối thường gặp. Tóm tắt lại 8 đến 12 dòng, hỏi "đúng chưa, có gì đổi so với lúc dựng mô hình không?", rồi vào lượt 1.

---

## Lượt 1 — Đội ngũ, công cụ, dữ liệu, ranh giới

Mục tiêu: biết ai đang làm gì, dữ liệu khách nằm ở đâu, có gì không được đụng. Quyết định tiêu chí "có người vận hành" và điều kiện chặn về dữ liệu cá nhân.

**Câu hỏi chính**

1. Hiện ai lo marketing, ai lo bán hàng, ai lo chăm sóc khách? Bao nhiêu người, có ai kiêm nhiều vai không? Anh chị tự tay làm bước nào? Có thuê ngoài khâu nào không (agency, freelancer, cộng tác viên)?
2. Thông tin khách hàng và lead đang nằm ở đâu? Trong điện thoại nhân viên, trong file bảng tính, trong phần mềm quản lý khách, hay rải ở nhiều chỗ? Nếu một nhân viên nghỉ, dữ liệu khách của người đó có ở lại công ty không?
3. Đội đã dùng AI vào việc gì chưa, dù chỉ là hỏi chatbot? Kết quả thế nào, vì sao dừng hoặc tiếp?
4. Mỗi tháng đang chi bao nhiêu cho công cụ marketing, bán hàng, quảng cáo? Sẵn sàng thêm khoảng bao nhiêu nếu thấy đáng?
5. Ngành của anh chị có quy định gì về quảng cáo, nhắn tin cho khách, hay dữ liệu khách mà mình phải tuân theo không? Khách có từng phàn nàn vì bị nhắn quá nhiều chưa?
6. Có việc nào anh chị nói ngay từ đầu là **không bao giờ** để máy tự làm? Vì sao?

**Câu đào sâu**

- "Nhân viên mới vào, mất bao lâu để họ tự trả lời khách được?" (đo mức độ quy trình đã thành văn)
- "Khách đồng ý cho mình nhắn tin lại bằng cách nào, hay mình cứ nhắn?" (cơ sở thu thập và đồng ý)
- "Nếu anh chị nghỉ một tuần không cầm điện thoại, bước nào trong bán hàng và marketing dừng lại?" (phụ thuộc vào chủ)

**Dấu hiệu cần ghi lại**

- Dữ liệu khách nằm trong điện thoại cá nhân → mọi agent CRM (A4, A7) bị chặn cho tới khi gom dữ liệu về một chỗ; đề xuất đầu tiên có thể là "gom dữ liệu", không phải AI.
- Chủ tự làm bước chốt hoặc bước trả lời inbox → điểm nghẽn năng lực nằm ở chủ; ưu tiên agent giảm việc cho chủ.
- Không có cơ sở đồng ý nhắn tin → mọi đề xuất nhắn tin chủ động (A3, A6) phải kèm bước xin đồng ý trước.
- Ngân sách công cụ hiện tại bằng 0 → tầng làm ngay phải là việc dùng được với chi phí gần 0.
- Có thuê agency làm nội dung hoặc quảng cáo → hỏi thêm ở lượt 2 và 3 xem doanh nghiệp có giữ được dữ liệu và tài sản không.

---

## Lượt 2 — Nội dung: làm bằng ai, quy trình nào, đau ở đâu

Mục tiêu: vẽ được dây chuyền nội dung từ ý tưởng tới đo, biết khâu nào người làm tay, khâu nào bỏ trống. Phục vụ **A1 Agent nội dung**.

**Câu hỏi chính**

1. Đang làm những loại nội dung gì: bài viết ngắn, bài dài, hình, video ngắn, video dài, livestream, email, tin nhắn chăm sóc? Loại nào ra đều, loại nào lâu lâu mới có? Một tuần tổng cộng ra bao nhiêu?
2. Kể dây chuyền một bài từ đầu tới cuối: ai nghĩ ý, ai viết nháp, ai duyệt, ai làm hình hoặc dựng video, ai đăng, ai xem số. Mỗi khâu mất bao lâu và ai làm? Có khâu nào một người làm hết không?
3. Ý tưởng lấy từ đâu: từ đầu người viết, từ câu khách hỏi, từ đối thủ, từ xu hướng? Có lịch nội dung viết trước không, hay tới ngày mới nghĩ? Có trụ cột chủ đề cố định không?
4. Có kho tư liệu để lấy ra viết không: lời khách nói, đánh giá, ảnh thật, số liệu kết quả, câu chuyện khách? Nằm ở đâu, ai giữ, có dễ tìm không?
5. Ba nỗi đau lớn nhất về nội dung là gì? Gợi ý để họ chọn: trễ lịch, cạn ý, viết chậm, giọng mỗi bài một kiểu, không biết bài nào hiệu quả, bài tốt đăng một lần rồi bỏ, phụ thuộc một người, thuê ngoài không hiểu sản phẩm.
6. Ai duyệt nội dung trước khi đăng và duyệt theo gì? Có bài nào từng đăng sai giá, sai cam kết, sai giọng phải gỡ chưa?
7. Sau khi đăng, có xem bài nào tốt bài nào không? Xem số gì, ai xem, có dùng kết quả đó cho bài sau không?

**Câu đào sâu**

- "Một bài viết dài tốt có được cắt ra thành bài ngắn, kịch bản video, tin nhắn chăm sóc không?" (tái sử dụng)
- "Nếu người làm nội dung nghỉ hai tuần, kênh có im không?" (phụ thuộc cá nhân)
- "Khách hỏi câu gì nhiều nhất trong inbox mà chưa bao giờ thành bài đăng?" (nội dung từ dữ liệu khách)

**Bảng kiểm lượt 2** (xếp 👤 🔧 ⚙️ ⛔)

| Việc | Xếp |
|---|:--:|
| Gom ý tưởng từ câu hỏi khách và bình luận | |
| Lên lịch nội dung tháng theo trụ cột | |
| Viết nháp bài ngắn | |
| Viết nháp bài dài hoặc kịch bản video | |
| Tạo hình minh hoạ hoặc dựng video | |
| Kiểm giọng thương hiệu và kiểm sự thật trước khi đăng | |
| Biến một bài thành nhiều định dạng | |
| Đăng đúng giờ lên các kênh | |
| Trả lời bình luận dưới bài | |
| Đọc số và rút bài học cho bài sau | |
| Lưu bài đã đăng và kết quả vào một chỗ | |

**Dấu hiệu cần ghi lại**

- Nhiều ô 👤 ở "viết nháp", "biến một bài thành nhiều định dạng", "lên lịch" → A1 điểm cao về độ lặp. Có trụ cột và giọng thương hiệu trong vault → A1 sẵn dữ liệu; chưa có → `/content-pillar-builder`, `/brand-voice-guide` trước.
- ⛔ ở "gom ý tưởng từ câu hỏi khách" trong khi inbox có nhiều câu lặp (lượt 4) → A1 nối với A3, nguồn ý tưởng rẻ nhất đang bị bỏ.
- ⛔ ở "kiểm giọng và kiểm sự thật" hoặc từng đăng sai giá → A1 phải có bước kiểm tự động trước khi trình duyệt; đây cũng là "người vẫn duyệt".
- ⛔ ở "đọc số" → A1 phần lịch không có gì để học; nối với A8 hoặc ghi "chưa có dữ liệu".
- Thuê agency mà kho tư liệu và bài đăng không ở phía doanh nghiệp → đề xuất đầu tiên là kéo tài sản về `Content Đã Đăng/`.

---

## Lượt 3 — Quảng cáo và kênh thu hút

Mục tiêu: biết quảng cáo chạy bằng ai, đo bằng gì, mất tiền ở đâu. Phục vụ **A2 Agent quảng cáo và đo chất lượng quảng cáo**.

**Câu hỏi chính**

1. Khách mới chủ yếu biết đến mình qua đâu? Kể theo thứ tự nhiều tới ít. Kênh nào anh chị chủ động làm, kênh nào tự nhiên đến (giới thiệu, tìm kiếm, đi ngang)?
2. Có chạy quảng cáo không? Ai chạy (người trong đội, agency, hay tự bấm)? Chi bao nhiêu một tháng, trên kênh nào?
3. Có biết một lead hoặc một đơn từ quảng cáo tốn bao nhiêu tiền không? Có đặt mức chi phí tối đa chấp nhận được chưa? Bao lâu xem số một lần, nhìn số nào để quyết định tắt, giữ, tăng?
4. Trước khi một bài quảng cáo chạy, ai duyệt và duyệt theo tiêu chí gì? Đã từng có bài chạy sai đối tượng, chạy lỗ, hay bị từ chối vì vi phạm quy định mà phát hiện muộn chưa? Mất bao nhiêu tiền lần đó?
5. Có thử nhiều phiên bản một bài quảng cáo để so không? Ai nghĩ phiên bản, ai kết luận cái nào thắng, kết luận dựa vào gì?
6. Trong toàn bộ việc quảng cáo và kênh, việc nào **nhàm nhất, lặp lại nhất**? Việc nào **tốn giờ nhất**?

**Câu đào sâu**

- "Bài nào chạy tốt thì có làm lại thành dạng khác hay chạy lại mùa sau không?" (tái sử dụng)
- "Cuối tuần hoặc buổi tối quảng cáo vẫn chạy, có ai xem số không?" (điểm mù theo giờ)
- "Lead từ quảng cáo về có ghi rõ nguồn không, để biết tiền chi ra đơn nào?" (nối A2 với A4)

**Bảng kiểm lượt 3**

| Việc | Xếp |
|---|:--:|
| Viết nội dung quảng cáo và biến thể | |
| Chấm nội dung quảng cáo trước khi chạy: đúng phân khúc, có bằng chứng, đúng quy định | |
| Đặt ngân sách và mức chi phí tối đa mỗi lead | |
| Xem số theo ngày hoặc theo giờ | |
| Phát hiện bất thường: chi phí tăng, lead giảm | |
| Quyết tắt, giữ, tăng ngân sách | |
| Kết luận phiên bản nào thắng | |
| Ghi nguồn cho từng lead về | |
| Lưu bài quảng cáo và kết quả để dùng lại | |

**Dấu hiệu cần ghi lại**

- Không biết chi phí mỗi lead → A2 phần "đo" chưa có dữ liệu; phần "chấm điểm nội dung trước khi chạy" vẫn làm được và điểm cao nếu từng đăng sai.
- Xem số theo tuần trong khi chu kỳ bán ngắn dưới 30 ngày → A2 phần "đọc số theo giờ, cảnh báo bất thường" là điểm chặn dòng tiền.
- ⛔ ở "kết luận phiên bản nào thắng" → A2 phần thử nghiệm cần `/thu-nghiem-ab` để đặt luật trước.
- ⛔ ở "ghi nguồn cho lead" → A4 và A8 sẽ thiếu dữ liệu; ghi vào "Dữ liệu cần gom trước".
- Không chạy quảng cáo → bỏ A2, không ép.

---

## Lượt 4 — Lead vào và chăm sóc qua tin nhắn, mục tiêu 24/7

Mục tiêu: tốc độ phản hồi theo khung giờ, câu hỏi lặp, lead rơi ở cửa, và khách cũ hỏi hỗ trợ có đang trộn vào cùng inbox không. Phục vụ **A3 Agent nhắn tin đa kênh** và phần chăm sóc 24/7. Đây thường là nơi mất tiền nhiều nhất ở doanh nghiệp Việt bán qua inbox.

**Câu hỏi chính**

1. Một lead mới xuất hiện qua đâu: tin nhắn Facebook, Zalo, bình luận, điền form, gọi điện, inbox trên sàn, người quen giới thiệu? Mỗi kênh khoảng bao nhiêu tin một ngày? Khách hay nhắn giờ nào nhiều nhất, có nhiều tin buổi tối và cuối tuần không?
2. Ai trực inbox, trực theo ca hay ai rảnh thì trả lời? Trong bao lâu kể từ khi khách nhắn thì có người trả lời, trong giờ và ngoài giờ? Buổi tối, cuối tuần, lễ Tết thì sao?
3. Mười câu khách hỏi nhiều nhất là gì? Đội trả lời bằng gõ tay, dán mẫu, hay mỗi người một kiểu? Có bộ câu trả lời chuẩn thành văn chưa, ai viết, bao lâu cập nhật?
4. Trong inbox, tin của khách **cũ** hỏi hỗ trợ, hỏi đơn, khiếu nại có trộn chung với tin của lead **mới** không? Ai phân biệt, bằng cách nào? Người trả lời có biết khách đó đã từng mua gì chưa không?
5. Khiếu nại hoặc việc khẩn đến lúc 10 giờ tối thì chuyện gì xảy ra? Ai được gọi, bao lâu có người xử lý?
6. Sau khi trả lời, lead được ghi lại ở đâu? Ghi những gì: tên, số điện thoại, nhu cầu, ngân sách, nguồn, đã từng mua chưa? Có phân loại nóng lạnh không, dựa vào gì?
7. Ước chừng bao nhiêu phần trăm tin vào là **hỏi cho biết** hoặc rác? Bao nhiêu phần trăm lead tử tế bị **quên trả lời hoặc trả lời chậm** đến mức mất? Nếu chưa đo, kể một lần gần nhất mất khách vì trả lời chậm.
8. Nếu có máy trả lời tin ngoài giờ, anh chị chấp nhận tới mức nào: chỉ báo "sẽ liên hệ sáng mai", trả lời câu hỏi thường gặp có nhãn là trợ lý, hay tư vấn tới lúc chốt? Vì sao dừng ở mức đó?

**Câu đào sâu**

- "Khách nhắn lúc 10 giờ tối, sáng hôm sau mình trả lời, đã bao giờ khách bảo 'em mua chỗ khác rồi' chưa?" (chi phí của trả lời chậm)
- "Cùng một câu hỏi, hai nhân viên trả lời có giống nhau không?" (độ chuẩn hoá)
- "Khách cũ nhắn hỏi hỗ trợ, có phải chờ lâu hơn lead mới không, vì nhân viên ưu tiên chốt?" (chất lượng chăm sóc bị hy sinh)

**Bảng kiểm lượt 4**

| Việc | Xếp |
|---|:--:|
| Trả lời tin đầu tiên trong giờ làm | |
| Trả lời tin đầu tiên ngoài giờ, cuối tuần, lễ | |
| Trả lời câu hỏi thường gặp | |
| Phân loại tin: mua ngay, hỏi thông tin, khách cũ hỏi hỗ trợ, khiếu nại, rác | |
| Nhận ra khách cũ và lịch sử mua khi họ nhắn | |
| Chuyển tin khẩn hoặc khiếu nại tới người đúng | |
| Ghi hồ sơ lead sau hội thoại | |
| Chấm nóng lạnh | |
| Nhắc người thật gọi lại lead ngoài giờ | |
| Gom câu hỏi mới vào bộ câu trả lời chuẩn | |

**Dấu hiệu cần ghi lại**

- ⛔ ở "trả lời ngoài giờ" và chu kỳ bán ngắn → A3 phần "giữ khách ngoài giờ, hẹn người thật" là điểm chặn dòng tiền số một. Ngưỡng chạm lead nóng lấy từ Hồ Sơ MHKD: 15 phút nếu chu kỳ dưới 30 ngày, 4 giờ nếu từ 30 ngày. So với thực tế để chỉ ra khoảng cách.
- Có 5 đến 10 câu hỏi lặp chiếm phần lớn inbox → A3 phần "trả lời câu hỏi lặp" điểm cao về độ lặp và dữ liệu sẵn, nếu đã có câu trả lời chuẩn được duyệt.
- Lead mới và khách cũ trộn chung, không ai nhận ra khách cũ → A3 phần "phân loại" và A4 phần "nối hồ sơ" là điều kiện để làm chăm sóc 24/7 tử tế; thiếu cái này, máy sẽ bán hàng cho khách đang khiếu nại.
- Khiếu nại ngoài giờ không có đường thoát → A3 phần "chuyển tin khẩn" là bắt buộc trước khi cho máy trả lời bất kỳ tin nào ngoài giờ.
- Câu 8 quyết định **mức tự động** của đề xuất A3: người dùng nói "chỉ báo sẽ liên hệ" thì đề xuất dừng ở đó trong 30 ngày đầu, không đẩy lên.
- Lead ghi tay hoặc không ghi → A4 phần "điền hồ sơ lead từ hội thoại" giải đúng nỗi đau, nhưng cần chỗ chứa dữ liệu trước.

---

## Lượt 5 — Tư vấn, chốt và CRM

Mục tiêu: sale làm bằng gì, pipeline có tồn tại không, CRM được dùng thật hay để đó, chủ can dự chỗ nào. Phục vụ **A4 Agent chấm điểm lead và CRM** và **A5 Agent phân tích cuộc gọi**.

**Câu hỏi chính**

1. Từ lúc lead tử tế tới lúc khách trả tiền, đi qua những bước gì? Kể theo thứ tự: gọi, hẹn gặp, demo, báo giá, thương lượng, ký, thanh toán, chuyển sang chăm sóc. Bước nào hay tắc? Các bước này có được đặt tên thành giai đoạn để cả đội dùng chung không?
2. Mỗi người bán hàng xử lý bao nhiêu lead một ngày, một tuần? Họ theo dõi lead bằng gì: trí nhớ, sổ, bảng tính, phần mềm? Nếu dùng phần mềm, bao nhiêu phần trăm lead được cập nhật đúng thực tế? Ai kiểm?
3. Kịch bản tư vấn có thành văn chưa: mở đầu, hỏi nhu cầu, trình bày, xử lý từ chối, chốt? Người giỏi nhất khác người còn lại ở chỗ nào? Nhân viên mới học bằng cách nào và mất bao lâu chốt được đơn đầu?
4. Báo giá làm thế nào, ai làm, mất bao lâu, từ mẫu hay soạn mới từng lần? Giá cố định hay thương lượng từng khách? Ai được quyền giảm giá, giảm tới đâu, có ghi lại không?
5. Sau khi báo giá, ai nhắc lại khách, nhắc bao nhiêu lần, cách nhau bao lâu, dựa vào gì để nhớ? Có bao giờ quên nhắc không? Có bao giờ nhắc quá nhiều khiến khách khó chịu không? Deal treo bao lâu thì coi là mất, ai quyết?
6. Cuộc gọi hoặc buổi gặp tư vấn có ghi âm, ghi chú lại không? Ghi ở đâu, ai đọc lại? Sau cuộc gọi, hồ sơ khách được cập nhật ngay hay để cuối ngày, cuối tuần, hay không cập nhật?
7. Ba lý do mất deal hay gặp nhất? Khách từ chối bằng câu gì? Đội trả lời câu đó thế nào, có câu trả lời chuẩn chưa? Có ai gom lý do mất deal lại để học không?
8. Bao nhiêu phần trăm lead tử tế thành khách? Bước nào anh chị **phải tự ra tay** thì mới chốt được? Khi khách trả tiền xong, ai báo cho bên chăm sóc và báo bằng gì?

**Câu đào sâu**

- "Tuần này có bao nhiêu deal đang treo mà không ai biết lần cuối chạm là khi nào?" (sức khoẻ pipeline)
- "Nếu một nhân viên bán hàng nghỉ việc hôm nay, bao nhiêu lead đi theo họ?" (dữ liệu thuộc công ty hay cá nhân)
- "Hoa hồng tính dựa vào con số nào, và con số đó lấy từ đâu?" (nếu lấy từ CRM, CRM sẽ được cập nhật; nếu không, sẽ bị bỏ)

**Bảng kiểm lượt 5**

| Việc | Xếp |
|---|:--:|
| Tạo hồ sơ lead với đủ trường: tên, liên hệ, nhu cầu, ngân sách, nguồn, phân khúc, giai đoạn | |
| Chấm điểm nóng lạnh và xếp ưu tiên gọi | |
| Chuẩn bị trước cuộc gọi: tóm tắt lead, lịch sử, gợi ý câu hỏi | |
| Ghi chú và cập nhật hồ sơ sau cuộc gọi | |
| Nháp báo giá từ mẫu | |
| Nhắc lại sau báo giá đúng nhịp | |
| Cảnh báo deal treo quá hạn | |
| Gợi ý câu trả lời cho từ chối | |
| Gom lý do mất deal và câu nói tốt của người giỏi | |
| Chuyển khách đã trả tiền sang chăm sóc kèm đủ thông tin | |
| Báo cáo pipeline cho chủ | |

**Dấu hiệu cần ghi lại**

- Giai đoạn pipeline chưa đặt tên chung hoặc phần mềm có mà cập nhật dưới nửa → A4 cần định nghĩa giai đoạn và luật cập nhật trước; đề xuất kèm `/phan-bo-va-cham-diem-lead`. Gợi ý cách rẻ nhất: dùng `/ghi-cuoc-gap` để kể bằng lời, máy điền hồ sơ.
- Quên nhắc lại hoặc nhắc không đều → A4 phần "nhắc chạm theo 5%, 15%, 30% chu kỳ bán" điểm cao về dòng tiền.
- Có ghi âm hoặc sẵn sàng ghi âm với sự đồng ý → A5 khả thi; không thể ghi → A5 xuống tầng chưa nên.
- ⛔ ở "chuẩn bị trước cuộc gọi" và chủ phải tự chốt → agent tóm tắt lead cho chủ là đề xuất giảm việc cho chủ hiệu quả nhất.
- Báo giá thương lượng và chủ quyết → AI chỉ nháp từ mẫu, **không** đề xuất AI quyết giá. Ghi vào "AI không làm".
- Không có câu trả lời chuẩn cho từ chối → `/objection-handler` trước, rồi A3 và A4 dùng kết quả.
- ⛔ ở "chuyển sang chăm sóc kèm đủ thông tin" → khách rơi ngay sau khi trả tiền; nối sang lượt 6.

---

## Lượt 6 — Sau bán, chăm sóc chủ động và mua lại

Mục tiêu: sau khi trả tiền chuyện gì xảy ra, chăm bằng người hay tự động, dữ liệu khách có gì để phân tích. Phục vụ **A6 Agent chăm sóc sau bán và mua lại** và **A7 Agent phân tích khách hàng và tự đề xuất**. Bỏ lượt này là lỗi phổ biến nhất, vì doanh nghiệp Việt thường dồn sức vào kéo khách mới.

**Câu hỏi chính**

1. Sau khi khách trả tiền, chuyện gì xảy ra trong tuần đầu? Ai liên hệ, hướng dẫn gì, qua kênh nào, vào ngày thứ mấy? Có lộ trình cố định (ngày 1, ngày 3, ngày 7, ngày 30) hay tuỳ người nhớ?
2. Chăm sóc chủ động hiện làm gì: hỏi thăm hài lòng, nhắc dùng, chúc mừng dịp, gửi mẹo dùng, báo chương trình? Bao lâu một lần, bằng người gõ hay tự động gửi? Khách phản hồi tỷ lệ bao nhiêu?
3. Khách khiếu nại hoặc hỏi hỗ trợ thì nhắn vào đâu, ai xử lý, trong bao lâu? Khiếu nại nào lặp lại nhiều nhất? Có ai gom khiếu nại lại tìm nguyên nhân gốc không?
4. Có chủ động xin đánh giá, lời chứng thực, hay nhờ khách giới thiệu không? Xin lúc nào, ai xin, tỷ lệ khách đồng ý? Đánh giá tốt hiện nằm ở đâu, có ai đem vào nội dung bán hàng không?
5. Với mô hình mua lại của anh chị (đã có trong Hồ Sơ MHKD), ai nhắc khách mua lại hoặc gia hạn? Nhắc trước bao lâu, dựa vào gì để biết đã đến lúc? Có biết bao nhiêu phần trăm khách quay lại không?
6. Hồ sơ mỗi khách hiện có những trường gì: ngày mua, sản phẩm, giá trị, kênh, người phụ trách, lần liên hệ cuối, lý do rời? Có phân nhóm khách không: khách lớn, khách thường, khách ngủ quên, khách sắp rời? Phân bằng gì?
7. Khách rời đi thường vì lý do gì, và mình biết lý do đó bằng cách nào? Có nhóm khách nào mua nhiều, ở lâu, ít phàn nàn không? Mình có biết họ là ai và họ giống nhau ở điểm gì không?
8. Nếu mỗi tuần có một bản "ba việc nên làm với khách cũ" kèm danh sách tên, ai sẽ đọc và làm? Hiện có ai làm việc đó không?

**Câu đào sâu**

- "Khách mua lần cuối cách đây 6 tháng, hôm nay có ai biết và gọi cho họ không?" (khách ngủ quên)
- "Tin chăm sóc gửi cho khách mới mua và khách mua 2 năm có giống nhau không?" (cá nhân hoá)
- "Khách nói 'đừng nhắn nữa' thì mình ghi ở đâu để không nhắn lại?" (danh sách từ chối)

**Bảng kiểm lượt 6**

| Việc | Xếp |
|---|:--:|
| Gửi lộ trình sau bán theo mốc ngày | |
| Hỏi thăm hài lòng và xin đánh giá đúng lúc | |
| Phân loại và nháp trả lời khiếu nại | |
| Gom khiếu nại tìm nguyên nhân gốc | |
| Nhắc mua lại hoặc gia hạn theo chu kỳ | |
| Phát hiện khách sắp rời, khách ngủ quên | |
| Phân nhóm khách theo giá trị và hành vi | |
| Tìm cơ hội bán thêm, bán chéo theo nhóm | |
| Đề xuất việc nên làm với khách cũ mỗi tuần | |
| Giữ danh sách khách không muốn nhận tin | |
| Đem lời khách tốt vào nội dung | |

**Dấu hiệu cần ghi lại**

- Không có lộ trình sau bán → A6 phần "onboarding theo lộ trình" cần viết lộ trình trước, `/onboarding-flow`, rồi mới giao agent gửi nhắc.
- Không nhắc mua lại trong khi `mo-hinh-mua-lai` là `theo-ky` hoặc `lien-tuc` → A6 phần "nhắc mua lại, cảnh báo sắp rời" là điểm chặn dòng tiền rõ nhất.
- Hồ sơ khách có ít nhất 4 trường (ngày, khách, giá trị, sản phẩm) ở một chỗ → A7 khả thi; không có → đề xuất đầu tiên là bảng 4 trường, không phải agent.
- Không biết tỷ lệ quay lại và không biết nhóm khách tốt → A7 có bài toán rõ nhưng thiếu dữ liệu; ghi vào "Dữ liệu cần gom trước".
- Câu 8 không có ai nhận → A7 điểm 0 ở tiêu chí người vận hành, xuống tầng kế tiếp dù bài toán hay.
- Chăm sóc chủ động đang ⚙️ tự động mà không có danh sách từ chối → rủi ro làm phiền, ghi vào "AI không làm" và cách chặn.
- Có nhiều đánh giá tốt chưa dùng → A1 có nguồn bằng chứng, nối với `/testimonial-collector`.

---

## Lượt 7 — Đo lường, quyết định, lo ngại

Mục tiêu: báo cáo, con số chủ xem, điều không bao giờ giao AI, người vận hành. Phục vụ **A8 Agent báo cáo** và phần "Ranh giới" của bản đồ.

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

- Báo cáo gom tay từ 3 nguồn trở lên mất trên 2 giờ mỗi kỳ → A8 điểm cao về độ lặp; nhịp đọc số lấy từ Hồ Sơ MHKD.
- Không chọn được ba con số → chưa nên làm A8; đề xuất `/mkt-kpi-dashboard` để chốt chỉ số trước.
- Lo "khách biết là máy" → mọi đề xuất A3, A6 phải ghi nguyên tắc **minh bạch**: máy trả lời có nhãn, chuyển người khi khách hỏi, không giả người.
- Lo "nói sai thông tin" → tầng làm ngay giới hạn ở việc AI **nháp và gợi ý**, người gửi.
- Không có người vận hành → điều kiện chặn thứ ba; tầng làm ngay để trống và nói thẳng vì sao.
- Câu 6 là **chỉ số thành công** của kế hoạch 30 ngày trong file đầu ra. Không tự thay bằng chỉ số Claude nghĩ hay hơn.

---

## Sau bảy lượt: kiểm tra trước khi dựng bảng

- Mỗi giai đoạn (thu hút, lead vào, tư vấn chốt, sau bán, đo lường) có ít nhất một bước được mô tả đủ sáu ô chưa? Giai đoạn nào trống hoàn toàn, hỏi thêm một câu: "Giai đoạn này hiện gần như không có gì, đúng không?" Người dùng xác nhận thì ghi "chưa có quy trình", đừng tự lấp.
- Bảng kiểm 👤 🔧 ⚙️ ⛔ đã điền đủ cho lượt 2 đến 6 chưa? Đếm nhanh: bao nhiêu ô 👤 lặp lại hằng ngày, bao nhiêu ô ⛔ nằm trên đường tiền. Hai con số này là xương sống của phần chấm điểm.
- Có bước nào người dùng kể hai lần với hai cách khác nhau không? Hỏi lại cho rõ.
- Có điểm đau nào nằm ngoài Sale & Marketing (kho, kế toán, nhân sự) không? Ghi một dòng "ngoài phạm vi", không đưa vào chấm điểm.
