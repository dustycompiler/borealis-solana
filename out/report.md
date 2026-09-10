# Borealis — Solana ecosystem report

**Generated** 2026-09-10T19:21:15Z · 2026-09-10 12:21:15 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-10T19:21:04Z · **RPC health** `ok`
**Health score** 95 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h -3.36%; DEX 24h $3.00B · 1d +11% · vs-7d-ago +31%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +39.44%. (threshold: `|7d %| >= 20`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +10.69%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +31.06%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 445,962,182 |
| Block height | 424,005,537 |
| Block time | 2026-09-10T19:21:04Z |
| Epoch | 1,032 (31.99% · slot 138,182/432,000) |
| Mean TPS (last ~3,600s) | 4,160.7 |
| Mean non-vote TPS | 2,030.5 |
| Median TPS (same window) | 4,137.3 |
| Mean slot time | 316.2 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 547,138,990,264 |
| Circulating supply | 586,335,374 SOL |
| Total supply | 633,830,647 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 13 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 437,881,529 SOL |
| Delinquent stake | 1,306,684.46 SOL (0.298%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.28% / 35.58% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 3.98% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.32M SOL | 3.73% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.52M SOL | 2.86% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.38M SOL | 2.60% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.19% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.28M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.34M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.88M SOL | 1.57% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.55M SOL | 1.50% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.95M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `6ptuwW4r…` · 1000.00K SOL · commission 100% · lag 406 slots
- `mXv18ov8…` · 220.40K SOL · commission 0% · lag 3463 slots
- `scs2Ra91…` · 58.59K SOL · commission 10% · lag 83100 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 108025 slots
- `inWVrrYJ…` · 8.46K SOL · commission 0% · lag 263085 slots
- `xLabscif…` · 3.36K SOL · commission 5% · lag 2173809 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 1996260 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 167020 slots
- `4GEEKSwu…` · 326.50 SOL · commission 5% · lag 152570 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 16426499 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 445962182 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 1123171 slots

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
| Jito tip-floor run-rate (NOT REV) | $58.65K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 58646 USD; at p95 floor → 2378255 USD. |
| Protocol fees 24h | $15.72M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9992 |
| p90 / p99 | 0.000015 / 0.000118 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $99.79 | coingecko.simple_price |
| 24h change | -3.36% | coingecko.simple_price |
| Market cap | $58.51B | coingecko.simple_price |
| 24h volume | $3.30B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.78B |
| TVL 1d / 7d / 30d | -2.84% / +1.26% / +19.27% |
| DEX volume 24h | $3.00B · 1d +10.69% · vs-7d-ago +31.06% |
| 7d DEX volume | $17.54B · +4.09% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $15.72M |
| Fees 1d / 7d | -5.90% / +39.44% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| BisonFi | $402.77M | +61.55% |
| Raydium AMM | $347.70M | -0.84% |
| PumpSwap | $340.96M | -53.74% |
| Meteora DLMM | $322.25M | +35.54% |
| HumidiFi | $285.64M | +86.20% |
| Tessera V | $248.02M | +58.67% |
| Orca DEX | $170.35M | +10.89% |
| Manifest Trade | $148.45M | +19.04% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.53B | -3.41% | -4.36% |
| Kamino Lend | Lending | $1.33B | -1.68% | -0.70% |
| Raydium AMM | Dexs | $1.11B | -3.29% | +1.50% |
| Jupiter Lend | Lending | $1.07B | -2.69% | -2.20% |
| Binance Staked SOL | Liquid Staking | $1.04B | -3.34% | -4.60% |
| Jito Liquid Staking | Liquid Staking | $1.03B | -3.40% | -2.19% |
| BlackRock BUIDL | RWA | $992.27M | -0.57% | +0.68% |
| Jupiter Perpetual Exchange | Derivatives | $740.22M | -1.73% | -3.27% |
| Jupiter Staked SOL | Liquid Staking | $517.37M | -3.47% | -3.94% |
| Sentora Curator | Risk Curators | $387.85M | -0.18% | -7.69% |

## Stablecoins

Solana circulating pegged-USD: **$15.95B**
(1d -0.33% · 7d +2.95%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.94B | -3.35% |
| USDT · Tether | $2.68B | -2.89% |
| USDGO · USDGO | $1.38B | +1.28% |
| USD1 · World Liberty Financial USD | $1.28B | +0.00% |
| BUIDL · BlackRock USD | $992.27M | +0.47% |
| PYUSD · PayPal USD | $733.52M | -2.54% |
| USDG · Global Dollar | $596.49M | +1.00% |
| USDe · Ethena USDe | $536.47M | -0.00% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $105.05M (lower bound, not a census).
24h volume $178.51M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.92B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.27M
- **OnRe** (RWA) — $308.49M
- **Ondo Yield Assets** (RWA) — $180.09M
- **Huma Finance V2** (RWA) — $169.50M
- **Hastra** (RWA) — $152.88M
- **Plume Vaults** (RWA) — $27.20M
- **Ondo Global Markets** (RWA) — $25.23M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.39M

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

- [Prompt to product in minutes. 

Vibe manufacture with @NomuStores on Solana.](https://x.com/solana/status/2098121215928131763) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 18:47:33 GMT
- [Watch the full episode on @chinsanity https://x.com/chinsanity/status/2097308982889340991](https://x.com/solana/status/2098109881710526589) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 18:02:31 GMT
- [Tuom Holmberg says anyone building an onchain product for retail should be doing it on Solana:

“If you're building something new in blockchain, no offense to my friends on these other chains but if you're building something onchain that's going to hit retail, you should definitely be doing it on Solana”

“There's no question”

@TuomHolmberg @Collector_Crypt @chinsanity](https://x.com/solana/status/2098109879034519583) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 18:02:30 GMT
- [Kings and queens at the ready

2026 WSOP Super Circuit Canada - Main Event continues 
https://x.com/i/broadcasts/1yxBePwRRLoJN](https://x.com/solana/status/2098094615869981067) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 17:01:51 GMT
- [RT by @solana: Tokenized stocks, now on @Pumpfun.

Launch Pumpfun tokens paired with 30+ tokenized stocks issued by Backpack Securities, including $SPCX, $NKE, $RDDT, $LULU, $MU, $SKHY and $AMC. More on the way.

All on @Solana. Redeemable 1:1 for the underlying shares.](https://x.com/BackpackOnchain/status/2098086411614519335) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 16:29:15 GMT
- [RT by @solana: $GRND has been live and tradable on Raydium for ~1 hour.

Since launch:
- $11.4M+ in trading volume
- 150K+ trades
- 34K+ wallets

Stonk szn on Solana.](https://x.com/Raydium/status/2098075151170412925) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 15:44:31 GMT
- [RT by @solana: Tap UP or DOWN to trade👆🏽

Real onchain orderbook on Solana!

Powered by @PhoenixTrade🧡](https://x.com/taptaptap_trade/status/2098048896521969728) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 14:00:11 GMT
- [$GRND is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2098058257247981981) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 14:37:23 GMT
- [RT by @anza_xyz: x.com/i/article/209802056112…](https://x.com/solana_devs/status/2098023409976492318) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 10 Sep 2026 12:18:54 GMT
- [Transaction V1 activation on mainnet-beta is moving to the start of epoch 1035, expected Sept 15 at ~1:20 AM UTC.

Teams across the ecosystem told us they needed more time to test and integrate V1 support. We listened.

How to get ready:

- V1 is live on devnet, test your integration now.

-  Compute budgets in V1 are set using a new transaction config. Compute budget instructions still work on legacy and V0 but no-op in V1.

- App developers: even if you don't plan to send V1 transactions, some changes may impact your app. Review the guide below.

Details: https://solana.com/upgrades/larger-transaction-sizes](https://x.com/anza_xyz/status/2097769035144561079) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 09 Sep 2026 19:28:07 GMT `upgrade` `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [Prompt to product in minutes. 

Vibe manufacture with @NomuStores on Solana.](https://x.com/solana/status/2098121215928131763) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 18:47:33 GMT
- [Watch the full episode on @chinsanity https://x.com/chinsanity/status/2097308982889340991](https://x.com/solana/status/2098109881710526589) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 18:02:31 GMT
- [Tuom Holmberg says anyone building an onchain product for retail should be doing it on Solana:

“If you're building something new in blockchain, no offense to my friends on these other chains but if you're building something onchain that's going to hit retail, you should definitely be doing it on Solana”

“There's no question”

@TuomHolmberg @Collector_Crypt @chinsanity](https://x.com/solana/status/2098109879034519583) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 18:02:30 GMT
- [Kings and queens at the ready

2026 WSOP Super Circuit Canada - Main Event continues 
https://x.com/i/broadcasts/1yxBePwRRLoJN](https://x.com/solana/status/2098094615869981067) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 17:01:51 GMT
- [RT by @solana: Tokenized stocks, now on @Pumpfun.

Launch Pumpfun tokens paired with 30+ tokenized stocks issued by Backpack Securities, including $SPCX, $NKE, $RDDT, $LULU, $MU, $SKHY and $AMC. More on the way.

All on @Solana. Redeemable 1:1 for the underlying shares.](https://x.com/BackpackOnchain/status/2098086411614519335) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 16:29:15 GMT
- [RT by @solana: $GRND has been live and tradable on Raydium for ~1 hour.

Since launch:
- $11.4M+ in trading volume
- 150K+ trades
- 34K+ wallets

Stonk szn on Solana.](https://x.com/Raydium/status/2098075151170412925) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 15:44:31 GMT
- [RT by @solana: Tap UP or DOWN to trade👆🏽

Real onchain orderbook on Solana!

Powered by @PhoenixTrade🧡](https://x.com/taptaptap_trade/status/2098048896521969728) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 14:00:11 GMT
- [$GRND is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2098058257247981981) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 14:37:23 GMT
- [RT by @anza_xyz: x.com/i/article/209802056112…](https://x.com/solana_devs/status/2098023409976492318) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 10 Sep 2026 12:18:54 GMT
- [Transaction V1 activation on mainnet-beta is moving to the start of epoch 1035, expected Sept 15 at ~1:20 AM UTC.

Teams across the ecosystem told us they needed more time to test and integrate V1 support. We listened.

How to get ready:

- V1 is live on devnet, test your integration now.

-  Compute budgets in V1 are set using a new transaction config. Compute budget instructions still work on legacy and V0 but no-op in V1.

- App developers: even if you don't plan to send V1 transactions, some changes may impact your app. Review the guide below.

Details: https://solana.com/upgrades/larger-transaction-sizes](https://x.com/anza_xyz/status/2097769035144561079) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 09 Sep 2026 19:28:07 GMT `upgrade` `mainnet`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-10 (2026-09-10 12:21:15 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 136ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 79ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 57ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 65ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 56ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6928ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 122ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 96ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 69ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 79ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 42ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 48ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 51ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 187ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 57ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 76ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 110ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 362ms https://solana.com/data
- `solana.com.databricks` [ok] 200 81ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 271ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 114ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 165ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 110ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 253ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 339ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 323ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 312ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 117ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 2254ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 248ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1967ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 2197ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 167ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 67ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 88ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 339ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 436ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 556ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 517ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 580ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 544ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 489ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 537ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 525ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 526ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 597ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 452ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 531ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 354ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2218ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1224ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1265ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2160ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2540ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1647ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1183ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1232ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.COINx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.WGSx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.WRLDx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.SPYx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.INDIx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.QQQx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.COINx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.FLNCx` [ok] 200 605ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.circ.INDIx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 543ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.FLNCx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.PCTx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.mult.COINx` [ok] 200 514ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 482ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.METCx` [ok] 200 536ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.QUBTx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.circ.WGSx` [ok] 200 1308ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.price.AIx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.BETRx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.PCTx` [ok] 200 727ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.METCx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.DRSx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.mult.METCx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.price.SAILx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.price.SCIx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.mult.BETRx` [ok] 200 772ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.BSYx` [ok] 200 686ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.price.GSATx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.mult.AIx` [ok] 200 1093ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.XRXx` [ok] 200 3092ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.MPx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.circ.SCIx` [ok] 200 1182ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 2781ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.SCIx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.circ.DRSx` [ok] 200 2223ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.circ.GSATx` [ok] 200 1230ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.circ.SAILx` [ok] 200 2258ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 689ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.BSYx` [ok] 200 1784ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.mult.GSATx` [ok] 200 499ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.mult.BSYx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.price.DCIx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.mult.WYFIx` [ok] 200 503ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 1346ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.SAILx` [ok] 200 816ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.circ.MPx` [ok] 200 2089ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.price.RYANx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.price.BXPx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.price.FRHCx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.circ.BXPx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.mult.MPx` [ok] 200 570ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.price.DVAx` [ok] 200 2244ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.price.DYx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.mult.BXPx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 1383ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 2163ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.circ.RYANx` [ok] 200 1079ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.mult.DCIx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.price.WMSx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.price.GDDYx` [ok] 200 2032ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.price.FDSx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.mult.RYANx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.circ.FDSx` [ok] 200 411ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.circ.DVAx` [ok] 200 1155ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.price.ALSNx` [ok] 200 524ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.mult.DVAx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.circ.DYx` [ok] 200 1337ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.price.SMTCx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.price.SFx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.circ.WMSx` [ok] 200 1018ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.circ.FRHCx` [ok] 200 2044ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.price.AMx` [ok] 200 1478ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.mult.FRHCx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.mult.WMSx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.AXSMx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.price.EGPx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.circ.GDDYx` [ok] 200 1405ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.mult.GDDYx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.circ.ALSNx` [ok] 200 1056ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.circ.SFx` [ok] 200 905ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.mult.SFx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.mult.ALSNx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.circ.SMTCx` [ok] 200 1193ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.price.BPOPx` [ok] 200 558ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.price.TTMIx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.price.AEISx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.circ.AXSMx` [ok] 200 1039ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.circ.AMx` [ok] 200 1341ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.AMx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.mult.SMTCx` [ok] 200 803ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.price.KTOSx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.circ.KTOSx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.mult.AXSMx` [ok] 200 849ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 1168ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.mult.KTOSx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.circ.AEISx` [ok] 200 1089ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.mult.BPOPx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.price.HRLx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.mult.AEISx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.circ.HRLx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.price.SEICx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.price.PAGx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.price.HIIx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.mult.HRLx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.mult.HIIx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.price.GFLx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.price.EHCx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.circ.PAGx` [ok] 200 622ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 3802ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.circ.EHCx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.circ.TTMIx` [ok] 200 2450ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.price.ARx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.mult.EHCx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.price.DPZx` [ok] 200 2271ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.circ.ARx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.mult.TTMIx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.MGMx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.circ.SEICx` [ok] 200 1462ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.mult.PAGx` [ok] 200 833ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.mult.ARx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.mult.SEICx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.circ.GFLx` [ok] 200 1476ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.price.DOCUx` [ok] 200 696ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.mult.GFLx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.circ.MGMx` [ok] 200 807ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.circ.DPZx` [ok] 200 951ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.price.HUBSx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.price.WTRGx` [ok] 200 777ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.circ.HUBSx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.price.AFGx` [ok] 200 992ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.mult.MGMx` [ok] 200 567ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.mult.DPZx` [ok] 200 643ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.mult.HUBSx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.price.JKHYx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.circ.WTRGx` [ok] 200 791ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 427ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.circ.JKHYx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.mult.WTRGx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.price.AMKRx` [ok] 200 571ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.mult.AFGx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.price.IESCx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.circ.AMKRx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.price.GMEDx` [ok] 200 883ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.circ.IESCx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.circ.EGPx` [ok] 200 6241ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.mult.JKHYx` [ok] 200 724ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.mult.IESCx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.CRx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.price.BMRNx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.circ.CRx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 623ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.mult.EGPx` [ok] 200 734ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.price.HALOx` [ok] 200 3283ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.circ.BMRNx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.price.JEFx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.mult.BMRNx` [ok] 200 392ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.circ.JEFx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.circ.HALOx` [ok] 200 439ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.price.AMHx` [ok] 200 627ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.mult.JEFx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.circ.DOCUx` [ok] 200 3570ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.circ.AMHx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.price.FIVEx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.mult.DOCUx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.mult.AMHx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.circ.FIVEx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.mult.AMKRx` [ok] 200 2169ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.price.VNOMx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.mult.HALOx` [ok] 200 738ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.mult.CRx` [ok] 200 1622ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.mult.FIVEx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.circ.VNOMx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.price.IVZx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.price.ITx` [ok] 200 646ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.price.AHRx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.circ.IVZx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.mult.VNOMx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.MDGLx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.mult.IVZx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.price.OCx` [ok] 200 2992ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.circ.AHRx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.price.NWSAx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.price.CORTx` [ok] 200 576ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.circ.OCx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.circ.MDGLx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.circ.NWSAx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.mult.OCx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.circ.ITx` [ok] 200 774ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.price.STRLx` [ok] 200 660ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.price.AURx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.mult.AHRx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.circ.AURx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.price.Hx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.mult.ITx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.NWSAx` [ok] 200 571ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.mult.AURx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.mult.MDGLx` [ok] 200 726ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.circ.STRLx` [ok] 200 475ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.price.ARWRx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.price.GWREx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.price.NWSx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.circ.ARWRx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.mult.STRLx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.price.MANHx` [ok] 200 427ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.circ.GWREx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.circ.MANHx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.price.UHALx` [ok] 200 2470ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.circ.UHALx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 698ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.price.BAXx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.CORTx` [ok] 200 2105ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.circ.Hx` [ok] 200 1457ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.circ.NWSx` [ok] 200 1135ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 829ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.price.CACIx` [ok] 200 1171ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.circ.BAXx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 1399ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.circ.CACIx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.BAXx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.CORTx` [ok] 200 613ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.mult.Hx` [ok] 200 1112ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 1467ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.mult.UHALx` [ok] 200 2072ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.mult.CACIx` [ok] 200 3083ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 46ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 163ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.BETRx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.WYFIx` [ok] 200 72ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.INDIx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 60ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 73ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.METCx` [ok] 200 97ms https://lite-api.jup.ag/tokens/v2/search?query=METCx
- `jup.tokens.search.PCTx` [ok] 200 65ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.FLNCx` [ok] 200 69ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jito.tip_floor` [ok] 200 256ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 270ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 79ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 69ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 46ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 226ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 57ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 130ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
