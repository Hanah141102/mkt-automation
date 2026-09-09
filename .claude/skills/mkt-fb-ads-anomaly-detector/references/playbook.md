# Playbook Facebook Ads — Đo lường theo giờ & ra quyết định

> Nguồn: AI-NEXUS™ Performance Marketing Playbook, phiên bản 1.0 (2026). Đây là quy tắc gốc mà `scripts/anomaly.py` cài đặt; khi script và tài liệu này lệch nhau, tài liệu này thắng và script phải sửa.

## Tóm tắt điều hành

Mục đích: phát hiện xu hướng bất thường đủ sớm để bảo vệ ngân sách, nhưng không phản ứng quá mức trước nhiễu dữ liệu theo giờ. Dashboard theo giờ phải trả lời bốn câu hỏi: chỉ số nào lệch, lệch bao nhiêu, đã đủ dữ liệu chưa, và hành động phù hợp là quan sát, kiểm tra, giảm ngân sách, dừng hay scale.

**Nguyên tắc cốt lõi:** `BẤT THƯỜNG = LỆCH ĐỦ LỚN + ĐỦ DỮ LIỆU + KÉO DÀI ĐỦ LÂU`

Ngoại lệ: lỗi website, checkout, link hoặc thiết lập phân phối có thể yêu cầu dừng ngay.

- Lỗi kỹ thuật ảnh hưởng trực tiếp đến bán hàng: dừng traffic bị ảnh hưởng, sửa và test trước khi bật lại.
- Chỉ số xấu trong một giờ nhưng mẫu nhỏ: giữ nguyên, không tối ưu theo cảm xúc.
- Xu hướng xấu kéo dài 2–3 giờ và đủ mẫu: tìm đúng điểm gãy trong phễu trước khi hành động.
- Kết quả tốt ổn định 2–3 ngày: scale ngân sách từng bước 10–20%, không tăng liên tục trong vài giờ.

Năm cấp độ hành động: **giữ nguyên → theo dõi → kiểm tra → giảm ngân sách → dừng**, cộng thêm **scale** khi kết quả tốt ổn định.

## 1. Thế nào là bất thường

### 1.1 Chọn đúng đường nền

Không so sánh 14h hôm nay với trung bình cả ngày. So với **cùng khung giờ của 7–14 ngày gần nhất**, cùng campaign, quốc gia, mục tiêu tối ưu và loại ngày (ngày thường / cuối tuần) nếu khác biệt lớn.

`BASELINE(H) = MEDIAN của cùng khung giờ H trong 7–14 ngày gần nhất`

Median ổn định hơn average khi có vài ngày tăng/giảm đột biến.

### 1.2 Rolling 3 giờ để giảm nhiễu

`ROLLING 3H = (giá trị giờ H + H-1 + H-2) / 3`

Với tỷ lệ (CTR, CVR…): **cộng tử số và mẫu số của ba giờ rồi tính lại tỷ lệ**, không lấy trung bình ba tỷ lệ.

`CTR rolling 3h = Tổng link click 3h / Tổng impression 3h × 100%`

### 1.3 Công thức độ lệch

`DEVIATION = (HIỆN TẠI − BASELINE) / BASELINE × 100%`

Chỉ số càng thấp càng tốt (CPM, CPC, CPA): deviation dương là xấu.
Chỉ số càng cao càng tốt (CTR, CVR, ROAS): dùng mức suy giảm

`MỨC SUY GIẢM = (BASELINE − HIỆN TẠI) / BASELINE × 100%`

### 1.4 Ngưỡng cảnh báo khởi đầu

| Độ lệch | Mức | Điều kiện bổ sung | Hành động |
|---|---|---|---|
| < 20% | Bình thường | Không có lỗi kỹ thuật | Giữ nguyên |
| 20–30% | Vàng | Mới xuất hiện | Theo dõi thêm |
| 30–50% | Cam | Đủ mẫu, kéo dài 2 giờ | Kiểm tra; có thể giảm |
| > 50% | Đỏ | Đủ mẫu hoặc có lỗi rõ | Xử lý ngay theo điểm gãy |
| Lỗi kỹ thuật | Khẩn cấp | Web/checkout/link hỏng | Dừng traffic bị ảnh hưởng |

