# Borealis — Solana ecosystem report

**Generated** 2026-08-30T05:48:40Z · 2026-08-29 22:48:40 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-30T05:48:29Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +0.87%; DEX 24h $1.81B · 1d -30% · vs-7d-ago -51%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -30.01%. (threshold: `|1d %| >= 8`)
- **ALERT · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -51.42%. (threshold: `|7d %| >= 20`)
- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -28.99%. (threshold: `|1d %| >= 8`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 105.00 USD is +37.8% vs 30d median 76.20 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Daily active addresses vs 30d median** — Current 837,981.00 is +27.5% vs 30d median 657,422.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 442,803,425 |
| Block height | 420,851,220 |
| Block time | 2026-08-30T05:48:29Z |
| Epoch | 1,025 (0.79% · slot 3,425/432,000) |
| Mean TPS (last ~3,600s) | 3,437.5 |
| Mean non-vote TPS | 1,291.5 |
| Median TPS (same window) | 3,399.7 |
| Mean slot time | 317.0 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 543,331,041,200 |
| Circulating supply | 585,122,456 SOL |
| Total supply | 633,173,916 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 681 |
| Delinquent | 16 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 437,106,417 SOL |
| Delinquent stake | 21,472.26 SOL (0.005%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.25% / 35.54% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.20M SOL | 3.94% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.09M SOL | 3.68% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.39M SOL | 2.83% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.48M SOL | 2.63% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.45M SOL | 2.16% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.13% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.02M SOL | 2.06% | 10% | 0 |
| 8 | `9eGrDohd…` | 7.30M SOL | 1.67% | 5% | 0 |
| 9 | `EvnRmnMr…` | 7.20M SOL | 1.65% | 7% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.11M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.60M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1550746 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 17304 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 123587 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 819671 slots
- `CpdzCVza…` · 315.26 SOL · commission 100% · lag 3074 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 44588 slots
- `HFTcVVrX…` · 152.80 SOL · commission 100% · lag 2968 slots
- `6pEtDovp…` · 131.96 SOL · commission 100% · lag 17352 slots
- `7G4Rfctw…` · 75.85 SOL · commission 100% · lag 41726 slots
- `DZKTNGR3…` · 48.61 SOL · commission 100% · lag 49268 slots
- `As9NxA9b…` · 46.69 SOL · commission 100% · lag 3091 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 442803425 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 167 | data/history.jsonl snapshot tape |
| TVL chart | 167 | data/history.jsonl snapshot tape |
| SOL chart | 166 | data/history.jsonl snapshot tape |
| history.jsonl rows | 167 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$953.12K** (9,080.5 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-28 |
| **Solana REV** | **11,337.8 SOL** / **$1.19M** | MEASURED UTC calendar day 2026-08-28: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-28 · UTC day 2026-08-28 · SOL-USD date 2026-08-28 |
| Jito tip-floor run-rate (NOT REV) | $14.79K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 14787 USD; at p95 floor → 328074 USD. |
| Protocol fees 24h | $11.17M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9968 |
| p90 / p99 | 0.000010 / 0.000106 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $105.00 | coingecko.simple_price |
| 24h change | +0.87% | coingecko.simple_price |
| Market cap | $61.43B | coingecko.simple_price |
| 24h volume | $2.10B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.91B |
| TVL 1d / 7d / 30d | +0.62% / +6.27% / +22.32% |
| DEX volume 24h | $1.81B · 1d -30.01% · vs-7d-ago -51.42% |
| 7d DEX volume | $19.03B · +8.64% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $11.17M |
| Fees 1d / 7d | -28.99% / -7.14% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $584.75M | +1.47% |
| BisonFi | $149.87M | -54.78% |
| Meteora DLMM | $142.97M | -48.83% |
| Orca DEX | $136.20M | -59.80% |
| Axiom | $124.30M | 0.00% |
| Raydium AMM | $113.04M | -35.19% |
| pump.fun | $110.08M | -6.41% |
| Scorch | $98.83M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.60B | +1.04% | +13.47% |
| Kamino Lend | Lending | $1.26B | +0.56% | +5.79% |
| Raydium AMM | Dexs | $1.13B | +1.23% | +9.07% |
| Jupiter Lend | Lending | $1.10B | +0.76% | +4.27% |
| Binance Staked SOL | Liquid Staking | $1.08B | +1.18% | +13.37% |
| Jito Liquid Staking | Liquid Staking | $1.06B | +0.92% | +11.42% |
| BlackRock BUIDL | RWA | $886.54M | 0.00% | +6.05% |
| Jupiter Perpetual Exchange | Derivatives | $771.89M | +0.57% | +4.33% |
| Jupiter Staked SOL | Liquid Staking | $546.57M | +1.23% | +11.68% |
| Marinade Native | Staking Pool | $429.74M | +1.32% | +32.90% |

## Stablecoins

Solana circulating pegged-USD: **$15.90B**
(1d -0.28% · 7d -0.46%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.99B | -0.88% |
| USDT · Tether | $2.84B | -0.00% |
| USDGO · USDGO | $1.25B | 0.00% |
| USD1 · World Liberty Financial USD | $1.18B | +0.96% |
| BUIDL · BlackRock USD | $886.54M | 0.00% |
| PYUSD · PayPal USD | $694.50M | +0.14% |
| USDG · Global Dollar | $621.96M | -0.15% |
| USDe · Ethena USDe | $534.51M | -0.01% |

## Tokenized equities (xStocks)


Listed 715 · Solana deployments 715 · priced 0 · priced-subset mcap — (lower bound, not a census).
24h volume $8.54M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $429.32M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 0 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.54M
- **xStocks** (RWA) — $429.67M
- **OnRe** (RWA) — $284.73M
- **Ondo Yield Assets** (RWA) — $179.18M
- **Hastra** (RWA) — $157.90M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $24.78M
- **Plume Vaults** (RWA) — $22.86M

## Daily active addresses

837,981 (Allium, as of 2026-08-28). Provider range 399,948–896,918. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

_As of 2026-08-30 (2026-08-29 22:48:40 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks market cap** — Listed Solana-deployed xStocks but quote and/or circulating missing. Mcap omitted.
- **xStocks** — priced up to 80 of 715 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.
- **xStocks** — price, circulating-supply, and/or currentMultiplier missing — market cap omitted (never assumed multiplier=1.0)

## Sources this run

- `rpc.getHealth` [ok] 200 126ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 91ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 87ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 91ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 85ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6636ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 170ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 32ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 63ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 34ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 31ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 25ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1019ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 61ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 402ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 45ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 73ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 338ms https://solana.com/data
- `solana.com.databricks` [ok] 200 102ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 494ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 79ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 41ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 165ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 110ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 378ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 147ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 152ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 156ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 2058ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1744ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1772ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1508ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 74ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 102ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 91ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 455ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 454ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 471ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 530ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 505ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 433ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 484ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 451ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 368ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 405ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 442ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 388ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 362ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 435ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1825ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1345ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1915ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1692ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1705ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1938ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1221ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.NVDAx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SPYx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GOOGLx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AAPLx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AMZNx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MSFTx` [FAIL]  12029ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METAx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/METAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.TSLAx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.MSFTx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.NVDAx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 806ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 708ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 547ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.QQQx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.COINx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/COINx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BANKCx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.QQQx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MMGx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SUOPTx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ZHAOMx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BANKCx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.TNGYIx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 750ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [ok] 200 833ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.TNGYIx` [ok] 200 543ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 490ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 725ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.JDLOGx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.JDLOGx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.KUNLx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CTINSx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WRFHDx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [FAIL]  12014ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.KUNLx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CTINSx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ENNHLx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SNBIOx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [FAIL]  12017ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HRZRBx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CRESBx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SMOIHx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.CMERPx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SMOIHx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.CSPCx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CSPCx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CRESMx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CRESBx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CMERPx` [ok] 200 793ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 439ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 1440ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.JTGEXx` [ok] 200 1048ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.WXXDCx` [ok] 200 1523ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 1735ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 1194ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.CMENDx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BDWAPx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MIXUx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ASMPTx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CMENDx` [ok] 200 1144ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 566ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 1130ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [FAIL]  12009ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.BDWAPx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.SITCx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.JDHLTx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SNDSCx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SNDSCx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 2349ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 1310ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 2170ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 999ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.CRESPx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PRADx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SINOTx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SINOTx` [ok] 200 724ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 1159ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 1183ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CLONPx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CTFJWx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.WHGROx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SINOx` [FAIL]  12011ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SINOx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WHGROx` [ok] 200 767ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 819ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 1044ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [FAIL]  12012ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CLPHDx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.PWAHLx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.GENTEx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CLPHDx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WUXIBx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WUXIBx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.GENTEx` [ok] 200 982ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 509ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 676ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CKAHx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SWPRPx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.CKINFx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CKINFx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HKCGAx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.KUAIx` [FAIL]  12018ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.HKCGAx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HKEXCx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.NONGx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.COVELx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.COVELx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.CHONGx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MEITx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.NONGx` [ok] 200 1139ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.GEELx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MEITx` [ok] 200 1032ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 1349ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 3242ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HNDLDx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PICCx` [FAIL]  12011ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MTRCPx` [ok] 200 1211ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.COSCx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.MTRCPx` [ok] 200 696ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 1421ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 1139ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [FAIL]  12010ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.COSCx` [ok] 200 1118ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.price.POPMTx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.POPMTx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.mult.POPMTx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.price.BOCOMx` [FAIL]  12012ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BOCOMx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 1702ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.BOCOMx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.price.CPETCx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CPETCx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.mult.CPETCx` [ok] 200 842ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.price.BOCHKx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BOCHKx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.price.CITICx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ANTASx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ANTASx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.mult.ANTASx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.mult.BOCHKx` [ok] 200 906ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.price.CRESLx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CITICx` [ok] 200 1036ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.mult.CITICx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.price.HAIERx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CRESLx` [ok] 200 871ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.circ.HAIERx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.mult.CRESLx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.price.ZJGLDx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PSBOCx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ZJGLDx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.circ.PSBOCx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.mult.PSBOCx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `xstocks.mult.HAIERx` [ok] 200 915ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.mult.ZJGLDx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.price.ICBCx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ICBCx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.mult.ICBCx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1206ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 178ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.BANKCx` [ok] 200 94ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.ZHAOMx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=ZHAOMx
- `jup.tokens.search.SUOPTx` [ok] 200 98ms https://lite-api.jup.ag/tokens/v2/search?query=SUOPTx
- `jup.tokens.search.TNGYIx` [ok] 200 94ms https://lite-api.jup.ag/tokens/v2/search?query=TNGYIx
- `jup.tokens.search.MMGx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=MMGx
- `jup.tokens.search.LAOPGx` [ok] 200 101ms https://lite-api.jup.ag/tokens/v2/search?query=LAOPGx
- `jup.tokens.search.JDLOGx` [ok] 200 95ms https://lite-api.jup.ag/tokens/v2/search?query=JDLOGx
- `jup.tokens.search.KUNLx` [ok] 200 95ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jito.tip_floor` [ok] 200 265ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 217ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 87ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 200ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 72ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 106ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 139ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 209ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
