# Borealis — Solana ecosystem report

**Generated** 2026-09-24T08:50:20Z · 2026-09-24 01:50:20 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-24T08:50:11Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -3.22%; DEX 24h $2.68B · 1d -16% · vs-7d-ago -4%; slot 265 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -16.03%. (threshold: `|1d %| >= 8`)
- **WARN · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -3.22%, DeFiLlama TVL 1d -2.03%, DEX 1d -16.03%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 449,979,468 |
| Block height | 428,019,589 |
| Block time | 2026-09-24T08:50:11Z |
| Epoch | 1,041 (61.91% · slot 267,469/432,000) |
| Mean TPS (last ~3,600s) | 4,117.4 |
| Mean non-vote TPS | 1,578.2 |
| Median TPS (same window) | 4,072.7 |
| Mean slot time | 265.2 ms |
| Median slot time | 265.5 ms |
| Transaction count (cluster) | 552,031,328,189 |
| Circulating supply | 587,577,338 SOL |
| Total supply | 634,608,450 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 11 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,764,444 SOL |
| Delinquent stake | 199,692.69 SOL (0.045%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.39% / 35.68% |
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
| 14 | `5Cchr1XG…` | 5.61M SOL | 1.27% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `6DTkuiey…` · 89.15K SOL · commission 100% · lag 449979468 slots
- `HDRqPft5…` · 71.15K SOL · commission 100% · lag 449979468 slots
- `t23p8aBQ…` · 14.37K SOL · commission 0% · lag 2384232 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 47627 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 1180758 slots
- `mrgn4atx…` · 2.21K SOL · commission 0% · lag 1382063 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 2104716 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 1486597 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 1217093 slots
- `R1parD2C…` · 2.87 SOL · commission 5% · lag 65930598 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 74960 slots

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
| Jito tip-floor run-rate (NOT REV) | $41.80K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 41800 USD; at p95 floor → 1644310 USD. |
| Protocol fees 24h | $16.52M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $113.79 | coingecko.simple_price |
| 24h change | -3.22% | coingecko.simple_price |
| Market cap | $66.85B | coingecko.simple_price |
| 24h volume | $4.79B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.40B |
| TVL 1d / 7d / 30d | -2.03% / +10.72% / +11.34% |
| DEX volume 24h | $2.68B · 1d -16.03% · vs-7d-ago -4.17% |
| 7d DEX volume | $19.96B · +11.85% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $16.52M |
| Fees 1d / 7d | -7.58% / +10.91% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| Raydium AMM | $370.01M | -22.25% |
| BisonFi | $368.17M | 0.00% |
| Orca DEX | $355.43M | -3.31% |
| PumpSwap | $270.19M | -57.39% |
| Meteora DLMM | $233.66M | -12.43% |
| Scorch | $129.41M | 0.00% |
| fomo Wallet | $125.97M | -14.79% |
| pump.fun | $121.03M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.85B | -1.76% | +16.83% |
| Kamino Lend | Lending | $1.41B | -1.28% | +5.11% |
| Raydium AMM | Dexs | $1.31B | -2.67% | +17.47% |
| Jito Liquid Staking | Liquid Staking | $1.19B | -2.75% | +15.98% |
| Binance Staked SOL | Liquid Staking | $1.18B | -3.26% | +14.34% |
| Jupiter Lend | Lending | $1.17B | -2.44% | +7.87% |
| Jupiter Perpetual Exchange | Derivatives | $804.09M | -2.19% | +8.45% |
| Jupiter Staked SOL | Liquid Staking | $596.60M | -2.63% | +15.78% |
| Marinade Native | Staking Pool | $442.46M | -2.76% | +16.52% |
| PumpSwap | Dexs | $376.74M | -1.35% | +17.40% |

## Stablecoins

Solana circulating pegged-USD: **$16.13B**
(1d -2.70% · 7d +4.21%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.55B | -5.07% |
| USDT · Tether | $2.14B | +0.00% |
| USDGO · USDGO | $1.42B | +1.00% |
| USD1 · World Liberty Financial USD | $1.38B | +0.73% |
| BUIDL · BlackRock USD | $987.68M | +0.01% |
| PYUSD · PayPal USD | $735.44M | -0.47% |
| USDG · Global Dollar | $631.44M | +0.30% |
| USDe · Ethena USDe | $496.72M | -1.17% |

## Tokenized equities (xStocks)

HTTP 503 Service Unavailable
Listed 0 · Solana deployments 0 · priced 0 · priced-subset mcap — (lower bound, not a census).
24h volume $151.93M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok None / mcap_computable None of attempted None; missing multiplier → mcap omitted, never silent 1.0).  

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$543.25M** across 16 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $301.16M
- **Huma** (RWA) — $196.70M
- **Plume Vaults** (RWA) — $28.21M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $2.98M
- **VNX** (RWA) — $2.70M
- **Oro Finance** (RWA) — $2.49M
- **International Stable Currency** (RWA) — $2.42M

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

_As of 2026-09-24 (2026-09-24 01:50:20 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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
- **Tokenized equities (xStocks)** — HTTP 503 Service Unavailable
- **xStocks** — asset list failed on backed.fi and xstocks.fi

## Sources this run

- `rpc.getHealth` [ok] 200 143ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 92ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 199ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 88ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 97ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5293ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 149ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 161ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 63ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 85ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 53ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 52ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1313ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 166ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 86ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 92ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 116ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 429ms https://solana.com/data
- `solana.com.databricks` [ok] 200 433ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 1900ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 133ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 112ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 117ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 374ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 404ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 208ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 225ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 207ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 5033ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1471ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 113ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 481ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 279ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 262ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 72ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 62ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 122ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 172ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 97ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 148ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 308ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 298ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 178ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 202ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 174ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 242ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 173ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 191ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 64ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 285ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 161ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 282ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 263ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 192ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 157ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 180ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 190ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 195ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 125ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 180ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 114ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 177ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 96ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 196ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [FAIL] 503 266ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0 — HTTP 503 Service Unavailable
- `xstocks.assets.p0` [FAIL] 503 574ms https://api.xstocks.fi/api/v2/public/assets?pageSize=100&page=0 — HTTP 503 Service Unavailable
- `llama.protocol.xstocks` [ok] 200 54ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 252ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jito.tip_floor` [ok] 200 160ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 348ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 312ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 116ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 60ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 107ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 66ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 2181ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
