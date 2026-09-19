# Borealis — Solana ecosystem report

**Generated** 2026-09-19T04:36:52Z · 2026-09-18 21:36:52 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-19T04:36:44Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h +7.48%; DEX 24h $3.26B · 1d +26% · vs-7d-ago -1%; slot 266 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +21.90%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +25.68%. (threshold: `|1d %| >= 8`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 448,301,225 |
| Block height | 426,342,084 |
| Block time | 2026-09-19T04:36:44Z |
| Epoch | 1,037 (73.43% · slot 317,225/432,000) |
| Mean TPS (last ~3,600s) | 4,134.3 |
| Mean non-vote TPS | 1,596.5 |
| Median TPS (same window) | 4,153.4 |
| Mean slot time | 265.7 ms |
| Median slot time | 265.5 ms |
| Transaction count (cluster) | 550,059,158,450 |
| Circulating supply | 587,296,514 SOL |
| Total supply | 634,297,763 SOL |
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

- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 1740787 slots
- `t23p8aBQ…` · 14.66K SOL · commission 0% · lag 705989 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 51632 slots
- `mrgn4atx…` · 2.26K SOL · commission 0% · lag 289552 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 426473 slots
- `Hgozywot…` · 807.55 SOL · commission 100% · lag 154411 slots
- `TiMxX1ya…` · 114.23 SOL · commission 0% · lag 72682746 slots
- `EWARp8Sy…` · 98.61 SOL · commission 5% · lag 1305229 slots
- `BZBKHmW1…` · 5.90 SOL · commission 5% · lag 45516746 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 64252355 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 2045198 slots

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
| **In-protocol fees 24h** | **$814.96K** (8,101.5 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-17 |
| **Solana REV** | **9,853.4 SOL** / **$991.19K** | MEASURED UTC calendar day 2026-09-17: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-17 · UTC day 2026-09-17 · SOL-USD date 2026-09-17 |
| Jito tip-floor run-rate (NOT REV) | $29.88K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 29878 USD; at p95 floor → 1640573 USD. |
| Protocol fees 24h | $17.88M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $112.52 | coingecko.simple_price |
| 24h change | +7.48% | coingecko.simple_price |
| Market cap | $66.10B | coingecko.simple_price |
| 24h volume | $6.15B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.30B |
| TVL 1d / 7d / 30d | +4.40% / +6.86% / +20.36% |
| DEX volume 24h | $3.26B · 1d +25.68% · vs-7d-ago -0.64% |
| 7d DEX volume | $16.04B · -19.04% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $17.88M |
| Fees 1d / 7d | +21.90% / +0.02% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $488.34M | +48.30% |
| Raydium AMM | $411.55M | +46.72% |
| BisonFi | $378.33M | 0.00% |
| Orca DEX | $355.26M | +108.54% |
| HumidiFi | $281.64M | 0.00% |
| Meteora DLMM | $239.38M | +34.54% |
| fomo Wallet | $176.39M | -19.05% |
| Manifest Trade | $170.83M | +49.01% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.81B | +10.72% | +15.77% |
| Kamino Lend | Lending | $1.40B | +4.68% | +4.14% |
| Raydium AMM | Dexs | $1.28B | +11.04% | +11.94% |
| Binance Staked SOL | Liquid Staking | $1.18B | +10.68% | +10.85% |
| Jito Liquid Staking | Liquid Staking | $1.17B | +12.31% | +12.01% |
| Jupiter Lend | Lending | $1.16B | +6.04% | +4.94% |
| Jupiter Perpetual Exchange | Derivatives | $801.25M | +6.46% | +6.85% |
| Jupiter Staked SOL | Liquid Staking | $588.21M | +10.39% | +11.41% |
| Marinade Native | Staking Pool | $432.89M | +10.78% | +11.19% |
| PumpSwap | Dexs | $369.73M | +12.35% | +12.79% |

## Stablecoins

Solana circulating pegged-USD: **$15.48B**
(1d +1.05% · 7d -4.38%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.01B | +4.66% |
| USDT · Tether | $2.12B | -7.03% |
| USDGO · USDGO | $1.38B | +0.14% |
| USD1 · World Liberty Financial USD | $1.33B | +0.76% |
| BUIDL · BlackRock USD | $993.18M | -0.01% |
| PYUSD · PayPal USD | $727.55M | -0.95% |
| USDG · Global Dollar | $624.77M | +0.14% |
| USDe · Ethena USDe | $519.20M | -0.86% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 1 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 1 · priced-subset mcap $10.09K (lower bound, not a census).
24h volume $116.97M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 1 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$577.35M** across 17 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $304.05M
- **Huma Finance V2** (RWA) — $200.83M
- **Plume Vaults** (RWA) — $28.12M
- **Ondo Global Markets** (RWA) — $26.88M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $2.95M
- **VNX** (RWA) — $2.78M
- **Oro Finance** (RWA) — $2.51M

## Daily active addresses

890,530 (Allium, as of 2026-09-18). Provider range 456,874–893,188. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

_As of 2026-09-19 (2026-09-18 21:36:52 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 89ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 61ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 31ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 34ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 36ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6362ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 109ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 64ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 29ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 52ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 31ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 36ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 24ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 69ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 55ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 51ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 95ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 318ms https://solana.com/data
- `solana.com.databricks` [ok] 200 259ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 321ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 115ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 29ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 57ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 201ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 244ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 51ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 58ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 54ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 260ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 390ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 332ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 60ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 198ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 25ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 40ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 40ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 86ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 154ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 63ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 47ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 92ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 134ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 113ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 174ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 138ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 153ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 134ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 134ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 27ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 146ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 93ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 122ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 118ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 137ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 91ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 110ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 95ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 99ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 70ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 68ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 125ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 135ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 115ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 116ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1897ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1037ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1206ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1087ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1178ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1090ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1034ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 2155ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.INDIx` [FAIL]  12018ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.XRXx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.FLNCx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.QUBTx` [FAIL]  12017ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PCTx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METCx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/METCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WRLDx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WGSx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.INDIx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.PCTx` [ok] 200 111ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.WGSx` [ok] 200 524ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 687ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.price.SCIx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.mult.AIx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.circ.SCIx` [ok] 200 524ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 1619ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.SCIx` [ok] 200 589ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.WYFIx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WYFIx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.BETRx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BETRx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.AAONx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DRSx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.BETRx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.circ.DRSx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.price.SAILx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AAONx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.SAILx` [ok] 200 111ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.BSYx` [FAIL]  12015ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DCIx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.mult.AAONx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.circ.BSYx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.circ.DCIx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.mult.SAILx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.mult.DCIx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.price.BXPx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.mult.BSYx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.circ.RYANx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.circ.BXPx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.mult.BXPx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.mult.RYANx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.price.GSATx` [FAIL]  12017ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.GSATx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.price.MPx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/MPx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.GSATx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.MPx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.mult.MPx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.price.ALSNx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.circ.ALSNx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.price.DVAx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DVAx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.price.GDDYx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.DVAx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.circ.GDDYx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.price.SFx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.mult.GDDYx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.circ.SFx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.price.FRHCx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DYx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/DYx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SFx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.circ.FRHCx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.circ.DYx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.price.WMSx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.EGPx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.mult.DYx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.price.AMx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/AMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WMSx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.circ.EGPx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.circ.AMx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.AMx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.price.FDSx` [FAIL]  12016ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.EGPx` [ok] 200 400ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.FDSx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.mult.WMSx` [ok] 200 533ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.mult.FDSx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.price.SMTCx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SMTCx` [ok] 200 111ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.mult.SMTCx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.price.PAGx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.circ.PAGx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.mult.PAGx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.price.AXSMx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AXSMx` [ok] 200 110ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.price.BPOPx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.AXSMx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.price.TTMIx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HIIx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.circ.TTMIx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.circ.HIIx` [ok] 200 110ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.mult.TTMIx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.AEISx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.EHCx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.circ.AEISx` [ok] 200 108ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.price.DPZx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.EHCx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.price.KTOSx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.BPOPx` [ok] 200 744ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.mult.HIIx` [ok] 200 635ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.price.HRLx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DPZx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.mult.EHCx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.AEISx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.circ.HRLx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.mult.DPZx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.mult.HRLx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.SEICx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.KTOSx` [ok] 200 1335ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.circ.SEICx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.mult.SEICx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.price.AFGx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.mult.KTOSx` [ok] 200 636ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.price.HUBSx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.circ.HUBSx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 640ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.mult.HUBSx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.mult.AFGx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.price.GFLx` [FAIL]  12014ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ARx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/ARx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MGMx` [FAIL]  12012ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DOCUx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MGMx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.price.HALOx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DOCUx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.mult.MGMx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.circ.ARx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.price.WTRGx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.DOCUx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.circ.HALOx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.circ.WTRGx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.mult.HALOx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.mult.ARx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.price.CRx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.circ.CRx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.circ.GFLx` [ok] 200 1025ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.CRx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.mult.GFLx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.price.JEFx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.price.AMHx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.JEFx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.circ.AMHx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.mult.JEFx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.price.ITx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.circ.ITx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.price.AMKRx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.ITx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.price.GMEDx` [FAIL]  12014ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AMKRx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.mult.AMKRx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.price.UHALx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.circ.UHALx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.mult.UHALx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.price.JKHYx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.JKHYx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.price.IESCx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.IESCx` [ok] 200 110ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.price.OCx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/OCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.JKHYx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.circ.OCx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.price.IVZx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.price.BMRNx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.IESCx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.circ.IVZx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.circ.BMRNx` [ok] 200 109ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.mult.OCx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.mult.IVZx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.mult.BMRNx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.price.FIVEx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.FIVEx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.mult.FIVEx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.price.MDGLx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.Hx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.circ.MDGLx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.circ.Hx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.price.VNOMx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MDGLx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.mult.Hx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.circ.VNOMx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.mult.VNOMx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.AHRx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AHRx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.mult.AHRx` [ok] 200 722ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.CORTx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CORTx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.price.STRLx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.NWSAx` [FAIL]  12010ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AURx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/AURx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CORTx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.circ.NWSAx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.mult.NWSAx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.price.BAXx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.BAXx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.circ.STRLx` [ok] 200 1047ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 1047ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.mult.AURx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.STRLx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.price.ARWRx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GWREx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.GWREx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.price.NWSx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.GWREx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.circ.ARWRx` [ok] 200 870ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 1025ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.NWSx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.price.MANHx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MANHx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.price.CACIx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CACIx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.price.RVTYx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/RVTYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.TXRHx` [FAIL]  12018ms https://api.backed.fi/api/v2/public/assets/TXRHx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.RVTYx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/RVTYx/circulating-supply?format=object
- `xstocks.mult.RVTYx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/RVTYx/multiplier?network=Solana
- `xstocks.circ.TXRHx` [ok] 200 1036ms https://api.backed.fi/api/v2/public/assets/TXRHx/circulating-supply?format=object
- `xstocks.mult.TXRHx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/TXRHx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 21ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 89ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.AIx` [ok] 200 45ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.XRXx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.METCx` [ok] 200 38ms https://lite-api.jup.ag/tokens/v2/search?query=METCx
- `jup.tokens.search.FLNCx` [ok] 200 40ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.PCTx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.WGSx` [ok] 200 45ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.INDIx` [ok] 200 51ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 37ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jito.tip_floor` [ok] 200 301ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 189ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 58ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 29ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 43ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 26ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 28ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 184ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
