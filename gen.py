#!/usr/bin/env python3
"""Generates the wireframe screens (build/screens/*.html) and the entry board (build/entries/entry-1.html)
from one shared grayscale component kit. Run: python3 build/gen.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">'

ORANGE = "#F7993F"
ORANGE_SOFT = "#FFDDBE"

KIT = """
*{box-sizing:border-box;margin:0;padding:0}
.phone{width:390px;height:844px;background:#fff;border-radius:46px;border:3px solid #1b1b1b;overflow:hidden;position:relative;font-family:Inter,system-ui,sans-serif;color:#111;display:flex;flex-direction:column;-webkit-font-smoothing:antialiased}
.status{height:46px;flex:none;display:flex;justify-content:space-between;align-items:flex-end;padding:0 30px 8px;font-size:14px;font-weight:600}
.status .ic{display:flex;gap:5px;align-items:center}
.topbar{display:flex;gap:10px;padding:6px 16px 10px;flex:none}
.city{background:#ececec;border-radius:14px;padding:0 14px;height:40px;display:flex;align-items:center;font-weight:700;font-size:16px;gap:8px;white-space:nowrap}
.search{flex:1;background:#ececec;border-radius:14px;height:40px;display:flex;align-items:center;padding:0 14px;color:#7a7a7a;font-size:14px;gap:8px;white-space:nowrap}
.video{margin:0 16px;height:216px;border-radius:18px;background:#555;position:relative;overflow:hidden;flex:none;color:#fff}
.video svg.scene{position:absolute;inset:0;width:100%;height:100%}
.vtitle{position:absolute;left:16px;top:14px;font-size:19px;font-weight:700;text-shadow:0 1px 6px rgba(0,0,0,.5)}
.bigplay{position:absolute;left:50%;top:50%;width:62px;height:62px;margin:-31px 0 0 -31px;border-radius:50%;background:rgba(20,20,20,.85);display:flex;align-items:center;justify-content:center}
.ctrls{position:absolute;left:0;right:0;bottom:0;padding:22px 14px 11px;display:flex;align-items:center;gap:9px;font-size:11.5px;font-weight:500;background:linear-gradient(transparent,rgba(0,0,0,.65))}
.ctrls .t{white-space:nowrap;letter-spacing:.2px}
.scrub{flex:1;height:4px;background:rgba(255,255,255,.38);border-radius:2px;position:relative}
.scrub .fill{height:100%;background:#fff;border-radius:2px}
.scrub .mk{position:absolute;top:-3px;width:10px;height:10px;border-radius:50%;background:#fff;border:2px solid #2b2b2b;transform:translateX(-50%)}
.scrub .mk.cur{background:ORANGE;border-color:#fff;width:14px;height:14px;top:-5px;box-shadow:0 0 0 4px rgba(247,153,63,.4)}
.scrub .tk{position:absolute;top:-2px;width:3px;height:8px;border-radius:2px;background:ORANGE;transform:translateX(-50%)}
.scrub .head{position:absolute;top:-4px;width:12px;height:12px;border-radius:50%;background:#fff;transform:translateX(-50%)}
.cc{border:1.5px solid #fff;border-radius:4px;font-size:9px;font-weight:700;padding:1px 4px}
.chip{position:absolute;left:12px;bottom:48px;background:#fff;color:#111;border-radius:999px;padding:6px 14px 6px 6px;display:flex;align-items:center;gap:8px;font-weight:600;font-size:13px;box-shadow:0 6px 18px rgba(0,0,0,.45)}
.chip .ring{width:28px;height:28px;flex:none}
.chip small{display:block;font-size:10px;font-weight:500;color:#666}
.rail{padding:16px 16px 0;flex:none;position:relative}
.rail .line{position:absolute;left:36px;right:36px;top:24px;height:2.5px;background:#8a8a8a}
.rail .nodes{display:flex;justify-content:space-between;position:relative}
.rail .nd{display:flex;flex-direction:column;align-items:center;width:59px;gap:7px}
.rail .dot{width:17px;height:17px;border-radius:50%;background:#fff;border:2.5px solid #666}
.rail .nd.cur .dot{width:22px;height:22px;margin:-2.5px 0;border-color:ORANGE;background:ORANGE;box-shadow:0 0 0 3px #fff,0 0 0 5px ORANGE_SOFT}
.rail .lb{font-size:10.5px;color:#222;font-weight:500;white-space:nowrap}
.rail .nd.cur .lb{background:ORANGE_SOFT;border-radius:999px;padding:2px 6px;font-weight:700;margin-top:-2px}
.rail .nd.done .dot{background:#8a8a8a;border-color:#8a8a8a}
.hint{text-align:center;color:#8a8a8a;font-size:12px;font-weight:500;padding:8px 0 0}
.sec{padding:14px 16px 0;flex:1;min-height:0}
.sech{display:flex;align-items:baseline;justify-content:space-between;margin-bottom:8px}
.sech h3{font-size:15px;font-weight:700}
.sech span{font-size:11.5px;color:#7a7a7a;font-weight:500}
.topic{display:flex;align-items:center;gap:10px;height:50px;border-bottom:1px solid #e6e6e6;font-size:14px}
.topic .ts{font-variant-numeric:tabular-nums;color:#555;font-size:12.5px;width:36px;font-weight:600}
.topic .nm{flex:1;font-weight:500}
.topic .bar{width:3px;height:30px;border-radius:2px;background:transparent;margin-left:-4px}
.topic.now .bar{background:ORANGE}
.topic.now .nm{font-weight:700}
.topic .pill{font-size:10.5px;font-weight:700;background:ORANGE_SOFT;padding:3px 8px;border-radius:999px}
.topic .pill.read{background:#e6e6e6;color:#444}
.topic .inf{width:26px;height:26px;border-radius:50%;border:1.5px solid #bdbdbd;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#555}
.upnext{margin-top:12px;background:#f3f3f3;border-radius:14px;padding:8px 10px 8px 8px;display:flex;align-items:center;gap:10px}
.upnext .th{width:64px;height:42px;border-radius:8px;overflow:hidden;position:relative;flex:none;background:#777}
.upnext .th svg{position:absolute;inset:0;width:100%;height:100%}
.upnext .tx{flex:1;min-width:0}
.upnext .tx small{display:block;font-size:10.5px;color:#777;font-weight:700;text-transform:uppercase;letter-spacing:.6px}
.upnext .tx b{display:block;font-size:13px;font-weight:700;margin-top:1px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.upnext .tx span{display:block;font-size:11.5px;color:#555;margin-top:1px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.upnext .pv{font-size:11px;font-weight:700;border:1.5px solid #bbb;border-radius:999px;padding:5px 9px;background:#fff;white-space:nowrap}
.nav{height:84px;flex:none;border-top:1px solid #e3e3e3;display:flex;padding:8px 12px 0;background:#fff}
.nav div{flex:1;display:flex;flex-direction:column;align-items:center;gap:4px;font-size:12px;font-weight:500;color:#333;padding:7px 0 4px;border-radius:14px}
.nav div.on{background:ORANGE_SOFT;font-weight:700}
.home{position:absolute;bottom:9px;left:50%;width:134px;height:5px;background:#111;border-radius:3px;transform:translateX(-50%)}
/* mini player + sheet */
.mini{margin:4px 16px 0;height:74px;background:#1e1e1e;border-radius:16px;display:flex;align-items:center;gap:10px;padding:8px 10px 8px 8px;color:#fff;flex:none}
.mini .th{width:92px;height:58px;border-radius:10px;overflow:hidden;position:relative;flex:none;background:#555}
.mini .th svg{position:absolute;inset:0;width:100%;height:100%}
.mini .tx{flex:1;min-width:0}
.mini .tx b{display:block;font-size:14px;font-weight:700}
.mini .tx span{display:block;font-size:11.5px;color:#b5b5b5;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mini .pb{height:3px;background:#555;border-radius:2px;margin-top:7px;position:relative}
.mini .pb i{position:absolute;left:0;top:0;height:100%;width:28.3%;background:ORANGE;border-radius:2px}
.mini .play{width:42px;height:42px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.sheet{margin-top:10px;background:#f3f3f3;border-radius:28px 28px 0 0;padding:8px 16px 0;flex:1;position:relative;overflow:hidden;display:flex;flex-direction:column}
.handle{width:44px;height:5px;background:#bdbdbd;border-radius:3px;margin:0 auto 10px}
.crumb{font-size:12px;color:#7a7a7a;font-weight:500;display:flex;align-items:center;gap:6px}
.crumb b{color:#333}
.sh{display:flex;justify-content:space-between;align-items:flex-start;gap:10px;margin-top:4px}
.sh h1{font-size:26px;font-weight:800;line-height:1.1;letter-spacing:-.3px}
.sh p{font-size:13px;color:#555;margin-top:4px;font-weight:500}
.tag{background:ORANGE_SOFT;border-radius:999px;padding:5px 10px;font-size:11.5px;font-weight:700;white-space:nowrap;margin-top:4px}
.seg{display:flex;background:#e2e2e2;border-radius:12px;padding:3px;margin-top:12px}
.seg div{flex:1;text-align:center;padding:7px 0;font-size:12.5px;font-weight:600;border-radius:10px;color:#666}
.seg div.on{background:#fff;color:#111;box-shadow:0 1px 3px rgba(0,0,0,.15)}
.seg div.on i{display:inline-block;width:6px;height:6px;border-radius:50%;background:ORANGE;margin-right:5px;vertical-align:1px}
.para{font-size:13.5px;line-height:1.5;color:#333;margin-top:12px}
.para a{color:#111;font-weight:700;border-bottom:2px solid ORANGE;text-decoration:none}
.lbl{font-size:14px;font-weight:700;margin-top:14px}
.ev{display:flex;gap:8px;margin-top:8px;flex-wrap:wrap}
.ev span{background:#e4e4e4;border-radius:999px;padding:7px 12px;font-size:12.5px;font-weight:500}
.acc{background:#fff;border:1.5px solid #d9d9d9;border-radius:14px;padding:0 14px;height:52px;display:flex;align-items:center;gap:10px;font-weight:700;font-size:15px;margin-top:8px}
.acc .sp{flex:1}
.acc .cnt{font-size:11.5px;color:#7a7a7a;font-weight:600}
.accopen{background:#fff;border:1.5px solid #d9d9d9;border-radius:14px;margin-top:8px;overflow:hidden}
.accopen .hd{padding:0 14px;height:48px;display:flex;align-items:center;gap:10px;font-weight:700;font-size:15px;border-bottom:1px solid #ececec}
.accopen .hd .sp{flex:1}
.place{display:flex;align-items:center;gap:10px;padding:9px 14px;border-bottom:1px solid #f0f0f0;font-size:13px}
.place:last-child{border-bottom:0}
.place .nm{flex:1;min-width:0}
.place .nm b{display:block;font-weight:600}
.place .nm span{font-size:11.5px;color:#777}
.jump{display:inline-flex;align-items:center;gap:4px;border:1.5px solid #ccc;border-radius:999px;padding:4px 8px 4px 6px;font-size:11px;font-weight:700;white-space:nowrap;background:#fafafa}
.jump i{width:0;height:0;border-left:7px solid #111;border-top:4.5px solid transparent;border-bottom:4.5px solid transparent}
.map{height:96px;background:#e3e3e3;position:relative;overflow:hidden}
.map svg{position:absolute;inset:0;width:100%;height:100%}
.map .cap{position:absolute;left:10px;bottom:7px;font-size:11px;font-weight:700;background:#fff;padding:2px 7px;border-radius:999px}
.footer{position:absolute;left:16px;right:16px;bottom:30px;display:flex;gap:10px}
.resume{flex:1;height:54px;background:#111;color:#fff;border-radius:16px;display:flex;align-items:center;justify-content:center;gap:10px;font-weight:700;font-size:16px}
.resume small{font-weight:500;opacity:.75;font-size:12px}
.sq{width:54px;height:54px;border-radius:16px;border:1.5px solid #cfcfcf;background:#fff;display:flex;align-items:center;justify-content:center}
.fade{position:absolute;left:0;right:0;bottom:0;height:120px;background:linear-gradient(rgba(243,243,243,0),#f3f3f3 55%);pointer-events:none}
.toast{position:absolute;left:12px;right:12px;bottom:50px;background:#fff;color:#111;border-radius:12px;padding:9px 12px;font-size:12.5px;font-weight:600;display:flex;align-items:center;gap:8px;box-shadow:0 6px 18px rgba(0,0,0,.4)}
.toast .ok{width:20px;height:20px;border-radius:50%;background:ORANGE;display:flex;align-items:center;justify-content:center;flex:none}
.toast small{font-weight:500;color:#666;margin-left:auto}
/* chapters */
.chh{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px}
.chh h2{font-size:20px;font-weight:800}
.tog{display:flex;align-items:center;gap:7px;font-size:11.5px;font-weight:600;color:#444}
.tog i{width:34px;height:20px;border-radius:999px;background:ORANGE;position:relative;display:inline-block}
.tog i:after{content:"";position:absolute;right:2px;top:2px;width:16px;height:16px;border-radius:50%;background:#fff}
.ch{display:flex;align-items:center;gap:10px;padding:7px 10px;border-radius:14px;margin:0 -4px}
.ch .th{width:50px;height:34px;border-radius:8px;background:#cfcfcf;position:relative;overflow:hidden;flex:none}
.ch .th svg{position:absolute;inset:0;width:100%;height:100%}
.ch .tx{flex:1;min-width:0}
.ch .tx b{font-size:13.5px;display:flex;justify-content:space-between;align-items:center}
.ch .tx b span{font-size:11px;color:#777;font-weight:600;font-variant-numeric:tabular-nums}
.ch .tx small{display:block;font-size:11px;color:#777;margin-top:1px}
.ch .pr{height:3px;background:#ddd;border-radius:2px;margin-top:5px;position:relative}
.ch .pr i{position:absolute;left:0;top:0;height:100%;background:#8a8a8a;border-radius:2px}
.ch.cur{background:#fff;border:1.5px solid ORANGE}
.ch.cur .pr i{background:ORANGE}
.ch .st{font-size:10.5px;font-weight:700;background:ORANGE_SOFT;padding:3px 8px;border-radius:999px}
.ch .st.done{background:#e4e4e4;color:#444}
.ch .st.off{background:transparent;color:#999;border:1.5px solid #ddd}
.dim{position:absolute;inset:0;background:rgba(0,0,0,.22)}
""".replace("ORANGE_SOFT", ORANGE_SOFT).replace("ORANGE", ORANGE)

# ---------- SVG parts ----------
def scene(w=358, h=216, title=True):
    return f'''<svg class="scene" viewBox="0 0 358 216" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6e6e6e"/><stop offset="1" stop-color="#a3a3a3"/></linearGradient>
<linearGradient id="wat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7d7d7d"/><stop offset="1" stop-color="#4f4f4f"/></linearGradient></defs>
<rect width="358" height="216" fill="url(#sky)"/>
<path d="M0 118 L40 96 L80 108 L120 84 L160 100 L200 92 L240 104 L280 90 L320 100 L358 92 L358 150 L0 150Z" fill="#7b7b7b"/>
<path d="M0 132 L50 118 L90 128 L140 112 L190 126 L230 118 L270 128 L300 122 L358 130 L358 160 L0 160Z" fill="#5f5f5f"/>
<g fill="#383838"><path d="M258 150 L258 92 L266 78 L268 60 L272 50 L274 42 L277 38 L280 42 L282 50 L286 60 L288 78 L296 92 L296 150Z"/><rect x="236" y="118" width="20" height="32" rx="2"/><path d="M234 118 L246 102 L258 118Z"/><rect x="302" y="112" width="28" height="38" rx="2"/><path d="M300 112 L316 94 L332 112Z"/></g>
<g fill="#4a4a4a"><rect x="220" y="150" width="138" height="6"/><rect x="214" y="156" width="144" height="6"/><rect x="208" y="162" width="150" height="6"/><rect x="202" y="168" width="156" height="6"/></g>
<rect y="174" width="358" height="42" fill="url(#wat)"/>
<g stroke="#9a9a9a" stroke-width="1" opacity=".5"><line x1="20" y1="184" x2="120" y2="184"/><line x1="60" y1="196" x2="200" y2="196"/><line x1="150" y1="206" x2="320" y2="206"/></g>
<g fill="#454545"><circle cx="34" cy="150" r="18"/><circle cx="60" cy="156" r="14"/><circle cx="14" cy="160" r="12"/><rect x="31" y="160" width="6" height="16"/></g>
</svg>'''

def icon(name, size=22, color="#111"):
    s = {
        "search": '<circle cx="10" cy="10" r="6.5" fill="none" stroke="C" stroke-width="2"/><path d="M15 15l5 5" stroke="C" stroke-width="2" stroke-linecap="round"/>',
        "chev": '<path d="M6 9l6 6 6-6" fill="none" stroke="C" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
        "chevr": '<path d="M9 6l6 6-6 6" fill="none" stroke="C" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
        "play": '<path d="M8 5l12 7-12 7z" fill="C"/>',
        "pause": '<rect x="6" y="5" width="4" height="14" rx="1" fill="C"/><rect x="14" y="5" width="4" height="14" rx="1" fill="C"/>',
        "full": '<path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5" fill="none" stroke="C" stroke-width="2" stroke-linecap="round"/>',
        "pin": '<path d="M12 22s7-7.2 7-12.5A7 7 0 0 0 5 9.5C5 14.8 12 22 12 22z" fill="C"/><circle cx="12" cy="9.5" r="2.6" fill="#fff"/>',
        "people": '<circle cx="9" cy="8" r="3.5" fill="C"/><circle cx="16.5" cy="9" r="2.8" fill="C"/><path d="M2.5 19c0-3.6 2.9-6 6.5-6s6.5 2.4 6.5 6z" fill="C"/><path d="M14.5 13.4c.6-.2 1.3-.4 2-.4 2.9 0 5 2 5 5h-5.2" fill="C"/>',
        "doc": '<path d="M6 3h8l4 4v14H6z" fill="none" stroke="C" stroke-width="2" stroke-linejoin="round"/><path d="M9 12h6M9 16h6" stroke="C" stroke-width="2" stroke-linecap="round"/>',
        "book": '<path d="M6 3h12v18l-6-4-6 4z" fill="none" stroke="C" stroke-width="2" stroke-linejoin="round"/>',
        "bookf": '<path d="M6 3h12v18l-6-4-6 4z" fill="C"/>',
        "timeline": '<path d="M3 12h18" stroke="C" stroke-width="2"/><circle cx="6" cy="12" r="2.6" fill="C"/><circle cx="12" cy="12" r="2.6" fill="#fff" stroke="C" stroke-width="2"/><circle cx="18" cy="12" r="2.6" fill="#fff" stroke="C" stroke-width="2"/>',
        "stories": '<rect x="4" y="5" width="16" height="14" rx="2.5" fill="none" stroke="C" stroke-width="2"/><path d="M8 10h8M8 14h5" stroke="C" stroke-width="2" stroke-linecap="round"/>',
        "check": '<path d="M5 12.5l4.5 4.5L19 8" fill="none" stroke="C" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>',
        "x": '<path d="M6 6l12 12M18 6L6 18" stroke="C" stroke-width="2.2" stroke-linecap="round"/>',
        "list": '<path d="M4 7h16M4 12h16M4 17h10" stroke="C" stroke-width="2.2" stroke-linecap="round"/>',
        "expand": '<path d="M14 4h6v6M20 4l-7 7M10 20H4v-6M4 20l7-7" fill="none" stroke="C" stroke-width="2" stroke-linecap="round"/>',
    }[name].replace('"C"', f'"{color}"')
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">{s}</svg>'

STATUS = f'''<div class="status"><span>9:41</span><span class="ic">
<svg width="17" height="12" viewBox="0 0 17 12"><rect x="0" y="8" width="3" height="4" rx=".8" fill="#111"/><rect x="4.5" y="5.5" width="3" height="6.5" rx=".8" fill="#111"/><rect x="9" y="3" width="3" height="9" rx=".8" fill="#111"/><rect x="13.5" y="0" width="3" height="12" rx=".8" fill="#111"/></svg>
<svg width="16" height="12" viewBox="0 0 16 12"><path d="M8 11.5L1 4.5a9.6 9.6 0 0 1 14 0z" fill="#111"/></svg>
<svg width="26" height="12" viewBox="0 0 26 12"><rect x=".5" y=".5" width="21" height="11" rx="3" fill="none" stroke="#111"/><rect x="2" y="2" width="18" height="8" rx="1.8" fill="#111"/><rect x="23" y="4" width="2" height="4" rx="1" fill="#111"/></svg></span></div>'''

TOPBAR = f'<div class="topbar"><div class="city">Nashik {icon("chev",18)}</div><div class="search">{icon("search",18,"#7a7a7a")}Search this city’s past</div></div>'

def nav(active="Timeline"):
    items = [("Timeline","timeline"),("Map","pin"),("Stories","stories"),("Saved","book")]
    return '<div class="nav">' + "".join(f'<div class="{"on" if n==active else ""}">{icon(i,24)}{n}</div>' for n,i in items) + '</div>'

ERA_PCT = [0, 18.75, 41.7, 59.4, 77.1, 92.7]   # 0:00 3:00 6:40 9:30 12:20 14:50 of 16:00
TOPIC_PCT = [19.3, 28.3, 38.5]                  # 3:05 4:32 6:10

def scrub(pct, cur_era=1, pulse=False, show_topics=True):
    mks = "".join(f'<i class="mk{" cur" if i==cur_era else ""}" style="left:{p}%"></i>' for i,p in enumerate(ERA_PCT))
    tks = "".join(f'<i class="tk" style="left:{p}%"></i>' for p in TOPIC_PCT) if show_topics else ""
    head = f'<i class="head" style="left:{pct}%"></i>'
    return f'<div class="scrub"><div class="fill" style="width:{pct}%"></div>{mks}{tks}{head}</div>'

def video(time="4:21", pct=27.2, playing=True, chip=False, toast=None, cur_era=1):
    play_ic = icon("pause",20,"#fff") if playing else icon("play",20,"#fff")
    big = "" if playing else f'<div class="bigplay">{icon("play",30,"#fff")}</div>'
    chip_html = ""
    if chip:
        chip_html = f'''<div class="chip"><svg class="ring" viewBox="0 0 28 28"><circle cx="14" cy="14" r="12" fill="none" stroke="#e2e2e2" stroke-width="3"/><circle cx="14" cy="14" r="12" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="75.4" stroke-dashoffset="22" stroke-linecap="round" transform="rotate(-90 14 14)"/><path d="M14 20s4.2-4.3 4.2-7.5a4.2 4.2 0 0 0-8.4 0C9.8 15.7 14 20 14 20z" fill="#111"/></svg><div>Pandavleni Caves<small>Tap to pause &amp; read more</small></div>{icon("chevr",16,"#555")}</div>'''
    toast_html = f'<div class="toast"><span class="ok">{icon("check",13,"#fff")}</span>{toast[0]}<small>{toast[1]}</small></div>' if toast else ""
    return f'''<div class="video">{scene()}<div class="vtitle">Nashik Through Time</div>{big}{chip_html}{toast_html}
<div class="ctrls">{play_ic}<span class="t">{time} / 16:00</span>{scrub(pct,cur_era)}<span class="cc">CC</span>{icon("full",18,"#fff")}</div></div>'''

ERAS = ["Ancient","Satavahana","Medieval","Maratha","British","Today"]
def rail(cur=1):
    nodes = "".join(f'<div class="nd{" cur" if i==cur else (" done" if i<cur else "")}"><div class="dot"></div><div class="lb">{e}</div></div>' for i,e in enumerate(ERAS))
    return f'<div class="rail"><div class="line"></div><div class="nodes">{nodes}</div></div>'

def topics(now=None, read=()):
    rows = [("3:05","Gautamiputra Satakarni"),("4:32","Pandavleni Caves"),("6:10","The trade road to Paithan")]
    out = ""
    for i,(t,n) in enumerate(rows):
        cls = "topic" + (" now" if i==now else "")
        pill = '<span class="pill">Now</span>' if i==now else ('<span class="pill read">Read</span>' if i in read else "")
        out += f'<div class="{cls}"><i class="bar"></i><span class="ts">{t}</span><span class="nm">{n}</span>{pill}<span class="inf">i</span></div>'
    return out

def upnext(k, t, n, d):
    return f'<div class="upnext"><div class="th">{scene()}</div><div class="tx"><small>{k}</small><b>{t} · {n}</b><span>{d}</span></div><span class="pv">Preview</span></div>'

def phone(inner):
    return f'<div class="phone">{STATUS}{inner}<div class="home"></div></div>'

# ---------- Screens ----------
S1 = phone(TOPBAR + video("4:21", 27.2, playing=True) + rail(1) + '<div class="hint">‹ Era rail follows the film · tap an era to jump ›</div>'
    + '<div class="sec"><div class="sech"><h3>In this chapter · Satavahana</h3><span>c. 2nd c. BCE – 3rd c. CE</span></div>' + topics() + upnext("Up next in the film","4:32","Pandavleni Caves","24 rock-cut caves · 2 min read") + '</div>' + nav("Timeline"))

S2 = phone(TOPBAR + video("4:32", 28.3, playing=True, chip=True) + rail(1) + '<div class="hint">Film keeps playing · chip slides away after 8 s</div>'
    + '<div class="sec"><div class="sech"><h3>In this chapter · Satavahana</h3><span>c. 2nd c. BCE – 3rd c. CE</span></div>' + topics(now=1) + upnext("After this","6:10","Trade road to Paithan","Coins and the Deccan route · 1 min") + '</div>' + nav("Timeline"))

MINI = f'''<div class="mini"><div class="th">{scene()}</div><div class="tx"><b>Paused at 4:32</b><span>Satavahana · 3:00 – 6:40</span><div class="pb"><i></i></div></div><div class="play">{icon("play",22,"#111")}</div></div>'''

FOOTER = f'<div class="fade"></div><div class="footer"><div class="resume">{icon("play",20,"#fff")}Resume at 4:32</div><div class="sq">{icon("book",22,"#111")}</div></div>'

S3 = phone(MINI + f'''<div class="sheet"><div class="handle"></div>
<div class="crumb">Satavahana {icon("chevr",12,"#999")} <b>4:32 in the film</b></div>
<div class="sh"><div><h1>Pandavleni Caves</h1><p>1st c. BCE – 3rd c. CE · Trirashmi hill</p></div><span class="tag">On screen now</span></div>
<div class="seg"><div class="on"><i></i>Summary</div><div>Explore</div><div>Sources</div></div>
<p class="para">Twenty-four Buddhist caves cut into Trirashmi hill between the 1st century BCE and the 3rd century CE. Their donor inscriptions name <a>Satavahana</a> kings and their <a>Kshatrapa</a> rivals, making the caves the best-dated record of who ruled Nashik, and when.</p>
<div class="lbl">Key evidence</div><div class="ev"><span>Inscriptions</span><span>Coins</span><span>Cave remains</span></div>
<div class="acc">{icon("pin",20)}Places<span class="sp"></span><span class="cnt">3</span>{icon("chev",18,"#555")}</div>
<div class="acc">{icon("people",20)}People<span class="sp"></span><span class="cnt">2</span>{icon("chev",18,"#555")}</div>
<div class="acc">{icon("doc",20)}Primary sources<span class="sp"></span><span class="cnt">4</span>{icon("chev",18,"#555")}</div>
{FOOTER}</div>''')

MAP = '''<div class="map"><svg viewBox="0 0 326 96" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg"><rect width="326" height="96" fill="#e6e6e6"/>
<path d="M0 30 C60 20 90 60 150 50 S240 20 326 36" stroke="#fff" stroke-width="5" fill="none"/><path d="M40 0 C60 40 50 70 90 96" stroke="#fff" stroke-width="4" fill="none"/><path d="M180 96 C200 60 250 70 326 70" stroke="#fff" stroke-width="4" fill="none"/>
<path d="M0 64 C70 70 120 90 200 80 S280 88 326 92" stroke="#bdbdbd" stroke-width="7" fill="none" opacity=".8"/>
<g fill="#111"><path d="M172 58s9-9.5 9-16a9 9 0 0 0-18 0c0 6.5 9 16 9 16z"/><circle cx="172" cy="42" r="3.2" fill="#fff"/></g>
<text x="184" y="22" font-family="Inter,sans-serif" font-size="9" font-weight="700" fill="#333">Trirashmi hill</text>
<text x="246" y="60" font-family="Inter,sans-serif" font-size="8" fill="#666">Godavari</text></svg><span class="cap">Open full map</span></div>'''

def place(n, s, t):
    return f'<div class="place">{icon("pin",16,"#555")}<div class="nm"><b>{n}</b><span>{s}</span></div><span class="jump"><i></i>{t}</span></div>'

S4 = phone(MINI + f'''<div class="sheet"><div class="handle"></div>
<div class="crumb">Satavahana {icon("chevr",12,"#999")} Pandavleni Caves {icon("chevr",12,"#999")} <b>Explore</b></div>
<div class="seg" style="margin-top:8px"><div>Summary</div><div class="on"><i></i>Explore</div><div>Sources</div></div>
<div class="accopen"><div class="hd">{icon("pin",20)}Places<span class="sp"></span>{icon("chev",18,"#555")}</div>{MAP}
{place("Cave 3 · Gautami Balashri vihara","Built by the queen mother, c. 150 CE","5:04")}
{place("Cave 10 · Nahapana vihara","Donated by Nahapana’s son-in-law","5:40")}
{place("Cave 18 · Chaitya hall","Oldest of the group, c. 1st century BCE","4:50")}</div>
<div class="accopen"><div class="hd">{icon("people",20)}People<span class="sp"></span>{icon("chev",18,"#555")}</div>
{place("Gautamiputra Satakarni","Satavahana king who retook Nashik","3:05")}
{place("Nahapana","Western Kshatrapa ruler, his rival","3:40")}</div>
<div class="acc">{icon("doc",20)}Primary sources<span class="sp"></span><span class="cnt">4</span>{icon("chev",18,"#555")}</div>
{FOOTER}</div>''')

def chapter(i, name, rng, meta, prog, state=""):
    st = {"cur":'<span class="st">Watching</span>',"done":'<span class="st done">Watched</span>',"off":'<span class="st off">Jump</span>'}.get(state,"")
    return f'<div class="ch{" cur" if state=="cur" else ""}"><div class="th">{scene()}</div><div class="tx"><b>{name}<span>{rng}</span></b><small>{meta}</small><div class="pr"><i style="width:{prog}%"></i></div></div>{st}</div>'

S5 = phone(TOPBAR + video("4:33", 28.4, playing=True, toast=("Resumed at 4:32","1 topic read")) + f'''
<div class="sheet" style="margin-top:12px;padding-top:10px"><div class="handle"></div>
<div class="chh"><h2>Chapters</h2><div class="tog">Auto-pause at markers<i></i></div></div>
{chapter(0,"Ancient","0:00 – 3:00","Godavari settlement · 2 topics · 2 read",100,"done")}
{chapter(1,"Satavahana","3:00 – 6:40","Caves, kings &amp; trade · 3 topics · 1 read",42,"cur")}
{chapter(2,"Medieval","6:40 – 9:30","Yadava &amp; Sultanate rule · 3 topics",0,"off")}
{chapter(3,"Maratha","9:30 – 12:20","Peshwa-era temples · 4 topics",0,"off")}
{chapter(4,"British","12:20 – 14:50","Cantonment &amp; railway · 2 topics",0,"off")}
{chapter(5,"Today","14:50 – 16:00","Kumbh Mela city · 2 topics",0,"off")}
</div>''' + nav("Timeline"))

SCREENS = [("01-watch",S1),("02-marker",S2),("03-pause-read",S3),("04-explore",S4),("05-resume-chapters",S5)]

for name, html in SCREENS:
    (ROOT/"screens"/f"{name}.html").write_text(f'<!doctype html><html><head><meta charset="utf-8">{FONT}<style>{KIT}body{{width:390px;height:844px;background:#fff;overflow:hidden}}.phone{{border:0;border-radius:0}}</style></head><body>{html}</body></html>')

# ---------- Board ----------
STEPS = [
    ("1","Watch","Film playing · era rail follows it",
     ["<b>Chapter markers live on the scrub bar</b>: six era dots plus small orange ticks for every topic the film mentions.",
      "<b>The era rail under the video auto-advances</b> with playback, so the viewer always knows <i>when</i> they are.",
      "<b>“In this chapter” lists upcoming topics</b> with timestamps; any row can be opened without hunting."]),
    ("2","Marker reached","4:32 · a “Learn more” chip slides in",
     ["<b>The film never interrupts itself.</b> At a marker a small chip appears over the frame with a countdown ring and leaves after 8 s.",
      "<b>Zero cost to ignore</b>: keep watching and nothing changes. The topic row below also lights up as “Now”.",
      "<b>Two ways in</b>: tap the chip, or tap any tick or row, even for a topic the film already passed."]),
    ("3","Pause & read","Video docks · bottom sheet opens",
     ["<b>One tap auto-pauses</b> and shrinks the film into a mini-player pinned at the top. It stays visible so the viewer never feels they “left” the documentary.",
      "<b>Level 1 is a 3-line summary</b>, key-evidence chips and collapsed Places / People / Sources. Enough to satisfy most curiosity in 20 seconds.",
      "<b>“Resume at 4:32” is always the primary button</b>, fixed above the thumb."]),
    ("4","Dig deeper","Explore level · map, places, people",
     ["<b>Depth is a segmented control</b> (Summary › Explore › Sources), so the reader chooses how far to go and the breadcrumb shows where they are.",
      "<b>Every place and person links back into the film</b> (▶ 5:04). Reading can jump the documentary, not just the other way round.",
      "<b>Mini-player and Resume stay put</b> while the sheet scrolls, regardless of depth."]),
    ("5","Resume & navigate","Back at the exact frame · chapter index",
     ["<b>Resume returns to 4:32</b> with a quiet confirmation toast; reading progress is counted per topic.",
      "<b>Chapters sheet</b> (pull up the scrub bar) shows what has been watched and read per era, and lets the viewer jump anywhere.",
      "<b>Auto-pause toggle</b>: viewers who prefer no chips can switch to “only when I tap”. Markers stay on the bar."]),
]

SCALE = 0.66
PW, PH = round(390*SCALE), round(844*SCALE)

flow_svg = f'''<svg width="520" height="176" viewBox="0 0 520 176" xmlns="http://www.w3.org/2000/svg" font-family="Inter,sans-serif">
<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4 0 8z" fill="#333"/></marker></defs>
<g font-size="12" font-weight="700" fill="#111" text-anchor="middle">
<rect x="4" y="60" width="92" height="44" rx="12" fill="#fff" stroke="#111" stroke-width="2"/><text x="50" y="78">Watching</text><text x="50" y="93" font-size="10" font-weight="500" fill="#666">film plays</text>
<rect x="138" y="60" width="104" height="44" rx="12" fill="#fff" stroke="#111" stroke-width="2"/><text x="190" y="78">Marker reached</text><text x="190" y="93" font-size="10" font-weight="500" fill="#666">chip for 8 s</text>
<rect x="284" y="60" width="104" height="44" rx="12" fill="{ORANGE_SOFT}" stroke="{ORANGE}" stroke-width="2"/><text x="336" y="78">Paused · reading</text><text x="336" y="93" font-size="10" font-weight="500" fill="#666">mini-player docked</text>
<rect x="424" y="60" width="92" height="44" rx="12" fill="#fff" stroke="#111" stroke-width="2"/><text x="470" y="78">Deeper</text><text x="470" y="93" font-size="10" font-weight="500" fill="#666">explore · sources</text>
</g>
<g stroke="#333" stroke-width="2" fill="none" marker-end="url(#ar)">
<path d="M96 82H136"/><path d="M242 82H282"/><path d="M388 82H422"/>
<path d="M190 60 C190 30 50 30 50 58"/>
<path d="M336 104 C336 150 60 150 50 108"/>
<path d="M470 104 C470 136 360 136 338 108"/>
</g>
<g font-size="10.5" font-weight="600" fill="#444" text-anchor="middle">
<text x="118" y="34">ignored → chip fades, keep watching</text>
<text x="196" y="156">Resume at 4:32 → exact frame, play continues</text>
<text x="404" y="148">Summary ‹› Explore ‹› Sources</text>

</g></svg>'''

rules = [
    ("Never interrupt", "The film pauses only on a deliberate tap, never by itself. Chips are invitations with a visible timer."),
    ("Keep the film in view", "A docked mini-player with the paused frame and timestamp keeps the sense of place while reading."),
    ("Depth on demand", "Summary › Explore › Sources. Three levels, one control, breadcrumb always visible."),
    ("One-tap return", "A fixed “Resume at m:ss” button is the only primary action in reading mode. Resume continues playback."),
    ("Links go both ways", "Places, people and sources carry ▶ timestamps that jump the documentary to the matching shot."),
    ("Works without the chips", "Scrub-bar ticks, the topic list and the chapters sheet give the same content with auto-pause off."),
]
rules_html = "".join(f'<div class="rule"><b>{t}</b><span>{d}</span></div>' for t,d in rules)

gest = [("Tap chip / tick / row","Pause + open topic sheet"),("Swipe sheet down","Dismiss and resume"),("Drag era rail","Jump between eras"),("Pull up scrub bar","Open chapters"),("Rotate phone","Full-screen film + side panel")]
gest_html = "".join(f'<div class="g"><span>{a}</span><span>{b}</span></div>' for a,b in gest)

cols = ""
for i,(n,t,sub,notes) in enumerate(STEPS):
    html = SCREENS[i][1]
    cols += f'''<div class="col"><div class="step"><span class="num">{n}</span><div><b>{t}</b><span>{sub}</span></div></div>
<div class="pw"><div class="pz">{html}</div></div>
<ul class="notes">{"".join(f"<li>{x}</li>" for x in notes)}</ul></div>'''

BOARD_CSS = f"""
@page{{size:1600px 1200px;margin:0}}
html,body{{width:1600px;height:1200px;overflow:hidden;background:#f6f6f6;font-family:Inter,system-ui,sans-serif;color:#111;-webkit-font-smoothing:antialiased}}
.board{{width:1600px;height:1200px;position:relative;padding:34px 44px 0}}
.hd{{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:18px;border-bottom:2px solid #111}}
.hd h1{{font-size:34px;font-weight:800;letter-spacing:-.6px;line-height:1}}
.hd h1 em{{font-style:normal;color:{ORANGE}}}
.hd p{{font-size:14.5px;color:#444;margin-top:9px;font-weight:500;max-width:1180px}}
.legend{{text-align:right;font-size:12px;color:#555;font-weight:500;line-height:1.6;white-space:nowrap;flex:none}}
.legend b{{display:block;font-size:13px;color:#111;font-weight:700}}
.legend i{{display:inline-block;width:11px;height:11px;border-radius:50%;background:{ORANGE};vertical-align:-1px;margin-right:5px}}
.row{{display:flex;justify-content:space-between;margin-top:20px}}
.col{{width:{PW+26}px}}
.step{{display:flex;align-items:center;gap:9px;height:42px;margin-bottom:8px}}
.step .num{{width:28px;height:28px;border-radius:50%;background:#111;color:#fff;font-weight:800;font-size:14px;display:flex;align-items:center;justify-content:center;flex:none}}
.step b{{display:block;font-size:16px;font-weight:800;line-height:1.1}}
.step span{{display:block;font-size:11.5px;color:#666;font-weight:500;margin-top:2px}}
.pw{{width:{PW+6}px;height:{PH+6}px;margin:0 auto}}
.pz{{transform:scale({SCALE});transform-origin:top left;width:390px;height:844px;filter:drop-shadow(0 10px 22px rgba(0,0,0,.14))}}
.notes{{list-style:none;margin-top:12px;display:flex;flex-direction:column;gap:5px}}
.notes li{{font-size:11.3px;line-height:1.4;color:#333;padding-left:12px;position:relative}}
.notes li:before{{content:"";position:absolute;left:0;top:6px;width:6px;height:6px;border-radius:50%;background:{ORANGE}}}
.notes li b{{font-weight:700;color:#111}}
.bottom{{position:absolute;left:44px;right:44px;bottom:30px;height:196px;display:flex;gap:30px;border-top:2px solid #111;padding-top:14px}}
.bt{{font-size:11px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:#777;margin-bottom:6px}}
.flow{{width:520px;flex:none}}
.rules{{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:7px 20px;align-content:start}}
.rule b{{display:block;font-size:12.5px;font-weight:800}}
.rule span{{display:block;font-size:11px;color:#444;line-height:1.35}}
.gest{{width:300px;flex:none}}
.g{{display:flex;justify-content:space-between;gap:10px;font-size:11px;padding:4px 0;border-bottom:1px solid #ddd}}
.g span:first-child{{font-weight:700;white-space:nowrap}}
.g span:last-child{{color:#444;text-align:right}}
"""

board = f'''<!doctype html><html><head><meta charset="utf-8"><title>Watch · Pause · Dig deeper · Resume — Interactive documentary UX</title>{FONT}<style>{KIT}{BOARD_CSS}</style></head><body><div class="board">
<div class="hd"><div><h1>Watch · Pause · <em>Dig deeper</em> · Resume</h1><p>Interaction concept for a mobile-first city-history site. The documentary stays the spine; reading is a layer the viewer pulls up and drops back at the exact frame. Shown for Nashik, 16-minute film, six eras.</p></div>
<div class="legend"><b>Grayscale wireframes · 390 × 844</b><i></i>orange = current / active state<br>Inter · no final colours or imagery</div></div>
<div class="row">{cols}</div>
<div class="bottom">
<div class="flow"><div class="bt">State flow</div>{flow_svg}</div>
<div class="rules-wrap" style="flex:1"><div class="bt">Interaction rules</div><div class="rules">{rules_html}</div></div>
<div class="gest"><div class="bt">Gestures</div>{gest_html}</div>
</div></div></body></html>'''
(ROOT/"entries"/"entry-1.html").write_text(board)
print("wrote", len(SCREENS), "screens + board")

# ---------- Clickable prototype ----------
PROTO_CSS = """
body{background:#e9e9e9;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:Inter,system-ui,sans-serif;padding:18px 0}
.demo{width:390px;display:flex;align-items:center;justify-content:space-between;font-size:12px;color:#444;margin-bottom:10px;gap:8px;flex-wrap:wrap}
.demo b{font-weight:700;color:#111}
.demo button{font:inherit;font-size:11.5px;font-weight:700;border:1.5px solid #bbb;background:#fff;border-radius:999px;padding:4px 9px;cursor:pointer}
.demo button.on{background:#111;color:#fff;border-color:#111}
.phone{box-shadow:0 20px 60px rgba(0,0,0,.25);flex:none}
.phone *{cursor:default}
.tap{cursor:pointer!important}
.tap *{cursor:pointer!important}
@media (max-width:430px){body{padding:0;background:#fff}.demo{display:none}.phone{border:0;border-radius:0;box-shadow:none;width:100vw;height:100vh;height:100dvh}}
#watch{display:flex;flex-direction:column;flex:1;min-height:0}
.pane{position:absolute;left:0;right:0;top:46px;bottom:0;display:flex;flex-direction:column;background:#fff;transform:translateY(102%);transition:transform .32s cubic-bezier(.2,.8,.2,1);will-change:transform}
.pane.open{transform:translateY(0)}
.sheet{overflow-y:auto}
.sheet::-webkit-scrollbar{display:none}
.sheetbody{padding-bottom:110px}
.chip{animation:chipin .35s cubic-bezier(.2,.8,.2,1)}
.chip.out{animation:chipout .3s ease forwards}
@keyframes chipin{from{transform:translateY(12px);opacity:0}to{transform:none;opacity:1}}
@keyframes chipout{to{transform:translateY(8px);opacity:0}}
.chip .ring .arc{transition:stroke-dashoffset .1s linear}
.toast{animation:chipin .3s ease}
.toast.out{animation:chipout .3s ease forwards}
#chapters{position:absolute;inset:0;display:none}
#chapters.open{display:block}
#chapters .dim{cursor:pointer}
#chapters .sheet{position:absolute;left:0;right:0;bottom:0;top:300px;margin:0;padding-top:10px}
.seg div{cursor:pointer}
.tog.off i{background:#bbb}.tog.off i:after{right:16px}
.srcrow{display:flex;gap:10px;padding:10px 14px;border-bottom:1px solid #f0f0f0;font-size:12.5px;align-items:flex-start}
.srcrow:last-child{border-bottom:0}
.srcrow b{display:block;font-weight:600}.srcrow span{color:#777;font-size:11.5px}
.empty{font-size:12.5px;color:#777;padding:14px 0}
.scrub{height:14px;background:none;display:flex;align-items:center}
.scrub .track{position:absolute;left:0;right:0;top:5px;height:4px;background:rgba(255,255,255,.38);border-radius:2px}
.scrub .fill{position:absolute;left:0;top:5px;height:4px}
.scrub .mk{top:2px}.scrub .mk.cur{top:0}.scrub .tk{top:3px;width:3px;height:8px}.scrub .head{top:1px}
.scrub .tk,.scrub .mk{cursor:pointer}
.sq.saved{background:#111;border-color:#111}
"""

PROTO_JS = r"""
const T=960;
const ERAS=[{n:'Ancient',s:0,meta:'Godavari settlement'},{n:'Satavahana',s:180,meta:'Caves, kings & trade'},{n:'Medieval',s:400,meta:'Yadava & Sultanate rule'},{n:'Maratha',s:570,meta:'Peshwa-era temples'},{n:'British',s:740,meta:'Cantonment & railway'},{n:'Today',s:890,meta:'Kumbh Mela city'}];
const TOPICS=[
{t:30,era:0,title:'Settlement on the Godavari',sub:'c. 1000 BCE onwards · river bank',summary:'Nashik grew where the young Godavari leaves the Western Ghats. Early farming settlements on its banks are known from pottery and burial finds, long before any written record.',ev:['Pottery','Burials','River terraces'],places:[{n:'Ramkund',s:'Sacred bathing ghat on the Godavari',t:50}],people:[],sources:[{n:'Excavation reports, Deccan College',s:'Chalcolithic levels at Nashik'}]},
{t:120,era:0,title:'Panchavati and the Ramayana',sub:'Legend · forest of five banyans',summary:'Tradition places Rama, Sita and Lakshmana’s forest exile at Panchavati on the Godavari. The story explains the city’s name, from the cutting of Shurpanakha’s nose (nasika).',ev:['Epic tradition','Temple names'],places:[{n:'Sita Gufa',s:'Cave shrine in Panchavati',t:140}],people:[{n:'Rama, Sita, Lakshmana',s:'Exiles of the epic',t:125}],sources:[{n:'Valmiki Ramayana, Aranya Kanda',s:'Forest exile episodes'}]},
{t:185,era:1,title:'Gautamiputra Satakarni',sub:'r. c. 106 – 130 CE · Satavahana king',summary:'The Satavahana king who drove the Western Kshatrapas out of the Deccan. His mother’s inscription at Pandavleni describes him as the one who “uprooted the Khakharata lineage”.',ev:['Inscriptions','Restruck coins'],places:[{n:'Cave 3 · Pandavleni',s:'Inscription of Gautami Balashri',t:300}],people:[{n:'Nahapana',s:'Western Kshatrapa rival',t:220},{n:'Gautami Balashri',s:'Queen mother, donor of Cave 3',t:300}],sources:[{n:'Nasik cave inscription No. 2',s:'Eulogy of Gautamiputra'},{n:'Jogalthembi hoard',s:'Nahapana’s coins restruck'}]},
{t:272,era:1,title:'Pandavleni Caves',sub:'1st c. BCE – 3rd c. CE · Trirashmi hill',summary:'Twenty-four Buddhist caves cut into Trirashmi hill between the 1st century BCE and the 3rd century CE. Their donor inscriptions name Satavahana kings and their Kshatrapa rivals, making the caves the best-dated record of who ruled Nashik, and when.',ev:['Inscriptions','Coins','Cave remains'],places:[{n:'Cave 3 · Gautami Balashri vihara',s:'Built by the queen mother, c. 150 CE',t:304},{n:'Cave 10 · Nahapana vihara',s:'Donated by Nahapana’s son-in-law',t:340},{n:'Cave 18 · Chaitya hall',s:'Oldest of the group, c. 1st century BCE',t:290}],people:[{n:'Gautamiputra Satakarni',s:'Satavahana king who retook Nashik',t:185},{n:'Nahapana',s:'Western Kshatrapa ruler, his rival',t:220}],sources:[{n:'Nasik cave inscriptions (Senart, 1905)',s:'Epigraphia Indica VIII'},{n:'Ushavadata’s donations',s:'Cave 10 inscription'},{n:'ASI site notice',s:'Trirashmi / Pandavleni'},{n:'Coin finds, Nashik district',s:'Satavahana lead & potin coins'}]},
{t:370,era:1,title:'The trade road to Paithan',sub:'Ports to the Deccan capital',summary:'Nashik sat on the route from the coastal ports of Sopara and Kalyan to Pratishthana (Paithan), the Satavahana capital. Cave donations by merchants and guilds show how much of the city’s wealth came from passing trade.',ev:['Guild inscriptions','Roman coins'],places:[{n:'Sopara',s:'Ancient port on the Konkan coast',t:380}],people:[{n:'Merchant donors',s:'Named in cave inscriptions',t:385}],sources:[{n:'Periplus of the Erythraean Sea',s:'1st-century trade manual'}]},
{t:420,era:2,title:'The Yadavas of Devagiri',sub:'12th – 13th century',summary:'Under the Yadava kings of Devagiri the region prospered and Marathi emerged as a court language. Temple building and land grants from this period survive around Nashik.',ev:['Copper-plate grants','Temple fragments'],places:[{n:'Devagiri (Daulatabad)',s:'Yadava capital',t:430}],people:[{n:'Singhana II',s:'Yadava king, r. 1200–1246',t:440}],sources:[{n:'Yadava copper plates',s:'Land grants near Nashik'}]},
{t:500,era:2,title:'Sultanate rule',sub:'14th – 17th century',summary:'After the Delhi Sultanate’s conquest of the Deccan the town passed to the Bahmani and then the Nizam Shahi sultans of Ahmadnagar, before the Mughals took it in the 1630s.',ev:['Chronicles','Fortifications'],places:[{n:'Ahmadnagar',s:'Nizam Shahi capital',t:520}],people:[{n:'Malik Ambar',s:'Nizam Shahi regent',t:540}],sources:[{n:'Burhan-i Ma’asir',s:'Nizam Shahi chronicle'}]},
{t:590,era:3,title:'Peshwa-era temples',sub:'18th century · Kalaram & Sundar Narayan',summary:'Maratha patronage rebuilt the city’s riverside. The Sundar Narayan temple (1756) and the black-stone Kalaram temple (1782, Sardar Rangarao Odhekar) still anchor Panchavati.',ev:['Temple inscriptions','Peshwa daftar'],places:[{n:'Kalaram temple',s:'Panchavati, 1782',t:600},{n:'Sundar Narayan temple',s:'Ahilyabai Holkar bridge, 1756',t:620}],people:[{n:'Sardar Rangarao Odhekar',s:'Builder of Kalaram',t:605}],sources:[{n:'Peshwa Daftar records',s:'Grants to Nashik temples'}]},
{t:680,era:3,title:'Trimbakeshwar',sub:'Jyotirlinga · source of the Godavari',summary:'Peshwa Balaji Bajirao rebuilt the Trimbakeshwar temple in the 1750s at the Godavari’s source, 28 km from the city, tying Nashik to one of the twelve jyotirlingas.',ev:['Temple architecture','Peshwa records'],places:[{n:'Trimbakeshwar temple',s:'Trimbak, 28 km west',t:690}],people:[{n:'Balaji Bajirao (Nanasaheb)',s:'Peshwa, patron',t:695}],sources:[{n:'Peshwa Daftar records',s:'Temple reconstruction'}]},
{t:760,era:4,title:'Deolali cantonment',sub:'Established 1861',summary:'The British set up a military cantonment at Deolali in 1861, later a transit camp for troops bound for the Western Front. Its slang legacy survives in the word “doolally”.',ev:['Cantonment records','Memoirs'],places:[{n:'Deolali camp',s:'16 km south-east',t:770}],people:[],sources:[{n:'Gazetteer of the Bombay Presidency, Nasik',s:'1883 edition'}]},
{t:840,era:4,title:'The railway arrives',sub:'1860s · Nashik Road station',summary:'The Great Indian Peninsula Railway’s Bombay–Bhusawal line reached the district in the 1860s. Nashik Road station, 8 km from the old town, pulled growth away from the river.',ev:['Railway maps','Gazetteers'],places:[{n:'Nashik Road station',s:'GIPR line',t:850}],people:[],sources:[{n:'GIPR annual reports',s:'1860s'}]},
{t:900,era:5,title:'Kumbh Mela city',sub:'Every 12 years · Ramkund',summary:'Nashik is one of four Kumbh Mela sites. Every twelve years millions bathe at Ramkund and Trimbakeshwar, and the city’s ghats are rebuilt around the event.',ev:['Crowd estimates','Civic plans'],places:[{n:'Ramkund',s:'Main bathing ghat',t:905}],people:[],sources:[{n:'Nashik Municipal Corporation, Kumbh plan 2027',s:'Infrastructure brief'}]},
{t:940,era:5,title:'Wine country',sub:'Since 1999',summary:'The first commercial vineyards opened near Nashik in 1999. The district now produces most of India’s wine, a new chapter for a valley that has traded along the Godavari for two millennia.',ev:['Industry data'],places:[{n:'Gangapur backwaters',s:'Vineyard belt',t:945}],people:[],sources:[{n:'Indian Grape Processing Board',s:'Production statistics'}]}
];
const fmt=s=>{s=Math.floor(s);return Math.floor(s/60)+':'+String(s%60).padStart(2,'0')};
const S={t:265,playing:true,speed:2,mode:'watch',topic:null,tab:'summary',auto:true,read:new Set(),saved:new Set(),chip:null,chipUntil:0,maxT:265,pausedAt:0};
const $=id=>document.getElementById(id);
const eraAt=t=>{let e=0;ERAS.forEach((x,i)=>{if(t>=x.s)e=i});return e};
const pct=t=>t/T*100;

function renderScrub(){
  let h='<div class="track"></div><div class="fill" style="width:'+pct(S.t)+'%"></div>';
  ERAS.forEach((e,i)=>h+='<i class="mk'+(i===eraAt(S.t)?' cur':'')+'" style="left:'+pct(e.s)+'%" data-era="'+i+'" title="'+e.n+'"></i>');
  TOPICS.forEach((x,i)=>{if(x.era===eraAt(S.t))h+='<i class="tk" style="left:'+pct(x.t)+'%" data-topic="'+i+'" title="'+x.title+'"></i>'});
  h+='<i class="head" style="left:'+pct(S.t)+'%"></i>';
  $('scrub').innerHTML=h;
}
function renderRail(){
  const cur=eraAt(S.t);
  $('rail').innerHTML='<div class="line"></div><div class="nodes">'+ERAS.map((e,i)=>'<div class="nd tap'+(i===cur?' cur':(i<cur?' done':''))+'" data-era="'+i+'"><div class="dot"></div><div class="lb">'+e.n+'</div></div>').join('')+'</div>';
}
function renderTopics(){
  const cur=eraAt(S.t);
  const list=TOPICS.map((x,i)=>({...x,i})).filter(x=>x.era===cur);
  const now=[...list].reverse().find(x=>x.t<=S.t);
  $('secTitle').textContent='In this chapter · '+ERAS[cur].n;
  let h=list.map(x=>{const isNow=now&&now.i===x.i;const pill=isNow?'<span class="pill">Now</span>':(S.read.has(x.i)?'<span class="pill read">Read</span>':'');
    return '<div class="topic tap'+(isNow?' now':'')+'" data-topic="'+x.i+'"><i class="bar"></i><span class="ts">'+fmt(x.t)+'</span><span class="nm">'+x.title+'</span>'+pill+'<span class="inf">i</span></div>'}).join('');
  const next=TOPICS.map((x,i)=>({...x,i})).find(x=>x.t>S.t+2);
  if(next)h+='<div class="upnext tap" data-topic="'+next.i+'"><div class="th">'+SCENE+'</div><div class="tx"><small>Up next in the film</small><b>'+fmt(next.t)+' · '+next.title+'</b><span>'+next.sub+'</span></div><span class="pv">Preview</span></div>';
  $('topics').innerHTML=h;
}
function tick(){
  if(S.playing&&S.mode==='watch'){
    const prev=S.t; S.t=Math.min(T,S.t+0.1*S.speed); if(S.t>S.maxT)S.maxT=S.t;
    if(S.t>=T){S.playing=false;$('playIc').innerHTML=ICON.play}
    const hit=TOPICS.findIndex(x=>prev<x.t&&x.t<=S.t);
    if(hit>=0&&S.auto){showChip(hit)}
    if(eraAt(prev)!==eraAt(S.t)){renderRail();renderScrub();renderTopics()}
    else if(Math.floor(prev)!==Math.floor(S.t)){renderTopics()}
  }
  $('time').textContent=fmt(S.t);
  const f=$('scrub').querySelector('.fill'),hd=$('scrub').querySelector('.head');
  if(f){f.style.width=pct(S.t)+'%';hd.style.left=pct(S.t)+'%'}
  if(S.chip!==null){const left=(S.chipUntil-Date.now())/8000;const arc=document.querySelector('.chip .arc');if(arc)arc.style.strokeDashoffset=75.4*(1-Math.max(0,left));if(left<=0)hideChip()}
}
function showChip(i){
  hideChip(true);S.chip=i;S.chipUntil=Date.now()+8000;const x=TOPICS[i];
  const d=document.createElement('div');d.className='chip tap';d.dataset.topic=i;
  d.innerHTML='<svg class="ring" viewBox="0 0 28 28"><circle cx="14" cy="14" r="12" fill="none" stroke="#e2e2e2" stroke-width="3"/><circle class="arc" cx="14" cy="14" r="12" fill="none" stroke="#F7993F" stroke-width="3" stroke-dasharray="75.4" stroke-dashoffset="0" stroke-linecap="round" transform="rotate(-90 14 14)"/><path d="M14 20s4.2-4.3 4.2-7.5a4.2 4.2 0 0 0-8.4 0C9.8 15.7 14 20 14 20z" fill="#111"/></svg><div>'+x.title+'<small>Tap to pause &amp; read more</small></div>'+ICON.chevr;
  $('video').appendChild(d);
}
function hideChip(now){const c=document.querySelector('.chip');S.chip=null;if(!c)return;if(now){c.remove();return}c.classList.add('out');setTimeout(()=>c.remove(),300)}
function toast(msg,sub){const old=document.querySelector('.toast');if(old)old.remove();const d=document.createElement('div');d.className='toast';d.innerHTML='<span class="ok">'+ICON.check+'</span>'+msg+(sub?'<small>'+sub+'</small>':'');$('video').appendChild(d);setTimeout(()=>{d.classList.add('out');setTimeout(()=>d.remove(),300)},2600)}
function seek(t,play){S.t=Math.max(0,Math.min(T,t));if(S.t>S.maxT)S.maxT=S.t;if(play!==undefined)S.playing=play;$('playIc').innerHTML=S.playing?ICON.pause:ICON.play;hideChip(true);renderScrub();renderRail();renderTopics();tick()}
function openTopic(i){
  hideChip(true);S.playing=false;S.pausedAt=S.t;S.mode='read';S.topic=i;S.tab='summary';S.read.add(i);
  renderRead();$('read').classList.add('open');$('chapters').classList.remove('open');
}
function renderRead(){
  const x=TOPICS[S.topic];const era=ERAS[x.era].n;const nxt=TOPICS[S.topic+1];const onScreen=S.pausedAt>=x.t-1&&(!nxt||S.pausedAt<nxt.t);
  $('miniT').textContent='Paused at '+fmt(S.pausedAt);$('miniS').textContent=era+' · '+fmt(ERAS[x.era].s)+' – '+fmt((ERAS[x.era+1]||{s:T}).s);$('miniPb').style.width=pct(S.pausedAt)+'%';
  const seg='<div class="seg">'+['summary','explore','sources'].map(k=>'<div class="'+(S.tab===k?'on':'')+'" data-tab="'+k+'">'+(S.tab===k?'<i></i>':'')+k[0].toUpperCase()+k.slice(1)+'</div>').join('')+'</div>';
  const crumb='<div class="crumb">'+era+' '+ICON.chevr12+(S.tab==='summary'?' <b>'+fmt(x.t)+' in the film</b>':' '+x.title+' '+ICON.chevr12+' <b>'+(S.tab==='explore'?'Explore':'Sources')+'</b>')+'</div>';
  const jump=p=>'<span class="jump tap" data-seek="'+p.t+'"><i></i>'+fmt(p.t)+'</span>';
  const row=(p,ic)=>'<div class="place">'+(ic||ICON.pin16)+'<div class="nm"><b>'+p.n+'</b><span>'+p.s+'</span></div>'+jump(p)+'</div>';
  let body='';
  if(S.tab==='summary'){
    body='<div class="sh"><div><h1>'+x.title+'</h1><p>'+x.sub+'</p></div>'+(onScreen?'<span class="tag">On screen now</span>':'<span class="tag" style="background:#e4e4e4">'+fmt(x.t)+' in film</span>')+'</div>'+seg+'<p class="para">'+x.summary+'</p><div class="lbl">Key evidence</div><div class="ev">'+x.ev.map(e=>'<span>'+e+'</span>').join('')+'</div>'
    +'<div class="acc tap" data-tab="explore">'+ICON.pin+'Places<span class="sp"></span><span class="cnt">'+x.places.length+'</span>'+ICON.chev+'</div><div class="acc tap" data-tab="explore">'+ICON.people+'People<span class="sp"></span><span class="cnt">'+x.people.length+'</span>'+ICON.chev+'</div><div class="acc tap" data-tab="sources">'+ICON.doc+'Primary sources<span class="sp"></span><span class="cnt">'+x.sources.length+'</span>'+ICON.chev+'</div>';
  }else if(S.tab==='explore'){
    body=seg+'<div class="accopen"><div class="hd">'+ICON.pin+'Places<span class="sp"></span>'+ICON.chev+'</div>'+MAP+(x.places.length?x.places.map(row).join(''):'<div class="empty" style="padding:12px 14px">No mapped places for this topic yet.</div>')+'</div>'
    +'<div class="accopen"><div class="hd">'+ICON.people+'People<span class="sp"></span>'+ICON.chev+'</div>'+(x.people.length?x.people.map(p=>row(p,ICON.people16)).join(''):'<div class="empty" style="padding:12px 14px">No people linked to this topic.</div>')+'</div>'
    +'<div class="acc tap" data-tab="sources">'+ICON.doc+'Primary sources<span class="sp"></span><span class="cnt">'+x.sources.length+'</span>'+ICON.chev+'</div>';
  }else{
    body=seg+'<div class="accopen"><div class="hd">'+ICON.doc+'Primary sources<span class="sp"></span>'+ICON.chev+'</div>'+x.sources.map(s=>'<div class="srcrow">'+ICON.doc16+'<div><b>'+s.n+'</b><span>'+s.s+'</span></div></div>').join('')+'</div><p class="para" style="font-size:12px;color:#666">Sources open in a reader view. Citations copy as plain text.</p>';
  }
  $('sheetBody').innerHTML=crumb+body;
  $('resumeLbl').textContent='Resume at '+fmt(S.pausedAt);
  $('saveBtn').className='sq tap'+(S.saved.has(S.topic)?' saved':'');$('saveBtn').innerHTML=S.saved.has(S.topic)?ICON.bookfW:ICON.book;
  $('sheet').scrollTop=0;
}
function resume(){S.mode='watch';$('read').classList.remove('open');seek(S.pausedAt,true);const n=S.read.size;toast('Resumed at '+fmt(S.pausedAt),n+' topic'+(n>1?'s':'')+' read')}
function renderChapters(){
  const cur=eraAt(S.t);
  $('chList').innerHTML=ERAS.map((e,i)=>{const end=(ERAS[i+1]||{s:T}).s;const tp=TOPICS.map((x,j)=>({...x,j})).filter(x=>x.era===i);const rd=tp.filter(x=>S.read.has(x.j)).length;
    const prog=Math.max(0,Math.min(1,(S.maxT-e.s)/(end-e.s)))*100;const st=i===cur?'<span class="st">Watching</span>':(S.maxT>=end?'<span class="st done">Watched</span>':'<span class="st off">Jump</span>');
    return '<div class="ch tap'+(i===cur?' cur':'')+'" data-era="'+i+'"><div class="th">'+SCENE+'</div><div class="tx"><b>'+e.n+'<span>'+fmt(e.s)+' – '+fmt(end)+'</span></b><small>'+e.meta+' · '+tp.length+' topics'+(rd?' · '+rd+' read':'')+'</small><div class="pr"><i style="width:'+prog+'%"></i></div></div>'+st+'</div>'}).join('');
  $('autoTog').className='tog tap'+(S.auto?'':' off');
}
document.addEventListener('click',ev=>{
  const el=ev.target.closest('[data-topic],[data-era],[data-seek],[data-tab],#playBtn,#resumeBtn,#saveBtn,#miniPlay,#chapBtn,#chapters .dim,#autoTog,#scrub,#handle,.demo button');
  if(!el)return;
  if(el.matches('.demo button')){if(el.dataset.speed){S.speed=+el.dataset.speed;document.querySelectorAll('.demo button[data-speed]').forEach(b=>b.classList.toggle('on',b===el))}else if(el.dataset.jump){S.mode='watch';$('read').classList.remove('open');$('chapters').classList.remove('open');seek(+el.dataset.jump,true)}return}
  if(el.id==='playBtn'){S.playing=!S.playing;$('playIc').innerHTML=S.playing?ICON.pause:ICON.play;return}
  if(el.id==='resumeBtn'||el.id==='miniPlay'||el.id==='handle'){resume();return}
  if(el.id==='saveBtn'){S.saved.has(S.topic)?S.saved.delete(S.topic):S.saved.add(S.topic);renderRead();return}
  if(el.id==='chapBtn'){renderChapters();$('chapters').classList.add('open');return}
  if(el.matches('#chapters .dim')){$('chapters').classList.remove('open');return}
  if(el.id==='autoTog'){S.auto=!S.auto;renderChapters();if(!S.auto)hideChip();return}
  if(el.dataset.tab){S.tab=el.dataset.tab;renderRead();return}
  if(el.dataset.seek){S.mode='watch';$('read').classList.remove('open');seek(+el.dataset.seek,true);toast('Jumped to '+fmt(+el.dataset.seek),'from '+TOPICS[S.topic].title);return}
  if(el.dataset.topic!==undefined){openTopic(+el.dataset.topic);return}
  if(el.dataset.era!==undefined){$('chapters').classList.remove('open');seek(ERAS[+el.dataset.era].s,true);return}
  if(el.id==='scrub'){const r=el.getBoundingClientRect();seek((ev.clientX-r.left)/r.width*T);return}
});
renderScrub();renderRail();renderTopics();tick();setInterval(tick,100);
"""

ICONS_JS = "const ICON=" + __import__("json").dumps({
    "play": icon("play",20,"#fff"), "pause": icon("pause",20,"#fff"), "chevr": icon("chevr",16,"#555"), "chevr12": icon("chevr",12,"#999"),
    "check": icon("check",13,"#fff"), "pin": icon("pin",20), "pin16": icon("pin",16,"#555"), "people": icon("people",20), "doc": icon("doc",20),
    "doc16": icon("doc",16,"#555"), "people16": icon("people",16,"#555"), "chev": icon("chev",18,"#555"), "book": icon("book",22,"#111"), "bookfW": icon("bookf",22,"#fff")}) + ";"
SCENE_JS = "const SCENE=" + __import__("json").dumps(scene()) + ";const MAP=" + __import__("json").dumps(MAP) + ";"

proto = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>Nashik Through Time — interactive documentary prototype</title>{FONT}<style>{KIT}{PROTO_CSS}</style></head><body>
<div class="demo"><span><b>Clickable prototype</b> · film is simulated</span><span>Speed <button data-speed="1">1×</button> <button data-speed="2" class="on">2×</button> <button data-speed="8">8×</button> <button data-jump="265">Jump to 4:25</button></span></div>
<div class="phone">{STATUS}
<div id="watch">{TOPBAR}
<div class="video" id="video">{scene()}<div class="vtitle">Nashik Through Time</div>
<div class="ctrls"><span id="playBtn" class="tap" style="display:flex"><span id="playIc">{icon("pause",20,"#fff")}</span></span><span class="t"><span id="time">4:25</span> / 16:00</span><div class="scrub tap" id="scrub"></div><span id="chapBtn" class="tap" title="Chapters">{icon("list",18,"#fff")}</span>{icon("full",18,"#fff")}</div></div>
<div class="rail" id="rail"></div><div class="hint">Era rail follows the film · tap an era to jump</div>
<div class="sec" style="overflow-y:auto"><div class="sech"><h3 id="secTitle">In this chapter</h3><span>tap i to read</span></div><div id="topics"></div></div>
{nav("Timeline")}</div>
<div class="pane" id="read">
<div class="mini" style="margin-top:6px"><div class="th">{scene()}</div><div class="tx"><b id="miniT">Paused</b><span id="miniS"></span><div class="pb"><i id="miniPb"></i></div></div><div class="play tap" id="miniPlay">{icon("play",22,"#111")}</div></div>
<div class="sheet" id="sheet"><div class="handle tap" id="handle" style="flex:none"></div><div class="sheetbody" id="sheetBody"></div></div>
<div class="fade"></div><div class="footer"><div class="resume tap" id="resumeBtn">{icon("play",20,"#fff")}<span id="resumeLbl">Resume</span></div><div class="sq tap" id="saveBtn">{icon("book",22,"#111")}</div></div>
</div>
<div id="chapters"><div class="dim"></div><div class="sheet"><div class="handle"></div><div class="chh"><h2>Chapters</h2><div class="tog tap" id="autoTog">Auto-pause at markers<i></i></div></div><div id="chList"></div></div></div>
<div class="home"></div></div>
<script>{ICONS_JS}{SCENE_JS}{PROTO_JS}</script></body></html>'''
(ROOT/"prototype"/"index.html").write_text(proto)
print("wrote prototype")
