# Borealis — Solana ecosystem report

**Generated** 2026-08-26T00:14:29Z · 2026-08-25 17:14:29 PT
**Author** dustycompiler · **Version** 1.3.0 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-26T00:14:17Z · **RPC health** `ok`
**Health score** 100 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 400)/400, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Verdict** WATCH — SOL 24h -5.44%; DEX 7d +103%; slot 365 ms
Updates every 15 min via GitHub Action.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +103.13%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +14.51%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +28.41%. (threshold: `|7d %| >= 20`)
- **WARN · Last TPS sample outside 2.5σ of the 60-sample window** — Last sample 4,974 TPS is +3.22σ vs window mean 4,148 (n=60, σ=257). (threshold: `|last sample − window mean| > 2.5σ`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 96.21 USD is +27.5% vs 30d median 75.45 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 441,746,184 |
| Block height | 419,794,750 |
| Block time | 2026-08-26T00:14:17Z |
| Epoch | 1,022 (56.06% · slot 242,185/432,000) |
| Mean TPS (last ~3,600s) | 4,148.3 |
| Mean non-vote TPS | 2,284.0 |
| Median TPS (same window) | 4,092.3 |
| Mean slot time | 365.3 ms |
| Median slot time | 365.9 ms |
| Transaction count (cluster) | 541,866,131,470 |
| Circulating supply | 583,375,566 SOL |
| Total supply | 632,859,426 SOL |
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

- `2bpfa8Jb…` · 29.73K SOL · commission 5% · lag 1106185 slots
- `5P35CJVK…` · 24.00K SOL · commission 100% · lag 1106185 slots
- `gangtCrQ…` · 16.66K SOL · commission 0% · lag 493505 slots
- `kom1oNHy…` · 2.19K SOL · commission 5% · lag 1109668 slots
- `4GEEKSwu…` · 1.35K SOL · commission 5% · lag 733818 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 441746184 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 25513 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 1106185 slots

## Trends

15-min Borealis tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 8 | data/history.jsonl 15-min tape |
| TVL chart | 8 | data/history.jsonl 15-min tape |
| SOL chart | 30 | solana.com/data SOL Price (DexPaprika) |
| history.jsonl rows | 8 | data/history.jsonl |

## Economics (honest stack — not REV)

| Metric | Value | Source |
| --- | ---: | --- |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | getBlock meta.fee n=31176 slots (441746169, 441746184) |
| p90 / p99 | 0.000014 / 0.000410 SOL | same sample |
| Priority p50 (est.) | 0.000000 SOL | priority est. = meta.fee − 5000×n_signatures (base fee 5000 lamports/sig). Sampled, not a 24h ledger sum. |
| Network fees 24h | 9,162.1 SOL ($881.48K) | solana.com/data Fees (Allium) |
| Protocol fees 24h | $14.49M | DeFiLlama Solana protocol fees 24h (not REV) |
| Jito/MEV tip floor | 0.000010 SOL p50 landed | https://bundles.jito.wtf/api/v1/bundles/tip_floor |
| REV total | — | No REV total: components are not summed (protocol fees are not network REV; sampled fees are not a 24h ledger). |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $96.21 | coinbase.exchange.SOL-USD.stats |
| 24h change | -5.44% | coinbase.exchange.SOL-USD.stats |
| Market cap | $56.13B | derived: price × RPC circulating supply (not CoinGecko mcap) |
| 24h volume | $173.64M | coinbase.exchange.SOL-USD.stats quote = last × base volume |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.60B |
| TVL 1d / 7d / 30d | +0.73% / +15.51% / +15.69% |
| DEX volume 24h | $3.00B |
| DEX volume 7d | $20.88B |
| DEX 1d change | +1.96% |
| Protocol fees 24h (DeFiLlama, not REV) | $14.49M |
| Fees 1d / 7d | +14.51% / +28.41% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $694.81M | -2.51% |
| Orca DEX | $469.41M | +17.08% |
| BisonFi | $409.15M | -6.69% |
| Meteora DLMM | $278.05M | +3.35% |
| Scorch | $218.92M | -19.10% |
| Manifest Trade | $197.29M | +39.31% |
| Raydium AMM | $193.12M | -6.73% |
| pump.fun | $95.40M | +24.76% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.48B | +0.97% | +28.73% |
| Kamino Lend | Lending | $1.18B | -1.18% | +10.77% |
| Jupiter Lend | Lending | $1.06B | -1.15% | +10.91% |
| Raydium AMM | Dexs | $1.06B | +0.59% | +23.71% |
| Binance Staked SOL | Liquid Staking | $999.33M | +2.00% | +27.81% |
| Jito Liquid Staking | Liquid Staking | $978.08M | +1.10% | +27.06% |
| BlackRock BUIDL | RWA | $876.38M | +4.14% | +1.16% |
| Jupiter Perpetual Exchange | Derivatives | $751.62M | -0.56% | +9.42% |
| Jupiter Staked SOL | Liquid Staking | $505.01M | +0.27% | +26.65% |
| xStocks | RWA | $430.54M | +2.18% | +12.61% |

## Stablecoins

Solana circulating pegged-USD: **$15.88B**
(1d -0.22% · 7d +2.77%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.10B | -2.47% |
| USDT · Tether | $2.83B | -0.00% |
| USDGO · USDGO | $1.24B | +3.77% |
| USD1 · World Liberty Financial USD | $1.11B | +4.03% |
| BUIDL · BlackRock USD | $876.38M | +12.77% |
| PYUSD · PayPal USD | $678.74M | -1.36% |
| USDG · Global Dollar | $629.31M | +3.57% |
| USDe · Ethena USDe | $537.01M | +0.11% |

## Tokenized equities (xStocks)

Sum of quote * circulating * multiplier over 24 priced Solana-deployed xStocks. Not a census of every tokenized equity on Solana.
Listed 715 · Solana deployments 715 · priced mcap $277.02M.
Formula: `quote * circulating * multiplier`. 715 of 715 listed xStocks have a Solana deployment (count share, not market-cap share)

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.06B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $876.38M
- **xStocks** (RWA) — $430.54M
- **OnRe** (RWA) — $277.20M
- **Ondo Yield Assets** (RWA) — $178.56M
- **Hastra** (RWA) — $163.57M
- **Theo Network thBill** (RWA) — $26.39M
- **Ondo Global Markets** (RWA) — $24.90M
- **Nest Credit** (RWA) — $22.70M

## Daily active addresses

749,721 (Allium, as of 2026-08-24). Provider range 361,127–854,284. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

## Public Dune embed

public Dune embed, not our query — Solana On-Chain Health & Activity Explorer (cryptoonchain)
Embed: https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
Dashboard: https://dune.com/cryptoonchain/solana-explorer
HTTP 200 · included: yes

## Status & news

**status.solana.com:** All Systems Operational (indicator `none`)

### X / announcements (public Nitter-style RSS, not Twitter API)

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
- [RT by @solana: Solana is becoming a global venue for new markets

Building durable liquidity for those markets requires professional market makers and the infrastructure to bring their strategies onchain

Polaris provides that path](https://x.com/polarislabxyz/status/2092279320840728861) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 15:53:57 GMT
- [RT by @anza_xyz: 300ms now pending on Solana mainnet 👀
effective start of epoch 1024 (~3 days)](https://x.com/bw_solana/status/2092259551659831608) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 25 Aug 2026 14:35:24 GMT `mainnet`
- [We're aware of today's arrayref crate supply-chain attack: https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/

Agave and Anza's software are not affected.

If you ran cargo update today, check your machine against indicators in the writeup. Stay safe out there.](https://x.com/anza_xyz/status/2090608013891813501) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 21 Aug 2026 01:12:46 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

### Foundation / Anza RSS

- [mb-020624](https://status.solana.com/incidents/n5kcgs8dl9pj) — status.solana.com · 2024-02-06T15:09:24Z `upgrade` `outage` `mainnet`
- [Cluster Instability](https://status.solana.com/incidents/ymr0gyj9xqyz) — status.solana.com · 2023-02-26T02:09:04Z `incident`
- [Public Endpoints and Explorer offline](https://status.solana.com/incidents/mf9plxrkjhnk) — status.solana.com · 2023-01-08T07:01:17Z `upgrade` `mainnet`
- [Degraded Performance](https://status.solana.com/incidents/kxsv0xcz9dn3) — status.solana.com · 2022-10-01T07:06:06Z `outage` `mainnet`
- [Mainnet Beta Clock Drift](https://status.solana.com/incidents/f68wm876ph9m) — status.solana.com · 2022-06-06T16:32:07Z `incident` `mainnet`
- [Mainnet Beta Outage](https://status.solana.com/incidents/m6qzbgc7np9b) — status.solana.com · 2022-06-01T21:06:03Z `outage` `mainnet`
- [Several RPC nodes down](https://status.solana.com/incidents/6qvg6z1k43zb) — status.solana.com · 2022-03-28T12:09:49Z
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) — solana.com/news · Mon, 24 Aug 2026 14:19:00 GMT `mainnet`
- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) — solana.com/news · Wed, 19 Aug 2026 10:00:00 GMT
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) — solana.com/news · Mon, 17 Aug 2026 00:00:00 GMT

## Editorial — Alpenglow (SIMD-0326) — not SIMD-025

_As of 2026-08-26 (2026-08-25 17:14:29 PT). Editorial. Dates and activation targets move. None of this is a live cluster metric; it is a dated reading of public Foundation / SIMD / Anza notes._

Public SIMD numbering: Alpenglow consensus is SIMD-0326. SIMD-0256 was a 2025 compute-unit block-limit increase (50M to 60M) and is not the consensus rewrite. This section uses the current names.

Alpenglow is Solana's next consensus protocol. Phase 1 (Votor) replaces TowerBFT voting with direct votes and certificates. Target finality is roughly 150ms versus ~12.8s TowerBFT. Rotor (Turbine replacement) is a later phase. Proof of History remains the ordering clock in current write-ups of the Agave 4.3 activation path.

- **SIMD-0326** — Alpenglow Consensus Protocol (Votor)
- **SIMD-0337** — Markers for Alpenglow Fast Leader Handover
- **SIMD-0357** — Alpenglow Validator Admission Ticket (VAT)
- **SIMD-0384** — Alpenglow Migration
- **SIMD-0387** — BLS Pubkey Management in Vote Account

### Public timeline (editorial)

- `2026-07-08` — SIMD-0387 (BLS pubkey in vote account) activated on mainnet.
- `2026-07-22` — SIMD-0357 VAT activated. Validators without an on-chain BLS pubkey are excluded from the VAT-admitted set. VAT does not itself turn on Alpenglow consensus.
- `2026-Q3` — Expected mainnet activation window for Votor via Agave 4.3. Anza's published 4.3 schedule (12 Aug 2026) targeted feature activation around 28 Sep 2026; that schedule is tentative.

### What to watch

- Agave 4.3 stake rollout percentages vs. the published schedule.
- Firedancer / Frankendancer Votor parity before a full Alpenswitch.
- Community cluster slot-time and fast-path finalization readings.
- Whether Rotor remains deferred after Votor activation.

- https://solana.com/upgrades/alpenglow
- https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0326-alpenglow.md
- https://forum.solana.com/t/simd-0326-proposal-for-the-new-alpenglow-consensus-protocol/4236

## Omissions

- **SOL/USD (CoinGecko live)** — CoinGecko HTTP 429 Too Many Requests. Showing coinbase.exchange.SOL-USD.stats instead.
- **xStocks** — priced 24 of 715 Solana-deployed symbols to cap RPC/HTTP

## Sources this run

- `rpc.getHealth` [ok] 200 448ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 316ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 253ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 243ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 268ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7040ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 441ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [FAIL] 429 34ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true — HTTP 429 Too Many Requests
- `coinbase.solusd.stats` [ok] 200 38ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 52ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 46ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 47ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 68ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 129ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 57ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 76ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 101ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 449ms https://solana.com/data
- `solana.com.databricks` [ok] 200 142ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 137ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 275ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 725ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 136ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 352ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 1317ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 620ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 631ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 604ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 192ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 176ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 177ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 181ms https://nitter.perennialte.ch/solana_devs/rss
- `rpc.getBalance` [ok] 200 247ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 243ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1130ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1051ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1104ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1312ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1394ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1314ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 822ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 923ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 869ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1140ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 913ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2097ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1222ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1051ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 899ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 731ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 6559ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 6040ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 6547ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 4677ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2904ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 4390ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1896ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 918ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [ok] 200 548ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.TSLAx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [FAIL] 400 187ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier — HTTP 400 Bad Request
- `xstocks.price.SPYx` [ok] 200 1211ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.SPYx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.SPYx` [FAIL] 400 353ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier — HTTP 400 Bad Request
- `xstocks.price.NVDAx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.NVDAx` [ok] 200 926ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [FAIL] 400 220ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier — HTTP 400 Bad Request
- `xstocks.price.AAPLx` [ok] 200 698ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.AAPLx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [FAIL] 400 180ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier — HTTP 400 Bad Request
- `xstocks.price.MSFTx` [ok] 200 1566ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.MSFTx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [FAIL] 400 227ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier — HTTP 400 Bad Request
- `xstocks.price.GOOGLx` [ok] 200 525ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 566ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [FAIL] 400 192ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier — HTTP 400 Bad Request
- `xstocks.price.AMZNx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.AMZNx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [FAIL] 400 189ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier — HTTP 400 Bad Request
- `xstocks.price.METAx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.METAx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.METAx` [FAIL] 400 308ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier — HTTP 400 Bad Request
- `xstocks.price.QQQx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.QQQx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.QQQx` [FAIL] 400 188ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier — HTTP 400 Bad Request
- `xstocks.price.COINx` [ok] 200 912ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.COINx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.COINx` [FAIL] 400 190ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier — HTTP 400 Bad Request
- `xstocks.price.BANKCx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.BANKCx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [FAIL] 400 265ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier — HTTP 400 Bad Request
- `xstocks.price.SUOPTx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [FAIL] 400 194ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier — HTTP 400 Bad Request
- `xstocks.price.MMGx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.MMGx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.MMGx` [FAIL] 400 424ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier — HTTP 400 Bad Request
- `xstocks.price.TNGYIx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [FAIL] 400 191ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier — HTTP 400 Bad Request
- `xstocks.price.ZHAOMx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [FAIL] 400 185ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier — HTTP 400 Bad Request
- `xstocks.price.LAOPGx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [FAIL] 400 189ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier — HTTP 400 Bad Request
- `xstocks.price.JDLOGx` [ok] 200 946ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [FAIL] 400 244ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier — HTTP 400 Bad Request
- `xstocks.price.CTINSx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.CTINSx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [FAIL] 400 195ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier — HTTP 400 Bad Request
- `xstocks.price.KUNLx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.KUNLx` [ok] 200 648ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [FAIL] 400 449ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier — HTTP 400 Bad Request
- `xstocks.price.WRFHDx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [FAIL] 400 351ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier — HTTP 400 Bad Request
- `xstocks.price.HAIDLx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [FAIL] 400 619ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier — HTTP 400 Bad Request
- `xstocks.price.SNBIOx` [ok] 200 1025ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [FAIL] 400 188ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier — HTTP 400 Bad Request
- `xstocks.price.SZIGHx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 1011ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [FAIL] 400 439ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier — HTTP 400 Bad Request
- `xstocks.price.ENNHLx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [FAIL] 400 206ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier — HTTP 400 Bad Request
- `jito.tip_floor` [ok] 200 177ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 335ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer

---

Borealis 1.3.0 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
