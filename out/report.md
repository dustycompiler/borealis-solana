# Borealis — Solana ecosystem report

**Generated** 2026-09-13T10:49:31Z · 2026-09-13 03:49:31 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-13T10:49:20Z · **RPC health** `ok`
**Health score** 91 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -2.37%; DEX 24h $2.47B · 1d -22% · vs-7d-ago +33%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -22.31%. (threshold: `|1d %| >= 8`)
- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -22.25%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +37.45%. (threshold: `|7d %| >= 20`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -2.37%, DeFiLlama TVL 1d -0.87%, DEX 1d -22.31%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **INFO · Daily active addresses vs 30d median** — Current 1,043,743.00 is +31.2% vs 30d median 795,694.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +32.64%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 446,684,091 |
| Block height | 424,726,759 |
| Block time | 2026-09-13T10:49:20Z |
| Epoch | 1,033 (99.10% · slot 428,092/432,000) |
| Mean TPS (last ~3,600s) | 3,490.3 |
| Mean non-vote TPS | 1,354.0 |
| Median TPS (same window) | 3,442.3 |
| Mean slot time | 315.7 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 548,008,535,716 |
| Circulating supply | 586,644,632 SOL |
| Total supply | 633,923,409 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 677 |
| Delinquent | 13 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 435,009,114 SOL |
| Delinquent stake | 1,828,567.26 SOL (0.419%) |
| Nakamoto (33% / 50% / 67%) | 18 / 40 / 79 |
| Top 10 / 20 stake share | 24.50% / 35.87% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.56M SOL | 4.04% | 7% | 0 |
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

- `pSo1KZXg…` · 1.64M SOL · commission 4% · lag 428064 slots
- `FGiEdzde…` · 128.28K SOL · commission 5% · lag 123653 slots
- `EWARp8Sy…` · 31.93K SOL · commission 5% · lag 6668 slots
- `mrgn4atx…` · 19.58K SOL · commission 0% · lag 131859 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 428064 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 428064 slots
- `4GEEKSwu…` · 326.50 SOL · commission 5% · lag 874479 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 984994 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 446684091 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 62635221 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 428064 slots
- `4kdjgZKJ…` · 1.05 SOL · commission 100% · lag 446684091 slots

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
| **In-protocol fees 24h** | **$829.53K** (8,175.5 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-11 |
| **Solana REV** | **9,658.8 SOL** / **$980.02K** | MEASURED UTC calendar day 2026-09-11: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-11 · UTC day 2026-09-11 · SOL-USD date 2026-09-11 |
| Jito tip-floor run-rate (NOT REV) | $63.12K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 63121 USD; at p95 floor → 11650321 USD. |
| Protocol fees 24h | $13.90M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9964 |
| p90 / p99 | 0.000007 / 0.000091 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $99.59 | coingecko.simple_price |
| 24h change | -2.37% | coingecko.simple_price |
| Market cap | $58.43B | coingecko.simple_price |
| 24h volume | $1.87B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.85B |
| TVL 1d / 7d / 30d | -0.87% / -1.19% / +20.62% |
| DEX volume 24h | $2.47B · 1d -22.31% · vs-7d-ago +32.64% |
| 7d DEX volume | $18.59B · +23.13% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $13.90M |
| Fees 1d / 7d | -22.25% / +37.45% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| BisonFi | $471.70M | 0.00% |
| PumpSwap | $377.15M | +28.21% |
| Raydium AMM | $298.95M | -46.21% |
| Tessera V | $202.03M | 0.00% |
| Meteora DLMM | $161.06M | -55.63% |
| HumidiFi | $155.95M | 0.00% |
| GoonFi | $111.18M | 0.00% |
| Scorch | $108.66M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.53B | -1.67% | -4.60% |
| Kamino Lend | Lending | $1.34B | -0.37% | +0.20% |
| Raydium AMM | Dexs | $1.12B | -1.26% | -2.17% |
| Jupiter Lend | Lending | $1.09B | -0.80% | -2.22% |
| Binance Staked SOL | Liquid Staking | $1.03B | -2.12% | -5.73% |
| Jito Liquid Staking | Liquid Staking | $1.03B | -1.66% | -5.31% |
| BlackRock BUIDL | RWA | $992.60M | 0.00% | -2.25% |
| Jupiter Perpetual Exchange | Derivatives | $743.26M | -1.07% | -2.61% |
| Jupiter Staked SOL | Liquid Staking | $517.67M | -1.63% | -5.33% |
| Sentora Curator | Risk Curators | $389.48M | -0.10% | -1.14% |

## Stablecoins

Solana circulating pegged-USD: **$16.11B**
(1d -0.18% · 7d -0.95%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.28B | +0.19% |
| USDT · Tether | $2.55B | -2.68% |
| USDGO · USDGO | $1.38B | 0.00% |
| USD1 · World Liberty Financial USD | $1.31B | +0.15% |
| BUIDL · BlackRock USD | $992.60M | 0.00% |
| PYUSD · PayPal USD | $707.23M | -0.17% |
| USDG · Global Dollar | $603.04M | +0.26% |
| USDe · Ethena USDe | $533.16M | -0.52% |

## Tokenized equities (xStocks)


Listed 800 · Solana deployments 800 · priced 0 · priced-subset mcap — (lower bound, not a census).
24h volume $78.30M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 0 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.93B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.60M
- **OnRe** (RWA) — $297.47M
- **Huma Finance V2** (RWA) — $192.48M
- **Ondo Yield Assets** (RWA) — $179.92M
- **Hastra** (RWA) — $148.76M
- **Plume Vaults** (RWA) — $27.48M
- **Ondo Global Markets** (RWA) — $25.55M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.36M

## Daily active addresses

1,043,743 (Allium, as of 2026-09-11). Provider range 418,707–1,043,743. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — solana.com/news · Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — solana.com/news · Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) — solana.com/news · Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — solana.com/news · Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — solana.com/news · Thu, 03 Sep 2026 15:15:00 GMT
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — solana.com/news · Wed, 02 Sep 2026 09:00:00 GMT
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) — solana.com/news · Tue, 01 Sep 2026 09:00:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-13 (2026-09-13 03:49:31 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **X / Twitter RSS** — Public X/Nitter-style RSS yielded no usable items this run (403/gated skipped). xcancel.solana empty-or-gated, xcancel.solana_status empty-or-gated, xcancel.anza_xyz empty-or-gated, xcancel.solana_devs empty-or-gated, nitter.solana TimeoutError: The read operation timed out, nitter.solana_status empty-or-gated
- **xStocks market cap** — Listed Solana-deployed xStocks but quote and/or circulating missing. Mcap omitted.
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.
- **xStocks** — price, circulating-supply, and/or currentMultiplier missing — market cap omitted (never assumed multiplier=1.0)

## Sources this run

- `rpc.getHealth` [ok] 200 58ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 28ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 37ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 28ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 64ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5589ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 59ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 73ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 71ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 160ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 33ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 25ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 38ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 64ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 49ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 46ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 94ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 275ms https://solana.com/data
- `solana.com.databricks` [ok] 200 85ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 453ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 108ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 26ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 48ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 422ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 1015ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 81ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 82ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 284ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [FAIL]  18398ms https://nitter.perennialte.ch/solana/rss — TimeoutError: The read operation timed out
- `rss.nitter.solana_status` [ok] 200 4120ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [FAIL] 502 3337ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_devs` [FAIL] 502 4338ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 502 Bad Gateway
- `rss.rsshub.solana` [FAIL] 404 224ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 21ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 29ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 30ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 179ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 238ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 219ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 213ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 136ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 263ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 28ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 309ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 317ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 420ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 135ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 216ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 256ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 345ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 427ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1396ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1579ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1255ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1312ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1323ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1364ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1123ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1497ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.QQQx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WGSx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.XRXx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WRLDx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.INDIx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.COINx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/COINx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SPYx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.FLNCx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.INDIx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 1050ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 1150ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 422ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.PCTx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METCx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/METCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.QUBTx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WYFIx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BETRx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AIx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/AIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.METCx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 830ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.price.DRSx` [FAIL]  12013ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SCIx` [FAIL]  12016ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.PCTx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 835ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 1249ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.SCIx` [ok] 200 1128ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.circ.BETRx` [ok] 200 2295ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.SCIx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.mult.BETRx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.circ.DRSx` [ok] 200 1686ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.SAILx` [FAIL]  12018ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BSYx` [FAIL]  12009ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SAILx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.mult.SAILx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.price.GSATx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MPx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/MPx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.GSATx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.price.DVAx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BSYx` [ok] 200 1146ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.mult.BSYx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.mult.GSATx` [ok] 200 635ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.MPx` [ok] 200 1084ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.price.DCIx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MPx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.circ.DVAx` [ok] 200 1081ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.price.GDDYx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.DVAx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.price.RYANx` [FAIL]  12014ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DCIx` [ok] 200 1256ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.circ.GDDYx` [ok] 200 1223ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.mult.DCIx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.mult.GDDYx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.circ.RYANx` [ok] 200 1392ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.mult.RYANx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.price.BXPx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DYx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/DYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.FRHCx` [FAIL]  12012ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BXPx` [ok] 200 1115ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.mult.BXPx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.WMSx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AMx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/AMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AMx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.AMx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.circ.FRHCx` [ok] 200 1251ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.circ.DYx` [ok] 200 1540ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 110ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.circ.WMSx` [ok] 200 1064ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.mult.WMSx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.FDSx` [FAIL]  12013ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ALSNx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ALSNx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.price.SMTCx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.FDSx` [ok] 200 959ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.circ.SMTCx` [ok] 200 1059ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.mult.SMTCx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.price.SFx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/SFx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AXSMx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AXSMx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.mult.AXSMx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.price.EGPx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SFx` [ok] 200 1150ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.price.BPOPx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SFx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.price.TTMIx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AEISx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.EGPx` [ok] 200 1118ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.circ.AEISx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.mult.EGPx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 1170ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.mult.AEISx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.mult.BPOPx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.price.DPZx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DPZx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.circ.TTMIx` [ok] 200 1732ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.DPZx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.mult.TTMIx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.HRLx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HRLx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.mult.HRLx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.KTOSx` [FAIL]  12015ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.KTOSx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.mult.KTOSx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.price.PAGx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.PAGx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.mult.PAGx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.price.SEICx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SEICx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.price.HIIx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HIIx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.price.EHCx` [FAIL]  12010ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SEICx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.mult.HIIx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.circ.EHCx` [ok] 200 499ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.price.GFLx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ARx` [FAIL]  12012ms https://api.backed.fi/api/v2/public/assets/ARx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.EHCx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.circ.GFLx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.circ.ARx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.price.MGMx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.ARx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.mult.GFLx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.circ.MGMx` [ok] 200 603ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.mult.MGMx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.price.DOCUx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DOCUx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.mult.DOCUx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.price.HALOx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HALOx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.mult.HALOx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.price.WTRGx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AFGx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WTRGx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.mult.WTRGx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.mult.AFGx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.price.HUBSx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HUBSx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.price.AMKRx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GMEDx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.HUBSx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.circ.AMKRx` [ok] 200 565ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.mult.AMKRx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.price.JKHYx` [FAIL]  12014ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.GMEDx` [ok] 200 762ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.mult.GMEDx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.circ.JKHYx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.mult.JKHYx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.price.IESCx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.IESCx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.mult.IESCx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.OCx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/OCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.OCx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.mult.OCx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.price.CRx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/CRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BMRNx` [FAIL]  12012ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CRx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.mult.CRx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.circ.BMRNx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.mult.BMRNx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.price.JEFx` [FAIL]  12015ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.JEFx` [ok] 200 109ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.mult.JEFx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.price.AMHx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AMHx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.price.FIVEx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.AMHx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.price.ITx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/ITx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.FIVEx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.mult.FIVEx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.circ.ITx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.mult.ITx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.price.MDGLx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MDGLx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.price.VNOMx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MDGLx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.circ.VNOMx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.mult.VNOMx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.UHALx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AHRx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.UHALx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.circ.AHRx` [ok] 200 111ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.mult.AHRx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.IVZx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.UHALx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.circ.IVZx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.mult.IVZx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.price.CORTx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CORTx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.mult.CORTx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.STRLx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.STRLx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.mult.STRLx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.price.NWSAx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.NWSAx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.mult.NWSAx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.price.AURx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/AURx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AURx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.price.Hx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/Hx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.Hx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.mult.Hx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.mult.AURx` [ok] 200 677ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.price.ARWRx` [FAIL]  12017ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ARWRx` [ok] 200 110ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.price.GWREx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.GWREx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.price.NWSx` [FAIL]  12011ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.ARWRx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.price.MANHx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CACIx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CACIx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.circ.MANHx` [ok] 200 556ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.price.BAXx` [FAIL]  12016ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MANHx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.circ.BAXx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.BAXx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 30ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.WGSx` [ok] 200 38ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.XRXx` [ok] 200 36ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.FLNCx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.WRLDx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.INDIx` [ok] 200 39ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 37ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.METCx` [ok] 200 39ms https://lite-api.jup.ag/tokens/v2/search?query=METCx
- `jup.tokens.search.PCTx` [ok] 200 37ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jito.tip_floor` [ok] 200 252ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 264ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 11ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 38ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 30ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 35ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 35ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 98ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
