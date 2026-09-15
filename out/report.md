# Borealis — Solana ecosystem report

**Generated** 2026-09-15T23:35:50Z · 2026-09-15 16:35:50 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-15T23:35:40Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -5.40%; DEX 24h $2.51B · 1d +40% · vs-7d-ago -10%; slot 318 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +40.24%. (threshold: `|1d %| >= 8`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 447,376,258 |
| Block height | 425,417,923 |
| Block time | 2026-09-15T23:35:40Z |
| Epoch | 1,035 (59.32% · slot 256,259/432,000) |
| Mean TPS (last ~3,600s) | 4,478.2 |
| Mean non-vote TPS | 2,356.7 |
| Median TPS (same window) | 4,420.4 |
| Mean slot time | 317.7 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 548,866,534,384 |
| Circulating supply | 587,027,559 SOL |
| Total supply | 634,111,115 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 679 |
| Delinquent | 10 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,088,348 SOL |
| Delinquent stake | 160,291.40 SOL (0.036%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.33% / 35.57% |
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

- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 815820 slots
- `mrgn4atx…` · 19.36K SOL · commission 0% · lag 120218 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 501457 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 331973 slots
- `4GEEKSwu…` · 196.81 SOL · commission 5% · lag 1566646 slots
- `EWARp8Sy…` · 99.64 SOL · commission 5% · lag 380262 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 1677161 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 63327388 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 1120231 slots
- `4kdjgZKJ…` · 1.05 SOL · commission 100% · lag 447376258 slots

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
| Jito tip-floor run-rate (NOT REV) | $49.32K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 49320 USD; at p95 floor → 887469 USD. |
| Protocol fees 24h | $13.58M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $97.18 | coingecko.simple_price |
| 24h change | -5.40% | coingecko.simple_price |
| Market cap | $57.05B | coingecko.simple_price |
| 24h volume | $3.85B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.73B |
| TVL 1d / 7d / 30d | -1.82% / -3.29% / +18.86% |
| DEX volume 24h | $2.51B · 1d +40.24% · vs-7d-ago -9.90% |
| 7d DEX volume | $18.19B · +8.72% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $13.58M |
| Fees 1d / 7d | -3.25% / -13.90% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $445.38M | +41.08% |
| BisonFi | $315.80M | +56.74% |
| Raydium AMM | $255.45M | -1.19% |
| Meteora DLMM | $198.81M | +26.04% |
| Orca DEX | $188.09M | +79.68% |
| HumidiFi | $179.41M | +65.45% |
| fomo Wallet | $170.87M | +0.61% |
| Tessera V | $115.58M | +8.02% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.53B | -3.55% | -2.83% |
| Kamino Lend | Lending | $1.33B | -2.65% | -2.22% |
| Raydium AMM | Dexs | $1.10B | -4.79% | -3.90% |
| Jupiter Lend | Lending | $1.07B | -4.50% | -0.57% |
| Binance Staked SOL | Liquid Staking | $1.00B | -6.34% | -6.61% |
| Jito Liquid Staking | Liquid Staking | $997.65M | -6.46% | -5.65% |
| Jupiter Perpetual Exchange | Derivatives | $727.98M | -4.52% | -2.81% |
| Jupiter Staked SOL | Liquid Staking | $500.96M | -6.64% | -6.32% |
| Sentora Curator | Risk Curators | $383.16M | -1.31% | +3.36% |
| Marinade Native | Staking Pool | $369.07M | -6.61% | -8.22% |

## Stablecoins

Solana circulating pegged-USD: **$15.56B**
(1d +0.21% · 7d -1.84%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.74B | -6.37% |
| USDT · Tether | $2.48B | +0.00% |
| USDGO · USDGO | $1.38B | -0.43% |
| USD1 · World Liberty Financial USD | $1.32B | +1.15% |
| BUIDL · BlackRock USD | $993.10M | +0.05% |
| PYUSD · PayPal USD | $716.80M | +1.35% |
| USDG · Global Dollar | $612.25M | +2.11% |
| USDe · Ethena USDe | $527.56M | -0.92% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $107.92M (lower bound, not a census).
24h volume $81.58M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$551.73M** across 18 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $300.57M
- **Huma Finance V2** (RWA) — $193.33M
- **Plume Vaults** (RWA) — $28.34M
- **MatrixDock XAUM** (RWA) — $6.74M
- **Midas RWA** (RWA) — $5.64M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $2.74M
- **VNX** (RWA) — $2.74M

## Daily active addresses

883,837 (Allium, as of 2026-09-14). Provider range 382,293–883,837. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Latest release: https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1](https://x.com/anza_xyz/status/2099988354427408431) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 22:26:54 GMT
- [🚨 Mainnet-beta validators: we're looking for volunteers to bring 25% of stake to Agave v4.3 by EOD Friday 9/18 per routine upgrade procedure.](https://x.com/anza_xyz/status/2099988322542362645) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 22:26:46 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: 🚨JUST IN: @Solana co-founder @Toly says Transaction V1, which went live on Solana mainnet today, removed “the biggest blocker” to making the network quantum resistant.](https://x.com/SolanaFloor/status/2099866466615206209) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 14:22:33 GMT `mainnet`
- [RT by @anza_xyz: Transactions V1 is now live on Solana, increasing max transaction sizes from 1,232 to 4,096 bytes. 

Complex operations like ZK proofs, large multisigs, and confidential transfers that required multiple transactions now fit in one.

Full details from @anza_xyz: https://x.com/anza_xyz/status/2099665631415341253](https://x.com/solana/status/2099685865572233303) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 02:24:55 GMT
- [x.com/i/article/209959253939…](https://x.com/anza_xyz/status/2099668755764871609) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:16:55 GMT
- [Full migration checklist, SDK minimum versions, and sample code in Rust, TypeScript, Go, and Python: https://solana.com/upgrades/larger-transaction-sizes](https://x.com/anza_xyz/status/2099665857135989215) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:05:24 GMT `upgrade`
- [Indexers, paymasters, and anyone reading priority fees: read transactionConfig instead of ComputeBudget instructions. Compute budget instructions are ignored for configuration in V1, so scanning them may return zero or misleading values for V1 transactions.

RPC operators: run v4.2.2 or v4.3.0-beta.3 to serve the larger size.](https://x.com/anza_xyz/status/2099665797732024594) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:05:10 GMT
- [Sending transactions for V1 is opt-in. Legacy and V0 remain supported while existing apps continue working as is.

Reading V1 transactions is not opt-in. If you read blocks or transactions over RPC, pass maxSupportedTransactionVersion: 1 on getTransaction, getBlock, and blockSubscribe. Without it, one V1 transaction fails the entire call.](https://x.com/anza_xyz/status/2099665716446441476) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:04:51 GMT
- [RT by @solana_devs: Solana Explorer shows # of transactions by version in each block.](https://x.com/a_milz/status/2099925636974559451) — X/Nitter-style RSS @solana_devs (not Twitter API) · Tue, 15 Sep 2026 18:17:41 GMT
- [Watch the full video here: https://youtu.be/Dk8qazM1i-w?si=AYWTde--ek4oG5kN](https://x.com/solana_devs/status/2099894022688944506) — X/Nitter-style RSS @solana_devs (not Twitter API) · Tue, 15 Sep 2026 16:12:03 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [Latest release: https://github.com/anza-xyz/agave/releases/tag/v4.3.0-rc.1](https://x.com/anza_xyz/status/2099988354427408431) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 22:26:54 GMT
- [🚨 Mainnet-beta validators: we're looking for volunteers to bring 25% of stake to Agave v4.3 by EOD Friday 9/18 per routine upgrade procedure.](https://x.com/anza_xyz/status/2099988322542362645) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 22:26:46 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: 🚨JUST IN: @Solana co-founder @Toly says Transaction V1, which went live on Solana mainnet today, removed “the biggest blocker” to making the network quantum resistant.](https://x.com/SolanaFloor/status/2099866466615206209) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 14:22:33 GMT `mainnet`
- [RT by @anza_xyz: Transactions V1 is now live on Solana, increasing max transaction sizes from 1,232 to 4,096 bytes. 

Complex operations like ZK proofs, large multisigs, and confidential transfers that required multiple transactions now fit in one.

Full details from @anza_xyz: https://x.com/anza_xyz/status/2099665631415341253](https://x.com/solana/status/2099685865572233303) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 02:24:55 GMT
- [x.com/i/article/209959253939…](https://x.com/anza_xyz/status/2099668755764871609) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:16:55 GMT
- [Full migration checklist, SDK minimum versions, and sample code in Rust, TypeScript, Go, and Python: https://solana.com/upgrades/larger-transaction-sizes](https://x.com/anza_xyz/status/2099665857135989215) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:05:24 GMT `upgrade`
- [Indexers, paymasters, and anyone reading priority fees: read transactionConfig instead of ComputeBudget instructions. Compute budget instructions are ignored for configuration in V1, so scanning them may return zero or misleading values for V1 transactions.

RPC operators: run v4.2.2 or v4.3.0-beta.3 to serve the larger size.](https://x.com/anza_xyz/status/2099665797732024594) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:05:10 GMT
- [Sending transactions for V1 is opt-in. Legacy and V0 remain supported while existing apps continue working as is.

Reading V1 transactions is not opt-in. If you read blocks or transactions over RPC, pass maxSupportedTransactionVersion: 1 on getTransaction, getBlock, and blockSubscribe. Without it, one V1 transaction fails the entire call.](https://x.com/anza_xyz/status/2099665716446441476) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 15 Sep 2026 01:04:51 GMT
- [RT by @solana_devs: Solana Explorer shows # of transactions by version in each block.](https://x.com/a_milz/status/2099925636974559451) — X/Nitter-style RSS @solana_devs (not Twitter API) · Tue, 15 Sep 2026 18:17:41 GMT
- [Watch the full video here: https://youtu.be/Dk8qazM1i-w?si=AYWTde--ek4oG5kN](https://x.com/solana_devs/status/2099894022688944506) — X/Nitter-style RSS @solana_devs (not Twitter API) · Tue, 15 Sep 2026 16:12:03 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-15 (2026-09-15 16:35:50 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **Median tx fee** — no getBlock samples
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 191ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 155ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 125ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 255ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 125ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6733ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 300ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 103ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 166ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 685ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 76ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 71ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 96ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 206ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 118ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 121ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 141ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 541ms https://solana.com/data
- `solana.com.databricks` [ok] 200 163ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 584ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 177ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 241ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 254ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 260ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 405ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 171ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 168ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 170ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 408ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 131ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1217ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1208ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 365ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 141ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 260ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 124ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 153ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 246ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 148ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 136ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 377ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 330ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 346ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 316ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 329ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 227ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 339ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 165ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 151ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 350ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 374ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 190ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 479ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 275ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 379ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 288ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 307ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 221ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 326ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 267ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 274ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 207ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 222ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 151ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1506ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1560ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1620ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1874ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1327ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1386ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1250ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1246ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.QQQx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.SPYx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.COINx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.FLNCx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.INDIx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.XRXx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.WRLDx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.circ.QQQx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.WGSx` [ok] 200 917ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.circ.COINx` [ok] 200 703ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.METCx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.PCTx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.mult.COINx` [ok] 200 736ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.WRLDx` [ok] 200 1246ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 1317ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 1342ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 1396ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.QUBTx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.mult.XRXx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 1317ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 1140ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.price.BETRx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.DRSx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.mult.METCx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.AIx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.BETRx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.PCTx` [ok] 200 1426ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.DRSx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.price.SCIx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.mult.BETRx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 762ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.SCIx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.DRSx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.SAILx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.mult.PCTx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.price.MPx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.mult.SCIx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.GSATx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.price.BSYx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.price.DVAx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.circ.SAILx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 1174ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.GSATx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.circ.MPx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.circ.DVAx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.circ.BSYx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.price.DCIx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.mult.DVAx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.mult.GSATx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.MPx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 1830ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.mult.BSYx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.price.BXPx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.price.DYx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.circ.RYANx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.circ.BXPx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.SAILx` [ok] 200 835ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.circ.DYx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.mult.BXPx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.WMSx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.price.AMx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.price.GDDYx` [ok] 200 678ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.circ.FRHCx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.mult.RYANx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.price.FDSx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.circ.WMSx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.circ.GDDYx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.circ.AMx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.price.ALSNx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.mult.WMSx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.circ.FDSx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 392ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.mult.AMx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.price.SMTCx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.mult.GDDYx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.price.SFx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.mult.FDSx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.price.EGPx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.circ.SMTCx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.circ.ALSNx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.price.BPOPx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.mult.SMTCx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.circ.EGPx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.price.AXSMx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.circ.BPOPx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.circ.DCIx` [ok] 200 1679ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.circ.AXSMx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.mult.BPOPx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.mult.EGPx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.price.AEISx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.mult.DCIx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.mult.AXSMx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.price.DPZx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.circ.SFx` [ok] 200 698ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.circ.AEISx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.price.PAGx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.mult.SFx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.price.HRLx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.circ.DPZx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.price.SEICx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.circ.PAGx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.mult.AEISx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.circ.HRLx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.price.KTOSx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.mult.DPZx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.circ.SEICx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.price.EHCx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.mult.PAGx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.price.GFLx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.price.HIIx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.mult.HRLx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.TTMIx` [ok] 200 1376ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.circ.GFLx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.SEICx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.circ.EHCx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.price.MGMx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.price.ARx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.circ.TTMIx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.circ.KTOSx` [ok] 200 563ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.mult.GFLx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.circ.MGMx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.price.DOCUx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.circ.ARx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.mult.TTMIx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.mult.EHCx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.KTOSx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.price.HALOx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.price.WTRGx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.mult.MGMx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.price.HUBSx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.mult.ARx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.circ.HALOx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.price.AFGx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.circ.WTRGx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.price.AMKRx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.mult.HALOx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.circ.AFGx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.price.GMEDx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.circ.AMKRx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.mult.WTRGx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.mult.AFGx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.mult.AMKRx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 1201ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.price.IESCx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.price.JKHYx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.HIIx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.price.OCx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.price.CRx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.circ.JKHYx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.mult.GMEDx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.price.BMRNx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.circ.DOCUx` [ok] 200 1150ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.circ.OCx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.mult.JKHYx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.circ.BMRNx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.mult.DOCUx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.price.JEFx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.price.AMHx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.JEFx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.mult.BMRNx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.price.FIVEx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.circ.HUBSx` [ok] 200 1247ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.price.ITx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.circ.AMHx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.mult.HUBSx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.circ.FIVEx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.mult.JEFx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.mult.OCx` [ok] 200 723ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.price.MDGLx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.circ.ITx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.price.UHALx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.circ.MDGLx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.mult.FIVEx` [ok] 200 550ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.circ.UHALx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.mult.MDGLx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.circ.CRx` [ok] 200 1420ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.price.VNOMx` [ok] 200 592ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.mult.ITx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.UHALx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.price.AHRx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.price.CORTx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.circ.VNOMx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.circ.IESCx` [ok] 200 1936ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.circ.CORTx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.circ.AHRx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 1167ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.mult.VNOMx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.STRLx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.price.IVZx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.mult.CORTx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.NWSAx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.mult.AHRx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.AURx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.circ.STRLx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.mult.IESCx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.Hx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.circ.NWSAx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.mult.CRx` [ok] 200 834ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.mult.STRLx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.circ.Hx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.price.GWREx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.price.NWSx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.price.MANHx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.circ.GWREx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.mult.NWSAx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.mult.Hx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.circ.MANHx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.price.CACIx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.mult.GWREx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.price.BAXx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.mult.MANHx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.price.ARWRx` [ok] 200 793ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.circ.BAXx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.circ.CACIx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.BAXx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.CACIx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.circ.ARWRx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.circ.IVZx` [ok] 200 1588ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.circ.AURx` [ok] 200 1665ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.mult.IVZx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 1405ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.AURx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 638ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 257ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INDIx` [ok] 200 114ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 120ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 128ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.XRXx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.BETRx` [ok] 200 132ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.FLNCx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.WGSx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.AIx` [ok] 200 109ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jito.tip_floor` [ok] 200 170ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 457ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 131ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 123ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 125ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 128ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 151ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 184ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
