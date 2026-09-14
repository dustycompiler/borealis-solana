# Borealis — Solana ecosystem report

**Generated** 2026-09-14T09:57:23Z · 2026-09-14 02:57:23 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-14T09:57:12Z · **RPC health** `ok`
**Health score** 88 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +2.35%; DEX 24h $1.64B · 1d -6% · vs-7d-ago -44%; slot 315 ms
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
| Slot | 446,947,864 |
| Block height | 424,990,381 |
| Block time | 2026-09-14T09:57:12Z |
| Epoch | 1,034 (60.15% · slot 259,864/432,000) |
| Mean TPS (last ~3,600s) | 3,499.2 |
| Mean non-vote TPS | 1,360.7 |
| Median TPS (same window) | 3,485.2 |
| Mean slot time | 315.4 ms |
| Median slot time | 315.0 ms |
| Transaction count (cluster) | 548,321,064,635 |
| Circulating supply | 586,892,847 SOL |
| Total supply | 634,017,592 SOL |
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
| Activated stake | 435,762,464 SOL |
| Delinquent stake | 2,977,903.23 SOL (0.679%) |
| Nakamoto (33% / 50% / 67%) | 18 / 40 / 79 |
| Top 10 / 20 stake share | 24.45% / 35.76% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.57M SOL | 4.03% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.36M SOL | 3.75% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.50M SOL | 2.87% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.37M SOL | 2.61% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.62M SOL | 2.21% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.25M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.03M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.37M SOL | 1.69% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.94M SOL | 1.59% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.55M SOL | 1.50% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.41% | 100% | 0 |
| 12 | `5pPRHnie…` | 5.96M SOL | 1.37% | 5% | 0 |
| 13 | `JD549Hsb…` | 5.88M SOL | 1.35% | 0% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `pSo1KZXg…` · 1.63M SOL · commission 4% · lag 691837 slots
- `7cVfgArC…` · 1.19M SOL · commission 6% · lag 235 slots
- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 387426 slots
- `mrgn4atx…` · 19.58K SOL · commission 0% · lag 94887 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 73063 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 691837 slots
- `4GEEKSwu…` · 196.81 SOL · commission 5% · lag 1138252 slots
- `toshB4tP…` · 136.49 SOL · commission 0% · lag 53403 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 1248767 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 17412181 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 446947864 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 691837 slots

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
| Jito tip-floor run-rate (NOT REV) | $20.52K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 20517 USD; at p95 floor → 227065 USD. |
| Protocol fees 24h | $14.26M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9964 |
| p90 / p99 | 0.000007 / 0.000059 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $102.21 | coingecko.simple_price |
| 24h change | +2.35% | coingecko.simple_price |
| Market cap | $59.97B | coingecko.simple_price |
| 24h volume | $2.32B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.90B |
| TVL 1d / 7d / 30d | -0.18% / -1.82% / +22.12% |
| DEX volume 24h | $1.64B · 1d -6.11% · vs-7d-ago -43.64% |
| 7d DEX volume | $17.32B · +7.77% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.26M |
| Fees 1d / 7d | +5.56% / -3.47% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $315.70M | -16.29% |
| Raydium AMM | $254.27M | -22.04% |
| BisonFi | $162.68M | 0.00% |
| fomo Wallet | $160.90M | -24.88% |
| Meteora DLMM | $157.73M | -2.07% |
| Orca DEX | $128.13M | +44.04% |
| HumidiFi | $85.03M | 0.00% |
| Tessera V | $81.22M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.55B | +0.34% | -2.84% |
| Kamino Lend | Lending | $1.35B | +0.30% | +1.41% |
| Raydium AMM | Dexs | $1.14B | -0.53% | -0.14% |
| Jupiter Lend | Lending | $1.10B | +0.07% | -0.06% |
| Binance Staked SOL | Liquid Staking | $1.05B | +0.44% | -3.66% |
| Jito Liquid Staking | Liquid Staking | $1.04B | -0.13% | -3.11% |
| BlackRock BUIDL | RWA | $992.60M | +0.00% | -2.25% |
| Jupiter Perpetual Exchange | Derivatives | $752.91M | +0.55% | -0.99% |
| Jupiter Staked SOL | Liquid Staking | $525.72M | +0.43% | -3.55% |
| Sentora Curator | Risk Curators | $389.38M | +0.36% | -0.45% |

## Stablecoins

