# Editorial Explainer Readability — proof frame phải tự giải thích được

Đọc reference này khi video kiến thức/kinh doanh có nguy cơ thành sơ đồ kỹ thuật nhỏ, user nói
“khó hiểu”, “quá ngắn”, hoặc cần học cấu trúc từ các launch HyperFrames dễ đọc.

## Nguyên tắc trung tâm

Một frame tốt phải đọc được khi đứng hình và tắt tiếng:

```text
Kicker nhỏ
HEADLINE NÓI THẲNG KẾT LUẬN

MỘT VẬT THỂ QUEN THUỘC Ở DISPLAY SCALE
chịu một hành động nhìn thấy được

[ TAKEAWAY PILL ]
```

Không biến mọi nội dung thành blueprint rail, node hoặc micro-label. Blueprint chỉ giải thích
cơ chế; vật thể quen thuộc mới giúp người xem nhận diện tình huống ngay.

## Layout 9:16 mặc định

- `y=120–240`: kicker 3–5 từ.
- `y=250–470`: headline 72–84px, tối đa hai dòng.
- `y=500–1240`: hero visual chiếm 55–65% vùng nội dung.
- `y=1300–1435`: takeaway 32–38px.
- `y>=1480`: chỉ captions.
- Text trong hero visual tối thiểu 28px; micro status 18–20px chỉ dùng cho mã/ngày/trạng thái ngắn.
- Tối đa 6 label và một focal; không thu nhỏ desktop UI để nhét đủ chi tiết.

## Chọn vật thể quen thuộc

| Điều cần nói | Vật thể ưu tiên | Hành động phải nhìn thấy |
|---|---|---|
| Chờ AI / bottleneck | laptop, progress bar, task queue | một việc chạy, các việc khác xếp hàng |
| CEO chốt đầu ra | brief, checklist, form | field được tick rồi nút giao việc kích hoạt |
| Nhiều agent | một work order + stepper | cùng document đổi trạng thái qua từng vai trò |
| Chạy song song | junction + đường nhánh dày | một token tách nhánh cùng lúc |
| Giữ quyền quyết định | gate, khóa, nút duyệt | nhánh nhạy cảm chạm gate và dừng thật |
| So sánh | bar/scale trước–sau | giá trị hoặc chiều dài đổi có nguyên nhân |

Icon chỉ được làm supporting. Nếu bỏ icon mà claim biến mất, metaphor chưa đủ cụ thể.

## Proof-frame contract

Thêm vào mỗi scene brief:

```yaml
headline: "Kết luận 4–8 từ"
familiar_object: "Vật thể người xem nhận ra ngay"
visible_action: "Động từ có thể thấy khi tắt text"
takeaway: "Câu chốt ngắn, không lặp caption"
proof_hold_s: 0.9
continuous_hf_s: 3.5
```

- Cho source object 0,45–0,70s để được nhận diện trước trigger.
- Không đặt Pexels giữa `trigger → transformation → proof`.
- Giữ proof tối thiểu 0,90s; nếu tail live-resolution, proof vẫn phải đọc ổn ở frame cuối.
- Mỗi HyperFrames argument nên có block liên tục tối thiểu 3,5s. Nếu quota footage làm block
  ngắn hơn, thiết kế evidence block riêng hoặc dùng readability override đã được user duyệt.

## Storyboard HTML approval gate

Với direction/preset mới, tạo một HTML review riêng trước khi author scene thật:

1. Một proof frame 9:16 cho mỗi scene.
2. Có nút/tab chuyển scene; không cần animation hoàn chỉnh.
3. Dùng exact headline, hero object và takeaway dự kiến.
4. Chụp contact sheet từ HTML và trình cả HTML + ảnh cho user.
5. Chỉ author `scenes/*.html` sau khi user duyệt.

HTML review là artifact approval, không mount vào master và không thay thế draft render QA.

## Màu và khả năng đọc

- Lấy màu từ `design.md` đã duyệt; tài liệu này không quy định palette.
- Dùng màu có contrast cao nhất trong palette cho body/headline.
- Accent sáng phù hợp cho line, border và surface lớn; không mặc định dùng cho chữ nhỏ.
- Nếu accent text không đạt AA, dùng phiên bản tối/sáng hơn cùng hue hoặc màu body chính; giữ accent ở underline/border.
- Success/danger phải đạt AA trên đúng background thực tế; chạy validator thay vì ước lượng.
- Tránh opacity animation trên text dài nếu nó tạo frame tương phản thấp; ưu tiên translate,
  clip reveal hoặc bật visibility đúng lúc.

## QA bắt buộc sau draft

Trích ít nhất bốn frame cho mỗi scene: source, trigger, transformation và proof. Kiểm tra:

- headline đọc được trong một nhịp nhìn;
- hero object thắng supporting về scale và contrast;
- label không nhỏ hơn giới hạn;
- proof frame tự giải thích claim;
- Pexels seam không để lại stripe/mask kéo dài;
- không có class/state làm mất geometry khi seek.

Với GSAP, không dùng `className:'+=is-active'` nếu class gốc giữ vị trí như `step-1`/`step-2`.
Dùng full class string (`step step-1 is-active`) hoặc animate CSS property trực tiếp; nếu không,
các step có thể rơi về cùng `top:0` và chồng nhau dù static inspect pass.

## Fail conditions

- Headline đẹp nhưng hình chỉ cùng chủ đề, không có động từ.
- Ba card/module ngang hàng thay cho một hero object.
- UI có nhiều label 18–24px và phải phóng to mới đọc được.
- Proof chỉ hiện ở vài frame cuối.
- Pexels chặt đôi một phép biến đổi đang diễn ra.
- Contact sheet đẹp nhưng từng frame không tự giải thích được claim.
