# Borealis — Solana ecosystem report

**Generated** 2026-09-04T00:52:32Z · 2026-09-03 17:52:32 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-04T00:52:21Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +4.01%; DEX 24h $2.45B · 1d +7% · vs-7d-ago -34%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -33.80%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -34.52%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 856,198.00 is +26.3% vs 30d median 677,709.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 103.63 USD is +25.2% vs 30d median 82.77 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 444,112,707 |
| Block height | 422,159,174 |
| Block time | 2026-09-04T00:52:21Z |
| Epoch | 1,028 (3.87% · slot 16,708/432,000) |
| Mean TPS (last ~3,600s) | 3,584.5 |
| Mean non-vote TPS | 1,456.4 |
| Median TPS (same window) | 3,547.4 |
| Mean slot time | 314.6 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 544,939,337,195 |
| Circulating supply | 585,360,845 SOL |
| Total supply | 633,455,735 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 19 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 436,594,517 SOL |
| Delinquent stake | 304,348.44 SOL (0.070%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 79 |
| Top 10 / 20 stake share | 24.40% / 35.73% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.39M SOL | 3.98% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.32M SOL | 3.74% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.46M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.38M SOL | 2.61% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.19% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.28M SOL | 2.13% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.38M SOL | 1.69% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.13M SOL | 1.63% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.84M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `vahMVcSS…` · 163.34K SOL · commission 0% · lag 25056 slots
- `xLabscif…` · 78.25K SOL · commission 5% · lag 324334 slots
- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 16701 slots
- `prt1st4R…` · 19.80K SOL · commission 5% · lag 625765 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 763984 slots
- `5ZjxMYBb…` · 4.06K SOL · commission 0% · lag 146785 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1326586 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 16701 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 674068 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 2128953 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1312356 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1353870 slots

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
| Jito tip-floor run-rate (NOT REV) | $27.61K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 27605 USD; at p95 floor → 6519873 USD. |
| Protocol fees 24h | $10.68M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9974 |
| p90 / p99 | 0.000010 / 0.000094 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.63 | coingecko.simple_price |
| 24h change | +4.01% | coingecko.simple_price |
| Market cap | $60.63B | coingecko.simple_price |
| 24h volume | $4.29B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.96B |
| TVL 1d / 7d / 30d | 0.00% / -0.98% / +23.90% |
| DEX volume 24h | $2.45B · 1d +6.99% · vs-7d-ago -33.80% |
| 7d DEX volume | $14.02B · -37.00% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $10.68M |
| Fees 1d / 7d | +1.39% / -34.52% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $1.02B | 0.00% |
| Orca DEX | $285.64M | +42.41% |
| BisonFi | $194.35M | 0.00% |
| Manifest Trade | $177.46M | +3.38% |
| Raydium AMM | $153.81M | +31.44% |
| Meteora DLMM | $137.83M | 0.00% |
| pump.fun | $75.20M | -9.58% |
| Axiom | $60.26M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.60B | +5.45% | -3.67% |
| Kamino Lend | Lending | $1.34B | +8.85% | +7.10% |
| Raydium AMM | Dexs | $1.13B | +4.85% | -2.98% |
| Jupiter Lend | Lending | $1.10B | +3.45% | +1.67% |
| Binance Staked SOL | Liquid Staking | $1.09B | +5.49% | -3.61% |
| Jito Liquid Staking | Liquid Staking | $1.06B | +5.75% | -3.41% |
| BlackRock BUIDL | RWA | $937.81M | +0.63% | -0.43% |
| Jupiter Perpetual Exchange | Derivatives | $769.20M | +3.80% | -2.72% |
| Jupiter Staked SOL | Liquid Staking | $543.22M | +5.65% | -3.52% |
| xStocks | RWA | $462.08M | +6.34% | +4.78% |

## Stablecoins

Solana circulating pegged-USD: **$16.20B**
(1d +1.59% · 7d -0.18%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.06B | +6.39% |
| USDT · Tether | $2.95B | +3.90% |
| USDGO · USDGO | $1.32B | +5.62% |
| USD1 · World Liberty Financial USD | $1.22B | +1.24% |
| BUIDL · BlackRock USD | $937.81M | +5.73% |
| PYUSD · PayPal USD | $860.34M | +16.53% |
| USDG · Global Dollar | $563.42M | -8.17% |
| USDe · Ethena USDe | $536.21M | -0.23% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 78 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 78 · priced-subset mcap $292.12M (lower bound, not a census).
24h volume $31.72M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $462.08M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 78 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.16B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $937.81M
- **xStocks** (RWA) — $462.08M
- **OnRe** (RWA) — $296.55M
- **Ondo Yield Assets** (RWA) — $179.46M
- **Hastra** (RWA) — $150.43M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $25.33M
- **Plume Vaults** (RWA) — $22.90M

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

- [1,000,000 payments per second. Live on Solana today with Payment Channels.

"Think of it like a bar tab or a prepaid meter: you put money down up front, run up usage without paying for each transaction, and settle payment once when you leave."](https://x.com/solana/status/2095623657406029907) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 21:23:09 GMT
- [Solana has the strongest founder ecosystem in crypto

Time to prove it in a bigger @colosseum arena](https://x.com/solana/status/2095598841621786803) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 19:44:32 GMT
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
- [Rent reduction is live on mainnet-beta.

Step 1 of SIMD-0437 activated at epoch 1028, the first of five feature gates on the road to cutting Solana's storage cost per byte by 90% overall.

Step 1 drops lamports per byte 6,960 → 6,333. Each remaining gate activates only after state growth checks out at the current level. We are stepping down to the final 696 safely, not on a fixed schedule. Follow here for an accurate timeline.

A safeguard gate (SIMD-0438) can restore the legacy value if state growth becomes a problem.](https://x.com/anza_xyz/status/2095654321350459648) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 23:25:00 GMT `upgrade` `mainnet`
- [Repo and benchmarks: https://github.com/anza-xyz/wincode

wincode is a drop-in replacement when layout and configuration match.](https://x.com/anza_xyz/status/2095612015192703481) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:53 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [1,000,000 payments per second. Live on Solana today with Payment Channels.

"Think of it like a bar tab or a prepaid meter: you put money down up front, run up usage without paying for each transaction, and settle payment once when you leave."](https://x.com/solana/status/2095623657406029907) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 21:23:09 GMT
- [Solana has the strongest founder ecosystem in crypto

Time to prove it in a bigger @colosseum arena](https://x.com/solana/status/2095598841621786803) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 19:44:32 GMT
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
- [Rent reduction is live on mainnet-beta.

Step 1 of SIMD-0437 activated at epoch 1028, the first of five feature gates on the road to cutting Solana's storage cost per byte by 90% overall.

Step 1 drops lamports per byte 6,960 → 6,333. Each remaining gate activates only after state growth checks out at the current level. We are stepping down to the final 696 safely, not on a fixed schedule. Follow here for an accurate timeline.

A safeguard gate (SIMD-0438) can restore the legacy value if state growth becomes a problem.](https://x.com/anza_xyz/status/2095654321350459648) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 23:25:00 GMT `upgrade` `mainnet`
- [Repo and benchmarks: https://github.com/anza-xyz/wincode

wincode is a drop-in replacement when layout and configuration match.](https://x.com/anza_xyz/status/2095612015192703481) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:53 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-04 (2026-09-03 17:52:32 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 166ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 184ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 157ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 147ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 148ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7104ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 212ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 162ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 140ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 280ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 86ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 112ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1065ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 337ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 129ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 130ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 220ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 531ms https://solana.com/data
- `solana.com.databricks` [ok] 200 199ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 802ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 229ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 127ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 146ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 399ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 690ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 300ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 320ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 316ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1038ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 4736ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1390ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 259ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 214ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 144ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 194ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 772ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 792ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 737ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 714ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 731ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 540ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 488ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 685ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 650ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 650ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 630ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 799ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 660ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 493ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1703ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2255ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2142ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1778ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1652ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2126ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 3249ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1172ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.METAx` [ok] 200 496ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.GOOGLx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.SPYx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.TSLAx` [ok] 200 611ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.MSFTx` [ok] 200 645ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.AMZNx` [ok] 200 719ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.TSLAx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.NVDAx` [ok] 200 847ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 543ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.NVDAx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.AAPLx` [ok] 200 1367ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.mult.NVDAx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 506ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.TSLAx` [ok] 200 777ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.AMZNx` [ok] 200 1074ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.MVLLx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.mult.GOOGLx` [ok] 200 950ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 821ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 800ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.MUUx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.circ.COINx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 1062ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.KORUx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.QQQx` [ok] 200 558ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.MVLLx` [ok] 200 1481ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 1905ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.DJTx` [ok] 200 1139ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.price.AXTIx` [ok] 200 1825ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.mult.KORUx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.INTWx` [ok] 200 843ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.mult.MVLLx` [ok] 200 757ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.SNXXx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.MUUx` [ok] 200 2136ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 900ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.circ.SOXSx` [ok] 200 525ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 4327ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 1033ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.mult.MUUx` [ok] 200 752ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.price.NWGx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.mult.DJTx` [ok] 200 1030ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.SNXXx` [ok] 200 751ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.AXTIx` [ok] 200 2040ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.SHEINx` [ok] 200 783ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.BANKCx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.NWGx` [ok] 200 582ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 707ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.AXTIx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 815ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.MMGx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.SUOPTx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.NWGx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.INTWx` [ok] 200 2580ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 4201ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 1407ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.mult.DRAMx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 545ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 578ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.price.SNBIOx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.KUNLx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 1002ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.WRFHDx` [ok] 200 1194ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 1604ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.ENNHLx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.SHEINx` [ok] 200 2859ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 439ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 498ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.SMOIHx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 647ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 509ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.HRZRBx` [ok] 200 634ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.JTGEXx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.SHEINx` [ok] 200 1155ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.JTGEXx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.CSPCx` [ok] 200 1030ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.ASMPTx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.MIXUx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.WXXDCx` [ok] 200 882ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.CSPCx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 921ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.MIXUx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.CMENDx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.WHRFRx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 734ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 1789ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.CRESPx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.JDHLTx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.SNDSCx` [ok] 200 556ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.WHRFRx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 526ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 823ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 766ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.WHGROx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.CRESPx` [ok] 200 1095ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.CLONPx` [ok] 200 508ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.CRESPx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 1075ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 581ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.SINOx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.CTFJWx` [ok] 200 1259ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.SINOTx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.CTPCAx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 496ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.GENTEx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.WHGROx` [ok] 200 812ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.GENTEx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 970ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 6726ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 626ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 1107ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.CKAHx` [ok] 200 1097ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.CKINFx` [ok] 200 749ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 697ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.NONGx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.HKEXCx` [ok] 200 602ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 1497ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.price.GEELx` [ok] 200 565ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.CHONGx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 1288ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.NONGx` [ok] 200 799ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 900ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.MTRCPx` [ok] 200 774ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.PICCx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.KUAIx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 599ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 428ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.COVELx` [ok] 200 711ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 602ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.MEITx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.price.HNDLDx` [ok] 200 1241ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.price.CKHUTx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.COSCx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 1070ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 800ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.circ.MTRCPx` [ok] 200 1759ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1433ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 506ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INTWx` [ok] 200 159ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.MUUx` [ok] 200 155ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.DRAMx` [ok] 200 142ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.KORUx` [ok] 200 139ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.MVLLx` [ok] 200 145ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SOXSx` [ok] 200 138ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jup.tokens.search.MEITx` [ok] 200 148ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 157ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jito.tip_floor` [ok] 200 293ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 342ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 134ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 288ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 149ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 144ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 148ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 388ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
