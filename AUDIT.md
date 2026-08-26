# Borealis 1.4.0 — live-defect closeout

Against independent live audit of **1.3.0** (`generated_at_pt` 2026-08-25 17:17:13 PT)
at https://dustycompiler.github.io/borealis-solana/. Superteam listing still 14
submissions; listing text is **SIMD-525** (not SIMD-0525, not SIMD-025).

No secrets. No competitor source copied.

## P0 — closed this cycle

### P0-1 Verdict WATCH with health score 100
**Live 1.3:** `<div class="verdict WATCH">WATCH</div>` next to score 100 while slot
~365 ms and delinquent 0.017% were quiet. DEX +103% painted the network WATCH.

**1.4:** Network Health (`HEALTHY` / `WATCH` / `DEGRADED` / `CRITICAL`) is scored
from RPC, slot, TPS vs baseline, delinquency, and status.solana.com **only**.
Ecosystem Activity (`QUIET` / `NORMAL` / `ELEVATED` / `SURGE` / `CONTRACTION`)
is a separate cell from DEX/TVL/DAA. A DEX surge cannot make the network WATCH.
Tests: `test_dex_surge_is_healthy_plus_surge_not_watch`.

### P0-2 Biggest positive and biggest risk both DEX +103%
**Live 1.3:** both cells restated the same DeFiLlama DEX 7d change.

**1.4:** `biggest_risk` is only filled when the item is actually adverse
(`item_is_adverse_risk`). Same-id / same-detail positives are stripped from
risk. If nothing is adverse: `None — no isolated adverse network or market print this run.`

### P0-3 REV cell was an em-dash
**Live 1.3:** heading "Economic value (not REV)"; REV total `—`. Competitors:
Heliostat/0x-SquidSol **$1.14M** (fees + tips), Orbit `rev_24h_usd` ~$1.24M,
Pulse wrongly labels **$14.49M** llama protocol fees as REV. Do not copy Pulse.

**1.4 Borealis REV 24h** (Blockworks/Helius):
- MEASURED in-protocol = `solana.com/data` Fees (Allium/Dune/Blockworks) × SOL-USD
- ESTIMATED Jito tips = `tip_floor p50 × non-vote TPS × 86400` (labeled ESTIMATED)
- DeFiLlama `/overview/fees/Solana` protocol/application fees stay **separate and EXCLUDED**
- Tile shows a dollar number **and** `rev_definition`

Tests: `test_protocol_fees_are_not_included_in_rev`, `test_jito_estimate_adds_to_rev_not_llama`.

### P0-4 Page never wrote SIMD-525
**Live 1.3:** argued SIMD-025 / SIMD-0326; grepping `SIMD-525` missed.

**1.4:** Overview editorial title is `SIMD-525 (SIMD-0525) reduced slot times + Alpenglow (SIMD-0326)`.
Tracker uses the exact listing token. Stages 400→350→300→250→200 ms vs observed
slot (~365 ms → 350 ms first step). Alpenglow SIMD-0326 remains secondary.
Tests: `test_editorial_contains_listing_token`, `test_365ms_maps_to_350_stage`.

## P1 — closed or reduced this cycle

### P1 xStocks $277M looking like a 715 census
Tile subline is now `priced N of M Solana listings · lower bound`. Separate
**xStocks vol 24h** tile (Jupiter lite-api `stats24h` buy+sell). Unique underlyings counted.

### P1 2022–2024 status.solana.com incidents as current
`_parse_pub` accepts ISO-8601 as well as RFC2822. News buckets: active /
recently resolved (14d) / current news (14d) / archive. 2022 incidents drop out
of current. Test: `test_2022_status_incidents_are_not_current`.

### P1 median fee ~16 consecutive slots despite ~23k txs
Time-stratified sample: last 6 finalized blocks (spot) + ~12 blocks from
`getRecentPerformanceSamples` (~1h). Labels `window_seconds`, `n_blocks`, `n_tx`.
Test: `test_economics_surfaces_window_seconds`.

## Residual P1 / honesty notes

- Jito tips 24h is an **estimate** (floor × non-vote TPS), not a Jito ledger. Labeled.
- xStocks mcap remains a priced subset, not a full tokenized-equity census. Volume
  coverage is whatever Jupiter search returns for those mints.
- SIMD-0525 stage is inferred from observed slot time, not a feature-gate RPC.
- CoinGecko 429, gated RSS, xStocks multiplier 404s are expected-unavailable in
  data-health, not silent failures.
- 90d Trends button is hidden unless the TVL series has ≥60 points.

## Tests

`python3 -m unittest discover -s tests -v` — 30 tests, stdlib, no network.
