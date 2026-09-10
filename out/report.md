# Borealis — Solana ecosystem report

**Generated** 2026-09-10T00:31:23Z · 2026-09-09 17:31:23 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-10T00:31:12Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h -2.23%; DEX 24h $2.71B · 1d -0% · vs-7d-ago +25%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +31.01%. (threshold: `|7d %| >= 20`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -2.23%, DeFiLlama TVL 1d -0.34%, DEX 1d -0.36%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +24.83%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 445,747,654 |
| Block height | 423,791,081 |
| Block time | 2026-09-10T00:31:12Z |
| Epoch | 1,031 (82.33% · slot 355,655/432,000) |
| Mean TPS (last ~3,600s) | 4,076.7 |
| Mean non-vote TPS | 1,960.2 |
| Median TPS (same window) | 4,072.8 |
| Mean slot time | 316.7 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 546,871,020,222 |
| Circulating supply | 586,250,023 SOL |
| Total supply | 633,736,249 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 13 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 438,449,318 SOL |
| Delinquent stake | 204,186.77 SOL (0.047%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.26% / 35.55% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 3.98% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.35M SOL | 3.73% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.53M SOL | 2.86% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.39M SOL | 2.60% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.18% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.03M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.32M SOL | 1.67% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.86M SOL | 1.56% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.60M SOL | 1.51% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.97M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `ECNnK4Vj…` · 140.82K SOL · commission 0% · lag 19952 slots
- `mrgn4atx…` · 20.28K SOL · commission 0% · lag 39115 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 11871 slots
- `inWVrrYJ…` · 9.89K SOL · commission 0% · lag 48557 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 2398931 slots
- `prt1st4R…` · 5.87K SOL · commission 5% · lag 2260712 slots
- `xLabscif…` · 4.17K SOL · commission 5% · lag 1959281 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 1781732 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 248898 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 420771 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 445747654 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 61698784 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 500 | data/history.jsonl snapshot tape |
| TVL chart | 500 | data/history.jsonl snapshot tape |
| SOL chart | 500 | data/history.jsonl snapshot tape |
| history.jsonl rows | 500 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$768.89K** (7,465.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-08 |
| **Solana REV** | **8,789.1 SOL** / **$905.27K** | MEASURED UTC calendar day 2026-09-08: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-08 · UTC day 2026-09-08 · SOL-USD date 2026-09-08 |
| Jito tip-floor run-rate (NOT REV) | $29.00K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 28997 USD; at p95 floor → 514733 USD. |
| Protocol fees 24h | $16.56M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9982 |
| p90 / p99 | 0.000015 / 0.000378 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $101.31 | coingecko.simple_price |
| 24h change | -2.23% | coingecko.simple_price |
| Market cap | $59.39B | coingecko.simple_price |
| 24h volume | $3.17B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.90B |
| TVL 1d / 7d / 30d | -0.34% / +4.31% / +21.34% |
| DEX volume 24h | $2.71B · 1d -0.36% · vs-7d-ago +24.83% |
| 7d DEX volume | $16.83B · -0.50% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $16.56M |
| Fees 1d / 7d | +5.92% / +31.01% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $737.12M | -15.61% |
| Raydium AMM | $435.13M | +41.36% |
| BisonFi | $249.32M | +22.18% |
| Meteora DLMM | $237.76M | +21.71% |
| Orca DEX | $169.53M | -28.43% |
| Tessera V | $156.31M | +4.56% |
| HumidiFi | $153.40M | +58.34% |
| Manifest Trade | $151.97M | +11.21% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.56B | -0.90% | +2.95% |
| Kamino Lend | Lending | $1.34B | -0.99% | +9.37% |
| Raydium AMM | Dexs | $1.15B | +0.40% | +7.03% |
| Jupiter Lend | Lending | $1.09B | +1.15% | +2.02% |
| Binance Staked SOL | Liquid Staking | $1.06B | -0.83% | +3.02% |
| Jito Liquid Staking | Liquid Staking | $1.05B | -0.91% | +4.46% |
| BlackRock BUIDL | RWA | $992.17M | -0.57% | +0.68% |
| Jupiter Perpetual Exchange | Derivatives | $746.71M | -0.21% | +0.58% |
| Jupiter Staked SOL | Liquid Staking | $529.53M | -0.79% | +2.76% |
| xStocks | RWA | $437.71M | -1.26% | +0.88% |

## Stablecoins

Solana circulating pegged-USD: **$16.20B**
(1d -0.39% · 7d +4.93%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.11B | -3.02% |
| USDT · Tether | $2.77B | -0.00% |
| USDGO · USDGO | $1.37B | +0.18% |
| USD1 · World Liberty Financial USD | $1.28B | +1.58% |
| BUIDL · BlackRock USD | $992.17M | +1.46% |
| PYUSD · PayPal USD | $756.75M | +3.43% |
| USDG · Global Dollar | $603.09M | +5.46% |
| USDe · Ethena USDe | $535.72M | -0.00% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 79 of 737 Solana-deployed listed symbols (multiplier ok 80/80; 737 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 737 · Solana deployments 737 · priced 79 · priced-subset mcap $293.47M (lower bound, not a census).
24h volume $180.83M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $436.89M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 79 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 737 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 737 unique underlyings among 737 Solana rows; not every tokenized equity on Solana). 737 of 737 listed xStocks have a Solana deployment (737 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.35B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.17M
- **xStocks** (RWA) — $437.71M
- **OnRe** (RWA) — $307.14M
- **Ondo Yield Assets** (RWA) — $179.66M
- **Huma Finance V2** (RWA) — $172.14M
- **Hastra** (RWA) — $149.46M
- **Ondo Global Markets** (RWA) — $25.91M
- **Plume Vaults** (RWA) — $25.76M

## Daily active addresses

889,097 (Allium, as of 2026-09-08). Provider range 468,434–891,389. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: Introducing Custom Pairs

Launch Pumpfun tokens paired with tokenized stocks, majors & more on Solana.

Launch with more variety, deeper liquidity & lower fees than anywhere else.](https://x.com/Pumpfun/status/2097785975434846285) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:35:26 GMT
- [All 20 are available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @Pumpfun, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2097787932232872294) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:43:12 GMT
- [$BA, $BABA, $BULL, $COST, $DELL, $DJT, $HIMS, $IBM, $JNJ, $LMT, $LULU, $NET, $PFE, $QUBT, $RBLX, $RDDT, $RIVN, $SHOP, $SNAP, $UPS

Verify the addresses on @tokens:
https://tokens.xyz/stocks?category=stocks](https://x.com/solana/status/2097787930576089185) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:43:12 GMT
- [Pinned: BREAKING: 20 more stocks live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2097787928558608863) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:43:11 GMT
- [RT by @solana: NEW: @world_xyz launches its official prediction market platform on @Solana for over 1 million waitlisted users, powered by Chainlink. 

Hundreds of markets across sports, crypto, politics, culture, and more. 

Chainlink. The prediction market oracle.](https://x.com/chainlink/status/2097674520978964562) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 13:12:33 GMT
- [RT by @solana: The launchpad wars have arrived. Who will win?

$STONK and $PONS are now available to trade with leverage on Phoenix:

https://phoenix.trade/try/stonk-sep09](https://x.com/PhoenixTrade/status/2097771106077737347) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 19:36:21 GMT
- [RT by @solana: ⬜️](https://x.com/joinfrontier/status/2097767709169607114) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 19:22:51 GMT
- [BIG DAY 🆘](https://x.com/solana/status/2097732906236178919) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 17:04:33 GMT
- [Transaction V1 activation on mainnet-beta is moving to the start of epoch 1035, expected Sept 15 at ~1:20 AM UTC.

Teams across the ecosystem told us they needed more time to test and integrate V1 support. We listened.

How to get ready:

- V1 is live on devnet, test your integration now.

-  Compute budgets in V1 are set using a new transaction config. Compute budget instructions still work on legacy and V0 but no-op in V1.

- App developers: even if you don't plan to send V1 transactions, some changes may impact your app. Review the guide below.

Details: https://solana.com/upgrades/larger-transaction-sizes](https://x.com/anza_xyz/status/2097769035144561079) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 09 Sep 2026 19:28:07 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: What is cool about transaction v1?
1) @multisig smart wallet being able to do everything onchain with big pqc based signatures 
2) two zkp root state transitions in one atomic tx, aka “based rollups”
3) routing to a bajilion markets at the same time](https://x.com/toly/status/2097345987937497491) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:27:04 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: Introducing Custom Pairs

Launch Pumpfun tokens paired with tokenized stocks, majors & more on Solana.

Launch with more variety, deeper liquidity & lower fees than anywhere else.](https://x.com/Pumpfun/status/2097785975434846285) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:35:26 GMT
- [All 20 are available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @Pumpfun, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2097787932232872294) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:43:12 GMT
- [$BA, $BABA, $BULL, $COST, $DELL, $DJT, $HIMS, $IBM, $JNJ, $LMT, $LULU, $NET, $PFE, $QUBT, $RBLX, $RDDT, $RIVN, $SHOP, $SNAP, $UPS

Verify the addresses on @tokens:
https://tokens.xyz/stocks?category=stocks](https://x.com/solana/status/2097787930576089185) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:43:12 GMT
- [Pinned: BREAKING: 20 more stocks live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2097787928558608863) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:43:11 GMT
- [RT by @solana: NEW: @world_xyz launches its official prediction market platform on @Solana for over 1 million waitlisted users, powered by Chainlink. 

Hundreds of markets across sports, crypto, politics, culture, and more. 

Chainlink. The prediction market oracle.](https://x.com/chainlink/status/2097674520978964562) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 13:12:33 GMT
- [RT by @solana: The launchpad wars have arrived. Who will win?

$STONK and $PONS are now available to trade with leverage on Phoenix:

https://phoenix.trade/try/stonk-sep09](https://x.com/PhoenixTrade/status/2097771106077737347) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 19:36:21 GMT
- [RT by @solana: ⬜️](https://x.com/joinfrontier/status/2097767709169607114) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 19:22:51 GMT
- [BIG DAY 🆘](https://x.com/solana/status/2097732906236178919) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 17:04:33 GMT
- [Transaction V1 activation on mainnet-beta is moving to the start of epoch 1035, expected Sept 15 at ~1:20 AM UTC.

Teams across the ecosystem told us they needed more time to test and integrate V1 support. We listened.

How to get ready:

- V1 is live on devnet, test your integration now.

-  Compute budgets in V1 are set using a new transaction config. Compute budget instructions still work on legacy and V0 but no-op in V1.

- App developers: even if you don't plan to send V1 transactions, some changes may impact your app. Review the guide below.

Details: https://solana.com/upgrades/larger-transaction-sizes](https://x.com/anza_xyz/status/2097769035144561079) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 09 Sep 2026 19:28:07 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: What is cool about transaction v1?
1) @multisig smart wallet being able to do everything onchain with big pqc based signatures 
2) two zkp root state transitions in one atomic tx, aka “based rollups”
3) routing to a bajilion markets at the same time](https://x.com/toly/status/2097345987937497491) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:27:04 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-10 (2026-09-09 17:31:23 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 737 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 85ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 32ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 30ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 29ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 51ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6467ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 60ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 69ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 48ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 269ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 25ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 34ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 32ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 67ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 79ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 60ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 88ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 384ms https://solana.com/data
- `solana.com.databricks` [ok] 200 133ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 544ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 113ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 105ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 57ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 112ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 700ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 71ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 81ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 75ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 232ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 252ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1237ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 2314ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 88ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 65ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 67ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 309ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 251ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 372ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 442ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 443ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 515ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 30ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 765ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 366ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 431ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 383ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 327ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 318ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 361ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 218ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2218ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 3109ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1348ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1169ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2769ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2049ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 3837ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1405ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AAPLx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.MSFTx` [ok] 200 833ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.MSFTx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 1145ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.AMZNx` [ok] 200 1234ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.mult.MSFTx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.price.GOOGLx` [ok] 200 1361ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.AMZNx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.NVDAx` [ok] 200 1558ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.QQQx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.SPYx` [ok] 200 1688ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.mult.AMZNx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.NVDAx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 756ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.FLNCx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.WGSx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.circ.AAPLx` [ok] 200 2046ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.TSLAx` [ok] 200 2498ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.mult.METAx` [ok] 200 650ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.WRLDx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.INDIx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.circ.FLNCx` [ok] 200 577ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 516ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.TSLAx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.XRXx` [ok] 200 1046ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.circ.WRLDx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.price.METCx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.PCTx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.mult.WRLDx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.METCx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.QUBTx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.mult.FLNCx` [ok] 200 629ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.mult.METCx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 655ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.XRXx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.PCTx` [ok] 200 597ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.BETRx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.AIx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.price.DRAMx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.circ.AIx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 1739ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.BETRx` [ok] 200 587ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 2750ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.XRXx` [ok] 200 1075ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 707ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.MUUx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.circ.DRAMx` [ok] 200 1108ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 576ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.MVLLx` [ok] 200 862ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.WYFIx` [ok] 200 2023ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.COINx` [ok] 200 771ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.AXTIx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.mult.AXTIx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.DJTx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 2188ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 1049ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 1311ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 751ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 733ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.KORUx` [ok] 200 603ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.MUUx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 774ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.price.INTWx` [ok] 200 747ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.circ.INTWx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.SNXXx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.SOXSx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.KORUx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.SOXSx` [ok] 200 611ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.mult.INTWx` [ok] 200 706ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.BANKCx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.INDIx` [ok] 200 3215ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.SNXXx` [ok] 200 1534ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 846ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.TNGYIx` [ok] 200 1038ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.SNXXx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.NWGx` [ok] 200 2177ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.mult.MMGx` [ok] 200 741ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.SHEINx` [ok] 200 2564ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.SHEINx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 972ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.KUNLx` [ok] 200 807ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.CTINSx` [ok] 200 1066ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.SHEINx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.TNGYIx` [ok] 200 1125ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.NWGx` [ok] 200 1157ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.JDLOGx` [ok] 200 2281ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 615ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 755ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 887ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.NWGx` [ok] 200 870ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.KUNLx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 749ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 2754ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 1436ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 901ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 1794ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 537ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 1911ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 690ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 923ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 644ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.CRESMx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 1648ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 524ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 2208ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.CMENDx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 1426ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.CMENDx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 1625ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.MIXUx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.JDHLTx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.CRESBx` [ok] 200 982ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 1148ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 1402ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 110ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.SNDSCx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.SITCx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 537ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.CRESPx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.CTFJWx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.SINOTx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.ASMPTx` [ok] 200 1573ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 770ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 608ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.CTPCAx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.PRADx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.CTPCAx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 2028ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 1215ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 860ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.GENTEx` [ok] 200 521ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 1084ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.CLONPx` [ok] 200 1774ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 497ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 651ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 826ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 742ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 817ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.CKAHx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.SMOIHx` [ok] 200 8052ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.WUXIBx` [ok] 200 1591ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.SINOx` [ok] 200 2022ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.circ.SMOIHx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 696ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 1456ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 1193ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 1334ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.KUAIx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 4685ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 1284ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 1628ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 2055ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 4196ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 2760ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 75ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INTWx` [ok] 200 64ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.MVLLx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SHEINx` [ok] 200 51ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.KORUx` [ok] 200 59ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.MUUx` [ok] 200 47ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.SNXXx` [ok] 200 56ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jup.tokens.search.DRAMx` [ok] 200 52ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.SOXSx` [ok] 200 53ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jito.tip_floor` [ok] 200 278ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 404ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 80ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 33ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 31ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 34ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 35ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 1715ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
