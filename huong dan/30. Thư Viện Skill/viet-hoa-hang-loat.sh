#!/usr/bin/env bash
# =============================================================================
#  Việt hoá hàng loạt phần thân file SKILL.md
# =============================================================================
#  Dịch toàn văn các skill còn tiếng Anh sang tiếng Việt bằng Claude Code
#  chạy ở chế độ không tương tác. Chạy được nhiều lần — skill đã dịch sẽ bỏ qua.
#
#  YÊU CẦU
#    - Đã cài Claude Code và đăng nhập (gõ `claude` chạy được)
#
#  CÁCH DÙNG
#    cd "30. Thư Viện Skill"
#    chmod +x viet-hoa-hang-loat.sh
#
#    ./viet-hoa-hang-loat.sh --xem                # xem còn skill nào chưa dịch
#    ./viet-hoa-hang-loat.sh --nhom "03"          # dịch cả một nhóm
#    ./viet-hoa-hang-loat.sh --skill blog-post    # dịch một skill
#    ./viet-hoa-hang-loat.sh --so-luong 20        # dịch 20 skill kế tiếp
#
#  LƯU Ý
#    - Mỗi skill tốn khoảng 15–60 giây và có tính phí theo tài khoản Claude.
#    - Toàn bộ 500+ skill sẽ tốn đáng kể. Nên dịch theo nhóm, khi thật sự cần.
#    - Bản gốc tiếng Anh được lưu lại ở references/<mã>-ban-goc-en.md
# =============================================================================

set -uo pipefail
KHO="$(cd "$(dirname "$0")" && pwd)/_Kho Skill"
VAULT="$(cd "$(dirname "$0")/../10. Hệ Điều Hành/Vault Doanh Nghiệp" 2>/dev/null && pwd)"
CHE_DO=""; THAM_SO=""; SO_LUONG=9999

while [[ $# -gt 0 ]]; do
  case "$1" in
    --xem)      CHE_DO="xem"; shift ;;
    --skill)    CHE_DO="skill";  THAM_SO="${2:-}"; shift 2 ;;
    --nhom)     CHE_DO="nhom";   THAM_SO="${2:-}"; shift 2 ;;
    --so-luong) CHE_DO="${CHE_DO:-tat-ca}"; SO_LUONG="${2:-20}"; shift 2 ;;
    *) echo "Tham số không hiểu: $1"; exit 1 ;;
  esac
done
[[ -z "$CHE_DO" ]] && CHE_DO="xem"

# --- Kiểm tra phần thân đã là tiếng Việt chưa ---
da_tieng_viet() {
  local f="$1"
  local than; than="$(awk 'BEGIN{n=0} /^---$/{n++; next} n>=2' "$f")"
  local vn en
  vn=$(printf '%s' "$than" | grep -oiE '[àáảãạăâèéẻẽẹêìíòóỏôơùúưỳýđ]' | wc -l | tr -d ' ')
  en=$(printf '%s' "$than" | grep -owiE 'the|and|when|with|for|your|this|that|user|should|must' | wc -l | tr -d ' ')
  [[ "$en" -lt 40 || "$vn" -gt $((en*3)) ]]
}

# --- Danh sách skill cần dịch ---
TAT_CA=()
while IFS= read -r d; do TAT_CA+=("$d"); done < <(find "$KHO" -mindepth 1 -maxdepth 1 -type d | sort)
CAN_DICH=()
for d in "${TAT_CA[@]}"; do
  f="$d/SKILL.md"; [[ -f "$f" ]] || continue
  ma="$(basename "$d")"
  case "$ma" in obsidian-*|json-canvas|hyperframes*|remotion-to-*|website-to-*|mkt-defuddle) continue ;; esac
  case "$CHE_DO" in
    skill) [[ "$ma" == "$THAM_SO" ]] || continue ;;
    nhom)  grep -q "^nhom: \"$THAM_SO" "$f" || continue ;;
  esac
  da_tieng_viet "$f" || CAN_DICH+=("$ma")
done

echo "Tổng skill trong kho : ${#TAT_CA[@]}"
echo "Còn tiếng Anh        : ${#CAN_DICH[@]}"
if [[ "$CHE_DO" == "xem" ]]; then
  printf '  %s\n' "${CAN_DICH[@]:0:40}"
  [[ ${#CAN_DICH[@]} -gt 40 ]] && echo "  … và $(( ${#CAN_DICH[@]} - 40 )) skill nữa"
  echo; echo "Chạy lại với --nhom \"03\" hoặc --so-luong 20 để bắt đầu dịch."
  exit 0
fi
[[ ${#CAN_DICH[@]} -eq 0 ]] && { echo "Không còn gì để dịch."; exit 0; }

command -v claude >/dev/null || { echo "LỖI: chưa cài Claude Code."; exit 1; }

dem=0; ok=0; loi=0
for ma in "${CAN_DICH[@]}"; do
  [[ $dem -ge $SO_LUONG ]] && break
  dem=$((dem+1))
  f="$KHO/$ma/SKILL.md"
  echo "[$dem/$(( SO_LUONG < ${#CAN_DICH[@]} ? SO_LUONG : ${#CAN_DICH[@]} ))] $ma"

  mkdir -p "$KHO/$ma/references"
  [[ -f "$KHO/$ma/references/$ma-ban-goc-en.md" ]] || cp "$f" "$KHO/$ma/references/$ma-ban-goc-en.md"

  if claude -p "Dịch toàn văn phần thân của file '$f' sang tiếng Việt rồi ghi đè lại chính file đó.

BẮT BUỘC:
- Giữ NGUYÊN toàn bộ khối frontmatter giữa hai dấu --- ở đầu file, không đổi một ký tự nào.
- Giữ NGUYÊN cấu trúc heading: đúng số lượng và đúng cấp độ #, ##, ###.
- Giữ NGUYÊN mọi khối mã, tên file, đường dẫn, biến, URL.
- Giữ NGUYÊN số cột và số dòng của mọi bảng, chỉ dịch nội dung trong ô.
- Dịch ĐỦ, không tóm tắt, không bỏ mục nào.
- Viết như người Việt viết cho chủ doanh nghiệp Việt Nam đọc, không dịch máy.
- Giữ nguyên tiếng Anh các thuật ngữ: offer, lead, landing page, KPI, ROAS, CPM, CTR, CPA, LTV, CAC, SEO, GA4, UTM, A/B test.
- Quy đổi ví dụ tiền USD sang VND, định dạng kiểu Việt Nam (1.000.000 đ).
- Ví dụ nền tảng nước ngoài thay bằng tương đương Việt Nam khi không làm sai ý.

Chỉ sửa đúng file đó, không tạo file mới, không hỏi lại." >/dev/null 2>&1
  then
    if da_tieng_viet "$f"; then
      echo "   ✓ xong"; ok=$((ok+1))
      [[ -n "${VAULT:-}" && -d "$VAULT/.claude/skills/$ma" ]] && cp "$f" "$VAULT/.claude/skills/$ma/SKILL.md" && echo "   ✓ đã đồng bộ sang vault"
    else
      echo "   ⚠ chạy xong nhưng phần thân vẫn còn nhiều tiếng Anh — kiểm tra tay"; loi=$((loi+1))
    fi
  else
    echo "   ✗ lỗi khi gọi Claude"; loi=$((loi+1))
  fi
done

echo
echo "==============================="
echo "Đã dịch xong : $ok"
echo "Cần xem lại  : $loi"
echo "Còn lại      : $(( ${#CAN_DICH[@]} - dem ))"
echo "==============================="
