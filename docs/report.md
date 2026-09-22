# Borealis — Solana ecosystem report

**Generated** 2026-09-22T10:49:15Z · 2026-09-22 03:49:15 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-22T10:49:06Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h +0.70%; DEX 24h $3.51B · 1d +26% · vs-7d-ago +39%; slot 266 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +24.82%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +32.93%. (threshold: `|7d %| >= 20`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +25.55%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +38.70%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 449,356,507 |
| Block height | 427,396,922 |
| Block time | 2026-09-22T10:49:06Z |
| Epoch | 1,040 (17.71% · slot 76,507/432,000) |
| Mean TPS (last ~3,600s) | 3,913.2 |
| Mean non-vote TPS | 1,384.4 |
| Median TPS (same window) | 3,898.0 |
| Mean slot time | 266.0 ms |
| Median slot time | 265.5 ms |
| Transaction count (cluster) | 551,291,413,365 |
| Circulating supply | 587,507,847 SOL |
| Total supply | 634,531,474 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 13 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,443,890 SOL |
| Delinquent stake | 417,859.00 SOL (0.095%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.34% / 35.66% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.83M SOL | 4.06% | 7% | 0 |
| 2 | `HEL1USMZ…` | 15.84M SOL | 3.60% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.35M SOL | 2.81% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.27M SOL | 2.56% | 5% | 0 |
| 5 | `E1r4Psq8…` | 10.21M SOL | 2.32% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.21M SOL | 2.10% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.14M SOL | 2.08% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.46M SOL | 1.70% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.09M SOL | 1.61% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.56M SOL | 1.49% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.25M SOL | 1.42% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.23M SOL | 1.42% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.35% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.62M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `TREEir31…` · 218.11K SOL · commission 5% · lag 8666 slots
- `6DTkuiey…` · 89.15K SOL · commission 100% · lag 449356507 slots
- `HDRqPft5…` · 71.15K SOL · commission 100% · lag 449356507 slots
- `t23p8aBQ…` · 14.37K SOL · commission 0% · lag 1761271 slots
- `AYY1TCe3…` · 10.71K SOL · commission 0% · lag 271567 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 557797 slots
- `mrgn4atx…` · 2.26K SOL · commission 0% · lag 759102 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 1481755 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 863636 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 594132 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 19820824 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 423167 slots

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
| **In-protocol fees 24h** | **$767.86K** (7,077.1 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-20 |
| **Solana REV** | **8,564.1 SOL** / **$929.20K** | MEASURED UTC calendar day 2026-09-20: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-20 · UTC day 2026-09-20 · SOL-USD date 2026-09-20 |
| Jito tip-floor run-rate (NOT REV) | $32.01K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 32013 USD; at p95 floor → 11159155 USD. |
| Protocol fees 24h | $18.05M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $116.62 | coingecko.simple_price |
| 24h change | +0.70% | coingecko.simple_price |
| Market cap | $68.51B | coingecko.simple_price |
| 24h volume | $6.11B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.46B |
| TVL 1d / 7d / 30d | +4.05% / +9.09% / +15.92% |
| DEX volume 24h | $3.51B · 1d +25.55% · vs-7d-ago +38.70% |
| 7d DEX volume | $20.22B · +11.06% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $18.05M |
| Fees 1d / 7d | +24.82% / +32.93% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| Raydium AMM | $515.06M | +74.48% |
| BisonFi | $446.78M | +5.31% |
| Orca DEX | $443.37M | +81.61% |
| PumpSwap | $390.12M | -19.19% |
| Meteora DLMM | $259.61M | +35.37% |
| HumidiFi | $253.12M | 0.00% |
| GoonFi | $159.53M | +68.22% |
| Manifest Trade | $159.50M | +58.34% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.87B | +4.78% | +20.42% |
| Kamino Lend | Lending | $1.42B | +0.92% | +5.34% |
| Raydium AMM | Dexs | $1.32B | +4.04% | +16.74% |
| Jito Liquid Staking | Liquid Staking | $1.22B | +1.66% | +18.06% |
| Binance Staked SOL | Liquid Staking | $1.20B | +3.59% | +15.74% |
| Jupiter Lend | Lending | $1.19B | +1.73% | +9.04% |
| Jupiter Perpetual Exchange | Derivatives | $817.16M | +2.25% | +9.98% |
| Jupiter Staked SOL | Liquid Staking | $608.82M | +1.93% | +17.19% |
| Marinade Native | Staking Pool | $449.68M | +1.75% | +17.48% |
| PumpSwap | Dexs | $378.04M | +5.10% | +14.83% |

## Stablecoins

Solana circulating pegged-USD: **$15.79B**
(1d +7.99% · 7d +4.81%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.27B | +3.08% |
| USDT · Tether | $2.14B | +0.95% |
| USDGO · USDGO | $1.40B | +1.45% |
| USD1 · World Liberty Financial USD | $1.35B | +1.52% |
| BUIDL · BlackRock USD | $993.48M | +0.03% |
| PYUSD · PayPal USD | $716.91M | -2.44% |
| USDG · Global Dollar | $621.41M | -1.53% |
| USDe · Ethena USDe | $505.62M | -0.63% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 13 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 13 · priced-subset mcap $116.43K (lower bound, not a census).
24h volume $210.10M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 13 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$553.21M** across 17 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $302.64M
- **Huma Finance V2** (RWA) — $177.61M
- **Plume Vaults** (RWA) — $28.21M
- **Ondo Global Markets** (RWA) — $27.48M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $3.01M
- **VNX** (RWA) — $2.72M
- **Oro Finance** (RWA) — $2.49M

## Daily active addresses

871,580 (Allium, as of 2026-09-21). Provider range 427,586–871,580. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — solana.com/news · Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — solana.com/news · Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — solana.com/news · Mon, 14 Sep 2026 11:00:00 GMT
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) — solana.com/news · Thu, 10 Sep 2026 20:16:00 GMT
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) — solana.com/news · Thu, 10 Sep 2026 20:16:00 GMT `mainnet`
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — solana.com/news · Tue, 08 Sep 2026 13:14:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-22 (2026-09-22 03:49:15 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 232ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 194ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 144ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 96ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 159ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5556ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 331ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 224ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 164ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 444ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 78ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 853ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1184ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 264ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 108ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 111ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 144ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 508ms https://solana.com/data
- `solana.com.databricks` [ok] 200 170ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 543ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 186ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 135ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 187ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 369ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 454ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 155ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 161ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 172ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 3702ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 14295ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 3031ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 720ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 284ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 170ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 190ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 175ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 155ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 170ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 116ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 134ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 247ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 196ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 153ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 213ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 201ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 236ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 203ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 210ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 154ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 223ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 185ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 184ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 185ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 198ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 171ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 160ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 187ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 182ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 137ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 176ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 179ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 134ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 214ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 180ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1974ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2196ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1764ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1370ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 3279ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1447ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 982ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 2546ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.WGSx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.INDIx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.FLNCx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.PCTx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.QUBTx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.XRXx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.WRLDx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.METCx` [ok] 200 638ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.INDIx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 558ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 621ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 475ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.BETRx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.mult.WGSx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.XRXx` [ok] 200 882ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.price.AAONx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.mult.QUBTx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 507ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.SCIx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.circ.AAONx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 607ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.AAONx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.price.SAILx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.mult.BETRx` [ok] 200 524ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.GSATx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.circ.WYFIx` [ok] 200 820ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.BSYx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.circ.SAILx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.MPx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.price.DRSx` [ok] 200 1009ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.circ.GSATx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.price.DVAx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.mult.WYFIx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.GSATx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.mult.SAILx` [ok] 200 583ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.price.DCIx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.price.GDDYx` [ok] 200 456ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.price.RYANx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.circ.DRSx` [ok] 200 1160ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.circ.BSYx` [ok] 200 1253ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.circ.MPx` [ok] 200 1208ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.circ.SCIx` [ok] 200 1890ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.mult.BSYx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 923ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.mult.MPx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.mult.SCIx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.mult.DCIx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.price.DYx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.price.WMSx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.circ.GDDYx` [ok] 200 1146ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.circ.WMSx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.circ.DVAx` [ok] 200 1919ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.price.AMx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.DYx` [ok] 200 571ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.mult.GDDYx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.mult.DVAx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.WMSx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.FDSx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.mult.AMx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.price.SMTCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.price.BXPx` [ok] 200 1361ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.circ.FDSx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.price.SFx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.circ.FRHCx` [ok] 200 1416ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.mult.FRHCx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.price.ALSNx` [ok] 200 1030ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.price.AXSMx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.price.EGPx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.circ.AXSMx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.circ.EGPx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 1481ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.mult.AXSMx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.circ.RYANx` [ok] 200 2920ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.circ.SMTCx` [ok] 200 1297ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.price.BPOPx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.price.TTMIx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.circ.BXPx` [ok] 200 1361ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.mult.RYANx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.mult.SMTCx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.mult.EGPx` [ok] 200 554ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.price.AEISx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.price.DPZx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.mult.BXPx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.KTOSx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.circ.AEISx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.circ.DPZx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.circ.SFx` [ok] 200 1875ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.circ.KTOSx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.price.HRLx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.mult.AEISx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.mult.SFx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.mult.DPZx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 1001ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.circ.HRLx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.price.PAGx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.price.HIIx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.mult.KTOSx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.mult.BPOPx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.circ.PAGx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.circ.TTMIx` [ok] 200 1256ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.circ.HIIx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.price.SEICx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.price.EHCx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.mult.HRLx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.GFLx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.mult.PAGx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.mult.TTMIx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.circ.SEICx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.circ.EHCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.mult.HIIx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.circ.GFLx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.price.DOCUx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.price.ARx` [ok] 200 392ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.mult.SEICx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.mult.EHCx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.price.HALOx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.circ.ALSNx` [ok] 200 2633ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.price.WTRGx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.AFGx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.price.MGMx` [ok] 200 607ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.circ.ARx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.circ.MGMx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.price.HUBSx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.mult.ARx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.mult.MGMx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.price.AMKRx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.price.GMEDx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.mult.GFLx` [ok] 200 1148ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.circ.GMEDx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.circ.DOCUx` [ok] 200 1300ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.circ.HALOx` [ok] 200 1252ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.price.JKHYx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.circ.AFGx` [ok] 200 1131ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.circ.WTRGx` [ok] 200 1283ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.mult.DOCUx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.circ.HUBSx` [ok] 200 907ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.mult.HALOx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.mult.AFGx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.price.IESCx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.price.OCx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.mult.HUBSx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.price.CRx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.price.JEFx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.circ.AMKRx` [ok] 200 1091ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.price.AMHx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.price.BMRNx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.mult.AMKRx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.circ.BMRNx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.price.FIVEx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.circ.JKHYx` [ok] 200 1243ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.mult.BMRNx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.circ.FIVEx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.mult.JKHYx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.circ.IESCx` [ok] 200 1180ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.circ.OCx` [ok] 200 1138ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.price.ITx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.mult.FIVEx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.price.MDGLx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.circ.CRx` [ok] 200 1307ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.mult.OCx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.circ.ITx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.circ.MDGLx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.price.VNOMx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.circ.JEFx` [ok] 200 1355ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.mult.CRx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.mult.MDGLx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.mult.JEFx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.mult.ITx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.price.UHALx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.price.AHRx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.mult.IESCx` [ok] 200 753ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.IVZx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.price.STRLx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.circ.AHRx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.circ.UHALx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.price.NWSAx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.price.CORTx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.circ.STRLx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.mult.UHALx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.circ.NWSAx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.mult.AHRx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.AURx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.mult.STRLx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.price.Hx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.price.ARWRx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.circ.VNOMx` [ok] 200 1419ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.circ.AMHx` [ok] 200 2690ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.circ.ARWRx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.mult.NWSAx` [ok] 200 798ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.circ.IVZx` [ok] 200 1337ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.mult.AMHx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.price.GWREx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.circ.CORTx` [ok] 200 1335ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.price.MANHx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.price.NWSx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.circ.GWREx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 1125ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.mult.CORTx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.circ.Hx` [ok] 200 1242ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.circ.MANHx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.mult.VNOMx` [ok] 200 938ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.mult.AURx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.mult.MANHx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.price.BAXx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.mult.Hx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.price.CACIx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.price.RVTYx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/RVTYx/price-data
- `xstocks.price.TXRHx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/TXRHx/price-data
- `xstocks.mult.GWREx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.circ.BAXx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.circ.CACIx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.circ.RVTYx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/RVTYx/circulating-supply?format=object
- `xstocks.circ.TXRHx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/TXRHx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.mult.RVTYx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/RVTYx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 428ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.TXRHx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/TXRHx/multiplier?network=Solana
- `xstocks.mult.IVZx` [ok] 200 1953ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 79ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 399ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.XRXx` [ok] 200 139ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 135ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.WGSx` [ok] 200 146ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.QUBTx` [ok] 200 132ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.FLNCx` [ok] 200 187ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.AIx` [ok] 200 145ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.WYFIx` [ok] 200 146ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.PCTx` [ok] 200 140ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jito.tip_floor` [ok] 200 121ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 352ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 156ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 139ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 145ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 148ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 91ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 374ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
