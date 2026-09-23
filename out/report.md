# Borealis — Solana ecosystem report

**Generated** 2026-09-23T19:47:42Z · 2026-09-23 12:47:42 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-23T19:47:32Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h -3.24%; DEX 24h $3.20B · 1d -7% · vs-7d-ago +18%; slot 265 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Last TPS sample outside 2.5σ of the 60-sample window** — Last sample 5,422 TPS is +3.64σ vs window mean 4,662 (n=60, σ=209). (threshold: `|last sample − window mean| > 2.5σ`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +24.54%. (threshold: `|7d %| >= 20`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -3.24%, DeFiLlama TVL 1d -1.11%, DEX 1d -6.82%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 449,802,452 |
| Block height | 427,842,648 |
| Block time | 2026-09-23T19:47:32Z |
| Epoch | 1,041 (20.94% · slot 90,454/432,000) |
| Mean TPS (last ~3,600s) | 4,662.5 |
| Mean non-vote TPS | 2,126.7 |
| Median TPS (same window) | 4,647.0 |
| Mean slot time | 264.9 ms |
| Median slot time | 264.3 ms |
| Transaction count (cluster) | 551,824,297,097 |
| Circulating supply | 587,577,868 SOL |
| Total supply | 634,608,991 SOL |
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

- `CjmXSapt…` · 131.54K SOL · commission 0% · lag 1267 slots
- `6DTkuiey…` · 89.15K SOL · commission 100% · lag 449802452 slots
- `HDRqPft5…` · 71.15K SOL · commission 100% · lag 449802452 slots
- `3PZSgErg…` · 36.93K SOL · commission 0% · lag 88522 slots
- `t23p8aBQ…` · 14.37K SOL · commission 0% · lag 2207216 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 71456 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 1003742 slots
- `mrgn4atx…` · 2.21K SOL · commission 0% · lag 1205047 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 1927700 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 1309581 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 1040077 slots
- `R1parD2C…` · 2.87 SOL · commission 5% · lag 65753582 slots

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
| Jito tip-floor run-rate (NOT REV) | $65.47K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 65470 USD; at p95 floor → 2734295 USD. |
| Protocol fees 24h | $17.87M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $114.40 | coingecko.simple_price |
| 24h change | -3.24% | coingecko.simple_price |
| Market cap | $67.22B | coingecko.simple_price |
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

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 78/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $116.02K (lower bound, not a census).
24h volume $131.18M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 78 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

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

_As of 2026-09-23 (2026-09-23 12:47:42 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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
- **xStocks** — IRDMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — AMTMx multiplier missing — mcap omitted (never assumed 1.0)

## Sources this run

- `rpc.getHealth` [ok] 200 230ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 186ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 231ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 206ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 165ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5612ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 344ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 186ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 151ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 278ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 80ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 908ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 749ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 408ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 143ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 139ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 156ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 627ms https://solana.com/data
- `solana.com.databricks` [ok] 200 214ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 682ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 176ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 139ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 137ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 492ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 1569ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 159ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 162ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 162ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 306ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 495ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 116ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 111ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 324ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 106ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 147ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 140ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 125ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 203ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 165ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 186ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 194ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 454ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 248ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 228ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 282ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 495ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 233ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 277ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 140ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 266ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 191ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 308ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 198ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 300ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 198ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 283ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 213ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 225ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 186ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 191ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 186ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 170ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 208ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 239ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 2254ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2206ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2802ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2476ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2968ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2196ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2062ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 3449ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.XRXx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.PCTx` [ok] 200 852ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.WRLDx` [ok] 200 1000ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.FLNCx` [ok] 200 1147ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.QUBTx` [ok] 200 1314ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.INDIx` [ok] 200 1413ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WGSx` [ok] 200 1633ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.METCx` [ok] 200 2133ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.PCTx` [ok] 200 2341ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 2925ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 2678ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 2423ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 2933ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 3332ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 1609ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.circ.METCx` [ok] 200 2972ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 1208ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.FLNCx` [ok] 200 4192ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 582ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.INDIx` [ok] 200 1290ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 2549ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 1281ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.mult.FLNCx` [ok] 200 1360ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 1124ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.price.MIDDx` [ok] 200 706ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data
- `xstocks.mult.QUBTx` [ok] 200 2280ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 1828ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 3512ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.WYFIx` [ok] 200 1956ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.ALMx` [ok] 200 803ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data
- `xstocks.circ.BETRx` [ok] 200 1150ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.RNGx` [ok] 200 775ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data
- `xstocks.price.RITMx` [ok] 200 1213ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data
- `xstocks.price.SHCx` [ok] 200 1015ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data
- `xstocks.mult.WYFIx` [ok] 200 1330ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 2219ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.price.WHx` [ok] 200 685ms https://api.backed.fi/api/v2/public/assets/WHx/price-data
- `xstocks.circ.ALMx` [ok] 200 2396ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object
- `xstocks.circ.RNGx` [ok] 200 2287ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 1035ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.circ.RITMx` [ok] 200 2084ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object
- `xstocks.circ.SHCx` [ok] 200 2170ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object
- `xstocks.mult.BETRx` [ok] 200 2854ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.REYNx` [ok] 200 839ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data
- `xstocks.circ.MIDDx` [ok] 200 4072ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object
- `xstocks.price.VSNTx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data
- `xstocks.mult.RNGx` [ok] 200 1546ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana
- `xstocks.circ.WHx` [ok] 200 2325ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object
- `xstocks.mult.RITMx` [ok] 200 1654ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana
- `xstocks.mult.SHCx` [ok] 200 1623ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana
- `xstocks.mult.ALMx` [ok] 200 2345ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana
- `xstocks.mult.MIDDx` [ok] 200 1301ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana
- `xstocks.price.IRDMx` [ok] 200 750ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data
- `xstocks.circ.REYNx` [ok] 200 1949ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object
- `xstocks.price.GXOx` [ok] 200 624ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data
- `xstocks.price.CARx` [ok] 200 1469ms https://api.backed.fi/api/v2/public/assets/CARx/price-data
- `xstocks.price.OZKx` [ok] 200 1450ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data
- `xstocks.circ.VSNTx` [ok] 200 2517ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object
- `xstocks.price.FBINx` [ok] 200 1496ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data
- `xstocks.mult.WHx` [ok] 200 2279ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana
- `xstocks.price.AMTMx` [ok] 200 806ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data
- `xstocks.circ.IRDMx` [ok] 200 2806ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object
- `xstocks.circ.OZKx` [ok] 200 2443ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object
- `xstocks.circ.CARx` [ok] 200 3058ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object
- `xstocks.circ.GXOx` [ok] 200 3405ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object
- `xstocks.mult.REYNx` [ok] 200 3562ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana
- `xstocks.mult.VSNTx` [ok] 200 3084ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana
- `xstocks.circ.FBINx` [ok] 200 3148ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object
- `xstocks.price.PSNx` [ok] 200 1068ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data
- `xstocks.mult.OZKx` [ok] 200 2003ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana
- `xstocks.price.MTNx` [ok] 200 1604ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data
- `xstocks.mult.GXOx` [ok] 200 2663ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana
- `xstocks.circ.AMTMx` [ok] 200 4219ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object
- `xstocks.mult.FBINx` [ok] 200 2242ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana
- `xstocks.mult.CARx` [ok] 200 3186ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana
- `xstocks.price.EPAMx` [ok] 200 914ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data
- `xstocks.circ.MTNx` [ok] 200 2347ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object
- `xstocks.circ.PSNx` [ok] 200 4016ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object
- `xstocks.mult.MTNx` [ok] 200 1998ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana
- `xstocks.circ.EPAMx` [ok] 200 2573ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object
- `xstocks.mult.PSNx` [ok] 200 1162ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana
- `xstocks.price.Mx` [ok] 200 488ms https://api.backed.fi/api/v2/public/assets/Mx/price-data
- `xstocks.mult.EPAMx` [ok] 200 2130ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana
- `xstocks.price.ELFx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data
- `xstocks.circ.Mx` [ok] 200 1908ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object
- `xstocks.mult.Mx` [ok] 200 979ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana
- `xstocks.price.SNDRx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data
- `xstocks.circ.ELFx` [ok] 200 1759ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object
- `xstocks.mult.IRDMx` [FAIL]  12057ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.ELFx` [ok] 200 910ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana
- `xstocks.price.VNOx` [ok] 200 665ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data
- `xstocks.price.EXPx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data
- `xstocks.circ.SNDRx` [ok] 200 1843ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object
- `xstocks.mult.SNDRx` [ok] 200 788ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana
- `xstocks.price.SAICx` [ok] 200 10684ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data
- `xstocks.price.PEGAx` [ok] 200 11897ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data
- `xstocks.price.VIRTx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data
- `xstocks.price.EXLSx` [ok] 200 10900ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data
- `xstocks.circ.VNOx` [ok] 200 1919ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object
- `xstocks.circ.EXPx` [ok] 200 1888ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object
- `xstocks.mult.AMTMx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.VIRTx` [ok] 200 1449ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object
- `xstocks.mult.EXPx` [ok] 200 1238ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana
- `xstocks.price.MKTXx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data
- `xstocks.circ.PEGAx` [ok] 200 2242ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object
- `xstocks.circ.EXLSx` [ok] 200 2016ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object
- `xstocks.mult.VIRTx` [ok] 200 928ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana
- `xstocks.mult.VNOx` [ok] 200 1937ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana
- `xstocks.circ.SAICx` [ok] 200 2751ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object
- `xstocks.price.VFCx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data
- `xstocks.price.CPBx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data
- `xstocks.price.CRUSx` [ok] 200 10600ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data
- `xstocks.mult.PEGAx` [ok] 200 1564ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana
- `xstocks.circ.MKTXx` [ok] 200 2199ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object
- `xstocks.mult.EXLSx` [ok] 200 1908ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana
- `xstocks.mult.SAICx` [ok] 200 1633ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana
- `xstocks.circ.VFCx` [ok] 200 1649ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object
- `xstocks.circ.CPBx` [ok] 200 1856ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object
- `xstocks.price.BCx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/BCx/price-data
- `xstocks.circ.CRUSx` [ok] 200 1796ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object
- `xstocks.price.ADTx` [ok] 200 819ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data
- `xstocks.mult.VFCx` [ok] 200 1276ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana
- `xstocks.price.NXSTx` [ok] 200 1914ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data
- `xstocks.mult.MKTXx` [ok] 200 1717ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana
- `xstocks.mult.CPBx` [ok] 200 1324ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana
- `xstocks.mult.CRUSx` [ok] 200 1071ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana
- `xstocks.circ.ADTx` [ok] 200 1107ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object
- `xstocks.price.KRMNx` [ok] 200 667ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data
- `xstocks.price.GTESx` [ok] 200 561ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data
- `xstocks.price.HRBx` [ok] 200 508ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data
- `xstocks.circ.BCx` [ok] 200 2168ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object
- `xstocks.price.ACIx` [ok] 200 1242ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data
- `xstocks.mult.ADTx` [ok] 200 1495ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana
- `xstocks.circ.NXSTx` [ok] 200 2040ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object
- `xstocks.mult.BCx` [ok] 200 1310ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana
- `xstocks.circ.ACIx` [ok] 200 1455ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object
- `xstocks.price.AXSx` [ok] 200 888ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data
- `xstocks.circ.GTESx` [ok] 200 2198ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object
- `xstocks.circ.KRMNx` [ok] 200 2474ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object
- `xstocks.price.DLBx` [ok] 200 831ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data
- `xstocks.mult.NXSTx` [ok] 200 1403ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana
- `xstocks.mult.ACIx` [ok] 200 1410ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana
- `xstocks.price.RYNx` [ok] 200 770ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data
- `xstocks.circ.HRBx` [ok] 200 3426ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object
- `xstocks.mult.GTESx` [ok] 200 1517ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana
- `xstocks.mult.KRMNx` [ok] 200 1459ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana
- `xstocks.price.POOLx` [ok] 200 849ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data
- `xstocks.circ.AXSx` [ok] 200 2101ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object
- `xstocks.price.LWx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/LWx/price-data
- `xstocks.price.TFXx` [ok] 200 558ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data
- `xstocks.circ.DLBx` [ok] 200 1871ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object
- `xstocks.mult.HRBx` [ok] 200 1227ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana
- `xstocks.price.AAONx` [ok] 200 762ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.circ.RYNx` [ok] 200 2140ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object
- `xstocks.circ.POOLx` [ok] 200 1732ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object
- `xstocks.mult.AXSx` [ok] 200 1814ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana
- `xstocks.circ.LWx` [ok] 200 2131ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object
- `xstocks.mult.DLBx` [ok] 200 2324ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana
- `xstocks.price.HXLx` [ok] 200 11640ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data
- `xstocks.circ.TFXx` [ok] 200 2815ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object
- `xstocks.circ.AAONx` [ok] 200 1594ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.mult.POOLx` [ok] 200 1407ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana
- `xstocks.price.INGMx` [ok] 200 677ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data
- `xstocks.price.SONx` [ok] 200 1495ms https://api.backed.fi/api/v2/public/assets/SONx/price-data
- `xstocks.mult.RYNx` [ok] 200 2302ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana
- `xstocks.price.TTDx` [ok] 200 846ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data
- `xstocks.price.HRx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/HRx/price-data
- `xstocks.mult.LWx` [ok] 200 2261ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana
- `xstocks.mult.AAONx` [ok] 200 1585ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.circ.HXLx` [ok] 200 2271ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object
- `xstocks.price.RLIx` [ok] 200 917ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data
- `xstocks.circ.SONx` [ok] 200 2170ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object
- `xstocks.price.CLFx` [ok] 200 1111ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data
- `xstocks.mult.TFXx` [ok] 200 3034ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana
- `xstocks.circ.TTDx` [ok] 200 2602ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object
- `xstocks.price.STWDx` [ok] 200 961ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data
- `xstocks.mult.HXLx` [ok] 200 1940ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana
- `xstocks.circ.INGMx` [ok] 200 3844ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object
- `xstocks.mult.SONx` [ok] 200 1615ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana
- `xstocks.circ.HRx` [ok] 200 2899ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object
- `xstocks.mult.TTDx` [ok] 200 1447ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana
- `xstocks.circ.RLIx` [ok] 200 2617ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object
- `xstocks.circ.CLFx` [ok] 200 2429ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object
- `xstocks.price.MSMx` [ok] 200 1173ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data
- `xstocks.price.CZRx` [ok] 200 1004ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data
- `xstocks.price.OMFx` [ok] 200 967ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data
- `xstocks.mult.INGMx` [ok] 200 2023ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana
- `xstocks.mult.HRx` [ok] 200 2395ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana
- `xstocks.circ.STWDx` [ok] 200 3103ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object
- `xstocks.mult.RLIx` [ok] 200 2037ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana
- `xstocks.circ.MSMx` [ok] 200 2114ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object
- `xstocks.price.CHEx` [ok] 200 812ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data
- `xstocks.price.Gx` [ok] 200 563ms https://api.backed.fi/api/v2/public/assets/Gx/price-data
- `xstocks.price.CROXx` [ok] 200 1637ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data
- `xstocks.mult.CLFx` [ok] 200 2661ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana
- `xstocks.circ.OMFx` [ok] 200 2566ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object
- `xstocks.price.ALGMx` [ok] 200 935ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data
- `xstocks.mult.STWDx` [ok] 200 1665ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana
- `xstocks.mult.MSMx` [ok] 200 1838ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana
- `xstocks.price.MTGx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data
- `xstocks.mult.OMFx` [ok] 200 1290ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana
- `xstocks.circ.CROXx` [ok] 200 2302ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object
- `xstocks.circ.Gx` [ok] 200 2375ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object
- `xstocks.circ.CZRx` [ok] 200 4873ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object
- `xstocks.circ.ALGMx` [ok] 200 1420ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object
- `xstocks.price.BEPCx` [ok] 200 1567ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data
- `xstocks.mult.CZRx` [ok] 200 1258ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana
- `xstocks.mult.CROXx` [ok] 200 1343ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana
- `xstocks.mult.ALGMx` [ok] 200 1386ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana
- `xstocks.price.MTDRx` [ok] 200 1642ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data
- `xstocks.mult.Gx` [ok] 200 1745ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana
- `xstocks.price.BYDx` [ok] 200 767ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data
- `xstocks.price.LYFTx` [ok] 200 951ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data
- `xstocks.price.STAGx` [ok] 200 675ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data
- `xstocks.circ.MTGx` [ok] 200 3492ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object
- `xstocks.price.INGRx` [ok] 200 1533ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data
- `xstocks.circ.BEPCx` [ok] 200 2189ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object
- `xstocks.circ.CHEx` [ok] 200 5507ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object
- `xstocks.circ.MTDRx` [ok] 200 2118ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object
- `xstocks.mult.BEPCx` [ok] 200 1452ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana
- `xstocks.mult.CHEx` [ok] 200 1538ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana
- `xstocks.mult.MTGx` [ok] 200 1906ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana
- `xstocks.circ.INGRx` [ok] 200 2222ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object
- `xstocks.circ.LYFTx` [ok] 200 2819ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object
- `xstocks.circ.STAGx` [ok] 200 2817ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object
- `xstocks.mult.MTDRx` [ok] 200 1753ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana
- `xstocks.price.MBGLx` [ok] 200 838ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data
- `xstocks.circ.BYDx` [ok] 200 3206ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object
- `xstocks.price.FNBx` [ok] 200 1440ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data
- `xstocks.price.CACCx` [ok] 200 1257ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data
- `xstocks.mult.INGRx` [ok] 200 1076ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana
- `xstocks.mult.STAGx` [ok] 200 1266ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana
- `xstocks.mult.LYFTx` [ok] 200 1444ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana
- `xstocks.mult.BYDx` [ok] 200 1205ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana
- `xstocks.circ.MBGLx` [ok] 200 2403ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object
- `xstocks.circ.FNBx` [ok] 200 2348ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object
- `xstocks.mult.MBGLx` [ok] 200 1391ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana
- `xstocks.circ.CACCx` [ok] 200 4037ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object
- `xstocks.mult.FNBx` [ok] 200 2151ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana
- `xstocks.mult.CACCx` [ok] 200 1233ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 743ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 360ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.XRXx` [ok] 200 137ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 159ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.QUBTx` [ok] 200 170ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.FLNCx` [ok] 200 145ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.AIx` [ok] 200 172ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.WYFIx` [ok] 200 143ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.WGSx` [ok] 200 143ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.WRLDx` [ok] 200 143ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jito.tip_floor` [ok] 200 446ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 435ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 133ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 145ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 179ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 94ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 141ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 208ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
