# Borealis — Solana ecosystem report

**Generated** 2026-09-01T12:53:40Z · 2026-09-01 05:53:40 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-01T12:53:29Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -0.64%; DEX 24h $2.50B · 1d +30% · vs-7d-ago -17%; slot 318 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +8.83%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +29.63%. (threshold: `|1d %| >= 8`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 101.96 USD is +33.2% vs 30d median 76.57 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,428,242 |
| Block height | 421,475,829 |
| Block time | 2026-09-01T12:53:29Z |
| Epoch | 1,026 (45.43% · slot 196,243/432,000) |
| Mean TPS (last ~3,600s) | 3,715.7 |
| Mean non-vote TPS | 1,588.4 |
| Median TPS (same window) | 3,604.4 |
| Mean slot time | 317.8 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 544,105,064,499 |
| Circulating supply | 585,206,853 SOL |
| Total supply | 633,267,283 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 679 |
| Delinquent | 15 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 438,147,548 SOL |
| Delinquent stake | 54,271.06 SOL (0.012%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.17% / 35.44% |
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

- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 20303 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 2175563 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 79519 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 642121 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 128586 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 36362 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1444488 slots
- `CpdzCVza…` · 212.44 SOL · commission 100% · lag 627891 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 669405 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 627785 slots
- `6pEtDovp…` · 131.86 SOL · commission 100% · lag 642169 slots
- `7G4Rfctw…` · 75.85 SOL · commission 100% · lag 666543 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 384 | data/history.jsonl snapshot tape |
| TVL chart | 384 | data/history.jsonl snapshot tape |
| SOL chart | 383 | data/history.jsonl snapshot tape |
| history.jsonl rows | 384 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$701.13K** (6,613.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-30 |
| **Solana REV** | **7,967.3 SOL** / **$844.73K** | MEASURED UTC calendar day 2026-08-30: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-30 · UTC day 2026-08-30 · SOL-USD date 2026-08-30 |
| Jito tip-floor run-rate (NOT REV) | $199.31K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 199312 USD; at p95 floor → 15182756 USD. |
| Protocol fees 24h | $13.39M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9965 |
| p90 / p99 | 0.000010 / 0.000191 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $101.96 | coingecko.simple_price |
| 24h change | -0.64% | coingecko.simple_price |
| Market cap | $59.68B | coingecko.simple_price |
| 24h volume | $2.99B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.80B |
| TVL 1d / 7d / 30d | +0.24% / +1.12% / +22.93% |
| DEX volume 24h | $2.50B · 1d +29.63% · vs-7d-ago -16.51% |
| 7d DEX volume | $17.68B · -15.50% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $13.39M |
| Fees 1d / 7d | +8.83% / -7.67% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $939.21M | +28.29% |
| BisonFi | $232.85M | +26.20% |
| Orca DEX | $220.45M | +19.52% |
| Meteora DLMM | $149.33M | +4.67% |
| Manifest Trade | $147.55M | +50.78% |
| Raydium AMM | $127.57M | +24.90% |
| Axiom | $113.58M | +35.58% |
| Jupiterz | $101.70M | +88.90% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.56B | -0.96% | +3.95% |
| Kamino Lend | Lending | $1.24B | -0.24% | +2.11% |
| Raydium AMM | Dexs | $1.12B | +1.78% | +0.91% |
| Jupiter Lend | Lending | $1.08B | -0.61% | -0.80% |
| Binance Staked SOL | Liquid Staking | $1.06B | -1.47% | +4.33% |
| Jito Liquid Staking | Liquid Staking | $1.03B | -0.80% | +3.12% |
| BlackRock BUIDL | RWA | $886.92M | +0.22% | +4.68% |
| Jupiter Perpetual Exchange | Derivatives | $757.21M | -1.16% | -0.76% |
| Jupiter Staked SOL | Liquid Staking | $529.02M | -1.01% | +2.78% |
| xStocks | RWA | $436.66M | +0.83% | +3.46% |

## Stablecoins

Solana circulating pegged-USD: **$15.66B**
(1d +0.05% · 7d -1.75%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.82B | +0.28% |
| USDT · Tether | $2.83B | -0.00% |
| USDGO · USDGO | $1.25B | -0.32% |
| USD1 · World Liberty Financial USD | $1.21B | +0.84% |
| BUIDL · BlackRock USD | $886.92M | +0.04% |
| PYUSD · PayPal USD | $774.47M | +11.79% |
| USDG · Global Dollar | $598.57M | -1.98% |
| USDe · Ethena USDe | $537.33M | +0.02% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 72 of 725 Solana-deployed listed symbols (multiplier ok 80/80; 725 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 725 · Solana deployments 725 · priced 72 · priced-subset mcap $285.34M (lower bound, not a census).
24h volume $26.04M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $436.66M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 72 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 725 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 725 unique underlyings among 725 Solana rows; not every tokenized equity on Solana). 725 of 725 listed xStocks have a Solana deployment (725 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.92M
- **xStocks** (RWA) — $436.66M
- **OnRe** (RWA) — $287.69M
- **Ondo Yield Assets** (RWA) — $179.94M
- **Hastra** (RWA) — $154.26M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $24.69M
- **Plume Vaults** (RWA) — $22.86M

## Daily active addresses

730,181 (Allium, as of 2026-08-30). Provider range 397,651–774,939. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Image](https://x.com/solana/status/2094769019521999135) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 12:47:07 GMT
- [Source: Blockworks https://lightspeed.vip/](https://x.com/solana/status/2094747982650601562) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 11:23:32 GMT
- [BREAKING: Solana processed 5.2B non-vote transactions in August. 

A new ATH, up 19% from July's record](https://x.com/solana/status/2094747980226253257) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 11:23:31 GMT
- [luma.com/breakpoint2026](https://x.com/solana/status/2094700536847294724) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 08:15:00 GMT
- [See you in London in November](https://x.com/solana/status/2094700536591503733) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 08:15:00 GMT
- [RT by @solana: What actually happens after you submit a transaction on Solana?

Well I broke it down for you. 

In just 1 minute you'll be able to understand exactly how Solana transactions work ↓](https://x.com/b_migliaccio/status/2094456121134051645) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 16:03:47 GMT
- [RT by @solana: PreStocks has surpassed 50,000 holders! 🫂📈🎉

OpenAI, Anthropic, Anduril and more. Pre-IPO exposure, once reserved for the wealthy elite, is tradable 24/7 on @Solana.

And we're just getting started 📈](https://x.com/PreStocks/status/2094655201366221145) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 05:14:51 GMT
- [RT by @solana: MetaDAO is rebuilding venture capital for the internet.

Check out our new website to learn more https://metadao.fi](https://x.com/MetaDAOProject/status/2094562367912992986) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 23:05:58 GMT
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

### X / announcements (public Nitter-style RSS, not Twitter API)

- [Image](https://x.com/solana/status/2094769019521999135) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 12:47:07 GMT
- [Source: Blockworks https://lightspeed.vip/](https://x.com/solana/status/2094747982650601562) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 11:23:32 GMT
- [BREAKING: Solana processed 5.2B non-vote transactions in August. 

A new ATH, up 19% from July's record](https://x.com/solana/status/2094747980226253257) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 11:23:31 GMT
- [luma.com/breakpoint2026](https://x.com/solana/status/2094700536847294724) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 08:15:00 GMT
- [See you in London in November](https://x.com/solana/status/2094700536591503733) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 08:15:00 GMT
- [RT by @solana: What actually happens after you submit a transaction on Solana?

Well I broke it down for you. 

In just 1 minute you'll be able to understand exactly how Solana transactions work ↓](https://x.com/b_migliaccio/status/2094456121134051645) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 16:03:47 GMT
- [RT by @solana: PreStocks has surpassed 50,000 holders! 🫂📈🎉

OpenAI, Anthropic, Anduril and more. Pre-IPO exposure, once reserved for the wealthy elite, is tradable 24/7 on @Solana.

And we're just getting started 📈](https://x.com/PreStocks/status/2094655201366221145) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 05:14:51 GMT
- [RT by @solana: MetaDAO is rebuilding venture capital for the internet.

Check out our new website to learn more https://metadao.fi](https://x.com/MetaDAOProject/status/2094562367912992986) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 23:05:58 GMT
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

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-01 (2026-09-01 05:53:40 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~318 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~318 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

## Sources this run

- `rpc.getHealth` [ok] 200 183ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 163ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 246ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 128ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 146ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5242ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 362ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 120ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 230ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 207ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 54ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 63ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 638ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 198ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 237ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 91ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 967ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 406ms https://solana.com/data
- `solana.com.databricks` [ok] 200 211ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 536ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 206ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 196ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 158ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 656ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 636ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 269ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 269ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 281ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 962ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1330ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1675ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1302ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 266ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 142ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 235ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 535ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 518ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 611ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 561ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 593ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 541ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 534ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 559ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 588ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 765ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 503ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 613ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 506ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 545ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1748ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1555ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1839ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1532ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1023ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1307ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1580ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1125ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.NVDAx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.NVDAx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.MSFTx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.GOOGLx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.TSLAx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.AAPLx` [ok] 200 554ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.SPYx` [ok] 200 615ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.METAx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.AAPLx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 674ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.QQQx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 695ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.TSLAx` [ok] 200 1379ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.AMZNx` [ok] 200 1980ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.mult.AAPLx` [ok] 200 1314ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.MVLLx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.mult.SPYx` [ok] 200 1194ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 679ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 1775ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.MUUx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.price.AXTIx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.DRAMx` [ok] 200 835ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.circ.AMZNx` [ok] 200 912ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 2261ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.price.DJTx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.AXTIx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 1260ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 1144ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 656ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.AXTIx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.KORUx` [ok] 200 743ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.DJTx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.DRAMx` [ok] 200 1161ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.INTWx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.circ.MUUx` [ok] 200 1241ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.MUUx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 735ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.circ.INTWx` [ok] 200 508ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.INTWx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 1246ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.price.SHEINx` [ok] 200 1184ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.price.MMGx` [ok] 200 456ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.MVLLx` [ok] 200 1738ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.MMGx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.SOXSx` [ok] 200 1062ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 1546ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.BANKCx` [ok] 200 834ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 427ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 672ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.SNXXx` [ok] 200 795ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 747ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.SOXSx` [ok] 200 987ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.SNBIOx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.CTINSx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 982ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.SHEINx` [ok] 200 1822ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 575ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.HRZRBx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.SMOIHx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.CRESBx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.WRFHDx` [ok] 200 1427ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [ok] 200 456ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.SHEINx` [ok] 200 864ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.CRESMx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.CSPCx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 1068ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 595ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 676ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 808ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.MIXUx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.CRESMx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.ASMPTx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.CMENDx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.MIXUx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.CMERPx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 530ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 897ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.SITCx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 760ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.SNDSCx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.SITCx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.CLONPx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.PRADx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 723ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.CLONPx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.SINOTx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.CLONPx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 706ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 698ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.SINOx` [ok] 200 510ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.CRESPx` [ok] 200 1388ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.WHGROx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.GENTEx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.CRESPx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 789ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.GENTEx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 632ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 551ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.CKAHx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.HKCGAx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 710ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 506ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 1059ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.COVELx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.CKINFx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.mult.CKAHx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.circ.COVELx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 648ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.price.MEITx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.GEELx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.CHONGx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.MEITx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 1000ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.WHGROx` [ok] 200 1813ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.KUAIx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.mult.COVELx` [ok] 200 803ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.CHONGx` [ok] 200 484ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.price.POPMTx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.circ.COSCx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.POPMTx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.POPMTx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 1115ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.CKHUTx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 796ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 1400ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1316ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 264ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 126ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 149ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 124ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 130ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 133ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 163ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.CTINSx` [ok] 200 120ms https://lite-api.jup.ag/tokens/v2/search?query=CTINSx
- `jup.tokens.search.KUNLx` [ok] 200 129ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jito.tip_floor` [ok] 200 127ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 347ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 123ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 106ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 161ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 162ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 103ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 137ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
