# -*- coding: utf-8 -*-
"""Cắt khoảng lặng + chuẩn bị toàn bộ media cho composition HyperFrames.

Chạy:  python3 build-assets.py
Ra:    public/media/*.wav (tiếng từng cảnh), public/media/*.mp4 (hình), public/media/*.jpg (ảnh tĩnh)
       media-manifest.json (thời lượng thật của từng cảnh)
"""
import subprocess, json, os, sys

SRC = "/Users/tonyhoang/Documents/GitHub/mkt-automation/nhat minh"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = f"{ROOT}/media"
os.makedirs(OUT, exist_ok=True)

A = f"{SRC}/1.mp4"
B = f"{SRC}/ChatGPT - 15 August 2026.mp4"
C = f"{SRC}/Ghi nhớ tiến bộ học tập cuối tuần.mp4"
D = f"{SRC}/Second Brain giúp em level up học tập.mp4"
E = f"{SRC}/b-roll second brain hấp dẫn.mp4"

# ---------------------------------------------------------------- EDL
# (nguồn, [ (vào, ra), ... ])  — mốc giờ gốc, đã bỏ khoảng lặng >= 0,55s
FRAMES = [
 ("f01", A, [(0.000,1.655),(1.944,5.312)]),
 ("f02", A, [(6.637,15.478)]),
 ("f03", A, [(16.290,20.275),(21.247,24.100)]),
 ("f04", C, [(1.199,7.958)]),
 ("f05", D, [(12.314,15.491),(15.766,17.797),(18.171,19.255),(19.538,20.559)]),
 ("f06", D, [(21.248,22.630),(23.567,25.226),(25.557,26.979),(27.323,29.824),(30.193,31.224)]),
 ("f07", D, [(32.066,34.192),(34.913,36.942),(37.629,39.062),(39.442,40.601),(42.478,45.664)]),
 ("f08", D, [(46.280,48.648)]),
 ("f09", D, [(53.061,53.436),(53.701,55.212),(55.736,60.381),(60.698,61.637),(62.058,67.449)]),
 ("f10", D, [(67.840,68.658),(70.292,72.068),(73.137,77.470),(77.804,80.463)]),
 ("f11", D, [(81.905,86.194),(87.253,90.702),(90.986,91.497),(92.066,92.745)]),
 ("f12", D, [(93.849,95.034),(96.121,101.296),(101.550,102.444)]),
 ("f13", D, [(124.061,125.981),(126.616,127.446),(128.035,129.051),(129.437,132.745),(133.030,133.839)]),
 ("f14", D, [(136.604,140.258),(140.630,141.875),(142.577,143.288),(143.620,145.533)]),
 ("f15", D, [(146.873,148.801),(149.296,151.755),(152.315,153.205),(153.760,155.648),
             (155.982,157.693),(157.977,159.274),(160.095,161.723),(162.622,164.600)]),
 ("f16", D, [(164.600,169.103),(170.473,172.008),(172.269,173.635),(173.914,174.748)]),
 ("f17", D, [(175.002,177.340),(177.959,180.084),(180.847,181.831),(182.132,185.870),(186.447,187.277)]),
 ("f18", D, [(187.676,190.273),(190.728,192.537),(193.222,195.328),(195.603,196.628),
             (197.000,197.690),(198.624,199.412)]),
 ("f19", D, [(199.973,201.280),(201.542,206.085),(206.435,207.128),(208.469,210.219),(210.599,214.100)]),
 ("f20", D, [(214.100,219.126)]),
]
END_CARD = 5.0  # f21, không lời

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print("FAIL:", " ".join(cmd[:8]), "…\n", r.stderr[-1500:]); sys.exit(1)
    return r

def dur(path):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                                 "-of","csv=p=0",path], capture_output=True, text=True).stdout.strip())

