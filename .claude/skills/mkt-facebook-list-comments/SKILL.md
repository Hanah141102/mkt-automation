---
name: mkt-facebook-list-comments
description: >-
  Tạo và đăng một chuỗi comment ngắn, đánh số 1–10 dưới bài viết Facebook dạng
  liệt kê. Dùng khi người dùng muốn mở rộng các ý trong caption thành các ứng
  dụng dễ hiểu ở phần bình luận, ví dụ “đăng 10 comment”, “comment đánh số” hoặc
  “bài listicle này thêm use case vào comments”. Skill này dùng Composio
  Facebook, xác minh đúng Page và bài viết trước khi thực hiện thao tác đăng.
---

# Facebook List Comments

## Mục tiêu

Biến một bài Facebook dạng liệt kê thành 10 comment riêng, ngắn, dễ đọc và
đánh số từ `1.` đến `10.`. Mỗi comment nêu một ứng dụng hoặc ý chính duy nhất,
giúp người đọc lướt phần bình luận vẫn hiểu được nội dung.

Nhận `page_id`, URL/ID bài viết và tên Page từ người dùng hoặc brand context. Không dùng Page, profile hay nhóm của lần chạy trước làm mặc định.

## Khi nào kích hoạt

Kích hoạt khi người dùng:

- yêu cầu “đăng comment”, “thêm 10 comment”, “comment đánh số 1–10” dưới bài Facebook;
- có bài viết/reel dạng danh sách và muốn giải thích từng ứng dụng ở phần bình luận;
- muốn nội dung comment ngắn, tiếng Việt dễ hiểu, tập trung use case SME.

Nếu người dùng chỉ yêu cầu **soạn nháp**, không gọi công cụ đăng. Nếu không có
URL/ID bài viết, tìm bài gần nhất trên đúng Page rồi báo lại bài đã xác định trước
khi đăng; không tự đoán từ một tài khoản khác.

## Quy tắc viết comment

1. Tạo đúng 10 comment, đánh số liên tục `1.` … `10.`; không dùng số emoji thay thế.
2. Mỗi comment là một đoạn độc lập, thường một câu, khoảng 12–25 từ.
3. Dùng tiếng Việt đời thường: bắt đầu bằng tên ứng dụng rồi nói agent làm gì.
4. Một comment chỉ có một use case; không nhồi nhiều ý hoặc lặp lại ý trước.
5. Bám sát nội dung bài viết và kiến thức đã có; không bịa tính năng, số liệu,
   khách hàng hay cam kết kết quả.
6. Ưu tiên các động từ cụ thể: nhận tin, lọc, nhập, nhắc, tổng hợp, dự báo,
   cập nhật, chuyển người duyệt.
7. Với tài chính/kế toán, có thể nêu dự toán và dòng tiền nhưng phải nhắc dùng
   công thức/kiểm tra; không để agent tự nộp thuế, chuyển tiền hoặc quyết định pháp lý.
8. Không thêm hashtag, link, CTA hoặc lời quảng cáo vào từng comment trừ khi
   người dùng yêu cầu.
9. Nếu bài có ít hơn 10 điểm, chỉ tách thành các ứng dụng con khi được suy ra
   rõ ràng từ bài; nếu phải bịa thêm, hỏi người dùng thay vì tự mở rộng.

### Mẫu giọng điệu

