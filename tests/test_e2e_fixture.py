#!/usr/bin/env python3
"""Fixture-backed HTML/MD/JSON sink. No network."""
from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path

from generate import VERSION, build_brief, write_outputs
from htmlout import render_html


def _snap(**over):
    cluster = {
        "health": "ok", "slot": 441000000, "tps_total": 4000, "tps_nonvote": 2000,
        "slot_time_sec": 0.365, "epoch": 1022, "block_height": 400000000,
        "absolute_slot": 441000000,
    }
    validators = {
        "delinquent_stake_pct": 0.02, "nakamoto_33": 19, "current_count": 1400,
        "delinquent_count": 2,
    }
    brief = build_brief(
        cluster, validators, {"usd_24h_change": -1.0},
        {"dex": {"change_7d_pct": 60, "change_1d_pct": -2, "total_24h_usd": 2.95e9,
                 "change_7d_over_7d_pct": 100, "total_7d_usd": 21.6e9}},
        {"score": 96, "tps_baseline": 3500}, [], [],
    )
    base = {
        "meta": {
            "version": VERSION,
            "generated_at_utc": "2026-08-26T02:13:17Z",
            "generated_at_pt": "2026-08-25 19:13:17 PT",
            "run_id": "fixture-e2e",
        },
        "cluster": cluster,
        "validators": validators,
        "market": {"usd": 96.9, "usd_24h_change": -1.0, "source": "coinbase"},
        "defi": {"tvl_usd": 9e9, "tvl_change_1d_pct": -0.8,
                 "dex": {"total_24h_usd": 2.95e9, "total_7d_usd": 21.6e9,
                         "change_1d_pct": -1.6, "change_7d_pct": 60.4,
                         "change_7d_over_7d_pct": 100.1,
                         "change_7d_meaning": "percent change of 24h DEX volume vs the 24h from 7 days ago"}},
        "stablecoins": {"circulating_usd": 1e10},
        "economics": {
            "rev_24h_usd": None, "rev_complete": False,
            "rev_kind": "INCOMPLETE — no 24h Jito tip tape on zero-key sources",
            "network_fees_usd_24h": 887_000, "network_fees_sol_24h": 9100,
            "protocol_fees_usd": 14_080_000, "protocol_fees_excluded_from_rev": True,
            "median_tx_fee_sol": 5e-6, "median_tx_fee_not_24h_census": True,
            "median_tx_fee_window_seconds": 9961,
        },
        "xstocks": {
            "count_solana": 715, "count_unique_underlying": 715, "count_priced": 80,
            "count_multiplier_ok": 80, "count_mcap_computable": 80,
            "market_cap_usd": 277e6, "volume_24h_usd": 23.5e6,
            "volume_kind": "Jupiter-reported xStocks subset 24h activity",
            "multiplier_route": "/public/assets/{sym}/multiplier?network=Solana",
        },
        "brief": brief,
        "health_score": {"score": 96, "formula": "25/30/25/20 Borealis heuristic"},
        "editorial": {"title": "SIMD-525 reduced slot times + Alpenglow (SIMD-0326)",
                      "correction": "Listing token SIMD-525 is SIMD-0525. Not SIMD-025.",
                      "summary": "Observed slot is INFERRED corroboration."},
        "news": {"current_news": [{"title": "Solana Changelog", "published": "2026-08-24T00:00:00Z"}],
                 "archive": [{"title": "Mainnet Beta Outage", "published": "2022-06-01T21:06:03Z"}],
                 "active_incidents": [], "recent_resolved": []},
        "anomalies": [],
        "insights": [],
        "data_health": {"headline": "required sources 3/3 OK", "headline_confidence": "HIGH"},
        "dune": {"label": "External Reference — public Dune embed, not a Borealis query"},
        "jito": {"landed_p50_sol": 6.5e-6, "ok": True},
        "sources": [],
        "omissions": [],
    }
    base.update(over)
    return base


class EndToEndFixtureTests(unittest.TestCase):
    def test_write_outputs_consistent_and_honest(self):
        snap = _snap()
        with tempfile.TemporaryDirectory() as td:
            out_dir = os.path.join(td, "out")
            docs_dir = os.path.join(td, "docs")
            write_outputs(snap, out_dir, docs_dir, screenshot=False)
            for name in ("index.html", "report.md", "report.json"):
                self.assertTrue(os.path.isfile(os.path.join(out_dir, name)))
                self.assertTrue(os.path.isfile(os.path.join(docs_dir, name)))
            html = Path(out_dir, "index.html").read_text(encoding="utf-8")
            md = Path(out_dir, "report.md").read_text(encoding="utf-8")
            js = json.loads(Path(out_dir, "report.json").read_text(encoding="utf-8"))
            self.assertEqual(js["meta"]["version"], VERSION)
            self.assertEqual(js["meta"]["generated_at_utc"], "2026-08-26T02:13:17Z")
            self.assertIsNone(js["economics"]["rev_24h_usd"])
            self.assertFalse(js["economics"]["rev_complete"])
            self.assertIn("INCOMPLETE", js["economics"]["rev_kind"])
            self.assertIn("incomplete", html.lower())
            self.assertIn("incomplete", md.lower())
            self.assertNotIn("Borealis REV 24h", html)
            self.assertNotIn("multiplier=1.0 assumed", html)
            self.assertIn("SIMD-525", html)
            self.assertIn("HEALTHY", html)
            self.assertIn("SURGE", html)
            # 2022 incident is archive in the model; must not be advertised as current
            self.assertIn("Archive (not current)", html)
            self.assertIn("Mainnet Beta Outage", html)
            current = html.split("Archive (not current)")[0]
            self.assertNotIn("Mainnet Beta Outage", current)
            self.assertIn("Solana Changelog", current)
            self.assertEqual(js["market"]["usd"], 96.9)
            self.assertIn("96.9", html.replace(",", "") + md.replace(",", ""))
            self.assertEqual(js["brief"]["network_health"], "HEALTHY")
            self.assertFalse(js["brief"]["biggest_risk"].lower().startswith("none") and js["brief"]["network_health"] != "HEALTHY")
            self.assertIn("External Reference", html + md + json.dumps(js))
            self.assertIn("live-pulse", html)
            self.assertIn("on-page-now", html)
            self.assertIn("solana-rpc.publicnode.com", html)
            self.assertNotIn("updates every 15 min via GitHub Action", html)

    def test_watch_delinquency_is_never_none_risk(self):
        cluster = {
            "health": "ok", "slot": 1, "tps_total": 4000, "tps_nonvote": 2000,
            "slot_time_sec": 0.365,
        }
        validators = {"delinquent_stake_pct": 1.42, "delinquent_count": 9, "nakamoto_33": 19}
        brief = build_brief(cluster, validators, {}, {}, {"score": 82, "tps_baseline": 3500}, [], [])
        self.assertEqual(brief["network_health"], "WATCH")
        self.assertIn("delinquen", brief["biggest_risk"].lower())
        self.assertFalse(brief["biggest_risk"].lower().startswith("none"))
        html = render_html(_snap(cluster=cluster, validators=validators, brief=brief,
                                 health_score={"score": 82}))
        self.assertIn("WATCH", html)
        self.assertNotIn("None — no isolated", html)
