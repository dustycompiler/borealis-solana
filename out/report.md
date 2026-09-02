# Borealis — Solana ecosystem report

**Generated** 2026-09-02T01:05:46Z · 2026-09-01 18:05:46 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-02T01:05:36Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h -3.50%; DEX 24h $2.36B · 1d -6% · vs-7d-ago -20%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -3.50%, DeFiLlama TVL 1d -0.82%, DEX 1d -5.72%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 99.66 USD is +30.0% vs 30d median 76.66 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,566,644 |
| Block height | 421,614,144 |
| Block time | 2026-09-02T01:05:36Z |
| Epoch | 1,026 (77.47% · slot 334,649/432,000) |
| Mean TPS (last ~3,600s) | 3,720.0 |
| Mean non-vote TPS | 1,576.7 |
| Median TPS (same window) | 3,665.9 |
| Mean slot time | 315.1 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 544,296,092,137 |
| Circulating supply | 585,206,346 SOL |
| Total supply | 633,266,777 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 678 |
| Delinquent | 16 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 438,032,301 SOL |
| Delinquent stake | 169,518.06 SOL (0.039%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.18% / 35.45% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.17M SOL | 3.92% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.28M SOL | 3.72% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.43M SOL | 2.84% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.48M SOL | 2.62% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.46M SOL | 2.16% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.22M SOL | 1.65% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.93M SOL | 1.58% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.50% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.11M SOL | 1.39% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.95M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.59M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `prt1st4R…` · 115.25K SOL · commission 5% · lag 79702 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 27058 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 2313965 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 217921 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 780523 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 266988 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 128005 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1582890 slots
- `CpdzCVza…` · 212.44 SOL · commission 100% · lag 766293 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 807807 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 766187 slots
- `6pEtDovp…` · 131.86 SOL · commission 100% · lag 780571 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 428 | data/history.jsonl snapshot tape |
| TVL chart | 428 | data/history.jsonl snapshot tape |
| SOL chart | 427 | data/history.jsonl snapshot tape |
| history.jsonl rows | 428 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$701.13K** (6,613.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-30 |
| **Solana REV** | **7,967.3 SOL** / **$844.73K** | MEASURED UTC calendar day 2026-08-30: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-30 · UTC day 2026-08-30 · SOL-USD date 2026-08-30 |
| Jito tip-floor run-rate (NOT REV) | $48.83K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 48835 USD; at p95 floor → 5430582 USD. |
| Protocol fees 24h | $14.36M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9989 |
| p90 / p99 | 0.000014 / 0.000205 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $99.66 | coingecko.simple_price |
| 24h change | -3.50% | coingecko.simple_price |
| Market cap | $58.32B | coingecko.simple_price |
| 24h volume | $3.40B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.66B |
| TVL 1d / 7d / 30d | -0.82% / +1.33% / +19.79% |
| DEX volume 24h | $2.36B · 1d -5.72% · vs-7d-ago -19.65% |
| 7d DEX volume | $15.91B · -27.75% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.36M |
| Fees 1d / 7d | +6.33% / +8.34% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $939.21M | 0.00% |
| Orca DEX | $218.97M | -14.02% |
| BisonFi | $204.83M | -12.03% |
| Raydium AMM | $152.16M | +7.75% |
| Manifest Trade | $147.23M | +12.53% |
| Meteora DLMM | $139.98M | -6.26% |
| Axiom | $113.58M | 0.00% |
| Jupiterz | $101.70M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.52B | -3.86% | +4.16% |
| Kamino Lend | Lending | $1.23B | -2.68% | +4.60% |
| Raydium AMM | Dexs | $1.08B | -2.69% | +0.55% |
| Jupiter Lend | Lending | $1.04B | -1.93% | -1.58% |
| Binance Staked SOL | Liquid Staking | $1.03B | -3.74% | +3.93% |
| Jito Liquid Staking | Liquid Staking | $1.01B | -2.89% | +3.07% |
| BlackRock BUIDL | RWA | $887.01M | -1.38% | -0.87% |
| Jupiter Perpetual Exchange | Derivatives | $743.79M | -3.14% | -0.52% |
| Jupiter Staked SOL | Liquid Staking | $517.69M | -3.09% | +2.51% |
| xStocks | RWA | $432.93M | -2.14% | +0.82% |

## Stablecoins

Solana circulating pegged-USD: **$15.47B**
(1d +0.04% · 7d -1.76%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.65B | -2.33% |
| USDT · Tether | $2.83B | -0.00% |
| USDGO · USDGO | $1.25B | -0.32% |
| USD1 · World Liberty Financial USD | $1.21B | +0.84% |
| BUIDL · BlackRock USD | $887.01M | +0.05% |
| PYUSD · PayPal USD | $737.94M | +6.54% |
| USDG · Global Dollar | $614.92M | +0.70% |
| USDe · Ethena USDe | $537.18M | +0.01% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 71 of 725 Solana-deployed listed symbols (multiplier ok 79/80; 725 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 725 · Solana deployments 725 · priced 71 · priced-subset mcap $284.76M (lower bound, not a census).
24h volume $26.92M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $431.96M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 79 / mcap_computable 71 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 725 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 725 unique underlyings among 725 Solana rows; not every tokenized equity on Solana). 725 of 725 listed xStocks have a Solana deployment (725 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $887.01M
- **xStocks** (RWA) — $432.93M
- **OnRe** (RWA) — $287.93M
- **Ondo Yield Assets** (RWA) — $179.34M
- **Hastra** (RWA) — $153.97M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $24.50M
- **Plume Vaults** (RWA) — $22.88M

## Daily active addresses

791,527 (Allium, as of 2026-08-31). Provider range 394,098–791,527. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: IP Supercycle (real)

Collector sentiment is starting to pick up again, and @opensea is right at the centre of it.

With the Collector Park coming up during NFT NYC, bringing together some of the biggest IPs in the space.

And now, Solana NFTs are officially coming to OpenSea.

The attention is shifting back onchain.

Pivot to NFTs.](https://x.com/shivst3r/status/2094856142123896872) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 18:33:19 GMT
- [RT by @solana: Green Candle Cup https://x.com/i/broadcasts/1rxmqpzvNqwxy](https://x.com/doublezero/status/2094878026781905186) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 20:00:17 GMT
- [RT by @solana: The Green Candle Cup is here, and we’re putting @Solana’s best traders head to head on a live leaderboard.

@solana_sailor just took the 1st place at the @PhoenixTrade competition, but @aut3z wants a rematch. We’ve given them their very own leaderboard for the GCC.

Remember, if you’re not first, you’re last.

Turn notifications on 🔔](https://x.com/doublezero/status/2094871289525649888) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 19:33:30 GMT
- [RT by @solana: Introducing the solmF-ONE Market, curated by @SteakhouseFi.

Tokenized private credit from Fasanara Capital, a London-based, FCA-regulated manager with $5B+ in AUM and a decade-long track record in SME lending, issued by Midas.

Kamino is the home of institutional credit markets.](https://x.com/kamino/status/2094837639346352498) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 17:19:48 GMT
- [OpenSOL is a nice name](https://x.com/solana/status/2094844023974363600) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 17:45:10 GMT
- [RT by @solana: Introducing Cohort 5 of the Solana Incubator.

Our most competitive pool yet — founders building across AI, robotics, and trading on @solana.

Day one of working with these teams:
🟣@clawpumptech
🟣@crowdbrainai
🟣@Lavaragexyz
🟣@morfimarkets
🟣@ownit_xyz
🟣@projectsolo

🧵👇](https://x.com/incubator/status/2094842504025694668) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 17:39:07 GMT
- [RT by @solana: The average active trader pays around $28,400 a year in swap fees. That's 0.85% on every trade, on the wallets everyone uses.

Most people never notice. You probably did, which is why you barely touch the swap tab anymore.

Aurus is live. 0.001 SOL per swap, flat, no matter the size.](https://x.com/aurus/status/2094827630361297199) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 16:40:01 GMT
- [RT by @solana: Week 1 at @cstldao. 🏰

Old walls. New ideas. Runs, cold plunges, BBQs, whiskey, poker, networking and plenty of building.

Big shoutout to all our partners and sponsors:
@solana
@FCATalyst
@jito
@JET_EUROPA_
@EasyA_Kickstart
@ConfirmoPay
@solanamobile
@QUBelfast
@NestiFi_
@post_polar_
@skyrisecreative
@DrNickA
@altitude
@NorioVentures
@BonkAdvisory
@ormeau_labs
@NI_Blockchain
@collym 
IRACE Digital 
Triple Crown Digital](https://x.com/superteamIE/status/2094825108472987758) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 16:30:00 GMT
- [Max transaction size is growing by more than 3x

A new transaction format, Transaction V1 (SIMD-0385), activates on testnet at epoch 1025 raising the transaction size limit from 1,232 to 4,096 bytes.

Use cases like ZK proofs, large multisigs, BLS signatures, and confidential transfers that required multiple transactions now fit in one atomic operation.

In addition to larger max transaction size, Transaction V1 configures transaction resource requests (such as priority fee) in the new V1 header instead of using compute budget instructions.

Transaction V1 is opt-in. Legacy (the original format) and V0 (the format that added address lookup tables) remain supported. Existing apps continue working as is, and can adopt V1 on their own timeline.

RPC operators: update to v4.2.2 or v4.3.0-beta.3 to serve the larger size.](https://x.com/anza_xyz/status/2094913006123761886) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 01 Sep 2026 22:19:16 GMT `upgrade`
- [We're removing floating-point math from Solana's core protocol. Layer by layer.

Layer one: SIMD-0391, activated on mainnet-beta at epoch 1026. It replaces all floating-point (floats) arithmetic in the Stake Program and validator client’s warmup and cooldown logic with fixed-point math.

Layer two: SIMD-0607, now proposed and in review. It targets the runtime itself, removing floats from the inflation rewards and rent calculation path.

Floats can round differently across different hardware, validator clients, and compilers, introducing the possibility of consensus divergence and liveness risk. SIMD-0391 and SIMD-0607 eliminates this by standardizing on fixed-point.

These two improvements aren't the end. Floating-point lives in other, less urgent paths that will transition to fixed-point eventually.](https://x.com/anza_xyz/status/2094509053687091401) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 31 Aug 2026 19:34:07 GMT `upgrade` `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: IP Supercycle (real)

Collector sentiment is starting to pick up again, and @opensea is right at the centre of it.

With the Collector Park coming up during NFT NYC, bringing together some of the biggest IPs in the space.

And now, Solana NFTs are officially coming to OpenSea.

The attention is shifting back onchain.

Pivot to NFTs.](https://x.com/shivst3r/status/2094856142123896872) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 18:33:19 GMT
- [RT by @solana: Green Candle Cup https://x.com/i/broadcasts/1rxmqpzvNqwxy](https://x.com/doublezero/status/2094878026781905186) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 20:00:17 GMT
- [RT by @solana: The Green Candle Cup is here, and we’re putting @Solana’s best traders head to head on a live leaderboard.

@solana_sailor just took the 1st place at the @PhoenixTrade competition, but @aut3z wants a rematch. We’ve given them their very own leaderboard for the GCC.

Remember, if you’re not first, you’re last.

Turn notifications on 🔔](https://x.com/doublezero/status/2094871289525649888) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 19:33:30 GMT
- [RT by @solana: Introducing the solmF-ONE Market, curated by @SteakhouseFi.

Tokenized private credit from Fasanara Capital, a London-based, FCA-regulated manager with $5B+ in AUM and a decade-long track record in SME lending, issued by Midas.

Kamino is the home of institutional credit markets.](https://x.com/kamino/status/2094837639346352498) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 17:19:48 GMT
- [OpenSOL is a nice name](https://x.com/solana/status/2094844023974363600) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 17:45:10 GMT
- [RT by @solana: Introducing Cohort 5 of the Solana Incubator.

Our most competitive pool yet — founders building across AI, robotics, and trading on @solana.

Day one of working with these teams:
🟣@clawpumptech
🟣@crowdbrainai
🟣@Lavaragexyz
🟣@morfimarkets
🟣@ownit_xyz
🟣@projectsolo

🧵👇](https://x.com/incubator/status/2094842504025694668) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 17:39:07 GMT
- [RT by @solana: The average active trader pays around $28,400 a year in swap fees. That's 0.85% on every trade, on the wallets everyone uses.

Most people never notice. You probably did, which is why you barely touch the swap tab anymore.

Aurus is live. 0.001 SOL per swap, flat, no matter the size.](https://x.com/aurus/status/2094827630361297199) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 16:40:01 GMT
- [RT by @solana: Week 1 at @cstldao. 🏰

Old walls. New ideas. Runs, cold plunges, BBQs, whiskey, poker, networking and plenty of building.

Big shoutout to all our partners and sponsors:
@solana
@FCATalyst
@jito
@JET_EUROPA_
@EasyA_Kickstart
@ConfirmoPay
@solanamobile
@QUBelfast
@NestiFi_
@post_polar_
@skyrisecreative
@DrNickA
@altitude
@NorioVentures
@BonkAdvisory
@ormeau_labs
@NI_Blockchain
@collym 
IRACE Digital 
Triple Crown Digital](https://x.com/superteamIE/status/2094825108472987758) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 16:30:00 GMT
- [Max transaction size is growing by more than 3x

A new transaction format, Transaction V1 (SIMD-0385), activates on testnet at epoch 1025 raising the transaction size limit from 1,232 to 4,096 bytes.

Use cases like ZK proofs, large multisigs, BLS signatures, and confidential transfers that required multiple transactions now fit in one atomic operation.

In addition to larger max transaction size, Transaction V1 configures transaction resource requests (such as priority fee) in the new V1 header instead of using compute budget instructions.

Transaction V1 is opt-in. Legacy (the original format) and V0 (the format that added address lookup tables) remain supported. Existing apps continue working as is, and can adopt V1 on their own timeline.

RPC operators: update to v4.2.2 or v4.3.0-beta.3 to serve the larger size.](https://x.com/anza_xyz/status/2094913006123761886) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 01 Sep 2026 22:19:16 GMT `upgrade`
- [We're removing floating-point math from Solana's core protocol. Layer by layer.

Layer one: SIMD-0391, activated on mainnet-beta at epoch 1026. It replaces all floating-point (floats) arithmetic in the Stake Program and validator client’s warmup and cooldown logic with fixed-point math.

Layer two: SIMD-0607, now proposed and in review. It targets the runtime itself, removing floats from the inflation rewards and rent calculation path.

Floats can round differently across different hardware, validator clients, and compilers, introducing the possibility of consensus divergence and liveness risk. SIMD-0391 and SIMD-0607 eliminates this by standardizing on fixed-point.

These two improvements aren't the end. Floating-point lives in other, less urgent paths that will transition to fixed-point eventually.](https://x.com/anza_xyz/status/2094509053687091401) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 31 Aug 2026 19:34:07 GMT `upgrade` `mainnet`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-02 (2026-09-01 18:05:46 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 725 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.
- **xStocks** — WRFHDx multiplier missing — mcap omitted (never assumed 1.0)

## Sources this run

- `rpc.getHealth` [ok] 200 686ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 619ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 740ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 591ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 666ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6975ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1223ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 169ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 169ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 130ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 79ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 883ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 753ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 254ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 294ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 138ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 190ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 699ms https://solana.com/data
- `solana.com.databricks` [ok] 200 227ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 450ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 248ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 137ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 135ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 395ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 683ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 299ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 314ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 301ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 433ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 3164ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1701ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1848ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 204ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 636ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 603ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2422ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2166ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2573ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2868ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2955ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2769ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2408ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3118ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2864ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2314ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2177ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2129ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2938ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2375ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2356ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2361ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2884ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1750ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1873ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2618ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 6353ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 758ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.MSFTx` [ok] 200 577ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.AAPLx` [ok] 200 1104ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.MSFTx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 1306ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.SPYx` [ok] 200 1483ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.mult.MSFTx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.price.NVDAx` [ok] 200 1935ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.NVDAx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.AMZNx` [ok] 200 2177ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.TSLAx` [ok] 200 2938ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.mult.NVDAx` [ok] 200 843ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 1782ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 2268ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.TSLAx` [ok] 200 888ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 498ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.QQQx` [ok] 200 2424ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.AMZNx` [ok] 200 2082ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.GOOGLx` [ok] 200 4376ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.mult.METAx` [ok] 200 1469ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 1844ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.TSLAx` [ok] 200 1105ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 620ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 845ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 1398ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.GOOGLx` [ok] 200 1575ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.KORUx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.price.AXTIx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.MUUx` [ok] 200 1254ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.mult.GOOGLx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.MVLLx` [ok] 200 1727ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.circ.KORUx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.MUUx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 454ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 747ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.AXTIx` [ok] 200 1055ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.SOXSx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.mult.MVLLx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.circ.SOXSx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 2113ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.mult.AXTIx` [ok] 200 700ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.INTWx` [ok] 200 1695ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.SHEINx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.SPYx` [ok] 200 6657ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.SOXSx` [ok] 200 972ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.mult.MUUx` [ok] 200 2318ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.SHEINx` [ok] 200 684ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.QQQx` [ok] 200 5116ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 1481ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.INTWx` [ok] 200 1334ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 653ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.SNXXx` [ok] 200 2541ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.mult.SPYx` [ok] 200 1775ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 934ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 1980ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 1310ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.TNGYIx` [ok] 200 1414ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.QQQx` [ok] 200 1725ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 1874ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 1709ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 1307ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 748ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 1730ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 1219ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.WRFHDx` [ok] 200 829ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.SNXXx` [ok] 200 1762ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 3828ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 2850ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 2835ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 1783ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 1307ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 593ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.CTINSx` [ok] 200 1239ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 5534ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 1179ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 1893ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 859ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.SNBIOx` [ok] 200 2832ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 4492ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 1578ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 1190ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 1479ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 808ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 3138ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.CMERPx` [ok] 200 1149ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 4950ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 1150ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 2709ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.WXXDCx` [ok] 200 821ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.CMENDx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 801ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 1343ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 4063ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.CSPCx` [ok] 200 1464ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 1479ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 6557ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 646ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 650ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 2724ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.WHRFRx` [ok] 200 2140ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.MIXUx` [ok] 200 1067ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 841ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.JDHLTx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 488ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 4823ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 1569ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 6789ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.WHRFRx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 1802ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.PRADx` [ok] 200 1343ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.CRESMx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.PRADx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 748ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 510ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 4422ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.SINOTx` [ok] 200 771ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 697ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 746ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 1032ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 730ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 852ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.CLONPx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 1122ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 5787ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.SINOx` [ok] 200 1495ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.SITCx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 1151ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.SINOTx` [ok] 200 1931ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 3480ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 2073ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.WHGROx` [ok] 200 1506ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 1264ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 439ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 677ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 621ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 1567ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 1256ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 1987ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.SINOx` [ok] 200 965ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 1429ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.HKCGAx` [ok] 200 1175ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 1406ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.HKEXCx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.price.KUAIx` [ok] 200 684ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 1890ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.KUAIx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 833ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 1131ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 872ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.NONGx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.MEITx` [ok] 200 1258ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.mult.HKEXCx` [ok] 200 1049ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 1518ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 4698ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.HNDLDx` [ok] 200 727ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.GENTEx` [ok] 200 654ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 1784ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.CHONGx` [ok] 200 2916ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.GEELx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 1596ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.PICCx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.COVELx` [ok] 200 2594ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 2863ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 1348ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 927ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 1642ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 1396ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 1765ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 4222ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 2479ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.price.POPMTx` [ok] 200 583ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.circ.COSCx` [ok] 200 2939ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 936ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.COVELx` [ok] 200 3872ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 2862ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 762ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 4965ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 6618ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 702ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.POPMTx` [ok] 200 6881ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.mult.POPMTx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1342ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 451ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 146ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 146ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 144ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 143ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 144ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 146ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.CTINSx` [ok] 200 144ms https://lite-api.jup.ag/tokens/v2/search?query=CTINSx
- `jup.tokens.search.KUNLx` [ok] 200 140ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jito.tip_floor` [ok] 200 127ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 379ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 156ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 600ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 628ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 691ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 609ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 171ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
