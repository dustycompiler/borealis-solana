# Borealis — Solana ecosystem report

**Generated** 2026-09-14T18:46:08Z · 2026-09-14 11:46:08 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-14T18:45:57Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +2.40%; DEX 24h $1.79B · 1d +3% · vs-7d-ago -40%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -39.77%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 447,048,305 |
| Block height | 425,090,672 |
| Block time | 2026-09-14T18:45:57Z |
| Epoch | 1,034 (83.40% · slot 360,306/432,000) |
| Mean TPS (last ~3,600s) | 4,238.5 |
| Mean non-vote TPS | 2,104.7 |
| Median TPS (same window) | 4,189.3 |
| Mean slot time | 315.8 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 548,447,656,355 |
| Circulating supply | 586,892,513 SOL |
| Total supply | 634,017,258 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 679 |
| Delinquent | 11 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 438,579,851 SOL |
| Delinquent stake | 160,515.71 SOL (0.037%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.30% / 35.53% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.57M SOL | 4.01% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.36M SOL | 3.73% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.50M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.37M SOL | 2.59% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.62M SOL | 2.19% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.25M SOL | 2.11% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.03M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.37M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.94M SOL | 1.58% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.55M SOL | 1.49% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `5pPRHnie…` | 5.96M SOL | 1.36% | 5% | 0 |
| 13 | `JD549Hsb…` | 5.88M SOL | 1.34% | 0% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 487867 slots
- `mrgn4atx…` · 19.58K SOL · commission 0% · lag 8761 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 173504 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 4020 slots
- `4GEEKSwu…` · 196.81 SOL · commission 5% · lag 1238693 slots
- `EWARp8Sy…` · 99.63 SOL · commission 5% · lag 52309 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 1349208 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 17512622 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 447048305 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 792278 slots
- `4kdjgZKJ…` · 1.05 SOL · commission 100% · lag 447048305 slots

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
| **In-protocol fees 24h** | **$711.96K** (6,973.3 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-12 |
| **Solana REV** | **7,963.8 SOL** / **$813.09K** | MEASURED UTC calendar day 2026-09-12: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-12 · UTC day 2026-09-12 · SOL-USD date 2026-09-12 |
| Jito tip-floor run-rate (NOT REV) | $77.12K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 77118 USD; at p95 floor → 5168743 USD. |
| Protocol fees 24h | $14.04M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9981 |
| p90 / p99 | 0.000010 / 0.000128 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.60 | coingecko.simple_price |
| 24h change | +2.40% | coingecko.simple_price |
| Market cap | $60.80B | coingecko.simple_price |
| 24h volume | $3.11B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.94B |
| TVL 1d / 7d / 30d | +0.52% / -1.13% / +22.98% |
| DEX volume 24h | $1.79B · 1d +2.72% · vs-7d-ago -39.77% |
| 7d DEX volume | $18.46B · +11.83% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.04M |
| Fees 1d / 7d | +3.22% / -4.96% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $315.70M | -16.29% |
| Raydium AMM | $272.83M | -16.35% |
| BisonFi | $201.48M | +23.85% |
| Meteora DLMM | $157.73M | -2.07% |
| fomo Wallet | $155.24M | -27.53% |
| Orca DEX | $136.37M | +53.30% |
| Manifest Trade | $109.11M | +21.02% |
| HumidiFi | $108.44M | +27.53% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.57B | +2.18% | -1.58% |
| Kamino Lend | Lending | $1.36B | +1.14% | +2.10% |
| Raydium AMM | Dexs | $1.15B | +2.25% | +1.10% |
| Jupiter Lend | Lending | $1.11B | +1.31% | +1.69% |
| Binance Staked SOL | Liquid Staking | $1.06B | +1.88% | -2.14% |
| Jito Liquid Staking | Liquid Staking | $1.05B | +1.92% | -1.46% |
| BlackRock BUIDL | RWA | $992.89M | +0.02% | -2.23% |
| Jupiter Perpetual Exchange | Derivatives | $756.18M | +1.24% | +0.52% |
| Jupiter Staked SOL | Liquid Staking | $530.08M | +1.98% | -2.02% |
| Marinade Native | Staking Pool | $390.55M | +1.82% | -5.77% |

## Stablecoins

Solana circulating pegged-USD: **$15.96B**
(1d -1.04% · 7d -2.32%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.18B | -1.73% |
| USDT · Tether | $2.49B | -2.36% |
| USDGO · USDGO | $1.39B | +0.65% |
| USD1 · World Liberty Financial USD | $1.31B | -0.00% |
| BUIDL · BlackRock USD | $992.89M | +0.03% |
| PYUSD · PayPal USD | $685.92M | -2.86% |
| USDG · Global Dollar | $619.01M | +2.55% |
| USDe · Ethena USDe | $531.38M | -0.76% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $109.24M (lower bound, not a census).
24h volume $91.97M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.93B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.89M
- **OnRe** (RWA) — $299.62M
- **Huma Finance V2** (RWA) — $194.13M
- **Ondo Yield Assets** (RWA) — $179.89M
- **Hastra** (RWA) — $142.80M
- **Ondo Global Markets** (RWA) — $27.62M
- **Plume Vaults** (RWA) — $27.59M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.40M

## Daily active addresses

808,902 (Allium, as of 2026-09-13). Provider range 394,537–881,822. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @anza_xyz: 🚨 V1 Transactions 🚨 

Coming in Epoch 1035 (~ 9 hours)!](https://x.com/readylayerone/status/2099527253936034154) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 14 Sep 2026 15:54:39 GMT
- [RT by @anza_xyz: Solana is the most battle-tested network.

Each stress test on Solana has been met with major improvements by the core engineering teams and further improved the network resiliency time over time.

Solana's resiliency isn't just about surviving the worst days, but also making ambition for a better future possible.

https://www.thestreet.com/crypto/innovation/solana-building-proving-and-earning-trust-in-public](https://x.com/jacobvcreech/status/2099517991662538803) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 14 Sep 2026 15:17:51 GMT
- [RT by @anza_xyz: The way you experience @solana dev content has just changed forever. 

Give a follow to @solanadevs on Instagram: https://www.instagram.com/solanadevs](https://x.com/solana_devs/status/2099186847343661436) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 13 Sep 2026 17:22:00 GMT
- [Step 2 of SIMD-0437 rent reduction is live.

How to reclaim excess SOL: https://x.com/a_milz/status/2095532192579661927?s=20](https://x.com/anza_xyz/status/2098519198783922184) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 21:09:00 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: 🚨JUST IN: The second wave of rent stimmy for @Solana users is on the way.

Rent reduction Step 2 goes live on mainnet in 7 hours, making another 612,000 $SOL reclaimable and bringing the total to 918,000 $SOL. 

Across all five steps, up to 3.06M $SOL ($319M) will become reclaimable.](https://x.com/SolanaFloor/status/2098406673874612536) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 13:41:52 GMT `mainnet`
- [RT by @anza_xyz: Yesterday total trades:

NASDAQ: 60,091,499
Solana: 32,460,600

Less than 2x to go 🤯](https://x.com/vibhu/status/2098446478951772539) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 16:20:02 GMT
- [alpenGO ⛰️✅](https://x.com/anza_xyz/status/2098443881058803737) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 16:09:43 GMT
- [RT by @anza_xyz: V1 Transactions are coming next week! 
Tell a friend. Or be like @HeyAndyS and tell lots of friends!](https://x.com/a_milz/status/2098159473298907137) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 10 Sep 2026 21:19:35 GMT
- [Solana is the most battle-tested network.

Read about how continuous stress testing and improvements have shaped Solana into the technical masterpiece it is today in this new op-ed by @jacobvcreech👇](https://x.com/solana_devs/status/2099540790393389332) — X/Nitter-style RSS @solana_devs (not Twitter API) · Mon, 14 Sep 2026 16:48:26 GMT
- [RT by @solana_devs: Solana Rent casually dropped again. 
Reclaim those Lamports 👇](https://x.com/a_milz/status/2099511002782199920) — X/Nitter-style RSS @solana_devs (not Twitter API) · Mon, 14 Sep 2026 14:50:04 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @anza_xyz: 🚨 V1 Transactions 🚨 

Coming in Epoch 1035 (~ 9 hours)!](https://x.com/readylayerone/status/2099527253936034154) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 14 Sep 2026 15:54:39 GMT
- [RT by @anza_xyz: Solana is the most battle-tested network.

Each stress test on Solana has been met with major improvements by the core engineering teams and further improved the network resiliency time over time.

Solana's resiliency isn't just about surviving the worst days, but also making ambition for a better future possible.

https://www.thestreet.com/crypto/innovation/solana-building-proving-and-earning-trust-in-public](https://x.com/jacobvcreech/status/2099517991662538803) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 14 Sep 2026 15:17:51 GMT
- [RT by @anza_xyz: The way you experience @solana dev content has just changed forever. 

Give a follow to @solanadevs on Instagram: https://www.instagram.com/solanadevs](https://x.com/solana_devs/status/2099186847343661436) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 13 Sep 2026 17:22:00 GMT
- [Step 2 of SIMD-0437 rent reduction is live.

How to reclaim excess SOL: https://x.com/a_milz/status/2095532192579661927?s=20](https://x.com/anza_xyz/status/2098519198783922184) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 21:09:00 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: 🚨JUST IN: The second wave of rent stimmy for @Solana users is on the way.

Rent reduction Step 2 goes live on mainnet in 7 hours, making another 612,000 $SOL reclaimable and bringing the total to 918,000 $SOL. 

Across all five steps, up to 3.06M $SOL ($319M) will become reclaimable.](https://x.com/SolanaFloor/status/2098406673874612536) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 13:41:52 GMT `mainnet`
- [RT by @anza_xyz: Yesterday total trades:

NASDAQ: 60,091,499
Solana: 32,460,600

Less than 2x to go 🤯](https://x.com/vibhu/status/2098446478951772539) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 16:20:02 GMT
- [alpenGO ⛰️✅](https://x.com/anza_xyz/status/2098443881058803737) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 16:09:43 GMT
- [RT by @anza_xyz: V1 Transactions are coming next week! 
Tell a friend. Or be like @HeyAndyS and tell lots of friends!](https://x.com/a_milz/status/2098159473298907137) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 10 Sep 2026 21:19:35 GMT
- [Solana is the most battle-tested network.

Read about how continuous stress testing and improvements have shaped Solana into the technical masterpiece it is today in this new op-ed by @jacobvcreech👇](https://x.com/solana_devs/status/2099540790393389332) — X/Nitter-style RSS @solana_devs (not Twitter API) · Mon, 14 Sep 2026 16:48:26 GMT
- [RT by @solana_devs: Solana Rent casually dropped again. 
Reclaim those Lamports 👇](https://x.com/a_milz/status/2099511002782199920) — X/Nitter-style RSS @solana_devs (not Twitter API) · Mon, 14 Sep 2026 14:50:04 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-14 (2026-09-14 11:46:08 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 56ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 116ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 37ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 41ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 31ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5837ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 58ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 149ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 42ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 64ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 34ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 95ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 868ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 86ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 30ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 67ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 101ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 402ms https://solana.com/data
- `solana.com.databricks` [ok] 200 129ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 389ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 57ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 30ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 61ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 247ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 233ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 62ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 54ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 54ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 597ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 237ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1714ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 3447ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 246ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 92ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 27ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 30ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 300ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 270ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 401ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 399ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 418ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 359ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 34ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 1152ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 319ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 351ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 482ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 391ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 307ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 293ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 327ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1298ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1236ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1293ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1760ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1368ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1518ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1275ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 2490ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.QQQx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.WRLDx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.SPYx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.XRXx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.WGSx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.circ.QQQx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.price.INDIx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.mult.QQQx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.FLNCx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.PCTx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.SPYx` [ok] 200 497ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.METCx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.METCx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.QUBTx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.mult.METCx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.WRLDx` [ok] 200 1151ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 1071ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 1090ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.WGSx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.PCTx` [ok] 200 1136ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.price.DRSx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.price.SCIx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.circ.FLNCx` [ok] 200 1565ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 1116ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.DRSx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.circ.SCIx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 1683ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 1055ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.BSYx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.mult.SCIx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.GSATx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.mult.DRSx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.MPx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.price.DVAx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.circ.WYFIx` [ok] 200 1312ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 1178ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.price.SAILx` [ok] 200 666ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.mult.WYFIx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.DCIx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.mult.BETRx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.price.GDDYx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.circ.GSATx` [ok] 200 1012ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.circ.BSYx` [ok] 200 1169ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.circ.MPx` [ok] 200 1177ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.mult.GSATx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.mult.BSYx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.circ.SAILx` [ok] 200 1112ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.price.BXPx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.mult.MPx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.mult.SAILx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 1273ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.circ.DVAx` [ok] 200 1571ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.circ.RYANx` [ok] 200 1102ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.mult.DVAx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.mult.DCIx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.price.DYx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.mult.RYANx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.circ.GDDYx` [ok] 200 1335ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.price.WMSx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.price.ALSNx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.price.FDSx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.price.AMx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.mult.GDDYx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.price.SMTCx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.circ.BXPx` [ok] 200 1196ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.mult.BXPx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.SFx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.circ.DYx` [ok] 200 1043ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.circ.FRHCx` [ok] 200 1071ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.circ.ALSNx` [ok] 200 1067ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.circ.FDSx` [ok] 200 1059ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.price.AXSMx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.mult.ALSNx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 1144ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.price.EGPx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.mult.FRHCx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.mult.AMx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.circ.SMTCx` [ok] 200 1201ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.price.BPOPx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.mult.FDSx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.mult.SMTCx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.price.TTMIx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.price.DPZx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.price.AEISx` [ok] 200 521ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.circ.SFx` [ok] 200 1385ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.circ.EGPx` [ok] 200 1072ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.circ.AXSMx` [ok] 200 1307ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.mult.EGPx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.mult.SFx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.mult.AXSMx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 1167ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.price.HRLx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.price.KTOSx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.price.PAGx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.circ.TTMIx` [ok] 200 999ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.BPOPx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.circ.WMSx` [ok] 200 2956ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.mult.TTMIx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.circ.DPZx` [ok] 200 1105ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.price.SEICx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.price.HIIx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.mult.WMSx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.EHCx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.circ.AEISx` [ok] 200 1285ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.mult.DPZx` [ok] 200 400ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.price.GFLx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.mult.AEISx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.circ.GFLx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.price.ARx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.mult.GFLx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.circ.PAGx` [ok] 200 1043ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.circ.HRLx` [ok] 200 1077ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.price.MGMx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.mult.HRLx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.mult.PAGx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.circ.SEICx` [ok] 200 1056ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.price.HALOx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.mult.SEICx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.circ.KTOSx` [ok] 200 1479ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.mult.KTOSx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.price.DOCUx` [ok] 200 562ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.price.WTRGx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.circ.EHCx` [ok] 200 1328ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.price.AFGx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.mult.EHCx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.circ.ARx` [ok] 200 1299ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.price.HUBSx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.circ.MGMx` [ok] 200 1271ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.mult.ARx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 2180ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.mult.MGMx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.price.AMKRx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.price.GMEDx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.mult.HIIx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.circ.HALOx` [ok] 200 1358ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.circ.DOCUx` [ok] 200 1098ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.circ.WTRGx` [ok] 200 1150ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.price.JKHYx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.DOCUx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.mult.HALOx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.circ.AFGx` [ok] 200 1272ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.price.OCx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.price.IESCx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.price.CRx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.mult.AFGx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.price.BMRNx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.circ.HUBSx` [ok] 200 1214ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.mult.HUBSx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.circ.GMEDx` [ok] 200 1122ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.circ.AMKRx` [ok] 200 1230ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.mult.AMKRx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.price.JEFx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.price.AMHx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.IESCx` [ok] 200 988ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.price.FIVEx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.circ.OCx` [ok] 200 1089ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.circ.JEFx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.circ.JKHYx` [ok] 200 1355ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.mult.JEFx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.circ.CRx` [ok] 200 1202ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.mult.OCx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.price.ITx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.mult.CRx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.mult.JKHYx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.price.MDGLx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.price.VNOMx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.mult.IESCx` [ok] 200 551ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.AHRx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.circ.BMRNx` [ok] 200 1867ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.circ.FIVEx` [ok] 200 1125ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.price.UHALx` [ok] 200 761ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.circ.ITx` [ok] 200 872ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.mult.BMRNx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.mult.FIVEx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.price.IVZx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.price.CORTx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.mult.ITx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.circ.VNOMx` [ok] 200 1014ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.price.STRLx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.circ.STRLx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.mult.VNOMx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.circ.MDGLx` [ok] 200 1497ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.mult.STRLx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.price.NWSAx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.price.AURx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.circ.AHRx` [ok] 200 1280ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.circ.UHALx` [ok] 200 1195ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.mult.MDGLx` [ok] 200 496ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.mult.UHALx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.price.ARWRx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.mult.AHRx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.Hx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.circ.AMHx` [ok] 200 2861ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.price.GWREx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.mult.AMHx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.circ.NWSAx` [ok] 200 1029ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 1012ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.price.NWSx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.mult.AURx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.circ.IVZx` [ok] 200 1880ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.price.MANHx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.mult.NWSAx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.circ.Hx` [ok] 200 902ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.circ.MANHx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.circ.CORTx` [ok] 200 2213ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.price.CACIx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.mult.MANHx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.Hx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.circ.GWREx` [ok] 200 1132ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.circ.ARWRx` [ok] 200 1334ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.mult.IVZx` [ok] 200 627ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.mult.CORTx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.BAXx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.mult.GWREx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.mult.ARWRx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.circ.BAXx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.BAXx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.circ.CACIx` [ok] 200 1096ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 3247ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.NWSx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1267ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 162ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.QUBTx` [ok] 200 40ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.INDIx` [ok] 200 53ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.WRLDx` [ok] 200 50ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.BETRx` [ok] 200 53ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.FLNCx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.XRXx` [ok] 200 44ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.AIx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.WGSx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jito.tip_floor` [ok] 200 264ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 368ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 82ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 59ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 40ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 51ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 36ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 101ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
