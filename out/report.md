# Borealis — Solana ecosystem report

**Generated** 2026-09-28T07:36:19Z · 2026-09-28 00:36:19 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-28T07:36:10Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -3.23%; DEX 24h $1.90B · 1d -12% · vs-7d-ago -32%; slot 269 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -11.76%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -31.97%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -13.61%. (threshold: `|1d %| >= 8`)
- **WARN · Last TPS sample outside 2.5σ of the 60-sample window** — Last sample 4,907 TPS is +2.66σ vs window mean 4,455 (n=60, σ=170). (threshold: `|last sample − window mean| > 2.5σ`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -3.23%, DeFiLlama TVL 1d -0.79%, DEX 1d -11.76%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 451,253,527 |
| Block height | 429,293,174 |
| Block time | 2026-09-28T07:36:10Z |
| Epoch | 1,044 (56.84% · slot 245,527/432,000) |
| Mean TPS (last ~3,600s) | 4,455.0 |
| Mean non-vote TPS | 1,954.6 |
| Median TPS (same window) | 4,459.6 |
| Mean slot time | 269.3 ms |
| Median slot time | 269.1 ms |
| Transaction count (cluster) | 553,572,279,309 |
| Circulating supply | 587,782,241 SOL |
| Total supply | 634,840,952 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 7 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 440,526,296 SOL |
| Delinquent stake | 23,510.93 SOL (0.005%) |
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

- `4YGgmwyq…` · 12.74K SOL · commission 3% · lag 908456 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 498263 slots
- `ARKk6Rgi…` · 63.93 SOL · commission 10% · lag 1231373 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 21717844 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 56959 slots
- `CZMekcZw…` · 1.00 SOL · commission 100% · lag 451253527 slots
- `CQYPRQ4v…` · 1.00 SOL · commission 100% · lag 17667 slots

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
| Jito tip-floor run-rate (NOT REV) | $77.45K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 77451 USD; at p95 floor → 406251 USD. |
| Protocol fees 24h | $15.50M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $118.05 | coingecko.simple_price |
| 24h change | -3.23% | coingecko.simple_price |
| Market cap | $69.39B | coingecko.simple_price |
| 24h volume | $4.41B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.56B |
| TVL 1d / 7d / 30d | -0.79% / +5.91% / +11.73% |
| DEX volume 24h | $1.90B · 1d -11.76% · vs-7d-ago -31.97% |
| 7d DEX volume | $17.48B · -11.89% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $15.50M |
| Fees 1d / 7d | -13.61% / +11.95% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| Orca DEX | $327.78M | +42.03% |
| PumpSwap | $297.07M | -42.16% |
| BisonFi | $251.33M | 0.00% |
| pump.fun | $210.79M | 0.00% |
| Raydium AMM | $200.92M | +0.98% |
| Meteora DLMM | $158.26M | -2.49% |
| fomo Wallet | $151.50M | -27.74% |
| Axiom | $150.83M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.94B | -0.88% | +9.54% |
| Kamino Lend | Lending | $1.45B | -1.57% | +4.17% |
| Raydium AMM | Dexs | $1.35B | -0.73% | +7.02% |
| Jito Liquid Staking | Liquid Staking | $1.24B | -0.76% | +7.52% |
| Binance Staked SOL | Liquid Staking | $1.22B | -1.04% | +5.04% |
| Jupiter Lend | Lending | $1.17B | -0.41% | +1.87% |
| Jupiter Perpetual Exchange | Derivatives | $817.85M | -0.60% | +2.91% |
| Jupiter Staked SOL | Liquid Staking | $616.48M | -1.08% | +6.71% |
| Marinade Native | Staking Pool | $460.60M | -1.11% | +8.32% |
| PumpSwap | Dexs | $391.62M | -1.89% | +6.40% |

## Stablecoins

Solana circulating pegged-USD: **$16.45B**
(1d -0.49% · 7d +5.16%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.32B | +0.29% |
| USDT · Tether | $2.67B | -0.00% |
| USDGO · USDGO | $1.41B | -0.14% |
| USD1 · World Liberty Financial USD | $1.39B | -0.00% |
| BUIDL · BlackRock USD | $987.88M | 0.00% |
| PYUSD · PayPal USD | $748.99M | -1.54% |
| USDG · Global Dollar | $680.44M | +0.07% |
| USDe · Ethena USDe | $464.20M | -0.73% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $110.53K (lower bound, not a census).
24h volume $56.56M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$546.06M** across 15 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $296.60M
- **Huma** (RWA) — $209.04M
- **Plume Vaults** (RWA) — $25.47M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $3.03M
- **Oro Finance** (RWA) — $2.43M
- **International Stable Currency** (RWA) — $2.43M
- **Byzanlink RWA Markets** (RWA) — $892.38K

## Daily active addresses

739,582 (Allium, as of 2026-09-27). Provider range 397,999–821,475. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

_As of 2026-09-28 (2026-09-28 00:36:19 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 78ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 42ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 40ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 37ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 35ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6480ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 69ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 78ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 24ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 135ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 21ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 21ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 37ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 72ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 47ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 46ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 76ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 252ms https://solana.com/data
- `solana.com.databricks` [ok] 200 1150ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 387ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 95ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 94ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 54ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 286ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 193ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 56ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 60ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 58ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 2247ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 339ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 60ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 37ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 169ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 95ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 41ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 39ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 60ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 211ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 75ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 44ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 117ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 218ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 147ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 283ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 138ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 195ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 111ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 226ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 36ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 241ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 102ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 182ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 120ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 162ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 274ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 244ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 115ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 213ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 158ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 224ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 87ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 123ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 156ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 93ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1179ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1488ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2017ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1094ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1604ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1687ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1302ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1403ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.PCTx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.WGSx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.FLNCx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.XRXx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.INDIx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WRLDx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.METCx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.XRXx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.price.BETRx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.mult.METCx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.QUBTx` [ok] 200 1018ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.AIx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.BETRx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.circ.INDIx` [ok] 200 1061ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.price.MIDDx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data
- `xstocks.circ.PCTx` [ok] 200 1122ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.circ.MIDDx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 1407ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.price.ALMx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data
- `xstocks.price.RITMx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data
- `xstocks.mult.MIDDx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.RITMx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 1866ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.price.SHCx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data
- `xstocks.mult.WYFIx` [ok] 200 1155ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.SHCx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object
- `xstocks.mult.RITMx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana
- `xstocks.circ.ALMx` [ok] 200 585ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object
- `xstocks.mult.SHCx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 1022ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.VSNTx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data
- `xstocks.mult.ALMx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana
- `xstocks.price.WHx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/WHx/price-data
- `xstocks.price.CARx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/CARx/price-data
- `xstocks.circ.WHx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object
- `xstocks.price.REYNx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data
- `xstocks.circ.REYNx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object
- `xstocks.price.RNGx` [ok] 200 910ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data
- `xstocks.mult.WHx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana
- `xstocks.circ.VSNTx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object
- `xstocks.mult.REYNx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana
- `xstocks.circ.CARx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object
- `xstocks.price.GXOx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data
- `xstocks.price.FBINx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data
- `xstocks.circ.RNGx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object
- `xstocks.price.OZKx` [ok] 200 761ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data
- `xstocks.circ.GXOx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object
- `xstocks.mult.VSNTx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana
- `xstocks.mult.CARx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana
- `xstocks.price.IRDMx` [ok] 200 810ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data
- `xstocks.circ.OZKx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object
- `xstocks.circ.FBINx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object
- `xstocks.circ.IRDMx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 2371ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.price.AMTMx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data
- `xstocks.mult.FBINx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana
- `xstocks.mult.OZKx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.circ.AMTMx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object
- `xstocks.price.SAICx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data
- `xstocks.mult.GXOx` [ok] 200 631ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana
- `xstocks.price.MTNx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data
- `xstocks.circ.SAICx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object
- `xstocks.price.EXLSx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data
- `xstocks.circ.EXLSx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object
- `xstocks.price.PEGAx` [ok] 200 670ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data
- `xstocks.mult.RNGx` [ok] 200 1051ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana
- `xstocks.circ.PEGAx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object
- `xstocks.price.EPAMx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data
- `xstocks.mult.SAICx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana
- `xstocks.price.PSNx` [ok] 200 974ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data
- `xstocks.circ.MTNx` [ok] 200 634ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object
- `xstocks.mult.EXLSx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana
- `xstocks.price.CRUSx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data
- `xstocks.mult.PEGAx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana
- `xstocks.circ.PSNx` [ok] 200 109ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object
- `xstocks.price.ELFx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data
- `xstocks.price.Mx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/Mx/price-data
- `xstocks.mult.MTNx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana
- `xstocks.circ.Mx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object
- `xstocks.mult.PSNx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana
- `xstocks.price.SNDRx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data
- `xstocks.price.VNOx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data
- `xstocks.circ.SNDRx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object
- `xstocks.circ.VNOx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object
- `xstocks.mult.Mx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana
- `xstocks.price.EXPx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data
- `xstocks.mult.VNOx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana
- `xstocks.mult.SNDRx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana
- `xstocks.mult.IRDMx` [ok] 200 1951ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana
- `xstocks.circ.EXPx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object
- `xstocks.price.MKTXx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data
- `xstocks.price.HXLx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data
- `xstocks.price.VIRTx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data
- `xstocks.circ.MKTXx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object
- `xstocks.circ.HXLx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object
- `xstocks.circ.CRUSx` [ok] 200 1191ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object
- `xstocks.mult.MKTXx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana
- `xstocks.mult.AMTMx` [ok] 200 2424ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana
- `xstocks.circ.VIRTx` [ok] 200 498ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object
- `xstocks.mult.HXLx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana
- `xstocks.mult.CRUSx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana
- `xstocks.price.VFCx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data
- `xstocks.price.NXSTx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data
- `xstocks.price.ADTx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data
- `xstocks.price.CPBx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data
- `xstocks.mult.EXPx` [ok] 200 777ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana
- `xstocks.circ.NXSTx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object
- `xstocks.circ.CPBx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object
- `xstocks.circ.VFCx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object
- `xstocks.price.BCx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/BCx/price-data
- `xstocks.mult.VIRTx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana
- `xstocks.circ.ADTx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object
- `xstocks.mult.VFCx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana
- `xstocks.circ.BCx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object
- `xstocks.mult.CPBx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana
- `xstocks.mult.NXSTx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana
- `xstocks.price.KRMNx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data
- `xstocks.circ.EPAMx` [ok] 200 2281ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object
- `xstocks.price.ACIx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data
- `xstocks.price.GTESx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data
- `xstocks.mult.BCx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana
- `xstocks.price.HRBx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data
- `xstocks.circ.ACIx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object
- `xstocks.circ.GTESx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object
- `xstocks.circ.KRMNx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object
- `xstocks.circ.ELFx` [ok] 200 2405ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object
- `xstocks.price.AXSx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data
- `xstocks.mult.KRMNx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana
- `xstocks.mult.GTESx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana
- `xstocks.mult.ELFx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana
- `xstocks.price.RYNx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data
- `xstocks.mult.EPAMx` [ok] 200 629ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana
- `xstocks.price.POOLx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data
- `xstocks.mult.ADTx` [ok] 200 920ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana
- `xstocks.price.DLBx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data
- `xstocks.circ.RYNx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object
- `xstocks.price.TFXx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data
- `xstocks.mult.ACIx` [ok] 200 601ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana
- `xstocks.circ.POOLx` [ok] 200 110ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object
- `xstocks.mult.POOLx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana
- `xstocks.price.LWx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/LWx/price-data
- `xstocks.price.SONx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/SONx/price-data
- `xstocks.mult.RYNx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana
- `xstocks.price.INGMx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data
- `xstocks.circ.HRBx` [ok] 200 1422ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object
- `xstocks.circ.DLBx` [ok] 200 933ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object
- `xstocks.mult.HRBx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana
- `xstocks.mult.DLBx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana
- `xstocks.circ.TFXx` [ok] 200 1053ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object
- `xstocks.mult.TFXx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana
- `xstocks.price.AAONx` [ok] 200 1227ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.price.RLIx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data
- `xstocks.price.HRx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/HRx/price-data
- `xstocks.circ.AXSx` [ok] 200 1731ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object
- `xstocks.circ.SONx` [ok] 200 1306ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object
- `xstocks.mult.AXSx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana
- `xstocks.price.TTDx` [ok] 200 779ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data
- `xstocks.circ.INGMx` [ok] 200 1119ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object
- `xstocks.mult.SONx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana
- `xstocks.price.CLFx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data
- `xstocks.circ.TTDx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object
- `xstocks.mult.TTDx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana
- `xstocks.circ.AAONx` [ok] 200 982ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.price.MSMx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data
- `xstocks.mult.AAONx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.price.STWDx` [ok] 200 813ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data
- `xstocks.price.CZRx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data
- `xstocks.circ.LWx` [ok] 200 2416ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object
- `xstocks.circ.STWDx` [ok] 200 111ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object
- `xstocks.circ.CLFx` [ok] 200 979ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object
- `xstocks.mult.LWx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana
- `xstocks.mult.STWDx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana
- `xstocks.price.CROXx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data
- `xstocks.price.OMFx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data
- `xstocks.circ.HRx` [ok] 200 1635ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object
- `xstocks.circ.OMFx` [ok] 200 108ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object
- `xstocks.circ.CROXx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object
- `xstocks.mult.OMFx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana
- `xstocks.circ.RLIx` [ok] 200 1999ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object
- `xstocks.price.CHEx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data
- `xstocks.circ.MSMx` [ok] 200 1251ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object
- `xstocks.circ.CHEx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object
- `xstocks.mult.RLIx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana
- `xstocks.mult.CHEx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana
- `xstocks.mult.CLFx` [ok] 200 1062ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana
- `xstocks.mult.INGMx` [ok] 200 2094ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana
- `xstocks.price.ALGMx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data
- `xstocks.circ.CZRx` [ok] 200 1227ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object
- `xstocks.mult.HRx` [ok] 200 910ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana
- `xstocks.circ.ALGMx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object
- `xstocks.mult.MSMx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana
- `xstocks.price.Gx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/Gx/price-data
- `xstocks.mult.CROXx` [ok] 200 866ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana
- `xstocks.price.MTGx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data
- `xstocks.price.MTDRx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data
- `xstocks.mult.CZRx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana
- `xstocks.circ.Gx` [ok] 200 109ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object
- `xstocks.price.LYFTx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data
- `xstocks.circ.MTDRx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object
- `xstocks.price.INGRx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data
- `xstocks.mult.Gx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana
- `xstocks.mult.ALGMx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana
- `xstocks.circ.MTGx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object
- `xstocks.circ.INGRx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object
- `xstocks.price.BEPCx` [ok] 200 666ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data
- `xstocks.circ.BEPCx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object
- `xstocks.price.STAGx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data
- `xstocks.mult.MTDRx` [ok] 200 596ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana
- `xstocks.mult.MTGx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana
- `xstocks.price.BYDx` [ok] 200 743ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data
- `xstocks.mult.BEPCx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana
- `xstocks.price.CACCx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data
- `xstocks.circ.BYDx` [ok] 200 107ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object
- `xstocks.circ.LYFTx` [ok] 200 844ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object
- `xstocks.circ.CACCx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object
- `xstocks.price.FNBx` [ok] 200 752ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data
- `xstocks.mult.LYFTx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana
- `xstocks.mult.CACCx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana
- `xstocks.price.MBGLx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data
- `xstocks.mult.BYDx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana
- `xstocks.circ.MBGLx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object
- `xstocks.circ.FNBx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object
- `xstocks.mult.MBGLx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana
- `xstocks.mult.INGRx` [ok] 200 1209ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana
- `xstocks.circ.STAGx` [ok] 200 1050ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object
- `xstocks.mult.STAGx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana
- `xstocks.mult.FNBx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 506ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 137ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.XRXx` [ok] 200 39ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.QUBTx` [ok] 200 49ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.FLNCx` [ok] 200 39ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.BETRx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.WGSx` [ok] 200 38ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.WYFIx` [ok] 200 40ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.AIx` [ok] 200 44ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.INDIx` [ok] 200 39ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jito.tip_floor` [ok] 200 57ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 338ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 72ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 77ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 36ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 35ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 36ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 2464ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
