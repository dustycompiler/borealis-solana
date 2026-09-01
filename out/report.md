# Borealis — Solana ecosystem report

**Generated** 2026-09-01T05:06:22Z · 2026-08-31 22:06:22 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-01T05:06:12Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h +2.21%; DEX 24h $2.46B · 1d +27% · vs-7d-ago -18%; slot 318 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · SOL price vs 30d median (solana.com/data)** — Current 103.82 USD is +35.6% vs 30d median 76.57 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +27.37%. (threshold: `|1d %| >= 8`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,339,966 |
| Block height | 421,387,568 |
| Block time | 2026-09-01T05:06:12Z |
| Epoch | 1,026 (24.99% · slot 107,970/432,000) |
| Mean TPS (last ~3,600s) | 3,813.7 |
| Mean non-vote TPS | 1,681.0 |
| Median TPS (same window) | 3,795.2 |
| Mean slot time | 317.8 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 544,005,574,232 |
| Circulating supply | 585,207,116 SOL |
| Total supply | 633,267,545 SOL |
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

- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 346 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 2087287 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 553845 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 40310 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 189130 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1356212 slots
- `CpdzCVza…` · 212.44 SOL · commission 100% · lag 539615 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 581129 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 539509 slots
- `6pEtDovp…` · 131.86 SOL · commission 100% · lag 553893 slots
- `7G4Rfctw…` · 75.85 SOL · commission 100% · lag 578267 slots
- `DZKTNGR3…` · 48.61 SOL · commission 100% · lag 585809 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 355 | data/history.jsonl snapshot tape |
| TVL chart | 355 | data/history.jsonl snapshot tape |
| SOL chart | 354 | data/history.jsonl snapshot tape |
| history.jsonl rows | 355 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$701.13K** (6,613.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-30 |
| **Solana REV** | **7,967.3 SOL** / **$844.73K** | MEASURED UTC calendar day 2026-08-30: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-30 · UTC day 2026-08-30 · SOL-USD date 2026-08-30 |
| Jito tip-floor run-rate (NOT REV) | $56.95K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 56951 USD; at p95 floor → 15078421 USD. |
| Protocol fees 24h | $13.29M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9953 |
| p90 / p99 | 0.000011 / 0.000116 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.82 | coingecko.simple_price |
| 24h change | +2.21% | coingecko.simple_price |
| Market cap | $60.76B | coingecko.simple_price |
| 24h volume | $3.01B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.83B |
| TVL 1d / 7d / 30d | +0.74% / +1.69% / +23.63% |
| DEX volume 24h | $2.46B · 1d +27.37% · vs-7d-ago -17.97% |
| 7d DEX volume | $17.42B · -16.72% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $13.29M |
| Fees 1d / 7d | +7.96% / -8.41% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $939.21M | +28.29% |
| BisonFi | $232.85M | +26.20% |
| Orca DEX | $220.81M | +19.71% |
| Meteora DLMM | $149.33M | +4.67% |
| Manifest Trade | $141.66M | +44.77% |
| Raydium AMM | $130.55M | +27.82% |
| pump.fun | $98.91M | +7.92% |
| Axiom | $83.77M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.58B | +2.01% | +3.87% |
| Kamino Lend | Lending | $1.25B | +0.78% | +1.30% |
| Raydium AMM | Dexs | $1.11B | +1.63% | +4.20% |
| Jupiter Lend | Lending | $1.08B | +0.86% | -2.67% |
| Binance Staked SOL | Liquid Staking | $1.07B | +1.73% | +2.97% |
| Jito Liquid Staking | Liquid Staking | $1.04B | +1.11% | +1.18% |
| BlackRock BUIDL | RWA | $886.92M | +0.22% | +4.68% |
| Jupiter Perpetual Exchange | Derivatives | $761.86M | +0.48% | -1.86% |
| Jupiter Staked SOL | Liquid Staking | $534.42M | +1.19% | +2.44% |
| xStocks | RWA | $441.71M | +2.87% | +3.83% |

## Stablecoins

Solana circulating pegged-USD: **$15.79B**
(1d +0.05% · 7d -1.78%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.78B | -0.31% |
| USDT · Tether | $2.83B | -0.00% |
| USDGO · USDGO | $1.24B | -0.40% |
| USD1 · World Liberty Financial USD | $1.21B | +0.84% |
| BUIDL · BlackRock USD | $886.92M | +0.04% |
| PYUSD · PayPal USD | $774.22M | +11.75% |
| USDG · Global Dollar | $608.74M | -0.30% |
| USDe · Ethena USDe | $537.30M | +0.02% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 71 of 725 Solana-deployed listed symbols (multiplier ok 80/80; 725 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 725 · Solana deployments 725 · priced 71 · priced-subset mcap $288.41M (lower bound, not a census).
24h volume $22.12M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $441.71M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 71 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 725 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 725 unique underlyings among 725 Solana rows; not every tokenized equity on Solana). 725 of 725 listed xStocks have a Solana deployment (725 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.92M
- **xStocks** (RWA) — $441.71M
- **OnRe** (RWA) — $287.71M
- **Ondo Yield Assets** (RWA) — $179.73M
- **Hastra** (RWA) — $154.58M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $24.96M
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

- [RT by @solana: MetaDAO is rebuilding venture capital for the internet.

Check out our new website to learn more https://metadao.fi](https://x.com/MetaDAOProject/status/2094562367912992986) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 23:05:58 GMT
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

- [RT by @solana: MetaDAO is rebuilding venture capital for the internet.

Check out our new website to learn more https://metadao.fi](https://x.com/MetaDAOProject/status/2094562367912992986) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 23:05:58 GMT
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

_As of 2026-09-01 (2026-08-31 22:06:22 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~318 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~318 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 839ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 783ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 724ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 707ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 718ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7485ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1480ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 33ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 133ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 61ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 27ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 40ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1017ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 68ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 175ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 47ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 99ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 260ms https://solana.com/data
- `solana.com.databricks` [ok] 200 78ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 353ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 83ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 186ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 196ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 253ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 491ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 157ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 166ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 159ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 2119ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1591ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1305ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 2477ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 133ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 703ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 845ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3085ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3098ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2911ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3246ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2955ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2827ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3031ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2765ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3431ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2707ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2782ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2797ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2951ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3072ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 3114ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1710ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1126ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 3949ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 3698ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2128ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1567ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1194ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.SPYx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.TSLAx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.AAPLx` [ok] 200 482ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.SPYx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 639ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.mult.SPYx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.GOOGLx` [ok] 200 749ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.MSFTx` [ok] 200 870ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.TSLAx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.MSFTx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 769ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.METAx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.mult.COINx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.MVLLx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 1195ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 1057ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.MUUx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.mult.MSFTx` [ok] 200 1155ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.price.AXTIx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.AMZNx` [ok] 200 2484ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.mult.QQQx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.KORUx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.price.DJTx` [ok] 200 775ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.DRAMx` [ok] 200 1363ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.NVDAx` [ok] 200 3093ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.DJTx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.MUUx` [ok] 200 1006ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 1005ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 999ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 796ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.INTWx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.SNXXx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.mult.DJTx` [ok] 200 678ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.circ.SNXXx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 1033ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.NVDAx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 1914ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.SHEINx` [ok] 200 513ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.mult.AXTIx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.BANKCx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.SOXSx` [ok] 200 1037ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.MMGx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.MMGx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 507ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.circ.SOXSx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.mult.SHEINx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.price.JDLOGx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 1527ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.MVLLx` [ok] 200 3618ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.CTINSx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.MVLLx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 1345ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.HAIDLx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.SNXXx` [ok] 200 1853ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 1238ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 811ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 1081ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 963ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 1165ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 582ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 1093ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.CMERPx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [ok] 200 606ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 957ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.CRESBx` [ok] 200 736ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.WXXDCx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.HRZRBx` [ok] 200 1206ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 1935ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 742ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 835ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.CSPCx` [ok] 200 943ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.CRESMx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 522ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 662ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.SNDSCx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.SITCx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.JDHLTx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 959ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.CRESPx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.SNDSCx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.CMENDx` [ok] 200 1053ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.CMENDx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.PRADx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 1813ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 1318ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 1198ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.CLONPx` [ok] 200 652ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.MIXUx` [ok] 200 1927ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.CTPCAx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.CLONPx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.circ.CTFJWx` [ok] 200 1197ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.MIXUx` [ok] 200 454ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 870ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.WUXIBx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.CLPHDx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.GENTEx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.CRESPx` [ok] 200 2196ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 1158ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 753ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.CKAHx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.CKINFx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.HKCGAx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.CKAHx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 1209ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 1010ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 1093ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 522ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.mult.KUAIx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.COVELx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 981ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 869ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.GEELx` [ok] 200 784ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.HKEXCx` [ok] 200 1170ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.price.CHONGx` [ok] 200 992ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.COVELx` [ok] 200 915ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 754ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.COVELx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.CKHUTx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 677ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 1748ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.CKHUTx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 814ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.CKHUTx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.circ.CHONGx` [ok] 200 1137ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.price.POPMTx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.circ.PICCx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.HNDLDx` [ok] 200 1854ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.PICCx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 1552ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.circ.HNDLDx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.POPMTx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 677ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 1496ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 1364ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.POPMTx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 1726ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 53ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 121ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 85ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.HKEXCx` [ok] 200 356ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MEITx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.MIXUx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 59ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.CTINSx` [ok] 200 352ms https://lite-api.jup.ag/tokens/v2/search?query=CTINSx
- `jito.tip_floor` [ok] 200 88ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 305ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 75ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 710ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 712ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 702ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 700ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 168ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
