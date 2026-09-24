# Borealis — Solana ecosystem report

**Generated** 2026-09-24T00:53:52Z · 2026-09-23 17:53:52 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-24T00:53:43Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h -3.33%; DEX 24h $3.09B · 1d -3% · vs-7d-ago +10%; slot 266 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -3.33%, DeFiLlama TVL 1d -1.16%, DEX 1d -3.38%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 449,871,624 |
| Block height | 427,911,766 |
| Block time | 2026-09-24T00:53:43Z |
| Epoch | 1,041 (36.95% · slot 159,625/432,000) |
| Mean TPS (last ~3,600s) | 4,654.0 |
| Mean non-vote TPS | 2,127.4 |
| Median TPS (same window) | 4,679.2 |
| Mean slot time | 266.0 ms |
| Median slot time | 265.5 ms |
| Transaction count (cluster) | 551,910,568,200 |
| Circulating supply | 587,577,654 SOL |
| Total supply | 634,608,765 SOL |
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
| Activated stake | 439,727,513 SOL |
| Delinquent stake | 236,623.47 SOL (0.054%) |
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

- `6DTkuiey…` · 89.15K SOL · commission 100% · lag 449871624 slots
- `HDRqPft5…` · 71.15K SOL · commission 100% · lag 449871624 slots
- `3PZSgErg…` · 36.93K SOL · commission 0% · lag 157694 slots
- `t23p8aBQ…` · 14.37K SOL · commission 0% · lag 2276388 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 140628 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 1072914 slots
- `mrgn4atx…` · 2.21K SOL · commission 0% · lag 1274219 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 1996872 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 1378753 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 1109249 slots
- `R1parD2C…` · 2.87 SOL · commission 5% · lag 65822754 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 292115 slots

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
| Jito tip-floor run-rate (NOT REV) | $115.07K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 115068 USD; at p95 floor → 1783801 USD. |
| Protocol fees 24h | $17.12M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $114.93 | coingecko.simple_price |
| 24h change | -3.33% | coingecko.simple_price |
| Market cap | $67.55B | coingecko.simple_price |
| 24h volume | $5.16B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.39B |
| TVL 1d / 7d / 30d | -1.16% / +11.52% / +14.53% |
| DEX volume 24h | $3.09B · 1d -3.38% · vs-7d-ago +10.27% |
| 7d DEX volume | $19.43B · +8.86% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $17.12M |
| Fees 1d / 7d | -4.20% / +14.96% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $634.15M | 0.00% |
| Raydium AMM | $395.67M | -16.86% |
| BisonFi | $368.17M | 0.00% |
| Orca DEX | $366.04M | -0.42% |
| Meteora DLMM | $266.83M | 0.00% |
| fomo Wallet | $133.69M | -9.56% |
| Scorch | $129.41M | 0.00% |
| pump.fun | $121.03M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.85B | -1.66% | +18.43% |
| Kamino Lend | Lending | $1.40B | -1.80% | +5.60% |
| Raydium AMM | Dexs | $1.30B | -2.41% | +17.56% |
| Jito Liquid Staking | Liquid Staking | $1.19B | -2.94% | +17.22% |
| Binance Staked SOL | Liquid Staking | $1.18B | -2.76% | +15.49% |
| Jupiter Lend | Lending | $1.17B | -0.44% | +10.39% |
| Jupiter Perpetual Exchange | Derivatives | $803.28M | -2.11% | +9.24% |
| Jupiter Staked SOL | Liquid Staking | $594.97M | -2.66% | +16.92% |
| Marinade Native | Staking Pool | $441.26M | -2.25% | +18.17% |
| PumpSwap | Dexs | $372.54M | -2.44% | +18.05% |

## Stablecoins

