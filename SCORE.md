# Borealis 1.4.0 — skeptical self-score

Scored 2026-08-25 **18:05 PT** (2026-08-26T01:05:00Z) against live
https://dustycompiler.github.io/borealis-solana/ (`generated_at_utc` **2026-08-26T01:03:25Z**,
`generated_at_pt` **2026-08-25 18:03:25 PT**, commit **fe724bb**).
Not a judge ranking. Do not inflate.

Scale: 0 missing · 3 present but misleading or thin · 4 honest and usable · 5 would survive a hostile grep.

| # | Rubric | Score | Evidence |
|---|---|---:|---|
| 1 | Live cluster TPS / slot / RPC | 4.8 | Live TPS ~4.2k, slot ~365 ms, getHealth ok, score 100. RPC 429 → publicnode is implemented and unit-tested. Not 5.0: this run did not exercise the fallback on the wire. |
| 2 | SOL 24h honesty | 4.6 | `(last − open) / open` from Coinbase this run (Gecko 429). Formula tested. Not 5.0: CoinGecko still 429s from shared IPs; headline confidence MED. |
| 3 | Health score 0–100 | 4.7 | Published 25/30/25/20 formula on page + tests. Live 100 matches quiet slot/delinquency. |
| 4 | Exec view (network ≠ ecosystem) | 5.0 | Live `<div class="verdict HEALTHY">` + ECOSYSTEM SURGE. DEX +66% does not paint WATCH. Biggest risk `None — no isolated adverse…`. Test `test_dex_surge_is_healthy_plus_surge_not_watch`. |
| 5 | Anomalies on run 1 | 4.5 | Llama 1d/7d + 30d medians + z-scores. This run: protocol-fees 7d ALERT, DEX 7d INFO, SOL vs 30d, TPS vs 30d. Empty-strip copy exists. |
| 6 | Median tx fee | 4.3 | Live p50 0.000005 SOL, `window_seconds=3340`, n_tx labeled. Time-stratified getBlock. **Gap:** still a ~55 min sample, not a 24h ledger. |
| 7 | Borealis REV | 4.4 | Live **$993.58K** = MEASURED in-protocol + ESTIMATED Jito tips. Llama protocol fees ~$14M shown EXCLUDED. Tests assert llama is not summed. **Gap:** Jito leg is floor × non-vote TPS, not a Jito ledger. |
| 8 | Tokenized equities / RWA | 4.2 | Live RWA TVL **$2.06B** (26 protocols). Priced-subset mcap **$276.42M** (24 of 715) + Jupiter vol subset. New labeled tile: xStocks protocol TVL **$430.26M** (DeFiLlama `protocol/xstocks`, liquidity, not mcap). Matches Heliostat’s $430M print without renaming it mcap. **Gap:** mcap is still 24 names; multiplier endpoint 400s every run; no 7d equity volume. |
| 9 | SIMD-525 tracker | 4.4 | Live heading uses listing token SIMD-525; 365 ms → 350 ms stage; one short SIMD-025 correction remains. **Gap:** stage is inferred from slot time, not a feature-gate RPC. |
| 10 | Intelligence brief | 4.6 | 3–6 evidence-linked lines, no LLM. DEX-without-stress + slot quiet + priced-subset mcap called out. |
| 11 | Charts 24h/7d/30d/90d | 4.5 | SVG + range buttons; TVL 90d from Llama; TPS/SOL public feeds 30d. Tape n is still short (~12). |
| 12 | Source · age · data-health | 4.1 | Live: `required sources 137/137 OK · 25 expected unavailable` + Gecko 429 note. Raw 162-row table still lists 24× `xstocks.mult.*` HTTP 400. **Gap:** we still *call* a known-400 multiplier route instead of skipping it. Old 108/132 headline is gone. |
| 13 | Tests | 4.5 | **33** stdlib unittests, no network. Added RPC 429 fallback, CoinGecko 429 → Coinbase, xStocks subset ≠ llama TVL. Does not replay a full generate.py. |
| 14 | 15-min Action + live freshness | 4.8 | Pages verified 2026-08-26T01:03:25Z (~2 min after push). Cadence 15 min. |
| 15 | Stdlib, no keys | 5.0 | urllib only. No Superteam submit this cycle. |

## Totals

- Categories: **15**
- Sum: **68.4**
- Mean: **4.56 / 5**
- Categories below 4.5: **6, 7, 8, 9, 12** (and 8 is the widest coverage gap)

## Remaining gaps (every category < 4.5)

1. **Median fee (4.3)** — `window_seconds≈3340` is labeled, but a judge can still read n_tx≈28k as a 24h census. Need a true 24h fee tape or a louder “not a 24h sum” next to the tile value.
2. **REV (4.4)** — Jito tips remain ESTIMATED (`tip_floor p50 × non-vote TPS × 86400`). No public no-key Jito 24h ledger.
3. **Tokenized / RWA (4.2)** — Heliostat-class **$430.26M** is now on the page as protocol TVL, but priced mcap is still **24/715**. Multiplier HTTP 400s are expected, not fixed. 7d tokenized volume still omitted.
4. **SIMD-525 (4.4)** — Observed-slot inference only. No feature-gate / activation-slot RPC.
5. **Data-health (4.1)** — Headline is honest; we still issue ~24 doomed `xstocks.mult` requests per run. Skip that route.

## What this cycle did not claim

- Did not copy Heliostat/Orbit/Pulse code.
- Did not treat llama protocol fees as REV.
- Did not treat DEX surge as network WATCH.
- Did not treat 2022 status.solana.com outages as current.
- Did not submit Superteam.
