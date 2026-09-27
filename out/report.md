# Borealis — Solana ecosystem report

**Generated** 2026-09-27T13:17:15Z · 2026-09-27 06:17:15 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-27T13:17:07Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +1.70%; DEX 24h $2.16B · 1d -18% · vs-7d-ago -25%; slot 268 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -17.52%. (threshold: `|1d %| >= 8`)
- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +18.18%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -25.07%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +25.18%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 451,007,898 |
| Block height | 429,047,602 |
| Block time | 2026-09-27T13:17:07Z |
| Epoch | 1,043 (99.98% · slot 431,899/432,000) |
| Mean TPS (last ~3,600s) | 4,431.4 |
| Mean non-vote TPS | 1,921.2 |
| Median TPS (same window) | 4,340.1 |
| Mean slot time | 268.3 ms |
| Median slot time | 267.9 ms |
| Transaction count (cluster) | 553,267,738,220 |
| Circulating supply | 587,711,732 SOL |
| Total supply | 634,762,935 SOL |
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
| Activated stake | 437,506,022 SOL |
| Delinquent stake | 36,632.09 SOL (0.008%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.61% / 35.43% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.86M SOL | 4.08% | 7% | 0 |
| 2 | `HEL1USMZ…` | 15.80M SOL | 3.61% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.34M SOL | 2.82% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.22M SOL | 2.57% | 5% | 0 |
| 5 | `E1r4Psq8…` | 10.84M SOL | 2.48% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.24M SOL | 2.11% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.18M SOL | 2.10% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.61M SOL | 1.74% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.09M SOL | 1.62% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.51M SOL | 1.49% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.25M SOL | 1.43% | 0% | 0 |
| 12 | `5pPRHnie…` | 5.93M SOL | 1.36% | 5% | 0 |
| 13 | `5Cchr1XG…` | 5.63M SOL | 1.29% | 100% | 0 |
| 14 | `9rkJMARq…` | 4.70M SOL | 1.07% | 8% | 0 |
| 15 | `GnC339vk…` | 4.62M SOL | 1.06% | 7% | 0 |

### Delinquency alerts

- `4YGgmwyq…` · 12.74K SOL · commission 3% · lag 662827 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 252634 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 2209188 slots
- `mrgn4atx…` · 2.21K SOL · commission 0% · lag 2410493 slots
- `Hgozywot…` · 790.08 SOL · commission 100% · lag 2515027 slots
- `2ooJ5UKS…` · 342.35 SOL · commission 0% · lag 590 slots
- `ARKk6Rgi…` · 63.93 SOL · commission 10% · lag 985744 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 2245523 slots
- `R1parD2C…` · 2.87 SOL · commission 5% · lag 66959028 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 132381 slots
- `CZMekcZw…` · 1.00 SOL · commission 100% · lag 451007898 slots
- `CQYPRQ4v…` · 1.00 SOL · commission 100% · lag 13453 slots

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
| **In-protocol fees 24h** | **$952.32K** (7,877.4 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-25 |
| **Solana REV** | **9,612.3 SOL** / **$1.16M** | MEASURED UTC calendar day 2026-09-25: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-25 · UTC day 2026-09-25 · SOL-USD date 2026-09-25 |
| Jito tip-floor run-rate (NOT REV) | $57.07K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 57066 USD; at p95 floor → 18011568 USD. |
| Protocol fees 24h | $17.82M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $122.74 | coingecko.simple_price |
| 24h change | +1.70% | coingecko.simple_price |
| Market cap | $72.24B | coingecko.simple_price |
| 24h volume | $3.52B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.73B |
| TVL 1d / 7d / 30d | +1.46% / +9.01% / +11.73% |
| DEX volume 24h | $2.16B · 1d -17.52% · vs-7d-ago -25.07% |
| 7d DEX volume | $19.19B · +1.91% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $17.82M |
| Fees 1d / 7d | +18.18% / +25.18% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $513.61M | +20.57% |
| BisonFi | $251.33M | -23.33% |
| pump.fun | $210.79M | +76.94% |
| Orca DEX | $203.45M | -47.28% |
| Raydium AMM | $176.72M | -40.46% |
| fomo Wallet | $171.04M | +17.79% |
| Meteora DLMM | $162.30M | -20.66% |
| Axiom | $150.83M | +70.34% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $2.02B | +2.75% | +17.27% |
| Kamino Lend | Lending | $1.49B | +1.57% | +8.64% |
| Raydium AMM | Dexs | $1.39B | +3.06% | +12.97% |
| Jito Liquid Staking | Liquid Staking | $1.29B | +2.78% | +15.00% |
| Binance Staked SOL | Liquid Staking | $1.27B | +2.71% | +13.32% |
| Jupiter Lend | Lending | $1.20B | +2.09% | +7.10% |
| Jupiter Perpetual Exchange | Derivatives | $838.51M | +1.84% | +7.88% |
| Jupiter Staked SOL | Liquid Staking | $641.76M | +3.17% | +15.02% |
| Marinade Native | Staking Pool | $478.00M | +3.08% | +15.87% |
| PumpSwap | Dexs | $405.16M | +1.55% | +14.57% |

## Stablecoins

Solana circulating pegged-USD: **$16.42B**
(1d -0.04% · 7d +6.37%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.28B | -2.54% |
| USDT · Tether | $2.67B | -0.00% |
| USDGO · USDGO | $1.41B | 0.00% |
| USD1 · World Liberty Financial USD | $1.39B | +0.00% |
| BUIDL · BlackRock USD | $987.88M | 0.00% |
| PYUSD · PayPal USD | $760.53M | -2.27% |
| USDG · Global Dollar | $674.33M | +1.04% |
| USDe · Ethena USDe | $466.61M | -3.43% |

## Tokenized equities (xStocks)


Listed 800 · Solana deployments 800 · priced 0 · priced-subset mcap — (lower bound, not a census).
24h volume $48.00M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 0 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$546.81M** across 15 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $296.59M
- **Huma** (RWA) — $209.72M
- **Plume Vaults** (RWA) — $25.46M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $3.06M
- **Oro Finance** (RWA) — $2.47M
- **International Stable Currency** (RWA) — $2.42M
- **Byzanlink RWA Markets** (RWA) — $891.61K

## Daily active addresses

768,421 (Allium, as of 2026-09-26). Provider range 397,575–839,312. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Solana Foundation Appoints Rachel Conlan as Chief Strategy Officer and Jamal Raees as General Manager of Payments](https://solana.com/news/solana-foundation-appoints-2026) — solana.com/news · Thu, 24 Sep 2026 13:20:00 GMT
- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — solana.com/news · Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — solana.com/news · Sat, 19 Sep 2026 11:28:00 GMT `mainnet`
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — solana.com/news · Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — solana.com/news · Wed, 16 Sep 2026 00:56:00 GMT
- [Solana Summer School 2026: From first program to demo day](https://solana.com/news/solana-summer-school-2026) — solana.com/news · Mon, 14 Sep 2026 12:00:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — solana.com/news · Mon, 14 Sep 2026 11:00:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-27 (2026-09-27 06:17:15 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=live, 200ms=pending. Observed mean slot ~268 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~268 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **X / Twitter RSS** — Public X/Nitter-style RSS yielded no usable items this run (403/gated skipped). xcancel.solana 451, xcancel.solana_status 451, xcancel.anza_xyz 451, xcancel.solana_devs 451, nitter.solana 403, nitter.solana_status 403
- **Median tx fee** — no getBlock samples
- **xStocks market cap** — Listed Solana-deployed xStocks but quote and/or circulating missing. Mcap omitted.
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.
- **xStocks** — price, circulating-supply, and/or currentMultiplier missing — market cap omitted (never assumed multiplier=1.0)

## Sources this run

- `rpc.getHealth` [ok] 200 451ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 185ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 196ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 186ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 184ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6063ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 390ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 222ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 234ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 192ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 111ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 947ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 151ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 366ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 159ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 165ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 197ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 677ms https://solana.com/data
- `solana.com.databricks` [ok] 200 457ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 553ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 288ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 202ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 640ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 342ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 670ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 221ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 217ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 218ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [FAIL] 403 206ms https://nitter.perennialte.ch/solana/rss — HTTP 403 Forbidden
- `rss.nitter.solana_status` [FAIL] 403 105ms https://nitter.perennialte.ch/solana_status/rss — HTTP 403 Forbidden
- `rss.nitter.anza_xyz` [FAIL] 403 104ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 403 Forbidden
- `rss.nitter.solana_devs` [FAIL] 403 103ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 403 Forbidden
- `rss.rsshub.solana` [FAIL] 404 506ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 141ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 221ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 185ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 332ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 245ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 262ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 207ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 285ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 362ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 251ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 248ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 257ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 249ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 234ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 208ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 184ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 230ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 235ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 239ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 237ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 244ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 258ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 258ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 231ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 256ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 236ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 280ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 228ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 219ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 241ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 279ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1905ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1753ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1906ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1992ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1428ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1830ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1588ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1689ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.QUBTx` [FAIL]  12075ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WRLDx` [FAIL]  12077ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.XRXx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.FLNCx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METCx` [FAIL]  12077ms https://api.backed.fi/api/v2/public/assets/METCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WGSx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.INDIx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PCTx` [FAIL]  12086ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.METCx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.PCTx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.METCx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 576ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.FLNCx` [ok] 200 1236ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 1672ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 859ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.WYFIx` [FAIL]  12069ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BETRx` [FAIL]  12081ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AIx` [FAIL]  12080ms https://api.backed.fi/api/v2/public/assets/AIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MIDDx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WYFIx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.ALMx` [FAIL]  12081ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.RITMx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BETRx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.MIDDx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.ALMx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object
- `xstocks.circ.RITMx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 509ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.BETRx` [ok] 200 556ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.ALMx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana
- `xstocks.mult.MIDDx` [ok] 200 682ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana
- `xstocks.price.RNGx` [FAIL]  12080ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.RITMx` [ok] 200 800ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana
- `xstocks.price.SHCx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.RNGx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object
- `xstocks.circ.SHCx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object
- `xstocks.mult.RNGx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana
- `xstocks.mult.SHCx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana
- `xstocks.price.WHx` [FAIL]  12082ms https://api.backed.fi/api/v2/public/assets/WHx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.REYNx` [FAIL]  12080ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.VSNTx` [FAIL]  12072ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WHx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object
- `xstocks.price.CARx` [FAIL]  12080ms https://api.backed.fi/api/v2/public/assets/CARx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.OZKx` [FAIL]  12077ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.REYNx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object
- `xstocks.mult.WHx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana
- `xstocks.circ.CARx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object
- `xstocks.price.IRDMx` [FAIL]  12069ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.OZKx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object
- `xstocks.circ.IRDMx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object
- `xstocks.circ.VSNTx` [ok] 200 727ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object
- `xstocks.mult.CARx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana
- `xstocks.price.GXOx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.OZKx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana
- `xstocks.mult.IRDMx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana
- `xstocks.mult.REYNx` [ok] 200 703ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana
- `xstocks.price.FBINx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.VSNTx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana
- `xstocks.circ.FBINx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object
- `xstocks.mult.FBINx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana
- `xstocks.circ.GXOx` [ok] 200 682ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object
- `xstocks.mult.GXOx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana
- `xstocks.price.AMTMx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AMTMx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object
- `xstocks.price.MTNx` [FAIL]  12068ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.AMTMx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana
- `xstocks.circ.MTNx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object
- `xstocks.price.PSNx` [FAIL]  12069ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PEGAx` [FAIL]  12076ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SAICx` [FAIL]  12077ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.EXLSx` [FAIL]  12080ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.PSNx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object
- `xstocks.mult.MTNx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana
- `xstocks.circ.PEGAx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object
- `xstocks.circ.SAICx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object
- `xstocks.circ.EXLSx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object
- `xstocks.mult.SAICx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana
- `xstocks.mult.PEGAx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana
- `xstocks.price.EPAMx` [FAIL]  12076ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.PSNx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana
- `xstocks.mult.EXLSx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana
- `xstocks.circ.EPAMx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object
- `xstocks.mult.EPAMx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana
- `xstocks.price.CRUSx` [FAIL]  12080ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CRUSx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object
- `xstocks.mult.CRUSx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana
- `xstocks.price.Mx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/Mx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.Mx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object
- `xstocks.price.ELFx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.Mx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana
- `xstocks.circ.ELFx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object
- `xstocks.price.SNDRx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.VNOx` [FAIL]  12077ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.EXPx` [FAIL]  12080ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.VIRTx` [FAIL]  12075ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SNDRx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object
- `xstocks.mult.ELFx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana
- `xstocks.circ.VNOx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object
- `xstocks.circ.VIRTx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object
- `xstocks.mult.VNOx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana
- `xstocks.price.MKTXx` [FAIL]  12077ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.EXPx` [ok] 200 499ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object
- `xstocks.mult.SNDRx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana
- `xstocks.mult.EXPx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana
- `xstocks.mult.VIRTx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana
- `xstocks.circ.MKTXx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object
- `xstocks.price.HXLx` [FAIL]  12081ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MKTXx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana
- `xstocks.circ.HXLx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object
- `xstocks.mult.HXLx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana
- `xstocks.price.CPBx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CPBx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object
- `xstocks.price.VFCx` [FAIL]  12076ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CPBx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana
- `xstocks.price.NXSTx` [FAIL]  12077ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.VFCx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object
- `xstocks.price.ADTx` [FAIL]  12077ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.NXSTx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object
- `xstocks.mult.VFCx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana
- `xstocks.price.BCx` [FAIL]  12080ms https://api.backed.fi/api/v2/public/assets/BCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ACIx` [FAIL]  12085ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ADTx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object
- `xstocks.circ.BCx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object
- `xstocks.mult.NXSTx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana
- `xstocks.mult.ADTx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana
- `xstocks.circ.ACIx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object
- `xstocks.price.KRMNx` [FAIL]  12076ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.KRMNx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object
- `xstocks.price.GTESx` [FAIL]  12081ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.BCx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana
- `xstocks.circ.GTESx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object
- `xstocks.mult.KRMNx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana
- `xstocks.mult.ACIx` [ok] 200 946ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana
- `xstocks.mult.GTESx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana
- `xstocks.price.HRBx` [FAIL]  12073ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HRBx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object
- `xstocks.price.AXSx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.HRBx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana
- `xstocks.circ.AXSx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object
- `xstocks.price.DLBx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.RYNx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.AXSx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana
- `xstocks.circ.RYNx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object
- `xstocks.circ.DLBx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object
- `xstocks.price.POOLx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.RYNx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana
- `xstocks.price.TFXx` [FAIL]  12076ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.POOLx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object
- `xstocks.mult.DLBx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana
- `xstocks.price.LWx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/LWx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.TFXx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object
- `xstocks.mult.POOLx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana
- `xstocks.price.AAONx` [FAIL]  12080ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.LWx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object
- `xstocks.circ.AAONx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.mult.TFXx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana
- `xstocks.mult.LWx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana
- `xstocks.mult.AAONx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.price.SONx` [FAIL]  12077ms https://api.backed.fi/api/v2/public/assets/SONx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.INGMx` [FAIL]  12080ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SONx` [ok] 200 498ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object
- `xstocks.circ.INGMx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object
- `xstocks.price.TTDx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SONx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana
- `xstocks.mult.INGMx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana
- `xstocks.circ.TTDx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object
- `xstocks.price.HRx` [FAIL]  12077ms https://api.backed.fi/api/v2/public/assets/HRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.RLIx` [FAIL]  12069ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.RLIx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object
- `xstocks.mult.TTDx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana
- `xstocks.price.CLFx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.STWDx` [FAIL]  12075ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CLFx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object
- `xstocks.price.MSMx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HRx` [ok] 200 959ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object
- `xstocks.mult.RLIx` [ok] 200 577ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana
- `xstocks.circ.STWDx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object
- `xstocks.circ.MSMx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object
- `xstocks.mult.HRx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana
- `xstocks.mult.STWDx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana
- `xstocks.mult.CLFx` [ok] 200 611ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana
- `xstocks.mult.MSMx` [ok] 200 959ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana
- `xstocks.price.CZRx` [FAIL]  12077ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.OMFx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.OMFx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object
- `xstocks.price.CROXx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.OMFx` [ok] 200 587ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana
- `xstocks.price.CHEx` [FAIL]  12076ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CZRx` [ok] 200 1412ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object
- `xstocks.price.Gx` [FAIL]  12070ms https://api.backed.fi/api/v2/public/assets/Gx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ALGMx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CHEx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object
- `xstocks.price.MTGx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.Gx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object
- `xstocks.mult.CHEx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana
- `xstocks.circ.MTGx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object
- `xstocks.price.BEPCx` [FAIL]  12077ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MTGx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana
- `xstocks.mult.CZRx` [ok] 200 1259ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana
- `xstocks.mult.Gx` [ok] 200 755ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana
- `xstocks.circ.ALGMx` [ok] 200 1701ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object
- `xstocks.circ.CROXx` [ok] 200 2578ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object
- `xstocks.mult.CROXx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana
- `xstocks.circ.BEPCx` [ok] 200 1269ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object
- `xstocks.mult.BEPCx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana
- `xstocks.mult.ALGMx` [ok] 200 2047ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana
- `xstocks.price.MTDRx` [FAIL]  12080ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.INGRx` [FAIL]  12080ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.INGRx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object
- `xstocks.price.LYFTx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BYDx` [FAIL]  12078ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MTDRx` [ok] 200 1738ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object
- `xstocks.price.STAGx` [FAIL]  12077ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.LYFTx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object
- `xstocks.mult.INGRx` [ok] 200 562ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana
- `xstocks.circ.BYDx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object
- `xstocks.circ.STAGx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object
- `xstocks.mult.STAGx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana
- `xstocks.price.FNBx` [FAIL]  12079ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.LYFTx` [ok] 200 1047ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana
- `xstocks.price.MBGLx` [FAIL]  12081ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.FNBx` [ok] 200 973ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object
- `xstocks.price.CACCx` [FAIL]  12069ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.FNBx` [ok] 200 722ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana
- `xstocks.mult.BYDx` [ok] 200 2534ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana
- `xstocks.mult.MTDRx` [ok] 200 2808ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana
- `xstocks.circ.MBGLx` [ok] 200 1314ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object
- `xstocks.circ.CACCx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object
- `xstocks.mult.MBGLx` [ok] 200 758ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana
- `xstocks.mult.CACCx` [ok] 200 760ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1060ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 421ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.METCx` [ok] 200 186ms https://lite-api.jup.ag/tokens/v2/search?query=METCx
- `jup.tokens.search.PCTx` [ok] 200 196ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.WGSx` [ok] 200 192ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.QUBTx` [ok] 200 182ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 192ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.XRXx` [ok] 200 191ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.INDIx` [ok] 200 196ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.FLNCx` [ok] 200 184ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jito.tip_floor` [ok] 200 505ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 487ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 143ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 320ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 337ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 351ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 197ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 240ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
