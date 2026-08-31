# Borealis — Solana ecosystem report

**Generated** 2026-08-31T14:48:33Z · 2026-08-31 07:48:33 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-31T14:48:23Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -3.00%; DEX 24h $1.93B · 1d +16% · vs-7d-ago -34%; slot 318 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -34.34%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +9.75%. (threshold: `|1d %| >= 8`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 103.50 USD is +35.2% vs 30d median 76.57 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **WARN · Last TPS sample outside 2.5σ of the 60-sample window** — Last sample 5,698 TPS is +3.03σ vs window mean 4,522 (n=60, σ=389). (threshold: `|last sample − window mean| > 2.5σ`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +15.50%. (threshold: `|1d %| >= 8`)
- **INFO · TPS vs 30d median (solana.com/data tx/86400)** — Current 4,521.54 TPS is +24.5% vs 30d median 3,631.80 TPS (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,177,871 |
| Block height | 421,225,539 |
| Block time | 2026-08-31T14:48:23Z |
| Epoch | 1,025 (87.47% · slot 377,873/432,000) |
| Mean TPS (last ~3,600s) | 4,521.5 |
| Mean non-vote TPS | 2,398.4 |
| Median TPS (same window) | 4,411.0 |
| Mean slot time | 318.4 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 543,792,041,026 |
| Circulating supply | 585,120,930 SOL |
| Total supply | 633,172,707 SOL |
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

- `mrgn4atx…` · 21.79K SOL · commission 0% · lag 196088 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1925192 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 391750 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 258446 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 27035 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1194117 slots
- `CpdzCVza…` · 315.26 SOL · commission 100% · lag 377520 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 419034 slots
- `HFTcVVrX…` · 152.80 SOL · commission 100% · lag 377414 slots
- `6pEtDovp…` · 131.96 SOL · commission 100% · lag 391798 slots
- `7G4Rfctw…` · 75.85 SOL · commission 100% · lag 416172 slots
- `DZKTNGR3…` · 48.61 SOL · commission 100% · lag 423714 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 299 | data/history.jsonl snapshot tape |
| TVL chart | 299 | data/history.jsonl snapshot tape |
| SOL chart | 298 | data/history.jsonl snapshot tape |
| history.jsonl rows | 299 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$814.10K** (7,855.5 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-29 |
| **Solana REV** | **9,341.6 SOL** / **$968.12K** | MEASURED UTC calendar day 2026-08-29: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-29 · UTC day 2026-08-29 · SOL-USD date 2026-08-29 |
| Jito tip-floor run-rate (NOT REV) | $126.52K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 126519 USD; at p95 floor → 2144759 USD. |
| Protocol fees 24h | $12.31M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9942 |
| p90 / p99 | 0.000011 / 0.000187 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.50 | coingecko.simple_price |
| 24h change | -3.00% | coingecko.simple_price |
| Market cap | $60.56B | coingecko.simple_price |
| 24h volume | $3.72B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.80B |
| TVL 1d / 7d / 30d | -1.89% / +4.28% / +22.06% |
| DEX volume 24h | $1.93B · 1d +15.50% · vs-7d-ago -34.34% |
| 7d DEX volume | $18.17B · -6.33% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $12.31M |
| Fees 1d / 7d | +9.75% / -2.95% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $732.11M | +25.20% |
| Orca DEX | $258.15M | +77.63% |
| BisonFi | $184.51M | +23.11% |
| Meteora DLMM | $142.67M | -0.21% |
| Manifest Trade | $131.61M | +51.77% |
| Raydium AMM | $111.76M | -8.47% |
| pump.fun | $91.65M | -16.74% |
| Axiom | $83.77M | -19.18% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.57B | -2.74% | +9.67% |
| Kamino Lend | Lending | $1.24B | -1.42% | +4.26% |
| Raydium AMM | Dexs | $1.10B | -1.91% | +6.59% |
| Jupiter Lend | Lending | $1.08B | -1.65% | +1.28% |
| Binance Staked SOL | Liquid Staking | $1.06B | -2.65% | +9.29% |
| Jito Liquid Staking | Liquid Staking | $1.03B | -2.77% | +7.69% |
| BlackRock BUIDL | RWA | $886.54M | 0.00% | +6.05% |
| Jupiter Perpetual Exchange | Derivatives | $759.60M | -1.87% | +1.72% |
| Jupiter Staked SOL | Liquid Staking | $531.71M | -2.71% | +7.66% |
| xStocks | RWA | $430.47M | +1.77% | +2.54% |

## Stablecoins

Solana circulating pegged-USD: **$15.71B**
(1d -1.08% · 7d -2.04%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.78B | -3.05% |
| USDT · Tether | $2.83B | -0.00% |
| USDGO · USDGO | $1.24B | -0.40% |
| USD1 · World Liberty Financial USD | $1.21B | +2.55% |
| BUIDL · BlackRock USD | $886.54M | 0.00% |
| PYUSD · PayPal USD | $693.87M | -0.08% |
| USDG · Global Dollar | $605.90M | -1.37% |
| USDe · Ethena USDe | $537.30M | +0.55% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 72 of 724 Solana-deployed listed symbols (multiplier ok 80/80; 724 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 724 · Solana deployments 724 · priced 72 · priced-subset mcap $287.24M (lower bound, not a census).
24h volume $16.79M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $430.47M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 72 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 724 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 724 unique underlyings among 724 Solana rows; not every tokenized equity on Solana). 724 of 724 listed xStocks have a Solana deployment (724 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.54M
- **xStocks** (RWA) — $430.47M
- **OnRe** (RWA) — $284.89M
- **Ondo Yield Assets** (RWA) — $179.96M
- **Hastra** (RWA) — $154.86M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $24.59M
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

- [RT by @solana: We crossed $100k in customer spend in August, x4 increase from July! 🎉

Followed by a 3x in number of orders, with leading categories being TCGs, hardware, and animal supplies.

Half of the purchases were managed by purchasing agents on @clawpumptech that shop Amazon & eBay with their trading fees, led by the success of @selfmadebySP3ND 🦞🛍️

Use SP3ND if you want to shop online with stables and without KYC.](https://x.com/SP3NDdotshop/status/2094432549770842136) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 14:30:07 GMT
- [Image](https://x.com/solana/status/2094420460079558763) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 13:42:04 GMT
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

- [RT by @solana: We crossed $100k in customer spend in August, x4 increase from July! 🎉

Followed by a 3x in number of orders, with leading categories being TCGs, hardware, and animal supplies.

Half of the purchases were managed by purchasing agents on @clawpumptech that shop Amazon & eBay with their trading fees, led by the success of @selfmadebySP3ND 🦞🛍️

Use SP3ND if you want to shop online with stables and without KYC.](https://x.com/SP3NDdotshop/status/2094432549770842136) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 14:30:07 GMT
- [Image](https://x.com/solana/status/2094420460079558763) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 13:42:04 GMT
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

_As of 2026-08-31 (2026-08-31 07:48:33 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 724 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 389ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 475ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 574ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 389ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 366ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7801ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 738ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 130ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 83ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 66ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 47ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 61ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1435ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 116ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 56ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 94ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 687ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 338ms https://solana.com/data
- `solana.com.databricks` [ok] 200 135ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 573ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 264ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 144ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 97ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 171ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 905ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 445ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 445ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 443ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 389ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1576ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1463ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [FAIL] 502 201ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 502 Bad Gateway
- `status.incidents` [ok] 200 295ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 363ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 393ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2769ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2144ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1369ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1387ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1578ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1670ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1622ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2844ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1714ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1925ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1968ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2898ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1757ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2016ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2480ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2424ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2077ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2128ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1482ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1886ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 5434ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1359ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.AMZNx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.SPYx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.GOOGLx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.AAPLx` [ok] 200 589ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.SPYx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.MSFTx` [ok] 200 694ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.NVDAx` [ok] 200 774ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.METAx` [ok] 200 804ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.TSLAx` [ok] 200 632ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.MSFTx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 595ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.AMZNx` [ok] 200 1166ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.DRAMx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.MUUx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.mult.QQQx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.MVLLx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.AXTIx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.mult.AMZNx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.AXTIx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.INTWx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.mult.COINx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.KORUx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.price.SOXSx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.mult.DRAMx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 742ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.MVLLx` [ok] 200 786ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.SOXSx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.price.SNXXx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.INTWx` [ok] 200 567ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 725ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.mult.MUUx` [ok] 200 918ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.mult.DJTx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.MVLLx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.SNXXx` [ok] 200 637ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.mult.MMGx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 657ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 596ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.SUOPTx` [ok] 200 891ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.JDLOGx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 1103ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.SUOPTx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 618ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.WRFHDx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.SNXXx` [ok] 200 1327ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.mult.INTWx` [ok] 200 1895ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.ENNHLx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.SMOIHx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 572ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 858ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 989ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 482ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 1205ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.CMERPx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.CSPCx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 548ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.WXXDCx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 3072ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 1161ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 1475ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.TNGYIx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 487ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.MIXUx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.CRESBx` [ok] 200 603ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 978ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 654ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.CMENDx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.ASMPTx` [ok] 200 525ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.CMENDx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 411ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 2343ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.SITCx` [ok] 200 929ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.JDHLTx` [ok] 200 776ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 1064ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 1085ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.CRESPx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.WHRFRx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 1994ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.MIXUx` [ok] 200 1683ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.CRESPx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 1615ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.CTFJWx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.SINOx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.CRESPx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 1425ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.CLONPx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.PWAHLx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.SINOx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 637ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.GENTEx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.SWPRPx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.WUXIBx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.GENTEx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 2025ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.CLONPx` [ok] 200 836ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 685ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.HKCGAx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.KUAIx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.CKAHx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.KUAIx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.mult.CKAHx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 896ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.COVELx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.CHONGx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.price.GEELx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.mult.HKEXCx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.COVELx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.CHONGx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 1174ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.price.MTRCPx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.mult.COVELx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.CKINFx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.MEITx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.circ.MTRCPx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.GEELx` [ok] 200 578ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.HNDLDx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.GEELx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.price.POPMTx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.mult.HNDLDx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 805ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.price.BOCOMx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.circ.POPMTx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.circ.BOCOMx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.BOCOMx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 972ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.POPMTx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 84ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 247ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 121ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 127ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 125ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 122ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 122ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 120ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 126ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.SINOTx` [ok] 200 123ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 342ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 419ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 149ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 365ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 410ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 609ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 418ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 377ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
