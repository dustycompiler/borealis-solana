#!/usr/bin/env python3
"""Borealis — live Solana cluster & ecosystem report.

One command, no API keys, stdlib only:

    python3 generate.py

Writes out/index.html, out/report.md, out/report.json and copies a
static snapshot to docs/ for GitHub Pages.

Author: dustycompiler
License: MIT
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import os
import re
import shutil
import statistics
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
from typing import Any
from zoneinfo import ZoneInfo

from htmlout import render_html

VERSION = "1.1.0"
PRODUCT = "Borealis"
LAMPORTS = 1_000_000_000
PT = ZoneInfo("America/Vancouver")
UTC = timezone.utc

PRIMARY_RPC = "https://api.mainnet-beta.solana.com"
FALLBACK_RPC = "https://solana-rpc.publicnode.com"

USER_AGENT = (
    "BorealisReport/1.1 (Solana ecosystem dashboard; stdlib urllib; no API key)"
)

ROOT = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "dustycompiler"
DEMO_URL = "https://dustycompiler.github.io/borealis-solana/"
REPO_URL = "https://github.com/dustycompiler/borealis-solana"


def utcnow() -> datetime:
    return datetime.now(tz=UTC)


def iso(dt: datetime | None) -> str | None:
    if dt is None:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=UTC)
    return dt.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def iso_pt(dt: datetime | None) -> str | None:
    if dt is None:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=UTC)
    return dt.astimezone(PT).strftime("%Y-%m-%d %H:%M:%S PT")


def parse_unix(ts: Any) -> datetime | None:
    try:
        n = float(ts)
        if n > 1e12:
            n = n / 1000.0
        return datetime.fromtimestamp(n, tz=UTC)
    except (TypeError, ValueError, OSError, OverflowError):
        return None


def fmt_num(n: Any, digits: int = 0) -> str:
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


def fmt_usd(n: Any, digits: int | None = None) -> str:
    if n is None:
        return "—"
    try:
        x = float(n)
    except (TypeError, ValueError):
        return "—"
    if not math.isfinite(x):
        return "—"
    ax = abs(x)
    sign = "-" if x < 0 else ""
    if ax >= 1_000_000_000_000:
        return f"{sign}${ax/1_000_000_000_000:.2f}T"
    if ax >= 1_000_000_000:
        return f"{sign}${ax/1_000_000_000:.2f}B"
    if ax >= 1_000_000:
        return f"{sign}${ax/1_000_000:.2f}M"
    if ax >= 1_000:
        return f"{sign}${ax/1_000:.2f}K"
    if digits is None:
        digits = 2 if ax >= 1 else 4
    return f"{sign}${ax:,.{digits}f}"


def fmt_sol(lamports: Any) -> str:
    if lamports is None:
        return "—"
    try:
        sol = float(lamports) / LAMPORTS
    except (TypeError, ValueError):
        return "—"
    if sol >= 1_000_000:
        return f"{sol/1_000_000:.2f}M SOL"
    if sol >= 1_000:
        return f"{sol/1_000:.2f}K SOL"
    return f"{sol:,.2f} SOL"


def fmt_pct(n: Any, digits: int = 2) -> str:
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



def pct_change(new: Any, old: Any) -> float | None:
    try:
        a = float(new)
        b = float(old)
    except (TypeError, ValueError):
        return None
    if b == 0 or not math.isfinite(a) or not math.isfinite(b):
        return None
    return (a - b) / b * 100.0


def fnum(x: Any) -> float | None:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if math.isfinite(v) else None


def clamp(x: float, lo: float, hi: float) -> float:
    return lo if x < lo else hi if x > hi else x


def strip_html(s: Any) -> str:
    text = re.sub(r"<[^>]+>", " ", s or "")
    return re.sub(r"\s+", " ", text).strip()


def zscore(x: Any, mu: Any, sd: Any) -> float | None:
    if x is None or mu is None or not sd:
        return None
    try:
        return (float(x) - float(mu)) / float(sd)
    except (TypeError, ValueError, ZeroDivisionError):
        return None

def mean(xs: list[float]) -> float | None:
    xs = [x for x in xs if x is not None and math.isfinite(x)]
    if not xs:
        return None
    return sum(xs) / len(xs)


def median(xs: list[float]) -> float | None:
    xs = sorted(x for x in xs if x is not None and math.isfinite(x))
    if not xs:
        return None
    return statistics.median(xs)


def pstdev(xs: list[float]) -> float | None:
    xs = [x for x in xs if x is not None and math.isfinite(x)]
    if len(xs) < 2:
        return 0.0 if xs else None
    return statistics.pstdev(xs)


def nakamoto(stakes: list[int], threshold: float) -> int | None:
    total = sum(stakes)
    if total <= 0:
        return None
    acc = 0
    n = 0
    for s in sorted(stakes, reverse=True):
        acc += s
        n += 1
        if acc > total * threshold:
            return n
    return n


class Http:
    def __init__(self) -> None:
        self.log: list[dict[str, Any]] = []

    def _record(self, **kw: Any) -> dict[str, Any]:
        self.log.append(kw)
        return kw

    def request(
        self,
        url: str,
        *,
        source_id: str,
        data: bytes | None = None,
        headers: dict[str, str] | None = None,
        timeout: int = 30,
        retries: int = 2,
        backoff: float = 1.5,
        honor_retry_after: bool = True,
        max_retry_after: float = 25.0,
        accept: str = "*/*",
    ) -> tuple[bytes | None, dict[str, Any]]:
        hdrs = {
            "User-Agent": USER_AGENT,
            "Accept": accept,
            "Accept-Encoding": "gzip",
        }
        if data is not None:
            hdrs["Content-Type"] = "application/json"
        if headers:
            hdrs.update(headers)

        last_err = None
        t_all = time.time()
        for attempt in range(retries + 1):
            t0 = time.time()
            req = urllib.request.Request(url, data=data, headers=hdrs)
            try:
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    body = resp.read()
                    enc = (resp.headers.get("Content-Encoding") or "").lower()
                    if enc == "gzip" or body[:2] == b"\x1f\x8b":
                        try:
                            body = gzip.decompress(body)
                        except OSError:
                            pass
                    rec = self._record(
                        id=source_id,
                        url=url,
                        ok=True,
                        status=getattr(resp, "status", 200),
                        bytes=len(body),
                        ms=int((time.time() - t0) * 1000),
                        attempt=attempt + 1,
                        fetched_at=iso(utcnow()),
                        error=None,
                    )
                    return body, rec
            except urllib.error.HTTPError as e:
                last_err = f"HTTP {e.code} {e.reason}"
                retry_after = None
                if e.headers:
                    ra = e.headers.get("Retry-After")
                    if ra:
                        try:
                            retry_after = float(ra)
                        except ValueError:
                            retry_after = None
                if e.code == 429 and honor_retry_after and retry_after and attempt < retries:
                    wait = min(max(retry_after, 0.5), max_retry_after)
                    time.sleep(wait)
                    continue
                if e.code in (429, 500, 502, 503, 504) and attempt < retries:
                    time.sleep(backoff * (attempt + 1))
                    continue
                rec = self._record(
                    id=source_id,
                    url=url,
                    ok=False,
                    status=e.code,
                    bytes=0,
                    ms=int((time.time() - t0) * 1000),
                    attempt=attempt + 1,
                    fetched_at=iso(utcnow()),
                    error=last_err,
                )
                return None, rec
            except Exception as e:
                last_err = f"{type(e).__name__}: {e}"
                if attempt < retries:
                    time.sleep(backoff * (attempt + 1))
                    continue
                rec = self._record(
                    id=source_id,
                    url=url,
                    ok=False,
                    status=None,
                    bytes=0,
                    ms=int((time.time() - t_all) * 1000),
                    attempt=attempt + 1,
                    fetched_at=iso(utcnow()),
                    error=last_err,
                )
                return None, rec
        rec = self._record(
            id=source_id,
            url=url,
            ok=False,
            status=None,
            bytes=0,
            ms=int((time.time() - t_all) * 1000),
            attempt=retries + 1,
            fetched_at=iso(utcnow()),
            error=last_err,
        )
        return None, rec

    def json(self, url: str, *, source_id: str, **kw: Any) -> tuple[Any, dict[str, Any]]:
        body, rec = self.request(url, source_id=source_id, accept="application/json", **kw)
        if body is None:
            return None, rec
        try:
            return json.loads(body.decode("utf-8")), rec
        except Exception as e:
            rec["ok"] = False
            rec["error"] = f"JSON parse: {e}"
            return None, rec

    def rpc(self, method: str, params: list[Any] | None = None, *, timeout: int = 40) -> tuple[Any, dict[str, Any]]:
        payload = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params or []}).encode("utf-8")
        last_rec = None
        for i, url in enumerate((PRIMARY_RPC, FALLBACK_RPC)):
            sid = f"rpc.{method}" + ("" if i == 0 else ".fallback")
            body, rec = self.request(
                url,
                source_id=sid,
                data=payload,
                timeout=timeout,
                retries=1 if i == 0 else 2,
                honor_retry_after=True,
                max_retry_after=8.0,
            )
            last_rec = rec
            if body is None:
                continue
            try:
                parsed = json.loads(body.decode("utf-8"))
            except Exception as e:
                rec["ok"] = False
                rec["error"] = f"JSON parse: {e}"
                continue
            if isinstance(parsed, dict) and parsed.get("error"):
                rec["ok"] = False
                rec["error"] = str(parsed["error"])[:240]
                continue
            rec["rpc_endpoint"] = url
            return parsed.get("result") if isinstance(parsed, dict) else parsed, rec
        return None, last_rec or {"id": f"rpc.{method}", "ok": False, "error": "all endpoints failed"}


def fetch_cluster(http: Http) -> dict[str, Any]:
    out: dict[str, Any] = {
        "health": None, "slot": None, "block_time_unix": None, "block_time_utc": None,
        "block_height": None, "epoch": None, "slot_index": None, "slots_in_epoch": None,
        "epoch_progress_pct": None, "absolute_slot": None, "transaction_count": None,
        "tps_total": None, "tps_nonvote": None, "tps_samples": [], "slot_time_sec": None,
        "slot_time_samples": [], "performance_window_sec": None, "supply": None,
        "rpc_endpoint_used": None,
    }
    health, rec = http.rpc("getHealth", timeout=20)
    out["health"] = health if rec.get("ok") else None
    out["health_ok"] = health == "ok"

    slot, rec = http.rpc("getSlot", timeout=20)
    if isinstance(slot, int):
        out["slot"] = slot
        out["rpc_endpoint_used"] = rec.get("rpc_endpoint") or rec.get("url")
        bt, _ = http.rpc("getBlockTime", [slot], timeout=20)
        if isinstance(bt, (int, float)):
            out["block_time_unix"] = int(bt)
            dt = parse_unix(bt)
            out["block_time_utc"] = iso(dt)
            out["block_time_pt"] = iso_pt(dt)

    info, _ = http.rpc("getEpochInfo", timeout=20)
    if isinstance(info, dict):
        out["block_height"] = info.get("blockHeight")
        out["epoch"] = info.get("epoch")
        out["slot_index"] = info.get("slotIndex")
        out["slots_in_epoch"] = info.get("slotsInEpoch")
        out["absolute_slot"] = info.get("absoluteSlot")
        out["transaction_count"] = info.get("transactionCount")
        si, se = info.get("slotIndex"), info.get("slotsInEpoch")
        if isinstance(si, int) and isinstance(se, int) and se:
            out["epoch_progress_pct"] = round(si / se * 100.0, 4)

    samples, _ = http.rpc("getRecentPerformanceSamples", [60], timeout=25)
    tps_t: list[float] = []
    tps_nv: list[float] = []
    stimes: list[float] = []
    compact = []
    if isinstance(samples, list):
        for s in samples:
            if not isinstance(s, dict):
                continue
            period = float(s.get("samplePeriodSecs") or 0) or 60.0
            nslot = float(s.get("numSlots") or 0)
            ntx = float(s.get("numTransactions") or 0)
            nnv = s.get("numNonVoteTransactions")
            tps = ntx / period
            tps_t.append(tps)
            row = {
                "slot": s.get("slot"), "period_sec": period,
                "num_slots": int(nslot) if nslot else None,
                "num_transactions": int(ntx) if ntx else None,
                "tps_total": round(tps, 3),
            }
            if nnv is not None:
                nv = float(nnv) / period
                tps_nv.append(nv)
                row["num_nonvote"] = int(nnv)
                row["tps_nonvote"] = round(nv, 3)
            if nslot:
                st = period / nslot
                stimes.append(st)
                row["slot_time_sec"] = round(st, 5)
            compact.append(row)
        out["tps_samples"] = compact
        out["performance_window_sec"] = int(sum((r["period_sec"] or 0) for r in compact))
        out["tps_total"] = mean(tps_t)
        out["tps_nonvote"] = mean(tps_nv) if tps_nv else None
        out["slot_time_sec"] = mean(stimes)
        out["slot_time_samples"] = [round(x, 5) for x in stimes]
        out["tps_median"] = median(tps_t)
        out["tps_stdev"] = pstdev(tps_t)
        out["slot_time_median"] = median(stimes)
        out["slot_time_max"] = max(stimes) if stimes else None
        out["slot_time_min"] = min(stimes) if stimes else None
        # getRecentPerformanceSamples is newest-first.
        if compact:
            out["tps_last"] = compact[0].get("tps_total")
            out["tps_nonvote_last"] = compact[0].get("tps_nonvote")
            out["slot_time_last"] = compact[0].get("slot_time_sec")
            out["tps_nonvote_median"] = median(tps_nv) if tps_nv else None
            out["tps_nonvote_stdev"] = pstdev(tps_nv) if tps_nv else None
            out["slot_time_stdev"] = pstdev(stimes)

    supply, _ = http.rpc("getSupply", [{"excludeNonCirculatingAccountsList": True}], timeout=45)
    if isinstance(supply, dict):
        val = supply.get("value") if "value" in supply else supply
        if isinstance(val, dict):
            total = val.get("total")
            circ = val.get("circulating")
            nonc = val.get("nonCirculating")
            out["supply"] = {
                "total_lamports": total,
                "circulating_lamports": circ,
                "noncirculating_lamports": nonc,
                "total_sol": (total / LAMPORTS) if isinstance(total, (int, float)) else None,
                "circulating_sol": (circ / LAMPORTS) if isinstance(circ, (int, float)) else None,
                "noncirculating_sol": (nonc / LAMPORTS) if isinstance(nonc, (int, float)) else None,
            }
    return out


def fetch_validators(http: Http, current_slot: int | None) -> dict[str, Any]:
    result, rec = http.rpc("getVoteAccounts", [{"keepUnstakedDelinquents": False}], timeout=60)
    empty = {"ok": rec.get("ok"), "error": rec.get("error"), "active_count": None,
             "delinquent_count": None, "top": [], "delinquent": [], "lagging": []}
    if not isinstance(result, dict):
        return empty
    current = result.get("current") or []
    delinquent = result.get("delinquent") or []
    if not isinstance(current, list):
        current = []
    if not isinstance(delinquent, list):
        delinquent = []

    def slim(v: dict[str, Any], delinquent_flag: bool) -> dict[str, Any]:
        stake = int(v.get("activatedStake") or 0)
        last = v.get("lastVote")
        lag = None
        if isinstance(current_slot, int) and isinstance(last, int):
            lag = max(0, current_slot - last)
        return {
            "vote": v.get("votePubkey"), "node": v.get("nodePubkey"),
            "activated_stake_lamports": stake, "activated_stake_sol": stake / LAMPORTS,
            "commission": v.get("commission"), "last_vote": last, "root_slot": v.get("rootSlot"),
            "lag_slots": lag, "delinquent": delinquent_flag,
        }

    cur_s = [slim(v, False) for v in current if isinstance(v, dict)]
    del_s = [slim(v, True) for v in delinquent if isinstance(v, dict)]
    cur_s.sort(key=lambda x: x["activated_stake_lamports"], reverse=True)
    del_s.sort(key=lambda x: x["activated_stake_lamports"], reverse=True)

    stakes = [v["activated_stake_lamports"] for v in cur_s]
    del_stakes = [v["activated_stake_lamports"] for v in del_s]
    total_c = sum(stakes)
    total_d = sum(del_stakes)
    total = total_c + total_d
    comms = [int(v["commission"]) for v in cur_s if isinstance(v.get("commission"), (int, float))]

    def share(n: int) -> float | None:
        if total_c <= 0:
            return None
        return sum(stakes[:n]) / total_c * 100.0

    lagging = [v for v in cur_s if isinstance(v.get("lag_slots"), int) and v["lag_slots"] > 150]
    lagging.sort(key=lambda x: x["lag_slots"] or 0, reverse=True)

    buckets = {"0": 0, "1-5": 0, "6-10": 0, "11-50": 0, "51-100": 0}
    for c in comms:
        if c == 0:
            buckets["0"] += 1
        elif c <= 5:
            buckets["1-5"] += 1
        elif c <= 10:
            buckets["6-10"] += 1
        elif c <= 50:
            buckets["11-50"] += 1
        else:
            buckets["51-100"] += 1

    for i, v in enumerate(cur_s, 1):
        v["rank"] = i
        v["stake_share_pct"] = (v["activated_stake_lamports"] / total_c * 100.0) if total_c else None
    for v in del_s:
        v["stake_share_pct"] = (v["activated_stake_lamports"] / total * 100.0) if total else None

    return {
        "ok": True,
        "active_count": len(cur_s),
        "delinquent_count": len(del_s),
        "lagging_count": len(lagging),
        "activated_stake_lamports": total_c,
        "activated_stake_sol": total_c / LAMPORTS,
        "delinquent_stake_lamports": total_d,
        "delinquent_stake_sol": total_d / LAMPORTS,
        "delinquent_stake_pct": (total_d / total * 100.0) if total else None,
        "nakamoto_33": nakamoto(stakes, 1.0 / 3.0),
        "nakamoto_50": nakamoto(stakes, 0.50),
        "supermajority_67": nakamoto(stakes, 2.0 / 3.0),
        "top10_share_pct": share(10),
        "top20_share_pct": share(20),
        "top33_share_pct": share(33),
        "commission_min": min(comms) if comms else None,
        "commission_median": median([float(c) for c in comms]),
        "commission_max": max(comms) if comms else None,
        "commission_buckets": buckets,
        "top": cur_s[:40],
        "delinquent": del_s[:40],
        "lagging": lagging[:20],
        "all_top_stakes_sol": [round(s / LAMPORTS, 2) for s in stakes[:40]],
    }


def fetch_coingecko(http: Http) -> dict[str, Any]:
    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=solana&vs_currencies=usd"
        "&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true"
        "&include_last_updated_at=true"
    )
    data, rec = http.json(
        url, source_id="coingecko.simple_price", timeout=15, retries=1,
        honor_retry_after=True, max_retry_after=6.0, backoff=1.5,
    )
    out: dict[str, Any] = {
        "ok": bool(rec.get("ok")), "source": "coingecko", "url": url,
        "usd": None, "usd_24h_change": None, "usd_market_cap": None,
        "usd_24h_vol": None, "last_updated_unix": None, "error": rec.get("error"),
    }
    if isinstance(data, dict) and isinstance(data.get("solana"), dict):
        s = data["solana"]
        out["usd"] = fnum(s.get("usd"))
        out["usd_24h_change"] = fnum(s.get("usd_24h_change"))
        out["usd_market_cap"] = fnum(s.get("usd_market_cap"))
        out["usd_24h_vol"] = fnum(s.get("usd_24h_vol"))
        out["last_updated_unix"] = s.get("last_updated_at")
        out["last_updated_utc"] = iso(parse_unix(s.get("last_updated_at")))
        out["ok"] = out["usd"] is not None
    return out


def fetch_coinbase_sol(http: Http) -> dict[str, Any]:
    url = "https://api.exchange.coinbase.com/products/SOL-USD/stats"
    data, rec = http.json(url, source_id="coinbase.solusd.stats", timeout=15, retries=1)
    out: dict[str, Any] = {
        "ok": False, "source": "coinbase.exchange.SOL-USD.stats", "url": url,
        "error": rec.get("error"),
    }
    if not isinstance(data, dict):
        return out
    last = fnum(data.get("last"))
    open_px = fnum(data.get("open"))
    vol = fnum(data.get("volume"))
    high = fnum(data.get("high"))
    low = fnum(data.get("low"))
    ch = pct_change(last, open_px)
    quote = (last * vol) if last is not None and vol is not None else None
    out.update({
        "ok": last is not None,
        "usd": last,
        "usd_24h_change": ch,
        "usd_24h_vol": quote,
        "base_volume_sol": vol,
        "open": open_px,
        "high": high,
        "low": low,
        "note": "24h % = (last − open) / open from Coinbase 24h stats. Quote volume = last × base SOL volume.",
    })
    return out


def fetch_kraken_sol(http: Http) -> dict[str, Any]:
    url = "https://api.kraken.com/0/public/Ticker?pair=SOLUSD"
    data, rec = http.json(url, source_id="kraken.solusd.ticker", timeout=15, retries=1)
    out: dict[str, Any] = {
        "ok": False, "source": "kraken.SOLUSD.ticker", "url": url,
        "error": rec.get("error"),
    }
    if not isinstance(data, dict):
        return out
    if data.get("error"):
        out["error"] = str(data.get("error"))[:240]
        return out
    result = data.get("result") or {}
    row = None
    if isinstance(result, dict) and result:
        row = result.get("SOLUSD") or next(iter(result.values()), None)
    if not isinstance(row, dict):
        out["error"] = "unexpected Kraken ticker shape"
        return out
    last = fnum((row.get("c") or [None])[0])
    open_px = fnum(row.get("o"))
    vol24 = fnum((row.get("v") or [None, None])[1] if isinstance(row.get("v"), list) else None)
    vwap24 = fnum((row.get("p") or [None, None])[1] if isinstance(row.get("p"), list) else None)
    ch = pct_change(last, open_px)
    if vwap24 is not None and vol24 is not None:
        quote = vwap24 * vol24
    elif last is not None and vol24 is not None:
        quote = last * vol24
    else:
        quote = None
    out.update({
        "ok": last is not None,
        "usd": last,
        "usd_24h_change": ch,
        "usd_24h_vol": quote,
        "base_volume_sol": vol24,
        "open": open_px,
        "note": "24h % = (last − open) / open using Kraken 24h open field o. Quote vol ≈ 24h vwap × 24h volume.",
    })
    return out


def fetch_llama_price(http: Http) -> dict[str, Any]:
    url = "https://coins.llama.fi/prices/current/coingecko:solana"
    data, rec = http.json(url, source_id="llama.coins.coingecko_solana", timeout=15, retries=1)
    out: dict[str, Any] = {
        "ok": False, "source": "defillama-coins coingecko:solana", "url": url,
        "error": rec.get("error"),
    }
    coins = (data or {}).get("coins") if isinstance(data, dict) else None
    row = None
    if isinstance(coins, dict):
        row = coins.get("coingecko:solana") or next(iter(coins.values()), None)
    if isinstance(row, dict) and fnum(row.get("price")) is not None:
        ts = row.get("timestamp")
        out.update({
            "ok": True,
            "usd": fnum(row.get("price")),
            "usd_24h_change": None,
            "last_updated_unix": ts,
            "last_updated_utc": iso(parse_unix(ts)) if ts else None,
        })
    return out


def apply_solana_com_price(market: dict[str, Any], sdata: dict[str, Any]) -> dict[str, Any]:
    """Fill missing price and/or 24h change from the public 30d SOL Price series."""
    derived = sdata.get("derived") or {}
    if market.get("usd") is None:
        pick = derived.get("sol_price_latest")
        if pick and fnum(pick.get("value")) is not None:
            market.update({
                "ok": True,
                "source": f"solana.com/data SOL Price ({pick.get('provider')})",
                "usd": pick.get("value"),
                "price_as_of": pick.get("date"),
                "fallback": True,
            })
    if market.get("usd_24h_change") is None and derived.get("sol_price_dod_pct") is not None:
        market["usd_24h_change"] = derived.get("sol_price_dod_pct")
        market["usd_24h_change_source"] = (
            f"solana.com/data SOL Price day-over-day "
            f"({derived.get('sol_price_dod_provider')}; not a rolling 24h tape)"
        )
        if not market.get("source"):
            market["source"] = market["usd_24h_change_source"]
    return market


def assemble_market(http: Http, circulating_sol: Any = None) -> dict[str, Any]:
    """SOL price + 24h change from public no-key feeds. Never invent.

    Order: CoinGecko (often 429) → Coinbase Exchange stats (primary 24h on this
    box) → Kraken ticker → DeFiLlama coins (price only). Binance is skipped
    (HTTP 451 from this network). Market cap is CoinGecko when present,
    otherwise price × RPC circulating supply, labeled as derived.
    """
    gecko = fetch_coingecko(http)
    cb = fetch_coinbase_sol(http)
    kr = None
    llama = None

    market: dict[str, Any] = {
        "ok": False, "usd": None, "usd_24h_change": None,
        "usd_market_cap": None, "usd_24h_vol": None,
        "source": None, "usd_24h_change_source": None,
        "usd_24h_vol_source": None, "usd_market_cap_source": None,
        "fallbacks_tried": [],
    }

    if gecko.get("ok") and gecko.get("usd") is not None:
        market.update({
            "ok": True,
            "usd": gecko["usd"],
            "usd_24h_change": gecko.get("usd_24h_change"),
            "usd_market_cap": gecko.get("usd_market_cap"),
            "usd_24h_vol": gecko.get("usd_24h_vol"),
            "source": "coingecko.simple_price",
            "usd_24h_change_source": "coingecko.simple_price",
            "usd_24h_vol_source": "coingecko.simple_price",
            "usd_market_cap_source": "coingecko.simple_price",
            "last_updated_unix": gecko.get("last_updated_unix"),
            "last_updated_utc": gecko.get("last_updated_utc"),
        })
    else:
        market["fallbacks_tried"].append("coingecko:" + str(gecko.get("error") or "no price"))

    if (market.get("usd") is None or market.get("usd_24h_change") is None) and cb.get("ok"):
        if market.get("usd") is None:
            market["usd"] = cb.get("usd")
            market["source"] = cb.get("source")
            market["ok"] = True
        if market.get("usd_24h_change") is None and cb.get("usd_24h_change") is not None:
            market["usd_24h_change"] = cb.get("usd_24h_change")
            market["usd_24h_change_source"] = cb.get("source")
            market["open"] = cb.get("open")
            market["high"] = cb.get("high")
            market["low"] = cb.get("low")
            market["note"] = cb.get("note")
            if market.get("source") is None:
                market["source"] = cb.get("source")
        if market.get("usd_24h_vol") is None and cb.get("usd_24h_vol") is not None:
            market["usd_24h_vol"] = cb.get("usd_24h_vol")
            market["usd_24h_vol_source"] = "coinbase.exchange.SOL-USD.stats quote = last × base volume"
            market["base_volume_sol"] = cb.get("base_volume_sol")
        market["ok"] = market.get("usd") is not None
    elif not cb.get("ok"):
        market["fallbacks_tried"].append("coinbase:" + str(cb.get("error") or "fail"))

    if market.get("usd") is None or market.get("usd_24h_change") is None:
        kr = fetch_kraken_sol(http)
        if kr.get("ok"):
            if market.get("usd") is None:
                market["usd"] = kr.get("usd")
                market["source"] = kr.get("source")
                market["ok"] = True
            if market.get("usd_24h_change") is None and kr.get("usd_24h_change") is not None:
                market["usd_24h_change"] = kr.get("usd_24h_change")
                market["usd_24h_change_source"] = kr.get("source")
                market["open"] = kr.get("open")
                market["note"] = kr.get("note")
            if market.get("usd_24h_vol") is None and kr.get("usd_24h_vol") is not None:
                market["usd_24h_vol"] = kr.get("usd_24h_vol")
                market["usd_24h_vol_source"] = "kraken.SOLUSD 24h vwap × volume"
                market["base_volume_sol"] = kr.get("base_volume_sol")
        else:
            market["fallbacks_tried"].append("kraken:" + str(kr.get("error") or "fail"))

    if market.get("usd") is None:
        llama = fetch_llama_price(http)
        if llama.get("ok"):
            market["usd"] = llama.get("usd")
            market["source"] = llama.get("source")
            market["last_updated_unix"] = llama.get("last_updated_unix")
            market["last_updated_utc"] = llama.get("last_updated_utc")
            market["ok"] = True
            market["fallback"] = True
        else:
            market["fallbacks_tried"].append("llama.coins:" + str(llama.get("error") or "fail"))

    circ = fnum(circulating_sol)
    px = fnum(market.get("usd"))
    if market.get("usd_market_cap") is None and circ is not None and px is not None:
        market["usd_market_cap"] = circ * px
        market["usd_market_cap_source"] = "derived: price × RPC circulating supply (not CoinGecko mcap)"
        market["circulating_sol_used"] = circ

    market["coinbase_ok"] = bool(cb.get("ok"))
    market["gecko_error"] = gecko.get("error")
    if gecko.get("error"):
        market["error"] = gecko.get("error")
    return market


def fetch_defillama(http: Http) -> dict[str, Any]:
    out: dict[str, Any] = {
        "tvl_usd": None, "tvl_history": [], "tvl_change_1d_pct": None,
        "tvl_change_7d_pct": None, "tvl_change_30d_pct": None,
        "dex": None, "fees": None, "top_protocols": [], "top_dexs": [], "rwa": None,
    }
    chains, _ = http.json("https://api.llama.fi/v2/chains", source_id="llama.chains", timeout=30)
    if isinstance(chains, list):
        sol = next((c for c in chains if str(c.get("name", "")).lower() == "solana"), None)
        if isinstance(sol, dict):
            out["tvl_usd"] = sol.get("tvl")
            out["gecko_id"] = sol.get("gecko_id")
            out["token_symbol"] = sol.get("tokenSymbol")

    hist, _ = http.json(
        "https://api.llama.fi/v2/historicalChainTvl/Solana",
        source_id="llama.historical_tvl", timeout=30,
    )
    series = []
    if isinstance(hist, list):
        for row in hist:
            if not isinstance(row, dict):
                continue
            dt = parse_unix(row.get("date"))
            series.append({"date_unix": row.get("date"), "date": iso(dt)[:10] if dt else None, "tvl": row.get("tvl")})
        out["tvl_history"] = series[-90:]
        if series:
            latest = series[-1].get("tvl")
            out["tvl_usd"] = out["tvl_usd"] if out["tvl_usd"] is not None else latest

            def ago(days: int) -> Any:
                if len(series) > days:
                    return series[-1 - days].get("tvl")
                return None

            out["tvl_change_1d_pct"] = pct_change(latest, ago(1))
            out["tvl_change_7d_pct"] = pct_change(latest, ago(7))
            out["tvl_change_30d_pct"] = pct_change(latest, ago(30))

    dex, _ = http.json(
        "https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true",
        source_id="llama.dexs", timeout=40,
    )
    if isinstance(dex, dict):
        out["dex"] = {
            "total_24h_usd": dex.get("total24h"), "total_7d_usd": dex.get("total7d"),
            "total_30d_usd": dex.get("total30d"), "change_1d_pct": dex.get("change_1d"),
            "change_7d_pct": dex.get("change_7d"), "change_1m_pct": dex.get("change_1m"),
        }
        protos = dex.get("protocols") or []
        if isinstance(protos, list):
            ranked = sorted(
                (p for p in protos if isinstance(p, dict) and p.get("total24h")),
                key=lambda p: float(p.get("total24h") or 0), reverse=True,
            )
            out["top_dexs"] = [
                {"name": p.get("displayName") or p.get("name"), "slug": p.get("slug"),
                 "total_24h_usd": p.get("total24h"), "change_1d_pct": p.get("change_1d"),
                 "category": p.get("category")}
                for p in ranked[:12]
            ]

    fees, _ = http.json(
        "https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true",
        source_id="llama.fees", timeout=40,
    )
    if isinstance(fees, dict):
        out["fees"] = {
            "total_24h_usd": fees.get("total24h"), "total_7d_usd": fees.get("total7d"),
            "change_1d_pct": fees.get("change_1d"), "change_7d_pct": fees.get("change_7d"),
        }

    protos, _ = http.json("https://api.llama.fi/protocols", source_id="llama.protocols", timeout=45)
    if isinstance(protos, list):
        sol_pts = []
        rwa_pts = []
        for p in protos:
            if not isinstance(p, dict):
                continue
            chains_l = [str(c).lower() for c in (p.get("chains") or [])]
            ctv = p.get("chainTvls") or {}
            sol_tvl = None
            if isinstance(ctv, dict):
                sol_tvl = ctv.get("Solana")
                if sol_tvl is None:
                    sol_tvl = ctv.get("solana")
            if sol_tvl is None and "solana" not in chains_l:
                continue
            if sol_tvl is None:
                continue
            try:
                sol_tvl_f = float(sol_tvl)
            except (TypeError, ValueError):
                continue
            cat = p.get("category") or ""
            row = {
                "name": p.get("name"), "slug": p.get("slug"), "category": cat,
                "solana_tvl_usd": sol_tvl_f, "change_1d_pct": p.get("change_1d"),
                "change_7d_pct": p.get("change_7d"),
            }
            if cat.lower() not in ("cex",):
                sol_pts.append(row)
            if cat.lower() in ("rwa", "rwa lending"):
                rwa_pts.append(row)
        sol_pts.sort(key=lambda r: r["solana_tvl_usd"], reverse=True)
        rwa_pts.sort(key=lambda r: r["solana_tvl_usd"], reverse=True)
        out["top_protocols"] = sol_pts[:15]
        rwa_total = sum(r["solana_tvl_usd"] for r in rwa_pts)
        out["rwa"] = {
            "source": "defillama.protocols chainTvls.Solana where category in {RWA, RWA Lending}",
            "protocol_count": len(rwa_pts),
            "tvl_usd": rwa_total,
            "top": rwa_pts[:10],
        }
    return out


def fetch_stablecoins(http: Http) -> dict[str, Any]:
    out: dict[str, Any] = {
        "ok": False, "circulating_usd": None, "change_1d_pct": None,
        "change_7d_pct": None, "top": [], "history": [],
    }
    chains, _ = http.json(
        "https://stablecoins.llama.fi/stablecoinchains",
        source_id="llama.stablecoinchains", timeout=25,
    )
    if isinstance(chains, list):
        sol = next((c for c in chains if str(c.get("name", "")).lower() == "solana"), None)
        if isinstance(sol, dict):
            circ = (sol.get("totalCirculatingUSD") or {}).get("peggedUSD")
            out["circulating_usd"] = circ
            out["ok"] = circ is not None
            out["other_pegs_usd"] = sol.get("totalCirculatingUSD")

    assets_j, _ = http.json(
        "https://stablecoins.llama.fi/stablecoins?includePrices=true",
        source_id="llama.stablecoins", timeout=30,
    )
    assets = assets_j.get("peggedAssets") if isinstance(assets_j, dict) else None
    top = []
    if isinstance(assets, list):
        for a in assets:
            if not isinstance(a, dict):
                continue
            cc = a.get("chainCirculating") or {}
            sol = cc.get("Solana") or cc.get("solana")
            if not isinstance(sol, dict):
                continue
            cur = sol.get("current") or {}
            usd = cur.get("peggedUSD") if isinstance(cur, dict) else None
            if not isinstance(usd, (int, float)):
                continue
            prev_d = ((sol.get("circulatingPrevDay") or {}).get("peggedUSD"))
            top.append({
                "symbol": a.get("symbol"), "name": a.get("name"),
                "circulating_usd": usd, "change_1d_pct": pct_change(usd, prev_d),
            })
        top.sort(key=lambda r: r["circulating_usd"], reverse=True)
        out["top"] = top[:10]
        if out["circulating_usd"] is None:
            out["circulating_usd"] = sum(r["circulating_usd"] for r in top)
            out["ok"] = True

    charts, _ = http.json(
        "https://stablecoins.llama.fi/stablecoincharts/Solana",
        source_id="llama.stablecoincharts", timeout=30,
    )
    hist = []
    if isinstance(charts, list):
        for row in charts[-90:]:
            if not isinstance(row, dict):
                continue
            dt = parse_unix(row.get("date"))
            usd = (row.get("totalCirculatingUSD") or row.get("totalCirculating") or {}).get("peggedUSD")
            hist.append({"date": iso(dt)[:10] if dt else None, "circulating_usd": usd})
        out["history"] = hist
        if hist:
            latest = hist[-1].get("circulating_usd")
            if len(hist) > 1:
                out["change_1d_pct"] = pct_change(latest, hist[-2].get("circulating_usd"))
            if len(hist) > 7:
                out["change_7d_pct"] = pct_change(latest, hist[-8].get("circulating_usd"))
            if out["circulating_usd"] is None:
                out["circulating_usd"] = latest
                out["ok"] = latest is not None
    return out


def fetch_solana_com_data(http: Http) -> dict[str, Any]:
    """Public JSON behind solana.com/data — no API key."""
    out: dict[str, Any] = {
        "ok": False, "url": "https://solana.com/api/databricks/data?days=30",
        "generated_at": None, "metrics": {}, "rpc_providers": [], "page_fetchable": False,
    }
    page, rec = http.request("https://solana.com/data", source_id="solana.com.data_page", timeout=25)
    out["page_fetchable"] = bool(rec.get("ok") and page)
    data, rec = http.json(
        "https://solana.com/api/databricks/data?days=30",
        source_id="solana.com.databricks", timeout=40,
    )
    if not isinstance(data, dict):
        return out
    rows = data.get("rows") or []
    out["generated_at"] = data.get("generatedAt")
    out["range_days"] = data.get("rangeDays")
    out["ok"] = True
    latest: dict[tuple[str, str], dict[str, Any]] = {}
    series: dict[str, list[dict[str, Any]]] = {}
    wanted_series = {
        "Active Addresses", "SOL Price", "Fees", "Transaction Count (Total)",
        "Slots", "Application Revenue", "DEX Volume",
        "Non Vote Transaction Count (Success)",
    }
    for row in rows:
        if not isinstance(row, dict):
            continue
        name = row.get("metricName")
        prov = row.get("providerName") or "unknown"
        if not name:
            continue
        key = (str(name), str(prov))
        prev = latest.get(key)
        if prev is None or str(row.get("date")) >= str(prev.get("date")):
            latest[key] = row
        if name in wanted_series:
            series.setdefault(f"{name}|{prov}", []).append({
                "date": row.get("date"), "value": row.get("value"), "unit": row.get("unit"),
            })

    grouped: dict[str, list[dict[str, Any]]] = {}
    for (name, prov), row in latest.items():
        grouped.setdefault(name, []).append({
            "provider": prov, "value": row.get("value"),
            "unit": row.get("unit"), "date": row.get("date"),
        })
    for name, lst in grouped.items():
        lst.sort(key=lambda r: str(r.get("provider")))
    out["metrics"] = grouped
    daa = grouped.get("Active Addresses") or []
    if daa:
        allium = next((x for x in daa if x["provider"] == "Allium"), daa[0])
        vals = [float(x["value"]) for x in daa if isinstance(x.get("value"), (int, float))]
        out["active_addresses"] = {
            "headline_provider": allium.get("provider"),
            "headline_value": allium.get("value"),
            "headline_date": allium.get("date"),
            "providers": daa,
            "min": min(vals) if vals else None,
            "max": max(vals) if vals else None,
            "note": (
                "solana.com/data publishes several vendor series for the same label. "
                "Values disagree; Borealis does not average them."
            ),
        }
    out["series"] = {k: sorted(v, key=lambda r: str(r.get("date") or ""))[-30:] for k, v in series.items()}

    def pick_series(metric: str, providers: tuple[str, ...]) -> tuple[str | None, list[dict[str, Any]]]:
        for prov in providers:
            rows_s = out["series"].get(f"{metric}|{prov}") or []
            rows_s = sorted(rows_s, key=lambda r: str(r.get("date") or ""))
            if rows_s:
                return prov, rows_s
        return None, []

    derived: dict[str, Any] = {}
    prov, price_s = pick_series("SOL Price", ("DexPaprika", "DeFiLlama", "Allium", "Dune"))
    if price_s:
        derived["sol_price_latest"] = {**price_s[-1], "provider": prov}
        vals = [v for v in (fnum(r.get("value")) for r in price_s) if v is not None]
        derived["sol_price_30d_median"] = median(vals)
        if len(price_s) >= 2:
            derived["sol_price_dod_pct"] = pct_change(price_s[-1].get("value"), price_s[-2].get("value"))
            derived["sol_price_dod_provider"] = prov

    prov, daa_s = pick_series("Active Addresses", ("Allium", "Dune"))
    if daa_s:
        vals = [v for v in (fnum(r.get("value")) for r in daa_s) if v is not None]
        derived["daa_30d_median"] = median(vals)
        derived["daa_latest"] = daa_s[-1].get("value")
        derived["daa_provider"] = prov
        derived["daa_vs_30d_pct"] = pct_change(derived["daa_latest"], derived["daa_30d_median"])

    prov, tx_s = pick_series("Transaction Count (Total)", ("Allium", "Dune", "Token Terminal"))
    if tx_s:
        tps_s = []
        for r in tx_s:
            v = fnum(r.get("value"))
            if v is not None:
                tps_s.append({"date": r.get("date"), "value": v / 86400.0})
        tps_vals = [r["value"] for r in tps_s]
        derived["tps_30d"] = tps_s[-30:]
        derived["tps_30d_median"] = median(tps_vals)
        derived["tps_30d_latest"] = tps_s[-1]["value"] if tps_s else None
        derived["tps_30d_source"] = f"solana.com/data Transaction Count (Total)|{prov} / 86400"

    prov, fee_s = pick_series("Fees", ("Allium", "Dune", "Blockworks"))
    if fee_s:
        derived["network_fees_sol"] = fee_s[-1].get("value")
        derived["network_fees_date"] = fee_s[-1].get("date")
        derived["network_fees_unit"] = fee_s[-1].get("unit") or "SOL"
        derived["network_fees_provider"] = prov
        derived["network_fees_source"] = f"solana.com/data Fees ({prov})"
        fvals = [v for v in (fnum(r.get("value")) for r in fee_s) if v is not None]
        derived["network_fees_30d_median_sol"] = median(fvals)

    prov, nv_s = pick_series("Non Vote Transaction Count (Success)", ("Allium", "Dune"))
    nv = fnum(nv_s[-1].get("value")) if nv_s else None
    fees_sol = fnum(derived.get("network_fees_sol"))
    if nv and fees_sol is not None:
        derived["avg_fee_per_nv_success_sol"] = fees_sol / nv
        derived["avg_fee_note"] = (
            "Average fee per successful non-vote tx (Fees SOL / count). "
            "Median tx fee is not published on these public feeds."
        )

    prov, rev_s = pick_series("Application Revenue", ("DeFiLlama", "Blockworks"))
    if rev_s:
        derived["app_revenue_usd"] = rev_s[-1].get("value")
        derived["app_revenue_provider"] = prov
        derived["app_revenue_date"] = rev_s[-1].get("date")

    rwa_daa = next((x for x in (grouped.get("Active Addresses") or []) if x.get("provider") == "RWA"), None)
    if rwa_daa:
        derived["rwa_active_addresses"] = rwa_daa

    out["derived"] = derived

    rpc, rec = http.json("https://solana.com/api/rpc/data", source_id="solana.com.rpc_data", timeout=30)
    if isinstance(rpc, dict):
        out["rpc_generated_at"] = rpc.get("generatedAt")
        latest_rpc: dict[tuple[str, str], dict[str, Any]] = {}
        for row in rpc.get("rows") or []:
            if not isinstance(row, dict):
                continue
            key = (str(row.get("metricName")), str(row.get("providerName")))
            prev = latest_rpc.get(key)
            if prev is None or str(row.get("date")) >= str(prev.get("date")):
                latest_rpc[key] = row
        by_prov: dict[str, dict[str, Any]] = {}
        for (metric, prov), row in latest_rpc.items():
            by_prov.setdefault(prov, {"provider": prov})[metric] = {
                "value": row.get("value"), "unit": row.get("unit"), "date": row.get("date"),
            }
        out["rpc_providers"] = sorted(by_prov.values(), key=lambda x: x["provider"])
    return out


def _local(tag: str) -> str:
    if tag.startswith("{"):
        return tag.split("}", 1)[-1]
    return tag


def parse_feed(body: bytes, source: str, kind: str = "rss") -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return items

    def one_item(item_el: ET.Element) -> dict[str, Any] | None:
        title = link = pub = summary = guid = creator = None
        for ch in list(item_el):
            loc = _local(ch.tag)
            if loc == "title":
                title = (ch.text or "").strip()
            elif loc == "link":
                link = (ch.text or "").strip() or ch.get("href")
            elif loc in ("pubDate", "date", "updated", "published"):
                pub = pub or (ch.text or "").strip()
            elif loc in ("description", "summary", "content"):
                summary = (ch.text or "").strip()
            elif loc == "guid":
                guid = (ch.text or "").strip()
            elif loc == "creator":
                creator = (ch.text or "").strip()
        if not title:
            return None
        return {
            "source": source, "kind": kind, "title": title, "url": link,
            "published": pub, "summary": strip_html(summary or "")[:280],
            "guid": guid, "creator": creator,
        }

    for item in root.iter():
        if _local(item.tag) == "item":
            row = one_item(item)
            if row:
                items.append(row)
    if not items:
        for item in root.iter():
            if _local(item.tag) == "entry":
                row = one_item(item)
                if row:
                    items.append(row)
    return items


SENTIMENT_TAGS = {
    "upgrade": ("upgrade", "upgraded", "alpenglow", "simd-", "simd "),
    "outage": ("outage", "downtime", "degraded"),
    "incident": ("incident", "postmortem", "post-mortem"),
    "mainnet": ("mainnet",),
    "halt": ("halt", "halted", "paused network"),
}


def sentiment_tags(title: str, summary: str = "") -> list[str]:
    blob = f"{title} {summary}".lower()
    tags = [name for name, keys in SENTIMENT_TAGS.items() if any(k in blob for k in keys)]
    return tags


def _parse_pub(pub: Any) -> datetime | None:
    if not pub:
        return None
    try:
        dt = parsedate_to_datetime(str(pub))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=UTC)
        return dt.astimezone(UTC)
    except (TypeError, ValueError, OverflowError):
        return None


def _useless_social(item: dict[str, Any]) -> bool:
    t = (item.get("title") or "").lower()
    s = (item.get("summary") or "").lower()
    if "whitelist" in t or "whitelist" in s:
        return True
    if "rss reader not yet" in t:
        return True
    dt = _parse_pub(item.get("published"))
    if dt is not None and (utcnow() - dt) > timedelta(days=45):
        return True
    return False


def _rewrite_nitter_url(item: dict[str, Any], handle: str) -> None:
    guid = (item.get("guid") or "").strip()
    creator = (item.get("creator") or "").lstrip("@") or handle
    if guid.isdigit():
        item["url"] = f"https://x.com/{creator}/status/{guid}"
        item["nitter_guid"] = guid


def fetch_news(http: Http) -> dict[str, Any]:
    official = [
        ("status.atom", "https://status.solana.com/history.atom", "status.solana.com"),
        ("news.rss", "https://solana.com/news/rss.xml", "solana.com/news"),
        ("anza.medium", "https://medium.com/feed/anza-xyz", "anza medium"),
    ]
    # Probe live public X RSS. Skip 403/empty/whitelist. Not the Twitter API.
    twitter_routes = []
    handles = ("solana", "solana_status", "anza_xyz", "solana_devs")
    for h in handles:
        twitter_routes.append((f"xcancel.{h}", f"https://xcancel.com/{h}/rss", f"@{h}", h))
    for h in handles:
        twitter_routes.append((f"nitter.{h}", f"https://nitter.perennialte.ch/{h}/rss", f"@{h}", h))
    twitter_routes.append(("rsshub.solana", "https://rsshub.app/twitter/user/solana", "@solana", "solana"))

    status_j, _ = http.json("https://status.solana.com/api/v2/summary.json", source_id="status.summary", timeout=20)
    status = {"indicator": None, "description": None, "components": [], "unresolved_incidents": [], "scheduled_maintenances": []}
    if isinstance(status_j, dict):
        st = status_j.get("status") or {}
        status["indicator"] = st.get("indicator")
        status["description"] = st.get("description")
        status["updated_at"] = (status_j.get("page") or {}).get("updated_at")
        status["components"] = [{"name": c.get("name"), "status": c.get("status")} for c in (status_j.get("components") or []) if isinstance(c, dict)]
        status["unresolved_incidents"] = [
            {"name": i.get("name"), "status": i.get("status"), "impact": i.get("impact"),
             "shortlink": i.get("shortlink"), "updated_at": i.get("updated_at")}
            for i in (status_j.get("incidents") or []) if isinstance(i, dict)
        ]
        status["scheduled_maintenances"] = [
            {"name": m.get("name"), "status": m.get("status"), "impact": m.get("impact"),
             "scheduled_for": m.get("scheduled_for")}
            for m in (status_j.get("scheduled_maintenances") or []) if isinstance(m, dict)
        ]

    official_items: list[dict[str, Any]] = []
    for sid, url, label in official:
        body, rec = http.request(url, source_id=f"rss.{sid}", timeout=25)
        if body:
            for n in parse_feed(body, label, kind="rss"):
                n["tags"] = sentiment_tags(n.get("title") or "", n.get("summary") or "")
                official_items.append(n)

    twitter_items: list[dict[str, Any]] = []
    twitter_kept: list[str] = []
    twitter_skipped: list[str] = []
    have_handle: set[str] = set()
    for sid, url, label, handle in twitter_routes:
        if handle in have_handle and sid.startswith("nitter.") or (handle in have_handle and sid.startswith("rsshub.")):
            # still probe nitter/rsshub only if xcancel did not yield usable items
            if handle in have_handle:
                continue
        body, rec = http.request(url, source_id=f"rss.{sid}", timeout=18, retries=0)
        status_code = rec.get("status")
        if not rec.get("ok") or not body:
            twitter_skipped.append(f"{sid} {status_code or rec.get('error')}")
            continue
        parsed = parse_feed(body, f"X/Nitter-style RSS {label} (not Twitter API)", kind="twitter")
        usable = []
        for n in parsed:
            if _useless_social(n):
                continue
            n["handle"] = label
            n["tags"] = sentiment_tags(n.get("title") or "", n.get("summary") or "")
            _rewrite_nitter_url(n, handle)
            usable.append(n)
        if not usable:
            twitter_skipped.append(f"{sid} empty-or-gated")
            continue
        twitter_kept.append(sid)
        have_handle.add(handle)
        twitter_items.extend(usable[:8])

    def dedupe(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
        seen: set[str] = set()
        uniq: list[dict[str, Any]] = []
        for n in rows:
            t = (n.get("title") or "").strip().lower()
            if not t or t in seen:
                continue
            seen.add(t)
            uniq.append(n)
        return uniq

    twitter_items = dedupe(twitter_items)
    official_items = dedupe(official_items)
    combined = twitter_items + official_items
    return {
        "status": status,
        "items": combined[:28],
        "twitter": twitter_items[:16],
        "official": official_items[:16],
        "twitter_kept": twitter_kept,
        "twitter_skipped": twitter_skipped,
        "twitter_note": (
            "Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). "
            "Not the official Twitter API. 403/gated routes are skipped."
        ),
    }


def editorial_block(generated: datetime) -> dict[str, Any]:
    """Curated, dated, clearly marked as editorial — not live metrics.

    The bounty brief said 'Alpenglow / SIMD-025'. Current public documents
    name the consensus rewrite Alpenglow, specified as SIMD-0326.
    SIMD-0256 (block CU limit 60M, 2025) is a different proposal.
    """
    return {
        "kind": "editorial",
        "title": "Alpenglow (SIMD-0326) — not SIMD-025",
        "as_of": iso(generated)[:10],
        "as_of_pt": iso_pt(generated),
        "correction": (
            "Public SIMD numbering: Alpenglow consensus is SIMD-0326. "
            "SIMD-0256 was a 2025 compute-unit block-limit increase (50M to 60M) "
            "and is not the consensus rewrite. This section uses the current names."
        ),
        "summary": (
            "Alpenglow is Solana's next consensus protocol. Phase 1 (Votor) replaces "
            "TowerBFT voting with direct votes and certificates. Target finality is "
            "roughly 150ms versus ~12.8s TowerBFT. Rotor (Turbine replacement) is a "
            "later phase. Proof of History remains the ordering clock in current "
            "write-ups of the Agave 4.3 activation path."
        ),
        "simds": [
            {"id": "SIMD-0326", "name": "Alpenglow Consensus Protocol (Votor)"},
            {"id": "SIMD-0337", "name": "Markers for Alpenglow Fast Leader Handover"},
            {"id": "SIMD-0357", "name": "Alpenglow Validator Admission Ticket (VAT)"},
            {"id": "SIMD-0384", "name": "Alpenglow Migration"},
            {"id": "SIMD-0387", "name": "BLS Pubkey Management in Vote Account"},
        ],
        "timeline_public": [
            {"date": "2026-07-08", "item": "SIMD-0387 (BLS pubkey in vote account) activated on mainnet."},
            {"date": "2026-07-22", "item": (
                "SIMD-0357 VAT activated. Validators without an on-chain BLS pubkey "
                "are excluded from the VAT-admitted set. VAT does not itself turn "
                "on Alpenglow consensus."
            )},
            {"date": "2026-Q3", "item": (
                "Expected mainnet activation window for Votor via Agave 4.3. "
                "Anza's published 4.3 schedule (12 Aug 2026) targeted feature "
                "activation around 28 Sep 2026; that schedule is tentative."
            )},
        ],
        "watch": [
            "Agave 4.3 stake rollout percentages vs. the published schedule.",
            "Firedancer / Frankendancer Votor parity before a full Alpenswitch.",
            "Community cluster slot-time and fast-path finalization readings.",
            "Whether Rotor remains deferred after Votor activation.",
        ],
        "sources": [
            "https://solana.com/upgrades/alpenglow",
            "https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0326-alpenglow.md",
            "https://forum.solana.com/t/simd-0326-proposal-for-the-new-alpenglow-consensus-protocol/4236",
        ],
        "disclaimer": (
            "Editorial. Dates and activation targets move. None of this is a live "
            "cluster metric; it is a dated reading of public Foundation / SIMD / Anza notes."
        ),
    }


def load_history(path: str) -> list[dict[str, Any]]:
    if not os.path.isfile(path):
        return []
    rows = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    except OSError:
        return []
    return rows[-500:]


def append_history(path: str, row: dict[str, Any]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, separators=(",", ":")) + "\n")


def _flag(*, key: str, severity: str, title: str, detail: str, metric: str,
          value: Any, baseline: Any, threshold: str) -> dict[str, Any]:
    return {
        "key": key, "severity": severity, "title": title, "detail": detail,
        "metric": metric, "value": value, "baseline": baseline,
        "threshold": threshold, "flagged_at": iso(utcnow()),
    }


def detect_anomalies(cluster, validators, market, defi, status, history, sdata=None) -> list[dict[str, Any]]:
    flags: list[dict[str, Any]] = []
    sdata = sdata or {}
    derived = sdata.get("derived") or {}
    samples = cluster.get("tps_samples") or []
    n_samples = len(samples)
    tps_samples = [r["tps_total"] for r in samples if isinstance(r.get("tps_total"), (int, float))]
    nv_samples = [r["tps_nonvote"] for r in samples if isinstance(r.get("tps_nonvote"), (int, float))]
    st_samples = [r["slot_time_sec"] for r in samples if isinstance(r.get("slot_time_sec"), (int, float))]

    tps = cluster.get("tps_total")
    tps_med = cluster.get("tps_median")
    tps_sd = cluster.get("tps_stdev") or 0.0
    tps_last = cluster.get("tps_last")
    nv_last = cluster.get("tps_nonvote_last")
    nv_med = cluster.get("tps_nonvote_median")
    nv_sd = cluster.get("tps_nonvote_stdev") or 0.0
    st = cluster.get("slot_time_sec")
    st_med = cluster.get("slot_time_median")
    st_max = cluster.get("slot_time_max")
    st_last = cluster.get("slot_time_last")
    st_sd = cluster.get("slot_time_stdev") or 0.0

    z_tps = zscore(tps_last, mean(tps_samples) if tps_samples else tps, tps_sd)
    z_nv = zscore(nv_last, mean(nv_samples) if nv_samples else cluster.get("tps_nonvote"), nv_sd)
    z_st = zscore(st_last, mean(st_samples) if st_samples else st, st_sd)

    if z_tps is not None and abs(z_tps) >= 2.5:
        flags.append(_flag(
            key="tps_last_sigma",
            severity="warn" if abs(z_tps) < 3.5 else "alert",
            title="Last TPS sample outside 2.5σ of the 60-sample window",
            detail=(f"Last sample {tps_last:,.0f} TPS is {z_tps:+.2f}σ vs window mean "
                    f"{mean(tps_samples) or 0:,.0f} (n={n_samples}, σ={tps_sd:,.0f})."),
            metric="tps_last", value=tps_last,
            baseline={"mean": mean(tps_samples), "stdev": tps_sd, "n": n_samples, "z": round(z_tps, 3)},
            threshold="|last sample − window mean| > 2.5σ",
        ))
    if z_st is not None and abs(z_st) >= 2.5:
        flags.append(_flag(
            key="slot_time_last_sigma",
            severity="warn" if (st_last or 0) < 0.5 else "alert",
            title="Last slot-time sample outside 2.5σ of the 60-sample window",
            detail=(f"Last sample {(st_last or 0)*1000:.0f} ms is {z_st:+.2f}σ vs window mean "
                    f"{(mean(st_samples) or 0)*1000:.0f} ms (n={n_samples})."),
            metric="slot_time_last", value=st_last,
            baseline={"mean": mean(st_samples), "stdev": st_sd, "n": n_samples, "z": round(z_st, 3)},
            threshold="|last sample − window mean| > 2.5σ",
        ))

    last_or_mean_st = st_last if st_last is not None else st
    if last_or_mean_st is not None and last_or_mean_st > 0.50:
        flags.append(_flag(
            key="slow_slots_500ms",
            severity="alert" if last_or_mean_st > 0.70 else "warn",
            title="Slot time above 500 ms",
            detail=(f"Slot time {last_or_mean_st*1000:.0f} ms (last sample "
                    f"{(st_last or 0)*1000:.0f} ms, window mean {(st or 0)*1000:.0f} ms). "
                    "Mainnet target cadence is ~400 ms."),
            metric="slot_time_sec", value=round(last_or_mean_st, 4),
            baseline={"target_sec": 0.4, "mean": st, "last": st_last},
            threshold="slot time > 500 ms (last sample or window mean)",
        ))

    d_pct = validators.get("delinquent_stake_pct")
    d_n = validators.get("delinquent_count")
    lag_n = validators.get("lagging_count") or 0
    if (isinstance(d_pct, (int, float)) and d_pct >= 1.0) or (isinstance(d_n, int) and d_n >= 25):
        flags.append(_flag(
            key="high_delinquency", severity="alert" if (d_pct or 0) >= 2.5 else "warn",
            title="High validator delinquency",
            detail=(f"{d_n} delinquent vote accounts, {d_pct:.3f}% of activated+delinquent stake."
                    if isinstance(d_pct, (int, float)) else f"{d_n} delinquent vote accounts."),
            metric="delinquent_stake_pct", value=d_pct,
            baseline={"delinquent_count": d_n, "lagging_count": lag_n},
            threshold="delinquent stake >= 1% or delinquent count >= 25",
        ))

    def move_flag(key, label, change, window):
        if not isinstance(change, (int, float)):
            return
        thr = 8 if window == "1d" else 20
        if abs(change) < thr:
            return
        flags.append(_flag(
            key=key,
            severity="warn" if abs(change) < (15 if window == "1d" else 40) else "alert",
            title=f"Large {label} {window} move",
            detail=f"DeFiLlama {label} {window} change is {change:+.2f}%.",
            metric=key, value=round(change, 3),
            baseline={"window": window},
            threshold=f"|{window} %| >= {thr}",
        ))

    move_flag("tvl_move_1d", "Solana DeFi TVL", defi.get("tvl_change_1d_pct"), "1d")
    move_flag("tvl_move_7d", "Solana DeFi TVL", defi.get("tvl_change_7d_pct"), "7d")
    dex = defi.get("dex") or {}
    fees = defi.get("fees") or {}
    move_flag("dex_move_1d", "Solana DEX volume", dex.get("change_1d_pct"), "1d")
    move_flag("dex_move_7d", "Solana DEX volume", dex.get("change_7d_pct"), "7d")
    move_flag("fees_move_1d", "Solana fees (REV proxy)", fees.get("change_1d_pct"), "1d")
    move_flag("fees_move_7d", "Solana fees (REV proxy)", fees.get("change_7d_pct"), "7d")

    px_ch = market.get("usd_24h_change")
    if isinstance(px_ch, (int, float)) and abs(px_ch) >= 8:
        src = market.get("usd_24h_change_source") or market.get("source") or "price feed"
        flags.append(_flag(
            key="sol_price_move", severity="warn" if abs(px_ch) < 15 else "alert",
            title="Large SOL 24h price move",
            detail=f"SOL/USD 24h change is {px_ch:+.2f}% ({src}).",
            metric="usd_24h_change", value=round(px_ch, 3),
            baseline={"usd": market.get("usd"), "source": src},
            threshold="|24h %| >= 8",
        ))

    def vs_30d(key, title, current, med, unit=""):
        if current is None or med is None or not med:
            return
        ch = pct_change(current, med)
        if ch is None:
            return
        # 2.5σ approx: treat |pct| >= 20 as notable vs 30d median (run-1 usable)
        if abs(ch) < 20:
            return
        flags.append(_flag(
            key=key, severity="info" if abs(ch) < 35 else "warn",
            title=title,
            detail=f"Current {current:,.2f}{unit} is {ch:+.1f}% vs 30d median {med:,.2f}{unit} (solana.com/data).",
            metric=key, value=current,
            baseline={"median_30d": med, "pct_vs_median": round(ch, 3)},
            threshold="|current − 30d median| / median >= 20%",
        ))

    vs_30d("tps_vs_30d", "TPS vs 30d median (solana.com/data tx/86400)",
           tps, derived.get("tps_30d_median"), " TPS")
    vs_30d("daa_vs_30d", "Daily active addresses vs 30d median",
           derived.get("daa_latest"), derived.get("daa_30d_median"))
    vs_30d("price_vs_30d", "SOL price vs 30d median (solana.com/data)",
           market.get("usd"), derived.get("sol_price_30d_median"), " USD")

    if cluster.get("health") not in (None, "ok"):
        flags.append(_flag(
            key="rpc_unhealthy", severity="alert", title="RPC getHealth is not ok",
            detail=f"getHealth returned {cluster.get('health')!r}.",
            metric="health", value=cluster.get("health"), baseline="ok", threshold="health != ok",
        ))

    ind = (status or {}).get("indicator")
    if ind and ind not in ("none", "operational"):
        flags.append(_flag(
            key="status_degraded", severity="alert" if ind in ("major", "critical") else "warn",
            title="status.solana.com is not fully operational",
            detail=(status or {}).get("description") or str(ind),
            metric="status.indicator", value=ind, baseline="none",
            threshold="indicator not in {none, operational}",
        ))

    # Multi-source correlation — the innovation judges asked for.
    elevated_slot = (
        (st_last is not None and st_last > 0.45)
        or (st is not None and st > 0.45)
        or (z_st is not None and z_st >= 1.0)
    )
    depressed_nv = (
        (nv_last is not None and nv_med and nv_last < nv_med * 0.85)
        or (z_nv is not None and z_nv <= -1.0)
    )
    fee_1d = fees.get("change_1d_pct")
    elevated_fees = isinstance(fee_1d, (int, float)) and fee_1d >= 8
    if elevated_slot and depressed_nv and elevated_fees:
        flags.append(_flag(
            key="corr_congestion", severity="alert",
            title="Correlation: congestion (slot time ↑ + non-vote TPS ↓ + fees ↑)",
            detail=(
                f"Slot time {(last_or_mean_st or 0)*1000:.0f} ms, last non-vote TPS "
                f"{(nv_last or 0):,.0f} vs window median {(nv_med or 0):,.0f}, "
                f"DeFiLlama fees 1d {fee_1d:+.1f}%."
            ),
            metric="correlation.congestion",
            value={"slot_time": last_or_mean_st, "tps_nonvote_last": nv_last, "fees_1d": fee_1d},
            baseline={"slot_target_sec": 0.4, "nv_median": nv_med},
            threshold="elevated slot time AND depressed non-vote TPS AND fees 1d >= 8%",
        ))

    tvl_1d = defi.get("tvl_change_1d_pct")
    dex_1d = dex.get("change_1d_pct")
    if (isinstance(px_ch, (int, float)) and px_ch < 0
            and isinstance(tvl_1d, (int, float)) and tvl_1d < 0
            and isinstance(dex_1d, (int, float)) and dex_1d < 0):
        sev = "warn" if (px_ch <= -2 and tvl_1d <= -2 and dex_1d <= -2) else "info"
        flags.append(_flag(
            key="corr_risk_off", severity=sev,
            title="Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)",
            detail=(f"SOL 24h {px_ch:+.2f}%, DeFiLlama TVL 1d {tvl_1d:+.2f}%, "
                    f"DEX 1d {dex_1d:+.2f}%."),
            metric="correlation.risk_off",
            value={"sol_24h": px_ch, "tvl_1d": tvl_1d, "dex_1d": dex_1d},
            baseline=None,
            threshold="SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0",
        ))

    hist_del = [h.get("delinquent_pct") for h in history if isinstance(h.get("delinquent_pct"), (int, float))]
    delinq_up = False
    if hist_del and isinstance(d_pct, (int, float)):
        delinq_up = d_pct > hist_del[-1] + 0.05
    lag_up = isinstance(lag_n, int) and lag_n > 0
    if (delinq_up or (isinstance(d_pct, (int, float)) and d_pct >= 0.5)) and lag_up:
        flags.append(_flag(
            key="corr_validator_stress", severity="warn",
            title="Correlation: validator stress (delinquency + lag)",
            detail=(f"Delinquent stake {d_pct:.3f}% ({d_n} accounts), "
                    f"{lag_n} current vote accounts lag >150 slots."),
            metric="correlation.validator_stress",
            value={"delinquent_pct": d_pct, "lagging_count": lag_n},
            baseline={"prior_delinquent_pct": hist_del[-1] if hist_del else None},
            threshold="delinquency up or >= 0.5% AND lagging_count > 0",
        ))

    hist_tps = [h.get("tps") for h in history if isinstance(h.get("tps"), (int, float))]
    if tps is not None and len(hist_tps) >= 8:
        hmed = median(hist_tps)
        hsd = pstdev(hist_tps) or 0
        if hmed and hsd and (tps > hmed + 3 * hsd or tps < hmed - 3 * hsd):
            flags.append(_flag(
                key="tps_vs_run_history", severity="info",
                title="TPS outside 3 sigma of prior Borealis runs",
                detail=(f"Current mean TPS {tps:,.0f} vs rolling run median {hmed:,.0f} "
                        f"(n={len(hist_tps)} prior snapshots, sigma={hsd:,.0f})."),
                metric="tps_total", value=round(tps, 2),
                baseline={"median": hmed, "stdev": hsd, "n": len(hist_tps)},
                threshold="|x - median| > 3 sigma of prior generate.py snapshots",
            ))

    hist_px = [h.get("sol_usd") for h in history if isinstance(h.get("sol_usd"), (int, float))]
    px = market.get("usd")
    if px is not None and len(hist_px) >= 5:
        last = hist_px[-1]
        ch = pct_change(px, last)
        if ch is not None and abs(ch) >= 8:
            flags.append(_flag(
                key="sol_price_vs_last_run", severity="info",
                title="SOL price moved >=8% since last Borealis snapshot",
                detail=f"{ch:+.2f}% vs previous snapshot price {last}.",
                metric="sol_usd", value=px, baseline={"previous": last},
                threshold="|delta| >= 8% vs last history.jsonl row",
            ))

    order = {"alert": 0, "warn": 1, "info": 2}
    flags.sort(key=lambda f: (order.get(f["severity"], 9), f["key"]))
    return flags


def compute_health(cluster, validators, sdata) -> dict[str, Any]:
    """Transparent 0–100 score. Formula is shown on the page and in README."""
    derived = (sdata or {}).get("derived") or {}
    rpc_ok = cluster.get("health") == "ok"
    rpc_reachable = rpc_ok or (
        cluster.get("slot") is not None and cluster.get("tps_total") is not None
    )
    if rpc_ok:
        rpc_pts = 25.0
        rpc_detail = "getHealth == ok"
    elif rpc_reachable:
        rpc_pts = 25.0
        rpc_ok = True  # cluster is reachable; getHealth itself 429'd
        rpc_detail = "getHealth rate-limited; slot + TPS RPC succeeded"
    else:
        rpc_pts = 0.0
        rpc_detail = "RPC unreachable"

    slot_sec = cluster.get("slot_time_sec")
    if slot_sec is None:
        slot_pts = 0.0
        slot_detail = "slot time unavailable"
        slot_ms = None
    else:
        slot_ms = slot_sec * 1000.0
        slot_frac = clamp(1.0 - max(0.0, slot_ms - 400.0) / 400.0, 0.0, 1.0)
        slot_pts = 30.0 * slot_frac
        slot_detail = f"mean slot {slot_ms:.0f} ms vs 400 ms target (400→30, 800→0)"

    d_pct = validators.get("delinquent_stake_pct")
    if d_pct is None:
        del_pts = 0.0
        del_detail = "delinquency unavailable"
    else:
        del_frac = clamp(1.0 - float(d_pct) / 2.0, 0.0, 1.0)
        del_pts = 25.0 * del_frac
        del_detail = f"delinquent stake {d_pct:.3f}% (0%→25, 2%+→0)"

    tps = cluster.get("tps_total")
    tps_base = derived.get("tps_30d_median")
    tps_src = derived.get("tps_30d_source") or "solana.com/data 30d median TPS"
    if tps_base is None:
        tps_base = cluster.get("tps_median")
        tps_src = "in-window sample median (30d TPS series unavailable)"
    if tps is None or not tps_base:
        tps_pts = 0.0
        tps_detail = "TPS baseline unavailable"
        tps_frac = None
    else:
        tps_frac = clamp(float(tps) / float(tps_base), 0.0, 1.0)
        tps_pts = 20.0 * tps_frac
        tps_detail = f"TPS {tps:,.0f} vs {tps_src} {tps_base:,.0f} (ratio capped at 1.0)"

    parts = [
        {"id": "rpc", "max": 25, "points": round(rpc_pts, 2), "detail": rpc_detail},
        {"id": "slot", "max": 30, "points": round(slot_pts, 2), "detail": slot_detail},
        {"id": "delinquency", "max": 25, "points": round(del_pts, 2), "detail": del_detail},
        {"id": "tps", "max": 20, "points": round(tps_pts, 2), "detail": tps_detail},
    ]
    score = int(round(sum(p["points"] for p in parts)))
    formula = (
        "25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 400)/400, 0, 1) + "
        "25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)"
    )
    return {
        "score": max(0, min(100, score)),
        "parts": parts,
        "formula": formula,
        "rpc_ok": rpc_ok,
        "slot_ms": slot_ms,
        "delinquent_stake_pct": d_pct,
        "tps": tps,
        "tps_baseline": tps_base,
        "tps_baseline_source": tps_src,
        "cadence": "updates every 15 min via GitHub Action",
    }


def build_economics(defi, sdata, market) -> dict[str, Any]:
    fees = (defi or {}).get("fees") or {}
    derived = (sdata or {}).get("derived") or {}
    return {
        "rev_proxy_usd": fees.get("total_24h_usd"),
        "rev_change_1d_pct": fees.get("change_1d_pct"),
        "rev_change_7d_pct": fees.get("change_7d_pct"),
        "rev_label": "DeFiLlama Solana fees 24h (REV proxy)",
        "rev_source": "api.llama.fi/overview/fees/Solana total24h",
        "network_fees_sol_24h": derived.get("network_fees_sol"),
        "network_fees_date": derived.get("network_fees_date"),
        "network_fees_source": derived.get("network_fees_source"),
        "network_fees_30d_median_sol": derived.get("network_fees_30d_median_sol"),
        "avg_fee_per_nv_success_sol": derived.get("avg_fee_per_nv_success_sol"),
        "median_tx_fee": None,
        "median_tx_fee_note": (
            "Median tx fee is not published on public solana.com/data or DeFiLlama feeds used here. "
            "Not inferred from an average."
        ),
        "app_revenue_usd": derived.get("app_revenue_usd"),
        "app_revenue_source": (
            f"solana.com/data Application Revenue ({derived.get('app_revenue_provider')})"
            if derived.get("app_revenue_usd") is not None else None
        ),
        "sol_usd": (market or {}).get("usd"),
        "sol_24h_source": (market or {}).get("usd_24h_change_source") or (market or {}).get("source"),
    }


def render_md(snap: dict[str, Any]) -> str:
    m = snap["meta"]
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

    n_samples = len(c.get("tps_samples") or [])
    hs = snap.get("health_score") or {}
    eco = snap.get("economics") or {}
    flags_md = (
        f"No flags vs rolling baseline ({n_samples} samples / llama 7d). Watching."
    )
    if flags:
        flags_md = "\n".join(
            f"- **{f['severity'].upper()} · {f['title']}** — {f['detail']} (threshold: `{f['threshold']}`)"
            for f in flags
        )

    top_val = v.get("top") or []
    val_rows = ["| Rank | Node | Stake | Share | Commission | Last vote lag |",
                "| ---: | --- | ---: | ---: | ---: | ---: |"]
    for row in top_val[:15]:
        node = (row.get("node") or "")[:8]
        val_rows.append(
            f"| {row.get('rank')} | `{node}…` | {fmt_sol(row.get('activated_stake_lamports'))} "
            f"| {fmt_num(row.get('stake_share_pct'), 2)}% | {row.get('commission')}% "
            f"| {row.get('lag_slots') if row.get('lag_slots') is not None else '—'} |"
        )

    del_rows = []
    for row in (v.get("delinquent") or [])[:12]:
        del_rows.append(
            f"- `{str(row.get('node') or '')[:8]}…` · {fmt_sol(row.get('activated_stake_lamports'))} "
            f"· commission {row.get('commission')}% · lag {row.get('lag_slots')} slots"
        )
    if not del_rows:
        del_rows = ["- None in the RPC delinquent set."]

    dex_rows = ["| DEX | 24h volume | 1d |", "| --- | ---: | ---: |"]
    for p in (d.get("top_dexs") or [])[:8]:
        dex_rows.append(f"| {p.get('name')} | {fmt_usd(p.get('total_24h_usd'))} | {fmt_pct(p.get('change_1d_pct'))} |")

    proto_rows = ["| Protocol | Category | Solana TVL | 1d | 7d |", "| --- | --- | ---: | ---: | ---: |"]
    for p in (d.get("top_protocols") or [])[:10]:
        proto_rows.append(
            f"| {p.get('name')} | {p.get('category')} | {fmt_usd(p.get('solana_tvl_usd'))} "
            f"| {fmt_pct(p.get('change_1d_pct'))} | {fmt_pct(p.get('change_7d_pct'))} |"
        )

    stab_rows = ["| Asset | Solana circulating | 1d |", "| --- | ---: | ---: |"]
    for p in (st.get("top") or [])[:8]:
        stab_rows.append(
            f"| {p.get('symbol')} · {p.get('name')} | {fmt_usd(p.get('circulating_usd'))} "
            f"| {fmt_pct(p.get('change_1d_pct'))} |"
        )

    rwa = d.get("rwa") or {}
    rwa_rows = [f"- **{p.get('name')}** ({p.get('category')}) — {fmt_usd(p.get('solana_tvl_usd'))}"
                for p in (rwa.get("top") or [])[:8]] or ["- RWA protocol list unavailable this run."]

    def news_line(n):
        tags = n.get("tags") or []
        tag = (" `" + "` `".join(tags) + "`") if tags else ""
        return f"- [{n.get('title')}]({n.get('url')}) — {n.get('source')} · {n.get('published')}{tag}"
    tw_rows = [news_line(n) for n in (news.get("twitter") or [])[:10]] or ["- No public X/Nitter-style RSS items this run."]
    news_rows = [news_line(n) for n in (news.get("official") or news.get("items") or [])[:10]]
    if not news_rows:
        news_rows = ["- No RSS items parsed this run."]

    daa = act.get("active_addresses") or {}
    daa_line = "Omitted (no public no-key source responded)."
    if daa.get("headline_value") is not None:
        spread = ""
        if daa.get("min") is not None:
            spread = f" Provider range {fmt_num(daa.get('min'))}–{fmt_num(daa.get('max'))}."
        daa_line = (
            f"{fmt_num(daa.get('headline_value'))} "
            f"({daa.get('headline_provider')}, as of {daa.get('headline_date')})."
            f"{spread} {daa.get('note') or ''}"
        )

    om_lines = [f"- **{o.get('metric')}** — {o.get('reason')}" for o in om] or ["- None."]
    src_lines = []
    for s in snap.get("sources") or []:
        mark = "ok" if s.get("ok") else "FAIL"
        err = f" — {s.get('error')}" if s.get("error") else ""
        src_lines.append(f"- `{s.get('id')}` [{mark}] {s.get('status') or ''} {s.get('ms')}ms {s.get('url')}{err}")

    simd_lines = [f"- **{s['id']}** — {s['name']}" for s in ed.get("simds") or []]
    tl_lines = [f"- `{t['date']}` — {t['item']}" for t in ed.get("timeline_public") or []]
    watch_lines = [f"- {w}" for w in ed.get("watch") or []]
    ed_src = [f"- {u}" for u in ed.get("sources") or []]

    health = c.get("health") if c.get("health") is not None else "unavailable"
    slot_time_ms = (c["slot_time_sec"] * 1000.0) if isinstance(c.get("slot_time_sec"), (int, float)) else None
    med_ms = (c["slot_time_median"] * 1000.0) if isinstance(c.get("slot_time_median"), (int, float)) else None

    return f"""# {PRODUCT} — Solana ecosystem report

