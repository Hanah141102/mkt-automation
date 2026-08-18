# -*- coding: utf-8 -*-
"""Sinh index.html (composition HyperFrames) từ bản mô tả 21 cảnh.

Chạy:  python3 build-index.py
Đọc:   media-manifest.json (thời lượng thật của từng cảnh, do build-assets.py tạo)
Ra:    index.html
"""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
MAN = json.load(open(f"{ROOT}/media-manifest.json"))
DUR = {f["id"]: f["duration"] for f in MAN["frames"]}

# thời điểm bắt đầu tuyệt đối của từng cảnh
ORDER = [f"f{i:02d}" for i in range(1, 22)]
START, t = {}, 0.0
for fid in ORDER:
    START[fid] = round(t, 3)
    t = round(t + DUR[fid], 3)
TOTAL = round(t, 3)

body, tl = [], []          # khối HTML · lệnh GSAP
def S(fid, off=0.0): return round(START[fid] + off, 3)

# ---------------------------------------------------------------- tiện ích HTML
def mask(txt, cls="", i=""):
    """Chữ dựng lên sau mặt nạ dòng — chỉ dùng transform, tua được."""
    return (f'<span class="mask {cls}" data-layout-allow-overlap="true">'
            f'<span class="mi"{i} data-layout-allow-overlap="true" '
            f'data-layout-allow-overflow="true">{txt}</span></span>')

def video(vid, src, fid, off=0.0, dur=None, wrap_style="", vid_style="", track=2):
    d = dur if dur is not None else DUR[fid] - off
    body.append(
        f'<div class="vwrap" id="w-{vid}" style="{wrap_style}">'
        f'<video id="v-{vid}" src="media/{src}" data-start="{S(fid,off)}" '
        f'data-duration="{round(d,3)}" data-track-index="{track}" '
        f'style="{vid_style}" muted playsinline></video></div>')

def scene(fid, inner, track):
    body.append(
        f'<div id="{fid}" class="clip scene" data-start="{START[fid]}" '
        f'data-duration="{DUR[fid]}" data-track-index="{track}">'
        f'<div class="stage" id="{fid}-stage">{inner}</div></div>')

def audio(fid, track):
    if DUR.get(fid) and os.path.exists(f"{ROOT}/media/{fid}.wav"):
        body.append(f'<audio id="a-{fid}" src="media/{fid}.wav" data-start="{START[fid]}" '
                    f'data-duration="{DUR[fid]}" data-track-index="{track}" data-volume="1"></audio>')

# ---------------------------------------------------------------- tiện ích GSAP
def rise(sel, at, stag=0.09, d=0.62, y=110):
    tl.append(f'tl.fromTo("{sel}",{{yPercent:{y}}},{{yPercent:0,duration:{d},'
              f'ease:"power3.out",stagger:{stag}}},{at});')

def fade(sel, at, d=0.5, y=26, stag=0.0):
    tl.append(f'tl.fromTo("{sel}",{{opacity:0,y:{y}}},{{opacity:1,y:0,duration:{d},'
              f'ease:"power2.out",stagger:{stag}}},{at});')

def pop(sel, at, stag=0.11, d=0.5):
    tl.append(f'tl.fromTo("{sel}",{{opacity:0,scale:0.84}},{{opacity:1,scale:1,duration:{d},'
              f'ease:"back.out(1.7)",stagger:{stag}}},{at});')

def kb(sel, at, d, a=1.0, b=1.07):
    tl.append(f'tl.fromTo("{sel}",{{scale:{a}}},{{scale:{b},duration:{d},ease:"none"}},{at});')

def grow(sel, at, d=0.7, stag=0.0):
    tl.append(f'tl.fromTo("{sel}",{{scaleX:0}},{{scaleX:1,duration:{d},'
              f'ease:"power2.out",stagger:{stag}}},{at});')

def dim(sel, at, to=0.32, d=0.7):
    tl.append(f'tl.to("{sel}",{{opacity:{to},duration:{d},ease:"power2.inOut"}},{at});')

def sfade(fid, d=0.4):
    """chồng mờ khi vào cảnh (dùng ở 4 mối ra/vào b-roll)"""
    tl.append(f'tl.fromTo("#{fid}-stage",{{opacity:0}},{{opacity:1,duration:{d},ease:"power1.out"}},{START[fid]});')

# ================================================================ NỀN
body.append(f'<div id="bg" class="clip" data-start="0" data-duration="{TOTAL}" '
            f'data-track-index="0"></div>')

# ================================================================ CÁC CẢNH
sc_track = lambda i: 5 + (i % 2)
vd_track = lambda i: 2 + (i % 2)
au_track = lambda i: 10 + (i % 2)

# ---- 01 · Chào -------------------------------------------------------------
i = 0
video("cam1", "f01_cam.mp4", "f01", wrap_style="", vid_style="", track=vd_track(i))
scene("f01", f"""
 <div class="rail">
   <div class="kick">{mask('BÀI THUYẾT TRÌNH')}</div>
   <h1 class="h1">{mask('NHẬT MINH')}</h1>
   <div class="ln" id="f01-ln"></div>
   <div class="sub">{mask('Lớp 3A05 · Vinschool Ocean Park')}</div>
 </div>""", sc_track(i))
