#!/usr/bin/env python3
"""Self-contained dark dashboard renderer for Borealis. Stdlib only."""
from __future__ import annotations

import html
import json
import math
from typing import Any

LAMPORTS = 1_000_000_000


def e(s: Any) -> str:
    return html.escape("" if s is None else str(s), quote=True)


def nfmt(n: Any, digits: int = 0) -> str:
    if n is None:
        return "—"
    try:
        x = float(n)
    except (TypeError, ValueError):
        return "—"
    if not math.isfinite(x):
        return "—"
    if digits == 0:
        return f"{x:,.0f}"
    return f"{x:,.{digits}f}"


def usd(n: Any, digits: int | None = None) -> str:
    if n is None:
        return "—"
    try:
        x = float(n)
    except (TypeError, ValueError):
        return "—"
    if not math.isfinite(x):
        return "—"
    ax = abs(x)
    sign = "−" if x < 0 else ""
    if ax >= 1_000_000_000_000:
        return f"{sign}${ax/1e12:.2f}T"
    if ax >= 1_000_000_000:
        return f"{sign}${ax/1e9:.2f}B"
    if ax >= 1_000_000:
        return f"{sign}${ax/1e6:.2f}M"
    if ax >= 1_000:
        return f"{sign}${ax/1e3:.2f}K"
    if digits is None:
        digits = 2 if ax >= 1 else 4
    return f"{sign}${ax:,.{digits}f}"


def pct(n: Any, digits: int = 2) -> str:
    if n is None:
        return "—"
    try:
        x = float(n)
    except (TypeError, ValueError):
        return "—"
    if not math.isfinite(x):
        return "—"
    sign = "+" if x > 0 else ""
    return f"{sign}{x:.{digits}f}%"


def delta_class(n: Any) -> str:
    try:
        x = float(n)
    except (TypeError, ValueError):
        return "flat"
    if x > 0.05:
        return "up"
    if x < -0.05:
        return "down"
    return "flat"


def sparkline(values, w=220, h=48, color="#3ee0b0", fill=True) -> str:
    vals = [v for v in values if isinstance(v, (int, float)) and math.isfinite(v)]
    if len(vals) < 2:
        return f'<svg class="spark" width="{w}" height="{h}"></svg>'
    lo, hi = min(vals), max(vals)
    span = (hi - lo) or 1.0
    pad = 2
    pts = []
    for i, v in enumerate(vals):
        x = pad + i * (w - 2 * pad) / (len(vals) - 1)
        y = pad + (1 - (v - lo) / span) * (h - 2 * pad)
        pts.append((x, y))
    d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    fill_d = d + f" L {pts[-1][0]:.1f},{h} L {pts[0][0]:.1f},{h} Z"
    last = pts[-1]
    fill_el = f'<path d="{fill_d}" fill="{color}" fill-opacity="0.12"/>' if fill else ""
    return (
        f'<svg class="spark" viewBox="0 0 {w} {h}" width="{w}" height="{h}" preserveAspectRatio="none">'
        f"{fill_el}<path d=\"{d}\" fill=\"none\" stroke=\"{color}\" stroke-width=\"1.6\"/>"
        f'<circle cx="{last[0]:.1f}" cy="{last[1]:.1f}" r="2.4" fill="{color}"/></svg>'
    )


def axis_fmt(n, money=False) -> str:
    try:
        x = float(n)
    except (TypeError, ValueError):
        return "—"
    ax = abs(x)
    sign = "−" if x < 0 else ""
    if money:
        if ax >= 1_000_000_000:
            return f"{sign}${ax/1e9:.2f}B"
        if ax >= 1_000_000:
            return f"{sign}${ax/1e6:.2f}M"
        if ax >= 1_000:
            return f"{sign}${ax/1e3:.1f}K"
        return f"{sign}${ax:.2f}"
    if ax >= 1_000_000:
        return f"{sign}{ax/1e6:.2f}M"
    if ax >= 1_000:
        return f"{sign}{ax/1e3:.1f}K"
    if ax >= 100:
        return f"{sign}{ax:.0f}"
    if ax >= 10:
        return f"{sign}{ax:.1f}"
    return f"{sign}{ax:.2f}"

def trend_chart(points, *, w=560, h=176, color="#3ee0b0", ylabel="", money=False) -> str:
    vals, labels = [], []
    for p in points or []:
        if isinstance(p, dict):
            v, ts = p.get("v"), p.get("ts")
        elif isinstance(p, (int, float)):
            v, ts = p, None
        else:
            continue
        if isinstance(v, (int, float)) and math.isfinite(v):
            vals.append(float(v))
            labels.append(str(ts or ""))
    if len(vals) < 2:
        return '<p class="muted tiny">Not enough points for a trend yet.</p>'
    body = sparkline(vals, w=max(w - 64, 200), h=max(h - 36, 80), color=color, fill=True)
    lo, hi, last = min(vals), max(vals), vals[-1]
    t0 = (labels[0] or "")[:10]
    t1 = (labels[-1] or "")[:10]
    return (
        '<div class="trend-wrap">'
        + '<div class="trend-y">' + '<span>' + e(axis_fmt(hi, money=money)) + '</span>'
        + '<span>' + e(axis_fmt(lo, money=money)) + '</span></div>'
        + '<div class="trend-plot">' + body + '<div class="trend-x">'
        + '<span>' + e(t0) + '</span>'
        + '<span>' + e(ylabel) + " " + e(axis_fmt(last, money=money)) + '</span>'
        + '<span>' + e(t1) + '</span></div></div></div>'
    )

def epoch_ring(pct_v) -> str:
    if pct_v is None:
        pct_v = 0
    pct_v = max(0.0, min(100.0, float(pct_v)))
    r = 42
    c = 2 * math.pi * r
    dash = c * pct_v / 100.0
    label = f"{pct_v:.1f}%"
    return (
        '<svg class="ring" viewBox="0 0 100 100" width="92" height="92">'
        f'<circle cx="50" cy="50" r="{r}" fill="none" stroke="#1c2430" stroke-width="8"/>'
        f'<circle cx="50" cy="50" r="{r}" fill="none" stroke="#3ee0b0" stroke-width="8" '
        f'stroke-linecap="round" stroke-dasharray="{dash:.2f} {c:.2f}" transform="rotate(-90 50 50)"/>'
        f'<text x="50" y="48" text-anchor="middle" fill="#e8eef7" font-size="15" font-weight="600">{label}</text>'
        '<text x="50" y="64" text-anchor="middle" fill="#8b98ab" font-size="8">EPOCH</text>'
        "</svg>"
    )


def score_ring(pct_v) -> str:
    if pct_v is None:
        pct_v = 0
    pct_v = max(0.0, min(100.0, float(pct_v)))
    r = 42
    c = 2 * 3.141592653589793 * r
    dash = c * pct_v / 100.0
    label = f"{pct_v:.0f}"
    return (
        '<svg class="ring" viewBox="0 0 100 100" width="72" height="72">'
        f'<circle cx="50" cy="50" r="{r}" fill="none" stroke="#1c2430" stroke-width="8"/>'
        f'<circle cx="50" cy="50" r="{r}" fill="none" stroke="#3ee0b0" stroke-width="8" '
        f'stroke-linecap="round" stroke-dasharray="{dash:.2f} {c:.2f}" transform="rotate(-90 50 50)"/>'
        f'<text x="50" y="54" text-anchor="middle" fill="#e8eef7" font-size="22" font-weight="600">{label}</text>'
        "</svg>"
    )


def stake_bars(top, total) -> str:
    if not top or not total:
        return '<p class="muted">Stake distribution unavailable.</p>'
    rows = []
    acc = 0.0
    for i, v in enumerate(top[:20]):
        share = (v.get("activated_stake_lamports") or 0) / total * 100.0
        acc += share
        node = e((v.get("node") or "")[:6])
        rows.append(
            f'<div class="bar-row" title="{e(v.get("node"))} {share:.2f}%">'
            f'<span class="bar-lab">{i+1:02d} {node}</span>'
            f'<span class="bar-track"><span class="bar-fill" style="width:{min(share*4.2,100):.2f}%"></span></span>'
            f'<span class="bar-n">{share:.2f}%</span></div>'
        )
    return f'<div class="bars">{"".join(rows)}</div><p class="muted tiny">Top 20 cumulative {acc:.1f}% of activated stake.</p>'


