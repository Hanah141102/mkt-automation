---
type: business-context
trang-thai: cho-xac-nhan
cap-nhat: 2026-08-06
# --- 6 THAM SỐ ĐIỀU KHIỂN — mọi skill đọc từ đây ---
# ⚠️ Giá trị dưới đây do AI ĐỀ XUẤT, chủ doanh nghiệp CHƯA xác nhận. Xem mục "Đề xuất tham số" cuối file.
loai-san-pham: hon-hop        # dịch vụ (tư vấn, triển khai, code theo yêu cầu) + sản phẩm số tự phát triển
chu-ky-ban-ngay: 60           # ⚠️ ước lượng gộp: khách Mỹ 30–60 ngày · khách VN 60–90 ngày
nguoi-mua-la-nguoi-dung: khong  # chủ doanh nghiệp/CTO ký, nhân viên nghiệp vụ mới là người dùng
mua-vu: deu                   # ⚠️ chưa xác nhận — phần mềm B2B thường không có mùa rõ rệt
thang-cao-diem:               # để trống vì mua-vu = deu
so-huu-diem-cham: co          # hợp đồng ký trực tiếp, mình giữ dữ liệu khách
mo-hinh-mua-lai: lien-tuc     # ⚠️ thuê đội theo tháng, khách dừng lúc nào cũng được
chu-ky-tieu-dung-ngay:        # để trống vì mô hình mua lại = lien-tuc
---

# Hồ Sơ Mô Hình Kinh Doanh

> [!important] File này điều khiển toàn bộ hệ thống
> Sáu tham số trong phần đầu file quyết định **mọi khuyến nghị** mà AI đưa ra sau này: giữ lead bao lâu, đọc số theo nhịp nào, chân dung khách mấy lớp, lịch nội dung ra sao, thiết kế phễu kiểu gì, giữ khách bằng cách nào.
>
> Điền sai một tham số ở đây thì hàng chục khuyến nghị phía sau sẽ sai theo. Điền xong nhớ chạy lại `/kiem-tra-cong 02`.

Chạy `/mo-hinh-kinh-doanh` để được phỏng vấn và điền tự động, hoặc điền tay theo hướng dẫn dưới.

---

## Tham số 1 — Loại sản phẩm chính

| Giá trị | Nghĩa là gì | Ví dụ |
|---|---|---|
| `so` | Sản phẩm số — làm một lần, bán nhiều lần, biên rất cao | Khoá học online, phần mềm, báo cáo, mẫu biểu |
| `dich-vu` | Có người phục vụ trực tiếp, năng lực giới hạn bởi số người | Đào tạo, tư vấn, spa, thi công, agency |
| `vat-ly` | Hàng hoá phải sản xuất, lưu kho, vận chuyển | Mỹ phẩm, thực phẩm, nội thất, thời trang |
| `hon-hop` | Hai loại trở lên, mỗi loại trên 25% doanh thu | Trung tâm dạy offline + bán khoá online |

**Điều khiển:** trọng số 12 bước · bước nào cần làm kỹ, bước nào lướt qua được.

| Bước | `so` | `dich-vu` | `vat-ly` |
|---|:--:|:--:|:--:|
| 05 Phễu | ●●● | ●● | ● |
| 06 Nội dung | ●●● | ●● | ●● |
| 08 Bán hàng | ●● | ●●● | ●●● |
| 09 Giao hàng | ● | ●●● | ●● |
| 10 Giữ khách | ●● | ●●● | ●●● |
| + Cung ứng | — | — | ●●● |

## Tham số 2 — Chu kỳ bán trung bình

Số ngày từ **lần chạm đầu tiên** tới **lúc khách thanh toán**. Nếu chưa đo, ước lượng từ 5–10 khách gần nhất.

**Điều khiển:** mọi ngưỡng thời gian trong hệ thống. Không còn con số cứng nào.

