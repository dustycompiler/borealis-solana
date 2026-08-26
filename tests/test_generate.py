#!/usr/bin/env python3
"""Stdlib tests for Borealis generate.py helpers. No network."""
from __future__ import annotations

import os
import statistics
import sys
import unittest
from datetime import datetime, timedelta, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from generate import (  # noqa: E402
    build_brief,
    build_economics,
    build_insights,
    compute_health,
    detect_anomalies,
    equity_mcap,
    fee_stats_from_lamports,
    filter_rss_by_recency,
    pct_24h,
    percentile,
    rss_is_stale,
)


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


class EconomicsHonestyTests(unittest.TestCase):
    def test_protocol_fees_are_not_headline_rev(self):
        eco = build_economics(
            {"fees": {"total_24h_usd": 1e6, "change_1d_pct": 4}},
            {"derived": {"network_fees_sol": 9000}},
            {"usd": 100},
            tx_fees={"ok": True, "p50_sol": 0.00001, "p90_sol": 0.00005, "p99_sol": 0.0002,
                     "n_fees": 12, "slot_lo": 1, "slot_hi": 10, "note": "sample"},
            jito={"ok": False, "error": "timeout"},
        )
        self.assertIsNone(eco.get("total_rev_usd"))
        self.assertIsNone(eco.get("rev_proxy_usd"))
        self.assertIn("not REV", eco.get("protocol_fees_label") or "")
        self.assertEqual(eco.get("protocol_fees_usd"), 1e6)
        self.assertAlmostEqual(eco.get("median_tx_fee_sol"), 0.00001)
        self.assertTrue(eco.get("jito", {}).get("omitted"))


class InsightBriefTests(unittest.TestCase):
    def test_activity_without_stress_and_healthy_verdict(self):
        cluster = {"tps_total": 4000, "slot_time_sec": 0.365, "health": "ok"}
        validators = {"delinquent_stake_pct": 0.04, "nakamoto_33": 19}
        market = {"usd": 100, "usd_24h_change": -1.0}
        defi = {"dex": {"change_7d_pct": 103, "change_1d_pct": 2, "total_24h_usd": 3e9},
                "top_dexs": [{"name": "Raydium"}], "tvl_usd": 5e9, "tvl_change_1d_pct": 0.2}
        tx_fees = {"ok": True, "p50_sol": 0.00002, "n_fees": 100, "slot_lo": 10, "slot_hi": 20}
        xs = {"market_cap_usd": 5e7, "count_solana": 40, "top": [{"symbol": "TSLAx"}]}
        ins = build_insights(cluster, validators, market, defi, tx_fees, xs, [])
        ids = [x["id"] for x in ins]
        self.assertIn("activity_without_stress", ids)
        self.assertTrue(1 <= len(ins) <= 6)
        brief = build_brief(cluster, validators, market, defi, {"score": 99}, [], ins)
        self.assertEqual(brief["verdict"], "HEALTHY")

    def test_degraded_when_slots_are_slow(self):
        cluster = {"tps_total": 500, "slot_time_sec": 0.85, "health": "ok"}
        brief = build_brief(cluster, {"delinquent_stake_pct": 0.1}, {}, {}, {"score": 40}, [], [])
        self.assertEqual(brief["verdict"], "DEGRADED")


if __name__ == "__main__":
    unittest.main()
