# Borealis — Solana ecosystem report

**Generated** 2026-09-04T22:06:40Z · 2026-09-04 15:06:40 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-04T22:06:29Z · **RPC health** `ok`
**Health score** 96 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -3.22%; DEX 24h $2.46B · 1d +7% · vs-7d-ago -34%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -33.53%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -27.54%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 894,816.00 is +26.2% vs 30d median 709,223.50 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 444,355,034 |
| Block height | 422,400,364 |
| Block time | 2026-09-04T22:06:29Z |
| Epoch | 1,028 (59.96% · slot 259,035/432,000) |
| Mean TPS (last ~3,600s) | 3,441.9 |
| Mean non-vote TPS | 1,315.3 |
| Median TPS (same window) | 3,444.0 |
| Mean slot time | 315.6 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 545,215,062,446 |
| Circulating supply | 585,359,983 SOL |
| Total supply | 633,455,009 SOL |
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

- `xLabscif…` · 78.25K SOL · commission 5% · lag 566661 slots
- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 3344 slots
- `prt1st4R…` · 19.80K SOL · commission 5% · lag 868092 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 1006311 slots
- `5ZjxMYBb…` · 4.06K SOL · commission 0% · lag 389112 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1568913 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 178477 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 916395 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 2371280 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1554683 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1596197 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 1554577 slots

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
| **In-protocol fees 24h** | **$595.41K** (6,074.3 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-02 |
| **Solana REV** | **7,160.1 SOL** / **$701.85K** | MEASURED UTC calendar day 2026-09-02: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-02 · UTC day 2026-09-02 · SOL-USD date 2026-09-02 |
| Jito tip-floor run-rate (NOT REV) | $92.44K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 92438 USD; at p95 floor → 1262598 USD. |
| Protocol fees 24h | $11.82M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9947 |
| p90 / p99 | 0.000010 / 0.000105 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $101.68 | coingecko.simple_price |
| 24h change | -3.22% | coingecko.simple_price |
| Market cap | $59.52B | coingecko.simple_price |
| 24h volume | $3.56B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.85B |
| TVL 1d / 7d / 30d | +2.55% / -2.77% / +21.67% |
| DEX volume 24h | $2.46B · 1d +7.44% · vs-7d-ago -33.53% |
| 7d DEX volume | $15.61B · -29.85% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $11.82M |
| Fees 1d / 7d | +4.91% / -27.54% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $838.66M | -17.87% |
| Orca DEX | $279.89M | +39.55% |
| BisonFi | $232.51M | +19.63% |
| Meteora DLMM | $186.49M | +35.31% |
| Raydium AMM | $165.10M | +41.08% |
| Manifest Trade | $159.78M | -6.92% |
| Jupiterz | $99.63M | +99.60% |
| Scorch | $77.86M | +94.49% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.55B | -2.97% | -1.55% |
| Kamino Lend | Lending | $1.32B | -1.36% | +8.27% |
| Raydium AMM | Dexs | $1.11B | +0.99% | -3.11% |
| Jupiter Lend | Lending | $1.07B | -2.81% | -1.11% |
| Binance Staked SOL | Liquid Staking | $1.06B | -3.26% | -0.68% |
| Jito Liquid Staking | Liquid Staking | $1.04B | -2.40% | -0.36% |
| BlackRock BUIDL | RWA | $977.90M | +1.04% | +0.60% |
| Jupiter Perpetual Exchange | Derivatives | $750.47M | -2.86% | -1.73% |
| Jupiter Staked SOL | Liquid Staking | $526.15M | -3.33% | -1.97% |
| xStocks | RWA | $448.59M | -3.01% | +4.03% |

## Stablecoins

Solana circulating pegged-USD: **$16.44B**
(1d +3.38% · 7d +2.61%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.31B | +8.54% |
| USDT · Tether | $2.95B | +1.38% |
| USDGO · USDGO | $1.36B | +8.05% |
| USD1 · World Liberty Financial USD | $1.25B | +3.52% |
| BUIDL · BlackRock USD | $977.90M | +9.79% |
| PYUSD · PayPal USD | $719.35M | -10.02% |
| USDG · Global Dollar | $580.65M | -4.40% |
| USDe · Ethena USDe | $533.90M | -0.43% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 78 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 78 · priced-subset mcap $287.75M (lower bound, not a census).
24h volume $24.12M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $448.59M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 78 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.36B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $977.90M
- **xStocks** (RWA) — $448.59M
- **OnRe** (RWA) — $297.47M
- **Huma Finance V2** (RWA) — $192.11M
- **Ondo Yield Assets** (RWA) — $179.03M
- **Hastra** (RWA) — $150.47M
- **Ondo Global Markets** (RWA) — $25.84M
- **Plume Vaults** (RWA) — $23.25M

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
- [RT by @solana: Cleaner. Faster. Built for what’s next.

Day one of the new Imperial.](https://x.com/ImperialPerps/status/2095889770010358035) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 15:00:35 GMT
- [RT by @solana: Memecoin trading on @Solana once drove the blockchain's revenue spike but its spot trading volume fell from 40% to 16% from H1 2025 to H1 2026.

As that faded, something interesting happened: our H1 2026 analysis shows stablecoin swaps grew from 6% to 19% of spot volume, and general trading rose from 41% to 53%.

Despite falling revenue, Solana now dominates equity token trading (~97% of onchain spot RWA volume) and out-earns Ethereum in absolute revenue — at roughly 22% of ETH's market cap.](https://x.com/21shares/status/2095870582508171610) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 13:44:20 GMT
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
- [RT by @solana: Cleaner. Faster. Built for what’s next.

Day one of the new Imperial.](https://x.com/ImperialPerps/status/2095889770010358035) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 15:00:35 GMT
- [RT by @solana: Memecoin trading on @Solana once drove the blockchain's revenue spike but its spot trading volume fell from 40% to 16% from H1 2025 to H1 2026.

As that faded, something interesting happened: our H1 2026 analysis shows stablecoin swaps grew from 6% to 19% of spot volume, and general trading rose from 41% to 53%.

Despite falling revenue, Solana now dominates equity token trading (~97% of onchain spot RWA volume) and out-earns Ethereum in absolute revenue — at roughly 22% of ETH's market cap.](https://x.com/21shares/status/2095870582508171610) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 04 Sep 2026 13:44:20 GMT
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

_As of 2026-09-04 (2026-09-04 15:06:40 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 141ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 136ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 235ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 83ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 78ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6974ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 116ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 151ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 225ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 147ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 65ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 67ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 79ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 156ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 137ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 123ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 152ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 337ms https://solana.com/data
- `solana.com.databricks` [ok] 200 164ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 844ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 192ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 123ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 177ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 321ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 896ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 243ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 236ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 250ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 6183ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2282ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2149ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 250ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 168ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 52ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 95ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 402ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 335ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 326ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 384ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 422ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 518ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 54ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 719ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 307ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 392ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 367ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 262ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 395ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 312ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 422ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2846ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1550ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1669ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1717ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1258ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1599ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1931ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1175ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AAPLx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.GOOGLx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.TSLAx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.MSFTx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.METAx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.AAPLx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.AMZNx` [ok] 200 652ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.SPYx` [ok] 200 685ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.NVDAx` [ok] 200 811ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.MSFTx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 662ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 802ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 675ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 831ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.MVLLx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.MUUx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.mult.GOOGLx` [ok] 200 888ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 707ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.price.AXTIx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.mult.COINx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.KORUx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.circ.AXTIx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 1208ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.DRAMx` [ok] 200 1119ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.INTWx` [ok] 200 528ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.circ.MVLLx` [ok] 200 1251ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.MUUx` [ok] 200 1407ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 729ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.MVLLx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.mult.AXTIx` [ok] 200 1234ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.SOXSx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.price.SNXXx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.mult.MUUx` [ok] 200 826ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.circ.DJTx` [ok] 200 1875ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.price.SHEINx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.mult.DJTx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 775ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 2146ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.circ.KORUx` [ok] 200 2465ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.SNXXx` [ok] 200 774ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 656ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.BANKCx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 736ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.circ.INTWx` [ok] 200 2718ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 771ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.SHEINx` [ok] 200 821ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 1161ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.TNGYIx` [ok] 200 786ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.BANKCx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.INTWx` [ok] 200 687ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.mult.TNGYIx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 757ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.SZIGHx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.CTINSx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 1008ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.SNBIOx` [ok] 200 693ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 558ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 1385ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.MMGx` [ok] 200 2104ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 513ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.CRESBx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.KUNLx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 1111ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 484ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.CRESMx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.CMERPx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 1363ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.CRESMx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 1396ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.circ.SMOIHx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 875ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.CMENDx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.CMENDx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.circ.WXXDCx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.MIXUx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 883ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.ASMPTx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.SITCx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.SNDSCx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.WHRFRx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 831ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.CRESPx` [ok] 200 634ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.CTFJWx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.PRADx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.CRESPx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 3510ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.PRADx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 1182ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.CSPCx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 845ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 1783ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.WHGROx` [ok] 200 634ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.CSPCx` [ok] 200 575ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.PWAHLx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 1383ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.SINOx` [ok] 200 1055ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.SINOx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.CLONPx` [ok] 200 522ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.CKAHx` [ok] 200 509ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.SINOx` [ok] 200 649ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 578ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.CKAHx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.CKINFx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 1098ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 550ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 439ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.price.NONGx` [ok] 200 902ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 1617ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.CHONGx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.mult.CHONGx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 2638ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.NWGx` [FAIL]  12056ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CRAUTx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 1610ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 1573ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.PICCx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.MTRCPx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.mult.GEELx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.HNDLDx` [ok] 200 752ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.NONGx` [ok] 200 1296ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.COVELx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 2781ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.mult.PICCx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 772ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.COVELx` [ok] 200 439ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.circ.NWGx` [ok] 200 2172ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.NWGx` [ok] 200 1561ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 96ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 226ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.MUUx` [ok] 200 109ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.KORUx` [ok] 200 113ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.INTWx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.MVLLx` [ok] 200 112ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SNXXx` [ok] 200 112ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jup.tokens.search.DRAMx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.SHEINx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.SOXSx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jito.tip_floor` [ok] 200 171ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 435ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 134ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 49ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 47ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 228ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 51ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 179ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
