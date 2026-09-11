# Borealis — Solana ecosystem report

**Generated** 2026-09-11T02:06:38Z · 2026-09-10 19:06:38 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-11T02:06:28Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h -1.74%; DEX 24h $2.95B · 1d -2% · vs-7d-ago +20%; slot 314 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +24.13%. (threshold: `|7d %| >= 20`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -1.74%, DeFiLlama TVL 1d -0.13%, DEX 1d -1.76%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **INFO · Daily active addresses vs 30d median** — Current 987,010.00 is +25.1% vs 30d median 789,133.50 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 446,039,118 |
| Block height | 424,082,427 |
| Block time | 2026-09-11T02:06:28Z |
| Epoch | 1,032 (49.80% · slot 215,120/432,000) |
| Mean TPS (last ~3,600s) | 3,793.1 |
| Mean non-vote TPS | 1,655.9 |
| Median TPS (same window) | 3,796.2 |
| Mean slot time | 314.4 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 547,234,209,579 |
| Circulating supply | 586,537,830 SOL |
| Total supply | 633,830,395 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 677 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,082,043 SOL |
| Delinquent stake | 106,170.00 SOL (0.024%) |
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

- `scs2Ra91…` · 58.59K SOL · commission 10% · lag 160036 slots
- `mrgn4atx…` · 19.89K SOL · commission 0% · lag 74879 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 184961 slots
- `inWVrrYJ…` · 8.46K SOL · commission 0% · lag 340021 slots
- `xLabscif…` · 3.36K SOL · commission 5% · lag 2250745 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 2073196 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 243956 slots
- `4GEEKSwu…` · 326.50 SOL · commission 5% · lag 229506 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 16503435 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 446039118 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 1200107 slots
- `4kdjgZKJ…` · 1.05 SOL · commission 100% · lag 446039118 slots

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
| Jito tip-floor run-rate (NOT REV) | $47.00K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 47002 USD; at p95 floor → 454899 USD. |
| Protocol fees 24h | $14.68M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=10025 |
| p90 / p99 | 0.000010 / 0.000281 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $99.36 | coingecko.simple_price |
| 24h change | -1.74% | coingecko.simple_price |
| Market cap | $58.23B | coingecko.simple_price |
| 24h volume | $3.00B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.75B |
| TVL 1d / 7d / 30d | -0.13% / -2.93% / +18.11% |
| DEX volume 24h | $2.95B · 1d -1.76% · vs-7d-ago +19.84% |
| 7d DEX volume | $16.61B · +6.41% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.68M |
| Fees 1d / 7d | -6.59% / +24.13% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $468.14M | +37.30% |
| BisonFi | $402.77M | 0.00% |
| Raydium AMM | $362.49M | -16.69% |
| HumidiFi | $285.64M | 0.00% |
| Tessera V | $248.02M | 0.00% |
| Meteora DLMM | $220.43M | -31.60% |
| Orca DEX | $176.72M | +4.24% |
| Manifest Trade | $149.05M | -1.92% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.52B | -2.24% | -4.27% |
| Kamino Lend | Lending | $1.30B | -0.95% | -2.83% |
| Raydium AMM | Dexs | $1.11B | -2.85% | -1.92% |
| Jupiter Lend | Lending | $1.07B | +2.74% | -2.37% |
| Binance Staked SOL | Liquid Staking | $1.03B | -2.32% | -5.36% |
| Jito Liquid Staking | Liquid Staking | $1.02B | -2.22% | -4.00% |
| BlackRock BUIDL | RWA | $992.51M | -0.68% | -0.63% |
| Jupiter Perpetual Exchange | Derivatives | $737.26M | -0.76% | -4.15% |
| Jupiter Staked SOL | Liquid Staking | $512.58M | -3.20% | -5.64% |
| Sentora Curator | Risk Curators | $387.91M | -0.29% | -3.69% |

## Stablecoins

Solana circulating pegged-USD: **$15.98B**
(1d -1.33% · 7d -1.74%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.99B | -1.64% |
| USDT · Tether | $2.68B | -3.25% |
| USDGO · USDGO | $1.38B | +0.73% |
| USD1 · World Liberty Financial USD | $1.28B | -0.00% |
| BUIDL · BlackRock USD | $992.51M | +0.03% |
| PYUSD · PayPal USD | $746.58M | -1.35% |
| USDG · Global Dollar | $599.04M | -0.43% |
| USDe · Ethena USDe | $536.49M | +0.16% |

## Tokenized equities (xStocks)

TimeoutError: The read operation timed out
Listed 0 · Solana deployments 0 · priced 0 · priced-subset mcap — (lower bound, not a census).
24h volume $96.97M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok None / mcap_computable None of attempted None; missing multiplier → mcap omitted, never silent 1.0).  

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.92B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.51M
- **OnRe** (RWA) — $309.41M
- **Ondo Yield Assets** (RWA) — $179.95M
- **Huma Finance V2** (RWA) — $168.42M
- **Hastra** (RWA) — $152.86M
- **Plume Vaults** (RWA) — $27.20M
- **Ondo Global Markets** (RWA) — $25.08M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.37M

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

_As of 2026-09-11 (2026-09-10 19:06:38 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~314 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~314 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **Tokenized equities (xStocks)** — TimeoutError: The read operation timed out
- **xStocks** — asset list failed on backed.fi and xstocks.fi

## Sources this run

- `rpc.getHealth` [ok] 200 261ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 340ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 225ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 239ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 207ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7948ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 397ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 127ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 83ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 122ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 68ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 1010ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 70ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 299ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 109ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 102ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 126ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 457ms https://solana.com/data
- `solana.com.databricks` [ok] 200 533ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 843ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 143ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 203ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 111ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 496ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 817ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 362ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 372ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 362ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 217ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 189ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1791ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1325ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 59ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 205ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 188ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 889ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 947ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 809ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1058ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 996ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1335ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 947ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 919ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 830ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1216ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 869ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 880ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 882ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 889ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [FAIL]  15134ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0 — TimeoutError: The read operation timed out
- `xstocks.assets.p0` [FAIL]  15122ms https://api.xstocks.fi/api/v2/public/assets?pageSize=100&page=0 — TimeoutError: The read operation timed out
- `llama.protocol.xstocks` [ok] 200 66ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 199ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jito.tip_floor` [ok] 200 160ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 511ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 135ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 185ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 205ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 186ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 193ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 195ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
