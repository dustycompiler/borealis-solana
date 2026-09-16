# Borealis — Solana ecosystem report

**Generated** 2026-09-16T20:07:25Z · 2026-09-16 13:07:25 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-16T20:07:14Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h +1.20%; DEX 24h $2.70B · 1d +7% · vs-7d-ago -3%; slot 320 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **INFO · TPS vs 30d median (solana.com/data tx/86400)** — Current 5,031.00 TPS is +29.9% vs 30d median 3,874.11 TPS (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 447,609,363 |
| Block height | 425,650,722 |
| Block time | 2026-09-16T20:07:14Z |
| Epoch | 1,036 (13.28% · slot 57,368/432,000) |
| Mean TPS (last ~3,600s) | 5,031.0 |
| Mean non-vote TPS | 2,933.9 |
| Median TPS (same window) | 5,017.6 |
| Mean slot time | 319.6 ms |
| Median slot time | 319.1 ms |
| Transaction count (cluster) | 549,170,428,588 |
| Circulating supply | 587,150,301 SOL |
| Total supply | 634,205,228 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 677 |
| Delinquent | 14 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,569,431 SOL |
| Delinquent stake | 191,651.35 SOL (0.044%) |
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

- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 1048925 slots
- `7d7x84ji…` · 35.25K SOL · commission 5% · lag 124881 slots
- `t23p8aBQ…` · 14.66K SOL · commission 0% · lag 14127 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 734562 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 565078 slots
- `Hgozywot…` · 807.47 SOL · commission 100% · lag 56602 slots
- `4GEEKSwu…` · 196.81 SOL · commission 5% · lag 1799751 slots
- `EWARp8Sy…` · 88.61 SOL · commission 5% · lag 613367 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 1910266 slots
- `Je6ckvDi…` · 3.50 SOL · commission 0% · lag 169222 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 18073680 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 447609363 slots

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
| **In-protocol fees 24h** | **$639.75K** (6,332.7 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-14 |
| **Solana REV** | **7,374.9 SOL** / **$745.04K** | MEASURED UTC calendar day 2026-09-14: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-14 · UTC day 2026-09-14 · SOL-USD date 2026-09-14 |
| Jito tip-floor run-rate (NOT REV) | $171.78K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 171783 USD; at p95 floor → 1492860 USD. |
| Protocol fees 24h | $14.08M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $98.47 | coingecko.simple_price |
| 24h change | +1.20% | coingecko.simple_price |
| Market cap | $57.78B | coingecko.simple_price |
| 24h volume | $3.49B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.72B |
| TVL 1d / 7d / 30d | -3.29% / -3.87% / +19.53% |
| DEX volume 24h | $2.70B · 1d +6.84% · vs-7d-ago -2.90% |
| 7d DEX volume | $18.12B · +4.88% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.08M |
| Fees 1d / 7d | +3.71% / -15.69% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $519.33M | +16.60% |
| BisonFi | $353.62M | +11.97% |
| HumidiFi | $232.02M | +29.33% |
| fomo Wallet | $226.51M | +32.34% |
| Raydium AMM | $220.70M | -31.98% |
| Orca DEX | $196.98M | +14.31% |
| Tessera V | $171.07M | +48.00% |
| Meteora DLMM | $168.53M | -15.23% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.55B | +0.56% | -2.11% |
| Kamino Lend | Lending | $1.33B | -0.37% | -1.52% |
| Raydium AMM | Dexs | $1.10B | -2.79% | -4.71% |
| Jupiter Lend | Lending | $1.06B | -2.04% | -3.75% |
| Binance Staked SOL | Liquid Staking | $1.01B | -1.91% | -6.05% |
| Jito Liquid Staking | Liquid Staking | $1.00B | -2.04% | -5.55% |
| Jupiter Perpetual Exchange | Derivatives | $732.25M | -0.95% | -2.82% |
| Jupiter Staked SOL | Liquid Staking | $505.36M | -1.53% | -5.83% |
| Marinade Native | Staking Pool | $372.48M | -1.78% | -6.25% |
| Sentora Curator | Risk Curators | $372.30M | -0.52% | +3.46% |

## Stablecoins

Solana circulating pegged-USD: **$15.40B**
(1d -2.63% · 7d -4.04%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.73B | -6.53% |
| USDT · Tether | $2.34B | -5.63% |
| USDGO · USDGO | $1.38B | -1.08% |
| USD1 · World Liberty Financial USD | $1.32B | +0.00% |
| BUIDL · BlackRock USD | $993.19M | +0.03% |
| PYUSD · PayPal USD | $704.14M | +0.29% |
| USDG · Global Dollar | $620.95M | +1.13% |
| USDe · Ethena USDe | $524.09M | -0.83% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $235.79K (lower bound, not a census).
24h volume $61.95M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$561.54M** across 19 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $302.28M
- **Huma Finance V2** (RWA) — $173.94M
- **Plume Vaults** (RWA) — $28.34M
- **Ondo Global Markets** (RWA) — $27.23M
- **MatrixDock XAUM** (RWA) — $6.83M
- **Midas RWA** (RWA) — $5.64M
- **Invesco USTB** (RWA) — $3.91M
- **VNX** (RWA) — $2.76M

## Daily active addresses

815,550 (Allium, as of 2026-09-15). Provider range 413,903–903,402. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

_As of 2026-09-16 (2026-09-16 13:07:25 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=activated-not-yet-effective, 200ms=pending. Observed mean slot ~320 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~320 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 691ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 466ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 596ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 708ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 553ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6828ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1376ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 168ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 126ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 152ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 138ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 735ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 949ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 448ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 306ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 174ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 239ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 412ms https://solana.com/data
- `solana.com.databricks` [ok] 200 179ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 531ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 180ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 561ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 127ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 341ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 320ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 124ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 294ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 151ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 1586ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 4457ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [FAIL] 502 2669ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_devs` [FAIL] 502 179ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 502 Bad Gateway
- `rss.rsshub.solana` [FAIL] 404 398ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 1033ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 633ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 442ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 655ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 284ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 714ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 163ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 726ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 281ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 579ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 234ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 718ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 350ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 805ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 442ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 561ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 332ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 737ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 334ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 786ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 324ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 697ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 297ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 627ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 222ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 686ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 277ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 674ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 250ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 678ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 236ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1597ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2111ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 3311ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1862ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 3950ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1729ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1896ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 2342ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.FLNCx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.WGSx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.WRLDx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.XRXx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.INDIx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.QUBTx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.circ.WGSx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.price.METCx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.FLNCx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.price.PCTx` [ok] 200 637ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.mult.WGSx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 406ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.XRXx` [ok] 200 940ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.price.DRSx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.price.AIx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.WYFIx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.SCIx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.circ.METCx` [ok] 200 1191ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.SAILx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.mult.WYFIx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.SAILx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.circ.PCTx` [ok] 200 1318ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.price.BSYx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.mult.SAILx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.price.GSATx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.circ.AIx` [ok] 200 1002ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.DRSx` [ok] 200 1288ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 594ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 963ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.MPx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.circ.SCIx` [ok] 200 1223ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.DVAx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.price.DCIx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.mult.SCIx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.GDDYx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.mult.BETRx` [ok] 200 1539ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.circ.BSYx` [ok] 200 1162ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.price.BXPx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.price.RYANx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.circ.GSATx` [ok] 200 1376ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.mult.BSYx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.circ.MPx` [ok] 200 1155ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.mult.GSATx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 1262ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.mult.MPx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.circ.DVAx` [ok] 200 1428ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.circ.RYANx` [ok] 200 996ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.price.DYx` [ok] 200 757ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.circ.GDDYx` [ok] 200 1500ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.circ.BXPx` [ok] 200 1271ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.price.WMSx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.mult.DCIx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.mult.RYANx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.mult.BXPx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.mult.DVAx` [ok] 200 499ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.price.AMx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.price.FDSx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.price.ALSNx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.mult.GDDYx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.price.SMTCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.price.SFx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.circ.DYx` [ok] 200 1071ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.circ.FDSx` [ok] 200 971ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.circ.WMSx` [ok] 200 1299ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 1105ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.mult.WMSx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.AXSMx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.circ.ALSNx` [ok] 200 1141ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.price.BPOPx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.mult.AMx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.circ.SMTCx` [ok] 200 1329ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.price.EGPx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.price.TTMIx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.circ.SFx` [ok] 200 1023ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 578ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.mult.SFx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.mult.SMTCx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.price.AEISx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.price.DPZx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.price.KTOSx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.circ.DPZx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.circ.EGPx` [ok] 200 1005ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.mult.DPZx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.circ.AXSMx` [ok] 200 1416ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.circ.BPOPx` [ok] 200 1280ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.price.HRLx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.mult.AXSMx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.mult.EGPx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.TTMIx` [ok] 200 1275ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.BPOPx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.price.PAGx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.mult.TTMIx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.circ.KTOSx` [ok] 200 1206ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.price.EHCx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.price.HIIx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.price.SEICx` [ok] 200 644ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.circ.AEISx` [ok] 200 1517ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.mult.KTOSx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.mult.AEISx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.circ.SEICx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.price.ARx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.circ.PAGx` [ok] 200 913ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.price.GFLx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.mult.SEICx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.circ.HRLx` [ok] 200 1295ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.mult.HRLx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.DOCUx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.price.MGMx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.mult.PAGx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 1063ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.circ.EHCx` [ok] 200 1217ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.circ.DOCUx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.price.HALOx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.mult.HIIx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.circ.HALOx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.mult.DOCUx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.mult.EHCx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.price.WTRGx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.AFGx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.mult.HALOx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.circ.ARx` [ok] 200 1251ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.circ.GFLx` [ok] 200 1221ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.price.AMKRx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.circ.WTRGx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.mult.GFLx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.circ.MGMx` [ok] 200 1123ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.mult.AFGx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.circ.AMKRx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.price.GMEDx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.price.HUBSx` [ok] 200 761ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.price.JKHYx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.WTRGx` [ok] 200 524ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.circ.HUBSx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.mult.MGMx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.circ.GMEDx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.circ.JKHYx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.price.IESCx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.mult.GMEDx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.mult.AMKRx` [ok] 200 606ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.mult.HUBSx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.price.OCx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.price.CRx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.mult.JKHYx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.price.BMRNx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.circ.IESCx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.price.JEFx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.circ.OCx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.circ.BMRNx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.price.AMHx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.JEFx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.mult.IESCx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.mult.ARx` [ok] 200 1537ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.mult.OCx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.mult.BMRNx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.price.FIVEx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.circ.AMHx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.circ.CRx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.mult.JEFx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.price.ITx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.price.MDGLx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.mult.AMHx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.price.UHALx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.circ.FIVEx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.circ.MDGLx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.circ.ITx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.circ.UHALx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.price.AHRx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.mult.ITx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.FIVEx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.mult.MDGLx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.price.VNOMx` [ok] 200 710ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.mult.UHALx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.circ.AHRx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.price.CORTx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.mult.CRx` [ok] 200 748ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.price.STRLx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.mult.AHRx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.NWSAx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.price.AURx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.circ.CORTx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.circ.STRLx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.price.IVZx` [ok] 200 563ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.circ.AURx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.circ.NWSAx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.circ.IVZx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.mult.AURx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.mult.NWSAx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.mult.CORTx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.Hx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.mult.STRLx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.circ.Hx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.price.NWSx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.price.GWREx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.price.ARWRx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.mult.Hx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.mult.IVZx` [ok] 200 616ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.circ.ARWRx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.circ.VNOMx` [ok] 200 1298ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.price.MANHx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.price.BAXx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.MANHx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.mult.VNOMx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.mult.ARWRx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.circ.GWREx` [ok] 200 691ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.circ.NWSx` [ok] 200 730ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.price.CACIx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.mult.MANHx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.price.RVTYx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/RVTYx/price-data
- `xstocks.price.TXRHx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/TXRHx/price-data
- `xstocks.circ.RVTYx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/RVTYx/circulating-supply?format=object
- `xstocks.circ.CACIx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.NWSx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.circ.TXRHx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/TXRHx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.mult.RVTYx` [ok] 200 422ms https://api.backed.fi/api/v2/public/assets/RVTYx/multiplier?network=Solana
- `xstocks.mult.CACIx` [ok] 200 496ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.mult.TXRHx` [ok] 200 554ms https://api.backed.fi/api/v2/public/assets/TXRHx/multiplier?network=Solana
- `xstocks.price.CNAx` [ok] 200 883ms https://api.backed.fi/api/v2/public/assets/CNAx/price-data
- `xstocks.circ.BAXx` [ok] 200 1454ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.BAXx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.circ.CNAx` [ok] 200 1113ms https://api.backed.fi/api/v2/public/assets/CNAx/circulating-supply?format=object
- `xstocks.mult.CNAx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/CNAx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 12218ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.circ.FRHCx` [ok] 200 1012ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 2869ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 262ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.QUBTx` [ok] 200 127ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.INDIx` [ok] 200 111ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.WRLDx` [ok] 200 96ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.XRXx` [ok] 200 122ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 110ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.FLNCx` [ok] 200 101ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.WGSx` [ok] 200 156ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.AIx` [ok] 200 112ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jito.tip_floor` [ok] 200 212ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 430ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 159ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 632ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 458ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 609ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 676ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 246ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