# ---------------------------------------------------------------- TIẾNG
# Mỗi mảnh: fade 12ms hai đầu để không lụp bụp ở mối cắt, rồi nối lại,
# cuối cùng chuẩn hoá độ to về -16 LUFS cho ba nguồn thu nghe bằng nhau.
manifest = {"frames": []}
print("== Cắt tiếng ==")
for fid, src, segs in FRAMES:
    parts, filt = [], []
    for i,(a,b) in enumerate(segs):
        filt.append(f"[0:a]atrim=start={a}:end={b},asetpts=PTS-STARTPTS,"
                    f"afade=t=in:st=0:d=0.012,afade=t=out:st={max(0,(b-a)-0.012):.4f}:d=0.012[a{i}]")
        parts.append(f"[a{i}]")
    chain = ";".join(filt) + ";" + "".join(parts) + f"concat=n={len(segs)}:v=0:a=1[cat];"
    chain += "[cat]loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000[out]"
    dst = f"{OUT}/{fid}.wav"
    run(["ffmpeg","-y","-v","error","-i",src,"-filter_complex",chain,"-map","[out]",
         "-ac","2","-c:a","pcm_s16le",dst])
    d = dur(dst)
    manifest["frames"].append({"id":fid,"audio":f"media/{fid}.wav","duration":round(d,3)})
    print(f"  {fid}  {d:6.3f}s  ({len(segs)} mảnh)")

manifest["frames"].append({"id":"f21","audio":None,"duration":END_CARD})

# ---------------------------------------------------------------- HÌNH: talking head
# 1.mp4 cắt cùng mốc với tiếng để khớp khẩu hình. Không lấy tiếng (tiếng đã ở file wav).
print("== Cắt hình talking head ==")
for fid, src, segs in FRAMES[:3]:
    filt, parts = [], []
    for i,(a,b) in enumerate(segs):
        filt.append(f"[0:v]trim=start={a}:end={b},setpts=PTS-STARTPTS[v{i}]")
        parts.append(f"[v{i}]")
    chain = ";".join(filt)+";"+"".join(parts)+f"concat=n={len(segs)}:v=1:a=0[cv];"
    chain += "[cv]scale=608:1080:flags=lanczos,fps=30[out]"
    run(["ffmpeg","-y","-v","error","-i",src,"-filter_complex",chain,"-map","[out]",
         "-an","-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p",
         f"{OUT}/{fid}_cam.mp4"])
    print(f"  {fid}_cam.mp4")

# ---------------------------------------------------------------- HÌNH: b-roll graph
print("== Cắt b-roll ==")
BROLL = [("e1",0.0,5.2),("e2",5.8,8.6),("e3",7.6,14.2),("e4",13.4,18.1),("e5",12.6,18.1)]
for name,a,b in BROLL:
    run(["ffmpeg","-y","-v","error","-ss",str(a),"-to",str(b),"-i",E,
         "-vf","crop=1520:855:392:112,scale=1920:1080:flags=lanczos,fps=30","-an",
         "-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p",f"{OUT}/{name}.mp4"])
    print(f"  {name}.mp4  {b-a:.1f}s")

# ---------------------------------------------------------------- ẢNH TĨNH
# Màn hình desktop trong bản thu gần như đứng yên suốt bài (scene-change = 0),
# nên dùng ảnh tĩnh sắc nét thay vì video — nhẹ hơn và Ken Burns mượt hơn.
print("== Cắt ảnh tĩnh màn hình ==")
STILLS = [
  ("s_note",   D, 60, "crop=1201:1316:161:46,scale=986:-1"),                 # note Obsidian
  ("s_side",   D, 60, "crop=300:1240:0:150,scale=-1:1080"),                   # sidebar Daily Notes
  ("s_answer", D, 60, "crop=1000:560:1680:820,scale=1400:-1"),                # câu trả lời AI
  ("s_prompt", D, 60, "crop=700:130:1860:660,scale=1400:-1"),                 # bong bóng câu hỏi
  ("s_python", D, 60, "crop=700:230:340:1140,scale=1400:-1"),                 # Level 4 — Python Hàm
  ("s_desk",   D, 60, "scale=1920:-1"),                                       # toàn màn hình
  ("s_english",B,  8, "crop=1100:1100:300:120,scale=1080:-1"),                # graph MOC Tiếng Anh
  ("s_graph",  C, 45, "crop=1300:1300:330:80,scale=1080:-1"),                 # graph sáng
]
for name, src, t, vf in STILLS:
    run(["ffmpeg","-y","-v","error","-ss",str(t),"-i",src,"-vframes","1","-vf",vf,
         "-q:v","2",f"{OUT}/{name}.jpg"])
    print(f"  {name}.jpg")