Các ngưỡng 20/30/50% là guardrail ban đầu; sau 4–8 tuần hiệu chỉnh theo độ biến động thực tế của từng tài khoản.

## 2. Bộ công thức theo phễu

### 2.1 Tầng phân phối

| Chỉ số | Công thức | Ý nghĩa | Tín hiệu xấu |
|---|---|---|---|
| CPM | Spend / Impression × 1.000 | Giá 1.000 lượt hiển thị | Tăng > 30% so với nền |
| Frequency | Impression / Reach | Mức lặp trên một người | Tăng cùng lúc CTR giảm |
| Pacing | Spend thực tế / Spend kỳ vọng | Tốc độ tiêu ngân sách | > 1,3 và CPA xấu |

### 2.2 Tầng creative

| Chỉ số | Công thức | Ý nghĩa | Tín hiệu xấu |
|---|---|---|---|
| CTR link | Link click / Impression × 100% | Khả năng thu hút click | Giảm > 30%, đủ 1.000–2.000 impression |
| CPC link | Spend / Link click | Chi phí một click | Tăng > 30% cùng CTR giảm |

### 2.3 Tầng landing page và mua hàng

| Chỉ số | Công thức | Điểm gãy có thể nằm ở |
|---|---|---|
| LPV Rate | Landing Page View / Link click | Tốc độ web, link, mobile, hosting |
| ATC Rate | Add to Cart / LPV | Sản phẩm, giá, niềm tin, offer |
| Checkout Rate | Initiate Checkout / Add to Cart | Phí ship, bước checkout |
| Purchase Rate | Purchase / Initiate Checkout | Thanh toán, tồn kho, tracking |
| CVR | Purchase / LPV | Hiệu quả chuyển đổi toàn trang |

### 2.4 Tầng tài chính

- `CPA = SPEND / PURCHASE`
- `ROAS = DOANH THU GHI NHẬN / SPEND`
- `BREAK-EVEN CPA = AOV − COGS − FULFILLMENT − PHÍ − HOÀN HỦY KỲ VỌNG`
- `BREAK-EVEN ROAS = AOV / BREAK-EVEN CPA`

ROAS đẹp trên Meta chưa chắc có lợi nhuận nếu hoàn/hủy cao hoặc chưa tính fulfillment. Quyết định cuối cùng ưu tiên số liệu backend.

## 3. Pacing — Meta có đang tiêu quá nhanh?

Không chia đều ngân sách ngày cho 24 giờ. Dùng **tỷ trọng chi tiêu tích lũy lịch sử đến từng giờ**.

- `SPEND KỲ VỌNG ĐẾN H = NGÂN SÁCH NGÀY × TỶ TRỌNG LỊCH SỬ ĐẾN H`
- `PACING RATIO = SPEND THỰC TẾ / SPEND KỲ VỌNG`

Ví dụ lúc 14h: ngân sách 12.000.000đ; tỷ trọng lịch sử đến 14h = 45% (median 7–14 ngày) → kỳ vọng 5.400.000đ; thực tế 7.020.000đ → pacing 1,30. Kết luận: tiêu nhanh hơn 30%. Nếu CPA/ROAS vẫn đạt target, chưa cần can thiệp. Nếu CPA xấu liên tục 2–3 giờ, có thể giảm ngân sách 20–30%.

## 4. Xác định điểm gãy trước khi dừng

Chỉ tắt quảng cáo khi dữ liệu cho thấy chính ad/ad set là nguyên nhân. Điểm gãy ở web/checkout thì thay creative không giải quyết được.