audio("f01", au_track(i))
rise("#f01 .kick .mi", S("f01", 0.35))
rise("#f01 .h1 .mi", S("f01", 0.55), d=0.72)
grow("#f01-ln", S("f01", 1.05))
rise("#f01 .sub .mi", S("f01", 1.25))

# ---- 02 · Kỳ nghỉ hè -------------------------------------------------------
i = 1
video("px2", "pexels/f02_ban.mp4", "f02", wrap_style="z-index:1", track=vd_track(i))
video("cam2", "f02_cam.mp4", "f02", wrap_style="z-index:2", track=vd_track(i) + 4)
scene("f02", f"""
 <div class="tint t75"></div>
 <div class="rail">
   <div class="chip c1">Kỳ nghỉ hè dài</div>
   <div class="chip c2">Bố &amp; chú đồng hành</div>
   <div class="chip c3 on">Một phương pháp học mới</div>
 </div>""", sc_track(i))
audio("f02", au_track(i))
pop("#f02 .c1", S("f02", 0.9))
pop("#f02 .c2", S("f02", 3.5))
dim("#f02 .c1", S("f02", 3.5))
pop("#f02 .c3", S("f02", 6.4))
dim("#f02 .c2", S("f02", 6.4))

# ---- 03 · SECOND BRAIN -----------------------------------------------------
i = 2
video("e1", "e1.mp4", "f03", off=1.6, dur=DUR["f03"] - 1.6,
      wrap_style="z-index:1", track=vd_track(i))
video("cam3", "f03_cam.mp4", "f03", wrap_style="z-index:3", track=vd_track(i) + 4,
      vid_style="")
scene("f03", f"""
 <div class="tint" id="f03-tint"></div>
 <div class="mid">
   <h1 class="h0">{mask('SECOND BRAIN')}</h1>
   <div class="teal-label">{mask('bộ não thứ hai')}</div>
 </div>""", sc_track(i))
audio("f03", au_track(i))
tl.append(f'tl.fromTo("#w-cam3",{{scale:1,x:0,y:0}},{{scale:0.30,x:921,y:320,'
          f'duration:0.9,ease:"power3.inOut"}},{S("f03",1.5)});')
tl.append(f'tl.fromTo("#f03-tint",{{opacity:0}},{{opacity:1,duration:0.5,ease:"power1.out"}},{S("f03",1.5)});')
rise("#f03 .h0 .mi", S("f03", 2.0), d=0.8)
rise("#f03 .teal-label .mi", S("f03", 2.5))
kb("#w-e1 video", S("f03", 1.6), DUR["f03"] - 1.6, 1.0, 1.09)

# ---- 04 · Vấn đề -----------------------------------------------------------
i = 3
video("px4", "pexels/f04_sach.mp4", "f04", wrap_style="z-index:1", track=vd_track(i))
scene("f04", f"""
 <div class="tint t75"></div>
 <div class="wide">
   <div class="h2 dimtxt">{mask('Có những tuần em <b>học rất nhiều</b>…')}</div>
   <div class="h2 amber gap">{mask('…nhưng cuối tuần không nhớ')}{mask('mình đã tiến bộ ở đâu.')}</div>
   <div class="ul" id="f04-ul"></div>
 </div>""", sc_track(i))
audio("f04", au_track(i))
rise("#f04 .dimtxt .mi", S("f04", 0.25), d=0.7)
rise("#f04 .amber .mi", S("f04", 2.6), stag=0.12, d=0.7)
grow("#f04-ul", S("f04", 4.3), d=0.9)

# ---- 05 · MindMirror -------------------------------------------------------
i = 4
scene("f05", f"""
 <div class="win win-r" id="f05-win"><img src="media/ob_vault.jpg" alt=""></div>
 <div class="col-l">
   <div class="def d1">MindMirror</div>
   <div class="def d2">= Second Brain · bộ não thứ hai</div>
   <div class="def d3 on">= chiếc gương soi lại việc học mỗi ngày</div>
 </div>""", sc_track(i))
audio("f05", au_track(i))
fade("#f05-win", S("f05", 0.15), d=0.7, y=34)
kb("#f05-win img", S("f05", 0.15), DUR["f05"] - 0.15, 1.0, 1.08)
pop("#f05 .d1", S("f05", 0.7))
pop("#f05 .d2", S("f05", 2.5))
pop("#f05 .d3", S("f05", 4.6))

# ---- 06 · Ghi vài dòng -----------------------------------------------------
i = 5
scene("f06", f"""
 <div class="win win-r" id="f06-win"><img src="media/ob_daily_body.jpg" alt=""></div>
 <div class="col-l">
   <div class="eyebrow">{mask('MỖI NGÀY EM GHI VÀI DÒNG')}</div>
   <div class="qcard q1"><span class="n">1</span>Em học thêm gì?</div>
   <div class="qcard q2"><span class="n">2</span>Còn chưa hiểu gì?</div>
   <div class="qcard q3 on"><span class="n">3</span>Vận động, thể thao thế nào?</div>
 </div>""", sc_track(i))