| Việc | Công thức |
|---|---|
| Giữ lead tối đa trước khi trả về nhóm chung | **1,5 × chu kỳ bán** |
| Thời hạn chạm lead nóng | 15 phút nếu chu kỳ < 30 ngày · 4 giờ nếu ≥ 30 ngày |
| Nhịp nhắc lại sau báo giá | **5% · 15% · 30%** của chu kỳ bán |
| Nhịp đọc số | < 30 ngày: tuần · 30–90: hai tuần · > 90: tháng |

> **Ví dụ:** chu kỳ 60 ngày → giữ lead 90 ngày · chạm nóng trong 4 giờ · nhắc lại sau 3, 9, 18 ngày · đọc số hai tuần một lần.

## Tham số 3 — Người mua có phải người dùng không

| Giá trị | Khi nào chọn |
|---|---|
| `co` | Người trả tiền cũng là người dùng sản phẩm |
| `khong` | Hai người khác nhau — phụ huynh/học sinh, công ty/nhân viên, người tặng/người nhận |

**Điều khiển:** số lớp chân dung khách. Nếu `khong`, `/customer-persona` chạy chế độ hai lớp và dựng thêm phần **cầu nối** — người dùng nói câu gì thì người mua quyết mua hoặc dừng.

## Tham số 4 — Nhu cầu theo mùa

| Giá trị | Khi nào chọn |
|---|---|
| `deu` | Nhu cầu trải tương đối đều cả năm |
| `co-mua` | Có tháng cao điểm rõ rệt — điền `thang-cao-diem` |

**Điều khiển:** lịch nội dung và lịch ngân sách. Nếu `co-mua`, `/content-plan-builder` dựng **lịch 12 tháng có cường độ khác nhau** thay vì lịch 30 ngày lặp lại, và dồn ngân sách quảng cáo vào 6–8 tuần trước mùa cao điểm.

## Tham số 5 — Có sở hữu điểm chạm không

> **Câu hỏi đúng là: giao dịch xảy ra ở đâu?** Không phải "khách biết đến mình từ đâu". Khách đến từ truyền miệng nhưng vẫn mua qua website của mình thì vẫn là `co`.

| Giá trị | Nghĩa là gì | Cách nhận biết |
|---|---|---|
| `co` | Giao dịch xảy ra trên nền tảng mình kiểm soát | Mình có tên, số điện thoại, email của khách sau khi mua |
| `ban-tren-san` | Giao dịch xảy ra trong Shopee, TikTok Shop, Lazada | Sàn giữ dữ liệu khách, mình chỉ thấy đơn hàng |
| `hon-hop` | Trên 25% doanh thu ở mỗi bên | Ghi rõ tỷ lệ trong phần mô tả |

**Chỉ chọn `hon-hop` khi thật sự có hai luồng giao dịch riêng** — vì nó buộc phải dựng và đo hai phễu. Nếu chỉ có nhiều nguồn traffic đổ về cùng một chỗ mua, đó vẫn là `co`.

**Điều khiển:** thiết kế phễu ở Bước 05.

- `co` → phễu cổ điển: quảng cáo → landing → thu thông tin → nuôi dưỡng → mua
- `ban-tren-san` → phễu nằm trong nền tảng. Trọng tâm chuyển sang: tối ưu trang sản phẩm, tốc độ phản hồi inbox, đánh giá, và **kéo khách ra kênh mình sở hữu sau khi mua** (Zalo, nhóm khách hàng)
- `hon-hop` → dựng hai phễu riêng, đo riêng

## Tham số 6 — Mô hình mua lại

| Giá trị | Nghĩa là gì | Chiến lược giữ khách |
|---|---|---|
| `khong` | Mua một lần rồi thôi | Tập trung vào giới thiệu và bán chéo |
| `lien-tuc` | Trả tiền định kỳ, có thể rời bất cứ lúc nào | Cảnh báo sớm, can thiệp trước khi rời |
| `theo-ky` | Có **điểm tái quyết định rời rạc** — cuối khoá, cuối hợp đồng, khi dùng hết | Dồn lực vào cửa sổ quyết định |