| Biến động quan sát | Chẩn đoán ưu tiên | Hành động |
|---|---|---|
| CPM tăng, CTR và CPA vẫn tốt | Đấu giá đắt hơn nhưng traffic vẫn chất lượng | Giữ nguyên |
| CPM tăng, CTR giảm, CPC tăng | Creative mỏi hoặc audience bão hòa | Tắt mẫu yếu; thay creative |
| Click tốt, LPV Rate giảm | Trang chậm, sai link hoặc lỗi mobile | Kiểm tra web; lỗi thật thì dừng traffic |
| ATC tốt, Checkout giảm | Phí ship, giá cuối hoặc UX checkout | Giảm ngân sách và sửa phễu |
| Checkout tốt, Purchase giảm mạnh | Thanh toán, tồn kho hoặc Purchase Event | Lỗi thật thì dừng ngay |
| Meta không có đơn, backend có đơn | Pixel/CAPI hoặc attribution | Giữ ads; sửa tracking |

## 5. Quy tắc dừng theo CPA mục tiêu

`SPEND MULTIPLE = SPEND CHƯA CÓ ĐƠN / CPA MỤC TIÊU`

Ví dụ CPA mục tiêu 500.000đ:
- 300.000 / 500.000 = 0,6x → quá ít dữ liệu, tiếp tục chạy.
- 750.000 / 500.000 = 1,5x → có nhiều ATC/Checkout: quan sát, kiểm tra độ trễ attribution; gần như không có tín hiệu mua: giảm ngân sách hoặc tắt creative yếu.
- 1.250.000 / 500.000 = 2,5x → không Purchase, rất ít ATC, không Checkout: có thể dừng ad/ad set. Backend đã có đơn mà Meta chưa ghi nhận: giữ và sửa tracking.

| Spend chưa có đơn | Có ATC/Checkout | Không có tín hiệu mua |
|---|---|---|
| < 1x CPA | Tiếp tục | Tiếp tục |
| 1–2x CPA | Chờ; kiểm tra checkout | Giảm hoặc tắt creative yếu |
| 2–3x CPA | Kiểm tra attribution/offer | Dừng ad hoặc ad set |
| > 3x CPA | Chỉ giữ nếu backend xác nhận đơn | Dừng |

## 6. Ví dụ phân tích hoàn chỉnh

Campaign TMĐT 12 triệu/ngày, CPA mục tiêu 500.000đ, ROAS mục tiêu 2,5. Từ 13h–16h:

| Chỉ số | Baseline | Rolling 3h | Độ lệch | Đánh giá |
|---|---|---|---|---|
| CPM | 80.000đ | 120.000đ | +50% | Đỏ |
| CTR link | 1,8% | 1,05% | −41,7% | Đỏ |
| CPC link | 4.444đ | 11.429đ | +157% | Đỏ |
| LPV Rate | 85% | 83% | −2,4% | Bình thường |
| ATC Rate | 8% | 7,6% | −5% | Bình thường |
| CPA | 500.000đ | 820.000đ | +64% | Đỏ |

Phân tích: CPM +50% là giá đấu cao hơn nền; CTR −41,7% kéo CPC +157% → tín hiệu creative/audience; LPV và ATC gần bình thường → web và offer không phải điểm gãy; CPA +64% là hệ quả của traffic đắt + creative yếu.

Quyết định: tắt creative CTR thấp rõ rệt sau khi đủ impression; bổ sung hook/creative mới; giảm ngân sách ad set 20–30% nếu CPA xấu thêm 2 giờ. Không dừng toàn bộ campaign nếu vẫn có ad đạt target.

## 7. Cây quyết định vận hành

- `CẢNH BÁO THẬT = |DEVIATION| ≥ 30% AND ĐỦ MẪU AND KÉO DÀI ≥ 2 GIỜ`
- `LỖI WEBSITE/CHECKOUT = DỪNG NGAY, KHÔNG CHỜ ĐỦ MẪU`

Để giảm cảnh báo giả: ưu tiên rolling 3 giờ và chỉ gửi cảnh báo mạnh khi có **ít nhất hai điều kiện xấu cùng xuất hiện** (CTR giảm + CPC tăng; CPA tăng + Spend Multiple vượt ngưỡng).