audio("f06", au_track(i))
fade("#f06-win", S("f06", 0.15), d=0.7, y=34)
kb("#f06-win img", S("f06", 0.15), DUR["f06"] - 0.15, 1.0, 1.06)
rise("#f06 .eyebrow .mi", S("f06", 0.2))
pop("#f06 .q1", S("f06", 1.5))
pop("#f06 .q2", S("f06", 3.3))
pop("#f06 .q3", S("f06", 5.1))

# ---- 07 · Câu hỏi cho AI ---------------------------------------------------
i = 6
scene("f07", f"""
 <div class="mid mid-tight">
   <div class="eyebrow teal">{mask('CUỐI TUẦN EM HỎI AI TRONG SECOND BRAIN')}</div>
   <div class="bubble" id="f07-bub">Những việc tuần này có giúp em
     <span class="hl">tiến gần hơn tới người em muốn trở thành</span> không?</div>
   <img class="proof" src="media/s_prompt.jpg" alt="">
 </div>""", sc_track(i))
audio("f07", au_track(i))
rise("#f07 .eyebrow .mi", S("f07", 0.2))
pop("#f07-bub", S("f07", 1.4), d=0.6)
tl.append(f'tl.fromTo("#f07 .hl",{{backgroundColor:"rgba(242,188,87,0)"}},'
          f'{{backgroundColor:"rgba(242,188,87,0.55)",duration:0.7,ease:"power2.out"}},{S("f07",5.2)});')
fade("#f07 .proof", S("f07", 7.4), d=0.6, y=14)

# ---- 08 · AI đang đọc ------------------------------------------------------
i = 7
video("e2", "e2.mp4", "f08", wrap_style="z-index:1", track=vd_track(i))
scene("f08", f"""
 <div class="tint"></div>
 <div class="mid"><div class="status" id="f08-st">Đang đọc lại nhật ký
   <b>10/08 → 16/08</b>…</div></div>""", sc_track(i))
audio("f08", au_track(i))
sfade("f08", 0.35)
pop("#f08-st", S("f08", 0.3), d=0.5)

# ---- 09 · Có, nhưng chưa đủ ------------------------------------------------
i = 8
scene("f09", f"""
 <img class="bgimg full faint" src="media/s_answer_bg.jpg" alt=""><div class="scrim-full"></div>
 <div class="mid">
   <div class="eyebrow teal">{mask('AI TRẢ LỜI')}</div>
   <div class="duo">
     <div class="scard ok s1"><div class="bdg">✔</div><div class="st">ĐANG ĐI<br>ĐÚNG HƯỚNG</div></div>
     <div class="scard warn s2"><div class="bdg">⚠</div><div class="st">CHƯA ĐỦ<br>BẰNG CHỨNG</div></div>
   </div>
   <div class="cap">“…chưa đủ bằng chứng để nói em đã hoàn thành.”</div>
 </div>""", sc_track(i))
audio("f09", au_track(i))
rise("#f09 .eyebrow .mi", S("f09", 0.3))
pop("#f09 .s1", S("f09", 2.4), d=0.55)
pop("#f09 .s2", S("f09", 5.6), d=0.55)
fade("#f09 .cap", S("f09", 8.6), d=0.6, y=18)

# ---- 10/11/12 · Ba tiêu chí ------------------------------------------------
# cảnh nào có cửa sổ Obsidian thật chiếu bên phải
WINDOW = {
 "f10": '<div class="win win-r" id="f10-win"><img src="media/ob_frame_gpt.jpg" alt=""></div>',
 "f11": '<div class="win win-r" id="f11-win"><img src="media/ob_whybot.jpg" alt=""></div>',
}
CRIT = [
 ("f10", "01", "HAM HỌC", "ok", "✔",
  ['Đặt câu hỏi', 'Python', 'Robot', 'Tiếng Anh'], "…và nối chúng với nhau.", 1.2, 0.95),
 ("f11", "02", "DÙNG CÔNG NGHỆ TẠO ĐIỀU CÓ ÍCH", "ok", "✔", None, None, 1.0, 0.0),
 ("f12", "03", "KHỎE MẠNH", "warn", "⚠", None, None, 1.0, 0.0),
]
for k, (fid, num, label, kind, mark, chips, tailtxt, at0, stag) in enumerate(CRIT):
    i = 9 + k
    if chips:
        inner_extra = ('<div class="chiprow">' +
            "".join(f'<span class="cc cc{j}">{c}</span>' +
                    ('<span class="lnk lnk%d"></span>' % j if j < len(chips) - 1 else '')
                    for j, c in enumerate(chips)) +
            f'</div><div class="cap">{tailtxt}</div>')
    elif fid == "f11":
        inner_extra = ('<div class="bigchip" id="f11-bc">WhyBot</div>'
                       '<div class="strike" id="f11-sk">không chỉ dùng AI để lấy đáp án</div>')
    else:
        inner_extra = ('<div class="h2 amber" id="f12-tx">'
                       + mask('Tuần này chưa có ghi chép xác nhận')
                       + mask('về vận động hoặc bơi.') + '</div>')
    win = WINDOW.get(fid, "")
    back = ('<div class="tint t70"></div>' if fid == "f12" else
            '<img class="bgimg full faint" src="media/s_answer_bg.jpg" alt="">'
            '<div class="scrim-full"></div>')
    scene(fid, f"""
     {back}
     {win}
     <div class="{'col-l' if win else 'wide wide-top'}">
       <div class="tag {kind}"><span class="tnum">{num}</span>{label}<span class="tmark">{mark}</span></div>
       {inner_extra}
     </div>""", sc_track(i))
    audio(fid, au_track(i))
    pop(f"#{fid} .tag", S(fid, 0.25), d=0.5)