**Điều khiển:** cách chạy Bước 10.

- `lien-tuc` → `/churn-prevention-playbook` (chấm điểm sức khoẻ, can thiệp liên tục)
- `theo-ky` → chiến dịch tập trung vào **2 tuần trước điểm tái quyết định**. Nếu là hàng tiêu dùng, điền `chu-ky-tieu-dung-ngay` và chạy `/nhac-mua-lai-theo-chu-ky`

---

## Ba ví dụ đã điền

### Ví dụ A — Bán sản phẩm số, chu kỳ dài

```yaml
loai-san-pham: so
chu-ky-ban-ngay: 75
nguoi-mua-la-nguoi-dung: co
mua-vu: deu
so-huu-diem-cham: co
mo-hinh-mua-lai: theo-ky        # gói báo cáo gia hạn hằng năm — KỲ HẠN CỐ ĐỊNH
chu-ky-tieu-dung-ngay: 365
```

**Hệ thống sẽ tự điều chỉnh:** giữ lead 112 ngày · chạm nóng trong 4 giờ · nhắc lại sau báo giá vào ngày 4, 11, 23 · đọc số hai tuần một lần kèm phân tích theo nhóm khách vào cùng tháng · **không đọc doanh thu theo tuần** · nhắc gia hạn theo **kỳ hạn cố định** (30 / 14 / 3 ngày trước ngày hết hạn), không phải theo tỷ lệ chu kỳ.

### Ví dụ B — Dịch vụ đào tạo, có mùa, người mua ≠ người dùng

```yaml
loai-san-pham: dich-vu
chu-ky-ban-ngay: 21
nguoi-mua-la-nguoi-dung: khong
mua-vu: co-mua
thang-cao-diem: [5,6,7,8,12,1]
so-huu-diem-cham: co
mo-hinh-mua-lai: theo-ky
chu-ky-tieu-dung-ngay: 90       # mỗi khoá 3 tháng
```

**Hệ thống sẽ tự điều chỉnh:** giữ lead 32 ngày · chạm nóng trong 15 phút · nhắc lại sau 1, 3, 6 ngày · đọc số hằng tuần · **chân dung khách hai lớp** (phụ huynh + học sinh + cầu nối) · lịch nội dung 12 tháng dồn vào tháng 4–8 và 11–1 · Bước 09 và Bước 10 nâng lên trọng số cao nhất · nhắc tái ghi danh theo kỳ hạn cố định: 30 / 14 / 3 ngày trước khi hết khoá.

### Ví dụ C — Hàng vật lý, bán sàn, mua lặp lại

```yaml
loai-san-pham: vat-ly
chu-ky-ban-ngay: 3
nguoi-mua-la-nguoi-dung: co
mua-vu: co-mua
thang-cao-diem: [11,12,1]
so-huu-diem-cham: ban-tren-san
mo-hinh-mua-lai: theo-ky
chu-ky-tieu-dung-ngay: 50
```

**Hệ thống sẽ tự điều chỉnh:** giữ lead 4 ngày · chạm nóng trong 15 phút · nhắc lại sau 4 giờ, 11 giờ, 22 giờ · đọc số hằng tuần · phễu bỏ landing page, tập trung trang sản phẩm và tốc độ inbox, kéo khách ra Zalo sau mua · **bật `/ke-hoach-hang-hoa`** vì là hàng vật lý · nhắc mua lại theo chu kỳ tiêu dùng: ngày 40 / 48 / 58.

---

## ⚠️ Đề xuất tham số cho Tony Hoang Company — CHỜ XÁC NHẬN

> Chạy `/mo-hinh-kinh-doanh` ngày 06/08/2026. Chủ doanh nghiệp yêu cầu AI soạn trước toàn bộ, nên sáu tham số dưới đây **do AI suy ra**, chưa được xác nhận. Đây là file điều khiển cả hệ thống — **hai phút xác nhận ở đây tiết kiệm hàng chục khuyến nghị sai phía sau**.

