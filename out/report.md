# Borealis — Solana ecosystem report

**Generated** 2026-09-07T20:24:56Z · 2026-09-07 13:24:56 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-07T20:24:46Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** WATCH · **Ecosystem** SURGE — SOL 24h -1.61%; DEX 24h $2.90B · 1d +56% · vs-7d-ago +51%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Correlation: congestion (slot time ↑ + non-vote TPS ↓ + fees ↑)** — Slot time 317 ms, last non-vote TPS 1,688 vs window median 1,954, DeFiLlama fees 1d +45.0%. (threshold: `elevated slot time AND depressed non-vote TPS AND fees 1d >= 8%`)
- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +44.97%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +55.76%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +50.52%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 445,155,515 |
| Block height | 423,199,695 |
| Block time | 2026-09-07T20:24:46Z |
| Epoch | 1,030 (45.26% · slot 195,518/432,000) |
| Mean TPS (last ~3,600s) | 4,106.5 |
| Mean non-vote TPS | 1,989.8 |
| Median TPS (same window) | 4,069.9 |
| Mean slot time | 317.0 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 546,116,511,601 |
| Circulating supply | 586,165,802 SOL |
| Total supply | 633,643,082 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,428,459 SOL |
| Delinquent stake | 49,528.97 SOL (0.011%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.19% / 35.46% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 3.97% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.34M SOL | 3.72% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.52M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.40M SOL | 2.59% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.56M SOL | 2.18% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.18M SOL | 2.09% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.38M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.86M SOL | 1.56% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.60M SOL | 1.50% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.39% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.39% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.97M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.64M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.85M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 108485 slots
- `xLabscif…` · 8.89K SOL · commission 5% · lag 1367142 slots
- `prt1st4R…` · 7.04K SOL · commission 5% · lag 1668573 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 1806792 slots
- `5ZjxMYBb…` · 3.79K SOL · commission 0% · lag 1189593 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 616324 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 1716876 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 2355164 slots
- `HFTcVVrX…` · 148.42 SOL · commission 100% · lag 2355058 slots
- `As9NxA9b…` · 46.58 SOL · commission 100% · lag 2355181 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 445155515 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 316504 slots

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
| **In-protocol fees 24h** | **$658.16K** (6,158.9 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-06 |
| **Solana REV** | **7,251.8 SOL** / **$774.94K** | MEASURED UTC calendar day 2026-09-06: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-06 · UTC day 2026-09-06 · SOL-USD date 2026-09-06 |
| Jito tip-floor run-rate (NOT REV) | $38.99K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 38990 USD; at p95 floor → 11405483 USD. |
| Protocol fees 24h | $14.66M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9963 |
| p90 / p99 | 0.000015 / 0.000412 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.94 | coingecko.simple_price |
| 24h change | -1.61% | coingecko.simple_price |
| Market cap | $60.93B | coingecko.simple_price |
| 24h volume | $3.20B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.90B |
| TVL 1d / 7d / 30d | -0.17% / +1.89% / +24.17% |
| DEX volume 24h | $2.90B · 1d +55.76% · vs-7d-ago +50.52% |
| 7d DEX volume | $16.07B · -11.56% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.66M |
| Fees 1d / 7d | +44.97% / +18.04% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $677.89M | -2.21% |
| Raydium AMM | $311.99M | +181.29% |
| Orca DEX | $267.46M | +111.63% |
| BisonFi | $241.45M | +32.54% |
| Meteora DLMM | $223.09M | +82.29% |
| Tessera V | $206.39M | +139.77% |
| HumidiFi | $143.21M | +123.80% |
| Manifest Trade | $132.04M | +12.67% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.59B | -2.30% | +1.24% |
| Kamino Lend | Lending | $1.33B | -1.62% | +7.04% |
| Raydium AMM | Dexs | $1.14B | -1.71% | +3.06% |
| Jupiter Lend | Lending | $1.09B | -2.55% | +2.09% |
| Binance Staked SOL | Liquid Staking | $1.08B | -2.37% | +1.89% |
| Jito Liquid Staking | Liquid Staking | $1.06B | -3.24% | +2.13% |
| BlackRock BUIDL | RWA | $977.90M | -0.00% | +0.58% |
| Jupiter Perpetual Exchange | Derivatives | $753.08M | -1.94% | -1.53% |
| Jupiter Staked SOL | Liquid Staking | $537.98M | -2.59% | +1.04% |
| xStocks | RWA | $447.32M | -0.79% | +1.60% |

## Stablecoins

Solana circulating pegged-USD: **$16.30B**
(1d +0.34% · 7d +4.87%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.32B | +0.21% |
| USDT · Tether | $2.77B | +0.00% |
| USDGO · USDGO | $1.37B | +1.11% |
| USD1 · World Liberty Financial USD | $1.26B | +0.16% |
| BUIDL · BlackRock USD | $977.90M | 0.00% |
| PYUSD · PayPal USD | $733.10M | -2.57% |
| USDG · Global Dollar | $576.82M | -0.94% |
| USDe · Ethena USDe | $535.69M | -0.11% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 63 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 63 · priced-subset mcap $638.14K (lower bound, not a census).
24h volume $60.87M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $447.32M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 63 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.36B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $977.90M
- **xStocks** (RWA) — $447.32M
- **OnRe** (RWA) — $302.47M
- **Huma Finance V2** (RWA) — $186.16M
- **Ondo Yield Assets** (RWA) — $180.03M
- **Hastra** (RWA) — $154.65M
- **Ondo Global Markets** (RWA) — $26.14M
- **Plume Vaults** (RWA) — $24.03M

## Daily active addresses

858,456 (Allium, as of 2026-09-06). Provider range 418,160–858,456. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [# How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — solana.com/news · Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) — solana.com/news · Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — solana.com/news · Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — solana.com/news · Thu, 03 Sep 2026 15:15:00 GMT
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — solana.com/news · Wed, 02 Sep 2026 09:00:00 GMT
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) — solana.com/news · Tue, 01 Sep 2026 09:00:00 GMT
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) — solana.com/news · Fri, 28 Aug 2026 16:00:00 GMT `mainnet`
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) — solana.com/news · Thu, 27 Aug 2026 04:15:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-07 (2026-09-07 13:24:56 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **X / Twitter RSS** — Public X/Nitter-style RSS yielded no usable items this run (403/gated skipped). xcancel.solana empty-or-gated, xcancel.solana_status empty-or-gated, xcancel.anza_xyz empty-or-gated, xcancel.solana_devs empty-or-gated, nitter.solana 403, nitter.solana_status 403
- **xStocks** — priced up to 80 of 726 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 568ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 492ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 470ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 501ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 479ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 8846ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 918ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 280ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 183ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 406ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 128ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 985ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1126ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 434ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 373ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 187ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 254ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 462ms https://solana.com/data
- `solana.com.databricks` [ok] 200 264ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 551ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 326ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 7321ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 188ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 474ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 885ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 383ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 395ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 413ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [FAIL] 403 222ms https://nitter.perennialte.ch/solana/rss — HTTP 403 Forbidden
- `rss.nitter.solana_status` [FAIL] 403 106ms https://nitter.perennialte.ch/solana_status/rss — HTTP 403 Forbidden
- `rss.nitter.anza_xyz` [FAIL] 403 125ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 403 Forbidden
- `rss.nitter.solana_devs` [FAIL] 403 111ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 403 Forbidden
- `rss.rsshub.solana` [FAIL] 404 510ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 1459ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 517ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 493ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1891ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1911ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1793ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1781ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1837ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2039ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1962ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2191ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1877ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1868ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1836ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1818ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1801ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1803ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1902ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2597ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2028ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1966ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1921ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1814ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1426ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1030ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.NVDAx` [FAIL]  12083ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AAPLx` [FAIL]  12082ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METAx` [FAIL]  12081ms https://api.backed.fi/api/v2/public/assets/METAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AMZNx` [FAIL]  12082ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SPYx` [FAIL]  12084ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MSFTx` [FAIL]  12083ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GOOGLx` [FAIL]  12083ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.TSLAx` [FAIL]  12091ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MSFTx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 503ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.NVDAx` [ok] 200 779ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 778ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 989ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 759ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 950ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 1708ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 1576ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.QQQx` [FAIL]  12073ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.COINx` [FAIL]  12071ms https://api.backed.fi/api/v2/public/assets/COINx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.QQQx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.DRAMx` [FAIL]  12084ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.COINx` [ok] 200 556ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.MVLLx` [FAIL]  12074ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.QQQx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.MUUx` [FAIL]  12081ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.COINx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.AXTIx` [FAIL]  12084ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DRAMx` [ok] 200 857ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.circ.AXTIx` [ok] 200 593ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.circ.MUUx` [ok] 200 723ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.MVLLx` [ok] 200 1061ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.DJTx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.KORUx` [FAIL]  12084ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MUUx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.circ.DJTx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.DJTx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.price.SHEINx` [ok] 200 487ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.KORUx` [ok] 200 768ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 1664ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.SHEINx` [ok] 200 829ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.KORUx` [ok] 200 880ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.NWGx` [ok] 200 1373ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.mult.SHEINx` [ok] 200 587ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.circ.NWGx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.BANKCx` [ok] 200 957ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.NWGx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 3506ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 532ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 544ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.TNGYIx` [ok] 200 824ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.price.MMGx` [ok] 200 1766ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 598ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.TNGYIx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.CTINSx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 699ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.MMGx` [ok] 200 1511ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 542ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 2617ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.price.SNBIOx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 794ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 783ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 795ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 1244ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 835ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 4700ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 815ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 928ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.WRFHDx` [ok] 200 3802ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.INTWx` [ok] 200 10404ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.CRESBx` [ok] 200 956ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.INTWx` [ok] 200 670ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 904ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.price.SOXSx` [ok] 200 11138ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.mult.INTWx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.SOXSx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 522ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 1689ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 861ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 11028ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 777ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.WXXDCx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.SNXXx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.CSPCx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 4596ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.JTGEXx` [ok] 200 1353ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.SNXXx` [ok] 200 877ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 682ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.CMENDx` [ok] 200 623ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.CMENDx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 1533ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 718ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 1347ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 1397ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.ASMPTx` [ok] 200 1118ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.JDHLTx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.CMERPx` [ok] 200 3779ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.SITCx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.SNDSCx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 1492ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.SNDSCx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.CMERPx` [ok] 200 1029ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 1409ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.PRADx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 1564ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.PRADx` [ok] 200 694ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 747ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.WHGROx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.CLONPx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.CRESPx` [ok] 200 2116ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 509ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.SINOx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.WHGROx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 1600ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.CRESPx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 503ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.CRESPx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.circ.CTPCAx` [ok] 200 622ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 577ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.CKAHx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 456ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 835ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 1153ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.GENTEx` [ok] 200 1471ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 1023ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.GENTEx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 591ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 509ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.HKCGAx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.KUAIx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 2152ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 951ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 509ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.SMOIHx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CHONGx` [ok] 200 701ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.COVELx` [ok] 200 533ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 802ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.NONGx` [ok] 200 1652ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.MEITx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 1292ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 1855ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 682ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 2199ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.COVELx` [ok] 200 1109ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.NONGx` [ok] 200 716ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 1289ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.HNDLDx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 649ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.GEELx` [ok] 200 962ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 1331ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 601ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.HNDLDx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 606ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 912ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 1362ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 717ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 3726ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1641ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 383ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INTWx` [ok] 200 205ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.SHEINx` [ok] 200 207ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.SNXXx` [ok] 200 192ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jup.tokens.search.SOXSx` [ok] 200 196ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jup.tokens.search.MEITx` [ok] 200 189ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 197ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.KUAIx` [ok] 200 191ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.MIXUx` [ok] 200 194ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jito.tip_floor` [ok] 200 201ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 444ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 114ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 480ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 481ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 480ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 405ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 275ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
