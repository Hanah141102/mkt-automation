---
updated: 2026-07-29
status: canonical
tags: [demo-ai, tracking, attribution, utm, measurement]
---
> [!warning] ĐÂY LÀ BÀI MẪU — DỮ LIỆU HƯ CẤU
> Toàn bộ tên công ty, tên người, tên miền, số tiền và số liệu trong tài liệu này **đã được thay bằng dữ liệu ví dụ**. Không dùng các con số ở đây làm căn cứ kinh doanh. Giá trị của bộ tài liệu này nằm ở **cấu trúc và cách lập luận**, không nằm ở số liệu.


# 29 — Tracking & Measurement Spec: dựng trong 7 ngày, không cần CRM

> Doc 16 mục 10 xếp tracking là **ưu tiên #1**. Doc 09 có luật cứng: **không bật ads trước khi tracking chạy**. Doc 04 ghi nguyên văn kênh hiện tại *"không đo gì cả"*. Tài liệu này là bản spec để đội dựng xong trong 7 ngày với đúng thứ đang có — **LadiPage, Zoom, Meta Ads, cổng thanh toán, Google Sheet.** Không mua thêm phần mềm nào.

---

## 0. Nguyên tắc gốc

| # | Nguyên tắc | Vì sao |
|:--:|---|---|
| 1 | **Một khách = một số điện thoại.** Số điện thoại là khóa nối mọi hệ | Không có CRM thì phải có một khóa chung, nếu không mọi bảng đều rời rạc |
| 2 | **Đo được đến `won`, không dừng ở CPL** | Doc 08 mục 7: *"Không dùng CPL đẹp để kết luận phễu tốt"* |
| 3 | **Tách hoàn toàn hai nhánh** `CEO-AIOS` và `DIGITAL-BUILDER` | Luật 7 của doc 10. Gộp báo cáo là mù cả hai |
| 4 | **Thà thiếu số còn hơn số sai.** Ô trống ghi rõ lý do trống | Nguyên tắc vàng của cả bộ hồ sơ |
| 5 | **Không ai được sửa số quá khứ.** Sửa thì ghi dòng mới có ngày | Chống tranh chấp số liệu — doc 24 mục 5.4 |

---

## 1. Kiến trúc tối thiểu — bốn khối

```
   META ADS  ─────┐
   FB/GROUP  ─────┼──▶  LANDING (LadiPage)  ──▶  GOOGLE SHEET "LEAD_MASTER"
   TIKTOK    ─────┘            │                        ▲   ▲   ▲
                               │                        │   │   │
                               ▼                        │   │   │
                          ZOOM ĐĂNG KÝ ──── export ─────┘   │   │
                                                            │   │
                          ZOOM ATTENDEE ─── export ─────────┘   │
                                                                │
                          CỔNG THANH TOÁN ── export ────────────┘
```

**Khối 1 — Nguồn:** Meta Ads, FB cá nhân An, group Cơm AI Lo, TikTok.
**Khối 2 — Điểm bắt:** một landing LadiPage duy nhất, ghi lại UTM.
**Khối 3 — Kho:** một Google Sheet `AFW_LEAD_MASTER` — **đây là nguồn sự thật duy nhất.**
**Khối 4 — Bảng đọc:** 4 tab dashboard tự tính bằng công thức, không ai gõ tay.

> **Vì sao Google Sheet chứ không phải CRM:** còn 2 tuần. Dựng CRM trong 2 tuần rồi vận hành sai còn tệ hơn Sheet chạy đúng. CRM là việc của Đợt 3 ([[28-ra-soat-khoang-trong-va-lo-trinh-hoan-thien]] mục 4), sau khi đã biết mình cần đo gì thật.

---

## 2. Quy ước UTM — bắt buộc, không ngoại lệ

### 2.1 Cấu trúc

```
?utm_source={nguồn}&utm_medium={loại}&utm_campaign={chiến dịch}&utm_content={creative}&utm_term={hook}
```

