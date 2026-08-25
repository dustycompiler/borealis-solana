# Borealis — Solana ecosystem report

**Generated** 2026-08-25T22:33:29Z · 2026-08-25 15:33:29 PT
**Author** hardest-worker · **Version** 1.0.0 · **License** MIT
**Cluster block time** 2026-08-25T22:33:16Z · **RPC health** `ok`

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

No anomaly flags on this run (thresholds in README).

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 441,729,599 |
| Block height | 419,778,230 |
| Block time | 2026-08-25T22:33:16Z |
| Epoch | 1,022 (52.22% · slot 225,600/432,000) |
| Mean TPS (last ~3,600s) | 4,045.0 |
| Mean non-vote TPS | 2,176.0 |
| Median TPS (same window) | 4,045.4 |
| Mean slot time | 365.3 ms |
| Median slot time | 365.9 ms |
| Transaction count (cluster) | 541,840,908,230 |
| Circulating supply | 583,375,632 SOL |
| Total supply | 632,859,493 SOL |

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

- `2bpfa8Jb…` · 29.73K SOL · commission 5% · lag 1089600 slots
- `mrgn4atx…` · 26.11K SOL · commission 0% · lag 9736 slots
- `5P35CJVK…` · 24.00K SOL · commission 100% · lag 1089600 slots
- `gangtCrQ…` · 16.66K SOL · commission 0% · lag 476920 slots
- `kom1oNHy…` · 2.19K SOL · commission 5% · lag 1093083 slots
- `4GEEKSwu…` · 1.35K SOL · commission 5% · lag 717233 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 441729599 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 8928 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 1089600 slots

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $97.28 | coingecko |
| 24h change | -0.30% | CoinGecko |
| Market cap | $56.75B | CoinGecko |
| 24h volume | $6.24B | CoinGecko |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.63B |
| TVL 1d / 7d / 30d | +1.25% / +16.11% / +16.29% |
| DEX volume 24h | $3.00B |
| DEX volume 7d | $20.88B |
| DEX 1d change | +1.96% |
| Fees 24h | $14.49M |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $694.81M | -2.51% |
| Orca DEX | $449.27M | +12.06% |
| BisonFi | $409.15M | -6.69% |
| Meteora DLMM | $278.05M | +3.35% |
| Scorch | $218.92M | -19.10% |
| Manifest Trade | $203.13M | +43.44% |
| Raydium AMM | $195.48M | -5.59% |
| pump.fun | $95.40M | +24.76% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.46B | +1.30% | +26.65% |
| Kamino Lend | Lending | $1.18B | -1.86% | +10.18% |
| Raydium AMM | Dexs | $1.06B | +0.59% | +23.71% |
| Jupiter Lend | Lending | $1.05B | -1.42% | +9.87% |
| Binance Staked SOL | Liquid Staking | $992.39M | +1.30% | +26.62% |
| Jito Liquid Staking | Liquid Staking | $971.50M | +0.42% | +25.99% |
| BlackRock BUIDL | RWA | $876.38M | +4.14% | +1.16% |
| Jupiter Perpetual Exchange | Derivatives | $747.69M | -0.43% | +8.69% |
| Jupiter Staked SOL | Liquid Staking | $500.66M | +1.28% | +25.26% |
| xStocks | RWA | $429.40M | +1.91% | +12.14% |

## Stablecoins

Solana circulating pegged-USD: **$15.85B**
(1d -0.21% · 7d +2.77%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.04B | -3.36% |
| USDT · Tether | $2.83B | -0.00% |
| USDGO · USDGO | $1.24B | +3.77% |
| USD1 · World Liberty Financial USD | $1.11B | +4.03% |
| BUIDL · BlackRock USD | $876.38M | +12.77% |
| PYUSD · PayPal USD | $667.92M | -2.93% |
| USDG · Global Dollar | $629.30M | +3.58% |
| USDe · Ethena USDe | $536.95M | +0.11% |

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.06B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $876.38M
- **xStocks** (RWA) — $429.40M
- **OnRe** (RWA) — $277.01M
- **Ondo Yield Assets** (RWA) — $178.56M
- **Hastra** (RWA) — $163.58M
- **Theo Network thBill** (RWA) — $26.39M
- **Ondo Global Markets** (RWA) — $24.86M
- **Nest Credit** (RWA) — $22.69M

## Daily active addresses

749,721 (Allium, as of 2026-08-24). Provider range 361,127–854,284. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

## Status & news

**status.solana.com:** All Systems Operational (indicator `none`)

- [mb-020624](https://status.solana.com/incidents/n5kcgs8dl9pj) — status · 2024-02-06T15:09:24Z
- [Cluster Instability](https://status.solana.com/incidents/ymr0gyj9xqyz) — status · 2023-02-26T02:09:04Z
- [Public Endpoints and Explorer offline](https://status.solana.com/incidents/mf9plxrkjhnk) — status · 2023-01-08T07:01:17Z
- [Degraded Performance](https://status.solana.com/incidents/kxsv0xcz9dn3) — status · 2022-10-01T07:06:06Z
- [Mainnet Beta Clock Drift](https://status.solana.com/incidents/f68wm876ph9m) — status · 2022-06-06T16:32:07Z
- [Mainnet Beta Outage](https://status.solana.com/incidents/m6qzbgc7np9b) — status · 2022-06-01T21:06:03Z
- [Several RPC nodes down](https://status.solana.com/incidents/6qvg6z1k43zb) — status · 2022-03-28T12:09:49Z
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) — solana.com/news · Mon, 24 Aug 2026 14:19:00 GMT
- [Lowering Slot Time and Validators Economic](https://solana.com/news/lowering-slot-time-and-validators-economic) — solana.com/news · Wed, 19 Aug 2026 10:00:00 GMT
- [Transaction v1 and the ALT Trade-off](https://solana.com/news/transaction-v1-and-the-alt-trade-off) — solana.com/news · Mon, 17 Aug 2026 00:00:00 GMT

## Editorial — Alpenglow (SIMD-0326) — not SIMD-025

_As of 2026-08-25 (2026-08-25 15:33:29 PT). Editorial. Dates and activation targets move. None of this is a live cluster metric; it is a dated reading of public Foundation / SIMD / Anza notes._

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

- None.

## Sources this run

- `rpc.getHealth` [ok] 200 84ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 132ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 45ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 35ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 45ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6815ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 81ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 82ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `llama.chains` [ok] 200 122ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 31ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 52ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 49ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 125ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 57ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 63ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 83ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 463ms https://solana.com/data
- `solana.com.databricks` [ok] 200 1246ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 361ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 105ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 199ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 90ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 204ms https://medium.com/feed/anza-xyz

---

Borealis 1.0.0 · MIT · author `hardest-worker` · regenerate with `python3 generate.py`
