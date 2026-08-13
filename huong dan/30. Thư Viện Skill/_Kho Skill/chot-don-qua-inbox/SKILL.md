---
name: chot-don-qua-inbox
description: "Xây kịch bản chốt đơn qua inbox Facebook, Instagram và TikTok Shop: trả lời bình luận kéo về inbox, tin nhắn tự động chào, khai thác nhu cầu, báo giá và chốt. Kèm quy tắc tốc độ phản hồi và cách bàn giao ca trực. Dùng khi khách nhắn thẳng vào trang thay vì để lại số."
allowed-tools: Read Write Glob
ten-viet: "Chốt Đơn Qua Inbox"
nhom: "07. Bán Hàng & Phễu"
ten-goc: "Chốt Đơn Qua Inbox"
---

# Chốt Đơn Qua Inbox

## Khi nào dùng skill này

- Khách nhắn thẳng vào fanpage, Instagram hoặc gian hàng TikTok Shop
- Bình luận dưới bài đăng nhiều nhưng không kéo được về inbox
- Nhiều người cùng trực inbox, khách bị hỏi lại thông tin đã trả lời
- Muốn đo được phễu chat: bao nhiêu người nhắn, bao nhiêu người chốt

**KHÁC với `/chot-don-qua-zalo`:** Zalo là kênh khách đã cho số, quan hệ gần hơn, nhắn được dài. Inbox là kênh **khách còn lạ, sốt ruột, và đang so sánh nhiều shop cùng lúc** — tốc độ và sự rõ ràng quan trọng hơn sự tinh tế.

---

## Nguyên tắc cốt lõi

TRONG INBOX, NGƯỜI TRẢ LỜI TRƯỚC THẮNG. KHÁCH THƯỜNG NHẮN 3–5 SHOP CÙNG LÚC VÀ MUA CỦA SHOP TRẢ LỜI ĐẦU TIÊN VỚI CÂU TRẢ LỜI RÕ RÀNG NHẤT — KHÔNG PHẢI SHOP RẺ NHẤT.

---

## Giai đoạn 1: Lấy ngữ cảnh

| Đầu vào | Câu hỏi | Mặc định |
|---|---|---|
| **Nền tảng** | "Khách nhắn qua Facebook, Instagram hay TikTok Shop?" | Facebook |
| **Sản phẩm** | "Bán gì, giá bao nhiêu, có bao nhiêu phiên bản?" | Đọc `00. Business Context/Sản Phẩm & Dịch Vụ/` |
| **Ai trực** | "Mấy người trực inbox, có chia ca không?" | 1 người |
| **Giờ trực** | "Trực từ mấy giờ tới mấy giờ?" | Giờ hành chính |
| **Câu hỏi hay gặp** | "5 câu khách hay hỏi nhất là gì?" | Giá, tồn kho, ship, bảo hành, cách dùng |

---

## Giai đoạn 2: Kéo bình luận về inbox

Bình luận là nơi khách bộc lộ nhu cầu công khai. Không kéo về inbox là mất khách cho đối thủ đang đọc cùng bài đó.

**Quy tắc trả lời bình luận:**

1. **Trả lời công khai một câu ngắn** — để người khác đọc cũng thấy shop có phản hồi
2. **Không báo giá công khai** nếu sản phẩm có nhiều phiên bản — sẽ tạo hiểu lầm
3. **Nhắn riêng ngay trong 2 phút** — đừng đợi khách tự inbox

```
Mẫu trả lời bình luận:
Công khai:  "Dạ có ạ, em nhắn riêng thông tin chi tiết cho mình nhé anh/chị ơi 💬"
Inbox ngay: "Em chào anh/chị ạ, em thấy anh/chị vừa hỏi về [sản phẩm] dưới bài [tên bài].
             Anh/chị đang cần loại [A] hay [B] ạ?"
```

Nhắc lại đúng bài khách đã bình luận — khách nhớ ngay và tin là người thật, không phải bot.

---

## Giai đoạn 3: Kịch bản inbox 4 nhịp

### Nhịp 1 — Tin chào tự động (dưới 30 giây)

Đặt tin nhắn chào tự động để khách không rơi vào im lặng. Nội dung bắt buộc:

```
Dạ em chào anh/chị, [Thương hiệu] xin nghe ạ 🌿
Em đang có mặt và sẽ trả lời anh/chị trong ít phút.
Trong lúc đợi, anh/chị cho em biết đang quan tâm:
1️⃣ [Sản phẩm/dịch vụ A]
2️⃣ [Sản phẩm/dịch vụ B]
3️⃣ Tư vấn xem loại nào hợp
```

Đánh số để khách chỉ cần gõ một chữ số. Đây là cách rẻ nhất để phân loại nhu cầu trước khi người thật vào.

### Nhịp 2 — Trả lời đúng câu hỏi, rồi mới hỏi lại

