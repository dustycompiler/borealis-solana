# Borealis — Solana ecosystem report

**Generated** 2026-09-23T16:01:14Z · 2026-09-23 09:01:14 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-23T16:01:05Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h -2.84%; DEX 24h $3.20B · 1d -7% · vs-7d-ago +18%; slot 267 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +24.54%. (threshold: `|7d %| >= 20`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -2.84%, DeFiLlama TVL 1d -0.34%, DEX 1d -6.82%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 449,751,338 |
| Block height | 427,791,555 |
| Block time | 2026-09-23T16:01:05Z |
| Epoch | 1,041 (9.11% · slot 39,340/432,000) |
| Mean TPS (last ~3,600s) | 4,725.1 |
| Mean non-vote TPS | 2,215.8 |
| Median TPS (same window) | 4,694.8 |
| Mean slot time | 267.2 ms |
| Median slot time | 266.7 ms |
| Transaction count (cluster) | 551,758,893,871 |
| Circulating supply | 587,578,040 SOL |
| Total supply | 634,609,163 SOL |
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

- `6DTkuiey…` · 89.15K SOL · commission 100% · lag 449751338 slots
- `HDRqPft5…` · 71.15K SOL · commission 100% · lag 449751338 slots
- `3PZSgErg…` · 36.93K SOL · commission 0% · lag 37408 slots
- `t23p8aBQ…` · 14.37K SOL · commission 0% · lag 2156102 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 20342 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 952628 slots
- `mrgn4atx…` · 2.21K SOL · commission 0% · lag 1153933 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 1876586 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 1258467 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 988963 slots
- `R1parD2C…` · 2.87 SOL · commission 5% · lag 65702468 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 171829 slots

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
| Jito tip-floor run-rate (NOT REV) | $77.28K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 77283 USD; at p95 floor → 796002 USD. |
| Protocol fees 24h | $17.87M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $114.05 | coingecko.simple_price |
| 24h change | -2.84% | coingecko.simple_price |
| Market cap | $67.01B | coingecko.simple_price |
| 24h volume | $5.13B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.44B |
| TVL 1d / 7d / 30d | -0.34% / +12.44% / +15.48% |
| DEX volume 24h | $3.20B · 1d -6.82% · vs-7d-ago +18.18% |
| 7d DEX volume | $21.22B · +17.10% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $17.87M |
| Fees 1d / 7d | -4.10% / +24.54% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $634.15M | +62.55% |
| Raydium AMM | $368.90M | -35.64% |
| BisonFi | $368.17M | -17.60% |
| Orca DEX | $327.86M | -27.63% |
| Meteora DLMM | $266.83M | +2.78% |
| fomo Wallet | $152.70M | -4.77% |
| Scorch | $129.41M | -14.10% |
| pump.fun | $121.03M | -0.93% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.86B | -0.20% | +20.14% |
| Kamino Lend | Lending | $1.40B | -1.68% | +5.44% |
| Raydium AMM | Dexs | $1.33B | +1.12% | +22.08% |
| Jito Liquid Staking | Liquid Staking | $1.21B | -0.04% | +20.54% |
| Binance Staked SOL | Liquid Staking | $1.20B | -0.19% | +18.68% |
| Jupiter Lend | Lending | $1.19B | +0.28% | +12.13% |
| Jupiter Perpetual Exchange | Derivatives | $797.70M | -2.12% | +9.13% |
| Jupiter Staked SOL | Liquid Staking | $604.00M | -0.29% | +19.89% |
| Marinade Native | Staking Pool | $448.88M | +0.33% | +20.90% |
| PumpSwap | Dexs | $382.55M | +1.19% | +21.64% |

## Stablecoins

Solana circulating pegged-USD: **$15.86B**
(1d -1.71% · 7d +5.79%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.29B | -12.03% |
| USDT · Tether | $2.14B | +0.00% |
| USDGO · USDGO | $1.42B | +1.00% |
| USD1 · World Liberty Financial USD | $1.37B | +1.42% |
| BUIDL · BlackRock USD | $987.58M | -0.59% |
| PYUSD · PayPal USD | $734.10M | +0.38% |
| USDG · Global Dollar | $630.91M | +1.66% |
| USDe · Ethena USDe | $499.97M | -0.41% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 10 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 10 · priced-subset mcap $107.26K (lower bound, not a census).
24h volume $136.15M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 10 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$543.76M** across 16 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $303.04M
- **Huma Finance V2** (RWA) — $195.31M
- **Plume Vaults** (RWA) — $28.20M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $3.01M
- **VNX** (RWA) — $2.69M
- **Oro Finance** (RWA) — $2.50M
- **International Stable Currency** (RWA) — $2.43M

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

_As of 2026-09-23 (2026-09-23 09:01:14 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=live, 200ms=pending. Observed mean slot ~267 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~267 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 363ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 269ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 321ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 246ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 247ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6782ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 550ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 115ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 124ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 68ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 188ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 2292ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 3901ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 110ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 80ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 88ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 99ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 664ms https://solana.com/data
- `solana.com.databricks` [ok] 200 308ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 740ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 289ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 253ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 92ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 235ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 429ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 236ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 233ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 247ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 2733ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2085ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 675ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 494ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 289ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 211ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 255ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 247ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 318ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 181ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 301ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 152ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 352ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 249ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 349ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 261ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 325ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 240ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 358ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 217ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 341ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 228ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 373ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 204ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 315ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 356ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 323ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 180ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 330ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 339ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 312ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 206ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 342ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 223ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 292ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 191ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 2583ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2901ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2366ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2777ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2726ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 3549ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2284ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 3752ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.FLNCx` [ok] 200 948ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.INDIx` [ok] 200 1104ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.METCx` [ok] 200 1129ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.WGSx` [ok] 200 1269ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.XRXx` [ok] 200 1429ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.PCTx` [ok] 200 1764ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.QUBTx` [ok] 200 2131ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.circ.FLNCx` [ok] 200 1340ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 1192ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 1650ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.PCTx` [ok] 200 1365ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 2270ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 1549ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 3249ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 1913ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 2353ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 2146ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 1955ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 3423ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 1400ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.QUBTx` [ok] 200 2780ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 1202ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.INDIx` [ok] 200 2282ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 1724ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.ALMx` [ok] 200 1313ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data
- `xstocks.price.RITMx` [ok] 200 924ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data
- `xstocks.price.RNGx` [ok] 200 975ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data
- `xstocks.circ.WYFIx` [ok] 200 2799ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.ALMx` [ok] 200 2360ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object
- `xstocks.circ.RITMx` [ok] 200 2533ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object
- `xstocks.circ.BETRx` [ok] 200 3160ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 3729ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.RNGx` [ok] 200 2616ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object
- `xstocks.mult.ALMx` [ok] 200 1624ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana
- `xstocks.mult.BETRx` [ok] 200 1310ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 1189ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 2701ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.RNGx` [ok] 200 1257ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana
- `xstocks.price.VSNTx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data
- `xstocks.price.CARx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/CARx/price-data
- `xstocks.price.WRLDx` [FAIL]  12041ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SHCx` [ok] 200 1202ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data
- `xstocks.price.REYNx` [ok] 200 885ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data
- `xstocks.mult.RITMx` [ok] 200 2765ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana
- `xstocks.price.OZKx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data
- `xstocks.circ.VSNTx` [ok] 200 1867ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object
- `xstocks.circ.SHCx` [ok] 200 1657ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object
- `xstocks.circ.REYNx` [ok] 200 1860ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 2146ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.OZKx` [ok] 200 2059ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 1008ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.VSNTx` [ok] 200 1565ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana
- `xstocks.mult.REYNx` [ok] 200 1281ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana
- `xstocks.price.IRDMx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data
- `xstocks.price.FBINx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data
- `xstocks.price.GXOx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data
- `xstocks.mult.SHCx` [ok] 200 2636ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana
- `xstocks.price.MIDDx` [ok] 200 11090ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data
- `xstocks.price.AMTMx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data
- `xstocks.mult.OZKx` [ok] 200 2281ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana
- `xstocks.circ.GXOx` [ok] 200 1736ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object
- `xstocks.circ.IRDMx` [ok] 200 2123ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object
- `xstocks.price.MTNx` [ok] 200 709ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data
- `xstocks.circ.FBINx` [ok] 200 2469ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object
- `xstocks.circ.AMTMx` [ok] 200 1669ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object
- `xstocks.mult.IRDMx` [ok] 200 874ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana
- `xstocks.circ.MIDDx` [ok] 200 2225ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object
- `xstocks.price.PSNx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data
- `xstocks.mult.GXOx` [ok] 200 1734ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana
- `xstocks.price.PEGAx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data
- `xstocks.mult.MIDDx` [ok] 200 927ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana
- `xstocks.mult.FBINx` [ok] 200 1597ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana
- `xstocks.price.SAICx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data
- `xstocks.price.EXLSx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data
- `xstocks.mult.AMTMx` [ok] 200 1556ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana
- `xstocks.circ.MTNx` [ok] 200 2268ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object
- `xstocks.price.EPAMx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data
- `xstocks.circ.PSNx` [ok] 200 1849ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object
- `xstocks.circ.PEGAx` [ok] 200 1571ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object
- `xstocks.mult.MTNx` [ok] 200 769ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana
- `xstocks.price.CRUSx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data
- `xstocks.mult.PSNx` [ok] 200 817ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana
- `xstocks.circ.EXLSx` [ok] 200 1727ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object
- `xstocks.price.WHx` [ok] 200 10488ms https://api.backed.fi/api/v2/public/assets/WHx/price-data
- `xstocks.mult.PEGAx` [ok] 200 796ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana
- `xstocks.price.Mx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/Mx/price-data
- `xstocks.price.ELFx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data
- `xstocks.mult.EXLSx` [ok] 200 857ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana
- `xstocks.circ.SAICx` [ok] 200 2651ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object
- `xstocks.circ.EPAMx` [ok] 200 2261ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object
- `xstocks.price.SNDRx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data
- `xstocks.circ.CRUSx` [ok] 200 1872ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object
- `xstocks.circ.WHx` [ok] 200 1487ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object
- `xstocks.mult.SAICx` [ok] 200 764ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana
- `xstocks.price.VNOx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data
- `xstocks.mult.EPAMx` [ok] 200 1238ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana
- `xstocks.circ.CARx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.ELFx` [ok] 200 2067ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object
- `xstocks.mult.CRUSx` [ok] 200 1050ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana
- `xstocks.mult.WHx` [ok] 200 1012ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana
- `xstocks.price.EXPx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data
- `xstocks.circ.Mx` [ok] 200 2443ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object
- `xstocks.price.VIRTx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data
- `xstocks.price.MKTXx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data
- `xstocks.mult.CARx` [ok] 200 1093ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana
- `xstocks.circ.SNDRx` [ok] 200 2124ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object
- `xstocks.mult.ELFx` [ok] 200 972ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana
- `xstocks.price.HXLx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data
- `xstocks.mult.Mx` [ok] 200 1139ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana
- `xstocks.price.CPBx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data
- `xstocks.circ.EXPx` [ok] 200 1486ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object
- `xstocks.circ.VNOx` [ok] 200 2120ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object
- `xstocks.mult.SNDRx` [ok] 200 1113ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana
- `xstocks.price.VFCx` [ok] 200 690ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data
- `xstocks.circ.VIRTx` [ok] 200 1852ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object
- `xstocks.circ.MKTXx` [ok] 200 2073ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object
- `xstocks.price.NXSTx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data
- `xstocks.mult.EXPx` [ok] 200 1022ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana
- `xstocks.circ.HXLx` [ok] 200 1869ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object
- `xstocks.price.ADTx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data
- `xstocks.mult.VNOx` [ok] 200 1528ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana
- `xstocks.mult.VIRTx` [ok] 200 1162ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana
- `xstocks.circ.CPBx` [ok] 200 2093ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object
- `xstocks.mult.MKTXx` [ok] 200 1126ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana
- `xstocks.price.KRMNx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data
- `xstocks.mult.HXLx` [ok] 200 1079ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana
- `xstocks.circ.VFCx` [ok] 200 2098ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object
- `xstocks.price.ACIx` [ok] 200 828ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data
- `xstocks.circ.ADTx` [ok] 200 1050ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object
- `xstocks.price.BCx` [ok] 200 922ms https://api.backed.fi/api/v2/public/assets/BCx/price-data
- `xstocks.circ.NXSTx` [ok] 200 2003ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object
- `xstocks.mult.CPBx` [ok] 200 1069ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana
- `xstocks.price.GTESx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data
- `xstocks.price.HRBx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data
- `xstocks.mult.VFCx` [ok] 200 1215ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana
- `xstocks.mult.ADTx` [ok] 200 1305ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana
- `xstocks.circ.ACIx` [ok] 200 1563ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object
- `xstocks.circ.KRMNx` [ok] 200 1827ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object
- `xstocks.circ.BCx` [ok] 200 1621ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object
- `xstocks.price.AXSx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data
- `xstocks.circ.HRBx` [ok] 200 792ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object
- `xstocks.price.DLBx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data
- `xstocks.mult.NXSTx` [ok] 200 1578ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana
- `xstocks.price.RYNx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data
- `xstocks.circ.GTESx` [ok] 200 1812ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object
- `xstocks.mult.KRMNx` [ok] 200 1137ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana
- `xstocks.mult.HRBx` [ok] 200 1152ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana
- `xstocks.mult.ACIx` [ok] 200 1662ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana
- `xstocks.price.POOLx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data
- `xstocks.mult.BCx` [ok] 200 1695ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana
- `xstocks.price.TFXx` [ok] 200 577ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data
- `xstocks.mult.GTESx` [ok] 200 1201ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana
- `xstocks.price.LWx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/LWx/price-data
- `xstocks.price.AAONx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.circ.DLBx` [ok] 200 1985ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object
- `xstocks.price.SONx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/SONx/price-data
- `xstocks.circ.AAONx` [ok] 200 910ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.mult.DLBx` [ok] 200 1036ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana
- `xstocks.price.INGMx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data
- `xstocks.circ.AXSx` [ok] 200 3469ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object
- `xstocks.circ.RYNx` [ok] 200 2976ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object
- `xstocks.circ.POOLx` [ok] 200 2061ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object
- `xstocks.mult.AAONx` [ok] 200 1103ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.circ.TFXx` [ok] 200 2481ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object
- `xstocks.circ.SONx` [ok] 200 1833ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object
- `xstocks.price.TTDx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data
- `xstocks.mult.AXSx` [ok] 200 1049ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana
- `xstocks.mult.POOLx` [ok] 200 951ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana
- `xstocks.mult.RYNx` [ok] 200 1086ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana
- `xstocks.price.RLIx` [ok] 200 524ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data
- `xstocks.price.CLFx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data
- `xstocks.price.HRx` [ok] 200 670ms https://api.backed.fi/api/v2/public/assets/HRx/price-data
- `xstocks.mult.SONx` [ok] 200 1172ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana
- `xstocks.mult.TFXx` [ok] 200 1405ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana
- `xstocks.price.STWDx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data
- `xstocks.circ.INGMx` [ok] 200 2311ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object
- `xstocks.circ.LWx` [ok] 200 4002ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object
- `xstocks.price.MSMx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data
- `xstocks.circ.TTDx` [ok] 200 1612ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object
- `xstocks.circ.STWDx` [ok] 200 821ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object
- `xstocks.circ.RLIx` [ok] 200 1619ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object
- `xstocks.mult.INGMx` [ok] 200 1130ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana
- `xstocks.mult.LWx` [ok] 200 1121ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana
- `xstocks.price.CZRx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data
- `xstocks.mult.TTDx` [ok] 200 1198ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana
- `xstocks.circ.CLFx` [ok] 200 2271ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object
- `xstocks.price.OMFx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data
- `xstocks.mult.STWDx` [ok] 200 1040ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana
- `xstocks.mult.RLIx` [ok] 200 1074ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana
- `xstocks.price.CROXx` [ok] 200 598ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data
- `xstocks.circ.MSMx` [ok] 200 1889ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object
- `xstocks.price.CHEx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data
- `xstocks.circ.CZRx` [ok] 200 821ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object
- `xstocks.price.Gx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/Gx/price-data
- `xstocks.circ.HRx` [ok] 200 3244ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object
- `xstocks.circ.CROXx` [ok] 200 911ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object
- `xstocks.mult.CZRx` [ok] 200 995ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana
- `xstocks.mult.MSMx` [ok] 200 1190ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana
- `xstocks.mult.CLFx` [ok] 200 1850ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana
- `xstocks.circ.OMFx` [ok] 200 1821ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object
- `xstocks.price.ALGMx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data
- `xstocks.mult.HRx` [ok] 200 1038ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana
- `xstocks.price.MTGx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data
- `xstocks.circ.CHEx` [ok] 200 1791ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object
- `xstocks.price.MTDRx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data
- `xstocks.price.BEPCx` [ok] 200 766ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data
- `xstocks.mult.CROXx` [ok] 200 1411ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana
- `xstocks.circ.ALGMx` [ok] 200 860ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object
- `xstocks.mult.OMFx` [ok] 200 1185ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana
- `xstocks.price.INGRx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data
- `xstocks.circ.Gx` [ok] 200 2461ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object
- `xstocks.price.LYFTx` [ok] 200 508ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data
- `xstocks.mult.CHEx` [ok] 200 1242ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana
- `xstocks.circ.MTGx` [ok] 200 1622ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object
- `xstocks.price.BYDx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data
- `xstocks.mult.ALGMx` [ok] 200 1584ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana
- `xstocks.circ.BEPCx` [ok] 200 1869ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object
- `xstocks.mult.Gx` [ok] 200 1218ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana
- `xstocks.circ.INGRx` [ok] 200 1752ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object
- `xstocks.circ.MTDRx` [ok] 200 2471ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object
- `xstocks.price.STAGx` [ok] 200 675ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data
- `xstocks.price.FNBx` [ok] 200 542ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data
- `xstocks.mult.MTGx` [ok] 200 1666ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana
- `xstocks.circ.LYFTx` [ok] 200 2536ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object
- `xstocks.circ.BYDx` [ok] 200 2151ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object
- `xstocks.mult.BEPCx` [ok] 200 1807ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana
- `xstocks.mult.MTDRx` [ok] 200 1325ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana
- `xstocks.price.MBGLx` [ok] 200 905ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data
- `xstocks.price.CACCx` [ok] 200 562ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data
- `xstocks.mult.INGRx` [ok] 200 2011ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana
- `xstocks.mult.LYFTx` [ok] 200 1294ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana
- `xstocks.circ.FNBx` [ok] 200 2315ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object
- `xstocks.circ.STAGx` [ok] 200 2706ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object
- `xstocks.mult.BYDx` [ok] 200 2250ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana
- `xstocks.circ.CACCx` [ok] 200 1902ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object
- `xstocks.mult.FNBx` [ok] 200 1461ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana
- `xstocks.circ.MBGLx` [ok] 200 2579ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object
- `xstocks.mult.STAGx` [ok] 200 1906ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana
- `xstocks.mult.MBGLx` [ok] 200 1283ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana
- `xstocks.mult.CACCx` [ok] 200 2272ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 840ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 248ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.XRXx` [ok] 200 130ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 123ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.QUBTx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.FLNCx` [ok] 200 161ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.WGSx` [ok] 200 121ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.AIx` [ok] 200 138ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.WYFIx` [ok] 200 161ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.INDIx` [ok] 200 122ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jito.tip_floor` [ok] 200 158ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 305ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 167ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 241ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 229ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 236ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 241ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 377ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