fade("#f10-win", S("f10", 0.9), d=0.7, y=34)
kb("#f10-win img", S("f10", 0.9), DUR["f10"] - 0.9, 1.0, 1.06)
fade("#f11-win", S("f11", 0.9), d=0.7, y=34)
kb("#f11-win img", S("f11", 0.9), DUR["f11"] - 0.9, 1.0, 1.06)
pop("#f10 .cc", S("f10", 1.6), stag=0.8, d=0.45)
grow("#f10 .lnk", S("f10", 2.15), d=0.4, stag=0.8)
tl.append('tl.set("#f10 .lnk",{transformOrigin:"left center"},0);')
fade("#f10 .cap", S("f10", 6.4), d=0.6, y=16)
pop("#f11-bc", S("f11", 3.4), d=0.6)
fade("#f11-sk", S("f11", 6.0), d=0.5, y=14)
tl.append(f'tl.fromTo("#f11-sk",{{color:"#93A4C4"}},{{color:"#697690",duration:0.6}},{S("f11",6.6)});')
rise("#f12-tx .mi", S("f12", 1.6), stag=0.12, d=0.7)

video("px12", "pexels/f12_boi.mp4", "f12", wrap_style="z-index:1", track=4)

# ---- 13 · AI không quyết định thay em --------------------------------------
i = 12
scene("f13", f"""
 <div class="mid">
   <h1 class="h0 tight">{mask('AI KHÔNG')}{mask('QUYẾT ĐỊNH THAY EM.')}</h1>
   <div class="ln wide-ln" id="f13-ln"></div>
   <div class="sub2">{mask('AI chỉ giúp em nhìn thấy điều cần cố gắng.')}</div>
 </div>""", sc_track(i))
audio("f13", au_track(i))
rise("#f13 .h0 .mi", S("f13", 0.2), stag=0.14, d=0.75)
grow("#f13-ln", S("f13", 1.5), d=0.8)
rise("#f13 .sub2 .mi", S("f13", 2.6), d=0.7)

# ---- 14 · Hai việc tuần mới ------------------------------------------------
i = 13
scene("f14", f"""
 <div class="mid">
   <div class="eyebrow">{mask('HAI VIỆC CHO TUẦN MỚI')}</div>
   <div class="duo">
     <div class="tile t1"><div class="th"><img src="media/ob_english.jpg" alt=""></div>
       <div class="tx"><span class="n">01</span><b>Mỗi ngày ôn 5 từ tiếng Anh</b><small>về giao tiếp</small></div></div>
     <div class="tile t2 on"><div class="th"><img src="media/ob_pygraph.jpg" alt=""></div>
       <div class="tx"><span class="n">02</span><b>Làm lại một bài tập hàm</b><small>trong Python</small></div></div>
   </div>
 </div>""", sc_track(i))
audio("f14", au_track(i))
rise("#f14 .eyebrow .mi", S("f14", 0.2))
pop("#f14 .t1", S("f14", 1.5), d=0.55)
pop("#f14 .t2", S("f14", 4.4), d=0.55)

# ---- 15 · Ba phẩm chất -----------------------------------------------------
i = 14
video("e3", "e3.mp4", "f15", off=0.0, wrap_style="z-index:1", track=vd_track(i))
scene("f15", f"""
 <div class="tint t60"></div>
 <div class="mid">
   <div class="eyebrow">{mask('EM MUỐN TRỞ THÀNH MỘT NGƯỜI')}</div>
   <div class="trio">
     <div class="pil p1">HAM HỌC</div>
     <div class="pil p2">KHỎE MẠNH</div>
     <div class="pil p3 on">DÙNG CÔNG NGHỆ<br>TẠO ĐIỀU CÓ ÍCH</div>
   </div>
 </div>""", sc_track(i))
audio("f15", au_track(i))
sfade("f15", 0.45)
kb("#w-e3 video", START["f15"], DUR["f15"], 1.0, 1.08)
rise("#f15 .eyebrow .mi", S("f15", 3.4))
pop("#f15 .p1", S("f15", 7.6), d=0.55)
pop("#f15 .p2", S("f15", 8.6), d=0.55)
pop("#f15 .p3", S("f15", 9.7), d=0.55)

