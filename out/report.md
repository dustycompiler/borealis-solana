# Borealis — Solana ecosystem report

**Generated** 2026-09-05T07:35:01Z · 2026-09-05 00:35:01 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-05T07:34:51Z · **RPC health** `ok`
**Health score** 95 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -1.29%; DEX 24h $1.85B · 1d -25% · vs-7d-ago -29%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -24.89%. (threshold: `|1d %| >= 8`)
- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -19.33%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -28.69%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -39.51%. (threshold: `|7d %| >= 20`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -1.29%, DeFiLlama TVL 1d -1.06%, DEX 1d -24.89%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **INFO · Daily active addresses vs 30d median** — Current 894,816.00 is +26.2% vs 30d median 709,223.50 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 444,463,363 |
| Block height | 422,508,135 |
| Block time | 2026-09-05T07:34:51Z |
| Epoch | 1,028 (85.04% · slot 367,366/432,000) |
| Mean TPS (last ~3,600s) | 3,179.0 |
| Mean non-vote TPS | 1,050.3 |
| Median TPS (same window) | 3,164.3 |
| Mean slot time | 315.8 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 545,325,265,780 |
| Circulating supply | 585,359,692 SOL |
| Total supply | 633,454,717 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 678 |
| Delinquent | 17 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 436,778,150 SOL |
| Delinquent stake | 120,716.18 SOL (0.028%) |
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

- `xLabscif…` · 78.25K SOL · commission 5% · lag 674990 slots
- `prt1st4R…` · 19.80K SOL · commission 5% · lag 976421 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 1114640 slots
- `5ZjxMYBb…` · 4.06K SOL · commission 0% · lag 497441 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1677242 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 286806 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 1024724 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 2479609 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1663012 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1704526 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 1662906 slots
- `6pEtDovp…` · 131.86 SOL · commission 100% · lag 1677290 slots

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
| Jito tip-floor run-rate (NOT REV) | $23.97K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 23965 USD; at p95 floor → 1296266 USD. |
| Protocol fees 24h | $9.54M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9938 |
| p90 / p99 | 0.000010 / 0.000113 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $102.48 | coingecko.simple_price |
| 24h change | -1.29% | coingecko.simple_price |
| Market cap | $59.99B | coingecko.simple_price |
| 24h volume | $3.05B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.86B |
| TVL 1d / 7d / 30d | -1.06% / -0.22% / +21.87% |
| DEX volume 24h | $1.85B · 1d -24.89% · vs-7d-ago -28.69% |
| 7d DEX volume | $14.32B · -32.59% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $9.54M |
| Fees 1d / 7d | -19.33% / -39.51% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $310.67M | -62.96% |
| BisonFi | $232.51M | 0.00% |
| Orca DEX | $228.55M | -19.98% |
| Meteora DLMM | $180.66M | -3.13% |
| Manifest Trade | $155.30M | -12.49% |
| Raydium AMM | $136.22M | -11.44% |
| Jupiterz | $99.63M | 0.00% |
| Scorch | $77.86M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.56B | -1.56% | -1.97% |
| Kamino Lend | Lending | $1.32B | -1.20% | +5.57% |
| Raydium AMM | Dexs | $1.11B | -1.81% | -1.40% |
| Jupiter Lend | Lending | $1.09B | +0.06% | +0.69% |
| Binance Staked SOL | Liquid Staking | $1.06B | -1.62% | -1.19% |
| Jito Liquid Staking | Liquid Staking | $1.04B | -0.95% | -0.31% |
| BlackRock BUIDL | RWA | $977.90M | +1.04% | +0.60% |
| Jupiter Perpetual Exchange | Derivatives | $750.36M | -1.96% | -2.25% |
| Jupiter Staked SOL | Liquid Staking | $526.56M | -2.01% | -2.48% |
| xStocks | RWA | $447.26M | -2.75% | +3.49% |

## Stablecoins

Solana circulating pegged-USD: **$16.25B**
(1d -0.24% · 7d +2.59%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.30B | +2.68% |
| USDT · Tether | $2.77B | -6.11% |
| USDGO · USDGO | $1.36B | +3.04% |
| USD1 · World Liberty Financial USD | $1.25B | +2.25% |
| BUIDL · BlackRock USD | $977.90M | +4.27% |
| PYUSD · PayPal USD | $718.76M | -16.42% |
| USDG · Global Dollar | $579.45M | +3.08% |
| USDe · Ethena USDe | $533.36M | -0.52% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 78 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 78 · priced-subset mcap $287.63M (lower bound, not a census).
24h volume $25.14M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $447.26M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 78 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.36B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $977.90M
- **xStocks** (RWA) — $447.26M
- **OnRe** (RWA) — $298.54M
- **Huma Finance V2** (RWA) — $192.14M
- **Ondo Yield Assets** (RWA) — $179.96M
- **Hastra** (RWA) — $150.48M
- **Ondo Global Markets** (RWA) — $25.89M
- **Plume Vaults** (RWA) — $23.99M

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
- [Repo and benchmarks: https://github.com/anza-xyz/wincode

wincode is a drop-in replacement when layout and configuration match.](https://x.com/anza_xyz/status/2095612015192703481) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:53 GMT
- [wincode has surpassed 5M downloads 📦📈

Our Rust crate started as a fix for serialization performance in the Agave validator client.

RustSec now lists it as a recommended bincode replacement. Built to make Solana faster, now adopted across the Rust community.

Credit to Anza IBRL engineering culture who keep pushing the envelope on speed.

How it works by wincode creator @zbr0wn: https://www.anza.xyz/blog/wincode-bincode-compatible-rust-serializer](https://x.com/anza_xyz/status/2095611874142548262) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:20 GMT
- [IBRL](https://x.com/anza_xyz/status/2095605589548417152) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:11:21 GMT
- [RT by @anza_xyz: .@vibhu, Chief Product Officer @SolanaFndn, on how Solana works with startups: capital through grants and venture, community through Superteam's 29 country chapters, and distribution once they're ready to ship.](https://x.com/SolanaFndn/status/2095542610094170305) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 16:01:06 GMT
- [RT by @anza_xyz: BREAKING: Solana ranks #1 for app revenue in August with $143M. 38% of all onchain app revenue.](https://x.com/solana/status/2095379848709677207) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 05:14:20 GMT
- [Prepare for the first step of rent reduction coming to mainnet-beta later today with this guide to reclaim your excess SOL.](https://x.com/anza_xyz/status/2095541509135495452) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 15:56:43 GMT `mainnet`
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — solana.com/news · Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — solana.com/news · Thu, 03 Sep 2026 15:15:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

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
- [Repo and benchmarks: https://github.com/anza-xyz/wincode

wincode is a drop-in replacement when layout and configuration match.](https://x.com/anza_xyz/status/2095612015192703481) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:53 GMT
- [wincode has surpassed 5M downloads 📦📈

Our Rust crate started as a fix for serialization performance in the Agave validator client.

RustSec now lists it as a recommended bincode replacement. Built to make Solana faster, now adopted across the Rust community.

Credit to Anza IBRL engineering culture who keep pushing the envelope on speed.

How it works by wincode creator @zbr0wn: https://www.anza.xyz/blog/wincode-bincode-compatible-rust-serializer](https://x.com/anza_xyz/status/2095611874142548262) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:20 GMT
- [IBRL](https://x.com/anza_xyz/status/2095605589548417152) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:11:21 GMT
- [RT by @anza_xyz: .@vibhu, Chief Product Officer @SolanaFndn, on how Solana works with startups: capital through grants and venture, community through Superteam's 29 country chapters, and distribution once they're ready to ship.](https://x.com/SolanaFndn/status/2095542610094170305) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 16:01:06 GMT
- [RT by @anza_xyz: BREAKING: Solana ranks #1 for app revenue in August with $143M. 38% of all onchain app revenue.](https://x.com/solana/status/2095379848709677207) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 05:14:20 GMT
- [Prepare for the first step of rent reduction coming to mainnet-beta later today with this guide to reclaim your excess SOL.](https://x.com/anza_xyz/status/2095541509135495452) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 15:56:43 GMT `mainnet`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-05 (2026-09-05 00:35:01 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 424ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 316ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 364ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 381ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 396ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7292ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 764ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 129ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 91ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 274ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 59ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 71ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 68ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 335ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 521ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 96ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 128ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 502ms https://solana.com/data
- `solana.com.databricks` [ok] 200 166ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 488ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 303ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 123ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 161ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 424ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 712ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 239ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 233ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 238ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [FAIL]  18256ms https://nitter.perennialte.ch/solana/rss — TimeoutError: The read operation timed out
- `rss.nitter.solana_status` [FAIL]  18054ms https://nitter.perennialte.ch/solana_status/rss — TimeoutError: The read operation timed out
- `rss.nitter.anza_xyz` [ok] 200 7941ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 892ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 326ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 276ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 358ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 319ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1326ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1263ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1278ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1218ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1173ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1495ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1179ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1523ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1438ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1271ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1809ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1355ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1212ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1145ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1721ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2047ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1872ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1489ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1270ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1379ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2072ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1273ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.METAx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.AAPLx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.METAx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.price.NVDAx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.MSFTx` [ok] 200 596ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.mult.METAx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.NVDAx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.AMZNx` [ok] 200 766ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.SPYx` [ok] 200 806ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.SPYx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 647ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.TSLAx` [ok] 200 1078ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.QQQx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.SPYx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.MSFTx` [ok] 200 655ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.GOOGLx` [ok] 200 1373ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.TSLAx` [ok] 200 484ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 838ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 542ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 656ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 1019ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 576ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.MVLLx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.KORUx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.price.DJTx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.price.AXTIx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.mult.GOOGLx` [ok] 200 648ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 690ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.MUUx` [ok] 200 454ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.price.DRAMx` [ok] 200 694ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.INTWx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.mult.COINx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.SOXSx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.circ.MVLLx` [ok] 200 1059ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 617ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.mult.AXTIx` [ok] 200 638ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.mult.MVLLx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.SOXSx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 1415ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.price.SHEINx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.mult.DJTx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 718ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 1477ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.SOXSx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 1572ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.circ.SHEINx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.BANKCx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.price.TNGYIx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.MUUx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.SHEINx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.SNXXx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.mult.MMGx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.SUOPTx` [ok] 200 482ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.HAIDLx` [ok] 200 508ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.LAOPGx` [ok] 200 1359ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.KUNLx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 1515ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.CTINSx` [ok] 200 1779ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.CRESBx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 1038ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 679ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 634ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.WXXDCx` [ok] 200 456ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.CRESMx` [ok] 200 908ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.HRZRBx` [ok] 200 1817ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 1050ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.CMENDx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 639ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 1737ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.ASMPTx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.MIXUx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.WHRFRx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.CMERPx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.SITCx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.CRESPx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 607ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.SITCx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 681ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.CRESPx` [ok] 200 730ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 899ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.CLONPx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.SITCx` [ok] 200 929ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.CTFJWx` [ok] 200 1165ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.CLONPx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.WHGROx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.GENTEx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 634ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.CKAHx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.SWPRPx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.GENTEx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 690ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 715ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.CKINFx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.HKEXCx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.KUAIx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.CHONGx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.circ.COVELx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 496ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.CHONGx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.HNDLDx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.KUAIx` [ok] 200 821ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.CKHUTx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.PICCx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 554ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.HNDLDx` [ok] 200 784ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 567ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 570ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 1202ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 1671ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.MTRCPx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 943ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.price.NWGx` [FAIL]  12036ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.NWGx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.NWGx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 2427ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 218ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.MUUx` [ok] 200 92ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.KORUx` [ok] 200 92ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.INTWx` [ok] 200 90ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.MVLLx` [ok] 200 140ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SNXXx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jup.tokens.search.DRAMx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.SHEINx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.SOXSx` [ok] 200 80ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jito.tip_floor` [ok] 200 122ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 296ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 269ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 348ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 320ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 420ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 334ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 268ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