def comm_bars(buckets) -> str:
    if not buckets:
        return ""
    mx = max(buckets.values()) or 1
    parts = []
    for k in ("0", "1-5", "6-10", "11-50", "51-100"):
        n = buckets.get(k, 0)
        h = 8 + 52 * n / mx
        parts.append(
            f'<div class="hist-col"><div class="hist-bar" style="height:{h:.0f}px"></div>'
            f'<div class="hist-n">{n}</div><div class="hist-k">{e(k)}%</div></div>'
        )
    return f'<div class="hist">{"".join(parts)}</div>'

CSS = '\n:root {\n  --bg: #07090d; --bg2: #0c1017; --card: #10151e; --card2: #141b26;\n  --line: #1d2633; --line2: #2a3546; --text: #e8eef7; --muted: #8b98ab;\n  --faint: #5d6b80; --teal: #3ee0b0; --teal2: #1aa37d; --blue: #7aa2ff;\n  --amber: #f0b429; --rose: #ff6b8a; --violet: #b794f6;\n  --ok: #3ee0b0; --warn: #f0b429; --alert: #ff6b8a;\n}\n* { box-sizing: border-box; }\nhtml, body { margin: 0; padding: 0; background: var(--bg); color: var(--text);\n  font-family: "IBM Plex Sans", "Segoe UI", system-ui, sans-serif;\n  font-size: 14px; line-height: 1.45; }\nbody { min-height: 100vh; }\nbody::before {\n  content: ""; position: fixed; inset: 0; pointer-events: none; z-index: 0;\n  background:\n    radial-gradient(900px 420px at 8% -10%, rgba(62,224,176,.10), transparent 55%),\n    radial-gradient(700px 380px at 92% 0%, rgba(122,162,255,.10), transparent 50%),\n    radial-gradient(600px 400px at 70% 110%, rgba(183,148,246,.07), transparent 50%);\n}\n.wrap { position: relative; z-index: 1; max-width: 1280px; margin: 0 auto; padding: 20px 22px 64px; }\na { color: var(--blue); text-decoration: none; }\na:hover { text-decoration: underline; }\n.top {\n  display: grid; grid-template-columns: 1fr auto auto; gap: 18px; align-items: center;\n  padding: 14px 0 18px; border-bottom: 1px solid var(--line);\n}\n.brand { display: flex; gap: 12px; align-items: center; }\n.mark { width: 36px; height: 36px; }\n.brand h1 { margin: 0; font-size: 22px; letter-spacing: .08em; font-weight: 600; }\n.brand h1 span { color: var(--teal); }\n.tag { margin: 2px 0 0; color: var(--muted); font-size: 12.5px; }\n.health-pill {\n  display: flex; align-items: center; gap: 8px; padding: 8px 12px; border-radius: 999px;\n  border: 1px solid var(--line2); background: var(--card); font-size: 12px; letter-spacing: .04em;\n}\n.dot { width: 8px; height: 8px; border-radius: 50%; background: var(--ok); box-shadow: 0 0 10px var(--ok); }\n.dot.warn { background: var(--warn); box-shadow: 0 0 10px var(--warn); }\n.dot.alert { background: var(--alert); box-shadow: 0 0 10px var(--alert); }\n.meta-clock { text-align: right; color: var(--muted); font-variant-numeric: tabular-nums; font-size: 12px; }\n.meta-clock b { display: block; color: var(--text); font-size: 13px; font-weight: 550; }\n.tabs { display: flex; gap: 4px; margin: 16px 0 14px; flex-wrap: wrap; }\n.tabs button {\n  background: transparent; color: var(--muted); border: 1px solid var(--line);\n  border-radius: 8px; padding: 6px 11px; cursor: pointer; font: inherit;\n}\n.tabs button.on, .tabs button:hover { color: var(--text); border-color: var(--line2); background: var(--card); }\n.kpis { display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; }\n@media (max-width: 1100px) { .kpis { grid-template-columns: repeat(3, 1fr); } .top { grid-template-columns: 1fr; } }\n@media (max-width: 640px) { .kpis { grid-template-columns: repeat(2, 1fr); } }\n.card {\n  background: linear-gradient(180deg, var(--card) 0%, var(--bg2) 100%);\n  border: 1px solid var(--line); border-radius: 12px; padding: 12px 13px 11px;\n}\n.card.ghost { opacity: .55; border-style: dashed; }\n.card h3 { margin: 0 0 6px; font-size: 11px; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); font-weight: 550; }\n.val { font-size: 22px; font-weight: 600; font-variant-numeric: tabular-nums; letter-spacing: -0.02em; }\n.sub { color: var(--muted); font-size: 11.5px; margin-top: 4px; font-variant-numeric: tabular-nums; }\n.chip { display: inline-block; padding: 1px 7px; border-radius: 999px; font-size: 11px; font-variant-numeric: tabular-nums; }\n.chip.up { color: var(--teal); background: rgba(62,224,176,.1); }\n.chip.down { color: var(--rose); background: rgba(255,107,138,.1); }\n.chip.flat { color: var(--muted); background: #1a2130; }\n.grid2 { display: grid; grid-template-columns: 1.35fr .65fr; gap: 10px; margin-top: 10px; }\n.grid3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-top: 10px; }\n.grid21 { display: grid; grid-template-columns: 1.15fr .85fr; gap: 10px; margin-top: 10px; }\n@media (max-width: 900px) { .grid2, .grid3, .grid21 { grid-template-columns: 1fr; } }\n.panel { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 14px 16px; }\n.panel h2 { margin: 0 0 10px; font-size: 13px; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); font-weight: 600; }\n.flag { border-left: 3px solid var(--warn); padding: 8px 10px; margin: 0 0 8px; background: #16120a; border-radius: 0 8px 8px 0; }\n.flag.alert { border-color: var(--alert); background: #1a1014; }\n.flag.info { border-color: var(--blue); background: #10141c; }\n.flag b { display: block; font-size: 13px; }\n.flag p { margin: 3px 0 0; color: var(--muted); font-size: 12.5px; }\ntable { width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; font-size: 12.5px; }\nth { text-align: left; color: var(--faint); font-weight: 550; font-size: 11px; letter-spacing: .08em; text-transform: uppercase; padding: 6px 8px; border-bottom: 1px solid var(--line); cursor: pointer; user-select: none; }\ntd { padding: 7px 8px; border-bottom: 1px solid #151c26; }\ntr:hover td { background: #141b26; }\n.mono { font-family: "IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace; font-size: 12px; }\n.muted { color: var(--muted); }\n.tiny { font-size: 11px; }\n.right { text-align: right; }\n.tools { display: flex; gap: 8px; margin: 0 0 10px; }\n.tools input {\n  flex: 1; background: var(--bg); border: 1px solid var(--line); color: var(--text);\n  border-radius: 8px; padding: 7px 10px; font: inherit;\n}\n.bars { display: flex; flex-direction: column; gap: 4px; }\n.bar-row { display: grid; grid-template-columns: 86px 1fr 52px; gap: 8px; align-items: center; font-size: 11.5px; }\n.bar-lab { color: var(--muted); font-family: "IBM Plex Mono", ui-monospace, monospace; }\n.bar-track { height: 7px; background: #1a2230; border-radius: 99px; overflow: hidden; }\n.bar-fill { display: block; height: 100%; background: linear-gradient(90deg, #1aa37d, #3ee0b0); }\n.bar-n { text-align: right; font-variant-numeric: tabular-nums; }\n.hist { display: flex; gap: 12px; align-items: flex-end; height: 96px; }\n.hist-col { display: flex; flex-direction: column; align-items: center; gap: 4px; flex: 1; }\n.hist-bar { width: 100%; background: linear-gradient(180deg, #7aa2ff, #3ee0b0); border-radius: 5px 5px 0 0; }\n.hist-n { font-size: 11px; }\n.hist-k { font-size: 10px; color: var(--faint); }\n.news { list-style: none; margin: 0; padding: 0; }\n.news li { padding: 8px 0; border-bottom: 1px solid var(--line); }\n.news .src { color: var(--faint); font-size: 11px; letter-spacing: .08em; text-transform: uppercase; }\n.ed { border: 1px solid #2a3a28; background: linear-gradient(180deg, #101810, #0c1017); }\n.ed h2 { color: var(--teal); }\n.ed .warnish { color: var(--amber); font-size: 12.5px; }\n.omit { color: var(--faint); font-style: italic; }\n.footer { margin-top: 22px; color: var(--faint); font-size: 12px; border-top: 1px solid var(--line); padding-top: 14px; }\n.hidden { display: none; }\n.src-ok { color: var(--teal); }\n.src-fail { color: var(--rose); }\n.epochbox { display: flex; gap: 14px; align-items: center; }\n.spark { display: block; width: 100%; height: 48px; margin-top: 6px; }\n.ring { display: block; }\n.status-row { display: flex; flex-wrap: wrap; gap: 6px; margin: 8px 0 0; }\n.status-row span { border: 1px solid var(--line); border-radius: 999px; padding: 2px 8px; font-size: 11px; color: var(--muted); }\n.status-row span.ok { color: var(--teal); border-color: #1c3a32; }\nbutton.linkish {\n  background: var(--bg); color: var(--text); border: 1px solid var(--line2);\n  border-radius: 8px; padding: 6px 10px; cursor: pointer; font: inherit; font-size: 12px;\n}\n'
JS = '\n(function(){\n  var el = document.getElementById("snapshot");\n  var snap = JSON.parse(el.textContent);\n  function $$(s, root){ return Array.prototype.slice.call((root||document).querySelectorAll(s)); }\n  function $(s, root){ return (root||document).querySelector(s); }\n  $$(".tabs button").forEach(function(btn){\n    btn.addEventListener("click", function(){\n      $$(".tabs button").forEach(function(b){ b.classList.remove("on"); });\n      btn.classList.add("on");\n      var id = btn.getAttribute("data-tab");\n      $$("[data-panel]").forEach(function(p){\n        if (p.getAttribute("data-panel") === id) p.classList.remove("hidden");\n        else p.classList.add("hidden");\n      });\n    });\n  });\n  var q = $("#q");\n  var rows = $$("#vtable tbody tr");\n  if (q) q.addEventListener("input", function(){\n    var s = q.value.toLowerCase();\n    rows.forEach(function(r){ r.style.display = r.textContent.toLowerCase().indexOf(s) >= 0 ? "" : "none"; });\n  });\n  $$("#vtable th[data-k]").forEach(function(th){\n    th.addEventListener("click", function(){\n      var k = th.getAttribute("data-k");\n      var tbody = $("#vtable tbody");\n      var rs = $$("#vtable tbody tr");\n      var dir = th.getAttribute("data-dir") === "asc" ? "desc" : "asc";\n      $$("#vtable th").forEach(function(x){ x.removeAttribute("data-dir"); });\n      th.setAttribute("data-dir", dir);\n      rs.sort(function(a,b){\n        var av = a.getAttribute("data-"+k) || "";\n        var bv = b.getAttribute("data-"+k) || "";\n        var an = parseFloat(av), bn = parseFloat(bv);\n        var cmp = (!isNaN(an) && !isNaN(bn)) ? (an-bn) : av.localeCompare(bv);\n        return dir === "asc" ? cmp : -cmp;\n      }).forEach(function(r){ tbody.appendChild(r); });\n    });\n  });\n  var cj = document.getElementById("copyjson");\n  if (cj) cj.addEventListener("click", function(){\n    var txt = JSON.stringify(snap, null, 2);\n    if (navigator.clipboard && navigator.clipboard.writeText) {\n      navigator.clipboard.writeText(txt).then(function(){ cj.textContent = "Copied snapshot"; });\n    }\n  });\n})();\n'


