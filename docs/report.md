# Borealis — Solana ecosystem report

**Generated** 2026-09-15T17:50:16Z · 2026-09-15 10:50:16 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-15T17:50:06Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -2.92%; DEX 24h $2.53B · 1d +41% · vs-7d-ago -9%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +41.27%. (threshold: `|1d %| >= 8`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 447,311,039 |
| Block height | 425,352,840 |
| Block time | 2026-09-15T17:50:06Z |
| Epoch | 1,035 (44.22% · slot 191,041/432,000) |
| Mean TPS (last ~3,600s) | 4,327.9 |
| Mean non-vote TPS | 2,201.7 |
| Median TPS (same window) | 4,310.1 |
| Mean slot time | 317.1 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 548,766,683,494 |
| Circulating supply | 587,027,820 SOL |
| Total supply | 634,111,376 SOL |
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
| Activated stake | 439,005,892 SOL |
| Delinquent stake | 242,746.93 SOL (0.055%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.33% / 35.58% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.76M SOL | 4.04% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.37M SOL | 3.73% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.49M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.37M SOL | 2.59% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.67M SOL | 2.20% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.26M SOL | 2.11% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.37M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.94M SOL | 1.58% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.55M SOL | 1.49% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.11M SOL | 1.39% | 100% | 0 |
| 12 | `5pPRHnie…` | 5.96M SOL | 1.36% | 5% | 0 |
| 13 | `JD549Hsb…` | 5.88M SOL | 1.34% | 0% | 0 |
| 14 | `5Cchr1XG…` | 5.65M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.84M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 750601 slots
- `GK2YYwmQ…` · 82.46K SOL · commission 0% · lag 19111 slots
- `mrgn4atx…` · 19.36K SOL · commission 0% · lag 54999 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 436238 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 266754 slots
- `4GEEKSwu…` · 196.81 SOL · commission 5% · lag 1501427 slots
- `EWARp8Sy…` · 99.64 SOL · commission 5% · lag 315043 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 1611942 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 63262169 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 1055012 slots
- `4kdjgZKJ…` · 1.05 SOL · commission 100% · lag 447311039 slots

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
| Jito tip-floor run-rate (NOT REV) | $59.21K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 59206 USD; at p95 floor → 19024950 USD. |
| Protocol fees 24h | $13.58M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $100.01 | coingecko.simple_price |
| 24h change | -2.92% | coingecko.simple_price |
| Market cap | $58.71B | coingecko.simple_price |
| 24h volume | $3.46B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.78B |
| TVL 1d / 7d / 30d | -0.95% / -2.43% / +19.91% |
| DEX volume 24h | $2.53B · 1d +41.27% · vs-7d-ago -9.24% |
| 7d DEX volume | $18.20B · +8.83% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $13.58M |
| Fees 1d / 7d | -3.25% / -13.90% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $445.38M | +41.08% |
| BisonFi | $315.80M | +56.74% |
| Raydium AMM | $241.36M | -6.64% |
| Meteora DLMM | $198.81M | +26.04% |
| fomo Wallet | $187.20M | +10.23% |
| HumidiFi | $179.41M | +65.45% |
| Orca DEX | $154.63M | +47.71% |
| Manifest Trade | $120.20M | +60.24% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.54B | -1.04% | -2.68% |
| Kamino Lend | Lending | $1.34B | -1.11% | +0.64% |
| Raydium AMM | Dexs | $1.11B | -1.76% | -2.57% |
| Jupiter Lend | Lending | $1.08B | -2.39% | +0.06% |
| Binance Staked SOL | Liquid Staking | $1.03B | -2.39% | -4.26% |
| Jito Liquid Staking | Liquid Staking | $1.02B | -2.21% | -2.95% |
| BlackRock BUIDL | RWA | $992.98M | -0.71% | -2.95% |
| Jupiter Perpetual Exchange | Derivatives | $737.59M | -2.17% | -1.86% |
| Jupiter Staked SOL | Liquid Staking | $514.64M | -1.97% | -3.12% |
| Sentora Curator | Risk Curators | $383.67M | +0.69% | +0.97% |

## Stablecoins

Solana circulating pegged-USD: **$15.73B**
(1d +0.22% · 7d -1.84%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.93B | -3.68% |
| USDT · Tether | $2.48B | +0.00% |
| USDGO · USDGO | $1.38B | -0.43% |
| USD1 · World Liberty Financial USD | $1.32B | +1.15% |
| BUIDL · BlackRock USD | $992.98M | +0.04% |
| PYUSD · PayPal USD | $712.64M | +0.76% |
| USDG · Global Dollar | $612.39M | +2.13% |
| USDe · Ethena USDe | $527.82M | -0.88% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $108.27M (lower bound, not a census).
24h volume $83.22M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.92B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.98M
- **OnRe** (RWA) — $300.56M
- **Huma Finance V2** (RWA) — $187.55M
- **Ondo Yield Assets** (RWA) — $180.09M
- **Hastra** (RWA) — $139.87M
- **Plume Vaults** (RWA) — $28.06M
- **Ondo Global Markets** (RWA) — $26.45M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.35M

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

- [JUST IN: Solana daily stablecoin active addresses hit 888K in September, up 269% from 333K a year ago.](https://x.com/solana/status/2099910897657602109) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 17:19:07 GMT
- [RT by @solana: Agentic Payments 🤝 Solana](https://x.com/solana_devs/status/2099893640071921795) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 16:10:32 GMT
- [RT by @solana: Opinion markets, not another prediction market.
No oracles. No “did it happen?"

You stake USDC on whether people agree with your take.
24 hours. Early conviction pays more.

Now on Seeker, App Store and Google Play.

Thanks @sunnymaanz + @marccolcer for breaking it down.](https://x.com/b4opinion/status/2099897803350986767) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 16:27:05 GMT
- [RT by @solana: Issuance and trading tell two different stories.

@Solana executes 74% of measured onchain fixed-income spot volume, with $5.4B traded over the past 12 months.

But almost all of that activity comes from private credit.

Meanwhile, products like BlackRock's BUIDL have grown through issuance and redemption rather than secondary trading -- BUIDL alone reached $741M on Solana in 2026.

It's why measuring RWA adoption requires looking beyond TVL and market cap.

More in the report: https://www.allium.so/reports/solana-rwa-ecosystem](https://x.com/AlliumLabs/status/2099891054166315398) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 16:00:16 GMT
- [RT by @solana: Cloak mainnet is live.

Onchain finance shouldn't mean public finance.

Cloak keeps your balances, amounts, and counterparties private, while letting you prove exactly what matters to exactly the people who need to see it.

Private by default. Auditable when required.

⚡ 0% protocol fees on USDC transactions for launch week.

https://www.cloak.ag/privacy](https://x.com/cloak_ag/status/2099883991151022258) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 15:32:12 GMT `mainnet`
- [$FLY is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2099878109818630542) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 15:08:49 GMT
- [Firefly Aerospace ($FLY) is the space and defense company behind Blue Ghost, the first commercial lander to touch down on the Moon.

Verify on Orb:
https://orbmarkets.io/token/FLYRq3en8r2Z69gN3KyAnDrvnitEJNkwPYY7favinHeD](https://x.com/solana/status/2099878107633361340) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 15:08:49 GMT
- [$FLY is now live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2099878104730947608) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 15:08:48 GMT
- [RT by @anza_xyz: 🚨JUST IN: @Solana co-founder @Toly says Transaction V1, which went live on Solana mainnet today, removed “the biggest blocker” to making the network quantum resistant.](https://x.com/SolanaFloor/status/2099866466615206209) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 14:22:33 GMT `mainnet`
- [RT by @anza_xyz: Transactions V1 is now live on Solana, increasing max transaction sizes from 1,232 to 4,096 bytes. 

Complex operations like ZK proofs, large multisigs, and confidential transfers that required multiple transactions now fit in one.

Full details from @anza_xyz: https://x.com/anza_xyz/status/2099665631415341253](https://x.com/solana/status/2099685865572233303) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 02:24:55 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [JUST IN: Solana daily stablecoin active addresses hit 888K in September, up 269% from 333K a year ago.](https://x.com/solana/status/2099910897657602109) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 17:19:07 GMT
- [RT by @solana: Agentic Payments 🤝 Solana](https://x.com/solana_devs/status/2099893640071921795) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 16:10:32 GMT
- [RT by @solana: Opinion markets, not another prediction market.
No oracles. No “did it happen?"

You stake USDC on whether people agree with your take.
24 hours. Early conviction pays more.

Now on Seeker, App Store and Google Play.

Thanks @sunnymaanz + @marccolcer for breaking it down.](https://x.com/b4opinion/status/2099897803350986767) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 16:27:05 GMT
- [RT by @solana: Issuance and trading tell two different stories.

@Solana executes 74% of measured onchain fixed-income spot volume, with $5.4B traded over the past 12 months.

But almost all of that activity comes from private credit.

Meanwhile, products like BlackRock's BUIDL have grown through issuance and redemption rather than secondary trading -- BUIDL alone reached $741M on Solana in 2026.

It's why measuring RWA adoption requires looking beyond TVL and market cap.

More in the report: https://www.allium.so/reports/solana-rwa-ecosystem](https://x.com/AlliumLabs/status/2099891054166315398) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 16:00:16 GMT
- [RT by @solana: Cloak mainnet is live.

Onchain finance shouldn't mean public finance.

Cloak keeps your balances, amounts, and counterparties private, while letting you prove exactly what matters to exactly the people who need to see it.

Private by default. Auditable when required.

⚡ 0% protocol fees on USDC transactions for launch week.

https://www.cloak.ag/privacy](https://x.com/cloak_ag/status/2099883991151022258) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 15:32:12 GMT `mainnet`
- [$FLY is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2099878109818630542) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 15:08:49 GMT
- [Firefly Aerospace ($FLY) is the space and defense company behind Blue Ghost, the first commercial lander to touch down on the Moon.

Verify on Orb:
https://orbmarkets.io/token/FLYRq3en8r2Z69gN3KyAnDrvnitEJNkwPYY7favinHeD](https://x.com/solana/status/2099878107633361340) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 15:08:49 GMT
- [$FLY is now live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2099878104730947608) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 15 Sep 2026 15:08:48 GMT
- [RT by @anza_xyz: 🚨JUST IN: @Solana co-founder @Toly says Transaction V1, which went live on Solana mainnet today, removed “the biggest blocker” to making the network quantum resistant.](https://x.com/SolanaFloor/status/2099866466615206209) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 14:22:33 GMT `mainnet`
- [RT by @anza_xyz: Transactions V1 is now live on Solana, increasing max transaction sizes from 1,232 to 4,096 bytes. 

Complex operations like ZK proofs, large multisigs, and confidential transfers that required multiple transactions now fit in one.

Full details from @anza_xyz: https://x.com/anza_xyz/status/2099665631415341253](https://x.com/solana/status/2099685865572233303) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 02:24:55 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-15 (2026-09-15 10:50:16 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **Median tx fee** — no getBlock samples
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 409ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 424ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 426ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 427ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 374ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6203ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 742ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 237ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 150ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 158ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 122ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 106ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1765ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 361ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 416ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 199ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 264ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 380ms https://solana.com/data
- `solana.com.databricks` [ok] 200 183ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 1336ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 194ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 92ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 235ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 370ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 334ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 166ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 163ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 167ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 2078ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 487ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2630ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1792ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 162ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 359ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 353ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 398ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 178ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 403ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 191ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 657ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 293ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 570ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 522ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 525ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 326ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 554ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 306ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 509ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 240ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 605ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 232ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 530ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 237ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 554ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 298ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 587ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 277ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 491ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 230ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 483ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 244ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 425ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 257ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 2159ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1542ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1723ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1071ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1293ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1335ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1694ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1299ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.WRLDx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.QQQx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.SPYx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.INDIx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.circ.WRLDx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.price.FLNCx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.WGSx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.COINx` [ok] 200 574ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.WRLDx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.XRXx` [ok] 200 1004ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.mult.QQQx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.PCTx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.mult.SPYx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.METCx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.mult.WGSx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.PCTx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.price.AIx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.price.QUBTx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.BETRx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.WYFIx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.price.DRSx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.circ.FLNCx` [ok] 200 1292ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.BETRx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.circ.DRSx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.BSYx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.mult.QUBTx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.SAILx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.mult.BETRx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.SCIx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.mult.DRSx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.GSATx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.circ.BSYx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 1321ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.price.DVAx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.price.MPx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.price.DCIx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.circ.SCIx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.BSYx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.mult.SCIx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.circ.SAILx` [ok] 200 864ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.price.BXPx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.price.GDDYx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.circ.GSATx` [ok] 200 1039ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.circ.DCIx` [ok] 200 870ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.mult.SAILx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 910ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.circ.MPx` [ok] 200 1302ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.mult.GSATx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.DVAx` [ok] 200 1344ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.mult.DCIx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.circ.RYANx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.price.DYx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.price.WMSx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.price.FRHCx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.mult.MPx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.mult.DVAx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.mult.RYANx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.price.FDSx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.price.ALSNx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.circ.BXPx` [ok] 200 1169ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.circ.ALSNx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.mult.BXPx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.AMx` [ok] 200 624ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.mult.ALSNx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.price.SMTCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.price.SFx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.circ.DYx` [ok] 200 1180ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.circ.FRHCx` [ok] 200 1198ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.circ.WMSx` [ok] 200 1296ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.mult.FRHCx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.mult.WMSx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.AXSMx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.circ.FDSx` [ok] 200 1362ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.price.EGPx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.circ.GDDYx` [ok] 200 2371ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.mult.GDDYx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 1177ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.price.BPOPx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.circ.SMTCx` [ok] 200 1110ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.mult.SMTCx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.circ.SFx` [ok] 200 1303ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.price.TTMIx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.mult.AMx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.price.DPZx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.circ.TTMIx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.price.AEISx` [ok] 200 528ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.mult.SFx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.circ.DPZx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.price.KTOSx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.mult.TTMIx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.circ.AXSMx` [ok] 200 1015ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.circ.KTOSx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.price.PAGx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.mult.AXSMx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.price.HRLx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.mult.KTOSx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.mult.DPZx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 999ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.circ.PAGx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.circ.HRLx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.price.HIIx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.price.SEICx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.price.EHCx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.mult.BPOPx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.mult.PAGx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.circ.EGPx` [ok] 200 1492ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.circ.HIIx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.mult.HRLx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.circ.SEICx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.circ.EHCx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.price.GFLx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.mult.EGPx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.mult.HIIx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.mult.SEICx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.mult.EHCx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.circ.AEISx` [ok] 200 1148ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.price.HALOx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.price.MGMx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.price.DOCUx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.circ.GFLx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.price.AFGx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.mult.AEISx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.mult.GFLx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.circ.MGMx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.price.WTRGx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.ARx` [ok] 200 760ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.price.HUBSx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.mult.MGMx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.price.AMKRx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.price.GMEDx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.circ.ARx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.mult.ARx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.circ.DOCUx` [ok] 200 1002ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.price.JKHYx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.DOCUx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.circ.HALOx` [ok] 200 1311ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.price.IESCx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.circ.WTRGx` [ok] 200 1099ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.mult.HALOx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.circ.AFGx` [ok] 200 1439ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.mult.WTRGx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.price.OCx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.circ.HUBSx` [ok] 200 1310ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.price.CRx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.mult.HUBSx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.circ.GMEDx` [ok] 200 1323ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.circ.AMKRx` [ok] 200 1492ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.circ.JKHYx` [ok] 200 882ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.mult.GMEDx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.mult.AFGx` [ok] 200 633ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.price.BMRNx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.mult.JKHYx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.mult.AMKRx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.price.FIVEx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.price.JEFx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.price.AMHx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.IESCx` [ok] 200 1127ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.circ.JEFx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.mult.IESCx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.ITx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.mult.JEFx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.price.MDGLx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.price.VNOMx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.circ.BMRNx` [ok] 200 959ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.circ.OCx` [ok] 200 1523ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.circ.CRx` [ok] 200 1468ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.mult.BMRNx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.circ.FIVEx` [ok] 200 1014ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.mult.OCx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.circ.AMHx` [ok] 200 1089ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.mult.CRx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.price.UHALx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.mult.FIVEx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.circ.ITx` [ok] 200 958ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.price.IVZx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.price.CORTx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.circ.UHALx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.price.AHRx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.mult.ITx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.UHALx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.price.STRLx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.circ.MDGLx` [ok] 200 1014ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.price.NWSAx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.price.AURx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.mult.MDGLx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.circ.VNOMx` [ok] 200 1324ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.circ.STRLx` [ok] 200 698ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.mult.VNOMx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.circ.IVZx` [ok] 200 987ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.price.Hx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.mult.STRLx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.price.ARWRx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.mult.IVZx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.price.NWSx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.price.GWREx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.circ.CORTx` [ok] 200 1402ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 1096ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.mult.CORTx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.mult.AURx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.circ.NWSAx` [ok] 200 1512ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.circ.AHRx` [ok] 200 1853ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.mult.NWSAx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.price.CACIx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.mult.AHRx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.MANHx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.circ.ARWRx` [ok] 200 1077ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.price.BAXx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.CACIx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.circ.NWSx` [ok] 200 1051ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.circ.MANHx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.circ.GWREx` [ok] 200 1054ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.mult.ARWRx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.circ.Hx` [ok] 200 1529ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.mult.MANHx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.circ.BAXx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.NWSx` [ok] 200 615ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 406ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.Hx` [ok] 200 611ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1149ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 259ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.QUBTx` [ok] 200 125ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.INDIx` [ok] 200 204ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.WRLDx` [ok] 200 130ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.XRXx` [ok] 200 101ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 118ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.FLNCx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.WGSx` [ok] 200 107ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.AIx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jito.tip_floor` [ok] 200 140ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 350ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 136ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 384ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 350ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 365ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 352ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 252ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
