# Borealis — Solana ecosystem report

**Generated** 2026-09-26T01:56:54Z · 2026-09-25 18:56:54 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-26T01:56:45Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +4.00%; DEX 24h $2.80B · 1d +14% · vs-7d-ago -21%; slot 271 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -20.84%. (threshold: `|7d %| >= 20`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +14.26%. (threshold: `|1d %| >= 8`)
- **INFO · TPS vs 30d median (solana.com/data tx/86400)** — Current 5,134.29 TPS is +27.5% vs 30d median 4,027.08 TPS (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 450,533,545 |
| Block height | 428,573,374 |
| Block time | 2026-09-26T01:56:45Z |
| Epoch | 1,042 (90.17% · slot 389,546/432,000) |
| Mean TPS (last ~3,600s) | 5,134.3 |
| Mean non-vote TPS | 2,653.2 |
| Median TPS (same window) | 5,183.9 |
| Mean slot time | 270.5 ms |
| Median slot time | 269.1 ms |
| Transaction count (cluster) | 552,700,617,655 |
| Circulating supply | 587,641,816 SOL |
| Total supply | 634,685,574 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 10 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 440,600,850 SOL |
| Delinquent stake | 36,345.69 SOL (0.008%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.41% / 35.63% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.82M SOL | 4.04% | 7% | 0 |
| 2 | `HEL1USMZ…` | 15.82M SOL | 3.59% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.39M SOL | 2.81% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.27M SOL | 2.56% | 5% | 0 |
| 5 | `E1r4Psq8…` | 10.60M SOL | 2.40% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.22M SOL | 2.09% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.16M SOL | 2.08% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.60M SOL | 1.72% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.09M SOL | 1.61% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.56M SOL | 1.49% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.15M SOL | 1.40% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.00M SOL | 1.36% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.35% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.62M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `4YGgmwyq…` · 12.74K SOL · commission 3% · lag 188474 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 67141 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 1734835 slots
- `mrgn4atx…` · 2.21K SOL · commission 0% · lag 1936140 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 2040674 slots
- `ARKk6Rgi…` · 63.93 SOL · commission 10% · lag 511391 slots
- `BbCQMWnf…` · 45.00 SOL · commission 0% · lag 60354 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 1771170 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 20997862 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 303426 slots

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
| **In-protocol fees 24h** | **$927.47K** (8,115.7 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-24 |
| **Solana REV** | **10,029.2 SOL** / **$1.15M** | MEASURED UTC calendar day 2026-09-24: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-24 · UTC day 2026-09-24 · SOL-USD date 2026-09-24 |
| Jito tip-floor run-rate (NOT REV) | $1.07M | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 1065390 USD; at p95 floor → 6488571 USD. |
| Protocol fees 24h | $14.94M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $122.03 | coingecko.simple_price |
| 24h change | +4.00% | coingecko.simple_price |
| Market cap | $71.69B | coingecko.simple_price |
| 24h volume | $6.40B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.64B |
| TVL 1d / 7d / 30d | +1.02% / +5.31% / +14.76% |
| DEX volume 24h | $2.80B · 1d +14.26% · vs-7d-ago -20.84% |
| 7d DEX volume | $18.90B · +6.77% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.94M |
| Fees 1d / 7d | -6.50% / -14.24% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $425.99M | +218.47% |
| BisonFi | $395.08M | 0.00% |
| Orca DEX | $385.91M | +20.40% |
| Raydium AMM | $293.77M | -14.41% |
| Meteora DLMM | $204.57M | +7.08% |
| HumidiFi | $190.33M | 0.00% |
| Manifest Trade | $147.34M | +35.89% |
| fomo Wallet | $145.21M | +33.79% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.99B | +5.81% | +10.44% |
| Kamino Lend | Lending | $1.47B | +3.30% | -3.17% |
| Raydium AMM | Dexs | $1.36B | +2.59% | +8.21% |
| Jito Liquid Staking | Liquid Staking | $1.27B | +4.19% | +8.53% |
| Binance Staked SOL | Liquid Staking | $1.25B | +5.13% | +7.18% |
| Jupiter Lend | Lending | $1.19B | +0.52% | +4.44% |
| Jupiter Perpetual Exchange | Derivatives | $831.28M | +2.17% | +3.90% |
| Jupiter Staked SOL | Liquid Staking | $633.68M | +4.12% | +7.99% |
| Marinade Native | Staking Pool | $469.79M | +5.10% | +8.77% |
| PumpSwap | Dexs | $398.48M | +3.70% | +8.76% |

## Stablecoins

Solana circulating pegged-USD: **$16.64B**
(1d -3.95% · 7d +7.11%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.47B | -9.29% |
| USDT · Tether | $2.67B | +0.00% |
| USDGO · USDGO | $1.41B | -0.71% |
| USD1 · World Liberty Financial USD | $1.39B | +0.72% |
| BUIDL · BlackRock USD | $987.88M | +0.01% |
| PYUSD · PayPal USD | $778.25M | +5.87% |
| USDG · Global Dollar | $667.47M | +5.00% |
| USDe · Ethena USDe | $483.21M | -2.11% |

## Tokenized equities (xStocks)


Listed 800 · Solana deployments 800 · priced 0 · priced-subset mcap — (lower bound, not a census).
24h volume $100.86M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 0 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$546.45M** across 15 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $296.56M
- **Huma** (RWA) — $209.91M
- **Plume Vaults** (RWA) — $25.45M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $3.06M
- **Oro Finance** (RWA) — $2.47M
- **International Stable Currency** (RWA) — $2.44M
- **Byzanlink RWA Markets** (RWA) — $891.62K

## Daily active addresses

773,786 (Allium, as of 2026-09-24). Provider range 414,000–872,265. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — solana.com/news · Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — solana.com/news · Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — solana.com/news · Sat, 19 Sep 2026 11:28:00 GMT `mainnet`
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — solana.com/news · Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — solana.com/news · Wed, 16 Sep 2026 00:56:00 GMT
- [Solana Summer School 2026: From first program to demo day](https://solana.com/news/solana-summer-school-2026) — solana.com/news · Mon, 14 Sep 2026 12:00:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — solana.com/news · Mon, 14 Sep 2026 11:00:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-26 (2026-09-25 18:56:54 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=live, 200ms=pending. Observed mean slot ~270 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~270 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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
- **xStocks market cap** — Listed Solana-deployed xStocks but quote and/or circulating missing. Mcap omitted.
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.
- **xStocks** — price, circulating-supply, and/or currentMultiplier missing — market cap omitted (never assumed multiplier=1.0)

## Sources this run

- `rpc.getHealth` [ok] 200 176ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 214ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 194ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 208ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 293ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5825ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 309ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 121ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 77ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 115ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 918ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 58ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1004ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 144ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 102ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 86ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 183ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 308ms https://solana.com/data
- `solana.com.databricks` [ok] 200 1355ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 545ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 111ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 125ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 131ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 353ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 324ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 124ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 117ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 117ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 4381ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2006ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1551ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 994ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 276ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 120ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 176ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 145ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 160ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 135ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 187ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 120ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 260ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 208ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 239ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 201ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 274ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 336ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 229ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 353ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 129ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 376ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 217ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 283ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 211ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 271ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 298ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 274ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 236ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 216ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 214ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 195ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 219ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 216ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 181ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 177ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 2095ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1448ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1275ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1250ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1407ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1682ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1332ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 2542ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.INDIx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WGSx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WRLDx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.FLNCx` [FAIL]  12029ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PCTx` [FAIL]  12034ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METCx` [FAIL]  12034ms https://api.backed.fi/api/v2/public/assets/METCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.XRXx` [FAIL]  12037ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.QUBTx` [FAIL]  12042ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.METCx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.mult.METCx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 696ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.INDIx` [ok] 200 1220ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 1216ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 1521ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.WYFIx` [FAIL]  12040ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BETRx` [FAIL]  12040ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WYFIx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.AIx` [FAIL]  12029ms https://api.backed.fi/api/v2/public/assets/AIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MIDDx` [FAIL]  12039ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AIx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.ALMx` [FAIL]  12049ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.AIx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.WHx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/WHx/price-data
- `xstocks.circ.ALMx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object
- `xstocks.circ.MIDDx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object
- `xstocks.circ.WHx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object
- `xstocks.mult.ALMx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana
- `xstocks.price.RITMx` [FAIL]  12033ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.RNGx` [FAIL]  12048ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BETRx` [ok] 200 1015ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.RITMx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object
- `xstocks.circ.RNGx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object
- `xstocks.mult.MIDDx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana
- `xstocks.mult.RITMx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana
- `xstocks.price.SHCx` [FAIL]  12044ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.RNGx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana
- `xstocks.mult.BETRx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.circ.SHCx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object
- `xstocks.mult.SHCx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana
- `xstocks.price.FBINx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data
- `xstocks.circ.FBINx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object
- `xstocks.mult.WHx` [ok] 200 2403ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana
- `xstocks.mult.FBINx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana
- `xstocks.price.AMTMx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data
- `xstocks.circ.AMTMx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object
- `xstocks.mult.AMTMx` [ok] 200 2124ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana
- `xstocks.price.PSNx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data
- `xstocks.circ.PSNx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object
- `xstocks.mult.PSNx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana
- `xstocks.price.REYNx` [FAIL]  12037ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.REYNx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object
- `xstocks.price.VSNTx` [FAIL]  12039ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.REYNx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana
- `xstocks.circ.VSNTx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object
- `xstocks.price.CARx` [FAIL]  12038ms https://api.backed.fi/api/v2/public/assets/CARx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.VSNTx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana
- `xstocks.price.OZKx` [FAIL]  12040ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.IRDMx` [FAIL]  12035ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CARx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object
- `xstocks.circ.OZKx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object
- `xstocks.circ.IRDMx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object
- `xstocks.price.GXOx` [FAIL]  12035ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.IRDMx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana
- `xstocks.mult.OZKx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana
- `xstocks.mult.CARx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana
- `xstocks.circ.GXOx` [ok] 200 428ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object
- `xstocks.price.Mx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/Mx/price-data
- `xstocks.circ.Mx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object
- `xstocks.price.EPAMx` [ok] 200 697ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data
- `xstocks.circ.EPAMx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object
- `xstocks.mult.EPAMx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana
- `xstocks.mult.GXOx` [ok] 200 1009ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana
- `xstocks.price.MTNx` [FAIL]  12038ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ELFx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data
- `xstocks.circ.MTNx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object
- `xstocks.price.SNDRx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data
- `xstocks.circ.SNDRx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object
- `xstocks.mult.MTNx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana
- `xstocks.mult.SNDRx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana
- `xstocks.circ.ELFx` [ok] 200 637ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object
- `xstocks.mult.ELFx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana
- `xstocks.mult.Mx` [ok] 200 1698ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana
- `xstocks.price.PEGAx` [FAIL]  12037ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.PEGAx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object
- `xstocks.mult.PEGAx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana
- `xstocks.price.HXLx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data
- `xstocks.circ.HXLx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object
- `xstocks.mult.HXLx` [ok] 200 1693ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana
- `xstocks.price.SAICx` [FAIL]  12036ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SAICx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object
- `xstocks.price.EXLSx` [FAIL]  12035ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SAICx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana
- `xstocks.circ.EXLSx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object
- `xstocks.price.VFCx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data
- `xstocks.circ.VFCx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object
- `xstocks.mult.EXLSx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana
- `xstocks.price.CRUSx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CRUSx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object
- `xstocks.mult.VFCx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana
- `xstocks.price.ADTx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data
- `xstocks.circ.ADTx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object
- `xstocks.mult.ADTx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana
- `xstocks.mult.CRUSx` [ok] 200 854ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana
- `xstocks.price.VNOx` [FAIL]  12034ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.EXPx` [FAIL]  12041ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BCx` [ok] 200 1018ms https://api.backed.fi/api/v2/public/assets/BCx/price-data
- `xstocks.circ.VNOx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object
- `xstocks.circ.EXPx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object
- `xstocks.circ.BCx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object
- `xstocks.price.VIRTx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MKTXx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.EXPx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana
- `xstocks.circ.VIRTx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object
- `xstocks.circ.MKTXx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object
- `xstocks.mult.BCx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana
- `xstocks.mult.MKTXx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana
- `xstocks.mult.VIRTx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana
- `xstocks.price.HRBx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data
- `xstocks.price.AXSx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data
- `xstocks.mult.VNOx` [ok] 200 820ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana
- `xstocks.circ.HRBx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object
- `xstocks.circ.AXSx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object
- `xstocks.price.GTESx` [ok] 200 574ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data
- `xstocks.mult.HRBx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana
- `xstocks.circ.GTESx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object
- `xstocks.mult.AXSx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana
- `xstocks.price.RYNx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data
- `xstocks.circ.RYNx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object
- `xstocks.mult.GTESx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana
- `xstocks.mult.RYNx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana
- `xstocks.price.LWx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/LWx/price-data
- `xstocks.circ.LWx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object
- `xstocks.mult.LWx` [ok] 200 661ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana
- `xstocks.price.CPBx` [FAIL]  12031ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CPBx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object
- `xstocks.mult.CPBx` [ok] 200 475ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana
- `xstocks.price.NXSTx` [FAIL]  12032ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.NXSTx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object
- `xstocks.mult.NXSTx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana
- `xstocks.price.ACIx` [FAIL]  12036ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ACIx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object
- `xstocks.price.KRMNx` [FAIL]  12039ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.KRMNx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object
- `xstocks.mult.ACIx` [ok] 200 1442ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana
- `xstocks.price.DLBx` [FAIL]  12038ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.KRMNx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana
- `xstocks.circ.DLBx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object
- `xstocks.mult.DLBx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana
- `xstocks.price.POOLx` [FAIL]  12040ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.RLIx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data
- `xstocks.circ.RLIx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object
- `xstocks.circ.POOLx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object
- `xstocks.price.TFXx` [FAIL]  12046ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.RLIx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana
- `xstocks.mult.POOLx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana
- `xstocks.circ.TFXx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object
- `xstocks.mult.TFXx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana
- `xstocks.price.MSMx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data
- `xstocks.circ.MSMx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object
- `xstocks.price.AAONx` [FAIL]  12039ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AAONx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.mult.MSMx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana
- `xstocks.mult.AAONx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.price.OMFx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data
- `xstocks.circ.OMFx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object
- `xstocks.mult.OMFx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana
- `xstocks.price.SONx` [FAIL]  12038ms https://api.backed.fi/api/v2/public/assets/SONx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SONx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object
- `xstocks.mult.SONx` [ok] 200 930ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana
- `xstocks.price.CHEx` [ok] 200 887ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data
- `xstocks.circ.CHEx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object
- `xstocks.mult.CHEx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana
- `xstocks.price.Gx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/Gx/price-data
- `xstocks.circ.Gx` [ok] 200 1344ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object
- `xstocks.mult.Gx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana
- `xstocks.price.INGMx` [FAIL]  12045ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.INGMx` [ok] 200 1505ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object
- `xstocks.mult.INGMx` [ok] 200 762ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana
- `xstocks.price.TTDx` [FAIL]  12055ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HRx` [FAIL]  12033ms https://api.backed.fi/api/v2/public/assets/HRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.TTDx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object
- `xstocks.mult.TTDx` [ok] 200 549ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana
- `xstocks.price.CLFx` [FAIL]  12038ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.STWDx` [FAIL]  12048ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CLFx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object
- `xstocks.circ.STWDx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object
- `xstocks.circ.HRx` [ok] 200 1465ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object
- `xstocks.mult.CLFx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana
- `xstocks.mult.STWDx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana
- `xstocks.mult.HRx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana
- `xstocks.price.CZRx` [FAIL]  12031ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CZRx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object
- `xstocks.mult.CZRx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana
- `xstocks.price.CROXx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CROXx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object
- `xstocks.mult.CROXx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana
- `xstocks.price.ALGMx` [FAIL]  12036ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ALGMx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object
- `xstocks.mult.ALGMx` [ok] 200 764ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana
- `xstocks.price.FNBx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data
- `xstocks.circ.FNBx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object
- `xstocks.mult.FNBx` [ok] 200 431ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana
- `xstocks.price.MBGLx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data
- `xstocks.circ.MBGLx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object
- `xstocks.mult.MBGLx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana
- `xstocks.price.MTGx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MTGx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object
- `xstocks.price.BEPCx` [FAIL]  12043ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MTGx` [ok] 200 792ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana
- `xstocks.circ.BEPCx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object
- `xstocks.mult.BEPCx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana
- `xstocks.price.MTDRx` [FAIL]  12040ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.INGRx` [FAIL]  12049ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MTDRx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object
- `xstocks.circ.INGRx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object
- `xstocks.price.LYFTx` [FAIL]  12040ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.LYFTx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object
- `xstocks.mult.MTDRx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana
- `xstocks.mult.INGRx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana
- `xstocks.mult.LYFTx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana
- `xstocks.price.BYDx` [FAIL]  12038ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BYDx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object
- `xstocks.mult.BYDx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana
- `xstocks.price.STAGx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.STAGx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object
- `xstocks.mult.STAGx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana
- `xstocks.price.CACCx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CACCx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object
- `xstocks.mult.CACCx` [ok] 200 938ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 604ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 187ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.WGSx` [ok] 200 91ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.METCx` [ok] 200 87ms https://lite-api.jup.ag/tokens/v2/search?query=METCx
- `jup.tokens.search.XRXx` [ok] 200 81ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.PCTx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.WRLDx` [ok] 200 89ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.INDIx` [ok] 200 92ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.FLNCx` [ok] 200 101ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.QUBTx` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jito.tip_floor` [ok] 200 121ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 258ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 163ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 120ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 120ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 133ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 125ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 1475ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
