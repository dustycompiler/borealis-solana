# Borealis — Solana ecosystem report

**Generated** 2026-09-18T15:06:21Z · 2026-09-18 08:06:21 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-18T15:06:12Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h +9.19%; DEX 24h $2.59B · 1d -7% · vs-7d-ago -14%; slot 268 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large SOL 24h price move** — SOL/USD 24h change is +9.19% (coingecko.simple_price). (threshold: `|24h %| >= 8`)
- **INFO · TPS vs 30d median (solana.com/data tx/86400)** — Current 5,311.93 TPS is +34.3% vs 30d median 3,954.42 TPS (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 448,119,004 |
| Block height | 426,159,953 |
| Block time | 2026-09-18T15:06:12Z |
| Epoch | 1,037 (31.25% · slot 135,006/432,000) |
| Mean TPS (last ~3,600s) | 5,311.9 |
| Mean non-vote TPS | 2,793.3 |
| Median TPS (same window) | 5,293.0 |
| Mean slot time | 267.6 ms |
| Median slot time | 266.7 ms |
| Transaction count (cluster) | 549,828,412,022 |
| Circulating supply | 587,297,112 SOL |
| Total supply | 634,298,366 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 677 |
| Delinquent | 11 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,453,838 SOL |
| Delinquent stake | 158,570.06 SOL (0.036%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.28% / 35.59% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.82M SOL | 4.05% | 7% | 0 |
| 2 | `HEL1USMZ…` | 15.82M SOL | 3.60% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.51M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.40M SOL | 2.59% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.78M SOL | 2.23% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.25M SOL | 2.11% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.08M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.40M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.09M SOL | 1.61% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.56M SOL | 1.49% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.21M SOL | 1.41% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.11M SOL | 1.39% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.97M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.67M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.84M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 1558566 slots
- `t23p8aBQ…` · 14.66K SOL · commission 0% · lag 523768 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 57890 slots
- `mrgn4atx…` · 2.26K SOL · commission 0% · lag 107331 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 244252 slots
- `Hgozywot…` · 807.55 SOL · commission 100% · lag 175379 slots
- `TiMxX1ya…` · 114.23 SOL · commission 0% · lag 72500525 slots
- `EWARp8Sy…` · 98.61 SOL · commission 5% · lag 1123008 slots
- `BZBKHmW1…` · 5.90 SOL · commission 5% · lag 45334525 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 64070134 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 1862977 slots

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
| **In-protocol fees 24h** | **$742.27K** (7,633.1 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-16 |
| **Solana REV** | **9,347.7 SOL** / **$909.00K** | MEASURED UTC calendar day 2026-09-16: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-16 · UTC day 2026-09-16 · SOL-USD date 2026-09-16 |
| Jito tip-floor run-rate (NOT REV) | $112.28K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 112279 USD; at p95 floor → 21484863 USD. |
| Protocol fees 24h | $14.68M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $109.93 | coingecko.simple_price |
| 24h change | +9.19% | coingecko.simple_price |
| Market cap | $64.69B | coingecko.simple_price |
| 24h volume | $5.28B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.07B |
| TVL 1d / 7d / 30d | +5.45% / +6.02% / +24.22% |
| DEX volume 24h | $2.59B · 1d -7.41% · vs-7d-ago -13.62% |
| 7d DEX volume | $17.44B · -5.59% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.68M |
| Fees 1d / 7d | -1.45% / +0.48% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| BisonFi | $378.33M | -14.03% |
| PumpSwap | $329.29M | -25.40% |
| Raydium AMM | $309.01M | +19.10% |
| HumidiFi | $281.64M | -6.68% |
| fomo Wallet | $201.47M | -24.71% |
| Meteora DLMM | $177.93M | +2.16% |
| Tessera V | $168.27M | +34.35% |
| Orca DEX | $153.36M | -40.09% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.75B | +8.62% | +12.44% |
| Kamino Lend | Lending | $1.36B | +0.62% | +2.25% |
| Raydium AMM | Dexs | $1.20B | +6.19% | +7.98% |
| Binance Staked SOL | Liquid Staking | $1.14B | +8.91% | +4.12% |
| Jupiter Lend | Lending | $1.13B | +4.10% | +5.22% |
| Jito Liquid Staking | Liquid Staking | $1.09B | +4.89% | +7.08% |
| Jupiter Perpetual Exchange | Derivatives | $768.77M | +2.75% | +4.00% |
| Jupiter Staked SOL | Liquid Staking | $548.30M | +5.13% | +5.83% |
| Marinade Native | Staking Pool | $418.59M | +8.56% | +8.34% |
| Sentora Curator | Risk Curators | $368.11M | +12.06% | +14.47% |

## Stablecoins

Solana circulating pegged-USD: **$15.18B**
(1d -0.38% · 7d -3.99%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.68B | -0.31% |
| USDT · Tether | $2.14B | -8.53% |
| USDGO · USDGO | $1.38B | +0.36% |
| USD1 · World Liberty Financial USD | $1.32B | -0.00% |
| BUIDL · BlackRock USD | $993.29M | +0.01% |
| PYUSD · PayPal USD | $734.10M | +2.08% |
| USDG · Global Dollar | $619.37M | -0.85% |
| USDe · Ethena USDe | $522.47M | -0.22% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $237.63K (lower bound, not a census).
24h volume $97.62M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$568.98M** across 17 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $303.70M
- **Huma Finance V2** (RWA) — $193.28M
- **Plume Vaults** (RWA) — $28.12M
- **Ondo Global Markets** (RWA) — $26.58M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $2.84M
- **VNX** (RWA) — $2.76M
- **Oro Finance** (RWA) — $2.50M

## Daily active addresses

857,896 (Allium, as of 2026-09-17). Provider range 409,337–857,896. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — solana.com/news · Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — solana.com/news · Mon, 14 Sep 2026 11:00:00 GMT
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) — solana.com/news · Thu, 10 Sep 2026 20:16:00 GMT
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) — solana.com/news · Thu, 10 Sep 2026 20:16:00 GMT `mainnet`
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — solana.com/news · Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — solana.com/news · Mon, 07 Sep 2026 07:00:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-18 (2026-09-18 08:06:21 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=live, 200ms=pending. Observed mean slot ~268 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `on-chain` — On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=live, 200ms=pending.
- `observed` — Observed mean slot ~268 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 158ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 147ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 120ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 197ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 148ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6682ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 302ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 104ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 215ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 747ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 71ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 64ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 998ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 199ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 420ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 145ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 160ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 416ms https://solana.com/data
- `solana.com.databricks` [ok] 200 157ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 370ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 112ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 94ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 93ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 260ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 370ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 132ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 160ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 119ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 1481ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2284ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 3421ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 2164ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 424ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 254ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 147ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 135ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 177ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 288ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 155ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 139ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 266ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 236ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 221ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 250ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 287ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 234ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 198ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 231ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 154ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 239ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 260ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 270ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 218ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 328ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 240ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 203ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 212ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 198ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 205ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 187ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 174ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 187ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 233ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 176ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1720ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1618ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1341ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1694ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 911ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 988ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 3825ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1487ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.WGSx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.METCx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.INDIx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WRLDx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.QUBTx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.circ.METCx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.price.PCTx` [ok] 200 565ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.QUBTx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.price.FLNCx` [ok] 200 663ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.circ.WRLDx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.price.XRXx` [ok] 200 800ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.mult.WRLDx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.PCTx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.price.BETRx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.AIx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.INDIx` [ok] 200 871ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.AAONx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.mult.XRXx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.BETRx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.AAONx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.price.SCIx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.price.DRSx` [ok] 200 522ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.mult.AIx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.BETRx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.SAILx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.circ.SCIx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.circ.DRSx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 929ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.BSYx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.circ.SAILx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.MPx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.mult.PCTx` [ok] 200 1197ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.price.GSATx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.mult.SCIx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.DVAx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.price.DCIx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.mult.SAILx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.circ.MPx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.circ.BSYx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.price.RYANx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.circ.DVAx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.price.GDDYx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.mult.MPx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.mult.DVAx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.circ.RYANx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.mult.AAONx` [ok] 200 1485ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.circ.GDDYx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.mult.RYANx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.mult.BSYx` [ok] 200 571ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.price.BXPx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.price.FRHCx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.price.DYx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.price.AMx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.BXPx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.mult.GDDYx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.mult.DCIx` [ok] 200 507ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.circ.GSATx` [ok] 200 1078ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.circ.FRHCx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.mult.BXPx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.price.ALSNx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.mult.GSATx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.mult.AMx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.price.WMSx` [ok] 200 598ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.circ.ALSNx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.price.SMTCx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.circ.WMSx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.mult.ALSNx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.circ.SMTCx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.price.AXSMx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.price.SFx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.price.EGPx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.price.BPOPx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.mult.SMTCx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.price.FDSx` [ok] 200 862ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.mult.WMSx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.circ.SFx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.price.TTMIx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.circ.BPOPx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.price.AEISx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.mult.BPOPx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.circ.DYx` [ok] 200 1501ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.circ.TTMIx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.mult.SFx` [ok] 200 824ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.circ.FDSx` [ok] 200 882ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.mult.TTMIx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.KTOSx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.price.DPZx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.mult.FDSx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.price.HRLx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.circ.KTOSx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.circ.EGPx` [ok] 200 1210ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.price.PAGx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.circ.DPZx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.circ.AEISx` [ok] 200 1012ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.circ.HRLx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.price.SEICx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.mult.EGPx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.PAGx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.mult.AEISx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.mult.HRLx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.circ.SEICx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.price.HIIx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.mult.PAGx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.mult.DPZx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.price.EHCx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.price.GFLx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.price.ARx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.price.MGMx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.circ.HIIx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.mult.KTOSx` [ok] 200 771ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.circ.EHCx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.circ.GFLx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.circ.ARx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.mult.EHCx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.GFLx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.price.DOCUx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.mult.HIIx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.circ.MGMx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.price.HALOx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.mult.SEICx` [ok] 200 800ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.mult.MGMx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.price.AFGx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.circ.HALOx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.price.HUBSx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.circ.AXSMx` [ok] 200 2745ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.price.AMKRx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.mult.ARx` [ok] 200 661ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.circ.DOCUx` [ok] 200 567ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.circ.HUBSx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.circ.AMKRx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.price.WTRGx` [ok] 200 747ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.mult.DOCUx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.mult.HUBSx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.price.GMEDx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.circ.WTRGx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.mult.HALOx` [ok] 200 602ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.circ.GMEDx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.mult.AFGx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.price.OCx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.mult.AMKRx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.price.BMRNx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.price.CRx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.circ.OCx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.price.JEFx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.circ.BMRNx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.circ.CRx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.price.IESCx` [ok] 200 778ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.mult.OCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 670ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.price.JKHYx` [ok] 200 989ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.BMRNx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.circ.IESCx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.mult.CRx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.price.FIVEx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.circ.JEFx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.circ.JKHYx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.price.ITx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.price.MDGLx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.mult.JEFx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.mult.JKHYx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.price.AMHx` [ok] 200 604ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.MDGLx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.price.UHALx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.circ.AMHx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.price.VNOMx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.mult.IESCx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.mult.MDGLx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.circ.ITx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.circ.UHALx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.circ.FIVEx` [ok] 200 668ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.circ.VNOMx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.price.AHRx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.mult.AXSMx` [ok] 200 2251ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.mult.UHALx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.price.IVZx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.price.CORTx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.circ.AHRx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.mult.FIVEx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.price.STRLx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.price.NWSAx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.circ.CORTx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.circ.IVZx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.mult.AHRx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.circ.STRLx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.mult.CORTx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.mult.IVZx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.mult.VNOMx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.Hx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.price.AURx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.mult.STRLx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.mult.ITx` [ok] 200 822ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.circ.Hx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.price.GWREx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.price.MANHx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.price.NWSx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.price.CACIx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.circ.NWSAx` [ok] 200 618ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.price.ARWRx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.circ.GWREx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.mult.Hx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.circ.MANHx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.circ.CACIx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.circ.ARWRx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.price.BAXx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.mult.NWSAx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.mult.MANHx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.circ.AURx` [ok] 200 635ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.circ.NWSx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.price.TXRHx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/TXRHx/price-data
- `xstocks.mult.AURx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.circ.BAXx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.NWSx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.price.RVTYx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/RVTYx/price-data
- `xstocks.mult.BAXx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.ARWRx` [ok] 200 641ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.circ.TXRHx` [ok] 200 1146ms https://api.backed.fi/api/v2/public/assets/TXRHx/circulating-supply?format=object
- `xstocks.mult.TXRHx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/TXRHx/multiplier?network=Solana
- `xstocks.circ.RVTYx` [ok] 200 1995ms https://api.backed.fi/api/v2/public/assets/RVTYx/circulating-supply?format=object
- `xstocks.mult.RVTYx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/RVTYx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 193ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 374ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.QUBTx` [ok] 200 101ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.INDIx` [ok] 200 133ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.WRLDx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.BETRx` [ok] 200 116ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.XRXx` [ok] 200 120ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.WGSx` [ok] 200 93ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.AIx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.FLNCx` [ok] 200 135ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jito.tip_floor` [ok] 200 155ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 366ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 141ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 126ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 122ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 130ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 121ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 229ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
