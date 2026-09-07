# Borealis — Solana ecosystem report

**Generated** 2026-09-07T17:23:49Z · 2026-09-07 10:23:49 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-07T17:23:39Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -1.96%; DEX 24h $2.90B · 1d +56% · vs-7d-ago +51%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +44.97%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +55.76%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +50.52%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 445,121,219 |
| Block height | 423,165,442 |
| Block time | 2026-09-07T17:23:39Z |
| Epoch | 1,030 (37.32% · slot 161,224/432,000) |
| Mean TPS (last ~3,600s) | 3,748.8 |
| Mean non-vote TPS | 1,626.0 |
| Median TPS (same window) | 3,735.7 |
| Mean slot time | 316.1 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 546,071,533,180 |
| Circulating supply | 586,165,922 SOL |
| Total supply | 633,643,201 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 674 |
| Delinquent | 14 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,023,081 SOL |
| Delinquent stake | 454,906.80 SOL (0.104%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.22% / 35.49% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 3.97% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.34M SOL | 3.72% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.52M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.40M SOL | 2.60% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.56M SOL | 2.18% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.18M SOL | 2.09% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.38M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.86M SOL | 1.56% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.60M SOL | 1.50% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.39% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.39% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.97M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.64M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.85M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `7RtC1Qgi…` · 276.02K SOL · commission 8% · lag 2036 slots
- `bxrAptB5…` · 129.36K SOL · commission 5% · lag 31728 slots
- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 74189 slots
- `xLabscif…` · 8.89K SOL · commission 5% · lag 1332846 slots
- `prt1st4R…` · 7.04K SOL · commission 5% · lag 1634277 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 1772496 slots
- `5ZjxMYBb…` · 3.79K SOL · commission 0% · lag 1155297 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 582028 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 1682580 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 2320868 slots
- `HFTcVVrX…` · 148.42 SOL · commission 100% · lag 2320762 slots
- `As9NxA9b…` · 46.58 SOL · commission 100% · lag 2320885 slots

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
| **In-protocol fees 24h** | **$658.16K** (6,158.9 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-06 |
| **Solana REV** | **7,251.8 SOL** / **$774.94K** | MEASURED UTC calendar day 2026-09-06: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-06 · UTC day 2026-09-06 · SOL-USD date 2026-09-06 |
| Jito tip-floor run-rate (NOT REV) | $22.44K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 22445 USD; at p95 floor → 845908 USD. |
| Protocol fees 24h | $14.66M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9997 |
| p90 / p99 | 0.000012 / 0.000106 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $104.08 | coingecko.simple_price |
| 24h change | -1.96% | coingecko.simple_price |
| Market cap | $61.01B | coingecko.simple_price |
| 24h volume | $3.31B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.93B |
| TVL 1d / 7d / 30d | +0.38% / +2.45% / +24.85% |
| DEX volume 24h | $2.90B · 1d +55.76% · vs-7d-ago +50.52% |
| 7d DEX volume | $16.07B · -11.56% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.66M |
| Fees 1d / 7d | +44.97% / +18.04% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $677.89M | -2.21% |
| Raydium AMM | $317.35M | +186.12% |
| Orca DEX | $287.93M | +127.83% |
| BisonFi | $241.45M | +32.54% |
| Meteora DLMM | $223.09M | +82.29% |
| Tessera V | $206.39M | +139.77% |
| Manifest Trade | $146.69M | +25.18% |
| HumidiFi | $143.21M | +123.80% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.60B | -1.99% | +2.17% |
| Kamino Lend | Lending | $1.33B | -1.15% | +6.61% |
| Raydium AMM | Dexs | $1.15B | +0.27% | +3.61% |
| Jupiter Lend | Lending | $1.09B | -2.66% | +2.58% |
| Binance Staked SOL | Liquid Staking | $1.09B | -0.77% | +2.86% |
| Jito Liquid Staking | Liquid Staking | $1.07B | -1.91% | +3.88% |
| BlackRock BUIDL | RWA | $977.90M | -0.00% | +0.58% |
| Jupiter Perpetual Exchange | Derivatives | $756.00M | -1.10% | -0.25% |
| Jupiter Staked SOL | Liquid Staking | $541.02M | -1.87% | +2.00% |
| xStocks | RWA | $447.07M | -0.69% | +2.74% |

## Stablecoins

Solana circulating pegged-USD: **$16.29B**
(1d +0.34% · 7d +4.87%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.31B | +0.06% |
| USDT · Tether | $2.77B | -0.00% |
| USDGO · USDGO | $1.37B | +1.11% |
| USD1 · World Liberty Financial USD | $1.26B | +0.16% |
| BUIDL · BlackRock USD | $977.90M | 0.00% |
| PYUSD · PayPal USD | $733.14M | -2.57% |
| USDG · Global Dollar | $578.41M | -0.67% |
| USDe · Ethena USDe | $535.10M | -0.22% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 60 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 60 · priced-subset mcap $237.39K (lower bound, not a census).
24h volume $70.02M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $447.07M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 60 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.36B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $977.90M
- **xStocks** (RWA) — $447.07M
- **OnRe** (RWA) — $302.40M
- **Huma Finance V2** (RWA) — $185.01M
- **Ondo Yield Assets** (RWA) — $179.59M
- **Hastra** (RWA) — $154.65M
- **Ondo Global Markets** (RWA) — $26.09M
- **Plume Vaults** (RWA) — $24.04M

## Daily active addresses

858,456 (Allium, as of 2026-09-06). Provider range 418,160–858,456. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [.@kamino is now available as a source of liquidity for onchain yield for @veda_labs 

https://x.com/veda_labs/status/2096992133324611869](https://x.com/solana/status/2097009524469022775) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 17:10:05 GMT
- [$DOGE is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more

Verify the address on @tokens:
https://tokens.xyz/doge?solana=DoGEV7LASBkQbibMc5k5vKnTZoMg423GpJ5QtJEGfm7R](https://x.com/solana/status/2096977197324202253) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 15:01:38 GMT
- [BREAKING: $DOGE is live on Solana via @sunrise. Much wow.](https://x.com/solana/status/2096977194627326097) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 15:01:37 GMT
- [RT by @solana: $DOGE is now listed on @Solana via Sunrise.](https://x.com/sunrise/status/2096976813113389215) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 15:00:06 GMT
- [RT by @solana: Over $150 million of tokenized equity volume on @solana yesterday.

More than $100 million @Raydium. 

Stonk szn on Solana](https://x.com/mst1287/status/2096976333989650856) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 14:58:12 GMT
- [RT by @solana: IT’S HAPPENING.

INDIES ON SOLANA SEASON 2 🔥](https://x.com/indiesonsolana/status/2096972664829292845) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 14:43:37 GMT
- [The bag stays on](https://x.com/solana/status/2096966455992721784) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 14:18:57 GMT
- [Join us:

https://luma.com/breakpoint2026](https://x.com/solana/status/2096954116035740018) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 13:29:55 GMT
- [RT by @anza_xyz: 200ms
8k txs (40k TPS)
300M CUs (1.5B CUPS)
5.5k shreds (27.5k SPS)

this is the block 🔳 Agave can handle](https://x.com/bw_solana/status/2096250616351965576) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 05 Sep 2026 14:54:28 GMT
- [RT by @anza_xyz: more users
→ more activity
→ problems exposed
→ IBRL
→ more capacity
→ more resilience
→ better products
→ more users

usage & execution is the moat](https://x.com/bw_solana/status/2095876304805740662) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 04 Sep 2026 14:07:05 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [.@kamino is now available as a source of liquidity for onchain yield for @veda_labs 

https://x.com/veda_labs/status/2096992133324611869](https://x.com/solana/status/2097009524469022775) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 17:10:05 GMT
- [$DOGE is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more

Verify the address on @tokens:
https://tokens.xyz/doge?solana=DoGEV7LASBkQbibMc5k5vKnTZoMg423GpJ5QtJEGfm7R](https://x.com/solana/status/2096977197324202253) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 15:01:38 GMT
- [BREAKING: $DOGE is live on Solana via @sunrise. Much wow.](https://x.com/solana/status/2096977194627326097) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 15:01:37 GMT
- [RT by @solana: $DOGE is now listed on @Solana via Sunrise.](https://x.com/sunrise/status/2096976813113389215) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 15:00:06 GMT
- [RT by @solana: Over $150 million of tokenized equity volume on @solana yesterday.

More than $100 million @Raydium. 

Stonk szn on Solana](https://x.com/mst1287/status/2096976333989650856) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 14:58:12 GMT
- [RT by @solana: IT’S HAPPENING.

INDIES ON SOLANA SEASON 2 🔥](https://x.com/indiesonsolana/status/2096972664829292845) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 14:43:37 GMT
- [The bag stays on](https://x.com/solana/status/2096966455992721784) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 14:18:57 GMT
- [Join us:

https://luma.com/breakpoint2026](https://x.com/solana/status/2096954116035740018) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 13:29:55 GMT
- [RT by @anza_xyz: 200ms
8k txs (40k TPS)
300M CUs (1.5B CUPS)
5.5k shreds (27.5k SPS)

this is the block 🔳 Agave can handle](https://x.com/bw_solana/status/2096250616351965576) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 05 Sep 2026 14:54:28 GMT
- [RT by @anza_xyz: more users
→ more activity
→ problems exposed
→ IBRL
→ more capacity
→ more resilience
→ better products
→ more users

usage & execution is the moat](https://x.com/bw_solana/status/2095876304805740662) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 04 Sep 2026 14:07:05 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-07 (2026-09-07 10:23:49 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~316 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~316 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **xStocks** — priced up to 80 of 726 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 693ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 672ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 668ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 763ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 675ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7217ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1372ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 109ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 60ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 151ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 39ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 49ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 62ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 115ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 74ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 73ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 103ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 346ms https://solana.com/data
- `solana.com.databricks` [ok] 200 82ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 254ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 138ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 92ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 73ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 231ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 1830ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 206ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 102ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 123ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1056ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1590ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1768ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 259ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 183ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 688ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 688ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2628ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2615ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2812ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2655ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2728ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2944ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2950ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3009ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2758ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3226ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3024ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2621ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2599ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2927ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2147ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2377ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 6739ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1568ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1666ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1811ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 6956ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 549ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [FAIL]  12029ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GOOGLx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MSFTx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AAPLx` [FAIL]  12029ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SPYx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METAx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/METAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AMZNx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.NVDAx` [FAIL]  12033ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AMZNx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 865ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 1080ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 1391ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 1628ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 1406ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 2177ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.QQQx` [FAIL]  12031ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DRAMx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.COINx` [FAIL]  12034ms https://api.backed.fi/api/v2/public/assets/COINx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.QQQx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.MVLLx` [FAIL]  12031ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MVLLx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.MUUx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AXTIx` [FAIL]  12035ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MVLLx` [ok] 200 989ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 1580ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.DJTx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AXTIx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.KORUx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.KORUx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.mult.MUUx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.SHEINx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.DRAMx` [ok] 200 3114ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 1485ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 1815ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.mult.SHEINx` [ok] 200 657ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.price.NWGx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.mult.DRAMx` [ok] 200 1272ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.NWGx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 4675ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.SUOPTx` [ok] 200 958ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.DJTx` [ok] 200 2332ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 650ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.NWGx` [ok] 200 3350ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 1866ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 4559ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.MMGx` [ok] 200 3785ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 2124ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.BANKCx` [ok] 200 1943ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.TNGYIx` [ok] 200 2508ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.JDLOGx` [ok] 200 548ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 5864ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 1420ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 1291ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 1404ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 1922ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 2332ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.INTWx` [FAIL]  12018ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SOXSx` [FAIL]  12030ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HAIDLx` [ok] 200 818ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.CTINSx` [ok] 200 3260ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.SNXXx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.HAIDLx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.SOXSx` [ok] 200 734ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.SOXSx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 431ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.SNXXx` [ok] 200 1340ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 3687ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.SNXXx` [ok] 200 881ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 3090ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 2251ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 2629ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.CRESBx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.INTWx` [ok] 200 3811ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 2214ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.KUNLx` [ok] 200 7914ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.SMOIHx` [ok] 200 3177ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 2170ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 6433ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.JTGEXx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 3205ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 3005ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 964ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 1611ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 731ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 978ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.CMENDx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.MIXUx` [ok] 200 580ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 887ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 1239ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.CRESMx` [ok] 200 1442ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.CMENDx` [ok] 200 1427ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 1538ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 1253ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 5376ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.SNDSCx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 2465ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.MIXUx` [ok] 200 3449ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 6934ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 1713ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.mult.CSPCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 1658ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [ok] 200 1861ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 843ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 1686ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 580ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 1426ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.CLONPx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.PRADx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 991ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.SINOTx` [ok] 200 1420ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.WHGROx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 678ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.CRESPx` [ok] 200 3144ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.PRADx` [ok] 200 700ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.SINOTx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 392ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.CRESPx` [ok] 200 783ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 871ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 524ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 1750ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.circ.CMERPx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.PWAHLx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CTPCAx` [ok] 200 1604ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 1304ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 757ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 939ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.CKAHx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 7710ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.mult.SINOx` [ok] 200 2560ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 1353ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.CKINFx` [ok] 200 719ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.CKINFx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 857ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.GENTEx` [ok] 200 2771ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 1302ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 801ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.SITCx` [ok] 200 1775ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 2661ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 1723ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.price.NONGx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.WUXIBx` [ok] 200 4086ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.COVELx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 1019ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 3296ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 2125ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 1822ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 1236ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.COVELx` [ok] 200 998ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 1426ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 1111ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.MTRCPx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.CHONGx` [ok] 200 744ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 1772ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 1268ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 851ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 603ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 786ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.price.CKHUTx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.HNDLDx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 1456ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 1565ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 2739ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.COSCx` [ok] 200 1136ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 2060ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 1497ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 1085ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 618ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 1694ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 8010ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.PICCx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 2245ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1759ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 152ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.SHEINx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.MEITx` [ok] 200 70ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.KUAIx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.MIXUx` [ok] 200 69ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.BANKCx` [ok] 200 58ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.HRZRBx` [ok] 200 53ms https://lite-api.jup.ag/tokens/v2/search?query=HRZRBx
- `jup.tokens.search.SUOPTx` [ok] 200 58ms https://lite-api.jup.ag/tokens/v2/search?query=SUOPTx
- `jito.tip_floor` [ok] 200 121ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 265ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 75ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 665ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 750ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 757ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 677ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 105ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
