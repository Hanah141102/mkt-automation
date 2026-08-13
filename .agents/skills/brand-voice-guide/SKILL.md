---
name: brand-voice-guide
description: "Soạn cẩm nang giọng thương hiệu cho doanh nghiệp Việt Nam: chốt xưng hô, 4 thuộc tính giọng, danh sách từ nên dùng và từ cấm bằng tiếng Việt, 10 quy tắc văn phong, và giọng riêng cho từng kênh (Zalo, inbox Facebook, TikTok, email, landing page, chatbot). Sinh ra file mà mọi skill viết nội dung sau này đều đọc. Dùng khi cần mọi người viết ra nghe như cùng một thương hiệu, khi thuê freelancer viết bài, khi content mỗi bài một giọng, hoặc khi chuẩn bị làm landing page và chatbot."
allowed-tools: Read Write Glob Grep
ten-viet: "Cẩm Nang Giọng Thương Hiệu"
nhom: "02. Thương Hiệu & Thiết Kế"
ten-goc: "Brand Voice Guide"
---

# Cẩm Nang Giọng Thương Hiệu

> [!important] File này là đầu vào của hàng chục skill khác
> `Brand Voice — Giọng Thương Hiệu.md` không phải một tài liệu để đọc cho vui. Nó là **nguồn cấu hình** mà `/content-copywriter`, `/blog-post`, `/mkt-caption-writer`, `/ads-copywriting`, `/email-sequence`, `/chot-don-qua-zalo`, `/chot-don-qua-inbox`, `/ui-ux-pro-max`, `/biz-email-setup`, `/biz-nextjs-chatbot-openrouter` đều phải đọc trước khi viết một chữ nào.
>
> Vì vậy **cấu trúc heading của file đầu ra là cố định** — xem Giai đoạn 4. Đổi heading là làm hỏng skill khác.

> [!warning] Đọc `Hồ Sơ Mô Hình Kinh Doanh` trước
> Ba tham số trong `00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md` thay đổi hẳn giọng nên chọn:
>
> | Tham số | Ảnh hưởng tới giọng |
> |---|---|
> | `nguoi-mua-la-nguoi-dung: khong` | **Bắt buộc dựng giọng hai lớp** — người trả tiền và người dùng nghe hai thứ khác nhau. Xem Giai đoạn 3b. |
> | `chu-ky-ban-ngay` ≥ 30 | Giọng nghiêng về **bằng chứng và chuyên môn** — khách cân nhắc lâu, cần lý do tin. Dưới 30 ngày thì nghiêng về **rõ ràng và thúc đẩy**. |
> | `loai-san-pham` | `dich-vu` → giọng gắn với con người, xưng "bên mình/chúng tôi". `so` → giọng gắn với sản phẩm, có thể xưng tên thương hiệu. `vat-ly` → giọng gắn với trải nghiệm và cảm giác. |
>
> File chưa điền thì hỏi người dùng ba thứ này trước, đừng đoán.

## Khi nào dùng skill này

- Lần đầu viết ra giọng thương hiệu thành văn bản
- Thuê freelancer hoặc nhân viên mới viết nội dung, cần đưa họ một tài liệu
- Content mỗi bài một giọng, đọc không ra cùng một thương hiệu
- **Chuẩn bị chạy `/ui-ux-pro-max` hoặc `/biz-nextjs-chatbot-openrouter`** — hai skill này cần giọng để không lấy mặc định
- Biến mô tả mơ hồ ("muốn chuyên nghiệp mà gần gũi") thành quy tắc viết được

**KHÔNG dùng** cho:

- Nhận diện hình ảnh — logo, màu, font. Đó là bộ nhận diện, không phải giọng.
- Định vị thương hiệu — chạy `/brand-positioning-builder` **trước**, vì giọng phải bám định vị.
- Lập kế hoạch nội dung — dùng `/content-plan-builder` và `/social-media-calendar`.
- Viết nội dung thật — dùng `/content-copywriter`, `/blog-post`, `/mkt-caption-writer`.
- Sửa nội dung cũ cho khớp giọng — dựng cẩm nang trước, sửa sau.

---

## Nguyên tắc cốt lõi

GIỌNG THƯƠNG HIỆU TIẾNG VIỆT ĐƯỢC QUYẾT ĐỊNH TRƯỚC HẾT BỞI XƯNG HÔ, KHÔNG PHẢI BỞI TÍNH TỪ. "CHUYÊN NGHIỆP, GẦN GŨI, ĐÁNG TIN" LÀ BA TỪ VÔ NGHĨA CHO TỚI KHI CHỐT ĐƯỢC THƯƠNG HIỆU XƯNG GÌ VÀ GỌI KHÁCH LÀ GÌ. CHỐT XƯNG HÔ TRƯỚC, MỌI THỨ KHÁC THEO SAU.

