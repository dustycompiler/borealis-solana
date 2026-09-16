# Borealis — Solana ecosystem report

**Generated** 2026-09-16T06:31:02Z · 2026-09-15 23:31:02 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-16T06:30:50Z · **RPC health** `ok`
**Health score** 96 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h -3.90%; DEX 24h $2.50B · 1d -0% · vs-7d-ago -10%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -3.90%, DeFiLlama TVL 1d -3.21%, DEX 1d -0.41%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 447,454,757 |
| Block height | 425,496,264 |
| Block time | 2026-09-16T06:30:50Z |
| Epoch | 1,035 (77.49% · slot 334,757/432,000) |
| Mean TPS (last ~3,600s) | 3,502.9 |
| Mean non-vote TPS | 1,370.1 |
| Median TPS (same window) | 3,487.4 |
| Mean slot time | 316.4 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 548,967,912,018 |
| Circulating supply | 587,064,791 SOL |
| Total supply | 634,110,850 SOL |
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
| Activated stake | 439,088,345 SOL |
| Delinquent stake | 160,293.90 SOL (0.036%) |
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

- `FGiEdzde…` · 128.30K SOL · commission 5% · lag 894319 slots
- `mrgn4atx…` · 19.36K SOL · commission 0% · lag 198717 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 579956 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 410472 slots
- `4GEEKSwu…` · 196.81 SOL · commission 5% · lag 1645145 slots
- `EWARp8Sy…` · 99.64 SOL · commission 5% · lag 458761 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 1755660 slots
- `Je6ckvDi…` · 2.50 SOL · commission 0% · lag 14616 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 63405887 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 1198730 slots
- `4kdjgZKJ…` · 1.05 SOL · commission 100% · lag 447454757 slots

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
| **In-protocol fees 24h** | **$639.75K** (6,332.7 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-14 |
| **Solana REV** | **7,374.9 SOL** / **$745.04K** | MEASURED UTC calendar day 2026-09-14: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-14 · UTC day 2026-09-14 · SOL-USD date 2026-09-14 |
| Jito tip-floor run-rate (NOT REV) | $67.51K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 67509 USD; at p95 floor → 577629 USD. |
| Protocol fees 24h | $14.22M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $97.09 | coingecko.simple_price |
| 24h change | -3.90% | coingecko.simple_price |
| Market cap | $57.00B | coingecko.simple_price |
| 24h volume | $3.94B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.73B |
| TVL 1d / 7d / 30d | -3.21% / -3.79% / +19.63% |
| DEX volume 24h | $2.50B · 1d -0.41% · vs-7d-ago -10.15% |
| 7d DEX volume | $16.84B · -2.57% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.22M |
| Fees 1d / 7d | +4.69% / -14.88% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $519.33M | +16.60% |
| BisonFi | $315.80M | 0.00% |
| Raydium AMM | $226.00M | -30.35% |
| fomo Wallet | $190.81M | +11.48% |
| Orca DEX | $184.33M | +6.96% |
| HumidiFi | $179.41M | 0.00% |
| Meteora DLMM | $168.53M | -15.23% |
| Manifest Trade | $117.68M | -9.95% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.54B | -1.74% | -2.30% |
| Kamino Lend | Lending | $1.33B | -1.57% | -2.31% |
| Raydium AMM | Dexs | $1.09B | -5.36% | -3.97% |
| Jupiter Lend | Lending | $1.08B | -1.57% | -1.79% |
| Binance Staked SOL | Liquid Staking | $1.00B | -4.24% | -7.25% |
| Jito Liquid Staking | Liquid Staking | $1.00B | -3.83% | -6.36% |
| Jupiter Perpetual Exchange | Derivatives | $729.82M | -2.55% | -2.60% |
| Jupiter Staked SOL | Liquid Staking | $502.53M | -4.13% | -6.90% |
| Sentora Curator | Risk Curators | $382.97M | -1.21% | +3.41% |
| Marinade Native | Staking Pool | $370.24M | -4.13% | -8.78% |

## Stablecoins

Solana circulating pegged-USD: **$15.50B**
(1d -2.61% · 7d -4.03%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.83B | -5.15% |
| USDT · Tether | $2.34B | -5.63% |
| USDGO · USDGO | $1.38B | -1.08% |
| USD1 · World Liberty Financial USD | $1.32B | -0.00% |
| BUIDL · BlackRock USD | $993.10M | +0.02% |
| PYUSD · PayPal USD | $715.61M | +1.91% |
| USDG · Global Dollar | $609.47M | -0.74% |
| USDe · Ethena USDe | $525.54M | -0.56% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $108.12M (lower bound, not a census).
24h volume $76.82M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$551.83M** across 18 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $300.67M
- **Huma Finance V2** (RWA) — $193.13M
- **Plume Vaults** (RWA) — $28.34M
- **MatrixDock XAUM** (RWA) — $6.79M
- **Midas RWA** (RWA) — $5.64M
- **Invesco USTB** (RWA) — $3.91M
- **VNX** (RWA) — $2.76M
- **Mansory** (RWA) — $2.74M

## Daily active addresses

815,550 (Allium, as of 2026-09-15). Provider range 413,903–903,402. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [250ms slots activation now pending on mainnet-beta.

400 → 350 → 300 → 250ms

Reminder, SIMD-0525 features take effect one epoch after they activate thus will go live at the epoch 1037 boundary ~05:01 UTC, Friday Sept 18.

- epoch 1035: pending activation
- epoch 1036: feature active
- epoch 1037: 250ms slots live

1 more step to 200ms.](https://x.com/anza_xyz/status/2100088118942781446) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 16 Sep 2026 05:03:19 GMT `upgrade` `mainnet`
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
- [Hoping developers on Solana have an awesome day!

New Solana SDK below](https://x.com/solana_devs/status/2100106226155811279) — X/Nitter-style RSS @solana_devs (not Twitter API) · Wed, 16 Sep 2026 06:15:17 GMT
- [RT by @solana_devs: 🚨 Mainnet-beta validators: we're looking for volunteers to bring 25% of stake to Agave v4.3 by EOD Friday 9/18 per routine upgrade procedure.](https://x.com/anza_xyz/status/2099988322542362645) — X/Nitter-style RSS @solana_devs (not Twitter API) · Tue, 15 Sep 2026 22:26:46 GMT `upgrade` `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [250ms slots activation now pending on mainnet-beta.

400 → 350 → 300 → 250ms

Reminder, SIMD-0525 features take effect one epoch after they activate thus will go live at the epoch 1037 boundary ~05:01 UTC, Friday Sept 18.

- epoch 1035: pending activation
- epoch 1036: feature active
- epoch 1037: 250ms slots live

1 more step to 200ms.](https://x.com/anza_xyz/status/2100088118942781446) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 16 Sep 2026 05:03:19 GMT `upgrade` `mainnet`
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
- [Hoping developers on Solana have an awesome day!

New Solana SDK below](https://x.com/solana_devs/status/2100106226155811279) — X/Nitter-style RSS @solana_devs (not Twitter API) · Wed, 16 Sep 2026 06:15:17 GMT
- [RT by @solana_devs: 🚨 Mainnet-beta validators: we're looking for volunteers to bring 25% of stake to Agave v4.3 by EOD Friday 9/18 per routine upgrade procedure.](https://x.com/anza_xyz/status/2099988322542362645) — X/Nitter-style RSS @solana_devs (not Twitter API) · Tue, 15 Sep 2026 22:26:46 GMT `upgrade` `mainnet`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-16 (2026-09-15 23:31:02 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **Median tx fee** — no getBlock samples
- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 212ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 226ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 192ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 198ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 176ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6879ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 382ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 132ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 81ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 5455ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 56ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 74ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 64ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 152ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 258ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 111ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 126ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 417ms https://solana.com/data
- `solana.com.databricks` [ok] 200 108ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 490ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 167ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 104ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 106ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 357ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 385ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 206ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 207ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 205ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 2433ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 149ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 3561ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 3276ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 269ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 274ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 199ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 174ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 234ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 173ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 194ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 122ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 263ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 252ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 275ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 383ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 282ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 235ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 271ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 191ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 174ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 208ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 263ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 212ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 238ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 202ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 315ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 228ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 215ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 187ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 216ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 197ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 223ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 193ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 223ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 302ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1828ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1575ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1627ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 4051ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1636ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1578ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1833ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1551ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.COINx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.SPYx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.XRXx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.INDIx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WRLDx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.FLNCx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.circ.SPYx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.WRLDx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 765ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.INDIx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.METCx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.PCTx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.QQQx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.QUBTx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.WGSx` [ok] 200 1103ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.circ.METCx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.BETRx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.mult.WRLDx` [ok] 200 561ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 540ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.BETRx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.WYFIx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.DRSx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.price.AIx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.BETRx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.SCIx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.mult.WYFIx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 828ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 727ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.AIx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.DRSx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.price.BSYx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.price.SAILx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.price.MPx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.mult.AIx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.DRSx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.circ.BSYx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.circ.MPx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.circ.SAILx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.price.DCIx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.price.DVAx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.circ.SCIx` [ok] 200 656ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.price.GDDYx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.mult.MPx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.mult.BSYx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.price.GSATx` [ok] 200 815ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.circ.DVAx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.mult.SAILx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.mult.SCIx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.mult.DVAx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.price.BXPx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.price.FRHCx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.mult.DCIx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.price.DYx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.circ.RYANx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.price.WMSx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.circ.FRHCx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.circ.GDDYx` [ok] 200 738ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.mult.RYANx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.price.AMx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.DYx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.mult.GDDYx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.circ.AMx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.FRHCx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.circ.WMSx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.circ.BXPx` [ok] 200 746ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.price.FDSx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.mult.AMx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.price.ALSNx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.circ.GSATx` [ok] 200 1122ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.price.SMTCx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.mult.WMSx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.SFx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.mult.BXPx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.circ.ALSNx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.price.AXSMx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.circ.SFx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.price.EGPx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.mult.GSATx` [ok] 200 622ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.FDSx` [ok] 200 729ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.price.BPOPx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.mult.ALSNx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.circ.EGPx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.circ.SMTCx` [ok] 200 685ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.price.TTMIx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.circ.AXSMx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.price.AEISx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.mult.SMTCx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.circ.TTMIx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.circ.BPOPx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.mult.SFx` [ok] 200 711ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.price.DPZx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.mult.TTMIx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.HRLx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.mult.AXSMx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.circ.DPZx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.price.KTOSx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.mult.BPOPx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.circ.AEISx` [ok] 200 667ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.price.SEICx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.price.PAGx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.mult.DPZx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.circ.HRLx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.circ.KTOSx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.mult.EGPx` [ok] 200 1106ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.SEICx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.mult.AEISx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.price.EHCx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.circ.PAGx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.price.HIIx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.mult.KTOSx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.mult.HRLx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.GFLx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.mult.SEICx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.circ.GFLx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.price.MGMx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.mult.PAGx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.circ.EHCx` [ok] 200 431ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.price.HALOx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.mult.HIIx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.price.ARx` [ok] 200 645ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.circ.MGMx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.price.WTRGx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.DOCUx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.mult.GFLx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.mult.EHCx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.MGMx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.circ.WTRGx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.price.HUBSx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.circ.HALOx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.circ.ARx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.circ.DOCUx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.price.AFGx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.mult.DOCUx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.circ.AFGx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.mult.HALOx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.price.AMKRx` [ok] 200 632ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.price.IESCx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.price.JKHYx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.AFGx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.circ.HUBSx` [ok] 200 668ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.mult.WTRGx` [ok] 200 697ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.circ.JKHYx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.mult.HUBSx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.price.GMEDx` [ok] 200 926ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.price.CRx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.price.OCx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.circ.AMKRx` [ok] 200 508ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.price.BMRNx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.circ.CRx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.circ.IESCx` [ok] 200 556ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.circ.OCx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.circ.BMRNx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.mult.ARx` [ok] 200 1282ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.mult.AMKRx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.mult.CRx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.price.JEFx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.mult.JKHYx` [ok] 200 808ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.mult.OCx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.mult.BMRNx` [ok] 200 499ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.price.AMHx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.price.ITx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.mult.IESCx` [ok] 200 828ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.MDGLx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.circ.AMHx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.circ.JEFx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.circ.ITx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.mult.GMEDx` [ok] 200 1068ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.price.VNOMx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.circ.MDGLx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.mult.JEFx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.price.UHALx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.mult.ITx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.circ.VNOMx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.price.AHRx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.price.FIVEx` [ok] 200 965ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.price.IVZx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.circ.UHALx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.mult.MDGLx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.mult.VNOMx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.circ.AHRx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.price.CORTx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.circ.FIVEx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.circ.IVZx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.mult.UHALx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.mult.AHRx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.mult.FIVEx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.price.AURx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.price.Hx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.price.ARWRx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.price.GWREx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.price.NWSAx` [ok] 200 662ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.circ.Hx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.circ.ARWRx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.circ.CORTx` [ok] 200 800ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.circ.NWSAx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.circ.GWREx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.mult.AURx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.price.STRLx` [ok] 200 1243ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.mult.ARWRx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.mult.CORTx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.mult.IVZx` [ok] 200 1017ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.price.NWSx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.price.MANHx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.price.CACIx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.price.BAXx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.mult.NWSAx` [ok] 200 595ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 657ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.circ.STRLx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.circ.CACIx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.circ.MANHx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.circ.BAXx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.Hx` [ok] 200 1033ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.mult.MANHx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.CACIx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.STRLx` [ok] 200 925ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 64ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 310ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.QUBTx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.INDIx` [ok] 200 95ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.WRLDx` [ok] 200 93ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.BETRx` [ok] 200 102ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.FLNCx` [ok] 200 91ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.XRXx` [ok] 200 95ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.WGSx` [ok] 200 92ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.AIx` [ok] 200 97ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jito.tip_floor` [ok] 200 81ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 311ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 121ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 183ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 175ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 179ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 175ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 313ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
