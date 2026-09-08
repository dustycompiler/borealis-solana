# Borealis — Solana ecosystem report

**Generated** 2026-09-08T22:50:04Z · 2026-09-08 15:50:04 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-08T22:49:55Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h -0.08%; DEX 24h $2.72B · 1d -6% · vs-7d-ago +9%; slot 318 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -0.08%, DeFiLlama TVL 1d -1.24%, DEX 1d -6.33%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 445,455,882 |
| Block height | 423,499,787 |
| Block time | 2026-09-08T22:49:55Z |
| Epoch | 1,031 (14.79% · slot 63,885/432,000) |
| Mean TPS (last ~3,600s) | 4,306.5 |
| Mean non-vote TPS | 2,189.3 |
| Median TPS (same window) | 4,297.2 |
| Mean slot time | 317.5 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 546,491,758,605 |
| Circulating supply | 586,251,022 SOL |
| Total supply | 633,737,248 SOL |
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
| Activated stake | 438,600,954 SOL |
| Delinquent stake | 52,551.00 SOL (0.012%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.25% / 35.53% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 3.98% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.35M SOL | 3.73% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.53M SOL | 2.86% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.39M SOL | 2.60% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.18% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.03M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.32M SOL | 1.67% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.86M SOL | 1.56% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.60M SOL | 1.51% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.97M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `mrgn4atx…` · 20.28K SOL · commission 0% · lag 101175 slots
- `inWVrrYJ…` · 9.89K SOL · commission 0% · lag 104853 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 2107159 slots
- `prt1st4R…` · 5.87K SOL · commission 5% · lag 1968940 slots
- `xLabscif…` · 4.17K SOL · commission 5% · lag 1667509 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 1489960 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 916691 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 128999 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 445455882 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 61407012 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 616871 slots

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
| **In-protocol fees 24h** | **$763.42K** (7,228.6 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-07 |
| **Solana REV** | **8,421.8 SOL** / **$889.43K** | MEASURED UTC calendar day 2026-09-07: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-07 · UTC day 2026-09-07 · SOL-USD date 2026-09-07 |
| Jito tip-floor run-rate (NOT REV) | $195.49K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 195490 USD; at p95 floor → 1293701 USD. |
| Protocol fees 24h | $15.65M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9976 |
| p90 / p99 | 0.000014 / 0.000137 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.35 | coingecko.simple_price |
| 24h change | -0.08% | coingecko.simple_price |
| Market cap | $60.59B | coingecko.simple_price |
| 24h volume | $3.07B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.92B |
| TVL 1d / 7d / 30d | -1.24% / -1.09% / +23.10% |
| DEX volume 24h | $2.72B · 1d -6.33% · vs-7d-ago +8.76% |
| 7d DEX volume | $16.29B · -7.85% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $15.65M |
| Fees 1d / 7d | +6.81% / +17.26% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $873.43M | +28.85% |
| Raydium AMM | $352.01M | -10.24% |
| BisonFi | $204.07M | -15.48% |
| Meteora DLMM | $195.35M | -12.44% |
| Orca DEX | $166.59M | -49.01% |
| Tessera V | $149.50M | -27.57% |
| Manifest Trade | $131.56M | +0.20% |
| pump.fun | $100.28M | +73.96% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.58B | -0.82% | +3.93% |
| Kamino Lend | Lending | $1.36B | +1.82% | +10.71% |
| Raydium AMM | Dexs | $1.14B | -0.09% | +3.18% |
| Binance Staked SOL | Liquid Staking | $1.07B | -0.98% | +3.76% |
| Jupiter Lend | Lending | $1.07B | -1.46% | +1.75% |
| Jito Liquid Staking | Liquid Staking | $1.06B | -0.82% | +5.51% |
| BlackRock BUIDL | RWA | $987.58M | -0.40% | -0.03% |
| Jupiter Perpetual Exchange | Derivatives | $749.00M | -0.85% | +0.76% |
| Jupiter Staked SOL | Liquid Staking | $534.75M | -0.60% | +3.37% |
| xStocks | RWA | $443.31M | -1.05% | +2.37% |

## Stablecoins

Solana circulating pegged-USD: **$16.23B**
(1d -0.27% · 7d +4.54%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.20B | -2.11% |
| USDT · Tether | $2.77B | +0.00% |
| USDGO · USDGO | $1.37B | +0.74% |
| USD1 · World Liberty Financial USD | $1.28B | +2.06% |
| BUIDL · BlackRock USD | $987.58M | +0.99% |
| PYUSD · PayPal USD | $727.72M | -2.78% |
| USDG · Global Dollar | $576.28M | -1.85% |
| USDe · Ethena USDe | $536.82M | +0.31% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 78 of 737 Solana-deployed listed symbols (multiplier ok 80/80; 737 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 737 · Solana deployments 737 · priced 78 · priced-subset mcap $290.19M (lower bound, not a census).
24h volume $90.65M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $443.31M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 78 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 737 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 737 unique underlyings among 737 Solana rows; not every tokenized equity on Solana). 737 of 737 listed xStocks have a Solana deployment (737 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.35B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $987.58M
- **xStocks** (RWA) — $443.31M
- **OnRe** (RWA) — $304.03M
- **Ondo Yield Assets** (RWA) — $180.06M
- **Huma Finance V2** (RWA) — $171.51M
- **Hastra** (RWA) — $149.87M
- **Ondo Global Markets** (RWA) — $25.77M
- **Plume Vaults** (RWA) — $24.11M

## Daily active addresses

867,112 (Allium, as of 2026-09-07). Provider range 478,831–936,187. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — solana.com/news · Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — solana.com/news · Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) — solana.com/news · Fri, 04 Sep 2026 04:18:00 GMT
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — solana.com/news · Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — solana.com/news · Thu, 03 Sep 2026 15:15:00 GMT
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — solana.com/news · Wed, 02 Sep 2026 09:00:00 GMT
- [Webinar Recap: Cross-Border Payments in Latin America](https://solana.com/news/webinar-recap-cross-border-payments-in-latin-america) — solana.com/news · Tue, 01 Sep 2026 09:00:00 GMT
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) — solana.com/news · Fri, 28 Aug 2026 16:00:00 GMT `mainnet`
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) — solana.com/news · Thu, 27 Aug 2026 04:15:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-08 (2026-09-08 15:50:04 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~318 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~318 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **X / Twitter RSS** — Public X/Nitter-style RSS yielded no usable items this run (403/gated skipped). xcancel.solana empty-or-gated, xcancel.solana_status empty-or-gated, xcancel.anza_xyz empty-or-gated, xcancel.solana_devs empty-or-gated, nitter.solana 502, nitter.solana_status 502
- **xStocks** — priced up to 80 of 737 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 570ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 458ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 452ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 436ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 441ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6794ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 948ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 111ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 35ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 98ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 31ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 40ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 29ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 73ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 35ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 56ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 88ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 346ms https://solana.com/data
- `solana.com.databricks` [ok] 200 762ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 511ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 96ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 81ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 52ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 312ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 1001ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 443ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 789ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 454ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [FAIL] 502 322ms https://nitter.perennialte.ch/solana/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_status` [FAIL] 502 142ms https://nitter.perennialte.ch/solana_status/rss — HTTP 502 Bad Gateway
- `rss.nitter.anza_xyz` [FAIL] 502 141ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_devs` [FAIL] 502 137ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 502 Bad Gateway
- `rss.rsshub.solana` [FAIL] 404 228ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 16ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 456ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 453ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1837ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1804ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2327ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2004ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2217ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2068ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2352ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2025ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2215ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2126ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2254ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1871ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2010ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2005ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 5286ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2199ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2173ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2423ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2220ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1584ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1322ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1206ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.NVDAx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.AAPLx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.GOOGLx` [ok] 200 475ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.AAPLx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.MSFTx` [ok] 200 741ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 863ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.AMZNx` [ok] 200 900ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.mult.AAPLx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.MSFTx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.AMZNx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.XRXx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.COINx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.COINx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 1445ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 657ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.FLNCx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.mult.COINx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.WGSx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.SPYx` [ok] 200 2233ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.METAx` [ok] 200 1426ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.price.WRLDx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.QQQx` [ok] 200 1502ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.QQQx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 1359ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 2825ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 918ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.FLNCx` [ok] 200 1243ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.WRLDx` [ok] 200 1041ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 879ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 1430ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 1450ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.price.PCTx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.METCx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.mult.WRLDx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 1151ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.price.BETRx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.mult.SPYx` [ok] 200 791ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.QUBTx` [ok] 200 854ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.circ.WYFIx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.AIx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.price.INDIx` [ok] 200 1507ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.circ.AIx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 1274ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 1314ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.MVLLx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.mult.PCTx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.circ.MVLLx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 1161ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 1337ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.MUUx` [ok] 200 542ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.circ.INDIx` [ok] 200 1090ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 2134ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 960ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.AXTIx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.mult.BETRx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.INTWx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.circ.MUUx` [ok] 200 654ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.price.SNXXx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.INTWx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.KORUx` [ok] 200 956ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.circ.SOXSx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.MUUx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.DJTx` [ok] 200 1124ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.KORUx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.mult.SOXSx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.mult.SNXXx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.SHEINx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.price.NWGx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.mult.KORUx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.DJTx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 1739ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.NWGx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 658ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.NWGx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 509ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.MMGx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.SHEINx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 1491ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.BANKCx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.BANKCx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 826ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 1304ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.SZIGHx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 522ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.CTINSx` [ok] 200 1988ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.CRESBx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.CTINSx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 832ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 865ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.SNBIOx` [ok] 200 1809ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.CTINSx` [ok] 200 610ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 810ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 844ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.JTGEXx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.CSPCx` [ok] 200 845ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 2305ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.CMERPx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.CSPCx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.AXTIx` [ok] 200 5600ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 622ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.CMENDx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.MIXUx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.SITCx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 1607ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.MIXUx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.CRESPx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.SNDSCx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.MIXUx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 909ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.CRESPx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 581ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.SINOTx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.SNDSCx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.PRADx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 753ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 1268ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 649ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.CTFJWx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.WHGROx` [ok] 200 672ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.CLONPx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 2114ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 847ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.WHGROx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 620ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.CTPCAx` [ok] 200 1023ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.CRAUTx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.GENTEx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.SINOTx` [ok] 200 2023ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.SWPRPx` [ok] 200 819ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.SINOTx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.CKINFx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.CKAHx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 612ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 684ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 692ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 1342ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.KUAIx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 83ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 231ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INTWx` [ok] 200 110ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.KORUx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.MVLLx` [ok] 200 98ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SHEINx` [ok] 200 111ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.MUUx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.SNXXx` [ok] 200 109ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jup.tokens.search.DRAMx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.SOXSx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jito.tip_floor` [ok] 200 146ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 305ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 113ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 455ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 457ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 453ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 436ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 178ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