---

## Giai đoạn 0: Đọc vault trước khi hỏi

**Bắt buộc. Không được bỏ qua để nhảy thẳng vào phỏng vấn.**

Đọc các file dưới đây rồi mới hỏi phần còn thiếu. Hỏi lại thứ vault đã có là vi phạm mục 7 của `CLAUDE.md`.

| File | Lấy ra cái gì |
|---|---|
| `00. Business Context/Hồ Sơ Mô Hình Kinh Doanh.md` | 3 tham số ở callout đầu skill |
| `00. Business Context/Chân Dung Doanh Nghiệp.md` | Doanh nghiệp làm gì, khách lý tưởng là ai |
| `00. Business Context/Định Vị Thương Hiệu.md` | Lời hứa, điểm khác biệt — **giọng phải bám cái này** |
| `00. Business Context/MHKD/Phân Khúc Khách Hàng/PK*.md` | Khách nói kiểu gì, độ tuổi, mức hiểu biết → quyết định xưng hô |
| `00. Business Context/MHKD/Giá Trị Cốt Lõi/GT*.md` | Thông điệp lõi để lấy làm câu mẫu ở Giai đoạn 3 |
| `00. Business Context/Business Model Canvas — *.md` | Ô Channels → biết phải viết giọng cho kênh nào |
| `00. Business Context/Chân Dung CEO — *.md` | Nếu thương hiệu gắn với người sáng lập, giọng phải là giọng của họ |
| `Nhật Ký CEO/` | Câu chữ thật của CEO. **Chỉ đọc mục có `rieng_tu: no`**, ưu tiên `#quan-diem`, `#cau-chuyen` |
| `04. Resources/Feedback & Chứng Thực/Thư Viện Lời Khách.md` | **Cách khách tự mô tả vấn đề của họ** — nguồn từ vựng tốt nhất, vì đó là từ họ thật sự dùng |

**Sau khi đọc, chỉ hỏi những gì còn thiếu:**

1. **Ba đến bốn tính từ** — "Thương hiệu nên nghe như thế nào? Ví dụ: thẳng thắn, ấm áp, chắc chắn, vui vẻ, điềm đạm."
2. **Thương hiệu ngưỡng mộ** — "Có thương hiệu Việt nào anh/chị thấy viết hay không? Không cần cùng ngành."
3. **Thương hiệu không muốn giống** — "Có thương hiệu nào anh/chị thấy viết khó chịu? Vì sao?"
4. **Bài viết cũ** — "Có bài nào anh/chị thấy 'đúng chất mình nhất' không? Gửi link hoặc dán vào."

**CỔNG: Nếu `Định Vị Thương Hiệu.md` chưa có, báo người dùng và đề nghị chạy `/brand-positioning-builder` trước.** Dựng giọng trên nền định vị trống sẽ ra một bộ chữ nghe hay nhưng không gắn với ai. Nếu người dùng vẫn muốn làm ngay, làm — nhưng ghi rõ trong file là giọng này chưa neo vào định vị.

---

## Giai đoạn 1: Chốt xưng hô — quyết định số một

Đây là việc phải làm trước mọi việc khác. Đưa bảng này cho người dùng chọn:

| Cặp xưng hô | Thương hiệu xưng | Gọi khách | Cảm giác | Hợp với |
|---|---|---|---|---|
| **Bên mình ↔ anh/chị** | bên mình, chúng mình | anh/chị | Thân thiện có chừng mực, phổ biến nhất ở SME Việt | Dịch vụ, spa, giáo dục, tư vấn, B2B nhỏ |
| **Chúng tôi ↔ anh/chị** | chúng tôi | anh/chị, quý anh/chị | Chững chạc, giữ khoảng cách | B2B, tài chính, y tế, pháp lý, doanh nghiệp vừa |
| **Mình ↔ bạn** | mình | bạn | Ngang hàng, trẻ | Sản phẩm số, cộng đồng, khách dưới 30 |
| **Em ↔ anh/chị** | em | anh/chị | Khiêm nhường, bán hàng trực tiếp | Bán lẻ, livestream, môi giới — **cẩn thận: hạ vị thế thương hiệu nếu dùng trên website** |
| **Chúng tôi ↔ quý khách** | chúng tôi | quý khách | Trang trọng, xa cách | Khách sạn, sự kiện cao cấp — **dễ thành sáo rỗng** |
| **Tên riêng CEO ↔ anh/chị** | tên riêng ("Minh nghĩ là…") | anh/chị | Cá nhân, gắn với người thật | Thương hiệu cá nhân, coach, chuyên gia |

**Ba quy tắc bắt buộc khi chốt:**