Sai lầm phổ biến nhất: khách hỏi giá, sale trả lời "anh/chị cho em xin số điện thoại ạ". Khách thoát ngay.

**Luật: trả lời trước, hỏi sau.**

```
Khách: "Giá bao nhiêu shop?"
Sai:   "Anh/chị để lại sđt em tư vấn ạ"
Đúng:  "Dạ gói [A] là [giá] ạ, gói [B] đầy đủ hơn là [giá].
        Anh/chị đang cần cho [tình huống 1] hay [tình huống 2] để em tư vấn đúng gói nhé?"
```

### Nhịp 3 — Khai thác và chốt

Inbox không có nhiều thời gian như Zalo. Tối đa **3 câu hỏi** trước khi chốt:

1. Dùng cho ai / tình huống nào
2. Đã dùng sản phẩm tương tự chưa
3. Cần khi nào

Rồi chốt ngay bằng câu **giả định đã mua**: *"Em lên đơn gói [B] cho anh/chị nhé, mình lấy màu [X] đ hay [Y] ạ?"*

### Nhịp 4 — Lấy thông tin và xác nhận

```
Checklist thông tin cần lấy:
- Họ tên
- Số điện thoại
- Địa chỉ (nếu giao hàng)
- Phương thức thanh toán
→ Nhắn lại toàn bộ để khách xác nhận trước khi lên đơn
```

Sau khi chốt, **xin kết bạn Zalo** để chăm sóc lâu dài — inbox nền tảng dễ mất, Zalo thì không. Từ đó chuyển sang `/chot-don-qua-zalo` cho các lần mua sau.

---

## Giai đoạn 4: Quy tắc vận hành inbox

### Tốc độ phản hồi — chỉ số quan trọng nhất

| Thời gian phản hồi | Kết quả thực tế |
|---|---|
| Dưới 5 phút | Tỷ lệ chốt cao nhất |
| 5–30 phút | Còn cứu được, khách đã hỏi shop khác |
| Trên 1 giờ | Phần lớn đã mua chỗ khác |
| Ngoài giờ | Bắt buộc có tin tự động hẹn giờ trả lời cụ thể |

### Bàn giao ca trực

Khi nhiều người cùng trực, khách hay bị hỏi lại thông tin đã nói. Quy tắc:

1. Người nhận ca **đọc lại toàn bộ hội thoại** trước khi nhắn
2. Ghi nhãn hội thoại theo trạng thái: `đang tư vấn` · `chờ khách quyết` · `đã chốt` · `mất`
3. Cuối ca, ghi tóm tắt các khách đang dở vào `01. Inbox/` để ca sau nắm

### Ghi vào vault

| Ghi gì | Ghi vào đâu |
|---|---|
| Khách đã chốt | `People/` + cập nhật pipeline |
| Số liệu chat tuần (số inbox, số chốt, tốc độ rep, lý do mất) | `03. Areas/Analytics & Reporting/Chăm Sóc Khách Hàng/` |
| Câu hỏi mới hay gặp | `01. Inbox/` → tuần sau bổ sung vào tin chào tự động và `/faq-generator` |

---

## Giai đoạn 5: Đo phễu chat

Đây là phễu hay bị bỏ đo nhất, trong khi nó ra tiền trực tiếp.

```
Bình luận / hiển thị
    ↓ tỷ lệ kéo về inbox
Số hội thoại mở
    ↓ tỷ lệ phản hồi trong 5 phút
Hội thoại được tư vấn
    ↓ tỷ lệ hỏi giá
Hội thoại có báo giá
    ↓ tỷ lệ chốt
Đơn hàng
```

Ghi số hằng tuần vào `03. Areas/Analytics & Reporting/Chăm Sóc Khách Hàng/`. Chạy `/mkt-marketing-performance-analysis` để tìm khúc rơi nhiều nhất.

---

## Đầu ra

- Tin nhắn chào tự động cho từng nền tảng
- Bộ mẫu trả lời cho 5–10 câu hỏi hay gặp nhất
- Kịch bản 4 nhịp copy dán được
- Quy tắc bàn giao ca trực
- Bảng chỉ số phễu chat để ghi hằng tuần

Lưu vào `04. Resources/Playbooks/Kịch Bản Chốt Đơn Qua Inbox.md`.

---

## Ràng buộc

- **Trả lời trước, xin thông tin sau.** Xin số trước khi trả lời là cách mất khách nhanh nhất.
- **Không dùng bot thay hoàn toàn người thật.** Bot chỉ để phân loại và giữ chân trong 30 giây đầu.
- **Không hứa ngoài phạm vi sản phẩm.** Chỉ nói những gì có trong hồ sơ sản phẩm.
- **Không để hội thoại quá 24 giờ không phản hồi** — nền tảng đánh giá thấp và giảm hiển thị trang.
- Emoji dùng vừa phải, theo đúng giọng trong `Brand Voice`. Thương hiệu nghiêm túc không rắc emoji khắp nơi.
