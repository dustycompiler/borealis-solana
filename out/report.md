# Borealis — Solana ecosystem report

**Generated** 2026-09-03T00:10:49Z · 2026-09-02 17:10:49 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-03T00:10:40Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +0.05%; DEX 24h $2.17B · 1d -13% · vs-7d-ago -26%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -13.19%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -26.01%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 840,200.00 is +26.5% vs 30d median 664,014.50 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 100.08 USD is +29.2% vs 30d median 77.46 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,830,501 |
| Block height | 421,877,779 |
| Block time | 2026-09-03T00:10:40Z |
| Epoch | 1,027 (38.54% · slot 166,504/432,000) |
| Mean TPS (last ~3,600s) | 3,525.5 |
| Mean non-vote TPS | 1,384.2 |
| Median TPS (same window) | 3,478.4 |
| Mean slot time | 314.5 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 544,607,809,451 |
| Circulating supply | 585,275,278 SOL |
| Total supply | 633,361,309 SOL |
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
| Activated stake | 438,220,370 SOL |
| Delinquent stake | 201,987.05 SOL (0.046%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.25% / 35.53% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.35M SOL | 3.96% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.33M SOL | 3.73% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.46M SOL | 2.84% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.30M SOL | 2.58% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.18% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.22M SOL | 1.65% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.13M SOL | 1.63% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.50% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.95M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.61M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `xLabscif…` · 84.41K SOL · commission 5% · lag 42128 slots
- `prt1st4R…` · 78.62K SOL · commission 5% · lag 343559 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 166251 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 481778 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1044380 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 530845 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 391862 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1846747 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1030150 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1071664 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 1030044 slots
- `6pEtDovp…` · 131.86 SOL · commission 100% · lag 1044428 slots

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
| **In-protocol fees 24h** | **$915.85K** (9,030.4 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-01 |
| **Solana REV** | **10,924.9 SOL** / **$1.11M** | MEASURED UTC calendar day 2026-09-01: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-01 · UTC day 2026-09-01 · SOL-USD date 2026-09-01 |
| Jito tip-floor run-rate (NOT REV) | $27.88K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 27883 USD; at p95 floor → 497862 USD. |
| Protocol fees 24h | $12.65M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9989 |
| p90 / p99 | 0.000011 / 0.000143 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $100.08 | coingecko.simple_price |
| 24h change | +0.05% | coingecko.simple_price |
| Market cap | $58.59B | coingecko.simple_price |
| 24h volume | $2.85B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.68B |
| TVL 1d / 7d / 30d | -5.01% / +1.39% / +19.87% |
| DEX volume 24h | $2.17B · 1d -13.19% · vs-7d-ago -26.01% |
| 7d DEX volume | $16.92B · -23.18% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $12.65M |
| Fees 1d / 7d | -6.15% / -4.62% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $827.37M | -11.91% |
| BisonFi | $204.83M | -12.03% |
| Orca DEX | $201.05M | -21.05% |
| Manifest Trade | $171.65M | +31.20% |
| Meteora DLMM | $139.98M | -6.26% |
| Raydium AMM | $117.02M | -17.13% |
| Axiom | $97.98M | -13.74% |
| Scorch | $64.72M | -14.96% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.52B | -0.66% | +2.32% |
| Kamino Lend | Lending | $1.23B | -0.05% | +3.47% |
| Raydium AMM | Dexs | $1.07B | -2.60% | +1.20% |
| Jupiter Lend | Lending | $1.06B | +0.52% | +0.02% |
| Binance Staked SOL | Liquid Staking | $1.03B | +0.33% | +2.65% |
| Jito Liquid Staking | Liquid Staking | $1.00B | -0.19% | +2.33% |
| BlackRock BUIDL | RWA | $890.69M | +0.11% | -1.06% |
| Jupiter Perpetual Exchange | Derivatives | $741.08M | -0.36% | -1.38% |
| Jupiter Staked SOL | Liquid Staking | $514.17M | -0.83% | +1.88% |
| xStocks | RWA | $434.66M | +0.40% | +1.82% |

## Stablecoins

Solana circulating pegged-USD: **$15.67B**
(1d -0.77% · 7d -1.85%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.73B | +0.03% |
| USDT · Tether | $2.90B | +2.49% |
| USDGO · USDGO | $1.25B | +0.81% |
| USD1 · World Liberty Financial USD | $1.21B | -0.00% |
| BUIDL · BlackRock USD | $890.69M | +0.43% |
| PYUSD · PayPal USD | $804.13M | +3.86% |
| USDG · Global Dollar | $608.87M | -0.46% |
| USDe · Ethena USDe | $536.00M | -0.24% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 72 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 72 · priced-subset mcap $286.35M (lower bound, not a census).
24h volume $28.00M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $434.66M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 72 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $890.69M
- **xStocks** (RWA) — $434.66M
- **OnRe** (RWA) — $288.74M
- **Ondo Yield Assets** (RWA) — $179.88M
- **Hastra** (RWA) — $153.64M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $24.94M
- **Plume Vaults** (RWA) — $22.89M

## Daily active addresses

840,200 (Allium, as of 2026-09-01). Provider range 418,283–917,329. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @anza_xyz: 🚨ATTENTION: large transactions have hit the testnet

https://explorer.solana.com/tx/5KxbxQxkqv2gPjRArDeFJSmfhG6X1vAbEjZFn5zGPsmLvsb4FYKbYTm7BBDSNarkEt2jL5878wmJ4cTYyvURPLnK?cluster=testnet](https://x.com/bw_solana/status/2095199360724431064) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 17:17:09 GMT `upgrade`
- [RT by @anza_xyz: Solana is the financial infra powering the token supercycle. 

We're building toward a future where the internet capital market becomes the biggest capital market.

More thoughts here:

https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/calilyliu/status/2095179874839462349) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 15:59:43 GMT
- [RT by @anza_xyz: V1 Transactions are coming to @solana and they are really cool! They will go live in a couple of weeks.

Max transaction size goes from 1,232 → 4,096 bytes. Compute budgeting moves out of instructions and into the transaction itself.

There are a few small breaking changes you need to be aware, and you can start testing locally today.  🧵](https://x.com/a_milz/status/2091903273632731271) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 24 Aug 2026 14:59:40 GMT
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
- [RT by @anza_xyz: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`
- [7/
Solana's first stake-weighted vote drew participation from hundreds of millions of SOL on each proposal, well above the one-third quorum.

Proposals: https://governance.solana.com

SIMD-0550: https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0550-double-disinflation.md

SIMD-0607: https://github.com/solana-foundation/solana-improvement-documents/pull/607](https://x.com/anza_xyz/status/2093445419502272913) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:37 GMT `upgrade`
- [The Token Supercycle: Everything of Value is Becoming Programmable](https://solana.com/news/the-token-supercycle-oped) — solana.com/news · Wed, 02 Sep 2026 09:00:00 GMT
- [Solana Changelog: August 27, 2026](https://solana.com/news/solana-changelog-august-27-2026) — solana.com/news · Fri, 28 Aug 2026 16:00:00 GMT `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @anza_xyz: 🚨ATTENTION: large transactions have hit the testnet

https://explorer.solana.com/tx/5KxbxQxkqv2gPjRArDeFJSmfhG6X1vAbEjZFn5zGPsmLvsb4FYKbYTm7BBDSNarkEt2jL5878wmJ4cTYyvURPLnK?cluster=testnet](https://x.com/bw_solana/status/2095199360724431064) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 17:17:09 GMT `upgrade`
- [RT by @anza_xyz: Solana is the financial infra powering the token supercycle. 

We're building toward a future where the internet capital market becomes the biggest capital market.

More thoughts here:

https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/calilyliu/status/2095179874839462349) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 15:59:43 GMT
- [RT by @anza_xyz: V1 Transactions are coming to @solana and they are really cool! They will go live in a couple of weeks.

Max transaction size goes from 1,232 → 4,096 bytes. Compute budgeting moves out of instructions and into the transaction itself.

There are a few small breaking changes you need to be aware, and you can start testing locally today.  🧵](https://x.com/a_milz/status/2091903273632731271) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 24 Aug 2026 14:59:40 GMT
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
- [RT by @anza_xyz: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`
- [7/
Solana's first stake-weighted vote drew participation from hundreds of millions of SOL on each proposal, well above the one-third quorum.

Proposals: https://governance.solana.com

SIMD-0550: https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0550-double-disinflation.md

SIMD-0607: https://github.com/solana-foundation/solana-improvement-documents/pull/607](https://x.com/anza_xyz/status/2093445419502272913) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:37 GMT `upgrade`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-03 (2026-09-02 17:10:49 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 726ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 525ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 594ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 672ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 546ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6779ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1341ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 145ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 48ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 240ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 46ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 83ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 43ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 125ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 155ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 88ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 126ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 236ms https://solana.com/data
- `solana.com.databricks` [ok] 200 117ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 643ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 115ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 107ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 110ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 280ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 488ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 97ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 95ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 94ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [FAIL] 404 1970ms https://nitter.perennialte.ch/solana/rss — HTTP 404 Not Found
- `rss.nitter.solana_status` [ok] 200 1728ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1838ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 927ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 258ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 159ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 675ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 549ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2513ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1852ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2231ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2856ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2279ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2648ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2132ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2821ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1887ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2672ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1879ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2483ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1900ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2354ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 7401ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2752ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 4344ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 3054ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 5597ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2368ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2619ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 991ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AAPLx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.METAx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.GOOGLx` [ok] 200 428ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.AMZNx` [ok] 200 742ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.METAx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.TSLAx` [ok] 200 945ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.mult.METAx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.SPYx` [ok] 200 1176ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.TSLAx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 986ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 727ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 1015ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.DRAMx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.MSFTx` [ok] 200 2235ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.MVLLx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.QQQx` [ok] 200 1456ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.COINx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 771ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 1326ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 997ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.price.MUUx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.price.NVDAx` [ok] 200 4000ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.MUUx` [ok] 200 648ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 1019ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.NVDAx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 1409ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 4253ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.MUUx` [ok] 200 422ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.KORUx` [ok] 200 1261ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.price.INTWx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.mult.NVDAx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 2446ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.mult.AAPLx` [ok] 200 653ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.NWGx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.price.SOXSx` [ok] 200 1296ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.AXTIx` [ok] 200 2941ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.circ.DJTx` [ok] 200 2084ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.circ.AXTIx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.circ.NWGx` [ok] 200 1159ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.circ.SOXSx` [ok] 200 670ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.INTWx` [ok] 200 2047ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.mult.NWGx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 513ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.KORUx` [ok] 200 2555ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 984ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 761ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.BANKCx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 2726ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 1152ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.SHEINx` [ok] 200 3204ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 589ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.INTWx` [ok] 200 1519ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.SHEINx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.SNXXx` [ok] 200 897ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.CTINSx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 844ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.SHEINx` [ok] 200 1064ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 2023ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.KUNLx` [ok] 200 802ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 1179ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 3248ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 3324ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.HAIDLx` [ok] 200 536ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.KUNLx` [ok] 200 902ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 2325ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 1734ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 997ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 807ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 741ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 1630ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.MMGx` [ok] 200 4774ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 815ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 823ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.CMERPx` [ok] 200 514ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.LAOPGx` [ok] 200 5275ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 1265ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 532ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 1286ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 3649ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.CRESMx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 1572ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 649ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 3051ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 941ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 2356ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.CSPCx` [ok] 200 3077ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 1275ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.CRESMx` [ok] 200 1783ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 1962ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 1209ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 2384ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 2713ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 1184ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.MIXUx` [ok] 200 3104ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.WXXDCx` [ok] 200 3786ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 986ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 7752ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.SITCx` [ok] 200 1255ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.CRESPx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.JDHLTx` [ok] 200 1119ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 911ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 645ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 820ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.PRADx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 2160ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 2150ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 678ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 2342ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 2091ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 831ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 574ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 3483ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 411ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.WHGROx` [ok] 200 1202ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.CLONPx` [ok] 200 1205ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 803ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.SINOx` [ok] 200 993ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.WHGROx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 953ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 1352ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 1767ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 992ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.GENTEx` [ok] 200 1295ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 1732ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.WUXIBx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.SINOTx` [ok] 200 5197ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 660ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 4925ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 919ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 1689ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 4039ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.CMENDx` [FAIL]  12033ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.SINOTx` [ok] 200 2109ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 1697ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 3063ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.CMENDx` [ok] 200 703ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 841ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 1582ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 2625ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 920ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 2784ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 1149ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.HKEXCx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 556ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 1173ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 1533ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 2920ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.CKINFx` [ok] 200 1979ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 2242ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 2021ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 1026ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.COVELx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.circ.KUAIx` [ok] 200 3025ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 1267ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.mult.KUAIx` [ok] 200 1113ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.CHONGx` [ok] 200 2536ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 2691ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 3429ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.price.MTRCPx` [ok] 200 1747ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.COVELx` [ok] 200 3591ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 4027ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.CKAHx` [ok] 200 8481ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 1297ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.circ.CHONGx` [ok] 200 2941ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 2985ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 2060ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 1250ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.CKHUTx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.PICCx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 755ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.MEITx` [ok] 200 2454ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.HNDLDx` [ok] 200 3751ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.CHONGx` [ok] 200 1362ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 5136ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 1265ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 1102ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 1715ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 2012ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 4178ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 1576ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 9843ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 62ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 283ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.HKEXCx` [ok] 200 75ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MEITx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 58ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.MIXUx` [ok] 200 58ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.BANKCx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.CTINSx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=CTINSx
- `jup.tokens.search.SINOTx` [ok] 200 89ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 2431ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 343ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 58ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 702ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 514ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 636ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 514ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 181ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