1. **Một cặp duy nhất cho cả thương hiệu**, không đổi giữa các kênh. Được phép nới nhẹ (Zalo dùng "bên mình" thân hơn website dùng "chúng tôi") nhưng **không được đảo vế** — đã gọi khách là "anh/chị" thì đừng chỗ nào gọi "bạn".
2. **Nếu `nguoi-mua-la-nguoi-dung: khong`** — chốt xưng hô cho *người trả tiền*, rồi ghi riêng cách nói với *người dùng* ở mục 7 của file đầu ra.
3. **Xưng "em" trên website là hạ vị thế.** Được trong tin nhắn 1-1 của nhân viên tư vấn, không được trong copy trang bán hàng hay email hệ thống.

### Sáu thang đo giọng

Sau khi chốt xưng hô, cho người dùng chấm 1–5 trên sáu thang. Ghim 3–4 thang có điểm lệch xa giữa (1–2 hoặc 4–5); thang nào ở giữa thì bỏ, đừng ghim cả sáu.

```
Trang trọng (1) ←——→ Đời thường (5):
Nghiêm túc  (1) ←——→ Dí dỏm    (5):
Chuyên sâu  (1) ←——→ Dễ hiểu   (5):
Điềm đạm    (1) ←——→ Mạnh mẽ   (5):
Giữ khoảng cách (1) ←——→ Gần gũi (5):
Ngang hàng  (1) ←——→ Chuyên gia (5):
```

Nếu người dùng bí, đưa bảng nguyên mẫu ở cuối skill và hỏi: "Cái nào gần với thương hiệu của anh/chị nhất?"

---

## Giai đoạn 2: Định nghĩa giọng

### 2.1 — Bốn thuộc tính giọng

Chọn **đúng 3–4**, không hơn. Mỗi thuộc tính viết theo khuôn:

```
THUỘC TÍNH: Thẳng thắn
Nghĩa là gì: Nói thẳng vào việc, không vòng vo, không rào đón.
Cụ thể là: Câu ngắn. Đặt kết luận lên đầu. Nói số thật.
KHÔNG phải là: Cộc lốc hay phán xét. Thẳng thắn khác với lạnh lùng.
Câu ví dụ ĐÚNG: "Gói này không hợp với anh/chị. Lý do: quy mô còn nhỏ, chưa cần tới."
Câu ví dụ SAI: "Chúng tôi rất tiếc phải thông báo rằng có thể sản phẩm chưa hoàn toàn phù hợp."
```

Kiểm tra chéo: đọc cả bốn thuộc tính liền nhau — chúng có tạo thành **một tính cách người** không? Nếu có hai thuộc tính đá nhau (vừa "trang trọng" vừa "đời thường"), bỏ một.

### 2.2 — Mười quy tắc văn phong tiếng Việt

Đây là bảng thay cho bộ quy tắc tiếng Anh. **Cả mười dòng đều phải điền**, không bỏ dòng nào.

| # | Quy tắc | Cần chốt gì | Ví dụ |
|---|---|---|---|
| 1 | **Xưng hô** | Cặp đã chốt ở Giai đoạn 1 | "bên mình" ↔ "anh/chị" |
| 2 | **Độ dài câu** | Trung bình bao nhiêu chữ | Ngắn 8–14 chữ · Vừa 15–22 · Dài trên 22 |
| 3 | **Hán-Việt hay thuần Việt** | Nghiêng bên nào | "khởi động" (Hán-Việt) hay "bắt đầu" (thuần Việt) · "tối ưu" hay "làm gọn lại" |
| 4 | **Dấu chấm than** | Mỗi đoạn tối đa mấy cái | Khuyến nghị: tối đa 1 mỗi bài, 0 trên trang bán hàng |
| 5 | **Emoji** | Kênh nào được, mấy cái | Zalo/TikTok: 1–2 · Email: 0–1 · Website: 0 |
| 6 | **Viết tắt & teencode** | Có dùng "ko, dc, k, ạ" không | Khuyến nghị: không, kể cả trên Zalo — trừ "ạ" cuối câu nếu xưng "em" |
| 7 | **Tiếng Anh chen vào** | Bao nhiêu, có giải thích không | Ví dụ: tối đa 1 từ mỗi đoạn, lần đầu mở ngoặc giải thích |
| 8 | **Cách gọi tên mình** | Viết hoa thế nào, có thêm "Công ty" không | "Rocket Agent" — không viết "ROCKET AGENT", không "Cty Rocket Agent" |
| 9 | **Số tiền & số liệu** | Định dạng cố định | `1.000.000 đ` · `499.000đ` · không dùng USD · không "khoảng vài triệu" |
| 10 | **Mở & kết** | Câu chào và câu chốt mặc định | Mở: "Chào anh/chị," · Kết: "Anh/chị cần gì cứ nhắn bên mình." |

