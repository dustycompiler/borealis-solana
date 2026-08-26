#!/usr/bin/env python3
"""Stdlib tests for Borealis generate.py helpers. No network."""
from __future__ import annotations

import json
import os
import statistics
import sys
import unittest
from datetime import datetime, timedelta, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from generate import (  # noqa: E402
    FALLBACK_RPC,
    PRIMARY_RPC,
    Http,
    assemble_market,
    aligned_rev_date,
    build_brief,
    build_data_health,
    cap_headline_confidence,
    build_economics,
    build_insights,
    classify_ecosystem_activity,
    classify_network_health,
    classify_news_items,
    complete_jito_days,
    compute_health,
    detect_anomalies,
    editorial_block,
    equity_mcap,
    fee_stats_from_lamports,
    fetch_xstocks,
    filter_rss_by_recency,
    infer_simd0525_stage,
    jito_gross_tips_sol,
    pct_24h,
    percentile,
    rss_is_stale,
)
from htmlout import render_html  # noqa: E402


UTC = timezone.utc


class HealthScoreTests(unittest.TestCase):
    def test_perfect_score_is_100(self):
        cluster = {
            "health": "ok",
            "slot": 1,
            "tps_total": 4000,
            "slot_time_sec": 0.400,
            "tps_median": 4000,
        }
        validators = {"delinquent_stake_pct": 0.0}
        sdata = {"derived": {"tps_30d_median": 4000.0, "tps_30d_source": "test baseline"}}
        h = compute_health(cluster, validators, sdata)
        self.assertEqual(h["score"], 100)
        by_id = {p["id"]: p for p in h["parts"]}
        self.assertEqual(by_id["rpc"]["points"], 25)
        self.assertEqual(by_id["slot"]["points"], 30)
        self.assertEqual(by_id["delinquency"]["points"], 25)
        self.assertEqual(by_id["tps"]["points"], 20)
        self.assertIn("25", h["formula"])
        self.assertIn("slot_ms", h["formula"])

    def test_slot_800ms_zeroes_slot_term(self):
        cluster = {
            "health": "ok", "slot": 1, "tps_total": 4000,
            "slot_time_sec": 0.800, "tps_median": 4000,
        }
        h = compute_health(cluster, {"delinquent_stake_pct": 0.0},
                           {"derived": {"tps_30d_median": 4000}})
        by_id = {p["id"]: p for p in h["parts"]}
        self.assertEqual(by_id["slot"]["points"], 0.0)
        self.assertEqual(h["score"], 70)  # 25+0+25+20

    def test_slot_600ms_is_half_slot_term(self):
        cluster = {
            "health": "ok", "slot": 1, "tps_total": 4000,
            "slot_time_sec": 0.600, "tps_median": 4000,
        }
        h = compute_health(cluster, {"delinquent_stake_pct": 0.0},
                           {"derived": {"tps_30d_median": 4000}})
        by_id = {p["id"]: p for p in h["parts"]}
        self.assertAlmostEqual(by_id["slot"]["points"], 15.0, places=2)

    def test_delinquency_linear_to_two_percent(self):
        cluster = {
            "health": "ok", "slot": 1, "tps_total": 4000,
            "slot_time_sec": 0.4, "tps_median": 4000,
        }
        h = compute_health(cluster, {"delinquent_stake_pct": 1.0},
                           {"derived": {"tps_30d_median": 4000}})
        by_id = {p["id"]: p for p in h["parts"]}
        self.assertAlmostEqual(by_id["delinquency"]["points"], 12.5, places=2)

    def test_tps_half_baseline_is_ten_points(self):
        cluster = {
            "health": "ok", "slot": 1, "tps_total": 2000,
            "slot_time_sec": 0.4, "tps_median": 2000,
        }
        h = compute_health(cluster, {"delinquent_stake_pct": 0.0},
                           {"derived": {"tps_30d_median": 4000}})
        by_id = {p["id"]: p for p in h["parts"]}
        self.assertAlmostEqual(by_id["tps"]["points"], 10.0, places=2)

    def test_rpc_unreachable_zeroes_rpc_term(self):
        cluster = {"health": None, "slot": None, "tps_total": None, "slot_time_sec": None}
        h = compute_health(cluster, {"delinquent_stake_pct": None}, {"derived": {}})
        by_id = {p["id"]: p for p in h["parts"]}
        self.assertEqual(by_id["rpc"]["points"], 0.0)
        self.assertEqual(h["score"], 0)


class Pct24hTests(unittest.TestCase):
    def test_formula_last_minus_open_over_open(self):
        self.assertAlmostEqual(pct_24h(110, 100), 10.0)
        self.assertAlmostEqual(pct_24h(90, 100), -10.0)
        self.assertAlmostEqual(pct_24h(100, 100), 0.0)

    def test_zero_open_is_none(self):
        self.assertIsNone(pct_24h(100, 0))

    def test_missing_values_are_none(self):
        self.assertIsNone(pct_24h(None, 100))
        self.assertIsNone(pct_24h(100, None))


def _quiet_cluster(**kw):
    samples = []
    for _ in range(60):
        samples.append({"tps_total": 3000.0, "tps_nonvote": 2000.0, "slot_time_sec": 0.40})
    tps = [r["tps_total"] for r in samples]
    st = [r["slot_time_sec"] for r in samples]
    nv = [r["tps_nonvote"] for r in samples]
    base = {
        "tps_samples": samples,
        "tps_total": statistics.mean(tps),
        "tps_median": statistics.median(tps),
        "tps_stdev": statistics.pstdev(tps),
        "tps_last": samples[-1]["tps_total"],
        "tps_nonvote": statistics.mean(nv),
        "tps_nonvote_median": statistics.median(nv),
        "tps_nonvote_stdev": statistics.pstdev(nv),
        "tps_nonvote_last": nv[-1],
        "slot_time_sec": statistics.mean(st),
        "slot_time_median": statistics.median(st),
        "slot_time_stdev": statistics.pstdev(st),
        "slot_time_last": st[-1],
        "slot_time_max": max(st),
        "health": "ok",
    }
    base.update(kw)
    return base


