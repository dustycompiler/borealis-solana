# Borealis — Solana ecosystem report

**Generated** 2026-09-24T10:00:53Z · 2026-09-24 03:00:53 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-24T10:00:44Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -3.59%; DEX 24h $2.68B · 1d -16% · vs-7d-ago -4%; slot 265 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -16.03%. (threshold: `|1d %| >= 8`)
- **WARN · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -3.59%, DeFiLlama TVL 1d -2.00%, DEX 1d -16.03%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 449,995,419 |
| Block height | 428,035,541 |
| Block time | 2026-09-24T10:00:44Z |
| Epoch | 1,041 (65.61% · slot 283,421/432,000) |
| Mean TPS (last ~3,600s) | 4,342.9 |
| Mean non-vote TPS | 1,804.5 |
| Median TPS (same window) | 4,315.1 |
| Mean slot time | 265.2 ms |
| Median slot time | 265.5 ms |
| Transaction count (cluster) | 552,049,727,786 |
| Circulating supply | 587,577,291 SOL |
| Total supply | 634,608,402 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,745,225 SOL |
| Delinquent stake | 218,911.39 SOL (0.050%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.40% / 35.68% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.84M SOL | 4.06% | 7% | 0 |
| 2 | `HEL1USMZ…` | 15.84M SOL | 3.60% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.36M SOL | 2.81% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.26M SOL | 2.56% | 5% | 0 |
| 5 | `E1r4Psq8…` | 10.34M SOL | 2.35% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.23M SOL | 2.10% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.16M SOL | 2.08% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.60M SOL | 1.73% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.09M SOL | 1.61% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.56M SOL | 1.49% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.22M SOL | 1.42% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.13M SOL | 1.39% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.35% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.61M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `6DTkuiey…` · 89.15K SOL · commission 100% · lag 449995419 slots
- `HDRqPft5…` · 71.15K SOL · commission 100% · lag 449995419 slots
- `STaKesuX…` · 19.22K SOL · commission 100% · lag 2158 slots
- `t23p8aBQ…` · 14.37K SOL · commission 0% · lag 2400183 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 63578 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 1196709 slots
- `mrgn4atx…` · 2.21K SOL · commission 0% · lag 1398014 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 2120667 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 1502548 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 1233044 slots
- `R1parD2C…` · 2.87 SOL · commission 5% · lag 65946549 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 90911 slots

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
| **In-protocol fees 24h** | **$1.09M** (9,201.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-22 |
| **Solana REV** | **11,385.8 SOL** / **$1.34M** | MEASURED UTC calendar day 2026-09-22: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-22 · UTC day 2026-09-22 · SOL-USD date 2026-09-22 |
| Jito tip-floor run-rate (NOT REV) | $43.15K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 43150 USD; at p95 floor → 1999701 USD. |
| Protocol fees 24h | $16.52M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $113.13 | coingecko.simple_price |
| 24h change | -3.59% | coingecko.simple_price |
| Market cap | $66.48B | coingecko.simple_price |
| 24h volume | $4.75B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.40B |
| TVL 1d / 7d / 30d | -2.00% / +10.74% / +11.36% |
| DEX volume 24h | $2.68B · 1d -16.03% · vs-7d-ago -4.17% |
| 7d DEX volume | $19.96B · +11.85% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $16.52M |
| Fees 1d / 7d | -7.58% / +10.91% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| BisonFi | $368.17M | 0.00% |
| Raydium AMM | $354.80M | -25.44% |
| Orca DEX | $347.44M | -5.49% |
| PumpSwap | $270.19M | -57.39% |
| Meteora DLMM | $233.66M | -12.43% |
| Scorch | $129.41M | 0.00% |
| pump.fun | $121.03M | 0.00% |
| fomo Wallet | $118.88M | -19.58% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.85B | -1.86% | +16.37% |
| Kamino Lend | Lending | $1.41B | -1.28% | +5.11% |
| Raydium AMM | Dexs | $1.31B | -2.67% | +17.47% |
| Jito Liquid Staking | Liquid Staking | $1.20B | -2.37% | +16.12% |
| Binance Staked SOL | Liquid Staking | $1.18B | -2.59% | +14.18% |
| Jupiter Lend | Lending | $1.17B | -2.28% | +7.94% |
| Jupiter Perpetual Exchange | Derivatives | $805.32M | -2.11% | +8.50% |
| Jupiter Staked SOL | Liquid Staking | $598.09M | -2.60% | +15.94% |
| Marinade Native | Staking Pool | $443.56M | -2.74% | +16.66% |
| PumpSwap | Dexs | $376.74M | -1.35% | +17.40% |

## Stablecoins

Solana circulating pegged-USD: **$17.11B**
(1d -2.70% · 7d +4.21%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $8.54B | +7.30% |
| USDT · Tether | $2.14B | +0.00% |
| USDGO · USDGO | $1.42B | +1.00% |
| USD1 · World Liberty Financial USD | $1.38B | +0.73% |
| BUIDL · BlackRock USD | $987.68M | +0.01% |
| PYUSD · PayPal USD | $735.07M | -0.52% |
| USDG · Global Dollar | $631.45M | +0.30% |
| USDe · Ethena USDe | $496.63M | -1.19% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $111.78K (lower bound, not a census).
24h volume $152.57M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$543.26M** across 16 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $301.16M
- **Huma** (RWA) — $196.70M
- **Plume Vaults** (RWA) — $28.21M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $2.98M
- **VNX** (RWA) — $2.70M
- **Oro Finance** (RWA) — $2.49M
- **International Stable Currency** (RWA) — $2.44M

## Daily active addresses

867,560 (Allium, as of 2026-09-22). Provider range 489,457–895,781. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — solana.com/news · Wed, 23 Sep 2026 14:06:00 GMT
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

_As of 2026-09-24 (2026-09-24 03:00:53 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=live, 200ms=pending. Observed mean slot ~265 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~265 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 226ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 141ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 244ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 204ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 168ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6107ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 385ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 89ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 112ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 168ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 59ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 835ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1194ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 195ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 601ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 94ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 134ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 456ms https://solana.com/data
- `solana.com.databricks` [ok] 200 280ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 577ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 192ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 96ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 141ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 186ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 330ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 119ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 117ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 134ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 133ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 190ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 90ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 162ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 308ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 177ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 133ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 135ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 205ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 168ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 164ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 90ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 249ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 155ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 267ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 165ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 227ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 166ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 232ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 153ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 134ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 183ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 208ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 159ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 270ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 162ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 242ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 143ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 186ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 180ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 193ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 110ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 193ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 140ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 230ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 150ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 2619ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2276ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 3019ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2908ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1971ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2091ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2332ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 2004ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.INDIx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.FLNCx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.QUBTx` [ok] 200 750ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.WRLDx` [ok] 200 761ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.WGSx` [ok] 200 784ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.circ.WRLDx` [ok] 200 1209ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.price.METCx` [ok] 200 2069ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.QUBTx` [ok] 200 1348ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 1986ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.price.XRXx` [ok] 200 3020ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.PCTx` [ok] 200 3088ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.INDIx` [ok] 200 2948ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 1454ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 1585ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 2846ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 1229ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.METCx` [ok] 200 1923ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.XRXx` [ok] 200 1074ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.price.BETRx` [ok] 200 545ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.AIx` [ok] 200 722ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.INDIx` [ok] 200 1096ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.WYFIx` [ok] 200 1095ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.MIDDx` [ok] 200 872ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data
- `xstocks.circ.PCTx` [ok] 200 2528ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 1982ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 2571ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 2470ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 1726ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.RITMx` [ok] 200 672ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data
- `xstocks.price.ALMx` [ok] 200 1161ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data
- `xstocks.circ.MIDDx` [ok] 200 2440ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 2177ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 3650ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.price.RNGx` [ok] 200 1169ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data
- `xstocks.mult.BETRx` [ok] 200 1914ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 4895ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.SHCx` [ok] 200 1338ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data
- `xstocks.circ.ALMx` [ok] 200 2328ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 1591ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.REYNx` [ok] 200 1178ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data
- `xstocks.circ.RNGx` [ok] 200 2109ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object
- `xstocks.price.WHx` [ok] 200 1942ms https://api.backed.fi/api/v2/public/assets/WHx/price-data
- `xstocks.mult.MIDDx` [ok] 200 2660ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana
- `xstocks.circ.RITMx` [ok] 200 3243ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object
- `xstocks.price.VSNTx` [ok] 200 956ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data
- `xstocks.circ.SHCx` [ok] 200 2444ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object
- `xstocks.mult.ALMx` [ok] 200 2133ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana
- `xstocks.circ.REYNx` [ok] 200 2470ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object
- `xstocks.price.CARx` [ok] 200 1835ms https://api.backed.fi/api/v2/public/assets/CARx/price-data
- `xstocks.circ.WHx` [ok] 200 2142ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object
- `xstocks.price.OZKx` [ok] 200 1301ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data
- `xstocks.circ.VSNTx` [ok] 200 2520ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object
- `xstocks.mult.RNGx` [ok] 200 3025ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana
- `xstocks.mult.SHCx` [ok] 200 2216ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana
- `xstocks.circ.CARx` [ok] 200 2388ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object
- `xstocks.circ.OZKx` [ok] 200 1840ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object
- `xstocks.mult.RITMx` [ok] 200 4813ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana
- `xstocks.price.GXOx` [ok] 200 1722ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data
- `xstocks.price.IRDMx` [ok] 200 2507ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data
- `xstocks.mult.WHx` [ok] 200 3189ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana
- `xstocks.price.FBINx` [ok] 200 632ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data
- `xstocks.mult.REYNx` [ok] 200 4312ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana
- `xstocks.price.AMTMx` [ok] 200 1044ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data
- `xstocks.mult.CARx` [ok] 200 2151ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana
- `xstocks.mult.VSNTx` [ok] 200 3913ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana
- `xstocks.price.MTNx` [ok] 200 1098ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data
- `xstocks.mult.OZKx` [ok] 200 2774ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana
- `xstocks.circ.GXOx` [ok] 200 2559ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object
- `xstocks.price.PSNx` [ok] 200 1460ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data
- `xstocks.circ.IRDMx` [ok] 200 2804ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object
- `xstocks.price.PEGAx` [ok] 200 1770ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data
- `xstocks.price.SAICx` [ok] 200 1410ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data
- `xstocks.circ.FBINx` [ok] 200 3530ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object
- `xstocks.circ.MTNx` [ok] 200 3055ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object
- `xstocks.mult.GXOx` [ok] 200 3477ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana
- `xstocks.circ.AMTMx` [ok] 200 5404ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object
- `xstocks.circ.PSNx` [ok] 200 4294ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object
- `xstocks.circ.PEGAx` [ok] 200 4071ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object
- `xstocks.price.EXLSx` [ok] 200 1381ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data
- `xstocks.mult.IRDMx` [ok] 200 5111ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana
- `xstocks.mult.MTNx` [ok] 200 4251ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana
- `xstocks.mult.FBINx` [ok] 200 5924ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana
- `xstocks.circ.EXLSx` [ok] 200 2610ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object
- `xstocks.price.CRUSx` [ok] 200 925ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data
- `xstocks.circ.SAICx` [ok] 200 6818ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object
- `xstocks.price.Mx` [ok] 200 961ms https://api.backed.fi/api/v2/public/assets/Mx/price-data
- `xstocks.price.EPAMx` [ok] 200 4163ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data
- `xstocks.mult.PSNx` [ok] 200 5383ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana
- `xstocks.mult.AMTMx` [ok] 200 6010ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana
- `xstocks.mult.PEGAx` [ok] 200 5936ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana
- `xstocks.circ.Mx` [ok] 200 2557ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object
- `xstocks.circ.CRUSx` [ok] 200 3386ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object
- `xstocks.mult.SAICx` [ok] 200 4295ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana
- `xstocks.mult.EXLSx` [ok] 200 5357ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana
- `xstocks.mult.CRUSx` [ok] 200 3213ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana
- `xstocks.mult.Mx` [ok] 200 4177ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana
- `xstocks.circ.EPAMx` [ok] 200 6290ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object
- `xstocks.mult.EPAMx` [ok] 200 2635ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana
- `xstocks.price.CPBx` [ok] 200 2408ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data
- `xstocks.price.SNDRx` [ok] 200 11403ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data
- `xstocks.price.ELFx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.VNOx` [ok] 200 11815ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data
- `xstocks.circ.CPBx` [ok] 200 1779ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object
- `xstocks.price.EXPx` [ok] 200 11595ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data
- `xstocks.price.VIRTx` [FAIL]  12046ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SNDRx` [ok] 200 3733ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object
- `xstocks.circ.VNOx` [ok] 200 3192ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object
- `xstocks.price.MKTXx` [ok] 200 11800ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data
- `xstocks.circ.ELFx` [ok] 200 4471ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object
- `xstocks.price.HXLx` [ok] 200 11431ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data
- `xstocks.mult.CPBx` [ok] 200 4226ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana
- `xstocks.circ.MKTXx` [ok] 200 990ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object
- `xstocks.price.VFCx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data
- `xstocks.mult.SNDRx` [ok] 200 2718ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana
- `xstocks.mult.VNOx` [ok] 200 2350ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana
- `xstocks.circ.EXPx` [ok] 200 4709ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object
- `xstocks.price.ADTx` [ok] 200 498ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data
- `xstocks.mult.MKTXx` [ok] 200 1838ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana
- `xstocks.mult.ELFx` [ok] 200 2947ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana
- `xstocks.mult.EXPx` [ok] 200 1611ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana
- `xstocks.circ.VFCx` [ok] 200 2776ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object
- `xstocks.price.ACIx` [ok] 200 925ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data
- `xstocks.price.BCx` [ok] 200 1541ms https://api.backed.fi/api/v2/public/assets/BCx/price-data
- `xstocks.price.NXSTx` [ok] 200 3008ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data
- `xstocks.price.KRMNx` [ok] 200 1353ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data
- `xstocks.mult.VFCx` [ok] 200 1344ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana
- `xstocks.circ.ADTx` [ok] 200 3043ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object
- `xstocks.circ.VIRTx` [ok] 200 7105ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object
- `xstocks.price.GTESx` [ok] 200 1007ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data
- `xstocks.mult.ADTx` [ok] 200 1021ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana
- `xstocks.circ.ACIx` [ok] 200 2427ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object
- `xstocks.circ.KRMNx` [ok] 200 2275ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object
- `xstocks.price.HRBx` [ok] 200 989ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data
- `xstocks.mult.ACIx` [ok] 200 988ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana
- `xstocks.mult.VIRTx` [ok] 200 1847ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana
- `xstocks.circ.NXSTx` [ok] 200 2949ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object
- `xstocks.circ.HXLx` [ok] 200 7648ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object
- `xstocks.price.DLBx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data
- `xstocks.circ.GTESx` [ok] 200 1976ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object
- `xstocks.mult.KRMNx` [ok] 200 1030ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana
- `xstocks.mult.NXSTx` [ok] 200 951ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana
- `xstocks.mult.HXLx` [ok] 200 861ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana
- `xstocks.price.TFXx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data
- `xstocks.mult.GTESx` [ok] 200 848ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana
- `xstocks.price.RYNx` [ok] 200 786ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data
- `xstocks.price.POOLx` [ok] 200 637ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data
- `xstocks.circ.BCx` [ok] 200 5163ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object
- `xstocks.price.AXSx` [ok] 200 2084ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data
- `xstocks.circ.HRBx` [ok] 200 2524ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object
- `xstocks.circ.RYNx` [ok] 200 1542ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object
- `xstocks.price.LWx` [ok] 200 1746ms https://api.backed.fi/api/v2/public/assets/LWx/price-data
- `xstocks.mult.BCx` [ok] 200 1661ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana
- `xstocks.circ.TFXx` [ok] 200 2157ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object
- `xstocks.circ.DLBx` [ok] 200 3272ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object
- `xstocks.price.AAONx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.mult.RYNx` [ok] 200 818ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana
- `xstocks.circ.AXSx` [ok] 200 2070ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object
- `xstocks.mult.HRBx` [ok] 200 1841ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana
- `xstocks.price.SONx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/SONx/price-data
- `xstocks.mult.DLBx` [ok] 200 932ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana
- `xstocks.price.INGMx` [ok] 200 484ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data
- `xstocks.price.TTDx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data
- `xstocks.mult.TFXx` [ok] 200 1503ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana
- `xstocks.price.HRx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/HRx/price-data
- `xstocks.circ.LWx` [ok] 200 2659ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object
- `xstocks.circ.INGMx` [ok] 200 1728ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object
- `xstocks.mult.AXSx` [ok] 200 2742ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana
- `xstocks.price.RLIx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data
- `xstocks.mult.INGMx` [ok] 200 901ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana
- `xstocks.circ.HRx` [ok] 200 2000ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object
- `xstocks.price.CLFx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data
- `xstocks.circ.RLIx` [ok] 200 1087ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object
- `xstocks.mult.HRx` [ok] 200 955ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana
- `xstocks.circ.CLFx` [ok] 200 863ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object
- `xstocks.price.STWDx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data
- `xstocks.circ.AAONx` [ok] 200 4934ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.mult.RLIx` [ok] 200 987ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana
- `xstocks.price.MSMx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data
- `xstocks.mult.LWx` [ok] 200 3873ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana
- `xstocks.mult.CLFx` [ok] 200 1514ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana
- `xstocks.circ.TTDx` [ok] 200 5345ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object
- `xstocks.price.CZRx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data
- `xstocks.price.OMFx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data
- `xstocks.circ.STWDx` [ok] 200 1980ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object
- `xstocks.mult.TTDx` [ok] 200 920ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana
- `xstocks.price.CROXx` [ok] 200 664ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data
- `xstocks.circ.CZRx` [ok] 200 1652ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object
- `xstocks.mult.AAONx` [ok] 200 3291ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.circ.OMFx` [ok] 200 1908ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object
- `xstocks.circ.SONx` [ok] 200 8263ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object
- `xstocks.price.CHEx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data
- `xstocks.circ.MSMx` [ok] 200 3227ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object
- `xstocks.circ.CHEx` [ok] 200 829ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object
- `xstocks.mult.STWDx` [ok] 200 2923ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana
- `xstocks.circ.POOLx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.SONx` [ok] 200 1332ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana
- `xstocks.mult.CZRx` [ok] 200 1880ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana
- `xstocks.price.Gx` [ok] 200 707ms https://api.backed.fi/api/v2/public/assets/Gx/price-data
- `xstocks.mult.OMFx` [ok] 200 2350ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana
- `xstocks.mult.POOLx` [ok] 200 1036ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana
- `xstocks.price.ALGMx` [ok] 200 1046ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data
- `xstocks.mult.CHEx` [ok] 200 1480ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana
- `xstocks.circ.CROXx` [ok] 200 3151ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object
- `xstocks.price.BEPCx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data
- `xstocks.price.MTDRx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data
- `xstocks.price.INGRx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data
- `xstocks.price.MTGx` [ok] 200 1710ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data
- `xstocks.mult.MSMx` [ok] 200 2967ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana
- `xstocks.mult.CROXx` [ok] 200 1089ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana
- `xstocks.price.LYFTx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data
- `xstocks.price.BYDx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data
- `xstocks.circ.INGRx` [ok] 200 2082ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object
- `xstocks.circ.ALGMx` [ok] 200 2814ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object
- `xstocks.circ.MTGx` [ok] 200 2161ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object
- `xstocks.circ.MTDRx` [ok] 200 2888ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object
- `xstocks.circ.Gx` [ok] 200 3802ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object
- `xstocks.circ.BEPCx` [ok] 200 3181ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object
- `xstocks.circ.BYDx` [ok] 200 2176ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object
- `xstocks.mult.MTGx` [ok] 200 1559ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana
- `xstocks.mult.MTDRx` [ok] 200 1331ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana
- `xstocks.price.STAGx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data
- `xstocks.mult.Gx` [ok] 200 1396ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana
- `xstocks.circ.LYFTx` [ok] 200 3335ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object
- `xstocks.price.FNBx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data
- `xstocks.mult.BYDx` [ok] 200 1169ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana
- `xstocks.mult.BEPCx` [ok] 200 1757ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana
- `xstocks.mult.ALGMx` [ok] 200 2481ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana
- `xstocks.price.CACCx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data
- `xstocks.price.MBGLx` [ok] 200 858ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data
- `xstocks.mult.INGRx` [ok] 200 3417ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana
- `xstocks.mult.LYFTx` [ok] 200 1724ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana
- `xstocks.circ.FNBx` [ok] 200 1989ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object
- `xstocks.circ.MBGLx` [ok] 200 2126ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object
- `xstocks.mult.FNBx` [ok] 200 1457ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana
- `xstocks.circ.STAGx` [ok] 200 3558ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object
- `xstocks.circ.CACCx` [ok] 200 3030ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object
- `xstocks.mult.MBGLx` [ok] 200 1200ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana
- `xstocks.mult.STAGx` [ok] 200 1744ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana
- `xstocks.mult.CACCx` [ok] 200 3349ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 67ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 309ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.BETRx` [ok] 200 96ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.XRXx` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.QUBTx` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.FLNCx` [ok] 200 97ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.AIx` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.WGSx` [ok] 200 91ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.WYFIx` [ok] 200 90ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.INDIx` [ok] 200 85ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jito.tip_floor` [ok] 200 168ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 248ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 133ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 154ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 127ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 126ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 202ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 209ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