### 2.3 — Từ nên dùng và từ cấm (tiếng Việt)

**Từ nên dùng** phải lấy từ hai nguồn thật, không được bịa:

1. Từ trong `Thư Viện Lời Khách.md` — cách khách tự mô tả vấn đề của họ
2. Từ trong `MHKD/Giá Trị Cốt Lõi/GT*.md` — cách thương hiệu mô tả giá trị

**Từ cấm** phân theo bốn nhóm. Điền tối thiểu 3 từ mỗi nhóm, lấy từ chính ngành của khách:

| Nhóm | Ví dụ từ cấm | Vì sao cấm |
|---|---|---|
| **Sáo rỗng** | "giải pháp toàn diện", "uy tín hàng đầu", "chuyên nghiệp tận tâm", "chất lượng vượt trội", "đội ngũ giàu kinh nghiệm", "đáp ứng mọi nhu cầu", "khẳng định vị thế", "đẳng cấp" | Ai cũng nói được, nên không nói lên điều gì. Thay bằng số hoặc bằng chứng cụ thể. |
| **Dịch máy** | "tận dụng", "tối ưu hoá trải nghiệm", "hệ sinh thái", "cách mạng hoá", "nâng tầm", "đột phá", "kiến tạo" | Đọc ra là biết dịch từ tiếng Anh. Người Việt nói chuyện không dùng những từ này. |
| **Hứa quá** | "cam kết 100%", "hiệu quả tức thì", "chắc chắn thành công", "duy nhất tại Việt Nam", "không cần nỗ lực" | Mất niềm tin, và có rủi ro pháp lý về quảng cáo sai sự thật. |
| **Bán hàng rẻ tiền** | "SIÊU HOT", "GIÁ SỐC", "CHỐT ĐƠN NGAY KẺO LỠ", "inbox e ngay ạ", "số lượng có hạn" (khi không có hạn thật) | Kéo tụt thương hiệu xuống mức bán hàng chợ. |

### 2.4 — Bảng "Chúng tôi LÀ / KHÔNG PHẢI"

Tối thiểu 5 dòng. Mỗi dòng là một cặp gần giống nhau nhưng khác hẳn về chất — đây là chỗ chặn Claude và người viết đi quá đà.

| Chúng tôi LÀ | Chúng tôi KHÔNG PHẢI |
|---|---|
| Tự tin | Kiêu ngạo |
| Thẳng thắn | Cộc lốc |
| Gần gũi | Xuề xoà |
| Hiểu nghề | Lên lớp |
| Nhiệt tình | Đeo bám |

---

## Giai đoạn 3: Chứng minh — viết giọng ra thành câu thật

**Đây là phần quan trọng nhất của cẩm nang.** Quy tắc trừu tượng không dùng được; câu mẫu thì dùng được ngay.

Lấy **một thông điệp lõi** từ `GT*.md` rồi viết lại thông điệp đó cho **bảy tình huống**. Mỗi mẫu 2–6 câu, kèm chú thích ngắn cho biết thuộc tính nào đang chi phối.

| # | Tình huống | Yêu cầu riêng |
|---|---|---|
| 1 | **Bài đăng Facebook** | Ba dòng đầu phải giữ chân trước khi bị "xem thêm" cắt |
| 2 | **Caption TikTok + lời thoại 5 giây đầu** | Nói được thành lời, không phải văn viết |
| 3 | **Tin nhắn Zalo mở lời** sau khi khách để lại số | Một tin, một câu hỏi, dễ trả lời |
| 4 | **Trả lời inbox khi khách hỏi giá** | Không né giá, không ép chốt |
| 5 | **Tiêu đề email + dòng preview** | Không dùng chữ hoa toàn bộ, không "GẤP" |
| 6 | **Tiêu đề chính + phụ của trang bán hàng** | Đây là mẫu mà `/ui-ux-pro-max` sẽ đọc |
| 7 | **Chatbot trả lời câu hỏi thường gặp** | Đây là mẫu mà `/biz-nextjs-chatbot-openrouter` sẽ đọc. Phải có cả **câu chatbot nói khi không biết câu trả lời** |

Thêm mẫu thứ 8 khi thương hiệu có xử lý khiếu nại: **trả lời một khách đang bực**. Đây là chỗ giọng dễ vỡ nhất.

### 3b — Giọng hai lớp (chỉ khi `nguoi-mua-la-nguoi-dung: khong`)

Khi người trả tiền và người dùng là hai người, viết thêm một bảng:

| | Người trả tiền | Người dùng hằng ngày |
|---|---|---|
| Họ quan tâm | Kết quả, chi phí, rủi ro | Việc của họ có nhẹ đi không, có bị thay thế không |
| Từ nên dùng | ... | ... |
| Từ tuyệt đối tránh | ... | Từ gợi ý cắt giảm nhân sự |
| Một câu mẫu | ... | ... |

