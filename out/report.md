# Borealis — Solana ecosystem report

**Generated** 2026-09-05T12:27:20Z · 2026-09-05 05:27:20 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-05T12:27:10Z · **RPC health** `ok`
**Health score** 94 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -1.70%; DEX 24h $1.88B · 1d -24% · vs-7d-ago -27%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -23.50%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -27.37%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -12.58%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -34.47%. (threshold: `|7d %| >= 20`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -1.70%, DeFiLlama TVL 1d -0.70%, DEX 1d -23.50%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **INFO · TPS vs 30d median (solana.com/data tx/86400)** — Current 3,008.96 TPS is -20.2% vs 30d median 3,772.26 TPS (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 444,519,139 |
| Block height | 422,563,657 |
| Block time | 2026-09-05T12:27:10Z |
| Epoch | 1,028 (97.95% · slot 423,142/432,000) |
| Mean TPS (last ~3,600s) | 3,009.0 |
| Mean non-vote TPS | 877.6 |
| Median TPS (same window) | 3,016.3 |
| Mean slot time | 314.6 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 545,379,280,482 |
| Circulating supply | 585,359,549 SOL |
| Total supply | 633,454,574 SOL |
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

- `xLabscif…` · 78.25K SOL · commission 5% · lag 730766 slots
- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 7256 slots
- `prt1st4R…` · 19.80K SOL · commission 5% · lag 1032197 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 1170416 slots
- `5ZjxMYBb…` · 4.06K SOL · commission 0% · lag 553217 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1733018 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 342582 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 1080500 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 2535385 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1718788 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1760302 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 1718682 slots

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
| Jito tip-floor run-rate (NOT REV) | $40.33K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 40327 USD; at p95 floor → 1239226 USD. |
| Protocol fees 24h | $10.33M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9964 |
| p90 / p99 | 0.000010 / 0.000095 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $102.41 | coingecko.simple_price |
| 24h change | -1.70% | coingecko.simple_price |
| Market cap | $59.94B | coingecko.simple_price |
| 24h volume | $2.70B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.88B |
| TVL 1d / 7d / 30d | -0.70% / +0.14% / +22.32% |
| DEX volume 24h | $1.88B · 1d -23.50% · vs-7d-ago -27.37% |
| 7d DEX volume | $14.90B · -29.85% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $10.33M |
| Fees 1d / 7d | -12.58% / -34.47% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $310.67M | -62.96% |
| BisonFi | $251.95M | +8.36% |
| Orca DEX | $210.00M | -26.48% |
| Meteora DLMM | $180.66M | -3.13% |
| Manifest Trade | $140.67M | -20.73% |
| Raydium AMM | $124.73M | -18.91% |
| Jupiterz | $64.61M | -35.15% |
| Scorch | $63.08M | -18.98% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.57B | -1.02% | -0.82% |
| Kamino Lend | Lending | $1.32B | -0.06% | +6.04% |
| Raydium AMM | Dexs | $1.11B | -0.60% | -0.70% |
| Jupiter Lend | Lending | $1.10B | +0.38% | +1.08% |
| Binance Staked SOL | Liquid Staking | $1.07B | -1.63% | +0.04% |
| Jito Liquid Staking | Liquid Staking | $1.05B | -0.20% | +0.87% |
| BlackRock BUIDL | RWA | $977.90M | +1.04% | +0.60% |
| Jupiter Perpetual Exchange | Derivatives | $753.16M | -1.80% | -1.59% |
| Jupiter Staked SOL | Liquid Staking | $530.25M | -1.00% | -1.28% |
| xStocks | RWA | $447.87M | -2.63% | +3.52% |

## Stablecoins

Solana circulating pegged-USD: **$16.28B**
(1d -0.24% · 7d +2.59%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.31B | +2.85% |
| USDT · Tether | $2.77B | -6.11% |
| USDGO · USDGO | $1.36B | +3.04% |
| USD1 · World Liberty Financial USD | $1.26B | +2.88% |
| BUIDL · BlackRock USD | $977.90M | +4.27% |
| PYUSD · PayPal USD | $713.71M | -17.00% |
| USDG · Global Dollar | $585.62M | +4.17% |
| USDe · Ethena USDe | $536.69M | +0.10% |

## Tokenized equities (xStocks)


Listed 726 · Solana deployments 726 · priced 0 · priced-subset mcap — (lower bound, not a census).
24h volume $23.17M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $447.87M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 0 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.36B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $977.90M
- **xStocks** (RWA) — $447.87M
- **OnRe** (RWA) — $298.87M
- **Huma Finance V2** (RWA) — $192.14M
- **Ondo Yield Assets** (RWA) — $179.98M
- **Hastra** (RWA) — $150.48M
- **Ondo Global Markets** (RWA) — $25.88M
- **Plume Vaults** (RWA) — $24.03M

## Daily active addresses

855,572 (Allium, as of 2026-09-04). Provider range 467,836–886,281. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [x.com/i/article/209620676578…](https://x.com/solana/status/2096206771232923652) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 12:00:14 GMT
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

- [x.com/i/article/209620676578…](https://x.com/solana/status/2096206771232923652) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 12:00:14 GMT
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

_As of 2026-09-05 (2026-09-05 05:27:20 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~315 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~315 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **xStocks market cap** — Listed Solana-deployed xStocks but quote and/or circulating missing. Mcap omitted.
- **xStocks** — priced up to 80 of 726 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.
- **xStocks** — price, circulating-supply, and/or currentMultiplier missing — market cap omitted (never assumed multiplier=1.0)

## Sources this run

- `rpc.getHealth` [ok] 200 433ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 338ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 328ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 546ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 388ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6780ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 713ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 89ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 26ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 280ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 21ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 21ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 26ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 71ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 102ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 44ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 85ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 499ms https://solana.com/data
- `solana.com.databricks` [ok] 200 70ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 543ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 104ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 154ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 71ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 401ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 890ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 434ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 436ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 446ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 302ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2001ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2203ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 174ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 231ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 340ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 350ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1072ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1934ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1389ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1049ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1236ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1039ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1235ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1574ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1157ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1978ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1077ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1257ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1189ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1141ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2930ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2146ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1819ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1883ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1254ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1106ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1334ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 930ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AMZNx` [FAIL]  12015ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SPYx` [FAIL]  12017ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.TSLAx` [FAIL]  12018ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AAPLx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.NVDAx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GOOGLx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MSFTx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METAx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/METAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AAPLx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 618ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 681ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 720ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 585ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 926ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 524ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.QQQx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.COINx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/COINx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DRAMx` [FAIL]  12010ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MVLLx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MUUx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AXTIx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DJTx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.KORUx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DRAMx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.circ.KORUx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.MUUx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 598ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.MVLLx` [ok] 200 519ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.mult.MVLLx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.MUUx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 901ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 1402ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 787ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.DJTx` [ok] 200 1593ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.price.INTWx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SOXSx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SNXXx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SHEINx` [FAIL]  12009ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.INTWx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.NWGx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SNXXx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.price.BANKCx` [FAIL]  12009ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.INTWx` [ok] 200 595ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.SHEINx` [ok] 200 687ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [FAIL]  12008ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SOXSx` [ok] 200 850ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.BANKCx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.SUOPTx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.SHEINx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.NWGx` [ok] 200 814ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.price.MMGx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SOXSx` [ok] 200 689ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.mult.SNXXx` [ok] 200 1152ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.mult.NWGx` [ok] 200 488ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 738ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ZHAOMx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.TNGYIx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.JDLOGx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ZHAOMx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.LAOPGx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.KUNLx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.LAOPGx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [FAIL]  12009ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.JDLOGx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [FAIL]  12011ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HAIDLx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 1652ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 1658ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SNBIOx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ENNHLx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ENNHLx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SZIGHx` [ok] 200 526ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HRZRBx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 1035ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.CRESBx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.ENNHLx` [ok] 200 1293ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.CMERPx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SZIGHx` [ok] 200 1178ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.CSPCx` [FAIL]  12007ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.HRZRBx` [ok] 200 1175ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 821ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 563ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 841ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 791ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CRESMx` [FAIL]  12016ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.JTGEXx` [ok] 200 583ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CRESMx` [ok] 200 591ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.CMENDx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WXXDCx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BDWAPx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.MIXUx` [FAIL]  12010ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MIXUx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 876ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MIXUx` [ok] 200 490ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 1521ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.BDWAPx` [ok] 200 980ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 1731ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 1708ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.SITCx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SITCx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SNDSCx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.JDHLTx` [ok] 200 519ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.CRESPx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PRADx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.JDHLTx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.SINOTx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SNDSCx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CRESPx` [ok] 200 770ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.CTFJWx` [ok] 200 563ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 861ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 899ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.CLONPx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CLONPx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 1530ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.WHGROx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WHGROx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.SINOx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CTPCAx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PWAHLx` [FAIL]  12009ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CTPCAx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 1473ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [FAIL]  12016ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CLPHDx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.GENTEx` [FAIL]  12013ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CTPCAx` [ok] 200 1321ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CLPHDx` [ok] 200 1098ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 1982ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.GENTEx` [ok] 200 1629ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 700ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WUXIBx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CKAHx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SWPRPx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.CKINFx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SWPRPx` [ok] 200 698ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 822ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [FAIL]  12008ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HKCGAx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.KUAIx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CKINFx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.KUAIx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.NONGx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HKEXCx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.COVELx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.COVELx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 1938ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.CHONGx` [FAIL]  12011ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MEITx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CHONGx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.price.GEELx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MTRCPx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CHONGx` [ok] 200 801ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.MTRCPx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 785ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MTRCPx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.price.PICCx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.HNDLDx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 1088ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 655ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 499ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.price.COSCx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CKHUTx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.COSCx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 1127ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1811ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 214ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.KORUx` [ok] 200 112ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.MVLLx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.DRAMx` [ok] 200 114ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.MUUx` [ok] 200 107ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.AXTIx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=AXTIx
- `jup.tokens.search.DJTx` [ok] 200 103ms https://lite-api.jup.ag/tokens/v2/search?query=DJTx
- `jup.tokens.search.INTWx` [ok] 200 107ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.SHEINx` [ok] 200 103ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jito.tip_floor` [ok] 200 476ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 403ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 131ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 335ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 345ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 317ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 530ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 193ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
