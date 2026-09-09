# Borealis — Solana ecosystem report

**Generated** 2026-09-09T08:07:32Z · 2026-09-09 01:07:32 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-09T08:07:22Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +2.08%; DEX 24h $2.58B · 1d -5% · vs-7d-ago +19%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +30.04%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 445,561,466 |
| Block height | 423,605,071 |
| Block time | 2026-09-09T08:07:22Z |
| Epoch | 1,031 (39.23% · slot 169,468/432,000) |
| Mean TPS (last ~3,600s) | 3,679.4 |
| Mean non-vote TPS | 1,568.3 |
| Median TPS (same window) | 3,642.3 |
| Mean slot time | 316.4 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 546,625,302,471 |
| Circulating supply | 586,250,671 SOL |
| Total supply | 633,736,897 SOL |
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

- `mrgn4atx…` · 20.28K SOL · commission 0% · lag 206759 slots
- `inWVrrYJ…` · 9.89K SOL · commission 0% · lag 210437 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 2212743 slots
- `prt1st4R…` · 5.87K SOL · commission 5% · lag 2074524 slots
- `xLabscif…` · 4.17K SOL · commission 5% · lag 1773093 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 1595544 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 62710 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 234583 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 445561466 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 61512596 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 722455 slots

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
| Jito tip-floor run-rate (NOT REV) | $64.80K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 64797 USD; at p95 floor → 754110 USD. |
| Protocol fees 24h | $16.44M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9978 |
| p90 / p99 | 0.000010 / 0.000071 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $104.82 | coingecko.simple_price |
| 24h change | +2.08% | coingecko.simple_price |
| Market cap | $61.43B | coingecko.simple_price |
| 24h volume | $2.84B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.97B |
| TVL 1d / 7d / 30d | +0.85% / +5.56% / +22.80% |
| DEX volume 24h | $2.58B · 1d -5.25% · vs-7d-ago +18.71% |
| 7d DEX volume | $15.86B · -6.25% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $16.44M |
| Fees 1d / 7d | +5.13% / +30.04% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $737.12M | -15.61% |
| Raydium AMM | $333.60M | +8.38% |
| Meteora DLMM | $237.76M | +21.71% |
| BisonFi | $204.07M | 0.00% |
| Tessera V | $149.50M | 0.00% |
| Manifest Trade | $125.60M | -8.08% |
| Orca DEX | $117.30M | -50.48% |
| pump.fun | $100.28M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.60B | +1.59% | +4.82% |
| Kamino Lend | Lending | $1.37B | +2.64% | +10.80% |
| Raydium AMM | Dexs | $1.15B | +0.55% | +6.03% |
| Jupiter Lend | Lending | $1.11B | +2.26% | +4.05% |
| Binance Staked SOL | Liquid Staking | $1.08B | +1.22% | +4.70% |
| Jito Liquid Staking | Liquid Staking | $1.07B | +1.71% | +6.75% |
| BlackRock BUIDL | RWA | $987.58M | -0.40% | +1.37% |
| Jupiter Perpetual Exchange | Derivatives | $756.49M | +0.89% | +1.35% |
| Jupiter Staked SOL | Liquid Staking | $539.77M | +1.07% | +4.14% |
| xStocks | RWA | $443.71M | +0.39% | +2.54% |

## Stablecoins

