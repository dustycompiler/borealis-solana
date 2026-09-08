# Borealis — Solana ecosystem report

**Generated** 2026-09-08T21:49:56Z · 2026-09-08 14:49:56 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-08T21:49:45Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h -0.81%; DEX 24h $2.72B · 1d -6% · vs-7d-ago +9%; slot 319 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -0.81%, DeFiLlama TVL 1d -1.21%, DEX 1d -6.33%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 445,444,515 |
| Block height | 423,488,426 |
| Block time | 2026-09-08T21:49:45Z |
| Epoch | 1,031 (12.16% · slot 52,516/432,000) |
| Mean TPS (last ~3,600s) | 4,225.8 |
| Mean non-vote TPS | 2,118.6 |
| Median TPS (same window) | 4,246.2 |
| Mean slot time | 318.8 ms |
| Median slot time | 319.1 ms |
| Transaction count (cluster) | 546,476,220,657 |
| Circulating supply | 586,251,063 SOL |
| Total supply | 633,737,289 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 11 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 438,600,954 SOL |
| Delinquent stake | 52,551.00 SOL (0.012%) |
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

- `mrgn4atx…` · 20.28K SOL · commission 0% · lag 89808 slots
- `inWVrrYJ…` · 9.89K SOL · commission 0% · lag 93486 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 2095792 slots
- `prt1st4R…` · 5.87K SOL · commission 5% · lag 1957573 slots
- `xLabscif…` · 4.17K SOL · commission 5% · lag 1656142 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 1478593 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 905324 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 117632 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 445444515 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 61395645 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 605504 slots

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
| **In-protocol fees 24h** | **$763.42K** (7,228.6 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-07 |
| **Solana REV** | **8,421.8 SOL** / **$889.43K** | MEASURED UTC calendar day 2026-09-07: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-07 · UTC day 2026-09-07 · SOL-USD date 2026-09-07 |
| Jito tip-floor run-rate (NOT REV) | $62.67K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 62673 USD; at p95 floor → 2290251 USD. |
| Protocol fees 24h | $15.65M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9942 |
| p90 / p99 | 0.000014 / 0.000105 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.05 | coingecko.simple_price |
| 24h change | -0.81% | coingecko.simple_price |
| Market cap | $60.41B | coingecko.simple_price |
| 24h volume | $3.08B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.92B |
| TVL 1d / 7d / 30d | -1.21% / -1.07% / +23.13% |
| DEX volume 24h | $2.72B · 1d -6.33% · vs-7d-ago +8.76% |
| 7d DEX volume | $16.29B · -7.85% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $15.65M |
| Fees 1d / 7d | +6.81% / +17.26% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $873.43M | +28.85% |
| Raydium AMM | $344.51M | -12.15% |
| BisonFi | $204.07M | -15.48% |
| Meteora DLMM | $195.35M | -12.44% |
| Orca DEX | $192.17M | -41.18% |
| Tessera V | $149.50M | -27.57% |
| Manifest Trade | $132.19M | +0.68% |
| pump.fun | $100.28M | +73.96% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.58B | -0.82% | +3.93% |
| Kamino Lend | Lending | $1.36B | +1.82% | +10.71% |
| Raydium AMM | Dexs | $1.14B | -0.78% | +3.21% |
| Binance Staked SOL | Liquid Staking | $1.07B | -0.98% | +3.76% |
| Jupiter Lend | Lending | $1.07B | -1.46% | +1.75% |
| Jito Liquid Staking | Liquid Staking | $1.06B | -0.82% | +5.51% |
| BlackRock BUIDL | RWA | $987.58M | -0.40% | -0.03% |
| Jupiter Perpetual Exchange | Derivatives | $749.00M | -0.85% | +0.76% |
| Jupiter Staked SOL | Liquid Staking | $534.75M | -0.60% | +3.37% |
| xStocks | RWA | $443.31M | -1.05% | +2.37% |

## Stablecoins

Solana circulating pegged-USD: **$16.23B**
(1d -0.27% · 7d +4.54%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.20B | -2.12% |
| USDT · Tether | $2.77B | +0.00% |
| USDGO · USDGO | $1.37B | +0.74% |
| USD1 · World Liberty Financial USD | $1.28B | +2.06% |
| BUIDL · BlackRock USD | $987.58M | +0.99% |
| PYUSD · PayPal USD | $727.69M | -2.78% |
| USDG · Global Dollar | $576.50M | -1.81% |
| USDe · Ethena USDe | $536.78M | +0.31% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 68 of 737 Solana-deployed listed symbols (multiplier ok 80/80; 737 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 737 · Solana deployments 737 · priced 68 · priced-subset mcap $289.90M (lower bound, not a census).
24h volume $92.47M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $443.31M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 68 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 737 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 737 unique underlyings among 737 Solana rows; not every tokenized equity on Solana). 737 of 737 listed xStocks have a Solana deployment (737 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.35B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $987.58M
- **xStocks** (RWA) — $443.31M
- **OnRe** (RWA) — $304.03M
- **Ondo Yield Assets** (RWA) — $180.06M
- **Huma Finance V2** (RWA) — $171.51M
- **Hastra** (RWA) — $149.87M
- **Ondo Global Markets** (RWA) — $25.77M
- **Plume Vaults** (RWA) — $24.11M

## Daily active addresses

867,112 (Allium, as of 2026-09-07). Provider range 478,831–936,187. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [The feed needs a little more shuffle 

2026 @WSOP Super Circuit Canada live on X https://x.com/i/broadcasts/1MJgNbALWnqGL](https://x.com/solana/status/2097439289302729029) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 21:37:49 GMT
- [$SPHR is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2097415067671384258) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 20:01:34 GMT
- [Sphere Entertainment ($SPHR) operates the Las Vegas Sphere, the world's most advanced venue, home to the largest LED screen on the planet.

Verify the address on @tokens:
https://tokens.xyz/sphr?solana=SPHRp8cZaSQBTp1KMNP4V1X821SXhXWt4Q2yLdyHzju](https://x.com/solana/status/2097415065150603323) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 20:01:34 GMT
- [BREAKING: $SPHR is live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2097415062441120076) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 20:01:33 GMT
- [Allium's report covers 35 issuers with live RWA products on Solana across five asset classes.

Full report here 👇
https://www.allium.so/reports/solana-rwa-ecosystem](https://x.com/solana/status/2097411330890502393) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 19:46:43 GMT
- [Solana takes 74% of onchain fixed-income volume, $5.4B of the market's $7.4B, most of it @maplefinance private credit.](https://x.com/solana/status/2097411313681182924) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 19:46:39 GMT
- [Pre-IPO exposure: you can trade these companies before they list, right from a Solana wallet.

SpaceX $330M. OpenAI $272M. Anthropic $228M, from 23,722 traders.

@PreStocks added $1.3B pricing companies before they list.](https://x.com/solana/status/2097411296522326073) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 19:46:35 GMT
- [Wallet holdings across RWA products on Solana are up 5x in a year, and tokenized stocks drove 98% of the increase since April.

@xStocksFI leads the class with $5.0B traded on Solana over 12 months. @Backpack launched its equity venue on June 12 and did $1.5B in two months, 19% of Solana's equity volume so far this year.](https://x.com/solana/status/2097411279157858766) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 19:46:31 GMT
- [RT by @anza_xyz: What is cool about transaction v1?
1) @multisig smart wallet being able to do everything onchain with big pqc based signatures 
2) two zkp root state transitions in one atomic tx, aka “based rollups”
3) routing to a bajilion markets at the same time](https://x.com/toly/status/2097345987937497491) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:27:04 GMT
- [Alpenglow is coming.](https://x.com/anza_xyz/status/2097352587817455967) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:53:18 GMT `upgrade`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [The feed needs a little more shuffle 

2026 @WSOP Super Circuit Canada live on X https://x.com/i/broadcasts/1MJgNbALWnqGL](https://x.com/solana/status/2097439289302729029) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 21:37:49 GMT
- [$SPHR is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2097415067671384258) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 20:01:34 GMT
- [Sphere Entertainment ($SPHR) operates the Las Vegas Sphere, the world's most advanced venue, home to the largest LED screen on the planet.

Verify the address on @tokens:
https://tokens.xyz/sphr?solana=SPHRp8cZaSQBTp1KMNP4V1X821SXhXWt4Q2yLdyHzju](https://x.com/solana/status/2097415065150603323) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 20:01:34 GMT
- [BREAKING: $SPHR is live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2097415062441120076) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 20:01:33 GMT
- [Allium's report covers 35 issuers with live RWA products on Solana across five asset classes.

Full report here 👇
https://www.allium.so/reports/solana-rwa-ecosystem](https://x.com/solana/status/2097411330890502393) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 19:46:43 GMT
- [Solana takes 74% of onchain fixed-income volume, $5.4B of the market's $7.4B, most of it @maplefinance private credit.](https://x.com/solana/status/2097411313681182924) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 19:46:39 GMT
- [Pre-IPO exposure: you can trade these companies before they list, right from a Solana wallet.

SpaceX $330M. OpenAI $272M. Anthropic $228M, from 23,722 traders.

@PreStocks added $1.3B pricing companies before they list.](https://x.com/solana/status/2097411296522326073) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 19:46:35 GMT
- [Wallet holdings across RWA products on Solana are up 5x in a year, and tokenized stocks drove 98% of the increase since April.

@xStocksFI leads the class with $5.0B traded on Solana over 12 months. @Backpack launched its equity venue on June 12 and did $1.5B in two months, 19% of Solana's equity volume so far this year.](https://x.com/solana/status/2097411279157858766) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 19:46:31 GMT
- [RT by @anza_xyz: What is cool about transaction v1?
1) @multisig smart wallet being able to do everything onchain with big pqc based signatures 
2) two zkp root state transitions in one atomic tx, aka “based rollups”
3) routing to a bajilion markets at the same time](https://x.com/toly/status/2097345987937497491) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:27:04 GMT
- [Alpenglow is coming.](https://x.com/anza_xyz/status/2097352587817455967) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:53:18 GMT `upgrade`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-08 (2026-09-08 14:49:56 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~319 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~319 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 245ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 173ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 159ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 191ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 172ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6845ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 374ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 69ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 132ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 62ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 30ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 27ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 872ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 82ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 33ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 55ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 81ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 215ms https://solana.com/data
- `solana.com.databricks` [ok] 200 61ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 1076ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 119ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 183ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 143ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 276ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 338ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 311ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 74ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 80ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 303ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 740ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2235ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 2000ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 42ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 173ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 178ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 757ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 871ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1070ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1189ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 923ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1075ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1196ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 892ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 978ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 970ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 945ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1119ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 923ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1040ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 3518ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1334ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 3453ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 3233ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1194ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1930ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1647ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 599ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.NVDAx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.METAx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.MSFTx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.SPYx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.NVDAx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.TSLAx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.METAx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.AMZNx` [ok] 200 884ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.GOOGLx` [ok] 200 889ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.mult.TSLAx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.XRXx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.AAPLx` [ok] 200 1043ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.COINx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 716ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.COINx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.WGSx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.mult.MSFTx` [ok] 200 834ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.FLNCx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.circ.WGSx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 691ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.PCTx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.INDIx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.circ.FLNCx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.price.WRLDx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.circ.PCTx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.WRLDx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.price.METCx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.mult.QQQx` [ok] 200 428ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.AIx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.METCx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.QUBTx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.mult.WRLDx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.DRAMx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.circ.BETRx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.MVLLx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.mult.METCx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.BETRx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 679ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.AIx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.price.MUUx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.mult.QUBTx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.price.AXTIx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.circ.WYFIx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.circ.MUUx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.price.INTWx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.KORUx` [ok] 200 532ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.WYFIx` [ok] 200 516ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.AXTIx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.DJTx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 2207ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.price.SOXSx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.SNXXx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.SOXSx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.SNXXx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.SHEINx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.BANKCx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.NWGx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.circ.SHEINx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.SHEINx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.MVLLx` [ok] 200 1780ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.mult.MUUx` [ok] 200 1563ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.INTWx` [ok] 200 1221ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.INTWx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.KORUx` [ok] 200 1390ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.price.CTINSx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.mult.BANKCx` [ok] 200 1045ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 597ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.HAIDLx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.CTINSx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.NWGx` [ok] 200 1242ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.NWGx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.SZIGHx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.HRZRBx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 1171ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 510ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 687ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.CRESBx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 849ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 841ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 1077ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 482ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 1971ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.MIXUx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.BDWAPx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.CMENDx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 2512ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.CSPCx` [ok] 200 1151ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.CRESMx` [ok] 200 874ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.CSPCx` [ok] 200 427ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 597ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.CRESMx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 801ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 809ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.mult.MIXUx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.SNDSCx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.CRESPx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 676ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 656ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.SINOTx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 687ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.SNDSCx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 525ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.CTPCAx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.CLONPx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 1044ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.PWAHLx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.WHGROx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.SINOTx` [ok] 200 1186ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.WHGROx` [ok] 200 726ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.GENTEx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 882ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 808ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.PRADx` [ok] 200 818ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 623ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.CKINFx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.CKAHx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.KUAIx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.CKINFx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 1560ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 737ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 1085ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 1687ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 3190ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 48ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 97ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INTWx` [ok] 200 43ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.KORUx` [ok] 200 43ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.SHEINx` [ok] 200 54ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.MVLLx` [ok] 200 41ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.MUUx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.SNXXx` [ok] 200 41ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jup.tokens.search.DRAMx` [ok] 200 73ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.SOXSx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jito.tip_floor` [ok] 200 190ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 202ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 81ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 174ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 171ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 150ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 172ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 286ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
