---
name: mkt-phan-tich-video-notebooklm
description: Phân tích một danh sách nguồn bằng NotebookLM CLI, gồm video YouTube, URL web, file local, Google Drive ID hoặc văn bản thô. Dùng khi người dùng muốn nạp nhiều nguồn vào cùng một notebook, hỏi đáp hoặc tổng hợp insight chéo giữa các nguồn và nhận kết quả bằng tiếng Việt mà không qua hệ thống database trung gian.
---

# Phân Tích Danh Sách Nguồn Bằng NotebookLM

Nhận trực tiếp danh sách nguồn, nạp chúng vào một notebook bằng CLI `nlm`, chờ xử lý hoàn tất, rồi truy vấn NotebookLM để tổng hợp kết quả. Không dùng MCP hay database trung gian.

## Đầu vào

Yêu cầu người dùng cung cấp ít nhất một nguồn. Chấp nhận các loại sau:

- URL video YouTube.
- URL trang web công khai.
- Đường dẫn tuyệt đối đến file local, như PDF hoặc tài liệu hỗ trợ bởi NotebookLM.
- Google Drive document ID.
- Văn bản thô.

Nhận thêm các trường tùy chọn:

- `notebook_id`: dùng notebook có sẵn.
- `title`: tên notebook mới.
- `question`: câu hỏi hoặc mục tiêu phân tích.
- `output`: đường dẫn file Markdown hoặc JSON cần lưu.
- `profile`: profile `nlm`; mặc định dùng profile hiện hành.

Nếu người dùng chỉ đưa danh sách nguồn, dùng câu hỏi mặc định:

```text
Tổng hợp các nguồn bằng tiếng Việt. Trình bày: tóm tắt điều cốt lõi, các luận điểm chung,
điểm khác biệt hoặc mâu thuẫn, insight đáng chú ý, hành động đề xuất và danh sách nguồn
hỗ trợ cho từng kết luận. Không suy diễn ngoài nội dung nguồn.
```

## Quy trình

### 1. Tự cài CLI nếu còn thiếu

Kiểm tra `nlm` trước. Nếu chưa có, tự cài package chính xác `notebooklm-mcp-cli`; không yêu cầu người dùng tự gõ lệnh cài.

```bash
if ! command -v nlm >/dev/null 2>&1; then
  if command -v uv >/dev/null 2>&1; then
    uv tool install notebooklm-mcp-cli
  elif command -v pipx >/dev/null 2>&1; then
    pipx install notebooklm-mcp-cli
  else
    python3 -m pip install --user notebooklm-mcp-cli
  fi
fi

hash -r
nlm_cmd=$(command -v nlm || true)
if [ -z "$nlm_cmd" ]; then
  nlm_cmd="$(python3 -m site --user-base)/bin/nlm"
fi
"$nlm_cmd" --version
```

Sau khi cài:

- Xác nhận binary chạy được bằng `"$nlm_cmd" --version`.
- Nếu cài lỗi, báo nguyên văn lỗi package manager và dừng; không giả vờ tiếp tục.
- Không tự nâng cấp nếu `nlm` đã tồn tại và đang chạy được.
- Dùng biến `nlm_cmd` thay cho lệnh `nlm` trong các bước sau nếu binary chưa có trong `PATH`.

### 2. Kiểm tra đăng nhập

```bash
"$nlm_cmd" login --check
```

Nếu chưa đăng nhập, tự chạy `"$nlm_cmd" login` để mở luồng đăng nhập, rồi chờ người dùng hoàn tất trên trình duyệt. Sau đó chạy lại `"$nlm_cmd" login --check`. Không hiển thị cookie, credential hoặc chạy `--debug` trong đầu ra chia sẻ.

### 3. Chuẩn hóa danh sách nguồn

- Phân loại từng nguồn thành `youtube`, `url`, `file`, `drive` hoặc `text`.
- Kiểm tra file local tồn tại trước khi upload.
- Giữ nguyên thứ tự nguồn để báo cáo lỗi chính xác.
- Loại bỏ mục trùng hoàn toàn nhưng không tự gộp các URL khác nhau.
- Báo rõ nguồn không hợp lệ; tiếp tục với các nguồn hợp lệ còn lại.

### 4. Chọn notebook

Nếu có `notebook_id`, xác minh notebook truy cập được:

```bash
"$nlm_cmd" source list <notebook_id> --json
```

Nếu chưa có `notebook_id`, tự tạo đúng một notebook cho yêu cầu hiện tại. Việc người dùng yêu cầu phân tích danh sách nguồn được xem là cho phép tạo notebook làm việc này:

