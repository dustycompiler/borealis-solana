# Borealis — Solana ecosystem report

**Generated** 2026-08-31T10:33:58Z · 2026-08-31 03:33:58 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-31T10:33:48Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -1.98%; DEX 24h $1.87B · 1d +12% · vs-7d-ago -36%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -36.38%. (threshold: `|7d %| >= 20`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +11.91%. (threshold: `|1d %| >= 8`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 102.81 USD is +34.6% vs 30d median 76.37 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,129,692 |
| Block height | 421,177,368 |
| Block time | 2026-08-31T10:33:48Z |
| Epoch | 1,025 (76.32% · slot 329,694/432,000) |
| Mean TPS (last ~3,600s) | 3,505.5 |
| Mean non-vote TPS | 1,365.4 |
| Median TPS (same window) | 3,469.3 |
| Mean slot time | 315.9 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 543,732,206,049 |
| Circulating supply | 585,121,181 SOL |
| Total supply | 633,172,864 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 679 |
| Delinquent | 18 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 437,082,504 SOL |
| Delinquent stake | 45,385.49 SOL (0.010%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.26% / 35.54% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.20M SOL | 3.94% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.09M SOL | 3.68% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.39M SOL | 2.83% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.48M SOL | 2.63% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.45M SOL | 2.16% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.13% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.02M SOL | 2.06% | 10% | 0 |
| 8 | `9eGrDohd…` | 7.30M SOL | 1.67% | 5% | 0 |
| 9 | `EvnRmnMr…` | 7.20M SOL | 1.65% | 7% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.11M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.60M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `mrgn4atx…` · 21.79K SOL · commission 0% · lag 147909 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1877013 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 343571 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 210267 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 449854 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1145938 slots
- `CpdzCVza…` · 315.26 SOL · commission 100% · lag 329341 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 370855 slots
- `HFTcVVrX…` · 152.80 SOL · commission 100% · lag 329235 slots
- `6pEtDovp…` · 131.96 SOL · commission 100% · lag 343619 slots
- `7G4Rfctw…` · 75.85 SOL · commission 100% · lag 367993 slots
- `DZKTNGR3…` · 48.61 SOL · commission 100% · lag 375535 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 282 | data/history.jsonl snapshot tape |
| TVL chart | 282 | data/history.jsonl snapshot tape |
| SOL chart | 281 | data/history.jsonl snapshot tape |
| history.jsonl rows | 282 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$814.10K** (7,855.5 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-29 |
| **Solana REV** | **9,341.6 SOL** / **$968.12K** | MEASURED UTC calendar day 2026-08-29: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-29 · UTC day 2026-08-29 · SOL-USD date 2026-08-29 |
| Jito tip-floor run-rate (NOT REV) | $12.42K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 12420 USD; at p95 floor → 7665466 USD. |
| Protocol fees 24h | $12.01M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2080 window_seconds=9980 |
| p90 / p99 | 0.000010 / 0.000103 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $102.81 | coingecko.simple_price |
| 24h change | -1.98% | coingecko.simple_price |
| Market cap | $60.15B | coingecko.simple_price |
| 24h volume | $3.70B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.81B |
| TVL 1d / 7d / 30d | -1.74% / +4.44% / +22.24% |
| DEX volume 24h | $1.87B · 1d +11.91% · vs-7d-ago -36.38% |
| 7d DEX volume | $17.96B · -7.42% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $12.01M |
| Fees 1d / 7d | +7.12% / -5.28% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $732.11M | +25.20% |
| Orca DEX | $247.90M | +70.57% |
| BisonFi | $184.51M | +23.11% |
| Meteora DLMM | $142.67M | -0.21% |
| Manifest Trade | $122.59M | +41.36% |
| Raydium AMM | $114.41M | -6.30% |
| Axiom | $103.65M | 0.00% |
| pump.fun | $91.65M | -16.74% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.56B | -2.12% | +10.38% |
| Kamino Lend | Lending | $1.25B | -0.63% | +5.66% |
| Raydium AMM | Dexs | $1.11B | -1.92% | +6.86% |
| Jupiter Lend | Lending | $1.08B | -1.61% | +1.77% |
| Binance Staked SOL | Liquid Staking | $1.06B | -2.04% | +9.89% |
| Jito Liquid Staking | Liquid Staking | $1.03B | -2.27% | +8.42% |
| BlackRock BUIDL | RWA | $886.54M | 0.00% | +6.05% |
| Jupiter Perpetual Exchange | Derivatives | $759.79M | -1.37% | +2.18% |
| Jupiter Staked SOL | Liquid Staking | $531.10M | -2.17% | +8.17% |
| xStocks | RWA | $432.38M | +2.36% | +3.57% |

## Stablecoins

Solana circulating pegged-USD: **$15.79B**
(1d -1.08% · 7d -2.04%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.86B | -1.92% |
| USDT · Tether | $2.83B | -0.00% |
| USDGO · USDGO | $1.24B | -0.40% |
| USD1 · World Liberty Financial USD | $1.21B | +2.55% |
| BUIDL · BlackRock USD | $886.54M | 0.00% |
| PYUSD · PayPal USD | $693.92M | -0.08% |
| USDG · Global Dollar | $608.50M | -0.97% |
| USDe · Ethena USDe | $537.38M | +0.55% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 80 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 80 · priced-subset mcap $284.97M (lower bound, not a census).
24h volume $12.27M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $432.38M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 80 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.54M
- **xStocks** (RWA) — $432.38M
- **OnRe** (RWA) — $284.92M
- **Ondo Yield Assets** (RWA) — $179.96M
- **Hastra** (RWA) — $154.87M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $24.74M
- **Plume Vaults** (RWA) — $22.86M

## Daily active addresses

741,873 (Allium, as of 2026-08-29). Provider range 419,515–768,976. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

## Public Dune embed

External Reference — public third-party Dune dashboard, not a Borealis query — Solana On-Chain Health & Activity Explorer (cryptoonchain)
Embed: https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
Dashboard: https://dune.com/cryptoonchain/solana-explorer
HTTP 200 · included: yes

## Status & news

**status.solana.com:** All Systems Operational (indicator `none`)

Recency is applied **after** RSS merge. Historic status.solana.com incidents (2022–2024) are archive, not current.

### Active incidents

- None open.

### Recently resolved

- None in the recency window.

### Current news

- [RT by @anza_xyz: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`
- [7/
Solana's first stake-weighted vote drew participation from hundreds of millions of SOL on each proposal, well above the one-third quorum.

Proposals: https://governance.solana.com

SIMD-0550: https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0550-double-disinflation.md

SIMD-0607: https://github.com/solana-foundation/solana-improvement-documents/pull/607](https://x.com/anza_xyz/status/2093445419502272913) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:37 GMT `upgrade`
- [6/
SGP-0003  ❌ did not pass and would have split the base fee into an inclusion fee for leaders plus a resource fee scaling with usage.

Restructuring fees changes revenue for validators and cost modeling for every app. Most non-passing stake abstained rather than opposed.

Majority support on a first attempt is a strong starting point and we can expect a reparameterized version to return for a vote.](https://x.com/anza_xyz/status/2093445282910601403) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:04 GMT
- [5/
When SIMD-0550 activates, every validator computes staking rewards on the new schedule.

Rewards math must be bit-for-bit identical across Agave and Firedancer. Floating point can't guarantee that, so SIMD-0607 replaces it with deterministic integer math, targeting Agave v4.4.](https://x.com/anza_xyz/status/2093445181974716831) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:06:40 GMT `upgrade`
- [4/
So when does it activate?

The implementation of SIMD-0550 is a single permanent feature gate that sets the taper to 0.30.

One prerequisite is in review, then the gate can be scheduled.](https://x.com/anza_xyz/status/2093445089356136470) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:06:18 GMT `upgrade`
- [3/
SGP-0002 ✅ doubles the annual disinflation rate from 15% to 30%.

Terminal rate stays 1.5% and arrives earlier in the year 2029 instead of 2032. Roughly 18.9M fewer SOL issued over six years.](https://x.com/anza_xyz/status/2093444975665217621) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:05:51 GMT
- [2/
SGP-0001 ✅ ratifies the Solana Constitution.

Stake-weighted voting is now the formal process for network decisions. Validators vote with active stake. Delegators can override their validator directly.](https://x.com/anza_xyz/status/2093444899446415842) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:05:33 GMT
- [We love our bread
We love our butter
But most of all
We love @solana](https://x.com/solana_devs/status/2094191210005156325) — X/Nitter-style RSS @solana_devs (not Twitter API) · Sun, 30 Aug 2026 22:31:07 GMT
- [21 founders. 2 minutes each.

@colosseum Demo Day. August 26, 2026.](https://x.com/solana_devs/status/2094112001517580707) — X/Nitter-style RSS @solana_devs (not Twitter API) · Sun, 30 Aug 2026 17:16:22 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @anza_xyz: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`
- [7/
Solana's first stake-weighted vote drew participation from hundreds of millions of SOL on each proposal, well above the one-third quorum.

Proposals: https://governance.solana.com

SIMD-0550: https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0550-double-disinflation.md

SIMD-0607: https://github.com/solana-foundation/solana-improvement-documents/pull/607](https://x.com/anza_xyz/status/2093445419502272913) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:37 GMT `upgrade`
- [6/
SGP-0003  ❌ did not pass and would have split the base fee into an inclusion fee for leaders plus a resource fee scaling with usage.

Restructuring fees changes revenue for validators and cost modeling for every app. Most non-passing stake abstained rather than opposed.

Majority support on a first attempt is a strong starting point and we can expect a reparameterized version to return for a vote.](https://x.com/anza_xyz/status/2093445282910601403) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:04 GMT
- [5/
When SIMD-0550 activates, every validator computes staking rewards on the new schedule.

Rewards math must be bit-for-bit identical across Agave and Firedancer. Floating point can't guarantee that, so SIMD-0607 replaces it with deterministic integer math, targeting Agave v4.4.](https://x.com/anza_xyz/status/2093445181974716831) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:06:40 GMT `upgrade`
- [4/
So when does it activate?

The implementation of SIMD-0550 is a single permanent feature gate that sets the taper to 0.30.

One prerequisite is in review, then the gate can be scheduled.](https://x.com/anza_xyz/status/2093445089356136470) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:06:18 GMT `upgrade`
- [3/
SGP-0002 ✅ doubles the annual disinflation rate from 15% to 30%.

Terminal rate stays 1.5% and arrives earlier in the year 2029 instead of 2032. Roughly 18.9M fewer SOL issued over six years.](https://x.com/anza_xyz/status/2093444975665217621) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:05:51 GMT
- [2/
SGP-0001 ✅ ratifies the Solana Constitution.

Stake-weighted voting is now the formal process for network decisions. Validators vote with active stake. Delegators can override their validator directly.](https://x.com/anza_xyz/status/2093444899446415842) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:05:33 GMT
- [We love our bread
We love our butter
But most of all
We love @solana](https://x.com/solana_devs/status/2094191210005156325) — X/Nitter-style RSS @solana_devs (not Twitter API) · Sun, 30 Aug 2026 22:31:07 GMT
- [21 founders. 2 minutes each.

@colosseum Demo Day. August 26, 2026.](https://x.com/solana_devs/status/2094112001517580707) — X/Nitter-style RSS @solana_devs (not Twitter API) · Sun, 30 Aug 2026 17:16:22 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-31 (2026-08-31 03:33:58 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~316 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

_Listing token SIMD-525 is SIMD-0525. Not SIMD-025._

- **SIMD-525** — Reduce Slot Times (400→350→300→250→200 ms)
- **SIMD-0326** — Alpenglow Consensus Protocol (Votor)
- **SIMD-0337** — Markers for Alpenglow Fast Leader Handover
- **SIMD-0357** — Alpenglow Validator Admission Ticket (VAT)
- **SIMD-0384** — Alpenglow Migration
- **SIMD-0387** — BLS Pubkey Management in Vote Account

### Public timeline (editorial)

- `2026-08-20` — Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.”
- `source` — solana.com/news “Lowering Slot Time and Validators Economic” remains a listing-token write-up for SIMD-525 (SIMD-0525).
- `2026-05-01` — SIMD-0525 created (Anza). Four feature gates: 350/300/250/200 ms.
- `on-chain` — On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending.
- `observed` — Observed mean slot ~316 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
- `2026-07-08` — SIMD-0387 (BLS pubkey in vote account) activated on mainnet.
- `2026-07-22` — SIMD-0357 VAT activated. VAT does not itself turn on Alpenglow consensus.

### What to watch

- Whether the 300 ms gate (effective epoch 1024 when activated at epoch-1023 start) is live once that epoch starts.
- Skip rate / skipped slots as later 50 ms steps (250/200) get Feature accounts on mainnet.
- Do not treat observed slot ms as activation proof.
- Firedancer / Frankendancer Votor parity before a full Alpenswitch.

- https://solana.com/news/solana-changelog-august-20-2026
- https://solana.com/news/lowering-slot-time-and-validators-economic
- https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0525-reduce-slot-times.md
- https://solana.com/upgrades/reduced-slot-times
- https://solana.com/upgrades/alpenglow
- https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0326-alpenglow.md

## Omissions

- **xStocks** — priced up to 80 of 715 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 303ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 301ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 268ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 365ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 301ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6736ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 561ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 31ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 55ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 58ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 35ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 25ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 28ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 82ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 41ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 45ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 71ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 639ms https://solana.com/data
- `solana.com.databricks` [ok] 200 52ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 544ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 172ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 30ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 54ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 260ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 371ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 87ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 83ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 72ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [FAIL] 404 1190ms https://nitter.perennialte.ch/solana/rss — HTTP 404 Not Found
- `rss.nitter.solana_status` [ok] 200 1879ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1325ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1923ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 150ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 92ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 286ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 351ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1031ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 837ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1280ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1227ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1299ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 268ms https://api.mainnet-beta.solana.com — {'code': -32007, 'message': 'Slot 443106031 was skipped, or missing due to ledger jump to recent snapshot'}
- `rpc.getBlock.fallback` [FAIL] 200 46ms https://solana-rpc.publicnode.com — {'code': -32007, 'message': 'Slot 443106031 was skipped, or missing due to ledger jump to recent snapshot'}
- `rpc.getBlock` [ok] 200 1131ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1210ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1097ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1206ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1467ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1043ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1042ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1215ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1227ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1347ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1363ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1267ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1100ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1283ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1256ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.METAx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.NVDAx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.AAPLx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.METAx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.price.MSFTx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.TSLAx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.GOOGLx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.SPYx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.mult.METAx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.TSLAx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.MSFTx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.BANKCx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.NVDAx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 406ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.AMZNx` [ok] 200 1034ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.mult.SPYx` [ok] 200 609ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.BANKCx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.AMZNx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.SUOPTx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.MMGx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 730ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.MMGx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.WRFHDx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.JDLOGx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.SNBIOx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.MMGx` [ok] 200 543ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 637ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [ok] 200 882ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 916ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.HRZRBx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.KUNLx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.KUNLx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 578ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.CMERPx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 640ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.CRESMx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 982ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.SMOIHx` [ok] 200 1073ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.mult.CRESMx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 906ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.BDWAPx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.JTGEXx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.CRESBx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.CMENDx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.mult.CMENDx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.ASMPTx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.SNDSCx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.MIXUx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.SITCx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.mult.CRESPx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.PRADx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 770ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.price.SINOTx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 640ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.SINOx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.SINOx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 672ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.WHRFRx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.CRAUTx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.GENTEx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.CKINFx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.CKAHx` [ok] 200 111ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.SWPRPx` [ok] 200 607ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 650ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.price.COVELx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.CHONGx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.mult.KUAIx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.CHONGx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 870ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 411ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.mult.HKEXCx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.MEITx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.circ.COVELx` [ok] 200 525ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.MTRCPx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.POPMTx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.price.BOCOMx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.mult.NONGx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.HNDLDx` [ok] 200 664ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.POPMTx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.HNDLDx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.price.CPETCx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.price.BOCHKx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.price.CITICx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.circ.CPETCx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.price.GEELx` [ok] 200 1257ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.BOCOMx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.circ.BOCHKx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.POPMTx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.mult.COVELx` [ok] 200 993ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.BOCOMx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.circ.CITICx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.mult.CPETCx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 784ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.price.ANTASx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.price.CRESLx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.price.HAIERx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.mult.GEELx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.CITICx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.price.PSBOCx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.circ.CRESLx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.circ.HAIERx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.price.ICBCx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.circ.ANTASx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.circ.PSBOCx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.mult.BOCHKx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.circ.ICBCx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.mult.PSBOCx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `xstocks.mult.ICBCx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `xstocks.mult.CRESLx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.mult.ANTASx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.price.ZJGLDx` [ok] 200 778ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.circ.ZJGLDx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.mult.ZJGLDx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.mult.HAIERx` [ok] 200 1518ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1102ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 143ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 39ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 40ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 37ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 39ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 47ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 39ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.CPETCx` [ok] 200 43ms https://lite-api.jup.ag/tokens/v2/search?query=CPETCx
- `jup.tokens.search.KUNLx` [ok] 200 40ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jito.tip_floor` [ok] 200 366ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 322ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 52ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 271ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 268ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 272ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 276ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 83ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
