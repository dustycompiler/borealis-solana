# Borealis — Solana ecosystem report

**Generated** 2026-09-23T18:25:50Z · 2026-09-23 11:25:50 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-23T18:25:41Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h -3.43%; DEX 24h $3.20B · 1d -7% · vs-7d-ago +18%; slot 267 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +24.54%. (threshold: `|7d %| >= 20`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -3.43%, DeFiLlama TVL 1d -0.99%, DEX 1d -6.82%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **INFO · TPS vs 30d median (solana.com/data tx/86400)** — Current 4,867.60 TPS is +22.1% vs 30d median 3,984.94 TPS (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 449,783,924 |
| Block height | 427,824,131 |
| Block time | 2026-09-23T18:25:41Z |
| Epoch | 1,041 (16.65% · slot 71,925/432,000) |
| Mean TPS (last ~3,600s) | 4,867.6 |
| Mean non-vote TPS | 2,345.3 |
| Median TPS (same window) | 4,870.7 |
| Mean slot time | 266.5 ms |
| Median slot time | 265.5 ms |
| Transaction count (cluster) | 551,801,405,174 |
| Circulating supply | 587,577,929 SOL |
| Total supply | 634,609,051 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,727,513 SOL |
| Delinquent stake | 236,623.47 SOL (0.054%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.40% / 35.68% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.84M SOL | 4.06% | 7% | 0 |
| 2 | `HEL1USMZ…` | 15.84M SOL | 3.60% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.36M SOL | 2.81% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.26M SOL | 2.56% | 5% | 0 |
| 5 | `E1r4Psq8…` | 10.34M SOL | 2.35% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.23M SOL | 2.10% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.16M SOL | 2.08% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.60M SOL | 1.73% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.09M SOL | 1.61% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.56M SOL | 1.49% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.22M SOL | 1.42% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.13M SOL | 1.39% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.35% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.61M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `6DTkuiey…` · 89.15K SOL · commission 100% · lag 449783924 slots
- `HDRqPft5…` · 71.15K SOL · commission 100% · lag 449783924 slots
- `3PZSgErg…` · 36.93K SOL · commission 0% · lag 69994 slots
- `t23p8aBQ…` · 14.37K SOL · commission 0% · lag 2188688 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 52928 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 985214 slots
- `mrgn4atx…` · 2.21K SOL · commission 0% · lag 1186519 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 1909172 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 1291053 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 1021549 slots
- `R1parD2C…` · 2.87 SOL · commission 5% · lag 65735054 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 204415 slots

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
| **In-protocol fees 24h** | **$1.08M** (9,224.4 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-21 |
| **Solana REV** | **11,259.0 SOL** / **$1.32M** | MEASURED UTC calendar day 2026-09-21: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-21 · UTC day 2026-09-21 · SOL-USD date 2026-09-21 |
| Jito tip-floor run-rate (NOT REV) | $332.99K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 332987 USD; at p95 floor → 25114176 USD. |
| Protocol fees 24h | $17.87M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $114.03 | coingecko.simple_price |
| 24h change | -3.43% | coingecko.simple_price |
| Market cap | $67.00B | coingecko.simple_price |
| 24h volume | $5.31B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.39B |
| TVL 1d / 7d / 30d | -0.99% / +11.70% / +14.72% |
| DEX volume 24h | $3.20B · 1d -6.82% · vs-7d-ago +18.18% |
| 7d DEX volume | $21.22B · +17.10% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $17.87M |
| Fees 1d / 7d | -4.10% / +24.54% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $634.15M | +62.55% |
| Raydium AMM | $398.81M | -30.42% |
| BisonFi | $368.17M | -17.60% |
| Orca DEX | $365.06M | -19.42% |
| Meteora DLMM | $266.83M | +2.78% |
| fomo Wallet | $156.29M | -2.53% |
| Scorch | $129.41M | -14.10% |
| Manifest Trade | $128.76M | -7.08% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.82B | -1.98% | +18.04% |
| Kamino Lend | Lending | $1.40B | -1.89% | +5.43% |
| Raydium AMM | Dexs | $1.31B | -1.34% | +19.71% |
| Jito Liquid Staking | Liquid Staking | $1.19B | -1.93% | +18.33% |
| Binance Staked SOL | Liquid Staking | $1.17B | -1.68% | +16.95% |
| Jupiter Lend | Lending | $1.17B | +0.23% | +11.15% |
| Jupiter Perpetual Exchange | Derivatives | $801.50M | -1.52% | +10.07% |
| Jupiter Staked SOL | Liquid Staking | $593.82M | -1.59% | +18.39% |
| Marinade Native | Staking Pool | $440.46M | -1.32% | +19.14% |
| PumpSwap | Dexs | $373.97M | -1.50% | +17.63% |

## Stablecoins

Solana circulating pegged-USD: **$15.86B**
(1d -1.71% · 7d +5.79%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.29B | -12.03% |
| USDT · Tether | $2.14B | +0.00% |
| USDGO · USDGO | $1.42B | +1.00% |
| USD1 · World Liberty Financial USD | $1.37B | +1.42% |
| BUIDL · BlackRock USD | $987.68M | -0.58% |
| PYUSD · PayPal USD | $734.18M | +0.39% |
| USDG · Global Dollar | $630.96M | +1.66% |
| USDe · Ethena USDe | $497.45M | -0.92% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 10 of 500 Solana-deployed listed symbols (multiplier ok 79/80; 500 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 500 · Solana deployments 500 · priced 10 · priced-subset mcap $107.60K (lower bound, not a census).
24h volume $132.40M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 79 / mcap_computable 10 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 500 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 500 unique underlyings among 500 Solana rows; not every tokenized equity on Solana). 500 of 500 listed xStocks have a Solana deployment (500 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$545.47M** across 16 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $303.05M
- **Huma Finance V2** (RWA) — $197.03M
- **Plume Vaults** (RWA) — $28.20M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $2.99M
- **VNX** (RWA) — $2.70M
- **Oro Finance** (RWA) — $2.49M
- **International Stable Currency** (RWA) — $2.44M

## Daily active addresses

867,560 (Allium, as of 2026-09-22). Provider range 489,457–892,240. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — solana.com/news · Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — solana.com/news · Sat, 19 Sep 2026 11:28:00 GMT `mainnet`
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — solana.com/news · Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — solana.com/news · Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — solana.com/news · Mon, 14 Sep 2026 11:00:00 GMT
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) — solana.com/news · Thu, 10 Sep 2026 20:16:00 GMT
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) — solana.com/news · Thu, 10 Sep 2026 20:16:00 GMT `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-23 (2026-09-23 11:25:50 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=live, 200ms=pending. Observed mean slot ~266 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~266 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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
- **xStocks** — priced up to 80 of 500 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.
- **xStocks** — SNDRx multiplier missing — mcap omitted (never assumed 1.0)

## Sources this run

- `rpc.getHealth` [ok] 200 124ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 51ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 67ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 70ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 130ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6362ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 137ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 110ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 113ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 68ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 26ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 30ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 41ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 67ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 72ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 57ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 87ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 247ms https://solana.com/data
- `solana.com.databricks` [ok] 200 102ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 400ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 182ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 46ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 72ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 255ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 188ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 55ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 59ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 52ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 3027ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1522ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1203ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1326ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 171ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 92ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 30ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 35ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 54ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 112ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 104ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 107ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 115ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 490ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 122ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 164ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 191ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 215ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 192ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 146ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 56ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 165ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 156ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 167ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 119ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 232ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 105ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 139ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 77ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 148ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 110ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 134ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 102ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 113ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 152ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 100ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1639ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2209ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2452ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1289ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1962ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [FAIL] 500 11768ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5 — HTTP 500 Internal Server Error
- `xstocks.price.INDIx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.XRXx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.FLNCx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.WGSx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.QUBTx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.METCx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.XRXx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.price.PCTx` [ok] 200 845ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.mult.QUBTx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.circ.FLNCx` [ok] 200 844ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.WRLDx` [ok] 200 1121ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.WYFIx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.XRXx` [ok] 200 699ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 548ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.BETRx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.METCx` [ok] 200 1112ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.AIx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.BETRx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 1576ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.price.MIDDx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data
- `xstocks.mult.BETRx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 734ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.MIDDx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object
- `xstocks.price.RITMx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data
- `xstocks.mult.AIx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.SHCx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data
- `xstocks.mult.FLNCx` [ok] 200 1310ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.ALMx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data
- `xstocks.price.RNGx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data
- `xstocks.mult.MIDDx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana
- `xstocks.circ.RNGx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object
- `xstocks.circ.SHCx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object
- `xstocks.price.REYNx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data
- `xstocks.circ.ALMx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object
- `xstocks.price.VSNTx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data
- `xstocks.price.WHx` [ok] 200 646ms https://api.backed.fi/api/v2/public/assets/WHx/price-data
- `xstocks.mult.RNGx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana
- `xstocks.mult.SHCx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana
- `xstocks.price.OZKx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data
- `xstocks.price.CARx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/CARx/price-data
- `xstocks.mult.ALMx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana
- `xstocks.circ.OZKx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object
- `xstocks.circ.CARx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object
- `xstocks.price.IRDMx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data
- `xstocks.mult.CARx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana
- `xstocks.mult.OZKx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana
- `xstocks.circ.REYNx` [ok] 200 1202ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object
- `xstocks.price.FBINx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data
- `xstocks.price.GXOx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data
- `xstocks.mult.REYNx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana
- `xstocks.price.AMTMx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data
- `xstocks.circ.AMTMx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object
- `xstocks.circ.GXOx` [ok] 200 1032ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object
- `xstocks.mult.AMTMx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana
- `xstocks.price.MTNx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data
- `xstocks.mult.GXOx` [ok] 200 570ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana
- `xstocks.price.PSNx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data
- `xstocks.circ.MTNx` [ok] 200 1280ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object
- `xstocks.mult.MTNx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana
- `xstocks.price.PEGAx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data
- `xstocks.circ.WRLDx` [FAIL] 500 10599ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object — HTTP 500 Internal Server Error
- `xstocks.mult.WRLDx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.SAICx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data
- `xstocks.circ.RITMx` [FAIL] 500 10557ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object — HTTP 500 Internal Server Error
- `xstocks.circ.VSNTx` [FAIL] 500 10264ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object — HTTP 500 Internal Server Error
- `xstocks.mult.VSNTx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana
- `xstocks.mult.RITMx` [ok] 200 874ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana
- `xstocks.price.EXLSx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data
- `xstocks.circ.WHx` [FAIL] 500 10831ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object — HTTP 500 Internal Server Error
- `xstocks.circ.EXLSx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object
- `xstocks.mult.WHx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana
- `xstocks.circ.IRDMx` [FAIL] 500 10297ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object — HTTP 500 Internal Server Error
- `xstocks.price.EPAMx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data
- `xstocks.price.CRUSx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data
- `xstocks.circ.EPAMx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object
- `xstocks.circ.CRUSx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object
- `xstocks.circ.FBINx` [FAIL] 500 10251ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object — HTTP 500 Internal Server Error
- `xstocks.mult.EXLSx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana
- `xstocks.circ.SAICx` [ok] 200 2297ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object
- `xstocks.mult.CRUSx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana
- `xstocks.mult.EPAMx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana
- `xstocks.mult.FBINx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana
- `xstocks.price.Mx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/Mx/price-data
- `xstocks.price.SNDRx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data
- `xstocks.mult.IRDMx` [ok] 200 779ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana
- `xstocks.price.ELFx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data
- `xstocks.circ.ELFx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object
- `xstocks.price.EXPx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data
- `xstocks.price.VNOx` [ok] 200 428ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data
- `xstocks.mult.SAICx` [ok] 200 847ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana
- `xstocks.mult.ELFx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana
- `xstocks.circ.VNOx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object
- `xstocks.price.VIRTx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data
- `xstocks.price.MKTXx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data
- `xstocks.mult.VNOx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana
- `xstocks.circ.SNDRx` [ok] 200 954ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object
- `xstocks.circ.MKTXx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object
- `xstocks.circ.Mx` [ok] 200 1278ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object
- `xstocks.price.HXLx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data
- `xstocks.circ.EXPx` [ok] 200 1081ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object
- `xstocks.mult.Mx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana
- `xstocks.circ.HXLx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object
- `xstocks.mult.MKTXx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana
- `xstocks.circ.PSNx` [ok] 200 10376ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object
- `xstocks.price.CPBx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data
- `xstocks.circ.VIRTx` [ok] 200 1130ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object
- `xstocks.circ.CPBx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object
- `xstocks.mult.EXPx` [ok] 200 778ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana
- `xstocks.mult.HXLx` [ok] 200 702ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana
- `xstocks.price.VFCx` [ok] 200 696ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data
- `xstocks.price.NXSTx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data
- `xstocks.mult.PSNx` [ok] 200 836ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana
- `xstocks.price.ADTx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data
- `xstocks.mult.VIRTx` [ok] 200 824ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana
- `xstocks.price.BCx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/BCx/price-data
- `xstocks.mult.CPBx` [ok] 200 697ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana
- `xstocks.circ.ADTx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object
- `xstocks.price.ACIx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data
- `xstocks.price.KRMNx` [ok] 200 422ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data
- `xstocks.circ.ACIx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object
- `xstocks.mult.ADTx` [ok] 200 755ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana
- `xstocks.mult.ACIx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana
- `xstocks.price.GTESx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data
- `xstocks.price.HRBx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data
- `xstocks.circ.PEGAx` [ok] 200 11779ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object
- `xstocks.mult.PEGAx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana
- `xstocks.price.AXSx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data
- `xstocks.circ.AXSx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object
- `xstocks.mult.AXSx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana
- `xstocks.price.DLBx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data
- `xstocks.circ.DLBx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object
- `xstocks.mult.DLBx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana
- `xstocks.price.RYNx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data
- `xstocks.circ.RYNx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object
- `xstocks.mult.RYNx` [ok] 200 665ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana
- `xstocks.price.POOLx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data
- `xstocks.circ.POOLx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object
- `xstocks.mult.POOLx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana
- `xstocks.price.TFXx` [ok] 200 594ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data
- `xstocks.circ.TFXx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object
- `xstocks.mult.TFXx` [ok] 200 760ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana
- `xstocks.price.LWx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/LWx/price-data
- `xstocks.circ.LWx` [ok] 200 691ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object
- `xstocks.mult.SNDRx` [FAIL] 500 10603ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana — HTTP 500 Internal Server Error
- `xstocks.mult.LWx` [ok] 200 454ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana
- `xstocks.price.SONx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/SONx/price-data
- `xstocks.price.AAONx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.circ.AAONx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.circ.BCx` [ok] 200 9897ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object
- `xstocks.mult.AAONx` [ok] 200 507ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.mult.BCx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana
- `xstocks.circ.NXSTx` [ok] 200 10641ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object
- `xstocks.price.INGMx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data
- `xstocks.circ.VFCx` [ok] 200 10984ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object
- `xstocks.price.TTDx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data
- `xstocks.circ.KRMNx` [ok] 200 10144ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object
- `xstocks.mult.VFCx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana
- `xstocks.mult.NXSTx` [ok] 200 941ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana
- `xstocks.mult.KRMNx` [ok] 200 647ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana
- `xstocks.circ.HRBx` [FAIL] 500 10257ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object — HTTP 500 Internal Server Error
- `xstocks.price.HRx` [ok] 200 694ms https://api.backed.fi/api/v2/public/assets/HRx/price-data
- `xstocks.circ.GTESx` [FAIL] 500 10527ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object — HTTP 500 Internal Server Error
- `xstocks.price.CLFx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data
- `xstocks.price.RLIx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data
- `xstocks.mult.GTESx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana
- `xstocks.mult.HRBx` [ok] 200 722ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana
- `xstocks.price.STWDx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data
- `xstocks.circ.RLIx` [ok] 200 653ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object
- `xstocks.price.MSMx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data
- `xstocks.circ.CLFx` [ok] 200 1466ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object
- `xstocks.circ.HRx` [ok] 200 1791ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object
- `xstocks.mult.RLIx` [ok] 200 977ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana
- `xstocks.mult.CLFx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana
- `xstocks.price.CZRx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data
- `xstocks.price.OMFx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data
- `xstocks.circ.STWDx` [ok] 200 1359ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object
- `xstocks.circ.OMFx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object
- `xstocks.circ.MSMx` [ok] 200 1227ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object
- `xstocks.mult.HRx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana
- `xstocks.price.CROXx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data
- `xstocks.mult.MSMx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana
- `xstocks.mult.OMFx` [ok] 200 548ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana
- `xstocks.mult.STWDx` [ok] 200 666ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana
- `xstocks.price.CHEx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data
- `xstocks.price.Gx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/Gx/price-data
- `xstocks.price.ALGMx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data
- `xstocks.circ.Gx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object
- `xstocks.circ.CZRx` [ok] 200 1200ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object
- `xstocks.circ.ALGMx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object
- `xstocks.mult.Gx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana
- `xstocks.mult.CZRx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana
- `xstocks.price.MTGx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data
- `xstocks.mult.ALGMx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana
- `xstocks.price.BEPCx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data
- `xstocks.price.MTDRx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data
- `xstocks.circ.BEPCx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object
- `xstocks.circ.MTGx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object
- `xstocks.circ.MTDRx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object
- `xstocks.mult.BEPCx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana
- `xstocks.mult.MTDRx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana
- `xstocks.mult.MTGx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana
- `xstocks.price.LYFTx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data
- `xstocks.price.INGRx` [ok] 200 522ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data
- `xstocks.circ.CHEx` [ok] 200 1972ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object
- `xstocks.price.BYDx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data
- `xstocks.circ.BYDx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object
- `xstocks.circ.LYFTx` [ok] 200 561ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object
- `xstocks.mult.CHEx` [ok] 200 638ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana
- `xstocks.circ.INGRx` [ok] 200 762ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object
- `xstocks.mult.BYDx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana
- `xstocks.price.FNBx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data
- `xstocks.mult.LYFTx` [ok] 200 647ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana
- `xstocks.price.STAGx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data
- `xstocks.circ.FNBx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object
- `xstocks.price.MBGLx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data
- `xstocks.mult.FNBx` [ok] 200 406ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana
- `xstocks.price.CACCx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data
- `xstocks.circ.STAGx` [ok] 200 681ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object
- `xstocks.mult.INGRx` [ok] 200 1168ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana
- `xstocks.circ.CACCx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object
- `xstocks.mult.STAGx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana
- `xstocks.mult.CACCx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana
- `xstocks.circ.SONx` [ok] 200 10002ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object
- `xstocks.circ.MBGLx` [ok] 200 1537ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object
- `xstocks.mult.SONx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana
- `xstocks.circ.TTDx` [ok] 200 9602ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object
- `xstocks.mult.MBGLx` [ok] 200 930ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana
- `xstocks.mult.TTDx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana
- `xstocks.circ.INGMx` [ok] 200 10343ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object
- `xstocks.mult.INGMx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana
- `xstocks.circ.CROXx` [ok] 200 8332ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object
- `xstocks.mult.CROXx` [ok] 200 1217ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 590ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 352ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.XRXx` [ok] 200 44ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 58ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.QUBTx` [ok] 200 51ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.FLNCx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.WGSx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.AIx` [ok] 200 59ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.WYFIx` [ok] 200 45ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.INDIx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jito.tip_floor` [ok] 200 384ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 251ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 60ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 97ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 51ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 41ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 50ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 224ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
