#!/usr/bin/env python3
"""Slot health follows the live SIMD-0525 gate, not a stale 400 ms floor."""
from __future__ import annotations

import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from generate import (  # noqa: E402
    SIMD0525_STAGES,
    SLOT_ALERT_RATIO,
    classify_network_health,
    compute_health,
    detect_anomalies,
    live_slot_target_ms,
    slot_component_points,
    slot_health_params,
)


def gates_with_live(g: int) -> dict:
    """Minimal classify_simd0525_gates-shaped payload with live floor G."""
    stages = []
    for st in SIMD0525_STAGES:
        tgt = st["target_ms"]
        if tgt == 400:
            status = "baseline" if g >= 400 else "superseded"
        elif g >= 400:
            status = "pending"
        elif tgt > g:
            status = "pending"
        else:
            status = "live"
        stages.append({
            "target_ms": tgt,
            "feature": st.get("feature"),
            "gate": st.get("gate"),
            "status": status,
        })
    return {
        "live_target_ms": None if g >= 400 else g,
        "stages": stages,
        "kind": "FEATURE_GATE",
    }


def _cluster(slot_ms: float, tps: float = 4000.0) -> dict:
    return {
        "health": "ok",
        "slot": 1,
        "tps_total": tps,
        "tps_median": tps,
        "slot_time_sec": slot_ms / 1000.0,
        "slot_time_last": slot_ms / 1000.0,
    }


def _sdata(tps: float = 4000.0) -> dict:
    return {"derived": {"tps_30d_median": tps, "tps_30d_source": "test baseline"}}


def _validators() -> dict:
    return {"delinquent_stake_pct": 0.0, "delinquent_count": 0}


def _slot_points(health: dict) -> float:
    by = {p["id"]: p for p in health["parts"]}
    return by["slot"]["points"]


class LiveSlotTargetTests(unittest.TestCase):
    def test_highest_live_stage_wins(self):
        g = gates_with_live(300)
        self.assertEqual(live_slot_target_ms(g), 300)
        self.assertEqual(live_slot_target_ms(gates_with_live(350)), 350)
        self.assertEqual(live_slot_target_ms(gates_with_live(250)), 250)
        self.assertEqual(live_slot_target_ms(gates_with_live(200)), 200)

    def test_historical_400_baseline_is_the_floor(self):
        self.assertEqual(live_slot_target_ms(gates_with_live(400)), 400)

    def test_missing_gates_do_not_silently_return_400(self):
        self.assertIsNone(live_slot_target_ms(None))
        self.assertIsNone(live_slot_target_ms({}))
        self.assertIsNone(live_slot_target_ms({"stages": [], "live_target_ms": None}))