# ---- 16 · Nhìn rõ ----------------------------------------------------------
i = 15
scene("f16", f"""
 <div class="mid">
   <h1 class="h1 flowline">{mask('NHÌN RÕ')}<span class="arw" id="f16-ar">→</span>{mask('CHỌN BƯỚC TIẾP THEO')}</h1>
 </div>""", sc_track(i))
audio("f16", au_track(i))
sfade("f16", 0.4)
rise("#f16 .mi", S("f16", 0.6), stag=0.55, d=0.7)
pop("#f16-ar", S("f16", 1.2), d=0.45)

# ---- 17 · Ý tưởng → hành động ----------------------------------------------
i = 16
video("e4", "e4.mp4", "f17", wrap_style="z-index:1", track=vd_track(i))
scene("f17", f"""
 <div class="tint t70"></div>
 <div class="mid">
   <div class="eyebrow teal">{mask('SỨC MẠNH CỦA SECOND BRAIN')}</div>
   <div class="flow2">
     <div class="fw f1">Ý TƯỞNG TRONG ĐẦU</div>
     <div class="arw2" id="f17-ar">→</div>
     <div class="fw f2 boxed">HÀNH ĐỘNG</div>
   </div>
 </div>""", sc_track(i))
audio("f17", au_track(i))
sfade("f17", 0.4)
kb("#w-e4 video", START["f17"], DUR["f17"], 1.0, 1.07)
rise("#f17 .eyebrow .mi", S("f17", 0.3))
fade("#f17 .f1", S("f17", 4.6), d=0.6, y=22)
pop("#f17-ar", S("f17", 5.6), d=0.45)
pop("#f17 .f2", S("f17", 6.2), d=0.55)

# ---- 18 · Người chọn vẫn là em ---------------------------------------------
i = 17
scene("f18", f"""
 <div class="kb kb-left" data-layout-allow-overflow="true"><img src="media/s_kid_smile.jpg" alt=""></div>
 <div class="rail">
   <h1 class="h1">{mask('NGƯỜI CHỌN')}{mask('VẪN LÀ <span class="box">EM</span>')}</h1>
   <div class="lvl" id="f18-lv">LEVEL UP ↑</div>
 </div>""", sc_track(i))
audio("f18", au_track(i))
kb("#f18 .kb img", START["f18"], DUR["f18"], 1.0, 1.06)
rise("#f18 .h1 .mi", S("f18", 0.8), stag=0.16, d=0.75)
pop("#f18-lv", S("f18", 5.6), d=0.6)

# ---- 19 · Lời chúc ---------------------------------------------------------
i = 18
video("px19", "pexels/f19_lop.mp4", "f19", off=0.2, dur=DUR["f19"] - 0.2,
      wrap_style="z-index:1", track=vd_track(i))
scene("f19", f"""
 <div class="tint t75"></div>
 <div class="kb kb-left" data-layout-allow-overflow="true"><img src="media/s_kid_calm.jpg" alt=""></div>
 <div class="rail">
   <div class="quiet" id="f19-q">“Em hy vọng cách học của em sẽ giúp nhiều bạn tìm ra
     phương pháp học mới và hiệu quả hơn trong thời đại số.”</div>
 </div>""", sc_track(i))
audio("f19", au_track(i))
kb("#f19 .kb img", START["f19"], DUR["f19"], 1.0, 1.05)
fade("#f19-q", S("f19", 1.2), d=0.9, y=30)

# ---- 20 · Cảm ơn -----------------------------------------------------------
i = 19
scene("f20", f"""
 <div class="mid">
   <h1 class="h1">{mask('CẢM ƠN MỌI NGƯỜI')}{mask('ĐÃ LẮNG NGHE')}</h1>
 </div>""", sc_track(i))
audio("f20", au_track(i))
rise("#f20 .mi", S("f20", 0.3), stag=0.14, d=0.7)

# ---- 21 · Thẻ kết ----------------------------------------------------------
i = 20
video("e5", "e5.mp4", "f21", wrap_style="z-index:1", track=vd_track(i))
scene("f21", f"""
 <div class="tint t75"></div>
 <div class="mid">
   <h1 class="h2 lock">{mask('SECOND BRAIN GIÚP EM')}{mask('LEVEL UP VIỆC HỌC')}</h1>
   <div class="ln wide-ln" id="f21-ln"></div>
   <div class="sub">Nhật Minh — Lớp 3A05, Vinschool Ocean Park</div>
   <div class="tiny">Dựng từ nhật ký học tập tháng 8/2026</div>
 </div>""", sc_track(i))
sfade("f21", 0.5)
rise("#f21 .lock .mi", S("f21", 0.4), stag=0.12, d=0.7)
grow("#f21-ln", S("f21", 1.3), d=0.7)
fade("#f21 .sub", S("f21", 1.7), d=0.6, y=18)
fade("#f21 .tiny", S("f21", 2.1), d=0.6, y=14)
tl.append(f'tl.to("#f21-stage",{{opacity:0,duration:0.7,ease:"power2.in"}},{S("f21",DUR["f21"]-0.75)});')