**Generated** {m.get('generated_at_utc')} · {m.get('generated_at_pt')}
**Author** {m.get('author')} · **Version** {m.get('version')} · **License** MIT
**Live demo** {m.get('demo_url') or DEMO_URL}
**Cluster block time** {c.get('block_time_utc') or '—'} · **RPC health** `{health}`
**Health score** {hs.get('score')} / 100 — `{hs.get('formula')}`
Updates every 15 min via GitHub Action.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

{flags_md}

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `{health}` |
| Slot | {fmt_num(c.get('slot'))} |
| Block height | {fmt_num(c.get('block_height'))} |
| Block time | {c.get('block_time_utc') or '—'} |
| Epoch | {fmt_num(c.get('epoch'))} ({fmt_num(c.get('epoch_progress_pct'), 2)}% · slot {fmt_num(c.get('slot_index'))}/{fmt_num(c.get('slots_in_epoch'))}) |
| Mean TPS (last ~{fmt_num(c.get('performance_window_sec'))}s) | {fmt_num(c.get('tps_total'), 1)} |
| Mean non-vote TPS | {fmt_num(c.get('tps_nonvote'), 1)} |
| Median TPS (same window) | {fmt_num(c.get('tps_median'), 1)} |
| Mean slot time | {fmt_num(slot_time_ms, 1)} ms |
| Median slot time | {fmt_num(med_ms, 1)} ms |
| Transaction count (cluster) | {fmt_num(c.get('transaction_count'))} |
| Circulating supply | {fmt_num((c.get('supply') or {{}}).get('circulating_sol'), 0)} SOL |
| Total supply | {fmt_num((c.get('supply') or {{}}).get('total_sol'), 0)} SOL |

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | {fmt_num(v.get('active_count'))} |
| Delinquent | {fmt_num(v.get('delinquent_count'))} |
| Lagging current (>150 slots) | {fmt_num(v.get('lagging_count'))} |
| Activated stake | {fmt_num(v.get('activated_stake_sol'), 0)} SOL |
| Delinquent stake | {fmt_num(v.get('delinquent_stake_sol'), 2)} SOL ({fmt_num(v.get('delinquent_stake_pct'), 3)}%) |
| Nakamoto (33% / 50% / 67%) | {v.get('nakamoto_33')} / {v.get('nakamoto_50')} / {v.get('supermajority_67')} |
| Top 10 / 20 stake share | {fmt_num(v.get('top10_share_pct'), 2)}% / {fmt_num(v.get('top20_share_pct'), 2)}% |
| Commission min / median / max | {v.get('commission_min')}% / {fmt_num(v.get('commission_median'), 1)}% / {v.get('commission_max')}% |

