# Borealis — Solana ecosystem report

**Generated** 2026-09-23T12:41:38Z · 2026-09-23 05:41:38 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-23T12:41:31Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h -0.15%; DEX 24h $3.20B · 1d -7% · vs-7d-ago +18%; slot 264 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +23.87%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 449,706,416 |
| Block height | 427,746,686 |
| Block time | 2026-09-23T12:41:31Z |
| Epoch | 1,040 (98.71% · slot 426,430/432,000) |
| Mean TPS (last ~3,600s) | 4,167.9 |
| Mean non-vote TPS | 1,627.2 |
| Median TPS (same window) | 4,198.9 |
| Mean slot time | 264.4 ms |
| Median slot time | 264.3 ms |
| Transaction count (cluster) | 551,702,357,583 |
| Circulating supply | 587,506,769 SOL |
| Total supply | 634,530,397 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,661,998 SOL |
| Delinquent stake | 199,750.97 SOL (0.045%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.33% / 35.64% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.83M SOL | 4.05% | 7% | 0 |
| 2 | `HEL1USMZ…` | 15.84M SOL | 3.60% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.35M SOL | 2.81% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.27M SOL | 2.56% | 5% | 0 |
| 5 | `E1r4Psq8…` | 10.21M SOL | 2.32% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.21M SOL | 2.10% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.14M SOL | 2.08% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.46M SOL | 1.70% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.09M SOL | 1.61% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.56M SOL | 1.49% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.25M SOL | 1.42% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.23M SOL | 1.42% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.35% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.62M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `6DTkuiey…` · 89.15K SOL · commission 100% · lag 449706416 slots
- `HDRqPft5…` · 71.15K SOL · commission 100% · lag 449706416 slots
- `t23p8aBQ…` · 14.37K SOL · commission 0% · lag 2111180 slots
- `AYY1TCe3…` · 10.71K SOL · commission 0% · lag 151275 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 907706 slots
- `mrgn4atx…` · 2.26K SOL · commission 0% · lag 1109011 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 1831664 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 1213545 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 944041 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 20170733 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 126907 slots
- `CQYPRQ4v…` · 1.00 SOL · commission 100% · lag 405972 slots

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
| Jito tip-floor run-rate (NOT REV) | $19.57K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 19573 USD; at p95 floor → 16461577 USD. |
| Protocol fees 24h | $17.78M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $117.09 | coingecko.simple_price |
| 24h change | -0.15% | coingecko.simple_price |
| Market cap | $68.79B | coingecko.simple_price |
| 24h volume | $4.51B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.50B |
| TVL 1d / 7d / 30d | +0.83% / +13.76% / +16.83% |
| DEX volume 24h | $3.20B · 1d -6.82% · vs-7d-ago +18.18% |
| 7d DEX volume | $21.22B · +17.10% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $17.78M |
| Fees 1d / 7d | -4.61% / +23.87% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $634.15M | +62.55% |
| Raydium AMM | $380.06M | -33.70% |
| BisonFi | $368.17M | -17.60% |
| Orca DEX | $332.75M | -26.55% |
| Meteora DLMM | $266.83M | +2.78% |
| fomo Wallet | $152.98M | -4.59% |
| Scorch | $129.41M | -14.10% |
| pump.fun | $121.03M | -0.93% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.87B | +0.35% | +20.73% |
| Kamino Lend | Lending | $1.42B | +0.25% | +7.08% |
| Raydium AMM | Dexs | $1.33B | +1.12% | +22.08% |
| Jito Liquid Staking | Liquid Staking | $1.21B | +0.47% | +21.10% |
| Binance Staked SOL | Liquid Staking | $1.20B | +0.43% | +19.29% |
| Jupiter Lend | Lending | $1.18B | +0.27% | +9.91% |
| Jupiter Perpetual Exchange | Derivatives | $815.04M | +0.27% | +11.75% |
| Jupiter Staked SOL | Liquid Staking | $606.24M | +0.47% | +20.68% |
| Marinade Native | Staking Pool | $450.13M | +1.00% | +21.58% |
| PumpSwap | Dexs | $390.56M | +4.73% | +24.48% |

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
| PYUSD · PayPal USD | $734.15M | +0.38% |
| USDG · Global Dollar | $630.05M | +1.51% |
| USDe · Ethena USDe | $500.04M | -0.41% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $117.98K (lower bound, not a census).
24h volume $142.97M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$536.86M** across 16 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $303.06M
- **Huma Finance V2** (RWA) — $188.39M
- **Plume Vaults** (RWA) — $28.20M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $3.01M
- **VNX** (RWA) — $2.72M
- **Oro Finance** (RWA) — $2.49M
- **International Stable Currency** (RWA) — $2.41M

## Daily active addresses

871,580 (Allium, as of 2026-09-21). Provider range 427,586–892,240. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

_As of 2026-09-23 (2026-09-23 05:41:38 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=live, 200ms=pending. Observed mean slot ~264 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~264 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 605ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 3145ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 675ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 3216ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 519ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6456ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1162ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 42ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 170ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 37ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 36ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 33ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 34ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 82ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 52ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 66ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 81ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 266ms https://solana.com/data
- `solana.com.databricks` [ok] 200 111ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 410ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 90ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 89ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 523ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 1148ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 412ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 95ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 94ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 96ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 1053ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2578ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 268ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 52ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 190ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 154ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 556ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 582ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 799ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 101ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 4808ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 76ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 618ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 175ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 617ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 166ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 861ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 185ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 549ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 164ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 670ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 162ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 609ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 173ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 7511ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 206ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 1831ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 137ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 650ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 163ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 664ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 134ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 519ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 97ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 588ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 105ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1391ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2017ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1396ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1495ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1038ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1229ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1492ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1551ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.FLNCx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.XRXx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.INDIx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WGSx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.METCx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.QUBTx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.WRLDx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.PCTx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.QUBTx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.circ.WRLDx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.FLNCx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.INDIx` [ok] 200 722ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.AAONx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.price.PRIx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/PRIx/price-data
- `xstocks.circ.WYFIx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.AIx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.BETRx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 1028ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.PRIx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/PRIx/circulating-supply?format=object
- `xstocks.price.ACMx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/ACMx/price-data
- `xstocks.circ.AIx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.price.ESIx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/ESIx/price-data
- `xstocks.circ.ACMx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/ACMx/circulating-supply?format=object
- `xstocks.circ.ESIx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/ESIx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.PRIx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/PRIx/multiplier?network=Solana
- `xstocks.circ.AAONx` [ok] 200 867ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.price.IDAx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/IDAx/price-data
- `xstocks.circ.IDAx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/IDAx/circulating-supply?format=object
- `xstocks.mult.ESIx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/ESIx/multiplier?network=Solana
- `xstocks.mult.IDAx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/IDAx/multiplier?network=Solana
- `xstocks.mult.ACMx` [ok] 200 835ms https://api.backed.fi/api/v2/public/assets/ACMx/multiplier?network=Solana
- `xstocks.price.SFDx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SFDx/price-data
- `xstocks.price.SAROx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/SAROx/price-data
- `xstocks.price.THGx` [ok] 200 1102ms https://api.backed.fi/api/v2/public/assets/THGx/price-data
- `xstocks.circ.SAROx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/SAROx/circulating-supply?format=object
- `xstocks.mult.AAONx` [ok] 200 968ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.circ.THGx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/THGx/circulating-supply?format=object
- `xstocks.price.EMNx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/EMNx/price-data
- `xstocks.price.AOSx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/AOSx/price-data
- `xstocks.mult.THGx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/THGx/multiplier?network=Solana
- `xstocks.circ.EMNx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/EMNx/circulating-supply?format=object
- `xstocks.mult.SAROx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/SAROx/multiplier?network=Solana
- `xstocks.price.Zx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/Zx/price-data
- `xstocks.price.APPFx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/APPFx/price-data
- `xstocks.circ.AOSx` [ok] 200 428ms https://api.backed.fi/api/v2/public/assets/AOSx/circulating-supply?format=object
- `xstocks.circ.SFDx` [ok] 200 1123ms https://api.backed.fi/api/v2/public/assets/SFDx/circulating-supply?format=object
- `xstocks.circ.APPFx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/APPFx/circulating-supply?format=object
- `xstocks.mult.AOSx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/AOSx/multiplier?network=Solana
- `xstocks.mult.EMNx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/EMNx/multiplier?network=Solana
- `xstocks.mult.APPFx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/APPFx/multiplier?network=Solana
- `xstocks.price.PATHx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/PATHx/price-data
- `xstocks.price.REXRx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/REXRx/price-data
- `xstocks.circ.Zx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/Zx/circulating-supply?format=object
- `xstocks.price.CBSHx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/CBSHx/price-data
- `xstocks.mult.SFDx` [ok] 200 558ms https://api.backed.fi/api/v2/public/assets/SFDx/multiplier?network=Solana
- `xstocks.price.LNCx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/LNCx/price-data
- `xstocks.mult.Zx` [ok] 200 510ms https://api.backed.fi/api/v2/public/assets/Zx/multiplier?network=Solana
- `xstocks.circ.CBSHx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/CBSHx/circulating-supply?format=object
- `xstocks.mult.CBSHx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CBSHx/multiplier?network=Solana
- `xstocks.price.MOSx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/MOSx/price-data
- `xstocks.circ.PATHx` [ok] 200 1113ms https://api.backed.fi/api/v2/public/assets/PATHx/circulating-supply?format=object
- `xstocks.price.PRMBx` [ok] 200 764ms https://api.backed.fi/api/v2/public/assets/PRMBx/price-data
- `xstocks.mult.INDIx` [ok] 200 4732ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.price.TKRx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/TKRx/price-data
- `xstocks.circ.PRMBx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/PRMBx/circulating-supply?format=object
- `xstocks.mult.PATHx` [ok] 200 1098ms https://api.backed.fi/api/v2/public/assets/PATHx/multiplier?network=Solana
- `xstocks.circ.MOSx` [ok] 200 1274ms https://api.backed.fi/api/v2/public/assets/MOSx/circulating-supply?format=object
- `xstocks.price.PCTYx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/PCTYx/price-data
- `xstocks.price.MORNx` [ok] 200 4832ms https://api.backed.fi/api/v2/public/assets/MORNx/price-data
- `xstocks.circ.PCTYx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/PCTYx/circulating-supply?format=object
- `xstocks.mult.PCTYx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/PCTYx/multiplier?network=Solana
- `xstocks.mult.PRMBx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/PRMBx/multiplier?network=Solana
- `xstocks.mult.MOSx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/MOSx/multiplier?network=Solana
- `xstocks.price.KNSLx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/KNSLx/price-data
- `xstocks.price.KMXx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/KMXx/price-data
- `xstocks.circ.PCTx` [ok] 200 6592ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.KNSLx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/KNSLx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.KNSLx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/KNSLx/multiplier?network=Solana
- `xstocks.price.TAPx` [ok] 200 639ms https://api.backed.fi/api/v2/public/assets/TAPx/price-data
- `xstocks.price.XPx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/XPx/price-data
- `xstocks.price.FRx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/FRx/price-data
- `xstocks.circ.MORNx` [ok] 200 1240ms https://api.backed.fi/api/v2/public/assets/MORNx/circulating-supply?format=object
- `xstocks.circ.LNCx` [ok] 200 3494ms https://api.backed.fi/api/v2/public/assets/LNCx/circulating-supply?format=object
- `xstocks.circ.REXRx` [ok] 200 4135ms https://api.backed.fi/api/v2/public/assets/REXRx/circulating-supply?format=object
- `xstocks.circ.KMXx` [ok] 200 1266ms https://api.backed.fi/api/v2/public/assets/KMXx/circulating-supply?format=object
- `xstocks.mult.LNCx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/LNCx/multiplier?network=Solana
- `xstocks.circ.TAPx` [ok] 200 1007ms https://api.backed.fi/api/v2/public/assets/TAPx/circulating-supply?format=object
- `xstocks.mult.REXRx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/REXRx/multiplier?network=Solana
- `xstocks.mult.KMXx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/KMXx/multiplier?network=Solana
- `xstocks.mult.TAPx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/TAPx/multiplier?network=Solana
- `xstocks.mult.MORNx` [ok] 200 796ms https://api.backed.fi/api/v2/public/assets/MORNx/multiplier?network=Solana
- `xstocks.price.LADx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/LADx/price-data
- `xstocks.price.BOKFx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/BOKFx/price-data
- `xstocks.price.WALx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/WALx/price-data
- `xstocks.price.ATRx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/ATRx/price-data
- `xstocks.circ.BOKFx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/BOKFx/circulating-supply?format=object
- `xstocks.price.NFGx` [ok] 200 582ms https://api.backed.fi/api/v2/public/assets/NFGx/price-data
- `xstocks.circ.ATRx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/ATRx/circulating-supply?format=object
- `xstocks.mult.BOKFx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/BOKFx/multiplier?network=Solana
- `xstocks.circ.FRx` [ok] 200 1410ms https://api.backed.fi/api/v2/public/assets/FRx/circulating-supply?format=object
- `xstocks.mult.FRx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/FRx/multiplier?network=Solana
- `xstocks.mult.ATRx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/ATRx/multiplier?network=Solana
- `xstocks.price.AVAVx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/AVAVx/price-data
- `xstocks.circ.XPx` [ok] 200 1847ms https://api.backed.fi/api/v2/public/assets/XPx/circulating-supply?format=object
- `xstocks.price.QRVOx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/QRVOx/price-data
- `xstocks.circ.AVAVx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/AVAVx/circulating-supply?format=object
- `xstocks.mult.XPx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/XPx/multiplier?network=Solana
- `xstocks.mult.AVAVx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/AVAVx/multiplier?network=Solana
- `xstocks.circ.TKRx` [ok] 200 3703ms https://api.backed.fi/api/v2/public/assets/TKRx/circulating-supply?format=object
- `xstocks.circ.LADx` [ok] 200 1230ms https://api.backed.fi/api/v2/public/assets/LADx/circulating-supply?format=object
- `xstocks.price.NNNx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/NNNx/price-data
- `xstocks.price.CNMx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/CNMx/price-data
- `xstocks.mult.LADx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/LADx/multiplier?network=Solana
- `xstocks.circ.CNMx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CNMx/circulating-supply?format=object
- `xstocks.circ.WALx` [ok] 200 1365ms https://api.backed.fi/api/v2/public/assets/WALx/circulating-supply?format=object
- `xstocks.circ.NFGx` [ok] 200 1244ms https://api.backed.fi/api/v2/public/assets/NFGx/circulating-supply?format=object
- `xstocks.mult.TKRx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/TKRx/multiplier?network=Solana
- `xstocks.circ.NNNx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/NNNx/circulating-supply?format=object
- `xstocks.mult.WALx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/WALx/multiplier?network=Solana
- `xstocks.mult.CNMx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CNMx/multiplier?network=Solana
- `xstocks.price.HLIx` [ok] 200 1309ms https://api.backed.fi/api/v2/public/assets/HLIx/price-data
- `xstocks.price.UGIx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/UGIx/price-data
- `xstocks.mult.NFGx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/NFGx/multiplier?network=Solana
- `xstocks.price.AXTAx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/AXTAx/price-data
- `xstocks.circ.HLIx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/HLIx/circulating-supply?format=object
- `xstocks.circ.UGIx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/UGIx/circulating-supply?format=object
- `xstocks.price.CAGx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CAGx/price-data
- `xstocks.circ.AXTAx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/AXTAx/circulating-supply?format=object
- `xstocks.mult.HLIx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/HLIx/multiplier?network=Solana
- `xstocks.mult.UGIx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/UGIx/multiplier?network=Solana
- `xstocks.mult.AXTAx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/AXTAx/multiplier?network=Solana
- `xstocks.price.VOYAx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/VOYAx/price-data
- `xstocks.price.COLBx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/COLBx/price-data
- `xstocks.price.ADCx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/ADCx/price-data
- `xstocks.mult.NNNx` [ok] 200 752ms https://api.backed.fi/api/v2/public/assets/NNNx/multiplier?network=Solana
- `xstocks.circ.COLBx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/COLBx/circulating-supply?format=object
- `xstocks.price.CHRDx` [ok] 200 1123ms https://api.backed.fi/api/v2/public/assets/CHRDx/price-data
- `xstocks.price.FPSx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/FPSx/price-data
- `xstocks.mult.COLBx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/COLBx/multiplier?network=Solana
- `xstocks.circ.CHRDx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/CHRDx/circulating-supply?format=object
- `xstocks.price.NCLHx` [ok] 200 621ms https://api.backed.fi/api/v2/public/assets/NCLHx/price-data
- `xstocks.price.BRXx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/BRXx/price-data
- `xstocks.mult.CHRDx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/CHRDx/multiplier?network=Solana
- `xstocks.circ.NCLHx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/NCLHx/circulating-supply?format=object
- `xstocks.price.AALx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/AALx/price-data
- `xstocks.mult.NCLHx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/NCLHx/multiplier?network=Solana
- `xstocks.circ.BRXx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/BRXx/circulating-supply?format=object
- `xstocks.circ.AALx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/AALx/circulating-supply?format=object
- `xstocks.mult.BRXx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/BRXx/multiplier?network=Solana
- `xstocks.circ.QRVOx` [ok] 200 2687ms https://api.backed.fi/api/v2/public/assets/QRVOx/circulating-supply?format=object
- `xstocks.mult.AALx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/AALx/multiplier?network=Solana
- `xstocks.price.TPGx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/TPGx/price-data
- `xstocks.mult.QRVOx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/QRVOx/multiplier?network=Solana
- `xstocks.price.VICRx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/VICRx/price-data
- `xstocks.price.FORMx` [ok] 200 739ms https://api.backed.fi/api/v2/public/assets/FORMx/price-data
- `xstocks.circ.TPGx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/TPGx/circulating-supply?format=object
- `xstocks.circ.CAGx` [ok] 200 1984ms https://api.backed.fi/api/v2/public/assets/CAGx/circulating-supply?format=object
- `xstocks.circ.VICRx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/VICRx/circulating-supply?format=object
- `xstocks.price.CUBEx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/CUBEx/price-data
- `xstocks.circ.FPSx` [ok] 200 1482ms https://api.backed.fi/api/v2/public/assets/FPSx/circulating-supply?format=object
- `xstocks.mult.TPGx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/TPGx/multiplier?network=Solana
- `xstocks.mult.VICRx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/VICRx/multiplier?network=Solana
- `xstocks.mult.FPSx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/FPSx/multiplier?network=Solana
- `xstocks.mult.CAGx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/CAGx/multiplier?network=Solana
- `xstocks.price.BRKRx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/BRKRx/price-data
- `xstocks.price.NEUx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/NEUx/price-data
- `xstocks.price.AMGx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/AMGx/price-data
- `xstocks.price.BIOx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/BIOx/price-data
- `xstocks.circ.BRKRx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/BRKRx/circulating-supply?format=object
- `xstocks.circ.VOYAx` [ok] 200 2723ms https://api.backed.fi/api/v2/public/assets/VOYAx/circulating-supply?format=object
- `xstocks.circ.ADCx` [ok] 200 2713ms https://api.backed.fi/api/v2/public/assets/ADCx/circulating-supply?format=object
- `xstocks.mult.ADCx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/ADCx/multiplier?network=Solana
- `xstocks.circ.FORMx` [ok] 200 1382ms https://api.backed.fi/api/v2/public/assets/FORMx/circulating-supply?format=object
- `xstocks.price.BAHx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/BAHx/price-data
- `xstocks.mult.BRKRx` [ok] 200 745ms https://api.backed.fi/api/v2/public/assets/BRKRx/multiplier?network=Solana
- `xstocks.mult.FORMx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/FORMx/multiplier?network=Solana
- `xstocks.circ.BAHx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/BAHx/circulating-supply?format=object
- `xstocks.price.CELHx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/CELHx/price-data
- `xstocks.circ.AMGx` [ok] 200 1033ms https://api.backed.fi/api/v2/public/assets/AMGx/circulating-supply?format=object
- `xstocks.circ.CUBEx` [ok] 200 1489ms https://api.backed.fi/api/v2/public/assets/CUBEx/circulating-supply?format=object
- `xstocks.mult.VOYAx` [ok] 200 594ms https://api.backed.fi/api/v2/public/assets/VOYAx/multiplier?network=Solana
- `xstocks.mult.BAHx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/BAHx/multiplier?network=Solana
- `xstocks.circ.CELHx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CELHx/circulating-supply?format=object
- `xstocks.mult.AMGx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/AMGx/multiplier?network=Solana
- `xstocks.price.MTCHx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/MTCHx/price-data
- `xstocks.mult.CUBEx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CUBEx/multiplier?network=Solana
- `xstocks.price.OGEx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/OGEx/price-data
- `xstocks.circ.BIOx` [ok] 200 1390ms https://api.backed.fi/api/v2/public/assets/BIOx/circulating-supply?format=object
- `xstocks.price.TTCx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/TTCx/price-data
- `xstocks.price.AREx` [ok] 200 567ms https://api.backed.fi/api/v2/public/assets/AREx/price-data
- `xstocks.mult.CELHx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/CELHx/multiplier?network=Solana
- `xstocks.circ.NEUx` [ok] 200 1630ms https://api.backed.fi/api/v2/public/assets/NEUx/circulating-supply?format=object
- `xstocks.mult.BIOx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/BIOx/multiplier?network=Solana
- `xstocks.mult.NEUx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/NEUx/multiplier?network=Solana
- `xstocks.price.LINEx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/LINEx/price-data
- `xstocks.price.CGNXx` [ok] 200 811ms https://api.backed.fi/api/v2/public/assets/CGNXx/price-data
- `xstocks.circ.CGNXx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CGNXx/circulating-supply?format=object
- `xstocks.mult.CGNXx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/CGNXx/multiplier?network=Solana
- `xstocks.price.TTEKx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/TTEKx/price-data
- `xstocks.circ.MTCHx` [ok] 200 1328ms https://api.backed.fi/api/v2/public/assets/MTCHx/circulating-supply?format=object
- `xstocks.price.AVTRx` [ok] 200 809ms https://api.backed.fi/api/v2/public/assets/AVTRx/price-data
- `xstocks.circ.AREx` [ok] 200 1180ms https://api.backed.fi/api/v2/public/assets/AREx/circulating-supply?format=object
- `xstocks.circ.AVTRx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/AVTRx/circulating-supply?format=object
- `xstocks.mult.AREx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/AREx/multiplier?network=Solana
- `xstocks.mult.AVTRx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/AVTRx/multiplier?network=Solana
- `xstocks.circ.LINEx` [ok] 200 1108ms https://api.backed.fi/api/v2/public/assets/LINEx/circulating-supply?format=object
- `xstocks.circ.OGEx` [ok] 200 1621ms https://api.backed.fi/api/v2/public/assets/OGEx/circulating-supply?format=object
- `xstocks.mult.LINEx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/LINEx/multiplier?network=Solana
- `xstocks.price.MHKx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/MHKx/price-data
- `xstocks.mult.OGEx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/OGEx/multiplier?network=Solana
- `xstocks.price.RRCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/RRCx/price-data
- `xstocks.price.VIAVx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/VIAVx/price-data
- `xstocks.mult.MTCHx` [ok] 200 928ms https://api.backed.fi/api/v2/public/assets/MTCHx/multiplier?network=Solana
- `xstocks.circ.TTEKx` [ok] 200 1078ms https://api.backed.fi/api/v2/public/assets/TTEKx/circulating-supply?format=object
- `xstocks.circ.TTCx` [ok] 200 2162ms https://api.backed.fi/api/v2/public/assets/TTCx/circulating-supply?format=object
- `xstocks.circ.VIAVx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/VIAVx/circulating-supply?format=object
- `xstocks.mult.TTEKx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/TTEKx/multiplier?network=Solana
- `xstocks.mult.TTCx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/TTCx/multiplier?network=Solana
- `xstocks.mult.VIAVx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/VIAVx/multiplier?network=Solana
- `xstocks.circ.RRCx` [ok] 200 1703ms https://api.backed.fi/api/v2/public/assets/RRCx/circulating-supply?format=object
- `xstocks.mult.RRCx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/RRCx/multiplier?network=Solana
- `xstocks.circ.MHKx` [ok] 200 2188ms https://api.backed.fi/api/v2/public/assets/MHKx/circulating-supply?format=object
- `xstocks.mult.MHKx` [ok] 200 975ms https://api.backed.fi/api/v2/public/assets/MHKx/multiplier?network=Solana
- `xstocks.price.MSGSx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/MSGSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MSGSx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/MSGSx/circulating-supply?format=object
- `xstocks.mult.MSGSx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/MSGSx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 612ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 148ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.BETRx` [ok] 200 82ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.XRXx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.QUBTx` [ok] 200 66ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WGSx` [ok] 200 70ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.FLNCx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.WYFIx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.AIx` [ok] 200 67ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.PCTx` [ok] 200 66ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jito.tip_floor` [ok] 200 163ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 301ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 103ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 554ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 556ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 749ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 733ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 290ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