CSS += """
.score-hero { display:flex; gap:12px; align-items:center; padding:8px 14px; border:1px solid var(--line2);
  border-radius:14px; background:linear-gradient(180deg,#121a14,#10151e); min-width:210px; }
.score-hero .val { font-size:28px; color:var(--teal); line-height:1; }
.score-parts { font-size:11px; color:var(--muted); line-height:1.4; }
.formula { font-family:"IBM Plex Mono", ui-monospace, monospace; font-size:10px; color:var(--faint);
  margin-top:6px; max-width:420px; }
.live-sol { display:none; margin-top:6px; font-size:11.5px; color:var(--muted); }
.live-sol.on { display:block; }
.tagchip { display:inline-block; margin:0 4px 0 0; padding:0 6px; border-radius:999px; font-size:10px;
  letter-spacing:.06em; text-transform:uppercase; color:var(--amber); border:1px solid #3a3220; }
.watching { color:var(--muted); font-size:13px; padding:6px 0 2px; }
.age { color:var(--teal); }
.score-hero .ring { width:64px; height:64px; }
.trend-grid { display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; margin-top:10px; }
@media (max-width: 980px) { .trend-grid { grid-template-columns:1fr; } }
.trend-wrap { display:grid; grid-template-columns:52px 1fr; gap:6px; align-items:stretch; }
.trend-y { display:flex; flex-direction:column; justify-content:space-between; color:var(--faint);
  font-size:10px; font-family:"IBM Plex Mono", ui-monospace, monospace; padding:8px 0 28px; text-align:right; }
.trend-plot .spark { height:128px; width:100%; margin-top:0; }
.trend-x { display:flex; justify-content:space-between; gap:8px; color:var(--faint); font-size:10px;
  font-family:"IBM Plex Mono", ui-monospace, monospace; margin-top:4px; }
.dune-frame { width:100%; min-height:560px; border:1px solid var(--line); border-radius:12px; background:#0b0f14; }
.burn-note { font-size:11px; color:var(--faint); margin-top:6px; word-break:break-all; }
.brief { display:grid; grid-template-columns:140px 140px 1fr 1fr; gap:10px; margin:14px 0 8px;
  padding:12px 14px; border:1px solid var(--line2); border-radius:14px;
  background:linear-gradient(180deg,#121a14,#0c1017); }
.brief .verdict { font-size:20px; font-weight:650; letter-spacing:.06em; }
.brief .verdict.HEALTHY { color:var(--teal); }
.brief .verdict.WATCH { color:var(--amber); }
.brief .verdict.DEGRADED, .brief .verdict.CRITICAL { color:var(--rose); }
.brief .verdict.SURGE, .brief .verdict.ELEVATED, .brief .verdict.FIRM { color:var(--teal); }
.brief .verdict.CONTRACTION, .brief .verdict.SOFT { color:var(--rose); }
.brief .verdict.QUIET, .brief .verdict.NORMAL, .brief .verdict.MIXED { color:var(--blue); }
.brief dl { margin:0; }
.brief dt { color:var(--faint); font-size:10px; letter-spacing:.1em; text-transform:uppercase; }
.brief dd { margin:2px 0 8px; font-size:13px; }
.insight { border-left:3px solid var(--teal); padding:6px 10px; margin:0 0 8px; background:#101810; border-radius:0 8px 8px 0; }
.meta-line { font-size:10px; color:var(--faint); margin-top:4px; }
.range-btns button { margin-right:4px; }
"""


JS = JS.replace("})();", "")
JS += """
  var ageEl = document.getElementById("age");
  var gen = (snap.meta && snap.meta.generated_at_utc) || "";
  function fmtAge(ms){
    var s = Math.floor(ms/1000);
    if (s < 60) return s + "s ago";
    if (s < 3600) return Math.floor(s/60) + "m ago";
    return Math.floor(s/3600) + "h " + Math.floor((s%3600)/60) + "m ago";
  }
  function tickAge(){
    if (!ageEl || !gen) return;
    var t0 = Date.parse(gen);
    if (isNaN(t0)) return;
    ageEl.textContent = fmtAge(Math.max(0, Date.now() - t0));
  }
  tickAge();
  setInterval(tickAge, 15000);
  var rb = document.getElementById("range-btns");
  if (rb) {
    rb.addEventListener("click", function(ev){
      var b = ev.target.closest("button[data-range]");
      if (!b) return;
      var r = b.getAttribute("data-range");
      rb.querySelectorAll("button").forEach(function(x){ x.classList.remove("on"); });
      b.classList.add("on");
      document.querySelectorAll(".range-grid").forEach(function(g){
        if (g.getAttribute("data-range") === r) g.classList.remove("hidden");
        else g.classList.add("hidden");
      });
    });
  }
  var live = document.getElementById("live-sol");
  if (live) {
    fetch("https://api.exchange.coinbase.com/products/SOL-USD/stats", {headers:{Accept:"application/json"}})
      .then(function(r){ if(!r.ok) throw new Error("http"); return r.json(); })
      .then(function(d){
        var last = parseFloat(d.last), openp = parseFloat(d.open);
        if (!isFinite(last) || !isFinite(openp) || !openp) return;
        var ch = (last-openp)/openp*100;
        var sign = ch>0?"+":"";
        var cls = ch>=0?"up":"down";
        live.innerHTML = "Live $" + last.toFixed(2) + " <span class=\\"chip " + cls + "\\">" + sign + ch.toFixed(2) + "%</span> · Coinbase · browser live vs snapshot";
        live.className = "live-sol on";
      })
      .catch(function(){ if (live.parentNode) live.parentNode.removeChild(live); });
  }
})();
"""

