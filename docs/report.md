# Borealis — Solana ecosystem report

**Generated** 2026-09-01T15:06:52Z · 2026-09-01 08:06:52 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-01T15:06:42Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -1.87%; DEX 24h $2.50B · 1d +30% · vs-7d-ago -17%; slot 320 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +9.69%. (threshold: `|1d %| >= 8`)
- **WARN · Last TPS sample outside 2.5σ of the 60-sample window** — Last sample 5,588 TPS is +2.69σ vs window mean 4,496 (n=60, σ=405). (threshold: `|last sample − window mean| > 2.5σ`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +29.63%. (threshold: `|1d %| >= 8`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 101.44 USD is +32.5% vs 30d median 76.57 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · TPS vs 30d median (solana.com/data tx/86400)** — Current 4,496.31 TPS is +22.2% vs 30d median 3,678.17 TPS (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,453,267 |
| Block height | 421,500,840 |
| Block time | 2026-09-01T15:06:42Z |
| Epoch | 1,026 (51.22% · slot 221,268/432,000) |
| Mean TPS (last ~3,600s) | 4,496.3 |
| Mean non-vote TPS | 2,381.8 |
| Median TPS (same window) | 4,441.5 |
| Mean slot time | 319.7 ms |
| Median slot time | 319.1 ms |
| Transaction count (cluster) | 544,141,400,787 |
| Circulating supply | 585,206,758 SOL |
| Total supply | 633,267,187 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 677 |
| Delinquent | 17 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 437,797,168 SOL |
| Delinquent stake | 404,651.44 SOL (0.092%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.19% / 35.47% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.17M SOL | 3.92% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.28M SOL | 3.72% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.43M SOL | 2.84% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.48M SOL | 2.62% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.46M SOL | 2.16% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.22M SOL | 1.65% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.93M SOL | 1.58% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.11M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.95M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.59M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `AHZxzLeR…` · 300.00K SOL · commission 100% · lag 126 slots
- `5t4shVsK…` · 50.38K SOL · commission 5% · lag 297 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 45328 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 2200588 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 104544 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 667146 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 153611 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 14628 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1469513 slots
- `CpdzCVza…` · 212.44 SOL · commission 100% · lag 652916 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 694430 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 652810 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 393 | data/history.jsonl snapshot tape |
| TVL chart | 393 | data/history.jsonl snapshot tape |
| SOL chart | 392 | data/history.jsonl snapshot tape |
| history.jsonl rows | 393 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$701.13K** (6,613.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-30 |
| **Solana REV** | **7,967.3 SOL** / **$844.73K** | MEASURED UTC calendar day 2026-08-30: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-30 · UTC day 2026-08-30 · SOL-USD date 2026-08-30 |
| Jito tip-floor run-rate (NOT REV) | $184.16K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 184161 USD; at p95 floor → 1600932 USD. |
| Protocol fees 24h | $13.50M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9945 |
| p90 / p99 | 0.000016 / 0.000375 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $101.44 | coingecko.simple_price |
| 24h change | -1.87% | coingecko.simple_price |
| Market cap | $59.36B | coingecko.simple_price |
| 24h volume | $2.97B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.78B |
| TVL 1d / 7d / 30d | -0.12% / +0.76% / +22.49% |
| DEX volume 24h | $2.50B · 1d +29.63% · vs-7d-ago -16.51% |
| 7d DEX volume | $17.68B · -15.50% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $13.50M |
| Fees 1d / 7d | +9.69% / -6.94% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $939.21M | +28.29% |
| BisonFi | $232.85M | +26.20% |
| Orca DEX | $220.52M | +19.56% |
| Manifest Trade | $149.34M | +52.61% |
| Meteora DLMM | $149.33M | +4.67% |
| Raydium AMM | $133.09M | +30.30% |
| Axiom | $113.58M | +35.58% |
| Jupiterz | $101.70M | +88.90% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.55B | -0.98% | +4.82% |
| Kamino Lend | Lending | $1.24B | -0.03% | +2.29% |
| Raydium AMM | Dexs | $1.11B | -0.40% | -0.44% |
| Jupiter Lend | Lending | $1.07B | -0.24% | -0.26% |
| Binance Staked SOL | Liquid Staking | $1.05B | -0.39% | +5.10% |
| Jito Liquid Staking | Liquid Staking | $1.02B | -0.91% | +3.99% |
| BlackRock BUIDL | RWA | $886.92M | +0.22% | +4.68% |
| Jupiter Perpetual Exchange | Derivatives | $754.94M | -0.63% | -0.56% |
| Jupiter Staked SOL | Liquid Staking | $526.97M | -2.15% | +3.34% |
| xStocks | RWA | $435.53M | +0.57% | +3.45% |

## Stablecoins

Solana circulating pegged-USD: **$15.66B**
(1d +0.05% · 7d -1.75%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.83B | +0.31% |
| USDT · Tether | $2.83B | -0.00% |
| USDGO · USDGO | $1.25B | -0.32% |
| USD1 · World Liberty Financial USD | $1.21B | +0.84% |
| BUIDL · BlackRock USD | $886.92M | +0.04% |
| PYUSD · PayPal USD | $774.39M | +11.79% |
| USDG · Global Dollar | $598.50M | -1.98% |
| USDe · Ethena USDe | $537.36M | +0.02% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 72 of 725 Solana-deployed listed symbols (multiplier ok 80/80; 725 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 725 · Solana deployments 725 · priced 72 · priced-subset mcap $285.60M (lower bound, not a census).
24h volume $28.08M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $435.53M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 72 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 725 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 725 unique underlyings among 725 Solana rows; not every tokenized equity on Solana). 725 of 725 listed xStocks have a Solana deployment (725 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.92M
- **xStocks** (RWA) — $435.53M
- **OnRe** (RWA) — $287.71M
- **Ondo Yield Assets** (RWA) — $179.63M
- **Hastra** (RWA) — $154.24M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $24.58M
- **Plume Vaults** (RWA) — $22.87M

## Daily active addresses

730,181 (Allium, as of 2026-08-30). Provider range 397,651–774,939. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [High-yield credit strategy from @Securitize is now usable as collateral on Solana through @Loopscale](https://x.com/solana/status/2094803259395330401) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 15:03:11 GMT
- [$GPRO is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2094802025834066189) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 14:58:17 GMT
- [GoPro ($GPRO) designs and sells action cameras and creator software, including the HERO and MAX lines, for sports, travel, and professional content production.

Verify the address on @tokens:
https://tokens.xyz/gpro?solana=GPRR2u6NS5yBQHWGauoJ9HXgjrTH8dDsrBfTV5zAYvDH](https://x.com/solana/status/2094802023669789098) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 14:58:16 GMT
- [BREAKING: $GPRO is live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2094802021111189880) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 14:58:16 GMT
- [RT by @solana: London is one of the best food cities on Earth 🤤

A city that offers an aggregation of global cuisines (we're ranked #4 best food-city in the world!)

You won't be short on options when you visit in November for Breakpoint 🍜](https://x.com/SuperteamUK/status/2094769899021201770) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 12:50:37 GMT
- [RT by @solana: $100k raised 

Bid now on @mallowdotart: https://nepal.mallow.art](https://x.com/solana/status/2094792998337093714) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 14:22:24 GMT
- [RT by @solana: The Green Candle Cup is live!

For the next 14 days, @Solana traders compete for $50,000 USDC in rewards.

Every competitor trades over @PhoenixTrade utilizes @triton_one's Shred Streaming powered by DoubleZero Edge, bringing high-performance data delivery directly into a trader’s stack.

The ultimate low-latency path of block data ↓](https://x.com/doublezero/status/2094787617178947666) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 14:01:01 GMT
- [RT by @solana: HINC is now live within @Loopscale's onchain credit markets on @solana.

Eligible users can put their HINC holdings to work as collateral to borrow USDG, accessing liquidity while continuing to hold their HINC position.](https://x.com/Securitize/status/2094772280882516288) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 13:00:05 GMT
- [We're removing floating-point math from Solana's core protocol. Layer by layer.

Layer one: SIMD-0391, activated on mainnet-beta at epoch 1026. It replaces all floating-point (floats) arithmetic in the Stake Program and validator client’s warmup and cooldown logic with fixed-point math.

Layer two: SIMD-0607, now proposed and in review. It targets the runtime itself, removing floats from the inflation rewards and rent calculation path.

Floats can round differently across different hardware, validator clients, and compilers, introducing the possibility of consensus divergence and liveness risk. SIMD-0391 and SIMD-0607 eliminates this by standardizing on fixed-point.

These two improvements aren't the end. Floating-point lives in other, less urgent paths that will transition to fixed-point eventually.](https://x.com/anza_xyz/status/2094509053687091401) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 31 Aug 2026 19:34:07 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [High-yield credit strategy from @Securitize is now usable as collateral on Solana through @Loopscale](https://x.com/solana/status/2094803259395330401) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 15:03:11 GMT
- [$GPRO is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2094802025834066189) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 14:58:17 GMT
- [GoPro ($GPRO) designs and sells action cameras and creator software, including the HERO and MAX lines, for sports, travel, and professional content production.

Verify the address on @tokens:
https://tokens.xyz/gpro?solana=GPRR2u6NS5yBQHWGauoJ9HXgjrTH8dDsrBfTV5zAYvDH](https://x.com/solana/status/2094802023669789098) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 14:58:16 GMT
- [BREAKING: $GPRO is live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2094802021111189880) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 14:58:16 GMT
- [RT by @solana: London is one of the best food cities on Earth 🤤

A city that offers an aggregation of global cuisines (we're ranked #4 best food-city in the world!)

You won't be short on options when you visit in November for Breakpoint 🍜](https://x.com/SuperteamUK/status/2094769899021201770) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 12:50:37 GMT
- [RT by @solana: $100k raised 

Bid now on @mallowdotart: https://nepal.mallow.art](https://x.com/solana/status/2094792998337093714) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 14:22:24 GMT
- [RT by @solana: The Green Candle Cup is live!

For the next 14 days, @Solana traders compete for $50,000 USDC in rewards.

Every competitor trades over @PhoenixTrade utilizes @triton_one's Shred Streaming powered by DoubleZero Edge, bringing high-performance data delivery directly into a trader’s stack.

The ultimate low-latency path of block data ↓](https://x.com/doublezero/status/2094787617178947666) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 14:01:01 GMT
- [RT by @solana: HINC is now live within @Loopscale's onchain credit markets on @solana.

Eligible users can put their HINC holdings to work as collateral to borrow USDG, accessing liquidity while continuing to hold their HINC position.](https://x.com/Securitize/status/2094772280882516288) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 13:00:05 GMT
- [We're removing floating-point math from Solana's core protocol. Layer by layer.

Layer one: SIMD-0391, activated on mainnet-beta at epoch 1026. It replaces all floating-point (floats) arithmetic in the Stake Program and validator client’s warmup and cooldown logic with fixed-point math.

Layer two: SIMD-0607, now proposed and in review. It targets the runtime itself, removing floats from the inflation rewards and rent calculation path.

Floats can round differently across different hardware, validator clients, and compilers, introducing the possibility of consensus divergence and liveness risk. SIMD-0391 and SIMD-0607 eliminates this by standardizing on fixed-point.

These two improvements aren't the end. Floating-point lives in other, less urgent paths that will transition to fixed-point eventually.](https://x.com/anza_xyz/status/2094509053687091401) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 31 Aug 2026 19:34:07 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-01 (2026-09-01 08:06:52 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~320 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~320 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **xStocks** — priced up to 80 of 725 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 218ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 113ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 112ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 135ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 121ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5736ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 361ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 221ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 102ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 98ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 38ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 55ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1374ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 127ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 96ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 89ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 98ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 544ms https://solana.com/data
- `solana.com.databricks` [ok] 200 122ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 677ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 207ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 213ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 88ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 537ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 919ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 508ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 442ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 452ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 418ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2582ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1262ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1281ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 209ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 126ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 118ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 638ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 691ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 591ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 602ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 679ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 737ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 584ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 737ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 755ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 702ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 762ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 694ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 710ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 622ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2072ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1110ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 4734ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 3575ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1573ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1071ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 3289ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 2619ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AMZNx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.AAPLx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.SPYx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.MSFTx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.AMZNx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.NVDAx` [ok] 200 598ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.METAx` [ok] 200 818ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.GOOGLx` [ok] 200 836ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.NVDAx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 615ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 632ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.GOOGLx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 594ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.MVLLx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.circ.METAx` [ok] 200 749ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 865ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 641ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.QQQx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.MUUx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.circ.MVLLx` [ok] 200 484ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 1052ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.price.TSLAx` [ok] 200 2460ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.MUUx` [ok] 200 550ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 490ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.circ.COINx` [ok] 200 908ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.KORUx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.METAx` [ok] 200 1115ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.MUUx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.price.SNXXx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.price.INTWx` [ok] 200 640ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.SHEINx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.TSLAx` [ok] 200 693ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 953ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.mult.KORUx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.mult.AXTIx` [ok] 200 601ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.SHEINx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.SNXXx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.TSLAx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.DJTx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.price.SOXSx` [ok] 200 1044ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.mult.SHEINx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.DJTx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.circ.SOXSx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.INTWx` [ok] 200 1046ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 1053ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 772ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.LAOPGx` [ok] 200 685ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 1387ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.INTWx` [ok] 200 702ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 600ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.SOXSx` [ok] 200 1041ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.price.KUNLx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 712ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.BANKCx` [ok] 200 1788ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 740ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.MMGx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [ok] 200 645ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 934ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.price.SNBIOx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.HAIDLx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 691ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 904ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 736ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 740ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 859ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.CMERPx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.CRESBx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 698ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 427ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 1499ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.CMERPx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.WXXDCx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.CSPCx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 963ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.CMENDx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.WXXDCx` [ok] 200 635ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.CMENDx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 2177ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 406ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 3172ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 2844ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 1076ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.SITCx` [ok] 200 923ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 756ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 2170ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 870ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.SNDSCx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 508ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.SINOTx` [ok] 200 400ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.WHGROx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.CRESPx` [ok] 200 428ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 820ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.CLPHDx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.CTFJWx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 544ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 882ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.PWAHLx` [ok] 200 482ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 853ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.GENTEx` [ok] 200 780ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.SWPRPx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.SINOx` [ok] 200 528ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 1225ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.CKINFx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 422ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.HKEXCx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.mult.HKEXCx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 1602ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 919ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.price.CKAHx` [ok] 200 1247ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.CHONGx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.CKAHx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.mult.KUAIx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 622ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.GEELx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.CHONGx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.price.PICCx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.GEELx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.COVELx` [ok] 200 1389ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.GENTEx` [ok] 200 2283ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.HNDLDx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.MTRCPx` [ok] 200 707ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.POPMTx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.circ.CKHUTx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 2022ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.MEITx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.COVELx` [ok] 200 1191ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 1592ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.POPMTx` [ok] 200 1317ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 888ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.POPMTx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 62ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 258ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 130ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 121ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 126ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 116ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 125ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 121ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.CTINSx` [ok] 200 126ms https://lite-api.jup.ag/tokens/v2/search?query=CTINSx
- `jup.tokens.search.KUNLx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jito.tip_floor` [ok] 200 643ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 364ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 159ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 120ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 140ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 140ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 124ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 210ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
