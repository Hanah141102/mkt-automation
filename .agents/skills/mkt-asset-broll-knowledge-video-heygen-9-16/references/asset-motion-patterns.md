# Ngữ pháp motion cho asset thật

Mục tiêu là làm ảnh/screenshot trở thành một hành động nhìn thấy được. Không dùng animation để che việc asset không chứng minh claim.

## Pattern router

### Screenshot callouts

Dùng cho dashboard, website, tài liệu và giao diện.

```text
headline → screenshot vào ở display scale → crop/zoom vùng chính
→ callout xuất hiện đúng spoken cue → proof hold
```

Giữ một screenshot xuyên scene. Không crossfade sang bản vẽ lại. Tối đa ba callout, mỗi callout chỉ một dòng ngắn.

### Progressive evidence stack

Dùng cho 2–4 ảnh chứng minh nhiều vế của cùng một kết luận.

Cho ảnh xuất hiện tuần tự theo VO và giữ lại trên canvas. Ảnh mới phải làm kết luận mạnh hơn; không xóa ảnh cũ chỉ để có chuyển động.

### Compare two

Dùng cho nội sàn/ngoại sàn, trước/sau hoặc đúng/sai.

Đặt hai hero pane khác màu nhãn nhưng không tạo hai dashboard nhỏ. Reveal bên thứ hai khi VO nêu đối trọng, sau đó cho một verdict/takeaway khóa frame.

### Big stat with proof

Dùng khi lời có con số quan trọng.

Hiện số ở display scale, rồi đưa ảnh/screenshot bằng chứng vào dưới hoặc sau số. Không để con số đứng một mình như title card. SFX `ting` chỉ tại một stat mạnh nhất.

### Full-screen evidence B-roll

Dùng Pexels hoặc video thật cho một hành động cụ thể. Clip 2–6 giây, muted, portrait ưu tiên. Cho footage chạy full-screen sạch; ngoài captions, không thêm annotation, chip, chart, tint note hoặc ảnh nhỏ. Kết thúc clip tại semantic boundary rồi clean-cut sang visual kế tiếp.

### Evidence-to-diagram

Dùng khi footage cho thấy hành động nhưng câu kế tiếp giải thích cơ chế. Kết thúc footage ở cuối vế hành động; bắt đầu diagram riêng đúng timestamp đó. Không chạy diagram ẩn bên dưới footage và không crossfade hai dominant visual.

### Sequential text/chart

Dùng khi không có asset sát nghĩa hoặc claim là một cơ chế/trình tự. Giữ toàn bộ node/card/row mang nghĩa ở trạng thái hidden. Reveal từng phần tại đúng keyword từ word alignment; connector chỉ xuất hiện khi hai đầu liên quan đã được nói. Không dùng generic stagger làm cả sơ đồ hiện sớm.

### Asset reset

Dùng nền ivory/white reset 0,10–0,20 giây giữa hai luận điểm không liên quan, giống nhịp editorial của video tham khảo. Không dùng reset ở mọi boundary và không để frame trắng quá 0,25 giây.

## Hai họ transition được phép

1. `clean-opaque`: clean cut, white/ivory reset hoặc opaque mask.
2. `directional-carrier`: crop edge, bàn tay, document frame hoặc action vector tiếp tục cùng hướng.

Flash chỉ dành cho một loud moment. Cấm translucent crossfade làm avatar, asset và Pexels chồng mờ lên nhau.

## Timing

- Cho hero asset 0,45–0,70 giây để được nhận diện trước action.
- Cue hình theo word alignment; không đoán timestamp.
- Mỗi reveal 0,25–0,55 giây, dùng `power2.out` hoặc `power3.out`.
- Proof hold ít nhất 0,90 giây.
- Tail dùng live-resolution có nghĩa hoặc deliberate stillness; không breathing loop trang trí.
- Khi Pexels chuyển sang chart, hai dominant placement butt-cut tại cùng semantic timestamp, sai lệch tối đa 50ms.

## Gate tự review

1. Tắt text vẫn nhận ra asset và hành động chính?
2. Asset có chứng minh claim hay chỉ cùng chủ đề?
3. Mỗi callout có spoken cue?
4. Hero asset thắng callout về scale và contrast?
5. Frame cuối tự giải thích được kết luận?
6. Seam có carrier/vector hoặc clean-cut reason?
7. Pexels có sạch ngoài captions và chart có reveal đúng từng keyword?

Fail câu 1–3 hoặc 7 thì đổi asset/cue plan trước khi sửa animation.
