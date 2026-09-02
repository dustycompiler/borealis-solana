# Borealis — Solana ecosystem report

**Generated** 2026-09-02T17:23:11Z · 2026-09-02 10:23:11 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-02T17:23:01Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -2.80%; DEX 24h $2.17B · 1d -13% · vs-7d-ago -26%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -2.80%, DeFiLlama TVL 1d -5.25%, DEX 1d -13.19%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **WARN · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -13.19%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -26.01%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 840,200.00 is +26.5% vs 30d median 664,014.50 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 98.21 USD is +26.8% vs 30d median 77.46 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,752,840 |
| Block height | 421,800,223 |
| Block time | 2026-09-02T17:23:01Z |
| Epoch | 1,027 (20.57% · slot 88,844/432,000) |
| Mean TPS (last ~3,600s) | 4,248.7 |
| Mean non-vote TPS | 2,119.7 |
| Median TPS (same window) | 4,185.3 |
| Mean slot time | 316.2 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 544,510,407,540 |
| Circulating supply | 585,275,692 SOL |
| Total supply | 633,361,565 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 19 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 438,029,873 SOL |
| Delinquent stake | 392,483.22 SOL (0.090%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.26% / 35.54% |
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

- `SLAY6uN1…` · 183.29K SOL · commission 5% · lag 19162 slots
- `nymsGg7Z…` · 91.62K SOL · commission 0% · lag 88842 slots
- `prt1st4R…` · 78.62K SOL · commission 5% · lag 265898 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 88590 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 404117 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 966719 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 453184 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 314201 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1769086 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 952489 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 994003 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 952383 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 488 | data/history.jsonl snapshot tape |
| TVL chart | 488 | data/history.jsonl snapshot tape |
| SOL chart | 487 | data/history.jsonl snapshot tape |
| history.jsonl rows | 488 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$832.18K** (8,091.7 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-31 |
| **Solana REV** | **9,754.9 SOL** / **$1.00M** | MEASURED UTC calendar day 2026-08-31: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-31 · UTC day 2026-08-31 · SOL-USD date 2026-08-31 |
| Jito tip-floor run-rate (NOT REV) | $35.64K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 35641 USD; at p95 floor → 18185460 USD. |
| Protocol fees 24h | $12.64M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9961 |
| p90 / p99 | 0.000013 / 0.000104 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $98.21 | coingecko.simple_price |
| 24h change | -2.80% | coingecko.simple_price |
| Market cap | $57.48B | coingecko.simple_price |
| 24h volume | $3.31B | coingecko.simple_price |

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
| Orca DEX | $217.89M | -14.45% |
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
Listed 726 · Solana deployments 726 · priced 73 · priced-subset mcap $285.52M (lower bound, not a census).
24h volume $20.79M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
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

_As of 2026-09-02 (2026-09-02 10:23:11 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 625ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 583ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 568ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 629ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 589ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6747ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1254ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 202ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 56ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 284ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 67ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 78ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 88ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 220ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 88ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 108ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 182ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 661ms https://solana.com/data
- `solana.com.databricks` [ok] 200 240ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 624ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 240ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 214ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 247ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 526ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 709ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 373ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 364ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 378ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1189ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1841ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2376ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 2205ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 211ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 595ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 581ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2374ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2540ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2860ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2378ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2231ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2657ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2355ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2908ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2618ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2624ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2362ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2543ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2447ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2299ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1839ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1763ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1588ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2507ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1973ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1861ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1622ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1527ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.METAx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.NVDAx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.GOOGLx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.MSFTx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.AMZNx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.SPYx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.AAPLx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.AMZNx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.MSFTx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 630ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 526ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.NVDAx` [ok] 200 1052ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.circ.COINx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.MVLLx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.QQQx` [ok] 200 969ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.NVDAx` [ok] 200 641ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 665ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 1262ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.MUUx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 2011ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.mult.MVLLx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.price.KORUx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.MUUx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 1273ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.SOXSx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.mult.QQQx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.SOXSx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.KORUx` [ok] 200 967ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 1506ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.mult.DRAMx` [ok] 200 1626ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.DJTx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.SOXSx` [ok] 200 604ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.TSLAx` [ok] 200 3653ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.SNXXx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.NWGx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.mult.TSLAx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.NWGx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 648ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 2129ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.INTWx` [ok] 200 1725ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.circ.INTWx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.SHEINx` [ok] 200 1251ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.price.BANKCx` [ok] 200 853ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.INTWx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.NWGx` [ok] 200 1043ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 1068ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.SHEINx` [ok] 200 622ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 1343ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.mult.TNGYIx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 2383ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 725ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.BANKCx` [ok] 200 1277ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.MMGx` [ok] 200 1038ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 799ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.MMGx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 2771ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 636ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 1562ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 919ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.SHEINx` [ok] 200 2436ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.KUNLx` [ok] 200 1224ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 1841ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.price.SNBIOx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 949ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 488ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.CTINSx` [ok] 200 2217ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 624ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 874ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 736ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.SMOIHx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 1308ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 567ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.CSPCx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.circ.CSPCx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 821ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 1081ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 1708ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.CTINSx` [ok] 200 1437ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 1536ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 1039ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.JTGEXx` [ok] 200 677ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 1437ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.JTGEXx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.CRESMx` [ok] 200 878ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 1310ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 616ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.CMERPx` [ok] 200 1646ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.MIXUx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.mult.CMERPx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 594ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.CSPCx` [ok] 200 1989ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.ASMPTx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.CMENDx` [ok] 200 1302ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 1075ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 1638ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 1516ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 1450ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 823ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.MIXUx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 1097ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.mult.CRESMx` [ok] 200 1098ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 592ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.CMENDx` [ok] 200 1494ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.WHRFRx` [ok] 200 1264ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.SINOTx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 1943ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.CTFJWx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 1281ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 1487ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 862ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 2034ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 545ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.CTFJWx` [ok] 200 957ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 1142ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.PRADx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.WHGROx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 537ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 1037ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.CLPHDx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.GENTEx` [ok] 200 555ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.GENTEx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 3253ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 1074ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 1753ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 850ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.CTPCAx` [ok] 200 2012ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 2579ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 1922ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 768ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 1596ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 4257ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 545ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.CKAHx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 670ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.KUAIx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.SINOx` [ok] 200 3754ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 715ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.CLONPx` [ok] 200 741ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 906ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 563ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 609ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 1493ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.NONGx` [ok] 200 1039ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.CKINFx` [ok] 200 991ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 1395ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 2188ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.COVELx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 1261ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 1379ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 645ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.mult.COVELx` [ok] 200 621ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.price.MTRCPx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.GEELx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.NONGx` [ok] 200 1304ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.CHONGx` [ok] 200 1099ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.price.HNDLDx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.CHONGx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.HNDLDx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 2562ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 498ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 896ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 1041ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 1753ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 2023ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 1933ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 4463ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1751ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 201ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.HKEXCx` [ok] 200 98ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MEITx` [ok] 200 98ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 136ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.MIXUx` [ok] 200 95ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.BANKCx` [ok] 200 127ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 114ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.CTINSx` [ok] 200 114ms https://lite-api.jup.ag/tokens/v2/search?query=CTINSx
- `jup.tokens.search.SINOTx` [ok] 200 109ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 182ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 475ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 151ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 565ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 567ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 565ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 648ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 436ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