### 2.2 Từ điển giá trị — chỉ được dùng giá trị trong bảng

| Tham số | Giá trị hợp lệ | Ghi chú |
|---|---|---|
| `utm_source` | `meta` · `fb-thang` · `group-comailo` · `tiktok` · `youtube` · `zalo` · `direct` | Viết thường, không dấu, nối bằng gạch ngang |
| `utm_medium` | `paid` · `organic` · `story` · `dm` · `bio` | Phân biệt trả tiền và không trả tiền. **Đây là cột quan trọng nhất** |
| `utm_campaign` | `afw-c1` (chuỗi 1) · `afw-c2` · `afw-c3`… | Đổi số chuỗi, giữ nguyên tiền tố. Không gắn năm |
| `utm_content` | `cr01` → `cr08` (8 paid creative master, doc 23 mục 5.2) · `org-{ngày}` cho organic | Mã hóa để so sánh được giữa các chuỗi |
| `utm_term` | `hook-noidau` · `hook-sosanh` · `hook-demo` · `hook-case` · `hook-soc` | Theo 5 khuôn hook. Cho phép so hook độc lập với creative |

### 2.3 Ví dụ đầy đủ

```
https://landing.demo-ai/afw?utm_source=meta&utm_medium=paid&utm_campaign=afw-c1&utm_content=cr03&utm_term=hook-demo
https://landing.demo-ai/afw?utm_source=fb-thang&utm_medium=organic&utm_campaign=afw-c1&utm_content=org-0805&utm_term=hook-noidau
```

### 2.4 Luật cứng

1. **Không có UTM thì không được đăng.** Link trần vào `direct` và mất dấu vĩnh viễn.
2. **Một creative = một `utm_content`.** Đổi ảnh, đổi video, đổi caption chính → đổi mã.
3. **Nguyệt giữ file `UTM_REGISTRY`** — bảng ánh xạ mã → mô tả + ảnh chụp creative. Không có file này thì 3 tuần sau không ai nhớ `cr05` là cái gì.
4. **Không dùng dấu tiếng Việt, không dùng khoảng trắng, không viết hoa** trong bất kỳ giá trị UTM nào.

---

## 3. Landing phải bắt được gì

### 3.0 Cấu trúc landing 3 tầng vé *(BOD chốt lượt 2)*

BOD đã chốt: **3 tầng 0đ / 280k / 700k hiện ngay trên landing, và bán thêm trong buổi 1.**

Đây là quyết định đúng về mặt kinh tế ([[34-mo-hinh-so-chuoi-1-va-ky-luat-ngan-sach]] mục 1) nhưng có một rủi ro vận hành phải chặn: **3 tầng hiện lên cùng lúc làm tăng ma sát → CPL tăng 20–40%.** Cách bố trí để giữ được tiền vé mà không giết CPL:

| Bố trí | Cách làm |
|---|---|
| **Nút chính, to nhất, màu thương hiệu** | **"Đăng ký miễn phí"** — một cú bấm, mở form |
| Ngay dưới, nhỏ hơn | Bảng so sánh 3 tầng: cái gì có ở tầng nào |
| **Sau khi submit form free** | **Trang order bump**: *"Chỉ hôm nay — nâng lên VIP 280k để nhận bản ghi trọn đời + workbook + bộ template"*. Đây là nơi thu phần lớn tiền vé |
| Buổi 1, phút 5–8 | Chào vé VIP lần hai cho người vào bằng tầng free |

> **Nguyên tắc: đăng ký phải luôn là một cú bấm. Vé là lời mời sau đó, không phải rào chắn trước đó.** Bảng 3 tầng vẫn hiện trên landing để tạo neo giá và cảm giác có lựa chọn — nhưng đường đi mặc định luôn là free trước, nâng cấp sau.

