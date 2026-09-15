# Borealis — Solana ecosystem report

**Generated** 2026-09-15T02:27:11Z · 2026-09-14 19:27:11 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-15T02:26:59Z · **RPC health** `ok`
**Health score** 76 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** WATCH · **Ecosystem** CONTRACTION — SOL 24h +1.37%; DEX 24h $2.19B · 1d +23% · vs-7d-ago -21%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -21.29%. (threshold: `|7d %| >= 20`)
- **WARN · High validator delinquency** — 11 delinquent vote accounts, 1.752% of activated+delinquent stake. (threshold: `delinquent stake >= 1% or delinquent count >= 25`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +22.52%. (threshold: `|1d %| >= 8`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 447,135,678 |
| Block height | 425,177,822 |
| Block time | 2026-09-15T02:26:59Z |
| Epoch | 1,035 (3.63% · slot 15,679/432,000) |
| Mean TPS (last ~3,600s) | 3,763.8 |
| Mean non-vote TPS | 1,656.2 |
| Median TPS (same window) | 3,751.2 |
| Mean slot time | 315.7 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 548,557,967,508 |
| Circulating supply | 587,028,520 SOL |
| Total supply | 634,111,924 SOL |
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

- `EvnRmnMr…` · 7.37M SOL · commission 7% · lag 1668 slots
- `ChKZmewG…` · 184.38K SOL · commission 10% · lag 28641 slots
- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 575240 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 260877 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 91393 slots
- `4GEEKSwu…` · 196.81 SOL · commission 5% · lag 1326066 slots
- `EWARp8Sy…` · 99.64 SOL · commission 5% · lag 139682 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 1436581 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 63086808 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 879651 slots
- `4kdjgZKJ…` · 1.05 SOL · commission 100% · lag 447135678 slots

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
| Jito tip-floor run-rate (NOT REV) | $72.95K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 72946 USD; at p95 floor → 676201 USD. |
| Protocol fees 24h | $14.42M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~1.6h · n_tx=1280 window_seconds=5813 |
| p90 / p99 | 0.000008 / 0.000410 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $102.28 | coingecko.simple_price |
| 24h change | +1.37% | coingecko.simple_price |
| Market cap | $60.03B | coingecko.simple_price |
| 24h volume | $3.36B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.93B |
| TVL 1d / 7d / 30d | +0.11% / +0.15% / +23.08% |
| DEX volume 24h | $2.19B · 1d +22.52% · vs-7d-ago -21.29% |
| 7d DEX volume | $17.12B · +2.34% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.42M |
| Fees 1d / 7d | +2.73% / -8.57% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $445.38M | +41.08% |
| Raydium AMM | $318.38M | +23.15% |
| BisonFi | $201.48M | 0.00% |
| Meteora DLMM | $198.81M | +26.04% |
| Orca DEX | $172.43M | +64.72% |
| fomo Wallet | $171.16M | +0.79% |
| Manifest Trade | $129.90M | +73.16% |
| HumidiFi | $108.44M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.57B | +2.92% | -0.91% |
| Kamino Lend | Lending | $1.36B | +1.54% | +1.90% |
| Raydium AMM | Dexs | $1.15B | +1.67% | +1.38% |
| Jupiter Lend | Lending | $1.11B | +1.77% | +1.21% |
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
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $109.24M (lower bound, not a census).
24h volume $93.96M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
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
- [RT by @anza_xyz: The way you experience @solana dev content has just changed forever. 

Give a follow to @solanadevs on Instagram: https://www.instagram.com/solanadevs](https://x.com/solana_devs/status/2099186847343661436) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 13 Sep 2026 17:22:00 GMT
- [Transaction V1 (SIMD-0385) is live on mainnet-beta.](https://x.com/solana_devs/status/2099672228858069044) — X/Nitter-style RSS @solana_devs (not Twitter API) · Tue, 15 Sep 2026 01:30:44 GMT `upgrade` `mainnet`
- [Solana on 48 campuses across 11 countries.

Beautiful.](https://x.com/solana_devs/status/2099605540678607010) — X/Nitter-style RSS @solana_devs (not Twitter API) · Mon, 14 Sep 2026 21:05:44 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

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
- [RT by @anza_xyz: The way you experience @solana dev content has just changed forever. 

Give a follow to @solanadevs on Instagram: https://www.instagram.com/solanadevs](https://x.com/solana_devs/status/2099186847343661436) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 13 Sep 2026 17:22:00 GMT
- [Transaction V1 (SIMD-0385) is live on mainnet-beta.](https://x.com/solana_devs/status/2099672228858069044) — X/Nitter-style RSS @solana_devs (not Twitter API) · Tue, 15 Sep 2026 01:30:44 GMT `upgrade` `mainnet`
- [Solana on 48 campuses across 11 countries.

Beautiful.](https://x.com/solana_devs/status/2099605540678607010) — X/Nitter-style RSS @solana_devs (not Twitter API) · Mon, 14 Sep 2026 21:05:44 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-15 (2026-09-14 19:27:11 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 326ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 228ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 205ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 194ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 182ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7445ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 444ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 185ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 95ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 88ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 80ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 70ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 105ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 358ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 160ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 145ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 164ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 486ms https://solana.com/data
- `solana.com.databricks` [ok] 200 132ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 516ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 154ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 128ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 131ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 221ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 384ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 213ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 202ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 197ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 423ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 211ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 4435ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 5807ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 316ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 241ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 211ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 184ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 270ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 216ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 259ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 191ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [ok] 200 834ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 807ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1004ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 952ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1032ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 738ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 824ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 856ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 325ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 293ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 239ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 233ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 341ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 319ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 264ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 229ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1617ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2034ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1939ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1636ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2130ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1841ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1804ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1115ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.WRLDx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.INDIx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WGSx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.FLNCx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.COINx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.XRXx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.circ.FLNCx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.SPYx` [ok] 200 555ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.XRXx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.WRLDx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 566ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 601ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 545ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.mult.COINx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.PCTx` [ok] 200 554ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.QUBTx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.BETRx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.mult.WGSx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.WYFIx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.METCx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.QUBTx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.price.DRSx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.circ.PCTx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.SCIx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.price.AIx` [ok] 200 547ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.PCTx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.circ.DRSx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 543ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.SCIx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.circ.BETRx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.SAILx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.price.BSYx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.price.GSATx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.mult.METCx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.BETRx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.DRSx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.mult.SCIx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.circ.BSYx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.circ.SAILx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.price.DVAx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.price.MPx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.mult.AIx` [ok] 200 572ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.circ.DVAx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.circ.MPx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.circ.GSATx` [ok] 200 510ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.price.RYANx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.mult.SAILx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.price.DCIx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.mult.BSYx` [ok] 200 522ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.mult.MPx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.circ.RYANx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.mult.DVAx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.mult.GSATx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.price.GDDYx` [ok] 200 685ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.price.DYx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.price.BXPx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.price.FRHCx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.circ.GDDYx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.price.AMx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.mult.RYANx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.circ.BXPx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.price.WMSx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.mult.GDDYx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.DCIx` [ok] 200 630ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.circ.DYx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.price.FDSx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.mult.BXPx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.circ.FRHCx` [ok] 200 525ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.mult.AMx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.price.SMTCx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.price.SFx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.circ.WMSx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.mult.FRHCx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.circ.FDSx` [ok] 200 392ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.circ.SMTCx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.price.AXSMx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.price.ALSNx` [ok] 200 608ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.circ.SFx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.price.EGPx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.price.BPOPx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.circ.AXSMx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.circ.ALSNx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.circ.EGPx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.mult.SMTCx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.mult.WMSx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.mult.ALSNx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.mult.SFx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.mult.EGPx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.price.AEISx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.mult.BPOPx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.price.HRLx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.price.DPZx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.price.PAGx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.circ.AEISx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.circ.HRLx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.circ.DPZx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.price.TTMIx` [ok] 200 753ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.mult.AEISx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.mult.HRLx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.circ.TTMIx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.AXSMx` [ok] 200 1039ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.price.SEICx` [ok] 200 639ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.price.HIIx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.price.KTOSx` [ok] 200 847ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.price.EHCx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.mult.DPZx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.circ.SEICx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.price.GFLx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.circ.HIIx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.mult.TTMIx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.circ.KTOSx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.circ.GFLx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.price.ARx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.mult.SEICx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.mult.HIIx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.mult.KTOSx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.price.MGMx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.circ.EHCx` [ok] 200 574ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.circ.ARx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.mult.GFLx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.price.WTRGx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.DOCUx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.circ.PAGx` [ok] 200 1349ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.price.HALOx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.circ.MGMx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.circ.WTRGx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.mult.ARx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.mult.MGMx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.price.AFGx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.circ.DOCUx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.mult.EHCx` [ok] 200 611ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.PAGx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.price.AMKRx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.circ.AFGx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.circ.HALOx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.price.HUBSx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.mult.DOCUx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.price.JKHYx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.price.GMEDx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.price.IESCx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.circ.AMKRx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.mult.AFGx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.price.OCx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.circ.IESCx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.circ.JKHYx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.mult.AMKRx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.circ.HUBSx` [ok] 200 516ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.price.CRx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.circ.OCx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.mult.IESCx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.mult.HALOx` [ok] 200 657ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.mult.JKHYx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.circ.CRx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.price.JEFx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.mult.OCx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.price.BMRNx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.price.FIVEx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.price.ITx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.mult.HUBSx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.mult.CRx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.price.MDGLx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.circ.JEFx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.circ.BMRNx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.circ.ITx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.price.AMHx` [ok] 200 563ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.FIVEx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.circ.MDGLx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.mult.BMRNx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.mult.JEFx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.circ.AMHx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.price.UHALx` [ok] 200 403ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.mult.FIVEx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.price.AHRx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.mult.MDGLx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.mult.ITx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.price.IVZx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.price.VNOMx` [ok] 200 710ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.circ.UHALx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.price.NWSAx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.circ.IVZx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.circ.AHRx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.circ.VNOMx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.mult.UHALx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.price.CORTx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.circ.NWSAx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.mult.IVZx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.mult.AHRx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.mult.VNOMx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.AURx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.price.Hx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.circ.CORTx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.price.STRLx` [ok] 200 687ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.price.ARWRx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.mult.NWSAx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.circ.AURx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.price.GWREx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.circ.Hx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.mult.CORTx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.MANHx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.circ.STRLx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.circ.GWREx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.price.NWSx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.price.CACIx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.mult.AURx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.mult.Hx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.mult.STRLx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.circ.CACIx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.price.BAXx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.MANHx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.circ.ARWRx` [ok] 200 629ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.circ.BAXx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.mult.CACIx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.mult.MANHx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 86ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 241ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INDIx` [ok] 200 98ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 114ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.FLNCx` [ok] 200 111ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.BETRx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.XRXx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.AIx` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.WGSx` [ok] 200 91ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jito.tip_floor` [ok] 200 392ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 423ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 123ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 183ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 220ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 197ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 195ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 246ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
