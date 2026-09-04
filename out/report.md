# Borealis — Solana ecosystem report

**Generated** 2026-09-04T07:24:44Z · 2026-09-04 00:24:44 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-04T07:24:33Z · **RPC health** `ok`
**Health score** 96 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +2.76%; DEX 24h $2.37B · 1d +4% · vs-7d-ago -36%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -35.85%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -32.83%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 856,198.00 is +26.3% vs 30d median 677,709.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 103.78 USD is +25.4% vs 30d median 82.77 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 444,187,374 |
| Block height | 422,233,518 |
| Block time | 2026-09-04T07:24:33Z |
| Epoch | 1,028 (21.15% · slot 91,375/432,000) |
| Mean TPS (last ~3,600s) | 3,290.0 |
| Mean non-vote TPS | 1,164.2 |
| Median TPS (same window) | 3,270.5 |
| Mean slot time | 315.4 ms |
| Median slot time | 315.0 ms |
| Transaction count (cluster) | 545,017,836,713 |
| Circulating supply | 585,360,503 SOL |
| Total supply | 633,455,528 SOL |
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

- `xLabscif…` · 78.25K SOL · commission 5% · lag 399001 slots
- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 63293 slots
- `prt1st4R…` · 19.80K SOL · commission 5% · lag 700432 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 838651 slots
- `5ZjxMYBb…` · 4.06K SOL · commission 0% · lag 221452 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1401253 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 10817 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 748735 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 2203620 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1387023 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1428537 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 1386917 slots

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
| Jito tip-floor run-rate (NOT REV) | $63.09K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 63088 USD; at p95 floor → 1658379 USD. |
| Protocol fees 24h | $10.96M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9947 |
| p90 / p99 | 0.000009 / 0.000112 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.78 | coingecko.simple_price |
| 24h change | +2.76% | coingecko.simple_price |
| Market cap | $60.75B | coingecko.simple_price |
| 24h volume | $4.04B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.91B |
| TVL 1d / 7d / 30d | +3.66% / -1.71% / +22.99% |
| DEX volume 24h | $2.37B · 1d +3.68% · vs-7d-ago -35.85% |
| 7d DEX volume | $15.39B · -30.87% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $10.96M |
| Fees 1d / 7d | +4.01% / -32.83% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $838.66M | -17.87% |
| Orca DEX | $282.43M | +40.81% |
| BisonFi | $232.51M | +19.63% |
| Meteora DLMM | $186.49M | +35.31% |
| Manifest Trade | $173.46M | +1.05% |
| Raydium AMM | $142.02M | +21.36% |
| pump.fun | $75.20M | -9.58% |
| Axiom | $60.26M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.58B | +3.35% | -3.07% |
| Kamino Lend | Lending | $1.33B | +6.38% | +7.45% |
| Raydium AMM | Dexs | $1.12B | +3.50% | -5.25% |
| Jupiter Lend | Lending | $1.09B | +1.71% | -1.66% |
| Binance Staked SOL | Liquid Staking | $1.08B | +3.47% | -2.08% |
| Jito Liquid Staking | Liquid Staking | $1.05B | +4.15% | -1.93% |
| BlackRock BUIDL | RWA | $937.81M | +0.63% | -0.43% |
| Jupiter Perpetual Exchange | Derivatives | $762.94M | +2.37% | -2.59% |
| Jupiter Staked SOL | Liquid Staking | $534.95M | +3.12% | -3.47% |
| xStocks | RWA | $459.09M | +5.93% | +4.55% |

## Stablecoins

