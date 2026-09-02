# Borealis — Solana ecosystem report

**Generated** 2026-09-02T17:35:46Z · 2026-09-02 10:35:46 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-02T17:35:35Z · **RPC health** `ok`
**Health score** 92 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -2.44%; DEX 24h $2.17B · 1d -13% · vs-7d-ago -26%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -2.44%, DeFiLlama TVL 1d -5.25%, DEX 1d -13.19%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **WARN · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -13.19%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -26.01%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 840,200.00 is +26.5% vs 30d median 664,014.50 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 98.66 USD is +27.4% vs 30d median 77.46 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,755,239 |
| Block height | 421,802,610 |
| Block time | 2026-09-02T17:35:35Z |
| Epoch | 1,027 (21.12% · slot 91,239/432,000) |
| Mean TPS (last ~3,600s) | 4,275.5 |
| Mean non-vote TPS | 2,146.2 |
| Median TPS (same window) | 4,134.5 |
| Mean slot time | 315.8 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 544,513,987,184 |
| Circulating supply | 585,275,682 SOL |
| Total supply | 633,361,556 SOL |
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
| Activated stake | 436,125,213 SOL |
| Delinquent stake | 2,297,144.00 SOL (0.524%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 79 |
| Top 10 / 20 stake share | 24.37% / 35.70% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.35M SOL | 3.98% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.33M SOL | 3.74% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.46M SOL | 2.86% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.30M SOL | 2.59% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.19% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.13% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.22M SOL | 1.66% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.13M SOL | 1.63% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.95M SOL | 1.37% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.61M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `FBbqKvwL…` · 1.90M SOL · commission 1% · lag 1550 slots
- `SLAY6uN1…` · 183.29K SOL · commission 5% · lag 21561 slots
- `nymsGg7Z…` · 91.62K SOL · commission 0% · lag 91241 slots
- `prt1st4R…` · 78.62K SOL · commission 5% · lag 268297 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 90989 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 406516 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 969118 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 455583 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 316600 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1771485 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 954888 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 996402 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 489 | data/history.jsonl snapshot tape |
| TVL chart | 489 | data/history.jsonl snapshot tape |
| SOL chart | 488 | data/history.jsonl snapshot tape |
| history.jsonl rows | 489 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$832.18K** (8,091.7 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-31 |
| **Solana REV** | **9,754.9 SOL** / **$1.00M** | MEASURED UTC calendar day 2026-08-31: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-31 · UTC day 2026-08-31 · SOL-USD date 2026-08-31 |
| Jito tip-floor run-rate (NOT REV) | $18.73K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 18734 USD; at p95 floor → 2286852 USD. |
| Protocol fees 24h | $12.64M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9973 |
| p90 / p99 | 0.000012 / 0.000109 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $98.66 | coingecko.simple_price |
| 24h change | -2.44% | coingecko.simple_price |
| Market cap | $57.74B | coingecko.simple_price |
| 24h volume | $3.24B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.67B |
| TVL 1d / 7d / 30d | -5.25% / +1.13% / +19.56% |
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
| Manifest Trade | $148.84M | +13.77% |
| Meteora DLMM | $139.98M | -6.26% |
| Raydium AMM | $125.41M | -11.19% |
| Axiom | $97.98M | -13.74% |
| Scorch | $64.72M | -14.96% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.51B | -3.28% | +3.84% |
| Kamino Lend | Lending | $1.23B | -1.51% | +4.18% |
| Raydium AMM | Dexs | $1.07B | -3.19% | +1.90% |
| Jupiter Lend | Lending | $1.06B | -1.69% | +0.95% |
| Binance Staked SOL | Liquid Staking | $1.02B | -3.07% | +4.63% |
| Jito Liquid Staking | Liquid Staking | $1.00B | -2.76% | +3.88% |
| BlackRock BUIDL | RWA | $887.09M | -1.38% | -0.87% |
| Jupiter Perpetual Exchange | Derivatives | $741.19M | -1.78% | -0.46% |
| Jupiter Staked SOL | Liquid Staking | $511.60M | -3.37% | +3.42% |
| xStocks | RWA | $431.50M | -0.75% | +1.87% |

## Stablecoins

Solana circulating pegged-USD: **$15.59B**
(1d -0.78% · 7d -1.86%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.71B | -0.23% |
| USDT · Tether | $2.90B | +2.47% |
| USDGO · USDGO | $1.25B | +0.81% |
| USD1 · World Liberty Financial USD | $1.21B | -0.00% |
| BUIDL · BlackRock USD | $887.09M | +0.02% |
| PYUSD · PayPal USD | $715.20M | -7.63% |
| USDG · Global Dollar | $612.30M | +0.11% |
| USDe · Ethena USDe | $535.93M | -0.24% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 73 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 73 · priced-subset mcap $285.49M (lower bound, not a census).
24h volume $20.74M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $431.50M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 73 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $887.09M
- **xStocks** (RWA) — $431.50M
- **OnRe** (RWA) — $288.65M
- **Ondo Yield Assets** (RWA) — $179.09M
- **Hastra** (RWA) — $153.75M
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
- [RT by @solana: You don’t need a bridge anymore.

Introducing Universal Deposit.

Send a token from any supported chain and receive USDC in your Solana wallet.

Universal Deposit handles the routing, bridging, and swapping automatically:

- Send funds from the wallet you already use
- Deposit from Ethereum, Base, Arbitrum and Sui
- No bridge apps, network switching and extra transactions
- Flat $0.30 fee, whether you send $100 or $10M

The most seamless cross-chain transfer experience is here.

All roads lead to Solana](https://x.com/JupiterExchange/status/2095161972274999712) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 14:48:35 GMT
- [RT by @solana: 🚨 Speaker announcement! @SECPaulSAtkins will deliver the closing keynote at Solana Summit DC on Sept 14. 

He'll discuss the SEC's vision for digital asset regulation. There's still time to register. https://luma.com/DCSummit](https://x.com/SolanaInstitute/status/2095147132227330347) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 13:49:36 GMT
- [RT by @anza_xyz: Solana is the financial infra powering the token supercycle. 

We're building toward a future where the internet capital market becomes the biggest capital market.

More thoughts here:

https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/calilyliu/status/2095179874839462349) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 15:59:43 GMT
- [RT by @anza_xyz: V1 Transactions are coming to @solana and they are really cool! They will go live in a couple of weeks.

Max transaction size goes from 1,232 → 4,096 bytes. Compute budgeting moves out of instructions and into the transaction itself.

There are a few small breaking changes you need to be aware, and you can start testing locally today.  🧵](https://x.com/a_milz/status/2091903273632731271) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 24 Aug 2026 14:59:40 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

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
- [RT by @solana: You don’t need a bridge anymore.

Introducing Universal Deposit.

Send a token from any supported chain and receive USDC in your Solana wallet.

Universal Deposit handles the routing, bridging, and swapping automatically:

- Send funds from the wallet you already use
- Deposit from Ethereum, Base, Arbitrum and Sui
- No bridge apps, network switching and extra transactions
- Flat $0.30 fee, whether you send $100 or $10M

The most seamless cross-chain transfer experience is here.

All roads lead to Solana](https://x.com/JupiterExchange/status/2095161972274999712) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 14:48:35 GMT
- [RT by @solana: 🚨 Speaker announcement! @SECPaulSAtkins will deliver the closing keynote at Solana Summit DC on Sept 14. 

He'll discuss the SEC's vision for digital asset regulation. There's still time to register. https://luma.com/DCSummit](https://x.com/SolanaInstitute/status/2095147132227330347) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 13:49:36 GMT
- [RT by @anza_xyz: Solana is the financial infra powering the token supercycle. 

We're building toward a future where the internet capital market becomes the biggest capital market.

More thoughts here:

https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/calilyliu/status/2095179874839462349) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 15:59:43 GMT
- [RT by @anza_xyz: V1 Transactions are coming to @solana and they are really cool! They will go live in a couple of weeks.

Max transaction size goes from 1,232 → 4,096 bytes. Compute budgeting moves out of instructions and into the transaction itself.

There are a few small breaking changes you need to be aware, and you can start testing locally today.  🧵](https://x.com/a_milz/status/2091903273632731271) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 24 Aug 2026 14:59:40 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-02 (2026-09-02 10:35:46 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 726 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 77ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 33ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 39ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 64ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 38ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6893ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 70ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 63ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 36ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 53ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 30ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 32ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 3949ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 70ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 71ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 58ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 95ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 495ms https://solana.com/data
- `solana.com.databricks` [ok] 200 59ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 343ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 66ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 166ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 51ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 117ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 425ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 81ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 106ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 74ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 713ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1863ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1784ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1666ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 94ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 30ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 34ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 341ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 319ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 442ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 292ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 400ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 394ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 39ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 3522ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 322ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 416ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 416ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 443ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 396ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 368ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 367ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1746ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2028ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2170ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1710ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1180ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2247ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2439ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 716ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AAPLx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.AMZNx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.MSFTx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.TSLAx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.METAx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.AMZNx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.SPYx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.TSLAx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.NVDAx` [ok] 200 699ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.mult.AMZNx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.GOOGLx` [ok] 200 804ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.mult.SPYx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 514ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.NVDAx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 781ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.mult.METAx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 601ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.TSLAx` [ok] 200 755ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.MVLLx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.mult.NVDAx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.MUUx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.circ.MVLLx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.MUUx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 887ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.MUUx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.price.DJTx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.mult.MVLLx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.AXTIx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.circ.DJTx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.price.INTWx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.mult.QQQx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.circ.GOOGLx` [ok] 200 1459ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.AXTIx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.SNXXx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.mult.GOOGLx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.SNXXx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.price.NWGx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.mult.SNXXx` [ok] 200 583ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.BANKCx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 1102ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.SHEINx` [ok] 200 994ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.price.SOXSx` [ok] 200 1444ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.mult.BANKCx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.SOXSx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 1595ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.circ.SUOPTx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.KORUx` [ok] 200 2110ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.SHEINx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.NWGx` [ok] 200 1579ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.MMGx` [ok] 200 922ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 4457ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.KORUx` [ok] 200 604ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 987ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.INTWx` [ok] 200 1316ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.KORUx` [ok] 200 662ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.mult.NWGx` [ok] 200 928ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.CTINSx` [ok] 200 616ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.AAPLx` [ok] 200 910ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.KUNLx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 1141ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.CTINSx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 1053ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 883ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.HRZRBx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 707ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.CMERPx` [ok] 200 916ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.CSPCx` [ok] 200 873ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 1752ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 1614ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.CMERPx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 2318ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.CSPCx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 1200ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 1720ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 724ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.SMOIHx` [ok] 200 2291ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.CRESMx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 736ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.WXXDCx` [ok] 200 875ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 1027ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.CMENDx` [ok] 200 933ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 1200ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.CRESMx` [ok] 200 1007ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 571ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 636ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.SITCx` [ok] 200 841ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.CRESPx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 1405ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 3104ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 596ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 779ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.MIXUx` [ok] 200 2833ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.mult.SINOTx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 871ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.PRADx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.CTFJWx` [ok] 200 1186ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.CLONPx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 1432ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 1180ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 623ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 694ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 1320ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 2689ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.GENTEx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 1311ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 1129ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.CTPCAx` [ok] 200 626ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.WUXIBx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 610ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 784ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 567ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 1022ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 638ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 1646ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 1391ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 854ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 1207ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 654ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.KUAIx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 1411ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 1213ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 1040ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.COVELx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.circ.NONGx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 1193ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.COVELx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 2127ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.mult.HKEXCx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 7780ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.COVELx` [ok] 200 612ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 1993ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 1541ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 777ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 2428ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 542ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.CKAHx` [ok] 200 1468ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.HNDLDx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.GEELx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.PICCx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.NONGx` [ok] 200 2165ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 785ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 1270ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 2245ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.CHONGx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 1497ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 1561ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.CKHUTx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 2229ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 1961ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1172ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 177ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.HKEXCx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MEITx` [ok] 200 39ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 43ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.MIXUx` [ok] 200 47ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.BANKCx` [ok] 200 41ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 49ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.CTINSx` [ok] 200 45ms https://lite-api.jup.ag/tokens/v2/search?query=CTINSx
- `jup.tokens.search.SINOTx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 284ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 270ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 78ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 38ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 25ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 31ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 71ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 2469ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
