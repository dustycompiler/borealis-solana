#!/usr/bin/env python3
"""Borealis — live Solana cluster & ecosystem report.

One command, no API keys, stdlib only:

    python3 generate.py

Writes out/index.html, out/report.md, out/report.json and copies a
static snapshot to docs/ for GitHub Pages.

Author: hardest-worker
License: MIT
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import os
import shutil
import statistics
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Any
from zoneinfo import ZoneInfo

from htmlout import render_html

VERSION = "1.0.0"
PRODUCT = "Borealis"
LAMPORTS = 1_000_000_000
PT = ZoneInfo("America/Vancouver")
UTC = timezone.utc

PRIMARY_RPC = "https://api.mainnet-beta.solana.com"
FALLBACK_RPC = "https://solana-rpc.publicnode.com"

USER_AGENT = (
    "BorealisReport/1.0 (Solana ecosystem dashboard; stdlib urllib; no API key)"
)

ROOT = os.path.dirname(os.path.abspath(__file__))


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
        url, source_id="coingecko.simple_price", timeout=20, retries=1,
        honor_retry_after=True, max_retry_after=8.0, backoff=2.0,
    )
    out: dict[str, Any] = {
        "ok": bool(rec.get("ok")), "source": "coingecko", "url": url,
        "usd": None, "usd_24h_change": None, "usd_market_cap": None,
        "usd_24h_vol": None, "last_updated_unix": None, "error": rec.get("error"),
    }
    if isinstance(data, dict) and isinstance(data.get("solana"), dict):
        s = data["solana"]
        out["usd"] = s.get("usd")
        out["usd_24h_change"] = s.get("usd_24h_change")
        out["usd_market_cap"] = s.get("usd_market_cap")
        out["usd_24h_vol"] = s.get("usd_24h_vol")
        out["last_updated_unix"] = s.get("last_updated_at")
        out["last_updated_utc"] = iso(parse_unix(s.get("last_updated_at")))
        out["ok"] = out["usd"] is not None
    return out


def fetch_price_fallbacks(http: Http, market: dict[str, Any]) -> dict[str, Any]:
    """Only used if CoinGecko 429s. Never presented as CoinGecko."""
    if market.get("usd") is not None:
        return market
    data, rec = http.json(
        "https://coins.llama.fi/prices/current/coingecko:solana",
        source_id="llama.coins.coingecko_solana", timeout=20, retries=1,
    )
    coins = (data or {}).get("coins") if isinstance(data, dict) else None
    row = None
    if isinstance(coins, dict):
        row = coins.get("coingecko:solana") or next(iter(coins.values()), None)
    if isinstance(row, dict) and isinstance(row.get("price"), (int, float)):
        ts = row.get("timestamp")
        market.update({
            "ok": True,
            "source": "defillama-coins (coingecko:solana id; CoinGecko public API 429)",
            "usd": row.get("price"),
            "usd_24h_change": None,
            "usd_market_cap": None,
            "usd_24h_vol": None,
            "last_updated_unix": ts,
            "last_updated_utc": iso(parse_unix(ts)) if ts else None,
            "fallback": True,
            "error": market.get("error"),
        })
        return market
    return market


def apply_solana_com_price(market: dict[str, Any], sdata: dict[str, Any]) -> dict[str, Any]:
    if market.get("usd") is not None:
        return market
    series = ((sdata.get("metrics") or {}).get("SOL Price")) or []
    pick = next((x for x in series if x.get("provider") == "DeFiLlama"), None)
    if pick is None and series:
        pick = series[0]
    if pick and isinstance(pick.get("value"), (int, float)):
        market.update({
            "ok": True,
            "source": f"solana.com/data SOL Price ({pick.get('provider')}; CoinGecko 429)",
            "usd": pick.get("value"),
            "usd_24h_change": None,
            "price_as_of": pick.get("date"),
            "fallback": True,
            "error": market.get("error"),
        })
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
    wanted_series = {"Active Addresses", "SOL Price"}
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
        if name in wanted_series and prov in ("Allium", "DeFiLlama", "Dune"):
            series.setdefault(f"{name}|{prov}", []).append({"date": row.get("date"), "value": row.get("value")})

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
    out["series"] = {k: v[-30:] for k, v in series.items()}

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


def parse_feed(body: bytes, source: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return items
    for item in root.iter():
        if _local(item.tag) != "item":
            continue
        title = link = pub = summary = None
        for ch in list(item):
            loc = _local(ch.tag)
            if loc == "title":
                title = (ch.text or "").strip()
            elif loc == "link":
                link = (ch.text or "").strip() or ch.get("href")
            elif loc in ("pubDate", "date", "updated"):
                pub = (ch.text or "").strip()
            elif loc in ("description", "summary"):
                summary = (ch.text or "").strip()
        if title:
            items.append({"source": source, "title": title, "url": link, "published": pub, "summary": (summary or "")[:280]})
    if not items:
        for item in root.iter():
            if _local(item.tag) != "entry":
                continue
            title = link = pub = summary = None
            for ch in list(item):
                loc = _local(ch.tag)
                if loc == "title":
                    title = (ch.text or "").strip()
                elif loc == "link":
                    link = ch.get("href") or (ch.text or "").strip()
                elif loc in ("updated", "published"):
                    pub = pub or (ch.text or "").strip()
                elif loc in ("summary", "content"):
                    summary = (ch.text or "").strip()
            if title:
                items.append({"source": source, "title": title, "url": link, "published": pub, "summary": (summary or "")[:280]})
    return items


def fetch_news(http: Http) -> dict[str, Any]:
    feeds = [
        ("status.atom", "https://status.solana.com/history.atom", "status"),
        ("news.rss", "https://solana.com/news/rss.xml", "solana.com/news"),
        ("anza.medium", "https://medium.com/feed/anza-xyz", "anza"),
    ]
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
    news: list[dict[str, Any]] = []
    for sid, url, label in feeds:
        body, rec = http.request(url, source_id=f"rss.{sid}", timeout=25)
        if body:
            news.extend(parse_feed(body, label))
    seen = set()
    uniq = []
    for n in news:
        t = (n.get("title") or "").strip().lower()
        if not t or t in seen:
            continue
        seen.add(t)
        uniq.append(n)
    return {"status": status, "items": uniq[:18]}


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


def detect_anomalies(cluster, validators, market, defi, status, history) -> list[dict[str, Any]]:
    flags: list[dict[str, Any]] = []
    tps_samples = [r["tps_total"] for r in (cluster.get("tps_samples") or []) if isinstance(r.get("tps_total"), (int, float))]
    tps = cluster.get("tps_total")
    tps_med = cluster.get("tps_median")
    tps_sd = cluster.get("tps_stdev") or 0.0
    if tps is not None and tps_med:
        if tps_sd and tps > tps_med + 2.5 * tps_sd and tps > tps_med * 1.35:
            flags.append(_flag(
                key="tps_spike", severity="warn", title="TPS spike vs last-hour baseline",
                detail=(f"Mean TPS {tps:,.0f} is {((tps/tps_med)-1)*100:.0f}% above the "
                        f"sample median {tps_med:,.0f} (sigma={tps_sd:,.0f}) from {len(tps_samples)} sixty-second windows."),
                metric="tps_total", value=round(tps, 2),
                baseline={"median": tps_med, "stdev": tps_sd, "n": len(tps_samples)},
                threshold="mean > median + 2.5 sigma and > 1.35x median",
            ))
        if tps < tps_med * 0.55 or (tps_sd and tps < tps_med - 2.5 * tps_sd and tps < tps_med * 0.75):
            flags.append(_flag(
                key="tps_drop", severity="alert", title="TPS drop vs last-hour baseline",
                detail=(f"Mean TPS {tps:,.0f} vs sample median {tps_med:,.0f} "
                        f"(sigma={tps_sd:,.0f}). Possible load drop or sampling gap."),
                metric="tps_total", value=round(tps, 2),
                baseline={"median": tps_med, "stdev": tps_sd, "n": len(tps_samples)},
                threshold="mean < 0.55x median, or < median - 2.5 sigma and < 0.75x median",
            ))

    st = cluster.get("slot_time_sec")
    st_med = cluster.get("slot_time_median")
    st_max = cluster.get("slot_time_max")
    if st is not None and st_med:
        slow = st > 0.60 or (st_max is not None and st_max > 0.80) or st > st_med * 1.5
        if slow:
            flags.append(_flag(
                key="slow_slots", severity="alert" if (st or 0) > 0.7 else "warn", title="Slow slots",
                detail=(f"Mean slot time {st:.3f}s (median {st_med:.3f}s, max {st_max:.3f}s). "
                        "Target cadence on mainnet is ~0.4s."),
                metric="slot_time_sec", value=round(st, 4),
                baseline={"median": st_med, "max": st_max},
                threshold="mean > 0.60s, max > 0.80s, or mean > 1.5x median",
            ))

    d_pct = validators.get("delinquent_stake_pct")
    d_n = validators.get("delinquent_count")
    if (isinstance(d_pct, (int, float)) and d_pct >= 1.0) or (isinstance(d_n, int) and d_n >= 25):
        flags.append(_flag(
            key="high_delinquency", severity="alert" if (d_pct or 0) >= 2.5 else "warn",
            title="High validator delinquency",
            detail=(f"{d_n} delinquent vote accounts, {d_pct:.3f}% of activated+delinquent stake."
                    if isinstance(d_pct, (int, float)) else f"{d_n} delinquent vote accounts."),
            metric="delinquent_stake_pct", value=d_pct,
            baseline={"delinquent_count": d_n},
            threshold="delinquent stake >= 1% or delinquent count >= 25",
        ))

    tvl_1d = defi.get("tvl_change_1d_pct")
    tvl_7d = defi.get("tvl_change_7d_pct")
    if isinstance(tvl_1d, (int, float)) and abs(tvl_1d) >= 8:
        flags.append(_flag(
            key="tvl_move_1d", severity="warn" if abs(tvl_1d) < 15 else "alert",
            title="Large Solana DeFi TVL 1-day move",
            detail=f"DeFiLlama historical chain TVL 1-day change is {tvl_1d:+.2f}%.",
            metric="tvl_change_1d_pct", value=round(tvl_1d, 3),
            baseline={"tvl_usd": defi.get("tvl_usd"), "change_7d_pct": tvl_7d},
            threshold="|1d %| >= 8",
        ))
    elif isinstance(tvl_7d, (int, float)) and abs(tvl_7d) >= 20:
        flags.append(_flag(
            key="tvl_move_7d", severity="warn", title="Large Solana DeFi TVL 7-day move",
            detail=f"DeFiLlama historical chain TVL 7-day change is {tvl_7d:+.2f}%.",
            metric="tvl_change_7d_pct", value=round(tvl_7d, 3),
            baseline={"tvl_usd": defi.get("tvl_usd")},
            threshold="|7d %| >= 20",
        ))

    px_ch = market.get("usd_24h_change")
    if isinstance(px_ch, (int, float)) and abs(px_ch) >= 8:
        flags.append(_flag(
            key="sol_price_move", severity="warn" if abs(px_ch) < 15 else "alert",
            title="Large SOL 24h price move",
            detail=f"CoinGecko SOL/USD 24h change is {px_ch:+.2f}%.",
            metric="usd_24h_change", value=round(px_ch, 3),
            baseline={"usd": market.get("usd")},
            threshold="|24h %| >= 8",
        ))

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

    flags_md = "No anomaly flags on this run (thresholds in README)."
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

    news_rows = []
    for n in (news.get("items") or [])[:10]:
        news_rows.append(f"- [{n.get('title')}]({n.get('url')}) — {n.get('source')} · {n.get('published')}")
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
**Cluster block time** {c.get('block_time_utc') or '—'} · **RPC health** `{health}`

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

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | {fmt_usd(px.get('usd'), 2)} | {px.get('source') or '—'} |
| 24h change | {fmt_pct(px.get('usd_24h_change'))} | CoinGecko |
| Market cap | {fmt_usd(px.get('usd_market_cap'))} | CoinGecko |
| 24h volume | {fmt_usd(px.get('usd_24h_vol'))} | CoinGecko |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | {fmt_usd(d.get('tvl_usd'))} |
| TVL 1d / 7d / 30d | {fmt_pct(d.get('tvl_change_1d_pct'))} / {fmt_pct(d.get('tvl_change_7d_pct'))} / {fmt_pct(d.get('tvl_change_30d_pct'))} |
| DEX volume 24h | {fmt_usd((d.get('dex') or {{}}).get('total_24h_usd'))} |
| DEX volume 7d | {fmt_usd((d.get('dex') or {{}}).get('total_7d_usd'))} |
| DEX 1d change | {fmt_pct((d.get('dex') or {{}}).get('change_1d_pct'))} |
| Fees 24h | {fmt_usd((d.get('fees') or {{}}).get('total_24h_usd'))} |

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
        om.append({"metric": "SOL/USD",
                   "reason": "CoinGecko 429 and public fallbacks (DeFiLlama coins, solana.com/data) also failed. Tile omitted."})
    elif mkt.get("fallback"):
        om.append({"metric": "SOL/USD (CoinGecko live)",
                   "reason": f"CoinGecko 429. Showing fallback from {mkt.get('source')}."})
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
    return om


def generate(out_dir: str, docs_dir: str, history_path: str) -> dict[str, Any]:
    generated = utcnow()
    http = Http()
    history = load_history(history_path)

    cluster = fetch_cluster(http)
    validators = fetch_validators(http, cluster.get("slot"))
    market = fetch_coingecko(http)
    market = fetch_price_fallbacks(http, market)
    defi = fetch_defillama(http)
    stable = fetch_stablecoins(http)
    sdata = fetch_solana_com_data(http)
    market = apply_solana_com_price(market, sdata)
    news = fetch_news(http)
    editorial = editorial_block(generated)

    activity = {}
    if sdata.get("active_addresses"):
        activity["active_addresses"] = sdata["active_addresses"]

    flags = detect_anomalies(cluster, validators, market, defi, news.get("status") or {}, history)

    snap: dict[str, Any] = {
        "meta": {
            "name": PRODUCT, "version": VERSION, "author": "hardest-worker", "license": "MIT",
            "generated_at_utc": iso(generated), "generated_at_pt": iso_pt(generated),
            "python": sys.version.split()[0],
            "run_id": hashlib.sha1(iso(generated).encode()).hexdigest()[:12],
        },
        "cluster": cluster, "validators": validators, "market": market, "defi": defi,
        "stablecoins": stable, "activity": activity,
        "solana_com_data": {
            "ok": sdata.get("ok"), "url": sdata.get("url"), "generated_at": sdata.get("generated_at"),
            "page_fetchable": sdata.get("page_fetchable"), "rpc_providers": sdata.get("rpc_providers"),
            "metric_names": sorted((sdata.get("metrics") or {}).keys()),
            "active_addresses": sdata.get("active_addresses"), "series": sdata.get("series"),
        },
        "news": news, "editorial": editorial, "anomalies": flags, "sources": http.log, "omissions": [],
        "baseline": {
            "history_points": len(history),
            "history_path": os.path.relpath(history_path, ROOT),
            "tps_window": "getRecentPerformanceSamples n=60 (~60s each)",
            "tvl_window": "DeFiLlama daily historicalChainTvl/Solana",
            "price_window": "CoinGecko include_24hr_change + prior history.jsonl rows",
        },
    }
    snap["omissions"] = build_omissions(snap)
    append_history(history_path, {
        "ts": iso(generated), "tps": cluster.get("tps_total"), "tps_nonvote": cluster.get("tps_nonvote"),
        "slot_time": cluster.get("slot_time_sec"), "slot": cluster.get("slot"),
        "delinquent_pct": validators.get("delinquent_stake_pct"),
        "delinquent_n": validators.get("delinquent_count"),
        "tvl": defi.get("tvl_usd"), "sol_usd": market.get("usd"), "anomaly_n": len(flags),
    })

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "report.json"), "w", encoding="utf-8") as f:
        json.dump(snap, f, indent=2, default=str)
        f.write("\n")
    with open(os.path.join(out_dir, "report.md"), "w", encoding="utf-8") as f:
        f.write(render_md(snap))
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_html(snap))
    os.makedirs(docs_dir, exist_ok=True)
    for name in ("index.html", "report.md", "report.json"):
        shutil.copy2(os.path.join(out_dir, name), os.path.join(docs_dir, name))
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
    print(f"sources ok {sum(1 for s in snap['sources'] if s.get('ok'))}/{len(snap['sources'])}  "
          f"anomalies {len(flags)}  omissions {len(snap.get('omissions') or [])}")
    for f in flags:
        print(f"  [{f['severity']}] {f['title']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
