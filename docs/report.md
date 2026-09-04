# Borealis — Solana ecosystem report

**Generated** 2026-09-04T04:38:01Z · 2026-09-03 21:38:01 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-04T04:37:51Z · **RPC health** `ok`
**Health score** 95 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +4.01%; DEX 24h $2.37B · 1d +4% · vs-7d-ago -36%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -35.85%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -33.12%. (threshold: `|7d %| >= 20`)
- **WARN · Last slot-time sample outside 2.5σ of the 60-sample window** — Last sample 326 ms is +2.71σ vs window mean 315 ms (n=60). (threshold: `|last sample − window mean| > 2.5σ`)
- **INFO · Daily active addresses vs 30d median** — Current 856,198.00 is +24.4% vs 30d median 688,266.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 104.19 USD is +25.9% vs 30d median 82.77 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 444,155,601 |
| Block height | 422,201,879 |
| Block time | 2026-09-04T04:37:51Z |
| Epoch | 1,028 (13.80% · slot 59,604/432,000) |
| Mean TPS (last ~3,600s) | 3,240.8 |
| Mean non-vote TPS | 1,111.7 |
| Median TPS (same window) | 3,202.2 |
| Mean slot time | 315.1 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 544,985,003,981 |
| Circulating supply | 585,360,589 SOL |
| Total supply | 633,455,615 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 18 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 436,757,852 SOL |
| Delinquent stake | 141,013.38 SOL (0.032%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 79 |
| Top 10 / 20 stake share | 24.39% / 35.71% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.39M SOL | 3.98% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.32M SOL | 3.74% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.46M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.38M SOL | 2.61% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.19% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.28M SOL | 2.12% | 7% | 0 |
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

- `xLabscif…` · 78.25K SOL · commission 5% · lag 367228 slots
- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 31520 slots
- `prt1st4R…` · 19.80K SOL · commission 5% · lag 668659 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 806878 slots
- `5ZjxMYBb…` · 4.06K SOL · commission 0% · lag 189679 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1369480 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 59595 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 716962 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 2171847 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1355250 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1396764 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 1355144 slots

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
| Jito tip-floor run-rate (NOT REV) | $30.89K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 30892 USD; at p95 floor → 330665 USD. |
| Protocol fees 24h | $10.91M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9978 |
| p90 / p99 | 0.000010 / 0.000099 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $104.19 | coingecko.simple_price |
| 24h change | +4.01% | coingecko.simple_price |
| Market cap | $60.98B | coingecko.simple_price |
| 24h volume | $4.14B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.92B |
| TVL 1d / 7d / 30d | +3.65% / -1.70% / +23.01% |
| DEX volume 24h | $2.37B · 1d +3.68% · vs-7d-ago -35.85% |
| 7d DEX volume | $15.39B · -30.87% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $10.91M |
| Fees 1d / 7d | +3.56% / -33.12% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $838.66M | -17.87% |
| Orca DEX | $289.05M | +44.12% |
| BisonFi | $232.51M | +19.63% |
| Meteora DLMM | $186.49M | +35.31% |
| Manifest Trade | $172.58M | +0.54% |
| Raydium AMM | $146.98M | +25.60% |
| pump.fun | $75.20M | -9.58% |
| Axiom | $60.26M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.58B | +2.76% | -4.63% |
| Kamino Lend | Lending | $1.33B | +8.11% | +6.55% |
| Raydium AMM | Dexs | $1.12B | +3.50% | -5.25% |
| Jupiter Lend | Lending | $1.09B | +1.62% | -3.00% |
| Binance Staked SOL | Liquid Staking | $1.08B | +3.40% | -2.15% |
| Jito Liquid Staking | Liquid Staking | $1.05B | +3.77% | -2.36% |
| BlackRock BUIDL | RWA | $937.81M | +0.63% | -0.43% |
| Jupiter Perpetual Exchange | Derivatives | $764.19M | +2.21% | -3.48% |
| Jupiter Staked SOL | Liquid Staking | $535.40M | +2.76% | -4.81% |
| xStocks | RWA | $458.62M | +5.45% | +3.61% |

## Stablecoins

Solana circulating pegged-USD: **$16.19B**
(1d +3.38% · 7d +2.60%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.04B | +4.49% |
| USDT · Tether | $2.95B | +1.38% |
| USDGO · USDGO | $1.32B | +4.86% |
| USD1 · World Liberty Financial USD | $1.23B | +1.86% |
| BUIDL · BlackRock USD | $937.81M | +5.29% |
| PYUSD · PayPal USD | $860.10M | +7.57% |
| USDG · Global Dollar | $559.97M | -7.82% |
| USDe · Ethena USDe | $535.71M | -0.09% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 77 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 77 · priced-subset mcap $291.89M (lower bound, not a census).
24h volume $31.82M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $458.62M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 77 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.16B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $937.81M
- **xStocks** (RWA) — $458.62M
- **OnRe** (RWA) — $296.74M
- **Ondo Yield Assets** (RWA) — $179.61M
- **Hastra** (RWA) — $150.39M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $25.40M
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

- [RT by @solana: $607M traded on Jupiter Mobile in August!

Month after month, the story's the same, people trade on the fastest, cheapest choice.

Just Use Jupiter (Mobile). 📲](https://x.com/jup_mobile/status/2095542334956179524) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 16:00:00 GMT
- [RT by @solana: Reminder: Hacker House is back ahead of Breakpoint Nov 1-12, 2026

Extend your stay in London to build among friends](https://x.com/hackerhouses/status/2095492756915245160) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 12:43:00 GMT
- [RT by @solana: Over $50M in deposits into Kamino Vaults through @BinanceWallet in less than 24 hours.

Bringing Solana’s onchain markets to millions of users globally.](https://x.com/kamino/status/2095607887850582087) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 20:20:29 GMT
- [Agents are booking restaurants, buying on Amazon, using APIs, and paying for their own compute on Solana

- @moonpay launched PayBox
- @tryramp added agent wallets
- Solana leads in x402 transactions (both volume & spend) 

@x402 in August:
https://x.com/x402/status/2095690533134102732?s=20](https://x.com/solana/status/2095697752625725459) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 02:17:35 GMT
- [1,000,000 payments per second. Live on Solana today with Payment Channels.

"Think of it like a bar tab or a prepaid meter: you put money down up front, run up usage without paying for each transaction, and settle payment once when you leave."](https://x.com/solana/status/2095623657406029907) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 21:23:09 GMT
- [Solana has the strongest founder ecosystem in crypto

Time to prove it in a bigger @colosseum arena](https://x.com/solana/status/2095598841621786803) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 19:44:32 GMT
- [Payment Channels is now live on Solana

Learn more about how to achieve 1M payments per second on Solana via x402 and MPP from @_rishinsharma, Head of AI Growth, @SolanaFndn](https://x.com/solana/status/2095585115250585952) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 18:50:00 GMT
- [1,000,000 payments per second 🤯

only possible on Solana](https://x.com/solana/status/2095577162598236283) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 18:18:24 GMT
- [Rent reduction is live on mainnet-beta.

Step 1 of SIMD-0437 activated at epoch 1028, the first of five feature gates on the road to cutting Solana's storage cost per byte by 90% overall.

Step 1 drops lamports per byte 6,960 → 6,333. Each remaining gate activates only after state growth checks out at the current level. We are stepping down to the final 696 safely, not on a fixed schedule. Follow here for an accurate timeline.

A safeguard gate (SIMD-0438) can restore the legacy value if state growth becomes a problem.](https://x.com/anza_xyz/status/2095654321350459648) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 23:25:00 GMT `upgrade` `mainnet`
- [Repo and benchmarks: https://github.com/anza-xyz/wincode

wincode is a drop-in replacement when layout and configuration match.](https://x.com/anza_xyz/status/2095612015192703481) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:53 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: $607M traded on Jupiter Mobile in August!

Month after month, the story's the same, people trade on the fastest, cheapest choice.

Just Use Jupiter (Mobile). 📲](https://x.com/jup_mobile/status/2095542334956179524) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 16:00:00 GMT
- [RT by @solana: Reminder: Hacker House is back ahead of Breakpoint Nov 1-12, 2026

Extend your stay in London to build among friends](https://x.com/hackerhouses/status/2095492756915245160) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 12:43:00 GMT
- [RT by @solana: Over $50M in deposits into Kamino Vaults through @BinanceWallet in less than 24 hours.

Bringing Solana’s onchain markets to millions of users globally.](https://x.com/kamino/status/2095607887850582087) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 20:20:29 GMT
- [Agents are booking restaurants, buying on Amazon, using APIs, and paying for their own compute on Solana

- @moonpay launched PayBox
- @tryramp added agent wallets
- Solana leads in x402 transactions (both volume & spend) 

@x402 in August:
https://x.com/x402/status/2095690533134102732?s=20](https://x.com/solana/status/2095697752625725459) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 02:17:35 GMT
- [1,000,000 payments per second. Live on Solana today with Payment Channels.

"Think of it like a bar tab or a prepaid meter: you put money down up front, run up usage without paying for each transaction, and settle payment once when you leave."](https://x.com/solana/status/2095623657406029907) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 21:23:09 GMT
- [Solana has the strongest founder ecosystem in crypto

Time to prove it in a bigger @colosseum arena](https://x.com/solana/status/2095598841621786803) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 19:44:32 GMT
- [Payment Channels is now live on Solana

Learn more about how to achieve 1M payments per second on Solana via x402 and MPP from @_rishinsharma, Head of AI Growth, @SolanaFndn](https://x.com/solana/status/2095585115250585952) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 18:50:00 GMT
- [1,000,000 payments per second 🤯

only possible on Solana](https://x.com/solana/status/2095577162598236283) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 18:18:24 GMT
- [Rent reduction is live on mainnet-beta.

Step 1 of SIMD-0437 activated at epoch 1028, the first of five feature gates on the road to cutting Solana's storage cost per byte by 90% overall.

Step 1 drops lamports per byte 6,960 → 6,333. Each remaining gate activates only after state growth checks out at the current level. We are stepping down to the final 696 safely, not on a fixed schedule. Follow here for an accurate timeline.

A safeguard gate (SIMD-0438) can restore the legacy value if state growth becomes a problem.](https://x.com/anza_xyz/status/2095654321350459648) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 23:25:00 GMT `upgrade` `mainnet`
- [Repo and benchmarks: https://github.com/anza-xyz/wincode

wincode is a drop-in replacement when layout and configuration match.](https://x.com/anza_xyz/status/2095612015192703481) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:53 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-04 (2026-09-03 21:38:01 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 524ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 435ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 432ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 466ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 423ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6710ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 890ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 174ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 78ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 111ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 32ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 62ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 53ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 104ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 85ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 86ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 158ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 497ms https://solana.com/data
- `solana.com.databricks` [ok] 200 326ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 554ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 252ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 144ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 87ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 186ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 892ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 436ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 434ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 437ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 841ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1355ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1504ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 194ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 172ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 432ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 428ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1878ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1924ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2168ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1566ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1598ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1517ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1415ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1585ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1552ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1415ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1571ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1598ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1385ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1469ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2896ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2279ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2668ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2243ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1905ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1683ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1902ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1925ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [ok] 200 550ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.SPYx` [ok] 200 610ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.AAPLx` [ok] 200 636ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.METAx` [ok] 200 738ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.GOOGLx` [ok] 200 925ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.NVDAx` [ok] 200 944ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.AAPLx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 585ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.MSFTx` [ok] 200 1143ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.NVDAx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.AMZNx` [ok] 200 1245ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.mult.TSLAx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 726ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 687ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 577ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.MSFTx` [ok] 200 759ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.MUUx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.price.MVLLx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.QQQx` [ok] 200 814ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.AXTIx` [ok] 200 400ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.circ.MUUx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 804ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 1088ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.MSFTx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.COINx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 1291ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.circ.DJTx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.circ.AXTIx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.mult.MUUx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.INTWx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.mult.COINx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.AXTIx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 475ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.price.SOXSx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.SHEINx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.mult.DRAMx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.MVLLx` [ok] 200 929ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.circ.SOXSx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.KORUx` [ok] 200 1335ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.circ.SHEINx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.BANKCx` [ok] 200 549ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.MMGx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.KORUx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.mult.SHEINx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.TNGYIx` [ok] 200 722ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.BANKCx` [ok] 200 530ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.SUOPTx` [ok] 200 571ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.SNXXx` [ok] 200 1318ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.BANKCx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.mult.SNXXx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [ok] 200 536ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.KUNLx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.HAIDLx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 846ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 794ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 989ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 1096ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.KUNLx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.CRESBx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.CMERPx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 1484ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.CRESBx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.CMERPx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 1111ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.MIXUx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.BDWAPx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.CSPCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 712ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.CSPCx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 1459ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.WHRFRx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.CMENDx` [ok] 200 561ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.SITCx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 543ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 923ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.mult.CMENDx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 1314ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.CRESPx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.PRADx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 648ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.CRESPx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 653ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.SINOx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.WHGROx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.CRESPx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.CTFJWx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.SINOx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 1012ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.WHGROx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 610ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.WHGROx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.SINOTx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.CTPCAx` [ok] 200 1264ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.GENTEx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.SWPRPx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 619ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.HKCGAx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.CRAUTx` [ok] 200 1006ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 582ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 928ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 677ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 625ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.price.HKEXCx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 588ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.KUAIx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 816ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 533ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 542ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 574ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.CHONGx` [ok] 200 641ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.price.COVELx` [ok] 200 715ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.MEITx` [ok] 200 620ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.MTRCPx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.CHONGx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.COVELx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.HNDLDx` [ok] 200 686ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.PICCx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 1163ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.HNDLDx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.PICCx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.MTRCPx` [ok] 200 728ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.COSCx` [ok] 200 608ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.CHONGx` [ok] 200 1255ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 692ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 794ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.price.NWGx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.NWGx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.NWGx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1647ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 707ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.MUUx` [ok] 200 125ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.INTWx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.DRAMx` [ok] 200 115ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.MVLLx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SOXSx` [ok] 200 121ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jup.tokens.search.KORUx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.MEITx` [ok] 200 120ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.SHEINx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jito.tip_floor` [ok] 200 452ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 319ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 131ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 420ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 420ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 475ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 433ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 206ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
