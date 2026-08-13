---
name: kiem-tra-cong
description: "Quét vault và chấm cổng Xong của một bước trong Khung Vận Hành A-Z bằng bằng chứng thật, thay vì để người dùng tự tick checklist. Chỉ ra chính xác còn thiếu gì, ở file nào, và chạy skill nào để bịt. Dùng trước khi chuyển sang bước tiếp theo."
allowed-tools: Read Glob Grep Bash
ten-viet: "Kiểm Tra Cổng Xong"
nhom: "11. Vận Hành & Công Nghệ"
ten-goc: "Kiểm Tra Cổng Xong"
---

# Kiểm Tra Cổng Xong

## Khi nào dùng skill này

- Trước khi chuyển từ bước này sang bước sau trong Khung Vận Hành A–Z
- Khi nghi ngờ mình đã bỏ sót gì đó ở bước trước
- Trong buổi nghiệm thu tuần theo Lộ Trình 8 Tuần
- Khi AI cho ra kết quả nhạt và nghi là do thiếu ngữ cảnh nền

**Cách gọi:** `/kiem-tra-cong 02` · `/kiem-tra-cong tất cả`

---

## Nguyên tắc cốt lõi

CHECKLIST NGƯỜI TỰ TICK LÀ CHECKLIST LUÔN ĐẦY ĐỦ. CHỈ CÓ BẰNG CHỨNG TRONG VAULT MỚI NÓI THẬT. SKILL NÀY KHÔNG HỎI NGƯỜI DÙNG ĐÃ LÀM CHƯA — NÓ ĐI ĐỌC FILE.

---

## Quy trình

1. Xác định bước cần kiểm tra
2. Chạy các phép kiểm tương ứng ở bảng dưới — **đọc file thật, không hỏi người dùng**
3. Với mỗi mục: ✅ đạt · ⚠️ đạt một phần · ❌ chưa đạt
4. Kết luận qua cổng hay chưa, kèm việc còn thiếu và skill để bịt

**Luật chấm:** một ❌ là chưa qua cổng. ⚠️ thì người dùng tự quyết, nhưng phải nói rõ rủi ro nếu đi tiếp.

---

## Bảng phép kiểm theo từng bước

### Bước 01 — Nền Móng
| Kiểm | Cách kiểm | Đạt khi |
|---|---|---|
| Vault đã chạy | Có `CLAUDE.md` ở gốc, có `.claude/skills/` | Cả hai tồn tại |
| Có sổ quyết định | `Decisions/` có ≥1 file không phải `[Mẫu]` | Có ít nhất 1 quyết định thật |
| Không trùng bản chuẩn | Tìm file trùng tên gần giống trong `00. Business Context/` | Không có 2 file cùng mô tả một thứ |

### Bước 02 — Định Vị
| Kiểm | Cách kiểm | Đạt khi |
|---|---|---|
| **Hồ Sơ Mô Hình Kinh Doanh** | Đọc frontmatter, kiểm 6 tham số | **Cả 6 trường đều có giá trị**, không còn rỗng |
| Chân Dung Doanh Nghiệp | Đếm từ, tìm chuỗi placeholder `[`, `...`, `TODO`, `chưa điền` | > 500 từ và không còn placeholder |
| Brand Voice | Đếm mục trong danh sách từ nên dùng / từ tránh / câu mẫu | ≥10 từ nên dùng, ≥10 từ tránh, ≥3 câu mẫu |
| Phân khúc khách hàng | Đếm file `PK*.md` trong `MHKD/Phân Khúc Khách Hàng/` | ≥1 file, mỗi phân khúc một file riêng |
| Giá trị cốt lõi | Đếm file `GT*.md` | ≥1 file |
| Business Model Canvas | Tìm 9 tiêu đề ô trong file BMC | Đủ 9 ô, không ô nào trống |