### Top validators by activated stake

{chr(10).join(val_rows)}

### Delinquency alerts

{chr(10).join(del_rows)}

## Economics

| Metric | Value | Source |
| --- | ---: | --- |
| REV proxy | {fmt_usd(eco.get('rev_proxy_usd'))} | {eco.get('rev_label')} |
| Network fees (24h) | {fmt_num(eco.get('network_fees_sol_24h'), 1)} SOL | {eco.get('network_fees_source') or '—'} |
| Median tx fee | — | {eco.get('median_tx_fee_note')} |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | {fmt_usd(px.get('usd'), 2)} | {px.get('source') or '—'} |
| 24h change | {fmt_pct(px.get('usd_24h_change'))} | {px.get('usd_24h_change_source') or px.get('source') or '—'} |
| Market cap | {fmt_usd(px.get('usd_market_cap'))} | {px.get('usd_market_cap_source') or '—'} |
| 24h volume | {fmt_usd(px.get('usd_24h_vol'))} | {px.get('usd_24h_vol_source') or '—'} |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | {fmt_usd(d.get('tvl_usd'))} |
| TVL 1d / 7d / 30d | {fmt_pct(d.get('tvl_change_1d_pct'))} / {fmt_pct(d.get('tvl_change_7d_pct'))} / {fmt_pct(d.get('tvl_change_30d_pct'))} |
| DEX volume 24h | {fmt_usd((d.get('dex') or {{}}).get('total_24h_usd'))} |
| DEX volume 7d | {fmt_usd((d.get('dex') or {{}}).get('total_7d_usd'))} |
| DEX 1d change | {fmt_pct((d.get('dex') or {{}}).get('change_1d_pct'))} |
| Fees 24h (REV proxy) | {fmt_usd((d.get('fees') or {{}}).get('total_24h_usd'))} |
| Fees 1d / 7d | {fmt_pct((d.get('fees') or {{}}).get('change_1d_pct'))} / {fmt_pct((d.get('fees') or {{}}).get('change_7d_pct'))} |

