# Borealis — Solana ecosystem report

**Generated** 2026-09-25T01:20:57Z · 2026-09-24 18:20:57 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-25T01:20:46Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h +2.18%; DEX 24h $2.26B · 1d -11% · vs-7d-ago -13%; slot 268 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -11.37%. (threshold: `|1d %| >= 8`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 450,202,547 |
| Block height | 428,242,548 |
| Block time | 2026-09-25T01:20:46Z |
| Epoch | 1,042 (13.55% · slot 58,547/432,000) |
| Mean TPS (last ~3,600s) | 4,492.4 |
| Mean non-vote TPS | 1,981.4 |
| Median TPS (same window) | 4,489.0 |
| Mean slot time | 267.6 ms |
| Median slot time | 267.3 ms |
| Transaction count (cluster) | 552,305,574,279 |
| Circulating supply | 587,648,068 SOL |
| Total supply | 634,686,610 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 10 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 440,528,829 SOL |
| Delinquent stake | 108,367.38 SOL (0.025%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.41% / 35.63% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.82M SOL | 4.04% | 7% | 0 |
| 2 | `HEL1USMZ…` | 15.82M SOL | 3.59% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.39M SOL | 2.81% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.27M SOL | 2.56% | 5% | 0 |
| 5 | `E1r4Psq8…` | 10.60M SOL | 2.41% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.22M SOL | 2.09% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.16M SOL | 2.08% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.60M SOL | 1.73% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.09M SOL | 1.61% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.56M SOL | 1.49% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.15M SOL | 1.40% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.00M SOL | 1.36% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.35% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.62M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `VicAQ3U2…` · 84.76K SOL · commission 5% · lag 35593 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 187391 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 1403837 slots
- `mrgn4atx…` · 2.21K SOL · commission 0% · lag 1605142 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 1709676 slots
- `ARKk6Rgi…` · 63.93 SOL · commission 10% · lag 180393 slots
- `BbCQMWnf…` · 45.00 SOL · commission 0% · lag 87981 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 1440172 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 20666864 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 298039 slots

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
| **In-protocol fees 24h** | **$1.02M** (8,787.2 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-23 |
| **Solana REV** | **10,711.2 SOL** / **$1.25M** | MEASURED UTC calendar day 2026-09-23: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-23 · UTC day 2026-09-23 · SOL-USD date 2026-09-23 |
| Jito tip-floor run-rate (NOT REV) | $137.00K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 136998 USD; at p95 floor → 16866661 USD. |
| Protocol fees 24h | $16.34M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $117.70 | coingecko.simple_price |
| 24h change | +2.18% | coingecko.simple_price |
| Market cap | $69.17B | coingecko.simple_price |
| 24h volume | $4.40B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.48B |
| TVL 1d / 7d / 30d | +0.34% / +9.94% / +15.38% |
| DEX volume 24h | $2.26B · 1d -11.37% · vs-7d-ago -12.74% |
| 7d DEX volume | $19.63B · +12.58% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $16.34M |
| Fees 1d / 7d | +1.45% / +16.39% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| Raydium AMM | $336.10M | -15.06% |
| BisonFi | $323.94M | 0.00% |
| Orca DEX | $315.11M | -13.92% |
| Meteora DLMM | $191.04M | -18.24% |
| PumpSwap | $133.76M | -50.49% |
| pump.fun | $115.24M | 0.00% |
| Scorch | $113.00M | 0.00% |
| fomo Wallet | $110.47M | -13.56% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.88B | +2.05% | +16.43% |
| Kamino Lend | Lending | $1.42B | +0.92% | +7.18% |
| Raydium AMM | Dexs | $1.32B | +1.84% | +15.98% |
| Jito Liquid Staking | Liquid Staking | $1.22B | +2.30% | +16.12% |
| Binance Staked SOL | Liquid Staking | $1.19B | +1.45% | +13.65% |
| Jupiter Lend | Lending | $1.18B | +0.71% | +8.28% |
| Jupiter Perpetual Exchange | Derivatives | $813.60M | +1.15% | +8.73% |
| Jupiter Staked SOL | Liquid Staking | $602.65M | +1.89% | +14.40% |
| Marinade Native | Staking Pool | $446.98M | +1.29% | +15.69% |
| PumpSwap | Dexs | $384.26M | +2.75% | +17.20% |

## Stablecoins

Solana circulating pegged-USD: **$16.38B**
(1d +7.72% · 7d +12.65%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $8.23B | +10.03% |
| USDT · Tether | $2.67B | +24.81% |
| USDGO · USDGO | $1.42B | +0.00% |
| USD1 · World Liberty Financial USD | $1.38B | -0.00% |
| BUIDL · BlackRock USD | $987.78M | +0.01% |
| PYUSD · PayPal USD | $735.08M | -1.28% |
| USDG · Global Dollar | $635.67M | +0.68% |
| USDe · Ethena USDe | $493.55M | -0.77% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 11 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 11 · priced-subset mcap $115.25K (lower bound, not a census).
24h volume $131.38M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 11 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$543.83M** across 16 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $299.13M
- **Huma** (RWA) — $199.26M
- **Plume Vaults** (RWA) — $28.26M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $3.00M
- **VNX** (RWA) — $2.68M
- **Oro Finance** (RWA) — $2.48M
- **International Stable Currency** (RWA) — $2.45M

## Daily active addresses

834,412 (Allium, as of 2026-09-23). Provider range 466,830–883,811. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — solana.com/news · Mon, 14 Sep 2026 11:00:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-25 (2026-09-24 18:20:57 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **X / Twitter RSS** — Public X/Nitter-style RSS yielded no usable items this run (403/gated skipped). xcancel.solana 451, xcancel.solana_status 451, xcancel.anza_xyz 451, xcancel.solana_devs 451, nitter.solana 200, nitter.solana_status empty-or-gated
- **Median tx fee** — no getBlock samples
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 136ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 93ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 109ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 91ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 96ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5199ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 171ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 102ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 32ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 39ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 59ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 29ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 44ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 71ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 44ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 61ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 93ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 513ms https://solana.com/data
- `solana.com.databricks` [ok] 200 14912ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 431ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 158ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 82ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 36ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 311ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 411ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 223ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 231ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 226ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 2200ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1336ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 658ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 231ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 191ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 232ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 106ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 113ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 116ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 208ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 128ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 135ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 157ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 231ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 138ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 230ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 154ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 281ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 174ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 252ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 89ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 178ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 122ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 657ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 148ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 202ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 131ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 230ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 135ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 256ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 129ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 535ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 113ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 202ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 126ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 211ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1815ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1374ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2443ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1892ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1884ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 4377ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1571ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1722ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.XRXx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.WGSx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.QUBTx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.circ.XRXx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.price.PCTx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.WGSx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.price.WRLDx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.METCx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.QUBTx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.price.FLNCx` [ok] 200 529ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.INDIx` [ok] 200 537ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.mult.XRXx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.WRLDx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.PCTx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.BETRx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.mult.FLNCx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.WYFIx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.price.ALMx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data
- `xstocks.mult.WYFIx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.price.RNGx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data
- `xstocks.mult.BETRx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.MIDDx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data
- `xstocks.price.WHx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/WHx/price-data
- `xstocks.circ.MIDDx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object
- `xstocks.price.REYNx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data
- `xstocks.circ.ALMx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object
- `xstocks.circ.WHx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object
- `xstocks.mult.ALMx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana
- `xstocks.circ.REYNx` [ok] 200 422ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 705ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.price.RITMx` [ok] 200 1073ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data
- `xstocks.mult.WHx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana
- `xstocks.mult.MIDDx` [ok] 200 769ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana
- `xstocks.price.VSNTx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data
- `xstocks.price.CARx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CARx/price-data
- `xstocks.mult.REYNx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana
- `xstocks.circ.VSNTx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object
- `xstocks.circ.CARx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object
- `xstocks.price.OZKx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data
- `xstocks.price.IRDMx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data
- `xstocks.mult.CARx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana
- `xstocks.circ.OZKx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object
- `xstocks.circ.IRDMx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object
- `xstocks.price.GXOx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data
- `xstocks.circ.GXOx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object
- `xstocks.circ.RNGx` [ok] 200 1924ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object
- `xstocks.mult.VSNTx` [ok] 200 740ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 1264ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.IRDMx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana
- `xstocks.price.FBINx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data
- `xstocks.mult.RNGx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana
- `xstocks.price.AMTMx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data
- `xstocks.circ.RITMx` [ok] 200 1445ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object
- `xstocks.mult.GXOx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana
- `xstocks.price.PSNx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data
- `xstocks.circ.FBINx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object
- `xstocks.circ.AMTMx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object
- `xstocks.price.PEGAx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data
- `xstocks.mult.RITMx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana
- `xstocks.mult.FBINx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana
- `xstocks.circ.PEGAx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object
- `xstocks.price.SAICx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data
- `xstocks.price.MTNx` [ok] 200 771ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data
- `xstocks.mult.AMTMx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana
- `xstocks.price.EXLSx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data
- `xstocks.circ.SAICx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object
- `xstocks.mult.OZKx` [ok] 200 1545ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana
- `xstocks.mult.PEGAx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana
- `xstocks.circ.MTNx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object
- `xstocks.mult.MTNx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana
- `xstocks.mult.SAICx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana
- `xstocks.price.Mx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/Mx/price-data
- `xstocks.price.SNDRx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data
- `xstocks.price.EPAMx` [ok] 200 663ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data
- `xstocks.price.CRUSx` [ok] 200 524ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data
- `xstocks.price.ELFx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data
- `xstocks.circ.EXLSx` [ok] 200 957ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object
- `xstocks.circ.PSNx` [ok] 200 1657ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object
- `xstocks.mult.EXLSx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana
- `xstocks.mult.PSNx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana
- `xstocks.price.VNOx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data
- `xstocks.circ.CRUSx` [ok] 200 1078ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object
- `xstocks.circ.SNDRx` [ok] 200 1299ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object
- `xstocks.mult.CRUSx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana
- `xstocks.circ.Mx` [ok] 200 1554ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object
- `xstocks.price.EXPx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data
- `xstocks.circ.EPAMx` [ok] 200 1548ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object
- `xstocks.price.VIRTx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data
- `xstocks.circ.ELFx` [ok] 200 1463ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object
- `xstocks.mult.EPAMx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana
- `xstocks.mult.ELFx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana
- `xstocks.circ.VNOx` [ok] 200 1086ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object
- `xstocks.mult.SNDRx` [ok] 200 810ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana
- `xstocks.price.HXLx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data
- `xstocks.price.CPBx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data
- `xstocks.circ.HXLx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object
- `xstocks.price.MKTXx` [ok] 200 646ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data
- `xstocks.circ.EXPx` [ok] 200 1133ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object
- `xstocks.mult.VNOx` [ok] 200 545ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana
- `xstocks.circ.MKTXx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object
- `xstocks.mult.Mx` [ok] 200 1247ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana
- `xstocks.circ.VIRTx` [ok] 200 1093ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object
- `xstocks.mult.EXPx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana
- `xstocks.price.VFCx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data
- `xstocks.price.ADTx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data
- `xstocks.circ.CPBx` [ok] 200 665ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object
- `xstocks.circ.VFCx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object
- `xstocks.price.NXSTx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data
- `xstocks.mult.VIRTx` [ok] 200 439ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana
- `xstocks.mult.VFCx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana
- `xstocks.price.BCx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/BCx/price-data
- `xstocks.mult.MKTXx` [ok] 200 903ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana
- `xstocks.price.ACIx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data
- `xstocks.circ.BCx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object
- `xstocks.circ.NXSTx` [ok] 200 694ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object
- `xstocks.circ.ADTx` [ok] 200 802ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object
- `xstocks.price.KRMNx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data
- `xstocks.mult.HXLx` [ok] 200 1481ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana
- `xstocks.circ.KRMNx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object
- `xstocks.circ.ACIx` [ok] 200 510ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object
- `xstocks.mult.NXSTx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana
- `xstocks.price.GTESx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data
- `xstocks.mult.BCx` [ok] 200 660ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana
- `xstocks.price.HRBx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data
- `xstocks.mult.KRMNx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana
- `xstocks.mult.ACIx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana
- `xstocks.mult.CPBx` [ok] 200 1725ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana
- `xstocks.price.DLBx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data
- `xstocks.mult.ADTx` [ok] 200 1006ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana
- `xstocks.price.AXSx` [ok] 200 498ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data
- `xstocks.price.RYNx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data
- `xstocks.circ.GTESx` [ok] 200 914ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object
- `xstocks.price.TFXx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data
- `xstocks.price.POOLx` [ok] 200 703ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data
- `xstocks.mult.GTESx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana
- `xstocks.circ.HRBx` [ok] 200 1256ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object
- `xstocks.mult.HRBx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana
- `xstocks.price.LWx` [ok] 200 647ms https://api.backed.fi/api/v2/public/assets/LWx/price-data
- `xstocks.circ.DLBx` [ok] 200 1426ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object
- `xstocks.circ.AXSx` [ok] 200 1502ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object
- `xstocks.price.AAONx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data
- `xstocks.circ.LWx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object
- `xstocks.circ.AAONx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object
- `xstocks.mult.LWx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana
- `xstocks.mult.DLBx` [ok] 200 629ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana
- `xstocks.price.SONx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/SONx/price-data
- `xstocks.mult.AXSx` [ok] 200 692ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana
- `xstocks.circ.SONx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object
- `xstocks.mult.AAONx` [ok] 200 752ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana
- `xstocks.price.TTDx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data
- `xstocks.price.INGMx` [ok] 200 549ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data
- `xstocks.circ.POOLx` [ok] 200 2014ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object
- `xstocks.price.HRx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/HRx/price-data
- `xstocks.circ.INGMx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object
- `xstocks.circ.TTDx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object
- `xstocks.circ.HRx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object
- `xstocks.mult.POOLx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana
- `xstocks.mult.HRx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana
- `xstocks.price.CLFx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data
- `xstocks.price.SHCx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CLFx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object
- `xstocks.circ.SHCx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object
- `xstocks.mult.SONx` [ok] 200 1411ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana
- `xstocks.circ.TFXx` [ok] 200 3332ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object
- `xstocks.mult.CLFx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana
- `xstocks.mult.SHCx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana
- `xstocks.mult.TTDx` [ok] 200 1218ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana
- `xstocks.mult.TFXx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana
- `xstocks.price.MSMx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data
- `xstocks.price.STWDx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data
- `xstocks.mult.INGMx` [ok] 200 1480ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana
- `xstocks.price.OMFx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data
- `xstocks.circ.RYNx` [ok] 200 4007ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object
- `xstocks.circ.STWDx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object
- `xstocks.price.CZRx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data
- `xstocks.price.CHEx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data
- `xstocks.mult.STWDx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana
- `xstocks.circ.OMFx` [ok] 200 663ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object
- `xstocks.circ.CZRx` [ok] 200 554ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object
- `xstocks.price.Gx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/Gx/price-data
- `xstocks.mult.CZRx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana
- `xstocks.mult.OMFx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana
- `xstocks.circ.Gx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object
- `xstocks.price.CROXx` [ok] 200 1118ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data
- `xstocks.circ.CROXx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object
- `xstocks.price.MTGx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data
- `xstocks.mult.RYNx` [ok] 200 1257ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana
- `xstocks.price.ALGMx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data
- `xstocks.circ.MTGx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object
- `xstocks.mult.Gx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana
- `xstocks.price.RLIx` [ok] 200 2915ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data
- `xstocks.circ.CHEx` [ok] 200 1699ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object
- `xstocks.circ.ALGMx` [ok] 200 519ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object
- `xstocks.circ.RLIx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object
- `xstocks.mult.CROXx` [ok] 200 726ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana
- `xstocks.price.MTDRx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data
- `xstocks.price.INGRx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data
- `xstocks.circ.MTDRx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object
- `xstocks.price.BEPCx` [ok] 200 766ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data
- `xstocks.mult.CHEx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana
- `xstocks.mult.ALGMx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana
- `xstocks.mult.MTGx` [ok] 200 823ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana
- `xstocks.circ.MSMx` [ok] 200 2341ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object
- `xstocks.circ.INGRx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object
- `xstocks.price.BYDx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data
- `xstocks.circ.BEPCx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object
- `xstocks.mult.INGRx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana
- `xstocks.circ.BYDx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object
- `xstocks.mult.MSMx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana
- `xstocks.mult.MTDRx` [ok] 200 475ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana
- `xstocks.price.LYFTx` [ok] 200 487ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data
- `xstocks.mult.BEPCx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana
- `xstocks.mult.RLIx` [ok] 200 800ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana
- `xstocks.price.FNBx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data
- `xstocks.price.STAGx` [ok] 200 537ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data
- `xstocks.circ.STAGx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object
- `xstocks.circ.FNBx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object
- `xstocks.circ.LYFTx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object
- `xstocks.mult.STAGx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana
- `xstocks.price.CACCx` [ok] 200 601ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data
- `xstocks.mult.FNBx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana
- `xstocks.circ.CACCx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object
- `xstocks.mult.BYDx` [ok] 200 1038ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana
- `xstocks.price.MBGLx` [ok] 200 1115ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data
- `xstocks.mult.CACCx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana
- `xstocks.circ.MBGLx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object
- `xstocks.mult.LYFTx` [ok] 200 921ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana
- `xstocks.mult.MBGLx` [ok] 200 1405ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 2700ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 202ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.XRXx` [ok] 200 115ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.QUBTx` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.FLNCx` [ok] 200 111ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.BETRx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.WGSx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.WYFIx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.AIx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.INDIx` [ok] 200 109ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jito.tip_floor` [ok] 200 101ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 341ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 130ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 92ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 96ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 100ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 80ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 193ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
