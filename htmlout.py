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


MARK = """<svg class="mark" viewBox="0 0 36 36" aria-hidden="true">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#3ee0b0"/><stop offset="1" stop-color="#7aa2ff"/>
  </linearGradient></defs>
  <rect x="1" y="1" width="34" height="34" rx="9" fill="#0c1017" stroke="url(#g)"/>
  <path d="M18 7 L22 15 L31 16 L24 22 L26 31 L18 26 L10 31 L12 22 L5 16 L14 15 Z" fill="url(#g)"/>
</svg>"""


def tile(title, value, sub="", chip=None, ghost=False, spark=""):
    cls = "card ghost" if ghost else "card"
    chip_html = ""
    if chip is not None:
        chip_html = f'<span class="chip {delta_class(chip)}">{pct(chip)}</span>'
    sub_html = f'<div class="sub">{sub} {chip_html}</div>' if (sub or chip is not None) else ""
    return f'<article class="{cls}"><h3>{e(title)}</h3><div class="val">{value}</div>{sub_html}{spark}</article>'


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

    kpis = "".join([
        tile("TPS", nfmt(c.get("tps_total"), 0),
             f"median {nfmt(c.get('tps_median'), 0)} · {nfmt(c.get('performance_window_sec'))}s window",
             spark=tps_spark),
        tile("Non-vote TPS", nfmt(c.get("tps_nonvote"), 0), "from numNonVoteTransactions", spark=nv_spark),
        tile("Slot time", (nfmt((c.get("slot_time_sec") or 0)*1000, 1) + " ms") if c.get("slot_time_sec") else "—",
             f"median {nfmt((c.get('slot_time_median') or 0)*1000, 1)} ms · max {nfmt((c.get('slot_time_max') or 0)*1000, 1)}",
             spark=st_spark),
        tile("Slot / height", f"{nfmt(c.get('slot'))}", f"height {nfmt(c.get('block_height'))}"),
        tile("SOL", usd(px.get("usd"), 2) if not px_ghost else "—",
             (px.get("source") or "CoinGecko") if not px_ghost else "CoinGecko 429 / omitted",
             chip=px.get("usd_24h_change"), ghost=px_ghost),
        tile("TVL", usd(d.get("tvl_usd")) if not tvl_ghost else "—",
             "DeFiLlama chain TVL", chip=d.get("tvl_change_1d_pct"), ghost=tvl_ghost, spark=tvl_spark),
        tile("DEX 24h", usd((d.get("dex") or {}).get("total_24h_usd")),
             f"7d {usd((d.get('dex') or {}).get('total_7d_usd'))}",
             chip=(d.get("dex") or {}).get("change_1d_pct")),
        tile("Stables", usd(st.get("circulating_usd")) if not stab_ghost else "—",
             "Solana pegged-USD", chip=st.get("change_1d_pct"), ghost=stab_ghost, spark=stab_spark),
        tile("RWA TVL", usd(rwa.get("tvl_usd")) if not rwa_ghost else "—",
             f"{nfmt(rwa.get('protocol_count'))} RWA protocols on Solana", ghost=rwa_ghost),
        tile("Active addrs", nfmt(daa.get("headline_value")) if not daa_ghost else "—",
             daa_sub, ghost=daa_ghost),
        tile("Validators", nfmt(v.get("active_count")),
             f"delinquent {nfmt(v.get('delinquent_count'))} · {pct(v.get('delinquent_stake_pct'), 3)} stake"),
        tile("Nakamoto 33%", nfmt(v.get("nakamoto_33")),
             f"50% {nfmt(v.get('nakamoto_50'))} · 67% {nfmt(v.get('supermajority_67'))}"),
    ])

    flag_html = '<p class="muted">No rolling-baseline flags this run. Thresholds live in README.</p>'
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

    news_lis = "".join(
        f'<li><div class="src">{e(n.get("source"))} · {e(n.get("published"))}</div>'
        f'<a href="{e(n.get("url"))}" rel="noopener">{e(n.get("title"))}</a></li>'
        for n in (news.get("items") or [])[:12]
    ) or '<li class="omit">No RSS items parsed.</li>'

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
    payload = json.dumps({
        "meta": m,
        "anomalies": flags,
        "validators_top": v.get("top") or [],
        "omissions": om,
    }, default=str).replace("<", "\\u003c")

    title = f"Borealis — Solana {m.get('generated_at_utc') or ''}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<meta name="color-scheme" content="dark"/>
<title>{e(title)}</title>
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
    <div class="health-pill"><span class="dot {dot}"></span>{e(health_label)}</div>
    <div class="meta-clock">
      <b>{e(m.get("generated_at_utc"))}</b>
      {e(m.get("generated_at_pt"))}<br/>run {e(m.get("run_id"))} · v{e(m.get("version"))}
    </div>
  </header>

  <nav class="tabs">
    <button class="on" data-tab="overview">Overview</button>
    <button data-tab="validators">Validators</button>
    <button data-tab="defi">DeFi &amp; assets</button>
    <button data-tab="news">News &amp; status</button>
    <button data-tab="anomalies">Anomalies</button>
    <button data-tab="sources">Sources</button>
  </nav>

  <section data-panel="overview">
    <div class="kpis">{kpis}</div>
    <div class="grid2">
      <div class="panel">
        <h2>Anomaly strip</h2>
        {flag_html}
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
        <p class="tiny muted">Not a full RWA market-cap census. Llama /rwa/* routes are Pro-only.</p>
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
      <h2 style="margin-top:16px">RSS / Atom</h2>
      <ul class="news">{news_lis}</ul>
      <p class="tiny muted">Feeds: status.solana.com/history.atom · solana.com/news/rss.xml · medium.com/feed/anza-xyz. No Twitter API.</p>
    </div>
  </section>

  <section class="hidden" data-panel="anomalies">
    <div class="panel">
      <h2>Rolling baseline flags</h2>
      {flag_html}
      <p class="tiny muted">In-run baseline: 60 performance samples. Cross-run baseline: data/history.jsonl (n={e((snap.get("baseline") or {}).get("history_points"))}). TVL uses DeFiLlama daily series. Price uses CoinGecko 24h change.</p>
    </div>
  </section>

  <section class="hidden" data-panel="sources">
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
    MIT · author hardest-worker · <a href="report.md">report.md</a> · <a href="report.json">report.json</a>
  </footer>
</div>
<script id="snapshot" type="application/json">{payload}</script>
<script>{JS}</script>
</body>
</html>
"""
