# Borealis — Solana ecosystem report

**Generated** 2026-08-28T21:52:11Z · 2026-08-28 14:52:11 PT
**Author** dustycompiler · **Version** 1.5.6 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-28T21:52:01Z · **RPC health** `ok`
**Health score** 100 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 400)/400, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -4.61%; DEX 24h $3.70B · 1d +57% · vs-7d-ago +34%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +47.11%. (threshold: `|7d %| >= 20`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 103.46 USD is +36.1% vs 30d median 76.00 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Daily active addresses vs 30d median** — Current 786,740.00 is +20.3% vs 30d median 653,923.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +57.34%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +33.73%. (threshold: `|7d %| >= 20`)
- **INFO · TPS vs 30d median (solana.com/data tx/86400)** — Current 4,654.69 TPS is +29.9% vs 30d median 3,584.53 TPS (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 442,440,680 |
| Block height | 420,488,670 |
| Block time | 2026-08-28T21:52:01Z |
| Epoch | 1,024 (16.82% · slot 72,684/432,000) |
| Mean TPS (last ~3,600s) | 4,654.7 |
| Mean non-vote TPS | 2,500.9 |
| Median TPS (same window) | 4,615.6 |
| Mean slot time | 317.3 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 542,883,463,692 |
| Circulating supply | 584,162,100 SOL |
| Total supply | 633,079,640 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 688 |
| Delinquent | 9 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 436,115,948 SOL |
| Delinquent stake | 18,340.78 SOL (0.004%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.15% / 35.47% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 16.99M SOL | 3.90% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.04M SOL | 3.68% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.39M SOL | 2.84% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.46M SOL | 2.63% | 5% | 0 |
| 5 | `C8Bey3LK…` | 9.29M SOL | 2.13% | 7% | 0 |
| 6 | `E1r4Psq8…` | 9.08M SOL | 2.08% | 0% | 0 |
| 7 | `CAo1dCGY…` | 9.00M SOL | 2.06% | 10% | 0 |
| 8 | `9eGrDohd…` | 7.29M SOL | 1.67% | 5% | 0 |
| 9 | `EvnRmnMr…` | 7.19M SOL | 1.65% | 7% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.10M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.60M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1188001 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 93979 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 456926 slots
- `kom1oNHy…` · 662.86 SOL · commission 5% · lag 1804164 slots
- `7ZjHeeYE…` · 176.09 SOL · commission 5% · lag 16203 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 442440680 slots
- `pSo1KZXg…` · 2.00 SOL · commission 4% · lag 102839 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 261325 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 1800681 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 38 | data/history.jsonl snapshot tape |
| TVL chart | 38 | data/history.jsonl snapshot tape |
| SOL chart | 37 | data/history.jsonl snapshot tape |
| history.jsonl rows | 38 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$1.14M** (10,859.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 |
| **Solana REV** | **13,424.0 SOL** / **$1.40M** | MEASURED UTC calendar day 2026-08-27: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 · UTC day 2026-08-27 · SOL-USD date 2026-08-27 |
| Jito tip-floor run-rate (NOT REV) | $130.80K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 130802 USD; at p95 floor → 1315882 USD. |
| Protocol fees 24h | $16.30M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9991 |
| p90 / p99 | 0.000019 / 0.000410 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.46 | coingecko.simple_price |
| 24h change | -4.61% | coingecko.simple_price |
| Market cap | $60.43B | coingecko.simple_price |
| 24h volume | $6.02B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.81B |
| TVL 1d / 7d / 30d | +0.71% / +9.05% / +21.30% |
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
| Orca DEX | $338.67M | +13.76% |
| Meteora DLMM | $245.52M | +32.85% |
| Raydium AMM | $184.27M | +10.82% |
| Axiom | $165.79M | +31.24% |
| Manifest Trade | $145.51M | +21.09% |
| pump.fun | $144.47M | +127.22% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.58B | -4.96% | +15.51% |
| Kamino Lend | Lending | $1.22B | -2.35% | +4.62% |
| Raydium AMM | Dexs | $1.14B | -0.75% | +13.36% |
| Jupiter Lend | Lending | $1.08B | -0.19% | +5.41% |
| Binance Staked SOL | Liquid Staking | $1.06B | -5.18% | +15.41% |
| Jito Liquid Staking | Liquid Staking | $1.04B | -5.35% | +13.26% |
| BlackRock BUIDL | RWA | $886.54M | -0.01% | +6.05% |
| Jupiter Perpetual Exchange | Derivatives | $763.64M | -2.90% | +3.39% |
| Jupiter Staked SOL | Liquid Staking | $536.69M | -5.29% | +12.51% |
| xStocks | RWA | $431.86M | -1.87% | +2.13% |

## Stablecoins

Solana circulating pegged-USD: **$15.87B**
(1d +0.53% · 7d -0.85%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.00B | +0.24% |
| USDT · Tether | $2.84B | +0.00% |
| USDGO · USDGO | $1.25B | -0.01% |
| USD1 · World Liberty Financial USD | $1.16B | +1.85% |
| BUIDL · BlackRock USD | $886.54M | +0.02% |
| PYUSD · PayPal USD | $682.42M | -0.30% |
| USDG · Global Dollar | $618.07M | +0.73% |
| USDe · Ethena USDe | $534.50M | -0.49% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 80 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 80 · priced-subset mcap $284.48M (lower bound, not a census).
24h volume $35.86M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $431.86M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 80 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.54M
- **xStocks** (RWA) — $431.86M
- **OnRe** (RWA) — $284.51M
- **Ondo Yield Assets** (RWA) — $178.96M
- **Hastra** (RWA) — $158.93M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $24.69M
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
- [Live from @mtndao Demo Day https://x.com/i/broadcasts/1nJOLQmXeXkxR](https://x.com/solana/status/2093416093633405225) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 19:11:05 GMT
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
- [Live from @mtndao Demo Day https://x.com/i/broadcasts/1nJOLQmXeXkxR](https://x.com/solana/status/2093416093633405225) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 19:11:05 GMT
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

_As of 2026-08-28 (2026-08-28 14:52:11 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 676ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 560ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 530ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 750ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 715ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7843ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1326ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 74ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 34ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 151ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 23ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 23ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 858ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 62ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 135ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 70ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 102ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 265ms https://solana.com/data
- `solana.com.databricks` [ok] 200 1147ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 152ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 66ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 171ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 60ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 277ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 357ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 81ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 76ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 79ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1050ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1720ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1418ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1467ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 188ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 719ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 538ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2308ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3220ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2853ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2427ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2424ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3183ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3272ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2404ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2516ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3035ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3042ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2412ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2488ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2661ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1427ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2197ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2414ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 3647ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2248ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 3423ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1746ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 632ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AAPLx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.MSFTx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.NVDAx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.MSFTx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.TSLAx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.AAPLx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.price.AMZNx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.NVDAx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.GOOGLx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.QQQx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.AAPLx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.GOOGLx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.SPYx` [ok] 200 670ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.TSLAx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.METAx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.BANKCx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.BANKCx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 785ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.COINx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 609ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 817ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.TNGYIx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.TSLAx` [ok] 200 936ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.MMGx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 637ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.KUNLx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.HAIDLx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 627ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 708ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 544ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 1583ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 690ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.SMOIHx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.CTINSx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 675ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.CMERPx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 679ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 920ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.CRESBx` [ok] 200 558ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.CSPCx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 1055ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 589ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 2406ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.BDWAPx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.CMENDx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.CMENDx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.WXXDCx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 1190ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 993ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 816ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.SITCx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.WHRFRx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 521ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.CRESPx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 525ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.mult.CRESPx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.PRADx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 711ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 1053ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.circ.WHGROx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 954ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.CTFJWx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.CLONPx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.WHGROx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.CTFJWx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.CTPCAx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.CTFJWx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 766ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.WUXIBx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.GENTEx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 825ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 888ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.SINOx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 1116ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.price.HKEXCx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.mult.CKAHx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.mult.HKEXCx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 532ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.SINOTx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.circ.CKINFx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.CHONGx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.NONGx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.COVELx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 1171ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 543ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.CHONGx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 985ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.KUAIx` [ok] 200 778ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.mult.CHONGx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.CKHUTx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.price.HNDLDx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.PICCx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.circ.HNDLDx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.price.POPMTx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.circ.MEITx` [ok] 200 651ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.POPMTx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 806ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.mult.MEITx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.POPMTx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.price.BOCOMx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.circ.COSCx` [ok] 200 509ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.BOCHKx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 607ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.CITICx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.circ.BOCOMx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 555ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.price.ANTASx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.price.CRESLx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.circ.ANTASx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.circ.BOCHKx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.price.CPETCx` [ok] 200 617ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.mult.ANTASx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.price.HAIERx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.circ.CITICx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.mult.BOCHKx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.price.ZJGLDx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.circ.CPETCx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.mult.CITICx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.circ.HAIERx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.mult.CPETCx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.price.PSBOCx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.circ.ZJGLDx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.mult.HAIERx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.circ.CRESLx` [ok] 200 647ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.mult.BOCOMx` [ok] 200 932ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.price.ICBCx` [ok] 200 630ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.circ.PSBOCx` [ok] 200 724ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.mult.ZJGLDx` [ok] 200 699ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.mult.CRESLx` [ok] 200 632ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.circ.ICBCx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.mult.ICBCx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `xstocks.mult.PSBOCx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 44ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 107ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 45ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 69ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 45ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 60ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 39ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 47ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.SINOTx` [ok] 200 55ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 256ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 277ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 70ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 634ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 536ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 507ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 671ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 259ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.6 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
