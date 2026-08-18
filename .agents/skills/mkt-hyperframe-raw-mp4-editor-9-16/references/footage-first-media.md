# Footage-first media policy

## Mục tiêu

Ưu tiên bằng chứng thật và hành động thật. HyperFrames chỉ giải thích cơ chế mà raw footage, media user, screenshot hoặc Pexels không thể chứng minh rõ.

## Thứ tự quyết định

1. Raw face cho hook, confession, punchline và CTA.
2. Ảnh/video do user cung cấp, nhất là screenshot sản phẩm, Obsidian, dashboard, tài liệu và kết quả thật.
3. Pexels có hành động khớp `noun + verb`.
4. HyperFrames cho transformation, causal chain, comparison hoặc missing-state.

Không dùng HyperFrames làm nền trang trí phía sau media thật rồi tính cả hai. Layer visually dominant mới được tính vào coverage.

## Visual mix mặc định

- HyperFrames: 0–20% tổng duration.
- Media user + Pexels full-screen: ít nhất 30%.
- Phần còn lại: raw face/screen recording.

Cho phép override nếu video cực ngắn hoặc không có media phù hợp. Ghi ratio, lý do và approval vào `STORYBOARD.md`.

## Media user và Obsidian

- Xem trực tiếp tất cả ảnh; với video, xem frame 10/50/90% và các đoạn có thay đổi lớn.
- User assignment luôn thắng auto scoring nếu file hợp lệ.
- Screenshot chiếm toàn khung hoặc gần toàn khung. Mỗi crop chỉ có một mục tiêu đọc: title, prompt, verdict, checklist hoặc node trung tâm.
- Cắt sidebar, dock, webcam, email và dữ liệu không phục vụ luận điểm.
- Không biến screenshot bằng chứng thành card nhỏ nghiêng.
- Không giả UI khi đã có UI thật. Nếu cần chú thích, không che text gốc.

## Pexels

Mỗi need ghi `intent_vi`, `query_en`, `noun`, `verb`, `desired_duration_s`, `avoid_when`. Query tiếng Anh phải literal: `child hands writing homework notebook close up`, không phải `better learning`.

- Dùng 2–6s; phân tán qua video; mỗi asset một lần.
- Ưu tiên close-up tay, giấy, màn hình và thao tác thật.
- Reject người/sản phẩm khiến người xem tưởng đó là nhân vật hoặc bằng chứng thật của user.
- Giữ creator, URL, license, query và SHA-256 trong manifest.
- Đọc source contact sheet trước trim contact sheet.
- Asset đúng chủ đề nhưng sai khoảnh khắc: đổi `source_start_s`.
- Asset sai nghĩa: exclude ID, đổi query một lần; vẫn sai thì bỏ.

## Placement

- Không đè 0–3s hook hoặc face moment bắt buộc.
- Không chen giữa causal trigger và proof của HyperFrame.
- Không dài hơn câu nó chứng minh.
- Không overlap hai real-media placement.
- B-roll master dùng track 45+, `muted`, H.264 yuv420p 30fps.

## Review gate

Storyboard phải liệt kê từng asset, output interval, source interval, crop, spoken anchor, provenance và privacy note. Contact sheet phải cho thấy raw face, mọi nhóm media user, mọi Pexels và ba state của từng HyperFrame.