### Bước 03 — Nghiên Cứu
| Kiểm | Cách kiểm | Đạt khi |
|---|---|---|
| Nghiên cứu thị trường | File trong `04. Resources/Market & Competitor Research/Nghiên Cứu Thị Trường/` | ≥1 file |
| Hồ sơ đối thủ | Đếm file trong `.../Đối Thủ/` | ≥3 file, mỗi đối thủ một file |
| Tách fact/suy luận/giả định | Tìm các nhãn phân loại trong file nghiên cứu | Có đánh dấu rõ |
| Chân dung khách chi tiết | File `PK*.md` có mục điểm đau và hành vi mua | Không chỉ có nhân khẩu |

### Bước 04 — Offer & Giá
| Kiểm | Cách kiểm | Đạt khi |
|---|---|---|
| Hồ sơ sản phẩm | File trong `00. Business Context/Sản Phẩm & Dịch Vụ/` | ≥1 file, mỗi gói một file |
| Có giá | Tìm chuỗi giá trong mỗi hồ sơ sản phẩm | **Mọi hồ sơ đều có giá cụ thể** |
| Điểm hoà vốn | Tìm file phân tích hoà vốn | Có, và có con số doanh thu hoà vốn |
| Offer giá thấp | Có gói giá thấp nhất dưới 20% gói cao nhất | Có ít nhất một offer thử |

### Bước 05 — Phễu
| Kiểm | Cách kiểm | Đạt khi |
|---|---|---|
| Sơ đồ phễu | File phễu trong `03. Areas/Sales Pipeline & CRM/` | Có, ưu tiên kèm `.canvas` |
| Mỗi bước có người và chỉ số | Đọc bảng trong file phễu | Không dòng nào để trống cột người phụ trách |
| Mồi thu lead | File trong `04. Resources/Templates/` | ≥1 mồi thu lead |
| Landing page | File landing trong `03. Areas/Brand & Content/` | ≥1, **trừ khi** `so-huu-diem-cham: ban-tren-san` |

### Bước 06 — Nội Dung
| Kiểm | Cách kiểm | Đạt khi |
|---|---|---|
| Trụ cột nội dung | File trụ cột trong `Brand & Content/` | 3–5 trụ cột |
| Lịch nội dung | `MOC/MOC Content Calendar.md` hoặc file lịch | Có, và có ngày cụ thể |
| Bài đã đăng | Đếm file trong `Content Đã Đăng/` | ≥5 file |
| Frontmatter đủ | Kiểm `content_pillar`, `format`, `hook` trong các bài | ≥80% bài có đủ 3 trường |
| Lịch theo mùa | Nếu `mua-vu: co-mua` → lịch phải là 12 tháng | Không phải lịch 30 ngày lặp lại |

### Bước 07 — Quảng Cáo
| Kiểm | Cách kiểm | Đạt khi |
|---|---|---|
| Kế hoạch quảng cáo | File trong `03. Areas/Marketing Channels/` | Có |
| **Ngưỡng dừng viết sẵn** | Tìm chuỗi ngưỡng dừng trong kế hoạch | **Có con số cụ thể** |
| Chi phí tối đa mỗi khách | Có con số CPA trần | Có |
| Rà tuân thủ | Nếu ngành rủi ro cao → file trong `Playbooks/Tuân Thủ — *.md` | Có |
| Đủ hàng | Nếu `loai-san-pham: vat-ly` → file tồn kho cập nhật trong 7 ngày | Có |

### Bước 08 — Bán Hàng
| Kiểm | Cách kiểm | Đạt khi |
|---|---|---|
| Kịch bản bán hàng | File trong `04. Resources/Playbooks/` | ≥1 |
| Sổ tay xử lý từ chối | File sổ tay, đếm số từ chối | ≥10 từ chối có câu trả lời |
| Kịch bản theo kênh | Kịch bản Zalo và inbox nếu bán qua hai kênh đó | Có |
| Pipeline đang sống | File pipeline tháng hiện tại, kiểm ngày cập nhật | Cập nhật trong 3 ngày qua |
| Lead có hồ sơ | Số dòng pipeline khớp số file trong `People/` | Chênh dưới 20% |
| Deal Thua có lý do | Mọi dòng trạng thái Thua có ô lý do | Không dòng nào trống |