# ---- Ảnh thẻ của bé -------------------------------------------------------
# Hiện ở góc dưới phải suốt các cảnh KHÔNG có hình Nhật Minh (04→17 và 20→21),
# để người xem không quên đang nghe ai nói. Tắt ở 01–03, 18–19 vì đã thấy mặt bé.
for tag, a, b, tr in [("ava1", "f04", "f18", 8), ("ava2", "f20", None, 9)]:
    st = START[a]
    en = START[b] if b else TOTAL
    body.append(
        f'<div id="{tag}" class="clip ava" data-start="{st}" data-duration="{round(en-st,3)}" '
        f'data-track-index="{tr}" data-layout-allow-overlap="true">'
        f'<img class="avaimg" src="media/avatar.jpg" alt="">'
        f'<span class="avaname">Nhật Minh</span></div>')
    tl.append(f'tl.fromTo("#{tag} .avaimg",{{opacity:0,scale:0.7}},{{opacity:1,scale:1,'
              f'duration:0.55,ease:"back.out(1.7)"}},{round(st+0.35,3)});')
    tl.append(f'tl.fromTo("#{tag} .avaname",{{opacity:0,x:16}},{{opacity:1,x:0,'
              f'duration:0.45,ease:"power2.out"}},{round(st+0.7,3)});')

