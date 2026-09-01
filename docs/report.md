# Borealis — Solana ecosystem report

**Generated** 2026-09-01T03:06:59Z · 2026-08-31 20:06:59 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-01T03:06:50Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h +1.79%; DEX 24h $2.46B · 1d +27% · vs-7d-ago -18%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +27.37%. (threshold: `|1d %| >= 8`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 103.33 USD is +35.0% vs 30d median 76.57 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,317,399 |
| Block height | 421,365,005 |
| Block time | 2026-09-01T03:06:50Z |
| Epoch | 1,026 (19.77% · slot 85,403/432,000) |
| Mean TPS (last ~3,600s) | 3,788.5 |
| Mean non-vote TPS | 1,655.0 |
| Median TPS (same window) | 3,737.8 |
| Mean slot time | 317.4 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 543,978,235,716 |
| Circulating supply | 585,207,187 SOL |
| Total supply | 633,267,617 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 680 |
| Delinquent | 14 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 438,157,999 SOL |
| Delinquent stake | 43,820.70 SOL (0.010%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.17% / 35.44% |
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
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.22M SOL | 1.65% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.93M SOL | 1.58% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.50% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.11M SOL | 1.39% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.95M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.59M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 10651 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 2064720 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 531278 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 17743 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 166563 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1333645 slots
- `CpdzCVza…` · 212.44 SOL · commission 100% · lag 517048 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 558562 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 516942 slots
- `6pEtDovp…` · 131.86 SOL · commission 100% · lag 531326 slots
- `7G4Rfctw…` · 75.85 SOL · commission 100% · lag 555700 slots
- `DZKTNGR3…` · 48.61 SOL · commission 100% · lag 563242 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 347 | data/history.jsonl snapshot tape |
| TVL chart | 347 | data/history.jsonl snapshot tape |
| SOL chart | 346 | data/history.jsonl snapshot tape |
| history.jsonl rows | 347 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$701.13K** (6,613.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-30 |
| **Solana REV** | **7,967.3 SOL** / **$844.73K** | MEASURED UTC calendar day 2026-08-30: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-30 · UTC day 2026-08-30 · SOL-USD date 2026-08-30 |
| Jito tip-floor run-rate (NOT REV) | $105.29K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 105286 USD; at p95 floor → 14774969 USD. |
| Protocol fees 24h | $13.28M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9976 |
| p90 / p99 | 0.000013 / 0.000187 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.33 | coingecko.simple_price |
| 24h change | +1.79% | coingecko.simple_price |
| Market cap | $60.46B | coingecko.simple_price |
| 24h volume | $3.08B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.84B |
| TVL 1d / 7d / 30d | +0.47% / +1.77% / +23.72% |
| DEX volume 24h | $2.46B · 1d +27.37% · vs-7d-ago -17.97% |
| 7d DEX volume | $17.42B · -16.72% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $13.28M |
| Fees 1d / 7d | +7.87% / -8.48% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $939.21M | +28.29% |
| BisonFi | $232.85M | +26.20% |
| Orca DEX | $220.81M | +19.71% |
| Meteora DLMM | $149.33M | +4.67% |
| Raydium AMM | $137.94M | +35.06% |
| Manifest Trade | $132.18M | +35.07% |
| pump.fun | $98.91M | +7.92% |
| Axiom | $83.77M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.57B | +0.97% | +3.40% |
| Kamino Lend | Lending | $1.25B | +0.90% | +3.45% |
| Raydium AMM | Dexs | $1.12B | -2.23% | +4.37% |
| Jupiter Lend | Lending | $1.09B | +1.02% | -0.25% |
| Binance Staked SOL | Liquid Staking | $1.07B | +1.24% | +6.48% |
| Jito Liquid Staking | Liquid Staking | $1.04B | +0.95% | +5.15% |
| BlackRock BUIDL | RWA | $886.92M | +0.22% | +4.68% |
| Jupiter Perpetual Exchange | Derivatives | $763.02M | +0.63% | +0.21% |
| Jupiter Staked SOL | Liquid Staking | $534.32M | +1.01% | +4.98% |
| xStocks | RWA | $441.00M | +2.53% | +4.07% |

## Stablecoins

Solana circulating pegged-USD: **$15.73B**
(1d +0.05% · 7d -1.78%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.73B | -1.17% |
| USDT · Tether | $2.83B | -0.00% |
| USDGO · USDGO | $1.24B | -0.40% |
| USD1 · World Liberty Financial USD | $1.21B | +0.84% |
| BUIDL · BlackRock USD | $886.92M | +0.04% |
| PYUSD · PayPal USD | $774.25M | +11.75% |
| USDG · Global Dollar | $609.25M | -0.22% |
| USDe · Ethena USDe | $537.37M | +0.02% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 72 of 724 Solana-deployed listed symbols (multiplier ok 80/80; 724 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 724 · Solana deployments 724 · priced 72 · priced-subset mcap $288.30M (lower bound, not a census).
24h volume $20.60M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $441.00M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 72 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 724 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 724 unique underlyings among 724 Solana rows; not every tokenized equity on Solana). 724 of 724 listed xStocks have a Solana deployment (724 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.92M
- **xStocks** (RWA) — $441.00M
- **OnRe** (RWA) — $287.71M
- **Ondo Yield Assets** (RWA) — $180.02M
- **Hastra** (RWA) — $154.58M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $25.07M
- **Plume Vaults** (RWA) — $22.86M

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

- [JUST IN: Solana NFTs are now live on @Opensea

Explore collections like @Claynosaurz, @DegenApeAcademy, @SolanaMBS, @FamousFoxFed, @bodoggos, and more ⛵️](https://x.com/solana/status/2094558621082280091) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 22:51:04 GMT
- [RT by @solana: Kamino Earn is now accessible to every @grok user through PayBox.

Access Solana-native yield directly through AI.](https://x.com/kamino/status/2094497112478363825) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 18:46:40 GMT
- [Pinned: $100M TVL in four months. Hylo built leverage that survives corrections.

No margin call, no traditional liquidation, no overhead. When markets drop, the system rebalances. Leverage adjusts, positions survive.

Leverage belonged to professionals, @hylo_so hands it to everyone.](https://x.com/solana/status/2094485371816157426) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 18:00:00 GMT
- [ethereum:0x07f5b6823751c2e2cd4560f28af75ff887102241 is available in your favorite Solana apps 

@Raydium, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @fomo, @ArcherExchange_, @kamino_swap, @mayan and more

Verify the token address: https://tokens.xyz/pons?solana=poNSfquKq512ApeYjVghwViSun4x1MhCqHVH2Paq4jN](https://x.com/solana/status/2094460900266934681) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 16:22:46 GMT
- [BREAKING: ethereum:0x07f5b6823751c2e2cd4560f28af75ff887102241 is live on Solana via @sunrise](https://x.com/solana/status/2094460897603588396) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 16:22:45 GMT
- [You can buy anything on Solana through Grok with @PayBox and @moonpay](https://x.com/solana/status/2094457248873681133) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 16:08:15 GMT
- [RT by @solana: thinking about getting a Seeker?

today’s the last day to get 20% off, plus a free $50 pack rip from @Collector_Crypt for the first 5k purchases.

use code CARDS20 and pay with Solana Pay.

ends tonight.

https://store.solanamobile.com](https://x.com/solanamobile/status/2094427416202526970) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 14:09:43 GMT
- [RT by @solana: We crossed $100k in customer spend in August, x4 increase from July! 🎉

Followed by a 3x in number of orders, with leading categories being TCGs, hardware, and animal supplies.

Half of the purchases were managed by purchasing agents on @clawpumptech that shop Amazon & eBay with their trading fees, led by the success of @selfmadebySP3ND 🦞🛍️

Use SP3ND if you want to shop online with stables and without KYC.](https://x.com/SP3NDdotshop/status/2094432549770842136) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 14:30:07 GMT
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

- [JUST IN: Solana NFTs are now live on @Opensea

Explore collections like @Claynosaurz, @DegenApeAcademy, @SolanaMBS, @FamousFoxFed, @bodoggos, and more ⛵️](https://x.com/solana/status/2094558621082280091) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 22:51:04 GMT
- [RT by @solana: Kamino Earn is now accessible to every @grok user through PayBox.

Access Solana-native yield directly through AI.](https://x.com/kamino/status/2094497112478363825) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 18:46:40 GMT
- [Pinned: $100M TVL in four months. Hylo built leverage that survives corrections.

No margin call, no traditional liquidation, no overhead. When markets drop, the system rebalances. Leverage adjusts, positions survive.

Leverage belonged to professionals, @hylo_so hands it to everyone.](https://x.com/solana/status/2094485371816157426) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 18:00:00 GMT
- [ethereum:0x07f5b6823751c2e2cd4560f28af75ff887102241 is available in your favorite Solana apps 

@Raydium, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @fomo, @ArcherExchange_, @kamino_swap, @mayan and more

Verify the token address: https://tokens.xyz/pons?solana=poNSfquKq512ApeYjVghwViSun4x1MhCqHVH2Paq4jN](https://x.com/solana/status/2094460900266934681) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 16:22:46 GMT
- [BREAKING: ethereum:0x07f5b6823751c2e2cd4560f28af75ff887102241 is live on Solana via @sunrise](https://x.com/solana/status/2094460897603588396) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 16:22:45 GMT
- [You can buy anything on Solana through Grok with @PayBox and @moonpay](https://x.com/solana/status/2094457248873681133) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 16:08:15 GMT
- [RT by @solana: thinking about getting a Seeker?

today’s the last day to get 20% off, plus a free $50 pack rip from @Collector_Crypt for the first 5k purchases.

use code CARDS20 and pay with Solana Pay.

ends tonight.

https://store.solanamobile.com](https://x.com/solanamobile/status/2094427416202526970) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 14:09:43 GMT
- [RT by @solana: We crossed $100k in customer spend in August, x4 increase from July! 🎉

Followed by a 3x in number of orders, with leading categories being TCGs, hardware, and animal supplies.

Half of the purchases were managed by purchasing agents on @clawpumptech that shop Amazon & eBay with their trading fees, led by the success of @selfmadebySP3ND 🦞🛍️

Use SP3ND if you want to shop online with stables and without KYC.](https://x.com/SP3NDdotshop/status/2094432549770842136) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 14:30:07 GMT
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

_As of 2026-09-01 (2026-08-31 20:06:59 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~317 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~317 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **xStocks** — priced up to 80 of 724 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 722ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 533ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 722ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 525ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 571ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7310ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1157ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 147ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 64ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 81ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 39ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 34ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 520ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 86ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 235ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 59ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 94ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 247ms https://solana.com/data
- `solana.com.databricks` [ok] 200 1077ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 593ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 185ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 51ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 91ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 375ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 505ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 167ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 156ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 147ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 828ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2275ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1747ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 2212ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 246ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 551ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 637ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2822ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1979ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2843ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2681ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1961ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2990ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2170ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2656ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2405ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3000ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2106ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2265ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2092ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2789ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1810ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 4776ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1607ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1397ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1316ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1320ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1353ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1472ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.METAx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.NVDAx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.AAPLx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.AMZNx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.NVDAx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.GOOGLx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.MSFTx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.AAPLx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.SPYx` [ok] 200 849ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.mult.TSLAx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.DRAMx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.mult.MSFTx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.MVLLx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.QQQx` [ok] 200 567ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.COINx` [ok] 200 603ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.QQQx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 1376ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 1312ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 857ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.price.KORUx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.COINx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.INTWx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.mult.DRAMx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.price.SOXSx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.MUUx` [ok] 200 1176ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.mult.METAx` [ok] 200 656ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.INTWx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.DJTx` [ok] 200 606ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.MUUx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.BANKCx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.price.SNXXx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.SOXSx` [ok] 200 508ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.SNXXx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.SOXSx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.SNXXx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.MUUx` [ok] 200 622ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 851ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.price.AXTIx` [ok] 200 1753ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.mult.DJTx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.KUNLx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.AXTIx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 1163ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.CTINSx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 851ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.BANKCx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.KUNLx` [ok] 200 570ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 1191ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 1806ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 574ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 610ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 794ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.SZIGHx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.price.ENNHLx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.CRESBx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 586ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 526ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.CMERPx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 988ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 1063ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 526ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.CMERPx` [ok] 200 917ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 951ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.CRESMx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 635ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.WXXDCx` [ok] 200 1111ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.MIXUx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 529ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 878ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.MIXUx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 2206ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 3208ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.price.SITCx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.SITCx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 999ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 2212ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.SITCx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.ASMPTx` [ok] 200 1011ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.WHRFRx` [ok] 200 503ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 649ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.PRADx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.CLONPx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.CTFJWx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.SINOTx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 729ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.SINOx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 698ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 551ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 854ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.CTPCAx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.WHGROx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 1062ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.CLPHDx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 1670ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.CRESPx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 577ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 734ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.CLONPx` [ok] 200 1839ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 566ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.COVELx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.NONGx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.COVELx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 532ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.NONGx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 919ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.GENTEx` [ok] 200 1597ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.HKCGAx` [ok] 200 655ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.NONGx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 768ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.mult.CKINFx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.CHONGx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.price.MEITx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.mult.KUAIx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.GENTEx` [ok] 200 585ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.CKAHx` [ok] 200 851ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 727ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.POPMTx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.price.BOCOMx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.circ.POPMTx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.circ.BOCOMx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.price.MTRCPx` [ok] 200 858ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.COSCx` [ok] 200 617ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.POPMTx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 649ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 740ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.BOCOMx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 1524ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.PICCx` [ok] 200 741ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 41ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 353ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 73ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.HKEXCx` [ok] 200 96ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MEITx` [ok] 200 65ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.MIXUx` [ok] 200 60ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 72ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 69ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.CTINSx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=CTINSx
- `jito.tip_floor` [ok] 200 101ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 316ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 87ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 706ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 553ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 563ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 524ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 318ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