class AnomalyTests(unittest.TestCase):
    def test_tvl_move_1d_flags_synthetic_series(self):
        flags = detect_anomalies(
            _quiet_cluster(),
            {"delinquent_stake_pct": 0.02, "delinquent_count": 2},
            {"usd": 100.0, "usd_24h_change": 1.0},
            {"tvl_change_1d_pct": 12.0, "tvl_change_7d_pct": 3.0, "dex": {}, "fees": {}},
            {"indicator": "none"},
            [],
            {},
        )
        keys = {f["key"] for f in flags}
        self.assertIn("tvl_move_1d", keys)

    def test_sol_24h_move_flags(self):
        flags = detect_anomalies(
            _quiet_cluster(),
            {"delinquent_stake_pct": 0.02, "delinquent_count": 2},
            {"usd": 100.0, "usd_24h_change": -11.0, "usd_24h_change_source": "coinbase"},
            {"tvl_change_1d_pct": 0.1, "dex": {}, "fees": {}},
            {"indicator": "none"},
            [],
            {},
        )
        self.assertTrue(any(f["key"] == "sol_price_move" for f in flags))

    def test_last_tps_sigma_on_synthetic_spike(self):
        samples = [{"tps_total": 3000.0, "tps_nonvote": 2000.0, "slot_time_sec": 0.40} for _ in range(59)]
        samples.append({"tps_total": 9000.0, "tps_nonvote": 2000.0, "slot_time_sec": 0.40})
        tps = [r["tps_total"] for r in samples]
        cluster = _quiet_cluster(
            tps_samples=samples,
            tps_total=statistics.mean(tps),
            tps_median=statistics.median(tps),
            tps_stdev=statistics.pstdev(tps),
            tps_last=9000.0,
        )
        flags = detect_anomalies(
            cluster,
            {"delinquent_stake_pct": 0.02, "delinquent_count": 2},
            {"usd": 100.0, "usd_24h_change": 0.2},
            {"dex": {}, "fees": {}},
            {"indicator": "none"},
            [],
            {},
        )
        self.assertTrue(any(f["key"] == "tps_last_sigma" for f in flags))

    def test_quiet_series_has_no_sigma_or_tvl_flags(self):
        flags = detect_anomalies(
            _quiet_cluster(),
            {"delinquent_stake_pct": 0.02, "delinquent_count": 2},
            {"usd": 100.0, "usd_24h_change": 0.4},
            {"tvl_change_1d_pct": 1.0, "tvl_change_7d_pct": 2.0, "dex": {"change_1d_pct": 1.0}, "fees": {"change_1d_pct": 1.0}},
            {"indicator": "none"},
            [],
            {},
        )
        keys = {f["key"] for f in flags}
        self.assertNotIn("tps_last_sigma", keys)
        self.assertNotIn("tvl_move_1d", keys)
        self.assertNotIn("sol_price_move", keys)


class RssRecencyTests(unittest.TestCase):
    def test_filter_drops_items_older_than_45_days(self):
        now = datetime(2026, 8, 25, 12, 0, tzinfo=UTC)
        recent = {"title": "recent", "published": "Mon, 24 Aug 2026 12:00:00 GMT"}
        old = {"title": "old", "published": "Mon, 01 Jan 2024 12:00:00 GMT"}
        missing = {"title": "missing", "published": None}
        kept = filter_rss_by_recency([recent, old, missing], now=now, max_age_days=45)
        self.assertEqual([x["title"] for x in kept], ["recent", "missing"])
        self.assertTrue(rss_is_stale(old["published"], now=now, max_age_days=45))
        self.assertFalse(rss_is_stale(recent["published"], now=now, max_age_days=45))
        self.assertFalse(rss_is_stale(None, now=now))

    def test_boundary_just_inside_window_is_kept(self):
        now = datetime(2026, 8, 25, tzinfo=UTC)
        pub = (now - timedelta(days=44)).strftime("%a, %d %b %Y %H:%M:%S GMT")
        self.assertFalse(rss_is_stale(pub, now=now, max_age_days=45))
        pub_out = (now - timedelta(days=46)).strftime("%a, %d %b %Y %H:%M:%S GMT")
        self.assertTrue(rss_is_stale(pub_out, now=now, max_age_days=45))


class FeeStatsTests(unittest.TestCase):
    def test_percentile_and_p50(self):
        xs = [1, 2, 3, 4, 5]
        self.assertEqual(percentile(xs, 0), 1)
        self.assertEqual(percentile(xs, 100), 5)
        self.assertEqual(percentile(xs, 50), 3)
        self.assertIsNone(percentile([], 50))

    def test_fee_stats_from_synthetic_lamports(self):
        fees = [5000] * 10 + [10000] * 8 + [50000] * 2
        st = fee_stats_from_lamports(fees)
        self.assertEqual(st["n"], 20)
        self.assertGreater(st["p90_lamports"], st["p50_lamports"])
        self.assertGreaterEqual(st["p99_lamports"], st["p90_lamports"])
        self.assertAlmostEqual(st["p50_sol"] * 1_000_000_000, st["p50_lamports"])


