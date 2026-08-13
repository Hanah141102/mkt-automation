---
name: ghi-cuoc-gap
description: "Ghi một lần, tự cập nhật bốn chỗ. Nhận mô tả tự do bằng tiếng Việt về một cuộc gặp, cuộc gọi hay tin nhắn với khách, rồi tự tạo biên bản, cập nhật hồ sơ khách, chuyển trạng thái pipeline và lưu câu khách nói vào thư viện. Dùng ngay sau mỗi lần trao đổi với khách."
allowed-tools: Read Write Edit Glob Grep
ten-viet: "Ghi Cuộc Gặp"
nhom: "07. Bán Hàng & Phễu"
ten-goc: "Ghi Cuộc Gặp"
---

# Ghi Cuộc Gặp

## Khi nào dùng skill này

Ngay sau khi vừa nói chuyện với khách — gọi điện, nhắn Zalo, trả lời inbox, gặp trực tiếp.

**Vấn đề skill này giải quyết:** hiện tại một cuộc gặp phải ghi bốn chỗ — biên bản, hồ sơ khách, pipeline, thư viện lời khách. Bốn lần gõ cho một sự việc. Đây là lý do người ta bỏ ghi, và bỏ ghi là lý do hệ thống chết.

Người dùng chỉ cần **kể lại bằng lời của mình**. Skill lo phần còn lại.

---

## Nguyên tắc cốt lõi

MA SÁT GHI CHÉP LÀ KẺ THÙ SỐ MỘT CỦA HỆ THỐNG. NGƯỜI DÙNG CHỈ NÊN PHẢI GÕ **MỘT LẦN**, BẰNG NGÔN NGỮ TỰ NHIÊN, KHÔNG THEO MẪU. MỌI VIỆC TÁCH DỮ LIỆU VÀ CẬP NHẬT ĐÚNG CHỖ LÀ VIỆC CỦA AI.

---

## Cách người dùng gọi

```
/ghi-cuoc-gap vừa gọi chị Lan hỏi khoá tiếng Anh cho con lớp 3,
chị lo con nhút nhát không dám nói, hỏi giá xong bảo để bàn với chồng,
hẹn thứ 5 gọi lại
```

Không cần đúng cấu trúc. Không cần đủ thông tin. Thiếu gì thì hỏi lại **tối đa ba câu**, rồi làm.

---

## Quy trình

### Bước 1 — Tách thông tin

Từ đoạn mô tả, rút ra:

| Trường | Cách rút | Nếu thiếu |
|---|---|---|
| Tên khách | Tên riêng xuất hiện trong câu | Hỏi lại |
| Kênh | "gọi" → điện thoại · "nhắn/Zalo" → Zalo · "inbox" → inbox · "gặp" → trực tiếp | Đoán từ ngữ cảnh |
| Ngày | Mặc định hôm nay, trừ khi nói "hôm qua", "thứ 2 vừa rồi" | Lấy hôm nay |
| Nhu cầu | Sản phẩm hoặc dịch vụ khách hỏi | Hỏi lại |
| Điểm đau | Câu thể hiện lo lắng, khó khăn của khách | Để trống, đánh dấu cần bổ sung |
| Phản đối | Lý do khách chưa quyết | Để trống |
| Bước tiếp | Hẹn gì, khi nào | Hỏi lại |
| Trạng thái mới | Suy ra từ nội dung (xem bảng dưới) | Đề xuất, để người dùng xác nhận |

### Bước 2 — Suy trạng thái pipeline

| Dấu hiệu trong lời kể | Trạng thái |
|---|---|
| Mới liên hệ lần đầu, chưa khai thác được gì | Đã liên hệ |
| Đã biết nhu cầu, đang trao đổi | Đang tư vấn |
| Đã nói giá cho khách | Đã báo giá |
| Khách nói "để suy nghĩ", "bàn với...", "cuối tháng quyết" | Chờ quyết |
| Khách đã chuyển tiền, đã ký | Thắng |
| Khách nói không mua, chọn bên khác | Thua — **bắt buộc hỏi lý do bằng lời khách** |
| Khách nói chưa phải lúc, vài tháng nữa | Nuôi dài hạn |

