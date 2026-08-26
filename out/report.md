# Borealis — Solana ecosystem report

**Generated** 2026-08-26T01:18:34Z · 2026-08-25 18:18:34 PT
**Author** dustycompiler · **Version** 1.4.1 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-26T01:18:19Z · **RPC health** `ok`
**Health score** 82 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 400)/400, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** WATCH · **Ecosystem** SURGE — SOL 24h -4.80%; DEX 7d +60%; slot 366 ms
Updates every 15 min via GitHub Action.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +60.43%. (threshold: `|7d %| >= 20`)
- **WARN · High validator delinquency** — 9 delinquent vote accounts, 1.424% of activated+delinquent stake. (threshold: `delinquent stake >= 1% or delinquent count >= 25`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +60.42%. (threshold: `|7d %| >= 20`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 96.94 USD is +28.5% vs 30d median 75.45 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · TPS vs 30d median (solana.com/data tx/86400)** — Current 4,248.80 TPS is +20.3% vs 30d median 3,531.29 TPS (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 441,756,682 |
| Block height | 419,805,244 |
| Block time | 2026-08-26T01:18:19Z |
| Epoch | 1,022 (58.49% · slot 252,683/432,000) |
| Mean TPS (last ~3,600s) | 4,248.8 |
| Mean non-vote TPS | 2,383.4 |
| Median TPS (same window) | 4,195.4 |
| Mean slot time | 366.0 ms |
| Median slot time | 365.9 ms |
| Transaction count (cluster) | 541,882,451,339 |
| Circulating supply | 583,375,522 SOL |
| Total supply | 632,859,383 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 686 |
| Delinquent | 9 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 428,921,546 SOL |
| Delinquent stake | 6,196,558.27 SOL (1.424%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 79 |
| Top 10 / 20 stake share | 24.63% / 35.63% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.07M SOL | 3.98% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.04M SOL | 3.74% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.27M SOL | 2.86% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.74M SOL | 2.74% | 5% | 0 |
| 5 | `C8Bey3LK…` | 9.20M SOL | 2.15% | 7% | 0 |
| 6 | `CAo1dCGY…` | 8.92M SOL | 2.08% | 10% | 0 |
| 7 | `E1r4Psq8…` | 8.58M SOL | 2.00% | 0% | 0 |
| 8 | `EvnRmnMr…` | 7.95M SOL | 1.85% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.30M SOL | 1.70% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.57M SOL | 1.53% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.02M SOL | 1.40% | 0% | 0 |
| 12 | `5pPRHnie…` | 5.93M SOL | 1.38% | 5% | 0 |
| 13 | `5Cchr1XG…` | 5.67M SOL | 1.32% | 100% | 0 |
| 14 | `GnC339vk…` | 4.83M SOL | 1.13% | 7% | 0 |
| 15 | `9rkJMARq…` | 4.67M SOL | 1.09% | 8% | 0 |

### Delinquency alerts

- `9jxgosAf…` · 6.12M SOL · commission 100% · lag 756 slots
- `2bpfa8Jb…` · 29.73K SOL · commission 5% · lag 1116683 slots
- `5P35CJVK…` · 24.00K SOL · commission 100% · lag 1116683 slots
- `gangtCrQ…` · 16.66K SOL · commission 0% · lag 504003 slots
- `kom1oNHy…` · 2.19K SOL · commission 5% · lag 1120166 slots
- `4GEEKSwu…` · 1.35K SOL · commission 5% · lag 744316 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 441756682 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 36011 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 1116683 slots

## Trends

15-min Borealis tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 15 | data/history.jsonl 15-min tape |
| TVL chart | 15 | data/history.jsonl 15-min tape |
| SOL chart | 14 | data/history.jsonl 15-min tape |
| history.jsonl rows | 15 | data/history.jsonl |

## Economics — Borealis REV (not DeFiLlama protocol fees)

Borealis REV follows Blockworks/Helius: in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito tips. DeFiLlama Solana protocol/application fees are NOT REV and are not summed.

| Metric | Value | Source |
| --- | ---: | --- |
| **Borealis REV 24h** | **$1.16M** (11,967.5 SOL) | MEASURED in-protocol + ESTIMATED Jito tips |
| In-protocol network fees 24h | 9,162.1 SOL ($888.17K) | solana.com/data Fees (Allium) MEASURED |
| Jito tips 24h | $271.96K | ESTIMATED · sensitivity (not a Jito ledger): tips at p50 floor → 271960 USD; at p95 floor → 3389145 USD. Headline REV uses p50. |
| Protocol fees 24h | $14.08M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9961 |
| p90 / p99 | 0.000018 / 0.000410 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $96.94 | coingecko.simple_price |
| 24h change | -4.80% | coingecko.simple_price |
| Market cap | $56.53B | coingecko.simple_price |
| 24h volume | $5.07B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.58B |
| TVL 1d / 7d / 30d | +0.73% / +15.51% / +15.69% |
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

Solana circulating pegged-USD: **$15.87B**
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

Priced-subset lower bound: quote × circulating × multiplier(assumed 1.0) over 80 of 715 Solana-deployed listed symbols (715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. public /multiplier is not fetched (historically HTTP 400). mcap uses multiplier=1.0 on circulating-supply as returned.
Listed 715 · Solana deployments 715 · priced 80 · priced-subset mcap $276.69M (lower bound, not a census).
24h volume $23.58M · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $430.26M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with multiplier assumed 1.0 (public /multiplier is not fetched (historically HTTP 400). mcap uses multiplier=1.0 on circulating-supply as returned.). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

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

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-26 (2026-08-25 18:18:34 PT). Editorial. Listing token SIMD-525 cites solana.com/news “Lowering Slot Time and Validators Economic”. Observed slot time is INFERRED corroboration, not a feature-gate RPC. Activation dates move. None of this is a live consensus metric._

Primary source for the listing token SIMD-525: solana.com/news “Lowering Slot Time and Validators Economic” (SIMD-0525 staged 400→350→300→250→200 ms). Observed mean slot ~366 ms is corroboration, labeled inferred — not a feature-gate RPC. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

_Listing token SIMD-525 is SIMD-0525. Not SIMD-025._

- **SIMD-525** — Reduce Slot Times (400→350→300→250→200 ms)
- **SIMD-0326** — Alpenglow Consensus Protocol (Votor)
- **SIMD-0337** — Markers for Alpenglow Fast Leader Handover
- **SIMD-0357** — Alpenglow Validator Admission Ticket (VAT)
- **SIMD-0384** — Alpenglow Migration
- **SIMD-0387** — BLS Pubkey Management in Vote Account

### Public timeline (editorial)

- `source` — solana.com/news “Lowering Slot Time and Validators Economic” is the primary public write-up for the SIMD-525 listing token (SIMD-0525).
- `2026-05-01` — SIMD-0525 created (Anza). Four feature gates: 350/300/250/200 ms.
- `2026-Q3` — Agave v4.2 schedule targeted the four SIMD-0525 steps on mainnet one epoch apart; schedule is tentative. First step is 400→350 ms.
- `observed` — Observed mean slot 366 ms is consistent with the 350 ms SIMD-0525 target (staged 400→350→300→250→200). INFERRED corroboration, not a feature-gate RPC.
- `2026-07-08` — SIMD-0387 (BLS pubkey in vote account) activated on mainnet.
- `2026-07-22` — SIMD-0357 VAT activated. VAT does not itself turn on Alpenglow consensus.

### What to watch

- Whether observed slot time stays near the inferred SIMD-0525 target after the next epoch.
- Skip rate / skipped slots as later 50 ms steps (300/250/200) are considered.
- Agave 4.2 / 4.3 stake rollout vs the published (tentative) schedule.
- Firedancer / Frankendancer Votor parity before a full Alpenswitch.

- https://solana.com/news/lowering-slot-time-and-validators-economic
- https://solana.com/upgrades/reduced-slot-times
- https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0525-reduce-slot-times.md
- https://solana.com/upgrades/alpenglow
- https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0326-alpenglow.md

## Omissions

- **xStocks** — priced up to 80 of 715 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 284ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 243ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 256ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 254ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 177ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6118ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 370ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 66ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 47ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 36ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 32ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 33ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 37ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 84ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 131ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 63ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 117ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 222ms https://solana.com/data
- `solana.com.databricks` [ok] 200 71ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 402ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 200ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 120ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 676ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 91ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 513ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 78ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 78ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 72ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 366ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 928ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 915ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 248ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 155ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 231ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 157ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 939ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 966ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1063ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 717ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1089ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 983ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1069ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1010ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1150ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1232ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1111ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1093ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 987ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 869ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1485ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1069ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1105ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1208ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2499ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2580ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1510ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.GOOGLx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.MSFTx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.AMZNx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.SPYx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.MSFTx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.NVDAx` [ok] 200 456ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.AAPLx` [ok] 200 570ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.TSLAx` [ok] 200 679ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.AAPLx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.MMGx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 439ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.price.METAx` [ok] 200 925ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.COINx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.BANKCx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.METAx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.QQQx` [ok] 200 732ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.KUNLx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.WRFHDx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.CTINSx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.SNBIOx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.CRESBx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.ENNHLx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.SZIGHx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.CRESBx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.CRESMx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.CMERPx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.WXXDCx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 532ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 707ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.SITCx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.CRESMx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 1580ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.CRESPx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.CRESPx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.SNDSCx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.ASMPTx` [ok] 200 834ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.CTFJWx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 1109ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.price.JDHLTx` [ok] 200 913ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.CTPCAx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.PWAHLx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.WHGROx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 111ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.CLONPx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.GENTEx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.GENTEx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.SWPRPx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.HKCGAx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.CKAHx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.price.COVELx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.COVELx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.GEELx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.CHONGx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.CHONGx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 729ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.MEITx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.HNDLDx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.price.SINOTx` [ok] 200 2649ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.KUAIx` [ok] 200 1173ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.NONGx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.circ.HNDLDx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.price.MTRCPx` [ok] 200 662ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.MEITx` [ok] 200 637ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.CKHUTx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.price.POPMTx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.price.CPETCx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.circ.CPETCx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.circ.POPMTx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 651ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.CITICx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.price.ANTASx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.price.BOCHKx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.circ.CITICx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 1333ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.ANTASx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 1480ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.HAIERx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.circ.PICCx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.HAIERx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.price.ZJGLDx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.circ.COSCx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.price.PSBOCx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.price.CRESLx` [ok] 200 563ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.circ.BOCHKx` [ok] 200 662ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.price.ICBCx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.circ.ZJGLDx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.circ.ICBCx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.circ.PSBOCx` [ok] 200 561ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.circ.CRESLx` [ok] 200 638ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.price.MIXUx` [ok] 200 6498ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.BOCOMx` [ok] 200 2880ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.price.SINOx` [ok] 200 5319ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.BOCOMx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `llama.protocol.xstocks` [ok] 200 39ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.TSLAx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=TSLAx
- `jup.tokens.search.SPYx` [ok] 200 48ms https://lite-api.jup.ag/tokens/v2/search?query=SPYx
- `jup.tokens.search.NVDAx` [ok] 200 47ms https://lite-api.jup.ag/tokens/v2/search?query=NVDAx
- `jup.tokens.search.GOOGLx` [ok] 200 54ms https://lite-api.jup.ag/tokens/v2/search?query=GOOGLx
- `jup.tokens.search.QQQx` [ok] 200 94ms https://lite-api.jup.ag/tokens/v2/search?query=QQQx
- `jup.tokens.search.AAPLx` [ok] 200 45ms https://lite-api.jup.ag/tokens/v2/search?query=AAPLx
- `jup.tokens.search.COINx` [ok] 200 49ms https://lite-api.jup.ag/tokens/v2/search?query=COINx
- `jup.tokens.search.METAx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=METAx
- `jup.tokens.search.AMZNx` [ok] 200 45ms https://lite-api.jup.ag/tokens/v2/search?query=AMZNx
- `jup.tokens.search.MSFTx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=MSFTx
- `jup.tokens.search.POPMTx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 71ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.HKEXCx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 60ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.CLONPx` [ok] 200 41ms https://lite-api.jup.ag/tokens/v2/search?query=CLONPx
- `jup.tokens.search.HAIDLx` [ok] 200 49ms https://lite-api.jup.ag/tokens/v2/search?query=HAIDLx
- `jup.tokens.search.SNBIOx` [ok] 200 55ms https://lite-api.jup.ag/tokens/v2/search?query=SNBIOx
- `jup.tokens.search.BANKCx` [ok] 200 44ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.NONGx` [ok] 200 43ms https://lite-api.jup.ag/tokens/v2/search?query=NONGx
- `jup.tokens.search.SINOx` [ok] 200 54ms https://lite-api.jup.ag/tokens/v2/search?query=SINOx
- `jup.tokens.search.MMGx` [ok] 200 41ms https://lite-api.jup.ag/tokens/v2/search?query=MMGx
- `jup.tokens.search.HKCGAx` [ok] 200 45ms https://lite-api.jup.ag/tokens/v2/search?query=HKCGAx
- `jup.tokens.search.CTPCAx` [ok] 200 55ms https://lite-api.jup.ag/tokens/v2/search?query=CTPCAx
- `jup.tokens.search.xStock` [ok] 200 72ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jito.tip_floor` [ok] 200 434ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 204ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 124ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md

---

Borealis 1.4.1 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