**`[PHẢI ĐO] ngay ngày đầu:** tỷ lệ mua vé. Nếu dưới 5% sau 200 đăng ký đầu tiên thì vấn đề ở trang order bump, không ở ads — sửa được trong 24h.

### 3.1 Trường bắt buộc trên form LadiPage

| Trường | Loại | Bắt buộc | Ghi chú |
|---|---|:--:|---|
| Họ tên | text | ✅ | |
| **Số điện thoại** | tel | ✅ | **Khóa nối toàn hệ.** Validate 10 số, bỏ khoảng trắng |
| Email | email | ✅ | **Kênh nhắc chính thứ hai** — BOD đã chốt bổ sung email marketing |
| **Anh/chị đang là?** | select | ✅ | 3 lựa chọn — xem 3.2. **Đây là trường phân luồng, không được bỏ** |
| Quy mô nhân sự | select | ⬜ | `1 mình` · `2–9` · `10–49` · `50+`. Dùng chấm điểm lead |
| 5 trường ẩn UTM | hidden | ✅ | source/medium/campaign/content/term |
| `ts_dangky` | hidden | ✅ | Dấu thời gian tự động |

**Trên trang thanh toán vé, thêm:**

| Trường | Bắt buộc | Ghi chú |
|---|:--:|---|
| **Cần hóa đơn VAT?** (Có/Không) | ✅ | **BOD chốt: xuất VAT đầy đủ.** Nếu Có → hiện 3 trường bên dưới |
| MST · Tên công ty · Địa chỉ | Có điều kiện | Thu lúc thanh toán rẻ hơn nhiều so với đi xin lại sau |

### 3.2 Trường phân luồng — thiết kế lại cho đúng hai nhánh

> Câu hỏi: **"Anh/chị đăng ký với vai trò nào?"**

| Lựa chọn hiển thị | Gán tag |
|---|---|
| Tôi đang điều hành một doanh nghiệp / đội nhóm | `CEO-AIOS` |
| Tôi là chuyên gia / coach / freelancer muốn đóng gói sản phẩm số | `DIGITAL-BUILDER` |
| Tôi đang tìm hiểu, chưa xác định | `CHUA-PHAN-LOAI` |

**Vì sao chỉ 3 lựa chọn:** doc 08 mục 8.1 — mỗi CTA phục vụ một nhánh. Nhưng chuỗi 1 dùng **một landing chung** (quyết định của doc 23), nên phân luồng phải xảy ra ngay tại form. Nhóm `CHUA-PHAN-LOAI` được hỏi lại ở form #2 trong buổi 2.

**Cấm:** thêm trường thứ 8. Mỗi trường thêm vào làm rơi 3–7% tỷ lệ điền form. Với vé miễn phí, form dài là cách nhanh nhất giết CPL.

### 3.3 Trang cảm ơn

Sau khi submit → **chuyển thẳng sang trang cảm ơn có 3 việc, theo thứ tự**:

1. Nút **"Vào nhóm Zalo của chuỗi"** — to nhất, trên cùng. Đây là kênh nhắc lịch duy nhất đang có (xem [[30-show-up-engine-khong-co-zalo-oa]]).
2. Nút **"Thêm lịch vào Google Calendar"** — link `.ics` 5 buổi.
3. Câu **"Kiểm tra tin nhắn — chúng tôi vừa gửi link phòng học"**.

Trang cảm ơn phải fire event `CompleteRegistration` cho Pixel.

---

## 4. Sự kiện phải bắn — từ điển event

| # | Tên event | Bắn ở đâu | Pixel Meta | Ghi vào Sheet | Dùng để |
|:--:|---|---|:--:|:--:|---|
| 1 | `PageView` | Landing | ✅ | ⬜ | Tính tỷ lệ điền form |
| 2 | `Lead` / `CompleteRegistration` | Trang cảm ơn | ✅ | ✅ | **CPL** — chỉ số ads chính |
| 3 | **`TicketPurchase`** | Thanh toán vé 280k/700k | ✅ (có `value`) | ✅ | **TỶ LỆ MUA VÉ — biến biết được sớm nhất và đắt thứ ba ([[34-mo-hinh-so-chuoi-1-va-ky-luat-ngan-sach]] mục 9)** |
| 4 | `JoinZaloGroup` | Click nút nhóm cộng đồng | ✅ (custom) | ✅ | Đo tỷ lệ vào nhóm — dự báo show rate |
| 5 | `Attend_D1` … `Attend_D5` | Export Zoom sau mỗi buổi | ⬜ | ✅ | **Show rate từng buổi, tách theo tầng vé** |
| 6 | `Purchase` | Cổng thanh toán khóa | ✅ (có `value`) | ✅ | Doanh thu + ROAS |
| 7 | `Upgrade` | Thanh toán phần chênh | ✅ (có `value`) | ✅ | **Tỷ lệ nâng cấp — chỉ số số một của doc 17 B5** |
| 8 | `FormInsight` | Submit form insight buổi 2 và 4 | ✅ (custom) | ✅ | Lọc tệp kim cương |

**Năm event bắt buộc tối thiểu nếu không kịp làm hết:** `Lead` · **`TicketPurchase`** · `Attend_D1` · `Purchase` · `Upgrade`. Thiếu bất kỳ cái nào là không đọc được chuỗi 1.

> `TicketPurchase` là event mới sau quyết định vé 3 tầng, và là event **phải chạy đúng ngay ngày đầu**. Nó vừa là doanh thu, vừa là tín hiệu dự báo show rate và tỷ lệ chốt của cả chuỗi.

---

## 5. Cấu trúc Google Sheet `AFW_LEAD_MASTER`

### Tab 1 — `LEAD` *(một dòng = một người)*

| Cột | Tên | Nguồn | Ai điền |
|:--:|---|---|---|
| A | `sdt` | Form | Tự động |
| B | `ho_ten` | Form | Tự động |
| C | `email` | Form | Tự động |
| D | `tag_nhanh` | Form (CEO-AIOS / DIGITAL-BUILDER / CHUA-PHAN-LOAI) | Tự động |
| E | `quy_mo` | Form | Tự động |
| F–J | `utm_source` … `utm_term` | Form hidden | Tự động |
| K | `ts_dangky` | Form | Tự động |
| **K2** | **`tang_ve`** — `FREE` / `VIP` / `VVIP` | Cổng thanh toán vé | **Bảo** |
| **K3** | **`ts_mua_ve`** + `mua_ve_o_dau` (`landing` / `buoi1`) | Cổng thanh toán vé | **Bảo** |
| L | `vao_nhom_zalo` | Đối chiếu tay sau D−1 | Chi |
| M–Q | `du_d1` … `du_d5` | Export Zoom mỗi tối | Hà |
| R | `so_buoi_du` | Công thức `=COUNTIF(M:Q,"x")` | Tự động |
| S | `mua_ngay` | Export thanh toán | Bảo |
| T | `goi_mua` | `5tr / 9tr / 11tr / 12tr / 19tr` | Bảo |
| U | `da_nang_cap` | `x` nếu có trả phần chênh | Bảo |
| V | `doanh_thu` | Số tiền thực nhận | Bảo |
| W | `nguoi_cham_soc` | Tên người trực Zalo | Người trực |
| X | `ghi_chu` | Tự do | Ai cũng được |

### Tab 2 — `ADS_DAILY` *(một dòng = một creative × một ngày)*

`ngay · ten_chien_dich · utm_content · utm_term · chi_phi · impression · click · lead_meta_bao · cpl_meta`

> **Lưu ý:** `lead_meta_bao` là số Meta báo, luôn lệch với số đăng ký thật trong Tab 1. **Luôn dùng số Tab 1 làm số chính thức.** Số Meta chỉ dùng để so sánh giữa các creative với nhau.

### Tab 3 — `DASHBOARD` *(chỉ công thức, cấm gõ tay)*

| Khối | Chỉ số | Công thức nguồn |
|---|---|---|
| **Đầu phễu** | Tổng đăng ký · đăng ký paid · đăng ký organic · CPL blended · CPL paid-only | Tab 1 + Tab 2 |
| **VÉ** ⭐ | **Tỷ lệ mua vé · số VIP · số VVIP · doanh thu vé · CPL hiệu dụng** *(chi ads − doanh thu vé) ÷ đăng ký* | Tab 1 cột K2, K3 |
| **Giữ phễu** | Tỷ lệ vào nhóm cộng đồng · **show rate D1→D5 TÁCH THEO TẦNG VÉ** · tỷ lệ rơi từng buổi | Tab 1 cột L, M–Q, K2 |
| **Cuối phễu** | Số buyer · tỷ lệ buyer/dự D1 · AOV · **tỷ lệ mua combo** · **tỷ lệ nâng cấp** | Tab 1 cột S–V |
| **Tiền** | Doanh thu · chi phí ads · ROAS · lãi gộp ước tính | Tab 1 + Tab 2 |

### Tab 4 — `THEO_NHANH` *(tách CEO-AIOS và DIGITAL-BUILDER)*

Toàn bộ chỉ số Tab 3, nhưng **lọc theo cột D**. Luật 7 doc 10: hai nhánh không bao giờ gộp báo cáo.

### Tab 5 — `THEO_CREATIVE`

`utm_content · chi phí · đăng ký · CPL · **% mua vé** · số dự D1 · số buyer · doanh thu · cost-per-buyer`

> **Hai cột quan trọng nhất là `% mua vé` và `cost-per-buyer`, không phải CPL.** Một creative CPL 42k mà không ai mua vé và không ai mua khóa thì tệ hơn creative CPL 126k có 18% mua vé. Doc 08 mục 7 đã nói nguyên lý; đây là nơi biến nó thành số, và [[34-mo-hinh-so-chuoi-1-va-ky-luat-ngan-sach]] mục 4.2 biến nó thành luật giữ/tắt ad.

---

## 6. Nhịp nhập liệu — ai làm gì, lúc nào

| Thời điểm | Việc | Ai | Thời lượng |
|---|---|---|---|
| Mỗi sáng 09h00 | Nhập chi phí + impression + click ads hôm qua vào Tab 2 | Nguyệt | 10 phút |
| Ngay sau mỗi buổi (22h00) | Export attendee Zoom → dán vào Tab 1 cột M–Q | Hà | 15 phút |
| Ngay sau mỗi buổi (22h30) | Export giao dịch → cập nhật cột S–V | Bảo | 15 phút |
| D−1 | Đối chiếu danh sách nhóm Zalo với Tab 1 → điền cột L | Chi | 30 phút |
| Mỗi sáng 09h30 | Đọc Tab 3, ra 1 quyết định ads | Nguyệt | 15 phút |

**Tổng: dưới 1,5 giờ/ngày cho cả đội.** Nếu vượt quá, spec đã sai — báo lại để cắt bớt.

---

## 7. Bảy cổng kiểm tra trước khi bật ads

Không qua đủ 7 cổng thì **không được bật đồng nào**. Đây là luật cứng của doc 09.

| # | Cổng | Cách kiểm | Ai xác nhận |
|:--:|---|---|---|
| 1 | Pixel Meta bắn đúng trên landing | Meta Pixel Helper thấy `PageView` | Nguyệt |
| 2 | `Lead` bắn đúng trên trang cảm ơn | Tự đăng ký thử, thấy event | Nguyệt |
| 3 | 5 trường UTM ẩn ghi được vào Sheet | Đăng ký thử qua link có UTM, kiểm cột F–J | Bảo |
| 4 | Form ghi đúng vào Tab 1 trong ≤60 giây | Đăng ký thử | Bảo |
| 5 | Trang cảm ơn có link nhóm cộng đồng hoạt động | Bấm thử từ điện thoại | Chi |
| 6 | Export Zoom ra được file có số điện thoại | Chạy thử một phòng Zoom 5 phút | Hà |
| 7 | Tab 3 tự tính đúng khi thêm dòng mới | Thêm 3 dòng giả rồi xóa | Nguyệt |
| **8** | **Trang order bump hiện đúng sau khi submit form free** | Đăng ký thử | **Bảo** |
| **9** | **Mua thử vé 280k → `TicketPurchase` bắn + cột K2/K3 ghi đúng** | Giao dịch thật rồi hoàn | **Bảo** |
| **10** | **Trường VAT hiện đúng khi tick "Có"** | Thử cả hai nhánh | **Bảo** |

**Test đầu-cuối bắt buộc:** một người lạ (không phải người dựng) đăng ký qua link có UTM đầy đủ trên điện thoại 4G → kiểm đủ 7 cổng → xóa dòng test. Làm **hai lần**, một lần Android một lần iPhone.

---

## 8. Ba thứ KHÔNG làm ở chuỗi 1

| Không làm | Vì sao |
|---|---|
| **Không dựng CRM** | 2 tuần không đủ. Sheet chạy đúng > CRM chạy sai. CRM để Đợt 3 |
| **Không làm server-side CAPI** | Tốn 3–5 ngày dev, lợi ích chỉ rõ khi quy mô ads lớn hơn. Ghi vào backlog |
| **Không gắn GA4** | Với một landing một CTA, GA4 không thêm quyết định nào mà Sheet không cho. Ghi vào backlog |

> Nguyên tắc: chuỗi 1 chỉ cần **đo đủ để ra quyết định**, không cần đo đẹp. Đo đẹp là việc của chuỗi 3 trở đi.

---

## 9. Rủi ro và cách chặn

| Rủi ro | Cách chặn |
|---|---|
| Đội quên gắn UTM khi đăng organic | Nguyệt tạo sẵn 20 link có UTM trong `UTM_REGISTRY`, đội chỉ copy |
| Số điện thoại nhập lệch định dạng (`+84`, `0`, có khoảng trắng) | Công thức chuẩn hóa ở cột phụ: bỏ ký tự không phải số, chuyển `84` → `0` |
| Zoom không xuất được số điện thoại | **Kiểm ngay hôm nay.** Nếu không xuất được thì nối bằng email — phải quyết trước khi mở đăng ký |
| Ai đó sửa công thức Tab 3 | Khóa Tab 3, chỉ Nguyệt có quyền sửa |
| Số Meta và số Sheet lệch nhau, đội cãi nhau | Luật: **Sheet là số chính thức.** Ghi vào đầu Tab 3 bằng chữ đỏ |
| Mất file | Bản sao tự động hằng ngày sang Drive riêng — đặt lịch một lần |

---

## Khối bàn giao

**Dùng ngay:** từ điển UTM (mục 2) · trường form (mục 3) · từ điển event (mục 4) · cấu trúc Sheet (mục 5) · 7 cổng kiểm tra (mục 7).

**`[PHẢI KIỂM NGAY HÔM NAY]`:** Zoom có xuất được số điện thoại người dự không. Nếu không, toàn bộ cách nối dữ liệu ở mục 1 phải đổi sang email — và phải đổi **trước** khi mở đăng ký.

**`[CẦN BỔ SUNG]`:** tên miền landing chính thức · link nhóm Zalo chuỗi 1 · quyền truy cập Sheet cho từng người.

**Không được làm:** bật ads khi chưa qua đủ 7 cổng · đăng link không có UTM · để hai người cùng sửa một ô.

*Tài liệu 29 · spec triển khai · 29/07/2026 · phái sinh từ [[16-webinar-funnel-blueprint]] mục 10, [[09-marketing-strategy]] mục 7, [[23-content-plan-afw-free-paid-da-kenh]] mục 10.*
