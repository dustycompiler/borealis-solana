# Borealis — Solana ecosystem report

**Generated** 2026-08-29T22:33:43Z · 2026-08-29 15:33:43 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-29T22:33:32Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +1.34%; DEX 24h $2.59B · 1d -30% · vs-7d-ago -28%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -29.99%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -28.06%. (threshold: `|7d %| >= 20`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 105.18 USD is +38.0% vs 30d median 76.20 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Daily active addresses vs 30d median** — Current 837,981.00 is +27.5% vs 30d median 657,156.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 442,721,161 |
| Block height | 420,768,988 |
| Block time | 2026-08-29T22:33:32Z |
| Epoch | 1,024 (81.75% · slot 353,162/432,000) |
| Mean TPS (last ~3,600s) | 4,089.2 |
| Mean non-vote TPS | 1,926.2 |
| Median TPS (same window) | 4,004.0 |
| Mean slot time | 316.5 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 543,230,093,713 |
| Circulating supply | 584,161,189 SOL |
| Total supply | 633,078,729 SOL |
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

- `mrgn4atx…` · 20.33K SOL · commission 0% · lag 6261 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1468482 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 41323 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 737407 slots
- `kom1oNHy…` · 662.86 SOL · commission 5% · lag 2084645 slots
- `7ZjHeeYE…` · 176.09 SOL · commission 5% · lag 5855 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 442721161 slots
- `pSo1KZXg…` · 2.00 SOL · commission 4% · lag 383320 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 541806 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 2081162 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 138 | data/history.jsonl snapshot tape |
| TVL chart | 138 | data/history.jsonl snapshot tape |
| SOL chart | 137 | data/history.jsonl snapshot tape |
| history.jsonl rows | 138 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$1.14M** (10,859.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 |
| **Solana REV** | **13,424.0 SOL** / **$1.40M** | MEASURED UTC calendar day 2026-08-27: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 · UTC day 2026-08-27 · SOL-USD date 2026-08-27 |
| Jito tip-floor run-rate (NOT REV) | $83.69K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 83688 USD; at p95 floor → 3719654 USD. |
| Protocol fees 24h | $15.73M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9967 |
| p90 / p99 | 0.000013 / 0.000303 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $105.18 | coingecko.simple_price |
| 24h change | +1.34% | coingecko.simple_price |
| Market cap | $61.43B | coingecko.simple_price |
| 24h volume | $2.36B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.91B |
| TVL 1d / 7d / 30d | -1.75% / +6.41% / +23.14% |
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
| Orca DEX | $151.01M | -58.70% |
| Raydium AMM | $129.07M | -29.30% |
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

Solana circulating pegged-USD: **$15.90B**
(1d -0.21% · 7d -0.49%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.00B | -0.85% |
| USDT · Tether | $2.84B | +0.00% |
| USDGO · USDGO | $1.25B | 0.00% |
| USD1 · World Liberty Financial USD | $1.18B | +3.26% |
| BUIDL · BlackRock USD | $886.54M | +0.01% |
| PYUSD · PayPal USD | $694.79M | +0.60% |
| USDG · Global Dollar | $615.96M | -0.77% |
| USDe · Ethena USDe | $534.31M | -0.64% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 70 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 70 · priced-subset mcap $475.34K (lower bound, not a census).
24h volume $18.28M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $433.38M — liquidity census, not mcap, not 24h volume.
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
- [$1B AUM in exactly 10 months for the @Bitwise Solana Staking ETF 🔥](https://x.com/solana/status/2093639798468837752) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 10:00:00 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`
- [7/
Solana's first stake-weighted vote drew participation from hundreds of millions of SOL on each proposal, well above the one-third quorum.

Proposals: https://governance.solana.com

SIMD-0550: https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0550-double-disinflation.md

SIMD-0607: https://github.com/solana-foundation/solana-improvement-documents/pull/607](https://x.com/anza_xyz/status/2093445419502272913) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:37 GMT `upgrade`

### X / announcements (public Nitter-style RSS, not Twitter API)

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
- [$1B AUM in exactly 10 months for the @Bitwise Solana Staking ETF 🔥](https://x.com/solana/status/2093639798468837752) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 10:00:00 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`
- [7/
Solana's first stake-weighted vote drew participation from hundreds of millions of SOL on each proposal, well above the one-third quorum.

Proposals: https://governance.solana.com

SIMD-0550: https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0550-double-disinflation.md

SIMD-0607: https://github.com/solana-foundation/solana-improvement-documents/pull/607](https://x.com/anza_xyz/status/2093445419502272913) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:37 GMT `upgrade`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-29 (2026-08-29 15:33:43 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 127ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 102ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 84ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 143ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 81ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6108ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 189ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 83ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 57ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 50ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 48ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 76ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 41ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 88ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 183ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 50ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 1170ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 554ms https://solana.com/data
- `solana.com.databricks` [ok] 200 49ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 709ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 103ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 87ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 57ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 288ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 807ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 438ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 435ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 454ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1993ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1225ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1431ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1565ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 224ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 79ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 87ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 607ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 489ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 486ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 505ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 495ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 477ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 598ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 492ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 422ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 469ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 530ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 466ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 440ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 618ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1893ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1806ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1912ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2895ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1170ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2060ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2137ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 672ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AAPLx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.TSLAx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SPYx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.NVDAx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MSFTx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AMZNx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GOOGLx` [FAIL]  12029ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METAx` [FAIL]  12029ms https://api.backed.fi/api/v2/public/assets/METAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MSFTx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 456ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 475ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.TSLAx` [ok] 200 929ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 971ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 1002ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.BANKCx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 403ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 1338ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 719ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.MMGx` [ok] 200 634ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 1637ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.WRFHDx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.KUNLx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.CTINSx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 524ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 809ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 646ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 834ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.price.ENNHLx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.SMOIHx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 810ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 2881ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 787ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.JTGEXx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.JTGEXx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 1008ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.CSPCx` [ok] 200 824ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.CRESMx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 1004ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.CMERPx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.MIXUx` [ok] 200 637ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 1014ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.WHRFRx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.MIXUx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 572ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.circ.SITCx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 618ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.PRADx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.CRESPx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.SINOTx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 1020ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.PWAHLx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.SINOx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.CLONPx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 1345ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 684ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.GENTEx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.WHGROx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 903ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 1622ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.SWPRPx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.GENTEx` [ok] 200 879ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.CKAHx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 1124ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.SINOx` [ok] 200 1774ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.KUAIx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 751ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 775ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.GENTEx` [ok] 200 1315ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.COVELx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.circ.COVELx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 800ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 542ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.price.GEELx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.HKEXCx` [ok] 200 1678ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.CHONGx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 890ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 537ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 858ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.QQQx` [FAIL]  12013ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MTRCPx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.HNDLDx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.GEELx` [ok] 200 913ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.COINx` [FAIL]  12012ms https://api.backed.fi/api/v2/public/assets/COINx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MEITx` [ok] 200 731ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.HNDLDx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 895ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.HNDLDx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.price.CPETCx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.mult.GEELx` [ok] 200 684ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.price.BOCHKx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.circ.CKHUTx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 994ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.CPETCx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.price.BOCOMx` [ok] 200 537ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.price.CITICx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.circ.PICCx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.POPMTx` [ok] 200 788ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.circ.BOCOMx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.CPETCx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.circ.POPMTx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.mult.BOCOMx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.price.CRESLx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.mult.POPMTx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.circ.CRESLx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.price.PSBOCx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.price.HAIERx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.price.ANTASx` [ok] 200 526ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.circ.CITICx` [ok] 200 772ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.mult.CRESLx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.price.ZJGLDx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.circ.HAIERx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.circ.PSBOCx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.circ.ANTASx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.mult.CITICx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.price.ICBCx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.mult.COSCx` [ok] 200 1453ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.circ.ZJGLDx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.mult.ANTASx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.mult.PSBOCx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `xstocks.circ.BOCHKx` [ok] 200 1556ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.mult.ZJGLDx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.mult.BOCHKx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.circ.ICBCx` [ok] 200 942ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.mult.HAIERx` [ok] 200 1066ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.mult.ICBCx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1766ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 220ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 118ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 110ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 101ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 109ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 2301ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.SINOTx` [ok] 200 113ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 279ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 212ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 123ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 148ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 92ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 83ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 78ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 202ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
