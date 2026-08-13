---
name: pricing-strategy
description: "Xây chiến lược giá: định vị trên thị trường, phân tích giá trị cảm nhận và cách thử độ nhạy giá. Dùng khi đặt giá lần đầu hoặc chuẩn bị điều chỉnh giá."
allowed-tools: Read Write
ten-viet: "Chiến Lược Giá"
nhom: "07. Bán Hàng & Phễu"
ten-goc: "Pricing Strategy"
---

# Chiến Lược Giá

## Khi nào dùng skill này

Dùng khi cần:
- Đặt giá cho sản phẩm hoặc dịch vụ mới
- Đánh giá và điều chỉnh mức giá đang bán
- Thiết kế cơ cấu giá theo bậc hoặc theo giá trị
- Phân tích giá đối thủ và định vị offer của mình

**KHÔNG dùng** để làm cơ cấu hoa hồng (dùng `commission-structure`) hay phân tích chi phí thuần tuý (dùng `cost-analysis`). Skill này dành cho quyết định giá mang tính chiến lược.

---

## Nguyên tắc cốt lõi

GIÁ LÀ MỘT TÍN HIỆU — NÓ NÓI LÊN GIÁ TRỊ, ĐỊNH VỊ THƯƠNG HIỆU VÀ QUYẾT ĐỊNH AI SẼ LÀ KHÁCH CỦA BẠN. ĐỪNG BAO GIỜ ĐẶT GIÁ CHỈ DỰA TRÊN CHI PHÍ.

---

## Giai đoạn 1: Đầu vào

### Đầu vào bắt buộc

| Đầu vào | Câu hỏi | Mặc định |
|---|---|---|
| **Sản phẩm/dịch vụ** | "Anh chị đang định giá cho cái gì?" | Không có mặc định — bắt buộc phải có |
| **Chi phí để giao được** | "Giao được cái này tốn bao nhiêu? (giá vốn, thời gian, nguyên vật liệu)" | Không có mặc định — bắt buộc phải có |
| **Khách mục tiêu** | "Người mua lý tưởng là ai? (mức chi trả, độ am hiểu)" | Chủ doanh nghiệp nhỏ và cá nhân kinh doanh |
| **Giá đối thủ** | "Đối thủ đang bán thứ tương tự với giá bao nhiêu?" | Chưa rõ — sẽ nghiên cứu |
| **Giá hiện tại (nếu có)** | "Hiện anh chị đang bán giá nào?" | Sản phẩm mới — chưa có giá |
| **Mô hình doanh thu** | "Thu một lần, thuê bao, phí duy trì hằng tháng, hay tính theo mức dùng?" | Thu một lần |

**CỔNG: Không đi tiếp khi chưa có sản phẩm, chi phí giao hàng và khách mục tiêu.**

---

## Giai đoạn 2: Phân tích giá

### Nền tảng: giá theo chi phí

```
## Phân tích chi phí

| Khoản mục | Chi phí |
|---|---|
| Chi phí trực tiếp (nguyên vật liệu, giá vốn, giao hàng) | [X] đ |
| Chi phí thời gian (số giờ × đơn giá giờ) | [X] đ |
| Chi phí chung phân bổ | [X] đ |
| **Tổng chi phí để giao được** | **[X] đ** |

| Hệ số nhân | Giá bán | Biên lợi nhuận |
|---|---|---|
| 2 lần chi phí | [X] đ | 50% |
| 3 lần chi phí | [X] đ | 67% |
| 5 lần chi phí | [X] đ | 80% |
```

### Giá theo giá trị

```
## Phân tích giá trị

| Yếu tố giá trị | Mô tả | Giá trị ước tính với khách |
|---|---|---|
| Thời gian tiết kiệm được | [Số giờ × giá trị một giờ của khách] | [X] đ |
| Doanh thu tạo thêm | [Tác động doanh thu dự kiến] | [X] đ |
| Chi phí tránh được | [Khoản chi bị loại bỏ nhờ dùng sản phẩm] | [X] đ |
| Rủi ro giảm đi | [Vấn đề được ngăn chặn] | [X] đ |
| **Tổng giá trị mang lại** | | **[X] đ** |

**Khoảng giá theo giá trị:** 10–20% tổng giá trị mang lại = [X] đ – [X] đ
```

### Định vị so với đối thủ

```
## Định vị trên thị trường

| Đối thủ | Giá | Định vị |
|---|---|---|
| [Đối thủ 1] | [X] đ | [Cao cấp / Tầm trung / Giá rẻ] |
| [Đối thủ 2] | [X] đ | [Cao cấp / Tầm trung / Giá rẻ] |
| [Đối thủ 3] | [X] đ | [Cao cấp / Tầm trung / Giá rẻ] |

**Ba lựa chọn định vị:**
- **Cao cấp (trên mặt bằng):** Cần có điểm khác biệt rõ, nhiều bằng chứng xã hội và trải nghiệm xứng tầm
- **Ngang thị trường:** An toàn nhưng không khác biệt, phải cạnh tranh bằng tính năng
- **Dưới mặt bằng (giá thâm nhập):** Có số lượng nhanh nhưng rất khó tăng giá về sau, và phát tín hiệu chất lượng thấp
```

---

## Giai đoạn 3: Cơ cấu giá

### Chọn mô hình phù hợp

**Một mức giá duy nhất:**
Hợp với: sản phẩm đơn giản, giá trị rõ ràng, khách quyết định nhanh