| # | Tham số | Đề xuất | Vì sao | Cần xác nhận |
|:--:|---|---|---|---|
| 1 | `loai-san-pham` | `hon-hop` | Vừa làm dịch vụ (tư vấn, triển khai, code theo yêu cầu) vừa bán sản phẩm phần mềm tự phát triển | **Nếu sản phẩm đóng gói dưới 25% doanh thu → đổi thành `dich-vu`** |
| 2 | `chu-ky-ban-ngay` | `60` | Ước lượng gộp: khách Mỹ 30–60 ngày, khách Việt Nam 60–90 ngày | Đếm lại 5–10 khách gần nhất: từ lần chạm đầu tới lúc chuyển tiền là bao nhiêu ngày |
| 3 | `nguoi-mua-la-nguoi-dung` | `khong` | Chủ doanh nghiệp/CTO ký hợp đồng, nhưng nhân viên nghiệp vụ mới là người dùng hằng ngày — chính là lý do nhiều dự án số hoá chết sau bàn giao | Khá chắc đúng, nhưng nên xác nhận |
| 4 | `mua-vu` | `deu` | Phần mềm B2B thường không có mùa rõ rệt | Kiểm tra: có tháng nào ký hợp đồng nhiều hơn hẳn không (quý 4 duyệt ngân sách năm sau?) |
| 5 | `so-huu-diem-cham` | `co` | Hợp đồng ký trực tiếp, mình giữ toàn bộ dữ liệu khách | **Nếu trên 25% doanh thu đi qua Upwork/nền tảng trung gian → đổi thành `hon-hop`** |
| 6 | `mo-hinh-mua-lai` | `lien-tuc` | Thuê đội theo tháng — khách dừng lúc nào cũng được, cần cảnh báo sớm liên tục | **Nếu doanh thu chủ yếu là hợp đồng bảo trì năm có ngày hết hạn cố định → đổi thành `theo-ky` và điền `chu-ky-tieu-dung-ngay: 365`** |

### Các ngưỡng hệ thống sẽ dùng (tính từ chu kỳ bán 60 ngày)

```
- Giữ lead tối đa trước khi trả về nhóm chung:  90 ngày   (1,5 × 60)
- Chạm lead nóng trong:                          4 giờ    (vì chu kỳ ≥ 30 ngày)
- Nhắc lại sau báo giá vào ngày:                 3 · 9 · 18
- Nhịp đọc số:                                   hai tuần một lần
```

> **Lưu ý quan trọng về hai mảng có nhịp khác nhau:** các ngưỡng trên hợp với mảng dịch vụ. Mảng sản phẩm đóng gói ([[PK3 — SME Mua Sản Phẩm Đóng Gói]]) có chu kỳ bán ước tính chỉ **3–14 ngày** — nhanh hơn hàng chục lần. Khi mảng sản phẩm đủ lớn, **phải tách phễu và tách nhịp đo riêng**, không dùng chung ngưỡng với mảng dịch vụ.

### Liên kết

- [[Business Model Canvas — Tony Hoang Company]] — 9 ô mô hình kinh doanh
- [[_MHKD Tony Hoang Company — Tổng Quan]] — chi tiết phân khúc & giá trị cốt lõi
- [[Đánh Giá Mô Hình Kinh Doanh — Tony Hoang Company]] — đánh giá tính nhất quán và rủi ro

---

## Khi nào cập nhật lại file này

- Ra mắt dòng sản phẩm thuộc loại khác (đang bán dịch vụ, thêm khoá học online)
- Chu kỳ bán thay đổi trên 30% so với lần đo trước
- Mở kênh bán mới làm đổi tham số sở hữu điểm chạm
- Sau mỗi lần rà quý ở Bước 12

Mỗi lần đổi, ghi lý do vào `Decisions/` — vì thay đổi ở đây kéo theo thay đổi ở hàng chục chỗ khác.
