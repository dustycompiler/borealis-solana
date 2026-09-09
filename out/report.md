# Borealis — Solana ecosystem report

**Generated** 2026-09-09T06:54:23Z · 2026-09-08 23:54:23 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-09T06:54:11Z · **RPC health** `ok`
**Health score** 73 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** DEGRADED · **Ecosystem** ELEVATED — SOL 24h +1.90%; DEX 24h $2.58B · 1d -5% · vs-7d-ago +19%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · High validator delinquency** — 12 delinquent vote accounts, 2.868% of activated+delinquent stake. (threshold: `delinquent stake >= 1% or delinquent count >= 25`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +30.04%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 445,547,588 |
| Block height | 423,591,343 |
| Block time | 2026-09-09T06:54:11Z |
| Epoch | 1,031 (36.02% · slot 155,588/432,000) |
| Mean TPS (last ~3,600s) | 3,809.4 |
| Mean non-vote TPS | 1,698.3 |
| Median TPS (same window) | 3,784.6 |
| Mean slot time | 316.9 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 546,609,230,889 |
| Circulating supply | 586,250,713 SOL |
| Total supply | 633,736,940 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 426,073,414 SOL |
| Delinquent stake | 12,580,091.02 SOL (2.868%) |
| Nakamoto (33% / 50% / 67%) | 19 / 43 / 82 |
| Top 10 / 20 stake share | 23.46% / 34.57% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 4.09% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.35M SOL | 3.84% | 0% | 0 |
| 3 | `JUPiTERr…` | 11.39M SOL | 2.67% | 5% | 0 |
| 4 | `E1r4Psq8…` | 9.57M SOL | 2.25% | 0% | 0 |
| 5 | `C8Bey3LK…` | 9.29M SOL | 2.18% | 7% | 0 |
| 6 | `CAo1dCGY…` | 9.03M SOL | 2.12% | 10% | 0 |
| 7 | `EvnRmnMr…` | 7.32M SOL | 1.72% | 7% | 0 |
| 8 | `9eGrDohd…` | 6.86M SOL | 1.61% | 5% | 0 |
| 9 | `Awes4Tr6…` | 6.60M SOL | 1.55% | 0% | 0 |
| 10 | `JD549Hsb…` | 6.12M SOL | 1.44% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.44% | 100% | 0 |
| 12 | `5pPRHnie…` | 5.97M SOL | 1.40% | 5% | 0 |
| 13 | `5Cchr1XG…` | 5.63M SOL | 1.32% | 100% | 0 |
| 14 | `GnC339vk…` | 4.83M SOL | 1.13% | 7% | 0 |
| 15 | `9rkJMARq…` | 4.66M SOL | 1.09% | 8% | 0 |

### Delinquency alerts

- `DRpbCBMx…` · 12.53M SOL · commission 0% · lag 1838 slots
- `mrgn4atx…` · 20.28K SOL · commission 0% · lag 192881 slots
- `inWVrrYJ…` · 9.89K SOL · commission 0% · lag 196559 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 2198865 slots
- `prt1st4R…` · 5.87K SOL · commission 5% · lag 2060646 slots
- `xLabscif…` · 4.17K SOL · commission 5% · lag 1759215 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 1581666 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 48832 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 220705 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 445547588 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 61498718 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 708577 slots

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
| Jito tip-floor run-rate (NOT REV) | $41.57K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 41573 USD; at p95 floor → 436343 USD. |
| Protocol fees 24h | $16.44M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9963 |
| p90 / p99 | 0.000012 / 0.000091 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $104.55 | coingecko.simple_price |
| 24h change | +1.90% | coingecko.simple_price |
| Market cap | $61.29B | coingecko.simple_price |
| 24h volume | $2.84B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.95B |
| TVL 1d / 7d / 30d | +0.54% / +5.23% / +22.42% |
| DEX volume 24h | $2.58B · 1d -5.25% · vs-7d-ago +18.71% |
| 7d DEX volume | $15.86B · -6.25% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $16.44M |
| Fees 1d / 7d | +5.13% / +30.04% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $737.12M | -15.61% |
| Raydium AMM | $337.79M | +9.74% |
| Meteora DLMM | $237.76M | +21.71% |
| BisonFi | $204.07M | 0.00% |
| Tessera V | $149.50M | 0.00% |
| Manifest Trade | $122.37M | -10.45% |
| Orca DEX | $117.30M | -50.48% |
| pump.fun | $100.28M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.60B | +1.23% | +4.77% |
| Kamino Lend | Lending | $1.37B | +2.64% | +10.80% |
| Raydium AMM | Dexs | $1.15B | +0.55% | +6.03% |
| Jupiter Lend | Lending | $1.11B | +1.59% | +3.82% |
| Binance Staked SOL | Liquid Staking | $1.08B | +1.22% | +4.70% |
| Jito Liquid Staking | Liquid Staking | $1.07B | +1.02% | +6.35% |
| BlackRock BUIDL | RWA | $987.58M | -0.40% | +1.37% |
| Jupiter Perpetual Exchange | Derivatives | $754.48M | +0.62% | +1.24% |
| Jupiter Staked SOL | Liquid Staking | $539.77M | +1.07% | +4.14% |
| xStocks | RWA | $445.47M | +0.11% | +3.17% |

## Stablecoins

Solana circulating pegged-USD: **$16.21B**
(1d -0.39% · 7d +4.94%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.14B | -2.51% |
| USDT · Tether | $2.76B | -0.00% |
| USDGO · USDGO | $1.37B | -0.36% |
| USD1 · World Liberty Financial USD | $1.28B | +1.58% |
| BUIDL · BlackRock USD | $987.58M | +0.99% |
| PYUSD · PayPal USD | $752.68M | +2.87% |
| USDG · Global Dollar | $590.29M | +3.22% |
| USDe · Ethena USDe | $536.66M | +0.16% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 77 of 737 Solana-deployed listed symbols (multiplier ok 80/80; 737 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 737 · Solana deployments 737 · priced 77 · priced-subset mcap $290.75M (lower bound, not a census).
24h volume $87.80M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $445.47M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 77 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 737 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 737 unique underlyings among 737 Solana rows; not every tokenized equity on Solana). 737 of 737 listed xStocks have a Solana deployment (737 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.35B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $987.58M
- **xStocks** (RWA) — $445.47M
- **OnRe** (RWA) — $304.55M
- **Ondo Yield Assets** (RWA) — $180.05M
- **Huma Finance V2** (RWA) — $171.21M
- **Hastra** (RWA) — $149.77M
- **Ondo Global Markets** (RWA) — $25.87M
- **Plume Vaults** (RWA) — $24.96M

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

- [RT by @solana: Meteora DBC now supports any token pair on @solana.

Stock tokens, RWAs, and other Token-2022 assets can now be used as quote tokens in DBC launch configurations.

If it’s on Solana, you can launch it on Meteora.](https://x.com/MeteoraAG/status/2097559327855034437) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 05:34:49 GMT
- [Join us on October 6th https://luma.com/solana-summit-singapore-2026](https://x.com/solana/status/2097552418582167824) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 05:07:21 GMT
- [Solana Summit APAC 🇸🇬 🔜](https://x.com/solana/status/2097552314605383827) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 05:06:57 GMT
- [RT by @solana: 2,000+ applications & counting. One week to go.

R[3]sidency × Construct is bringing together some of the strongest early-stage builders across AI, crypto, fintech, robotics and beyond.

Built by Fabric Ventures and @wintermute_t, with @solana, @SuperteamUK and continued support from @coinbase.

Swipe through for a look at the applicant pool →

Applications close 15 September.](https://x.com/fabric_vc/status/2097324225556258890) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 14:00:36 GMT
- [memes are useless](https://x.com/solana/status/2097483917808791801) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 00:35:10 GMT
- [RT by @solana: Visa, Western Union, PayPal, Stripe, Youtube, Worldpay, Nuvei, Fiserv, Mastercard, BlackRock, WisdomTree, Franklin Templeton, Ondo Finance, Citi Bank, Hamilton Lane, JPMorgan, State Street, Galaxy Digital, Société Générale, R3, BNY Mellon, Morgan Stanley, Bitwise, Fidelity, RockawayX, Kingdom of Bhutan, Zodia Markets, and many others choose to build on Solana](https://x.com/solquicks/status/2097443726901793155) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 21:55:27 GMT
- [RT by @solana: 🚨JUST IN: Sphere Entertainment’s tokenized stock $SPHR hit $5.37M in volume on @Solana within two hours of launch, equivalent to 14.2% of the underlying stock’s daily volume, driven by a surge in memestock pairs.](https://x.com/SolanaFloor/status/2097452587457171943) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 22:30:40 GMT
- [The feed needs a little more shuffle 

2026 @WSOP Super Circuit Canada live on X https://x.com/i/broadcasts/1MJgNbALWnqGL](https://x.com/solana/status/2097439289302729029) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 21:37:49 GMT
- [RT by @anza_xyz: What is cool about transaction v1?
1) @multisig smart wallet being able to do everything onchain with big pqc based signatures 
2) two zkp root state transitions in one atomic tx, aka “based rollups”
3) routing to a bajilion markets at the same time](https://x.com/toly/status/2097345987937497491) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:27:04 GMT
- [Alpenglow is coming.](https://x.com/anza_xyz/status/2097352587817455967) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:53:18 GMT `upgrade`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: Meteora DBC now supports any token pair on @solana.

Stock tokens, RWAs, and other Token-2022 assets can now be used as quote tokens in DBC launch configurations.

If it’s on Solana, you can launch it on Meteora.](https://x.com/MeteoraAG/status/2097559327855034437) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 05:34:49 GMT
- [Join us on October 6th https://luma.com/solana-summit-singapore-2026](https://x.com/solana/status/2097552418582167824) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 05:07:21 GMT
- [Solana Summit APAC 🇸🇬 🔜](https://x.com/solana/status/2097552314605383827) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 05:06:57 GMT
- [RT by @solana: 2,000+ applications & counting. One week to go.

R[3]sidency × Construct is bringing together some of the strongest early-stage builders across AI, crypto, fintech, robotics and beyond.

Built by Fabric Ventures and @wintermute_t, with @solana, @SuperteamUK and continued support from @coinbase.

Swipe through for a look at the applicant pool →

Applications close 15 September.](https://x.com/fabric_vc/status/2097324225556258890) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 14:00:36 GMT
- [memes are useless](https://x.com/solana/status/2097483917808791801) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 00:35:10 GMT
- [RT by @solana: Visa, Western Union, PayPal, Stripe, Youtube, Worldpay, Nuvei, Fiserv, Mastercard, BlackRock, WisdomTree, Franklin Templeton, Ondo Finance, Citi Bank, Hamilton Lane, JPMorgan, State Street, Galaxy Digital, Société Générale, R3, BNY Mellon, Morgan Stanley, Bitwise, Fidelity, RockawayX, Kingdom of Bhutan, Zodia Markets, and many others choose to build on Solana](https://x.com/solquicks/status/2097443726901793155) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 21:55:27 GMT
- [RT by @solana: 🚨JUST IN: Sphere Entertainment’s tokenized stock $SPHR hit $5.37M in volume on @Solana within two hours of launch, equivalent to 14.2% of the underlying stock’s daily volume, driven by a surge in memestock pairs.](https://x.com/SolanaFloor/status/2097452587457171943) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 22:30:40 GMT
- [The feed needs a little more shuffle 

2026 @WSOP Super Circuit Canada live on X https://x.com/i/broadcasts/1MJgNbALWnqGL](https://x.com/solana/status/2097439289302729029) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 21:37:49 GMT
- [RT by @anza_xyz: What is cool about transaction v1?
1) @multisig smart wallet being able to do everything onchain with big pqc based signatures 
2) two zkp root state transitions in one atomic tx, aka “based rollups”
3) routing to a bajilion markets at the same time](https://x.com/toly/status/2097345987937497491) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:27:04 GMT
- [Alpenglow is coming.](https://x.com/anza_xyz/status/2097352587817455967) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:53:18 GMT `upgrade`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-09 (2026-09-08 23:54:23 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 737 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 285ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 175ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 212ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 226ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 155ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5967ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 384ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 156ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 158ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 239ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 76ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 847ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1119ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 258ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 117ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 114ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 139ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 623ms https://solana.com/data
- `solana.com.databricks` [ok] 200 387ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 624ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 148ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 131ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 187ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 356ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 677ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 311ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 347ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 365ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 2168ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 607ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1501ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1499ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 199ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 225ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 201ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 755ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 769ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 649ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 827ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 735ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 685ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 960ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 961ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 709ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 830ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 839ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 753ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 543ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 693ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2131ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1604ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1949ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1756ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1889ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1747ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1542ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 831ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.METAx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.AAPLx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.GOOGLx` [ok] 200 589ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.AAPLx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.TSLAx` [ok] 200 839ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.mult.AAPLx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.SPYx` [ok] 200 939ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.NVDAx` [ok] 200 1199ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.QQQx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.METAx` [ok] 200 895ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.TSLAx` [ok] 200 651ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.AMZNx` [ok] 200 1571ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.mult.SPYx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 603ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.FLNCx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.mult.TSLAx` [ok] 200 639ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.WGSx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.circ.NVDAx` [ok] 200 961ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.XRXx` [ok] 200 625ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.WRLDx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.MSFTx` [ok] 200 2407ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.mult.NVDAx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.INDIx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.circ.WGSx` [ok] 200 694ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 1821ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.WGSx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.XRXx` [ok] 200 1443ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.price.PCTx` [ok] 200 496ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.AMZNx` [ok] 200 2255ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 1753ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 1074ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.INDIx` [ok] 200 1362ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.price.QUBTx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.METCx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.WRLDx` [ok] 200 2320ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 653ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 1261ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.price.AIx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.PCTx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.METCx` [ok] 200 1217ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.circ.AIx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 1766ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.AIx` [ok] 200 400ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.AXTIx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.MVLLx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.mult.METCx` [ok] 200 1164ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.price.MUUx` [ok] 200 708ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.price.DJTx` [ok] 200 613ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.MVLLx` [ok] 200 922ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.BETRx` [ok] 200 2598ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 675ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.BETRx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 1481ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.AXTIx` [ok] 200 1992ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.KORUx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.MUUx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 5429ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 4943ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.price.SHEINx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.price.INTWx` [ok] 200 1143ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.SOXSx` [ok] 200 898ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.mult.AXTIx` [ok] 200 1159ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 1143ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 2528ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.QUBTx` [ok] 200 5970ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.SHEINx` [ok] 200 815ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.SOXSx` [ok] 200 1214ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.BANKCx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.SNXXx` [ok] 200 2403ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 1138ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.SNXXx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 2681ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 1364ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 533ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.INTWx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 962ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 1493ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.KUNLx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.KUNLx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 596ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 1000ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 1200ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 970ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 654ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 431ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 649ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.SMOIHx` [ok] 200 1354ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.mult.CRESBx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.CMERPx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.CSPCx` [ok] 200 862ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 738ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 524ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 2526ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.CRESMx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 482ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.CSPCx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.CMENDx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.JTGEXx` [ok] 200 1742ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 2405ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 431ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.ASMPTx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.CMENDx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.PRADx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.CRESPx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.SNDSCx` [ok] 200 719ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.circ.PRADx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 439ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 1161ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 1591ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.CLONPx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.SINOTx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.CRESPx` [ok] 200 558ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 1894ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 920ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.SINOTx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.PWAHLx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 716ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 724ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.CLONPx` [ok] 200 706ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 825ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 576ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 685ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.WUXIBx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 953ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.CKAHx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 1185ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.GENTEx` [ok] 200 945ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 760ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.NWGx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HKCGAx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.NWGx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 1300ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.NWGx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 1676ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 1617ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.CKAHx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 1276ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 1586ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 1588ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 6591ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 2131ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1469ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 271ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.AMZNx` [ok] 200 134ms https://lite-api.jup.ag/tokens/v2/search?query=AMZNx
- `jup.tokens.search.INTWx` [ok] 200 142ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.SHEINx` [ok] 200 148ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.KORUx` [ok] 200 134ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.MVLLx` [ok] 200 137ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.MUUx` [ok] 200 138ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.DRAMx` [ok] 200 132ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.SNXXx` [ok] 200 144ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jito.tip_floor` [ok] 200 117ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 314ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 236ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 129ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 147ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 140ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 227ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 251ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