class EquityMcapTests(unittest.TestCase):
    def test_formula_quote_times_circ_times_mult(self):
        self.assertAlmostEqual(equity_mcap(10, 100, 2), 2000)
        self.assertIsNone(equity_mcap(None, 100, 1))
        self.assertIsNone(equity_mcap(10, None, 1))
        self.assertIsNone(equity_mcap(10, 100, None))  # never silent 1.0


class EconomicsHonestyTests(unittest.TestCase):
    def test_protocol_fees_are_not_included_in_rev(self):
        eco = build_economics(
            {"fees": {"total_24h_usd": 1e6, "change_1d_pct": 4}},
            {"derived": {"network_fees_sol": 9000, "network_fees_source": "solana.com/data Fees (Allium)"}},
            {"usd": 100},
            tx_fees={"ok": True, "p50_sol": 0.00001, "p90_sol": 0.00005, "p99_sol": 0.0002,
                     "n_fees": 12, "n_tx": 12, "slot_lo": 1, "slot_hi": 10, "window_seconds": 3600, "note": "sample"},
            jito={"ok": False, "error": "timeout"},
        )
        # Full REV is incomplete (no 24h Jito tape). Llama $1M is excluded.
        self.assertIsNone(eco.get("rev_24h_usd"))
        self.assertIsNone(eco.get("total_rev_usd"))
        self.assertFalse(eco.get("rev_complete"))
        self.assertIn("INCOMPLETE", eco.get("rev_kind") or "")
        self.assertAlmostEqual(eco.get("network_fees_usd_24h"), 900_000)
        self.assertEqual((eco.get("headline_primary") or {}).get("usd"), 900_000)
        self.assertNotEqual(eco.get("rev_24h_usd"), 1e6)
        self.assertNotEqual(eco.get("network_fees_usd_24h"), 1e6)
        self.assertTrue(eco.get("protocol_fees_excluded_from_rev"))
        self.assertIn("not REV", eco.get("protocol_fees_label") or "")
        self.assertEqual(eco.get("protocol_fees_usd"), 1e6)
        self.assertIsNone(eco.get("rev_proxy_usd"))
        self.assertIn("Blockworks", eco.get("rev_definition") or "")
        self.assertEqual(eco.get("median_tx_fee_window_seconds"), 3600)
        self.assertTrue(eco.get("jito", {}).get("omitted"))

    def test_jito_runrate_is_not_rev(self):
        eco = build_economics(
            {"fees": {"total_24h_usd": 14_490_000}},
            {"derived": {"network_fees_sol": 9000}},
            {"usd": 100},
            tx_fees={"ok": True, "p50_sol": 0.00001},
            jito={"ok": True, "landed_p50_sol": 1e-5},
            cluster={"tps_nonvote": 2000},
        )
        tips = 1e-5 * 2000 * 86400 * 100  # $172,800
        self.assertIsNone(eco.get("rev_24h_usd"))
        self.assertFalse(eco.get("rev_complete"))
        self.assertAlmostEqual(eco.get("network_fees_usd_24h"), 900_000)
        self.assertNotEqual(eco.get("rev_24h_usd"), 900_000 + tips)
        self.assertNotEqual(eco.get("rev_24h_usd"), 900_000)
        jr = eco.get("jito_runrate_not_rev") or {}
        self.assertTrue(jr.get("not_a_24h_aggregate"))
        self.assertFalse(jr.get("included_in_headline"))
        self.assertAlmostEqual(jr.get("runrate_24h_usd"), tips)
        self.assertLess(eco.get("network_fees_usd_24h"), 14_490_000)
        self.assertEqual(eco.get("protocol_fees_usd"), 14_490_000)
        self.assertNotIn("ESTIMATED", (eco.get("jito", {}).get("tips_24h_kind") or ""))
        self.assertIn("INVALID", (jr.get("kind") or "").upper())



    def _jito_daily(self, fee_day="2026-08-25", include_today=True):
        rows = [
            {"day": "2026-08-26 00:00:00.000 UTC", "jito_tips": 16.12, "validator_tips": 306.33,
             "count_mev_tips": 1.83e6},
            {"day": "2026-08-25 00:00:00.000 UTC", "jito_tips": 113.294, "validator_tips": 2152.587,
             "count_mev_tips": 12.15e6},
            {"day": "2026-08-24 00:00:00.000 UTC", "jito_tips": 88.961, "validator_tips": 1690.259,
             "count_mev_tips": 11.49e6},
        ]
        if not include_today:
            rows = rows[1:]
        return {
            "ok": True,
            "utc_today": "2026-08-26",
            "rows": rows,
            "accounting": "gross = jito_tips + validator_tips",
        }

    def test_gross_mev_is_jito_plus_validator_not_either_alone(self):
        row = {"jito_tips": 113.294, "validator_tips": 2152.587}
        gross = jito_gross_tips_sol(row)
        self.assertAlmostEqual(gross, 2265.881)
        self.assertAlmostEqual(113.294 / gross, 0.05, places=5)
        self.assertNotEqual(gross, 113.294)
        self.assertNotEqual(gross, 2152.587)
        self.assertIsNone(jito_gross_tips_sol({"jito_tips": 113.294}))
        self.assertIsNone(jito_gross_tips_sol({"validator_tips": 2152.587}))

    def test_skip_incomplete_today_jito_row(self):
        complete = complete_jito_days(self._jito_daily()["rows"], "2026-08-26")
        self.assertNotIn("2026-08-26", complete)
        self.assertIn("2026-08-25", complete)
        eco = build_economics(
            {"fees": {"total_24h_usd": 14_490_000}},
            {"derived": {"network_fees_sol": 9000, "network_fees_date": "2026-08-26",
                         "network_fees_source": "solana.com/data Fees"}},
            {"usd": 100},
            jito_daily=self._jito_daily(),
        )
        self.assertFalse(eco.get("rev_complete"))
        self.assertIsNone(eco.get("rev_24h_usd"))
        self.assertIn("INCOMPLETE", eco.get("rev_kind") or "")

    def test_refuse_mixed_utc_dates(self):
        # Fees on Aug 24, complete Jito available for Aug 25 only in this cut.
        eco = build_economics(
            {"fees": {"total_24h_usd": 14_490_000}},
            {"derived": {"network_fees_sol": 9000, "network_fees_date": "2026-08-24",
                         "network_fees_source": "solana.com/data Fees"}},
            {"usd": 100},
            jito_daily={
                "ok": True, "utc_today": "2026-08-26",
                "rows": [{"day": "2026-08-25 00:00:00.000 UTC",
                          "jito_tips": 113.294, "validator_tips": 2152.587}],
            },
        )
        self.assertIsNone(aligned_rev_date("2026-08-24", complete_jito_days(
            [{"day": "2026-08-25", "jito_tips": 1, "validator_tips": 19}], "2026-08-26")))
        self.assertFalse(eco.get("rev_complete"))
        self.assertIsNone(eco.get("rev_24h_usd"))
        # Must not silently add Aug 25 Jito to Aug 24 fees
        self.assertNotAlmostEqual((eco.get("rev_24h_usd") or 0), 900_000 + 2265.881 * 100)

    def test_aligned_complete_rev_sums_fees_and_gross_tips(self):
        llama = 14_490_000
        floor = 1e-5 * 2000 * 86400 * 100  # $172,800
        eco = build_economics(
            {"fees": {"total_24h_usd": llama}},
            {"derived": {"network_fees_sol": 9000, "network_fees_date": "2026-08-25",
                         "network_fees_source": "solana.com/data Fees (Allium)"}},
            {"usd": 100},
            tx_fees={"ok": True, "p50_sol": 0.00001, "sampled_runrate_24h_sol": 9100},
            jito={"ok": True, "landed_p50_sol": 1e-5, "landed_p95_sol": 4e-5},
            cluster={"tps_nonvote": 2000},
            jito_daily=self._jito_daily(),
        )
        gross = 113.294 + 2152.587
        self.assertTrue(eco.get("rev_complete"))
        self.assertEqual(eco.get("rev_utc_day"), "2026-08-25")
        self.assertAlmostEqual(eco.get("rev_24h_sol"), 9000 + gross)
        self.assertAlmostEqual(eco.get("rev_24h_usd"), 900_000 + gross * 100)
        self.assertAlmostEqual(eco.get("total_rev_usd"), 900_000 + gross * 100)
        # Llama app fees and tip-floor product are not in REV
        self.assertNotAlmostEqual(eco.get("rev_24h_usd"), llama)
        self.assertNotAlmostEqual(eco.get("rev_24h_usd"), 900_000 + llama)
        self.assertNotAlmostEqual(eco.get("rev_24h_usd"), 900_000 + floor)
        self.assertLess(eco.get("rev_24h_usd"), llama)
        jr = eco.get("jito_runrate_not_rev") or {}
        self.assertFalse(jr.get("included_in_headline"))
        self.assertTrue(eco.get("protocol_fees_excluded_from_rev"))
        self.assertEqual(eco.get("protocol_fees_usd"), llama)
        ids = {c["id"]: c for c in eco.get("rev_components") or []}
        self.assertTrue(ids["jito_mev_tips"].get("included_in_headline"))
        self.assertFalse(ids["jito_tips_floor_runrate"].get("included_in_headline"))
        from htmlout import render_html
        html = render_html({
            "meta": {"version": "1.5.1", "generated_at_utc": "2026-08-26T03:00:00Z",
                     "generated_at_pt": "2026-08-25 20:00:00 PT"},
            "cluster": {"health": "ok", "slot_time_sec": 0.365, "tps_total": 4000},
            "brief": {"network_health": "HEALTHY", "ecosystem_activity": "SURGE",
                      "verdict": "HEALTHY", "biggest_positive": "DEX",
                      "biggest_risk": "None — no isolated adverse network or market print this run.",
                      "score": 100, "what_changed": "x", "why_it_matters": "y"},
            "health_score": {"score": 100, "formula": "25x"},
            "economics": eco,
        })
        self.assertIn("2026-08-25", html)
        self.assertIn("Solana REV", html)
        # The REV tile should show a dollar figure, not the word incomplete as the value
        self.assertIn("UTC calendar day 2026-08-25", html)

