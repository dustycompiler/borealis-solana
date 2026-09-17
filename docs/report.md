# Borealis — Solana ecosystem report

**Generated** 2026-09-17T02:38:59Z · 2026-09-16 19:38:59 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-17T02:38:49Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h +1.88%; DEX 24h $2.73B · 1d +1% · vs-7d-ago -11%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

No flags vs rolling baseline (60 samples / llama 7d). Watching.

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 447,683,438 |
| Block height | 425,724,715 |
| Block time | 2026-09-17T02:38:49Z |
| Epoch | 1,036 (30.43% · slot 131,439/432,000) |
| Mean TPS (last ~3,600s) | 4,180.7 |
| Mean non-vote TPS | 2,048.6 |
| Median TPS (same window) | 4,111.6 |
| Mean slot time | 316.7 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 549,269,688,976 |
| Circulating supply | 587,212,542 SOL |
| Total supply | 634,204,968 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 679 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,605,492 SOL |
| Delinquent stake | 155,590.73 SOL (0.035%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.35% / 35.66% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.77M SOL | 4.04% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.35M SOL | 3.72% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.49M SOL | 2.84% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.38M SOL | 2.59% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.74M SOL | 2.22% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.26M SOL | 2.11% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.05M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.39M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.08M SOL | 1.61% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.56M SOL | 1.49% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.20M SOL | 1.41% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.11M SOL | 1.39% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.66M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 1123000 slots
- `t23p8aBQ…` · 14.66K SOL · commission 0% · lag 88202 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 808637 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 639153 slots
- `4GEEKSwu…` · 196.81 SOL · commission 5% · lag 1873826 slots
- `EWARp8Sy…` · 88.61 SOL · commission 5% · lag 687442 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 1984341 slots
- `Je6ckvDi…` · 3.50 SOL · commission 0% · lag 243297 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 18147755 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 447683438 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 1427411 slots
- `4kdjgZKJ…` · 1.05 SOL · commission 100% · lag 447683438 slots

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
| **In-protocol fees 24h** | **$723.33K** (7,138.9 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-15 |
| **Solana REV** | **8,668.9 SOL** / **$878.35K** | MEASURED UTC calendar day 2026-09-15: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-15 · UTC day 2026-09-15 · SOL-USD date 2026-09-15 |
| Jito tip-floor run-rate (NOT REV) | $51.82K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 51823 USD; at p95 floor → 736960 USD. |
| Protocol fees 24h | $14.04M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $99.20 | coingecko.simple_price |
| 24h change | +1.88% | coingecko.simple_price |
| Market cap | $58.23B | coingecko.simple_price |
| 24h volume | $3.41B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.74B |
| TVL 1d / 7d / 30d | +0.02% / -2.02% / +18.04% |
| DEX volume 24h | $2.73B · 1d +1.11% · vs-7d-ago -11.14% |
| 7d DEX volume | $16.51B · -8.32% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.04M |
| Fees 1d / 7d | -0.16% / -10.62% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $441.42M | -15.00% |
| BisonFi | $353.62M | 0.00% |
| fomo Wallet | $267.61M | +56.59% |
| Raydium AMM | $263.56M | +5.94% |
| Orca DEX | $262.55M | +38.81% |
| HumidiFi | $232.02M | 0.00% |
| Meteora DLMM | $174.16M | +3.34% |
| Tessera V | $171.07M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.55B | +1.00% | -0.54% |
| Kamino Lend | Lending | $1.33B | +0.07% | -1.16% |
| Raydium AMM | Dexs | $1.11B | -0.43% | -3.37% |
| Jupiter Lend | Lending | $1.06B | -0.59% | -2.42% |
| Jito Liquid Staking | Liquid Staking | $1.02B | +1.92% | -1.42% |
| Binance Staked SOL | Liquid Staking | $1.02B | +1.50% | -2.76% |
| Jupiter Perpetual Exchange | Derivatives | $730.63M | +0.12% | -2.15% |
| Jupiter Staked SOL | Liquid Staking | $508.77M | +1.14% | -3.16% |
| Sentora Curator | Risk Curators | $372.26M | +0.04% | +3.10% |
| Marinade Native | Staking Pool | $371.48M | +0.65% | -4.70% |

## Stablecoins

Solana circulating pegged-USD: **$15.40B**
(1d -1.21% · 7d -5.06%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.71B | -0.81% |
| USDT · Tether | $2.34B | -5.63% |
| USDGO · USDGO | $1.38B | +0.00% |
| USD1 · World Liberty Financial USD | $1.32B | +0.00% |
| BUIDL · BlackRock USD | $993.19M | +0.01% |
| PYUSD · PayPal USD | $719.06M | +0.49% |
| USDG · Global Dollar | $624.55M | +2.01% |
| USDe · Ethena USDe | $524.26M | -0.64% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $239.14K (lower bound, not a census).
24h volume $73.11M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$571.87M** across 19 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $302.48M
- **Huma Finance V2** (RWA) — $184.08M
- **Plume Vaults** (RWA) — $28.45M
- **Ondo Global Markets** (RWA) — $27.25M
- **MatrixDock XAUM** (RWA) — $6.72M
- **Midas RWA** (RWA) — $5.64M
- **Invesco USTB** (RWA) — $3.91M
- **VNX** (RWA) — $2.76M

## Daily active addresses

815,550 (Allium, as of 2026-09-15). Provider range 424,129–867,494. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — solana.com/news · Mon, 14 Sep 2026 11:00:00 GMT
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — solana.com/news · Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — solana.com/news · Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) — solana.com/news · Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — solana.com/news · Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — solana.com/news · Thu, 03 Sep 2026 15:15:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-17 (2026-09-16 19:38:59 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=activated-not-yet-effective, 200ms=pending. Observed mean slot ~317 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `on-chain` — On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=activated-not-yet-effective, 200ms=pending.
- `observed` — Observed mean slot ~317 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 315ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 272ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 306ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 281ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 265ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6856ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 519ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 137ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 92ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 67ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 54ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 1096ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1353ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 119ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 570ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 115ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 103ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 557ms https://solana.com/data
- `solana.com.databricks` [ok] 200 121ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 582ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 174ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 132ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 87ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 410ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 575ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 233ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 235ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 243ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 2267ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2235ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2474ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 2925ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 266ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 281ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 258ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 257ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 285ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 336ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 337ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 140ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 390ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 253ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 375ms https://api.mainnet-beta.solana.com — {'code': -32007, 'message': 'Slot 447654585 was skipped, or missing due to ledger jump to recent snapshot'}
- `rpc.getBlock.fallback` [FAIL] 200 106ms https://solana-rpc.publicnode.com — {'code': -32007, 'message': 'Slot 447654585 was skipped, or missing due to ledger jump to recent snapshot'}
- `rpc.getBlock` [FAIL] 200 407ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 237ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 365ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 194ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 448ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 290ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 397ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 193ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 422ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 279ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 442ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 476ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 361ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 209ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 406ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 378ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 380ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 219ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 333ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 196ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 2093ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1712ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2000ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1109ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 3216ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1631ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1740ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1432ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.QUBTx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.PCTx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.INDIx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.METCx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.WRLDx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.circ.QUBTx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.price.XRXx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.FLNCx` [ok] 200 549ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.WGSx` [ok] 200 570ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.mult.INDIx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 528ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 558ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.XRXx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 583ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 574ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.BETRx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.DRSx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.price.SCIx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.mult.FLNCx` [ok] 200 603ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 777ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.DRSx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.SAILx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.price.AIx` [ok] 200 648ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.price.GSATx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.circ.SCIx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.mult.BETRx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.BSYx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.circ.AIx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.GSATx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 516ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.mult.SCIx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.circ.SAILx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.price.MPx` [ok] 200 608ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.circ.BSYx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.mult.GSATx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.DCIx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.price.GDDYx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.price.DVAx` [ok] 200 497ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.mult.SAILx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.mult.BSYx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.price.BXPx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.circ.DCIx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.circ.GDDYx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.price.DYx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.circ.MPx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.circ.DVAx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.circ.RYANx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.circ.BXPx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.price.FRHCx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.mult.DCIx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.mult.GDDYx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.mult.DVAx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.mult.RYANx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.mult.BXPx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.circ.FRHCx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.price.WMSx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.price.AMx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.price.ALSNx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.mult.MPx` [ok] 200 587ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.circ.DYx` [ok] 200 592ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.price.FDSx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.price.SFx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.mult.DYx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.price.AXSMx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.price.SMTCx` [ok] 200 704ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.circ.AXSMx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.price.EGPx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.circ.SMTCx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.mult.AXSMx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.circ.EGPx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.mult.SMTCx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.circ.ALSNx` [ok] 200 993ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.price.BPOPx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.mult.EGPx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 1251ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.price.TTMIx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.price.AEISx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.circ.FDSx` [ok] 200 1163ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.circ.SFx` [ok] 200 1163ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.price.DPZx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.mult.AMx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.circ.WMSx` [ok] 200 1720ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.circ.DPZx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.mult.SFx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.price.KTOSx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.mult.DPZx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.price.PAGx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.mult.WMSx` [ok] 200 566ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 1151ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.price.SEICx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.circ.PAGx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.price.HIIx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.price.HRLx` [ok] 200 577ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.circ.KTOSx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.mult.BPOPx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.circ.SEICx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.circ.HIIx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.circ.HRLx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.circ.AEISx` [ok] 200 1285ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.mult.PAGx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.mult.KTOSx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.price.EHCx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.mult.SEICx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.circ.TTMIx` [ok] 200 1558ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.HIIx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.price.GFLx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.circ.EHCx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.mult.AEISx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.price.ARx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.price.MGMx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.circ.GFLx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.HRLx` [ok] 200 545ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.DOCUx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.mult.TTMIx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.HALOx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.mult.EHCx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.circ.ARx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.mult.GFLx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.circ.MGMx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.price.AFGx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.price.HUBSx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.price.AMKRx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.price.WTRGx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.mult.ARx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.mult.MGMx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.price.GMEDx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.price.JKHYx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.circ.HALOx` [ok] 200 1169ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.circ.AMKRx` [ok] 200 953ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 1042ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.mult.HALOx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.mult.AFGx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.circ.JKHYx` [ok] 200 950ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 1023ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.circ.HUBSx` [ok] 200 1476ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.circ.DOCUx` [ok] 200 1771ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.mult.AMKRx` [ok] 200 503ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.price.IESCx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.circ.WTRGx` [ok] 200 1526ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.mult.JKHYx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.mult.HUBSx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.price.CRx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.price.OCx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.mult.DOCUx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.price.BMRNx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.price.AMHx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.price.JEFx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.price.ITx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.price.FIVEx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.circ.IESCx` [ok] 200 1125ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.circ.OCx` [ok] 200 905ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.circ.JEFx` [ok] 200 861ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.mult.OCx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.circ.CRx` [ok] 200 1180ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.mult.IESCx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.VNOMx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.mult.CRx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.circ.AMHx` [ok] 200 1382ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.mult.JEFx` [ok] 200 490ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.circ.BMRNx` [ok] 200 1430ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.price.MDGLx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.circ.FIVEx` [ok] 200 1282ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.mult.BMRNx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.price.UHALx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.mult.FIVEx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.price.IVZx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.price.CORTx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.circ.ITx` [ok] 200 1806ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.price.AHRx` [ok] 200 649ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.mult.ITx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.circ.MDGLx` [ok] 200 908ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.price.NWSAx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.circ.UHALx` [ok] 200 1064ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.price.STRLx` [ok] 200 1068ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.mult.UHALx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.circ.CORTx` [ok] 200 1094ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.circ.IVZx` [ok] 200 1255ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.circ.VNOMx` [ok] 200 1892ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.mult.MDGLx` [ok] 200 808ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.price.AURx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.mult.CORTx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.mult.IVZx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.circ.AHRx` [ok] 200 1230ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.mult.VNOMx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.ARWRx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.price.Hx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.price.GWREx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.mult.AHRx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.circ.NWSAx` [ok] 200 1003ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.price.NWSx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.price.MANHx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.mult.NWSAx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.circ.STRLx` [ok] 200 1314ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 1006ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.price.CACIx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.circ.ARWRx` [ok] 200 1090ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.mult.STRLx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.circ.GWREx` [ok] 200 1231ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.price.BAXx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.Hx` [ok] 200 1329ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.mult.AURx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.circ.MANHx` [ok] 200 1148ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.price.TXRHx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/TXRHx/price-data
- `xstocks.circ.NWSx` [ok] 200 1339ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.mult.MANHx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.price.CNAx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CNAx/price-data
- `xstocks.price.RVTYx` [ok] 200 581ms https://api.backed.fi/api/v2/public/assets/RVTYx/price-data
- `xstocks.mult.Hx` [ok] 200 872ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.circ.CACIx` [ok] 200 1655ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.circ.BAXx` [ok] 200 1422ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.circ.CNAx` [ok] 200 971ms https://api.backed.fi/api/v2/public/assets/CNAx/circulating-supply?format=object
- `xstocks.circ.RVTYx` [ok] 200 947ms https://api.backed.fi/api/v2/public/assets/RVTYx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.circ.TXRHx` [ok] 200 1456ms https://api.backed.fi/api/v2/public/assets/TXRHx/circulating-supply?format=object
- `xstocks.mult.RVTYx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/RVTYx/multiplier?network=Solana
- `xstocks.mult.CNAx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/CNAx/multiplier?network=Solana
- `xstocks.mult.TXRHx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/TXRHx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 827ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 254ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INDIx` [ok] 200 121ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 126ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 129ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.XRXx` [ok] 200 131ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 122ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.WGSx` [ok] 200 125ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.FLNCx` [ok] 200 115ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.AIx` [ok] 200 129ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jito.tip_floor` [ok] 200 304ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 266ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 148ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 302ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 234ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 272ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 284ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 195ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
