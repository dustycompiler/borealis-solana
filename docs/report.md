# Borealis — Solana ecosystem report

**Generated** 2026-09-12T14:06:19Z · 2026-09-12 07:06:19 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-12T14:06:08Z · **RPC health** `ok`
**Health score** 91 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -2.86%; DEX 24h $3.18B · 1d +9% · vs-7d-ago +69%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +22.31%. (threshold: `|1d %| >= 8`)
- **ALERT · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +71.21%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 967,396.00 is +21.7% vs 30d median 794,650.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +8.96%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +69.19%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 446,448,001 |
| Block height | 424,490,796 |
| Block time | 2026-09-12T14:06:08Z |
| Epoch | 1,033 (44.45% · slot 192,003/432,000) |
| Mean TPS (last ~3,600s) | 3,481.1 |
| Mean non-vote TPS | 1,356.0 |
| Median TPS (same window) | 3,480.2 |
| Mean slot time | 317.2 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 547,733,050,072 |
| Circulating supply | 586,632,859 SOL |
| Total supply | 633,924,134 SOL |
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
| Activated stake | 435,137,392 SOL |
| Delinquent stake | 1,700,289.29 SOL (0.389%) |
| Nakamoto (33% / 50% / 67%) | 18 / 40 / 79 |
| Top 10 / 20 stake share | 24.49% / 35.86% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.56M SOL | 4.03% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.36M SOL | 3.76% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.52M SOL | 2.88% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.37M SOL | 2.61% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.67M SOL | 2.22% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.23M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.02M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.36M SOL | 1.69% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.94M SOL | 1.60% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.55M SOL | 1.51% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.13M SOL | 1.41% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.12M SOL | 1.41% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.37% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.62M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `pSo1KZXg…` · 1.64M SOL · commission 4% · lag 191974 slots
- `EWARp8Sy…` · 31.93K SOL · commission 5% · lag 23840 slots
- `mrgn4atx…` · 19.58K SOL · commission 0% · lag 55768 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 191974 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 191974 slots
- `4GEEKSwu…` · 326.50 SOL · commission 5% · lag 638389 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 748904 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 446448001 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 62399131 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 191974 slots
- `4kdjgZKJ…` · 1.05 SOL · commission 100% · lag 446448001 slots
- `3BoZ4AF2…` · 1.00 SOL · commission 100% · lag 446448001 slots

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
| **In-protocol fees 24h** | **$714.96K** (7,191.9 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-10 |
| **Solana REV** | **8,405.9 SOL** / **$835.65K** | MEASURED UTC calendar day 2026-09-10: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-10 · UTC day 2026-09-10 · SOL-USD date 2026-09-10 |
| Jito tip-floor run-rate (NOT REV) | $21.16K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 21164 USD; at p95 floor → 241501 USD. |
| Protocol fees 24h | $17.88M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9945 |
| p90 / p99 | 0.000010 / 0.000070 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $101.94 | coingecko.simple_price |
| 24h change | -2.86% | coingecko.simple_price |
| Market cap | $59.80B | coingecko.simple_price |
| 24h volume | $3.30B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.90B |
| TVL 1d / 7d / 30d | +2.57% / +0.46% / +22.01% |
| DEX volume 24h | $3.18B · 1d +8.96% · vs-7d-ago +69.19% |
| 7d DEX volume | $19.31B · +29.54% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $17.88M |
| Fees 1d / 7d | +22.31% / +71.21% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| BisonFi | $471.70M | +19.17% |
| Raydium AMM | $384.57M | +6.29% |
| Meteora DLMM | $363.04M | +64.69% |
| PumpSwap | $294.17M | -37.16% |
| Orca DEX | $213.61M | +27.29% |
| Tessera V | $202.03M | -12.92% |
| Manifest Trade | $163.39M | +12.12% |
| HumidiFi | $155.95M | -51.67% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.56B | +2.69% | -0.17% |
| Kamino Lend | Lending | $1.35B | +1.67% | +2.39% |
| Raydium AMM | Dexs | $1.14B | +2.47% | +2.84% |
| Jupiter Lend | Lending | $1.10B | +2.77% | +0.40% |
| Binance Staked SOL | Liquid Staking | $1.06B | +2.41% | -0.54% |
| Jito Liquid Staking | Liquid Staking | $1.05B | +2.60% | -0.00% |
| BlackRock BUIDL | RWA | $992.60M | -0.61% | -2.25% |
| Jupiter Perpetual Exchange | Derivatives | $753.33M | +1.91% | +0.11% |
| Jupiter Staked SOL | Liquid Staking | $527.78M | +1.87% | -0.32% |
| Marinade Native | Staking Pool | $389.19M | +2.70% | -3.63% |

## Stablecoins

Solana circulating pegged-USD: **$16.13B**
(1d +1.20% · 7d -0.31%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.24B | +3.68% |
| USDT · Tether | $2.60B | -2.99% |
| USDGO · USDGO | $1.38B | -0.01% |
| USD1 · World Liberty Financial USD | $1.30B | +1.51% |
| BUIDL · BlackRock USD | $992.60M | +0.01% |
| PYUSD · PayPal USD | $706.84M | -5.31% |
| USDG · Global Dollar | $596.15M | -0.49% |
| USDe · Ethena USDe | $535.75M | -0.16% |

## Tokenized equities (xStocks)


Listed 800 · Solana deployments 800 · priced 0 · priced-subset mcap — (lower bound, not a census).
24h volume $92.89M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 0 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.92B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.60M
- **OnRe** (RWA) — $294.85M
- **Huma Finance V2** (RWA) — $191.54M
- **Ondo Yield Assets** (RWA) — $180.05M
- **Hastra** (RWA) — $148.78M
- **Plume Vaults** (RWA) — $27.43M
- **Ondo Global Markets** (RWA) — $25.93M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.35M

## Daily active addresses

967,396 (Allium, as of 2026-09-10). Provider range 482,447–988,015. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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
- [RT by @anza_xyz: Step 2 of rent reduction (SIMD-0437) goes live today.

Lamports per byte drops 6,333 → 5,080 at epoch 1033. With step 2, rent will have dropped 27% from its initial value.

Read more here: https://solana.com/upgrades/reduced-rent](https://x.com/solana_devs/status/2098426593538388400) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 15:01:01 GMT `upgrade`
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
- [For Solana builders heading to Token2049 this October. 

Applications are now open the Origins Hackathon. $150k prizes.

Apply now: https://builderbase.com/event/token2049-origins-hackathon](https://x.com/solana_devs/status/2098766882505425123) — X/Nitter-style RSS @solana_devs (not Twitter API) · Sat, 12 Sep 2026 13:33:12 GMT
- [RT by @solana_devs: been working on this with the @SolanaFndn team. 

pretty cool seeing it live now.

http://hackathons.solana.com brings the whole flow into one place: find a hackathon, register, check the tracks and deadlines, build your project and submit it for judging.

teams can sponsor tracks, builders can explore projects in the showcase, and the leaderboard keeps track of participation across hackathons.

Stocklana is already live with $100k in prizes. go have a look and start building.](https://x.com/0xSrMessi/status/2098517552162898430) — X/Nitter-style RSS @solana_devs (not Twitter API) · Fri, 11 Sep 2026 21:02:27 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

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
- [RT by @anza_xyz: Step 2 of rent reduction (SIMD-0437) goes live today.

Lamports per byte drops 6,333 → 5,080 at epoch 1033. With step 2, rent will have dropped 27% from its initial value.

Read more here: https://solana.com/upgrades/reduced-rent](https://x.com/solana_devs/status/2098426593538388400) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 15:01:01 GMT `upgrade`
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
- [For Solana builders heading to Token2049 this October. 

Applications are now open the Origins Hackathon. $150k prizes.

Apply now: https://builderbase.com/event/token2049-origins-hackathon](https://x.com/solana_devs/status/2098766882505425123) — X/Nitter-style RSS @solana_devs (not Twitter API) · Sat, 12 Sep 2026 13:33:12 GMT
- [RT by @solana_devs: been working on this with the @SolanaFndn team. 

pretty cool seeing it live now.

http://hackathons.solana.com brings the whole flow into one place: find a hackathon, register, check the tracks and deadlines, build your project and submit it for judging.

teams can sponsor tracks, builders can explore projects in the showcase, and the leaderboard keeps track of participation across hackathons.

Stocklana is already live with $100k in prizes. go have a look and start building.](https://x.com/0xSrMessi/status/2098517552162898430) — X/Nitter-style RSS @solana_devs (not Twitter API) · Fri, 11 Sep 2026 21:02:27 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-12 (2026-09-12 07:06:19 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks market cap** — Listed Solana-deployed xStocks but quote and/or circulating missing. Mcap omitted.
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.
- **xStocks** — price, circulating-supply, and/or currentMultiplier missing — market cap omitted (never assumed multiplier=1.0)

## Sources this run

- `rpc.getHealth` [ok] 200 262ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 193ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 243ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 287ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 238ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6707ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 427ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 118ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 77ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 118ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 83ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 80ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 89ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 159ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 115ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 107ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 152ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 745ms https://solana.com/data
- `solana.com.databricks` [ok] 200 294ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 521ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 211ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 122ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 124ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 729ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 1674ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 254ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 236ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 510ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 940ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 204ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 4281ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 3567ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 288ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 201ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 174ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 189ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 736ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 674ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 723ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 713ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 787ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 724ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 794ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 881ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 735ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 700ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 723ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 850ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 648ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 663ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1433ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1582ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 912ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 892ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1142ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1043ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1346ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1445ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.QQQx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WRLDx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.COINx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/COINx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WGSx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.FLNCx` [FAIL]  12032ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SPYx` [FAIL]  12036ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.XRXx` [FAIL]  12043ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.INDIx` [FAIL]  12048ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WRLDx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 817ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.PCTx` [FAIL]  12048ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WYFIx` [FAIL]  12031ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METCx` [FAIL]  12047ms https://api.backed.fi/api/v2/public/assets/METCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.QUBTx` [FAIL]  12043ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BETRx` [FAIL]  12048ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AIx` [FAIL]  12048ms https://api.backed.fi/api/v2/public/assets/AIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DRSx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.PCTx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.DRSx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.circ.BETRx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.BETRx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.DRSx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.SCIx` [FAIL]  12039ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SCIx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.mult.METCx` [ok] 200 607ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.SCIx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.SAILx` [FAIL]  12038ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BSYx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GSATx` [FAIL]  12042ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MPx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/MPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DVAx` [FAIL]  12033ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DCIx` [FAIL]  12046ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BSYx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.circ.SAILx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.circ.MPx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.circ.DVAx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.mult.MPx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.mult.BSYx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.mult.SAILx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.price.GDDYx` [FAIL]  12034ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.DVAx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.price.RYANx` [FAIL]  12049ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.GDDYx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.mult.DCIx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.circ.RYANx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.mult.GDDYx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.mult.RYANx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.circ.GSATx` [ok] 200 998ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.mult.GSATx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.price.BXPx` [FAIL]  12038ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.FRHCx` [FAIL]  12031ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DYx` [FAIL]  12049ms https://api.backed.fi/api/v2/public/assets/DYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WMSx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.FRHCx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.circ.BXPx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.circ.DYx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.circ.WMSx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.price.AMx` [FAIL]  12033ms https://api.backed.fi/api/v2/public/assets/AMx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.BXPx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.FDSx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.DYx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.mult.FRHCx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.circ.FDSx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.price.ALSNx` [FAIL]  12036ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.AMx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.mult.FDSx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.circ.ALSNx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.mult.WMSx` [ok] 200 652ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.SMTCx` [FAIL]  12050ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.ALSNx` [ok] 200 525ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.circ.SMTCx` [ok] 200 555ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.mult.SMTCx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.price.SFx` [FAIL]  12046ms https://api.backed.fi/api/v2/public/assets/SFx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AXSMx` [FAIL]  12043ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.EGPx` [FAIL]  12032ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.EGPx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.circ.AXSMx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.circ.SFx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.price.BPOPx` [FAIL]  12057ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.AXSMx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.price.TTMIx` [FAIL]  12068ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SFx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.mult.EGPx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.price.AEISx` [FAIL]  12046ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BPOPx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.circ.TTMIx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.circ.AEISx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.mult.BPOPx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.mult.TTMIx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.DPZx` [FAIL]  12032ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.AEISx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.circ.DPZx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.price.HRLx` [FAIL]  12035ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.DPZx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.circ.HRLx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.mult.HRLx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.KTOSx` [FAIL]  12048ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PAGx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SEICx` [FAIL]  12034ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.KTOSx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.circ.PAGx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.circ.SEICx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.price.HIIx` [FAIL]  12049ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.KTOSx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.price.EHCx` [FAIL]  12035ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.PAGx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.mult.SEICx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.circ.EHCx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.circ.HIIx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.price.GFLx` [FAIL]  12044ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.EHCx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.HIIx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.price.ARx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/ARx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ARx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.price.MGMx` [FAIL]  12055ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MGMx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.mult.MGMx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.mult.ARx` [ok] 200 585ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.circ.GFLx` [ok] 200 1470ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.GFLx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.price.DOCUx` [FAIL]  12033ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HALOx` [FAIL]  12056ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WTRGx` [FAIL]  12042ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DOCUx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.circ.HALOx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.mult.DOCUx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.price.AFGx` [FAIL]  12041ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HUBSx` [FAIL]  12049ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.HALOx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.circ.AFGx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.circ.WTRGx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.circ.HUBSx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.mult.AFGx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.mult.HUBSx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.price.AMKRx` [FAIL]  12032ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GMEDx` [FAIL]  12036ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AMKRx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.mult.AMKRx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.price.JKHYx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.GMEDx` [ok] 200 422ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.circ.JKHYx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.mult.JKHYx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.price.IESCx` [FAIL]  12033ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.OCx` [FAIL]  12048ms https://api.backed.fi/api/v2/public/assets/OCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.IESCx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.circ.OCx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.price.CRx` [FAIL]  12038ms https://api.backed.fi/api/v2/public/assets/CRx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.IESCx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.BMRNx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.OCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.price.JEFx` [FAIL]  12046ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CRx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.circ.BMRNx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.circ.JEFx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.mult.CRx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.mult.BMRNx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.mult.JEFx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.price.AMHx` [FAIL]  12036ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AMHx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.price.FIVEx` [FAIL]  12036ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.AMHx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.price.ITx` [FAIL]  12045ms https://api.backed.fi/api/v2/public/assets/ITx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ITx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.circ.FIVEx` [ok] 200 686ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.mult.ITx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.FIVEx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.price.MDGLx` [FAIL]  12034ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.VNOMx` [FAIL]  12037ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MDGLx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.circ.VNOMx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.price.UHALx` [FAIL]  12037ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MDGLx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.mult.VNOMx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.IVZx` [FAIL]  12039ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AHRx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.UHALx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.circ.AHRx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.circ.IVZx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.mult.UHALx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.mult.IVZx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.mult.AHRx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.CORTx` [FAIL]  12046ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CORTx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.mult.CORTx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.STRLx` [FAIL]  12033ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.NWSAx` [FAIL]  12049ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.NWSAx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.circ.STRLx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.mult.NWSAx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.mult.STRLx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.price.AURx` [FAIL]  12064ms https://api.backed.fi/api/v2/public/assets/AURx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.Hx` [FAIL]  12048ms https://api.backed.fi/api/v2/public/assets/Hx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AURx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.circ.Hx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.price.ARWRx` [FAIL]  12050ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.AURx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.price.GWREx` [FAIL]  12035ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ARWRx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.circ.GWREx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.price.NWSx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.Hx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.mult.GWREx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.price.MANHx` [FAIL]  12033ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MANHx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.price.CACIx` [FAIL]  12034ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BAXx` [FAIL]  12036ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CACIx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.circ.BAXx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 73ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 337ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.WRLDx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.INDIx` [ok] 200 111ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.WGSx` [ok] 200 111ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.FLNCx` [ok] 200 113ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.XRXx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.PCTx` [ok] 200 131ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.BETRx` [ok] 200 124ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.QUBTx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jito.tip_floor` [ok] 200 185ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 279ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 192ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 164ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 158ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 187ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 284ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 1802ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