**Câu nối** — người dùng nói câu gì thì người trả tiền quyết mua, và ngược lại. Đây là phần `/customer-persona` cũng dựng; hai file phải khớp nhau.

---

## Giai đoạn 4: Ghi file — cấu trúc CỐ ĐỊNH

Ghi vào **đúng một chỗ**, không hỏi người dùng chọn nơi khác:

```
00. Business Context/Brand Voice — Giọng Thương Hiệu.md
```

Frontmatter:

```yaml
---
tags: [identity, brand-voice]
created: YYYY-MM-DD
---
```

**Heading phải đúng thứ tự và đúng chữ dưới đây** — skill khác grep theo heading này:

```markdown
# Brand Voice — Giọng Thương Hiệu [Tên thương hiệu]

## 0. Tra nhanh 30 giây
[Bảng gọn: xưng hô · 4 thuộc tính · 3 từ nên dùng nhất · 3 từ cấm nặng nhất · độ dài câu.
 Đây là khối duy nhất mà skill viết nội dung cần đọc khi làm việc nhanh.]

## 1. Bốn thuộc tính giọng
## 2. Xưng hô
## 3. Chúng tôi LÀ / KHÔNG PHẢI
## 4. Từ nên dùng & từ cấm
## 5. Mười quy tắc văn phong
## 6. Giọng theo từng kênh
## 7. Giọng cho hai lớp khách        ← bỏ mục này nếu nguoi-mua-la-nguoi-dung = co
## 8. Giọng mẫu — 7 tình huống
## 9. Checklist 10 câu trước khi đăng
## 10. Nguồn & mức tin cậy

## 🔗 Kết nối với
- [[Chân Dung Doanh Nghiệp]]
- [[Định Vị Thương Hiệu]]
- [[Hồ Sơ Mô Hình Kinh Doanh]]
```

**Mục 10 bắt buộc tách ba loại** theo nguyên tắc 3 mục 5 của `CLAUDE.md`:

| Loại | Đánh dấu |
|---|---|
| Người dùng nói ra trực tiếp | ✅ đã xác nhận |
| Claude suy ra từ file trong vault | 🔵 suy luận từ `[tên file]` |
| Claude tự đề xuất, chưa ai duyệt | ⚠️ đề xuất, cần chốt |

Ghi xong, báo lại **đường dẫn đầy đủ** và nhắc người dùng: các skill nội dung sẽ tự đọc file này từ giờ.

---

## Bảng nguyên mẫu giọng — dùng khi người dùng bí

| Nguyên mẫu | Chất lõi | Nghe như | Thương hiệu Việt gần với nó | Hợp với |
|---|---|---|---|---|
| **Người thầy** | Chuyên môn + rõ ràng | Chắc chắn, có số, giải thích được | Các trang tư vấn tài chính, phòng khám uy tín | B2B, tư vấn, y tế, giáo dục |
| **Người bạn** | Ấm áp + dễ gần | Trò chuyện, đồng cảm, không lên lớp | Thương hiệu mỹ phẩm và F&B nội địa trẻ | Bán lẻ, spa, F&B, cộng đồng |
| **Người dẫn đường** | Thúc đẩy + có lộ trình | Khích lệ, hướng hành động, chia bước | Coach và trung tâm đào tạo kỹ năng | Khoá học, coaching, thể hình |
| **Người phá cách** | Thẳng + dám nói ngược | Ngắn, sắc, dám chê cái sai của ngành | Thương hiệu thách thức trong ngành cũ | Thương hiệu mới cần gây chú ý |
| **Người kỹ tính** | Gu + chọn lọc | Điềm đạm, ít lời, chú trọng chi tiết | Thương hiệu thủ công, nội thất cao cấp | Sản phẩm cao cấp, thiết kế |

Phần lớn thương hiệu là **pha của hai nguyên mẫu**. Chốt một cái chính, một cái phụ.

---

## Ví dụ 1 — Chuỗi spa (B2C, bán trực tiếp)

**Đầu vào:** 3 cơ sở tại TP.HCM, 28 nhân sự · khách nữ 28–45, thu nhập khá · tính từ: ấm áp, chắc tay, không màu mè · không muốn giống: "các spa hay hô GIÁ SỐC" · kênh: Facebook, Zalo, TikTok, website.

**Xưng hô chốt:** bên mình ↔ anh/chị *(không dùng "em" vì muốn giữ vị thế chuyên môn)*

**Bốn thuộc tính:**