**Giá theo bậc (Cơ bản / Tiêu chuẩn / Cao cấp):**
```
| Bậc | Giá | Gồm những gì | Nhắm tới ai |
|---|---|---|---|
| [Cơ bản] | [X] đ | [Tính năng lõi] | Khách nhạy cảm về giá |
| [Tiêu chuẩn] | [X] đ | [Lõi + nâng cao] | Phần lớn khách (neo ở đây) |
| [Cao cấp] | [X] đ | [Tất cả + phần thêm] | Khách dùng nhiều, doanh nghiệp |
```
Hợp với: phần mềm, khoá học, gói dịch vụ

**Thuê bao:**
Giá theo tháng so với theo năm, có ưu đãi khi cam kết cả năm (thường giảm 15–20% so với trả tháng)

**Trả theo kết quả:**
Giá gắn với kết quả thật sự mang lại — thu được nhiều giá trị nhất, nhưng cũng rủi ro nhất

### Kỹ thuật neo giá

- Trình bày bậc cao nhất trước để neo cảm nhận
- Bậc giữa mới là bậc mục tiêu — phần lớn khách sẽ chọn bậc này
- Thêm một bậc mồi nếu cần, để bậc mục tiêu trông đáng tiền nhất

---

## Giai đoạn 4: Kế hoạch thử nghiệm

### Thử độ nhạy giá

```
## Kế hoạch thử giá

### Cách bố trí thử nghiệm
- Thử 2–3 mức giá cùng lúc
- Tối thiểu 100 lượt truy cập mỗi phương án mới đủ tin cậy
- Đo: tỷ lệ chuyển đổi, doanh thu trên mỗi lượt truy cập, tổng doanh thu

### Các mức giá cần thử
| Phương án | Giá | Giả thuyết |
|---|---|---|
| A (hiện tại/thấp) | [X] đ | Chuyển đổi cao hơn, doanh thu mỗi đơn thấp hơn |
| B (mục tiêu) | [X] đ | Cân bằng giữa chuyển đổi và doanh thu |
| C (cao cấp) | [X] đ | Chuyển đổi thấp hơn, doanh thu mỗi đơn cao hơn |

### Tín hiệu cần theo dõi
- Tỷ lệ chuyển đổi tụt trên 30% ở mức giá cao = giá quá cao
- Chuyển đổi không đổi ở mức giá cao = còn dư địa tăng giá
- Tỷ lệ hoàn tiền cao ở mọi mức giá = vấn đề nằm ở chất lượng giao hàng, không phải ở giá
```

---

## Ví dụ: định giá một khoá học trực tuyến

**Chi phí:** 50 triệu để sản xuất, 120 nghìn chi phí giao hàng mỗi lượt bán.
**Giá trị:** Học viên tiết kiệm 10 giờ mỗi tuần (tương đương 2,5 triệu/tuần với đơn giá 250 nghìn/giờ).
**Đối thủ:** khoảng 2,4 – 12 triệu.

**Khuyến nghị:** Một mức 4,9 triệu, hoặc ba bậc 2,4 / 4,9 / 12 triệu. Bậc giữa (4,9 triệu) gồm khoá học và bộ mẫu biểu. Bậc cao cấp (12 triệu) thêm các buổi kèm riêng. Mức giá này lấy khoảng 2% giá trị mà học viên nhận được mỗi tháng.

---

## Những lỗi thường gặp

- **Chỉ định giá theo chi phí** — chi phí của bạn không liên quan gì tới người mua. Định giá theo giá trị mang lại, không theo chi phí bỏ ra.
- **Copy giá đối thủ** — điểm khác biệt của bạn phải biện minh được cho một mức giá khác. Học mô hình giá, đừng chép con số.
- **Đặt giá thấp vì sợ** — giá thấp hút đúng nhóm khách nhạy cảm về giá, và đây lại là nhóm rời bỏ nhanh nhất, phàn nàn nhiều nhất.
- **Quá nhiều bậc giá** — tối đa 3 bậc. Nhiều hơn là khách tê liệt không chọn được.
- **Không bao giờ thử** — đặt giá, thử, rồi điều chỉnh. Giá là thứ lặp đi lặp lại, không phải chốt một lần là xong.

---

## Xử lý tình huống

- **Không có dữ liệu đối thủ:** Định giá theo phân tích giá trị. Lấy quy tắc 10–20% giá trị mang lại làm điểm khởi đầu.
- **Sản phẩm phổ thông, không có gì khác biệt:** Cạnh tranh bằng trải nghiệm, cách đóng gói hoặc cam kết bảo đảm — đừng cạnh tranh bằng giá. Hoặc tìm một ngách hẹp hơn để tạo được khác biệt.
- **Cần tăng giá sản phẩm đang bán:** Giữ giá cũ cho khách hiện hữu, áp giá mới cho khách mới. Đi kèm việc tăng giá phải là một phần giá trị tăng thêm được nói rõ.
- **Khách nói đắt quá:** Bình thường — nên có khoảng 20–30% người hỏi thấy bạn đắt. Nếu không ai thấy đắt, nghĩa là bạn đang bán quá rẻ.

---

## Ghi kết quả vào đâu

> [!important] Không ghi vào vault thì coi như chưa làm
> Kết quả chỉ hiện trong khung chat sẽ mất khi đóng phiên. Hệ thống chỉ thông minh bằng đúng dữ liệu được ghi lại.

| | |
|---|---|
| **Thư mục** | `00. Business Context/Sản Phẩm & Dịch Vụ/` |
| **Tên file** | cập nhật hồ sơ sản phẩm tương ứng |
| **Bắt buộc** | Quyết định giá ghi thêm vào `Decisions/` |

Sau khi ghi xong, báo lại cho người dùng **đường dẫn đầy đủ** của file vừa tạo để họ mở kiểm tra.