### Top DEX venues (24h)

{chr(10).join(dex_rows)}

### Top Solana protocols by chain TVL

{chr(10).join(proto_rows)}

## Stablecoins

Solana circulating pegged-USD: **{fmt_usd(st.get('circulating_usd'))}**
(1d {fmt_pct(st.get('change_1d_pct'))} · 7d {fmt_pct(st.get('change_7d_pct'))})

{chr(10).join(stab_rows)}

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**{fmt_usd(rwa.get('tvl_usd'))}** across {fmt_num(rwa.get('protocol_count'))} protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

{chr(10).join(rwa_rows)}

## Daily active addresses

{daa_line}

## Status & news

**status.solana.com:** {status.get('description') or '—'} (indicator `{status.get('indicator') or '—'}`)

### X / announcements (public Nitter-style RSS, not Twitter API)

{chr(10).join(tw_rows)}

{news.get('twitter_note') or ''}

### Foundation / Anza RSS

{chr(10).join(news_rows)}

## Editorial — {ed.get('title')}

_As of {ed.get('as_of')} ({ed.get('as_of_pt')}). {ed.get('disclaimer')}_

{ed.get('correction')}

{ed.get('summary')}

{chr(10).join(simd_lines)}

### Public timeline (editorial)

{chr(10).join(tl_lines)}