MARK = """<svg class="mark" viewBox="0 0 36 36" aria-hidden="true">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#3ee0b0"/><stop offset="1" stop-color="#7aa2ff"/>
  </linearGradient></defs>
  <rect x="1" y="1" width="34" height="34" rx="9" fill="#0c1017" stroke="url(#g)"/>
  <path d="M18 7 L22 15 L31 16 L24 22 L26 31 L18 26 L10 31 L12 22 L5 16 L14 15 Z" fill="url(#g)"/>
</svg>"""


def tile(title, value, sub="", chip=None, ghost=False, spark="", source=None, conf=None, extra=""):
    cls = "card ghost" if ghost else "card"
    chip_html = ""
    if chip is not None:
        chip_html = f'<span class="chip {delta_class(chip)}">{pct(chip)}</span>'
    sub_html = f'<div class="sub">{sub} {chip_html}</div>' if (sub or chip is not None) else ""
    prov = provenance(source, conf, extra)
    return f'<article class="{cls}"><h3>{e(title)}</h3><div class="val">{value}</div>{sub_html}{prov}{spark}</article>'


def provenance(source=None, conf=None, extra=""):
    bits = [x for x in (source, conf, extra) if x]
    if not bits:
        return ""
    return '<div class="meta-line">' + e(" · ".join(str(b) for b in bits)) + "</div>"


