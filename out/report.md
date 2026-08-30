# Borealis — Solana ecosystem report

**Generated** 2026-08-30T01:18:50Z · 2026-08-29 18:18:50 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-30T01:18:40Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +1.25%; DEX 24h $1.81B · 1d -30% · vs-7d-ago -51%; slot 318 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -29.96%. (threshold: `|1d %| >= 8`)
- **ALERT · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -51.39%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -8.39%. (threshold: `|1d %| >= 8`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 105.17 USD is +38.0% vs 30d median 76.20 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Daily active addresses vs 30d median** — Current 837,981.00 is +27.5% vs 30d median 657,156.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 442,752,374 |
| Block height | 420,800,181 |
| Block time | 2026-08-30T01:18:40Z |
| Epoch | 1,024 (88.98% · slot 384,378/432,000) |
| Mean TPS (last ~3,600s) | 4,106.6 |
| Mean non-vote TPS | 1,952.9 |
| Median TPS (same window) | 4,077.7 |
| Mean slot time | 317.7 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 543,270,917,710 |
| Circulating supply | 585,036,082 SOL |
| Total supply | 633,078,622 SOL |
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
| Activated stake | 436,095,791 SOL |
| Delinquent stake | 38,497.86 SOL (0.009%) |
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

- `mrgn4atx…` · 20.33K SOL · commission 0% · lag 37474 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1499695 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 72536 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 768620 slots
- `kom1oNHy…` · 662.86 SOL · commission 5% · lag 2115858 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 442752374 slots
- `pSo1KZXg…` · 2.00 SOL · commission 4% · lag 414533 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 573019 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 2112375 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 149 | data/history.jsonl snapshot tape |
| TVL chart | 149 | data/history.jsonl snapshot tape |
| SOL chart | 148 | data/history.jsonl snapshot tape |
| history.jsonl rows | 149 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$1.14M** (10,859.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 |
| **Solana REV** | **13,424.0 SOL** / **$1.40M** | MEASURED UTC calendar day 2026-08-27: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 · UTC day 2026-08-27 · SOL-USD date 2026-08-27 |
| Jito tip-floor run-rate (NOT REV) | $44.08K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 44079 USD; at p95 floor → 13308944 USD. |
| Protocol fees 24h | $14.41M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9957 |
| p90 / p99 | 0.000010 / 0.000105 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $105.17 | coingecko.simple_price |
| 24h change | +1.25% | coingecko.simple_price |
| Market cap | $61.54B | coingecko.simple_price |
| 24h volume | $2.24B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.89B |
| TVL 1d / 7d / 30d | -0.00% / +5.91% / +21.91% |
| DEX volume 24h | $1.81B · 1d -29.96% · vs-7d-ago -51.39% |
| 7d DEX volume | $19.03B · +8.65% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.41M |
| Fees 1d / 7d | -8.39% / +19.79% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $584.75M | +1.47% |
| BisonFi | $149.87M | -54.78% |
| Orca DEX | $145.33M | -57.11% |
| Meteora DLMM | $142.97M | -48.83% |
| Axiom | $124.30M | 0.00% |
| Raydium AMM | $119.67M | -31.39% |
| pump.fun | $110.08M | -6.41% |
| Scorch | $98.83M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.61B | +1.64% | +15.33% |
| Kamino Lend | Lending | $1.26B | +2.40% | +6.36% |
| Raydium AMM | Dexs | $1.14B | +0.07% | +9.98% |
| Binance Staked SOL | Liquid Staking | $1.09B | +1.46% | +15.28% |
| Jupiter Lend | Lending | $1.07B | -1.80% | +3.18% |
| Jito Liquid Staking | Liquid Staking | $1.06B | +1.49% | +13.25% |
| BlackRock BUIDL | RWA | $886.54M | 0.00% | +6.05% |
| Jupiter Perpetual Exchange | Derivatives | $773.76M | +0.70% | +5.10% |
| Jupiter Staked SOL | Liquid Staking | $548.54M | +1.83% | +13.37% |
| xStocks | RWA | $433.90M | +0.42% | +3.90% |

## Stablecoins

Solana circulating pegged-USD: **$15.90B**
(1d -0.21% · 7d -0.49%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.00B | -0.84% |
| USDT · Tether | $2.84B | +0.00% |
| USDGO · USDGO | $1.25B | 0.00% |
| USD1 · World Liberty Financial USD | $1.18B | +3.26% |
| BUIDL · BlackRock USD | $886.54M | +0.01% |
| PYUSD · PayPal USD | $694.54M | +0.56% |
| USDG · Global Dollar | $615.70M | -0.81% |
| USDe · Ethena USDe | $534.51M | -0.60% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 70 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 70 · priced-subset mcap $475.34K (lower bound, not a census).
24h volume $18.67M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $434.42M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 70 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.54M
- **xStocks** (RWA) — $433.90M
- **OnRe** (RWA) — $284.65M
- **Ondo Yield Assets** (RWA) — $179.56M
- **Hastra** (RWA) — $157.91M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $24.78M
- **Plume Vaults** (RWA) — $22.86M

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

- [Solana development will never be the same](https://x.com/solana/status/2093829689857220905) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 22:34:34 GMT `upgrade`
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

- [Solana development will never be the same](https://x.com/solana/status/2093829689857220905) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 22:34:34 GMT `upgrade`
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

_As of 2026-08-30 (2026-08-29 18:18:50 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 715 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 573ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 537ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 542ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 744ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 544ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6685ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1097ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 69ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 55ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 383ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 22ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 40ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 29ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 62ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 232ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 50ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 73ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 235ms https://solana.com/data
- `solana.com.databricks` [ok] 200 136ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 508ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 178ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 55ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 60ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 206ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 350ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 67ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 76ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 77ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 3885ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2252ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1463ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1374ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 91ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 532ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 615ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2161ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2102ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2907ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2468ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2145ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2154ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2688ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2524ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2180ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2140ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2512ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2303ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2875ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2170ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1195ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1074ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2255ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1489ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1184ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1478ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1395ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.NVDAx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SPYx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METAx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/METAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GOOGLx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AAPLx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.TSLAx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MSFTx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AMZNx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AAPLx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.SPYx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.TNGYIx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.NVDAx` [ok] 200 699ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 939ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 871ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 1044ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.CTINSx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 727ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.KUNLx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.KUNLx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 1435ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 857ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 947ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 1061ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.price.SNBIOx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.HRZRBx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 1109ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.ENNHLx` [ok] 200 1254ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 1135ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 697ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 1420ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 1897ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 838ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 1154ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 825ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.CMENDx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.CMENDx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 730ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.CMERPx` [ok] 200 2233ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 861ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 1282ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.CMERPx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 621ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 2287ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.ASMPTx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 763ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 503ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.price.SITCx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 1220ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.SITCx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 1149ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 640ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 403ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 826ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.mult.CRESMx` [ok] 200 580ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.CRESPx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.SNDSCx` [ok] 200 770ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.CRESPx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.PRADx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 638ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.SINOx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.CTPCAx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 513ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 110ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 567ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 795ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.WHGROx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.SINOx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 982ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.GENTEx` [ok] 200 787ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 899ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.CKAHx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.WUXIBx` [ok] 200 1254ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 747ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 1938ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 1478ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 985ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 1008ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.circ.NONGx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.QQQx` [FAIL]  12017ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.KUAIx` [ok] 200 652ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.COVELx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.COINx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/COINx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.QQQx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 1384ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.COVELx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.MTRCPx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.MEITx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 411ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 2184ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.circ.MTRCPx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.HNDLDx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.HNDLDx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.CHONGx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.POPMTx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.mult.HKEXCx` [ok] 200 1300ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.price.CPETCx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.price.BOCOMx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.price.CKHUTx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.PICCx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.POPMTx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.price.CITICx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.circ.CPETCx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.POPMTx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 936ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.CITICx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.circ.BOCOMx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.price.ANTASx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.mult.CITICx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.circ.ANTASx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.CRESLx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.price.ZJGLDx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.mult.GEELx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.BOCOMx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.price.BOCHKx` [ok] 200 574ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.circ.CRESLx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.price.HAIERx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.mult.ANTASx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.mult.CRESLx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.circ.HAIERx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.price.ICBCx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.mult.HAIERx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.mult.CPETCx` [ok] 200 775ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.circ.BOCHKx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.price.PSBOCx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.mult.BOCHKx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.circ.PSBOCx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.circ.ICBCx` [ok] 200 818ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.mult.ICBCx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `xstocks.circ.ZJGLDx` [ok] 200 1379ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.mult.PSBOCx` [ok] 200 832ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `xstocks.mult.ZJGLDx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1143ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 181ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 38ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 41ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 51ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 45ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.SINOTx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 165ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 439ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 63ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 525ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 531ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 535ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 536ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 132ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