## 8. Ngưỡng đủ mẫu để hành động

| Nhóm chỉ số | Mẫu tối thiểu tham khảo | Cửa sổ | Ghi chú |
|---|---|---|---|
| CPM/CTR | 1.000–2.000 impression | Rolling 3h | Tài khoản lớn dùng ngưỡng cao hơn |
| LPV Rate | 30–50 link click | Rolling 3h | Lỗi trang thật có thể dừng ngay |
| ATC Rate | 50+ LPV | 3–6h | So với sản phẩm/nguồn traffic tương đồng |
| Purchase CVR | 100+ LPV hoặc đủ spend | 3–24h | Luôn kiểm tra backend |
| CPA | Theo Spend Multiple | Tích lũy | 1x cảnh báo; 2–3x mới cân nhắc dừng |
| ROAS | Nhiều hơn 1–2 đơn | Ngày / 3 ngày | Không scale từ một giờ may mắn |

Mẫu tối thiểu không phải quy luật thống kê tuyệt đối. Sản phẩm CPA cao hoặc conversion ít: dùng cửa sổ dài hơn thay vì ép quyết định theo giờ.

## 9. Quy tắc scale khi kết quả tốt

- CPA thấp hơn target và ROAS cao hơn target ít nhất khoảng 20%.
- Kết quả ổn định 2–3 ngày, đủ số đơn, backend xác nhận lợi nhuận.
- Tăng ngân sách 10–20% mỗi lần; theo dõi ít nhất 24 giờ.
- CPA tăng > 30% sau scale và kéo dài → ngừng tăng hoặc quay về mức trước.
- Mở rộng bằng creative và audience mới để giảm phụ thuộc vào một quảng cáo thắng.

## 10. Checklist khi có cảnh báo

- Kiểm tra đơn hàng và doanh thu backend trước khi tin hoàn toàn vào Meta.
- Kiểm tra Pixel/CAPI và độ trễ attribution.
- Tự mở quảng cáo trên mobile, click link, tải landing page.
- Test Add to Cart, mã giảm giá, phí ship và thanh toán.
- So với cùng giờ của 7–14 ngày, không so với trung bình cả ngày.
- Kiểm tra impression, click và Spend Multiple đã đủ để kết luận chưa.
- Xem breakdown theo creative; chỉ tắt mẫu yếu nếu campaign vẫn có mẫu tốt.
- Ghi lại hành động và thời điểm để đánh giá tác động sau 24 giờ.

## 11. Bảng quyết định nhanh

| Tình huống | Điều kiện | Quyết định |
|---|---|---|
| Lỗi website/checkout | Xác minh lỗi thật | Dừng traffic ngay |
| Tracking lỗi | Backend vẫn có đơn | Giữ ads; sửa Pixel/CAPI |
| Chỉ số xấu 1 giờ | Mẫu nhỏ | Không chỉnh |
| CPM tăng | CPA vẫn đạt target | Giữ nguyên |
| CTR giảm | > 30%, đủ impression, CPC tăng | Tắt creative yếu |
| LPV Rate giảm | > 30%, có 30–50 click | Kiểm tra trang |
| CPA xấu | Kéo dài 2–3 giờ | Giảm 20–30% |
| Không có đơn | Spend 2–3x CPA, không tín hiệu mua | Dừng ad/ad set |
| Kết quả tốt | Ổn định 2–3 ngày | Scale 10–20% |

## Kết luận

Đừng dừng quảng cáo chỉ vì ROAS của một giờ xấu. Dừng khi xu hướng lệch đủ lớn, đủ dữ liệu, kéo dài đủ lâu và xác định đúng điểm gãy. Riêng lỗi kỹ thuật làm mất khả năng bán hàng phải xử lý ngay. Hệ thống đo theo giờ không thay thế người vận hành; nó giúp tập trung vào bất thường đáng chú ý, ra quyết định nhất quán, và giảm cả hai sai lầm: đốt ngân sách quá lâu hoặc tắt một quảng cáo tốt quá sớm.