# ảnh thẻ của bé — hiện ở góc dưới phải mọi cảnh KHÔNG có hình Nhật Minh
run(["ffmpeg","-y","-v","error","-i",f"{SRC}/minh avatar.jpg","-vframes","1",
     "-vf","crop=820:820:190:70,scale=400:400:flags=lanczos","-q:v","2",f"{OUT}/avatar.jpg"])
print("  avatar.jpg")

# chân dung tĩnh cho cảnh 18-19 (bé đang im lặng, không lệch khẩu hình)
for name, t in [("s_kid_smile",23.80),("s_kid_calm",6.30),("s_kid_look",16.00)]:
    run(["ffmpeg","-y","-v","error","-ss",str(t),"-i",A,"-vframes","1",
         "-vf","scale=608:-1:flags=lanczos","-q:v","2",f"{OUT}/{name}.jpg"])
    print(f"  {name}.jpg")

# Ảnh chụp màn hình đều là giao diện NỀN SÁNG. HyperFrames đặt style nội tuyến lên <img>
# nên filter/opacity trong CSS không ăn — nung thẳng độ tối vào file ảnh cho chắc.
print("== Hạ sáng ảnh nền ==")
for name, br, sat in [("s_side",-0.34,0.55),("s_note",-0.30,0.60),
                      ("s_answer",-0.36,0.50),("s_english",-0.38,0.50),("s_python",-0.30,0.60)]:
    run(["ffmpeg","-y","-v","error","-i",f"{OUT}/{name}.jpg",
         "-vf",f"eq=brightness={br}:saturation={sat}:contrast=0.92","-q:v","3",
         f"{OUT}/{name}_bg.jpg"])
    print(f"  {name}_bg.jpg")

# ---------------------------------------------------------------- ẢNH OBSIDIAN THẬT
# 4 ảnh chụp bố cung cấp (độ phân giải cao, giao diện sáng) — cắt thành panel để
# CHIẾU RÕ trong khung, không dùng làm nền mờ nữa.
print("== Cắt panel Obsidian ==")
P1  = f"{ROOT}/nhat minh brain 1.png"
PNK = f"{ROOT}/nhat minh brain nhat ky.png"
PGP = f"{ROOT}/nhat minh brain chatgpt.png"
PPY = f"{ROOT}/nhat minh brain python.png"
PANELS = [
  ("ob_vault",     P1,  "crop=1803:1256:40:0,scale=1500:-1"),          # toàn cửa sổ vault
  ("ob_daily",     PNK, "crop=1438:1263:40:0,scale=1400:-1"),          # toàn cửa sổ nhật ký
  ("ob_daily_body",PNK, "crop=1048:815:430:85,scale=1300:-1"),         # thân note 2026-08-16
  ("ob_sidebar",   PNK, "crop=360:790:40:80,scale=-1:1040"),           # danh sách Daily Notes
  ("ob_frame_gpt", PGP, "crop=1014:760:430:365,scale=1300:-1"),        # khung Tự nghĩ → Dạy lại
  ("ob_evidence",  PNK, "crop=1048:210:430:975,scale=1300:-1"),        # mục Bằng chứng cần lưu
  ("ob_pygraph",   PPY, "crop=1600:1190:415:60,scale=1400:-1"),        # graph MOC Python
  ("ob_whybot",    f"{SRC}/app whybot.png",
                        "crop=1526:810:415:190,scale=1400:-1"),         # note WhyBot
  ("ob_english",   f"{SRC}/minh brain tieng anh thuc hanh.png",
                        "crop=1120:760:800:350,scale=1400:-1"),          # graph MOC Tiếng Anh
]
for name, src, vf in PANELS:
    run(["ffmpeg","-y","-v","error","-i",src,"-vframes","1",
         "-vf",vf + ",eq=brightness=-0.05:saturation=0.94","-q:v","2",f"{OUT}/{name}.jpg"])
    print(f"  {name}.jpg")

total = sum(f["duration"] for f in manifest["frames"])
manifest["total"] = round(total,3)
json.dump(manifest, open(f"{ROOT}/media-manifest.json","w"), ensure_ascii=False, indent=1)
print(f"\nTỔNG THỜI LƯỢNG = {total:.2f}s = {int(total)//60}:{total%60:05.2f}")