def render_html(snap: dict) -> str:
    m = snap.get("meta") or {}
    c = snap.get("cluster") or {}
    v = snap.get("validators") or {}
    px = snap.get("market") or {}
    d = snap.get("defi") or {}
    st = snap.get("stablecoins") or {}
    act = snap.get("activity") or {}
    news = snap.get("news") or {}
    flags = snap.get("anomalies") or []
    ed = snap.get("editorial") or {}
    om = snap.get("omissions") or []
    status = news.get("status") or {}
    scom = snap.get("solana_com_data") or {}
    hs = snap.get("health_score") or {}
    eco = snap.get("economics") or {}
    hist = snap.get("history") or []
    inc = snap.get("incinerator") or {}
    trends = snap.get("trends") or {}
    dune = snap.get("dune") or {}
    chart = trends.get("chart") or {}
    brief = snap.get("brief") or {}
    xs = snap.get("xstocks") or {}
    insights = snap.get("insights") or []
    txf = snap.get("tx_fees") or {}
    dh = snap.get("data_health") or {}
    eco = snap.get("economics") or eco

    health = c.get("health")
    health_ok = health == "ok"
    worst = None
    if flags:
        if any(f.get("severity") == "alert" for f in flags):
            worst = "alert"
        elif any(f.get("severity") == "warn" for f in flags):
            worst = "warn"
    dot = "alert" if (not health_ok or worst == "alert") else ("warn" if worst == "warn" else "")
    health_label = "RPC " + (health if health is not None else "unavailable")
    if flags:
        health_label += f" · {len(flags)} flag{'s' if len(flags)!=1 else ''}"

    tps_vals = [r.get("tps_total") for r in reversed(c.get("tps_samples") or [])]
    tps_spark = sparkline([x for x in tps_vals if isinstance(x, (int, float))], color="#3ee0b0")
    nv_vals = [r.get("tps_nonvote") for r in reversed(c.get("tps_samples") or [])]
    nv_spark = sparkline([x for x in nv_vals if isinstance(x, (int, float))], color="#7aa2ff")
    st_vals = [((r.get("slot_time_sec") or 0) * 1000) for r in reversed(c.get("tps_samples") or [])]
    st_spark = sparkline([x for x in st_vals if x], color="#b794f6")
    tvl_spark = sparkline([x.get("tvl") for x in (d.get("tvl_history") or []) if isinstance(x.get("tvl"), (int, float))], color="#f0b429")
    stab_spark = sparkline([x.get("circulating_usd") for x in (st.get("history") or []) if isinstance(x.get("circulating_usd"), (int, float))], color="#3ee0b0")

    daa = act.get("active_addresses") or {}
    daa_ghost = daa.get("headline_value") is None
    daa_sub = "no public source" if daa_ghost else (
        f"{e(daa.get('headline_provider'))} · {e(daa.get('headline_date'))}"
        + (f" · range {nfmt(daa.get('min'))}–{nfmt(daa.get('max'))}" if daa.get("min") is not None else "")
    )

    px_ghost = px.get("usd") is None
    tvl_ghost = d.get("tvl_usd") is None
    stab_ghost = not st.get("ok")
    rwa = d.get("rwa") or {}
    rwa_ghost = rwa.get("tvl_usd") is None

    age = (m.get("generated_at_utc") or m.get("generated_at") or "this snapshot")
    hc = (dh.get("headline_confidence") or "MED")
    fee_conf = "HIGH" if (eco.get("median_tx_fee_n") or 0) and eco.get("median_tx_fee_n") >= 200 else (
        "MED" if eco.get("median_tx_fee_sol") is not None else "LOW"
    )
    xs_conf = "MED" if xs.get("market_cap_usd") is not None else "LOW"
    kpis = "".join([
        tile("TPS", nfmt(c.get("tps_total"), 0),
             f"median {nfmt(c.get('tps_median'), 0)} · {nfmt(c.get('performance_window_sec'))}s window",
             spark=tps_spark, source="getRecentPerformanceSamples", conf="HIGH", extra=age),
        tile("Non-vote TPS", nfmt(c.get("tps_nonvote"), 0), "from numNonVoteTransactions", spark=nv_spark,
             source="getRecentPerformanceSamples", conf="HIGH", extra=age),
        tile("Slot time", (nfmt((c.get("slot_time_sec") or 0)*1000, 1) + " ms") if c.get("slot_time_sec") else "—",
             f"median {nfmt((c.get('slot_time_median') or 0)*1000, 1)} ms · max {nfmt((c.get('slot_time_max') or 0)*1000, 1)}",
             spark=st_spark, source="getRecentPerformanceSamples", conf="HIGH", extra=age),
        tile("SOL", usd(px.get("usd"), 2) if not px_ghost else "—",
             (px.get("usd_24h_change_source") or px.get("source") or "price") if not px_ghost else "price omitted",
             chip=px.get("usd_24h_change"), ghost=px_ghost,
             source=px.get("usd_24h_change_source") or px.get("source") or "Coinbase/Kraken",
             conf=("MED" if "fallback" in str(px.get("usd_24h_change_source") or "").lower() or "coinbase" in str(px.get("source") or "").lower() else hc),
             extra=age),
        tile("Median tx fee",
             ((nfmt(eco.get("median_tx_fee_sol"), 6) + " SOL") if eco.get("median_tx_fee_sol") is not None else "—"),
             (f"p90 {nfmt(eco.get('median_tx_fee_p90_sol'), 6)} · n_tx={nfmt(eco.get('median_tx_fee_n'))} · window_seconds={nfmt(eco.get('median_tx_fee_window_seconds'))}"
              if eco.get("median_tx_fee_sol") is not None else "getBlock sample omitted"),
             ghost=eco.get("median_tx_fee_sol") is None,
             source="RPC getBlock meta.fee time-stratified", conf=fee_conf, extra=age),
        tile("Borealis REV 24h",
             usd(eco.get("rev_24h_usd")) if eco.get("rev_24h_usd") is not None else "—",
             (eco.get("rev_kind") or eco.get("rev_label") or "in-protocol fees + Jito tips"),
             ghost=eco.get("rev_24h_usd") is None,
             source="solana.com Fees + Jito tip-floor estimate; NOT DeFiLlama protocol fees",
             conf="MED", extra=age),
        tile("TVL", usd(d.get("tvl_usd")) if not tvl_ghost else "—",
             "DeFiLlama chain TVL", chip=d.get("tvl_change_1d_pct"), ghost=tvl_ghost, spark=tvl_spark,
             source="api.llama.fi/v2/chains", conf="HIGH", extra=age),
        tile("DEX 24h", usd((d.get("dex") or {}).get("total_24h_usd")),
             f"7d {usd((d.get('dex') or {}).get('total_7d_usd'))}",
             chip=(d.get("dex") or {}).get("change_1d_pct"),
             source="api.llama.fi/overview/dexs/Solana", conf="HIGH", extra=age),
        tile("Stables", usd(st.get("circulating_usd")) if not stab_ghost else "—",
             "Solana pegged-USD", chip=st.get("change_1d_pct"), ghost=stab_ghost, spark=stab_spark,
             source="stablecoins.llama.fi", conf="HIGH", extra=age),
        tile("RWA TVL", usd(rwa.get("tvl_usd")) if not rwa_ghost else "—",
             f"{nfmt(rwa.get('protocol_count'))} RWA protocols on Solana (DeFiLlama, not equities)", ghost=rwa_ghost,
             source="DeFiLlama RWA category TVL", conf="MED", extra=age),
        tile("xStocks vol 24h",
             usd(xs.get("volume_24h_usd")) if xs.get("volume_24h_usd") is not None else "—",
             (xs.get("volume_kind") or "tokenized-equity DEX volume, priced subset"),
             ghost=xs.get("volume_24h_usd") is None,
             source=xs.get("volume_source") or "Jupiter lite-api stats24h", conf="MED", extra=age),
        tile("xStocks mcap",
             usd(xs.get("market_cap_usd")) if xs.get("market_cap_usd") is not None else "—",
             f"priced {nfmt(xs.get('count_priced'))} of {nfmt(xs.get('count_solana'))} Solana listings · lower bound",
             ghost=xs.get("market_cap_usd") is None,
             source="xStocks public API · quote × circulating × multiplier (not a 715 census)", conf=xs_conf, extra=age),
        tile("Active addrs", nfmt(daa.get("headline_value")) if not daa_ghost else "—",
             daa_sub, ghost=daa_ghost,
             source="solana.com/data Active Addresses", conf="MED", extra=age),
        tile("Validators", nfmt(v.get("active_count")),
             f"delinquent {nfmt(v.get('delinquent_count'))} · {pct(v.get('delinquent_stake_pct'), 3)} stake",
             source="getVoteAccounts", conf="HIGH", extra=age),
        tile("Nakamoto 33%", nfmt(v.get("nakamoto_33")),
             f"50% {nfmt(v.get('nakamoto_50'))} · 67% {nfmt(v.get('supermajority_67'))}",
             source="derived from getVoteAccounts stake", conf="HIGH", extra=age),
        tile("Burned SOL",
             (nfmt(inc.get("sol"), 2) + " SOL") if inc.get("ok") and inc.get("sol") is not None else "—",
             "incinerator getBalance · Foundation burn address",
             ghost=not inc.get("ok"),
             source="getBalance incinerator", conf=("HIGH" if inc.get("ok") else "LOW"), extra=age),
    ])

    n_samples = len(c.get("tps_samples") or [])
    empty_copy = (snap.get("baseline") or {}).get("empty_copy") or (
        f"No flags vs rolling baseline ({n_samples} samples / llama 7d). Watching."
    )
    flag_html = f'<p class="watching">{e(empty_copy)}</p>'
    if flags:
        bits = []
        for f in flags:
            bits.append(
                f'<div class="flag {e(f.get("severity"))}"><b>{e(f.get("severity"," ").upper())} · {e(f.get("title"))}</b>'
                f'<p>{e(f.get("detail"))}</p>'
                f'<p class="tiny">threshold {e(f.get("threshold"))} · {e(f.get("flagged_at"))}</p></div>'
            )
        flag_html = "".join(bits)

    supply = c.get("supply") or {}
    epoch_html = (
        '<div class="epochbox">' + epoch_ring(c.get("epoch_progress_pct")) +
        f'<div><div class="val">Epoch {nfmt(c.get("epoch"))}</div>'
        f'<div class="sub">slot {nfmt(c.get("slot_index"))} / {nfmt(c.get("slots_in_epoch"))}</div>'
        f'<div class="sub">block time {e(c.get("block_time_utc") or "—")}</div>'
        f'<div class="sub">circulating {nfmt(supply.get("circulating_sol"))} SOL</div></div></div>'
    )

    # validators table
    trs = []
    for row in (v.get("top") or []):
        trs.append(
            "<tr "
            f'data-rank="{row.get("rank") or 0}" '
            f'data-stake="{row.get("activated_stake_lamports") or 0}" '
            f'data-share="{row.get("stake_share_pct") or 0}" '
            f'data-commission="{row.get("commission") or 0}" '
            f'data-lag="{row.get("lag_slots") or 0}">'
            f'<td>{row.get("rank")}</td>'
            f'<td class="mono" title="{e(row.get("node"))}">{e((row.get("node") or "")[:8])}…</td>'
            f'<td class="right">{nfmt((row.get("activated_stake_lamports") or 0)/LAMPORTS, 0)}</td>'
            f'<td class="right">{nfmt(row.get("stake_share_pct"), 2)}%</td>'
            f'<td class="right">{row.get("commission")}%</td>'
            f'<td class="right">{row.get("lag_slots") if row.get("lag_slots") is not None else "—"}</td>'
            "</tr>"
        )
    del_html = "".join(
        f'<li class="mono">{e((r.get("node") or "")[:8])}… · {nfmt((r.get("activated_stake_lamports") or 0)/LAMPORTS, 0)} SOL · '
        f'comm {r.get("commission")}% · lag {r.get("lag_slots")}</li>'
        for r in (v.get("delinquent") or [])[:12]
    ) or '<li class="muted">None in the RPC delinquent set.</li>'

    dex_trs = "".join(
        f'<tr><td>{e(p.get("name"))}</td><td class="right">{usd(p.get("total_24h_usd"))}</td>'
        f'<td class="right"><span class="chip {delta_class(p.get("change_1d_pct"))}">{pct(p.get("change_1d_pct"))}</span></td></tr>'
        for p in (d.get("top_dexs") or [])[:10]
    )
    proto_trs = "".join(
        f'<tr><td>{e(p.get("name"))}</td><td class="muted">{e(p.get("category"))}</td>'
        f'<td class="right">{usd(p.get("solana_tvl_usd"))}</td>'
        f'<td class="right"><span class="chip {delta_class(p.get("change_1d_pct"))}">{pct(p.get("change_1d_pct"))}</span></td>'
        f'<td class="right">{pct(p.get("change_7d_pct"))}</td></tr>'
        for p in (d.get("top_protocols") or [])[:12]
    )
    stab_trs = "".join(
        f'<tr><td>{e(p.get("symbol"))}</td><td class="muted">{e(p.get("name"))}</td>'
        f'<td class="right">{usd(p.get("circulating_usd"))}</td>'
        f'<td class="right">{pct(p.get("change_1d_pct"))}</td></tr>'
        for p in (st.get("top") or [])[:8]
    )
    rwa_lis = "".join(
        f'<li><b>{e(p.get("name"))}</b> <span class="muted">{e(p.get("category"))}</span> · {usd(p.get("solana_tvl_usd"))}</li>'
        for p in (rwa.get("top") or [])[:8]
    ) or '<li class="omit">RWA list unavailable this run.</li>'

    def news_li(n):
        tags = "".join(f'<span class="tagchip">{e(x)}</span>' for x in (n.get("tags") or []))
        return (
            f'<li><div class="src">{e(n.get("source"))} · {e(n.get("published"))} {tags}</div>'
            f'<a href="{e(n.get("url"))}" rel="noopener">{e(n.get("title"))}</a></li>'
        )
    tw_lis = "".join(news_li(n) for n in (news.get("twitter") or [])[:10]) or (
        '<li class="omit">No public X/Nitter-style RSS this run (403/gated skipped).</li>'
    )
    news_lis = "".join(news_li(n) for n in (news.get("current_news") or news.get("official") or [])[:12]) or (
        '<li class="omit">No current RSS items this run.</li>'
    )
    active_lis = "".join(news_li(n) for n in (news.get("active_incidents") or [])[:8]) or (
        '<li class="omit">No open incidents.</li>'
    )
    resolved_lis = "".join(news_li(n) for n in (news.get("recent_resolved") or [])[:8]) or (
        '<li class="omit">No recently resolved incidents in the recency window.</li>'
    )
    archive_lis = "".join(news_li(n) for n in (news.get("archive") or [])[:6]) or (
        '<li class="omit">No archive items.</li>'
    )

    comps = "".join(
        f'<span class="{"ok" if (x.get("status")=="operational") else ""}">{e(x.get("name"))}: {e(x.get("status"))}</span>'
        for x in (status.get("components") or [])[:10]
    )

    rpc_rows = "".join(
        "<tr>"
        f'<td class="mono">{e(r.get("provider"))}</td>'
        f'<td class="right">{nfmt(((r.get("RPC Avg Latency") or {}).get("value")), 2)}</td>'
        f'<td class="right">{nfmt(((r.get("RPC P95 Latency") or {}).get("value")), 1)}</td>'
        f'<td class="right">{nfmt(((r.get("RPC Error Rate") or {}).get("value")), 2)}</td>'
        "</tr>"
        for r in (scom.get("rpc_providers") or [])
    )

    src_rows = "".join(
        "<tr>"
        f'<td class="mono">{e(s.get("id"))}</td>'
        f'<td class="{"src-ok" if s.get("ok") else "src-fail"}">{"ok" if s.get("ok") else "FAIL"}</td>'
        f'<td class="right">{s.get("status") or "—"}</td>'
        f'<td class="right">{s.get("ms")}ms</td>'
        f'<td class="tiny muted">{e(s.get("error") or s.get("url"))}</td>'
        "</tr>"
        for s in (snap.get("sources") or [])
    )
    om_lis = "".join(f'<li><b>{e(o.get("metric"))}</b> — {e(o.get("reason"))}</li>' for o in om) or "<li>None.</li>"

    simd = "".join(f'<li><b>{e(s.get("id"))}</b> — {e(s.get("name"))}</li>' for s in (ed.get("simds") or []))
    tl = "".join(f'<li><span class="mono">{e(t.get("date"))}</span> — {e(t.get("item"))}</li>' for t in (ed.get("timeline_public") or []))
    watch = "".join(f'<li>{e(w)}</li>' for w in (ed.get("watch") or []))
    ed_src = "".join(f'<li><a href="{e(u)}">{e(u)}</a></li>' for u in (ed.get("sources") or []))

    daa_note = e(daa.get("note") or "")
    hist_spark_tps = sparkline(
        [x.get("tps") for x in hist if isinstance(x.get("tps"), (int, float))],
        w=280, h=42, color="#3ee0b0",
    )
    hist_spark_px = sparkline(
        [x.get("sol_usd") for x in hist if isinstance(x.get("sol_usd"), (int, float))],
        w=280, h=42, color="#f0b429",
    )
    parts = hs.get("parts") or []
    parts_txt = " · ".join(
        f"{p.get('id')} {p.get('points')}/{p.get('max')}" for p in parts
    )
    score_n = hs.get("score")
    score_cls = "" if isinstance(score_n, (int, float)) and score_n >= 80 else "warn"
    if isinstance(score_n, (int, float)) and score_n < 55:
        score_cls = "alert"
    score_hero = (
        f'<div class="score-hero">{score_ring(score_n if score_n is not None else 0)}'
        f'<div><div class="tiny muted">HEALTH SCORE</div>'
        f'<div class="val">{e(score_n if score_n is not None else "—")}</div>'
        f'<div class="score-parts">{e(parts_txt)}</div>'
        f'<p class="formula">{e(hs.get("formula") or "")}</p></div></div>'
    )
    dune_html = ''
    if dune.get('ok') and dune.get('embed_url'):
        dune_html = (
            '<div class="panel" style="margin-top:10px">'
            + '<h2>Public Dune embed</h2>'
            + '<p class="tiny muted">'
            + e(dune.get('label') or 'public Dune embed, not our query') + ' — '
            + e(dune.get('title') or '') + '</p>'
            + '<iframe class="dune-frame" title="public Dune embed, not our query" loading="lazy" referrerpolicy="no-referrer" sandbox="allow-scripts allow-same-origin allow-popups" src="' + e(dune.get('embed_url')) + '"></iframe>'
            + '<p class="tiny muted">' + '<a href="' + e(dune.get('dashboard_url') or '') + '" rel="noopener">Open on Dune</a> · no API key</p>'
            + '</div>'
        )
    else:
        dune_html = (
            '<div class="panel" style="margin-top:10px">'
            + '<h2>Public Dune embed</h2>'
            + '<p class="omit">' + e(dune.get('error') or 'Public Dune embed skipped (no key, embed did not return 200).') + '</p></div>'
        )


    vrd = e(brief.get("network_health") or brief.get("verdict") or "WATCH")
    actl = e(brief.get("ecosystem_activity") or "NORMAL")
    brief_html = (
        f'<section class="brief" aria-label="executive view">'
        f'<div><div class="tiny muted">NETWORK HEALTH</div>'
        f'<div class="verdict {vrd}">{vrd}</div>'
        f'<div class="tiny muted">score {e(brief.get("score"))} · RPC/slot/TPS/delinquency</div></div>'
        f'<div><div class="tiny muted">ECOSYSTEM</div>'
        f'<div class="verdict {actl}">{actl}</div>'
        f'<div class="tiny muted">DEX/TVL/DAA · {e(brief.get("market_posture") or "")}</div></div>'
        f'<dl><dt>What changed</dt><dd>{e(brief.get("what_changed"))}</dd>'
        f'<dt>Why it matters</dt><dd>{e(brief.get("why_it_matters"))}</dd></dl>'
        f'<dl><dt>Biggest positive</dt><dd>{e(brief.get("biggest_positive"))}</dd>'
        f'<dt>Biggest risk</dt><dd>{e(brief.get("biggest_risk"))}</dd></dl>'
        f'</section>'
    )
    ins_bits = []
    for ins in insights[:6]:
        ins_bits.append(
            f'<div class="insight"><b>{e(ins.get("title"))}</b>'
            f'<p>{e(ins.get("detail"))}</p>'
            f'<p class="tiny muted">evidence: {e(", ".join(ins.get("evidence") or []))}</p></div>'
        )
    insight_html = "".join(ins_bits) or '<p class="watching">No insight lines this run.</p>'
    xs_rows = "".join(
        f'<tr><td>{e(a.get("symbol"))}</td><td>{e(a.get("name"))}</td>'
        f'<td class="right">{usd(a.get("quote"), 2)}</td>'
        f'<td class="right">{nfmt(a.get("circulating"), 2)}</td>'
        f'<td class="right">{nfmt(a.get("multiplier"), 4)}</td>'
        f'<td class="right">{usd(a.get("mcap_usd"))}</td></tr>'
        for a in (xs.get("top") or [])[:10]
    )
    fee_box = (
        f'<div class="panel"><h2>Sampled tx fees (getBlock meta.fee)</h2>'
        f'<p class="val">{nfmt(eco.get("median_tx_fee_sol"), 6)} SOL'
        f' <span class="muted">p50</span> · {usd(eco.get("median_tx_fee_usd"), 4)}</p>'
        f'<p class="sub">p90 {nfmt(eco.get("median_tx_fee_p90_sol"), 6)} · p99 {nfmt(eco.get("median_tx_fee_p99_sol"), 6)} SOL'
        f' · n_tx={nfmt(eco.get("median_tx_fee_n"))} · window_seconds={nfmt(eco.get("median_tx_fee_window_seconds"))}'
        f' · slots {e(eco.get("median_tx_fee_slots"))}</p>'
        f'<p class="tiny muted">{e(eco.get("median_tx_fee_note"))}</p>'
        f'<p class="tiny muted">Priority p50 {nfmt(eco.get("priority_p50_sol"), 6)} SOL · {e(eco.get("priority_note"))}</p>'
        f'</div>'
    )
    jt = eco.get("jito") or {}
    if jt.get("ok") and jt.get("landed_p50_sol") is not None:
        jito_cell = f'{nfmt(jt.get("landed_p50_sol"), 6)} SOL p50 landed · p95 {nfmt(jt.get("landed_p95_sol"), 6)}'
    else:
        jito_cell = e(jt.get("reason") or "omitted")
    eco_box = (
        f'<div class="panel"><h2>Borealis REV 24h</h2>'
        f'<p class="val">{usd(eco.get("rev_24h_usd"))}</p>'
        f'<p class="sub">{e(eco.get("rev_kind") or "")}</p>'
        f'<table><tbody>'
        f'<tr><td>In-protocol network fees 24h</td><td class="right">{nfmt(eco.get("network_fees_sol_24h"), 1)} SOL'
        f' ({usd(eco.get("network_fees_usd_24h"))}) · MEASURED</td></tr>'
        f'<tr><td>Jito tips 24h</td><td class="right">{usd((eco.get("jito") or {}).get("tips_24h_usd"))}'
        f' · {e((eco.get("jito") or {}).get("tips_24h_kind") or "omitted")}</td></tr>'
        f'<tr><td>Protocol fees 24h</td><td class="right">{usd(eco.get("protocol_fees_usd"))} · EXCLUDED</td></tr>'
        f'<tr><td>Jito tip floor</td><td class="right">{jito_cell}</td></tr>'
        f'</tbody></table>'
        f'<p class="tiny muted">{e(eco.get("rev_definition") or "")} '
        f'Protocol fees are DeFiLlama application fees and are not summed into REV.</p></div>'
    )
    xs_box = (
        f'<div class="panel"><h2>Tokenized equities · xStocks</h2>'
        f'<p>24h volume {usd(xs.get("volume_24h_usd"))} · priced-subset mcap {usd(xs.get("market_cap_usd"))}</p>'
        f'<p class="tiny muted">{e(xs.get("count_meaning") or "")} Priced {nfmt(xs.get("count_priced"))} of '
        f'{nfmt(xs.get("count_solana"))} Solana listings ({nfmt(xs.get("count_unique_underlying"))} unique underlyings). '
        f'{e(xs.get("volume_coverage") or xs.get("mcap_note") or "")}</p>'
        f'<table><thead><tr><th>Sym</th><th>Name</th><th class="right">Quote</th>'
        f'<th class="right">Circ</th><th class="right">Mult</th><th class="right">Mcap</th></tr></thead>'
        f'<tbody>{xs_rows or "<tr><td colspan=6 class=omit>No priced xStocks this run.</td></tr>"}</tbody></table></div>'
    )
    dh_fail = "".join(
        f'<li><b>{e(x.get("id"))}</b> — {e(x.get("error") or x.get("status"))}</li>'
        for x in (dh.get("failures") or [])[:8]
    )
    dh_html = (
        f'<div class="panel" style="margin-top:10px"><h2>Data health</h2>'
        f'<p>{e(dh.get("headline") or ("sources " + str(dh.get("ok")) + "/" + str(dh.get("total"))))} · headline confidence {e(dh.get("headline_confidence"))}</p>'
        f'<ul>{dh_fail or "<li>No fetch failures this run.</li>"}</ul></div>'
    )


    def _tail(pts, n):
        pts = pts or []
        return pts[-n:] if n and len(pts) > n else pts
    daily = trends.get("daily") or {}
    runp = trends.get("run") or {}
    has_90d = len(daily.get("tvl") or []) >= 60
    range_sets = {
        "24h": (runp.get("tps") or _tail(daily.get("tps"), 2),
                runp.get("tvl") or _tail(daily.get("tvl"), 2),
                runp.get("sol") or _tail(daily.get("sol"), 2),
                "15-min tape or last daily points"),
        "7d": (_tail(daily.get("tps"), 7), _tail(daily.get("tvl"), 7), _tail(daily.get("sol"), 7),
               "daily seed 7d"),
        "30d": (_tail(daily.get("tps"), 30), _tail(daily.get("tvl"), 30), _tail(daily.get("sol"), 30),
                "daily seed 30d"),
    }
    if has_90d:
        range_sets["90d"] = (_tail(daily.get("tps"), 90), _tail(daily.get("tvl"), 90), _tail(daily.get("sol"), 90),
                             "90d where the series exists (TVL llama); TPS/SOL public feeds are 30d")
    range_bits = []
    for key, (tp, tv, so, lab) in range_sets.items():
        hide = "" if key == "30d" else " hidden"
        range_bits.append(
            f'<div class="trend-grid range-grid{hide}" data-range="{key}">'
            f'<div class="trend-card"><h3>TPS {key}</h3>{trend_chart(tp, color="#3ee0b0", ylabel="TPS")}'
            f'<p class="tiny muted">{e(lab)}</p></div>'
            f'<div class="trend-card"><h3>TVL {key}</h3>{trend_chart(tv, color="#f0b429", ylabel="TVL", money=True)}'
            f'<p class="tiny muted">{e(lab)}</p></div>'
            f'<div class="trend-card"><h3>SOL {key}</h3>{trend_chart(so, color="#7aa2ff", ylabel="SOL", money=True)}'
            f'<p class="tiny muted">{e(lab)}</p></div></div>'
        )
    range_html = "".join(range_bits)

    payload = json.dumps({
        "meta": m,
        "anomalies": flags,
        "validators_top": v.get("top") or [],
        "omissions": om,
        "health_score": hs,
        "market": {"usd": px.get("usd"), "usd_24h_change": px.get("usd_24h_change"),
                   "source": px.get("source")},
    }, default=str).replace("<", "\\u003c")

    title = f"Borealis — Solana {m.get('generated_at_utc') or ''}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="color-scheme" content="dark"/>
