# Borealis — Solana ecosystem report

**Generated** 2026-09-04T02:06:42Z · 2026-09-03 19:06:42 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-04T02:06:32Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +3.61%; DEX 24h $2.37B · 1d +4% · vs-7d-ago -36%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -35.89%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -34.25%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 856,198.00 is +26.3% vs 30d median 677,709.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 103.63 USD is +25.2% vs 30d median 82.77 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 444,126,810 |
| Block height | 422,173,207 |
| Block time | 2026-09-04T02:06:32Z |
| Epoch | 1,028 (7.13% · slot 30,812/432,000) |
| Mean TPS (last ~3,600s) | 3,580.3 |
| Mean non-vote TPS | 1,459.5 |
| Median TPS (same window) | 3,575.4 |
| Mean slot time | 315.8 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 544,955,304,625 |
| Circulating supply | 585,360,688 SOL |
| Total supply | 633,455,693 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 19 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 436,594,517 SOL |
| Delinquent stake | 304,348.44 SOL (0.070%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 79 |
| Top 10 / 20 stake share | 24.40% / 35.73% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.39M SOL | 3.98% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.32M SOL | 3.74% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.46M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.38M SOL | 2.61% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.19% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.28M SOL | 2.13% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.38M SOL | 1.69% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.13M SOL | 1.63% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.84M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `vahMVcSS…` · 163.34K SOL · commission 0% · lag 39159 slots
- `xLabscif…` · 78.25K SOL · commission 5% · lag 338437 slots
- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 2729 slots
- `prt1st4R…` · 19.80K SOL · commission 5% · lag 639868 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 778087 slots
- `5ZjxMYBb…` · 4.06K SOL · commission 0% · lag 160888 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1340689 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 30804 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 688171 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 2143056 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1326459 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1367973 slots

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
| **In-protocol fees 24h** | **$595.41K** (6,074.3 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-02 |
| **Solana REV** | **7,160.1 SOL** / **$701.85K** | MEASURED UTC calendar day 2026-09-02: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-02 · UTC day 2026-09-02 · SOL-USD date 2026-09-02 |
| Jito tip-floor run-rate (NOT REV) | $73.48K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 73479 USD; at p95 floor → 30891049 USD. |
| Protocol fees 24h | $10.73M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9949 |
| p90 / p99 | 0.000010 / 0.000112 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.63 | coingecko.simple_price |
| 24h change | +3.61% | coingecko.simple_price |
| Market cap | $60.67B | coingecko.simple_price |
| 24h volume | $4.25B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.94B |
| TVL 1d / 7d / 30d | +0.84% / -1.24% / +23.58% |
| DEX volume 24h | $2.37B · 1d +3.62% · vs-7d-ago -35.89% |
| 7d DEX volume | $15.38B · -30.87% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $10.73M |
| Fees 1d / 7d | +1.82% / -34.25% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $838.66M | -17.87% |
| Orca DEX | $285.64M | +42.41% |
| BisonFi | $232.51M | +19.63% |
| Meteora DLMM | $186.49M | +35.31% |
| Manifest Trade | $174.59M | +1.71% |
| Raydium AMM | $153.08M | +30.82% |
| pump.fun | $75.20M | -9.58% |
| Axiom | $60.26M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.58B | +3.98% | -4.98% |
| Kamino Lend | Lending | $1.33B | +8.29% | +6.36% |
| Raydium AMM | Dexs | $1.13B | +4.85% | -2.98% |
| Jupiter Lend | Lending | $1.09B | +2.80% | -1.76% |
| Binance Staked SOL | Liquid Staking | $1.08B | +4.08% | -4.45% |
| Jito Liquid Staking | Liquid Staking | $1.05B | +4.31% | -4.69% |
| BlackRock BUIDL | RWA | $937.81M | +0.63% | -0.43% |
| Jupiter Perpetual Exchange | Derivatives | $765.17M | +2.97% | -3.59% |
| Jupiter Staked SOL | Liquid Staking | $537.63M | +4.07% | -5.41% |
| xStocks | RWA | $462.08M | +6.34% | +4.78% |

## Stablecoins

Solana circulating pegged-USD: **$16.23B**
(1d +3.12% · 7d +2.36%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.08B | +6.78% |
| USDT · Tether | $2.95B | +3.90% |
| USDGO · USDGO | $1.32B | +5.62% |
| USD1 · World Liberty Financial USD | $1.22B | +1.24% |
| BUIDL · BlackRock USD | $937.81M | +5.73% |
| PYUSD · PayPal USD | $860.11M | +16.50% |
| USDG · Global Dollar | $562.68M | -8.29% |
| USDe · Ethena USDe | $536.12M | -0.24% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 77 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 77 · priced-subset mcap $291.95M (lower bound, not a census).
24h volume $31.62M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $462.08M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 77 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.16B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $937.81M
- **xStocks** (RWA) — $462.08M
- **OnRe** (RWA) — $296.75M
- **Ondo Yield Assets** (RWA) — $179.46M
- **Hastra** (RWA) — $150.39M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $25.38M
- **Plume Vaults** (RWA) — $22.90M

## Daily active addresses

856,198 (Allium, as of 2026-09-02). Provider range 446,040–877,460. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — solana.com/news · Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — solana.com/news · Thu, 03 Sep 2026 15:15:00 GMT
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — solana.com/news · Wed, 02 Sep 2026 09:00:00 GMT
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) — solana.com/news · Tue, 01 Sep 2026 09:00:00 GMT
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) — solana.com/news · Fri, 28 Aug 2026 16:00:00 GMT `mainnet`
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) — solana.com/news · Thu, 27 Aug 2026 04:15:00 GMT
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) — solana.com/news · Mon, 24 Aug 2026 14:19:00 GMT `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-04 (2026-09-03 19:06:42 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~316 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `on-chain` — On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending.
- `observed` — Observed mean slot ~316 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **X / Twitter RSS** — Public X/Nitter-style RSS yielded no usable items this run (403/gated skipped). xcancel.solana empty-or-gated, xcancel.solana_status empty-or-gated, xcancel.anza_xyz empty-or-gated, xcancel.solana_devs empty-or-gated, nitter.solana TimeoutError: The read operation timed out, nitter.solana_status 502
- **xStocks** — priced up to 80 of 726 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 239ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 212ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 211ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 274ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 206ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6612ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 442ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 83ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 39ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 43ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 50ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 34ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 31ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 80ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 103ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 72ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 78ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 505ms https://solana.com/data
- `solana.com.databricks` [ok] 200 137ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 405ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 103ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 81ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 109ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 160ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 834ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 435ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 438ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 440ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [FAIL]  18184ms https://nitter.perennialte.ch/solana/rss — TimeoutError: The read operation timed out
- `rss.nitter.solana_status` [FAIL] 502 6131ms https://nitter.perennialte.ch/solana_status/rss — HTTP 502 Bad Gateway
- `rss.nitter.anza_xyz` [FAIL] 502 234ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_devs` [FAIL] 502 223ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 502 Bad Gateway
- `rss.rsshub.solana` [FAIL] 404 217ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 92ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 210ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 209ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 960ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 929ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 973ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 917ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 932ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 810ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 907ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 837ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 929ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 913ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 775ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 895ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 762ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 911ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2243ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 6388ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 4337ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2544ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2092ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 3547ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 3393ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1414ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.SPYx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.TSLAx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.AMZNx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.MSFTx` [ok] 200 801ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.GOOGLx` [ok] 200 801ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.NVDAx` [ok] 200 809ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.SPYx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.AMZNx` [ok] 200 617ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 1403ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.TSLAx` [ok] 200 928ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 525ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.COINx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.MVLLx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.MUUx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.mult.COINx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 1150ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.MVLLx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.price.AXTIx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.mult.AMZNx` [ok] 200 1324ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.DJTx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 1100ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.circ.AXTIx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.DJTx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.price.INTWx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.mult.AXTIx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.KORUx` [ok] 200 688ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.circ.SOXSx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.KORUx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 632ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.AAPLx` [ok] 200 3968ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.mult.QQQx` [ok] 200 1041ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 740ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.SHEINx` [ok] 200 865ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.price.BANKCx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.AAPLx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.INTWx` [ok] 200 932ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 1372ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 2778ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.MMGx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.TNGYIx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.MUUx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 2048ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.circ.SUOPTx` [ok] 200 693ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 926ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.SNXXx` [ok] 200 826ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.circ.SHEINx` [ok] 200 2099ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 1169ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.SHEINx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 606ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 815ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.price.CTINSx` [ok] 200 826ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.HAIDLx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.KUNLx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 715ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 654ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 682ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.KUNLx` [ok] 200 1182ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 1113ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 3074ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.HRZRBx` [ok] 200 667ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.CMERPx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 514ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 719ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.circ.CTINSx` [ok] 200 2821ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.JTGEXx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 1438ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.CMERPx` [ok] 200 1201ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 622ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.WXXDCx` [ok] 200 819ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.CSPCx` [ok] 200 1021ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 970ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.MIXUx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.mult.CSPCx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 2482ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 881ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.ASMPTx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.MIXUx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.CMENDx` [ok] 200 1145ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 1018ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 2003ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 1034ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 1045ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.CRESMx` [ok] 200 2826ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 1233ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.SNDSCx` [ok] 200 1087ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.CRESPx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.SINOTx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.SITCx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.PRADx` [ok] 200 585ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.WHGROx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 788ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.CRESPx` [ok] 200 1304ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 895ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 637ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.PRADx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 1537ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 591ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.CTPCAx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 1918ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.price.NWGx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CLONPx` [ok] 200 2383ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 717ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.GENTEx` [ok] 200 1182ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.CLONPx` [ok] 200 652ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.CTPCAx` [ok] 200 1444ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 1892ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 1383ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 595ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.circ.NWGx` [ok] 200 1571ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.CKAHx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.WUXIBx` [ok] 200 1145ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.NWGx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 626ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.KUAIx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 2673ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 2697ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.circ.NONGx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 1468ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 1695ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.circ.COVELx` [ok] 200 454ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 643ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.COVELx` [ok] 200 392ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 1522ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.CHONGx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.price.MTRCPx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.CKAHx` [ok] 200 2321ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 829ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 846ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.mult.CHONGx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 1067ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 2808ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.PICCx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.HNDLDx` [ok] 200 587ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.MTRCPx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 506ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.GEELx` [ok] 200 777ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 722ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 846ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 1033ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 2042ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 54ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 218ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.MUUx` [ok] 200 111ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.INTWx` [ok] 200 102ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.DRAMx` [ok] 200 107ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.KORUx` [ok] 200 121ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.MVLLx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SOXSx` [ok] 200 107ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jup.tokens.search.MEITx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 103ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jito.tip_floor` [ok] 200 594ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 253ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 123ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 206ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 253ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 205ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 221ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 217ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
