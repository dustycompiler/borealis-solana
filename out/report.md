# Borealis — Solana ecosystem report

**Generated** 2026-09-11T05:24:04Z · 2026-09-10 22:24:04 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-11T05:23:54Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h -2.12%; DEX 24h $2.95B · 1d -2% · vs-7d-ago +20%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +25.24%. (threshold: `|7d %| >= 20`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -2.12%, DeFiLlama TVL 1d -1.29%, DEX 1d -1.73%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **INFO · Daily active addresses vs 30d median** — Current 987,010.00 is +24.7% vs 30d median 791,527.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 446,076,541 |
| Block height | 424,119,825 |
| Block time | 2026-09-11T05:23:54Z |
| Epoch | 1,032 (58.46% · slot 252,542/432,000) |
| Mean TPS (last ~3,600s) | 3,583.5 |
| Mean non-vote TPS | 1,457.5 |
| Median TPS (same window) | 3,586.6 |
| Mean slot time | 316.4 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 547,279,224,145 |
| Circulating supply | 586,537,711 SOL |
| Total supply | 633,830,276 SOL |
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
| Activated stake | 439,046,903 SOL |
| Delinquent stake | 141,310.07 SOL (0.032%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.22% / 35.49% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 3.97% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.32M SOL | 3.72% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.52M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.38M SOL | 2.59% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.18% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.28M SOL | 2.11% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.34M SOL | 1.67% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.88M SOL | 1.57% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.55M SOL | 1.49% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.12M SOL | 1.39% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.12M SOL | 1.39% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.95M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `scs2Ra91…` · 58.59K SOL · commission 10% · lag 197459 slots
- `EWARp8Sy…` · 35.14K SOL · commission 5% · lag 5600 slots
- `mrgn4atx…` · 19.89K SOL · commission 0% · lag 21305 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 222384 slots
- `inWVrrYJ…` · 8.46K SOL · commission 0% · lag 377444 slots
- `xLabscif…` · 3.36K SOL · commission 5% · lag 2288168 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 2110619 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 281379 slots
- `4GEEKSwu…` · 326.50 SOL · commission 5% · lag 266929 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 16540858 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 446076541 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 1237530 slots

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
| **In-protocol fees 24h** | **$1.01M** (9,683.4 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-09 |
| **Solana REV** | **11,493.1 SOL** / **$1.20M** | MEASURED UTC calendar day 2026-09-09: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-09 · UTC day 2026-09-09 · SOL-USD date 2026-09-09 |
| Jito tip-floor run-rate (NOT REV) | $103.88K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 103882 USD; at p95 floor → 544332 USD. |
| Protocol fees 24h | $14.81M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9973 |
| p90 / p99 | 0.000011 / 0.000516 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $99.69 | coingecko.simple_price |
| 24h change | -2.12% | coingecko.simple_price |
| Market cap | $58.47B | coingecko.simple_price |
| 24h volume | $3.01B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.78B |
| TVL 1d / 7d / 30d | -1.29% / -2.55% / +18.58% |
| DEX volume 24h | $2.95B · 1d -1.73% · vs-7d-ago +19.88% |
| 7d DEX volume | $16.62B · +6.42% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.81M |
| Fees 1d / 7d | -5.75% / +25.24% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $468.14M | +37.30% |
| BisonFi | $402.77M | 0.00% |
| Raydium AMM | $385.98M | -11.29% |
| HumidiFi | $285.64M | 0.00% |
| Tessera V | $248.02M | 0.00% |
| Meteora DLMM | $220.43M | -31.60% |
| Orca DEX | $176.72M | +4.24% |
| Manifest Trade | $147.87M | -2.69% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.52B | -2.40% | -3.66% |
| Kamino Lend | Lending | $1.33B | -0.73% | -0.37% |
| Raydium AMM | Dexs | $1.11B | -1.26% | -0.68% |
| Jupiter Lend | Lending | $1.07B | -0.92% | -1.83% |
| Binance Staked SOL | Liquid Staking | $1.03B | -2.07% | -3.95% |
| Jito Liquid Staking | Liquid Staking | $1.02B | -2.47% | -3.00% |
| BlackRock BUIDL | RWA | $992.51M | -0.68% | -0.63% |
| Jupiter Perpetual Exchange | Derivatives | $738.90M | -1.00% | -3.31% |
| Jupiter Staked SOL | Liquid Staking | $513.27M | -1.99% | -4.13% |
| Sentora Curator | Risk Curators | $388.12M | -0.43% | -3.39% |

## Stablecoins

Solana circulating pegged-USD: **$15.98B**
(1d -1.32% · 7d -1.73%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.00B | -1.44% |
| USDT · Tether | $2.67B | -3.25% |
| USDGO · USDGO | $1.38B | +0.73% |
| USD1 · World Liberty Financial USD | $1.28B | -0.00% |
| BUIDL · BlackRock USD | $992.51M | +0.03% |
| PYUSD · PayPal USD | $736.18M | -2.72% |
| USDG · Global Dollar | $598.75M | -0.49% |
| USDe · Ethena USDe | $536.45M | +0.16% |

## Tokenized equities (xStocks)


Listed 100 · Solana deployments 100 · priced 0 · priced-subset mcap — (lower bound, not a census).
24h volume $100.62M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 10 / mcap_computable 0 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 100 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 100 unique underlyings among 100 Solana rows; not every tokenized equity on Solana). 100 of 100 listed xStocks have a Solana deployment (100 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.92B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.51M
- **OnRe** (RWA) — $309.56M
- **Ondo Yield Assets** (RWA) — $180.12M
- **Huma Finance V2** (RWA) — $169.01M
- **Hastra** (RWA) — $152.86M
- **Plume Vaults** (RWA) — $27.20M
- **Ondo Global Markets** (RWA) — $25.07M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.38M

## Daily active addresses

987,010 (Allium, as of 2026-09-09). Provider range 464,935–1,040,024. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: Turns out pairing memes with tokenized stocks on @Solana makes markets interesting again.

@Pumpfun and @LaunchOnSF helped push xStocks beyond 300,000 unique holders by bringing 20,000+ in the last 24h.

Deep liquidity on @Raydium supported $30M+ in volume, led by $SPYx pairs.](https://x.com/xStocksFi/status/2098140644078149990) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 20:04:45 GMT
- [RT by @solana: $DNUT is now listed on @Solana via Sunrise.

Issued by @Backpack Securities.](https://x.com/sunrise/status/2098137657763397707) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 19:52:53 GMT
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
- [The pace of Agave development has increased.

Stable releases ship roughly every 6 weeks, carrying protocol improvements and features to mainnet-beta faster than they used to.

Many of these changes seamlessly improve Solana, but some features require direct action from our ecosystem: validators, app developers, RPC providers, exchanges, block builders, and more.

With @SolanaFndn, we're improving both how changes roll out and how you hear about them.

Operationally: integration windows where builders test protocol changes together well before mainnet-beta activation.

Communications: earlier, clearer notice of changes that impact RPCs, apps, validators, and block builders, amplified through every channel the ecosystem already follows.

When the ecosystem integrates as fast as we ship, everyone moves faster and Solana wins.

Blog coming soon on what we're improving.](https://x.com/anza_xyz/status/2098147825662214499) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 10 Sep 2026 20:33:17 GMT `mainnet`
- [RT by @anza_xyz: Attention Solana devs 🚨

The new transaction version might break your applications!

They are waiting for you to fix you apps, but they are not waiting long anymore 👇](https://x.com/HeyAndyS/status/2098142776030269673) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 10 Sep 2026 20:13:14 GMT `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: Turns out pairing memes with tokenized stocks on @Solana makes markets interesting again.

@Pumpfun and @LaunchOnSF helped push xStocks beyond 300,000 unique holders by bringing 20,000+ in the last 24h.

Deep liquidity on @Raydium supported $30M+ in volume, led by $SPYx pairs.](https://x.com/xStocksFi/status/2098140644078149990) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 20:04:45 GMT
- [RT by @solana: $DNUT is now listed on @Solana via Sunrise.

Issued by @Backpack Securities.](https://x.com/sunrise/status/2098137657763397707) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 19:52:53 GMT
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
- [The pace of Agave development has increased.

Stable releases ship roughly every 6 weeks, carrying protocol improvements and features to mainnet-beta faster than they used to.

Many of these changes seamlessly improve Solana, but some features require direct action from our ecosystem: validators, app developers, RPC providers, exchanges, block builders, and more.

With @SolanaFndn, we're improving both how changes roll out and how you hear about them.

Operationally: integration windows where builders test protocol changes together well before mainnet-beta activation.

Communications: earlier, clearer notice of changes that impact RPCs, apps, validators, and block builders, amplified through every channel the ecosystem already follows.

When the ecosystem integrates as fast as we ship, everyone moves faster and Solana wins.

Blog coming soon on what we're improving.](https://x.com/anza_xyz/status/2098147825662214499) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 10 Sep 2026 20:33:17 GMT `mainnet`
- [RT by @anza_xyz: Attention Solana devs 🚨

The new transaction version might break your applications!

They are waiting for you to fix you apps, but they are not waiting long anymore 👇](https://x.com/HeyAndyS/status/2098142776030269673) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 10 Sep 2026 20:13:14 GMT `mainnet`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-11 (2026-09-10 22:24:04 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks market cap** — Listed Solana-deployed xStocks but quote and/or circulating missing. Mcap omitted.
- **xStocks** — priced up to 80 of 100 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.
- **xStocks** — METCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — WGSx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — QUBTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — XRXx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — INDIx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — WRLDx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — FLNCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — WYFIx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — DRSx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SAILx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — AIx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — GSATx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — BSYx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SCIx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MPx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — DVAx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — DYx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — GDDYx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — RYANx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — BXPx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — FRHCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — AXSMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — WMSx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — AMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — FDSx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SMTCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — ALSNx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SFx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — EGPx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — AEISx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — BPOPx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — PAGx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — KTOSx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — DPZx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — HRLx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SEICx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — HIIx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — EHCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — GFLx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — DOCUx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — ARx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MGMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — HALOx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — AFGx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — HUBSx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — AMKRx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — GMEDx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — IESCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — OCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CRx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — AMHx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — BMRNx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — JEFx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — FIVEx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — ITx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MDGLx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — VNOMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — UHALx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — NWSAx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — IVZx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — AURx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — Hx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — ARWRx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CNAx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — GWREx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — NWSx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MANHx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — BAXx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — RVTYx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — TXRHx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — price, circulating-supply, and/or currentMultiplier missing — market cap omitted (never assumed multiplier=1.0)

## Sources this run

- `rpc.getHealth` [ok] 200 261ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 209ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 247ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 184ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 238ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6998ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 410ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 146ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 76ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 122ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 78ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 55ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 61ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 135ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 114ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 103ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 122ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 639ms https://solana.com/data
- `solana.com.databricks` [ok] 200 107ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 498ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 140ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 253ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 108ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 351ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 1112ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 371ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 387ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 368ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 219ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 150ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1207ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1368ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 126ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 242ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 185ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 870ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 823ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 916ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1135ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 910ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1317ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1016ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 863ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 998ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1003ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 864ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 879ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 820ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 889ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [FAIL]  15112ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0 — TimeoutError: The read operation timed out
- `xstocks.assets.p0` [ok] 200 9139ms https://api.xstocks.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [FAIL]  15054ms https://api.xstocks.fi/api/v2/public/assets?pageSize=100&page=1 — TimeoutError: The read operation timed out
- `xstocks.price.INDIx` [FAIL]  12037ms https://api.xstocks.fi/api/v2/public/assets/INDIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.QUBTx` [FAIL]  12039ms https://api.xstocks.fi/api/v2/public/assets/QUBTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METCx` [FAIL]  12042ms https://api.xstocks.fi/api/v2/public/assets/METCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WRLDx` [FAIL]  12047ms https://api.xstocks.fi/api/v2/public/assets/WRLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WGSx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/WGSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PCTx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/PCTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.XRXx` [FAIL]  12053ms https://api.xstocks.fi/api/v2/public/assets/XRXx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.FLNCx` [FAIL]  12060ms https://api.xstocks.fi/api/v2/public/assets/FLNCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.QUBTx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.METCx` [FAIL]  12046ms https://api.xstocks.fi/api/v2/public/assets/METCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.XRXx` [FAIL]  12038ms https://api.xstocks.fi/api/v2/public/assets/XRXx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.WGSx` [FAIL]  12042ms https://api.xstocks.fi/api/v2/public/assets/WGSx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.INDIx` [FAIL]  12053ms https://api.xstocks.fi/api/v2/public/assets/INDIx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.PCTx` [FAIL]  12047ms https://api.xstocks.fi/api/v2/public/assets/PCTx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.WRLDx` [FAIL]  12054ms https://api.xstocks.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.FLNCx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.PCTx` [ok] 200 3850ms https://api.xstocks.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.METCx` [FAIL]  12047ms https://api.xstocks.fi/api/v2/public/assets/METCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.WGSx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/WGSx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.QUBTx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.XRXx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/XRXx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.INDIx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/INDIx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.WRLDx` [FAIL]  12044ms https://api.xstocks.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.FLNCx` [FAIL]  12042ms https://api.xstocks.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.WYFIx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/WYFIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DRSx` [FAIL]  12045ms https://api.xstocks.fi/api/v2/public/assets/DRSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AIx` [FAIL]  12045ms https://api.xstocks.fi/api/v2/public/assets/AIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BETRx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/BETRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SAILx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/SAILx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SCIx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/SCIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BSYx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/BSYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GSATx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/GSATx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WYFIx` [FAIL]  12038ms https://api.xstocks.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.DRSx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/DRSx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.SAILx` [FAIL]  12043ms https://api.xstocks.fi/api/v2/public/assets/SAILx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.AIx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/AIx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.BETRx` [FAIL]  12046ms https://api.xstocks.fi/api/v2/public/assets/BETRx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.GSATx` [FAIL]  12038ms https://api.xstocks.fi/api/v2/public/assets/GSATx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.SCIx` [FAIL]  12053ms https://api.xstocks.fi/api/v2/public/assets/SCIx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.BSYx` [FAIL]  12058ms https://api.xstocks.fi/api/v2/public/assets/BSYx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.BETRx` [ok] 200 2771ms https://api.xstocks.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.DRSx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/DRSx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.SAILx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/SAILx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.AIx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/AIx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.GSATx` [FAIL]  12044ms https://api.xstocks.fi/api/v2/public/assets/GSATx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.BSYx` [FAIL]  12042ms https://api.xstocks.fi/api/v2/public/assets/BSYx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.SCIx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/SCIx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.MPx` [FAIL]  12054ms https://api.xstocks.fi/api/v2/public/assets/MPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DVAx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/DVAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DYx` [FAIL]  12037ms https://api.xstocks.fi/api/v2/public/assets/DYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DCIx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/DCIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.RYANx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/RYANx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GDDYx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/GDDYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BXPx` [FAIL]  12055ms https://api.xstocks.fi/api/v2/public/assets/BXPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.FRHCx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/FRHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MPx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/MPx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.DVAx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/DVAx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.DCIx` [FAIL]  12047ms https://api.xstocks.fi/api/v2/public/assets/DCIx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.DYx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/DYx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.GDDYx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.BXPx` [FAIL]  12042ms https://api.xstocks.fi/api/v2/public/assets/BXPx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.RYANx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/RYANx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.FRHCx` [FAIL]  12047ms https://api.xstocks.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.MPx` [FAIL]  12046ms https://api.xstocks.fi/api/v2/public/assets/MPx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.DVAx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/DVAx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.DCIx` [ok] 200 5915ms https://api.xstocks.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.mult.DYx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/DYx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.GDDYx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.RYANx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/RYANx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.BXPx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/BXPx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.FRHCx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.WMSx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/WMSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AMx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/AMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.FDSx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/FDSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SFx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/SFx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AXSMx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/AXSMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SMTCx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/SMTCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ALSNx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/ALSNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.EGPx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/EGPx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AXSMx` [ok] 200 355ms https://api.xstocks.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.circ.WMSx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/WMSx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.AMx` [FAIL]  12039ms https://api.xstocks.fi/api/v2/public/assets/AMx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.FDSx` [FAIL]  12044ms https://api.xstocks.fi/api/v2/public/assets/FDSx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.SFx` [FAIL]  12046ms https://api.xstocks.fi/api/v2/public/assets/SFx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.ALSNx` [FAIL]  12045ms https://api.xstocks.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.SMTCx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.EGPx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/EGPx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.AXSMx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.WMSx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/WMSx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.AMx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/AMx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.FDSx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/FDSx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.AEISx` [ok] 200 5022ms https://api.xstocks.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.mult.SMTCx` [FAIL]  12042ms https://api.xstocks.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.ALSNx` [FAIL]  12045ms https://api.xstocks.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.SFx` [FAIL]  12046ms https://api.xstocks.fi/api/v2/public/assets/SFx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.EGPx` [FAIL]  12047ms https://api.xstocks.fi/api/v2/public/assets/EGPx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.BPOPx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/BPOPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.TTMIx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/TTMIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DPZx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/DPZx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AEISx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/AEISx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.KTOSx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/KTOSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HRLx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/HRLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SEICx` [FAIL]  12040ms https://api.xstocks.fi/api/v2/public/assets/SEICx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PAGx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/PAGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BPOPx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.TTMIx` [FAIL]  12046ms https://api.xstocks.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.PAGx` [ok] 200 5120ms https://api.xstocks.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.circ.KTOSx` [ok] 200 5265ms https://api.xstocks.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.circ.DPZx` [FAIL]  12043ms https://api.xstocks.fi/api/v2/public/assets/DPZx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.HRLx` [ok] 200 6262ms https://api.xstocks.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.mult.TTMIx` [ok] 200 4423ms https://api.xstocks.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.circ.SEICx` [ok] 200 7507ms https://api.xstocks.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.mult.AEISx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/AEISx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.BPOPx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.PAGx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/PAGx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.KTOSx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.DPZx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/DPZx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.HRLx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/HRLx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.HIIx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/HIIx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SEICx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/SEICx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.EHCx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/EHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GFLx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/GFLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ARx` [FAIL]  12047ms https://api.xstocks.fi/api/v2/public/assets/ARx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MGMx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/MGMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DOCUx` [FAIL]  12037ms https://api.xstocks.fi/api/v2/public/assets/DOCUx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HALOx` [FAIL]  12054ms https://api.xstocks.fi/api/v2/public/assets/HALOx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HIIx` [FAIL]  12041ms https://api.xstocks.fi/api/v2/public/assets/HIIx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.WTRGx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/WTRGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.EHCx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/EHCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.GFLx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/GFLx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.DOCUx` [ok] 200 9247ms https://api.xstocks.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.circ.ARx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/ARx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.MGMx` [FAIL]  12054ms https://api.xstocks.fi/api/v2/public/assets/MGMx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.HALOx` [FAIL]  12047ms https://api.xstocks.fi/api/v2/public/assets/HALOx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.HIIx` [FAIL]  12043ms https://api.xstocks.fi/api/v2/public/assets/HIIx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.WTRGx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.EHCx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/EHCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.GFLx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/GFLx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.WTRGx` [ok] 200 5940ms https://api.xstocks.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.mult.DOCUx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.ARx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/ARx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.MGMx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/MGMx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.HALOx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/HALOx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.AFGx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/AFGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HUBSx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/HUBSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AMKRx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/AMKRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GMEDx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/GMEDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.JKHYx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/JKHYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.IESCx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/IESCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.OCx` [FAIL]  12054ms https://api.xstocks.fi/api/v2/public/assets/OCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CRx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/CRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AFGx` [FAIL]  12041ms https://api.xstocks.fi/api/v2/public/assets/AFGx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.HUBSx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.AMKRx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.GMEDx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.JKHYx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.IESCx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/IESCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.OCx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/OCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.CRx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/CRx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.AFGx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/AFGx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.HUBSx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.AMKRx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.GMEDx` [FAIL]  12047ms https://api.xstocks.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.JKHYx` [ok] 200 10378ms https://api.xstocks.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.mult.IESCx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/IESCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.OCx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/OCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.CRx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/CRx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.BMRNx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/BMRNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.JEFx` [FAIL]  12055ms https://api.xstocks.fi/api/v2/public/assets/JEFx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AMHx` [FAIL]  12053ms https://api.xstocks.fi/api/v2/public/assets/AMHx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.FIVEx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/FIVEx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ITx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/ITx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MDGLx` [FAIL]  12047ms https://api.xstocks.fi/api/v2/public/assets/MDGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.VNOMx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/VNOMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.UHALx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/UHALx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AMHx` [ok] 200 6315ms https://api.xstocks.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.circ.BMRNx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.JEFx` [FAIL]  12037ms https://api.xstocks.fi/api/v2/public/assets/JEFx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.FIVEx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.ITx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/ITx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.MDGLx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.VNOMx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.UHALx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/UHALx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.AMHx` [FAIL]  12054ms https://api.xstocks.fi/api/v2/public/assets/AMHx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.BMRNx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.JEFx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/JEFx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.FIVEx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.ITx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/ITx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.MDGLx` [FAIL]  12039ms https://api.xstocks.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.VNOMx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.UHALx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/UHALx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.AHRx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/AHRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.IVZx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/IVZx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CORTx` [FAIL]  12053ms https://api.xstocks.fi/api/v2/public/assets/CORTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.NWSAx` [FAIL]  12491ms https://api.xstocks.fi/api/v2/public/assets/NWSAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.STRLx` [FAIL]  12506ms https://api.xstocks.fi/api/v2/public/assets/STRLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CORTx` [ok] 200 7804ms https://api.xstocks.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.price.AURx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/AURx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.NWSAx` [FAIL] 502 3304ms https://api.xstocks.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.Hx` [FAIL]  12054ms https://api.xstocks.fi/api/v2/public/assets/Hx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CORTx` [ok] 200 875ms https://api.xstocks.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.ARWRx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/ARWRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AHRx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/AHRx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.IVZx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/IVZx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.AHRx` [ok] 200 3274ms https://api.xstocks.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.circ.STRLx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/STRLx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.AURx` [FAIL]  12044ms https://api.xstocks.fi/api/v2/public/assets/AURx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.NWSAx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.Hx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/Hx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.GWREx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/GWREx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ARWRx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.IVZx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/IVZx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.NWSx` [FAIL]  12052ms https://api.xstocks.fi/api/v2/public/assets/NWSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.STRLx` [ok] 200 9423ms https://api.xstocks.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.mult.AURx` [FAIL]  12039ms https://api.xstocks.fi/api/v2/public/assets/AURx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.MANHx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/MANHx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.Hx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/Hx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.GWREx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/GWREx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.ARWRx` [FAIL]  12048ms https://api.xstocks.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.CNAx` [FAIL] 503 206ms https://api.xstocks.fi/api/v2/public/assets/CNAx/price-data — HTTP 503 Service Unavailable
- `xstocks.circ.CNAx` [FAIL] 503 207ms https://api.xstocks.fi/api/v2/public/assets/CNAx/circulating-supply?format=object — HTTP 503 Service Unavailable
- `xstocks.mult.CNAx` [FAIL] 503 198ms https://api.xstocks.fi/api/v2/public/assets/CNAx/multiplier?network=Solana — HTTP 503 Service Unavailable
- `xstocks.price.CACIx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/CACIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CACIx` [FAIL] 503 211ms https://api.xstocks.fi/api/v2/public/assets/CACIx/circulating-supply?format=object — HTTP 503 Service Unavailable
- `xstocks.circ.NWSx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/NWSx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.BAXx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/BAXx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CACIx` [ok] 200 5039ms https://api.xstocks.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.price.RVTYx` [FAIL]  12039ms https://api.xstocks.fi/api/v2/public/assets/RVTYx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MANHx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/MANHx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.TXRHx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/TXRHx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.GWREx` [FAIL]  12050ms https://api.xstocks.fi/api/v2/public/assets/GWREx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.NWSx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/NWSx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.BAXx` [FAIL]  12053ms https://api.xstocks.fi/api/v2/public/assets/BAXx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.RVTYx` [FAIL]  12055ms https://api.xstocks.fi/api/v2/public/assets/RVTYx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.MANHx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/MANHx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.TXRHx` [FAIL]  12051ms https://api.xstocks.fi/api/v2/public/assets/TXRHx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.BAXx` [FAIL]  12043ms https://api.xstocks.fi/api/v2/public/assets/BAXx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.RVTYx` [FAIL]  12053ms https://api.xstocks.fi/api/v2/public/assets/RVTYx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.TXRHx` [FAIL]  12049ms https://api.xstocks.fi/api/v2/public/assets/TXRHx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `llama.protocol.xstocks` [ok] 200 904ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 220ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.PCTx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.METCx` [ok] 200 97ms https://lite-api.jup.ag/tokens/v2/search?query=METCx
- `jup.tokens.search.WGSx` [ok] 200 98ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.QUBTx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.XRXx` [ok] 200 96ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.INDIx` [ok] 200 107ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.WRLDx` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.FLNCx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jito.tip_floor` [ok] 200 530ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 453ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 129ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 251ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 343ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 218ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 205ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 1315ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
