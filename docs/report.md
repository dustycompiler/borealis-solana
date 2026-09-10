# Borealis — Solana ecosystem report

**Generated** 2026-09-10T06:54:52Z · 2026-09-09 23:54:52 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-10T06:54:43Z · **RPC health** `ok`
**Health score** 97 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h -2.40%; DEX 24h $2.56B · 1d -6% · vs-7d-ago +12%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +38.15%. (threshold: `|7d %| >= 20`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -2.40%, DeFiLlama TVL 1d -1.43%, DEX 1d -5.68%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 445,820,583 |
| Block height | 423,863,977 |
| Block time | 2026-09-10T06:54:43Z |
| Epoch | 1,031 (99.21% · slot 428,586/432,000) |
| Mean TPS (last ~3,600s) | 3,576.9 |
| Mean non-vote TPS | 1,443.1 |
| Median TPS (same window) | 3,557.6 |
| Mean slot time | 315.0 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 546,960,933,509 |
| Circulating supply | 586,249,785 SOL |
| Total supply | 633,736,012 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 438,590,143 SOL |
| Delinquent stake | 63,361.83 SOL (0.014%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.25% / 35.53% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 3.98% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.35M SOL | 3.73% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.53M SOL | 2.86% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.39M SOL | 2.60% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.18% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.03M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.32M SOL | 1.67% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.86M SOL | 1.56% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.60M SOL | 1.51% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.97M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `mrgn4atx…` · 20.28K SOL · commission 0% · lag 112044 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 84800 slots
- `inWVrrYJ…` · 9.89K SOL · commission 0% · lag 121486 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 2471860 slots
- `prt1st4R…` · 5.87K SOL · commission 5% · lag 2333641 slots
- `xLabscif…` · 4.17K SOL · commission 5% · lag 2032210 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 1854661 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 25421 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 10971 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 445820583 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 61771713 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 981572 slots

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
| **In-protocol fees 24h** | **$768.89K** (7,465.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-08 |
| **Solana REV** | **8,789.1 SOL** / **$905.27K** | MEASURED UTC calendar day 2026-09-08: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-08 · UTC day 2026-09-08 · SOL-USD date 2026-09-08 |
| Jito tip-floor run-rate (NOT REV) | $36.82K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 36816 USD; at p95 floor → 547945 USD. |
| Protocol fees 24h | $15.57M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9985 |
| p90 / p99 | 0.000010 / 0.000093 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $102.01 | coingecko.simple_price |
| 24h change | -2.40% | coingecko.simple_price |
| Market cap | $59.80B | coingecko.simple_price |
| 24h volume | $3.23B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.87B |
| TVL 1d / 7d / 30d | -1.43% / +2.73% / +20.99% |
| DEX volume 24h | $2.56B · 1d -5.68% · vs-7d-ago +11.68% |
| 7d DEX volume | $16.13B · -4.32% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $15.57M |
| Fees 1d / 7d | -5.98% / +38.15% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| Raydium AMM | $406.12M | +15.82% |
| PumpSwap | $340.96M | -53.74% |
| Meteora DLMM | $322.25M | +35.54% |
| BisonFi | $249.32M | 0.00% |
| Orca DEX | $177.14M | +15.31% |
| Tessera V | $156.31M | 0.00% |
| HumidiFi | $153.40M | 0.00% |
| Manifest Trade | $149.06M | +19.53% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.56B | -1.25% | +2.02% |
| Kamino Lend | Lending | $1.34B | -1.98% | +7.02% |
| Raydium AMM | Dexs | $1.13B | -0.85% | +4.69% |
| Jupiter Lend | Lending | $1.09B | -1.17% | +1.21% |
| Binance Staked SOL | Liquid Staking | $1.06B | -2.09% | +2.02% |
| Jito Liquid Staking | Liquid Staking | $1.05B | -2.23% | +3.53% |
| BlackRock BUIDL | RWA | $992.17M | -0.57% | +0.68% |
| Jupiter Perpetual Exchange | Derivatives | $748.51M | -0.10% | +0.32% |
| Jupiter Staked SOL | Liquid Staking | $528.03M | -2.17% | +1.71% |
| xStocks | RWA | $438.24M | -1.12% | +0.60% |

## Stablecoins

Solana circulating pegged-USD: **$16.22B**
(1d -0.33% · 7d +2.95%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.13B | -0.68% |
| USDT · Tether | $2.76B | -0.00% |
| USDGO · USDGO | $1.37B | +0.55% |
| USD1 · World Liberty Financial USD | $1.28B | -0.00% |
| BUIDL · BlackRock USD | $992.17M | +0.47% |
| PYUSD · PayPal USD | $756.68M | +0.54% |
| USDG · Global Dollar | $599.44M | +1.51% |
| USDe · Ethena USDe | $535.61M | -0.16% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 78 of 737 Solana-deployed listed symbols (multiplier ok 80/80; 737 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 737 · Solana deployments 737 · priced 78 · priced-subset mcap $293.47M (lower bound, not a census).
24h volume $184.05M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $438.24M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 78 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 737 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 737 unique underlyings among 737 Solana rows; not every tokenized equity on Solana). 737 of 737 listed xStocks have a Solana deployment (737 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.35B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.17M
- **xStocks** (RWA) — $438.24M
- **OnRe** (RWA) — $307.20M
- **Ondo Yield Assets** (RWA) — $180.12M
- **Huma Finance V2** (RWA) — $167.12M
- **Hastra** (RWA) — $149.39M
- **Ondo Global Markets** (RWA) — $25.95M
- **Plume Vaults** (RWA) — $25.76M

## Daily active addresses

889,097 (Allium, as of 2026-09-08). Provider range 468,434–891,389. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [the winningest products will always emerge from the ultra-competititive bloodsport arena we call solana](https://x.com/solana/status/2097920505550672034) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 05:30:00 GMT
- [luma.com/solana-summit-korea…](https://x.com/solana/status/2097907059622871165) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 04:36:34 GMT
- [🇰🇷 솔라나 서밋 코리아가 20일 앞으로 다가왔습니다.

See you in Seoul](https://x.com/solana/status/2097907054019239970) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 04:36:33 GMT
- [maximum potential](https://x.com/solana/status/2097875445597323530) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 02:30:57 GMT
- [RT by @solana: Introducing Custom Pairs

Launch Pumpfun tokens paired with tokenized stocks, majors & more on Solana.

Launch with more variety, deeper liquidity & lower fees than anywhere else.](https://x.com/Pumpfun/status/2097785975434846285) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:35:26 GMT
- [All 20 are available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @Pumpfun, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2097787932232872294) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:43:12 GMT
- [$BA, $BABA, $BULL, $COST, $DELL, $DJT, $HIMS, $IBM, $JNJ, $LMT, $LULU, $NET, $PFE, $QUBT, $RBLX, $RDDT, $RIVN, $SHOP, $SNAP, $UPS

Verify the addresses on @tokens:
https://tokens.xyz/stocks?category=stocks](https://x.com/solana/status/2097787930576089185) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:43:12 GMT
- [Pinned: BREAKING: 20 more stocks live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2097787928558608863) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:43:11 GMT
- [Transaction V1 activation on mainnet-beta is moving to the start of epoch 1035, expected Sept 15 at ~1:20 AM UTC.

Teams across the ecosystem told us they needed more time to test and integrate V1 support. We listened.

How to get ready:

- V1 is live on devnet, test your integration now.

-  Compute budgets in V1 are set using a new transaction config. Compute budget instructions still work on legacy and V0 but no-op in V1.

- App developers: even if you don't plan to send V1 transactions, some changes may impact your app. Review the guide below.

Details: https://solana.com/upgrades/larger-transaction-sizes](https://x.com/anza_xyz/status/2097769035144561079) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 09 Sep 2026 19:28:07 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: What is cool about transaction v1?
1) @multisig smart wallet being able to do everything onchain with big pqc based signatures 
2) two zkp root state transitions in one atomic tx, aka “based rollups”
3) routing to a bajilion markets at the same time](https://x.com/toly/status/2097345987937497491) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:27:04 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [the winningest products will always emerge from the ultra-competititive bloodsport arena we call solana](https://x.com/solana/status/2097920505550672034) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 05:30:00 GMT
- [luma.com/solana-summit-korea…](https://x.com/solana/status/2097907059622871165) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 04:36:34 GMT
- [🇰🇷 솔라나 서밋 코리아가 20일 앞으로 다가왔습니다.

See you in Seoul](https://x.com/solana/status/2097907054019239970) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 04:36:33 GMT
- [maximum potential](https://x.com/solana/status/2097875445597323530) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 10 Sep 2026 02:30:57 GMT
- [RT by @solana: Introducing Custom Pairs

Launch Pumpfun tokens paired with tokenized stocks, majors & more on Solana.

Launch with more variety, deeper liquidity & lower fees than anywhere else.](https://x.com/Pumpfun/status/2097785975434846285) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:35:26 GMT
- [All 20 are available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @Pumpfun, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2097787932232872294) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:43:12 GMT
- [$BA, $BABA, $BULL, $COST, $DELL, $DJT, $HIMS, $IBM, $JNJ, $LMT, $LULU, $NET, $PFE, $QUBT, $RBLX, $RDDT, $RIVN, $SHOP, $SNAP, $UPS

Verify the addresses on @tokens:
https://tokens.xyz/stocks?category=stocks](https://x.com/solana/status/2097787930576089185) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:43:12 GMT
- [Pinned: BREAKING: 20 more stocks live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2097787928558608863) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 20:43:11 GMT
- [Transaction V1 activation on mainnet-beta is moving to the start of epoch 1035, expected Sept 15 at ~1:20 AM UTC.

Teams across the ecosystem told us they needed more time to test and integrate V1 support. We listened.

How to get ready:

- V1 is live on devnet, test your integration now.

-  Compute budgets in V1 are set using a new transaction config. Compute budget instructions still work on legacy and V0 but no-op in V1.

- App developers: even if you don't plan to send V1 transactions, some changes may impact your app. Review the guide below.

Details: https://solana.com/upgrades/larger-transaction-sizes](https://x.com/anza_xyz/status/2097769035144561079) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 09 Sep 2026 19:28:07 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: What is cool about transaction v1?
1) @multisig smart wallet being able to do everything onchain with big pqc based signatures 
2) two zkp root state transitions in one atomic tx, aka “based rollups”
3) routing to a bajilion markets at the same time](https://x.com/toly/status/2097345987937497491) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:27:04 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-10 (2026-09-09 23:54:52 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 737 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 712ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 636ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 654ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 620ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 666ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7410ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1284ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 220ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 137ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 124ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 65ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 60ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1288ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 140ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 137ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 585ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 149ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 406ms https://solana.com/data
- `solana.com.databricks` [ok] 200 134ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 508ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 158ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 1075ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 109ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 405ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 614ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 251ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 252ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 523ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 803ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 670ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1131ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1729ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 210ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 638ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 673ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2436ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2504ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2591ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2670ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2307ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2542ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2509ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2291ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1564ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2168ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2372ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2489ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2212ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2245ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2175ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1726ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1300ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1349ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1621ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1444ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2565ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 3159ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.GOOGLx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.NVDAx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.NVDAx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.AAPLx` [ok] 200 808ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.AMZNx` [ok] 200 927ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.AAPLx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.MSFTx` [ok] 200 1223ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.AMZNx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.METAx` [ok] 200 1317ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.mult.AAPLx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.TSLAx` [ok] 200 1463ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.COINx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.TSLAx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.SPYx` [ok] 200 1853ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.QQQx` [ok] 200 694ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.MSFTx` [ok] 200 650ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.FLNCx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.circ.METAx` [ok] 200 616ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.price.XRXx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.circ.SPYx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.FLNCx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.INDIx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.mult.FLNCx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.XRXx` [ok] 200 618ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.price.PCTx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.WRLDx` [ok] 200 554ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.mult.QQQx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.INDIx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.PCTx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.QUBTx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.mult.PCTx` [ok] 200 570ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.price.METCx` [ok] 200 1094ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.QUBTx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 602ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.price.WGSx` [ok] 200 1587ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.circ.METCx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 2054ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 1053ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.mult.WRLDx` [ok] 200 1049ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.MVLLx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.AIx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.BETRx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 545ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 574ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.BETRx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.DRAMx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.MUUx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.circ.AIx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.circ.DRAMx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 694ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.mult.MUUx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.price.KORUx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.METCx` [ok] 200 1259ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.MVLLx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.mult.AXTIx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.DJTx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.price.INTWx` [ok] 200 791ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.circ.INTWx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 877ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.price.SNXXx` [ok] 200 1724ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.mult.INTWx` [ok] 200 596ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.SOXSx` [ok] 200 1681ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.SUOPTx` [ok] 200 1114ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.SNXXx` [ok] 200 1288ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.SNXXx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.SHEINx` [ok] 200 3215ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 1650ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.MMGx` [ok] 200 1531ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 5462ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.SHEINx` [ok] 200 1088ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.SHEINx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.SUOPTx` [ok] 200 2067ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 528ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.KUNLx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 799ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 854ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 595ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 6057ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.KORUx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 545ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 667ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.HRZRBx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.KUNLx` [ok] 200 1319ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.CMERPx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 683ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 1302ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.CRESBx` [ok] 200 1323ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 1346ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.WXXDCx` [ok] 200 643ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 1372ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.CRESBx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.WXXDCx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.MIXUx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 2272ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 1641ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.CSPCx` [ok] 200 1792ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.SITCx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 899ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 677ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.SITCx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 836ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.MIXUx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 1403ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.SNDSCx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.CMENDx` [ok] 200 1851ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 597ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.CRESMx` [ok] 200 1810ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.mult.CMENDx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.circ.CRESPx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 400ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.JDHLTx` [ok] 200 1722ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 769ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 1726ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 1560ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 1159ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.CTPCAx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.SNDSCx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.NWGx` [FAIL]  12029ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CTPCAx` [ok] 200 565ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.NWGx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 536ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.NWGx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 1772ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.SINOx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 2038ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.SINOTx` [ok] 200 2317ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 475ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 1077ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 679ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 3300ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.GENTEx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 743ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 392ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 3656ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.WUXIBx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.SWPRPx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 1530ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 944ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.CKINFx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 1257ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 751ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.WHGROx` [ok] 200 5240ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 1163ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 1140ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.CLONPx` [ok] 200 929ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 1306ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 985ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 4486ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 403ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 1315ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 2007ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.KUAIx` [ok] 200 1058ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 6308ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 1492ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 124ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 194ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INTWx` [ok] 200 97ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.MVLLx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SHEINx` [ok] 200 93ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.KORUx` [ok] 200 93ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.MUUx` [ok] 200 94ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.SNXXx` [ok] 200 93ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jup.tokens.search.DRAMx` [ok] 200 93ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.SOXSx` [ok] 200 88ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jito.tip_floor` [ok] 200 178ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 391ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 181ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 638ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 608ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 601ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 625ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 420ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