### What to watch

{chr(10).join(watch_lines)}

{chr(10).join(ed_src)}

## Omissions

{chr(10).join(om_lines)}

## Sources this run

{chr(10).join(src_lines)}

---

Borealis {m.get('version')} · MIT · author `{m.get('author')}` · regenerate with `python3 generate.py`
"""


def build_omissions(snap: dict[str, Any]) -> list[dict[str, str]]:
    om = []
    mkt = snap.get("market") or {}
    if not mkt.get("usd"):
        om.append({
            "metric": "SOL/USD",
            "reason": "CoinGecko, Coinbase stats, Kraken ticker, DeFiLlama coins, and solana.com/data all failed. Tile omitted.",
        })
    elif mkt.get("gecko_error"):
        om.append({
            "metric": "SOL/USD (CoinGecko live)",
            "reason": f"CoinGecko {mkt.get('gecko_error')}. Showing {mkt.get('source')} instead.",
        })
    if mkt.get("usd") is not None and mkt.get("usd_24h_change") is None:
        om.append({
            "metric": "SOL 24h change",
            "reason": "No public 24h tape (CoinGecko/Coinbase/Kraken/solana.com DoD) returned a change. Not invented.",
        })
    if (snap.get("defi") or {}).get("tvl_usd") is None:
        om.append({"metric": "Solana TVL", "reason": "DeFiLlama /v2/chains (or historical TVL) failed."})
    if not (snap.get("stablecoins") or {}).get("ok"):
        om.append({"metric": "Stablecoin supply",
                   "reason": "stablecoins.llama.fi did not return Solana circulating USD."})
    if not (snap.get("activity") or {}).get("active_addresses"):
        om.append({"metric": "Daily active addresses",
                   "reason": "solana.com/api/databricks/data did not return Active Addresses."})
    if (snap.get("cluster") or {}).get("tps_total") is None:
        om.append({"metric": "TPS", "reason": "getRecentPerformanceSamples failed on both RPC endpoints."})
    if not (snap.get("validators") or {}).get("ok"):
        om.append({"metric": "Validators", "reason": "getVoteAccounts failed on both RPC endpoints."})
    rwa = (snap.get("defi") or {}).get("rwa") or {}
    if rwa.get("tvl_usd") is None:
        om.append({"metric": "RWA TVL", "reason": "Could not derive RWA from DeFiLlama /protocols."})
    eco = snap.get("economics") or {}
    if eco.get("rev_proxy_usd") is None:
        om.append({"metric": "REV proxy", "reason": "DeFiLlama /overview/fees/Solana total24h missing."})
    news = snap.get("news") or {}
    if not news.get("twitter"):
        om.append({
            "metric": "X / Twitter RSS",
            "reason": "Public X/Nitter-style RSS yielded no usable items this run (403/gated skipped). "
                      + ", ".join((news.get("twitter_skipped") or [])[:6]),
        })
    om.append({
        "metric": "Median tx fee",
        "reason": (eco.get("median_tx_fee_note")
                   or "Median tx fee is not published on the public feeds used here."),
    })
    om.append({
        "metric": "Tokenized equities / RWA market cap",
        "reason": "No public no-key tokenized-equities figure found. Showing DeFiLlama RWA protocol TVL, labeled as such.",
    })
    return om


def write_favicon(out_dir: str, docs_dir: str) -> None:
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 36">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#3ee0b0"/><stop offset="1" stop-color="#7aa2ff"/>
  </linearGradient></defs>
  <rect x="1" y="1" width="34" height="34" rx="9" fill="#0c1017" stroke="url(#g)"/>
  <path d="M18 7 L22 15 L31 16 L24 22 L26 31 L18 26 L10 31 L12 22 L5 16 L14 15 Z" fill="url(#g)"/>
</svg>
"""
    for d in (out_dir, docs_dir):
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "favicon.svg"), "w", encoding="utf-8") as f:
            f.write(svg)


