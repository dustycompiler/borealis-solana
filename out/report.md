# Borealis — Solana ecosystem report

**Generated** 2026-09-05T10:34:45Z · 2026-09-05 03:34:45 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-05T10:34:34Z · **RPC health** `ok`
**Health score** 95 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -1.21%; DEX 24h $1.85B · 1d -25% · vs-7d-ago -29%; slot 314 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -24.89%. (threshold: `|1d %| >= 8`)
- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -19.31%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -28.69%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -39.50%. (threshold: `|7d %| >= 20`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -1.21%, DeFiLlama TVL 1d -0.96%, DEX 1d -24.89%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **INFO · Daily active addresses vs 30d median** — Current 894,816.00 is +26.2% vs 30d median 709,223.50 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 444,497,646 |
| Block height | 422,542,273 |
| Block time | 2026-09-05T10:34:34Z |
| Epoch | 1,028 (92.97% · slot 401,646/432,000) |
| Mean TPS (last ~3,600s) | 3,083.9 |
| Mean non-vote TPS | 951.0 |
| Median TPS (same window) | 3,071.3 |
| Mean slot time | 314.3 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 545,358,952,990 |
| Circulating supply | 585,359,602 SOL |
| Total supply | 633,454,628 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 677 |
| Delinquent | 18 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 436,757,852 SOL |
| Delinquent stake | 141,013.38 SOL (0.032%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 79 |
| Top 10 / 20 stake share | 24.39% / 35.71% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.39M SOL | 3.98% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.32M SOL | 3.74% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.46M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.38M SOL | 2.61% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.19% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.28M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.38M SOL | 1.69% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.13M SOL | 1.63% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.84M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `xLabscif…` · 78.25K SOL · commission 5% · lag 709273 slots
- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 33240 slots
- `prt1st4R…` · 19.80K SOL · commission 5% · lag 1010704 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 1148923 slots
- `5ZjxMYBb…` · 4.06K SOL · commission 0% · lag 531724 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1711525 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 321089 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 1059007 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 2513892 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1697295 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1738809 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 1697189 slots

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
| **In-protocol fees 24h** | **$581.35K** (5,727.6 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-03 |
| **Solana REV** | **6,747.5 SOL** / **$684.86K** | MEASURED UTC calendar day 2026-09-03: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-03 · UTC day 2026-09-03 · SOL-USD date 2026-09-03 |
| Jito tip-floor run-rate (NOT REV) | $24.87K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 24870 USD; at p95 floor → 191146 USD. |
| Protocol fees 24h | $9.54M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9973 |
| p90 / p99 | 0.000008 / 0.000101 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $102.65 | coingecko.simple_price |
| 24h change | -1.21% | coingecko.simple_price |
| Market cap | $60.08B | coingecko.simple_price |
| 24h volume | $2.87B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.87B |
| TVL 1d / 7d / 30d | -0.96% / -0.12% / +22.00% |
| DEX volume 24h | $1.85B · 1d -24.89% · vs-7d-ago -28.69% |
| 7d DEX volume | $14.32B · -32.59% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $9.54M |
| Fees 1d / 7d | -19.31% / -39.50% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $310.67M | -62.96% |
| BisonFi | $232.51M | 0.00% |
| Orca DEX | $210.00M | -26.48% |
| Meteora DLMM | $180.66M | -3.13% |
| Manifest Trade | $145.24M | -18.15% |
| Raydium AMM | $128.66M | -16.35% |
| Jupiterz | $99.63M | 0.00% |
| Scorch | $77.86M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.57B | -0.83% | -0.60% |
| Kamino Lend | Lending | $1.32B | -0.53% | +6.06% |
| Raydium AMM | Dexs | $1.10B | -1.25% | -1.60% |
| Jupiter Lend | Lending | $1.10B | +0.43% | +0.95% |
| Binance Staked SOL | Liquid Staking | $1.07B | -0.76% | +0.14% |
| Jito Liquid Staking | Liquid Staking | $1.05B | -0.05% | +1.10% |
| BlackRock BUIDL | RWA | $977.90M | +1.04% | +0.60% |
| Jupiter Perpetual Exchange | Derivatives | $753.98M | -1.69% | -1.51% |
| Jupiter Staked SOL | Liquid Staking | $531.15M | -0.72% | -1.17% |
| xStocks | RWA | $448.05M | -2.59% | +3.59% |

## Stablecoins

Solana circulating pegged-USD: **$16.27B**
(1d -0.25% · 7d +2.58%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.31B | +2.73% |
| USDT · Tether | $2.77B | -6.11% |
| USDGO · USDGO | $1.36B | +3.04% |
| USD1 · World Liberty Financial USD | $1.26B | +2.88% |
| BUIDL · BlackRock USD | $977.90M | +4.27% |
| PYUSD · PayPal USD | $718.74M | -16.42% |
| USDG · Global Dollar | $589.62M | +4.89% |
| USDe · Ethena USDe | $533.27M | -0.52% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 60 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 60 · priced-subset mcap $283.33K (lower bound, not a census).
24h volume $24.66M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $448.05M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 60 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.36B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $977.90M
- **xStocks** (RWA) — $448.05M
- **OnRe** (RWA) — $298.86M
- **Huma Finance V2** (RWA) — $192.13M
- **Ondo Yield Assets** (RWA) — $180.01M
- **Hastra** (RWA) — $150.48M
- **Ondo Global Markets** (RWA) — $25.86M
- **Plume Vaults** (RWA) — $24.03M

## Daily active addresses

894,816 (Allium, as of 2026-09-03). Provider range 452,031–894,816. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [IBRL was never a meme. It's the reason Solana exists.

"With some very difficult but clever engineering, you can make a blockchain function as one giant computer that syncs all the financial information in the world at the speed of light."

"Alpenglow is a consensus improvement that will bring finality down to 100 milliseconds. It's going to feel like you're using any traditional system."

"This is us trying to, in a single unified environment, scale everything up so all of the world's markets, everything, could fit in one spot."](https://x.com/solana/status/2096115815397638649) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 05:58:48 GMT `upgrade`
- [RT by @solana: solana is the best blockchain to ever exist](https://x.com/blknoiz06/status/2095994812444934521) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 21:57:59 GMT
- [RT by @solana: Institutions have already chosen Solana.

Next, agents will decide Solana as the best rails to operate their financial operations on.

The amount of volume that will pass through Solana in 2027 will be unprecendented.](https://x.com/UpexiAllan/status/2095659426099405090) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 23:45:17 GMT
- [RT by @solana: yesterday was our biggest day on Solana. ever.

luxury szn is just getting started](https://x.com/Beezie/status/2095934952592621950) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 18:00:07 GMT
- [RT by @solana: The ultimate Solana Ecosystem Map for founders.](https://x.com/ivan_nomadz/status/2095847670245998726) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 12:13:18 GMT
- [Live poker from @WSOP returns with the 2026 WSOP Super Circuit Canada - Main Event
https://x.com/i/broadcasts/1rxmqpbndpQxy](https://x.com/solana/status/2095982604998582717) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 21:09:29 GMT
- [RT by @solana: The .sol Upgrade eligibility checker is live.

If you held a .sol before the Aug 17 snapshot, you can now check whether it’s eligible to receive a matching new .sol at https://migration.sns.id.

Here’s what to know ↓](https://x.com/sns/status/2095899967001153880) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 15:41:06 GMT `upgrade`
- [RT by @solana: x.com/i/article/209536081870…](https://x.com/solanapayments/status/2095902548976705723) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 15:51:22 GMT
- [RT by @anza_xyz: more users
→ more activity
→ problems exposed
→ IBRL
→ more capacity
→ more resilience
→ better products
→ more users

usage & execution is the moat](https://x.com/bw_solana/status/2095876304805740662) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 04 Sep 2026 14:07:05 GMT
- [Rent reduction is live on mainnet-beta.

Step 1 of SIMD-0437 activated at epoch 1028, the first of five feature gates on the road to cutting Solana's storage cost per byte by 90% overall.

Step 1 drops lamports per byte 6,960 → 6,333. Each remaining gate activates only after state growth checks out at the current level. We are stepping down to the final 696 safely, not on a fixed schedule. Follow here for an accurate timeline.

A safeguard gate (SIMD-0438) can restore the legacy value if state growth becomes a problem.](https://x.com/anza_xyz/status/2095654321350459648) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 23:25:00 GMT `upgrade` `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [IBRL was never a meme. It's the reason Solana exists.

"With some very difficult but clever engineering, you can make a blockchain function as one giant computer that syncs all the financial information in the world at the speed of light."

"Alpenglow is a consensus improvement that will bring finality down to 100 milliseconds. It's going to feel like you're using any traditional system."

"This is us trying to, in a single unified environment, scale everything up so all of the world's markets, everything, could fit in one spot."](https://x.com/solana/status/2096115815397638649) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 05:58:48 GMT `upgrade`
- [RT by @solana: solana is the best blockchain to ever exist](https://x.com/blknoiz06/status/2095994812444934521) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 21:57:59 GMT
- [RT by @solana: Institutions have already chosen Solana.

Next, agents will decide Solana as the best rails to operate their financial operations on.

The amount of volume that will pass through Solana in 2027 will be unprecendented.](https://x.com/UpexiAllan/status/2095659426099405090) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 23:45:17 GMT
- [RT by @solana: yesterday was our biggest day on Solana. ever.

luxury szn is just getting started](https://x.com/Beezie/status/2095934952592621950) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 18:00:07 GMT
- [RT by @solana: The ultimate Solana Ecosystem Map for founders.](https://x.com/ivan_nomadz/status/2095847670245998726) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 12:13:18 GMT
- [Live poker from @WSOP returns with the 2026 WSOP Super Circuit Canada - Main Event
https://x.com/i/broadcasts/1rxmqpbndpQxy](https://x.com/solana/status/2095982604998582717) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 21:09:29 GMT
- [RT by @solana: The .sol Upgrade eligibility checker is live.

If you held a .sol before the Aug 17 snapshot, you can now check whether it’s eligible to receive a matching new .sol at https://migration.sns.id.

Here’s what to know ↓](https://x.com/sns/status/2095899967001153880) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 15:41:06 GMT `upgrade`
- [RT by @solana: x.com/i/article/209536081870…](https://x.com/solanapayments/status/2095902548976705723) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 15:51:22 GMT
- [RT by @anza_xyz: more users
→ more activity
→ problems exposed
→ IBRL
→ more capacity
→ more resilience
→ better products
→ more users

usage & execution is the moat](https://x.com/bw_solana/status/2095876304805740662) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 04 Sep 2026 14:07:05 GMT
- [Rent reduction is live on mainnet-beta.

Step 1 of SIMD-0437 activated at epoch 1028, the first of five feature gates on the road to cutting Solana's storage cost per byte by 90% overall.

Step 1 drops lamports per byte 6,960 → 6,333. Each remaining gate activates only after state growth checks out at the current level. We are stepping down to the final 696 safely, not on a fixed schedule. Follow here for an accurate timeline.

A safeguard gate (SIMD-0438) can restore the legacy value if state growth becomes a problem.](https://x.com/anza_xyz/status/2095654321350459648) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 23:25:00 GMT `upgrade` `mainnet`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-05 (2026-09-05 03:34:45 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~314 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~314 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 86ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 36ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 38ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 58ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 47ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6169ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 89ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 84ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 26ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 56ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 21ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 31ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 513ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 77ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 148ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 52ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 94ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 171ms https://solana.com/data
- `solana.com.databricks` [ok] 200 71ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 311ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 164ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 28ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 47ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 123ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 293ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 77ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 75ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 81ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1812ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2956ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2883ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 458ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 193ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 30ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 31ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 230ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 179ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 215ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 198ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 305ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 249ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 26ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 268ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 190ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 293ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 188ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 247ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 147ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 250ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 168ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2011ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1249ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1148ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1269ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1528ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1302ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1681ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1330ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.MSFTx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SPYx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METAx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/METAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.TSLAx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AAPLx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.NVDAx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AMZNx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GOOGLx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AAPLx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 633ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 719ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.NVDAx` [ok] 200 2041ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.TSLAx` [ok] 200 2987ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 3087ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 862ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.QQQx` [FAIL]  12018ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.COINx` [FAIL]  12014ms https://api.backed.fi/api/v2/public/assets/COINx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DRAMx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MVLLx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MUUx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DRAMx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 1430ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.AXTIx` [FAIL]  12012ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.QQQx` [ok] 200 1875ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 1711ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.DJTx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AXTIx` [ok] 200 1160ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.circ.MUUx` [ok] 200 2560ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 870ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.SHEINx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.mult.MUUx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.KORUx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SHEINx` [ok] 200 109ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.SHEINx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.AXTIx` [ok] 200 1449ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 982ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.BANKCx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.KORUx` [ok] 200 1295ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.KORUx` [ok] 200 792ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 2704ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 583ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 2688ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.DJTx` [ok] 200 1607ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.KUNLx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 718ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.TNGYIx` [ok] 200 2814ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.price.WRFHDx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.KUNLx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 777ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.SZIGHx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 422ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.HRZRBx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.SMOIHx` [ok] 200 957ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.CRESBx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 592ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 603ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 925ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.CMERPx` [ok] 200 1939ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.CRESMx` [ok] 200 912ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.CSPCx` [ok] 200 1025ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 111ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 111ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.BDWAPx` [ok] 200 456ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.INTWx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WXXDCx` [ok] 200 1039ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 1017ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 411ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.price.SOXSx` [FAIL]  12011ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WHRFRx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.INTWx` [ok] 200 1220ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.SNXXx` [FAIL]  12015ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.INTWx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 961ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.SOXSx` [ok] 200 533ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 484ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 529ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 706ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.CRESPx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.NWGx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MIXUx` [ok] 200 3230ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.CRESPx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.NWGx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 924ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 814ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.NWGx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 1221ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.SINOx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.SINOx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.SINOTx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.WHGROx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.SNXXx` [ok] 200 1904ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 814ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.CLONPx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.SINOTx` [ok] 200 547ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.SNXXx` [ok] 200 843ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.CLPHDx` [ok] 200 704ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.WUXIBx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 1596ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 912ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.KUAIx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 667ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.NONGx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 722ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 400ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.NONGx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 625ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.NONGx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 516ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.COVELx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.HKEXCx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 1394ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.COVELx` [ok] 200 427ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.GEELx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.CKAHx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 1346ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.price.MTRCPx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.CHONGx` [ok] 200 862ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.price.HNDLDx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.CKAHx` [ok] 200 638ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 1539ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 718ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.CHONGx` [ok] 200 657ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 1328ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 1033ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 814ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.PICCx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 923ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.HNDLDx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 998ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 756ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 1144ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1119ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 145ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.SHEINx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.MEITx` [ok] 200 41ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 41ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.HKEXCx` [ok] 200 38ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 43ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.BANKCx` [ok] 200 34ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.SUOPTx` [ok] 200 39ms https://lite-api.jup.ag/tokens/v2/search?query=SUOPTx
- `jup.tokens.search.CTINSx` [ok] 200 41ms https://lite-api.jup.ag/tokens/v2/search?query=CTINSx
- `jito.tip_floor` [ok] 200 298ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 262ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 16ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 34ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 30ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 41ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 37ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 124ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
