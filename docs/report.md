# Borealis — Solana ecosystem report

**Generated** 2026-09-11T14:52:46Z · 2026-09-11 07:52:46 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-11T14:52:34Z · **RPC health** `ok`
**Health score** 92 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +2.99%; DEX 24h $2.92B · 1d -3% · vs-7d-ago +19%; slot 318 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +23.60%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 987,010.00 is +24.7% vs 30d median 791,527.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · TPS vs 30d median (solana.com/data tx/86400)** — Current 4,723.27 TPS is +23.3% vs 30d median 3,831.22 TPS (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 446,184,301 |
| Block height | 424,227,456 |
| Block time | 2026-09-11T14:52:34Z |
| Epoch | 1,032 (83.40% · slot 360,302/432,000) |
| Mean TPS (last ~3,600s) | 4,723.3 |
| Mean non-vote TPS | 2,627.2 |
| Median TPS (same window) | 4,644.6 |
| Mean slot time | 318.1 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 547,412,399,196 |
| Circulating supply | 586,537,361 SOL |
| Total supply | 633,829,926 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 672 |
| Delinquent | 17 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 437,116,383 SOL |
| Delinquent stake | 2,071,830.27 SOL (0.472%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.33% / 35.65% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 3.99% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.32M SOL | 3.73% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.52M SOL | 2.87% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.38M SOL | 2.60% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.19% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.28M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.34M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.88M SOL | 1.57% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.55M SOL | 1.50% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.95M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `pSo1KZXg…` · 1.64M SOL · commission 4% · lag 90726 slots
- `pitch9cM…` · 100.40K SOL · commission 5% · lag 973 slots
- `EBk678aQ…` · 95.16K SOL · commission 5% · lag 96433 slots
- `mrgn2vUP…` · 90.78K SOL · commission 0% · lag 9106 slots
- `scs2Ra91…` · 58.59K SOL · commission 10% · lag 305219 slots
- `EWARp8Sy…` · 35.14K SOL · commission 5% · lag 42947 slots
- `mrgn4atx…` · 19.89K SOL · commission 0% · lag 44745 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 330144 slots
- `inWVrrYJ…` · 8.46K SOL · commission 0% · lag 485204 slots
- `xLabscif…` · 3.36K SOL · commission 5% · lag 2395928 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 2218379 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 389139 slots

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
| Jito tip-floor run-rate (NOT REV) | $114.06K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 114059 USD; at p95 floor → 2380480 USD. |
| Protocol fees 24h | $14.61M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9966 |
| p90 / p99 | 0.000013 / 0.000201 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $102.99 | coingecko.simple_price |
| 24h change | +2.99% | coingecko.simple_price |
| Market cap | $60.45B | coingecko.simple_price |
| 24h volume | $3.94B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.83B |
| TVL 1d / 7d / 30d | -0.47% / -1.73% / +19.58% |
| DEX volume 24h | $2.92B · 1d -2.61% · vs-7d-ago +18.80% |
| 7d DEX volume | $18.00B · +15.32% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.61M |
| Fees 1d / 7d | -6.98% / +23.60% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $468.14M | +37.30% |
| Raydium AMM | $408.96M | -6.01% |
| BisonFi | $395.81M | -1.73% |
| HumidiFi | $322.67M | +12.96% |
| Tessera V | $232.00M | -6.46% |
| Meteora DLMM | $220.43M | -31.60% |
| Orca DEX | $201.48M | +18.84% |
| Manifest Trade | $135.72M | -10.69% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.55B | +2.42% | +0.35% |
| Kamino Lend | Lending | $1.34B | +1.04% | +1.57% |
| Raydium AMM | Dexs | $1.11B | -0.83% | -0.67% |
| Jupiter Lend | Lending | $1.08B | -0.08% | +0.19% |
| Binance Staked SOL | Liquid Staking | $1.05B | +2.05% | -2.64% |
| Jito Liquid Staking | Liquid Staking | $1.04B | +0.69% | -1.50% |
| BlackRock BUIDL | RWA | $992.51M | -0.68% | -0.63% |
| Jupiter Perpetual Exchange | Derivatives | $749.52M | +1.81% | +0.12% |
| Jupiter Staked SOL | Liquid Staking | $524.59M | +2.11% | +0.12% |
| Sentora Curator | Risk Curators | $388.02M | +0.63% | -2.57% |

## Stablecoins

Solana circulating pegged-USD: **$15.97B**
(1d -1.33% · 7d -1.74%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.01B | -1.26% |
| USDT · Tether | $2.67B | -3.25% |
| USDGO · USDGO | $1.38B | +0.73% |
| USD1 · World Liberty Financial USD | $1.28B | -0.00% |
| BUIDL · BlackRock USD | $992.51M | +0.03% |
| PYUSD · PayPal USD | $706.61M | -6.61% |
| USDG · Global Dollar | $606.02M | +0.71% |
| USDe · Ethena USDe | $536.36M | +0.14% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $106.88M (lower bound, not a census).
24h volume $113.78M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.90B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.51M
- **OnRe** (RWA) — $294.72M
- **Ondo Yield Assets** (RWA) — $179.85M
- **Huma Finance V2** (RWA) — $170.16M
- **Hastra** (RWA) — $150.67M
- **Plume Vaults** (RWA) — $27.21M
- **Ondo Global Markets** (RWA) — $25.51M
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

- [$WEN is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2098423204117410226) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 14:47:33 GMT
- [Wendy's ($WEN) is one of the largest fast food chains in the world, with over 7,000 restaurants across roughly 30 countries.

Verify the address on @tokens:
https://tokens.xyz/wendy-s?solana=WENAZ2WyPbmgvUcKfQ8hyMDfBQP9bZ65hsZ5KTFrRGZ](https://x.com/solana/status/2098423201806385330) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 14:47:32 GMT
- [BREAKING: $WEN is live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2098423198815813857) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 14:47:32 GMT
- [Pinned: STOCKLANA

The stock market is open for building.  

One week to build something innovative with stocks on Solana. $100K in prizes.

Sept 11 - 18, opening bell to closing bell:
https://hackathons.solana.com/hackathons/stocklana](https://x.com/solana/status/2098403597004263760) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 13:29:38 GMT
- [RT by @solana: BREAKING: Tokenized equity holders on @Solana crossed 727,000 addresses, up more than 300,000 in under two weeks.](https://x.com/tokens/status/2098372990715257230) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 11:28:01 GMT
- [RT by @solana: solana is back as the biggest route for the trading terminal volume](https://x.com/Adam_Tehc/status/2098308450157514956) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 07:11:33 GMT
- [RT by @solana: JUST IN: Tokenized $GRND volume onchain has surpassed volume across traditional US stock markets.

Backpack tokenized GRND has crossed $32M on @Solana in less than 24 hours, versus roughly $20M across traditional US stock markets yesterday.](https://x.com/BackpackOnchain/status/2098397354240172139) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 13:04:50 GMT
- [Join @SolanaInstitute Washington x Wall Street Summit:  https://luma.com/DCSummit](https://x.com/solana/status/2098378997050835035) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 11:51:53 GMT
- [Step 2 of SIMD-0437 rent reduction is coming to mainnet-beta at ~21:15 UTC on September 11.

Lamports per byte drops 6,333 → 5,080 at epoch 1033. With step 2, rent will have dropped 27% from its initial value.

As a reminder, there is no fixed schedule between gates. Step 3 will activate only after state growth safely checks out. SIMD-0438 standing by as the reverse gear if needed.

Three gates remain.](https://x.com/anza_xyz/status/2098396412061028556) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 13:01:05 GMT `upgrade` `mainnet`
- [The pace of Agave development has increased.

Stable releases ship roughly every 6 weeks, carrying protocol improvements and features to mainnet-beta faster than they used to.

Many of these changes seamlessly improve Solana, but some features require direct action from our ecosystem: validators, app developers, RPC providers, exchanges, block builders, and more.

With @SolanaFndn, we're improving both how changes roll out and how you hear about them.

Operationally: integration windows where builders test protocol changes together well before mainnet-beta activation.

Communications: earlier, clearer notice of changes that impact RPCs, apps, validators, and block builders, amplified through every channel the ecosystem already follows.

When the ecosystem integrates as fast as we ship, everyone moves faster and Solana wins.

Blog coming soon on what we're improving.](https://x.com/anza_xyz/status/2098147825662214499) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 10 Sep 2026 20:33:17 GMT `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [$WEN is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2098423204117410226) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 14:47:33 GMT
- [Wendy's ($WEN) is one of the largest fast food chains in the world, with over 7,000 restaurants across roughly 30 countries.

Verify the address on @tokens:
https://tokens.xyz/wendy-s?solana=WENAZ2WyPbmgvUcKfQ8hyMDfBQP9bZ65hsZ5KTFrRGZ](https://x.com/solana/status/2098423201806385330) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 14:47:32 GMT
- [BREAKING: $WEN is live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2098423198815813857) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 14:47:32 GMT
- [Pinned: STOCKLANA

The stock market is open for building.  

One week to build something innovative with stocks on Solana. $100K in prizes.

Sept 11 - 18, opening bell to closing bell:
https://hackathons.solana.com/hackathons/stocklana](https://x.com/solana/status/2098403597004263760) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 13:29:38 GMT
- [RT by @solana: BREAKING: Tokenized equity holders on @Solana crossed 727,000 addresses, up more than 300,000 in under two weeks.](https://x.com/tokens/status/2098372990715257230) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 11:28:01 GMT
- [RT by @solana: solana is back as the biggest route for the trading terminal volume](https://x.com/Adam_Tehc/status/2098308450157514956) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 07:11:33 GMT
- [RT by @solana: JUST IN: Tokenized $GRND volume onchain has surpassed volume across traditional US stock markets.

Backpack tokenized GRND has crossed $32M on @Solana in less than 24 hours, versus roughly $20M across traditional US stock markets yesterday.](https://x.com/BackpackOnchain/status/2098397354240172139) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 13:04:50 GMT
- [Join @SolanaInstitute Washington x Wall Street Summit:  https://luma.com/DCSummit](https://x.com/solana/status/2098378997050835035) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 11:51:53 GMT
- [Step 2 of SIMD-0437 rent reduction is coming to mainnet-beta at ~21:15 UTC on September 11.

Lamports per byte drops 6,333 → 5,080 at epoch 1033. With step 2, rent will have dropped 27% from its initial value.

As a reminder, there is no fixed schedule between gates. Step 3 will activate only after state growth safely checks out. SIMD-0438 standing by as the reverse gear if needed.

Three gates remain.](https://x.com/anza_xyz/status/2098396412061028556) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 13:01:05 GMT `upgrade` `mainnet`
- [The pace of Agave development has increased.

Stable releases ship roughly every 6 weeks, carrying protocol improvements and features to mainnet-beta faster than they used to.

Many of these changes seamlessly improve Solana, but some features require direct action from our ecosystem: validators, app developers, RPC providers, exchanges, block builders, and more.

With @SolanaFndn, we're improving both how changes roll out and how you hear about them.

Operationally: integration windows where builders test protocol changes together well before mainnet-beta activation.

Communications: earlier, clearer notice of changes that impact RPCs, apps, validators, and block builders, amplified through every channel the ecosystem already follows.

When the ecosystem integrates as fast as we ship, everyone moves faster and Solana wins.

Blog coming soon on what we're improving.](https://x.com/anza_xyz/status/2098147825662214499) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 10 Sep 2026 20:33:17 GMT `mainnet`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-11 (2026-09-11 07:52:46 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 268ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 195ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 180ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 209ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 216ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6777ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 406ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 149ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 76ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 64ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 50ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 53ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1330ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 148ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 123ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 84ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 120ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 606ms https://solana.com/data
- `solana.com.databricks` [ok] 200 122ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 545ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 133ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 261ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 107ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 426ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 1016ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 371ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 673ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 368ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 306ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 211ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1577ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1782ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 283ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 179ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 217ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1096ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 947ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 925ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1048ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1175ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 945ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 907ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 968ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 817ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 915ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 945ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1175ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 921ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1107ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1909ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1795ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1780ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2061ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1616ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1358ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1404ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1579ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.SPYx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.COINx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.INDIx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WRLDx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.WGSx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.circ.SPYx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.FLNCx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.QQQx` [ok] 200 601ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.XRXx` [ok] 200 622ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.mult.SPYx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 526ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.price.PCTx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.WGSx` [ok] 200 537ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.FLNCx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.FLNCx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.price.QUBTx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.mult.XRXx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.METCx` [ok] 200 630ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.BETRx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.WYFIx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.DRSx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.price.SCIx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.price.AIx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.BETRx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.BSYx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.price.SAILx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.price.GSATx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.mult.BETRx` [ok] 200 641ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 439ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.MPx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.price.DCIx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.price.DVAx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.circ.SCIx` [ok] 200 1369ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.circ.DRSx` [ok] 200 1502ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.circ.BSYx` [ok] 200 1163ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.mult.SCIx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.circ.GSATx` [ok] 200 1329ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.mult.BSYx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.price.GDDYx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.circ.MPx` [ok] 200 1235ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.mult.GSATx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.SAILx` [ok] 200 1599ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.circ.DCIx` [ok] 200 1181ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.price.BXPx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.mult.MPx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.price.DYx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.price.RYANx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.mult.DCIx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.mult.SAILx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.circ.DVAx` [ok] 200 1284ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.price.AMx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.price.WMSx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.circ.AMx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.DVAx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.circ.GDDYx` [ok] 200 1175ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.mult.AMx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.mult.GDDYx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.circ.BXPx` [ok] 200 1257ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.circ.DYx` [ok] 200 1219ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.price.FDSx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.price.SMTCx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.circ.FRHCx` [ok] 200 1130ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.price.ALSNx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.circ.RYANx` [ok] 200 1376ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.circ.WMSx` [ok] 200 1233ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.circ.ALSNx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.mult.RYANx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.mult.BXPx` [ok] 200 621ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.SFx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.price.AXSMx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.mult.WMSx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.mult.ALSNx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.price.BPOPx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.price.EGPx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.circ.SFx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.price.TTMIx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.price.AEISx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.circ.TTMIx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.SFx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.circ.SMTCx` [ok] 200 1385ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.mult.TTMIx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.DPZx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.circ.AXSMx` [ok] 200 924ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.price.HRLx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.mult.SMTCx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.circ.DPZx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.circ.FDSx` [ok] 200 1731ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.mult.AXSMx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.circ.HRLx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.circ.BPOPx` [ok] 200 1253ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.circ.AEISx` [ok] 200 1099ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.price.PAGx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.circ.EGPx` [ok] 200 1297ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.price.KTOSx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.mult.DPZx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.mult.HRLx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.mult.BPOPx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.circ.PAGx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.mult.AEISx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.price.SEICx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.circ.KTOSx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.price.HIIx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.price.EHCx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.price.GFLx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.price.ARx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.circ.SEICx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.mult.KTOSx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.mult.PAGx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.mult.EGPx` [ok] 200 603ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.EHCx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.price.MGMx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.circ.GFLx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.price.DOCUx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.circ.ARx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.mult.SEICx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.price.HALOx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.mult.EHCx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.GFLx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.circ.HALOx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.mult.ARx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.price.AFGx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.circ.MGMx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.price.WTRGx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.mult.HIIx` [ok] 200 566ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.price.HUBSx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.circ.AFGx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.price.AMKRx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.price.GMEDx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.circ.HUBSx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.mult.MGMx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.mult.HALOx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.circ.WTRGx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.mult.AFGx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.circ.GMEDx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.circ.AMKRx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.price.IESCx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.price.JKHYx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.AMKRx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.circ.DOCUx` [ok] 200 1150ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.circ.JKHYx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.mult.HUBSx` [ok] 200 530ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.circ.IESCx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.price.OCx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.price.BMRNx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.mult.DOCUx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.price.CRx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.price.JEFx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.mult.JKHYx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.circ.BMRNx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.circ.OCx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.mult.IESCx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.circ.CRx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.price.AMHx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.JEFx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.price.FIVEx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.mult.OCx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.mult.BMRNx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.price.ITx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.mult.WTRGx` [ok] 200 1023ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.mult.CRx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.circ.FIVEx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.circ.ITx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.price.UHALx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.price.MDGLx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.price.VNOMx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.circ.AMHx` [ok] 200 605ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.circ.UHALx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.mult.FIVEx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.mult.JEFx` [ok] 200 693ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.circ.MDGLx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.circ.VNOMx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.mult.ITx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.UHALx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.mult.MDGLx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.price.STRLx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.mult.VNOMx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.mult.AMHx` [ok] 200 488ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.price.ARWRx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.price.Hx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.price.AHRx` [ok] 200 1123ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.price.CORTx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.circ.STRLx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.price.IVZx` [ok] 200 793ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.price.AURx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.circ.ARWRx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.circ.Hx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.circ.CORTx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.circ.AHRx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.mult.STRLx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.circ.IVZx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.price.NWSAx` [ok] 200 941ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.mult.Hx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.mult.AHRx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.GWREx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.mult.CORTx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.mult.ARWRx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.mult.IVZx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.circ.NWSAx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.mult.AURx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.price.MANHx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.price.NWSx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.circ.GWREx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.price.BAXx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.price.CACIx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.circ.NWSx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.circ.MANHx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.circ.BAXx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.circ.CACIx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.NWSAx` [ok] 200 454ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.mult.MANHx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.CACIx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 509ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 291ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 213ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INDIx` [ok] 200 103ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 109ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.BETRx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.FLNCx` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.XRXx` [ok] 200 98ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.PCTx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.WGSx` [ok] 200 107ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jito.tip_floor` [ok] 200 271ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 369ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 348ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 175ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 189ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 204ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 176ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 182ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