```
THUỘC TÍNH: Chắc tay
Nghĩa là gì: Nói bằng chuyên môn, không nói bằng cảm tính.
Cụ thể là: Nêu quy trình, nêu thời gian, nêu điều kiện da phù hợp.
KHÔNG phải là: Khoe thuật ngữ y khoa để doạ khách.
ĐÚNG: "Da anh/chị đang mỏng, liệu trình này cần giãn thành 6 buổi thay vì 4."
SAI:  "Liệu trình công nghệ cao đột phá, hiệu quả tức thì sau 1 lần!"
```

*(Ba thuộc tính còn lại: Ấm áp · Thành thật · Điềm đạm)*

**Từ nên dùng:** da anh/chị, liệu trình, giãn buổi, hợp da, thấy rõ sau…, bên mình kiểm tra trước
**Từ cấm:** GIÁ SỐC · hiệu quả tức thì · trắng bật tông · cam kết 100% · đẳng cấp · công nghệ đột phá

**Chúng tôi LÀ / KHÔNG PHẢI:** Chắc tay ↔ Doạ khách · Ấm áp ↔ Nịnh · Thành thật ↔ Bi quan · Điềm đạm ↔ Lạnh nhạt · Chuyên môn ↔ Lên lớp

**Mẫu — trả lời inbox khi khách hỏi giá:**

> Dạ chào chị, liệu trình này bên mình 4 buổi, 6.800.000 đ.
> Trước khi chốt, bên mình muốn xem tình trạng da của chị đã — có trường hợp da mỏng thì phải giãn thành 6 buổi, chi phí khác đi. Chị gửi giúp bên mình 2 ảnh chụp dưới ánh sáng tự nhiên nhé.
>
> *[Thành thật: nói giá ngay, không né. Chắc tay: nêu điều kiện chuyên môn. Ấm áp: "nhé" cuối câu. Không có emoji, không có "ạ" vì xưng "bên mình" chứ không xưng "em".]*

**Mẫu — chatbot khi không biết câu trả lời:**

> Câu này bên mình chưa có sẵn thông tin chính xác, để bên mình hỏi lại kỹ thuật viên rồi trả lời anh/chị trong hôm nay nhé. Anh/chị để lại số điện thoại giúp bên mình được không ạ?
>
> *[Thành thật: không bịa. Chắc tay: hẹn thời hạn cụ thể. Chuyển sang người thật thay vì đoán.]*

---

## Ví dụ 2 — Công ty giải pháp AI cho SME (B2B, chu kỳ bán dài, người mua ≠ người dùng)

**Đầu vào:** bán AI Agent và tự động hoá cho doanh nghiệp 10–50 nhân sự · `chu-ky-ban-ngay: 45` · `nguoi-mua-la-nguoi-dung: khong` · tính từ: thẳng thắn, hiểu nghề, không hù doạ · không muốn giống: "mấy bên bán chatbot hô AI thay thế con người" · kênh: Facebook cá nhân founder, LinkedIn, hội thảo, email, landing page.

**Xưng hô chốt:** bên mình ↔ anh/chị *(B2B nhỏ, chủ doanh nghiệp là người quyết — "chúng tôi" quá xa, "mình/bạn" quá suồng)*

**Bốn thuộc tính:** Thẳng thắn · Hiểu nghề · Không hù doạ · Có bằng chứng
*(Vì `chu-ky-ban-ngay: 45` ≥ 30 nên giọng nghiêng về bằng chứng và chuyên môn — đúng như callout đầu skill.)*

```
THUỘC TÍNH: Không hù doạ
Nghĩa là gì: Không bán bằng nỗi sợ tụt hậu.
Cụ thể là: Nói agent làm được gì và KHÔNG làm được gì, ngay trong lần đầu.
KHÔNG phải là: Hạ thấp giá trị của AI. Nói đúng khả năng, không nói thấp đi.
ĐÚNG: "Agent xử lý trọn khoảng 60–80% câu lặp. Phần khó vẫn cần người."
SAI:  "Doanh nghiệp không dùng AI năm nay sẽ bị đối thủ bỏ lại phía sau."
```

**Từ cấm riêng của ngành này:** thay thế hoàn toàn con người · chuyển đổi số toàn diện · cách mạng 4.0 · không dùng AI là tụt hậu · giải pháp all-in-one · hệ sinh thái số

**Giọng hai lớp** *(vì `nguoi-mua-la-nguoi-dung: khong`)*:

