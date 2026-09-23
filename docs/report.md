# Borealis — Solana ecosystem report

**Generated** 2026-09-23T20:01:19Z · 2026-09-23 13:01:19 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-23T20:01:10Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h -3.04%; DEX 24h $3.20B · 1d -7% · vs-7d-ago +18%; slot 265 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +24.54%. (threshold: `|7d %| >= 20`)
- **WARN · Last TPS sample outside 2.5σ of the 60-sample window** — Last sample 5,474 TPS is +3.09σ vs window mean 4,700 (n=60, σ=250). (threshold: `|last sample − window mean| > 2.5σ`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -3.04%, DeFiLlama TVL 1d -1.11%, DEX 1d -6.82%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 449,805,532 |
| Block height | 427,845,722 |
| Block time | 2026-09-23T20:01:10Z |
| Epoch | 1,041 (21.65% · slot 93,532/432,000) |
| Mean TPS (last ~3,600s) | 4,700.5 |
| Mean non-vote TPS | 2,170.5 |
| Median TPS (same window) | 4,678.6 |
| Mean slot time | 265.4 ms |
| Median slot time | 264.9 ms |
| Transaction count (cluster) | 551,828,250,190 |
| Circulating supply | 587,577,858 SOL |
| Total supply | 634,608,981 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 674 |
| Delinquent | 13 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,595,969 SOL |
| Delinquent stake | 368,167.60 SOL (0.084%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.40% / 35.69% |
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

- `CjmXSapt…` · 131.54K SOL · commission 0% · lag 4347 slots
- `6DTkuiey…` · 89.15K SOL · commission 100% · lag 449805532 slots
- `HDRqPft5…` · 71.15K SOL · commission 100% · lag 449805532 slots
- `3PZSgErg…` · 36.93K SOL · commission 0% · lag 91602 slots
- `t23p8aBQ…` · 14.37K SOL · commission 0% · lag 2210296 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 74536 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 1006822 slots
- `mrgn4atx…` · 2.21K SOL · commission 0% · lag 1208127 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 1930780 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 1312661 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 1043157 slots
- `R1parD2C…` · 2.87 SOL · commission 5% · lag 65756662 slots

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
| **In-protocol fees 24h** | **$1.09M** (9,201.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-22 |
| **Solana REV** | **11,385.8 SOL** / **$1.34M** | MEASURED UTC calendar day 2026-09-22: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-22 · UTC day 2026-09-22 · SOL-USD date 2026-09-22 |
| Jito tip-floor run-rate (NOT REV) | $72.67K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 72668 USD; at p95 floor → 2149306 USD. |
| Protocol fees 24h | $17.87M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $114.61 | coingecko.simple_price |
| 24h change | -3.04% | coingecko.simple_price |
| Market cap | $67.35B | coingecko.simple_price |
| 24h volume | $5.20B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.39B |
| TVL 1d / 7d / 30d | -1.11% / +11.57% / +14.59% |
| DEX volume 24h | $3.20B · 1d -6.82% · vs-7d-ago +18.18% |
| 7d DEX volume | $21.22B · +17.10% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $17.87M |
| Fees 1d / 7d | -4.10% / +24.54% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $634.15M | +62.55% |
| Raydium AMM | $406.22M | -29.13% |
| BisonFi | $368.17M | -17.60% |
| Orca DEX | $365.06M | -19.42% |
| Meteora DLMM | $266.83M | +2.78% |
| fomo Wallet | $156.29M | -2.53% |
| Scorch | $129.41M | -14.10% |
| Manifest Trade | $125.55M | -9.40% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.84B | -2.02% | +19.29% |
| Kamino Lend | Lending | $1.40B | -2.35% | +5.51% |
| Raydium AMM | Dexs | $1.31B | -1.34% | +19.71% |
| Jito Liquid Staking | Liquid Staking | $1.18B | -2.21% | +18.06% |
| Jupiter Lend | Lending | $1.17B | -0.55% | +10.99% |
| Binance Staked SOL | Liquid Staking | $1.17B | -3.18% | +16.29% |
| Jupiter Perpetual Exchange | Derivatives | $799.93M | -2.23% | +9.73% |
| Jupiter Staked SOL | Liquid Staking | $591.70M | -3.08% | +17.72% |
| Marinade Native | Staking Pool | $438.84M | -2.69% | +18.46% |
| PumpSwap | Dexs | $373.97M | -1.50% | +17.63% |

## Stablecoins

Solana circulating pegged-USD: **$15.87B**
(1d -1.71% · 7d +5.80%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.29B | -12.03% |
| USDT · Tether | $2.14B | +0.00% |
| USDGO · USDGO | $1.42B | +1.00% |
| USD1 · World Liberty Financial USD | $1.38B | +2.16% |
| BUIDL · BlackRock USD | $987.68M | -0.58% |
| PYUSD · PayPal USD | $733.88M | +0.35% |
| USDG · Global Dollar | $631.24M | +1.71% |
| USDe · Ethena USDe | $497.46M | -0.92% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 1 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 1 · priced-subset mcap $11.10K (lower bound, not a census).
24h volume $131.82M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 1 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$545.52M** across 16 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $303.06M
- **Huma Finance V2** (RWA) — $197.04M
- **Plume Vaults** (RWA) — $28.21M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $2.98M
- **VNX** (RWA) — $2.70M
- **Oro Finance** (RWA) — $2.49M
- **International Stable Currency** (RWA) — $2.47M

## Daily active addresses

867,560 (Allium, as of 2026-09-22). Provider range 489,457–895,781. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

_As of 2026-09-23 (2026-09-23 13:01:19 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=live, 200ms=pending. Observed mean slot ~265 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~265 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 143ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 78ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 141ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 79ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 181ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7061ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 489ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 45ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 74ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 67ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 43ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 39ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1222ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 86ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 70ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 77ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 104ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 340ms https://solana.com/data
- `solana.com.databricks` [ok] 200 1119ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 730ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 199ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 68ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 113ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 282ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 211ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 98ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 100ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 100ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 2789ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1126ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1131ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 671ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 292ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 48ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 186ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 106ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 206ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 127ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 121ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 231ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 275ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 434ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 271ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 261ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 177ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 230ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 204ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 261ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 119ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 297ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 188ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 163ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 192ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 250ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 256ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 182ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 152ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 285ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 142ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 264ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 247ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 243ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 136ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 236ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 5687ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 3408ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 4827ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 5199ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 8131ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2939ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 4389ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 2536ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.FLNCx` [ok] 200 11407ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.XRXx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METCx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/METCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WRLDx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.QUBTx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WGSx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.INDIx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PCTx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.FLNCx` [ok] 200 2133ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 1657ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 1687ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.PCTx` [ok] 200 1895ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 2024ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 2114ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 2156ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 769ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 863ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 953ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 1316ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 3026ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 955ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 792ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 1896ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 2764ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.WYFIx` [FAIL]  12014ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BETRx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AIx` [FAIL]  12029ms https://api.backed.fi/api/v2/public/assets/AIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MIDDx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ALMx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BETRx` [ok] 200 848ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.RITMx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.RNGx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WYFIx` [ok] 200 1872ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.BETRx` [ok] 200 1051ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.SHCx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AIx` [ok] 200 1946ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 1151ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.ALMx` [ok] 200 2227ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object
- `xstocks.circ.MIDDx` [ok] 200 2461ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object
- `xstocks.circ.RITMx` [ok] 200 2043ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object
- `xstocks.circ.RNGx` [ok] 200 1917ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 1136ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.ALMx` [ok] 200 928ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana
- `xstocks.mult.MIDDx` [ok] 200 965ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana
- `xstocks.mult.RNGx` [ok] 200 867ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana
- `xstocks.mult.RITMx` [ok] 200 1778ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana
- `xstocks.circ.SHCx` [ok] 200 3701ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object
- `xstocks.mult.SHCx` [ok] 200 868ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana
- `xstocks.price.FBINx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data
- `xstocks.circ.FBINx` [ok] 200 1919ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object
- `xstocks.mult.FBINx` [ok] 200 898ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana
- `xstocks.price.WHx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/WHx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.REYNx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.VSNTx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WHx` [ok] 200 1705ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object
- `xstocks.price.CARx` [FAIL]  12029ms https://api.backed.fi/api/v2/public/assets/CARx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.OZKx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.IRDMx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.REYNx` [ok] 200 1957ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object
- `xstocks.circ.VSNTx` [ok] 200 1676ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object
- `xstocks.price.GXOx` [FAIL]  12016ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.WHx` [ok] 200 1822ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana
- `xstocks.circ.CARx` [ok] 200 1871ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object
- `xstocks.circ.OZKx` [ok] 200 2040ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object
- `xstocks.circ.IRDMx` [ok] 200 1676ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object
- `xstocks.mult.VSNTx` [ok] 200 1304ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana
- `xstocks.mult.REYNx` [ok] 200 1870ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana
- `xstocks.mult.CARx` [ok] 200 1393ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana
- `xstocks.circ.GXOx` [ok] 200 2141ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object
- `xstocks.mult.OZKx` [ok] 200 1528ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana
- `xstocks.mult.IRDMx` [ok] 200 1811ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana
- `xstocks.price.EXLSx` [ok] 200 786ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data
- `xstocks.mult.GXOx` [ok] 200 1240ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana
- `xstocks.price.AMTMx` [FAIL]  12015ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.EXLSx` [ok] 200 2089ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object
- `xstocks.circ.AMTMx` [ok] 200 2045ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object
- `xstocks.mult.EXLSx` [ok] 200 1825ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana
- `xstocks.mult.AMTMx` [ok] 200 1780ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana
- `xstocks.price.MTNx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PSNx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PEGAx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SAICx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.EPAMx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MTNx` [ok] 200 2509ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object
- `xstocks.circ.PSNx` [ok] 200 1795ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object
- `xstocks.price.CRUSx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.PEGAx` [ok] 200 2421ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object
- `xstocks.circ.SAICx` [ok] 200 2216ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object
- `xstocks.mult.PSNx` [ok] 200 1216ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana
- `xstocks.circ.EPAMx` [ok] 200 2145ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object
- `xstocks.mult.PEGAx` [ok] 200 1054ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana
- `xstocks.circ.CRUSx` [ok] 200 1739ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object
- `xstocks.mult.SAICx` [ok] 200 1183ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana
- `xstocks.mult.MTNx` [ok] 200 2625ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana
- `xstocks.mult.EPAMx` [ok] 200 902ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana
- `xstocks.price.VIRTx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data
- `xstocks.mult.CRUSx` [ok] 200 946ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana
- `xstocks.price.Mx` [ok] 200 11145ms https://api.backed.fi/api/v2/public/assets/Mx/price-data
- `xstocks.price.HXLx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data
- `xstocks.price.MKTXx` [ok] 200 1573ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data
- `xstocks.price.ELFx` [ok] 200 11232ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data
- `xstocks.circ.VIRTx` [ok] 200 2195ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object
- `xstocks.circ.HXLx` [ok] 200 2552ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object
- `xstocks.mult.VIRTx` [ok] 200 760ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana
- `xstocks.circ.MKTXx` [ok] 200 1761ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object
- `xstocks.price.CPBx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data
- `xstocks.circ.Mx` [ok] 200 3401ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object
- `xstocks.circ.ELFx` [ok] 200 2034ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object
- `xstocks.mult.MKTXx` [ok] 200 1137ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana
- `xstocks.mult.Mx` [ok] 200 912ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana
- `xstocks.mult.ELFx` [ok] 200 804ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana
- `xstocks.price.NXSTx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data
- `xstocks.mult.HXLx` [ok] 200 1994ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana
- `xstocks.price.VFCx` [ok] 200 770ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data
- `xstocks.circ.CPBx` [ok] 200 2397ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object
- `xstocks.price.ADTx` [ok] 200 1166ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data
- `xstocks.price.BCx` [ok] 200 1219ms https://api.backed.fi/api/v2/public/assets/BCx/price-data
- `xstocks.mult.CPBx` [ok] 200 957ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana
- `xstocks.circ.NXSTx` [ok] 200 1936ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object
- `xstocks.price.ACIx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data
- `xstocks.circ.VFCx` [ok] 200 2341ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object
- `xstocks.circ.ADTx` [ok] 200 2039ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object
- `xstocks.circ.BCx` [ok] 200 1865ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object
- `xstocks.circ.ACIx` [ok] 200 1813ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object
- `xstocks.mult.VFCx` [ok] 200 1601ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana
- `xstocks.mult.ADTx` [ok] 200 1065ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana
- `xstocks.mult.BCx` [ok] 200 1376ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana
- `xstocks.price.KRMNx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data
- `xstocks.mult.NXSTx` [ok] 200 2715ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana
- `xstocks.price.GTESx` [ok] 200 711ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data
- `xstocks.price.VNOx` [ok] 200 10726ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data
- `xstocks.price.HRBx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data
- `xstocks.mult.ACIx` [ok] 200 1240ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana
- `xstocks.price.AXSx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data
- `xstocks.price.EXPx` [ok] 200 10661ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data
- `xstocks.price.DLBx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data
- `xstocks.price.SNDRx` [ok] 200 12019ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data
- `xstocks.circ.KRMNx` [ok] 200 1959ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object
- `xstocks.circ.VNOx` [ok] 200 1893ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object
- `xstocks.circ.AXSx` [ok] 200 1803ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object
- `xstocks.circ.EXPx` [ok] 200 1732ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object
- `xstocks.circ.HRBx` [ok] 200 2125ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object
- `xstocks.circ.DLBx` [ok] 200 2108ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object
- `xstocks.circ.GTESx` [ok] 200 2682ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object
- `xstocks.mult.KRMNx` [ok] 200 1199ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana
- `xstocks.mult.VNOx` [ok] 200 1127ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana
- `xstocks.mult.HRBx` [ok] 200 1167ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana
- `xstocks.circ.SNDRx` [ok] 200 2714ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object
- `xstocks.price.RYNx` [ok] 200 705ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data
- `xstocks.price.POOLx` [ok] 200 1050ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data
- `xstocks.mult.DLBx` [ok] 200 1445ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana
- `xstocks.mult.EXPx` [ok] 200 2338ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana
- `xstocks.mult.AXSx` [ok] 200 2407ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana
- `xstocks.price.TFXx` [ok] 200 1173ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data
- `xstocks.price.LWx` [ok] 200 764ms https://api.backed.fi/api/v2/public/assets/LWx/price-data
- `xstocks.mult.GTESx` [ok] 200 2175ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana
- `xstocks.price.SONx` [ok] 200 576ms https://api.backed.fi/api/v2/public/assets/SONx/price-data
- `xstocks.price.AAONx` [ok] 200 745ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.circ.RYNx` [ok] 200 2177ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object
- `xstocks.circ.POOLx` [ok] 200 1980ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object
- `xstocks.circ.TFXx` [ok] 200 2132ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object
- `xstocks.price.INGMx` [ok] 200 1804ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data
- `xstocks.mult.SNDRx` [ok] 200 3562ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana
- `xstocks.circ.SONx` [ok] 200 2181ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object
- `xstocks.circ.LWx` [ok] 200 2336ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object
- `xstocks.mult.RYNx` [ok] 200 1951ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana
- `xstocks.price.TTDx` [ok] 200 983ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data
- `xstocks.mult.TFXx` [ok] 200 1456ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana
- `xstocks.mult.POOLx` [ok] 200 2480ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana
- `xstocks.circ.INGMx` [ok] 200 1896ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object
- `xstocks.mult.LWx` [ok] 200 1604ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana
- `xstocks.circ.AAONx` [ok] 200 3774ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.mult.SONx` [ok] 200 1933ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana
- `xstocks.price.CLFx` [ok] 200 725ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data
- `xstocks.price.STWDx` [ok] 200 868ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data
- `xstocks.circ.TTDx` [ok] 200 1844ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object
- `xstocks.price.RLIx` [ok] 200 2095ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data
- `xstocks.price.MSMx` [ok] 200 1110ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data
- `xstocks.price.HRx` [ok] 200 2653ms https://api.backed.fi/api/v2/public/assets/HRx/price-data
- `xstocks.mult.INGMx` [ok] 200 1932ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana
- `xstocks.mult.AAONx` [ok] 200 1937ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.price.CZRx` [ok] 200 798ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data
- `xstocks.mult.TTDx` [ok] 200 1567ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana
- `xstocks.circ.CLFx` [ok] 200 2362ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object
- `xstocks.price.OMFx` [ok] 200 825ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data
- `xstocks.circ.STWDx` [ok] 200 2443ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object
- `xstocks.price.CROXx` [ok] 200 799ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data
- `xstocks.circ.HRx` [ok] 200 2107ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object
- `xstocks.circ.MSMx` [ok] 200 2432ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object
- `xstocks.mult.CLFx` [ok] 200 1430ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana
- `xstocks.circ.CZRx` [ok] 200 2213ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object
- `xstocks.circ.RLIx` [ok] 200 3444ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object
- `xstocks.price.CHEx` [ok] 200 871ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data
- `xstocks.mult.MSMx` [ok] 200 1483ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana
- `xstocks.circ.CROXx` [ok] 200 2177ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object
- `xstocks.mult.HRx` [ok] 200 1992ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana
- `xstocks.mult.STWDx` [ok] 200 2329ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana
- `xstocks.circ.OMFx` [ok] 200 2951ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object
- `xstocks.price.Gx` [ok] 200 774ms https://api.backed.fi/api/v2/public/assets/Gx/price-data
- `xstocks.mult.CZRx` [ok] 200 1563ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana
- `xstocks.price.ALGMx` [ok] 200 818ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data
- `xstocks.mult.RLIx` [ok] 200 1710ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana
- `xstocks.price.MTGx` [ok] 200 990ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data
- `xstocks.price.BEPCx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data
- `xstocks.mult.CROXx` [ok] 200 1578ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana
- `xstocks.mult.OMFx` [ok] 200 1561ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana
- `xstocks.price.INGRx` [ok] 200 662ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data
- `xstocks.price.MTDRx` [ok] 200 1322ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data
- `xstocks.circ.Gx` [ok] 200 1846ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object
- `xstocks.circ.CHEx` [ok] 200 2911ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object
- `xstocks.circ.ALGMx` [ok] 200 1908ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object
- `xstocks.price.LYFTx` [ok] 200 1085ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data
- `xstocks.circ.BEPCx` [ok] 200 2246ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object
- `xstocks.circ.MTGx` [ok] 200 2595ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object
- `xstocks.circ.LYFTx` [ok] 200 998ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object
- `xstocks.mult.CHEx` [ok] 200 1801ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana
- `xstocks.mult.ALGMx` [ok] 200 1617ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana
- `xstocks.circ.INGRx` [ok] 200 2298ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object
- `xstocks.mult.BEPCx` [ok] 200 1455ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana
- `xstocks.mult.Gx` [ok] 200 2512ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana
- `xstocks.price.BYDx` [ok] 200 746ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data
- `xstocks.circ.MTDRx` [ok] 200 2749ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object
- `xstocks.price.STAGx` [ok] 200 783ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data
- `xstocks.mult.MTGx` [ok] 200 1747ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana
- `xstocks.price.MBGLx` [ok] 200 660ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data
- `xstocks.price.FNBx` [ok] 200 984ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data
- `xstocks.price.CACCx` [ok] 200 786ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data
- `xstocks.mult.LYFTx` [ok] 200 2728ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana
- `xstocks.mult.MTDRx` [ok] 200 1879ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana
- `xstocks.circ.STAGx` [ok] 200 2450ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object
- `xstocks.circ.BYDx` [ok] 200 2710ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object
- `xstocks.circ.MBGLx` [ok] 200 2892ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object
- `xstocks.mult.INGRx` [ok] 200 4245ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana
- `xstocks.mult.STAGx` [ok] 200 1219ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana
- `xstocks.circ.FNBx` [ok] 200 3040ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object
- `xstocks.mult.BYDx` [ok] 200 1490ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana
- `xstocks.circ.CACCx` [ok] 200 3061ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object
- `xstocks.mult.MBGLx` [ok] 200 1235ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana
- `xstocks.mult.FNBx` [ok] 200 979ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana
- `xstocks.mult.CACCx` [ok] 200 987ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 37ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 160ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.FLNCx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.XRXx` [ok] 200 68ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.PCTx` [ok] 200 72ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.INDIx` [ok] 200 124ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.WRLDx` [ok] 200 79ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.WGSx` [ok] 200 59ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.METCx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=METCx
- `jup.tokens.search.QUBTx` [ok] 200 83ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jito.tip_floor` [ok] 200 154ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 381ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 91ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 119ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 106ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 195ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 77ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 574ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
