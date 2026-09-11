# Borealis — Solana ecosystem report

**Generated** 2026-09-11T07:07:26Z · 2026-09-11 00:07:26 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-11T07:07:16Z · **RPC health** `ok`
**Health score** 89 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h -1.72%; DEX 24h $2.95B · 1d -2% · vs-7d-ago +20%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +25.31%. (threshold: `|7d %| >= 20`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -1.72%, DeFiLlama TVL 1d -1.11%, DEX 1d -1.73%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **INFO · Daily active addresses vs 30d median** — Current 987,010.00 is +24.7% vs 30d median 791,527.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 446,096,197 |
| Block height | 424,139,447 |
| Block time | 2026-09-11T07:07:16Z |
| Epoch | 1,032 (63.01% · slot 272,201/432,000) |
| Mean TPS (last ~3,600s) | 3,541.1 |
| Mean non-vote TPS | 1,436.8 |
| Median TPS (same window) | 3,513.1 |
| Mean slot time | 315.4 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 547,301,679,195 |
| Circulating supply | 586,537,653 SOL |
| Total supply | 633,830,218 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 668 |
| Delinquent | 21 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 436,345,974 SOL |
| Delinquent stake | 2,842,239.28 SOL (0.647%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 79 |
| Top 10 / 20 stake share | 24.37% / 35.71% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 4.00% | 7% | 0 |
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

- `pSo1KZXg…` · 1.64M SOL · commission 4% · lag 2622 slots
- `3YVoK8UN…` · 409.65K SOL · commission 5% · lag 3750 slots
- `ECNnK4Vj…` · 138.57K SOL · commission 5% · lag 11078 slots
- `EPFZFVrX…` · 114.39K SOL · commission 0% · lag 6320 slots
- `FdH9QEQB…` · 99.92K SOL · commission 0% · lag 10860 slots
- `EBk678aQ…` · 95.16K SOL · commission 5% · lag 8329 slots
- `mrgn2vUP…` · 90.78K SOL · commission 0% · lag 1305 slots
- `VicAQ3U2…` · 84.38K SOL · commission 5% · lag 1624 slots
- `SANDCxXB…` · 59.04K SOL · commission 5% · lag 1525 slots
- `scs2Ra91…` · 58.59K SOL · commission 10% · lag 217115 slots
- `mrgn4atx…` · 19.89K SOL · commission 0% · lag 40961 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 242040 slots

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
| Jito tip-floor run-rate (NOT REV) | $49.43K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 49430 USD; at p95 floor → 1239163 USD. |
| Protocol fees 24h | $14.82M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9979 |
| p90 / p99 | 0.000010 / 0.000105 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $99.82 | coingecko.simple_price |
| 24h change | -1.72% | coingecko.simple_price |
| Market cap | $58.53B | coingecko.simple_price |
| 24h volume | $3.04B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.79B |
| TVL 1d / 7d / 30d | -1.11% / -2.36% / +18.82% |
| DEX volume 24h | $2.95B · 1d -1.73% · vs-7d-ago +19.88% |
| 7d DEX volume | $16.62B · +6.42% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.82M |
| Fees 1d / 7d | -5.70% / +25.31% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $468.14M | +37.30% |
| Raydium AMM | $406.06M | -6.68% |
| BisonFi | $402.77M | 0.00% |
| HumidiFi | $285.64M | 0.00% |
| Tessera V | $248.02M | 0.00% |
| Meteora DLMM | $220.43M | -31.60% |
| Orca DEX | $206.08M | +21.55% |
| Manifest Trade | $146.78M | -3.41% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.53B | -2.08% | -3.35% |
| Kamino Lend | Lending | $1.33B | -0.70% | -0.10% |
| Raydium AMM | Dexs | $1.11B | -1.26% | -0.68% |
| Jupiter Lend | Lending | $1.07B | -1.18% | -1.74% |
| Binance Staked SOL | Liquid Staking | $1.04B | -2.24% | -3.87% |
| Jito Liquid Staking | Liquid Staking | $1.02B | -2.05% | -2.64% |
| BlackRock BUIDL | RWA | $992.51M | -0.68% | -0.63% |
| Jupiter Perpetual Exchange | Derivatives | $740.49M | -1.07% | -2.94% |
| Jupiter Staked SOL | Liquid Staking | $516.38M | -2.21% | -3.90% |
| Sentora Curator | Risk Curators | $388.08M | -0.35% | -3.39% |

## Stablecoins

Solana circulating pegged-USD: **$15.98B**
(1d -1.32% · 7d -1.73%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.00B | -1.43% |
| USDT · Tether | $2.67B | -3.25% |
| USDGO · USDGO | $1.38B | +0.73% |
| USD1 · World Liberty Financial USD | $1.28B | -0.00% |
| BUIDL · BlackRock USD | $992.51M | +0.03% |
| PYUSD · PayPal USD | $736.18M | -2.72% |
| USDG · Global Dollar | $598.21M | -0.59% |
| USDe · Ethena USDe | $536.45M | +0.16% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $105.53M (lower bound, not a census).
24h volume $103.13M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.92B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.51M
- **OnRe** (RWA) — $309.54M
- **Ondo Yield Assets** (RWA) — $180.09M
- **Huma Finance V2** (RWA) — $169.40M
- **Hastra** (RWA) — $152.86M
- **Plume Vaults** (RWA) — $27.20M
- **Ondo Global Markets** (RWA) — $25.27M
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

_As of 2026-09-11 (2026-09-11 00:07:26 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 476ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 481ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 457ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 511ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 469ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6660ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 938ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 108ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 27ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 90ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 22ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 40ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 32ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 72ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 36ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 53ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 92ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 425ms https://solana.com/data
- `solana.com.databricks` [ok] 200 45ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 503ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 99ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 256ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 42ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 280ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 1252ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 442ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 709ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 450ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 202ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 126ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1349ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1442ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 221ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 439ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 455ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1875ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1815ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1691ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1942ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1853ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1924ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1897ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2071ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1996ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2083ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1666ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2048ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1758ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1685ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1559ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1573ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1381ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1525ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1482ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1445ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1307ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1784ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.XRXx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.WRLDx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.INDIx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WGSx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.FLNCx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.QQQx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.SPYx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.COINx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.INDIx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.PCTx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.AIx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.price.QUBTx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.WYFIx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.price.DRSx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.circ.PCTx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 509ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.AIx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.DRSx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.price.METCx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.SCIx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.mult.PCTx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.SAILx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.price.GSATx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.circ.SCIx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.mult.BETRx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.price.MPx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.circ.SAILx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.price.BSYx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.circ.GSATx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.mult.SCIx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.DVAx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.price.DCIx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.circ.BSYx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.mult.SAILx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.GSATx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.DVAx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.price.GDDYx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.mult.BSYx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.price.BXPx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.mult.DVAx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.circ.GDDYx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.price.DYx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.circ.BXPx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.price.FRHCx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.price.WMSx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.circ.DYx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.mult.GDDYx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.mult.BXPx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.AMx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.MPx` [ok] 200 1027ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 859ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.price.FDSx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.circ.AMx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.MPx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 1053ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.price.ALSNx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.circ.RYANx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.mult.AMx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.price.SMTCx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.mult.DCIx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.circ.FDSx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.mult.RYANx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.circ.SMTCx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.price.SFx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.price.AXSMx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.price.EGPx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.circ.FRHCx` [ok] 200 1081ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.mult.SMTCx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.circ.WMSx` [ok] 200 1145ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.price.BPOPx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.mult.FDSx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.mult.WMSx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.TTMIx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.mult.FRHCx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.price.AEISx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.circ.TTMIx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.circ.SFx` [ok] 200 847ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.price.DPZx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.circ.ALSNx` [ok] 200 1361ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.mult.SFx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.mult.TTMIx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.circ.DPZx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.price.KTOSx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.circ.EGPx` [ok] 200 1134ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.price.HRLx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.circ.AXSMx` [ok] 200 1168ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 921ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.circ.KTOSx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.circ.HRLx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.mult.AXSMx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.mult.EGPx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.price.PAGx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.mult.BPOPx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.mult.KTOSx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.mult.HRLx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.SEICx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.circ.PAGx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.mult.DPZx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.price.GFLx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.circ.AEISx` [ok] 200 1066ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.price.HIIx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.price.EHCx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.price.ARx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.circ.SEICx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.price.MGMx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.mult.PAGx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.circ.EHCx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.mult.SEICx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.circ.ARx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.circ.MGMx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.mult.AEISx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.mult.HIIx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.price.HALOx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.mult.EHCx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.MGMx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.mult.ARx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.price.WTRGx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.AFGx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.circ.GFLx` [ok] 200 623ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.price.HUBSx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.price.GMEDx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.price.DOCUx` [ok] 200 551ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.circ.WTRGx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.price.AMKRx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.circ.HUBSx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.mult.GFLx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.circ.GMEDx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.mult.AFGx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.price.JKHYx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.GMEDx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.mult.HUBSx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.price.OCx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.circ.JKHYx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.price.IESCx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.price.CRx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.price.BMRNx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.circ.OCx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.circ.HALOx` [ok] 200 1008ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.circ.IESCx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.mult.JKHYx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.circ.AMKRx` [ok] 200 750ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.mult.OCx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.circ.BMRNx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.mult.IESCx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.JEFx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.circ.CRx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.circ.DOCUx` [ok] 200 1047ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.mult.AMKRx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.price.AMHx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.mult.BMRNx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.price.FIVEx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.circ.JEFx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.mult.CRx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.circ.AMHx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.price.ITx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.circ.FIVEx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.price.MDGLx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.mult.DOCUx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.price.VNOMx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.circ.ITx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.circ.MDGLx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.mult.FIVEx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.circ.VNOMx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.price.AHRx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.mult.HALOx` [ok] 200 920ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.price.UHALx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.mult.MDGLx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.mult.ITx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.VNOMx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.circ.AHRx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.circ.UHALx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.price.STRLx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.price.CORTx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.price.NWSAx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.price.AURx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.mult.UHALx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.mult.AHRx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.mult.JEFx` [ok] 200 869ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.circ.CORTx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.circ.STRLx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.circ.NWSAx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.price.ARWRx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.price.GWREx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.mult.CORTx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.mult.AURx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.mult.STRLx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.circ.ARWRx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.circ.GWREx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.price.MANHx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.price.CACIx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.mult.ARWRx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.mult.GWREx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.price.IVZx` [ok] 200 1098ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.price.Hx` [ok] 200 654ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.price.NWSx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.circ.MANHx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.circ.Hx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.price.BAXx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.IVZx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.mult.NWSAx` [ok] 200 620ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.circ.CACIx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.circ.NWSx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.circ.BAXx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.Hx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.mult.IVZx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.CACIx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 817ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 657ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INDIx` [ok] 200 116ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 112ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.WYFIx` [ok] 200 123ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.BETRx` [ok] 200 121ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.FLNCx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.XRXx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.PCTx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jito.tip_floor` [ok] 200 408ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 466ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 125ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 439ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 447ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 442ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 456ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 222ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