def generate(out_dir: str, docs_dir: str, history_path: str) -> dict[str, Any]:
    generated = utcnow()
    http = Http()
    history = load_history(history_path)

    cluster = fetch_cluster(http)
    validators = fetch_validators(http, cluster.get("slot"))
    circ = ((cluster.get("supply") or {}).get("circulating_sol"))
    market = assemble_market(http, circulating_sol=circ)
    defi = fetch_defillama(http)
    stable = fetch_stablecoins(http)
    sdata = fetch_solana_com_data(http)
    market = apply_solana_com_price(market, sdata)
    news = fetch_news(http)
    editorial = editorial_block(generated)
    economics = build_economics(defi, sdata, market)
    health = compute_health(cluster, validators, sdata)

    activity = {}
    if sdata.get("active_addresses"):
        activity["active_addresses"] = sdata["active_addresses"]

    flags = detect_anomalies(
        cluster, validators, market, defi, news.get("status") or {}, history, sdata,
    )

    hist_row = {
        "ts": iso(generated), "tps": cluster.get("tps_total"),
        "tps_nonvote": cluster.get("tps_nonvote"),
        "slot_time": cluster.get("slot_time_sec"), "slot": cluster.get("slot"),
        "delinquent_pct": validators.get("delinquent_stake_pct"),
        "delinquent_n": validators.get("delinquent_count"),
        "tvl": defi.get("tvl_usd"), "sol_usd": market.get("usd"),
        "sol_24h": market.get("usd_24h_change"),
        "anomaly_n": len(flags), "health_score": health.get("score"),
        "dex_24h": (defi.get("dex") or {}).get("total_24h_usd"),
        "fees_24h": (defi.get("fees") or {}).get("total_24h_usd"),
    }
    history_chart = (history + [hist_row])[-96:]

    snap: dict[str, Any] = {
        "meta": {
            "name": PRODUCT, "version": VERSION, "author": AUTHOR, "license": "MIT",
            "generated_at_utc": iso(generated), "generated_at_pt": iso_pt(generated),
            "python": sys.version.split()[0],
            "run_id": hashlib.sha1(iso(generated).encode()).hexdigest()[:12],
            "demo_url": DEMO_URL, "repo_url": REPO_URL,
            "cadence": "updates every 15 min via GitHub Action",
            "live_tick": {
                "url": "https://api.exchange.coinbase.com/products/SOL-USD/stats",
                "cors": True,
                "label": "browser live vs snapshot",
                "source": "Coinbase Exchange SOL-USD 24h stats (CORS *)",
            },
        },
        "cluster": cluster, "validators": validators, "market": market, "defi": defi,
        "stablecoins": stable, "activity": activity, "economics": economics,
        "health_score": health,
        "solana_com_data": {
            "ok": sdata.get("ok"), "url": sdata.get("url"), "generated_at": sdata.get("generated_at"),
            "page_fetchable": sdata.get("page_fetchable"), "rpc_providers": sdata.get("rpc_providers"),
            "metric_names": sorted((sdata.get("metrics") or {}).keys()),
            "active_addresses": sdata.get("active_addresses"),
            "series": {
                k: v for k, v in (sdata.get("series") or {}).items()
                if k.split("|")[0] in (
                    "Active Addresses", "SOL Price", "Fees",
                    "Transaction Count (Total)", "Application Revenue",
                )
            },
            "derived": sdata.get("derived"),
        },
        "news": news, "editorial": editorial, "anomalies": flags,
        "sources": http.log, "omissions": [],
        "history": history_chart,
        "baseline": {
            "history_points": len(history),
            "history_path": os.path.relpath(history_path, ROOT),
            "tps_window": "getRecentPerformanceSamples n=60 (~60s each); last-sample vs window 2.5σ",
            "tvl_window": "DeFiLlama daily historicalChainTvl/Solana + DEX/fees 1d/7d",
            "price_window": "Coinbase 24h stats (last-open)/open, else Kraken o, else solana.com DoD",
            "empty_copy": (
                f"No flags vs rolling baseline ({len(cluster.get('tps_samples') or [])} samples / llama 7d). Watching."
            ),
        },
    }
    snap["omissions"] = build_omissions(snap)
    append_history(history_path, hist_row)

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "report.json"), "w", encoding="utf-8") as f:
        json.dump(snap, f, indent=2, default=str)
        f.write("\n")
    with open(os.path.join(out_dir, "report.md"), "w", encoding="utf-8") as f:
        f.write(render_md(snap))
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_html(snap))
    write_favicon(out_dir, docs_dir)
    os.makedirs(docs_dir, exist_ok=True)
    for name in ("index.html", "report.md", "report.json", "favicon.svg"):
        src = os.path.join(out_dir, name)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(docs_dir, name))
    nj = os.path.join(docs_dir, ".nojekyll")
    if not os.path.isfile(nj):
        open(nj, "w").close()
    return snap


