---
workflow: general-video
flow: companion
storyboard: yes
message: "Second Brain giúp em nhìn lại một tuần học và tự chọn bước tiếp theo — người quyết định vẫn là em"
destination: youtube
aspect: 1920x1080
language: vi
audience: "Phụ huynh, thầy cô và các bạn học sinh cấp 1–2"
length: 170s
angle: "Bài thuyết trình của học sinh lớp 3, dựng lại từ 5 file quay sẵn"
---

## Intent

Ghép 5 file quay rời của bé Nhật Minh (lớp 3A05, Vinschool Ocean Park) thành **một
video thuyết trình hoàn chỉnh 16:9**, mở đầu bằng `1.mp4`. Bỏ hết khoảng hở, chỗ nói
vấp và các đoạn nói trùng giữa các bản thu, giữ đúng một mạch: **vấn đề → phương pháp
→ bằng chứng AI phản hồi → lựa chọn của em → lời chúc**.

Tông: trong sáng, gọn gàng, nghiêm túc vừa đủ — video để nộp bài / chia sẻ cho phụ
huynh và các bạn, không phải clip giải trí. Hiệu ứng chữ (HyperFrames) làm nhiệm vụ
**đọc hộ màn hình**: bản thu gốc là màn hình desktop 2560×1440 với chữ rất nhỏ và
webcam bé chỉ ~220px, nên phần chữ động là thứ giữ người xem hiểu được nội dung.

## Assets

- `nhat minh/1.mp4` — talking head dọc 480×854, 24.1s. **Mở đầu video** (Frame 1–3) và làm cutaway câm ở Frame 18–19.
- `nhat minh/Second Brain giúp em level up học tập.mp4` — 2560×1440, 222s. **Mạch chính** của bài thuyết trình (Frame 5–20).
- `nhat minh/Ghi nhớ tiến bộ học tập cuối tuần.mp4` — 2560×1440, 128.8s. Chỉ lấy `00:01.20–00:07.96` để **vá câu mở đầu bị thiếu** trong bản chính (Frame 4); phần graph view dùng làm b-roll câm.
- `nhat minh/b-roll second brain hấp dẫn.mp4` — 1920×1080, 18.1s. Graph view Obsidian tối, dùng ở Frame 3, 8, 15, 17, 21.
- `nhat minh/ChatGPT - 15 August 2026.mp4` — 2560×1440, 19.5s. **Chỉ dùng hình, tắt tiếng**: graph MOC Tiếng Anh Thực Hành làm nền Frame 14.
- `nhat minh/TRANSCRIPT_CHINH_XAC_KEM_TIMESTAMPS.md` — transcript đã hiệu đính, là nguồn chữ chuẩn cho mọi text overlay.
- `nhat minh brain 1.png` — cửa sổ Obsidian: vault + MOC Python. Chiếu ở Frame 5.
- `nhat minh brain nhat ky.png` — trang nhật ký `2026-08-16`. Chiếu ở Frame 6 và Frame 11 (mục "Bằng chứng cần lưu").
- `nhat minh brain chatgpt.png` — khung "Tự nghĩ → Hỏi lại → Kiểm chứng → Dạy lại". Chiếu ở Frame 10.
- `nhat minh brain python.png` — graph view MOC Python. Chiếu ở Frame 14.
- `nhat minh/app whybot.png` — note dự án WhyBot. Chiếu ở Frame 11.
- `nhat minh/minh brain tieng anh thuc hanh.png` — graph MOC Tiếng Anh. Chiếu ở Frame 14.
- `nhat minh/minh avatar.jpg` — ảnh thẻ, cắt tròn làm huy hiệu góc dưới phải.
- `media/pexels/` — 4 clip + 1 ảnh tải từ Pexels, nguồn ghi ở `media/pexels/NGUON.md`.
  (Ảnh chữ tiếng Anh của Pexels đã thôi dùng ở Frame 14, thay bằng graph thật của bé.)
- `media/fonts/` — 18 file `.woff2` Be Vietnam Pro, nhúng thẳng để bản dựng không cần mạng.

## Customizations

- **Cắt khoảng lặng tự động**: giữ 0,15s hơi thở hai đầu mỗi mối cắt; chỉ cắt khoảng lặng ≥ 0,55s. Bản chính 222s → 149s.
- **Vá câu mở đầu**: bản `Second Brain giúp em level up học tập.mp4` bắt đầu giữa câu ("Đến cuối tuần…"). Lấy trọn câu đủ từ file `Ghi nhớ tiến bộ học tập cuối tuần.mp4`.
- **Chữ động thay vì zoom màn hình thô**: mỗi câu trả lời của AI được sắp chữ lại bằng HyperFrames, ảnh màn hình thật đặt cạnh làm bằng chứng.
- **Cutaway câm**: dùng các khung hình bé đang im lặng trong `1.mp4` (5,16–6,79s · 15,33–16,44s · 20,13–21,40s · 23,56–24,10s) để cắt về mặt bé ở Frame 18–19 mà không lệch khẩu hình.

## Notes

- **Tên trường: Vinschool Ocean Park** (bố xác nhận 15/08/2026). Bản hiệu đính transcript
  trước đó ghi nhầm "Smart City" — đã sửa trong video, trong hồ sơ dự án và trong hai file
  transcript gốc ở `nhat minh/`.
- **B-roll Pexels chỉ dùng cảnh vật, không dùng mặt người.** Đã bỏ hai clip có mặt trẻ em
  nước ngoài (bố dạy con, lớp học đông) vì người xem dễ nhầm với Nhật Minh và lệch tông
  một bài thuyết trình của học sinh Việt Nam. Thay bằng: sổ và bút trên bàn, tay lật trang
  vở, hồ bơi vắng, lớp học trống.
- **Ảnh Obsidian được chiếu rõ, không làm nền mờ.** Bố đã gửi 4 ảnh độ phân giải cao;
  chúng đặt trong khung cửa sổ bo góc bên phải, neo mép trái để không cắt mất chữ đầu dòng.

- **Bỏ tiếng** hai đoạn: bé đùa với ChatGPT voice mode, và đoạn bố dặn con phía sau. Chỉ giữ phần hình làm b-roll câm. (Chốt ngày 15/08/2026.)
- Bong bóng webcam trong bản thu chính che mất chữ ở khối "Khỏe mạnh" — khi crop vùng câu trả lời AI phải né hoặc làm mờ mềm bong bóng đó.
- Toàn bộ chữ trên màn hình bằng tiếng Việt có dấu. Tên riêng giữ nguyên: MindMirror, Second Brain, WhyBot, Python, Obsidian.
- `1.mp4` chỉ rộng 480px — luôn đặt trong thẻ dọc ~600×1067, **không** phóng full-bleed.
