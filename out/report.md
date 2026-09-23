# Borealis — Solana ecosystem report

**Generated** 2026-09-23T00:01:07Z · 2026-09-22 17:01:07 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-23T00:00:58Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h -0.28%; DEX 24h $3.43B · 1d +23% · vs-7d-ago +36%; slot 266 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +26.21%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +37.26%. (threshold: `|7d %| >= 20`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +22.67%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +35.51%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 449,534,168 |
| Block height | 427,574,489 |
| Block time | 2026-09-23T00:00:58Z |
| Epoch | 1,040 (58.84% · slot 254,170/432,000) |
| Mean TPS (last ~3,600s) | 4,513.8 |
| Mean non-vote TPS | 1,984.2 |
| Median TPS (same window) | 4,458.9 |
| Mean slot time | 266.3 ms |
| Median slot time | 266.7 ms |
| Transaction count (cluster) | 551,511,465,622 |
| Circulating supply | 587,507,270 SOL |
| Total supply | 634,530,897 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 677 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,661,998 SOL |
| Delinquent stake | 199,750.97 SOL (0.045%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.33% / 35.64% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.83M SOL | 4.05% | 7% | 0 |
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

- `6DTkuiey…` · 89.15K SOL · commission 100% · lag 449534168 slots
- `HDRqPft5…` · 71.15K SOL · commission 100% · lag 449534168 slots
- `t23p8aBQ…` · 14.37K SOL · commission 0% · lag 1938932 slots
- `AYY1TCe3…` · 10.71K SOL · commission 0% · lag 8196 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 735458 slots
- `mrgn4atx…` · 2.26K SOL · commission 0% · lag 936763 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 1659416 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 1041297 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 771793 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 19998485 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 600828 slots
- `CQYPRQ4v…` · 1.00 SOL · commission 100% · lag 233724 slots

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
| **In-protocol fees 24h** | **$1.08M** (9,224.4 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-21 |
| **Solana REV** | **11,259.0 SOL** / **$1.32M** | MEASURED UTC calendar day 2026-09-21: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-21 · UTC day 2026-09-21 · SOL-USD date 2026-09-21 |
| Jito tip-floor run-rate (NOT REV) | $45.59K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 45591 USD; at p95 floor → 8757568 USD. |
| Protocol fees 24h | $18.64M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0006) | NOT a 24h census · ~0.0h · n_tx=160 window_seconds=1 |
| p90 / p99 | 0.000005 / 0.000005 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $118.54 | coingecko.simple_price |
| 24h change | -0.28% | coingecko.simple_price |
| Market cap | $69.64B | coingecko.simple_price |
| 24h volume | $4.66B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.50B |
| TVL 1d / 7d / 30d | +4.70% / +9.78% / +16.65% |
| DEX volume 24h | $3.43B · 1d +22.67% · vs-7d-ago +35.51% |
| 7d DEX volume | $20.73B · +13.88% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $18.64M |
| Fees 1d / 7d | +26.21% / +37.26% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| Raydium AMM | $480.23M | +62.68% |
| BisonFi | $446.78M | +5.31% |
| PumpSwap | $390.12M | -19.19% |
| Orca DEX | $368.96M | +51.13% |
| Meteora DLMM | $259.61M | +35.37% |
| GoonFi | $159.53M | +68.22% |
| Tessera V | $155.45M | +50.88% |
| Scorch | $150.64M | +128.35% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.88B | -0.70% | +22.99% |
| Kamino Lend | Lending | $1.43B | +0.35% | +7.61% |
| Raydium AMM | Dexs | $1.34B | +0.86% | +21.96% |
| Jito Liquid Staking | Liquid Staking | $1.23B | -0.87% | +22.96% |
| Binance Staked SOL | Liquid Staking | $1.21B | -2.04% | +20.53% |
| Jupiter Lend | Lending | $1.18B | -2.09% | +10.43% |
| Jupiter Perpetual Exchange | Derivatives | $820.58M | -0.95% | +12.72% |
| Jupiter Staked SOL | Liquid Staking | $611.25M | -1.18% | +22.02% |
| Marinade Native | Staking Pool | $451.44M | -0.07% | +22.32% |
| PumpSwap | Dexs | $381.84M | +1.75% | +17.26% |

## Stablecoins

Solana circulating pegged-USD: **$16.51B**
(1d +8.00% · 7d +4.82%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.97B | +12.96% |
| USDT · Tether | $2.14B | +0.95% |
| USDGO · USDGO | $1.40B | +1.45% |
| USD1 · World Liberty Financial USD | $1.37B | +2.94% |
| BUIDL · BlackRock USD | $987.58M | -0.56% |
| PYUSD · PayPal USD | $717.23M | -2.42% |
| USDG · Global Dollar | $629.59M | -0.23% |
| USDe · Ethena USDe | $502.77M | -1.22% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $120.44K (lower bound, not a census).
24h volume $162.58M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$536.82M** across 16 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $302.65M
- **Huma Finance V2** (RWA) — $188.67M
- **Plume Vaults** (RWA) — $28.21M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $3.02M
- **VNX** (RWA) — $2.73M
- **Oro Finance** (RWA) — $2.50M
- **International Stable Currency** (RWA) — $2.47M

## Daily active addresses

871,580 (Allium, as of 2026-09-21). Provider range 427,586–892,240. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-23 (2026-09-22 17:01:07 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 265ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 232ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 224ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 222ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 210ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6274ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 453ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 124ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 29ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 51ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 37ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 58ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 37ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 86ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 49ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 60ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 94ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 324ms https://solana.com/data
- `solana.com.databricks` [ok] 200 68ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 427ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 101ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 213ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 65ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 283ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 417ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 236ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 230ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 235ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 2091ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2379ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 792ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1553ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 276ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 158ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 225ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 236ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 245ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 134ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 251ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 120ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 296ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 3289ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 333ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 231ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 302ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 401ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 335ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 218ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 388ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 211ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 297ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 216ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 263ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 222ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [ok] 200 513ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 279ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 238ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 384ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 187ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 295ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 11374ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 284ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 193ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 2624ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1421ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1574ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1212ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1590ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 4638ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1413ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 5416ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.QUBTx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.INDIx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WRLDx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.PCTx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.FLNCx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.WGSx` [ok] 200 516ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.METCx` [ok] 200 602ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.METCx` [ok] 200 976ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 1228ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.price.XRXx` [ok] 200 1682ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.circ.QUBTx` [ok] 200 1514ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 1197ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.METCx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 1489ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 1615ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.INDIx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.price.AAONx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.mult.QUBTx` [ok] 200 725ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.PRIx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/PRIx/price-data
- `xstocks.circ.WRLDx` [ok] 200 2465ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 885ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 892ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.ACMx` [ok] 200 490ms https://api.backed.fi/api/v2/public/assets/ACMx/price-data
- `xstocks.price.ESIx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/ESIx/price-data
- `xstocks.circ.ESIx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/ESIx/circulating-supply?format=object
- `xstocks.circ.BETRx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.AAONx` [ok] 200 1143ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 1451ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.PRIx` [ok] 200 1050ms https://api.backed.fi/api/v2/public/assets/PRIx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 841ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 1435ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.BETRx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.MORNx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/MORNx/price-data
- `xstocks.mult.ESIx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/ESIx/multiplier?network=Solana
- `xstocks.price.THGx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/THGx/price-data
- `xstocks.circ.MORNx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/MORNx/circulating-supply?format=object
- `xstocks.mult.PRIx` [ok] 200 536ms https://api.backed.fi/api/v2/public/assets/PRIx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 652ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.IDAx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/IDAx/price-data
- `xstocks.circ.ACMx` [ok] 200 1304ms https://api.backed.fi/api/v2/public/assets/ACMx/circulating-supply?format=object
- `xstocks.mult.MORNx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/MORNx/multiplier?network=Solana
- `xstocks.price.SAROx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/SAROx/price-data
- `xstocks.mult.AAONx` [ok] 200 896ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.price.EMNx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/EMNx/price-data
- `xstocks.circ.IDAx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/IDAx/circulating-supply?format=object
- `xstocks.price.SFDx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/SFDx/price-data
- `xstocks.circ.THGx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/THGx/circulating-supply?format=object
- `xstocks.price.Zx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/Zx/price-data
- `xstocks.circ.SAROx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/SAROx/circulating-supply?format=object
- `xstocks.mult.THGx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/THGx/multiplier?network=Solana
- `xstocks.mult.IDAx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/IDAx/multiplier?network=Solana
- `xstocks.mult.SAROx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/SAROx/multiplier?network=Solana
- `xstocks.price.AOSx` [ok] 200 606ms https://api.backed.fi/api/v2/public/assets/AOSx/price-data
- `xstocks.mult.ACMx` [ok] 200 654ms https://api.backed.fi/api/v2/public/assets/ACMx/multiplier?network=Solana
- `xstocks.price.CBSHx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/CBSHx/price-data
- `xstocks.price.REXRx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/REXRx/price-data
- `xstocks.price.APPFx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/APPFx/price-data
- `xstocks.circ.REXRx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/REXRx/circulating-supply?format=object
- `xstocks.price.PATHx` [ok] 200 786ms https://api.backed.fi/api/v2/public/assets/PATHx/price-data
- `xstocks.mult.REXRx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/REXRx/multiplier?network=Solana
- `xstocks.circ.PATHx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/PATHx/circulating-supply?format=object
- `xstocks.price.LNCx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/LNCx/price-data
- `xstocks.mult.PATHx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/PATHx/multiplier?network=Solana
- `xstocks.price.MOSx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/MOSx/price-data
- `xstocks.circ.AOSx` [ok] 200 1234ms https://api.backed.fi/api/v2/public/assets/AOSx/circulating-supply?format=object
- `xstocks.circ.APPFx` [ok] 200 1002ms https://api.backed.fi/api/v2/public/assets/APPFx/circulating-supply?format=object
- `xstocks.mult.APPFx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/APPFx/multiplier?network=Solana
- `xstocks.mult.AOSx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/AOSx/multiplier?network=Solana
- `xstocks.circ.CBSHx` [ok] 200 1356ms https://api.backed.fi/api/v2/public/assets/CBSHx/circulating-supply?format=object
- `xstocks.price.PRMBx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/PRMBx/price-data
- `xstocks.circ.Zx` [ok] 200 2187ms https://api.backed.fi/api/v2/public/assets/Zx/circulating-supply?format=object
- `xstocks.price.TKRx` [ok] 200 422ms https://api.backed.fi/api/v2/public/assets/TKRx/price-data
- `xstocks.circ.PRMBx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/PRMBx/circulating-supply?format=object
- `xstocks.circ.LNCx` [ok] 200 1190ms https://api.backed.fi/api/v2/public/assets/LNCx/circulating-supply?format=object
- `xstocks.circ.MOSx` [ok] 200 868ms https://api.backed.fi/api/v2/public/assets/MOSx/circulating-supply?format=object
- `xstocks.mult.Zx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/Zx/multiplier?network=Solana
- `xstocks.circ.SFDx` [ok] 200 2675ms https://api.backed.fi/api/v2/public/assets/SFDx/circulating-supply?format=object
- `xstocks.mult.PRMBx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/PRMBx/multiplier?network=Solana
- `xstocks.mult.MOSx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/MOSx/multiplier?network=Solana
- `xstocks.circ.TKRx` [ok] 200 639ms https://api.backed.fi/api/v2/public/assets/TKRx/circulating-supply?format=object
- `xstocks.price.TAPx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/TAPx/price-data
- `xstocks.mult.SFDx` [ok] 200 612ms https://api.backed.fi/api/v2/public/assets/SFDx/multiplier?network=Solana
- `xstocks.price.KNSLx` [ok] 200 550ms https://api.backed.fi/api/v2/public/assets/KNSLx/price-data
- `xstocks.mult.CBSHx` [ok] 200 1286ms https://api.backed.fi/api/v2/public/assets/CBSHx/multiplier?network=Solana
- `xstocks.price.PCTYx` [ok] 200 698ms https://api.backed.fi/api/v2/public/assets/PCTYx/price-data
- `xstocks.circ.TAPx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/TAPx/circulating-supply?format=object
- `xstocks.mult.LNCx` [ok] 200 902ms https://api.backed.fi/api/v2/public/assets/LNCx/multiplier?network=Solana
- `xstocks.price.KMXx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/KMXx/price-data
- `xstocks.circ.KNSLx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/KNSLx/circulating-supply?format=object
- `xstocks.circ.PCTYx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/PCTYx/circulating-supply?format=object
- `xstocks.mult.TAPx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/TAPx/multiplier?network=Solana
- `xstocks.price.XPx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/XPx/price-data
- `xstocks.mult.KNSLx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/KNSLx/multiplier?network=Solana
- `xstocks.circ.KMXx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/KMXx/circulating-supply?format=object
- `xstocks.mult.PCTYx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/PCTYx/multiplier?network=Solana
- `xstocks.price.NFGx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/NFGx/price-data
- `xstocks.circ.XPx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/XPx/circulating-supply?format=object
- `xstocks.price.LADx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/LADx/price-data
- `xstocks.price.FRx` [ok] 200 770ms https://api.backed.fi/api/v2/public/assets/FRx/price-data
- `xstocks.mult.XPx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/XPx/multiplier?network=Solana
- `xstocks.circ.EMNx` [ok] 200 4265ms https://api.backed.fi/api/v2/public/assets/EMNx/circulating-supply?format=object
- `xstocks.circ.LADx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/LADx/circulating-supply?format=object
- `xstocks.circ.FRx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/FRx/circulating-supply?format=object
- `xstocks.price.WALx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/WALx/price-data
- `xstocks.circ.NFGx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/NFGx/circulating-supply?format=object
- `xstocks.price.BOKFx` [ok] 200 764ms https://api.backed.fi/api/v2/public/assets/BOKFx/price-data
- `xstocks.mult.LADx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/LADx/multiplier?network=Solana
- `xstocks.circ.WALx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/WALx/circulating-supply?format=object
- `xstocks.mult.FRx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/FRx/multiplier?network=Solana
- `xstocks.mult.NFGx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/NFGx/multiplier?network=Solana
- `xstocks.mult.EMNx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/EMNx/multiplier?network=Solana
- `xstocks.circ.BOKFx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/BOKFx/circulating-supply?format=object
- `xstocks.mult.KMXx` [ok] 200 971ms https://api.backed.fi/api/v2/public/assets/KMXx/multiplier?network=Solana
- `xstocks.price.ATRx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/ATRx/price-data
- `xstocks.price.AVAVx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/AVAVx/price-data
- `xstocks.price.QRVOx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/QRVOx/price-data
- `xstocks.mult.BOKFx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/BOKFx/multiplier?network=Solana
- `xstocks.price.CNMx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CNMx/price-data
- `xstocks.circ.ATRx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/ATRx/circulating-supply?format=object
- `xstocks.price.HLIx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/HLIx/price-data
- `xstocks.circ.QRVOx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/QRVOx/circulating-supply?format=object
- `xstocks.mult.TKRx` [ok] 200 1996ms https://api.backed.fi/api/v2/public/assets/TKRx/multiplier?network=Solana
- `xstocks.mult.ATRx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/ATRx/multiplier?network=Solana
- `xstocks.circ.AVAVx` [ok] 200 588ms https://api.backed.fi/api/v2/public/assets/AVAVx/circulating-supply?format=object
- `xstocks.price.UGIx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/UGIx/price-data
- `xstocks.mult.QRVOx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/QRVOx/multiplier?network=Solana
- `xstocks.price.CHRDx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/CHRDx/price-data
- `xstocks.circ.UGIx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/UGIx/circulating-supply?format=object
- `xstocks.price.AXTAx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/AXTAx/price-data
- `xstocks.circ.HLIx` [ok] 200 751ms https://api.backed.fi/api/v2/public/assets/HLIx/circulating-supply?format=object
- `xstocks.price.NNNx` [ok] 200 998ms https://api.backed.fi/api/v2/public/assets/NNNx/price-data
- `xstocks.mult.UGIx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/UGIx/multiplier?network=Solana
- `xstocks.mult.AVAVx` [ok] 200 595ms https://api.backed.fi/api/v2/public/assets/AVAVx/multiplier?network=Solana
- `xstocks.circ.NNNx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/NNNx/circulating-supply?format=object
- `xstocks.circ.CHRDx` [ok] 200 580ms https://api.backed.fi/api/v2/public/assets/CHRDx/circulating-supply?format=object
- `xstocks.mult.WALx` [ok] 200 1523ms https://api.backed.fi/api/v2/public/assets/WALx/multiplier?network=Solana
- `xstocks.circ.AXTAx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/AXTAx/circulating-supply?format=object
- `xstocks.price.VOYAx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/VOYAx/price-data
- `xstocks.mult.CHRDx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CHRDx/multiplier?network=Solana
- `xstocks.circ.CNMx` [ok] 200 1434ms https://api.backed.fi/api/v2/public/assets/CNMx/circulating-supply?format=object
- `xstocks.mult.HLIx` [ok] 200 715ms https://api.backed.fi/api/v2/public/assets/HLIx/multiplier?network=Solana
- `xstocks.mult.NNNx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/NNNx/multiplier?network=Solana
- `xstocks.mult.AXTAx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/AXTAx/multiplier?network=Solana
- `xstocks.price.COLBx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/COLBx/price-data
- `xstocks.circ.VOYAx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/VOYAx/circulating-supply?format=object
- `xstocks.price.CAGx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/CAGx/price-data
- `xstocks.price.NCLHx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/NCLHx/price-data
- `xstocks.price.ADCx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/ADCx/price-data
- `xstocks.price.FPSx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/FPSx/price-data
- `xstocks.circ.COLBx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/COLBx/circulating-supply?format=object
- `xstocks.mult.VOYAx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/VOYAx/multiplier?network=Solana
- `xstocks.price.BRXx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/BRXx/price-data
- `xstocks.mult.CNMx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/CNMx/multiplier?network=Solana
- `xstocks.circ.ADCx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/ADCx/circulating-supply?format=object
- `xstocks.circ.NCLHx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/NCLHx/circulating-supply?format=object
- `xstocks.circ.FPSx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/FPSx/circulating-supply?format=object
- `xstocks.price.AALx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/AALx/price-data
- `xstocks.circ.CAGx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/CAGx/circulating-supply?format=object
- `xstocks.circ.BRXx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/BRXx/circulating-supply?format=object
- `xstocks.price.FORMx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/FORMx/price-data
- `xstocks.mult.NCLHx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/NCLHx/multiplier?network=Solana
- `xstocks.mult.CAGx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/CAGx/multiplier?network=Solana
- `xstocks.mult.BRXx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/BRXx/multiplier?network=Solana
- `xstocks.circ.FORMx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/FORMx/circulating-supply?format=object
- `xstocks.mult.COLBx` [ok] 200 648ms https://api.backed.fi/api/v2/public/assets/COLBx/multiplier?network=Solana
- `xstocks.price.VICRx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/VICRx/price-data
- `xstocks.mult.FORMx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/FORMx/multiplier?network=Solana
- `xstocks.circ.VICRx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/VICRx/circulating-supply?format=object
- `xstocks.price.TPGx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/TPGx/price-data
- `xstocks.mult.ADCx` [ok] 200 792ms https://api.backed.fi/api/v2/public/assets/ADCx/multiplier?network=Solana
- `xstocks.price.BRKRx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/BRKRx/price-data
- `xstocks.price.BIOx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/BIOx/price-data
- `xstocks.price.CUBEx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/CUBEx/price-data
- `xstocks.circ.TPGx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/TPGx/circulating-supply?format=object
- `xstocks.circ.AALx` [ok] 200 943ms https://api.backed.fi/api/v2/public/assets/AALx/circulating-supply?format=object
- `xstocks.mult.FPSx` [ok] 200 1043ms https://api.backed.fi/api/v2/public/assets/FPSx/multiplier?network=Solana
- `xstocks.circ.CUBEx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/CUBEx/circulating-supply?format=object
- `xstocks.price.NEUx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/NEUx/price-data
- `xstocks.mult.TPGx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/TPGx/multiplier?network=Solana
- `xstocks.mult.CUBEx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/CUBEx/multiplier?network=Solana
- `xstocks.mult.VICRx` [ok] 200 631ms https://api.backed.fi/api/v2/public/assets/VICRx/multiplier?network=Solana
- `xstocks.circ.NEUx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/NEUx/circulating-supply?format=object
- `xstocks.price.CELHx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/CELHx/price-data
- `xstocks.price.BAHx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/BAHx/price-data
- `xstocks.price.AREx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/AREx/price-data
- `xstocks.circ.BIOx` [ok] 200 633ms https://api.backed.fi/api/v2/public/assets/BIOx/circulating-supply?format=object
- `xstocks.mult.NEUx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/NEUx/multiplier?network=Solana
- `xstocks.circ.BAHx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/BAHx/circulating-supply?format=object
- `xstocks.mult.BIOx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/BIOx/multiplier?network=Solana
- `xstocks.circ.AREx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/AREx/circulating-supply?format=object
- `xstocks.price.AMGx` [ok] 200 817ms https://api.backed.fi/api/v2/public/assets/AMGx/price-data
- `xstocks.mult.BAHx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/BAHx/multiplier?network=Solana
- `xstocks.price.CGNXx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/CGNXx/price-data
- `xstocks.mult.AREx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/AREx/multiplier?network=Solana
- `xstocks.mult.AALx` [ok] 200 1158ms https://api.backed.fi/api/v2/public/assets/AALx/multiplier?network=Solana
- `xstocks.price.TTCx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/TTCx/price-data
- `xstocks.circ.AMGx` [ok] 200 543ms https://api.backed.fi/api/v2/public/assets/AMGx/circulating-supply?format=object
- `xstocks.price.LINEx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/LINEx/price-data
- `xstocks.mult.AMGx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/AMGx/multiplier?network=Solana
- `xstocks.circ.CELHx` [ok] 200 1190ms https://api.backed.fi/api/v2/public/assets/CELHx/circulating-supply?format=object
- `xstocks.price.MTCHx` [ok] 200 1023ms https://api.backed.fi/api/v2/public/assets/MTCHx/price-data
- `xstocks.circ.BRKRx` [ok] 200 1886ms https://api.backed.fi/api/v2/public/assets/BRKRx/circulating-supply?format=object
- `xstocks.price.OGEx` [ok] 200 888ms https://api.backed.fi/api/v2/public/assets/OGEx/price-data
- `xstocks.price.MSGSx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/MSGSx/price-data
- `xstocks.mult.CELHx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/CELHx/multiplier?network=Solana
- `xstocks.circ.CGNXx` [ok] 200 1173ms https://api.backed.fi/api/v2/public/assets/CGNXx/circulating-supply?format=object
- `xstocks.price.AVTRx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/AVTRx/price-data
- `xstocks.mult.BRKRx` [ok] 200 695ms https://api.backed.fi/api/v2/public/assets/BRKRx/multiplier?network=Solana
- `xstocks.mult.CGNXx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/CGNXx/multiplier?network=Solana
- `xstocks.circ.TTCx` [ok] 200 1202ms https://api.backed.fi/api/v2/public/assets/TTCx/circulating-supply?format=object
- `xstocks.circ.MSGSx` [ok] 200 712ms https://api.backed.fi/api/v2/public/assets/MSGSx/circulating-supply?format=object
- `xstocks.price.TTEKx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/TTEKx/price-data
- `xstocks.price.MHKx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/MHKx/price-data
- `xstocks.circ.MTCHx` [ok] 200 1080ms https://api.backed.fi/api/v2/public/assets/MTCHx/circulating-supply?format=object
- `xstocks.mult.MSGSx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/MSGSx/multiplier?network=Solana
- `xstocks.mult.TTCx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/TTCx/multiplier?network=Solana
- `xstocks.circ.LINEx` [ok] 200 1522ms https://api.backed.fi/api/v2/public/assets/LINEx/circulating-supply?format=object
- `xstocks.price.VIAVx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/VIAVx/price-data
- `xstocks.price.RRCx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/RRCx/price-data
- `xstocks.circ.OGEx` [ok] 200 1409ms https://api.backed.fi/api/v2/public/assets/OGEx/circulating-supply?format=object
- `xstocks.mult.MTCHx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/MTCHx/multiplier?network=Solana
- `xstocks.circ.VIAVx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/VIAVx/circulating-supply?format=object
- `xstocks.mult.VIAVx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/VIAVx/multiplier?network=Solana
- `xstocks.mult.OGEx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/OGEx/multiplier?network=Solana
- `xstocks.mult.LINEx` [ok] 200 581ms https://api.backed.fi/api/v2/public/assets/LINEx/multiplier?network=Solana
- `xstocks.circ.MHKx` [ok] 200 1065ms https://api.backed.fi/api/v2/public/assets/MHKx/circulating-supply?format=object
- `xstocks.mult.MHKx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/MHKx/multiplier?network=Solana
- `xstocks.circ.TTEKx` [ok] 200 1342ms https://api.backed.fi/api/v2/public/assets/TTEKx/circulating-supply?format=object
- `xstocks.circ.AVTRx` [ok] 200 2239ms https://api.backed.fi/api/v2/public/assets/AVTRx/circulating-supply?format=object
- `xstocks.mult.TTEKx` [ok] 200 818ms https://api.backed.fi/api/v2/public/assets/TTEKx/multiplier?network=Solana
- `xstocks.mult.AVTRx` [ok] 200 484ms https://api.backed.fi/api/v2/public/assets/AVTRx/multiplier?network=Solana
- `xstocks.circ.RRCx` [ok] 200 1865ms https://api.backed.fi/api/v2/public/assets/RRCx/circulating-supply?format=object
- `xstocks.mult.RRCx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/RRCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 20ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 441ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.BETRx` [ok] 200 118ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.XRXx` [ok] 200 114ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.QUBTx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WGSx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.FLNCx` [ok] 200 123ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.WYFIx` [ok] 200 120ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.AIx` [ok] 200 156ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.INDIx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jito.tip_floor` [ok] 200 133ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 396ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 208ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 228ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 216ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 227ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 219ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 364ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