class InsightBriefTests(unittest.TestCase):
    def _surge_fixture(self):
        cluster = {"tps_total": 4000, "tps_nonvote": 1500, "slot_time_sec": 0.365, "health": "ok", "slot": 1}
        validators = {"delinquent_stake_pct": 0.017, "nakamoto_33": 19}
        market = {"usd": 100, "usd_24h_change": -1.0}
        defi = {"dex": {"change_7d_pct": 103, "change_1d_pct": 2, "total_24h_usd": 3e9},
                "top_dexs": [{"name": "Raydium"}], "tvl_usd": 5e9, "tvl_change_1d_pct": 0.2}
        tx_fees = {"ok": True, "p50_sol": 0.00002, "n_fees": 100, "n_tx": 100,
                   "window_seconds": 3500, "slot_lo": 10, "slot_hi": 20}
        xs = {"market_cap_usd": 5e7, "count_solana": 715, "count_priced": 24,
              "count_unique_underlying": 40, "top": [{"symbol": "TSLAx"}]}
        flags = [{
            "key": "dex_move_7d", "severity": "info",
            "title": "Large Solana DEX volume 7d move",
            "detail": "DeFiLlama Solana DEX volume 7d change is +103.13%.",
        }]
        return cluster, validators, market, defi, tx_fees, xs, flags

    def test_activity_without_stress_and_healthy_verdict(self):
        cluster, validators, market, defi, tx_fees, xs, flags = self._surge_fixture()
        ins = build_insights(cluster, validators, market, defi, tx_fees, xs, flags)
        ids = [x["id"] for x in ins]
        self.assertIn("activity_without_stress", ids)
        self.assertTrue(1 <= len(ins) <= 6)
        brief = build_brief(cluster, validators, market, defi, {"score": 100, "tps_baseline": 3500}, flags, ins)
        self.assertEqual(brief["verdict"], "HEALTHY")
        self.assertEqual(brief["network_health"], "HEALTHY")

    def test_dex_surge_is_healthy_plus_surge_not_watch(self):
        cluster, validators, market, defi, tx_fees, xs, flags = self._surge_fixture()
        ins = build_insights(cluster, validators, market, defi, tx_fees, xs, flags)
        brief = build_brief(cluster, validators, market, defi, {"score": 100, "tps_baseline": 3500}, flags, ins)
        self.assertEqual(brief["network_health"], "HEALTHY")
        self.assertEqual(brief["ecosystem_activity"], "SURGE")
        self.assertNotEqual(brief["verdict"], "WATCH")
        self.assertIn("DEX", brief["biggest_positive"])
        self.assertNotIn("+103", brief["biggest_risk"])
        self.assertNotEqual(brief["biggest_positive"], brief["biggest_risk"])
        self.assertTrue(
            brief["biggest_risk"].lower().startswith("none")
            or "no isolated" in brief["biggest_risk"].lower()
        )

    def test_degraded_when_slots_are_slow(self):
        cluster = {"tps_total": 500, "slot_time_sec": 0.72, "health": "ok"}
        brief = build_brief(cluster, {"delinquent_stake_pct": 0.1}, {}, {}, {"score": 40}, [], [])
        self.assertEqual(brief["verdict"], "DEGRADED")

    def test_critical_when_slots_are_very_slow(self):
        cluster = {"tps_total": 500, "slot_time_sec": 0.85, "health": "ok"}
        brief = build_brief(cluster, {"delinquent_stake_pct": 0.1}, {}, {}, {"score": 40}, [], [])
        self.assertEqual(brief["network_health"], "CRITICAL")
        self.assertIn("slot", brief["biggest_risk"].lower())
        self.assertFalse(brief["biggest_risk"].lower().startswith("none"))

    def test_healthy_plus_dex_surge_risk_is_none(self):
        cluster = {"tps_total": 4000, "tps_nonvote": 1500, "slot_time_sec": 0.365, "health": "ok", "slot": 1}
        validators = {"delinquent_stake_pct": 0.017, "nakamoto_33": 19}
        defi = {"dex": {"change_7d_pct": 60, "change_1d_pct": 2, "total_24h_usd": 3e9},
                "tvl_usd": 5e9, "tvl_change_1d_pct": 0.2}
        brief = build_brief(cluster, validators, {"usd": 100, "usd_24h_change": 0.5}, defi,
                            {"score": 100, "tps_baseline": 3500}, [], [])
        self.assertEqual(brief["network_health"], "HEALTHY")
        self.assertTrue(brief["biggest_risk"].startswith("None"))
        self.assertIn("vs-7d-ago", brief["what_changed"])
        self.assertNotIn("DEX 7d +", brief["what_changed"])

    def test_delinquency_watch_is_the_biggest_risk(self):
        cluster = {"tps_total": 4000, "slot_time_sec": 0.40, "health": "ok", "slot": 1}
        brief = build_brief(
            cluster,
            {"delinquent_stake_pct": 1.42, "delinquent_count": 12},
            {}, {}, {"score": 82, "tps_baseline": 3500}, [], [],
        )
        self.assertEqual(brief["network_health"], "WATCH")
        self.assertIn("delinquen", brief["biggest_risk"].lower())
        self.assertFalse(brief["biggest_risk"].lower().startswith("none"))

    def test_slot_watch_is_the_biggest_risk(self):
        cluster = {"tps_total": 4000, "slot_time_sec": 0.65, "health": "ok", "slot": 1}
        brief = build_brief(
            cluster, {"delinquent_stake_pct": 0.1}, {}, {}, {"score": 85, "tps_baseline": 3500}, [], [],
        )
        self.assertIn(brief["network_health"], ("WATCH", "DEGRADED"))
        self.assertIn("slot", brief["biggest_risk"].lower())
        self.assertFalse(brief["biggest_risk"].lower().startswith("none"))

    def test_rpc_down_risk_mentions_rpc(self):
        cluster = {"tps_total": None, "slot": None, "slot_time_sec": None, "health": None}
        brief = build_brief(cluster, {"delinquent_stake_pct": 0.0}, {}, {}, {}, [], [])
        self.assertIn(brief["network_health"], ("CRITICAL", "DEGRADED"))
        self.assertIn("rpc", brief["biggest_risk"].lower())
        self.assertFalse(brief["biggest_risk"].lower().startswith("none"))