Solana circulating pegged-USD: **$16.67B**
(1d -1.70% · 7d +5.80%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $8.08B | -2.53% |
| USDT · Tether | $2.14B | +0.00% |
| USDGO · USDGO | $1.42B | +1.00% |
| USD1 · World Liberty Financial USD | $1.38B | +2.16% |
| BUIDL · BlackRock USD | $987.68M | -0.58% |
| PYUSD · PayPal USD | $744.95M | +1.85% |
| USDG · Global Dollar | $631.34M | +1.72% |
| USDe · Ethena USDe | $497.40M | -0.94% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $115.61K (lower bound, not a census).
24h volume $147.21M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$543.54M** across 16 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $301.08M
- **Huma** (RWA) — $197.05M
- **Plume Vaults** (RWA) — $28.21M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $2.98M
- **VNX** (RWA) — $2.70M
- **Oro Finance** (RWA) — $2.48M
- **International Stable Currency** (RWA) — $2.45M

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

_As of 2026-09-24 (2026-09-23 17:53:52 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 196ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 133ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 54ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 73ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 138ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5369ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 306ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 165ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 100ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 620ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 54ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 736ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 986ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 178ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 654ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 86ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 108ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 276ms https://solana.com/data
- `solana.com.databricks` [ok] 200 305ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 401ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 202ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 42ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 60ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 350ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 333ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 93ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 83ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 83ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 2901ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1233ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 743ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 78ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 216ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 120ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 58ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 55ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 99ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 172ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 83ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 100ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 155ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 210ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 145ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 163ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 230ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 235ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 175ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 174ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 58ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 199ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 150ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 213ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 127ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 156ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 150ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 259ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 180ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 203ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 152ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 319ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 120ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 164ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 95ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 150ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 7962ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 3618ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2235ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 3856ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 4505ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2067ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 11550ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 4245ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.INDIx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WGSx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.WRLDx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.QUBTx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.PCTx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.XRXx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.FLNCx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.METCx` [ok] 200 662ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.WRLDx` [ok] 200 739ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.PCTx` [ok] 200 911ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 1822ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 1692ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 1835ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 1197ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.XRXx` [ok] 200 2271ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.METCx` [ok] 200 1956ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 1453ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 871ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 1034ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.mult.INDIx` [ok] 200 1185ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.price.MIDDx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data
- `xstocks.circ.WGSx` [ok] 200 3305ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 1044ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 1086ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.WYFIx` [ok] 200 1116ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.ALMx` [ok] 200 565ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data
- `xstocks.price.RNGx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data
- `xstocks.circ.BETRx` [ok] 200 916ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.RITMx` [ok] 200 736ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data
- `xstocks.mult.WGSx` [ok] 200 939ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.ALMx` [ok] 200 872ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 1504ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.BETRx` [ok] 200 787ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 1195ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.WHx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/WHx/price-data
- `xstocks.price.SHCx` [ok] 200 1010ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data
- `xstocks.price.REYNx` [ok] 200 804ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data
- `xstocks.circ.MIDDx` [ok] 200 2718ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object
- `xstocks.circ.RNGx` [ok] 200 2145ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 1298ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.circ.WHx` [ok] 200 1022ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object
- `xstocks.circ.RITMx` [ok] 200 2040ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object
- `xstocks.mult.RNGx` [ok] 200 880ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana
- `xstocks.mult.ALMx` [ok] 200 2403ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana
- `xstocks.price.VSNTx` [ok] 200 955ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data
- `xstocks.mult.WHx` [ok] 200 1255ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana
- `xstocks.mult.RITMx` [ok] 200 1190ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana
- `xstocks.price.OZKx` [ok] 200 745ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data
- `xstocks.mult.MIDDx` [ok] 200 1799ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana
- `xstocks.price.GXOx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data
- `xstocks.circ.SHCx` [ok] 200 2759ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object
- `xstocks.price.FBINx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data
- `xstocks.price.IRDMx` [ok] 200 672ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data
- `xstocks.price.CARx` [ok] 200 1412ms https://api.backed.fi/api/v2/public/assets/CARx/price-data
- `xstocks.circ.REYNx` [ok] 200 2641ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object
- `xstocks.circ.OZKx` [ok] 200 895ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object
- `xstocks.circ.VSNTx` [ok] 200 2096ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object
- `xstocks.circ.FBINx` [ok] 200 890ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object
- `xstocks.mult.SHCx` [ok] 200 1604ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana
- `xstocks.mult.REYNx` [ok] 200 1811ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana
- `xstocks.circ.GXOx` [ok] 200 2340ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object
- `xstocks.mult.FBINx` [ok] 200 1601ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana
- `xstocks.price.AMTMx` [ok] 200 1077ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data
- `xstocks.circ.IRDMx` [ok] 200 2802ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object
- `xstocks.mult.OZKx` [ok] 200 2645ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana
- `xstocks.price.PSNx` [ok] 200 924ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data
- `xstocks.price.PEGAx` [ok] 200 672ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data
- `xstocks.price.MTNx` [ok] 200 1800ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data
- `xstocks.circ.CARx` [ok] 200 4452ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object
- `xstocks.mult.GXOx` [ok] 200 2592ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana
- `xstocks.circ.MTNx` [ok] 200 1148ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object
- `xstocks.mult.VSNTx` [ok] 200 4003ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana
- `xstocks.circ.AMTMx` [ok] 200 2377ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object
- `xstocks.mult.IRDMx` [ok] 200 2379ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana
- `xstocks.circ.PSNx` [ok] 200 1960ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object
- `xstocks.price.SAICx` [ok] 200 911ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data
- `xstocks.price.EXLSx` [ok] 200 857ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data
- `xstocks.circ.PEGAx` [ok] 200 2129ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object
- `xstocks.price.EPAMx` [ok] 200 969ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data
- `xstocks.mult.MTNx` [ok] 200 1313ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana
- `xstocks.mult.AMTMx` [ok] 200 1768ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana
- `xstocks.mult.PSNx` [ok] 200 1433ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana
- `xstocks.mult.CARx` [ok] 200 2319ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana
- `xstocks.circ.SAICx` [ok] 200 1244ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object
- `xstocks.price.CRUSx` [ok] 200 1223ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data
- `xstocks.mult.PEGAx` [ok] 200 1760ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana
- `xstocks.price.Mx` [ok] 200 845ms https://api.backed.fi/api/v2/public/assets/Mx/price-data
- `xstocks.circ.EXLSx` [ok] 200 1977ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object
- `xstocks.price.ELFx` [ok] 200 1119ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data
- `xstocks.circ.EPAMx` [ok] 200 2187ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object
- `xstocks.price.VNOx` [ok] 200 802ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data
- `xstocks.price.SNDRx` [ok] 200 1728ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data
- `xstocks.mult.SAICx` [ok] 200 2305ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana
- `xstocks.circ.CRUSx` [ok] 200 2054ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object
- `xstocks.circ.SNDRx` [ok] 200 1299ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object
- `xstocks.mult.EPAMx` [ok] 200 1929ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana
- `xstocks.mult.EXLSx` [ok] 200 2704ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana
- `xstocks.price.EXPx` [ok] 200 1292ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data
- `xstocks.circ.VNOx` [ok] 200 2219ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object
- `xstocks.circ.ELFx` [ok] 200 2681ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object
- `xstocks.circ.Mx` [ok] 200 3289ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object
- `xstocks.mult.CRUSx` [ok] 200 1935ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana
- `xstocks.price.MKTXx` [ok] 200 1254ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data
- `xstocks.price.VIRTx` [ok] 200 1415ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data
- `xstocks.mult.SNDRx` [ok] 200 1800ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana
- `xstocks.mult.ELFx` [ok] 200 1746ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana
- `xstocks.mult.VNOx` [ok] 200 1768ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana
- `xstocks.price.HXLx` [ok] 200 1312ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data
- `xstocks.price.CPBx` [ok] 200 1048ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data
- `xstocks.mult.Mx` [ok] 200 1978ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana
- `xstocks.circ.EXPx` [ok] 200 2353ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object
- `xstocks.price.VFCx` [ok] 200 951ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data
- `xstocks.price.ADTx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data
- `xstocks.price.NXSTx` [ok] 200 1475ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data
- `xstocks.circ.MKTXx` [ok] 200 2281ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object
- `xstocks.circ.VIRTx` [ok] 200 2741ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object
- `xstocks.circ.HXLx` [ok] 200 1989ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object
- `xstocks.mult.EXPx` [ok] 200 1907ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana
- `xstocks.circ.ADTx` [ok] 200 1721ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object
- `xstocks.circ.CPBx` [ok] 200 2643ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object
- `xstocks.price.BCx` [ok] 200 932ms https://api.backed.fi/api/v2/public/assets/BCx/price-data
- `xstocks.circ.VFCx` [ok] 200 2692ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object
- `xstocks.mult.MKTXx` [ok] 200 2353ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana
- `xstocks.circ.BCx` [ok] 200 1096ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object
- `xstocks.mult.HXLx` [ok] 200 2206ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana
- `xstocks.price.ACIx` [ok] 200 749ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data
- `xstocks.mult.VIRTx` [ok] 200 2658ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana
- `xstocks.circ.NXSTx` [ok] 200 3715ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object
- `xstocks.price.GTESx` [ok] 200 722ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data
- `xstocks.mult.ADTx` [ok] 200 2699ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana
- `xstocks.circ.ACIx` [ok] 200 924ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object
- `xstocks.mult.VFCx` [ok] 200 2042ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana
- `xstocks.price.KRMNx` [ok] 200 1320ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data
- `xstocks.mult.CPBx` [ok] 200 2976ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana
- `xstocks.price.AXSx` [ok] 200 779ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data
- `xstocks.mult.BCx` [ok] 200 2433ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana
- `xstocks.price.HRBx` [ok] 200 1690ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data
- `xstocks.mult.ACIx` [ok] 200 1813ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana
- `xstocks.price.DLBx` [ok] 200 1463ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data
- `xstocks.circ.AXSx` [ok] 200 1178ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object
- `xstocks.mult.NXSTx` [ok] 200 2708ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana
- `xstocks.price.RYNx` [ok] 200 1013ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data
- `xstocks.circ.GTESx` [ok] 200 2567ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object
- `xstocks.price.POOLx` [ok] 200 1141ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data
- `xstocks.price.TFXx` [ok] 200 865ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data
- `xstocks.circ.KRMNx` [ok] 200 3065ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object
- `xstocks.circ.HRBx` [ok] 200 2263ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object
- `xstocks.circ.DLBx` [ok] 200 2353ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object
- `xstocks.mult.GTESx` [ok] 200 2082ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana
- `xstocks.mult.AXSx` [ok] 200 2613ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana
- `xstocks.mult.KRMNx` [ok] 200 1747ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana
- `xstocks.circ.RYNx` [ok] 200 2769ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object
- `xstocks.circ.POOLx` [ok] 200 2177ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object
- `xstocks.price.LWx` [ok] 200 885ms https://api.backed.fi/api/v2/public/assets/LWx/price-data
- `xstocks.price.AAONx` [ok] 200 923ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.price.SONx` [ok] 200 725ms https://api.backed.fi/api/v2/public/assets/SONx/price-data
- `xstocks.mult.HRBx` [ok] 200 2125ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana
- `xstocks.price.INGMx` [ok] 200 939ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data
- `xstocks.circ.TFXx` [ok] 200 3936ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object
- `xstocks.mult.DLBx` [ok] 200 2926ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana
- `xstocks.circ.LWx` [ok] 200 1847ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object
- `xstocks.mult.POOLx` [ok] 200 2283ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana
- `xstocks.circ.AAONx` [ok] 200 2020ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.mult.RYNx` [ok] 200 2773ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana
- `xstocks.circ.SONx` [ok] 200 2366ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object
- `xstocks.price.HRx` [ok] 200 950ms https://api.backed.fi/api/v2/public/assets/HRx/price-data
- `xstocks.mult.AAONx` [ok] 200 1520ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.mult.LWx` [ok] 200 1916ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana
- `xstocks.mult.TFXx` [ok] 200 2115ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana
- `xstocks.circ.INGMx` [ok] 200 2917ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object
- `xstocks.mult.SONx` [ok] 200 2250ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana
- `xstocks.mult.INGMx` [ok] 200 1952ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana
- `xstocks.circ.HRx` [ok] 200 3799ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object
- `xstocks.mult.HRx` [ok] 200 981ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana
- `xstocks.price.CROXx` [ok] 200 846ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data
- `xstocks.circ.CROXx` [ok] 200 2104ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object
- `xstocks.mult.CROXx` [ok] 200 904ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana
- `xstocks.price.CHEx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data
- `xstocks.price.TTDx` [ok] 200 11422ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data
- `xstocks.circ.CHEx` [ok] 200 1922ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object
- `xstocks.price.RLIx` [ok] 200 11579ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data
- `xstocks.price.STWDx` [ok] 200 10826ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data
- `xstocks.price.CLFx` [ok] 200 10875ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data
- `xstocks.mult.CHEx` [ok] 200 930ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana
- `xstocks.price.Gx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/Gx/price-data
- `xstocks.price.MSMx` [ok] 200 11414ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data
- `xstocks.price.CZRx` [ok] 200 10384ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data
- `xstocks.circ.RLIx` [ok] 200 1563ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object
- `xstocks.circ.TTDx` [ok] 200 3023ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object
- `xstocks.circ.CLFx` [ok] 200 1841ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object
- `xstocks.mult.RLIx` [ok] 200 889ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana
- `xstocks.circ.STWDx` [ok] 200 2125ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object
- `xstocks.price.ALGMx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data
- `xstocks.circ.MSMx` [ok] 200 1675ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object
- `xstocks.circ.Gx` [ok] 200 2048ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object
- `xstocks.mult.TTDx` [ok] 200 1055ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana
- `xstocks.mult.CLFx` [ok] 200 995ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana
- `xstocks.price.OMFx` [ok] 200 11027ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data
- `xstocks.price.MTGx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data
- `xstocks.price.BEPCx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data
- `xstocks.mult.STWDx` [ok] 200 1020ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana
- `xstocks.circ.CZRx` [ok] 200 2404ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object
- `xstocks.mult.MSMx` [ok] 200 1087ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana
- `xstocks.price.MTDRx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data
- `xstocks.mult.Gx` [ok] 200 1227ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana
- `xstocks.circ.ALGMx` [ok] 200 1817ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object
- `xstocks.price.LYFTx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data
- `xstocks.mult.CZRx` [ok] 200 998ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana
- `xstocks.price.INGRx` [ok] 200 1087ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data
- `xstocks.circ.MTGx` [ok] 200 1499ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object
- `xstocks.price.BYDx` [ok] 200 719ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data
- `xstocks.circ.BEPCx` [ok] 200 1867ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object
- `xstocks.circ.OMFx` [ok] 200 2214ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object
- `xstocks.mult.ALGMx` [ok] 200 1165ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana
- `xstocks.circ.MTDRx` [ok] 200 1999ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object
- `xstocks.mult.OMFx` [ok] 200 1141ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana
- `xstocks.mult.BEPCx` [ok] 200 1306ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana
- `xstocks.circ.INGRx` [ok] 200 1828ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object
- `xstocks.price.STAGx` [ok] 200 1190ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data
- `xstocks.mult.MTGx` [ok] 200 1908ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana
- `xstocks.mult.MTDRx` [ok] 200 1356ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana
- `xstocks.price.FNBx` [ok] 200 889ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data
- `xstocks.circ.BYDx` [ok] 200 2199ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object
- `xstocks.price.MBGLx` [ok] 200 907ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data
- `xstocks.price.CACCx` [ok] 200 784ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data
- `xstocks.mult.INGRx` [ok] 200 1253ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana
- `xstocks.mult.BYDx` [ok] 200 1032ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana
- `xstocks.circ.LYFTx` [ok] 200 4674ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object
- `xstocks.circ.MBGLx` [ok] 200 1651ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object
- `xstocks.circ.STAGx` [ok] 200 2476ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object
- `xstocks.circ.CACCx` [ok] 200 1711ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object
- `xstocks.circ.FNBx` [ok] 200 1893ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object
- `xstocks.mult.STAGx` [ok] 200 1221ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana
- `xstocks.mult.FNBx` [ok] 200 1123ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana
- `xstocks.mult.CACCx` [ok] 200 1251ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana
- `xstocks.mult.LYFTx` [ok] 200 1633ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana
- `xstocks.mult.MBGLx` [ok] 200 1687ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 55ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 146ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.XRXx` [ok] 200 78ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 88ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.QUBTx` [ok] 200 95ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.FLNCx` [ok] 200 91ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.AIx` [ok] 200 87ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.WGSx` [ok] 200 80ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.WYFIx` [ok] 200 120ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.INDIx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jito.tip_floor` [ok] 200 68ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 269ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 86ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 57ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 57ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 54ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 57ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 1198ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
