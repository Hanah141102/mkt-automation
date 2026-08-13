---
name: ke-hoach-hang-hoa
description: "Nối kế hoạch marketing với kế hoạch hàng hoá: dự báo bán theo chiến dịch, tính ngưỡng đặt hàng lại, thời gian chờ nhà cung cấp và mức tồn an toàn, để không cháy hàng giữa lúc quảng cáo đang chạy. Dùng cho doanh nghiệp bán hàng vật lý."
allowed-tools: Read Write Glob
ten-viet: "Kế Hoạch Hàng Hoá"
nhom: "11. Vận Hành & Công Nghệ"
ten-goc: "Kế Hoạch Hàng Hoá"
---

# Kế Hoạch Hàng Hoá

## Khi nào dùng skill này

- Bán hàng vật lý — `loai-san-pham: vat-ly` hoặc `hon-hop` trong Hồ Sơ Mô Hình Kinh Doanh
- Đã từng cháy hàng giữa chiến dịch, hoặc ngược lại: ôm tồn kho không bán được
- Chuẩn bị chạy quảng cáo mạnh, mùa cao điểm, hoặc ra mắt sản phẩm mới
- Nhập hàng từ nhà cung cấp có thời gian chờ dài

**KHÔNG dùng** cho sản phẩm số hoặc dịch vụ — hai loại đó không có ràng buộc tồn kho.

---

## Nguyên tắc cốt lõi

MARKETING VÀ HÀNG HOÁ PHẢI CHẠY CÙNG MỘT LỊCH. QUẢNG CÁO TỐT MÀ HẾT HÀNG KHÔNG PHẢI THÀNH CÔNG — ĐÓ LÀ TIỀN QUẢNG CÁO ĐỔ ĐI KÈM THEO MẤT THỨ HẠNG GIAN HÀNG VÀ MẤT KHÁCH VÀO TAY ĐỐI THỦ.

---

## Giai đoạn 1: Lấy ngữ cảnh

Đọc trước: `00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md` (mùa vụ, chu kỳ bán) và `Sản Phẩm & Dịch Vụ/`.

| Đầu vào | Câu hỏi | Mặc định |
|---|---|---|
| **Danh mục hàng** | "Anh chị đang bán bao nhiêu mã hàng? Mã nào chiếm nhiều doanh thu nhất?" | Bắt buộc phải có |
| **Thời gian chờ hàng** | "Từ lúc đặt nhà cung cấp tới lúc hàng về kho mất bao lâu? Có mã nào lâu hơn hẳn không?" | Bắt buộc phải có |
| **Số lượng đặt tối thiểu** | "Mỗi lần đặt phải lấy ít nhất bao nhiêu?" | Không có ràng buộc |
| **Tồn hiện tại** | "Hiện còn bao nhiêu mỗi mã?" | Chưa đếm |
| **Tốc độ bán** | "Trung bình mỗi tuần bán bao nhiêu mỗi mã? Tuần cao nhất thì bao nhiêu?" | Chưa đo |
| **Hạn sử dụng** | "Hàng có hạn không? Bao lâu?" | Không có hạn |

**CỔNG: Không có thời gian chờ hàng và tốc độ bán thì không tính được gì. Hỏi trước, đừng đoán.**

---

## Giai đoạn 2: Ba con số phải tính cho từng mã hàng

### 1. Mức tồn an toàn

Đệm để chịu được lúc bán nhanh bất thường hoặc hàng về trễ.

```
Tồn an toàn = (Tốc độ bán tuần cao nhất − Tốc độ bán trung bình) × Thời gian chờ (tính theo tuần)
```

### 2. Ngưỡng đặt lại

Chạm ngưỡng này là phải đặt hàng ngay, không chờ hết.

```
Ngưỡng đặt lại = (Tốc độ bán trung bình tuần × Thời gian chờ tuần) + Tồn an toàn
```

### 3. Số ngày còn bán được

Chỉ số cảnh báo, đọc hằng tuần.

```
Số ngày còn lại = Tồn hiện tại ÷ (Tốc độ bán trung bình tuần ÷ 7)
```