```text
1. CSKH 24/7: nhận tin nhắn, trả lời câu hỏi thường gặp và chuyển ca khó cho nhân viên.
2. Sales: hỏi nhu cầu, phân loại khách, tư vấn và nhắc lại khách chưa chốt.
3. Cứu lead cũ: tự tìm khách từng hỏi nhưng chưa mua để follow-up đúng ngữ cảnh.
4. Marketing: nghiên cứu insight, tạo nội dung, đăng bài, đo kết quả và tối ưu.
5. Kế toán: đọc hóa đơn, nhập dữ liệu vào Sheets và nhắc hạn chứng từ.
6. Tài chính: gom doanh thu, chi phí, công nợ thành dự toán và dòng tiền có công thức kiểm tra.
7. Tuyển dụng: lọc CV theo tiêu chí, trả lời ứng viên và xếp lịch phỏng vấn.
8. Giữ khách: nhắc mua lại, gợi ý combo và cứu đơn hàng bị bỏ quên.
9. Sản xuất content: biến một brief thành kịch bản, video, caption và lịch đăng.
10. Điều phối nội bộ: đọc SOP, giao việc cho agent chuyên môn và chờ duyệt việc quan trọng.
```

Mẫu trên chỉ là chuẩn về độ ngắn và cách diễn đạt; thay nội dung theo đúng
caption đang xử lý.

## Quy trình đăng an toàn

### 1. Kiểm tra kết nối

Ưu tiên Composio:

```bash
command -v composio
composio whoami
composio search "Facebook comment page post"
```

Nếu Facebook toolkit chưa kết nối, dừng và báo người dùng. Không in access token
hoặc credential.

### 2. Xác định Page và bài viết

Sau khi xác minh đúng Page, lấy danh sách bài bằng:

```bash
composio execute FACEBOOK_GET_PAGE_POSTS \
  -d '{"page_id":"<FACEBOOK_PAGE_ID>","limit":25}'
```

Đối chiếu `permalink_url`, tiêu đề/message và thời gian với URL người dùng đưa.
Với Reel, ưu tiên ID composite trả về trong trường `id`, dạng
`page_id_post_id`; không tự ghép ID từ URL nếu chưa kiểm tra quyền truy cập.

### 3. Soạn và xác nhận

Soạn đủ 10 comment, kiểm tra số thứ tự, độ dài, trùng ý và các claim nhạy cảm.
Trước thao tác state-changing, hiển thị ngắn gọn nội dung cuối cùng cùng URL/
`object_id`. Chỉ đăng khi người dùng yêu cầu xuất bản rõ ràng hoặc xác nhận
preview; không đăng nếu họ chỉ nói “soạn giúp”.

### 4. Đăng tuần tự

Mỗi comment là một lần gọi, luôn dùng cùng `object_id` của bài viết:

```bash
composio execute FACEBOOK_CREATE_COMMENT \
  -d '{"object_id":"<PAGE_ID>_<POST_ID>","message":"1. ..."}'
```

Gọi tuần tự từ 1 đến 10, không chạy song song để giữ thứ tự và dễ xác định lỗi.
Lưu `data.id` của từng comment. Không retry mù một comment đã trả về
`successful: true`.

### 5. Xác minh

Sau khi đăng, kiểm tra từng ID (hoặc tối thiểu tất cả ID đã tạo trong response)
bằng:

```bash
composio execute FACEBOOK_GET_COMMENT \
  -d '{"comment_id":"<comment_id>","fields":"id,message,from,parent"}'
```

Xác nhận `from.id` khớp `page_id` đã duyệt, message đúng nội dung và `parent` trỏ
đến đúng bài. Báo cáo URL bài viết, số comment thành công và nếu có comment
thất bại thì nêu rõ số thứ tự; không tự đăng lại khi chưa được duyệt.

## Lỗi và giới hạn

- Nếu `FACEBOOK_GET_PAGE_POSTS` không trả về bài hoặc `object_id` bị từ chối,
  dừng; có thể token thiếu quyền đọc/engagement.
- Nếu một lần đăng thất bại, ghi lại số thứ tự và lỗi, tiếp tục chỉ khi việc đó
  không làm sai thứ tự hoặc tạo spam; nếu không chắc, dừng toàn bộ chuỗi.
- Không dùng URL ngoài trong comment trừ khi người dùng yêu cầu và đã duyệt URL.
- Không bình luận vào profile cá nhân, group hoặc bài không thuộc Page mặc định
  nếu chưa có chỉ định rõ ràng.