class FeeWindowTests(unittest.TestCase):
    def test_fee_stats_still_percentiles(self):
        fees = [5000] * 10 + [10000] * 8 + [50000] * 2
        st = fee_stats_from_lamports(fees)
        self.assertEqual(st["n"], 20)
        self.assertGreater(st["p90_lamports"], st["p50_lamports"])

    def test_economics_surfaces_window_seconds(self):
        eco = build_economics(
            {}, {"derived": {"network_fees_sol": 1}}, {"usd": 100},
            tx_fees={"ok": True, "p50_sol": 5e-6, "n_tx": 23000, "window_seconds": 3480,
                     "note": "Time-stratified getBlock sample"},
        )
        self.assertEqual(eco.get("median_tx_fee_window_seconds"), 3480)
        self.assertTrue(eco.get("median_tx_fee_not_24h_census"))


class NewsRecencyTests(unittest.TestCase):
    def test_2022_status_incidents_are_not_current(self):
        now = datetime(2026, 8, 25, 12, 0, tzinfo=UTC)
        items = [
            {"title": "Mainnet Beta Outage", "published": "2022-06-01T21:06:03Z",
             "source": "status.solana.com", "url": "https://status.solana.com/incidents/old"},
            {"title": "Solana Changelog: August 20, 2026", "published": "Mon, 24 Aug 2026 14:19:00 GMT",
             "source": "solana.com/news", "url": "https://solana.com/news/changelog"},
        ]
        b = classify_news_items(items, now=now, unresolved=[], incidents=[])
        current_titles = [x["title"] for x in b["current_news"]]
        self.assertIn("Solana Changelog: August 20, 2026", current_titles)
        self.assertNotIn("Mainnet Beta Outage", current_titles)
        self.assertNotIn("Mainnet Beta Outage", current_titles)
        archive_titles = [x["title"] for x in b["archive"]]
        self.assertNotIn("Mainnet Beta Outage", archive_titles)

    def test_recency_filter_after_merge_drops_old(self):
        now = datetime(2026, 8, 25, tzinfo=UTC)
        merged = [
            {"title": "old", "published": "Mon, 01 Jan 2022 12:00:00 GMT", "source": "solana.com/news"},
            {"title": "new", "published": "Mon, 24 Aug 2026 12:00:00 GMT", "source": "solana.com/news"},
        ]
        kept = filter_rss_by_recency(merged, now=now, max_age_days=45)
        self.assertEqual([x["title"] for x in kept], ["new"])