Solana circulating pegged-USD: **$15.97B**
(1d -1.05% · 7d -2.33%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.20B | -1.42% |
| USDT · Tether | $2.48B | -2.36% |
| USDGO · USDGO | $1.38B | 0.00% |
| USD1 · World Liberty Financial USD | $1.31B | -0.00% |
| BUIDL · BlackRock USD | $992.60M | 0.00% |
| PYUSD · PayPal USD | $693.06M | -1.82% |
| USDG · Global Dollar | $604.08M | +0.09% |
| USDe · Ethena USDe | $532.86M | -0.46% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $106.50M (lower bound, not a census).
24h volume $78.83M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.93B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.60M
- **OnRe** (RWA) — $299.57M
- **Huma Finance V2** (RWA) — $192.57M
- **Ondo Yield Assets** (RWA) — $179.62M
- **Hastra** (RWA) — $145.39M
- **Plume Vaults** (RWA) — $27.55M
- **Ondo Global Markets** (RWA) — $26.72M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.35M

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

_As of 2026-09-14 (2026-09-14 02:57:23 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 155ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 30ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 64ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 30ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 30ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6449ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 212ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 148ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 24ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 57ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 25ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 26ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 29ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 75ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 158ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 56ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 75ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 177ms https://solana.com/data
- `solana.com.databricks` [ok] 200 293ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 413ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 106ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 27ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 42ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 106ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 158ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 57ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 53ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 56ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 5832ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 15390ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [FAIL]  18029ms https://nitter.perennialte.ch/anza_xyz/rss — TimeoutError: The read operation timed out
- `rss.nitter.solana_devs` [FAIL] 502 3280ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 502 Bad Gateway
- `rss.rsshub.solana` [FAIL] 404 163ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 189ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 117ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 105ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 238ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 256ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 389ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 464ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 295ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 219ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 31ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 272ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 294ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 259ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 291ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 335ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 312ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 218ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 310ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1351ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1433ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1287ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1319ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1385ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1729ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1383ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1130ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.XRXx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.COINx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.FLNCx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.SPYx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.INDIx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.circ.COINx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.WGSx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.QQQx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.COINx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.WRLDx` [ok] 200 613ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.PCTx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.SPYx` [ok] 200 1127ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.INDIx` [ok] 200 1280ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 1356ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.price.METCx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.mult.INDIx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.QUBTx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.circ.PCTx` [ok] 200 1407ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 1522ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 2040ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.price.BETRx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.XRXx` [ok] 200 2325ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 1192ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.AIx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.BETRx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.DRSx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.price.SCIx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.mult.METCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.price.SAILx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.circ.QUBTx` [ok] 200 1176ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 2937ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 1803ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.QUBTx` [ok] 200 586ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.BSYx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.price.GSATx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.circ.AIx` [ok] 200 1072ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.DRSx` [ok] 200 945ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.circ.SCIx` [ok] 200 1027ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.mult.SCIx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 1743ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.DVAx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.price.GDDYx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.price.MPx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.price.DCIx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.circ.SAILx` [ok] 200 1669ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.circ.GSATx` [ok] 200 1064ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.circ.BSYx` [ok] 200 1151ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.mult.BSYx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.mult.GSATx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.circ.WYFIx` [ok] 200 1498ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.RYANx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.BXPx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.circ.DVAx` [ok] 200 1103ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.price.DYx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.circ.GDDYx` [ok] 200 1173ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.mult.DVAx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.circ.MPx` [ok] 200 1170ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.mult.GDDYx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.price.WMSx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.mult.SAILx` [ok] 200 1065ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.mult.RYANx` [ok] 200 588ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 1365ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.mult.MPx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.mult.DCIx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.circ.BXPx` [ok] 200 993ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.mult.BXPx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.ALSNx` [ok] 200 497ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.circ.DYx` [ok] 200 1187ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.circ.FRHCx` [ok] 200 943ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.price.SFx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.price.FDSx` [ok] 200 874ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.price.SMTCx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.mult.FRHCx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.price.AMx` [ok] 200 985ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.mult.DYx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.price.AXSMx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.price.EGPx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.circ.FDSx` [ok] 200 1040ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.circ.ALSNx` [ok] 200 1278ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.circ.SFx` [ok] 200 1154ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.circ.SMTCx` [ok] 200 1113ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.circ.AXSMx` [ok] 200 904ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.circ.WMSx` [ok] 200 2146ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.mult.SMTCx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.price.BPOPx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.mult.WMSx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.AEISx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.price.TTMIx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.price.DPZx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.mult.AXSMx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 1512ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.price.HRLx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.mult.SFx` [ok] 200 772ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.price.KTOSx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.mult.AMx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.price.PAGx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.circ.EGPx` [ok] 200 1921ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.mult.EGPx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.TTMIx` [ok] 200 1020ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.price.SEICx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.circ.BPOPx` [ok] 200 1199ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.mult.BPOPx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.circ.HRLx` [ok] 200 1140ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.price.HIIx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.circ.KTOSx` [ok] 200 973ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.mult.TTMIx` [ok] 200 565ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.circ.DPZx` [ok] 200 1614ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.mult.KTOSx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.circ.AEISx` [ok] 200 1725ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.mult.HRLx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.circ.PAGx` [ok] 200 1200ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.price.GFLx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.mult.DPZx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.price.ARx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.mult.AEISx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.price.MGMx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.price.EHCx` [ok] 200 640ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.price.DOCUx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.circ.SEICx` [ok] 200 1273ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.mult.PAGx` [ok] 200 668ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.mult.SEICx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 1153ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.price.WTRGx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.HALOx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.circ.MGMx` [ok] 200 878ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.circ.GFLx` [ok] 200 1240ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.circ.DOCUx` [ok] 200 890ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.mult.HIIx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.circ.ARx` [ok] 200 1304ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.mult.GFLx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.mult.MGMx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.price.AFGx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.price.AMKRx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.circ.EHCx` [ok] 200 1229ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.mult.ARx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.price.HUBSx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.mult.EHCx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.price.GMEDx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.circ.WTRGx` [ok] 200 1167ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.circ.HALOx` [ok] 200 1159ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.price.JKHYx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.WTRGx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.mult.HALOx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.mult.DOCUx` [ok] 200 1083ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.price.IESCx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.price.OCx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.circ.AFGx` [ok] 200 1111ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.circ.AMKRx` [ok] 200 1045ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.circ.HUBSx` [ok] 200 980ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 920ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.price.CRx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.mult.AFGx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.price.BMRNx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.mult.HUBSx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.price.AMHx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.price.JEFx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.mult.AMKRx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.circ.JKHYx` [ok] 200 1014ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.price.FIVEx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.mult.JKHYx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.circ.OCx` [ok] 200 1081ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.price.ITx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.mult.OCx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.circ.IESCx` [ok] 200 1320ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.price.MDGLx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.mult.IESCx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.VNOMx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.circ.VNOMx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.circ.AMHx` [ok] 200 1348ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.mult.VNOMx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.UHALx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.circ.BMRNx` [ok] 200 1628ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.circ.CRx` [ok] 200 1854ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.circ.ITx` [ok] 200 1078ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.circ.FIVEx` [ok] 200 1371ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.mult.BMRNx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.mult.CRx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.mult.AMHx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.price.AHRx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.price.IVZx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.mult.ITx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.circ.MDGLx` [ok] 200 1099ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.price.CORTx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.circ.JEFx` [ok] 200 1962ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.price.STRLx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.mult.JEFx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.mult.MDGLx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.price.AURx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.circ.UHALx` [ok] 200 925ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.mult.FIVEx` [ok] 200 767ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.price.NWSAx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.mult.UHALx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.price.Hx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.price.ARWRx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.circ.AHRx` [ok] 200 971ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.circ.STRLx` [ok] 200 943ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.circ.IVZx` [ok] 200 1198ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.circ.CORTx` [ok] 200 1130ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.mult.STRLx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.mult.AHRx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.NWSx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.mult.IVZx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.price.MANHx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.circ.NWSAx` [ok] 200 1168ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.mult.CORTx` [ok] 200 587ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.circ.AURx` [ok] 200 1507ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.price.CACIx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.price.GWREx` [ok] 200 704ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.mult.NWSAx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.circ.Hx` [ok] 200 1292ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.mult.AURx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.mult.Hx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.price.BAXx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.ARWRx` [ok] 200 1764ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 1283ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.circ.MANHx` [ok] 200 1117ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.mult.NWSx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.circ.GWREx` [ok] 200 1259ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.circ.BAXx` [ok] 200 1195ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.BAXx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.GWREx` [ok] 200 836ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.circ.CACIx` [ok] 200 2470ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 24ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 93ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INDIx` [ok] 200 39ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 41ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 40ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.BETRx` [ok] 200 45ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.FLNCx` [ok] 200 41ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.XRXx` [ok] 200 37ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.PCTx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.AIx` [ok] 200 48ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jito.tip_floor` [ok] 200 265ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 205ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 47ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 36ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 106ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 39ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 26ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 228ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
