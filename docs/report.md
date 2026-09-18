# Borealis — Solana ecosystem report

**Generated** 2026-09-18T04:38:12Z · 2026-09-17 21:38:12 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-18T04:38:02Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h +5.45%; DEX 24h $2.55B · 1d -9% · vs-7d-ago -15%; slot 318 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -8.77%. (threshold: `|1d %| >= 8`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 447,978,606 |
| Block height | 426,019,647 |
| Block time | 2026-09-18T04:38:02Z |
| Epoch | 1,036 (98.75% · slot 426,609/432,000) |
| Mean TPS (last ~3,600s) | 4,211.9 |
| Mean non-vote TPS | 2,097.1 |
| Median TPS (same window) | 4,254.6 |
| Mean slot time | 318.4 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 549,663,996,260 |
| Circulating supply | 587,211,509 SOL |
| Total supply | 634,203,936 SOL |
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
| Activated stake | 439,595,193 SOL |
| Delinquent stake | 165,889.92 SOL (0.038%) |
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

- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 1418168 slots
- `NWY18yrP…` · 18.05K SOL · commission 10% · lag 91456 slots
- `t23p8aBQ…` · 14.66K SOL · commission 0% · lag 383370 slots
- `mrgn4atx…` · 2.26K SOL · commission 0% · lag 110327 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 103854 slots
- `Hgozywot…` · 807.47 SOL · commission 100% · lag 34981 slots
- `4GEEKSwu…` · 196.81 SOL · commission 5% · lag 2168994 slots
- `EWARp8Sy…` · 88.61 SOL · commission 5% · lag 982610 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 2279509 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 18442923 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 41443 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 1722579 slots

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
| **In-protocol fees 24h** | **$742.27K** (7,633.1 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-16 |
| **Solana REV** | **9,347.7 SOL** / **$909.00K** | MEASURED UTC calendar day 2026-09-16: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-16 · UTC day 2026-09-16 · SOL-USD date 2026-09-16 |
| Jito tip-floor run-rate (NOT REV) | $64.12K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 64118 USD; at p95 floor → 1181614 USD. |
| Protocol fees 24h | $13.89M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $104.71 | coingecko.simple_price |
| 24h change | +5.45% | coingecko.simple_price |
| Market cap | $61.48B | coingecko.simple_price |
| 24h volume | $3.77B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.91B |
| TVL 1d / 7d / 30d | +1.12% / +2.47% / +20.06% |
| DEX volume 24h | $2.55B · 1d -8.77% · vs-7d-ago -14.90% |
| 7d DEX volume | $16.06B · -13.03% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $13.89M |
| Fees 1d / 7d | -1.23% / -4.90% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| BisonFi | $440.07M | 0.00% |
| PumpSwap | $329.29M | -25.40% |
| HumidiFi | $301.79M | 0.00% |
| Raydium AMM | $289.14M | +11.44% |
| fomo Wallet | $216.17M | -19.22% |
| Meteora DLMM | $177.93M | +2.16% |
| Orca DEX | $167.15M | -34.70% |
| Tessera V | $125.24M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.63B | +3.58% | +7.33% |
| Kamino Lend | Lending | $1.34B | -0.05% | +1.06% |
| Raydium AMM | Dexs | $1.15B | +3.85% | +3.29% |
| Jupiter Lend | Lending | $1.09B | +1.03% | +2.05% |
| Binance Staked SOL | Liquid Staking | $1.06B | +3.92% | +2.91% |
| Jito Liquid Staking | Liquid Staking | $1.06B | +3.40% | +3.77% |
| Jupiter Perpetual Exchange | Derivatives | $752.66M | +2.05% | +1.88% |
| Jupiter Staked SOL | Liquid Staking | $532.85M | +4.38% | +3.69% |
| Marinade Native | Staking Pool | $390.79M | +3.31% | +2.43% |
| Sentora Curator | Risk Curators | $368.50M | +10.40% | +14.24% |

## Stablecoins

Solana circulating pegged-USD: **$15.22B**
(1d -0.39% · 7d -3.99%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.71B | +0.15% |
| USDT · Tether | $2.14B | -8.53% |
| USDGO · USDGO | $1.38B | +0.36% |
| USD1 · World Liberty Financial USD | $1.32B | -0.00% |
| BUIDL · BlackRock USD | $993.29M | +0.01% |
| PYUSD · PayPal USD | $739.27M | +2.81% |
| USDG · Global Dollar | $623.95M | -0.11% |
| USDe · Ethena USDe | $523.53M | -0.12% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $245.14K (lower bound, not a census).
24h volume $80.88M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$573.21M** across 18 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $303.06M
- **Huma Finance V2** (RWA) — $191.83M
- **Plume Vaults** (RWA) — $28.08M
- **Ondo Global Markets** (RWA) — $27.34M
- **Midas RWA** (RWA) — $5.64M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $2.79M
- **VNX** (RWA) — $2.78M

## Daily active addresses

836,063 (Allium, as of 2026-09-16). Provider range 409,337–851,851. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — solana.com/news · Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — solana.com/news · Mon, 14 Sep 2026 11:00:00 GMT
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) — solana.com/news · Thu, 10 Sep 2026 20:16:00 GMT
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) — solana.com/news · Thu, 10 Sep 2026 20:16:00 GMT `mainnet`
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — solana.com/news · Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — solana.com/news · Mon, 07 Sep 2026 07:00:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-18 (2026-09-17 21:38:12 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=activated-not-yet-effective, 200ms=pending. Observed mean slot ~318 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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

- **X / Twitter RSS** — Public X/Nitter-style RSS yielded no usable items this run (403/gated skipped). xcancel.solana 451, xcancel.solana_status 451, xcancel.anza_xyz 451, xcancel.solana_devs 451, nitter.solana 403, nitter.solana_status 403
- **Median tx fee** — no getBlock samples
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 543ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 529ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 435ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 367ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 374ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5915ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 768ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 571ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 238ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 698ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 204ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 4284ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1567ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 645ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 1223ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 552ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 437ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 704ms https://solana.com/data
- `solana.com.databricks` [ok] 200 1635ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 577ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 375ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 190ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 625ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 567ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 1021ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 423ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 419ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 406ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [FAIL] 403 604ms https://nitter.perennialte.ch/solana/rss — HTTP 403 Forbidden
- `rss.nitter.solana_status` [FAIL] 403 1400ms https://nitter.perennialte.ch/solana_status/rss — HTTP 403 Forbidden
- `rss.nitter.anza_xyz` [FAIL] 403 176ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 403 Forbidden
- `rss.nitter.solana_devs` [FAIL] 403 178ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 403 Forbidden
- `rss.rsshub.solana` [FAIL] 404 297ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 187ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 378ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 368ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 397ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 576ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 398ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 339ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 533ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 455ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 471ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 444ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 471ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 497ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 686ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 508ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 627ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 430ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 524ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 462ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 480ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 485ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 475ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 482ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 431ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 454ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 474ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 414ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 458ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 441ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 420ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 413ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 3118ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1702ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 997ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2630ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1109ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1931ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1691ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1045ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.WRLDx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.XRXx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.QUBTx` [ok] 200 656ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.METCx` [ok] 200 658ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.WGSx` [ok] 200 677ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.PCTx` [ok] 200 677ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.INDIx` [ok] 200 715ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.FLNCx` [ok] 200 718ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.circ.METCx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 1168ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.mult.METCx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 1016ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 1105ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 1515ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.PCTx` [ok] 200 1291ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 1280ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.INDIx` [ok] 200 1422ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.FLNCx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 691ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.BETRx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.SCIx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.price.SAILx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.price.BSYx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.mult.QUBTx` [ok] 200 1005ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.GSATx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.circ.WYFIx` [ok] 200 1017ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.BSYx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.price.DRSx` [ok] 200 797ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.price.MPx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.mult.WYFIx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.DRSx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.circ.SAILx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.circ.SCIx` [ok] 200 735ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.price.DVAx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.mult.DRSx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.mult.BSYx` [ok] 200 548ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 1259ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.SAILx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.circ.DVAx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.mult.SCIx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.GDDYx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.circ.MPx` [ok] 200 750ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.price.DCIx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.mult.DVAx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.price.BXPx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.circ.GDDYx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.circ.GSATx` [ok] 200 1298ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.price.RYANx` [ok] 200 521ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.mult.AIx` [ok] 200 674ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.circ.BXPx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.mult.GDDYx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.mult.GSATx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.RYANx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.circ.FRHCx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.price.DYx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.mult.BXPx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 657ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.price.AMx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.DYx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.price.FDSx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.mult.RYANx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.mult.MPx` [ok] 200 1054ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.price.WMSx` [ok] 200 627ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.circ.AMx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.circ.FDSx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.price.SMTCx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.mult.DYx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.price.ALSNx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.circ.WMSx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.mult.AMx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.mult.DCIx` [ok] 200 759ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.price.SFx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.circ.ALSNx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.price.EGPx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.price.TTMIx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.circ.SFx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.price.BPOPx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.mult.WMSx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.AXSMx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.mult.ALSNx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.mult.SFx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.circ.EGPx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.circ.BPOPx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.price.AEISx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.price.KTOSx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.price.DPZx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.mult.BPOPx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.mult.EGPx` [ok] 200 456ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.SMTCx` [ok] 200 1251ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.circ.DPZx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.price.HRLx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.price.PAGx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.circ.AXSMx` [ok] 200 1035ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.mult.DPZx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.circ.HRLx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.circ.PAGx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.circ.TTMIx` [ok] 200 1239ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.SMTCx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.mult.AXSMx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.mult.PAGx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.circ.KTOSx` [ok] 200 954ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.mult.TTMIx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.circ.AEISx` [ok] 200 1096ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.price.HIIx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.price.EHCx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.mult.KTOSx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.price.ARx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.price.SEICx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.circ.HIIx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.mult.AEISx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.price.GFLx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.circ.EHCx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.circ.ARx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.price.MGMx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.mult.HRLx` [ok] 200 906ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.DOCUx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.circ.GFLx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.EHCx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.HIIx` [ok] 200 427ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.circ.MGMx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.mult.ARx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.price.WTRGx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.HALOx` [ok] 200 403ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.price.HUBSx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.price.AFGx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.circ.WTRGx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.mult.GFLx` [ok] 200 582ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.circ.HUBSx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.price.AMKRx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.circ.SEICx` [ok] 200 1217ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.mult.MGMx` [ok] 200 743ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.mult.HUBSx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.mult.AFGx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.circ.DOCUx` [ok] 200 1168ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.price.GMEDx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.price.IESCx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.mult.SEICx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.price.JKHYx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.circ.GMEDx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.price.OCx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.circ.HALOx` [ok] 200 1136ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.mult.DOCUx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 964ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.circ.OCx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.mult.HALOx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.price.CRx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.price.BMRNx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.price.JEFx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.mult.OCx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.price.AMHx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.AMKRx` [ok] 200 1232ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.price.FIVEx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.circ.AMHx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.circ.JKHYx` [ok] 200 1003ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.circ.IESCx` [ok] 200 1139ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.mult.AMKRx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.mult.JKHYx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.mult.AMHx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.mult.IESCx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.ITx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.circ.CRx` [ok] 200 1020ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.price.VNOMx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.circ.ITx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.price.MDGLx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.price.UHALx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.circ.BMRNx` [ok] 200 1219ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.mult.CRx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.mult.ITx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.circ.UHALx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.circ.JEFx` [ok] 200 1381ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.price.AHRx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.price.IVZx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.mult.UHALx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.mult.BMRNx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.mult.JEFx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.circ.AHRx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.price.CORTx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.price.STRLx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.price.NWSAx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.mult.AHRx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.circ.VNOMx` [ok] 200 1178ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.circ.MDGLx` [ok] 200 1129ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.price.AURx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.mult.MDGLx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.circ.FIVEx` [ok] 200 2180ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.price.Hx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.mult.FIVEx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.circ.CORTx` [ok] 200 1181ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.mult.VNOMx` [ok] 200 925ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.ARWRx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.circ.NWSAx` [ok] 200 1240ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.circ.IVZx` [ok] 200 1742ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.mult.CORTx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.GWREx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.price.NWSx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.mult.IVZx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.circ.STRLx` [ok] 200 1737ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.circ.GWREx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.price.MANHx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.mult.NWSAx` [ok] 200 647ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.circ.Hx` [ok] 200 1201ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.mult.STRLx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.mult.GWREx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.circ.MANHx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.price.CACIx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.circ.ARWRx` [ok] 200 1036ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.price.BAXx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.mult.Hx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.circ.AURx` [ok] 200 1924ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.circ.CACIx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.price.RVTYx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/RVTYx/price-data
- `xstocks.circ.BAXx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.price.TXRHx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/TXRHx/price-data
- `xstocks.mult.AURx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.mult.ARWRx` [ok] 200 428ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.circ.RVTYx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/RVTYx/circulating-supply?format=object
- `xstocks.price.CNAx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/CNAx/price-data
- `xstocks.mult.BAXx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 1142ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.circ.CNAx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/CNAx/circulating-supply?format=object
- `xstocks.mult.NWSx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.mult.RVTYx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/RVTYx/multiplier?network=Solana
- `xstocks.mult.CNAx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/CNAx/multiplier?network=Solana
- `xstocks.mult.CACIx` [ok] 200 1008ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.circ.TXRHx` [ok] 200 1265ms https://api.backed.fi/api/v2/public/assets/TXRHx/circulating-supply?format=object
- `xstocks.mult.TXRHx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/TXRHx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 987ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 548ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INDIx` [ok] 200 192ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 192ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 184ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.XRXx` [ok] 200 176ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 205ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.WGSx` [ok] 200 176ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.FLNCx` [ok] 200 184ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.AIx` [ok] 200 203ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jito.tip_floor` [ok] 200 2004ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 523ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 323ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 370ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 366ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 376ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 396ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 719ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