class Simd525Tests(unittest.TestCase):
    def test_editorial_contains_listing_token(self):
        now = datetime(2026, 8, 25, tzinfo=UTC)
        ed = editorial_block(now, cluster={"slot_time_sec": 0.365})
        blob = json_blob(ed)
        self.assertIn("SIMD-525", blob)
        self.assertIn("400", blob)
        self.assertIn("200", blob)
        self.assertIn("lowering-slot-time-and-validators-economic", blob)
        self.assertLessEqual(blob.lower().count("simd-025"), 1)
        self.assertIn("INFERRED", blob)
        html = render_html({
            "meta": {"version": "1.4.0", "generated_at_utc": "2026-08-26T00:00:00Z",
                     "generated_at_pt": "2026-08-25 17:00:00 PT"},
            "cluster": {"health": "ok", "slot_time_sec": 0.365, "tps_total": 4000},
            "brief": {"network_health": "HEALTHY", "ecosystem_activity": "SURGE",
                      "verdict": "HEALTHY", "biggest_positive": "DEX +103%",
                      "biggest_risk": "None — no isolated adverse network or market print this run.",
                      "score": 100, "what_changed": "DEX 7d +103%", "why_it_matters": "network healthy"},
            "editorial": ed,
            "economics": {"rev_24h_usd": None, "rev_complete": False,
                          "rev_kind": "INCOMPLETE — no 24h Jito tip tape on zero-key sources",
                          "network_fees_usd_24h": 1_140_000,
                          "headline_primary": {"label": "in-protocol network fees 24h", "usd": 1_140_000},
                          "rev_definition": "Blockworks/Helius: fees + tips"},
            "health_score": {"score": 100, "formula": "25x"},
        })
        self.assertIn("SIMD-525", html)
        self.assertIn("HEALTHY", html)
        self.assertIn("$1.14M", html)  # in-protocol fees 24h, not Full REV
        self.assertIn("incomplete", html)
        self.assertNotIn("Borealis REV 24h", html)

    def test_365ms_maps_to_350_stage(self):
        st = infer_simd0525_stage(365)
        self.assertEqual(st["inferred_target_ms"], 350)


def json_blob(obj) -> str:
    import json
    return json.dumps(obj)




class ScriptedHttp(Http):
    """No-network Http: first matching url substring wins."""

    def __init__(self, script):
        super().__init__()
        self.script = script  # list of (substr, status, body_bytes_or_none)

    def request(self, url, *, source_id, data=None, **kw):
        for substr, status, body in self.script:
            if substr in url:
                ok = status == 200 and body is not None
                rec = self._record(
                    id=source_id, url=url, ok=ok, status=status,
                    bytes=len(body or b""), ms=1, attempt=1,
                    fetched_at="t", error=None if ok else f"HTTP {status}",
                )
                return (body if ok else None), rec
        rec = self._record(
            id=source_id, url=url, ok=False, status=599, bytes=0, ms=1,
            attempt=1, fetched_at="t", error="unscripted",
        )
        return None, rec