```bash
"$nlm_cmd" notebook create "<title>"
```

Lấy notebook ID từ kết quả lệnh rồi kiểm tra lại bằng:

```bash
"$nlm_cmd" notebook list --json
```

### 5. Nạp từng nguồn và chờ xử lý

Chạy từng nguồn riêng để xác định chính xác nguồn nào lỗi. Luôn dùng `--wait`.

```bash
# YouTube
"$nlm_cmd" source add <notebook_id> --youtube "<youtube_url>" --wait --wait-timeout 600

# URL web
"$nlm_cmd" source add <notebook_id> --url "<url>" --wait --wait-timeout 600

# File local
"$nlm_cmd" source add <notebook_id> --file "/absolute/path/to/file.pdf" --wait --wait-timeout 600

# Google Drive
"$nlm_cmd" source add <notebook_id> --drive "<drive_document_id>" --wait --wait-timeout 600

# Văn bản thô
"$nlm_cmd" source add <notebook_id> --text "<text>" --title "<source_title>" --wait --wait-timeout 600
```

Sau khi nạp xong, lấy danh sách source ID thực tế:

```bash
"$nlm_cmd" source list <notebook_id> --json
```

Không giả định có lệnh `nlm source status`; phiên bản CLI hiện hành không có lệnh này.

### 6. Phân tích

Truy vấn toàn bộ nguồn đã nạp:

```bash
"$nlm_cmd" notebook query <notebook_id> "<question>" --json
```

Khi chỉ cần một nhóm nguồn, truyền danh sách source ID:

```bash
"$nlm_cmd" notebook query <notebook_id> "<question>" \
  --source-ids "<source_id_1>,<source_id_2>" --json
```

Nếu cần hiểu riêng một nguồn trước khi tổng hợp, dùng:

```bash
"$nlm_cmd" source describe <source_id> --json
```

Với `nlm 0.5.26`, câu trả lời JSON nằm tại `.value.answer`. Kiểm tra bằng:

```bash
"$nlm_cmd" notebook query <notebook_id> "<question>" --json \
  | jq -e '.value.answer | type == "string" and length > 0'
```

Nếu phiên bản mới đổi schema, dùng `jq 'paths(scalars)'` để xác định đường dẫn thực tế thay vì báo query thất bại khi exit code bằng `0`.

### 7. Trả kết quả

Trả về:

1. Notebook ID và link `https://notebooklm.google.com/notebook/<notebook_id>`.
2. Số nguồn nhận vào, số nguồn nạp thành công và danh sách nguồn lỗi.
3. Kết quả tổng hợp bằng tiếng Việt.
4. Các kết luận chưa đủ bằng chứng hoặc có mâu thuẫn giữa nguồn.
5. Đường dẫn file đầu ra nếu người dùng yêu cầu lưu.

Khi lưu trong vault này, ưu tiên:

```text
04. Resources/Market & Competitor Research/Video AI/NotebookLM/
```

Tạo wikilink tới dự án hoặc note nghiên cứu liên quan để không sinh note mồ côi.

## Quy tắc an toàn

- Không tự động xoá source hoặc notebook sau khi phân tích.
- Chỉ chạy `nlm source delete` hoặc `nlm notebook delete` khi người dùng yêu cầu rõ ràng và đã xác nhận đúng ID.
- Không tạo quá một notebook mới cho cùng một yêu cầu nếu người dùng không yêu cầu tách riêng.
- Không đưa dữ liệu riêng tư hoặc dữ liệu khách hàng vào NotebookLM nếu người dùng chưa cho phép.
- Không báo thành công nếu chưa kiểm tra `nlm source list <notebook_id> --json` và nhận được kết quả query.

## Xử lý lỗi

- `nlm` không tồn tại: tự cài `notebooklm-mcp-cli` theo thứ tự `uv` → `pipx` → `pip --user`, rồi kiểm tra lại binary.
- Đăng nhập hết hạn: yêu cầu chạy lại `nlm login`.
- Một nguồn lỗi: ghi nhận lỗi, tiếp tục các nguồn còn lại và không âm thầm bỏ qua.
- Hết thời gian xử lý: thử lại một lần với `--wait-timeout` lớn hơn; nếu vẫn lỗi thì báo nguồn bị kẹt.
- Query lỗi: xác nhận còn ít nhất một source đã xử lý thành công rồi chạy lại một lần.
- Cú pháp CLI khác tài liệu: đọc `nlm <nhóm-lệnh> <lệnh> --help` trên máy hiện tại và dùng cú pháp thực tế.
