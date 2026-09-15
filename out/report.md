# Borealis — Solana ecosystem report

**Generated** 2026-09-15T03:07:16Z · 2026-09-14 20:07:16 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-15T03:07:05Z · **RPC health** `ok`
**Health score** 76 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** WATCH · **Ecosystem** CONTRACTION — SOL 24h +0.71%; DEX 24h $2.21B · 1d +24% · vs-7d-ago -21%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -20.62%. (threshold: `|7d %| >= 20`)
- **WARN · High validator delinquency** — 11 delinquent vote accounts, 1.752% of activated+delinquent stake. (threshold: `delinquent stake >= 1% or delinquent count >= 25`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +23.55%. (threshold: `|1d %| >= 8`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 447,143,301 |
| Block height | 425,185,316 |
| Block time | 2026-09-15T03:07:05Z |
| Epoch | 1,035 (5.39% · slot 23,304/432,000) |
| Mean TPS (last ~3,600s) | 3,704.2 |
| Mean non-vote TPS | 1,599.1 |
| Median TPS (same window) | 3,712.2 |
| Mean slot time | 315.5 ms |
| Median slot time | 315.0 ms |
| Transaction count (cluster) | 548,566,786,083 |
| Circulating supply | 587,028,455 SOL |
| Total supply | 634,111,900 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 678 |
| Delinquent | 11 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 431,550,964 SOL |
| Delinquent stake | 7,697,675.58 SOL (1.752%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 81 |
| Top 10 / 20 stake share | 24.46% / 35.40% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.76M SOL | 4.11% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.37M SOL | 3.79% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.49M SOL | 2.89% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.37M SOL | 2.63% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.67M SOL | 2.24% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.26M SOL | 2.14% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.09% | 10% | 0 |
| 8 | `9eGrDohd…` | 6.94M SOL | 1.61% | 5% | 0 |
| 9 | `Awes4Tr6…` | 6.55M SOL | 1.52% | 0% | 0 |
| 10 | `9jxgosAf…` | 6.11M SOL | 1.42% | 100% | 0 |
| 11 | `5pPRHnie…` | 5.96M SOL | 1.38% | 5% | 0 |
| 12 | `JD549Hsb…` | 5.88M SOL | 1.36% | 0% | 0 |
| 13 | `5Cchr1XG…` | 5.65M SOL | 1.31% | 100% | 0 |
| 14 | `GnC339vk…` | 4.84M SOL | 1.12% | 7% | 0 |
| 15 | `9rkJMARq…` | 4.73M SOL | 1.10% | 8% | 0 |

### Delinquency alerts

- `EvnRmnMr…` · 7.37M SOL · commission 7% · lag 3679 slots
- `ChKZmewG…` · 184.38K SOL · commission 10% · lag 36264 slots
- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 582863 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 268500 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 99016 slots
- `4GEEKSwu…` · 196.81 SOL · commission 5% · lag 1333689 slots
- `EWARp8Sy…` · 99.64 SOL · commission 5% · lag 147305 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 1444204 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 63094431 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 887274 slots
- `4kdjgZKJ…` · 1.05 SOL · commission 100% · lag 447143301 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 500 | data/history.jsonl snapshot tape |
| TVL chart | 500 | data/history.jsonl snapshot tape |
| SOL chart | 500 | data/history.jsonl snapshot tape |
| history.jsonl rows | 500 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$613.63K** (6,155.5 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-13 |
| **Solana REV** | **7,126.1 SOL** / **$710.39K** | MEASURED UTC calendar day 2026-09-13: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-13 · UTC day 2026-09-13 · SOL-USD date 2026-09-13 |
| Jito tip-floor run-rate (NOT REV) | $109.30K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 109296 USD; at p95 floor → 1405370 USD. |
| Protocol fees 24h | $13.30M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.3h · n_tx=960 window_seconds=8314 |
| p90 / p99 | 0.000008 / 0.000083 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $101.72 | coingecko.simple_price |
| 24h change | +0.71% | coingecko.simple_price |
| Market cap | $59.74B | coingecko.simple_price |
| 24h volume | $3.33B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.93B |
| TVL 1d / 7d / 30d | +0.73% / +0.08% / +23.00% |
| DEX volume 24h | $2.21B · 1d +23.55% · vs-7d-ago -20.62% |
| 7d DEX volume | $17.14B · +2.45% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $13.30M |
| Fees 1d / 7d | -5.22% / -15.65% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $445.38M | +41.08% |
| Raydium AMM | $314.69M | +21.73% |
| BisonFi | $201.48M | 0.00% |
| Meteora DLMM | $198.81M | +26.04% |
| Orca DEX | $172.43M | +64.72% |
| fomo Wallet | $171.05M | +0.72% |
| Manifest Trade | $125.47M | +67.26% |
| HumidiFi | $108.44M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.57B | +2.92% | -0.91% |
| Kamino Lend | Lending | $1.36B | +1.54% | +1.90% |
| Raydium AMM | Dexs | $1.15B | +1.67% | +1.38% |
| Jupiter Lend | Lending | $1.10B | +1.39% | +0.84% |
| Binance Staked SOL | Liquid Staking | $1.06B | +2.43% | -1.43% |
| Jito Liquid Staking | Liquid Staking | $1.05B | +2.94% | -0.80% |
| BlackRock BUIDL | RWA | $992.89M | -0.70% | -2.93% |
| Jupiter Perpetual Exchange | Derivatives | $753.78M | +1.62% | +0.15% |
| Jupiter Staked SOL | Liquid Staking | $530.24M | +2.94% | -1.13% |
| Marinade Native | Staking Pool | $390.50M | +2.51% | -4.91% |

## Stablecoins

Solana circulating pegged-USD: **$15.99B**
(1d +0.24% · 7d -1.82%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.18B | -0.21% |
| USDT · Tether | $2.49B | -0.00% |
| USDGO · USDGO | $1.39B | +0.65% |
| USD1 · World Liberty Financial USD | $1.32B | +1.15% |
| BUIDL · BlackRock USD | $992.89M | +0.03% |
| PYUSD · PayPal USD | $702.38M | -0.73% |
| USDG · Global Dollar | $613.97M | +2.38% |
| USDe · Ethena USDe | $528.87M | -0.74% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $109.14M (lower bound, not a census).
24h volume $93.89M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.93B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.89M
- **OnRe** (RWA) — $299.85M
- **Huma Finance V2** (RWA) — $197.20M
- **Ondo Yield Assets** (RWA) — $179.69M
- **Hastra** (RWA) — $142.12M
- **Plume Vaults** (RWA) — $27.60M
- **Ondo Global Markets** (RWA) — $26.59M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.34M

## Daily active addresses

808,902 (Allium, as of 2026-09-13). Provider range 382,293–808,902. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @anza_xyz: Transactions V1 is now live on Solana, increasing max transaction sizes from 1,232 to 4,096 bytes. 

Complex operations like ZK proofs, large multisigs, and confidential transfers that required multiple transactions now fit in one.

Full details from @anza_xyz: https://x.com/anza_xyz/status/2099665631415341253](https://x.com/solana/status/2099685865572233303) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 02:24:55 GMT
- [x.com/i/article/209959253939…](https://x.com/anza_xyz/status/2099668755764871609) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:16:55 GMT
- [Full migration checklist, SDK minimum versions, and sample code in Rust, TypeScript, Go, and Python: https://solana.com/upgrades/larger-transaction-sizes](https://x.com/anza_xyz/status/2099665857135989215) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:05:24 GMT `upgrade`
- [Indexers, paymasters, and anyone reading priority fees: read transactionConfig instead of ComputeBudget instructions. Compute budget instructions are ignored for configuration in V1, so scanning them may return zero or misleading values for V1 transactions.

RPC operators: run v4.2.2 or v4.3.0-beta.3 to serve the larger size.](https://x.com/anza_xyz/status/2099665797732024594) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:05:10 GMT
- [Sending transactions for V1 is opt-in. Legacy and V0 remain supported while existing apps continue working as is.

Reading V1 transactions is not opt-in. If you read blocks or transactions over RPC, pass maxSupportedTransactionVersion: 1 on getTransaction, getBlock, and blockSubscribe. Without it, one V1 transaction fails the entire call.](https://x.com/anza_xyz/status/2099665716446441476) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:04:51 GMT
- [Transaction V1 (SIMD-0385) is live on mainnet-beta.

Max transaction size grows from 1,232 to 4,096 bytes. ZK proofs, large multisigs, BLS signatures, and confidential transfers that required multiple transactions now fit in one atomic operation.

V1 also moves resource requests (compute unit limit, priority fee, loaded accounts data size, heap size) into the transaction header instead of compute budget instructions.](https://x.com/anza_xyz/status/2099665631415341253) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:04:31 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: 🚨 V1 Transactions 🚨 

Coming in Epoch 1035 (~ 9 hours)!](https://x.com/readylayerone/status/2099527253936034154) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 14 Sep 2026 15:54:39 GMT
- [RT by @anza_xyz: Solana is the most battle-tested network.

Each stress test on Solana has been met with major improvements by the core engineering teams and further improved the network resiliency time over time.

Solana's resiliency isn't just about surviving the worst days, but also making ambition for a better future possible.

https://www.thestreet.com/crypto/innovation/solana-building-proving-and-earning-trust-in-public](https://x.com/jacobvcreech/status/2099517991662538803) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 14 Sep 2026 15:17:51 GMT
- [Transaction V1 (SIMD-0385) is live on mainnet-beta.](https://x.com/solana_devs/status/2099672228858069044) — X/Nitter-style RSS @solana_devs (not Twitter API) · Tue, 15 Sep 2026 01:30:44 GMT `upgrade` `mainnet`
- [Solana on 48 campuses across 11 countries.

Beautiful.](https://x.com/solana_devs/status/2099605540678607010) — X/Nitter-style RSS @solana_devs (not Twitter API) · Mon, 14 Sep 2026 21:05:44 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @anza_xyz: Transactions V1 is now live on Solana, increasing max transaction sizes from 1,232 to 4,096 bytes. 

Complex operations like ZK proofs, large multisigs, and confidential transfers that required multiple transactions now fit in one.

Full details from @anza_xyz: https://x.com/anza_xyz/status/2099665631415341253](https://x.com/solana/status/2099685865572233303) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 02:24:55 GMT
- [x.com/i/article/209959253939…](https://x.com/anza_xyz/status/2099668755764871609) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:16:55 GMT
- [Full migration checklist, SDK minimum versions, and sample code in Rust, TypeScript, Go, and Python: https://solana.com/upgrades/larger-transaction-sizes](https://x.com/anza_xyz/status/2099665857135989215) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:05:24 GMT `upgrade`
- [Indexers, paymasters, and anyone reading priority fees: read transactionConfig instead of ComputeBudget instructions. Compute budget instructions are ignored for configuration in V1, so scanning them may return zero or misleading values for V1 transactions.

RPC operators: run v4.2.2 or v4.3.0-beta.3 to serve the larger size.](https://x.com/anza_xyz/status/2099665797732024594) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:05:10 GMT
- [Sending transactions for V1 is opt-in. Legacy and V0 remain supported while existing apps continue working as is.

Reading V1 transactions is not opt-in. If you read blocks or transactions over RPC, pass maxSupportedTransactionVersion: 1 on getTransaction, getBlock, and blockSubscribe. Without it, one V1 transaction fails the entire call.](https://x.com/anza_xyz/status/2099665716446441476) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:04:51 GMT
- [Transaction V1 (SIMD-0385) is live on mainnet-beta.

Max transaction size grows from 1,232 to 4,096 bytes. ZK proofs, large multisigs, BLS signatures, and confidential transfers that required multiple transactions now fit in one atomic operation.

V1 also moves resource requests (compute unit limit, priority fee, loaded accounts data size, heap size) into the transaction header instead of compute budget instructions.](https://x.com/anza_xyz/status/2099665631415341253) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:04:31 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: 🚨 V1 Transactions 🚨 

Coming in Epoch 1035 (~ 9 hours)!](https://x.com/readylayerone/status/2099527253936034154) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 14 Sep 2026 15:54:39 GMT
- [RT by @anza_xyz: Solana is the most battle-tested network.

Each stress test on Solana has been met with major improvements by the core engineering teams and further improved the network resiliency time over time.

Solana's resiliency isn't just about surviving the worst days, but also making ambition for a better future possible.

https://www.thestreet.com/crypto/innovation/solana-building-proving-and-earning-trust-in-public](https://x.com/jacobvcreech/status/2099517991662538803) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 14 Sep 2026 15:17:51 GMT
- [Transaction V1 (SIMD-0385) is live on mainnet-beta.](https://x.com/solana_devs/status/2099672228858069044) — X/Nitter-style RSS @solana_devs (not Twitter API) · Tue, 15 Sep 2026 01:30:44 GMT `upgrade` `mainnet`
- [Solana on 48 campuses across 11 countries.

Beautiful.](https://x.com/solana_devs/status/2099605540678607010) — X/Nitter-style RSS @solana_devs (not Twitter API) · Mon, 14 Sep 2026 21:05:44 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-15 (2026-09-14 20:07:16 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 508ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 551ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 466ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 438ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 509ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6171ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 968ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 142ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 201ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 376ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 88ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 90ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1164ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 256ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 467ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 132ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 143ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 596ms https://solana.com/data
- `solana.com.databricks` [ok] 200 191ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 1370ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 258ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 112ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 132ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 611ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 514ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 162ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 180ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 167ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 272ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 317ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1705ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1811ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 332ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 133ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 464ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 538ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 510ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 213ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 464ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 132ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [ok] 200 2054ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1733ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2172ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1964ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1823ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 544ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 277ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 565ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 222ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 581ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 211ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 485ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 209ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 515ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 173ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [ok] 200 2212ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 516ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 189ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 2963ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1878ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1705ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1715ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1770ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1480ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1594ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1481ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.SPYx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.FLNCx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.WRLDx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.circ.SPYx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.WGSx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.circ.WRLDx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.INDIx` [ok] 200 548ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.QQQx` [ok] 200 633ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.FLNCx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.XRXx` [ok] 200 1003ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.circ.QQQx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.METCx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.INDIx` [ok] 200 602ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.XRXx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.PCTx` [ok] 200 488ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.WYFIx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.METCx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.price.QUBTx` [ok] 200 632ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.mult.COINx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.WYFIx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.BETRx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.QUBTx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.price.DRSx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.mult.QQQx` [ok] 200 1018ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.DRSx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 866ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 484ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.SAILx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.price.SCIx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.price.BSYx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.circ.SAILx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 431ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.circ.SCIx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.price.MPx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.mult.BETRx` [ok] 200 583ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.GSATx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.mult.SCIx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.circ.BSYx` [ok] 200 551ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.circ.MPx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 2043ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.GSATx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.mult.SAILx` [ok] 200 718ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.mult.BSYx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.price.DCIx` [ok] 200 530ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.price.RYANx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.price.BXPx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.price.DVAx` [ok] 200 831ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.price.GDDYx` [ok] 200 545ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.mult.GSATx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.price.DYx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.circ.BXPx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.circ.RYANx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.circ.GDDYx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.circ.DVAx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.mult.RYANx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 392ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.mult.MPx` [ok] 200 892ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.mult.GDDYx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.mult.DVAx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.circ.FRHCx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.price.WMSx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.circ.DYx` [ok] 200 617ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.price.FDSx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.price.ALSNx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.mult.BXPx` [ok] 200 616ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.AMx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.ALSNx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.circ.WMSx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.circ.FDSx` [ok] 200 431ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.price.SMTCx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.mult.DYx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.price.SFx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.mult.WMSx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.mult.DCIx` [ok] 200 1221ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.circ.SMTCx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.circ.SFx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.price.BPOPx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.price.AXSMx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.mult.ALSNx` [ok] 200 691ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.price.TTMIx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.price.EGPx` [ok] 200 490ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.mult.SFx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.circ.AXSMx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.mult.SMTCx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.mult.AMx` [ok] 200 875ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.circ.EGPx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.price.AEISx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.price.DPZx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.circ.TTMIx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.BPOPx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.mult.AXSMx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.price.KTOSx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.mult.EGPx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.AEISx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.circ.DPZx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.mult.TTMIx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.HRLx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.price.PAGx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.price.HIIx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.circ.HRLx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.price.EHCx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.price.SEICx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.mult.DPZx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.circ.PAGx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.circ.HIIx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.mult.AEISx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.circ.EHCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.circ.KTOSx` [ok] 200 563ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.circ.SEICx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.mult.HRLx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.mult.PAGx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.mult.HIIx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.price.ARx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.mult.KTOSx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.mult.EHCx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.SEICx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.price.WTRGx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.HALOx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.circ.ARx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.price.AFGx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.price.DOCUx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.price.MGMx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.price.HUBSx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.mult.ARx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.circ.HUBSx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.circ.MGMx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.circ.DOCUx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.price.GFLx` [ok] 200 1168ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.mult.DOCUx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.circ.HALOx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.mult.HUBSx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.mult.MGMx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.circ.AFGx` [ok] 200 663ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.circ.WTRGx` [ok] 200 697ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.price.GMEDx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.price.IESCx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.price.JKHYx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.price.AMKRx` [ok] 200 712ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.mult.AFGx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.circ.GFLx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.HALOx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.circ.IESCx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.price.OCx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.circ.JKHYx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.circ.AMKRx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.price.BMRNx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.mult.GFLx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.circ.OCx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.price.CRx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.mult.AMKRx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.price.JEFx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.circ.BMRNx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.circ.CRx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.mult.OCx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.circ.GMEDx` [ok] 200 843ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.price.AMHx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.JEFx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.mult.BMRNx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.price.FIVEx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.mult.JKHYx` [ok] 200 708ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.mult.CRx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.circ.AMHx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.circ.FIVEx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.price.ITx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.price.MDGLx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.price.VNOMx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.mult.JEFx` [ok] 200 513ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 567ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.mult.AMHx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.circ.ITx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.mult.FIVEx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.mult.IESCx` [ok] 200 1246ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.circ.VNOMx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.price.UHALx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.price.IVZx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.price.AHRx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.mult.ITx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.price.CORTx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.price.STRLx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.mult.VNOMx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.circ.IVZx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.circ.CORTx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.price.NWSAx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.price.AURx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.circ.AHRx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.circ.UHALx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.circ.STRLx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.circ.MDGLx` [ok] 200 909ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.circ.NWSAx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.mult.IVZx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.circ.AURx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.mult.AHRx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.mult.CORTx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.mult.STRLx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.mult.UHALx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.mult.NWSAx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.mult.MDGLx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.price.Hx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.mult.AURx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.price.ARWRx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.price.GWREx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.price.NWSx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.price.BAXx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.price.MANHx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.circ.Hx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.circ.GWREx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.price.CACIx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.circ.ARWRx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.circ.BAXx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.circ.MANHx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.circ.CACIx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.mult.GWREx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.mult.MANHx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.mult.Hx` [ok] 200 902ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 81ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 357ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INDIx` [ok] 200 168ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 139ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 144ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.FLNCx` [ok] 200 136ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.BETRx` [ok] 200 142ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.XRXx` [ok] 200 148ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.AIx` [ok] 200 166ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.WGSx` [ok] 200 156ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jito.tip_floor` [ok] 200 326ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 296ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 151ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 463ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 538ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 467ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 440ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 190ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
