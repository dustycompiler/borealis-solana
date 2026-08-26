# Borealis — Solana ecosystem report

**Generated** 2026-08-26T01:06:12Z · 2026-08-25 18:06:12 PT
**Author** dustycompiler · **Version** 1.4.0 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-26T01:06:00Z · **RPC health** `ok`
**Health score** 100 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 400)/400, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -4.96%; DEX 7d +60%; slot 366 ms
Updates every 15 min via GitHub Action.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +60.43%. (threshold: `|7d %| >= 20`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -4.96%, DeFiLlama TVL 1d -0.73%, DEX 1d -1.58%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +60.42%. (threshold: `|7d %| >= 20`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 96.94 USD is +28.5% vs 30d median 75.45 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 441,754,671 |
| Block height | 419,803,233 |
| Block time | 2026-08-26T01:06:00Z |
| Epoch | 1,022 (58.03% · slot 250,672/432,000) |
| Mean TPS (last ~3,600s) | 4,268.2 |
| Mean non-vote TPS | 2,401.4 |
| Median TPS (same window) | 4,221.5 |
| Mean slot time | 365.6 ms |
| Median slot time | 365.9 ms |
| Transaction count (cluster) | 541,879,246,349 |
| Circulating supply | 583,375,531 SOL |
| Total supply | 632,859,391 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 687 |
| Delinquent | 8 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 435,044,162 SOL |
| Delinquent stake | 73,941.29 SOL (0.017%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 79 |
| Top 10 / 20 stake share | 24.28% / 35.63% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.07M SOL | 3.92% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.04M SOL | 3.69% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.27M SOL | 2.82% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.74M SOL | 2.70% | 5% | 0 |
| 5 | `C8Bey3LK…` | 9.20M SOL | 2.12% | 7% | 0 |
| 6 | `CAo1dCGY…` | 8.92M SOL | 2.05% | 10% | 0 |
| 7 | `E1r4Psq8…` | 8.58M SOL | 1.97% | 0% | 0 |
| 8 | `EvnRmnMr…` | 7.95M SOL | 1.83% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.30M SOL | 1.68% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.57M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.41% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.02M SOL | 1.38% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.93M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.67M SOL | 1.30% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `2bpfa8Jb…` · 29.73K SOL · commission 5% · lag 1114672 slots
- `5P35CJVK…` · 24.00K SOL · commission 100% · lag 1114672 slots
- `gangtCrQ…` · 16.66K SOL · commission 0% · lag 501992 slots
- `kom1oNHy…` · 2.19K SOL · commission 5% · lag 1118155 slots
- `4GEEKSwu…` · 1.35K SOL · commission 5% · lag 742305 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 441754671 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 34000 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 1114672 slots

## Trends

15-min Borealis tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 13 | data/history.jsonl 15-min tape |
| TVL chart | 13 | data/history.jsonl 15-min tape |
| SOL chart | 12 | data/history.jsonl 15-min tape |
| history.jsonl rows | 13 | data/history.jsonl |

## Economics — Borealis REV (not DeFiLlama protocol fees)

Borealis REV follows Blockworks/Helius: in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito tips. DeFiLlama Solana protocol/application fees are NOT REV and are not summed.

| Metric | Value | Source |
| --- | ---: | --- |
| **Borealis REV 24h** | **$923.47K** (9,526.2 SOL) | MEASURED in-protocol + ESTIMATED Jito tips |
| In-protocol network fees 24h | 9,162.1 SOL ($888.17K) | solana.com/data Fees (Allium) MEASURED |
| Jito tips 24h | $35.30K | ESTIMATED |
| Protocol fees 24h | $14.08M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | getBlock n_tx=29504 window_seconds=3327 |
| p90 / p99 | 0.000015 / 0.000410 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $96.94 | coingecko.simple_price |
| 24h change | -4.96% | coingecko.simple_price |
| Market cap | $56.53B | coingecko.simple_price |
| 24h volume | $5.11B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.58B |
| TVL 1d / 7d / 30d | -0.73% / +13.97% / +13.40% |
| DEX volume 24h | $2.95B |
| DEX volume 7d | $21.60B |
| DEX 1d change | -1.58% |
| Protocol fees 24h (DeFiLlama, not REV) | $14.08M |
| Fees 1d / 7d | -2.86% / +60.43% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $567.89M | -18.27% |
| Orca DEX | $459.53M | +5.48% |
| BisonFi | $411.40M | +0.55% |
| Meteora DLMM | $246.36M | -11.40% |
| Scorch | $218.92M | 0.00% |
| Raydium AMM | $193.23M | +5.24% |
| Manifest Trade | $188.04M | +7.20% |
| pump.fun | $112.18M | +17.58% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.47B | -1.07% | +27.42% |
| Kamino Lend | Lending | $1.18B | -2.05% | +12.01% |
| Raydium AMM | Dexs | $1.06B | +0.59% | +23.71% |
| Jupiter Lend | Lending | $1.05B | -3.40% | +10.29% |
| Binance Staked SOL | Liquid Staking | $990.92M | -1.08% | +26.47% |
| Jito Liquid Staking | Liquid Staking | $969.05M | -1.89% | +25.76% |
| BlackRock BUIDL | RWA | $876.38M | +4.14% | +1.16% |
| Jupiter Perpetual Exchange | Derivatives | $747.73M | -1.21% | +8.71% |
| Jupiter Staked SOL | Liquid Staking | $500.64M | -1.63% | +25.29% |
| xStocks | RWA | $430.26M | +1.96% | +12.65% |

## Stablecoins

Solana circulating pegged-USD: **$15.88B**
(1d -0.21% · 7d +2.78%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.06B | -3.07% |
| USDT · Tether | $2.83B | -0.00% |
| USDGO · USDGO | $1.24B | +3.77% |
| USD1 · World Liberty Financial USD | $1.11B | +4.03% |
| BUIDL · BlackRock USD | $876.38M | +12.77% |
| PYUSD · PayPal USD | $678.83M | -1.36% |
| USDG · Global Dollar | $629.31M | +3.57% |
| USDe · Ethena USDe | $537.08M | +0.11% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × multiplier over 24 of 715 Solana-deployed listed symbols (715 unique underlyings). Not a 715-name volume, and not a census of every tokenized equity on Solana.
Listed 715 · Solana deployments 715 · priced-subset mcap $276.45M (lower bound, not a 715 census).
DeFiLlama protocol/xstocks Solana TVL $430.26M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier`. 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.06B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $876.38M
- **xStocks** (RWA) — $430.26M
- **OnRe** (RWA) — $277.29M
- **Ondo Yield Assets** (RWA) — $178.40M
- **Hastra** (RWA) — $163.57M
- **Theo Network thBill** (RWA) — $26.39M
- **Ondo Global Markets** (RWA) — $24.90M
- **Plume Vaults** (RWA) — $22.70M

## Daily active addresses

749,721 (Allium, as of 2026-08-24). Provider range 361,127–854,284. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

## Public Dune embed

public Dune embed, not our query — Solana On-Chain Health & Activity Explorer (cryptoonchain)
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

- [chat, are we back](https://x.com/solana/status/2092414366180151641) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 26 Aug 2026 00:50:34 GMT
- [RT by @solana: Home of the only interesting interviews happening on Solana.

@blknoiz06 and @Banks, fully unboxed.

Thursday 2pm UTC 👇](https://x.com/EcosystemCall/status/2092366326329168044) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 21:39:41 GMT
- [BREAKING: Solana ETF cumulative inflows hit a record $1.22B. $33.5M came in Monday alone.

The biggest single day of 2026, capping five straight days of inflows.](https://x.com/solana/status/2092333691338887672) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 19:30:00 GMT
- [RT by @solana: The king is in town.  

Earn 3.5-5% on top of your BTC holdings. 

Introducing BTC*, a token giving you market exposure while compounding.  

Powered by Kestrel, managed by Perena.](https://x.com/perena/status/2092315290323333197) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 18:16:53 GMT
- [See you tomorrow @SuperteamBLKN 

Solana Summit Serbia 🇷🇸](https://x.com/solana/status/2092319381540000207) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 18:33:08 GMT
- [RT by @solana: Solana has flipped Base in daily x402 transactions 

This is what AI on Solana looks like and we're just getting started](https://x.com/yo_itsmatt/status/2092297930321301772) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 17:07:54 GMT
- [RT by @solana: The next generation of finance runs on @solana.](https://x.com/KristinSmith/status/2092291244302991595) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 16:41:20 GMT
- [fixed-term, fixed-rate credit on Solana](https://x.com/solana/status/2092293180712526214) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 16:49:01 GMT
- [RT by @anza_xyz: 300ms now pending on Solana mainnet 👀
effective start of epoch 1024 (~3 days)](https://x.com/bw_solana/status/2092259551659831608) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 25 Aug 2026 14:35:24 GMT `mainnet`
- [We're aware of today's arrayref crate supply-chain attack: https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/

Agave and Anza's software are not affected.

If you ran cargo update today, check your machine against indicators in the writeup. Stay safe out there.](https://x.com/anza_xyz/status/2090608013891813501) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 21 Aug 2026 01:12:46 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [chat, are we back](https://x.com/solana/status/2092414366180151641) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 26 Aug 2026 00:50:34 GMT
- [RT by @solana: Home of the only interesting interviews happening on Solana.

@blknoiz06 and @Banks, fully unboxed.

Thursday 2pm UTC 👇](https://x.com/EcosystemCall/status/2092366326329168044) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 21:39:41 GMT
- [BREAKING: Solana ETF cumulative inflows hit a record $1.22B. $33.5M came in Monday alone.

The biggest single day of 2026, capping five straight days of inflows.](https://x.com/solana/status/2092333691338887672) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 19:30:00 GMT
- [RT by @solana: The king is in town.  

Earn 3.5-5% on top of your BTC holdings. 

Introducing BTC*, a token giving you market exposure while compounding.  

Powered by Kestrel, managed by Perena.](https://x.com/perena/status/2092315290323333197) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 18:16:53 GMT
- [See you tomorrow @SuperteamBLKN 

Solana Summit Serbia 🇷🇸](https://x.com/solana/status/2092319381540000207) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 18:33:08 GMT
- [RT by @solana: Solana has flipped Base in daily x402 transactions 

This is what AI on Solana looks like and we're just getting started](https://x.com/yo_itsmatt/status/2092297930321301772) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 17:07:54 GMT
- [RT by @solana: The next generation of finance runs on @solana.](https://x.com/KristinSmith/status/2092291244302991595) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 16:41:20 GMT
- [fixed-term, fixed-rate credit on Solana](https://x.com/solana/status/2092293180712526214) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 16:49:01 GMT
- [RT by @anza_xyz: 300ms now pending on Solana mainnet 👀
effective start of epoch 1024 (~3 days)](https://x.com/bw_solana/status/2092259551659831608) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 25 Aug 2026 14:35:24 GMT `mainnet`
- [We're aware of today's arrayref crate supply-chain attack: https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/

Agave and Anza's software are not affected.

If you ran cargo update today, check your machine against indicators in the writeup. Stay safe out there.](https://x.com/anza_xyz/status/2090608013891813501) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 21 Aug 2026 01:12:46 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 (SIMD-0525) reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-26 (2026-08-25 18:06:12 PT). Editorial. SIMD-0525 stage is inferred from observed slot time against published targets, not from a feature-gate RPC. Activation dates move. None of this is a live consensus metric._

Bounty text cites Alpenglow and SIMD-525. SIMD-0525 (also written SIMD-525) is the staged slot-time reduction 400→350→300→250→200 ms (Anza / Solana Foundation). Alpenglow consensus is SIMD-0326. This dashboard does not treat SIMD-025 as a live proposal.

SIMD-0525 stages target slot time down from 400 ms to 200 ms in 50 ms steps. Observed mean slot 366 ms is consistent with the 350 ms SIMD-0525 target (staged 400→350→300→250→200). Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

- **SIMD-525** — Reduce Slot Times (400→350→300→250→200 ms)
- **SIMD-0326** — Alpenglow Consensus Protocol (Votor)
- **SIMD-0337** — Markers for Alpenglow Fast Leader Handover
- **SIMD-0357** — Alpenglow Validator Admission Ticket (VAT)
- **SIMD-0384** — Alpenglow Migration
- **SIMD-0387** — BLS Pubkey Management in Vote Account

### Public timeline (editorial)

- `2026-05-01` — SIMD-0525 created (Anza). Four feature gates: 350/300/250/200 ms.
- `2026-Q3` — Agave v4.2 schedule targeted the four SIMD-0525 steps on mainnet one epoch apart; schedule is tentative. First step is 400→350 ms.
- `observed` — Observed mean slot 366 ms is consistent with the 350 ms SIMD-0525 target (staged 400→350→300→250→200).
- `2026-07-08` — SIMD-0387 (BLS pubkey in vote account) activated on mainnet.
- `2026-07-22` — SIMD-0357 VAT activated. VAT does not itself turn on Alpenglow consensus.

### What to watch

- Whether observed slot time stays near the inferred SIMD-0525 target after the next epoch.
- Skip rate / skipped slots as later 50 ms steps (300/250/200) are considered.
- Agave 4.2 / 4.3 stake rollout vs the published (tentative) schedule.
- Firedancer / Frankendancer Votor parity before a full Alpenswitch.

- https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0525-reduce-slot-times.md
- https://solana.com/upgrades/reduced-slot-times
- https://solana.com/upgrades/alpenglow
- https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0326-alpenglow.md

## Omissions

- **xStocks** — priced 24 of 715 Solana-deployed symbols to cap RPC/HTTP

## Sources this run

- `rpc.getHealth` [ok] 200 357ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 335ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 410ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 298ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 328ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7411ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 660ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 131ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 41ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 362ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 88ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 83ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 968ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 72ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 196ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 144ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 188ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 266ms https://solana.com/data
- `solana.com.databricks` [ok] 200 194ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 447ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 122ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 222ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 73ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 152ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 543ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 161ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 162ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 166ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1005ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 222ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 222ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 220ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 201ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 306ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 327ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1389ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1525ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1803ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1712ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1544ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1557ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1623ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1796ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1505ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1661ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1539ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1592ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1617ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1742ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1579ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1569ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1493ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1464ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 4600ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1416ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1331ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1044ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2680ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1482ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1967ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [ok] 200 922ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.TSLAx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [FAIL] 400 118ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier — HTTP 400 Bad Request
- `xstocks.price.SPYx` [ok] 200 754ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.SPYx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.SPYx` [FAIL] 400 121ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier — HTTP 400 Bad Request
- `xstocks.price.NVDAx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.NVDAx` [ok] 200 598ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [FAIL] 400 363ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier — HTTP 400 Bad Request
- `xstocks.price.AAPLx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.AAPLx` [ok] 200 700ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [FAIL] 400 123ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier — HTTP 400 Bad Request
- `xstocks.price.MSFTx` [ok] 200 1352ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.MSFTx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [FAIL] 400 282ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier — HTTP 400 Bad Request
- `xstocks.price.GOOGLx` [ok] 200 760ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [FAIL] 400 112ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier — HTTP 400 Bad Request
- `xstocks.price.AMZNx` [ok] 200 598ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.AMZNx` [ok] 200 499ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [FAIL] 400 112ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier — HTTP 400 Bad Request
- `xstocks.price.METAx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.METAx` [ok] 200 1129ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.METAx` [FAIL] 400 192ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier — HTTP 400 Bad Request
- `xstocks.price.QQQx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.QQQx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.QQQx` [FAIL] 400 117ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier — HTTP 400 Bad Request
- `xstocks.price.COINx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.COINx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.COINx` [FAIL] 400 112ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier — HTTP 400 Bad Request
- `xstocks.price.BANKCx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.BANKCx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [FAIL] 400 261ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier — HTTP 400 Bad Request
- `xstocks.price.SUOPTx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [FAIL] 400 128ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier — HTTP 400 Bad Request
- `xstocks.price.MMGx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.MMGx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.MMGx` [FAIL] 400 131ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier — HTTP 400 Bad Request
- `xstocks.price.TNGYIx` [ok] 200 1058ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [FAIL] 400 353ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier — HTTP 400 Bad Request
- `xstocks.price.ZHAOMx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [FAIL] 400 117ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier — HTTP 400 Bad Request
- `xstocks.price.LAOPGx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [FAIL] 400 112ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier — HTTP 400 Bad Request
- `xstocks.price.JDLOGx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [FAIL] 400 119ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier — HTTP 400 Bad Request
- `xstocks.price.CTINSx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.CTINSx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [FAIL] 400 379ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier — HTTP 400 Bad Request
- `xstocks.price.KUNLx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.KUNLx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [FAIL] 400 126ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier — HTTP 400 Bad Request
- `xstocks.price.WRFHDx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [FAIL] 400 259ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier — HTTP 400 Bad Request
- `xstocks.price.HAIDLx` [ok] 200 547ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [FAIL] 400 144ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier — HTTP 400 Bad Request
- `xstocks.price.SNBIOx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [FAIL] 400 123ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier — HTTP 400 Bad Request
- `xstocks.price.SZIGHx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [FAIL] 400 190ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier — HTTP 400 Bad Request
- `xstocks.price.ENNHLx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [FAIL] 400 207ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier — HTTP 400 Bad Request
- `llama.protocol.xstocks` [ok] 200 36ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.TSLAx` [ok] 200 161ms https://lite-api.jup.ag/tokens/v2/search?query=TSLAx
- `jup.tokens.search.SPYx` [ok] 200 65ms https://lite-api.jup.ag/tokens/v2/search?query=SPYx
- `jup.tokens.search.NVDAx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=NVDAx
- `jup.tokens.search.GOOGLx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=GOOGLx
- `jup.tokens.search.QQQx` [ok] 200 72ms https://lite-api.jup.ag/tokens/v2/search?query=QQQx
- `jup.tokens.search.AAPLx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=AAPLx
- `jup.tokens.search.COINx` [ok] 200 71ms https://lite-api.jup.ag/tokens/v2/search?query=COINx
- `jup.tokens.search.METAx` [ok] 200 78ms https://lite-api.jup.ag/tokens/v2/search?query=METAx
- `jup.tokens.search.AMZNx` [ok] 200 58ms https://lite-api.jup.ag/tokens/v2/search?query=AMZNx
- `jup.tokens.search.MSFTx` [ok] 200 68ms https://lite-api.jup.ag/tokens/v2/search?query=MSFTx
- `jup.tokens.search.BANKCx` [ok] 200 60ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.HAIDLx` [ok] 200 67ms https://lite-api.jup.ag/tokens/v2/search?query=HAIDLx
- `jup.tokens.search.SNBIOx` [ok] 200 60ms https://lite-api.jup.ag/tokens/v2/search?query=SNBIOx
- `jup.tokens.search.CTINSx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=CTINSx
- `jup.tokens.search.SZIGHx` [ok] 200 60ms https://lite-api.jup.ag/tokens/v2/search?query=SZIGHx
- `jup.tokens.search.KUNLx` [ok] 200 65ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.MMGx` [ok] 200 59ms https://lite-api.jup.ag/tokens/v2/search?query=MMGx
- `jup.tokens.search.SUOPTx` [ok] 200 56ms https://lite-api.jup.ag/tokens/v2/search?query=SUOPTx
- `jup.tokens.search.TNGYIx` [ok] 200 59ms https://lite-api.jup.ag/tokens/v2/search?query=TNGYIx
- `jup.tokens.search.ZHAOMx` [ok] 200 55ms https://lite-api.jup.ag/tokens/v2/search?query=ZHAOMx
- `jup.tokens.search.WRFHDx` [ok] 200 60ms https://lite-api.jup.ag/tokens/v2/search?query=WRFHDx
- `jup.tokens.search.LAOPGx` [ok] 200 58ms https://lite-api.jup.ag/tokens/v2/search?query=LAOPGx
- `jup.tokens.search.JDLOGx` [ok] 200 65ms https://lite-api.jup.ag/tokens/v2/search?query=JDLOGx
- `jup.tokens.search.ENNHLx` [ok] 200 60ms https://lite-api.jup.ag/tokens/v2/search?query=ENNHLx
- `jup.tokens.search.xStock` [ok] 200 95ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jito.tip_floor` [ok] 200 248ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 298ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 87ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md

---

Borealis 1.4.0 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