class FailureFixtureTests(unittest.TestCase):
    def test_rpc_429_falls_back_to_publicnode(self):
        ok_body = json.dumps({"jsonrpc": "2.0", "id": 1, "result": "ok"}).encode()
        http = ScriptedHttp([
            ("api.mainnet-beta.solana.com", 429, None),
            ("solana-rpc.publicnode.com", 200, ok_body),
        ])
        result, rec = http.rpc("getHealth")
        self.assertEqual(result, "ok")
        self.assertTrue(rec.get("ok"))
        self.assertIn("fallback", rec.get("id") or "")
        self.assertTrue(any(r.get("status") == 429 for r in http.log))
        self.assertEqual(PRIMARY_RPC, "https://api.mainnet-beta.solana.com")
        self.assertEqual(FALLBACK_RPC, "https://solana-rpc.publicnode.com")

    def test_coingecko_429_uses_coinbase_and_is_expected(self):
        cb = json.dumps({"last": "100", "open": "90", "volume": "10",
                         "high": "110", "low": "80"}).encode()
        http = ScriptedHttp([
            ("api.coingecko.com", 429, None),
            ("api.exchange.coinbase.com", 200, cb),
        ])
        market = assemble_market(http)
        self.assertTrue(market.get("ok"))
        self.assertAlmostEqual(market.get("usd"), 100.0)
        self.assertIn("coinbase", (market.get("source") or "").lower())
        self.assertTrue(any(
            s.get("id") == "coingecko.simple_price" and s.get("status") == 429
            for s in http.log
        ))
        dh = build_data_health(http.log, market, {"tps_total": 4000})
        self.assertGreaterEqual(dh["expected_unavailable"], 1)
        self.assertIn("required sources", dh["headline"])
        self.assertIn("expected unavailable", dh["headline"])
        self.assertNotIn("108/132", dh["headline"])
        # raw 0/1 would be misleading; gecko 429 is not a required miss
        self.assertEqual(dh["ok"], dh["total"])

    def test_xstocks_mcap_labeled_priced_subset_not_llama_tvl(self):
        html = render_html({
            "meta": {"version": "1.4.0", "generated_at_utc": "2026-08-26T00:00:00Z",
                     "generated_at_pt": "2026-08-25 17:00:00 PT"},
            "cluster": {"health": "ok", "slot_time_sec": 0.365, "tps_total": 4000},
            "brief": {"network_health": "HEALTHY", "ecosystem_activity": "SURGE",
                      "verdict": "HEALTHY", "biggest_positive": "DEX",
                      "biggest_risk": "None — no isolated adverse network or market print this run.",
                      "score": 100, "what_changed": "x", "why_it_matters": "y"},
            "health_score": {"score": 100, "formula": "25x"},
            "economics": {"rev_24h_usd": None, "rev_complete": False,
                          "rev_kind": "INCOMPLETE — no 24h Jito tip tape on zero-key sources",
                          "network_fees_usd_24h": 1_000_000,
                          "headline_primary": {"label": "in-protocol network fees 24h", "usd": 1_000_000},
                          "protocol_fees_usd": 14_000_000},
            "xstocks": {
                "market_cap_usd": 276_000_000,
                "count_priced": 24, "count_solana": 715,
                "count_unique_underlying": 40,
                "volume_24h_usd": 23_000_000,
                "llama_solana_tvl_usd": 430_000_000,
                "mcap_note": "Priced-subset lower bound over 24 of 715",
                "volume_coverage": "priced-subset / search hits, not all 715",
            },
            "data_health": {
                "headline": "required sources 10/10 OK · 3 expected unavailable",
                "headline_confidence": "HIGH",
                "expected_unavailable": 3,
                "notes": ["3 expected misses (gated RSS, CoinGecko 429, Jupiter search 429/404)"],
                "failures": [],
            },
        })
        self.assertIn('<div class="verdict HEALTHY">', html)
        self.assertIn("priced 24 of 715", html)
        self.assertIn("lower bound", html)
        self.assertIn("priced-subset", html)
        self.assertIn("$276.00M", html)
        self.assertIn("$430.00M", html)
        self.assertIn("liquidity, not mcap", html)
        self.assertIn("required sources 10/10 OK", html)
        self.assertIn("expected unavailable", html)
        self.assertNotIn("108/132", html)
        # protocol fees stay excluded from in-protocol fees / Full REV tiles
        self.assertIn("$1.00M", html)
        self.assertIn("incomplete", html)
        self.assertNotIn("Borealis REV 24h", html)
        proto_chunk = html.split("In-protocol fees 24h")[1].split("Protocol fees")[0] if "In-protocol fees 24h" in html else html
        self.assertNotIn("$14.00M", proto_chunk)



class MultiplierFetchTests(unittest.TestCase):
    def _assets(self):
        return json.dumps({
            "nodes": [{
                "name": "Tesla xStock", "symbol": "TSLAx", "underlyingSymbol": "TSLA",
                "isTradingHalted": False,
                "deployments": [{"network": "Solana", "address": "SoLtsla111", "solanaTokenProgram": "spl"}],
            }],
            "page": {"hasNextPage": False, "currentPage": 0},
        }).encode()

    def test_xstocks_fetches_multiplier_and_uses_currentMultiplier(self):
        price = json.dumps({"quote": 10}).encode()
        circ = json.dumps({"value": 100}).encode()
        mult = json.dumps({"currentMultiplier": 2}).encode()
        http = ScriptedHttp([
            ("/public/assets?pageSize", 200, self._assets()),
            ("/price-data", 200, price),
            ("circulating-supply", 200, circ),
            ("/multiplier?network=Solana", 200, mult),
        ])
        xs = fetch_xstocks(http)
        urls = [str(r.get("url") or "") for r in http.log]
        ids = [str(r.get("id") or "") for r in http.log]
        self.assertTrue(any("/multiplier?network=Solana" in u for u in urls))
        self.assertTrue(any(i.startswith("xstocks.mult") for i in ids))
        self.assertIn("multiplier", xs.get("multiplier_route") or "")
        self.assertTrue(xs.get("ok"))
        self.assertAlmostEqual(xs.get("market_cap_usd"), 2000.0)  # 10*100*2, not silent 1.0
        self.assertEqual(xs.get("count_multiplier_ok"), 1)
        self.assertEqual(xs.get("count_mcap_computable"), 1)
        self.assertFalse(xs.get("mcap_is_census"))
        self.assertIn("Solana", xs.get("count_meaning") or "")

    def test_missing_multiplier_omits_mcap_never_silent_one(self):
        price = json.dumps({"quote": 10}).encode()
        circ = json.dumps({"value": 100}).encode()
        http = ScriptedHttp([
            ("/public/assets?pageSize", 200, self._assets()),
            ("/price-data", 200, price),
            ("circulating-supply", 200, circ),
            ("/multiplier", 400, None),
        ])
        xs = fetch_xstocks(http)
        urls = [str(r.get("url") or "") for r in http.log]
        self.assertTrue(any("/multiplier?network=Solana" in u for u in urls))
        self.assertIsNone(xs.get("market_cap_usd"))
        self.assertEqual(xs.get("count_multiplier_ok"), 0)
        self.assertEqual(xs.get("count_mcap_computable"), 0)
        row = (xs.get("assets") or [{}])[0]
        self.assertIsNone(row.get("multiplier"))
        self.assertIsNone(row.get("mcap_usd"))
        # 10*100*1.0 would be 1000 — that silent 1.0 is the 1.4.1 lie
        self.assertNotEqual(row.get("mcap_usd"), 1000.0)
        dh = build_data_health(http.log, {"usd": 100}, {"tps_total": 4000})
        self.assertGreaterEqual(dh["expected_unavailable"], 1)