### Bước 09 — Giao Hàng
| Kiểm | Cách kiểm | Đạt khi |
|---|---|---|
| Quy trình chuẩn | File `QT — *.md` trong `Playbooks/` | ≥1, và **≥3 nếu `loai-san-pham: dich-vu`** |
| Luồng đón khách mới | File onboarding | Có |
| Tiêu chí nghiệm thu | Checklist chất lượng | Có |

### Bước 10 — Giữ Khách
| Kiểm | Cách kiểm | Đạt khi |
|---|---|---|
| Vòng đời khách | File trong `Customer Success & Retention/` | Có |
| Chứng thực | Đếm file trong `04. Resources/Feedback & Chứng Thực/` | ≥5 chứng thực thật |
| Cơ chế giữ khách khớp mô hình | `lien-tuc` → playbook churn · `theo-ky` → hệ nhắc mua lại | Đúng loại |

### Bước 11 — Đo Lường
| Kiểm | Cách kiểm | Đạt khi |
|---|---|---|
| Kế hoạch tracking | File tracking trong `Analytics & Reporting/` | Có |
| Báo cáo định kỳ | Đếm file báo cáo, kiểm nhịp so với chu kỳ bán | ≥2 kỳ liên tiếp, đúng nhịp |
| Định nghĩa chỉ số | File định nghĩa có công thức | Mỗi chỉ số có công thức viết ra |
| Báo cáo giải thích được | Tìm phần "vì sao" trong báo cáo | Không chỉ liệt kê số |

### Bước 12 — Cải Tiến
| Kiểm | Cách kiểm | Đạt khi |
|---|---|---|
| Biên bản rút kinh nghiệm | File retro | ≥1 |
| Backlog cải tiến | File backlog | Mỗi mục có người và hạn |
| Quy trình mới sinh ra | So số file `QT — *.md` với tháng trước | Có tăng |

---

## Mẫu báo cáo

```
CỔNG BƯỚC 02 — ĐỊNH VỊ

✅ Hồ Sơ Mô Hình Kinh Doanh    — đủ 6/6 tham số
✅ Chân Dung Doanh Nghiệp       — 1.847 từ, không còn placeholder
✅ Brand Voice                  — 12 từ nên dùng · 14 từ tránh · 5 câu mẫu
❌ Phân khúc khách hàng         — chỉ có 1 file nhưng mô tả 3 nhóm khác nhau
                                  → tách thành PK1, PK2, PK3 · chạy /customer-persona
⚠️  Business Model Canvas        — ô 7 "Hoạt động chính" đang trống
                                  → chạy /mo-hinh-kinh-doanh, chỉ điền ô còn thiếu

KẾT LUẬN: CHƯA QUA CỔNG (1 lỗi nặng, 1 cảnh báo)
Còn 2 việc, ước 40 phút.

Nếu đi tiếp Bước 03 ngay: nghiên cứu đối thủ sẽ so sai đối tượng,
vì chưa biết chính xác mình phục vụ mấy nhóm khách.
```

Với `/kiem-tra-cong tất cả`, xuất bảng tổng hợp 12 bước và chỉ ra **bước yếu nhất nên làm trước**.

---

## Ghi kết quả vào đâu

| | |
|---|---|
| **Thư mục** | `50. Triển Khai 90 Ngày/` — hoặc `01. Inbox/` nếu chạy trong lúc làm việc |
| **Tên file** | `Kiểm Tra Cổng — Bước NN — YYYY-MM-DD.md` |
| **Bắt buộc** | Chỉ ghi file khi chạy `tất cả` hoặc khi người dùng yêu cầu lưu; kiểm một bước lẻ thì báo trong chat là đủ |

---

## Ràng buộc

- **Không hỏi người dùng "đã làm chưa".** Đi đọc file. Đó là toàn bộ lý do skill này tồn tại.
- **Không tick đạt khi file tồn tại nhưng rỗng.** Kiểm nội dung, không kiểm sự tồn tại.
- **Không nói suông "chưa đạt"** — luôn kèm file nào thiếu gì và skill nào bịt được.
- Đọc `Hồ Sơ Mô Hình Kinh Doanh` trước để biết phép kiểm nào **không áp dụng** cho mô hình này (ví dụ: không đòi landing page với doanh nghiệp bán trên sàn).
