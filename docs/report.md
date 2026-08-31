# Borealis — Solana ecosystem report

**Generated** 2026-08-31T13:33:39Z · 2026-08-31 06:33:39 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-31T13:33:29Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -3.62%; DEX 24h $1.93B · 1d +16% · vs-7d-ago -34%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -34.34%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +8.73%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +15.50%. (threshold: `|1d %| >= 8`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 102.83 USD is +34.3% vs 30d median 76.57 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,163,758 |
| Block height | 421,211,429 |
| Block time | 2026-08-31T13:33:29Z |
| Epoch | 1,025 (84.20% · slot 363,759/432,000) |
| Mean TPS (last ~3,600s) | 3,955.8 |
| Mean non-vote TPS | 1,821.0 |
| Median TPS (same window) | 3,971.1 |
| Mean slot time | 316.7 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 543,771,743,821 |
| Circulating supply | 585,121,077 SOL |
| Total supply | 633,172,761 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 679 |
| Delinquent | 18 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 437,082,504 SOL |
| Delinquent stake | 45,385.49 SOL (0.010%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.26% / 35.54% |
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

- `mrgn4atx…` · 21.79K SOL · commission 0% · lag 181975 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1911079 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 377637 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 244333 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 12922 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1180004 slots
- `CpdzCVza…` · 315.26 SOL · commission 100% · lag 363407 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 404921 slots
- `HFTcVVrX…` · 152.80 SOL · commission 100% · lag 363301 slots
- `6pEtDovp…` · 131.96 SOL · commission 100% · lag 377685 slots
- `7G4Rfctw…` · 75.85 SOL · commission 100% · lag 402059 slots
- `DZKTNGR3…` · 48.61 SOL · commission 100% · lag 409601 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 294 | data/history.jsonl snapshot tape |
| TVL chart | 294 | data/history.jsonl snapshot tape |
| SOL chart | 293 | data/history.jsonl snapshot tape |
| history.jsonl rows | 294 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$814.10K** (7,855.5 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-29 |
| **Solana REV** | **9,341.6 SOL** / **$968.12K** | MEASURED UTC calendar day 2026-08-29: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-29 · UTC day 2026-08-29 · SOL-USD date 2026-08-29 |
| Jito tip-floor run-rate (NOT REV) | $26.86K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 26857 USD; at p95 floor → 930017 USD. |
| Protocol fees 24h | $12.19M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9964 |
| p90 / p99 | 0.000010 / 0.000098 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $102.83 | coingecko.simple_price |
| 24h change | -3.62% | coingecko.simple_price |
| Market cap | $60.19B | coingecko.simple_price |
| 24h volume | $3.76B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.83B |
| TVL 1d / 7d / 30d | -1.36% / +4.83% / +22.71% |
| DEX volume 24h | $1.93B · 1d +15.50% · vs-7d-ago -34.34% |
| 7d DEX volume | $18.17B · -6.33% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $12.19M |
| Fees 1d / 7d | +8.73% / -3.85% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $732.11M | +25.20% |
| Orca DEX | $258.15M | +77.63% |
| BisonFi | $184.51M | +23.11% |
| Meteora DLMM | $142.67M | -0.21% |
| Manifest Trade | $130.72M | +50.73% |
| Raydium AMM | $111.86M | -8.39% |
| pump.fun | $91.65M | -16.74% |
| Axiom | $83.77M | -19.18% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.59B | -1.04% | +11.99% |
| Kamino Lend | Lending | $1.25B | -0.80% | +4.71% |
| Raydium AMM | Dexs | $1.11B | -1.92% | +6.86% |
| Jupiter Lend | Lending | $1.09B | -0.68% | +2.81% |
| Binance Staked SOL | Liquid Staking | $1.07B | -0.73% | +11.50% |
| Jito Liquid Staking | Liquid Staking | $1.05B | -1.07% | +9.97% |
| BlackRock BUIDL | RWA | $886.54M | 0.00% | +6.05% |
| Jupiter Perpetual Exchange | Derivatives | $766.07M | -0.67% | +3.03% |
| Jupiter Staked SOL | Liquid Staking | $538.57M | -0.99% | +9.84% |
| xStocks | RWA | $433.08M | +2.49% | +3.22% |

## Stablecoins

Solana circulating pegged-USD: **$15.70B**
(1d -1.09% · 7d -2.05%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.78B | -3.16% |
| USDT · Tether | $2.83B | -0.00% |
| USDGO · USDGO | $1.24B | -0.40% |
| USD1 · World Liberty Financial USD | $1.21B | +2.55% |
| BUIDL · BlackRock USD | $886.54M | 0.00% |
| PYUSD · PayPal USD | $693.76M | -0.08% |
| USDG · Global Dollar | $606.17M | -1.32% |
| USDe · Ethena USDe | $537.30M | +0.55% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 72 of 724 Solana-deployed listed symbols (multiplier ok 80/80; 724 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 724 · Solana deployments 724 · priced 72 · priced-subset mcap $285.02M (lower bound, not a census).
24h volume $13.34M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $433.08M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 72 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 724 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 724 unique underlyings among 724 Solana rows; not every tokenized equity on Solana). 724 of 724 listed xStocks have a Solana deployment (724 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.54M
- **xStocks** (RWA) — $433.08M
- **OnRe** (RWA) — $284.88M
- **Ondo Yield Assets** (RWA) — $179.33M
- **Hastra** (RWA) — $154.87M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $24.70M
- **Plume Vaults** (RWA) — $22.86M

## Daily active addresses

730,181 (Allium, as of 2026-08-30). Provider range 417,138–768,976. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: We came to build,
We stayed for the vibe.](https://x.com/SuperteamGEO/status/2094090572373926329) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 15:51:13 GMT
- [Join us in London: https://luma.com/breakpoint2026](https://x.com/solana/status/2094408145749819758) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 12:53:08 GMT
- [Pinned: What do you want to know about Breakpoint? 

Ask @platis_e 👇](https://x.com/solana/status/2094408142885163086) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 12:53:08 GMT
- [RT by @solana: INSIGHT: @solana leads all blockchains in spot DEX volume across the 24h, 7d and 30d timeframes.](https://x.com/tokens/status/2094384458871062830) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 11:19:01 GMT
- [RT by @solana: New contests, new ways to make bank, and a whole lot more for this week in @ridemarkets 

🔔 Introducing Opening Bell

A new Ride fund exclusively for stock tokens on @sunrise @Backpack 

For the first time in history, you can boost a trade with over 20x more funding thanks to the multiple communities on Solana providing passive capital for your management alpha

But wait, there's more!](https://x.com/deanmachine/status/2094376063799369999) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 10:45:39 GMT
- [RT by @solana: GM from 🇬🇧 London town! The Events 🥷are in London for Breakpoint site visits and we’ve got the @goatfishxyz with us 🎥🐐 So… what are you dying to know about Breakpoint? 👀

Drop your questions below 👇 Nothing is off limits….ish…](https://x.com/platis_e/status/2094357002617041016) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 09:29:55 GMT
- [RT by @solana: New Solana jobs just dropped on the Superteam Talent Portal

Check out the job board below!](https://x.com/SuperteamTalent/status/2094347126755205387) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 08:50:40 GMT
- [RT by @solana: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT
- [RT by @anza_xyz: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: We came to build,
We stayed for the vibe.](https://x.com/SuperteamGEO/status/2094090572373926329) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 15:51:13 GMT
- [Join us in London: https://luma.com/breakpoint2026](https://x.com/solana/status/2094408145749819758) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 12:53:08 GMT
- [Pinned: What do you want to know about Breakpoint? 

Ask @platis_e 👇](https://x.com/solana/status/2094408142885163086) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 12:53:08 GMT
- [RT by @solana: INSIGHT: @solana leads all blockchains in spot DEX volume across the 24h, 7d and 30d timeframes.](https://x.com/tokens/status/2094384458871062830) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 11:19:01 GMT
- [RT by @solana: New contests, new ways to make bank, and a whole lot more for this week in @ridemarkets 

🔔 Introducing Opening Bell

A new Ride fund exclusively for stock tokens on @sunrise @Backpack 

For the first time in history, you can boost a trade with over 20x more funding thanks to the multiple communities on Solana providing passive capital for your management alpha

But wait, there's more!](https://x.com/deanmachine/status/2094376063799369999) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 10:45:39 GMT
- [RT by @solana: GM from 🇬🇧 London town! The Events 🥷are in London for Breakpoint site visits and we’ve got the @goatfishxyz with us 🎥🐐 So… what are you dying to know about Breakpoint? 👀

Drop your questions below 👇 Nothing is off limits….ish…](https://x.com/platis_e/status/2094357002617041016) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 09:29:55 GMT
- [RT by @solana: New Solana jobs just dropped on the Superteam Talent Portal

Check out the job board below!](https://x.com/SuperteamTalent/status/2094347126755205387) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 08:50:40 GMT
- [RT by @solana: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT
- [RT by @anza_xyz: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-31 (2026-08-31 06:33:39 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 724 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 92ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 64ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 153ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 131ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 65ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7340ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 89ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 77ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 62ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 76ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 36ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 40ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1594ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 120ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 87ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 91ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 90ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 211ms https://solana.com/data
- `solana.com.databricks` [ok] 200 85ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 376ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 103ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 564ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 155ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 116ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 457ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 98ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 103ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 101ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 2305ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 4736ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1755ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1984ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 66ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 61ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 35ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 373ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 479ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 374ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 402ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 408ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 392ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 446ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 404ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 402ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 349ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 394ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 367ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 417ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 345ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1586ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1857ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1783ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 3195ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1294ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1806ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1440ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 757ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AAPLx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.AMZNx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.AAPLx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.GOOGLx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.SPYx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.mult.AAPLx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.METAx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.NVDAx` [ok] 200 602ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.AMZNx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.TSLAx` [ok] 200 654ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.mult.AMZNx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.price.MSFTx` [ok] 200 793ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.TSLAx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 487ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 677ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.TSLAx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 849ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 596ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.MVLLx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.DRAMx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.mult.COINx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 1448ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.DJTx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.MSFTx` [ok] 200 1262ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.INTWx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.mult.QQQx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.INTWx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 846ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.SNXXx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.SOXSx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.SNXXx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.SOXSx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.price.KORUx` [ok] 200 1307ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.SNXXx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 1595ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.MUUx` [ok] 200 1852ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.mult.MSFTx` [ok] 200 1278ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.DJTx` [ok] 200 1693ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 488ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.DJTx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 638ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.TNGYIx` [ok] 200 685ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 1068ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.KUNLx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.KUNLx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 906ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.MMGx` [ok] 200 1145ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.MMGx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.MUUx` [ok] 200 1507ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 717ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 696ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 475ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.SMOIHx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 1403ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.SMOIHx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 3187ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 657ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.CSPCx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.CRESBx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.SUOPTx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 490ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 790ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.CRESMx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.JTGEXx` [ok] 200 922ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.CSPCx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 883ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.CMERPx` [ok] 200 656ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 719ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.CMENDx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 635ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 855ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 811ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 700ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.BANKCx` [ok] 200 5784ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 1980ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.WXXDCx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.JDHLTx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 3643ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 717ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.mult.MIXUx` [ok] 200 856ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 1154ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.CRESPx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 1078ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.SITCx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 2705ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.CLONPx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.CRESPx` [ok] 200 766ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.CTFJWx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 985ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.CTFJWx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.GENTEx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.SINOTx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 1305ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 923ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 1357ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.SINOTx` [ok] 200 507ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 521ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.GENTEx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.PWAHLx` [ok] 200 1252ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.WHGROx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 3647ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 725ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.CKAHx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 750ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 782ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 939ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.price.KUAIx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 646ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.COVELx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.NONGx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.COVELx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 1418ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 740ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 1083ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.CHONGx` [ok] 200 607ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.price.MTRCPx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.MEITx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.mult.KUAIx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.CHONGx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.price.GEELx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.MEITx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.price.HNDLDx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.GEELx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.CHONGx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 561ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.HNDLDx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 817ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 710ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.price.BOCOMx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.price.PICCx` [ok] 200 945ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.BOCOMx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.price.POPMTx` [ok] 200 610ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.circ.PICCx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.POPMTx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 774ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 1592ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.BOCOMx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.mult.POPMTx` [ok] 200 1159ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 2497ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.HKCGAx` [ok] 200 4680ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 696ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 725ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1122ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 178ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 59ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 60ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 64ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 58ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.SINOTx` [ok] 200 66ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 127ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 265ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 84ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 82ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 63ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 49ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 53ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 313ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
