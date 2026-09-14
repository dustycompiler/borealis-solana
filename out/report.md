# Borealis — Solana ecosystem report

**Generated** 2026-09-14T10:52:57Z · 2026-09-14 03:52:57 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-14T10:52:47Z · **RPC health** `ok`
**Health score** 91 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +2.38%; DEX 24h $1.64B · 1d -6% · vs-7d-ago -44%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -43.64%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 446,958,440 |
| Block height | 425,000,942 |
| Block time | 2026-09-14T10:52:47Z |
| Epoch | 1,034 (62.60% · slot 270,445/432,000) |
| Mean TPS (last ~3,600s) | 3,457.9 |
| Mean non-vote TPS | 1,325.7 |
| Median TPS (same window) | 3,452.3 |
| Mean slot time | 315.3 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 548,332,534,003 |
| Circulating supply | 586,892,817 SOL |
| Total supply | 634,017,562 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 678 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 436,948,146 SOL |
| Delinquent stake | 1,792,221.16 SOL (0.408%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.39% / 35.66% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.57M SOL | 4.02% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.36M SOL | 3.74% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.50M SOL | 2.86% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.37M SOL | 2.60% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.62M SOL | 2.20% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.25M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.03M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.37M SOL | 1.69% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.94M SOL | 1.59% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.55M SOL | 1.50% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `5pPRHnie…` | 5.96M SOL | 1.37% | 5% | 0 |
| 13 | `JD549Hsb…` | 5.88M SOL | 1.34% | 0% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `pSo1KZXg…` · 1.63M SOL · commission 4% · lag 702413 slots
- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 398002 slots
- `mrgn4atx…` · 19.58K SOL · commission 0% · lag 105463 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 83639 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 702413 slots
- `4GEEKSwu…` · 196.81 SOL · commission 5% · lag 1148828 slots
- `toshB4tP…` · 136.49 SOL · commission 0% · lag 63979 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 1259343 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 17422757 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 446958440 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 702413 slots
- `4kdjgZKJ…` · 1.05 SOL · commission 100% · lag 446958440 slots

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
| **In-protocol fees 24h** | **$711.96K** (6,973.3 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-12 |
| **Solana REV** | **7,963.8 SOL** / **$813.09K** | MEASURED UTC calendar day 2026-09-12: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-12 · UTC day 2026-09-12 · SOL-USD date 2026-09-12 |
| Jito tip-floor run-rate (NOT REV) | $31.47K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 31473 USD; at p95 floor → 235098 USD. |
| Protocol fees 24h | $14.26M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9973 |
| p90 / p99 | 0.000008 / 0.000080 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $101.88 | coingecko.simple_price |
| 24h change | +2.38% | coingecko.simple_price |
| Market cap | $59.83B | coingecko.simple_price |
| 24h volume | $2.39B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.89B |
| TVL 1d / 7d / 30d | -0.26% / -1.90% / +22.02% |
| DEX volume 24h | $1.64B · 1d -6.11% · vs-7d-ago -43.64% |
| 7d DEX volume | $17.32B · +7.77% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.26M |
| Fees 1d / 7d | +5.55% / -3.48% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $315.70M | -16.29% |
| Raydium AMM | $250.08M | -23.32% |
| BisonFi | $162.68M | 0.00% |
| fomo Wallet | $160.90M | -24.88% |
| Meteora DLMM | $157.73M | -2.07% |
| Orca DEX | $128.13M | +44.04% |
| HumidiFi | $85.03M | 0.00% |
| Tessera V | $81.22M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.55B | +1.26% | -3.36% |
| Kamino Lend | Lending | $1.35B | +0.67% | +1.05% |
| Raydium AMM | Dexs | $1.14B | -0.53% | -0.14% |
| Jupiter Lend | Lending | $1.10B | +0.76% | -0.18% |
| Binance Staked SOL | Liquid Staking | $1.05B | +1.33% | -3.63% |
| Jito Liquid Staking | Liquid Staking | $1.04B | +0.28% | -2.80% |
| BlackRock BUIDL | RWA | $992.60M | +0.00% | -2.25% |
| Jupiter Perpetual Exchange | Derivatives | $751.95M | +1.17% | -0.57% |
| Jupiter Staked SOL | Liquid Staking | $524.50M | +0.19% | -3.04% |
| Sentora Curator | Risk Curators | $388.86M | +0.34% | -0.50% |

## Stablecoins

Solana circulating pegged-USD: **$15.96B**
(1d -1.05% · 7d -2.32%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.19B | -1.65% |
| USDT · Tether | $2.48B | -2.36% |
| USDGO · USDGO | $1.39B | +0.65% |
| USD1 · World Liberty Financial USD | $1.31B | -0.00% |
| BUIDL · BlackRock USD | $992.60M | 0.00% |
| PYUSD · PayPal USD | $693.11M | -1.82% |
| USDG · Global Dollar | $604.14M | +0.09% |
| USDe · Ethena USDe | $532.87M | -0.46% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $106.64M (lower bound, not a census).
24h volume $80.02M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.93B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.60M
- **OnRe** (RWA) — $299.58M
- **Huma Finance V2** (RWA) — $192.60M
- **Ondo Yield Assets** (RWA) — $180.11M
- **Hastra** (RWA) — $144.97M
- **Plume Vaults** (RWA) — $27.55M
- **Ondo Global Markets** (RWA) — $26.57M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.32M

## Daily active addresses

830,449 (Allium, as of 2026-09-12). Provider range 394,537–881,822. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-14 (2026-09-14 03:52:57 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~315 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~315 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 593ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 569ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 749ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 628ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 570ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6556ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1162ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 41ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 64ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 57ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 31ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 28ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 965ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 82ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 53ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 48ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 82ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 297ms https://solana.com/data
- `solana.com.databricks` [ok] 200 74ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 531ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 229ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 115ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 90ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 304ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 312ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 91ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 99ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 90ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 4530ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 302ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [FAIL] 502 201ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_devs` [FAIL] 502 687ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 502 Bad Gateway
- `rss.rsshub.solana` [FAIL] 404 268ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 133ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 554ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 532ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2536ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2339ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2338ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2012ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2591ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2142ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2111ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1885ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2515ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2566ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1799ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1964ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2590ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2242ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1997ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1895ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1434ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1386ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1662ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1533ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1466ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1229ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.SPYx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.FLNCx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.COINx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.INDIx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.QQQx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.COINx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.XRXx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.WRLDx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.mult.COINx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.WGSx` [ok] 200 591ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.mult.FLNCx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.PCTx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.WRLDx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.QUBTx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.circ.WGSx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 858ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.price.BETRx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.WYFIx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.QQQx` [ok] 200 645ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 795ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 704ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 717ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.DRSx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.price.SAILx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.mult.QUBTx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.METCx` [ok] 200 1150ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.BSYx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.price.SCIx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.mult.BETRx` [ok] 200 406ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.circ.BSYx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.circ.SAILx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.circ.SCIx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.price.GSATx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.circ.DRSx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.mult.SAILx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.mult.BSYx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.SCIx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.circ.GSATx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.price.MPx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.mult.DRSx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.DCIx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.price.RYANx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.price.GDDYx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.price.BXPx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.circ.DCIx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.circ.MPx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.price.AIx` [ok] 200 1243ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.GDDYx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.circ.RYANx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.price.DVAx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.circ.AIx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.GSATx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.BXPx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.circ.DVAx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.mult.BXPx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.GDDYx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.mult.RYANx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.mult.DCIx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.price.DYx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.price.WMSx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.mult.DVAx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.price.ALSNx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.circ.DYx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.price.FDSx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.circ.FRHCx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.circ.WMSx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.price.SMTCx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.price.AMx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.mult.DYx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.circ.FDSx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.circ.SMTCx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.price.SFx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.mult.FDSx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.circ.ALSNx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.price.AXSMx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.mult.SMTCx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.circ.SFx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.circ.AXSMx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.mult.MPx` [ok] 200 1204ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.price.BPOPx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.price.EGPx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.price.TTMIx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.price.AEISx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.mult.WMSx` [ok] 200 705ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.circ.AMx` [ok] 200 709ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.circ.TTMIx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.circ.EGPx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.price.DPZx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.circ.AEISx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.mult.EGPx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.mult.AMx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.mult.TTMIx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.circ.DPZx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.mult.AEISx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.price.PAGx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.price.KTOSx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.mult.DPZx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.circ.PAGx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.price.HRLx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.price.SEICx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.mult.PAGx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.circ.HRLx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.mult.AXSMx` [ok] 200 1110ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.circ.KTOSx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.price.EHCx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.circ.SEICx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.mult.SFx` [ok] 200 1264ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.price.GFLx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.mult.KTOSx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.circ.GFLx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.price.HIIx` [ok] 200 661ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.price.MGMx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.mult.BPOPx` [ok] 200 1150ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.price.ARx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.mult.GFLx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.circ.EHCx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.circ.ARx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.price.HALOx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.price.DOCUx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.mult.EHCx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.HIIx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.mult.SEICx` [ok] 200 654ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.circ.HALOx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.mult.ARx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.circ.DOCUx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.price.WTRGx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.AFGx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.circ.MGMx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.price.AMKRx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.circ.WTRGx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.price.HUBSx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.mult.HALOx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.circ.AMKRx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.mult.WTRGx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.mult.MGMx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.mult.DOCUx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.circ.HUBSx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.price.GMEDx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.mult.HRLx` [ok] 200 1329ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.IESCx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.mult.AMKRx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.mult.AFGx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.price.CRx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.circ.IESCx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.price.JEFx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.circ.CRx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.mult.IESCx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.JKHYx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.circ.JEFx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.mult.GMEDx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.mult.CRx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.circ.JKHYx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.price.FIVEx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.mult.JKHYx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.mult.JEFx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.price.ITx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.circ.FIVEx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.price.AMHx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.AMHx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.circ.ITx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.mult.FIVEx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.price.VNOMx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.price.BMRNx` [ok] 200 829ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.circ.VNOMx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.price.UHALx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.price.OCx` [ok] 200 1159ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.circ.BMRNx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.price.AHRx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.circ.OCx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.circ.UHALx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.mult.ITx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.VNOMx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.circ.AHRx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.price.IVZx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.mult.OCx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.price.MDGLx` [ok] 200 771ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.mult.UHALx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.circ.IVZx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.circ.MDGLx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.price.NWSAx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.price.STRLx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.price.CORTx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.mult.MDGLx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.circ.NWSAx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.circ.CORTx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.price.AURx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.mult.BMRNx` [ok] 200 911ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.mult.AHRx` [ok] 200 638ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.mult.NWSAx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.circ.STRLx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.price.GWREx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.mult.STRLx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.mult.AURx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.price.Hx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.mult.IVZx` [ok] 200 905ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.mult.CORTx` [ok] 200 499ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.NWSx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.circ.GWREx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.price.MANHx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.circ.Hx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.price.CACIx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.circ.MANHx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.mult.Hx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.circ.CACIx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.mult.CACIx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.price.BAXx` [ok] 200 958ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.BAXx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.HUBSx` [ok] 200 3738ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.price.ARWRx` [ok] 200 1618ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.circ.ARWRx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.mult.BAXx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.ARWRx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 586ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 139ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INDIx` [ok] 200 64ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 72ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.BETRx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.FLNCx` [ok] 200 59ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.XRXx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.PCTx` [ok] 200 58ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.AIx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jito.tip_floor` [ok] 200 116ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 289ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 74ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 552ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 684ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 620ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 598ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 140ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
