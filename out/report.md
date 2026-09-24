# Borealis — Solana ecosystem report

**Generated** 2026-09-24T02:22:18Z · 2026-09-23 19:22:18 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-24T02:22:09Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -2.75%; DEX 24h $2.68B · 1d -16% · vs-7d-ago -4%; slot 266 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -16.03%. (threshold: `|1d %| >= 8`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -2.75%, DeFiLlama TVL 1d -0.97%, DEX 1d -16.03%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 449,891,603 |
| Block height | 427,931,740 |
| Block time | 2026-09-24T02:22:09Z |
| Epoch | 1,041 (41.57% · slot 179,603/432,000) |
| Mean TPS (last ~3,600s) | 4,448.9 |
| Mean non-vote TPS | 1,918.0 |
| Median TPS (same window) | 4,440.1 |
| Mean slot time | 265.5 ms |
| Median slot time | 265.5 ms |
| Transaction count (cluster) | 551,934,363,850 |
| Circulating supply | 587,577,591 SOL |
| Total supply | 634,608,703 SOL |
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

- `6DTkuiey…` · 89.15K SOL · commission 100% · lag 449891603 slots
- `HDRqPft5…` · 71.15K SOL · commission 100% · lag 449891603 slots
- `3PZSgErg…` · 36.93K SOL · commission 0% · lag 177673 slots
- `t23p8aBQ…` · 14.37K SOL · commission 0% · lag 2296367 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 160607 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 1092893 slots
- `mrgn4atx…` · 2.21K SOL · commission 0% · lag 1294198 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 2016851 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 1398732 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 1129228 slots
- `R1parD2C…` · 2.87 SOL · commission 5% · lag 65842733 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 312094 slots

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
| Jito tip-floor run-rate (NOT REV) | $67.04K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 67042 USD; at p95 floor → 3233230 USD. |
| Protocol fees 24h | $16.91M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $115.03 | coingecko.simple_price |
| 24h change | -2.75% | coingecko.simple_price |
| Market cap | $67.56B | coingecko.simple_price |
| 24h volume | $5.04B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.40B |
| TVL 1d / 7d / 30d | -0.97% / +10.61% / +11.23% |
| DEX volume 24h | $2.68B · 1d -16.03% · vs-7d-ago -4.17% |
| 7d DEX volume | $19.96B · +11.85% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $16.91M |
| Fees 1d / 7d | -5.42% / +13.49% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| Raydium AMM | $393.92M | -17.22% |
| BisonFi | $368.17M | 0.00% |
| Orca DEX | $357.93M | -2.63% |
| PumpSwap | $270.19M | -57.39% |
| Meteora DLMM | $233.66M | -12.43% |
| fomo Wallet | $129.50M | -12.40% |
| Scorch | $129.41M | 0.00% |
| pump.fun | $121.03M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.86B | -1.49% | +19.58% |
| Kamino Lend | Lending | $1.41B | -1.45% | +6.02% |
| Raydium AMM | Dexs | $1.31B | -2.10% | +18.27% |
| Jito Liquid Staking | Liquid Staking | $1.19B | -2.68% | +18.33% |
| Binance Staked SOL | Liquid Staking | $1.18B | -2.64% | +17.08% |
| Jupiter Lend | Lending | $1.17B | -0.82% | +10.64% |
| Jupiter Perpetual Exchange | Derivatives | $804.31M | -1.98% | +10.09% |
| Jupiter Staked SOL | Liquid Staking | $596.92M | -2.35% | +17.32% |
| Marinade Native | Staking Pool | $442.71M | -1.93% | +19.17% |
| PumpSwap | Dexs | $372.54M | -2.44% | +18.05% |

## Stablecoins

Solana circulating pegged-USD: **$16.91B**
(1d -2.69% · 7d +4.22%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $8.32B | +4.58% |
| USDT · Tether | $2.14B | +0.00% |
| USDGO · USDGO | $1.42B | +1.00% |
| USD1 · World Liberty Financial USD | $1.38B | +0.73% |
| BUIDL · BlackRock USD | $987.68M | +0.01% |
| PYUSD · PayPal USD | $744.64M | +0.77% |
| USDG · Global Dollar | $631.40M | +0.30% |
| USDe · Ethena USDe | $497.35M | -1.05% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 10 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 10 · priced-subset mcap $102.81K (lower bound, not a census).
24h volume $153.37M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 10 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$543.24M** across 16 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $301.15M
- **Huma** (RWA) — $196.68M
- **Plume Vaults** (RWA) — $28.21M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $2.99M
- **VNX** (RWA) — $2.70M
- **Oro Finance** (RWA) — $2.49M
- **International Stable Currency** (RWA) — $2.44M

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

_As of 2026-09-24 (2026-09-23 19:22:18 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 154ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 133ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 64ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 56ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 84ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6898ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 121ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 58ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 34ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 41ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 32ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 37ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 28ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 76ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 62ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 50ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 82ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 210ms https://solana.com/data
- `solana.com.databricks` [ok] 200 75ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 361ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 56ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 196ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 84ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 204ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 283ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 55ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 52ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 55ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 1663ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1684ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 58ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 36ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 241ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 186ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 26ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 94ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 46ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 146ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 81ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 54ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 178ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 204ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 181ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 131ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 96ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 228ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 139ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 248ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 25ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 106ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 148ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 181ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 73ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 98ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 173ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 169ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 64ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 159ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 125ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 160ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 83ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 135ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 83ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 88ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1856ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 3584ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 3454ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2093ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 3994ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2224ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 3228ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 2293ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.INDIx` [ok] 200 1274ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.PCTx` [ok] 200 1505ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.PCTx` [ok] 200 2933ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 3473ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 1053ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 1076ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.price.BETRx` [ok] 200 498ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.WYFIx` [ok] 200 1865ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.BETRx` [ok] 200 2043ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 686ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.BETRx` [ok] 200 1025ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.MIDDx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data
- `xstocks.circ.AIx` [ok] 200 2340ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.price.FLNCx` [ok] 200 11236ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.WRLDx` [ok] 200 11238ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.XRXx` [ok] 200 11457ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.circ.MIDDx` [ok] 200 1981ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object
- `xstocks.price.METCx` [ok] 200 11649ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.WGSx` [ok] 200 11736ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.QUBTx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.AIx` [ok] 200 1214ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.MIDDx` [ok] 200 845ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana
- `xstocks.price.ALMx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data
- `xstocks.price.RITMx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data
- `xstocks.circ.FLNCx` [ok] 200 1669ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 1633ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 764ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 1974ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 712ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 1951ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 2771ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 2403ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.ALMx` [ok] 200 1781ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object
- `xstocks.price.RNGx` [ok] 200 617ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data
- `xstocks.mult.WGSx` [ok] 200 733ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.SHCx` [ok] 200 844ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data
- `xstocks.price.WHx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/WHx/price-data
- `xstocks.price.REYNx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data
- `xstocks.mult.ALMx` [ok] 200 902ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana
- `xstocks.price.VSNTx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data
- `xstocks.mult.METCx` [ok] 200 1428ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.price.CARx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/CARx/price-data
- `xstocks.mult.QUBTx` [ok] 200 1872ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.circ.VSNTx` [ok] 200 843ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object
- `xstocks.price.OZKx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data
- `xstocks.circ.WHx` [ok] 200 1768ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object
- `xstocks.circ.RNGx` [ok] 200 2595ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object
- `xstocks.circ.SHCx` [ok] 200 2289ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object
- `xstocks.circ.REYNx` [ok] 200 2369ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object
- `xstocks.mult.VSNTx` [ok] 200 1214ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana
- `xstocks.mult.RNGx` [ok] 200 877ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana
- `xstocks.price.IRDMx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data
- `xstocks.mult.WHx` [ok] 200 1646ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana
- `xstocks.circ.CARx` [ok] 200 2315ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object
- `xstocks.price.GXOx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data
- `xstocks.mult.SHCx` [ok] 200 1529ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana
- `xstocks.price.FBINx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data
- `xstocks.mult.REYNx` [ok] 200 1749ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana
- `xstocks.price.AMTMx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data
- `xstocks.mult.CARx` [ok] 200 866ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana
- `xstocks.circ.OZKx` [ok] 200 2799ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object
- `xstocks.price.MTNx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data
- `xstocks.price.PSNx` [ok] 200 596ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data
- `xstocks.circ.IRDMx` [ok] 200 1848ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object
- `xstocks.mult.OZKx` [ok] 200 946ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana
- `xstocks.circ.FBINx` [ok] 200 1541ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object
- `xstocks.price.PEGAx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data
- `xstocks.circ.AMTMx` [ok] 200 1807ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object
- `xstocks.mult.IRDMx` [ok] 200 978ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana
- `xstocks.circ.GXOx` [ok] 200 2485ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object
- `xstocks.circ.MTNx` [ok] 200 1614ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object
- `xstocks.circ.PSNx` [ok] 200 1828ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object
- `xstocks.mult.FBINx` [ok] 200 1217ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana
- `xstocks.price.SAICx` [ok] 200 980ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data
- `xstocks.mult.AMTMx` [ok] 200 1101ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana
- `xstocks.price.EXLSx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data
- `xstocks.mult.MTNx` [ok] 200 1269ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana
- `xstocks.mult.GXOx` [ok] 200 1421ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana
- `xstocks.mult.PSNx` [ok] 200 1014ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana
- `xstocks.price.CRUSx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data
- `xstocks.price.Mx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/Mx/price-data
- `xstocks.price.ELFx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data
- `xstocks.circ.PEGAx` [ok] 200 2766ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object
- `xstocks.price.EPAMx` [ok] 200 1861ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data
- `xstocks.circ.EXLSx` [ok] 200 1726ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object
- `xstocks.circ.SAICx` [ok] 200 2581ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object
- `xstocks.circ.Mx` [ok] 200 1953ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object
- `xstocks.mult.PEGAx` [ok] 200 1614ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana
- `xstocks.circ.RITMx` [FAIL]  12029ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.ELFx` [ok] 200 2242ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object
- `xstocks.price.SNDRx` [ok] 200 619ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data
- `xstocks.mult.EXLSx` [ok] 200 1742ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana
- `xstocks.mult.SAICx` [ok] 200 1362ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana
- `xstocks.circ.EPAMx` [ok] 200 2121ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object
- `xstocks.mult.Mx` [ok] 200 1317ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana
- `xstocks.circ.CRUSx` [ok] 200 3436ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object
- `xstocks.price.EXPx` [ok] 200 686ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data
- `xstocks.price.VNOx` [ok] 200 807ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data
- `xstocks.mult.RITMx` [ok] 200 1610ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana
- `xstocks.mult.ELFx` [ok] 200 1397ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana
- `xstocks.price.VIRTx` [ok] 200 715ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data
- `xstocks.price.MKTXx` [ok] 200 507ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data
- `xstocks.price.HXLx` [ok] 200 645ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data
- `xstocks.mult.EPAMx` [ok] 200 1641ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana
- `xstocks.mult.CRUSx` [ok] 200 1277ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana
- `xstocks.circ.SNDRx` [ok] 200 1965ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object
- `xstocks.price.VFCx` [ok] 200 807ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data
- `xstocks.circ.EXPx` [ok] 200 2136ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object
- `xstocks.price.CPBx` [ok] 200 1111ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data
- `xstocks.circ.VNOx` [ok] 200 2193ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object
- `xstocks.circ.VIRTx` [ok] 200 2115ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object
- `xstocks.circ.HXLx` [ok] 200 1887ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object
- `xstocks.circ.MKTXx` [ok] 200 2145ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object
- `xstocks.mult.SNDRx` [ok] 200 1922ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana
- `xstocks.circ.VFCx` [ok] 200 1793ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object
- `xstocks.mult.EXPx` [ok] 200 1588ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana
- `xstocks.price.NXSTx` [ok] 200 1378ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data
- `xstocks.mult.MKTXx` [ok] 200 1635ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana
- `xstocks.circ.CPBx` [ok] 200 2291ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object
- `xstocks.mult.VNOx` [ok] 200 2315ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana
- `xstocks.mult.VIRTx` [ok] 200 2234ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana
- `xstocks.price.ADTx` [ok] 200 1285ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data
- `xstocks.mult.VFCx` [ok] 200 1566ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana
- `xstocks.mult.HXLx` [ok] 200 2455ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana
- `xstocks.price.BCx` [ok] 200 974ms https://api.backed.fi/api/v2/public/assets/BCx/price-data
- `xstocks.price.ACIx` [ok] 200 1226ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data
- `xstocks.price.GTESx` [ok] 200 687ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data
- `xstocks.circ.ADTx` [ok] 200 1043ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object
- `xstocks.price.KRMNx` [ok] 200 1371ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data
- `xstocks.mult.CPBx` [ok] 200 1647ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana
- `xstocks.price.HRBx` [ok] 200 1314ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data
- `xstocks.circ.NXSTx` [ok] 200 2282ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object
- `xstocks.circ.ACIx` [ok] 200 1120ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object
- `xstocks.circ.BCx` [ok] 200 2048ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object
- `xstocks.mult.ADTx` [ok] 200 1512ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana
- `xstocks.price.AXSx` [ok] 200 1649ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data
- `xstocks.price.DLBx` [ok] 200 845ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data
- `xstocks.mult.NXSTx` [ok] 200 1790ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana
- `xstocks.mult.ACIx` [ok] 200 1704ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana
- `xstocks.mult.BCx` [ok] 200 1687ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana
- `xstocks.circ.KRMNx` [ok] 200 3105ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object
- `xstocks.circ.GTESx` [ok] 200 3545ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object
- `xstocks.circ.HRBx` [ok] 200 2943ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object
- `xstocks.price.POOLx` [ok] 200 1110ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data
- `xstocks.price.TFXx` [ok] 200 581ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data
- `xstocks.circ.AXSx` [ok] 200 2749ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object
- `xstocks.price.RYNx` [ok] 200 2321ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data
- `xstocks.circ.DLBx` [ok] 200 2626ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object
- `xstocks.circ.TFXx` [ok] 200 1436ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object
- `xstocks.mult.KRMNx` [ok] 200 2323ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana
- `xstocks.mult.GTESx` [ok] 200 2059ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana
- `xstocks.mult.HRBx` [ok] 200 2522ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana
- `xstocks.price.LWx` [ok] 200 665ms https://api.backed.fi/api/v2/public/assets/LWx/price-data
- `xstocks.circ.POOLx` [ok] 200 2554ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object
- `xstocks.price.AAONx` [ok] 200 884ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.mult.AXSx` [ok] 200 2094ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana
- `xstocks.circ.RYNx` [ok] 200 2170ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object
- `xstocks.mult.TFXx` [ok] 200 1841ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana
- `xstocks.price.SONx` [ok] 200 1039ms https://api.backed.fi/api/v2/public/assets/SONx/price-data
- `xstocks.mult.DLBx` [ok] 200 2091ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana
- `xstocks.circ.AAONx` [ok] 200 985ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.price.INGMx` [ok] 200 792ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data
- `xstocks.price.TTDx` [ok] 200 591ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data
- `xstocks.price.HRx` [ok] 200 615ms https://api.backed.fi/api/v2/public/assets/HRx/price-data
- `xstocks.mult.POOLx` [ok] 200 2290ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana
- `xstocks.circ.LWx` [ok] 200 2445ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object
- `xstocks.mult.RYNx` [ok] 200 2000ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana
- `xstocks.price.RLIx` [ok] 200 773ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data
- `xstocks.mult.AAONx` [ok] 200 1969ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.circ.SONx` [ok] 200 2464ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object
- `xstocks.circ.HRx` [ok] 200 1851ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object
- `xstocks.circ.INGMx` [ok] 200 2351ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object
- `xstocks.price.CLFx` [ok] 200 851ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data
- `xstocks.circ.TTDx` [ok] 200 2439ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object
- `xstocks.price.STWDx` [ok] 200 1043ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data
- `xstocks.mult.LWx` [ok] 200 2426ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana
- `xstocks.mult.INGMx` [ok] 200 1782ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana
- `xstocks.mult.HRx` [ok] 200 2050ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana
- `xstocks.mult.SONx` [ok] 200 2336ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana
- `xstocks.circ.RLIx` [ok] 200 2738ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object
- `xstocks.price.MSMx` [ok] 200 1202ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data
- `xstocks.circ.CLFx` [ok] 200 2442ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object
- `xstocks.price.CZRx` [ok] 200 1279ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data
- `xstocks.circ.STWDx` [ok] 200 2489ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object
- `xstocks.price.CROXx` [ok] 200 1084ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data
- `xstocks.price.OMFx` [ok] 200 1318ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data
- `xstocks.mult.TTDx` [ok] 200 3230ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana
- `xstocks.price.CHEx` [ok] 200 610ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data
- `xstocks.mult.RLIx` [ok] 200 1902ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana
- `xstocks.mult.CLFx` [ok] 200 2271ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana
- `xstocks.circ.MSMx` [ok] 200 3390ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object
- `xstocks.circ.CZRx` [ok] 200 2898ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object
- `xstocks.price.ALGMx` [ok] 200 1334ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data
- `xstocks.circ.OMFx` [ok] 200 2871ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object
- `xstocks.circ.CHEx` [ok] 200 1981ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object
- `xstocks.circ.CROXx` [ok] 200 3638ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object
- `xstocks.mult.CZRx` [ok] 200 1125ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana
- `xstocks.mult.MSMx` [ok] 200 1189ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana
- `xstocks.mult.OMFx` [ok] 200 1143ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana
- `xstocks.price.BEPCx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data
- `xstocks.mult.CHEx` [ok] 200 1306ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana
- `xstocks.mult.STWDx` [ok] 200 4589ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana
- `xstocks.price.INGRx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data
- `xstocks.circ.ALGMx` [ok] 200 1685ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object
- `xstocks.mult.CROXx` [ok] 200 1105ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana
- `xstocks.price.MTDRx` [ok] 200 730ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data
- `xstocks.price.LYFTx` [ok] 200 545ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data
- `xstocks.price.BYDx` [ok] 200 529ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data
- `xstocks.mult.ALGMx` [ok] 200 1189ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana
- `xstocks.price.STAGx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data
- `xstocks.circ.BEPCx` [ok] 200 2113ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object
- `xstocks.circ.BYDx` [ok] 200 1119ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object
- `xstocks.circ.INGRx` [ok] 200 2264ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object
- `xstocks.mult.BEPCx` [ok] 200 1195ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana
- `xstocks.circ.MTDRx` [ok] 200 2689ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object
- `xstocks.circ.LYFTx` [ok] 200 2663ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object
- `xstocks.circ.STAGx` [ok] 200 1629ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object
- `xstocks.price.FNBx` [ok] 200 591ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data
- `xstocks.mult.BYDx` [ok] 200 1667ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana
- `xstocks.price.MBGLx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data
- `xstocks.mult.LYFTx` [ok] 200 845ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana
- `xstocks.mult.MTDRx` [ok] 200 1111ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana
- `xstocks.mult.STAGx` [ok] 200 847ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana
- `xstocks.mult.INGRx` [ok] 200 1847ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana
- `xstocks.price.CACCx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data
- `xstocks.circ.CACCx` [ok] 200 727ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object
- `xstocks.circ.FNBx` [ok] 200 1932ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object
- `xstocks.circ.MBGLx` [ok] 200 2190ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object
- `xstocks.mult.FNBx` [ok] 200 880ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana
- `xstocks.mult.CACCx` [ok] 200 1429ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana
- `xstocks.price.Gx` [ok] 200 10679ms https://api.backed.fi/api/v2/public/assets/Gx/price-data
- `xstocks.mult.MBGLx` [ok] 200 2404ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana
- `xstocks.circ.Gx` [ok] 200 1652ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object
- `xstocks.mult.Gx` [ok] 200 784ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana
- `xstocks.price.MTGx` [ok] 200 10636ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data
- `xstocks.circ.MTGx` [ok] 200 2110ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object
- `xstocks.mult.MTGx` [ok] 200 1924ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 25ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.XRXx` [ok] 200 45ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 75ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.FLNCx` [ok] 200 74ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.AIx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.WYFIx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.INDIx` [ok] 200 49ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.WGSx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.WRLDx` [ok] 200 47ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jito.tip_floor` [ok] 200 432ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 254ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 45ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 30ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 29ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 67ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 128ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 1208ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
