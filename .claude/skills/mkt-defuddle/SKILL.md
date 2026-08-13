---
name: mkt-defuddle
description: "Trích nội dung sạch từ trang web, loại bỏ menu và quảng cáo để tiết kiệm dung lượng đọc. Dùng thay cho tải trang thông thường khi cần đọc bài viết, tài liệu hoặc trang đối thủ."
---

# Trích Nội Dung Sạch Từ Web

Use Defuddle CLI to extract clean readable content from web pages. Prefer over WebFetch for standard web pages — it removes navigation, ads, and clutter, reducing token usage.

If not installed: `npm install -g mkt-defuddle`

## Usage

Always use `--md` for markdown output:

```bash
mkt-defuddle parse <url> --md
```

Save to file:

```bash
mkt-defuddle parse <url> --md -o content.md
```

Extract specific metadata:

```bash
mkt-defuddle parse <url> -p title
mkt-defuddle parse <url> -p description
mkt-defuddle parse <url> -p domain
```

## Output formats

| Flag | Format |
|------|--------|
| `--md` | Markdown (default choice) |
| `--json` | JSON with both HTML and markdown |
| (none) | HTML |
| `-p <name>` | Specific metadata property |