| | Chủ doanh nghiệp (trả tiền) | Nhân viên sale/CSKH (dùng hằng ngày) |
|---|---|---|
| Quan tâm | Mất bao nhiêu lead, tốn bao nhiêu, bao lâu thấy kết quả | Có bị thay thế không, việc có nặng thêm không |
| Từ nên dùng | lead rơi, chi phí một nhân sự, sau 2 tuần thấy số | agent nhận ca đêm, anh/chị nhận khách nóng, đỡ phải gõ lại |
| Từ tuyệt đối tránh | cách mạng, chuyển đổi số toàn diện | **thay thế, cắt giảm, tự động hoá nhân sự** |
| Câu mẫu | "Trả lời chậm 8 tiếng thì khách đã đặt bên khác. Bên mình đo trước 2 tuần rồi mới bật." | "Việc gõ lại bảng giá lần thứ 200 để agent làm. Anh/chị giữ phần chốt khách khó." |

**Câu nối:** nếu nhân viên nói "cái này đỡ việc thật" thì chủ chốt tiếp; nếu nhân viên nói "khách phàn nàn" thì chủ dừng. **Mọi câu chữ hướng tới nhân viên đều phải nói về việc nhẹ đi, không bao giờ nói về việc cắt giảm.**

**Mẫu — tiêu đề trang bán hàng** *(mẫu mà `/ui-ux-pro-max` sẽ đọc)*:

> **Khách nhắn lúc 10 giờ đêm. Sáng mai trả lời thì họ đã mua chỗ khác.**
> Bên mình dựng nhân sự số trực Zalo, Facebook và TikTok Shop 24/7, trả lời trong 30 giây — chi phí bằng khoảng một phần ba lương một bạn chăm sóc khách hàng.
>
> *[Thẳng thắn: mở bằng đúng cảnh khách đang gặp. Có bằng chứng: "một phần ba lương" là mốc so sánh đo được. Không hù doạ: không có chữ "tụt hậu" nào. Hiểu nghề: gọi đúng ba kênh mà SME Việt thật sự dùng.]*

---

## Cổng kiểm tra trước khi giao

**Không bỏ dòng nào.** Thiếu một dòng là cẩm nang không dùng được cho skill hạ nguồn.

```
[ ] Đã đọc 00. Business Context/ trước khi hỏi người dùng
[ ] Xưng hô đã chốt, một cặp duy nhất, ghi ở mục 2
[ ] 3–4 thuộc tính, mỗi cái có "nghĩa là gì / KHÔNG phải là / câu ĐÚNG / câu SAI"
[ ] Không có hai thuộc tính đá nhau
[ ] Đủ 10 quy tắc văn phong, không dòng nào bỏ trống
[ ] Từ nên dùng lấy từ Thư Viện Lời Khách hoặc GT*.md — không bịa
[ ] Từ cấm đủ 4 nhóm, mỗi nhóm ≥ 3 từ, có từ riêng của ngành khách
[ ] Bảng LÀ / KHÔNG PHẢI ≥ 5 dòng
[ ] Đủ 7 mẫu câu, mỗi mẫu có chú thích thuộc tính
[ ] Có mẫu chatbot nói khi không biết câu trả lời
[ ] Nếu nguoi-mua-la-nguoi-dung = khong: có mục 7 giọng hai lớp
[ ] Mục 10 tách rõ ✅ xác nhận / 🔵 suy luận / ⚠️ đề xuất
[ ] Heading đúng thứ tự cố định ở Giai đoạn 4
[ ] Ghi đúng 00. Business Context/Brand Voice — Giọng Thương Hiệu.md
[ ] Đã link tới Chân Dung Doanh Nghiệp và Định Vị Thương Hiệu
```

---

## Xử lý tình huống khó

### Người dùng không mô tả nổi giọng của mình

1. Đưa bảng sáu thang đo, cho chấm 1–5
2. Hỏi 2–3 thương hiệu họ thích, rồi mô tả ngược ra thuộc tính
3. Đọc `Nhật Ký CEO/` — giọng thật của người sáng lập thường đã nằm sẵn ở đó
4. Vẫn bí thì đưa bảng nguyên mẫu và hỏi "cái nào gần nhất"
5. **Luôn đưa một bản nháp để họ sửa, đừng đưa trang trắng**

### Nội dung cũ ngược hẳn với giọng muốn có

1. Nói thẳng khoảng cách: "Nội dung hiện tại đang trang trọng và nhiều từ Hán-Việt. Giọng anh/chị muốn thì đời thường hơn nhiều. Cẩm nang này sẽ nhắm tới chỗ muốn đến, không phải chỗ đang đứng."
2. Thêm mục **Trước / Sau** với 3 đoạn viết lại từ chính nội dung cũ của họ
3. Chỉ ra 3 chỗ nên sửa trước: trang chủ, trang giới thiệu, bài đăng nhiều tương tác nhất

### Nhiều dòng sản phẩm cần giọng khác nhau

Vault này chỉ cho **một doanh nghiệp** (mục 1 `CLAUDE.md`). Nên **mặc định là một giọng duy nhất**, các dòng sản phẩm chỉ khác ở mức nhấn, ghi vào mục 6.

