# Borealis — Solana ecosystem report

**Generated** 2026-09-19T20:48:38Z · 2026-09-19 13:48:38 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-19T20:48:30Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -2.25%; DEX 24h $3.54B · 1d +36% · vs-7d-ago +8%; slot 267 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +18.99%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +36.44%. (threshold: `|1d %| >= 8`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 448,520,030 |
| Block height | 426,560,800 |
| Block time | 2026-09-19T20:48:30Z |
| Epoch | 1,038 (24.08% · slot 104,034/432,000) |
| Mean TPS (last ~3,600s) | 4,552.0 |
| Mean non-vote TPS | 2,025.1 |
| Median TPS (same window) | 4,498.9 |
| Mean slot time | 267.2 ms |
| Median slot time | 266.7 ms |
| Transaction count (cluster) | 550,305,916,615 |
| Circulating supply | 587,367,659 SOL |
| Total supply | 634,376,131 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 679 |
| Delinquent | 11 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 440,082,204 SOL |
| Delinquent stake | 145,167.56 SOL (0.033%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.28% / 35.66% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.85M SOL | 4.06% | 7% | 0 |
| 2 | `HEL1USMZ…` | 15.82M SOL | 3.59% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.50M SOL | 2.84% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.36M SOL | 2.58% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.79M SOL | 2.22% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.25M SOL | 2.10% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.12M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.43M SOL | 1.69% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.09M SOL | 1.61% | 5% | 0 |
| 10 | `9jxgosAf…` | 6.63M SOL | 1.51% | 100% | 0 |
| 11 | `Awes4Tr6…` | 6.56M SOL | 1.49% | 0% | 0 |
| 12 | `JD549Hsb…` | 6.21M SOL | 1.41% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.35% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.65M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.84M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 1959592 slots
- `t23p8aBQ…` · 14.48K SOL · commission 0% · lag 924794 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 645278 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 27159 slots
- `EWARp8Sy…` · 64.91 SOL · commission 5% · lag 1524034 slots
- `FLVgaCPv…` · 9.28 SOL · commission 5% · lag 20504492 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 18984347 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 412349 slots
- `HDRqPft5…` · 2.00 SOL · commission 100% · lag 448520030 slots
- `6DTkuiey…` · 2.00 SOL · commission 100% · lag 448520030 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 2264003 slots

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
| **In-protocol fees 24h** | **$814.96K** (8,101.5 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-17 |
| **Solana REV** | **9,853.4 SOL** / **$991.19K** | MEASURED UTC calendar day 2026-09-17: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-17 · UTC day 2026-09-17 · SOL-USD date 2026-09-17 |
| Jito tip-floor run-rate (NOT REV) | $81.57K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 81570 USD; at p95 floor → 734248 USD. |
| Protocol fees 24h | $17.46M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $111.13 | coingecko.simple_price |
| 24h change | -2.25% | coingecko.simple_price |
| Market cap | $65.35B | coingecko.simple_price |
| 24h volume | $3.15B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.23B |
| TVL 1d / 7d / 30d | +5.66% / +5.61% / +18.95% |
| DEX volume 24h | $3.54B · 1d +36.44% · vs-7d-ago +7.86% |
| 7d DEX volume | $17.70B · -10.70% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $17.46M |
| Fees 1d / 7d | +18.99% / -2.36% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| BisonFi | $532.67M | +40.80% |
| PumpSwap | $488.34M | +48.30% |
| HumidiFi | $334.93M | +18.92% |
| Raydium AMM | $326.32M | +16.33% |
| Orca DEX | $300.65M | +76.48% |
| Meteora DLMM | $239.38M | +34.54% |
| Tessera V | $205.65M | +22.21% |
| fomo Wallet | $156.65M | -28.10% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.77B | -1.04% | +13.51% |
| Kamino Lend | Lending | $1.38B | -1.10% | +2.03% |
| Raydium AMM | Dexs | $1.26B | +4.92% | +10.60% |
| Binance Staked SOL | Liquid Staking | $1.15B | -0.71% | +8.91% |
| Jito Liquid Staking | Liquid Staking | $1.15B | -0.85% | +10.19% |
| Jupiter Lend | Lending | $1.14B | -0.93% | +3.59% |
| Jupiter Perpetual Exchange | Derivatives | $792.79M | -1.11% | +5.40% |
| Jupiter Staked SOL | Liquid Staking | $574.12M | -1.46% | +8.89% |
| Marinade Native | Staking Pool | $424.71M | -0.92% | +9.24% |
| Sentora Curator | Risk Curators | $364.74M | +0.21% | +12.67% |

## Stablecoins

Solana circulating pegged-USD: **$15.41B**
(1d +1.03% · 7d -4.40%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.95B | +3.79% |
| USDT · Tether | $2.12B | -7.03% |
| USDGO · USDGO | $1.38B | +0.14% |
| USD1 · World Liberty Financial USD | $1.33B | +0.76% |
| BUIDL · BlackRock USD | $993.18M | -0.01% |
| PYUSD · PayPal USD | $726.17M | -1.13% |
| USDG · Global Dollar | $627.99M | +0.64% |
| USDe · Ethena USDe | $511.87M | -2.26% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $239.43K (lower bound, not a census).
24h volume $86.83M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$580.70M** across 17 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $304.05M
- **Huma Finance V2** (RWA) — $201.72M
- **Plume Vaults** (RWA) — $28.12M
- **Ondo Global Markets** (RWA) — $26.88M
- **Invesco USTB** (RWA) — $3.91M
- **Remora Markets** (RWA) — $3.05M
- **Mansory** (RWA) — $2.93M
- **VNX** (RWA) — $2.74M

## Daily active addresses

890,530 (Allium, as of 2026-09-18). Provider range 456,874–893,188. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — solana.com/news · Mon, 07 Sep 2026 07:00:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-19 (2026-09-19 13:48:38 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=live, 200ms=pending. Observed mean slot ~267 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~267 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 413ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 530ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 379ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 445ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 401ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6278ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 755ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 137ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 192ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 77ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 65ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 1009ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 76ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 131ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 76ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 83ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 133ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 360ms https://solana.com/data
- `solana.com.databricks` [ok] 200 122ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 245ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 228ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 280ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 147ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 307ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 538ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 240ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 235ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 233ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 1885ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 335ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 623ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 316ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 210ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 270ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 384ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 509ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 429ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 160ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 455ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 117ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 474ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 235ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 497ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 276ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 605ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 288ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 561ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 234ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 427ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 259ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 636ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 239ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 495ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 209ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 421ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 171ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 694ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 313ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 424ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 268ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 456ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 341ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 451ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 150ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1856ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 4900ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2675ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1676ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 6081ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2148ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2687ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 5714ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.WRLDx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.PCTx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.METCx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.INDIx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WGSx` [ok] 200 456ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.XRXx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.QUBTx` [ok] 200 526ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.FLNCx` [ok] 200 574ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.circ.PCTx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.WRLDx` [ok] 200 852ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 547ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 508ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.WGSx` [ok] 200 771ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.price.AIx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.FLNCx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.DRSx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.circ.BETRx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.price.SCIx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.mult.WRLDx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.AAONx` [ok] 200 545ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.circ.DRSx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.BETRx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.circ.AAONx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.price.GSATx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.price.SAILx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.price.MPx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.mult.AAONx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.circ.GSATx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.circ.SAILx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 1066ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.BSYx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.circ.MPx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 672ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.DVAx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.mult.GSATx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.mult.SAILx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.price.DCIx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.mult.MPx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.circ.BSYx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.price.GDDYx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.circ.DVAx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.circ.SCIx` [ok] 200 1095ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.price.BXPx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.price.FRHCx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.price.RYANx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.circ.DCIx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.mult.BSYx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.mult.DVAx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.circ.BXPx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.circ.FRHCx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.price.WMSx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.mult.DCIx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.circ.RYANx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.mult.BXPx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.DYx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.mult.FRHCx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.circ.GDDYx` [ok] 200 755ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.price.FDSx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.circ.DYx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.mult.GDDYx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.price.ALSNx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.mult.RYANx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.circ.FDSx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.price.SMTCx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.circ.ALSNx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.price.SFx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.price.AXSMx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.price.AMx` [ok] 200 882ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.SFx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.circ.SMTCx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.circ.AXSMx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 506ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.SFx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.mult.SCIx` [ok] 200 1667ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.circ.WMSx` [ok] 200 1228ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.price.EGPx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.mult.SMTCx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.mult.AMx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.price.BPOPx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.mult.AXSMx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.circ.EGPx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.price.TTMIx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.mult.WMSx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.DPZx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.price.AEISx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.price.KTOSx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.circ.BPOPx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.price.HRLx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.price.PAGx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.circ.TTMIx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.circ.AEISx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.mult.EGPx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.KTOSx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.circ.HRLx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.mult.TTMIx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.SEICx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.mult.AEISx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.circ.DPZx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.circ.PAGx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.mult.BPOPx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.circ.SEICx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.price.HIIx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.price.EHCx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.mult.KTOSx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.mult.DPZx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.mult.PAGx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.mult.HRLx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.mult.SEICx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.circ.EHCx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.price.ARx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.price.HALOx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.price.MGMx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.price.GFLx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.mult.HIIx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.price.WTRGx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.circ.ARx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.mult.EHCx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.circ.HALOx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.circ.MGMx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.circ.GFLx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.price.AFGx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.circ.WTRGx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.price.HUBSx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.price.DOCUx` [ok] 200 566ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.mult.MGMx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.mult.ARx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.circ.DOCUx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.circ.HUBSx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.mult.GFLx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.mult.HALOx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.price.AMKRx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.price.JKHYx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.DOCUx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.mult.HUBSx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.price.GMEDx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.price.IESCx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.price.OCx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.circ.AMKRx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.circ.JKHYx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.price.CRx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.circ.GMEDx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 758ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.circ.IESCx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.circ.OCx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.mult.JKHYx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.mult.AMKRx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.circ.CRx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.mult.GMEDx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.mult.AFGx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.mult.IESCx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.mult.OCx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.price.JEFx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.mult.CRx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.price.AMHx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.price.BMRNx` [ok] 200 598ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.price.MDGLx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.price.VNOMx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.price.UHALx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.circ.AMHx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.circ.BMRNx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.circ.JEFx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.price.FIVEx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.price.ITx` [ok] 200 536ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.mult.BMRNx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.circ.MDGLx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.circ.FIVEx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.mult.JEFx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.circ.VNOMx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.price.AHRx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.price.IVZx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.circ.ITx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.mult.FIVEx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.circ.AHRx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.circ.IVZx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.price.STRLx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.mult.ITx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.MDGLx` [ok] 200 548ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.mult.IVZx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.price.NWSAx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.circ.STRLx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.price.AURx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.mult.VNOMx` [ok] 200 732ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.CORTx` [ok] 200 832ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.mult.STRLx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.circ.NWSAx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.price.Hx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.price.ARWRx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.circ.UHALx` [ok] 200 1296ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.circ.CORTx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.mult.AHRx` [ok] 200 710ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.GWREx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.mult.NWSAx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.circ.ARWRx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.circ.Hx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.mult.UHALx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.price.NWSx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.mult.CORTx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.mult.AURx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.price.MANHx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.mult.Hx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.price.CACIx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.circ.NWSx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.price.RVTYx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/RVTYx/price-data
- `xstocks.circ.MANHx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.circ.CACIx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.price.TXRHx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/TXRHx/price-data
- `xstocks.circ.RVTYx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/RVTYx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.CACIx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.mult.RVTYx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/RVTYx/multiplier?network=Solana
- `xstocks.price.BAXx` [ok] 200 790ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.GWREx` [ok] 200 1250ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.circ.TXRHx` [ok] 200 556ms https://api.backed.fi/api/v2/public/assets/TXRHx/circulating-supply?format=object
- `xstocks.circ.BAXx` [ok] 200 503ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.TXRHx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/TXRHx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.GWREx` [ok] 200 955ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 39ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 249ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.QUBTx` [ok] 200 128ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.INDIx` [ok] 200 123ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.WRLDx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.XRXx` [ok] 200 118ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.WGSx` [ok] 200 116ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.FLNCx` [ok] 200 124ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.AIx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jito.tip_floor` [ok] 200 137ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 278ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 124ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 395ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 506ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 367ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 420ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 240ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
