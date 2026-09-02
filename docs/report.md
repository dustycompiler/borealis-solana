# Borealis — Solana ecosystem report

**Generated** 2026-09-02T18:41:52Z · 2026-09-02 11:41:52 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-02T18:41:44Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +0.45%; DEX 24h $2.17B · 1d -13% · vs-7d-ago -26%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -13.19%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -26.01%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 840,200.00 is +26.5% vs 30d median 664,014.50 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 99.19 USD is +28.0% vs 30d median 77.46 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,767,826 |
| Block height | 421,815,193 |
| Block time | 2026-09-02T18:41:44Z |
| Epoch | 1,027 (24.03% · slot 103,829/432,000) |
| Mean TPS (last ~3,600s) | 4,280.9 |
| Mean non-vote TPS | 2,147.9 |
| Median TPS (same window) | 4,229.4 |
| Mean slot time | 315.4 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 544,530,955,611 |
| Circulating supply | 585,275,469 SOL |
| Total supply | 633,361,511 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 20 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 437,939,127 SOL |
| Delinquent stake | 483,229.65 SOL (0.110%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.27% / 35.55% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.35M SOL | 3.96% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.33M SOL | 3.73% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.46M SOL | 2.85% | 0% | 0 |
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

- `SLAY6uN1…` · 183.29K SOL · commission 5% · lag 34148 slots
- `nymsGg7Z…` · 91.62K SOL · commission 0% · lag 103828 slots
- `mrgn2vUP…` · 90.75K SOL · commission 0% · lag 5169 slots
- `prt1st4R…` · 78.62K SOL · commission 5% · lag 280884 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 103576 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 419103 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 981705 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 468170 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 329187 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1784072 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 967475 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1008989 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 493 | data/history.jsonl snapshot tape |
| TVL chart | 493 | data/history.jsonl snapshot tape |
| SOL chart | 492 | data/history.jsonl snapshot tape |
| history.jsonl rows | 493 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$832.18K** (8,091.7 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-31 |
| **Solana REV** | **9,754.9 SOL** / **$1.00M** | MEASURED UTC calendar day 2026-08-31: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-31 · UTC day 2026-08-31 · SOL-USD date 2026-08-31 |
| Jito tip-floor run-rate (NOT REV) | $18.41K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 18408 USD; at p95 floor → 2933552 USD. |
| Protocol fees 24h | $12.64M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9975 |
| p90 / p99 | 0.000010 / 0.000105 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $99.19 | coingecko.simple_price |
| 24h change | +0.45% | coingecko.simple_price |
| Market cap | $58.07B | coingecko.simple_price |
| 24h volume | $3.16B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.67B |
| TVL 1d / 7d / 30d | -5.28% / +1.10% / +19.53% |
| DEX volume 24h | $2.17B · 1d -13.19% · vs-7d-ago -26.01% |
| 7d DEX volume | $16.92B · -23.18% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $12.64M |
| Fees 1d / 7d | -5.97% / -4.59% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $827.37M | -11.91% |
| Orca DEX | $210.30M | -17.43% |
| BisonFi | $204.83M | -12.03% |
| Manifest Trade | $154.42M | +18.03% |
| Meteora DLMM | $139.98M | -6.26% |
| Raydium AMM | $125.50M | -11.13% |
| Axiom | $97.98M | -13.74% |
| Scorch | $64.72M | -14.96% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.52B | -2.39% | +4.29% |
| Kamino Lend | Lending | $1.23B | -1.37% | +4.77% |
| Raydium AMM | Dexs | $1.07B | -3.19% | +1.90% |
| Jupiter Lend | Lending | $1.06B | -1.63% | +0.94% |
| Binance Staked SOL | Liquid Staking | $1.02B | -2.69% | +3.97% |
| Jito Liquid Staking | Liquid Staking | $1.00B | -2.76% | +3.88% |
| BlackRock BUIDL | RWA | $887.09M | -1.38% | -0.87% |
| Jupiter Perpetual Exchange | Derivatives | $741.19M | -1.78% | -0.46% |
| Jupiter Staked SOL | Liquid Staking | $511.47M | -3.00% | +2.77% |
| xStocks | RWA | $431.50M | -0.75% | +1.87% |

## Stablecoins

Solana circulating pegged-USD: **$15.54B**
(1d -0.78% · 7d -1.86%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.67B | -0.85% |
| USDT · Tether | $2.90B | +2.49% |
| USDGO · USDGO | $1.25B | +0.81% |
| USD1 · World Liberty Financial USD | $1.21B | -0.00% |
| BUIDL · BlackRock USD | $887.09M | +0.02% |
| PYUSD · PayPal USD | $715.15M | -7.63% |
| USDG · Global Dollar | $609.96M | -0.28% |
| USDe · Ethena USDe | $535.92M | -0.24% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 73 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 73 · priced-subset mcap $285.07M (lower bound, not a census).
24h volume $23.99M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $431.61M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 73 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $887.09M
- **xStocks** (RWA) — $431.50M
- **OnRe** (RWA) — $288.65M
- **Ondo Yield Assets** (RWA) — $179.09M
- **Hastra** (RWA) — $153.77M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $24.91M
- **Plume Vaults** (RWA) — $22.89M

## Daily active addresses

840,200 (Allium, as of 2026-09-01). Provider range 397,651–840,200. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Read more on @CoinDesk : https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/solana/status/2095210145227616641) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 18:00:00 GMT
- [5.5 billion people on the internet. All of them use money. @calilyliu on the token supercycle.

"What we're in the midst of right now is the token supercycle. Everything of value is becoming programmable." 

"Money, assets, ownership, and markets are always going to move towards the largest market, and that largest market is the internet capital market." 

"This is not just a market rally or a near-term narrative. It's a structural transformation of global capital markets."](https://x.com/solana/status/2095210144514687362) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 18:00:00 GMT
- [RT by @solana: Solana is the only chain with no limits on what you can build on it

Every app on this map is live onchain 👇](https://x.com/magicblock/status/2095190681564377568) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 16:42:39 GMT
- [Join us at Breakpoint

https://solana.com/breakpoint](https://x.com/solana/status/2095180764942148018) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 16:03:15 GMT
- [All value is programmable. 

Welcome to the Token Supercycle.](https://x.com/solana/status/2095180762375147846) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 16:03:14 GMT
- [Powered by @mallowdotart 🤝
https://x.com/meditatingsloth/status/2095150725374644367](https://x.com/solana/status/2095173778766729432) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 15:35:29 GMT
- [Pinned: $166,946.50 raised for Nepal flood relief.

Thank you to everyone that took part. 

Your logos will be up on our pfp and pinned post for the next week.](https://x.com/solana/status/2095173372158394780) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 15:33:53 GMT
- [Video](https://x.com/solana/status/2095172398123463088) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 15:30:00 GMT
- [RT by @anza_xyz: Solana is the financial infra powering the token supercycle. 

We're building toward a future where the internet capital market becomes the biggest capital market.

More thoughts here:

https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/calilyliu/status/2095179874839462349) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 15:59:43 GMT
- [RT by @anza_xyz: V1 Transactions are coming to @solana and they are really cool! They will go live in a couple of weeks.

Max transaction size goes from 1,232 → 4,096 bytes. Compute budgeting moves out of instructions and into the transaction itself.

There are a few small breaking changes you need to be aware, and you can start testing locally today.  🧵](https://x.com/a_milz/status/2091903273632731271) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 24 Aug 2026 14:59:40 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [Read more on @CoinDesk : https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/solana/status/2095210145227616641) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 18:00:00 GMT
- [5.5 billion people on the internet. All of them use money. @calilyliu on the token supercycle.

"What we're in the midst of right now is the token supercycle. Everything of value is becoming programmable." 

"Money, assets, ownership, and markets are always going to move towards the largest market, and that largest market is the internet capital market." 

"This is not just a market rally or a near-term narrative. It's a structural transformation of global capital markets."](https://x.com/solana/status/2095210144514687362) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 18:00:00 GMT
- [RT by @solana: Solana is the only chain with no limits on what you can build on it

Every app on this map is live onchain 👇](https://x.com/magicblock/status/2095190681564377568) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 16:42:39 GMT
- [Join us at Breakpoint

https://solana.com/breakpoint](https://x.com/solana/status/2095180764942148018) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 16:03:15 GMT
- [All value is programmable. 

Welcome to the Token Supercycle.](https://x.com/solana/status/2095180762375147846) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 16:03:14 GMT
- [Powered by @mallowdotart 🤝
https://x.com/meditatingsloth/status/2095150725374644367](https://x.com/solana/status/2095173778766729432) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 15:35:29 GMT
- [Pinned: $166,946.50 raised for Nepal flood relief.

Thank you to everyone that took part. 

Your logos will be up on our pfp and pinned post for the next week.](https://x.com/solana/status/2095173372158394780) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 15:33:53 GMT
- [Video](https://x.com/solana/status/2095172398123463088) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 15:30:00 GMT
- [RT by @anza_xyz: Solana is the financial infra powering the token supercycle. 

We're building toward a future where the internet capital market becomes the biggest capital market.

More thoughts here:

https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/calilyliu/status/2095179874839462349) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 15:59:43 GMT
- [RT by @anza_xyz: V1 Transactions are coming to @solana and they are really cool! They will go live in a couple of weeks.

Max transaction size goes from 1,232 → 4,096 bytes. Compute budgeting moves out of instructions and into the transaction itself.

There are a few small breaking changes you need to be aware, and you can start testing locally today.  🧵](https://x.com/a_milz/status/2091903273632731271) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 24 Aug 2026 14:59:40 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-02 (2026-09-02 11:41:52 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 726 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 412ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 2192ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 481ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 323ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 457ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 8106ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 731ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 99ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 38ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 99ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 27ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 29ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 73ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 65ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 531ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 53ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 661ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 562ms https://solana.com/data
- `solana.com.databricks` [ok] 200 337ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 378ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 176ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 77ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 62ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 447ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 914ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 441ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 443ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 441ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 552ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 3899ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2042ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 2148ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 151ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 322ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 1378ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1869ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1190ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2104ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1599ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 56864ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1677ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2026ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1500ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2118ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 525ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 566ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 502ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 442ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 442ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1885ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1806ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 4117ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2117ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1586ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1881ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2148ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1264ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.SPYx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.METAx` [ok] 200 514ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.GOOGLx` [ok] 200 558ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.AAPLx` [ok] 200 596ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.METAx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.NVDAx` [ok] 200 835ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.TSLAx` [ok] 200 846ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.AMZNx` [ok] 200 986ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.mult.AAPLx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.MSFTx` [ok] 200 1005ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.NVDAx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 497ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.METAx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.TSLAx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.AMZNx` [ok] 200 665ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.DRAMx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.circ.MSFTx` [ok] 200 765ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 576ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 497ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.MSFTx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 962ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 1815ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 701ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.MUUx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.price.AXTIx` [ok] 200 661ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.KORUx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.COINx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.INTWx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.circ.KORUx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 1202ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.MUUx` [ok] 200 649ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 1265ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.MVLLx` [ok] 200 1572ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.SOXSx` [ok] 200 602ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.circ.DJTx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.circ.MVLLx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.SHEINx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.INTWx` [ok] 200 513ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.MVLLx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.MUUx` [ok] 200 601ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.SHEINx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.price.NWGx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.mult.AXTIx` [ok] 200 1101ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 801ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.price.MMGx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.SOXSx` [ok] 200 716ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.NWGx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 913ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.SNXXx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 852ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.MMGx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 612ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.BANKCx` [ok] 200 1346ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.SOXSx` [ok] 200 1075ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 1438ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.price.LAOPGx` [ok] 200 662ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.SNXXx` [ok] 200 1333ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.BANKCx` [ok] 200 956ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 506ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.NWGx` [ok] 200 1983ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 785ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 1674ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 1040ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 1000ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.SZIGHx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 498ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 856ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 763ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.KUNLx` [ok] 200 995ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 865ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.ENNHLx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 577ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.KUNLx` [ok] 200 706ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 954ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.CRESBx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 770ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 693ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.CRESMx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 1404ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 611ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 1992ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.CMERPx` [ok] 200 600ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 664ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.CRESMx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.WXXDCx` [ok] 200 588ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 1726ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 1822ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.MIXUx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.mult.CMENDx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 704ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.SITCx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 991ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 3530ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 603ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.price.JDHLTx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.SNDSCx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.CRESPx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.WXXDCx` [ok] 200 1435ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.circ.CRESPx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 656ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.CLONPx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 1228ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 1739ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 824ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.mult.MIXUx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.CLONPx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 880ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 1312ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.PWAHLx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.PRADx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 1213ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.SINOTx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 831ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 1160ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 1342ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 1065ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.SINOx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.SINOTx` [ok] 200 615ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 943ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 749ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.GENTEx` [ok] 200 697ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 1150ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 740ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 972ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.CKINFx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 849ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 793ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 1232ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 1473ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.NONGx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 1628ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 2024ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.price.COVELx` [ok] 200 1217ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.CHONGx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.CKINFx` [ok] 200 1967ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 1130ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 1879ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.CHONGx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 634ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 2580ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.COVELx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.CHONGx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 536ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.COSCx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.HNDLDx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.MTRCPx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.MEITx` [ok] 200 1308ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.GEELx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.HNDLDx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 696ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.MTRCPx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.HNDLDx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 618ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.COVELx` [ok] 200 1264ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 591ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 1233ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 1369ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 969ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 1303ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1953ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 349ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.HKEXCx` [ok] 200 101ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MEITx` [ok] 200 102ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.MIXUx` [ok] 200 103ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.BANKCx` [ok] 200 101ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.CTINSx` [ok] 200 96ms https://lite-api.jup.ag/tokens/v2/search?query=CTINSx
- `jup.tokens.search.SINOTx` [ok] 200 103ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 429ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 246ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 121ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 79ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 149ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 81ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 88ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 125ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