**Luôn hiện trạng thái đề xuất cho người dùng xác nhận** trước khi ghi. Không tự chuyển trạng thái Thắng hoặc Thua mà không hỏi.

### Bước 3 — Ghi vào bốn chỗ

**① Biên bản** → `Meetings/YYYY-MM-DD — [Kênh] — [Tên khách].md`

Dùng mẫu `Meetings/[Mẫu] Biên Bản Gặp Khách.md`. Phần **"Khách nói gì"** chép nguyên văn nếu người dùng có trích lời khách.

**② Hồ sơ khách** → `People/[Tên] — [Nguồn] (PK<số>).md`

- Chưa có file → tạo mới từ mẫu `People/[Mẫu] Hồ Sơ Khách.md`
- Đã có → **thêm dòng vào bảng "Đã trao đổi gì"**, cập nhật `trang-thai` và `cham-gan-nhat` trong frontmatter, bổ sung điểm đau mới nếu có
- Không ghi đè nội dung cũ

**③ Pipeline** → `03. Areas/Sales Pipeline & CRM/Pipeline Tháng [MM-YYYY].md`

Cập nhật dòng của khách trong bảng "Đang chạy": trạng thái, ngày chạm gần nhất, bước tiếp. Nếu chuyển sang Thắng hoặc Thua thì chuyển dòng xuống bảng tương ứng.

**④ Thư viện lời khách** → `04. Resources/Feedback & Chứng Thực/Thư Viện Lời Khách.md`

Nếu người dùng có trích câu khách nói, thêm vào thư viện kèm ngày, tên khách, giai đoạn, chủ đề. Đây là nguyên liệu cho content, quảng cáo và cải thiện offer sau này — chép **nguyên văn**, không viết lại cho hay.

### Bước 4 — Báo lại gọn

```
✓ Đã ghi 4 chỗ:
  Meetings/2026-08-21 — Gọi điện — Chị Lan.md
  People/Chị Lan — Facebook (PK1).md          (thêm điểm đau: con nhút nhát)
  Pipeline Tháng 08-2026.md                    (Đã liên hệ → Đã báo giá)
  Thư Viện Lời Khách.md                        (+1 câu, chủ đề: lo con nhút nhát)

⏰ Bước tiếp: gọi lại thứ 5 (24/08)
⚠️  Chưa có: nguồn khách đến từ đâu, ngân sách dự kiến
```

---

## Trường hợp đặc biệt

**Khách mới hoàn toàn** → tạo hồ sơ mới, hỏi thêm nguồn (`quảng cáo / giới thiệu / tự tìm thấy`) để chấm điểm lead đúng.

**Nhiều khách trong một lần gõ** → tách thành nhiều bộ hồ sơ riêng, không gộp.

**Cuộc gặp với công ty, không phải cá nhân** → tạo thêm file trong `Companies/`, link hai chiều.

**Khách nói câu đáng giá cho marketing** → ngoài thư viện lời khách, gợi ý người dùng cân nhắc làm nội dung từ câu đó.

**Deal Thua** → bắt buộc hỏi *"khách nói lý do gì, anh chị nhớ nguyên văn không?"*. Lý do thua ghi bằng lời khách là dữ liệu quý nhất trong toàn bộ vault.

---

## Ghi kết quả vào đâu

Đã ghi ở Bước 3 — bốn nơi cùng lúc. Không tạo file nào ngoài bốn nơi đó.

---

## Ràng buộc

- **Không bịa thông tin không có trong lời kể.** Thiếu thì đánh dấu ⚠️ để người dùng bổ sung sau.
- **Không ghi đè nội dung cũ trong hồ sơ khách** — luôn thêm vào, giữ lịch sử.
- **Không tự chuyển sang Thắng hoặc Thua** mà không có xác nhận.
- **Không hỏi quá 3 câu.** Ghi thiếu còn hơn không ghi. Người dùng đang bận, hỏi nhiều là họ bỏ.
- Chép lời khách **nguyên văn**, kể cả khi câu văn lủng củng. Đó là giá trị của nó.
