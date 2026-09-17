# Borealis — Solana ecosystem report

**Generated** 2026-09-17T08:07:25Z · 2026-09-17 01:07:25 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-17T08:07:15Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h +3.55%; DEX 24h $2.73B · 1d +1% · vs-7d-ago -11%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

No flags vs rolling baseline (60 samples / llama 7d). Watching.

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 447,745,711 |
| Block height | 425,786,938 |
| Block time | 2026-09-17T08:07:15Z |
| Epoch | 1,036 (44.84% · slot 193,713/432,000) |
| Mean TPS (last ~3,600s) | 3,858.0 |
| Mean non-vote TPS | 1,728.9 |
| Median TPS (same window) | 3,779.6 |
| Mean slot time | 316.6 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 549,350,381,244 |
| Circulating supply | 587,212,331 SOL |
| Total supply | 634,204,758 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 15 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,363,246 SOL |
| Delinquent stake | 397,836.85 SOL (0.090%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.37% / 35.68% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.77M SOL | 4.04% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.35M SOL | 3.72% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.49M SOL | 2.84% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.38M SOL | 2.59% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.74M SOL | 2.22% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.26M SOL | 2.11% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.05M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.39M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.08M SOL | 1.61% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.56M SOL | 1.49% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.20M SOL | 1.41% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.11M SOL | 1.39% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.66M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `ChKZmewG…` · 184.39K SOL · commission 10% · lag 21005 slots
- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 1185273 slots
- `GK2YYwmQ…` · 55.59K SOL · commission 0% · lag 4679 slots
- `t23p8aBQ…` · 14.66K SOL · commission 0% · lag 150475 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 870910 slots
- `mrgn4atx…` · 2.26K SOL · commission 0% · lag 2009 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 701426 slots
- `4GEEKSwu…` · 196.81 SOL · commission 5% · lag 1936099 slots
- `EWARp8Sy…` · 88.61 SOL · commission 5% · lag 749715 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 2046614 slots
- `Je6ckvDi…` · 3.50 SOL · commission 0% · lag 305570 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 18210028 slots

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
| **In-protocol fees 24h** | **$723.33K** (7,138.9 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-15 |
| **Solana REV** | **8,668.9 SOL** / **$878.35K** | MEASURED UTC calendar day 2026-09-15: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-15 · UTC day 2026-09-15 · SOL-USD date 2026-09-15 |
| Jito tip-floor run-rate (NOT REV) | $39.19K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 39194 USD; at p95 floor → 4676924 USD. |
| Protocol fees 24h | $14.20M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $100.03 | coingecko.simple_price |
| 24h change | +3.55% | coingecko.simple_price |
| Market cap | $58.74B | coingecko.simple_price |
| 24h volume | $3.46B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.82B |
| TVL 1d / 7d / 30d | +1.74% / -0.56% / +19.81% |
| DEX volume 24h | $2.73B · 1d +1.12% · vs-7d-ago -11.14% |
| 7d DEX volume | $16.51B · -8.32% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.20M |
| Fees 1d / 7d | +0.97% / -9.61% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $441.42M | -15.00% |
| BisonFi | $353.62M | 0.00% |
| Orca DEX | $262.55M | +38.81% |
| Raydium AMM | $255.24M | +2.60% |
| fomo Wallet | $250.05M | +46.32% |
| HumidiFi | $232.02M | 0.00% |
| Meteora DLMM | $174.16M | +3.34% |
| Tessera V | $171.07M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.59B | +2.97% | +1.88% |
| Kamino Lend | Lending | $1.34B | +1.23% | +0.46% |
| Raydium AMM | Dexs | $1.13B | +3.01% | -0.42% |
| Jupiter Lend | Lending | $1.08B | +0.31% | -0.31% |
| Binance Staked SOL | Liquid Staking | $1.04B | +3.24% | -2.07% |
| Jito Liquid Staking | Liquid Staking | $1.03B | +2.93% | -1.45% |
| Jupiter Perpetual Exchange | Derivatives | $742.24M | +1.77% | -0.69% |
| Jupiter Staked SOL | Liquid Staking | $515.87M | +2.82% | -2.09% |
| Marinade Native | Staking Pool | $380.22M | +2.86% | -2.63% |
| Sentora Curator | Risk Curators | $371.96M | -0.12% | +3.09% |

## Stablecoins

Solana circulating pegged-USD: **$15.38B**
(1d -1.21% · 7d -5.06%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.69B | -1.09% |
| USDT · Tether | $2.34B | -5.63% |
| USDGO · USDGO | $1.38B | +0.36% |
| USD1 · World Liberty Financial USD | $1.32B | +0.00% |
| BUIDL · BlackRock USD | $993.19M | +0.01% |
| PYUSD · PayPal USD | $712.30M | -0.44% |
| USDG · Global Dollar | $623.57M | +1.84% |
| USDe · Ethena USDe | $524.26M | -0.64% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $231.67K (lower bound, not a census).
24h volume $72.82M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$572.49M** across 19 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $302.88M
- **Huma Finance V2** (RWA) — $184.06M
- **Plume Vaults** (RWA) — $28.50M
- **Ondo Global Markets** (RWA) — $27.47M
- **MatrixDock XAUM** (RWA) — $6.77M
- **Midas RWA** (RWA) — $5.64M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $2.76M

## Daily active addresses

836,063 (Allium, as of 2026-09-16). Provider range 420,584–867,494. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — solana.com/news · Mon, 14 Sep 2026 11:00:00 GMT
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — solana.com/news · Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — solana.com/news · Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) — solana.com/news · Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — solana.com/news · Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — solana.com/news · Thu, 03 Sep 2026 15:15:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-17 (2026-09-17 01:07:25 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=activated-not-yet-effective, 200ms=pending. Observed mean slot ~317 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `on-chain` — On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=activated-not-yet-effective, 200ms=pending.
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

- **X / Twitter RSS** — Public X/Nitter-style RSS yielded no usable items this run (403/gated skipped). xcancel.solana 451, xcancel.solana_status 451, xcancel.anza_xyz 451, xcancel.solana_devs 451, nitter.solana 200, nitter.solana_status empty-or-gated
- **Median tx fee** — no getBlock samples
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 270ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 172ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 216ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 242ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 163ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7081ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 417ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 170ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 332ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 132ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 75ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 75ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1139ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 260ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 140ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 115ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 151ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 728ms https://solana.com/data
- `solana.com.databricks` [ok] 200 179ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 532ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 308ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 272ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 130ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 374ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 329ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 156ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 166ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 172ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 231ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 553ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2476ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 239ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 308ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 123ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 238ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 202ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 260ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 220ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 176ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 128ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 366ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 351ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 236ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 227ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 255ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 212ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 237ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 204ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 160ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 213ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 230ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 231ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 225ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 224ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 434ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 228ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 216ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 450ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 203ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 196ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 209ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 286ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 238ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 220ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 4816ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1755ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1539ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1415ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1154ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1603ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1848ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1408ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.QUBTx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.XRXx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.FLNCx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.INDIx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.PCTx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.METCx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.WGSx` [ok] 200 574ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.WRLDx` [ok] 200 1019ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.circ.PCTx` [ok] 200 1139ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 1347ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 1199ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 1465ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 1189ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 1693ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.WYFIx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.WRLDx` [ok] 200 1152ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.price.SCIx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.price.AIx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.QUBTx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.DRSx` [ok] 200 542ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.circ.AIx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.price.SAILx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.price.BSYx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.circ.DRSx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.circ.SCIx` [ok] 200 896ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.mult.BETRx` [ok] 200 747ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.DRSx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 820ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.GSATx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.price.MPx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.circ.SAILx` [ok] 200 1236ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.price.DVAx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.mult.SCIx` [ok] 200 825ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.DCIx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.mult.SAILx` [ok] 200 604ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.price.GDDYx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.circ.DVAx` [ok] 200 1149ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.mult.DVAx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.circ.DCIx` [ok] 200 1651ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.mult.DCIx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.price.BXPx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.circ.FLNCx` [ok] 200 6758ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 5165ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.BXPx` [ok] 200 983ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.BXPx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.circ.MPx` [ok] 200 4523ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.circ.GSATx` [ok] 200 4642ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.mult.MPx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.circ.BSYx` [ok] 200 5460ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.price.WMSx` [ok] 200 672ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.price.DYx` [ok] 200 1019ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.price.AMx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.GDDYx` [ok] 200 3966ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.mult.BSYx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.circ.FRHCx` [ok] 200 883ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.mult.GDDYx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.price.FDSx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.mult.GSATx` [ok] 200 868ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.RYANx` [ok] 200 3625ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.mult.RYANx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.price.ALSNx` [ok] 200 638ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.price.SMTCx` [ok] 200 641ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.price.SFx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.circ.SFx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 1215ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.mult.SFx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.price.AXSMx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.price.EGPx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.circ.ALSNx` [ok] 200 1141ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.price.BPOPx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.circ.DYx` [ok] 200 3064ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.circ.AMx` [ok] 200 2901ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.circ.EGPx` [ok] 200 1254ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.circ.WMSx` [ok] 200 3227ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.circ.FDSx` [ok] 200 2686ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.mult.EGPx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.mult.DYx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.mult.FDSx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.price.TTMIx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.price.AEISx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.mult.WMSx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 1404ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.circ.SMTCx` [ok] 200 2930ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.price.KTOSx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.mult.AMx` [ok] 200 1039ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.mult.BPOPx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.price.HRLx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.mult.SMTCx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.price.DPZx` [ok] 200 989ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.circ.AXSMx` [ok] 200 2834ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.price.PAGx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.price.SEICx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.circ.AEISx` [ok] 200 1263ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.mult.AXSMx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.circ.TTMIx` [ok] 200 1522ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.AEISx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.price.HIIx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.mult.TTMIx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.price.EHCx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.circ.KTOSx` [ok] 200 1326ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.price.GFLx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.circ.HRLx` [ok] 200 1207ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.mult.HIIx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.circ.DPZx` [ok] 200 1312ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.mult.HRLx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.ARx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.circ.SEICx` [ok] 200 1082ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.circ.ARx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.mult.DPZx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.mult.SEICx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.price.MGMx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.price.DOCUx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.mult.ARx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.price.HALOx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.mult.KTOSx` [ok] 200 990ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.circ.EHCx` [ok] 200 1170ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.price.WTRGx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.AFGx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.circ.GFLx` [ok] 200 1210ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.EHCx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.GFLx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.price.AMKRx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.circ.DOCUx` [ok] 200 1183ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.price.HUBSx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.circ.AMKRx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.circ.MGMx` [ok] 200 1377ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.circ.HALOx` [ok] 200 1249ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.mult.DOCUx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.circ.AFGx` [ok] 200 1093ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.circ.WTRGx` [ok] 200 1230ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.price.GMEDx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.mult.HALOx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.mult.MGMx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.mult.AMKRx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.price.JKHYx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.AFGx` [ok] 200 508ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.price.OCx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.price.BMRNx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.price.IESCx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.circ.BMRNx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.price.CRx` [ok] 200 858ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.mult.BMRNx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.circ.PAGx` [ok] 200 4295ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.price.JEFx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.mult.PAGx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.circ.HUBSx` [ok] 200 1966ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 1604ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.circ.JKHYx` [ok] 200 1418ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.mult.HUBSx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.mult.JKHYx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.circ.OCx` [ok] 200 1623ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.price.AMHx` [ok] 200 684ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.price.FIVEx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.price.ITx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.mult.OCx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 693ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.circ.CRx` [ok] 200 1284ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.price.MDGLx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.circ.JEFx` [ok] 200 1182ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.circ.IESCx` [ok] 200 1805ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.price.VNOMx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.mult.CRx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.mult.JEFx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.price.UHALx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.mult.IESCx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.AHRx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.price.IVZx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.circ.AMHx` [ok] 200 1402ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.circ.VNOMx` [ok] 200 1001ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.mult.VNOMx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.CORTx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.circ.ITx` [ok] 200 1838ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.circ.UHALx` [ok] 200 1220ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.price.STRLx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.circ.AHRx` [ok] 200 1177ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.mult.UHALx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.mult.ITx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.AHRx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.circ.FIVEx` [ok] 200 2302ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.circ.MDGLx` [ok] 200 2038ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.price.NWSAx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.circ.IVZx` [ok] 200 1431ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.price.AURx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.price.Hx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.mult.FIVEx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.mult.IVZx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.mult.MDGLx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.price.ARWRx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.circ.CORTx` [ok] 200 978ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.price.NWSx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.price.GWREx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.circ.NWSx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.CORTx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.circ.NWSAx` [ok] 200 1080ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 979ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.price.MANHx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.price.CACIx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.circ.STRLx` [ok] 200 1612ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.mult.NWSAx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.circ.Hx` [ok] 200 1263ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.mult.STRLx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.price.BAXx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.mult.AURx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.circ.GWREx` [ok] 200 946ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.circ.ARWRx` [ok] 200 1162ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.price.RVTYx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/RVTYx/price-data
- `xstocks.mult.Hx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.circ.BAXx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.price.TXRHx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/TXRHx/price-data
- `xstocks.mult.ARWRx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.mult.GWREx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.price.CNAx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/CNAx/price-data
- `xstocks.circ.MANHx` [ok] 200 1238ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.circ.CACIx` [ok] 200 1331ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.circ.RVTYx` [ok] 200 1008ms https://api.backed.fi/api/v2/public/assets/RVTYx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.CACIx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.mult.RVTYx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/RVTYx/multiplier?network=Solana
- `xstocks.circ.CNAx` [ok] 200 1207ms https://api.backed.fi/api/v2/public/assets/CNAx/circulating-supply?format=object
- `xstocks.circ.TXRHx` [ok] 200 1565ms https://api.backed.fi/api/v2/public/assets/TXRHx/circulating-supply?format=object
- `xstocks.mult.CNAx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/CNAx/multiplier?network=Solana
- `xstocks.mult.TXRHx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/TXRHx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 675ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 300ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.QUBTx` [ok] 200 137ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.INDIx` [ok] 200 142ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.WRLDx` [ok] 200 136ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.XRXx` [ok] 200 137ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 142ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.WGSx` [ok] 200 135ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.FLNCx` [ok] 200 133ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.AIx` [ok] 200 144ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jito.tip_floor` [ok] 200 119ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 349ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 137ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 148ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 161ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 150ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 160ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 170ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
