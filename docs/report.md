# Borealis — Solana ecosystem report

**Generated** 2026-09-27T23:14:47Z · 2026-09-27 16:14:47 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-27T23:14:38Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** WATCH · **Ecosystem** CONTRACTION — SOL 24h -0.12%; DEX 24h $2.16B · 1d -18% · vs-7d-ago -25%; slot 269 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Correlation: congestion (slot time ↑ + non-vote TPS ↓ + fees ↑)** — Slot time 270 ms, last non-vote TPS 1,721 vs window median 2,366, DeFiLlama fees 1d +19.0%. (threshold: `elevated slot time AND depressed non-vote TPS AND fees 1d >= 8%`)
- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -17.52%. (threshold: `|1d %| >= 8`)
- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +18.97%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -25.07%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +26.02%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 451,141,439 |
| Block height | 429,181,109 |
| Block time | 2026-09-27T23:14:38Z |
| Epoch | 1,044 (30.89% · slot 133,440/432,000) |
| Mean TPS (last ~3,600s) | 4,830.6 |
| Mean non-vote TPS | 2,332.9 |
| Median TPS (same window) | 4,853.4 |
| Mean slot time | 269.3 ms |
| Median slot time | 269.1 ms |
| Transaction count (cluster) | 553,432,172,286 |
| Circulating supply | 587,782,605 SOL |
| Total supply | 634,841,316 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 8 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 440,525,953 SOL |
| Delinquent stake | 23,853.34 SOL (0.005%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.46% / 35.37% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.87M SOL | 4.06% | 7% | 0 |
| 2 | `HEL1USMZ…` | 15.84M SOL | 3.60% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.33M SOL | 2.80% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.22M SOL | 2.55% | 5% | 0 |
| 5 | `E1r4Psq8…` | 10.84M SOL | 2.46% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.24M SOL | 2.10% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.21M SOL | 2.09% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.62M SOL | 1.73% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.09M SOL | 1.61% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.51M SOL | 1.48% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.27M SOL | 1.42% | 0% | 0 |
| 12 | `5pPRHnie…` | 5.91M SOL | 1.34% | 5% | 0 |
| 13 | `5Cchr1XG…` | 5.63M SOL | 1.28% | 100% | 0 |
| 14 | `9rkJMARq…` | 4.70M SOL | 1.07% | 8% | 0 |
| 15 | `GnC339vk…` | 4.62M SOL | 1.05% | 7% | 0 |

### Delinquency alerts

- `4YGgmwyq…` · 12.74K SOL · commission 3% · lag 796368 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 386175 slots
- `2ooJ5UKS…` · 342.41 SOL · commission 0% · lag 134131 slots
- `ARKk6Rgi…` · 63.93 SOL · commission 10% · lag 1119285 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 21605756 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 265922 slots
- `CZMekcZw…` · 1.00 SOL · commission 100% · lag 451141439 slots
- `CQYPRQ4v…` · 1.00 SOL · commission 100% · lag 66567 slots

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
| **In-protocol fees 24h** | **$1.20M** (9,949.3 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-26 |
| **Solana REV** | **12,524.8 SOL** / **$1.52M** | MEASURED UTC calendar day 2026-09-26: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-26 · UTC day 2026-09-26 · SOL-USD date 2026-09-26 |
| Jito tip-floor run-rate (NOT REV) | $141.41K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 141407 USD; at p95 floor → 5580032 USD. |
| Protocol fees 24h | $17.94M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $121.46 | coingecko.simple_price |
| 24h change | -0.12% | coingecko.simple_price |
| Market cap | $71.38B | coingecko.simple_price |
| 24h volume | $3.87B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.70B |
| TVL 1d / 7d / 30d | +0.97% / +8.47% / +11.18% |
| DEX volume 24h | $2.16B · 1d -17.52% · vs-7d-ago -25.07% |
| 7d DEX volume | $19.19B · +1.91% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $17.94M |
| Fees 1d / 7d | +18.97% / +26.02% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $513.61M | +20.57% |
| BisonFi | $251.33M | -23.33% |
| Orca DEX | $240.17M | -37.77% |
| pump.fun | $210.79M | +76.94% |
| Raydium AMM | $178.78M | -39.76% |
| Meteora DLMM | $162.30M | -20.66% |
| fomo Wallet | $158.70M | +9.29% |
| Axiom | $150.83M | +70.34% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.99B | +0.74% | +13.50% |
| Kamino Lend | Lending | $1.48B | +0.78% | +6.84% |
| Raydium AMM | Dexs | $1.39B | +1.26% | +12.60% |
| Jito Liquid Staking | Liquid Staking | $1.27B | +0.82% | +11.33% |
| Binance Staked SOL | Liquid Staking | $1.25B | +0.77% | +9.64% |
| Jupiter Lend | Lending | $1.20B | +1.19% | +4.98% |
| Jupiter Perpetual Exchange | Derivatives | $832.58M | +0.72% | +5.84% |
| Jupiter Staked SOL | Liquid Staking | $634.20M | +0.79% | +11.30% |
| Marinade Native | Staking Pool | $472.79M | +0.90% | +12.72% |
| PumpSwap | Dexs | $400.06M | -0.06% | +13.92% |

## Stablecoins

Solana circulating pegged-USD: **$16.38B**
(1d -0.04% · 7d +6.37%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.25B | -2.85% |
| USDT · Tether | $2.67B | -0.00% |
| USDGO · USDGO | $1.41B | 0.00% |
| USD1 · World Liberty Financial USD | $1.39B | +0.00% |
| BUIDL · BlackRock USD | $987.88M | 0.00% |
| PYUSD · PayPal USD | $743.57M | -4.45% |
| USDG · Global Dollar | $674.04M | +1.00% |
| USDe · Ethena USDe | $465.99M | -3.57% |

## Tokenized equities (xStocks)


Listed 800 · Solana deployments 800 · priced 0 · priced-subset mcap — (lower bound, not a census).
24h volume $46.76M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 0 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$549.86M** across 15 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $296.59M
- **Huma** (RWA) — $212.76M
- **Plume Vaults** (RWA) — $25.47M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $3.07M
- **Oro Finance** (RWA) — $2.47M
- **International Stable Currency** (RWA) — $2.41M
- **Byzanlink RWA Markets** (RWA) — $891.60K

## Daily active addresses

768,421 (Allium, as of 2026-09-26). Provider range 430,262–821,475. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

_As of 2026-09-27 (2026-09-27 16:14:47 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=live, 200ms=pending. Observed mean slot ~269 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~269 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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
- **xStocks market cap** — Listed Solana-deployed xStocks but quote and/or circulating missing. Mcap omitted.
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.
- **xStocks** — price, circulating-supply, and/or currentMultiplier missing — market cap omitted (never assumed multiplier=1.0)

## Sources this run

- `rpc.getHealth` [ok] 200 158ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 208ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 176ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 149ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 141ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5444ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 299ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 156ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 240ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 152ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 77ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 96ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 95ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 241ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 132ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 132ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 163ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 503ms https://solana.com/data
- `solana.com.databricks` [ok] 200 519ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 1611ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 247ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 176ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 125ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 394ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 464ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 165ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 163ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 162ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 2225ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1256ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 3850ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1879ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 289ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 235ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 138ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 151ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 118ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 176ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 211ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 135ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 293ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 254ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 233ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 312ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 279ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 260ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 234ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 224ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 92ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 230ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 226ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 392ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 204ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 390ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 248ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 1035ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 278ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 573ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 228ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 285ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 203ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 214ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 143ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 170ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1776ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1601ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1681ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 980ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1769ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1616ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1590ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1362ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.FLNCx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.INDIx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.QUBTx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WGSx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.XRXx` [FAIL]  12055ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PCTx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WRLDx` [FAIL]  12057ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METCx` [FAIL]  12059ms https://api.backed.fi/api/v2/public/assets/METCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.QUBTx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 612ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 1125ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 1199ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.WRLDx` [ok] 200 1393ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.PCTx` [ok] 200 1602ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 1026ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.XRXx` [ok] 200 2989ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 599ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.WYFIx` [FAIL]  12056ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BETRx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AIx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/AIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BETRx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.price.MIDDx` [FAIL]  12057ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.BETRx` [ok] 200 456ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.circ.WYFIx` [ok] 200 953ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.ALMx` [FAIL]  12056ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ALMx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object
- `xstocks.price.RITMx` [FAIL]  12045ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.RNGx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.AIx` [ok] 200 1347ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 1261ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.MIDDx` [ok] 200 1462ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object
- `xstocks.circ.RITMx` [ok] 200 969ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object
- `xstocks.mult.RITMx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana
- `xstocks.mult.ALMx` [ok] 200 1366ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana
- `xstocks.circ.RNGx` [ok] 200 1242ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object
- `xstocks.price.SHCx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.RNGx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana
- `xstocks.mult.MIDDx` [ok] 200 968ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana
- `xstocks.circ.SHCx` [ok] 200 1193ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object
- `xstocks.mult.SHCx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana
- `xstocks.price.WHx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/WHx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.REYNx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.VSNTx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WHx` [ok] 200 1285ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object
- `xstocks.mult.WHx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana
- `xstocks.price.CARx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/CARx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.OZKx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.REYNx` [ok] 200 1154ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object
- `xstocks.price.IRDMx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.REYNx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana
- `xstocks.price.GXOx` [FAIL]  12044ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.GXOx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object
- `xstocks.circ.VSNTx` [ok] 200 1553ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object
- `xstocks.mult.VSNTx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana
- `xstocks.circ.OZKx` [ok] 200 1520ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object
- `xstocks.circ.IRDMx` [ok] 200 1174ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object
- `xstocks.mult.GXOx` [ok] 200 788ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana
- `xstocks.price.FBINx` [FAIL]  12050ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CARx` [ok] 200 2006ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object
- `xstocks.mult.IRDMx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana
- `xstocks.mult.CARx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana
- `xstocks.mult.OZKx` [ok] 200 785ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana
- `xstocks.circ.FBINx` [ok] 200 1240ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object
- `xstocks.mult.FBINx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana
- `xstocks.price.AMTMx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AMTMx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object
- `xstocks.mult.AMTMx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana
- `xstocks.price.MTNx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PSNx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PEGAx` [FAIL]  12050ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MTNx` [ok] 200 1355ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object
- `xstocks.price.SAICx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.EXLSx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MTNx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana
- `xstocks.price.EPAMx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.PSNx` [ok] 200 1406ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object
- `xstocks.mult.PSNx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana
- `xstocks.circ.PEGAx` [ok] 200 1339ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object
- `xstocks.mult.PEGAx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana
- `xstocks.price.CRUSx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SAICx` [ok] 200 1428ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object
- `xstocks.circ.EPAMx` [ok] 200 1328ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object
- `xstocks.mult.SAICx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana
- `xstocks.circ.EXLSx` [ok] 200 2182ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object
- `xstocks.mult.EXLSx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana
- `xstocks.circ.CRUSx` [ok] 200 1324ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object
- `xstocks.mult.EPAMx` [ok] 200 1345ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana
- `xstocks.mult.CRUSx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana
- `xstocks.price.Mx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/Mx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ELFx` [FAIL]  12060ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.Mx` [ok] 200 2394ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object
- `xstocks.price.SNDRx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.Mx` [ok] 200 427ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana
- `xstocks.price.VNOx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.EXPx` [FAIL]  12041ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ELFx` [ok] 200 1737ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object
- `xstocks.mult.ELFx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana
- `xstocks.circ.VNOx` [ok] 200 1063ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object
- `xstocks.circ.SNDRx` [ok] 200 1614ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object
- `xstocks.price.VIRTx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.VNOx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana
- `xstocks.mult.SNDRx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana
- `xstocks.price.HXLx` [FAIL]  12043ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MKTXx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.EXPx` [ok] 200 1312ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object
- `xstocks.circ.VIRTx` [ok] 200 1264ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object
- `xstocks.mult.VIRTx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana
- `xstocks.mult.EXPx` [ok] 200 1212ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana
- `xstocks.circ.MKTXx` [ok] 200 1777ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object
- `xstocks.circ.HXLx` [ok] 200 1930ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object
- `xstocks.mult.MKTXx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana
- `xstocks.mult.HXLx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana
- `xstocks.price.CPBx` [FAIL]  12045ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.VFCx` [FAIL]  12059ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CPBx` [ok] 200 1648ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object
- `xstocks.price.NXSTx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CPBx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana
- `xstocks.price.ADTx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ADTx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object
- `xstocks.mult.ADTx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana
- `xstocks.circ.VFCx` [ok] 200 1863ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object
- `xstocks.circ.NXSTx` [ok] 200 1346ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object
- `xstocks.price.BCx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/BCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ACIx` [FAIL]  12046ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.VFCx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana
- `xstocks.price.KRMNx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.NXSTx` [ok] 200 1026ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana
- `xstocks.price.GTESx` [FAIL]  12046ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ACIx` [ok] 200 879ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object
- `xstocks.mult.ACIx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana
- `xstocks.circ.BCx` [ok] 200 2253ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object
- `xstocks.circ.GTESx` [ok] 200 1244ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object
- `xstocks.mult.BCx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana
- `xstocks.mult.GTESx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana
- `xstocks.circ.KRMNx` [ok] 200 4597ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object
- `xstocks.mult.KRMNx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana
- `xstocks.price.HRBx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AXSx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DLBx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HRBx` [ok] 200 1578ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object
- `xstocks.mult.HRBx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana
- `xstocks.circ.AXSx` [ok] 200 1454ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object
- `xstocks.price.RYNx` [FAIL]  12047ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.AXSx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana
- `xstocks.price.POOLx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.RYNx` [ok] 200 1263ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object
- `xstocks.price.TFXx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.RYNx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana
- `xstocks.price.LWx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/LWx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DLBx` [ok] 200 2658ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object
- `xstocks.mult.DLBx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana
- `xstocks.circ.POOLx` [ok] 200 2050ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object
- `xstocks.mult.POOLx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana
- `xstocks.circ.LWx` [ok] 200 1225ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object
- `xstocks.circ.TFXx` [ok] 200 1609ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object
- `xstocks.mult.TFXx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana
- `xstocks.mult.LWx` [ok] 200 1696ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana
- `xstocks.price.AAONx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AAONx` [ok] 200 666ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.mult.AAONx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.price.SONx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/SONx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.INGMx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.TTDx` [FAIL]  12055ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SONx` [ok] 200 2088ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object
- `xstocks.mult.SONx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana
- `xstocks.price.HRx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/HRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.INGMx` [ok] 200 2227ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object
- `xstocks.mult.INGMx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana
- `xstocks.price.RLIx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.TTDx` [ok] 200 1271ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object
- `xstocks.mult.TTDx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana
- `xstocks.price.CLFx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HRx` [ok] 200 1264ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object
- `xstocks.circ.CLFx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object
- `xstocks.mult.HRx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana
- `xstocks.price.STWDx` [FAIL]  12056ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.RLIx` [ok] 200 2411ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object
- `xstocks.mult.RLIx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana
- `xstocks.mult.CLFx` [ok] 200 1795ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana
- `xstocks.price.MSMx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MSMx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object
- `xstocks.mult.MSMx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana
- `xstocks.circ.STWDx` [ok] 200 2155ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object
- `xstocks.mult.STWDx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana
- `xstocks.price.CZRx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CZRx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object
- `xstocks.price.OMFx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CZRx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana
- `xstocks.circ.OMFx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object
- `xstocks.mult.OMFx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana
- `xstocks.price.CROXx` [FAIL]  12042ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CHEx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CHEx` [ok] 200 1264ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object
- `xstocks.circ.CROXx` [ok] 200 1652ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object
- `xstocks.price.Gx` [FAIL]  12049ms https://api.backed.fi/api/v2/public/assets/Gx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ALGMx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.Gx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object
- `xstocks.mult.CROXx` [ok] 200 741ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana
- `xstocks.mult.Gx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana
- `xstocks.circ.ALGMx` [ok] 200 565ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object
- `xstocks.price.MTGx` [FAIL]  12054ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.ALGMx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana
- `xstocks.price.BEPCx` [FAIL]  12056ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MTGx` [ok] 200 831ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object
- `xstocks.mult.CHEx` [ok] 200 2276ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana
- `xstocks.circ.BEPCx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object
- `xstocks.mult.BEPCx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana
- `xstocks.mult.MTGx` [ok] 200 1041ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana
- `xstocks.price.MTDRx` [FAIL]  12058ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MTDRx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object
- `xstocks.price.INGRx` [FAIL]  12040ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.INGRx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object
- `xstocks.mult.MTDRx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana
- `xstocks.mult.INGRx` [ok] 200 630ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana
- `xstocks.price.LYFTx` [FAIL]  12050ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BYDx` [FAIL]  12055ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.LYFTx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object
- `xstocks.circ.BYDx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object
- `xstocks.mult.BYDx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana
- `xstocks.price.STAGx` [FAIL]  12049ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.STAGx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object
- `xstocks.mult.LYFTx` [ok] 200 711ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana
- `xstocks.mult.STAGx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana
- `xstocks.price.FNBx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MBGLx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.FNBx` [ok] 200 536ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object
- `xstocks.mult.FNBx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana
- `xstocks.price.CACCx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CACCx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object
- `xstocks.mult.CACCx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana
- `xstocks.circ.MBGLx` [ok] 200 1589ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object
- `xstocks.mult.MBGLx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 90ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 304ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.QUBTx` [ok] 200 145ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.METCx` [ok] 200 143ms https://lite-api.jup.ag/tokens/v2/search?query=METCx
- `jup.tokens.search.FLNCx` [ok] 200 153ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.WGSx` [ok] 200 145ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.WRLDx` [ok] 200 154ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.PCTx` [ok] 200 152ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.INDIx` [ok] 200 140ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.XRXx` [ok] 200 143ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jito.tip_floor` [ok] 200 112ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 375ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 303ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 147ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 188ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 185ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 206ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 6159ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
