# Anti-patterns cho raw video 9:16

## Source edit

- Cắt theo transcript segment thô làm gãy từ: dùng word-level và nghe seam.
- Ép video đúng duration storyboard bằng cách speed-up/cắt cụt câu: audio thật quyết định duration.
- Giữ thông tin lớp, trường, địa chỉ, email hoặc logo nhận dạng không cần thiết.
- Dùng take đầu bị vấp khi take sau hoàn chỉnh hơn.

## Media

- Pexels chỉ “cùng chủ đề” nhưng sai hành động.
- Dùng người stock như thể đó là nhân vật thật của user.
- Screenshot thành card nhỏ/nghiêng nên không đọc được.
- Để desktop, dock, webcam hoặc sidebar chiếm khung dọc.
- Chèn media giữa causal trigger và proof.
- Dùng hơn 20% HyperFrames khi media thật đã đủ bằng chứng.

## HyperFrames

- Nhiều card cùng trọng lượng, icon đứng yên hoặc particle/bokeh để lấp khoảng trống.
- Fake morph bằng crossfade; camera move không tạo thông tin.
- `Math.random()`, CSS infinite animation, exit animation, relative tween hoặc DOM measurement giữa timeline.
- Headline tiếng Việt line-height <1.14, tracking quá `-0.04em`, nội dung thiết yếu dưới y=1460.
- Scene agent sửa master, chạy render hoặc tự đổi visual thesis.

## Caption/SFX

- Caption paste theo câu dài, hơn 2 dòng hoặc timing dựa trên source thay vì rough cut.
- Text effect lặp nguyên caption.
- SFX ở mọi transition, volume >0.30, nhiều cue chồng nhau hoặc cue không có spoken/visual anchor.

## Render

- Tin lint master đã kiểm tra toàn bộ scene; vẫn phải inspect và xem frame draft.
- GPU auto treo sau calibration nhưng tiếp tục chờ: chuyển software workers 2.
- Bàn giao trước khi xem contact sheet, ffprobe, hook, seams, proof, CTA và privacy frame.
