# Borealis 1.4.1 — skeptical self-score

Scored 2026-08-25 **18:15 PT** (2026-08-26T01:15:11Z) against the generated snapshot
that this commit ships (`generated_at_utc` **2026-08-26T01:15:11Z**,
`generated_at_pt` **2026-08-25 18:15:11 PT**, version **1.4.1**). Live URL
https://dustycompiler.github.io/borealis-solana/ is verified after push.
Not a judge ranking. Do not inflate.

Scale: 0 missing · 3 present but misleading or thin · 4 honest and usable · 5 would survive a hostile grep.

| # | Rubric | Score | Evidence |
|---|---|---:|---|
| 1 | Live cluster TPS / slot / RPC | 4.8 | Live TPS ~4.2k, slot ~366 ms, getHealth path + publicnode fallback unit-tested. This run health **82** because delinquent stake ~1.45% (formula, not a freeze). Not 5.0: this run did not exercise the 429 fallback on the wire. |
| 2 | SOL 24h honesty | 4.6 | `(last − open) / open` from Coinbase this run (Gecko 429). Formula tested. Not 5.0: CoinGecko still 429s from shared IPs; headline confidence MED. |
| 3 | Health score 0–100 | 4.7 | Published 25/30/25/20 formula on page + tests. Live 82 matches delinquency ≥1% (slot still ~366 ms). |
| 4 | Exec view (network ≠ ecosystem) | 5.0 | This run: network **WATCH** (delinquency) + ecosystem **SURGE** (DEX +60%). DEX does not paint WATCH; WATCH is from an actual network flag. Test `test_dex_surge_is_healthy_plus_surge_not_watch` still holds on the quiet-slot fixture. |
| 5 | Anomalies on run 1 | 4.5 | Llama 1d/7d + 30d medians + z-scores. This run: protocol-fees 7d ALERT, high delinquency WARN, DEX 7d INFO, SOL vs 30d, TPS vs 30d, risk-off. Empty-strip copy exists. |
| 6 | Median tx fee | 4.6 | Live p50 0.000005 SOL, `window_seconds=9961` (~2.8h), `not_24h_census=true`, n_tx=2240 (≤160 txs/slot × 14 slots: 2 spot + 12 stratified). Tile subline **NOT a 24h census**. Not 5.0: still a stratified sample, not a 24h ledger (would need archive RPC). |
| 7 | Borealis REV | 4.6 | Live **$991.18K** = MEASURED in-protocol + ESTIMATED Jito tips. Llama protocol fees EXCLUDED. One-line sensitivity: p50 floor → ~$103K tips; p95 floor → ~$19.9M tips; headline uses p50. Tests assert llama is not summed and p95 is not the headline. **Gap:** no public no-key Jito 24h ledger — the p95 spread is the point. |
| 8 | Tokenized equities / RWA | 4.5 | Live RWA TVL **$2.06B**. Priced-subset mcap **$276.71M** (**80 of 715**, not 24). Public `/multiplier` **never fetched** (0 `xstocks.mult.*` rows). Jupiter 24h vol subset; **7d omitted** because Jupiter lite-api has no 7d stats and Llama `protocol/xstocks` has no volume series. Llama xStocks TVL **$430.26M** labeled liquidity, not mcap. **Gap:** 80/715 is still a lower bound (HTTP budget, extra names add almost no mcap); 7d equity volume is an external API hole. |
| 9 | SIMD-525 tracker | 4.6 | Primary source: solana.com/news “Lowering Slot Time and Validators Economic”. Heading uses listing token SIMD-525. Observed ~366 ms is **INFERRED corroboration**, not a feature-gate RPC. One short SIMD-025 correction, tiny, not a headline. **Gap:** no feature-gate / activation-slot RPC (by design this cycle). |
| 10 | Intelligence brief | 4.6 | 3–6 evidence-linked lines, no LLM. DEX-without-stress + priced-subset mcap called out. This run biggest risk is SOL/TVL, not DEX +60%. |
| 11 | Charts 24h/7d/30d/90d | 4.5 | SVG + range buttons; TVL 90d from Llama; TPS/SOL public feeds 30d. Tape n is still short. |
| 12 | Source · age · data-health | 4.7 | Live: `required sources 245/245 OK · 1 expected unavailable` (CoinGecko 429). **Zero** `xstocks.mult.*` rows — that route is not requested. Not 5.0: Gecko 429 from shared IPs is an external blocker. |
| 13 | Tests | 4.7 | **36** stdlib unittests, no network. Added multiplier-route skip, fee `window_seconds` + `not_24h_census` tile, Jito p50-vs-p95 sensitivity. DEX surge HEALTHY+SURGE still covered. Does not replay a full generate.py. |
| 14 | 15-min Action + live freshness | 4.8 | Cadence 15 min. Live Pages verified after this push for a new `generated_at`. |
| 15 | Stdlib, no keys | 5.0 | urllib + stdlib ThreadPoolExecutor. No Superteam submit this cycle. |

## Totals

- Categories: **15**
- Sum: **70.2**
- Mean: **4.68 / 5**
- Categories below 4.5: **none**. Thinnest is **8 Tokenized (4.5)** — coverage, not labeling.

## Remaining gaps (external blockers, not laziness)

1. **Median fee (4.6)** — ~2.8h stratified sample, loudly labeled. A true 24h fee tape needs an archive RPC or hours of getBlock; public RPC budget cannot census the ledger.
2. **REV (4.6)** — Jito tips remain ESTIMATED (`tip_floor × non-vote TPS × 86400`). No public no-key Jito 24h ledger. p50 vs p95 sensitivity is the honest range, not a second ledger.
3. **Tokenized / RWA (4.5)** — priced **80/715** without keys; `/multiplier` skipped. Extra names beyond the top ~24 barely move mcap. **7d tokenized volume** does not exist on Jupiter lite-api (stats5m/1h/6h/24h only) or DeFiLlama `protocol/xstocks` (TVL, not volume). Inventing 7×24h would be a lie.
4. **SIMD-525 (4.6)** — listing token cited from solana.com/news. Observed slot is corroboration. A feature-gate RPC is still not probed (this cycle treats it as inferred on purpose).
5. **CoinGecko 429** — shared CI/Pages IPs. Coinbase 24h is the working path. External.

## What this cycle did not claim

- Did not copy Heliostat/Orbit/Pulse code.
- Did not treat llama protocol fees as REV.
- Did not treat DEX surge as network WATCH.
- Did not treat 2022 status.solana.com outages as current.
- Did not call the xStocks `/multiplier` route.
- Did not present 80-name (or 24-name) mcap as a 715 census.
- Did not rename Llama xStocks TVL as mcap.
- Did not invent a Jito ledger or a 7d tokenized-volume series.
- Did not submit Superteam.
