# Borealis — Solana ecosystem report

**Generated** 2026-08-29T00:48:27Z · 2026-08-28 17:48:27 PT
**Author** dustycompiler · **Version** 1.5.6 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-29T00:48:16Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 400)/400, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -4.89%; DEX 24h $3.70B · 1d +57% · vs-7d-ago +34%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +47.11%. (threshold: `|7d %| >= 20`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 104.03 USD is +36.9% vs 30d median 76.00 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +57.34%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +33.73%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 442,474,060 |
| Block height | 420,522,026 |
| Block time | 2026-08-29T00:48:16Z |
| Epoch | 1,024 (24.55% · slot 106,064/432,000) |
| Mean TPS (last ~3,600s) | 4,096.5 |
| Mean non-vote TPS | 1,938.9 |
| Median TPS (same window) | 4,008.8 |
| Mean slot time | 316.9 ms |
| Median slot time | 316.6 ms |
| Transaction count (cluster) | 542,928,358,904 |
| Circulating supply | 584,161,982 SOL |
| Total supply | 633,079,522 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 686 |
| Delinquent | 11 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 435,015,039 SOL |
| Delinquent stake | 1,119,249.70 SOL (0.257%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 79 |
| Top 10 / 20 stake share | 24.21% / 35.56% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 16.99M SOL | 3.91% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.04M SOL | 3.69% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.39M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.46M SOL | 2.63% | 5% | 0 |
| 5 | `C8Bey3LK…` | 9.29M SOL | 2.14% | 7% | 0 |
| 6 | `E1r4Psq8…` | 9.08M SOL | 2.09% | 0% | 0 |
| 7 | `CAo1dCGY…` | 9.00M SOL | 2.07% | 10% | 0 |
| 8 | `9eGrDohd…` | 7.29M SOL | 1.68% | 5% | 0 |
| 9 | `EvnRmnMr…` | 7.19M SOL | 1.65% | 7% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.41% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.10M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.37% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.60M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `CQdLgwkm…` · 1.08M SOL · commission 0% · lag 3600 slots
- `mrgn4atx…` · 20.33K SOL · commission 0% · lag 19120 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1221381 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 127359 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 490306 slots
- `kom1oNHy…` · 662.86 SOL · commission 5% · lag 1837544 slots
- `7ZjHeeYE…` · 176.09 SOL · commission 5% · lag 49583 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 442474060 slots
- `pSo1KZXg…` · 2.00 SOL · commission 4% · lag 136219 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 294705 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 1834061 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 50 | data/history.jsonl snapshot tape |
| TVL chart | 50 | data/history.jsonl snapshot tape |
| SOL chart | 49 | data/history.jsonl snapshot tape |
| history.jsonl rows | 50 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$1.14M** (10,859.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 |
| **Solana REV** | **13,424.0 SOL** / **$1.40M** | MEASURED UTC calendar day 2026-08-27: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 · UTC day 2026-08-27 · SOL-USD date 2026-08-27 |
| Jito tip-floor run-rate (NOT REV) | $171.67K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 171673 USD; at p95 floor → 17494911 USD. |
| Protocol fees 24h | $16.30M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9962 |
| p90 / p99 | 0.000018 / 0.000312 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $104.03 | coingecko.simple_price |
| 24h change | -4.89% | coingecko.simple_price |
| Market cap | $60.77B | coingecko.simple_price |
| 24h volume | $5.80B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.83B |
| TVL 1d / 7d / 30d | +0.96% / +9.32% / +21.61% |
| DEX volume 24h | $3.70B · 1d +57.34% · vs-7d-ago +33.73% |
| 7d DEX volume | $22.25B · +72.25% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $16.30M |
| Fees 1d / 7d | +7.19% / +47.11% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $1.46B | +90.88% |
| BisonFi | $416.99M | +65.84% |
| Orca DEX | $338.28M | +13.62% |
| Meteora DLMM | $245.52M | +32.85% |
| Raydium AMM | $174.43M | +4.90% |
| Axiom | $165.79M | +31.24% |
| pump.fun | $144.47M | +127.22% |
| Manifest Trade | $141.33M | +17.61% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.59B | -4.69% | +13.54% |
| Kamino Lend | Lending | $1.23B | -2.27% | +3.69% |
| Raydium AMM | Dexs | $1.12B | -3.39% | +11.16% |
| Jupiter Lend | Lending | $1.09B | +1.01% | +4.41% |
| Binance Staked SOL | Liquid Staking | $1.07B | -5.02% | +13.51% |
| Jito Liquid Staking | Liquid Staking | $1.05B | -4.63% | +11.32% |
| BlackRock BUIDL | RWA | $886.54M | +0.01% | +6.05% |
| Jupiter Perpetual Exchange | Derivatives | $768.34M | -2.83% | +2.14% |
| Jupiter Staked SOL | Liquid Staking | $540.48M | -4.52% | +10.66% |
| xStocks | RWA | $432.09M | -2.02% | +1.38% |

## Stablecoins

Solana circulating pegged-USD: **$15.89B**
(1d +0.54% · 7d -0.84%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.00B | +0.26% |
| USDT · Tether | $2.84B | +0.00% |
| USDGO · USDGO | $1.25B | -0.01% |
| USD1 · World Liberty Financial USD | $1.16B | +1.85% |
| BUIDL · BlackRock USD | $886.54M | +0.02% |
| PYUSD · PayPal USD | $693.46M | +1.31% |
| USDG · Global Dollar | $624.49M | +1.77% |
| USDe · Ethena USDe | $534.51M | -0.49% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 80 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 80 · priced-subset mcap $285.10M (lower bound, not a census).
24h volume $35.63M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $432.09M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 80 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.54M
- **xStocks** (RWA) — $432.09M
- **OnRe** (RWA) — $284.53M
- **Ondo Yield Assets** (RWA) — $179.94M
- **Hastra** (RWA) — $157.93M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $24.67M
- **Plume Vaults** (RWA) — $22.87M

## Daily active addresses

786,740 (Allium, as of 2026-08-27). Provider range 387,557–903,429. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: Pokémon Sealed by Kimji is LIVE. 🥡

Chase sealed packs from modern hits to vintage grails.

Build your collection. Put it to work. Earn while it sits in the pool.

Rip → Own → Earn.

Only possible on @Solana.

https://kimji.fun](https://x.com/Kimji_fun/status/2093480910801023339) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 23:28:38 GMT
- [RT by @solana: Collector’s Cup: Live at Solana Summer House.

Collector Crypt, Slabz and Gacha Sports go head to head in a competition to see who can pull the most valuable cards.

A little competition. A little luck. A lot of cardboard.

Watch it live in person or on Solana’s livestream.](https://x.com/Collector_Crypt/status/2093415324733313209) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 19:08:01 GMT
- [Watch the full episode with @Genfinity https://x.com/Genfinity/status/2091888668608741539](https://x.com/solana/status/2093428522803183681) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 20:00:28 GMT
- [Catch the Solana Summer House livestream on X tomorrow https://x.com/solana/status/2093005893759816030](https://x.com/solana/status/2093428510983704770) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 20:00:25 GMT
- [Solana Spaces co-founder JW on why he'll ride or die for Solana culture:

"It's such a collaborative environment. It's so cool to be friends with someone, then six months later they start a company, then six months later they're absolutely crushing it and they're everywhere."

"You get to watch your friends win every day. It's so fun to see your friends win."

"That spirit of collaboration and camaraderie, rooting for each other, doing each other favors, making the intros. You don't see that in many other places."

@DegentlemanJohn @solanaspaces @IOV_OWL](https://x.com/solana/status/2093428498740531429) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 20:00:22 GMT
- [RT by @solana: We’ve helped 15 startups raise $45,000,000 from over 137,000 people on the internet.

Now we want to help consumer app founders do the same. On top of giving them up to $10k/mo in marketing/ad spend!

DM me if you want to win](https://x.com/mitchellsniffle/status/2093105171392077908) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 22:35:35 GMT
- [RT by @solana: BREAKING: @Bitwise’s @Solana staking ETF has crossed $1B in assets under management, ten months after launch.](https://x.com/tokens/status/2093379191324721320) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 16:44:26 GMT
- [RT by @solana: .@mtndao founders @edgarpavlovsky and @barrett_io welcome us to the Summer Edition of Demo Day.

25 teams will be showcasing what they've been building all month.](https://x.com/SolanaEvents/status/2093414731000475680) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 19:05:40 GMT
- [7/
Solana's first stake-weighted vote drew participation from hundreds of millions of SOL on each proposal, well above the one-third quorum.

Proposals: https://governance.solana.com

SIMD-0550: https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0550-double-disinflation.md

SIMD-0607: https://github.com/solana-foundation/solana-improvement-documents/pull/607](https://x.com/anza_xyz/status/2093445419502272913) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:37 GMT `upgrade`
- [6/
SGP-0003  ❌ did not pass and would have split the base fee into an inclusion fee for leaders plus a resource fee scaling with usage.

Restructuring fees changes revenue for validators and cost modeling for every app. Most non-passing stake abstained rather than opposed.

Majority support on a first attempt is a strong starting point and we can expect a reparameterized version to return for a vote.](https://x.com/anza_xyz/status/2093445282910601403) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:04 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: Pokémon Sealed by Kimji is LIVE. 🥡

Chase sealed packs from modern hits to vintage grails.

Build your collection. Put it to work. Earn while it sits in the pool.

Rip → Own → Earn.

Only possible on @Solana.

https://kimji.fun](https://x.com/Kimji_fun/status/2093480910801023339) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 23:28:38 GMT
- [RT by @solana: Collector’s Cup: Live at Solana Summer House.

Collector Crypt, Slabz and Gacha Sports go head to head in a competition to see who can pull the most valuable cards.

A little competition. A little luck. A lot of cardboard.

Watch it live in person or on Solana’s livestream.](https://x.com/Collector_Crypt/status/2093415324733313209) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 19:08:01 GMT
- [Watch the full episode with @Genfinity https://x.com/Genfinity/status/2091888668608741539](https://x.com/solana/status/2093428522803183681) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 20:00:28 GMT
- [Catch the Solana Summer House livestream on X tomorrow https://x.com/solana/status/2093005893759816030](https://x.com/solana/status/2093428510983704770) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 20:00:25 GMT
- [Solana Spaces co-founder JW on why he'll ride or die for Solana culture:

"It's such a collaborative environment. It's so cool to be friends with someone, then six months later they start a company, then six months later they're absolutely crushing it and they're everywhere."

"You get to watch your friends win every day. It's so fun to see your friends win."

"That spirit of collaboration and camaraderie, rooting for each other, doing each other favors, making the intros. You don't see that in many other places."

@DegentlemanJohn @solanaspaces @IOV_OWL](https://x.com/solana/status/2093428498740531429) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 20:00:22 GMT
- [RT by @solana: We’ve helped 15 startups raise $45,000,000 from over 137,000 people on the internet.

Now we want to help consumer app founders do the same. On top of giving them up to $10k/mo in marketing/ad spend!

DM me if you want to win](https://x.com/mitchellsniffle/status/2093105171392077908) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 22:35:35 GMT
- [RT by @solana: BREAKING: @Bitwise’s @Solana staking ETF has crossed $1B in assets under management, ten months after launch.](https://x.com/tokens/status/2093379191324721320) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 16:44:26 GMT
- [RT by @solana: .@mtndao founders @edgarpavlovsky and @barrett_io welcome us to the Summer Edition of Demo Day.

25 teams will be showcasing what they've been building all month.](https://x.com/SolanaEvents/status/2093414731000475680) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 19:05:40 GMT
- [7/
Solana's first stake-weighted vote drew participation from hundreds of millions of SOL on each proposal, well above the one-third quorum.

Proposals: https://governance.solana.com

SIMD-0550: https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0550-double-disinflation.md

SIMD-0607: https://github.com/solana-foundation/solana-improvement-documents/pull/607](https://x.com/anza_xyz/status/2093445419502272913) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:37 GMT `upgrade`
- [6/
SGP-0003  ❌ did not pass and would have split the base fee into an inclusion fee for leaders plus a resource fee scaling with usage.

Restructuring fees changes revenue for validators and cost modeling for every app. Most non-passing stake abstained rather than opposed.

Majority support on a first attempt is a strong starting point and we can expect a reparameterized version to return for a vote.](https://x.com/anza_xyz/status/2093445282910601403) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:04 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-29 (2026-08-28 17:48:27 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~317 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~317 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **xStocks** — priced up to 80 of 715 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 750ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 474ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 727ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 681ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 541ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6872ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1247ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 86ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 170ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 101ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 82ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 61ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 100ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 208ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 121ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 102ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 132ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 334ms https://solana.com/data
- `solana.com.databricks` [ok] 200 483ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 369ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 277ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 116ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 170ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 267ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 678ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 259ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 244ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 245ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 878ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2275ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2148ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1530ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 216ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 614ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 471ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3164ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3175ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2635ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2099ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3197ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2890ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2827ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2020ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3204ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2576ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3159ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2013ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2189ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2193ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1507ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 3749ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1768ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1037ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1360ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1136ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2062ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 635ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.NVDAx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.GOOGLx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.MSFTx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.AAPLx` [ok] 200 542ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.NVDAx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.SPYx` [ok] 200 638ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.TSLAx` [ok] 200 665ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.MSFTx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 779ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.mult.NVDAx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.AAPLx` [ok] 200 392ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 507ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.price.MMGx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.TNGYIx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.COINx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 1088ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.AMZNx` [ok] 200 1880ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 406ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.TSLAx` [ok] 200 1110ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.AMZNx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 1157ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.MMGx` [ok] 200 908ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.CTINSx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.JDLOGx` [ok] 200 727ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.price.SNBIOx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.CTINSx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.SUOPTx` [ok] 200 660ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 1604ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 932ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 977ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 648ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 900ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.CSPCx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.CRESBx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.CSPCx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 497ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 635ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 507ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.WXXDCx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.ASMPTx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.MIXUx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 2093ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 965ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.JDHLTx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 762ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.SITCx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 647ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.PRADx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.CMENDx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 582ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.SINOTx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.WHGROx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.SINOTx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.WHGROx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 1250ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 650ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.SWPRPx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.PRADx` [ok] 200 1098ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 548ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.CKAHx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 749ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.GENTEx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.WUXIBx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.GENTEx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.COVELx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.GEELx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.mult.CKINFx` [ok] 200 547ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.COVELx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.HNDLDx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.CHONGx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 951ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.mult.COVELx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 741ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.MTRCPx` [ok] 200 599ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.HNDLDx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.CHONGx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 766ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.MTRCPx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.price.POPMTx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.mult.MEITx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.price.BOCOMx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 652ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.POPMTx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 641ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.COSCx` [ok] 200 583ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.CKHUTx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 575ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.POPMTx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.CPETCx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.circ.BOCOMx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.price.ANTASx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.price.CRESLx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.mult.PICCx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.CPETCx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.mult.BOCOMx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.price.CITICx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.circ.ANTASx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.price.HAIERx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.circ.CRESLx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.price.BOCHKx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.circ.CITICx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.price.ZJGLDx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.mult.ANTASx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.circ.HAIERx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.mult.CRESLx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.circ.BOCHKx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.circ.ZJGLDx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.price.PSBOCx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.mult.CITICx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.mult.HAIERx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.price.ICBCx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.mult.ZJGLDx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.mult.CPETCx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.circ.PSBOCx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.mult.BOCHKx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 1060ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.ICBCx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.mult.PSBOCx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.ICBCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1302ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 358ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 98ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 101ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 102ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 85ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 97ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.SINOTx` [ok] 200 97ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 145ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 359ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 135ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 612ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 449ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 748ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 649ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 379ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.6 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