# ================================================================ CSS
# Be Vietnam Pro — bộ chữ dựng riêng cho tiếng Việt, dấu đặt gọn và không đè nhau.
# Nhúng thẳng từ media/fonts/ để bản dựng không phụ thuộc mạng.
FONTCSS = open(f"{ROOT}/media/fonts/be-vietnam-pro.css").read()
CSS = FONTCSS + """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1920px;height:1080px;overflow:hidden;background:#070B16}
body{font-family:'Be Vietnam Pro',sans-serif;color:#F2F5FC;-webkit-font-smoothing:antialiased}
#root{position:relative;width:1920px;height:1080px;overflow:hidden}
#bg{position:absolute;inset:0;background:
 radial-gradient(1200px 700px at 78% 18%,rgba(56,214,200,.09),transparent 60%),
 radial-gradient(900px 600px at 12% 82%,rgba(196,43,84,.10),transparent 62%),#070B16;z-index:0}
.vwrap{position:absolute;inset:0;z-index:1}
.vwrap video{position:absolute;width:1920px;height:1080px;object-fit:cover;left:0;top:0}
#w-cam1 video,#w-cam2 video{width:592px;height:1000px;object-fit:cover;left:132px;top:40px;
 border-radius:26px;box-shadow:0 40px 90px rgba(0,0,0,.6)}
#w-cam3{z-index:3}
#w-cam3 video{width:592px;height:1000px;object-fit:cover;left:132px;top:40px;
 border-radius:26px;box-shadow:0 40px 90px rgba(0,0,0,.6);border:6px solid rgba(242,245,252,.28)}
.scene{position:absolute;inset:0;z-index:5}
.stage{position:absolute;inset:0}
.tint{position:absolute;inset:0;background:rgba(7,11,22,.52)}
.tint.t60{background:rgba(7,11,22,.60)}
.tint.t70{background:rgba(7,11,22,.70)}
.tint.t75{background:rgba(7,11,22,.78)}

/* khung xương */
.rail{position:absolute;left:830px;right:110px;top:50%;transform:translateY(-50%)}
.rail-wide{left:330px;right:760px}
.mid{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;
 justify-content:center;text-align:center;padding:0 150px;gap:26px}
.mid-tight{gap:34px}
.wide{position:absolute;left:150px;right:150px;top:50%;transform:translateY(-50%)}
.wide-top{top:46%}
.wide-inset{left:400px}
.veil-r{position:absolute;right:0;top:0;width:1060px;height:1080px;background:rgba(7,11,22,.45)}
.scrim-full{position:absolute;inset:0;background:radial-gradient(1100px 720px at 50% 50%,rgba(7,11,22,.62),rgba(7,11,22,.90))}

/* chữ */
.mask{display:block;overflow:hidden;padding-top:.16em;padding-bottom:.12em}
.mi{display:block}
.h0{font-size:138px;font-weight:800;letter-spacing:-.024em;line-height:1.13}
.h0.tight{font-size:116px}
.h1{font-size:88px;font-weight:800;letter-spacing:-.02em;line-height:1.15}
.h2{font-size:58px;font-weight:700;letter-spacing:-.01em;line-height:1.32}
.kick{font-size:22px;font-weight:800;letter-spacing:.34em;color:#F2BC57;margin-bottom:14px}
.eyebrow{font-size:26px;font-weight:800;letter-spacing:.24em;color:#93A4C4}
.eyebrow.teal{color:#38D6C8}
.sub{font-size:30px;font-weight:500;color:#C6D2E8;letter-spacing:.03em;margin-top:16px}
.sub2{font-size:34px;font-weight:600;color:#93A4C4}
.tiny{font-size:20px;font-weight:500;color:#6E7E9E;letter-spacing:.06em}
.dimtxt{color:#9FB0CD}
.amber{color:#F2BC57}
.amber b,.dimtxt b{color:#F2F5FC;font-weight:900}
.gap{margin-top:18px}
.ln{height:5px;width:280px;background:#C42B54;border-radius:3px;margin-top:22px;
 transform-origin:left center;display:block}
.wide-ln{width:520px;margin:8px auto 0}
.ul{height:4px;width:760px;background:#F2BC57;border-radius:3px;margin-top:26px;
 transform-origin:left center;display:block}
.box,.boxed{background:#C42B54;padding:0 18px;border-radius:12px;display:inline-block}
.cap{font-size:28px;font-weight:500;color:#93A4C4;margin-top:26px;font-style:italic}

/* chip · thẻ */
.chip{display:inline-block;background:rgba(255,255,255,.06);border:2px solid #33415F;
 border-radius:46px;padding:18px 34px;font-size:34px;font-weight:650;color:#C7D3EA;margin-bottom:22px}
.chip.on{background:#C42B54;border-color:#C42B54;color:#fff;font-weight:800}
.def{background:rgba(10,16,30,.92);border:2px solid #35446A;border-left:7px solid #38D6C8;
 border-radius:14px;padding:22px 26px;font-size:38px;font-weight:750;margin-bottom:20px}
.def.d2,.def.d3{font-size:33px;font-weight:600;color:#C6D2E8}
.def.on{border-left-color:#F2BC57;color:#fff}
.qcard{background:rgba(10,16,30,.94);border:2px solid #35446A;border-radius:16px;
 padding:24px 28px;font-size:40px;font-weight:750;margin-top:22px}
.qcard.on{border-color:#F2BC57}
.qcard .n{display:block;font-size:20px;color:#38D6C8;font-weight:900;letter-spacing:.16em;margin-bottom:8px}
.teal-label{font-size:34px;font-weight:800;letter-spacing:.3em;color:#38D6C8;text-transform:uppercase}

/* bong bóng câu hỏi */
.bubble{background:#F2F4F8;color:#131A26;border-radius:30px;padding:38px 46px;font-size:44px;
 font-weight:600;max-width:1260px;line-height:1.46;text-align:left}
.hl{border-radius:6px;padding:0 6px}
.proof{width:900px;border-radius:10px;opacity:.42;border:1px solid #33415F}

/* trạng thái AI */
.status{background:rgba(10,16,30,.90);border:2px solid #38D6C8;border-radius:60px;
 padding:22px 52px;font-size:38px;font-weight:600;color:#CFF6F1}
.status b{color:#fff;font-weight:800}

/* thẻ đôi */
.duo{display:flex;gap:34px;justify-content:center;width:100%}
.scard{flex:1;max-width:520px;background:rgba(10,16,30,.94);border:2px solid #35446A;
 border-radius:20px;padding:40px 30px}
.scard.ok{border-color:#38D6C8}
.scard.warn{border-color:#F2BC57}
.scard.warn .st{color:#F2BC57}
.bdg{font-size:54px;margin-bottom:14px}
.st{font-size:42px;font-weight:800;line-height:1.26}
.tcard{flex:1;max-width:560px;background:rgba(10,16,30,.94);border:2px solid #35446A;
 border-radius:20px;padding:34px 32px;text-align:left}
.tcard.on{border-color:#F2BC57}
.tcard .n{display:block;font-size:22px;color:#38D6C8;font-weight:900;letter-spacing:.14em;margin-bottom:12px}
.tcard b{font-size:38px;font-weight:800;display:block;line-height:1.2}
.tcard small{display:block;font-size:26px;color:#93A4C4;font-weight:500;margin-top:8px}

/* nhãn tiêu chí */
.tag{display:inline-flex;align-items:center;gap:16px;border-radius:14px;padding:18px 30px;
 font-size:32px;font-weight:800;letter-spacing:.05em;line-height:1.25}
.tag.ok{background:rgba(56,214,200,.14);border:2px solid #38D6C8;color:#38D6C8}
.tag.warn{background:rgba(242,188,87,.14);border:2px solid #F2BC57;color:#F2BC57}
.tnum{font-family:"IBM Plex Mono",monospace;opacity:.8}
.tmark{font-size:30px}
.chiprow{display:flex;align-items:center;gap:14px;margin-top:40px;flex-wrap:wrap}
.cc{background:rgba(10,16,30,.94);border:2px solid #3A4A6E;border-radius:12px;
 padding:16px 24px;font-size:32px;font-weight:700}
.lnk{display:block;width:34px;height:3px;background:#38D6C8;transform-origin:left center}
.bigchip{display:block;width:max-content;background:#C42B54;border-radius:20px;padding:20px 50px;
 font-size:78px;font-weight:800;letter-spacing:-.012em;margin-top:36px;line-height:1.2}
.strike{display:block;font-size:32px;color:#93A4C4;text-decoration:line-through;margin-top:26px}

/* trụ cột */
.trio{display:flex;gap:26px;justify-content:center;width:100%}
.pil{flex:1;max-width:420px;background:rgba(10,16,30,.88);border:2px solid #38D6C8;
 border-radius:18px;padding:30px 18px;font-size:32px;font-weight:800;letter-spacing:.02em;line-height:1.32}
.pil.on{background:#38D6C8;color:#062120}

/* dòng chảy */
.flowline{display:flex;align-items:center;gap:34px;justify-content:center;flex-wrap:wrap}
.arw{color:#F2BC57;font-size:76px;display:inline-block}
.flow2{display:flex;align-items:center;gap:40px;justify-content:center;flex-wrap:wrap}
.fw{font-size:58px;font-weight:800;letter-spacing:-.012em;line-height:1.2}
.arw2{color:#F2BC57;font-size:82px;display:inline-block}
.lvl{margin-top:34px;color:#F2BC57;font-weight:900;font-size:44px;letter-spacing:.14em;display:inline-block}
.quiet{font-size:42px;font-weight:500;color:#D6E0F2;font-style:italic;line-height:1.54}
.lock{letter-spacing:.01em}

/* ảnh thẻ góc dưới phải */
.ava{position:absolute;right:0;bottom:0;left:auto;top:auto;width:100%;height:100%;
 pointer-events:none;z-index:8}
.avaimg{position:absolute;right:62px;bottom:58px;width:132px;height:132px;border-radius:50%;
 object-fit:cover;border:4px solid rgba(242,245,252,.92);box-shadow:0 18px 46px rgba(0,0,0,.8)}
.avaname{position:absolute;right:200px;bottom:92px;font-size:23px;font-weight:700;
 letter-spacing:.04em;color:#EDF1FA;white-space:nowrap;background:rgba(9,13,24,.88);
 border:1px solid rgba(242,245,252,.22);border-radius:22px;padding:8px 18px}

/* cửa sổ Obsidian thật — chiếu rõ, không phải nền mờ */
.win{position:absolute;border-radius:22px;overflow:hidden;background:#0A0F1E;
 border:2px solid rgba(242,245,252,.18);box-shadow:0 44px 110px rgba(0,0,0,.72)}
.win img{width:100%;height:100%;object-fit:cover;object-position:top left;display:block}
.win-r{right:78px;top:72px;width:1015px;height:940px}
.win-strip{right:78px;top:50%;transform:translateY(-50%);width:1015px;height:240px}
.col-l{position:absolute;left:104px;top:50%;transform:translateY(-50%);width:660px}

/* thẻ có ảnh minh hoạ */
.tile{flex:1;max-width:640px;background:rgba(10,16,30,.96);border:2px solid #35446A;
 border-radius:22px;overflow:hidden;text-align:left}
.tile.on{border-color:#F2BC57}
.th{height:300px;overflow:hidden}
.th img{width:100%;height:100%;object-fit:cover;display:block}
.tx{padding:26px 30px 30px}
.tile .n{display:block;font-size:22px;color:#38D6C8;font-weight:900;letter-spacing:.14em;margin-bottom:10px}
.tile b{font-size:35px;font-weight:700;display:block;line-height:1.3}
.tile small{display:block;font-size:26px;color:#93A4C4;font-weight:500;margin-top:8px}

/* ảnh nền */
.bgimg{position:absolute;object-fit:cover}
.bgimg.left-strip{left:0;top:0;width:262px;height:1080px;opacity:.42}
.strip-fade{position:absolute;left:0;top:0;width:400px;height:1080px;background:linear-gradient(90deg,rgba(7,11,22,0) 0%,rgba(7,11,22,.55) 55%,#070B16 100%)}
.bgimg.full{left:0;top:0;width:1920px;height:1080px}
.bgimg.faint{opacity:.30}
.bgimg.faint2{opacity:.32}
.kb{position:absolute;overflow:hidden}
.kb img{width:100%;height:100%;object-fit:cover;display:block}
.kb-right{right:0;top:0;width:1060px;height:1080px;opacity:.38}
.kb-left{left:0;top:0;width:700px;height:1080px}
.scrim-r{position:absolute;left:700px;top:0;width:520px;height:1080px;
 background:linear-gradient(90deg,#070B16 0%,rgba(7,11,22,.86) 55%,rgba(7,11,22,0) 100%)}
"""

# ================================================================ XUẤT FILE
# mỗi <img> phải có id riêng — trình dựng bơm khung hình theo getElementById,
# trùng id sẽ khiến ảnh render ra trắng trơn.
_n = [0]
def _uid(chunk):
    out = []
    for piece in chunk.split("<img "):
        if out:
            _n[0] += 1
            out.append(f'id="im{_n[0]}" ' + piece)
        else:
            out.append(piece)
    return "<img ".join(out)
body = [_uid(b) for b in body]

HTML = f"""<!doctype html>
<html lang="vi">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>Second Brain giúp em level up việc học — Nhật Minh</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>{CSS}</style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}"
         data-width="1920" data-height="1080" data-fps="30">
{chr(10).join("      " + b for b in body)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
{chr(10).join("      " + x for x in tl)}
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
open(f"{ROOT}/index.html", "w").write(HTML)
print(f"index.html — {len(ORDER)} cảnh · {TOTAL}s · {len(tl)} tween")
for fid in ORDER:
    print(f"  {fid}  bắt đầu {START[fid]:7.3f}  dài {DUR[fid]:6.3f}")
