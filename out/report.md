# Borealis — Solana ecosystem report

**Generated** 2026-09-25T17:21:19Z · 2026-09-25 10:21:19 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-25T17:21:10Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h +3.83%; DEX 24h $2.45B · 1d -4% · vs-7d-ago -5%; slot 268 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **INFO · TPS vs 30d median (solana.com/data tx/86400)** — Current 4,953.43 TPS is +23.1% vs 30d median 4,024.00 TPS (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 450,418,255 |
| Block height | 428,458,139 |
| Block time | 2026-09-25T17:21:10Z |
| Epoch | 1,042 (63.48% · slot 274,255/432,000) |
| Mean TPS (last ~3,600s) | 4,953.4 |
| Mean non-vote TPS | 2,447.2 |
| Median TPS (same window) | 4,967.8 |
| Mean slot time | 268.4 ms |
| Median slot time | 267.9 ms |
| Transaction count (cluster) | 552,555,795,580 |
| Circulating supply | 587,653,359 SOL |
| Total supply | 634,685,953 SOL |
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

- `4YGgmwyq…` · 12.74K SOL · commission 3% · lag 73184 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 130338 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 1619545 slots
- `mrgn4atx…` · 2.21K SOL · commission 0% · lag 1820850 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 1925384 slots
- `ARKk6Rgi…` · 63.93 SOL · commission 10% · lag 396101 slots
- `BbCQMWnf…` · 45.00 SOL · commission 0% · lag 303689 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 1655880 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 20882572 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 188136 slots

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
| Jito tip-floor run-rate (NOT REV) | $11.29M | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 11291770 USD; at p95 floor → 59700694 USD. |
| Protocol fees 24h | $15.98M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $121.39 | coingecko.simple_price |
| 24h change | +3.83% | coingecko.simple_price |
| Market cap | $71.25B | coingecko.simple_price |
| 24h volume | $6.15B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.56B |
| TVL 1d / 7d / 30d | +2.65% / +11.30% / +16.80% |
| DEX volume 24h | $2.45B · 1d -4.00% · vs-7d-ago -5.48% |
| 7d DEX volume | $20.84B · +19.47% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $15.98M |
| Fees 1d / 7d | -1.37% / +13.85% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| BisonFi | $395.08M | +21.96% |
| Orca DEX | $344.60M | -5.86% |
| Raydium AMM | $292.89M | -25.98% |
| Meteora DLMM | $191.04M | -18.24% |
| HumidiFi | $190.33M | +289.09% |
| Manifest Trade | $133.79M | +17.05% |
| PumpSwap | $133.76M | -50.49% |
| pump.fun | $123.23M | +6.93% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.95B | +5.21% | +11.77% |
| Kamino Lend | Lending | $1.46B | +3.05% | +5.62% |
| Raydium AMM | Dexs | $1.35B | +4.17% | +12.62% |
| Jito Liquid Staking | Liquid Staking | $1.25B | +3.83% | +10.68% |
| Binance Staked SOL | Liquid Staking | $1.23B | +5.00% | +8.73% |
| Jupiter Lend | Lending | $1.17B | +0.35% | +3.28% |
| Jupiter Perpetual Exchange | Derivatives | $823.60M | +2.71% | +4.24% |
| Jupiter Staked SOL | Liquid Staking | $624.15M | +4.89% | +9.73% |
| Marinade Native | Staking Pool | $462.90M | +4.99% | +10.59% |
| PumpSwap | Dexs | $390.35M | +5.64% | +13.43% |

## Stablecoins

Solana circulating pegged-USD: **$17.25B**
(1d +7.73% · 7d +12.67%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $8.12B | +8.59% |
| USDT · Tether | $2.67B | +24.81% |
| USDGO · USDGO | $1.41B | -0.71% |
| USD1 · World Liberty Financial USD | $1.38B | -0.00% |
| BUIDL · BlackRock USD | $987.88M | +0.02% |
| PYUSD · PayPal USD | $711.71M | -4.42% |
| USDG · Global Dollar | $696.99M | +10.39% |
| USDe · Ethena USDe | $486.55M | -2.19% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $113.49K (lower bound, not a census).
24h volume $106.76M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$543.60M** across 16 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $298.23M
- **Huma** (RWA) — $200.00M
- **Plume Vaults** (RWA) — $28.17M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $3.04M
- **VNX** (RWA) — $2.69M
- **Oro Finance** (RWA) — $2.47M
- **International Stable Currency** (RWA) — $2.42M

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
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — solana.com/news · Mon, 14 Sep 2026 11:00:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-25 (2026-09-25 10:21:19 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **X / Twitter RSS** — Public X/Nitter-style RSS yielded no usable items this run (403/gated skipped). xcancel.solana 451, xcancel.solana_status 451, xcancel.anza_xyz 451, xcancel.solana_devs 451, nitter.solana 200, nitter.solana_status TimeoutError: The read operation timed out
- **Median tx fee** — no getBlock samples
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 92ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 121ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 53ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 108ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 77ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5070ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 141ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 183ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 124ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 126ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 129ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 55ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1359ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 170ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 64ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 75ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 127ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 379ms https://solana.com/data
- `solana.com.databricks` [ok] 200 1364ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 540ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 144ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 108ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 198ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 353ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 492ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 204ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 206ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 206ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 3597ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [FAIL]  18120ms https://nitter.perennialte.ch/solana_status/rss — TimeoutError: The read operation timed out
- `rss.nitter.anza_xyz` [FAIL] 502 9263ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_devs` [FAIL] 502 239ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 502 Bad Gateway
- `rss.rsshub.solana` [FAIL] 404 282ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 180ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 128ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 94ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 147ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 206ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 137ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 165ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 215ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 364ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 230ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 406ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 242ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 331ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 147ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 364ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 54ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 1055ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 223ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 835ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 228ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 1096ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 251ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 521ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 194ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 377ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 190ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 257ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 181ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 628ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 115ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 646ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 4058ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2865ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2357ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1709ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2152ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1848ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2524ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1642ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.QUBTx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.FLNCx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.WRLDx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.INDIx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.PCTx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.METCx` [ok] 200 544ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.WGSx` [ok] 200 558ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.XRXx` [ok] 200 608ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.circ.WRLDx` [ok] 200 526ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 586ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.XRXx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.mult.METCx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 933ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.PCTx` [ok] 200 632ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.INDIx` [ok] 200 877ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 602ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 1005ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.MIDDx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data
- `xstocks.mult.PCTx` [ok] 200 532ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 610ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 547ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.price.ALMx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data
- `xstocks.price.RITMx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data
- `xstocks.price.BETRx` [ok] 200 815ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.MIDDx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object
- `xstocks.price.RNGx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data
- `xstocks.price.SHCx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data
- `xstocks.circ.RITMx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object
- `xstocks.circ.ALMx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object
- `xstocks.mult.MIDDx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 749ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.RITMx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana
- `xstocks.mult.ALMx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana
- `xstocks.circ.RNGx` [ok] 200 525ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object
- `xstocks.circ.BETRx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.REYNx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data
- `xstocks.mult.RNGx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 1132ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.REYNx` [ok] 200 548ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object
- `xstocks.circ.SHCx` [ok] 200 1192ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.WHx` [ok] 200 1025ms https://api.backed.fi/api/v2/public/assets/WHx/price-data
- `xstocks.price.VSNTx` [ok] 200 892ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data
- `xstocks.price.CARx` [ok] 200 881ms https://api.backed.fi/api/v2/public/assets/CARx/price-data
- `xstocks.circ.WHx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object
- `xstocks.circ.VSNTx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object
- `xstocks.mult.SHCx` [ok] 200 676ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana
- `xstocks.mult.WHx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana
- `xstocks.mult.REYNx` [ok] 200 831ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana
- `xstocks.price.OZKx` [ok] 200 1145ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data
- `xstocks.mult.BETRx` [ok] 200 1488ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.FBINx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data
- `xstocks.price.GXOx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data
- `xstocks.circ.OZKx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object
- `xstocks.price.AMTMx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data
- `xstocks.mult.VSNTx` [ok] 200 664ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana
- `xstocks.price.IRDMx` [ok] 200 1107ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data
- `xstocks.circ.GXOx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object
- `xstocks.mult.OZKx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana
- `xstocks.circ.CARx` [ok] 200 1343ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object
- `xstocks.mult.GXOx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana
- `xstocks.price.PEGAx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data
- `xstocks.price.SAICx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data
- `xstocks.price.PSNx` [ok] 200 924ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data
- `xstocks.circ.PSNx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object
- `xstocks.circ.FBINx` [ok] 200 1865ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object
- `xstocks.circ.AMTMx` [ok] 200 1801ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object
- `xstocks.price.MTNx` [ok] 200 2225ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data
- `xstocks.mult.FBINx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana
- `xstocks.mult.CARx` [ok] 200 1904ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana
- `xstocks.mult.PSNx` [ok] 200 1321ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana
- `xstocks.circ.SAICx` [ok] 200 1643ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object
- `xstocks.price.EXLSx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data
- `xstocks.price.CRUSx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data
- `xstocks.mult.SAICx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana
- `xstocks.circ.MTNx` [ok] 200 840ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object
- `xstocks.circ.PEGAx` [ok] 200 2220ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object
- `xstocks.price.EPAMx` [ok] 200 678ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data
- `xstocks.circ.CRUSx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object
- `xstocks.price.Mx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/Mx/price-data
- `xstocks.circ.EXLSx` [ok] 200 656ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object
- `xstocks.mult.PEGAx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana
- `xstocks.mult.CRUSx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana
- `xstocks.circ.EPAMx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object
- `xstocks.circ.IRDMx` [ok] 200 3246ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object
- `xstocks.mult.EXLSx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana
- `xstocks.price.SNDRx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data
- `xstocks.price.ELFx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data
- `xstocks.circ.Mx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object
- `xstocks.mult.EPAMx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana
- `xstocks.circ.SNDRx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object
- `xstocks.mult.Mx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana
- `xstocks.price.EXPx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data
- `xstocks.price.VIRTx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data
- `xstocks.circ.ELFx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object
- `xstocks.mult.SNDRx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana
- `xstocks.circ.EXPx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object
- `xstocks.circ.VIRTx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object
- `xstocks.mult.IRDMx` [ok] 200 879ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana
- `xstocks.mult.ELFx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana
- `xstocks.mult.VIRTx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana
- `xstocks.price.HXLx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data
- `xstocks.price.VFCx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data
- `xstocks.mult.AMTMx` [ok] 200 2885ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana
- `xstocks.price.MKTXx` [ok] 200 623ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data
- `xstocks.price.VNOx` [ok] 200 1237ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data
- `xstocks.circ.HXLx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object
- `xstocks.price.NXSTx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data
- `xstocks.mult.MTNx` [ok] 200 2128ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana
- `xstocks.circ.MKTXx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object
- `xstocks.mult.HXLx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana
- `xstocks.price.CPBx` [ok] 200 811ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data
- `xstocks.mult.EXPx` [ok] 200 1089ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana
- `xstocks.price.ADTx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data
- `xstocks.circ.NXSTx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object
- `xstocks.mult.MKTXx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana
- `xstocks.circ.CPBx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object
- `xstocks.price.BCx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/BCx/price-data
- `xstocks.price.ACIx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data
- `xstocks.price.KRMNx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data
- `xstocks.mult.CPBx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana
- `xstocks.mult.NXSTx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana
- `xstocks.circ.BCx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object
- `xstocks.price.HRBx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data
- `xstocks.price.GTESx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data
- `xstocks.circ.HRBx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object
- `xstocks.mult.BCx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana
- `xstocks.circ.GTESx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object
- `xstocks.mult.HRBx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana
- `xstocks.circ.VFCx` [ok] 200 1697ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object
- `xstocks.price.DLBx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data
- `xstocks.mult.GTESx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana
- `xstocks.price.AXSx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data
- `xstocks.circ.DLBx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object
- `xstocks.price.RYNx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data
- `xstocks.circ.AXSx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object
- `xstocks.circ.ACIx` [ok] 200 1523ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object
- `xstocks.circ.RYNx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object
- `xstocks.mult.AXSx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana
- `xstocks.mult.RYNx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana
- `xstocks.circ.VNOx` [ok] 200 2662ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object
- `xstocks.mult.VFCx` [ok] 200 1023ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana
- `xstocks.price.POOLx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data
- `xstocks.price.TFXx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data
- `xstocks.price.LWx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/LWx/price-data
- `xstocks.circ.KRMNx` [ok] 200 2075ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object
- `xstocks.mult.DLBx` [ok] 200 947ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana
- `xstocks.mult.VNOx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana
- `xstocks.mult.ACIx` [ok] 200 750ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana
- `xstocks.circ.TFXx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object
- `xstocks.price.AAONx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.circ.POOLx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object
- `xstocks.price.INGMx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data
- `xstocks.mult.TFXx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana
- `xstocks.circ.AAONx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.circ.INGMx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object
- `xstocks.mult.KRMNx` [ok] 200 583ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana
- `xstocks.mult.POOLx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana
- `xstocks.price.TTDx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data
- `xstocks.price.HRx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/HRx/price-data
- `xstocks.mult.INGMx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana
- `xstocks.circ.ADTx` [ok] 200 3218ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object
- `xstocks.price.SONx` [ok] 200 758ms https://api.backed.fi/api/v2/public/assets/SONx/price-data
- `xstocks.circ.TTDx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object
- `xstocks.price.RLIx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data
- `xstocks.price.CLFx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data
- `xstocks.circ.HRx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object
- `xstocks.mult.ADTx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana
- `xstocks.mult.AAONx` [ok] 200 532ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.circ.LWx` [ok] 200 1157ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object
- `xstocks.mult.TTDx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana
- `xstocks.circ.RLIx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object
- `xstocks.price.STWDx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data
- `xstocks.price.MSMx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data
- `xstocks.mult.LWx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana
- `xstocks.circ.CLFx` [ok] 200 427ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object
- `xstocks.mult.RLIx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana
- `xstocks.circ.MSMx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object
- `xstocks.price.OMFx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data
- `xstocks.price.CZRx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data
- `xstocks.mult.CLFx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana
- `xstocks.circ.SONx` [ok] 200 829ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object
- `xstocks.price.CROXx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data
- `xstocks.mult.MSMx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana
- `xstocks.circ.CZRx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object
- `xstocks.circ.OMFx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object
- `xstocks.circ.CROXx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object
- `xstocks.mult.SONx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana
- `xstocks.mult.OMFx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana
- `xstocks.mult.CZRx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana
- `xstocks.price.CHEx` [ok] 200 640ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data
- `xstocks.price.ALGMx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data
- `xstocks.price.MTGx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data
- `xstocks.price.BEPCx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data
- `xstocks.circ.ALGMx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object
- `xstocks.mult.CROXx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana
- `xstocks.circ.CHEx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object
- `xstocks.circ.MTGx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object
- `xstocks.circ.BEPCx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object
- `xstocks.price.Gx` [ok] 200 923ms https://api.backed.fi/api/v2/public/assets/Gx/price-data
- `xstocks.mult.HRx` [ok] 200 1711ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana
- `xstocks.mult.ALGMx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana
- `xstocks.price.INGRx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data
- `xstocks.circ.STWDx` [ok] 200 1723ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object
- `xstocks.mult.CHEx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana
- `xstocks.price.MTDRx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data
- `xstocks.mult.BEPCx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana
- `xstocks.circ.INGRx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object
- `xstocks.mult.STWDx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana
- `xstocks.price.STAGx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data
- `xstocks.mult.MTGx` [ok] 200 697ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana
- `xstocks.price.LYFTx` [ok] 200 617ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data
- `xstocks.circ.STAGx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object
- `xstocks.price.MBGLx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data
- `xstocks.price.BYDx` [ok] 200 609ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data
- `xstocks.price.FNBx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data
- `xstocks.circ.Gx` [ok] 200 931ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object
- `xstocks.circ.MBGLx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object
- `xstocks.circ.FNBx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object
- `xstocks.circ.BYDx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object
- `xstocks.mult.INGRx` [ok] 200 750ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana
- `xstocks.mult.Gx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana
- `xstocks.mult.MBGLx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana
- `xstocks.mult.FNBx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana
- `xstocks.mult.BYDx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana
- `xstocks.price.CACCx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data
- `xstocks.circ.MTDRx` [ok] 200 1325ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object
- `xstocks.mult.STAGx` [ok] 200 847ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana
- `xstocks.circ.CACCx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object
- `xstocks.mult.MTDRx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana
- `xstocks.mult.CACCx` [ok] 200 475ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana
- `xstocks.circ.LYFTx` [ok] 200 1566ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object
- `xstocks.mult.LYFTx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 5996ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 270ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.XRXx` [ok] 200 133ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.QUBTx` [ok] 200 150ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.FLNCx` [ok] 200 130ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.BETRx` [ok] 200 137ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.WGSx` [ok] 200 143ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.WYFIx` [ok] 200 139ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.AIx` [ok] 200 138ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.WRLDx` [ok] 200 151ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jito.tip_floor` [ok] 200 431ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 379ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 144ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 58ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 64ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 61ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 53ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 232ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