| Số ngày còn lại | Trạng thái | Hành động |
|---|---|---|
| Nhiều hơn 2× thời gian chờ | 🟢 An toàn | Không làm gì |
| 1–2× thời gian chờ | 🟡 Cần đặt | Đặt hàng trong tuần này |
| Dưới 1× thời gian chờ | 🔴 Sắp cháy | Đặt gấp **và giảm ngân sách quảng cáo cho mã này** |
| Dưới 7 ngày | ⛔ Khẩn | Tạm dừng quảng cáo mã này, chuyển ngân sách sang mã còn hàng |

---

## Giai đoạn 3: Nối với lịch marketing

Đây là phần khác biệt so với một bảng quản lý kho thông thường.

### Trước mỗi chiến dịch — bắt buộc kiểm tra

```
CHECKLIST TRƯỚC KHI BẬT QUẢNG CÁO

- [ ] Mã hàng sẽ chạy quảng cáo có đủ hàng cho **ít nhất 1,5 lần thời gian chờ** không?
- [ ] Nếu chiến dịch chạy gấp đôi kỳ vọng, có đủ hàng không?
- [ ] Nhà cung cấp đã được báo trước về đợt tăng chưa?
- [ ] Có phương án B nếu cháy hàng: mã thay thế, mở đặt trước, hay tắt quảng cáo?
```

Nếu không tick được đủ 4 ô, **lùi ngày bật quảng cáo** thay vì chạy rồi cháy hàng.

### Trước mùa cao điểm

Đọc `thang-cao-diem` trong Hồ Sơ Mô Hình Kinh Doanh, rồi tính ngược:

```
Ngày đặt hàng muộn nhất = Ngày bắt đầu mùa cao điểm − Thời gian chờ − 2 tuần đệm
```

Ghi ngày này vào lịch, đặt nhắc. Đây là mốc hay bị lỡ nhất.

### Sau chiến dịch

Đối chiếu bán thật với dự báo. Sai số trên 30% thì phải chỉnh lại cách dự báo, không chỉ chỉnh số lượng đặt.

---

## Giai đoạn 4: Xử lý hàng chậm

Hàng tồn lâu là tiền chết, và với hàng có hạn thì là tiền sắp mất.

| Số ngày tồn | Hành động |
|---|---|
| Quá 2× chu kỳ bán bình thường | Đưa vào combo với mã bán chạy |
| Quá 3× | Giảm giá có thời hạn, chạy `/discount-strategy` |
| Quá 4×, hoặc còn 1/3 hạn sử dụng | Xả — thà thu hồi vốn còn hơn ôm |

**Luật:** không nhập thêm mã nào đang ở nhóm chậm, kể cả khi nhà cung cấp chào giá tốt.

---

## Đầu ra

Một bảng theo dõi cập nhật hằng tuần:

| Mã hàng | Tồn | Bán/tuần | Ngày còn lại | Ngưỡng đặt lại | Trạng thái | Có đang chạy QC? |
|---|---|---|---|---|---|---|
| | | | | | 🟢🟡🔴 | |

Kèm: ngày đặt hàng muộn nhất cho mùa cao điểm · danh sách mã chậm cần xử lý · checklist trước chiến dịch.

---

## Ghi kết quả vào đâu

| | |
|---|---|
| **Thư mục** | `03. Areas/Analytics & Reporting/` (tạo thư mục con `Hàng Hoá & Tồn Kho/`) |
| **Tên file** | `Tồn Kho Tuần [NN-YYYY].md` · `Kế Hoạch Nhập Mùa [Tên mùa].md` |
| **Bắt buộc** | Link tới file chiến dịch quảng cáo tương ứng trong `03. Areas/Marketing Channels/` |

Quyết định nhập hàng lớn hoặc xả hàng ghi thêm vào `Decisions/`.

---

## Ràng buộc

- **Không bật quảng cáo cho mã sắp hết.** Đây là lỗi tốn tiền nhất và cũng phổ biến nhất.
- **Không dự báo bằng cảm tính khi đã có 3 tháng dữ liệu.** Dùng số thật.
- **Không nhập theo giá tốt.** Nhập theo tốc độ bán.
- Với hàng có hạn sử dụng, luôn tính ngược từ hạn — không chỉ tính từ tốc độ bán.