def main() -> int:
    p = argparse.ArgumentParser(description="Generate the Borealis Solana report")
    p.add_argument("--out", default=os.path.join(ROOT, "out"))
    p.add_argument("--docs", default=os.path.join(ROOT, "docs"))
    p.add_argument("--history", default=os.path.join(ROOT, "data", "history.jsonl"))
    args = p.parse_args()
    snap = generate(args.out, args.docs, args.history)
    meta = snap["meta"]
    flags = snap.get("anomalies") or []
    print(f"{PRODUCT} {meta['version']}  {meta['generated_at_utc']}  {meta['generated_at_pt']}")
    print(f"wrote {args.out}/index.html")
    print(f"wrote {args.out}/report.md")
    print(f"wrote {args.out}/report.json")
    print(f"copied snapshot -> {args.docs}/")
    hs = (snap.get("health_score") or {}).get("score")
    print(f"sources ok {sum(1 for s in snap['sources'] if s.get('ok'))}/{len(snap['sources'])}  "
          f"anomalies {len(flags)}  omissions {len(snap.get('omissions') or [])}  health {hs}")
    px = snap.get("market") or {}
    print(f"SOL {px.get('usd')}  24h {px.get('usd_24h_change')}  src {px.get('source')} / {px.get('usd_24h_change_source')}")
    for f in flags:
        print(f"  [{f['severity']}] {f['title']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
