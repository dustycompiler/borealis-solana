# Borealis — Solana ecosystem report

**Generated** 2026-08-29T21:48:39Z · 2026-08-29 14:48:39 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-29T21:48:28Z · **RPC health** `ok`
**Health score** 96 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +1.39%; DEX 24h $2.59B · 1d -30% · vs-7d-ago -28%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -29.99%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -28.06%. (threshold: `|7d %| >= 20`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 104.99 USD is +37.8% vs 30d median 76.20 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Daily active addresses vs 30d median** — Current 837,981.00 is +27.5% vs 30d median 657,156.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 442,712,631 |
| Block height | 420,760,466 |
| Block time | 2026-08-29T21:48:28Z |
| Epoch | 1,024 (79.78% · slot 344,636/432,000) |
| Mean TPS (last ~3,600s) | 4,021.4 |
| Mean non-vote TPS | 1,850.1 |
| Median TPS (same window) | 3,972.1 |
| Mean slot time | 316.1 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 543,218,896,195 |
| Circulating supply | 584,161,218 SOL |
| Total supply | 633,078,758 SOL |
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
| Activated stake | 435,399,993 SOL |
| Delinquent stake | 734,295.96 SOL (0.168%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 79 |
| Top 10 / 20 stake share | 24.19% / 35.52% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 16.99M SOL | 3.90% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.04M SOL | 3.68% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.39M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.46M SOL | 2.63% | 5% | 0 |
| 5 | `C8Bey3LK…` | 9.29M SOL | 2.13% | 7% | 0 |
| 6 | `E1r4Psq8…` | 9.08M SOL | 2.09% | 0% | 0 |
| 7 | `CAo1dCGY…` | 9.00M SOL | 2.07% | 10% | 0 |
| 8 | `9eGrDohd…` | 7.29M SOL | 1.68% | 5% | 0 |
| 9 | `EvnRmnMr…` | 7.19M SOL | 1.65% | 7% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.41% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.10M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.60M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `6YY2VS44…` · 716.13K SOL · commission 0% · lag 278 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1459952 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 32793 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 728877 slots
- `kom1oNHy…` · 662.86 SOL · commission 5% · lag 2076115 slots
- `pSo1KZXg…` · 2.00 SOL · commission 4% · lag 374790 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 442712631 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 533276 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 2072632 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 135 | data/history.jsonl snapshot tape |
| TVL chart | 135 | data/history.jsonl snapshot tape |
| SOL chart | 134 | data/history.jsonl snapshot tape |
| history.jsonl rows | 135 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$1.14M** (10,859.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 |
| **Solana REV** | **13,424.0 SOL** / **$1.40M** | MEASURED UTC calendar day 2026-08-27: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 · UTC day 2026-08-27 · SOL-USD date 2026-08-27 |
| Jito tip-floor run-rate (NOT REV) | $73.69K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 73691 USD; at p95 floor → 3327085 USD. |
| Protocol fees 24h | $15.73M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9990 |
| p90 / p99 | 0.000015 / 0.000205 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $104.99 | coingecko.simple_price |
| 24h change | +1.39% | coingecko.simple_price |
| Market cap | $61.33B | coingecko.simple_price |
| 24h volume | $2.44B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.91B |
| TVL 1d / 7d / 30d | -1.71% / +6.46% / +23.20% |
| DEX volume 24h | $2.59B · 1d -29.99% · vs-7d-ago -28.06% |
| 7d DEX volume | $21.24B · +42.05% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $15.73M |
| Fees 1d / 7d | -3.52% / +17.92% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $576.29M | -60.54% |
| BisonFi | $331.44M | -20.52% |
| Meteora DLMM | $279.39M | +13.80% |
| Orca DEX | $187.43M | -48.74% |
| Raydium AMM | $132.39M | -27.48% |
| Axiom | $124.30M | -25.03% |
| pump.fun | $117.62M | -18.59% |
| Scorch | $98.83M | -11.31% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.61B | +1.88% | +14.03% |
| Kamino Lend | Lending | $1.26B | +2.78% | +5.74% |
| Raydium AMM | Dexs | $1.14B | +0.07% | +9.98% |
| Jupiter Lend | Lending | $1.10B | +1.24% | +4.50% |
| Binance Staked SOL | Liquid Staking | $1.09B | +1.57% | +14.03% |
| Jito Liquid Staking | Liquid Staking | $1.06B | +1.53% | +11.98% |
| BlackRock BUIDL | RWA | $886.54M | +0.00% | +6.05% |
| Jupiter Perpetual Exchange | Derivatives | $772.82M | +1.20% | +4.23% |
| Jupiter Staked SOL | Liquid Staking | $547.40M | +1.99% | +12.14% |
| xStocks | RWA | $433.46M | +0.52% | +3.70% |

## Stablecoins

Solana circulating pegged-USD: **$15.89B**
(1d -0.21% · 7d -0.49%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.00B | -0.80% |
| USDT · Tether | $2.84B | +0.00% |
| USDGO · USDGO | $1.25B | 0.00% |
| USD1 · World Liberty Financial USD | $1.17B | +2.28% |
| BUIDL · BlackRock USD | $886.54M | +0.01% |
| PYUSD · PayPal USD | $694.77M | +0.60% |
| USDG · Global Dollar | $616.08M | -0.75% |
| USDe · Ethena USDe | $534.28M | -0.64% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 70 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 70 · priced-subset mcap $475.34K (lower bound, not a census).
24h volume $18.41M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $433.46M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 70 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.54M
- **xStocks** (RWA) — $433.46M
- **OnRe** (RWA) — $284.65M
- **Ondo Yield Assets** (RWA) — $179.89M
- **Hastra** (RWA) — $157.92M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $24.76M
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

- [Solana Summer House. Live from LA at 22:00 UTC.
https://x.com/i/broadcasts/1kKzDPlapyeJv](https://x.com/solana/status/2093805895440548150) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 21:00:01 GMT
- [GM](https://x.com/solana/status/2093792801767240094) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 20:07:59 GMT
- [RT by @solana: In partnership with @Solana Summer House and @gmgnai, we’re proud to present the second edition of the Legend Trade Series - the world’s first live competitive trading tournament.

Four traders. Live markets. One winner.

Streaming live today on the Solana, Legend, and GMGN X accounts at 3:00pm PST](https://x.com/legendtrade/status/2093733443901530289) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 16:12:07 GMT
- [RT by @solana: LA, we're ready! Are you?](https://x.com/solanaspaces/status/2093712738916958462) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 14:49:50 GMT
- [RT by @solana: they’re writing about Agentic DeFi on Solana in Yahoo Finance 

bullish on @kamino and @PayBox](https://x.com/moonpay/status/2093709741167907090) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 14:37:56 GMT
- [RT by @solana: JTX hit new volume record today with over $20m. Yesterday was 3rd highest day at $17m. Combined for $41k in fees ($7.5m annualized)

Product is young but early feedback is strong and improves every day. Give @jtx_trade a shot and let us know what you think](https://x.com/brian_smith_0/status/2093461777753477186) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 22:12:37 GMT
- [RT by @solana: Simply speechless.

STARs launch was incredible. Thank you to everyone who showed up, contributed, supported, and helped make this happen.

The future of Argentina couldn’t be in better hands🇦🇷

Official recap video coming soon.](https://x.com/SuperteamAR/status/2093692434408415729) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 13:29:09 GMT
- [Pinned: x.com/i/article/209360567779…](https://x.com/solana/status/2093673446677135865) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 12:13:42 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`
- [7/
Solana's first stake-weighted vote drew participation from hundreds of millions of SOL on each proposal, well above the one-third quorum.

Proposals: https://governance.solana.com

SIMD-0550: https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0550-double-disinflation.md

SIMD-0607: https://github.com/solana-foundation/solana-improvement-documents/pull/607](https://x.com/anza_xyz/status/2093445419502272913) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:37 GMT `upgrade`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [Solana Summer House. Live from LA at 22:00 UTC.
https://x.com/i/broadcasts/1kKzDPlapyeJv](https://x.com/solana/status/2093805895440548150) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 21:00:01 GMT
- [GM](https://x.com/solana/status/2093792801767240094) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 20:07:59 GMT
- [RT by @solana: In partnership with @Solana Summer House and @gmgnai, we’re proud to present the second edition of the Legend Trade Series - the world’s first live competitive trading tournament.

Four traders. Live markets. One winner.

Streaming live today on the Solana, Legend, and GMGN X accounts at 3:00pm PST](https://x.com/legendtrade/status/2093733443901530289) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 16:12:07 GMT
- [RT by @solana: LA, we're ready! Are you?](https://x.com/solanaspaces/status/2093712738916958462) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 14:49:50 GMT
- [RT by @solana: they’re writing about Agentic DeFi on Solana in Yahoo Finance 

bullish on @kamino and @PayBox](https://x.com/moonpay/status/2093709741167907090) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 14:37:56 GMT
- [RT by @solana: JTX hit new volume record today with over $20m. Yesterday was 3rd highest day at $17m. Combined for $41k in fees ($7.5m annualized)

Product is young but early feedback is strong and improves every day. Give @jtx_trade a shot and let us know what you think](https://x.com/brian_smith_0/status/2093461777753477186) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 22:12:37 GMT
- [RT by @solana: Simply speechless.

STARs launch was incredible. Thank you to everyone who showed up, contributed, supported, and helped make this happen.

The future of Argentina couldn’t be in better hands🇦🇷

Official recap video coming soon.](https://x.com/SuperteamAR/status/2093692434408415729) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 13:29:09 GMT
- [Pinned: x.com/i/article/209360567779…](https://x.com/solana/status/2093673446677135865) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 12:13:42 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`
- [7/
Solana's first stake-weighted vote drew participation from hundreds of millions of SOL on each proposal, well above the one-third quorum.

Proposals: https://governance.solana.com

SIMD-0550: https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0550-double-disinflation.md

SIMD-0607: https://github.com/solana-foundation/solana-improvement-documents/pull/607](https://x.com/anza_xyz/status/2093445419502272913) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:37 GMT `upgrade`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-29 (2026-08-29 14:48:39 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 715 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 729ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 719ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 746ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 790ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 722ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7610ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1539ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 139ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 34ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 35ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 31ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 23ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 25ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 69ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 137ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 58ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 97ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 252ms https://solana.com/data
- `solana.com.databricks` [ok] 200 114ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 358ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 59ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 168ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 47ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 90ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 470ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 75ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 69ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 75ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1887ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2503ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2141ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [FAIL] 502 1029ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 502 Bad Gateway
- `status.incidents` [ok] 200 132ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 703ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 724ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2844ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2787ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2898ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3364ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2917ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2900ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3089ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3122ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2883ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2697ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 3069ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2928ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2783ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2889ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1218ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1267ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1225ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1738ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1256ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1102ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1420ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 392ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.NVDAx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GOOGLx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METAx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/METAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MSFTx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AAPLx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SPYx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.TSLAx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AMZNx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.NVDAx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 411ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.SUOPTx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.BANKCx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.MSFTx` [ok] 200 1135ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 878ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 400ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 1542ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.mult.METAx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.TNGYIx` [ok] 200 585ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 605ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 708ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.TNGYIx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 1654ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.price.CTINSx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.BANKCx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.MMGx` [ok] 200 1748ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 1475ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 2265ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.SNBIOx` [ok] 200 633ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.price.HRZRBx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 1469ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.JTGEXx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.CMERPx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.CMERPx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 454ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.BDWAPx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.MIXUx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.CMENDx` [ok] 200 839ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.CRESMx` [ok] 200 1158ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 1511ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 913ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.ASMPTx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 588ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 1129ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 1716ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.CMENDx` [ok] 200 1333ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.SNDSCx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.CMENDx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.PRADx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 960ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.CRESPx` [ok] 200 795ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 1249ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 1021ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 973ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.SINOTx` [ok] 200 1288ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.SNDSCx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.PWAHLx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.SITCx` [ok] 200 760ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 111ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CTPCAx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.GENTEx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.SINOx` [ok] 200 862ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.GENTEx` [ok] 200 484ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 785ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.WHGROx` [ok] 200 1369ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 1188ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 1368ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.price.KUAIx` [ok] 200 786ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.KUAIx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 1060ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 1802ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.KUAIx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.COVELx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.circ.COVELx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.COVELx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.price.MEITx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.mult.CKINFx` [ok] 200 1522ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.CHONGx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.price.GEELx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.mult.CHONGx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.QQQx` [FAIL]  12018ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MTRCPx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.QQQx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 1026ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 1478ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.COINx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/COINx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.QQQx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.MEITx` [ok] 200 714ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.CKHUTx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.WHGROx` [ok] 200 3000ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.BOCOMx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.price.POPMTx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.price.CPETCx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.price.HNDLDx` [ok] 200 487ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.PICCx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.POPMTx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.circ.CPETCx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.circ.BOCOMx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.mult.POPMTx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.mult.BOCOMx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.mult.CPETCx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.price.BOCHKx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.mult.PICCx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.BOCHKx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.price.ANTASx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.circ.ANTASx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.mult.BOCHKx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.mult.ANTASx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 989ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.price.HAIERx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.mult.COSCx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.price.CRESLx` [ok] 200 683ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.price.PSBOCx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.circ.CKHUTx` [ok] 200 1359ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.price.CITICx` [ok] 200 997ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.circ.PSBOCx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.price.ZJGLDx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.mult.PSBOCx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `xstocks.circ.ZJGLDx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.price.ICBCx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.circ.HAIERx` [ok] 200 1165ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.circ.ICBCx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 2511ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.ICBCx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.CRESLx` [ok] 200 1175ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.mult.HAIERx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 2262ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.CITICx` [ok] 200 1158ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.mult.ZJGLDx` [ok] 200 998ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.mult.CITICx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.CRESLx` [ok] 200 734ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 34ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 302ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 47ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 53ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 86ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 79ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 52ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.SINOTx` [ok] 200 54ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 409ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 285ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 61ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 706ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 723ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 790ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 710ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 92ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
