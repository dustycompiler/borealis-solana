# Borealis — Solana ecosystem report

**Generated** 2026-08-29T06:48:44Z · 2026-08-28 23:48:44 PT
**Author** dustycompiler · **Version** 1.5.6 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-29T06:48:34Z · **RPC health** `ok`
**Health score** 100 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 400)/400, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -3.78%; DEX 24h $2.62B · 1d -29% · vs-7d-ago -27%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -29.33%. (threshold: `|1d %| >= 8`)
- **WARN · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -3.78%, DeFiLlama TVL 1d -2.58%, DEX 1d -29.33%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -27.38%. (threshold: `|7d %| >= 20`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 103.55 USD is +35.9% vs 30d median 76.20 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Daily active addresses vs 30d median** — Current 837,981.00 is +27.5% vs 30d median 657,156.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 442,542,223 |
| Block height | 420,590,150 |
| Block time | 2026-08-29T06:48:34Z |
| Epoch | 1,024 (40.33% · slot 174,228/432,000) |
| Mean TPS (last ~3,600s) | 3,892.7 |
| Mean non-vote TPS | 1,733.1 |
| Median TPS (same window) | 3,937.8 |
| Mean slot time | 316.8 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 543,010,884,049 |
| Circulating supply | 584,161,765 SOL |
| Total supply | 633,079,305 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 687 |
| Delinquent | 10 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 436,095,615 SOL |
| Delinquent stake | 38,673.95 SOL (0.009%) |
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

- `mrgn4atx…` · 20.33K SOL · commission 0% · lag 87283 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1289544 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 195522 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 558469 slots
- `kom1oNHy…` · 662.86 SOL · commission 5% · lag 1905707 slots
- `7ZjHeeYE…` · 176.09 SOL · commission 5% · lag 117746 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 442542223 slots
- `pSo1KZXg…` · 2.00 SOL · commission 4% · lag 204382 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 362868 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 1902224 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 74 | data/history.jsonl snapshot tape |
| TVL chart | 74 | data/history.jsonl snapshot tape |
| SOL chart | 73 | data/history.jsonl snapshot tape |
| history.jsonl rows | 74 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$1.14M** (10,859.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 |
| **Solana REV** | **13,424.0 SOL** / **$1.40M** | MEASURED UTC calendar day 2026-08-27: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 · UTC day 2026-08-27 · SOL-USD date 2026-08-27 |
| Jito tip-floor run-rate (NOT REV) | $139.55K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 139549 USD; at p95 floor → 1488772 USD. |
| Protocol fees 24h | $15.45M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2080 window_seconds=9966 |
| p90 / p99 | 0.000010 / 0.000176 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.55 | coingecko.simple_price |
| 24h change | -3.78% | coingecko.simple_price |
| Market cap | $60.49B | coingecko.simple_price |
| 24h volume | $5.29B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.86B |
| TVL 1d / 7d / 30d | -2.58% / +5.51% / +22.11% |
| DEX volume 24h | $2.62B · 1d -29.33% · vs-7d-ago -27.38% |
| 7d DEX volume | $20.95B · +40.47% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $15.45M |
| Fees 1d / 7d | -5.24% / +15.82% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $576.29M | -60.54% |
| BisonFi | $331.44M | -20.52% |
| Orca DEX | $310.21M | -15.16% |
| Meteora DLMM | $279.39M | +13.80% |
| Raydium AMM | $172.88M | -5.31% |
| Axiom | $165.79M | 0.00% |
| Manifest Trade | $134.91M | -25.71% |
| pump.fun | $117.62M | -18.59% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.59B | -2.67% | +13.02% |
| Kamino Lend | Lending | $1.25B | +0.56% | +3.38% |
| Raydium AMM | Dexs | $1.12B | -4.92% | +7.10% |
| Jupiter Lend | Lending | $1.08B | -2.08% | +1.25% |
| Binance Staked SOL | Liquid Staking | $1.07B | -2.51% | +9.80% |
| Jito Liquid Staking | Liquid Staking | $1.05B | -2.57% | +8.19% |
| BlackRock BUIDL | RWA | $886.54M | +0.01% | +6.05% |
| Jupiter Perpetual Exchange | Derivatives | $767.61M | -2.29% | +0.77% |
| Jupiter Staked SOL | Liquid Staking | $539.95M | -2.57% | +7.05% |
| xStocks | RWA | $432.17M | -1.76% | +1.13% |

## Stablecoins

Solana circulating pegged-USD: **$15.93B**
(1d -0.21% · 7d -0.49%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.04B | -0.33% |
| USDT · Tether | $2.84B | +0.00% |
| USDGO · USDGO | $1.25B | 0.00% |
| USD1 · World Liberty Financial USD | $1.17B | +2.28% |
| BUIDL · BlackRock USD | $886.54M | +0.01% |
| PYUSD · PayPal USD | $693.19M | +0.38% |
| USDG · Global Dollar | $622.50M | +0.31% |
| USDe · Ethena USDe | $535.34M | -0.44% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 10 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 10 · priced-subset mcap $284.63M (lower bound, not a census).
24h volume $32.09M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $432.09M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 10 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.54M
- **xStocks** (RWA) — $432.17M
- **OnRe** (RWA) — $284.63M
- **Ondo Yield Assets** (RWA) — $179.27M
- **Hastra** (RWA) — $157.94M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $24.73M
- **Plume Vaults** (RWA) — $22.87M

## Daily active addresses

837,981 (Allium, as of 2026-08-28). Provider range 399,948–903,429. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: 2,000+ new custom pairs since launch.

New: Launching Solana pairs is now free. The first trade activates the coin.

What we’ve shipped in the past week:

- Custom Pairs on Robinhood, Solana, and Base, powered by @dopplerprotocol 

- Trade coins from major launchpads including @Pumpfun , @ponsdotfamily , and @longdotxyz

- Expanded pair search and sorting on the home page

- Pair rewards can now be claimed from the token page or wallet.](https://x.com/zora/status/2093441769362928019) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 20:53:06 GMT
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
- [The Token Supercycle Is Here: Solana Brings Breakpoint 2026 to London](https://solana.com/news/breakpoint-2026-london-speakers) — solana.com/news · Thu, 27 Aug 2026 04:15:00 GMT
- [Solana Changelog: August 20, 2026](https://solana.com/news/solana-changelog-august-20-2026) — solana.com/news · Mon, 24 Aug 2026 14:19:00 GMT `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: 2,000+ new custom pairs since launch.

New: Launching Solana pairs is now free. The first trade activates the coin.

What we’ve shipped in the past week:

- Custom Pairs on Robinhood, Solana, and Base, powered by @dopplerprotocol 

- Trade coins from major launchpads including @Pumpfun , @ponsdotfamily , and @longdotxyz

- Expanded pair search and sorting on the home page

- Pair rewards can now be claimed from the token page or wallet.](https://x.com/zora/status/2093441769362928019) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 20:53:06 GMT
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

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-29 (2026-08-28 23:48:44 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 616ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 628ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 744ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 695ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 579ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7758ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1150ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 120ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 125ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 392ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 38ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 24ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 969ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 66ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 231ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 47ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 803ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 449ms https://solana.com/data
- `solana.com.databricks` [ok] 200 75ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 371ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 174ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 230ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 241ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 292ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 501ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 145ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 153ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 149ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 911ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2358ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [FAIL] 502 2335ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_devs` [FAIL] 502 787ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 502 Bad Gateway
- `status.incidents` [ok] 200 79ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 545ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 543ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2990ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2515ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2374ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2046ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3150ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2259ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1996ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2062ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2842ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2516ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2249ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2268ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 730ms https://api.mainnet-beta.solana.com — {'code': -32007, 'message': 'Slot 442536979 was skipped, or missing due to ledger jump to recent snapshot'}
- `rpc.getBlock.fallback` [FAIL] 200 94ms https://solana-rpc.publicnode.com — {'code': -32007, 'message': 'Slot 442536979 was skipped, or missing due to ledger jump to recent snapshot'}
- `rpc.getBlock` [ok] 200 2613ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1636ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1362ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 3375ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1443ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1445ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1202ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1490ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1349ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.SPYx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.AMZNx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.AAPLx` [ok] 200 428ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.AMZNx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.GOOGLx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.AAPLx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.MSFTx` [ok] 200 621ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.TSLAx` [ok] 200 649ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.NVDAx` [ok] 200 736ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 766ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.TSLAx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.NVDAx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.NVDAx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.METAx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.BANKCx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SUOPTx` [FAIL]  12016ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MMGx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.TNGYIx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ZHAOMx` [FAIL]  12016ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MMGx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BANKCx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.LAOPGx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.CTINSx` [FAIL]  12015ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.ZHAOMx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.mult.TNGYIx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 1616ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 1475ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.KUNLx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WRFHDx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HAIDLx` [FAIL]  12018ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.KUNLx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HAIDLx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ENNHLx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SZIGHx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 771ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 526ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [FAIL]  12008ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HRZRBx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SMOIHx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 626ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 808ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.CRESBx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CMERPx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CSPCx` [FAIL]  12010ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CRESBx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CRESBx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.CRESMx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CSPCx` [ok] 200 747ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 725ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [FAIL]  12008ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CSPCx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.WXXDCx` [ok] 200 428ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.CMENDx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BDWAPx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CMENDx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.MIXUx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ASMPTx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MIXUx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [FAIL]  12016ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WHRFRx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.SITCx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.JDHLTx` [FAIL]  12012ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ASMPTx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SNDSCx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.CRESPx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PRADx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CRESPx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.SINOTx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CTFJWx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CLONPx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WHGROx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SINOx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SINOTx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 522ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [FAIL]  12011ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CTPCAx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CLPHDx` [FAIL]  12015ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.PWAHLx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.GENTEx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CRAUTx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.GENTEx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.GENTEx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CKAHx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CKAHx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 633ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.CKINFx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CKINFx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.KUAIx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CKINFx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 692ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.NONGx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.COVELx` [FAIL]  12012ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.NONGx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.circ.COVELx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.CHONGx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MEITx` [FAIL]  12009ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.COVELx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 717ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.GEELx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CHONGx` [ok] 200 1085ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.MTRCPx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MTRCPx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 718ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HNDLDx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.price.PICCx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.COSCx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.PICCx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.COSCx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.price.POPMTx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.PICCx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.POPMTx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.mult.POPMTx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.price.BOCOMx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CPETCx` [FAIL]  12018ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.COSCx` [ok] 200 1273ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.circ.CPETCx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.price.BOCHKx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BOCHKx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.mult.CPETCx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.mult.BOCHKx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.price.CITICx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BOCOMx` [ok] 200 640ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.circ.CITICx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.mult.CITICx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.mult.BOCOMx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.price.ANTASx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CRESLx` [FAIL]  12018ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ANTASx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.price.HAIERx` [FAIL]  12009ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CRESLx` [ok] 200 637ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.price.ZJGLDx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CRESLx` [ok] 200 627ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.price.PSBOCx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ICBCx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ZJGLDx` [ok] 200 1799ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.circ.HAIERx` [ok] 200 3177ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.mult.ANTASx` [ok] 200 4311ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.mult.HAIERx` [ok] 200 1430ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.mult.ZJGLDx` [ok] 200 3776ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.circ.PSBOCx` [ok] 200 6688ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.circ.ICBCx` [ok] 200 6998ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.mult.PSBOCx` [ok] 200 521ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `xstocks.mult.ICBCx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1276ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 301ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.MMGx` [ok] 200 55ms https://lite-api.jup.ag/tokens/v2/search?query=MMGx
- `jup.tokens.search.LAOPGx` [ok] 200 51ms https://lite-api.jup.ag/tokens/v2/search?query=LAOPGx
- `jup.tokens.search.ZHAOMx` [ok] 200 51ms https://lite-api.jup.ag/tokens/v2/search?query=ZHAOMx
- `jup.tokens.search.BANKCx` [ok] 200 50ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.TNGYIx` [ok] 200 52ms https://lite-api.jup.ag/tokens/v2/search?query=TNGYIx
- `jup.tokens.search.JDLOGx` [ok] 200 52ms https://lite-api.jup.ag/tokens/v2/search?query=JDLOGx
- `jup.tokens.search.SUOPTx` [ok] 200 60ms https://lite-api.jup.ag/tokens/v2/search?query=SUOPTx
- `jup.tokens.search.CTINSx` [ok] 200 53ms https://lite-api.jup.ag/tokens/v2/search?query=CTINSx
- `jito.tip_floor` [ok] 200 88ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 356ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 73ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 542ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 531ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 748ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 638ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 139ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.6 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