Solana circulating pegged-USD: **$16.24B**
(1d +3.37% · 7d +2.60%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.09B | +5.30% |
| USDT · Tether | $2.95B | +1.38% |
| USDGO · USDGO | $1.32B | +4.86% |
| USD1 · World Liberty Financial USD | $1.23B | +1.86% |
| BUIDL · BlackRock USD | $937.81M | +5.29% |
| PYUSD · PayPal USD | $861.17M | +7.71% |
| USDG · Global Dollar | $558.85M | -8.01% |
| USDe · Ethena USDe | $535.34M | -0.15% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 78 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 78 · priced-subset mcap $291.96M (lower bound, not a census).
24h volume $31.64M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $459.09M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 78 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.16B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $937.81M
- **xStocks** (RWA) — $459.09M
- **OnRe** (RWA) — $296.74M
- **Ondo Yield Assets** (RWA) — $179.36M
- **Hastra** (RWA) — $150.38M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $25.47M
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

- [IBRL](https://x.com/solana/status/2095745875255648336) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 05:28:48 GMT
- [JUST IN: @SuperteamAU has helped launch the Buy Australian AI Partnership as a founding partner, alongside the National AI Centre, Stone & Chalk and four of Australia's major banks.](https://x.com/solana/status/2095738924177973409) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 05:01:11 GMT
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
- [Rent reduction is live on mainnet-beta.

Step 1 of SIMD-0437 activated at epoch 1028, the first of five feature gates on the road to cutting Solana's storage cost per byte by 90% overall.

Step 1 drops lamports per byte 6,960 → 6,333. Each remaining gate activates only after state growth checks out at the current level. We are stepping down to the final 696 safely, not on a fixed schedule. Follow here for an accurate timeline.

A safeguard gate (SIMD-0438) can restore the legacy value if state growth becomes a problem.](https://x.com/anza_xyz/status/2095654321350459648) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 23:25:00 GMT `upgrade` `mainnet`
- [Repo and benchmarks: https://github.com/anza-xyz/wincode

wincode is a drop-in replacement when layout and configuration match.](https://x.com/anza_xyz/status/2095612015192703481) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:53 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [IBRL](https://x.com/solana/status/2095745875255648336) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 05:28:48 GMT
- [JUST IN: @SuperteamAU has helped launch the Buy Australian AI Partnership as a founding partner, alongside the National AI Centre, Stone & Chalk and four of Australia's major banks.](https://x.com/solana/status/2095738924177973409) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 05:01:11 GMT
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
- [Rent reduction is live on mainnet-beta.

Step 1 of SIMD-0437 activated at epoch 1028, the first of five feature gates on the road to cutting Solana's storage cost per byte by 90% overall.

Step 1 drops lamports per byte 6,960 → 6,333. Each remaining gate activates only after state growth checks out at the current level. We are stepping down to the final 696 safely, not on a fixed schedule. Follow here for an accurate timeline.

A safeguard gate (SIMD-0438) can restore the legacy value if state growth becomes a problem.](https://x.com/anza_xyz/status/2095654321350459648) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 23:25:00 GMT `upgrade` `mainnet`
- [Repo and benchmarks: https://github.com/anza-xyz/wincode

wincode is a drop-in replacement when layout and configuration match.](https://x.com/anza_xyz/status/2095612015192703481) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:53 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-04 (2026-09-04 00:24:44 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 196ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 104ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 88ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 66ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 69ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6035ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 205ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 139ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 77ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 278ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 81ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 75ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 85ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 210ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 81ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 121ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 167ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 566ms https://solana.com/data
- `solana.com.databricks` [ok] 200 248ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 670ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 374ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 228ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 251ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 348ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 719ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 376ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 375ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 371ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1290ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1627ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1266ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 213ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 1395ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 108ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 57ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 233ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 309ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 306ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 364ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 410ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 455ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 102ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 3591ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 363ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 424ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 528ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 338ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 313ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 429ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 437ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2713ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1862ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1369ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2030ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2517ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1609ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2744ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 701ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.SPYx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.NVDAx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.MSFTx` [ok] 200 589ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.SPYx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.AAPLx` [ok] 200 665ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.GOOGLx` [ok] 200 742ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.mult.SPYx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.AMZNx` [ok] 200 939ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.TSLAx` [ok] 200 978ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.NVDAx` [ok] 200 616ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 525ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.GOOGLx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.METAx` [ok] 200 1686ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.QQQx` [ok] 200 619ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 812ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 1087ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.TSLAx` [ok] 200 1142ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 1808ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.mult.METAx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 780ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.MVLLx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.AXTIx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.circ.MSFTx` [ok] 200 2447ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.mult.AAPLx` [ok] 200 773ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 522ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.MUUx` [ok] 200 1105ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.circ.DJTx` [ok] 200 498ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.price.KORUx` [ok] 200 571ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.price.INTWx` [ok] 200 544ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.circ.COINx` [ok] 200 2003ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 767ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 1240ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 1579ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.SHEINx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.mult.DJTx` [ok] 200 892ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.circ.MUUx` [ok] 200 1042ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.KORUx` [ok] 200 927ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.price.NWGx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.circ.SOXSx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.MUUx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.price.SUOPTx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.SNXXx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.circ.INTWx` [ok] 200 1752ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 644ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.SHEINx` [ok] 200 714ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 582ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.NWGx` [ok] 200 1291ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 647ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 543ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.SOXSx` [ok] 200 1571ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.mult.NWGx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 521ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 676ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.CTINSx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.WRFHDx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 498ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 706ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.CTINSx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 1315ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.KUNLx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 967ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.CTINSx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 1069ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 411ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.ENNHLx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 1292ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.SMOIHx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 513ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.BANKCx` [ok] 200 3781ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 918ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.BANKCx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 697ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 759ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 1199ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 1779ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.BDWAPx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.CMERPx` [ok] 200 717ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 1656ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 880ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 882ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.CSPCx` [ok] 200 1031ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 662ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.CRESBx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 863ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.CMENDx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 1295ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.SNDSCx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.CSPCx` [ok] 200 607ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 744ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 749ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 651ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.SINOTx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.CRESPx` [ok] 200 1077ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.MIXUx` [ok] 200 1564ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 859ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.CRESPx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.CRESPx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 1107ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 1403ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.WHGROx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.MIXUx` [ok] 200 663ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 519ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 587ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.SITCx` [ok] 200 2852ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.PWAHLx` [ok] 200 745ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.CTPCAx` [ok] 200 946ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.WHGROx` [ok] 200 574ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 555ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 830ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.CLONPx` [ok] 200 829ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 1889ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 895ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.GENTEx` [ok] 200 709ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.WUXIBx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.SITCx` [ok] 200 750ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.GENTEx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 620ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 1439ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 840ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 1548ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 634ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 1119ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.CKAHx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 1996ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 1679ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 627ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.price.MTRCPx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.COVELx` [ok] 200 1024ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.MEITx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 741ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.COVELx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 1004ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.COVELx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 827ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 592ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.HNDLDx` [ok] 200 808ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.price.GEELx` [ok] 200 1495ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.PICCx` [ok] 200 920ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.CHONGx` [ok] 200 2101ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.HNDLDx` [ok] 200 586ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 631ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 1059ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 482ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 1191ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 2633ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.CKHUTx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 906ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1727ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 193ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.SHEINx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.MUUx` [ok] 200 96ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.INTWx` [ok] 200 91ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.DRAMx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.MVLLx` [ok] 200 90ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SOXSx` [ok] 200 96ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jup.tokens.search.KORUx` [ok] 200 142ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.MEITx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jito.tip_floor` [ok] 200 349ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 511ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 139ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 108ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 110ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 201ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 61ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 260ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