<meta name="description" content="Borealis — live Solana cluster and ecosystem report. No API keys. Updates every 15 minutes."/>
<meta property="og:title" content="Borealis — live Solana cluster report"/>
<meta property="og:description" content="Public RPC, DeFiLlama, Coinbase 24h, solana.com/data, and Nitter-style X RSS. Health score, anomalies, no API keys."/>
<meta property="og:type" content="website"/>
<meta property="og:url" content="https://dustycompiler.github.io/borealis-solana/"/>
<meta property="og:image" content="https://dustycompiler.github.io/borealis-solana/favicon.svg"/>
<meta name="twitter:card" content="summary"/>
<title>{e(title)}</title>
<link rel="icon" href="favicon.svg" type="image/svg+xml"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet"/>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
  <header class="top">
    <div class="brand">{MARK}
      <div>
        <h1>BOREAL<span>IS</span></h1>
        <p class="tag">Live Solana cluster &amp; ecosystem report · Superteam Canada bounty build · no API keys</p>
      </div>
    </div>
    {score_hero}
    <div class="meta-clock">
      <b>{e(m.get("generated_at_utc"))}</b>
      {e(m.get("generated_at_pt"))}<br/>
      snapshot <span id="age" class="age">just now</span>
      · updates every 15 min via GitHub Action<br/>
      <span class="tiny">{e(health_label)}</span>
      · run {e(m.get("run_id"))} · v{e(m.get("version"))}
      <div id="live-sol" class="live-sol"></div>
    </div>
  </header>
  {brief_html}

  <nav class="tabs">
    <button class="on" data-tab="overview">Overview</button>
    <button data-tab="validators">Validators</button>
    <button data-tab="defi">DeFi &amp; assets</button>
    <button data-tab="news">News &amp; status</button>
    <button data-tab="anomalies">Anomalies</button>
    <button data-tab="trends">Trends</button>
    <button data-tab="sources">Sources</button>
  </nav>

  <section data-panel="overview">
    <div class="kpis">{kpis}</div>
    <div class="panel" style="margin-top:10px">
      <h2>Borealis Intelligence</h2>
      {insight_html}
    </div>
    <div class="grid3" style="margin-top:10px">{fee_box}{eco_box}{xs_box}</div>
    <div class="panel" style="margin-top:10px">
      <h2>Trends · TPS / TVL / SOL</h2>
      <p class="tiny muted">{e((trends or {}).get("note") or "")}</p>
      <div class="range-btns tools" id="range-btns">
        <button class="linkish" type="button" data-range="24h">24h</button>
        <button class="linkish" type="button" data-range="7d">7d</button>
        <button class="linkish on" type="button" data-range="30d">30d</button>
        {('<button class="linkish" type="button" data-range="90d">90d</button>' if has_90d else "")}
      </div>
      {range_html}
    </div>
    <div class="grid2">
      <div class="panel">
        <h2>Anomaly strip</h2>
        {flag_html}
        <p class="tiny muted">History TPS</p>
        {hist_spark_tps}
        <p class="tiny muted">History SOL</p>
        {hist_spark_px}
        <p class="tiny muted">data/history.jsonl n={len(hist)} · last-sample 2.5σ · llama 1d/7d · multi-source correlation</p>
      </div>
      <div class="panel">
        <h2>Epoch</h2>
        {epoch_html}
        <p class="tiny muted" style="margin-top:10px">status.solana.com: {e(status.get("description") or "—")} ({e(status.get("indicator") or "—")})</p>
        <div class="status-row">{comps}</div>
      </div>
    </div>
    <div class="grid21">
      <div class="panel">
        <h2>Stake concentration (top 20)</h2>
        {stake_bars(v.get("top") or [], v.get("activated_stake_lamports"))}
      </div>
      <div class="panel">
        <h2>Commission buckets</h2>
        {comm_bars(v.get("commission_buckets") or {})}
        <p class="tiny muted">min {v.get("commission_min")}% · median {nfmt(v.get("commission_median"),1)}% · max {v.get("commission_max")}%</p>
        <p class="tiny muted">top 10 share {nfmt(v.get("top10_share_pct"),2)}% · top 20 {nfmt(v.get("top20_share_pct"),2)}%</p>
      </div>
    </div>
    <div class="panel ed" style="margin-top:10px">
      <h2>Editorial · {e(ed.get("title"))}</h2>
      <p class="tiny muted">As of {e(ed.get("as_of"))} ({e(ed.get("as_of_pt"))}). {e(ed.get("disclaimer"))}</p>
      <p class="warnish">{e(ed.get("correction"))}</p>
      <p>{e(ed.get("summary"))}</p>
      <ul>{simd}</ul>
      <h2>Public timeline</h2>
      <ul>{tl}</ul>
      <h2>Watch</h2>
      <ul>{watch}</ul>
      <ul class="tiny">{ed_src}</ul>
    </div>
  </section>

  <section class="hidden" data-panel="validators">
    <div class="panel">
      <h2>Vote accounts · click headers to sort · type to filter</h2>
      <div class="tools">
        <input id="q" placeholder="Filter node / vote pubkey…  (table is the top 40 by stake)"/>
      </div>
      <table id="vtable">
        <thead><tr>
          <th data-k="rank">Rank</th><th>Node</th>
          <th data-k="stake" class="right">Stake (SOL)</th>
          <th data-k="share" class="right">Share</th>
          <th data-k="commission" class="right">Comm</th>
          <th data-k="lag" class="right">Lag slots</th>
        </tr></thead>
        <tbody>{"".join(trs)}</tbody>
      </table>
    </div>
    <div class="panel" style="margin-top:10px">
      <h2>Delinquency alerts</h2>
      <ul>{del_html}</ul>
      <p class="tiny muted">Lagging current (&gt;150 slots behind getSlot) among otherwise-current accounts: {nfmt(v.get("lagging_count"))}.</p>
    </div>
  </section>

  <section class="hidden" data-panel="defi">
    <div class="grid21">
      <div class="panel">
        <h2>Top DEX venues (DeFiLlama 24h)</h2>
        <table><thead><tr><th>DEX</th><th class="right">24h</th><th class="right">1d</th></tr></thead>
        <tbody>{dex_trs}</tbody></table>
      </div>
      <div class="panel">
        <h2>Stablecoins on Solana</h2>
        <table><thead><tr><th>Sym</th><th>Name</th><th class="right">Circ.</th><th class="right">1d</th></tr></thead>
        <tbody>{stab_trs}</tbody></table>
      </div>
    </div>
    <div class="panel" style="margin-top:10px">
      <h2>Top protocols by Solana chain TVL</h2>
      <table><thead><tr><th>Protocol</th><th>Category</th><th class="right">TVL</th><th class="right">1d</th><th class="right">7d</th></tr></thead>
      <tbody>{proto_trs}</tbody></table>
    </div>
    <div class="grid2" style="margin-top:10px">
      <div class="panel">
        <h2>RWA (DeFiLlama category rollup)</h2>
        <p>Protocol TVL tagged RWA / RWA Lending with a Solana chain split: <b>{usd(rwa.get("tvl_usd"))}</b></p>
        <ul>{rwa_lis}</ul>
        <p class="tiny muted">Labeled RWA protocol TVL — not a tokenized-equities market cap. Llama /rwa/* routes are Pro-only.</p>
        <p class="tiny muted">Median tx fee is sampled from getBlock meta.fee (see Overview). Protocol fees 24h {usd(eco.get("protocol_fees_usd"))} are DeFiLlama, not REV. Network fees {nfmt(eco.get("network_fees_sol_24h"),1)} SOL ({e(eco.get("network_fees_source") or "—")}).</p>
      </div>
      <div class="panel">
        <h2>Daily active addresses</h2>
        <p>{nfmt(daa.get("headline_value")) if not daa_ghost else "Omitted this run."}</p>
        <p class="tiny muted">{daa_note}</p>
        <p class="tiny muted">{daa_sub}</p>
        <h2 style="margin-top:16px">Public RPC latencies (solana.com/data)</h2>
        <table><thead><tr><th>Provider</th><th class="right">Avg ms</th><th class="right">P95 ms</th><th class="right">Err %</th></tr></thead>
        <tbody>{rpc_rows}</tbody></table>
        <p class="tiny muted">solana.com/api/rpc/data generated {e(scom.get("rpc_generated_at"))}</p>
      </div>
    </div>
  </section>

  <section class="hidden" data-panel="news">
    <div class="panel">
      <h2>status.solana.com · {e(status.get("description") or "—")}</h2>
      <div class="status-row">{comps}</div>
      <p class="tiny muted">{e(news.get("recency_note") or "Recency applied after RSS merge. 2022–2024 incidents are archive, not current.")}</p>
    </div>
    <div class="grid2" style="margin-top:10px">
      <div class="panel">
        <h2>Active incidents</h2>
        <ul class="news">{active_lis}</ul>
        <h2 style="margin-top:14px">Recently resolved</h2>
        <ul class="news">{resolved_lis}</ul>
      </div>
      <div class="panel">
        <h2>Current news</h2>
        <ul class="news">{news_lis}</ul>
        <h2 style="margin-top:14px">X announcements (public Nitter-style RSS)</h2>
        <ul class="news">{tw_lis}</ul>
        <p class="tiny muted">{e(news.get("twitter_note") or "Not the official Twitter API. 403/gated routes skipped.")}</p>
      </div>
    </div>
    <div class="panel" style="margin-top:10px">
      <h2>Archive (not current)</h2>
      <ul class="news">{archive_lis}</ul>
    </div>
  </section>

  <section class="hidden" data-panel="anomalies">
    <div class="panel">
      <h2>Rolling baseline flags</h2>
      {flag_html}
      <p class="tiny muted">Last-sample vs 60-window 2.5σ · slot &gt;500ms · llama TVL/DEX/fees |1d|&gt;8% or |7d|&gt;20% · 30d median from solana.com/data · correlation: congestion / risk-off / validator stress. history.jsonl n={e((snap.get("baseline") or {}).get("history_points"))}.</p>
      <p class="tiny muted">Health formula: {e(hs.get("formula") or "")}</p>
      {hist_spark_tps}{hist_spark_px}
    </div>
  </section>

  <section class="hidden" data-panel="trends">
    <div class="panel">
      <h2>Multi-run tape · data/history.jsonl</h2>
      <p class="tiny muted">{e((trends or {}).get("note") or "")} · run points {nfmt((trends.get("run") or {}).get("n"))}</p>
      <div class="trend-grid">
        <div class="trend-card"><h3>TPS (15-min tape)</h3>{trend_chart((trends.get("run") or {}).get("tps") or [], color="#3ee0b0", ylabel="TPS")}</div>
        <div class="trend-card"><h3>TVL (15-min tape)</h3>{trend_chart((trends.get("run") or {}).get("tvl") or [], color="#f0b429", ylabel="TVL", money=True)}</div>
        <div class="trend-card"><h3>SOL (15-min tape)</h3>{trend_chart((trends.get("run") or {}).get("sol") or [], color="#7aa2ff", ylabel="SOL", money=True)}</div>
      </div>
    </div>
    <div class="panel" style="margin-top:10px">
      <h2>Daily seed · DeFiLlama + solana.com/data</h2>
      <div class="trend-grid">
        <div class="trend-card"><h3>TPS 30d</h3>{trend_chart((trends.get("daily") or {}).get("tps") or [], color="#3ee0b0", ylabel="TPS")}
          <p class="tiny muted">{e((trends.get("daily") or {}).get("tps_source") or "")}</p></div>
        <div class="trend-card"><h3>TVL 90d</h3>{trend_chart((trends.get("daily") or {}).get("tvl") or [], color="#f0b429", ylabel="TVL", money=True)}
          <p class="tiny muted">{e((trends.get("daily") or {}).get("tvl_source") or "")}</p></div>
        <div class="trend-card"><h3>SOL 30d</h3>{trend_chart((trends.get("daily") or {}).get("sol") or [], color="#7aa2ff", ylabel="SOL", money=True)}
          <p class="tiny muted">{e((trends.get("daily") or {}).get("sol_source") or "")}</p></div>
      </div>
    </div>
  </section>

  <section class="hidden" data-panel="sources">
    {dh_html}
    {dune_html}
    <div class="panel">
      <h2>This run</h2>
      <p class="tiny muted">{e(m.get("generated_at_utc"))} · python {e(m.get("python"))} · author {e(m.get("author"))}</p>
      <button class="linkish" id="copyjson" type="button">Copy report.json</button>
      <p style="margin-top:12px"><b>Omissions</b></p>
      <ul>{om_lis}</ul>
      <table style="margin-top:12px"><thead><tr><th>Source</th><th>Ok</th><th>HTTP</th><th>ms</th><th>URL / error</th></tr></thead>
      <tbody>{src_rows}</tbody></table>
    </div>
  </section>

  <footer class="footer">
    Borealis is read-only public telemetry. Numbers are never invented: a failed fetch becomes a dashed tile and an omissions row.
    MIT · author dustycompiler · updates every 15 min via GitHub Action ·
    <a href="https://github.com/dustycompiler/borealis-solana">repo</a> ·
    <a href="report.md">report.md</a> · <a href="report.json">report.json</a>
  </footer>
</div>
<script id="snapshot" type="application/json">{payload}</script>
<script>{JS}</script>
</body>
</html>
"""
