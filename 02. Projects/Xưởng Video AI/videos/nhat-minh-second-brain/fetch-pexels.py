# -*- coding: utf-8 -*-
"""Tìm và tải b-roll Pexels cho các nhịp không có gì để quay.

Chạy:  python3 fetch-pexels.py            # chỉ liệt kê kết quả tìm được
       python3 fetch-pexels.py --download  # tải các mục đã chốt trong PICKS
Cần:   PEXELS_API_KEY trong mkt-automation/.env
"""
import json, os, sys, subprocess, urllib.request, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = f"{ROOT}/media/pexels"
os.makedirs(OUT, exist_ok=True)

KEY = os.environ.get("PEXELS_API_KEY", "")
if not KEY:
    for line in open("/Users/tonyhoang/Documents/GitHub/mkt-automation/.env"):
        if line.startswith("PEXELS_API_KEY"):
            KEY = line.split("=", 1)[1].strip().strip('"').strip("'")
assert KEY, "thiếu PEXELS_API_KEY"

def api(path, **q):
    url = f"https://api.pexels.com/{path}?" + urllib.parse.urlencode(q)
    req = urllib.request.Request(url, headers={"Authorization": KEY,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    return json.load(urllib.request.urlopen(req))

# cảnh cần b-roll → truy vấn. Cố ý ưu tiên cảnh vật / bàn tay / chi tiết,
# tránh khuôn mặt trẻ em lạ để người xem không nhầm với Nhật Minh.
QUERIES = {
 "f02_ban":    ("videos", "sunlight morning desk notebook plant no people"),
 "f19_lop":    ("videos", "empty classroom desks chairs school"),
}

def search(kind, q, n=6):
    if kind == "videos":
        r = api("videos/search", query=q, per_page=n, orientation="landscape", size="medium")
        return [{"id": v["id"], "w": v["width"], "h": v["height"], "dur": v["duration"],
                 "by": v["user"]["name"], "page": v["url"],
                 "file": max([f for f in v["video_files"]
                              if f.get("width") and f["width"] <= 1920],
                             key=lambda f: f["width"], default=None)}
                for v in r["videos"]]
    r = api("v1/search", query=q, per_page=n, orientation="landscape")
    return [{"id": p["id"], "w": p["width"], "h": p["height"], "dur": None,
             "by": p["photographer"], "page": p["url"],
             "file": {"link": p["src"]["large2x"], "width": 1880}} for p in r["photos"]]

# ------------------------------------------------------------------ đã chốt
# (tên file, loại, id Pexels, cắt lấy từ giây thứ mấy, dài bao nhiêu giây)
PICKS = []
if os.path.exists(f"{ROOT}/pexels-picks.json"):
    PICKS = json.load(open(f"{ROOT}/pexels-picks.json"))

if "--download" in sys.argv:
    credits = []
    for p in PICKS:
        dst_raw = f"{OUT}/_raw_{p['name']}"
        if not os.path.exists(dst_raw):
            req = urllib.request.Request(p["link"], headers={"User-Agent": "Mozilla/5.0"})
            open(dst_raw, "wb").write(urllib.request.urlopen(req).read())
        if p["kind"] == "videos":
            # kéo chậm nhẹ khi clip gốc ngắn hơn cảnh; làm mờ khi có mặt người lạ
            steps = ["crop='min(iw,ih*16/9)':'min(ih,iw*9/16)'", "scale=1920:1080:flags=lanczos"]
            if p.get("speed", 1.0) != 1.0:
                steps.append(f"setpts={p['speed']}*PTS")
            steps.append("fps=30")
            if p.get("blur", 0):
                steps.append(f"gblur=sigma={p['blur']}")
            steps.append("eq=brightness=-0.14:saturation=0.62:contrast=0.94")
            vf = ",".join(steps)
            subprocess.run(["ffmpeg","-y","-v","error","-ss",str(p.get("ss",0)),
                            "-t",str(p.get("dur",5)),"-i",dst_raw,"-vf",vf,"-an",
                            "-c:v","libx264","-preset","medium","-crf","20",
                            "-pix_fmt","yuv420p",f"{OUT}/{p['name']}.mp4"], check=True)
        else:
            subprocess.run(["ffmpeg","-y","-v","error","-i",dst_raw,
                            "-vf","crop='min(iw,ih*16/9)':'min(ih,iw*9/16)',scale=1920:1080:flags=lanczos,"
                                  "eq=brightness=-0.16:saturation=0.65:contrast=0.94",
                            "-q:v","3",f"{OUT}/{p['name']}.jpg"], check=True)
        credits.append(f"- {p['name']} — {p['by']} / Pexels — {p['page']}")
        print("  tải xong", p["name"])
    open(f"{ROOT}/media/pexels/NGUON.md","w").write(
        "# Nguồn b-roll Pexels\n\nGiấy phép Pexels — dùng thương mại tự do, không bắt buộc "
        "ghi công nhưng vẫn ghi lại ở đây để truy vết.\n\n" + "\n".join(credits) + "\n")
    print(f"\nĐã ghi nguồn vào media/pexels/NGUON.md ({len(credits)} mục)")
else:
    for tag, (kind, q) in QUERIES.items():
        print(f"\n### {tag} — {kind} — “{q}”")
        for r in search(kind, q):
            f = r["file"]
            if not f: continue
            print(f'  {{"name":"{tag}","kind":"{kind}","id":{r["id"]},"by":"{r["by"]}",'
                  f'"page":"{r["page"]}","link":"{f["link"]}"}}  # {r["w"]}x{r["h"]}'
                  + (f' {r["dur"]}s' if r["dur"] else ""))
