# Borealis — Solana ecosystem report

**Generated** 2026-08-26T02:13:17Z · 2026-08-25 19:13:17 PT
**Author** dustycompiler · **Version** 1.5.0 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-26T02:13:05Z · **RPC health** `ok`
**Health score** 100 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 400)/400, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -3.56%; DEX 24h $2.95B · 1d -2% · vs-7d-ago +60%; slot 365 ms
Updates every 15 min via GitHub Action.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +50.10%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -9.12%. (threshold: `|1d %| >= 8`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -3.56%, DeFiLlama TVL 1d -0.76%, DEX 1d -1.58%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +60.42%. (threshold: `|7d %| >= 20`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 96.87 USD is +28.4% vs 30d median 75.45 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 441,765,676 |
| Block height | 419,814,213 |
| Block time | 2026-08-26T02:13:05Z |
| Epoch | 1,022 (60.57% · slot 261,676/432,000) |
| Mean TPS (last ~3,600s) | 3,951.1 |
| Mean non-vote TPS | 2,086.4 |
| Median TPS (same window) | 3,916.5 |
| Mean slot time | 365.5 ms |
| Median slot time | 365.9 ms |
| Transaction count (cluster) | 541,895,318,730 |
| Circulating supply | 583,375,488 SOL |
| Total supply | 632,859,349 SOL |
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
| Activated stake | 435,018,049 SOL |
| Delinquent stake | 100,054.30 SOL (0.023%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 79 |
| Top 10 / 20 stake share | 24.29% / 35.63% |
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

- `2bpfa8Jb…` · 29.73K SOL · commission 5% · lag 1125677 slots
- `mrgn4atx…` · 26.11K SOL · commission 0% · lag 447 slots
- `5P35CJVK…` · 24.00K SOL · commission 100% · lag 1125677 slots
- `gangtCrQ…` · 16.66K SOL · commission 0% · lag 512997 slots
- `kom1oNHy…` · 2.19K SOL · commission 5% · lag 1129160 slots
- `4GEEKSwu…` · 1.35K SOL · commission 5% · lag 753310 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 441765676 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 45005 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 1125677 slots

## Trends

15-min Borealis tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 17 | data/history.jsonl 15-min tape |
| TVL chart | 17 | data/history.jsonl 15-min tape |
| SOL chart | 16 | data/history.jsonl 15-min tape |
| history.jsonl rows | 17 | data/history.jsonl |

## Economics — in-protocol fees (full REV incomplete)

Borealis REV follows Blockworks/Helius: in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito tips. This run cannot publish a REV number: there is no 24h Jito tip tape on zero-key sources. tip_floor p50 × non-vote TPS × 86400 is kept as an INVALID sensitivity (per-bundle landed percentile, not a tape). DeFiLlama Solana protocol/application fees are NOT REV and are not summed.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$887.53K** (9,162.1 SOL) | solana.com/data Fees (Allium) MEASURED |
| **Full REV** | incomplete | INCOMPLETE — no 24h Jito tip tape on zero-key sources — Jito 24h aggregate unavailable; tip-floor is a bundle percentile, not a tape |
| Jito tip-floor run-rate (NOT REV) | $36.90K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 36898 USD; at p95 floor → 4727245 USD. |
| Protocol fees 24h | $13.17M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9973 |
| p90 / p99 | 0.000015 / 0.000701 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $96.87 | coingecko.simple_price |
| 24h change | -3.56% | coingecko.simple_price |
| Market cap | $56.47B | coingecko.simple_price |
| 24h volume | $4.81B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.58B |
| TVL 1d / 7d / 30d | -0.76% / +13.97% / +13.40% |
| DEX volume 24h | $2.95B · 1d -1.58% · vs-7d-ago +60.42% |
| 7d DEX volume | $21.60B · +100.14% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $13.17M |
| Fees 1d / 7d | -9.12% / +50.10% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $567.89M | -18.27% |
| Orca DEX | $424.69M | -2.52% |
| BisonFi | $411.40M | +0.55% |
| Meteora DLMM | $246.36M | -11.40% |
| Scorch | $218.92M | 0.00% |
| Raydium AMM | $189.57M | +3.25% |
| Manifest Trade | $172.20M | -1.83% |
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
| xStocks | RWA | $428.14M | +1.58% | +12.25% |

## Stablecoins

Solana circulating pegged-USD: **$15.87B**
(1d -0.21% · 7d +2.78%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.04B | -3.26% |
| USDT · Tether | $2.84B | -0.00% |
| USDGO · USDGO | $1.24B | +3.77% |
| USD1 · World Liberty Financial USD | $1.11B | +4.03% |
| BUIDL · BlackRock USD | $876.38M | +12.77% |
| PYUSD · PayPal USD | $678.94M | -1.34% |
| USDG · Global Dollar | $629.28M | +3.57% |
| USDe · Ethena USDe | $537.10M | +0.11% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 80 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 80 · priced-subset mcap $277.51M (lower bound, not a census).
24h volume $23.50M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $428.14M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 80 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.06B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $876.38M
- **xStocks** (RWA) — $428.14M
- **OnRe** (RWA) — $277.29M
- **Ondo Yield Assets** (RWA) — $178.30M
- **Hastra** (RWA) — $163.76M
- **Theo Network thBill** (RWA) — $26.39M
- **Ondo Global Markets** (RWA) — $24.81M
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

_As of 2026-08-26 (2026-08-25 19:13:17 PT). Editorial. Listing token SIMD-525 cites solana.com/news “Lowering Slot Time and Validators Economic”. Observed slot time is INFERRED corroboration, not a feature-gate RPC. Activation dates move. None of this is a live consensus metric._

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
- `observed` — Observed mean slot 365 ms is consistent with the 350 ms SIMD-0525 target (staged 400→350→300→250→200). INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 159ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 122ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 97ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 94ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 104ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7469ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 291ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 197ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 64ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 50ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 88ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 383ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 107ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 96ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 294ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 55ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 174ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 360ms https://solana.com/data
- `solana.com.databricks` [ok] 200 176ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 431ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 69ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 48ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 171ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 387ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 492ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 157ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 158ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 162ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 260ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 219ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 805ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 225ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 139ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 89ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 110ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 560ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 602ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 786ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 633ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 643ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 628ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 825ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 610ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 732ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 612ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 807ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 722ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 535ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 550ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 4649ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 6634ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 4177ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 5639ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 3871ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1247ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1310ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 809ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.SPYx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.MSFTx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.GOOGLx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.NVDAx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.AAPLx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.NVDAx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.TSLAx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.mult.NVDAx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.MSFTx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.TSLAx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.GOOGLx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 641ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.BANKCx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 1151ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.COINx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.TSLAx` [ok] 200 696ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.AMZNx` [ok] 200 1757ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.LAOPGx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.SUOPTx` [ok] 200 717ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.SPYx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 685ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.CTINSx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 577ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 1010ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.HAIDLx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.CTINSx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [ok] 200 621ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 571ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.price.ENNHLx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.JDLOGx` [ok] 200 920ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 872ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.SMOIHx` [ok] 200 475ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.CMERPx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.CSPCx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.circ.CRESBx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 802ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 542ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.BDWAPx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.CMENDx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 722ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.price.SNDSCx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.ASMPTx` [ok] 200 768ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.CRESMx` [ok] 200 802ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.MIXUx` [ok] 200 1088ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.CRESPx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 868ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.mult.MIXUx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 956ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 1048ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.PRADx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.CTFJWx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 1414ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 513ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.CTPCAx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.WHGROx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 792ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.CLONPx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.CLPHDx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.GENTEx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.SINOx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 1373ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.SITCx` [ok] 200 1280ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.CKAHx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.CKINFx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.GENTEx` [ok] 200 428ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 548ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.CLONPx` [ok] 200 749ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.SINOTx` [ok] 200 943ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 607ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 770ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.MTRCPx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.mult.NONGx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.COVELx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.HNDLDx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 702ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.COVELx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.PICCx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.CHONGx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.CHONGx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 487ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 879ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.COVELx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 570ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.BOCOMx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.price.BOCHKx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.price.CPETCx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.price.CITICx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.price.POPMTx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.price.ANTASx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.circ.CPETCx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.circ.CITICx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.BOCHKx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.circ.ANTASx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.CPETCx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.circ.BOCOMx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.price.CRESLx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.circ.CKHUTx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.CITICx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.mult.ANTASx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.circ.POPMTx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.mult.BOCOMx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.circ.CRESLx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.price.HAIERx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.mult.CKHUTx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.POPMTx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.price.PSBOCx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.price.ICBCx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.mult.CRESLx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.circ.HAIERx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.circ.ICBCx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.circ.PSBOCx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.mult.ICBCx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `xstocks.mult.BOCHKx` [ok] 200 701ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.mult.HAIERx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.mult.PSBOCx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `xstocks.price.ZJGLDx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.circ.ZJGLDx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.mult.ZJGLDx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 42ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.TSLAx` [ok] 200 124ms https://lite-api.jup.ag/tokens/v2/search?query=TSLAx
- `jup.tokens.search.SPYx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=SPYx
- `jup.tokens.search.NVDAx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=NVDAx
- `jup.tokens.search.GOOGLx` [ok] 200 66ms https://lite-api.jup.ag/tokens/v2/search?query=GOOGLx
- `jup.tokens.search.QQQx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=QQQx
- `jup.tokens.search.AAPLx` [ok] 200 69ms https://lite-api.jup.ag/tokens/v2/search?query=AAPLx
- `jup.tokens.search.COINx` [ok] 200 64ms https://lite-api.jup.ag/tokens/v2/search?query=COINx
- `jup.tokens.search.METAx` [ok] 200 72ms https://lite-api.jup.ag/tokens/v2/search?query=METAx
- `jup.tokens.search.AMZNx` [ok] 200 56ms https://lite-api.jup.ag/tokens/v2/search?query=AMZNx
- `jup.tokens.search.MSFTx` [ok] 200 69ms https://lite-api.jup.ag/tokens/v2/search?query=MSFTx
- `jup.tokens.search.POPMTx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.HKEXCx` [ok] 200 56ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MEITx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.MIXUx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUNLx` [ok] 200 72ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.SNBIOx` [ok] 200 60ms https://lite-api.jup.ag/tokens/v2/search?query=SNBIOx
- `jup.tokens.search.HAIDLx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=HAIDLx
- `jup.tokens.search.CHONGx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=CHONGx
- `jup.tokens.search.MMGx` [ok] 200 68ms https://lite-api.jup.ag/tokens/v2/search?query=MMGx
- `jup.tokens.search.CRESPx` [ok] 200 74ms https://lite-api.jup.ag/tokens/v2/search?query=CRESPx
- `jup.tokens.search.NONGx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=NONGx
- `jup.tokens.search.BANKCx` [ok] 200 59ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.CLONPx` [ok] 200 68ms https://lite-api.jup.ag/tokens/v2/search?query=CLONPx
- `jup.tokens.search.xStock` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jito.tip_floor` [ok] 200 95ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 306ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 77ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md

---

Borealis 1.5.0 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
