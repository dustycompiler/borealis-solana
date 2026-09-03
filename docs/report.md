# Borealis — Solana ecosystem report

**Generated** 2026-09-03T19:34:02Z · 2026-09-03 12:34:02 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-03T19:33:52Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +6.19%; DEX 24h $2.29B · 1d +5% · vs-7d-ago -3%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -17.43%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -30.88%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 856,198.00 is +26.3% vs 30d median 677,709.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 105.31 USD is +27.2% vs 30d median 82.77 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 444,052,154 |
| Block height | 422,098,907 |
| Block time | 2026-09-03T19:33:52Z |
| Epoch | 1,027 (89.85% · slot 388,155/432,000) |
| Mean TPS (last ~3,600s) | 3,995.2 |
| Mean non-vote TPS | 1,870.5 |
| Median TPS (same window) | 3,868.8 |
| Mean slot time | 315.3 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 544,866,634,619 |
| Circulating supply | 585,274,588 SOL |
| Total supply | 633,360,624 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 20 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 437,932,678 SOL |
| Delinquent stake | 489,678.90 SOL (0.112%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.27% / 35.55% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.35M SOL | 3.96% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.33M SOL | 3.73% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.46M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.30M SOL | 2.58% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.18% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.22M SOL | 1.65% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.13M SOL | 1.63% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.50% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.95M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.61M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `7Zm1pE4F…` · 269.52K SOL · commission 8% · lag 917 slots
- `xLabscif…` · 84.41K SOL · commission 5% · lag 263781 slots
- `prt1st4R…` · 78.62K SOL · commission 5% · lag 565212 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 86869 slots
- `5ZjxMYBb…` · 18.18K SOL · commission 0% · lag 86232 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 703431 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1266033 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 752498 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 613515 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 2068400 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1251803 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1293317 slots

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
| **In-protocol fees 24h** | **$595.41K** (6,074.3 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-02 |
| **Solana REV** | **7,160.1 SOL** / **$701.85K** | MEASURED UTC calendar day 2026-09-02: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-02 · UTC day 2026-09-02 · SOL-USD date 2026-09-02 |
| Jito tip-floor run-rate (NOT REV) | $42.26K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 42258 USD; at p95 floor → 34037869 USD. |
| Protocol fees 24h | $10.54M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9974 |
| p90 / p99 | 0.000010 / 0.000107 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $105.31 | coingecko.simple_price |
| 24h change | +6.19% | coingecko.simple_price |
| Market cap | $61.69B | coingecko.simple_price |
| 24h volume | $4.04B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.96B |
| TVL 1d / 7d / 30d | +5.50% / +3.20% / +25.06% |
| DEX volume 24h | $2.29B · 1d +5.42% · vs-7d-ago -2.65% |
| 7d DEX volume | $16.85B · -21.10% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $10.54M |
| Fees 1d / 7d | -17.43% / -30.88% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $1.02B | +23.42% |
| Orca DEX | $267.01M | +21.94% |
| BisonFi | $194.35M | -5.12% |
| Manifest Trade | $184.75M | +25.62% |
| Raydium AMM | $147.77M | -3.12% |
| Meteora DLMM | $137.83M | -1.54% |
| pump.fun | $83.17M | +50.90% |
| Axiom | $60.26M | -38.49% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.60B | +6.30% | -3.21% |
| Kamino Lend | Lending | $1.34B | +8.80% | +5.66% |
| Raydium AMM | Dexs | $1.13B | +6.01% | -0.84% |
| Jupiter Lend | Lending | $1.10B | +4.58% | -2.27% |
| Binance Staked SOL | Liquid Staking | $1.09B | +6.42% | -2.38% |
| Jito Liquid Staking | Liquid Staking | $1.06B | +6.53% | -1.26% |
| BlackRock BUIDL | RWA | $890.78M | +0.11% | -1.06% |
| Jupiter Perpetual Exchange | Derivatives | $770.23M | +4.34% | -3.15% |
| Jupiter Staked SOL | Liquid Staking | $544.18M | +6.40% | -3.38% |
| xStocks | RWA | $462.82M | +7.23% | +4.79% |

## Stablecoins

Solana circulating pegged-USD: **$15.98B**
(1d +1.59% · 7d -0.19%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.89B | +3.81% |
| USDT · Tether | $2.95B | +3.90% |
| USDGO · USDGO | $1.32B | +5.62% |
| USD1 · World Liberty Financial USD | $1.22B | +1.24% |
| BUIDL · BlackRock USD | $890.78M | +0.43% |
| PYUSD · PayPal USD | $819.23M | +10.96% |
| USDG · Global Dollar | $596.27M | -2.81% |
| USDe · Ethena USDe | $536.23M | -0.23% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 78 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 78 · priced-subset mcap $294.21M (lower bound, not a census).
24h volume $36.73M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $462.82M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 78 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.11B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $890.78M
- **xStocks** (RWA) — $462.82M
- **OnRe** (RWA) — $295.53M
- **Ondo Yield Assets** (RWA) — $179.25M
- **Hastra** (RWA) — $150.50M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $25.27M
- **Plume Vaults** (RWA) — $22.89M

## Daily active addresses

856,198 (Allium, as of 2026-09-02). Provider range 446,040–877,460. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Payment Channels is now live on Solana

Learn more about how to achieve 1M payments per second on Solana via x402 and MPP from @_rishinsharma, Head of AI Growth, @SolanaFndn](https://x.com/solana/status/2095585115250585952) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 18:50:00 GMT
- [1,000,000 payments per second 🤯

only possible on Solana](https://x.com/solana/status/2095577162598236283) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 18:18:24 GMT
- [RT by @solana: Base handled 63% of x402 transactions in early August. By the end of the month it was down to 4%.

@solana went from 6% of transactions to 81% over the same stretch.

Volume followed. Solana held 5% of it through mid-August and closed the month at 50%, ahead of Base at 38%.

Data: @artemis](https://x.com/eco/status/2095566752558276742) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 17:37:02 GMT
- [RT by @solana: Tokenized equities on @solana saw over $1.3B volume in August. 

With a vast universe of trading, lending and other assorted venues, have you ever wondered how that flow looks when visualized?

This is how the flow of Solana's tokenized equities universe looked in August 👇](https://x.com/zinnresearch/status/2095550054853476813) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 16:30:41 GMT
- [RT by @solana: CLOCK IN - a Solana Mobile Hackathon by @RadiantsDAO is coming 🔜

September 8 - October 8

It’s almost time to clock-in.

https://solanamobile.com/hackathon](https://x.com/solanamobile/status/2095546195229716737) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 16:15:20 GMT
- [RT by @solana: 🚨BREAKING: @Solana has flipped @Base in both weekly x402 transaction count and volume for the first time, now processing more than 90% of x402 transactions.

x402 lets AI agents and apps pay for online services with stablecoins.](https://x.com/SolanaFloor/status/2095485302563623237) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 12:13:23 GMT
- [Why We Ship: @Beezie 

It started with her dad, hunting coins and basketball cards in the aisles for the what if. @AndreaMYellie turned it into Beezie, one of the fastest-growing collectibles platforms in the world. Now she's bringing Birkins to Solana.](https://x.com/solana/status/2095534784990810491) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 15:30:00 GMT
- [RT by @solana: 📊 @Solana ETFs ended August at all-time highs of $1.44B net assets, up 45% YTD.

This growth came after 7 consecutive days of net flows exceeding $10M.](https://x.com/TokenRelations/status/2095513176485839199) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 14:04:08 GMT
- [Prepare for the first step of rent reduction coming to mainnet-beta later today with this guide to reclaim your excess SOL.](https://x.com/anza_xyz/status/2095541509135495452) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 15:56:43 GMT `mainnet`
- [RT by @anza_xyz: 🚨ATTENTION: large transactions have hit the testnet

https://explorer.solana.com/tx/5KxbxQxkqv2gPjRArDeFJSmfhG6X1vAbEjZFn5zGPsmLvsb4FYKbYTm7BBDSNarkEt2jL5878wmJ4cTYyvURPLnK?cluster=testnet](https://x.com/bw_solana/status/2095199360724431064) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 17:17:09 GMT `upgrade`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [Payment Channels is now live on Solana

Learn more about how to achieve 1M payments per second on Solana via x402 and MPP from @_rishinsharma, Head of AI Growth, @SolanaFndn](https://x.com/solana/status/2095585115250585952) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 18:50:00 GMT
- [1,000,000 payments per second 🤯

only possible on Solana](https://x.com/solana/status/2095577162598236283) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 18:18:24 GMT
- [RT by @solana: Base handled 63% of x402 transactions in early August. By the end of the month it was down to 4%.

@solana went from 6% of transactions to 81% over the same stretch.

Volume followed. Solana held 5% of it through mid-August and closed the month at 50%, ahead of Base at 38%.

Data: @artemis](https://x.com/eco/status/2095566752558276742) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 17:37:02 GMT
- [RT by @solana: Tokenized equities on @solana saw over $1.3B volume in August. 

With a vast universe of trading, lending and other assorted venues, have you ever wondered how that flow looks when visualized?

This is how the flow of Solana's tokenized equities universe looked in August 👇](https://x.com/zinnresearch/status/2095550054853476813) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 16:30:41 GMT
- [RT by @solana: CLOCK IN - a Solana Mobile Hackathon by @RadiantsDAO is coming 🔜

September 8 - October 8

It’s almost time to clock-in.

https://solanamobile.com/hackathon](https://x.com/solanamobile/status/2095546195229716737) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 16:15:20 GMT
- [RT by @solana: 🚨BREAKING: @Solana has flipped @Base in both weekly x402 transaction count and volume for the first time, now processing more than 90% of x402 transactions.

x402 lets AI agents and apps pay for online services with stablecoins.](https://x.com/SolanaFloor/status/2095485302563623237) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 12:13:23 GMT
- [Why We Ship: @Beezie 

It started with her dad, hunting coins and basketball cards in the aisles for the what if. @AndreaMYellie turned it into Beezie, one of the fastest-growing collectibles platforms in the world. Now she's bringing Birkins to Solana.](https://x.com/solana/status/2095534784990810491) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 15:30:00 GMT
- [RT by @solana: 📊 @Solana ETFs ended August at all-time highs of $1.44B net assets, up 45% YTD.

This growth came after 7 consecutive days of net flows exceeding $10M.](https://x.com/TokenRelations/status/2095513176485839199) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 14:04:08 GMT
- [Prepare for the first step of rent reduction coming to mainnet-beta later today with this guide to reclaim your excess SOL.](https://x.com/anza_xyz/status/2095541509135495452) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 15:56:43 GMT `mainnet`
- [RT by @anza_xyz: 🚨ATTENTION: large transactions have hit the testnet

https://explorer.solana.com/tx/5KxbxQxkqv2gPjRArDeFJSmfhG6X1vAbEjZFn5zGPsmLvsb4FYKbYTm7BBDSNarkEt2jL5878wmJ4cTYyvURPLnK?cluster=testnet](https://x.com/bw_solana/status/2095199360724431064) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 17:17:09 GMT `upgrade`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-03 (2026-09-03 12:34:02 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~315 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~315 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **xStocks** — priced up to 80 of 726 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 188ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 98ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 92ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 90ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 90ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6900ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 253ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 87ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 53ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 332ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 29ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 29ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 27ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 68ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 114ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 101ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 1205ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 571ms https://solana.com/data
- `solana.com.databricks` [ok] 200 65ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 218ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 160ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 93ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 143ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 297ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 772ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 446ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 453ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 446ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1423ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1771ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2357ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 184ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 96ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 79ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 165ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 531ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 531ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 692ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 624ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 545ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 551ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 588ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 502ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 588ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 694ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 477ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 449ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 621ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 432ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2060ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1740ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1739ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1838ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1976ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1816ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1370ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.SPYx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.GOOGLx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.AMZNx` [ok] 200 580ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.TSLAx` [ok] 200 587ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.AAPLx` [ok] 200 613ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.NVDAx` [ok] 200 652ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.mult.GOOGLx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.QQQx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.NVDAx` [ok] 200 585ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.MSFTx` [ok] 200 1270ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.SPYx` [ok] 200 1133ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.MSFTx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.MUUx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.price.MVLLx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.mult.SPYx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 870ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.TSLAx` [ok] 200 1101ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.mult.TSLAx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.KORUx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.price.INTWx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.DRAMx` [ok] 200 947ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.circ.DRAMx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 1287ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 1152ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.mult.COINx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 1358ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 1192ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.circ.MUUx` [ok] 200 1629ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 849ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.MVLLx` [ok] 200 629ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.KORUx` [ok] 200 1585ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 1550ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 961ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.circ.AXTIx` [ok] 200 1182ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.NWGx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.mult.AXTIx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.SNXXx` [ok] 200 1009ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.MUUx` [ok] 200 1550ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.SNXXx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.mult.DJTx` [ok] 200 1887ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.INTWx` [ok] 200 1305ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 749ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.NWGx` [ok] 200 789ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.price.SUOPTx` [ok] 200 582ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.BANKCx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.SOXSx` [ok] 200 1745ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 710ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.SOXSx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 790ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.NWGx` [ok] 200 1085ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.mult.TNGYIx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.SHEINx` [ok] 200 2746ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.price.CTINSx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 657ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.SHEINx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 635ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 1171ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.SHEINx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.SZIGHx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.price.ENNHLx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 949ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.JTGEXx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.CMERPx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.CMENDx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.BDWAPx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.SITCx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.mult.CSPCx` [ok] 200 1000ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 1095ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 648ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 1223ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.MIXUx` [ok] 200 1240ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.MMGx` [ok] 200 4866ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.CRESPx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.SINOTx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.PRADx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.MMGx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 606ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 1127ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 1238ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.SINOTx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 1347ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 1254ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.SINOx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.CRESPx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 1313ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 1796ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.SINOx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.MIXUx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 1054ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CTFJWx` [ok] 200 1415ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.CLONPx` [ok] 200 1172ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.CLONPx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 1135ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 774ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.SWPRPx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.GENTEx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 744ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 1535ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 1561ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 710ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 1094ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 1012ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.CKINFx` [ok] 200 684ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 1015ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.COVELx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.circ.MEITx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 604ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 2450ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 554ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 422ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 723ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.KUAIx` [ok] 200 665ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.HNDLDx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.KUAIx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.MEITx` [ok] 200 923ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.CHONGx` [ok] 200 910ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.price.GEELx` [ok] 200 1259ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.CKHUTx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.COVELx` [ok] 200 1588ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.COVELx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 727ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1558ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 217ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.KORUx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.INTWx` [ok] 200 109ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.MUUx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.DRAMx` [ok] 200 112ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.SOXSx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jup.tokens.search.MVLLx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.MEITx` [ok] 200 117ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jito.tip_floor` [ok] 200 111ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 295ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 152ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 85ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 87ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 84ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 93ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 2209ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