class GateTransitionScoreAlertTests(unittest.TestCase):
    """400 → 350 → 300 → 250 → 200: score/alert use G, not a stale 400 ms floor."""

    GATES = (400, 350, 300, 250, 200)

    def test_each_live_gate_keys_score_and_alert(self):
        for G in self.GATES:
            gates = gates_with_live(G)
            self.assertEqual(live_slot_target_ms(gates), G, msg=f"G={G}")
            params = slot_health_params(gates)
            self.assertEqual(params["G"], G)
            self.assertAlmostEqual(params["alert_ms"], SLOT_ALERT_RATIO * G)
            # full score at G
            h = compute_health(_cluster(float(G)), _validators(), _sdata(), gates=gates)
            self.assertAlmostEqual(_slot_points(h), 30.0, places=2, msg=f"G={G} at {G} ms")
            # zero at 2G
            h2 = compute_health(_cluster(float(2 * G)), _validators(), _sdata(), gates=gates)
            self.assertAlmostEqual(_slot_points(h2), 0.0, places=2, msg=f"G={G} at {2 * G} ms")
            # 1.25G alerts; just under does not
            alert = SLOT_ALERT_RATIO * G
            flags_hi = detect_anomalies(
                _cluster(alert + 1.0), _validators(),
                {"usd": 100.0, "usd_24h_change": 0.1},
                {"dex": {}, "fees": {}}, {"indicator": "none"}, [], {},
                gates=gates,
            )
            self.assertTrue(
                any(f["key"] == "slow_slots" for f in flags_hi),
                msg=f"G={G} should alert at {alert + 1} ms",
            )
            flags_lo = detect_anomalies(
                _cluster(max(G, alert - 1.0)), _validators(),
                {"usd": 100.0, "usd_24h_change": 0.1},
                {"dex": {}, "fees": {}}, {"indicator": "none"}, [], {},
                gates=gates,
            )
            self.assertFalse(
                any(f["key"] == "slow_slots" for f in flags_lo),
                msg=f"G={G} should not alert at {max(G, alert - 1)} ms",
            )
            # formula must name this G, not a leftover 400 (unless G is 400)
            if G != 400:
                self.assertNotIn("slot_ms − 400", h["formula"])
                self.assertIn(f"slot_ms − {G}", h["formula"])

    def test_live_G300_300ms_full_390ms_is_21_and_alerts(self):
        gates = gates_with_live(300)
        h300 = compute_health(_cluster(300.0), _validators(), _sdata(), gates=gates)
        h390 = compute_health(_cluster(390.0), _validators(), _sdata(), gates=gates)
        h400 = compute_health(_cluster(400.0), _validators(), _sdata(), gates=gates)
        self.assertAlmostEqual(_slot_points(h300), 30.0, places=2)
        self.assertAlmostEqual(_slot_points(h390), 21.0, places=2)
        self.assertNotAlmostEqual(_slot_points(h400), 30.0, places=2)
        self.assertAlmostEqual(_slot_points(h400), 20.0, places=2)
        self.assertAlmostEqual(slot_component_points(390.0, 300), 21.0, places=6)
        flags = detect_anomalies(
            _cluster(390.0), _validators(),
            {"usd": 100.0, "usd_24h_change": 0.1},
            {"dex": {}, "fees": {}}, {"indicator": "none"}, [], {},
            gates=gates,
        )
        self.assertTrue(any(f["key"] == "slow_slots" for f in flags))
        self.assertFalse(any(f["key"] == "slow_slots_500ms" for f in flags))
        net = classify_network_health(
            _cluster(390.0), _validators(), h390, flags, gates=gates,
        )
        self.assertEqual(net["label"], "WATCH")
        self.assertIn("375", net["dominant"] or "")

    def test_historical_G400_390ms_still_full_and_does_not_alert(self):
        """Proves we did not invert old 400 ms floor behavior."""
        gates = gates_with_live(400)
        h390 = compute_health(_cluster(390.0), _validators(), _sdata(), gates=gates)
        self.assertAlmostEqual(_slot_points(h390), 30.0, places=2)
        flags = detect_anomalies(
            _cluster(390.0), _validators(),
            {"usd": 100.0, "usd_24h_change": 0.1},
            {"dex": {}, "fees": {}}, {"indicator": "none"}, [], {},
            gates=gates,
        )
        self.assertFalse(any(f["key"] == "slow_slots" for f in flags))
        net = classify_network_health(
            _cluster(390.0), _validators(), h390, flags, gates=gates,
        )
        self.assertEqual(net["label"], "HEALTHY")

    def test_live_G250_300ms_not_full_alert_follows_312_5(self):
        gates = gates_with_live(250)
        h300 = compute_health(_cluster(300.0), _validators(), _sdata(), gates=gates)
        self.assertAlmostEqual(_slot_points(h300), 24.0, places=2)
        params = slot_health_params(gates)
        self.assertAlmostEqual(params["alert_ms"], 312.5)
        flags_300 = detect_anomalies(
            _cluster(300.0), _validators(),
            {"usd": 100.0, "usd_24h_change": 0.1},
            {"dex": {}, "fees": {}}, {"indicator": "none"}, [], {},
            gates=gates,
        )
        self.assertFalse(any(f["key"] == "slow_slots" for f in flags_300))
        flags_313 = detect_anomalies(
            _cluster(313.0), _validators(),
            {"usd": 100.0, "usd_24h_change": 0.1},
            {"dex": {}, "fees": {}}, {"indicator": "none"}, [], {},
            gates=gates,
        )
        self.assertTrue(any(f["key"] == "slow_slots" for f in flags_313))

    def test_gate_unavailable_refuses_400ms_floor(self):
        h = compute_health(_cluster(400.0), _validators(), _sdata(), gates=None)
        self.assertAlmostEqual(_slot_points(h), 0.0, places=2)
        self.assertIsNone(h["live_slot_target_ms"])
        self.assertIn("refusing", (h.get("slot_gate_note") or h["parts"][1]["detail"]).lower())
        flags = detect_anomalies(
            _cluster(400.0), _validators(),
            {"usd": 100.0, "usd_24h_change": 0.1},
            {"dex": {}, "fees": {}}, {"indicator": "none"}, [], {},
        )
        self.assertFalse(any(f["key"] in ("slow_slots", "slow_slots_500ms") for f in flags))


if __name__ == "__main__":
    unittest.main()