Chỉ tách file riêng khi người dùng khẳng định đây là **hai thương hiệu tách bạch có tên riêng**. Khi đó đặt tên `Brand Voice — Giọng Thương Hiệu ([Tên]).md` và ghi rõ ở đầu mỗi file rằng nó không phải giọng mặc định.

### Giọng muốn có không hợp với khách

Ví dụ: bán dịch vụ kế toán nhưng muốn giọng phá cách.

1. **Không từ chối.** Nêu căng thẳng: "Giọng phá cách trong ngành kế toán rất hiếm. Nó có thể thành điểm khác biệt lớn, cũng có thể làm khách thận trọng thấy thiếu tin cậy."
2. Hỏi: "Khách của anh/chị thuộc nhóm thích đọc thứ mới lạ, hay nhóm truyền thống?"
3. Nếu vẫn giữ hướng đó, làm theo — nhưng thêm mục **Ranh giới**: giọng phá cách dừng ở đâu (ví dụ: không bao giờ đùa về tiền bạc hay rủi ro pháp lý của khách).
4. Nếu họ cân nhắc lại, đề xuất đường giữa: "thẳng thắn và dễ hiểu" đạt được phần lớn năng lượng của giọng phá cách mà không mang rủi ro.

### Ba lần sửa vẫn không đúng

1. Dừng sinh, đổi cách: "Anh/chị viết giúp em 2–3 câu theo đúng kiểu anh/chị muốn thương hiệu nói. Viết đại thôi, không cần chỉn chu."
2. Lấy chính câu họ viết làm chuẩn — bám nhịp, bám từ, bám năng lượng
3. Trình bày lại: "Dựa trên cách anh/chị viết tự nhiên, đây là những gì em thấy…"

---

## Những lỗi không được phạm

- **KHÔNG** hỏi lại thứ đã có trong `00. Business Context/`. Đọc trước, hỏi phần thiếu.
- **KHÔNG** để danh sách từ nên dùng / từ cấm bằng tiếng Anh. Cẩm nang giọng tiếng Việt phải có từ tiếng Việt.
- **KHÔNG** đưa quy tắc không tồn tại trong tiếng Việt (viết tắt kiểu "we're", dấu phẩy Oxford). Dùng đúng 10 quy tắc ở mục 2.2.
- **KHÔNG** dựng giọng mà chưa chốt xưng hô. Đó là quyết định đầu tiên, không phải chi tiết phụ.
- **KHÔNG** quá 4 thuộc tính. Năm thuộc tính nghĩa là không ai nhớ cái nào.
- **KHÔNG** viết thuộc tính đá nhau — "trang trọng" và "đời thường" không thể cùng là thuộc tính chính.
- **KHÔNG** bỏ phần câu mẫu. Bảy mẫu câu **chính là** cẩm nang; phần còn lại chỉ là giàn giáo.
- **KHÔNG** đưa nhiều phương án giọng rồi bắt người dùng chọn. Chọn một cái tốt nhất dựa trên đầu vào, rồi tinh chỉnh.
- **KHÔNG** viết cẩm nang dài quá 3 trang. Không ai đọc thì coi như không tồn tại.
- **KHÔNG** bịa từ vựng của khách. Từ nên dùng phải lấy từ `Thư Viện Lời Khách.md` hoặc `GT*.md`.
- **KHÔNG** đổi heading của file đầu ra. Skill khác grep theo heading đó.
- **KHÔNG** ghi file ra chỗ khác ngoài `00. Business Context/Brand Voice — Giọng Thương Hiệu.md`.

---

## Ghi kết quả vào đâu

> [!important] Không ghi vào vault thì coi như chưa làm
> Kết quả chỉ hiện trong khung chat sẽ mất khi đóng phiên. Hệ thống chỉ thông minh bằng đúng dữ liệu được ghi lại.

| | |
|---|---|
| **Thư mục** | `00. Business Context/` |
| **Tên file** | `Brand Voice — Giọng Thương Hiệu.md` |
| **Bắt buộc link tới** | `Chân Dung Doanh Nghiệp` · `Định Vị Thương Hiệu` · `Hồ Sơ Mô Hình Kinh Doanh` |
| **Heading** | Cố định theo Giai đoạn 4 — skill khác đọc theo heading |

Sau khi ghi xong, báo lại **đường dẫn đầy đủ** và nói rõ với người dùng: từ giờ mọi skill viết nội dung sẽ đọc file này, nên sửa giọng thì sửa ở đây, đừng sửa từng bài.

**Việc nên gợi ý tiếp theo:** chạy `/kiem-tra-cong 02` để chấm cổng Business Context, hoặc chạy `/content-pillar-builder` để biến giọng vừa chốt thành hệ thống trụ cột nội dung.
