# Preset subtitle `social-outline`

Preset này tái hiện subtitle trong ảnh mẫu user cung cấp: chữ trắng đậm, viền đen rõ, không hộp nền, căn giữa thấp nhưng vẫn nằm trong safe area.

## Thông số 1080×1920

| Thuộc tính | Giá trị |
|---|---|
| Font | Be Vietnam Pro |
| Weight | 800 |
| Font size | 54px mặc định; 50px khi dòng dài |
| Line height | 1.12 |
| Màu chữ | `#FFFFFF` |
| Viền | `6px #0A0A0A` |
| Shadow | `0 3px 8px rgba(0,0,0,.50)` |
| Nền | Không có |
| Max width | 920px |
| Padding ngang | 64px |
| Vị trí | `bottom: 300px` |
| Số dòng | Tối đa 2 |
| Nhóm từ | 2–6 từ, ưu tiên một cụm nghĩa |

Marker danh sách (`#1`, `#2`) đứng riêng phía trên caption: 72px, weight 800, viền 7px, gap 12px. Marker không được lặp trong dòng caption.

## Motion

- Entrance 0,14s: opacity 0→1, scale 0.94→1, y 10→0, `power2.out`.
- Không bounce, karaoke từng từ hoặc đổi màu liên tục.
- Hard hide đúng `end`; timing không hand-edit.
- Nếu caption vắt thành 3 dòng, rút nhóm từ; không giảm font dưới 48px.

## Tương phản và tránh che mặt

Viền đen là lớp tương phản chính, không thêm box. Nếu áo trắng/nền trắng làm chữ khó đọc, tăng shadow hoặc thêm gradient tối rất nhẹ ở master; không đổi sang hộp caption. Có thể dịch stage trong khoảng `bottom: 260–340px` để tránh miệng/tay nhưng phải giữ nhất quán trong một scene.