Solana circulating pegged-USD: **$16.21B**
(1d -0.39% · 7d +4.94%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.14B | -2.56% |
| USDT · Tether | $2.76B | -0.00% |
| USDGO · USDGO | $1.37B | -0.36% |
| USD1 · World Liberty Financial USD | $1.28B | +1.58% |
| BUIDL · BlackRock USD | $987.58M | +0.99% |
| PYUSD · PayPal USD | $752.70M | +2.87% |
| USDG · Global Dollar | $590.31M | +3.22% |
| USDe · Ethena USDe | $536.66M | +0.16% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 78 of 737 Solana-deployed listed symbols (multiplier ok 80/80; 737 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 737 · Solana deployments 737 · priced 78 · priced-subset mcap $291.03M (lower bound, not a census).
24h volume $85.93M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $443.71M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 78 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 737 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 737 unique underlyings among 737 Solana rows; not every tokenized equity on Solana). 737 of 737 listed xStocks have a Solana deployment (737 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.35B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $987.58M
- **xStocks** (RWA) — $443.71M
- **OnRe** (RWA) — $304.55M
- **Ondo Yield Assets** (RWA) — $180.05M
- **Huma Finance V2** (RWA) — $171.25M
- **Hastra** (RWA) — $149.77M
- **Ondo Global Markets** (RWA) — $25.88M
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

_As of 2026-09-09 (2026-09-09 01:07:32 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 737 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 346ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 377ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 339ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 338ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 306ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6139ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 659ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 90ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 85ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 39ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 32ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 20ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 29ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 63ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 35ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 45ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 65ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 462ms https://solana.com/data
- `solana.com.databricks` [ok] 200 52ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 469ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 112ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 24ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 101ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 427ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 910ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 460ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 634ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 439ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1387ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 273ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1129ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1345ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 160ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 312ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 313ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1325ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1271ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1440ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1560ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1540ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1343ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1408ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1419ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1593ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1376ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1328ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1228ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1579ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1491ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2613ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1873ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2100ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1843ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1665ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1598ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2051ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 889ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.NVDAx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.TSLAx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.GOOGLx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.MSFTx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.AMZNx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.NVDAx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.AMZNx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.AAPLx` [ok] 200 507ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.mult.NVDAx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.price.SPYx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.mult.MSFTx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.GOOGLx` [ok] 200 536ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.QQQx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.XRXx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.circ.SPYx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 792ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.FLNCx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.mult.QQQx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 1000ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.WGSx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.INDIx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WRLDx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.mult.AMZNx` [ok] 200 1306ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 703ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.INDIx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.XRXx` [ok] 200 1013ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 1210ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 765ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.price.QUBTx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.PCTx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.price.METCx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.mult.WGSx` [ok] 200 510ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.mult.PCTx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.MVLLx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.mult.FLNCx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.circ.MVLLx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.DRAMx` [ok] 200 762ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.WYFIx` [ok] 200 959ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.price.AIx` [ok] 200 954ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.AXTIx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.BETRx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.MUUx` [ok] 200 816ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.circ.AIx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.KORUx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.price.DJTx` [ok] 200 406ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.mult.METCx` [ok] 200 1417ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 563ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 864ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 572ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 691ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.mult.AXTIx` [ok] 200 989ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.mult.MUUx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.INTWx` [ok] 200 756ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.SHEINx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.SHEINx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 1321ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.price.NWGx` [ok] 200 689ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.mult.WYFIx` [ok] 200 1085ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 1571ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.SHEINx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 1345ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 652ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.SNXXx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.KORUx` [ok] 200 738ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.NWGx` [ok] 200 1124ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.INTWx` [ok] 200 1802ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 977ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.NWGx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 1376ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.JDLOGx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.MMGx` [ok] 200 903ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.SOXSx` [ok] 200 3221ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.KUNLx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 1049ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.HAIDLx` [ok] 200 779ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.HRZRBx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.KUNLx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.SNBIOx` [ok] 200 881ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.SMOIHx` [ok] 200 636ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 2546ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 624ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 519ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 1520ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 660ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 1163ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 706ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.JTGEXx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.CRESMx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 1129ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.BDWAPx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.CRESMx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 599ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 949ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.ASMPTx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.MIXUx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 897ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.CMERPx` [ok] 200 2030ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 1117ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.SITCx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 1254ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 674ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 1099ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 595ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 1308ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.mult.CMENDx` [ok] 200 924ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.CRESPx` [ok] 200 722ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.CMERPx` [ok] 200 1163ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.CRESPx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 1257ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.PRADx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.WHRFRx` [ok] 200 660ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.CLONPx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.PWAHLx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 392ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.SINOTx` [ok] 200 997ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 604ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.CTPCAx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.CLONPx` [ok] 200 774ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 510ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 932ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 586ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.SWPRPx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.WHGROx` [ok] 200 1452ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 622ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.CKINFx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.CTFJWx` [ok] 200 1404ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.CKAHx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 514ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 794ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 728ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 595ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 68ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 334ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INTWx` [ok] 200 101ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.KORUx` [ok] 200 185ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.SHEINx` [ok] 200 101ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.MVLLx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.MUUx` [ok] 200 98ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.SNXXx` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jup.tokens.search.DRAMx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.SOXSx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jito.tip_floor` [ok] 200 314ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 282ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 238ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 332ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 341ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 338ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 408ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 360ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
