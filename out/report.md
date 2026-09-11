# Borealis — Solana ecosystem report

**Generated** 2026-09-11T17:23:54Z · 2026-09-11 10:23:54 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-11T17:23:43Z · **RPC health** `ok`
**Health score** 93 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +2.23%; DEX 24h $2.92B · 1d -3% · vs-7d-ago +19%; slot 318 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +23.60%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 967,396.00 is +22.0% vs 30d median 793,088.50 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 446,212,833 |
| Block height | 424,255,900 |
| Block time | 2026-09-11T17:23:43Z |
| Epoch | 1,032 (90.01% · slot 388,834/432,000) |
| Mean TPS (last ~3,600s) | 4,363.9 |
| Mean non-vote TPS | 2,249.3 |
| Median TPS (same window) | 4,372.6 |
| Mean slot time | 317.9 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 547,453,040,479 |
| Circulating supply | 586,537,254 SOL |
| Total supply | 633,829,819 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 14 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 437,366,153 SOL |
| Delinquent stake | 1,822,059.58 SOL (0.415%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.31% / 35.63% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 3.99% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.32M SOL | 3.73% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.52M SOL | 2.86% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.38M SOL | 2.60% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.19% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.28M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.34M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.88M SOL | 1.57% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.55M SOL | 1.50% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.95M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `pSo1KZXg…` · 1.64M SOL · commission 4% · lag 119258 slots
- `EBk678aQ…` · 95.16K SOL · commission 5% · lag 124965 slots
- `EWARp8Sy…` · 35.14K SOL · commission 5% · lag 71479 slots
- `mrgn4atx…` · 19.89K SOL · commission 0% · lag 73277 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 358676 slots
- `inWVrrYJ…` · 8.46K SOL · commission 0% · lag 513736 slots
- `xLabscif…` · 3.36K SOL · commission 5% · lag 2424460 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 2246911 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 417671 slots
- `4GEEKSwu…` · 326.50 SOL · commission 5% · lag 403221 slots
- `stacheBm…` · 3.00 SOL · commission 5% · lag 16677150 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 446212833 slots

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
| **In-protocol fees 24h** | **$1.01M** (9,683.4 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-09 |
| **Solana REV** | **11,493.1 SOL** / **$1.20M** | MEASURED UTC calendar day 2026-09-09: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-09 · UTC day 2026-09-09 · SOL-USD date 2026-09-09 |
| Jito tip-floor run-rate (NOT REV) | $38.20K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 38203 USD; at p95 floor → 1418396 USD. |
| Protocol fees 24h | $14.61M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9965 |
| p90 / p99 | 0.000012 / 0.000305 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $102.12 | coingecko.simple_price |
| 24h change | +2.23% | coingecko.simple_price |
| Market cap | $59.90B | coingecko.simple_price |
| 24h volume | $4.20B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.88B |
| TVL 1d / 7d / 30d | +0.38% / -0.89% / +20.60% |
| DEX volume 24h | $2.92B · 1d -2.61% · vs-7d-ago +18.80% |
| 7d DEX volume | $18.00B · +15.32% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.61M |
| Fees 1d / 7d | -6.98% / +23.60% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $468.14M | +37.30% |
| Raydium AMM | $456.93M | +5.01% |
| BisonFi | $395.81M | -1.73% |
| HumidiFi | $322.67M | +12.96% |
| Tessera V | $232.00M | -6.46% |
| Meteora DLMM | $220.43M | -31.60% |
| Orca DEX | $201.48M | +18.84% |
| Manifest Trade | $141.51M | -6.88% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.58B | +3.24% | +2.93% |
| Kamino Lend | Lending | $1.35B | +2.48% | +3.32% |
| Raydium AMM | Dexs | $1.11B | -0.83% | -0.67% |
| Jupiter Lend | Lending | $1.09B | +1.96% | +1.19% |
| Binance Staked SOL | Liquid Staking | $1.07B | +2.73% | +1.56% |
| Jito Liquid Staking | Liquid Staking | $1.06B | +3.65% | +3.10% |
| BlackRock BUIDL | RWA | $992.60M | -0.68% | -0.62% |
| Jupiter Perpetual Exchange | Derivatives | $759.53M | +3.17% | +1.46% |
| Jupiter Staked SOL | Liquid Staking | $532.75M | +2.79% | +1.68% |
| Marinade Native | Staking Pool | $392.38M | +1.99% | -4.09% |

## Stablecoins

Solana circulating pegged-USD: **$16.13B**
(1d -1.50% · 7d -1.62%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.20B | +0.98% |
| USDT · Tether | $2.67B | -3.25% |
| USDGO · USDGO | $1.38B | +0.73% |
| USD1 · World Liberty Financial USD | $1.29B | +0.42% |
| BUIDL · BlackRock USD | $992.60M | +0.04% |
| PYUSD · PayPal USD | $693.45M | -8.36% |
| USDG · Global Dollar | $603.29M | +0.26% |
| USDe · Ethena USDe | $536.46M | +0.14% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $107.46M (lower bound, not a census).
24h volume $119.31M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.90B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.60M
- **OnRe** (RWA) — $294.72M
- **Ondo Yield Assets** (RWA) — $180.05M
- **Huma Finance V2** (RWA) — $170.16M
- **Hastra** (RWA) — $150.67M
- **Plume Vaults** (RWA) — $27.21M
- **Ondo Global Markets** (RWA) — $25.30M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.37M

## Daily active addresses

967,396 (Allium, as of 2026-09-10). Provider range 488,212–1,040,024. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [The Privacy Show w/ @catmcgee https://x.com/i/broadcasts/1DxLdZRdXeRxm](https://x.com/solana/status/2098457925404795298) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 17:05:31 GMT
- [New episode of The Privacy Show today @ 1 PM ET.

@catmcgee sits down with @Jamie_Alethieum and @JonShapeShift to talk all things privacy.](https://x.com/solana/status/2098440785913946621) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 15:57:25 GMT
- [$WEN is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2098423204117410226) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 14:47:33 GMT
- [Wendy's ($WEN) is one of the largest fast food chains in the world, with over 7,000 restaurants across roughly 30 countries.

Verify the address on @tokens:
https://tokens.xyz/wendy-s?solana=WENAZ2WyPbmgvUcKfQ8hyMDfBQP9bZ65hsZ5KTFrRGZ](https://x.com/solana/status/2098423201806385330) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 14:47:32 GMT
- [BREAKING: $WEN is live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2098423198815813857) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 14:47:32 GMT
- [Pinned: STOCKLANA

The stock market is open for building.  

One week to build something innovative with stocks on Solana. $100K in prizes.

Sept 11 - 18, opening bell to closing bell:
https://hackathons.solana.com/hackathons/stocklana](https://x.com/solana/status/2098403597004263760) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 13:29:38 GMT
- [RT by @solana: BREAKING: Tokenized equity holders on @Solana crossed 727,000 addresses, up more than 300,000 in under two weeks.](https://x.com/tokens/status/2098372990715257230) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 11:28:01 GMT
- [RT by @solana: solana is back as the biggest route for the trading terminal volume](https://x.com/Adam_Tehc/status/2098308450157514956) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 07:11:33 GMT
- [RT by @anza_xyz: Yesterday total trades:

NASDAQ: 60,091,499
Solana: 32,460,600

Less than 2x to go 🤯](https://x.com/vibhu/status/2098446478951772539) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 16:20:02 GMT
- [alpenGO ⛰️✅](https://x.com/anza_xyz/status/2098443881058803737) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 16:09:43 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [The Privacy Show w/ @catmcgee https://x.com/i/broadcasts/1DxLdZRdXeRxm](https://x.com/solana/status/2098457925404795298) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 17:05:31 GMT
- [New episode of The Privacy Show today @ 1 PM ET.

@catmcgee sits down with @Jamie_Alethieum and @JonShapeShift to talk all things privacy.](https://x.com/solana/status/2098440785913946621) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 15:57:25 GMT
- [$WEN is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2098423204117410226) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 14:47:33 GMT
- [Wendy's ($WEN) is one of the largest fast food chains in the world, with over 7,000 restaurants across roughly 30 countries.

Verify the address on @tokens:
https://tokens.xyz/wendy-s?solana=WENAZ2WyPbmgvUcKfQ8hyMDfBQP9bZ65hsZ5KTFrRGZ](https://x.com/solana/status/2098423201806385330) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 14:47:32 GMT
- [BREAKING: $WEN is live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2098423198815813857) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 14:47:32 GMT
- [Pinned: STOCKLANA

The stock market is open for building.  

One week to build something innovative with stocks on Solana. $100K in prizes.

Sept 11 - 18, opening bell to closing bell:
https://hackathons.solana.com/hackathons/stocklana](https://x.com/solana/status/2098403597004263760) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 13:29:38 GMT
- [RT by @solana: BREAKING: Tokenized equity holders on @Solana crossed 727,000 addresses, up more than 300,000 in under two weeks.](https://x.com/tokens/status/2098372990715257230) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 11:28:01 GMT
- [RT by @solana: solana is back as the biggest route for the trading terminal volume](https://x.com/Adam_Tehc/status/2098308450157514956) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 07:11:33 GMT
- [RT by @anza_xyz: Yesterday total trades:

NASDAQ: 60,091,499
Solana: 32,460,600

Less than 2x to go 🤯](https://x.com/vibhu/status/2098446478951772539) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 16:20:02 GMT
- [alpenGO ⛰️✅](https://x.com/anza_xyz/status/2098443881058803737) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 16:09:43 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-11 (2026-09-11 10:23:54 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~318 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `on-chain` — On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending.
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

- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 232ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 204ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 158ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 147ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 161ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5934ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 281ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 157ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 157ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 269ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 76ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 797ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 3611ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 199ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 202ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 105ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 1019ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 462ms https://solana.com/data
- `solana.com.databricks` [ok] 200 169ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 490ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 158ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 189ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 111ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 404ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 839ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 266ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 227ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 293ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 3501ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1208ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1921ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 11416ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 117ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 146ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 130ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 677ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 698ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 758ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 777ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1004ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 948ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 722ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 887ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 885ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 962ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 917ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 631ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 651ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 950ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1807ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1517ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1548ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2698ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1236ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1296ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1173ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1217ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.XRXx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.INDIx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.FLNCx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.WRLDx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.SPYx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.QQQx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.WGSx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.COINx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.XRXx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.PCTx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.mult.COINx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.QUBTx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.METCx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.WYFIx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.INDIx` [ok] 200 1043ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 1185ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 1209ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 1023ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.WGSx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.SCIx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.circ.BETRx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.DRSx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.circ.PCTx` [ok] 200 1130ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.BETRx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.SAILx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.circ.METCx` [ok] 200 1223ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 1303ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.BSYx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.price.MPx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.price.DVAx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.price.GSATx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.mult.METCx` [ok] 200 519ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.DVAx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.circ.GSATx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.circ.SCIx` [ok] 200 1173ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.price.DCIx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.mult.SCIx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.mult.GSATx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.mult.DVAx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.circ.SAILx` [ok] 200 1098ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.circ.MPx` [ok] 200 709ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.price.RYANx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.price.BXPx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.price.GDDYx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.mult.SAILx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.circ.DRSx` [ok] 200 1510ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.mult.MPx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.mult.DCIx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.circ.GDDYx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.circ.BXPx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.price.FRHCx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.mult.DRSx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.WMSx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.mult.GDDYx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.price.DYx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.mult.BXPx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.circ.FRHCx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.price.AMx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.WMSx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.price.FDSx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.price.ALSNx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.circ.DYx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.WMSx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.circ.ALSNx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.circ.FDSx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.price.SMTCx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.mult.AMx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.mult.FDSx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.price.AXSMx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.mult.ALSNx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.price.SFx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.price.EGPx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.circ.AXSMx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.circ.SMTCx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.circ.SFx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.price.TTMIx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.circ.RYANx` [ok] 200 1429ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.circ.EGPx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.price.BPOPx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.mult.SMTCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.circ.TTMIx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.price.AEISx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.circ.BPOPx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.mult.EGPx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.mult.TTMIx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.mult.RYANx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.circ.BSYx` [ok] 200 2683ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.circ.AEISx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.price.DPZx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.price.HRLx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.price.KTOSx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.mult.BSYx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.mult.BPOPx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.mult.AXSMx` [ok] 200 808ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.circ.KTOSx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.circ.DPZx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.mult.SFx` [ok] 200 845ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.mult.AEISx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.price.SEICx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.price.PAGx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.price.HIIx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.price.GFLx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.circ.SEICx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.price.EHCx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.circ.HIIx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.mult.KTOSx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.circ.GFLx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.SEICx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.mult.DPZx` [ok] 200 488ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.mult.HIIx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.mult.GFLx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.price.MGMx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.price.HALOx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.price.DOCUx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.price.ARx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.price.WTRGx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.circ.MGMx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.circ.HALOx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.circ.ARx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.circ.DOCUx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.circ.WTRGx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.circ.HRLx` [ok] 200 1272ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.mult.MGMx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.mult.DOCUx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.mult.HALOx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.mult.HRLx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.AFGx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.price.HUBSx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.circ.PAGx` [ok] 200 1174ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.mult.WTRGx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.price.AMKRx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.circ.HUBSx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.mult.PAGx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.price.JKHYx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.circ.AMKRx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.price.IESCx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.circ.JKHYx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.price.GMEDx` [ok] 200 528ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.mult.HUBSx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.circ.IESCx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.mult.JKHYx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.circ.GMEDx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.mult.AMKRx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.mult.AFGx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.price.OCx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.price.CRx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.price.BMRNx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.mult.IESCx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.JEFx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.mult.ARx` [ok] 200 1387ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.circ.CRx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.circ.BMRNx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.price.AMHx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.JEFx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.circ.EHCx` [ok] 200 2069ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.mult.GMEDx` [ok] 200 496ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.price.FIVEx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.circ.OCx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.mult.CRx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.mult.BMRNx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.circ.AMHx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.mult.JEFx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.price.VNOMx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.mult.EHCx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.circ.FIVEx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.price.UHALx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.circ.VNOMx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.price.AHRx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.price.ITx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.mult.AMHx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.mult.OCx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.circ.AHRx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.mult.FIVEx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.circ.ITx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.price.IVZx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.mult.VNOMx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.mult.AHRx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.circ.IVZx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.price.STRLx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.price.NWSAx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.mult.ITx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.price.MDGLx` [ok] 200 974ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.circ.STRLx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.mult.IVZx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.circ.NWSAx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.price.Hx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.price.ARWRx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.price.CORTx` [ok] 200 764ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.mult.STRLx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.mult.NWSAx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.price.AURx` [ok] 200 558ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.circ.ARWRx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.price.GWREx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.circ.CORTx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.circ.MDGLx` [ok] 200 506ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.circ.UHALx` [ok] 200 1192ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.price.NWSx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.circ.Hx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.mult.MDGLx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.price.MANHx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.mult.Hx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.mult.AURx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.price.CACIx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.mult.NWSx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.mult.CORTx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.BAXx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.BAXx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.UHALx` [ok] 200 739ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.circ.MANHx` [ok] 200 1148ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.circ.GWREx` [ok] 200 1600ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.circ.CACIx` [ok] 200 1417ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.mult.MANHx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.CACIx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 645ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 223ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INDIx` [ok] 200 127ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 121ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 128ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.FLNCx` [ok] 200 143ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.BETRx` [ok] 200 117ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.XRXx` [ok] 200 130ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.PCTx` [ok] 200 152ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.WGSx` [ok] 200 107ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jito.tip_floor` [ok] 200 297ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 248ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 120ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 171ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 170ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 120ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 132ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 676ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
