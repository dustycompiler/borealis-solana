# Borealis — Solana ecosystem report

**Generated** 2026-09-19T19:48:25Z · 2026-09-19 12:48:25 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-19T19:48:17Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -2.39%; DEX 24h $3.54B · 1d +36% · vs-7d-ago +8%; slot 267 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +18.99%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +36.44%. (threshold: `|1d %| >= 8`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 448,506,504 |
| Block height | 426,547,271 |
| Block time | 2026-09-19T19:48:17Z |
| Epoch | 1,038 (20.95% · slot 90,505/432,000) |
| Mean TPS (last ~3,600s) | 4,683.4 |
| Mean non-vote TPS | 2,161.7 |
| Median TPS (same window) | 4,650.6 |
| Mean slot time | 267.0 ms |
| Median slot time | 267.9 ms |
| Transaction count (cluster) | 550,289,464,481 |
| Circulating supply | 587,367,702 SOL |
| Total supply | 634,376,174 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 677 |
| Delinquent | 13 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 440,069,130 SOL |
| Delinquent stake | 158,241.26 SOL (0.036%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.28% / 35.66% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.85M SOL | 4.06% | 7% | 0 |
| 2 | `HEL1USMZ…` | 15.82M SOL | 3.59% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.50M SOL | 2.84% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.36M SOL | 2.58% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.79M SOL | 2.22% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.25M SOL | 2.10% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.12M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.43M SOL | 1.69% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.09M SOL | 1.61% | 5% | 0 |
| 10 | `9jxgosAf…` | 6.63M SOL | 1.51% | 100% | 0 |
| 11 | `Awes4Tr6…` | 6.56M SOL | 1.49% | 0% | 0 |
| 12 | `JD549Hsb…` | 6.21M SOL | 1.41% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.35% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.65M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.84M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 1946066 slots
- `t23p8aBQ…` · 14.48K SOL · commission 0% · lag 911268 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 119212 slots
- `mrgn4atx…` · 2.26K SOL · commission 0% · lag 494831 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 631752 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 13633 slots
- `EWARp8Sy…` · 64.91 SOL · commission 5% · lag 1510508 slots
- `FLVgaCPv…` · 9.28 SOL · commission 5% · lag 20490966 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 18970821 slots
- `HDRqPft5…` · 2.00 SOL · commission 100% · lag 448506504 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 398823 slots
- `6DTkuiey…` · 2.00 SOL · commission 100% · lag 448506504 slots

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
| Jito tip-floor run-rate (NOT REV) | $408.69K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 408692 USD; at p95 floor → 20801722 USD. |
| Protocol fees 24h | $17.46M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $111.21 | coingecko.simple_price |
| 24h change | -2.39% | coingecko.simple_price |
| Market cap | $65.32B | coingecko.simple_price |
| 24h volume | $3.29B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.24B |
| TVL 1d / 7d / 30d | +5.87% / +5.82% / +19.19% |
| DEX volume 24h | $3.54B · 1d +36.44% · vs-7d-ago +7.86% |
| 7d DEX volume | $17.70B · -10.70% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $17.46M |
| Fees 1d / 7d | +18.99% / -2.36% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| BisonFi | $532.67M | +40.80% |
| PumpSwap | $488.34M | +48.30% |
| HumidiFi | $334.93M | +18.92% |
| Raydium AMM | $330.64M | +17.87% |
| Orca DEX | $300.65M | +76.48% |
| Meteora DLMM | $239.38M | +34.54% |
| Tessera V | $205.65M | +22.21% |
| fomo Wallet | $156.65M | -28.10% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.78B | -0.82% | +13.74% |
| Kamino Lend | Lending | $1.39B | -0.30% | +2.68% |
| Raydium AMM | Dexs | $1.26B | +4.92% | +10.60% |
| Binance Staked SOL | Liquid Staking | $1.16B | +0.73% | +9.11% |
| Jito Liquid Staking | Liquid Staking | $1.15B | -0.63% | +10.09% |
| Jupiter Lend | Lending | $1.14B | -0.35% | +3.89% |
| Jupiter Perpetual Exchange | Derivatives | $792.27M | -0.90% | +5.33% |
| Jupiter Staked SOL | Liquid Staking | $576.03M | -0.76% | +9.08% |
| Marinade Native | Staking Pool | $426.13M | -0.29% | +9.49% |
| Sentora Curator | Risk Curators | $364.43M | +0.37% | +12.89% |

## Stablecoins

Solana circulating pegged-USD: **$15.43B**
(1d +1.05% · 7d -4.38%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.96B | +3.97% |
| USDT · Tether | $2.12B | -7.03% |
| USDGO · USDGO | $1.38B | +0.14% |
| USD1 · World Liberty Financial USD | $1.33B | +0.76% |
| BUIDL · BlackRock USD | $993.18M | -0.01% |
| PYUSD · PayPal USD | $726.19M | -1.13% |
| USDG · Global Dollar | $628.03M | +0.65% |
| USDe · Ethena USDe | $511.96M | -2.25% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $239.43K (lower bound, not a census).
24h volume $90.48M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$577.89M** across 17 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $304.04M
- **Huma Finance V2** (RWA) — $201.47M
- **Plume Vaults** (RWA) — $28.12M
- **Ondo Global Markets** (RWA) — $26.85M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $2.93M
- **VNX** (RWA) — $2.76M
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

- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — solana.com/news · Sat, 19 Sep 2026 11:28:00 GMT `mainnet`
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

_As of 2026-09-19 (2026-09-19 12:48:25 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **X / Twitter RSS** — Public X/Nitter-style RSS yielded no usable items this run (403/gated skipped). xcancel.solana 451, xcancel.solana_status 451, xcancel.anza_xyz 451, xcancel.solana_devs 451, nitter.solana 502, nitter.solana_status 502
- **Median tx fee** — no getBlock samples
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 247ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 518ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 91ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 183ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 163ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5413ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 334ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 109ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 155ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 129ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 82ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 2703ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1131ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 330ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 94ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 131ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 181ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 412ms https://solana.com/data
- `solana.com.databricks` [ok] 200 180ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 658ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 159ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 305ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 453ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 356ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 477ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 161ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 157ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 164ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [FAIL] 502 1518ms https://nitter.perennialte.ch/solana/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_status` [FAIL] 502 209ms https://nitter.perennialte.ch/solana_status/rss — HTTP 502 Bad Gateway
- `rss.nitter.anza_xyz` [FAIL] 502 243ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_devs` [ok] 200 114ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 312ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 269ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 139ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 167ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 110ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 210ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 282ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 149ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 187ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 349ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 281ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 223ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 270ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 260ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 367ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 250ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 139ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 232ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 278ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 264ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 176ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 255ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 242ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 249ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 170ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 220ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 253ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 295ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 195ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 408ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 215ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 190ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1654ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1733ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1373ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1798ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1376ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1719ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1066ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1766ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.INDIx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.XRXx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.WRLDx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.QUBTx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.METCx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.FLNCx` [ok] 200 570ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.PCTx` [ok] 200 581ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.METCx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 602ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.METCx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.WGSx` [ok] 200 1215ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.WYFIx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.WRLDx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 516ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 887ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.price.AAONx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.price.BETRx` [ok] 200 456ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.XRXx` [ok] 200 1333ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.price.AIx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.price.DRSx` [ok] 200 496ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.circ.AAONx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.DRSx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.price.SAILx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.mult.AAONx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.mult.BETRx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.BSYx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.circ.WYFIx` [ok] 200 1028ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.SAILx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.GSATx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.price.SCIx` [ok] 200 543ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.price.MPx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.circ.BSYx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.DVAx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.circ.GSATx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.mult.SAILx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.circ.SCIx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.circ.MPx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.price.DCIx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.circ.DVAx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.mult.GSATx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.price.GDDYx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.mult.BSYx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 1197ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.SCIx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.mult.DVAx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.price.BXPx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.circ.GDDYx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.mult.MPx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.price.DYx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.circ.BXPx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.circ.RYANx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.mult.GDDYx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.price.AMx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.DYx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.mult.BXPx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.circ.FRHCx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.mult.RYANx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.price.WMSx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.circ.AMx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.price.ALSNx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.mult.FRHCx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.circ.WMSx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.circ.DCIx` [ok] 200 1034ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.price.FDSx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.price.SMTCx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.mult.AMx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.circ.ALSNx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.price.SFx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.circ.FDSx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.circ.SMTCx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.mult.DCIx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.price.AXSMx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.price.EGPx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.circ.SFx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.mult.SMTCx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.price.BPOPx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.circ.AXSMx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.mult.SFx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.circ.EGPx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.price.TTMIx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.price.AEISx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.mult.AXSMx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.price.DPZx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.circ.BPOPx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.mult.WMSx` [ok] 200 854ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.HRLx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.circ.AEISx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.price.KTOSx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.circ.DPZx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.mult.BPOPx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.mult.EGPx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.TTMIx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.circ.HRLx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.mult.AEISx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.circ.KTOSx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.price.PAGx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.mult.DPZx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.price.HIIx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.price.SEICx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.mult.TTMIx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.mult.HRLx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.GFLx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.circ.PAGx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.mult.KTOSx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.price.EHCx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.circ.SEICx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.price.MGMx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.circ.GFLx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.PAGx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.circ.EHCx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.mult.HIIx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.circ.MGMx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.mult.SEICx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.mult.GFLx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.mult.EHCx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.price.WTRGx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.HALOx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.price.DOCUx` [ok] 200 701ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.price.ARx` [ok] 200 780ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.price.AFGx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.price.HUBSx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.price.AMKRx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.mult.MGMx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.circ.WTRGx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.circ.ARx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.circ.AMKRx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.price.GMEDx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.mult.WTRGx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.mult.ARx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.mult.AMKRx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.circ.GMEDx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.price.JKHYx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.price.OCx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.mult.GMEDx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.price.IESCx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.circ.HALOx` [ok] 200 1161ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.circ.HUBSx` [ok] 200 1104ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.price.CRx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.circ.DOCUx` [ok] 200 1254ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.circ.OCx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 1286ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.circ.IESCx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.mult.HALOx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.mult.HUBSx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.circ.CRx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.mult.OCx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.mult.DOCUx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.mult.AFGx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.mult.IESCx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.JEFx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.mult.CRx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.price.AMHx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.price.FIVEx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.price.MDGLx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.price.ITx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.price.BMRNx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.price.VNOMx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.circ.AMHx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.circ.FIVEx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.circ.JEFx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.circ.MDGLx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.circ.ITx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.circ.BMRNx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.circ.JKHYx` [ok] 200 1358ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.circ.VNOMx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.mult.FIVEx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.mult.JEFx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.mult.ITx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.JKHYx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.mult.VNOMx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.UHALx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.price.AHRx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.price.CORTx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.price.STRLx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.mult.BMRNx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.mult.MDGLx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.price.NWSAx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.price.IVZx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.circ.UHALx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.circ.AHRx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.circ.CORTx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.price.Hx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.circ.IVZx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.circ.NWSAx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.price.AURx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.mult.UHALx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.mult.AHRx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.mult.CORTx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.circ.Hx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.mult.NWSAx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.price.ARWRx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.circ.AURx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.price.GWREx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.mult.Hx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.price.NWSx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.price.MANHx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.mult.IVZx` [ok] 200 487ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.mult.AURx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.circ.GWREx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.circ.ARWRx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.price.CACIx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.price.BAXx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.NWSx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.price.RVTYx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/RVTYx/price-data
- `xstocks.mult.GWREx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.mult.ARWRx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.circ.STRLx` [ok] 200 1265ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.mult.NWSx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.price.TXRHx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/TXRHx/price-data
- `xstocks.mult.STRLx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.circ.MANHx` [ok] 200 1271ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.circ.CACIx` [ok] 200 1082ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.circ.BAXx` [ok] 200 1099ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.circ.TXRHx` [ok] 200 1070ms https://api.backed.fi/api/v2/public/assets/TXRHx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.circ.RVTYx` [ok] 200 1387ms https://api.backed.fi/api/v2/public/assets/RVTYx/circulating-supply?format=object
- `xstocks.mult.RVTYx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/RVTYx/multiplier?network=Solana
- `xstocks.mult.TXRHx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/TXRHx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 83ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 237ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.QUBTx` [ok] 200 155ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.INDIx` [ok] 200 152ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.WRLDx` [ok] 200 151ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.XRXx` [ok] 200 143ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 143ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.WGSx` [ok] 200 137ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.FLNCx` [ok] 200 135ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.AIx` [ok] 200 144ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jito.tip_floor` [ok] 200 272ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 309ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 147ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 139ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 288ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 95ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 178ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 201ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