class FeeCensusLabelTests(unittest.TestCase):
    def test_fee_json_and_tile_scream_not_24h_census(self):
        eco = build_economics(
            {}, {"derived": {"network_fees_sol": 1}}, {"usd": 100},
            tx_fees={"ok": True, "p50_sol": 5e-6, "p90_sol": 1e-5, "n_tx": 4000, "n_fees": 4000,
                     "window_seconds": 9800, "window_hours_label": "~2.7h",
                     "not_24h_census": True,
                     "note": "NOT a 24h census. Time-stratified getBlock sample."},
        )
        self.assertEqual(eco.get("median_tx_fee_window_seconds"), 9800)
        self.assertTrue(eco.get("median_tx_fee_not_24h_census"))
        html = render_html({
            "meta": {"version": "1.4.1", "generated_at_utc": "2026-08-26T00:00:00Z",
                     "generated_at_pt": "2026-08-25 17:00:00 PT"},
            "cluster": {"health": "ok", "slot_time_sec": 0.365, "tps_total": 4000},
            "brief": {"network_health": "HEALTHY", "ecosystem_activity": "SURGE",
                      "verdict": "HEALTHY", "biggest_positive": "DEX",
                      "biggest_risk": "None — no isolated adverse network or market print this run.",
                      "score": 100, "what_changed": "x", "why_it_matters": "y"},
            "health_score": {"score": 100, "formula": "25x"},
            "economics": eco,
        })
        self.assertIn("NOT a 24h census", html)
        self.assertIn("window_seconds", html)
        self.assertTrue("9800" in html or "9,800" in html)
        self.assertTrue(eco.get("median_tx_fee_not_24h_census"))

    def test_jito_sensitivity_p50_vs_p95_not_a_ledger(self):
        eco = build_economics(
            {"fees": {"total_24h_usd": 14_490_000}},
            {"derived": {"network_fees_sol": 9000}},
            {"usd": 100},
            tx_fees={"ok": True, "p50_sol": 0.00001, "window_seconds": 9000, "not_24h_census": True},
            jito={"ok": True, "landed_p50_sol": 1e-5, "landed_p95_sol": 4e-5},
            cluster={"tps_nonvote": 2000},
        )
        tips_p50 = 1e-5 * 2000 * 86400 * 100
        tips_p95 = 4e-5 * 2000 * 86400 * 100
        self.assertIsNone(eco.get("rev_24h_usd"))
        self.assertFalse(eco.get("rev_complete"))
        self.assertAlmostEqual(eco.get("network_fees_usd_24h"), 900_000)
        self.assertNotEqual(eco.get("rev_24h_usd"), 900_000 + tips_p50)
        self.assertNotEqual(eco.get("rev_24h_usd"), 900_000 + tips_p95)
        jr = eco.get("jito_runrate_not_rev") or {}
        self.assertTrue(jr.get("not_a_24h_aggregate"))
        self.assertFalse(jr.get("included_in_headline"))
        self.assertAlmostEqual(jr.get("runrate_24h_usd"), tips_p50)
        self.assertAlmostEqual(jr.get("runrate_p95_usd"), tips_p95)
        self.assertIn("p50", (eco.get("rev_sensitivity") or "").lower())
        self.assertIn("p95", (eco.get("rev_sensitivity") or "").lower())
        self.assertFalse(eco.get("rev_jito_is_ledger"))
        self.assertIn("INVALID", (jr.get("kind") or "").upper())




if __name__ == "__main__":
    unittest.main()


class ConfidenceCapTests(unittest.TestCase):
    def test_incomplete_rev_and_subset_mcap_are_not_high(self):
        dh = {"headline_confidence": "HIGH", "notes": [], "ok": 10, "total": 10}
        out = cap_headline_confidence(
            dh,
            {"rev_complete": False, "network_fees_date": "2026-08-24"},
            {"count_mcap_computable": 80, "count_solana": 715},
        )
        self.assertEqual(out["headline_confidence"], "MIXED")
        blob = " ".join(out["notes"]).lower()
        self.assertIn("rev incomplete", blob)
        self.assertIn("priced subset", blob)
        self.assertNotEqual(out["headline_confidence"], "HIGH")

    def test_complete_census_can_stay_high(self):
        dh = {"headline_confidence": "HIGH", "notes": []}
        out = cap_headline_confidence(
            dh,
            {"rev_complete": True},
            {"count_mcap_computable": 10, "count_solana": 10},
        )
        self.assertEqual(out["headline_confidence"], "HIGH")
