# Đặc tả thiết kế — Second Brain giúp em level up việc học

**Ý đồ một câu:** một cuốn sổ tay số mở ra trong đêm — nền mực sâu, chữ sáng rõ, mọi
hiệu ứng chỉ phục vụ một việc: **đọc hộ người xem những gì màn hình gốc quá nhỏ để đọc**.

## Bảng màu

| Vai trò | Mã | Dùng ở đâu |
|---|---|---|
| Nền sâu | `#070B16` | nền toàn khung |
| Nền thẻ | `#101A2E` | thẻ, panel, khối chữ |
| Viền | `#22304E` | đường kẻ, viền thẻ |
| Chữ chính | `#F2F5FC` | tiêu đề, nội dung |
| Chữ phụ | `#93A4C4` | nhãn, chú thích |
| Đỏ đô | `#C42B54` | nhấn thương hiệu — lấy từ đồng phục Vinschool của bé |
| Vàng | `#F2BC57` | cảnh báo, "chưa đủ bằng chứng", điểm nhấn phụ |
| Xanh ngọc | `#38D6C8` | mọi thứ thuộc về AI / Second Brain / graph |

Ba màu nhấn có phân vai rõ: **đỏ đô = em**, **xanh ngọc = AI**, **vàng = chỗ chưa đạt**.
Không dùng lẫn.

## Chữ

- **Be Vietnam Pro** — toàn bộ chữ hiển thị. 800 cho tiêu đề lớn, 700 cho nhãn, 600/500 cho nội dung.
  Bộ chữ này **dựng riêng cho tiếng Việt**: dấu chồng (Ế, Ộ, Ữ) đặt gọn, không đè nhau,
  không tràn khỏi dòng. Nhúng thẳng 18 file `.woff2` ở `media/fonts/` nên bản dựng
  không phụ thuộc mạng.

  > Vòng đầu dùng **Montserrat** và hỏng: dấu mũ trên Ô bị cắt cụt ở dòng trên cùng,
  > Ế trong "QUYẾT" chồng dấu chật cứng, dấu nặng dưới Ị đâm xuống dòng kẻ. Bài học:
  > một bộ chữ "có hỗ trợ tiếng Việt" không có nghĩa là **dựng cho** tiếng Việt.

- Dòng phải nới rộng hơn tiếng Anh: tiêu đề lớn `line-height` tối thiểu **1.13**,
  nội dung **1.32**. Mặt nạ dòng chừa `padding-top: .16em` để đỉnh dấu không bị cắt.
- **IBM Plex Mono** — mã giờ, nhãn kỹ thuật, tên file.
- Không dùng `<br>` trong đoạn văn; chỉ dùng cho tiêu đề ngắn cố ý xuống dòng.

## Bố cục

- Lề an toàn 110px mỗi bên.
- Ba khung xương lặp lại cả phim: **thẻ dọc + chữ bên phải** (cảnh có mặt bé) ·
  **ảnh màn hình mờ + chữ nổi lên trên** (cảnh giải thích) · **chữ toàn khung** (cảnh chốt ý).
- Ảnh chụp màn hình gốc **luôn ở dưới 30% độ đậm** và làm nền — chưa bao giờ là nội dung chính.
  Nội dung chính luôn là chữ được sắp lại.

## Chuyển động

- Vào cảnh: chữ dựng lên sau mặt nạ dòng (`yPercent 110 → 0`), 0,5–0,7s, `power3.out`.
- Thẻ và chip: `scale 0.86 → 1` kèm `back.out(1.7)`, so le 0,08s.
- Ảnh nền: Ken Burns rất chậm, `scale 1.0 → 1.06` suốt cảnh.
- Chuyển cảnh: cắt thẳng. Chỉ 4 chỗ chồng mờ 0,4s khi vào/ra b-roll graph.
- Không có hiệu ứng nào lặp vô hạn; mọi tween đều nằm trên dòng thời gian tua được.

## Nguyên tắc tiết chế

Bé đang nói. Chữ vào **sau** từ khoá khoảng 0,15s, rồi đứng yên. Không có chữ nào
chạy suốt cảnh cạnh tranh với giọng nói.
