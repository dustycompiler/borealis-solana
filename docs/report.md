# Borealis — Solana ecosystem report

**Generated** 2026-09-10T20:50:30Z · 2026-09-10 13:50:30 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-10T20:50:20Z · **RPC health** `ok`
**Health score** 91 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h -2.23%; DEX 24h $3.00B · 1d +11% · vs-7d-ago +31%; slot 316 ms
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
| Slot | 445,979,133 |
| Block height | 424,022,468 |
| Block time | 2026-09-10T20:50:20Z |
| Epoch | 1,032 (35.91% · slot 155,133/432,000) |
| Mean TPS (last ~3,600s) | 4,131.3 |
| Mean non-vote TPS | 2,005.2 |
| Median TPS (same window) | 4,172.0 |
| Mean slot time | 316.3 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 547,160,842,918 |
| Circulating supply | 586,335,316 SOL |
| Total supply | 633,830,589 SOL |
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
| Activated stake | 436,638,296 SOL |
| Delinquent stake | 2,549,916.98 SOL (0.581%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.35% / 35.69% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 3.99% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.32M SOL | 3.74% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.52M SOL | 2.87% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.38M SOL | 2.61% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.19% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.28M SOL | 2.13% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.34M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.88M SOL | 1.58% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.55M SOL | 1.50% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.95M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `ana2y2Yv…` · 2.44M SOL · commission 0% · lag 409 slots
- `scs2Ra91…` · 58.59K SOL · commission 10% · lag 100051 slots
- `mrgn4atx…` · 19.89K SOL · commission 0% · lag 14894 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 124976 slots
- `inWVrrYJ…` · 8.46K SOL · commission 0% · lag 280036 slots
- `xLabscif…` · 3.36K SOL · commission 5% · lag 2190760 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 2013211 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 183971 slots
- `4GEEKSwu…` · 326.50 SOL · commission 5% · lag 169521 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 16443450 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 445979133 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 1140122 slots

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
| Jito tip-floor run-rate (NOT REV) | $38.35K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 38353 USD; at p95 floor → 89998975 USD. |
| Protocol fees 24h | $15.72M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9961 |
| p90 / p99 | 0.000011 / 0.000195 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $99.90 | coingecko.simple_price |
| 24h change | -2.23% | coingecko.simple_price |
| Market cap | $58.59B | coingecko.simple_price |
| 24h volume | $3.25B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.78B |
| TVL 1d / 7d / 30d | -2.89% / +1.21% / +19.21% |
| DEX volume 24h | $3.00B · 1d +10.69% · vs-7d-ago +31.06% |
| 7d DEX volume | $17.54B · +4.09% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $15.72M |
| Fees 1d / 7d | -5.90% / +39.44% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| BisonFi | $402.77M | +61.55% |
| Raydium AMM | $350.36M | -0.08% |
| PumpSwap | $340.96M | -53.74% |
| Meteora DLMM | $322.25M | +35.54% |
| HumidiFi | $285.64M | +86.20% |
| Tessera V | $248.02M | +58.67% |
| Orca DEX | $170.35M | +10.89% |
| Manifest Trade | $155.08M | +24.36% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.53B | -3.70% | -4.56% |
| Kamino Lend | Lending | $1.32B | -2.21% | -0.71% |
| Raydium AMM | Dexs | $1.11B | -3.29% | +1.50% |
| Jupiter Lend | Lending | $1.07B | -2.88% | -3.07% |
| Binance Staked SOL | Liquid Staking | $1.04B | -3.65% | -5.07% |
| Jito Liquid Staking | Liquid Staking | $1.02B | -3.70% | -3.83% |
| BlackRock BUIDL | RWA | $992.51M | -1.38% | -0.01% |
| Jupiter Perpetual Exchange | Derivatives | $739.32M | -1.61% | -4.30% |
| Jupiter Staked SOL | Liquid Staking | $516.39M | -3.78% | -5.40% |
| Sentora Curator | Risk Curators | $387.95M | -0.35% | -8.10% |

## Stablecoins

Solana circulating pegged-USD: **$15.88B**
(1d -0.32% · 7d +2.96%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.91B | -3.79% |
| USDT · Tether | $2.67B | -3.25% |
| USDGO · USDGO | $1.38B | +1.28% |
| USD1 · World Liberty Financial USD | $1.28B | +0.00% |
| BUIDL · BlackRock USD | $992.51M | +0.50% |
| PYUSD · PayPal USD | $733.90M | -2.50% |
| USDG · Global Dollar | $595.74M | +0.88% |
| USDe · Ethena USDe | $536.50M | -0.00% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $105.05M (lower bound, not a census).
24h volume $99.54M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.92B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.51M
- **OnRe** (RWA) — $308.52M
- **Ondo Yield Assets** (RWA) — $180.03M
- **Huma Finance V2** (RWA) — $169.24M
- **Hastra** (RWA) — $152.87M
- **Plume Vaults** (RWA) — $27.20M
- **Ondo Global Markets** (RWA) — $25.18M
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

_As of 2026-09-10 (2026-09-10 13:50:30 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 79ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 85ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 81ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 141ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 37ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7143ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 118ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 126ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 48ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 81ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 43ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 40ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1084ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 118ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 206ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 79ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 110ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 533ms https://solana.com/data
- `solana.com.databricks` [ok] 200 97ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 499ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 117ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 298ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 97ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 229ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 650ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 101ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 109ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 523ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 423ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 698ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1687ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1570ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 45ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 71ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 80ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 313ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 347ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 484ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 476ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 382ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 391ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 61ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 571ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 365ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 368ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 483ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 395ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 406ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 390ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 286ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1623ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2500ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1795ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1680ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1559ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1744ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1178ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 2919ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.COINx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.XRXx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.INDIx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WGSx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.circ.XRXx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 439ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.XRXx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.FLNCx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.SPYx` [ok] 200 543ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.COINx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.PCTx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.FLNCx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.price.WRLDx` [ok] 200 954ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.circ.PCTx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 778ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.WRLDx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 736ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 591ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 1174ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 526ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.price.QUBTx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.WYFIx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.WGSx` [ok] 200 1555ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 624ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.METCx` [ok] 200 696ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.METCx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.DRSx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.mult.METCx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.WYFIx` [ok] 200 591ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 1917ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.SAILx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.price.BETRx` [ok] 200 1158ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.SAILx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.mult.SAILx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 596ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.SCIx` [ok] 200 1052ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.price.GSATx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.price.BSYx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.mult.SPYx` [ok] 200 987ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.GSATx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 1922ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.DRSx` [ok] 200 1470ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 1326ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.DVAx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.price.AIx` [ok] 200 2560ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.price.MPx` [ok] 200 791ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.mult.BETRx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.circ.MPx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.circ.BSYx` [ok] 200 1272ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.price.DCIx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.circ.AIx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.MPx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.circ.SCIx` [ok] 200 1796ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.price.RYANx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.price.BXPx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.mult.BSYx` [ok] 200 651ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.price.DYx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.mult.GSATx` [ok] 200 1972ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 966ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.price.GDDYx` [ok] 200 1186ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.circ.DVAx` [ok] 200 1340ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.circ.DYx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.mult.DVAx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.mult.SCIx` [ok] 200 1022ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.mult.DCIx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.mult.DYx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.price.FDSx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.price.WMSx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.price.ALSNx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.price.AMx` [ok] 200 976ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.FRHCx` [ok] 200 1414ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.circ.BXPx` [ok] 200 2364ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.circ.WMSx` [ok] 200 1337ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.circ.GDDYx` [ok] 200 2181ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.circ.ALSNx` [ok] 200 1237ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.mult.WMSx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.mult.BXPx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.mult.GDDYx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.mult.ALSNx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.price.SMTCx` [ok] 200 558ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.price.SFx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.price.AXSMx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.price.EGPx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.circ.FDSx` [ok] 200 2035ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.price.BPOPx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.circ.AMx` [ok] 200 1440ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.circ.AXSMx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.mult.AXSMx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.price.TTMIx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.mult.AMx` [ok] 200 575ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.circ.TTMIx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.circ.SFx` [ok] 200 1085ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.circ.EGPx` [ok] 200 1091ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.mult.SFx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.mult.TTMIx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.DPZx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.price.KTOSx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.circ.DPZx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.circ.KTOSx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.price.AEISx` [ok] 200 1033ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.mult.DPZx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.circ.AEISx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.price.HRLx` [ok] 200 997ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.price.PAGx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.mult.AEISx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.circ.PAGx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.circ.RYANx` [ok] 200 5711ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.circ.SMTCx` [ok] 200 2658ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.price.SEICx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.mult.RYANx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.mult.KTOSx` [ok] 200 1187ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.price.HIIx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.mult.EGPx` [ok] 200 1773ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 2644ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.price.EHCx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.price.GFLx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.circ.HIIx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.circ.SEICx` [ok] 200 819ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.circ.HRLx` [ok] 200 1567ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.circ.GFLx` [ok] 200 606ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.GFLx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.mult.BPOPx` [ok] 200 1458ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.price.ARx` [ok] 200 657ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.circ.ARx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.price.MGMx` [ok] 200 724ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.mult.HIIx` [ok] 200 2024ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.mult.ARx` [ok] 200 513ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.circ.MGMx` [ok] 200 578ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.price.HALOx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.mult.MGMx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.circ.HALOx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.mult.SMTCx` [ok] 200 3478ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.price.DOCUx` [ok] 200 689ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.mult.HALOx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.price.AFGx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.circ.AFGx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.circ.EHCx` [ok] 200 3333ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.mult.AFGx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.price.AMKRx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.mult.SEICx` [ok] 200 3468ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.mult.PAGx` [ok] 200 4413ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.circ.AMKRx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.price.JKHYx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.circ.DOCUx` [ok] 200 952ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.price.GMEDx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.mult.AMKRx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.price.HUBSx` [ok] 200 1005ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.price.WTRGx` [ok] 200 1294ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.IESCx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.mult.DOCUx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.circ.WTRGx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.circ.IESCx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.circ.HUBSx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.mult.EHCx` [ok] 200 1316ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.HUBSx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.circ.JKHYx` [ok] 200 901ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.price.BMRNx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.mult.JKHYx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.price.JEFx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.price.CRx` [ok] 200 550ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.circ.BMRNx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.circ.JEFx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.mult.JEFx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.mult.BMRNx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 1616ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.price.FIVEx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.price.OCx` [ok] 200 1776ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.mult.WTRGx` [ok] 200 1833ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.circ.FIVEx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.circ.CRx` [ok] 200 901ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.price.AMHx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.price.MDGLx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.mult.IESCx` [ok] 200 2150ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.circ.AMHx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.price.VNOMx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.circ.VNOMx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.circ.OCx` [ok] 200 809ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.price.ITx` [ok] 200 877ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.mult.VNOMx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.circ.MDGLx` [ok] 200 751ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.mult.OCx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.price.UHALx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.circ.ITx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.mult.CRx` [ok] 200 954ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.circ.UHALx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.price.AHRx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.circ.AHRx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.mult.ITx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.price.IVZx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.price.CORTx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.circ.IVZx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.mult.IVZx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.circ.CORTx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.mult.AHRx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.NWSAx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.price.STRLx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.mult.FIVEx` [ok] 200 1921ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.mult.CORTx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.AURx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.circ.NWSAx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.mult.UHALx` [ok] 200 1457ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.mult.NWSAx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.circ.STRLx` [ok] 200 889ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 768ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.mult.HRLx` [ok] 200 8458ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.mult.STRLx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.mult.AURx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.price.NWSx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.price.GWREx` [ok] 200 645ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.price.MANHx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.price.ARWRx` [ok] 200 783ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.circ.GWREx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.price.Hx` [ok] 200 1398ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.price.CACIx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.circ.MANHx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.circ.ARWRx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.circ.Hx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.mult.Hx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.mult.MANHx` [ok] 200 506ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.price.BAXx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.NWSx` [ok] 200 948ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 820ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.circ.BAXx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.NWSx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.MDGLx` [ok] 200 4375ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.circ.CACIx` [ok] 200 2042ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.mult.AMHx` [ok] 200 5697ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 53ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 294ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INDIx` [ok] 200 65ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 74ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.WYFIx` [ok] 200 70ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.BETRx` [ok] 200 77ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.FLNCx` [ok] 200 74ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.XRXx` [ok] 200 77ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.PCTx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jito.tip_floor` [ok] 200 189ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 400ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 87ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 49ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 56ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 75ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 41ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 1498ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
