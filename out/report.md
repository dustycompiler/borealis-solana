# Borealis — Solana ecosystem report

**Generated** 2026-09-14T20:37:50Z · 2026-09-14 13:37:50 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-14T20:37:40Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +3.24%; DEX 24h $1.79B · 1d +3% · vs-7d-ago -40%; slot 317 ms
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
| Slot | 447,069,422 |
| Block height | 425,111,777 |
| Block time | 2026-09-14T20:37:40Z |
| Epoch | 1,034 (88.29% · slot 381,423/432,000) |
| Mean TPS (last ~3,600s) | 4,302.3 |
| Mean non-vote TPS | 2,177.0 |
| Median TPS (same window) | 4,283.8 |
| Mean slot time | 317.4 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 548,475,776,922 |
| Circulating supply | 586,892,438 SOL |
| Total supply | 634,017,183 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 678 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 438,502,249 SOL |
| Delinquent stake | 238,117.66 SOL (0.054%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.30% / 35.54% |
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

- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 508984 slots
- `D3htsc6i…` · 77.60K SOL · commission 5% · lag 8761 slots
- `mrgn4atx…` · 19.58K SOL · commission 0% · lag 29878 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 194621 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 25137 slots
- `4GEEKSwu…` · 196.81 SOL · commission 5% · lag 1259810 slots
- `EWARp8Sy…` · 99.63 SOL · commission 5% · lag 73426 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 1370325 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 17533739 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 447069422 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 813395 slots
- `4kdjgZKJ…` · 1.05 SOL · commission 100% · lag 447069422 slots

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
| Jito tip-floor run-rate (NOT REV) | $69.91K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 69910 USD; at p95 floor → 2459550 USD. |
| Protocol fees 24h | $14.04M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9948 |
| p90 / p99 | 0.000010 / 0.000169 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $104.61 | coingecko.simple_price |
| 24h change | +3.24% | coingecko.simple_price |
| Market cap | $61.37B | coingecko.simple_price |
| 24h volume | $3.41B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.95B |
| TVL 1d / 7d / 30d | +0.70% / -0.95% / +23.20% |
| DEX volume 24h | $1.79B · 1d +2.72% · vs-7d-ago -39.77% |
| 7d DEX volume | $18.46B · +11.83% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.04M |
| Fees 1d / 7d | +3.22% / -4.96% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $315.70M | -16.29% |
| Raydium AMM | $280.35M | -14.04% |
| BisonFi | $201.48M | +23.85% |
| Meteora DLMM | $157.73M | -2.07% |
| fomo Wallet | $155.24M | -27.53% |
| Orca DEX | $136.37M | +53.30% |
| Manifest Trade | $116.34M | +29.04% |
| HumidiFi | $108.44M | +27.53% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.58B | +2.40% | -0.22% |
| Kamino Lend | Lending | $1.36B | +1.08% | +2.19% |
| Raydium AMM | Dexs | $1.15B | +2.25% | +1.10% |
| Jupiter Lend | Lending | $1.11B | +1.25% | +2.08% |
| Binance Staked SOL | Liquid Staking | $1.07B | +2.40% | -0.69% |
| Jito Liquid Staking | Liquid Staking | $1.06B | +2.45% | -0.08% |
| BlackRock BUIDL | RWA | $992.89M | +0.02% | -2.23% |
| Jupiter Perpetual Exchange | Derivatives | $760.67M | +1.60% | +1.01% |
| Jupiter Staked SOL | Liquid Staking | $534.99M | +2.40% | -0.56% |
| Marinade Native | Staking Pool | $392.91M | +2.02% | -4.66% |

## Stablecoins

Solana circulating pegged-USD: **$16.01B**
(1d -1.03% · 7d -2.31%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.22B | -1.18% |
| USDT · Tether | $2.49B | -2.36% |
| USDGO · USDGO | $1.39B | +0.65% |
| USD1 · World Liberty Financial USD | $1.32B | +1.15% |
| BUIDL · BlackRock USD | $992.89M | +0.03% |
| PYUSD · PayPal USD | $685.25M | -2.95% |
| USDG · Global Dollar | $609.94M | +1.05% |
| USDe · Ethena USDe | $531.97M | -0.66% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $109.53M (lower bound, not a census).
24h volume $93.73M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.93B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.89M
- **OnRe** (RWA) — $299.62M
- **Huma Finance V2** (RWA) — $194.13M
- **Ondo Yield Assets** (RWA) — $179.93M
- **Hastra** (RWA) — $142.13M
- **Plume Vaults** (RWA) — $27.59M
- **Ondo Global Markets** (RWA) — $26.65M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.37M

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
- [Transaction v1 goes live on mainnet in ~5 hours](https://x.com/solana_devs/status/2099590412042191264) — X/Nitter-style RSS @solana_devs (not Twitter API) · Mon, 14 Sep 2026 20:05:37 GMT `mainnet`
- [Solana is the most battle-tested network.

Read about how continuous stress testing and improvements have shaped Solana into the technical masterpiece it is today in this new op-ed by @jacobvcreech👇](https://x.com/solana_devs/status/2099540790393389332) — X/Nitter-style RSS @solana_devs (not Twitter API) · Mon, 14 Sep 2026 16:48:26 GMT

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
- [Transaction v1 goes live on mainnet in ~5 hours](https://x.com/solana_devs/status/2099590412042191264) — X/Nitter-style RSS @solana_devs (not Twitter API) · Mon, 14 Sep 2026 20:05:37 GMT `mainnet`
- [Solana is the most battle-tested network.

Read about how continuous stress testing and improvements have shaped Solana into the technical masterpiece it is today in this new op-ed by @jacobvcreech👇](https://x.com/solana_devs/status/2099540790393389332) — X/Nitter-style RSS @solana_devs (not Twitter API) · Mon, 14 Sep 2026 16:48:26 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-14 (2026-09-14 13:37:50 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~317 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~317 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 291ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 166ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 268ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 200ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 116ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6589ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 247ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 168ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 92ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 141ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 78ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 412ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1044ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 485ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 101ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 861ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 926ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 381ms https://solana.com/data
- `solana.com.databricks` [ok] 200 288ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 411ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 184ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 149ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 172ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 296ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 322ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 134ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 113ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 147ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 342ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 274ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2313ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1642ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 396ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 95ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 281ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 136ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 666ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 652ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 742ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 821ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 823ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 955ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 798ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 871ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 826ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 701ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 800ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 710ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 899ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 764ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1628ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1410ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1450ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1408ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 3292ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1575ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1446ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1225ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.INDIx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.SPYx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.WGSx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.COINx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.SPYx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 550ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.COINx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.XRXx` [ok] 200 644ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.FLNCx` [ok] 200 785ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.circ.QQQx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.WRLDx` [ok] 200 1187ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.METCx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.mult.SPYx` [ok] 200 968ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.PCTx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.WGSx` [ok] 200 1337ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.QUBTx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.circ.XRXx` [ok] 200 1285ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 1253ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.INDIx` [ok] 200 2083ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 1145ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.mult.WRLDx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 1156ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.price.DRSx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.circ.BETRx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.SCIx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.mult.BETRx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 1133ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.SCIx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.price.BSYx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.price.SAILx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.circ.DRSx` [ok] 200 574ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.circ.BSYx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.price.AIx` [ok] 200 1163ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.SCIx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 514ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.circ.METCx` [ok] 200 2276ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.GSATx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.circ.SAILx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.mult.BSYx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.circ.WYFIx` [ok] 200 1695ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 487ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.mult.SAILx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.circ.GSATx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.price.MPx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.mult.METCx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.price.DVAx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.circ.MPx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.price.GDDYx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.mult.WYFIx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.circ.DVAx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.mult.GSATx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.mult.MPx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.circ.GDDYx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.price.DCIx` [ok] 200 670ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.price.BXPx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.circ.RYANx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.price.DYx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.mult.DVAx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.mult.GDDYx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 1231ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.DYx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.price.WMSx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.circ.BXPx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.circ.FRHCx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.circ.DCIx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.circ.WMSx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.price.AMx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.mult.DYx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.mult.RYANx` [ok] 200 565ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.mult.FRHCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.price.FDSx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.price.ALSNx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.mult.DCIx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.price.SMTCx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.circ.FDSx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.mult.WMSx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.AXSMx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.mult.AMx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.circ.ALSNx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.mult.BXPx` [ok] 200 826ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.EGPx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.price.BPOPx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.circ.SMTCx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.circ.AXSMx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.price.TTMIx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.mult.FDSx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.price.SFx` [ok] 200 729ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.mult.ALSNx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.circ.EGPx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.mult.AXSMx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.mult.SMTCx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.price.DPZx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.circ.SFx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.circ.TTMIx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.price.AEISx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.mult.EGPx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.mult.BPOPx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.circ.DPZx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.circ.AEISx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.price.HRLx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.price.SEICx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.mult.SFx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.price.PAGx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.mult.DPZx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.circ.HRLx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.circ.SEICx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.mult.AEISx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.price.KTOSx` [ok] 200 677ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.circ.PAGx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.price.EHCx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.price.GFLx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.mult.HRLx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.circ.EHCx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.mult.PAGx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.mult.TTMIx` [ok] 200 801ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.ARx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.price.DOCUx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.mult.SEICx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.price.MGMx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.price.HIIx` [ok] 200 884ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.mult.EHCx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.circ.ARx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.circ.DOCUx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.price.HALOx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.price.WTRGx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.mult.ARx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.circ.HALOx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.circ.MGMx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.mult.DOCUx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.circ.KTOSx` [ok] 200 1115ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.price.HUBSx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.circ.WTRGx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.mult.HALOx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.circ.GFLx` [ok] 200 1138ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.KTOSx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.mult.MGMx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.circ.HUBSx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.mult.GFLx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.mult.HIIx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.price.GMEDx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.price.AMKRx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.price.JKHYx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.HUBSx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.price.IESCx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.price.AFGx` [ok] 200 805ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.circ.JKHYx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.price.CRx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.price.BMRNx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.price.OCx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.mult.JKHYx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.mult.AFGx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.circ.OCx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.price.JEFx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.price.AMHx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.mult.GMEDx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.mult.OCx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.price.FIVEx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.circ.AMHx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.price.ITx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.circ.IESCx` [ok] 200 1188ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.circ.AMKRx` [ok] 200 1302ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.circ.ITx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.mult.AMKRx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.circ.CRx` [ok] 200 1236ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.price.MDGLx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.price.VNOMx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.circ.BMRNx` [ok] 200 1385ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.mult.IESCx` [ok] 200 548ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.mult.CRx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.circ.JEFx` [ok] 200 1302ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.mult.BMRNx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.price.UHALx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.price.AHRx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.price.IVZx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.mult.ITx` [ok] 200 897ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.JEFx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.circ.UHALx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.price.STRLx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.price.CORTx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.mult.UHALx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.circ.AHRx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.mult.AHRx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.AURx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.circ.IVZx` [ok] 200 1010ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.circ.MDGLx` [ok] 200 1681ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.price.NWSAx` [ok] 200 867ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.circ.VNOMx` [ok] 200 1692ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.circ.FIVEx` [ok] 200 2291ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.mult.IVZx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.circ.CORTx` [ok] 200 992ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.mult.MDGLx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.circ.STRLx` [ok] 200 1140ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.price.ARWRx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.mult.CORTx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.mult.VNOMx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.mult.FIVEx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.mult.STRLx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.price.GWREx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.price.NWSx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.circ.AURx` [ok] 200 966ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.mult.AURx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.price.CACIx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.price.MANHx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.price.Hx` [ok] 200 808ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.circ.CACIx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.price.BAXx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.MANHx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.circ.BAXx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.circ.ARWRx` [ok] 200 1036ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.circ.GWREx` [ok] 200 904ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.circ.NWSx` [ok] 200 985ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.circ.NWSAx` [ok] 200 1707ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.mult.NWSx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.mult.NWSAx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.mult.GWREx` [ok] 200 565ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.circ.Hx` [ok] 200 1119ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.mult.Hx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 606ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 228ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.QUBTx` [ok] 200 115ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.INDIx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.WRLDx` [ok] 200 125ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.BETRx` [ok] 200 121ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.FLNCx` [ok] 200 120ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.XRXx` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.AIx` [ok] 200 123ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.WGSx` [ok] 200 118ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jito.tip_floor` [ok] 200 205ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 349ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 149ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 122ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 117ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 120ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 117ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 401ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
