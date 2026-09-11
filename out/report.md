# Borealis — Solana ecosystem report

**Generated** 2026-09-11T21:22:43Z · 2026-09-11 14:22:43 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-11T21:22:32Z · **RPC health** `ok`
**Health score** 93 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +2.92%; DEX 24h $2.92B · 1d -3% · vs-7d-ago +19%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +23.60%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 967,396.00 is +22.0% vs 30d median 793,088.50 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 446,257,970 |
| Block height | 424,300,970 |
| Block time | 2026-09-11T21:22:32Z |
| Epoch | 1,033 (0.46% · slot 1,970/432,000) |
| Mean TPS (last ~3,600s) | 4,349.8 |
| Mean non-vote TPS | 2,229.4 |
| Median TPS (same window) | 4,249.5 |
| Mean slot time | 317.0 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 547,515,059,439 |
| Circulating supply | 586,623,425 SOL |
| Total supply | 633,924,711 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 677 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 435,137,392 SOL |
| Delinquent stake | 1,700,289.29 SOL (0.389%) |
| Nakamoto (33% / 50% / 67%) | 18 / 40 / 79 |
| Top 10 / 20 stake share | 24.49% / 35.86% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.56M SOL | 4.03% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.36M SOL | 3.76% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.52M SOL | 2.88% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.37M SOL | 2.61% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.67M SOL | 2.22% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.23M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.02M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.36M SOL | 1.69% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.94M SOL | 1.60% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.55M SOL | 1.51% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.13M SOL | 1.41% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.12M SOL | 1.41% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.37% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.62M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `pSo1KZXg…` · 1.64M SOL · commission 4% · lag 1943 slots
- `EWARp8Sy…` · 31.93K SOL · commission 5% · lag 479 slots
- `mrgn4atx…` · 19.58K SOL · commission 0% · lag 1943 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 1943 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 1943 slots
- `4GEEKSwu…` · 326.50 SOL · commission 5% · lag 448358 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 558873 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 446257970 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 62209100 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 1943 slots
- `4kdjgZKJ…` · 1.05 SOL · commission 100% · lag 446257970 slots
- `3BoZ4AF2…` · 1.00 SOL · commission 100% · lag 446257970 slots

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
| **In-protocol fees 24h** | **$1.01M** (9,683.4 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-09 |
| **Solana REV** | **11,493.1 SOL** / **$1.20M** | MEASURED UTC calendar day 2026-09-09: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-09 · UTC day 2026-09-09 · SOL-USD date 2026-09-09 |
| Jito tip-floor run-rate (NOT REV) | $144.68K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 144684 USD; at p95 floor → 2167995 USD. |
| Protocol fees 24h | $14.61M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9969 |
| p90 / p99 | 0.000010 / 0.000138 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $102.83 | coingecko.simple_price |
| 24h change | +2.92% | coingecko.simple_price |
| Market cap | $60.32B | coingecko.simple_price |
| 24h volume | $4.57B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.87B |
| TVL 1d / 7d / 30d | +0.15% / -1.11% / +20.33% |
| DEX volume 24h | $2.92B · 1d -2.61% · vs-7d-ago +18.80% |
| 7d DEX volume | $18.00B · +15.32% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.61M |
| Fees 1d / 7d | -6.98% / +23.60% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| Raydium AMM | $505.05M | +16.07% |
| PumpSwap | $468.14M | +37.30% |
| BisonFi | $395.81M | -1.73% |
| HumidiFi | $322.67M | +12.96% |
| Tessera V | $232.00M | -6.46% |
| Meteora DLMM | $220.43M | -31.60% |
| Orca DEX | $201.48M | +18.84% |
| Manifest Trade | $151.47M | -0.33% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.55B | +1.50% | +0.17% |
| Kamino Lend | Lending | $1.35B | +1.75% | +1.17% |
| Raydium AMM | Dexs | $1.14B | +3.21% | +3.19% |
| Jupiter Lend | Lending | $1.07B | +0.38% | +0.35% |
| Binance Staked SOL | Liquid Staking | $1.05B | +1.32% | -0.64% |
| Jito Liquid Staking | Liquid Staking | $1.04B | +1.32% | +0.95% |
| BlackRock BUIDL | RWA | $992.60M | -0.61% | -2.25% |
| Jupiter Perpetual Exchange | Derivatives | $747.17M | +1.06% | -0.49% |
| Jupiter Staked SOL | Liquid Staking | $523.52M | +1.38% | +0.00% |
| Sentora Curator | Risk Curators | $387.52M | +0.91% | -2.48% |

## Stablecoins

Solana circulating pegged-USD: **$16.23B**
(1d -1.50% · 7d -1.63%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.24B | +1.45% |
| USDT · Tether | $2.61B | -5.42% |
| USDGO · USDGO | $1.38B | +0.72% |
| USD1 · World Liberty Financial USD | $1.30B | +1.51% |
| BUIDL · BlackRock USD | $992.60M | +0.04% |
| PYUSD · PayPal USD | $694.54M | -8.23% |
| USDG · Global Dollar | $600.65M | -0.18% |
| USDe · Ethena USDe | $536.50M | +0.14% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 14 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $107.16M (lower bound, not a census).
24h volume $119.78M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 14 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.91B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.60M
- **OnRe** (RWA) — $294.74M
- **Ondo Yield Assets** (RWA) — $180.05M
- **Huma Finance V2** (RWA) — $173.85M
- **Hastra** (RWA) — $150.64M
- **Plume Vaults** (RWA) — $27.43M
- **Ondo Global Markets** (RWA) — $25.92M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.36M

## Daily active addresses

967,396 (Allium, as of 2026-09-10). Provider range 488,212–1,040,024. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [$DKNG is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2098504297323405375) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 20:09:47 GMT
- [DraftKings ($DKNG) operates a leading US sportsbook and gaming platform, live in over 25 states with millions of monthly players.

Verify the address on @tokens:
https://tokens.xyz/dkng?solana=DKNGQFNGQmoBdXSRGKJ8tTu7uPDasw5JDcfMmWniNfow](https://x.com/solana/status/2098504290998338029) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 20:09:45 GMT
- [Pinned: BREAKING: $DKNG is live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2098504287672267068) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 20:09:45 GMT
- [RT by @solana: collectibles are having a moment on solana.

join @taylorfox__ & @allocateur to talk consumer apps, collectibles & the @ripcarsio phenomenon.

september 15 · 12pm ET · live on spaces

hosted by @KittyKunt_ & @vesper792 for @MeteoraEco.

spaces link ⏬](https://x.com/MeteoraEco/status/2098481736623788127) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 18:40:08 GMT
- [RT by @solana: Yesterday total trades:

NASDAQ: 60,091,499
Solana: 32,460,600

Less than 2x to go 🤯](https://x.com/vibhu/status/2098446478951772539) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 16:20:02 GMT
- [Memes paired with stocks paired with memes](https://x.com/solana/status/2098474871542161916) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 18:12:51 GMT
- [The Privacy Show w/ @catmcgee https://x.com/i/broadcasts/1DxLdZRdXeRxm](https://x.com/solana/status/2098457925404795298) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 17:05:31 GMT
- [New episode of The Privacy Show today @ 1 PM ET.

@catmcgee sits down with @Jamie_Alethieum and @JonShapeShift to talk all things privacy.](https://x.com/solana/status/2098440785913946621) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 15:57:25 GMT
- [Step 2 of SIMD-0437 rent reduction is live.

How to reclaim excess SOL: https://x.com/a_milz/status/2095532192579661927?s=20](https://x.com/anza_xyz/status/2098519198783922184) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 21:09:00 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: 🚨JUST IN: The second wave of rent stimmy for @Solana users is on the way.

Rent reduction Step 2 goes live on mainnet in 7 hours, making another 612,000 $SOL reclaimable and bringing the total to 918,000 $SOL. 

Across all five steps, up to 3.06M $SOL ($319M) will become reclaimable.](https://x.com/SolanaFloor/status/2098406673874612536) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 13:41:52 GMT `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [$DKNG is available in your favorite Solana apps 

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2098504297323405375) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 20:09:47 GMT
- [DraftKings ($DKNG) operates a leading US sportsbook and gaming platform, live in over 25 states with millions of monthly players.

Verify the address on @tokens:
https://tokens.xyz/dkng?solana=DKNGQFNGQmoBdXSRGKJ8tTu7uPDasw5JDcfMmWniNfow](https://x.com/solana/status/2098504290998338029) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 20:09:45 GMT
- [Pinned: BREAKING: $DKNG is live on Solana via @sunrise, issued by @Backpack Securities](https://x.com/solana/status/2098504287672267068) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 20:09:45 GMT
- [RT by @solana: collectibles are having a moment on solana.

join @taylorfox__ & @allocateur to talk consumer apps, collectibles & the @ripcarsio phenomenon.

september 15 · 12pm ET · live on spaces

hosted by @KittyKunt_ & @vesper792 for @MeteoraEco.

spaces link ⏬](https://x.com/MeteoraEco/status/2098481736623788127) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 18:40:08 GMT
- [RT by @solana: Yesterday total trades:

NASDAQ: 60,091,499
Solana: 32,460,600

Less than 2x to go 🤯](https://x.com/vibhu/status/2098446478951772539) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 16:20:02 GMT
- [Memes paired with stocks paired with memes](https://x.com/solana/status/2098474871542161916) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 18:12:51 GMT
- [The Privacy Show w/ @catmcgee https://x.com/i/broadcasts/1DxLdZRdXeRxm](https://x.com/solana/status/2098457925404795298) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 17:05:31 GMT
- [New episode of The Privacy Show today @ 1 PM ET.

@catmcgee sits down with @Jamie_Alethieum and @JonShapeShift to talk all things privacy.](https://x.com/solana/status/2098440785913946621) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 15:57:25 GMT
- [Step 2 of SIMD-0437 rent reduction is live.

How to reclaim excess SOL: https://x.com/a_milz/status/2095532192579661927?s=20](https://x.com/anza_xyz/status/2098519198783922184) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 21:09:00 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: 🚨JUST IN: The second wave of rent stimmy for @Solana users is on the way.

Rent reduction Step 2 goes live on mainnet in 7 hours, making another 612,000 $SOL reclaimable and bringing the total to 918,000 $SOL. 

Across all five steps, up to 3.06M $SOL ($319M) will become reclaimable.](https://x.com/SolanaFloor/status/2098406673874612536) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 13:41:52 GMT `mainnet`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-11 (2026-09-11 14:22:43 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 800 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 60ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 35ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 32ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 82ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 36ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7070ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 67ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 74ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 59ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 41ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 29ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 41ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 42ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 72ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 139ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 85ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 136ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 574ms https://solana.com/data
- `solana.com.databricks` [ok] 200 61ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 474ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 144ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 31ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 53ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 233ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 333ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 72ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 93ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 75ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 295ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 202ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 4748ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 2145ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 95ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 30ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 70ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 380ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 436ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 435ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 401ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 351ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 437ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 34ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 483ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 480ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 444ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 509ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 353ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 442ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 321ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 447ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1431ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1420ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1551ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1367ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1257ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1059ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1252ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1124ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.COINx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.SPYx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.WRLDx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.INDIx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.WGSx` [ok] 200 547ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.XRXx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.circ.WRLDx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 827ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.WGSx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.price.FLNCx` [ok] 200 872ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.circ.INDIx` [ok] 200 506ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.PCTx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.mult.FLNCx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.XRXx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.WYFIx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.price.METCx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.QUBTx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.AIx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.QUBTx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.price.BETRx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.AIx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 1613ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.WYFIx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.WRLDx` [ok] 200 1324ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.DRSx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.price.SAILx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.mult.COINx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.SCIx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.mult.BETRx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.MPx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.circ.MPx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.price.BSYx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.price.DVAx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.circ.PCTx` [ok] 200 1176ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.mult.MPx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.price.GDDYx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.price.DCIx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.circ.GDDYx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.circ.DCIx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.mult.GDDYx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.circ.DVAx` [ok] 200 835ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.circ.SCIx` [ok] 200 1281ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.circ.DRSx` [ok] 200 1365ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.circ.SAILx` [ok] 200 1387ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.mult.DCIx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.price.GSATx` [ok] 200 1498ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.mult.SCIx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.circ.GSATx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.mult.GSATx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.mult.SAILx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.price.BXPx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.price.FRHCx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.price.WMSx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.mult.DVAx` [ok] 200 842ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.circ.FRHCx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.circ.BSYx` [ok] 200 1815ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 876ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.mult.BSYx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.price.FDSx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.mult.FRHCx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.price.AMx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.WMSx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.price.DYx` [ok] 200 1047ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.price.ALSNx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.circ.FDSx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.mult.WMSx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.circ.ALSNx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.price.SMTCx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.mult.FDSx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.price.SFx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.circ.BXPx` [ok] 200 951ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.circ.SFx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.mult.BXPx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.BPOPx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.mult.SFx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.price.AXSMx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.circ.RYANx` [ok] 200 1632ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.circ.SMTCx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.circ.BPOPx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.circ.AXSMx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.price.TTMIx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.mult.RYANx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.price.EGPx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.mult.SMTCx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.circ.TTMIx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.BPOPx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.mult.AXSMx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.mult.TTMIx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.HRLx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.circ.DYx` [ok] 200 1238ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.price.DPZx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.price.KTOSx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.price.PAGx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.circ.AMx` [ok] 200 1474ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.circ.KTOSx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.price.AEISx` [ok] 200 738ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.price.SEICx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.circ.AEISx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.mult.KTOSx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.mult.AMx` [ok] 200 586ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.price.HIIx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.mult.AEISx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.circ.HRLx` [ok] 200 990ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.circ.DPZx` [ok] 200 988ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.price.GFLx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.price.EHCx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.circ.PAGx` [ok] 200 1100ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.circ.GFLx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.DPZx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.mult.PAGx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.mult.HRLx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.circ.EGPx` [ok] 200 1824ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.price.DOCUx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.mult.EGPx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.circ.SEICx` [ok] 200 1258ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.mult.GFLx` [ok] 200 698ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.price.ARx` [ok] 200 693ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.mult.SEICx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.price.MGMx` [ok] 200 616ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.price.AFGx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.price.HALOx` [ok] 200 633ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.circ.EHCx` [ok] 200 1221ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.price.WTRGx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.circ.HIIx` [ok] 200 1506ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.circ.AFGx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.mult.HIIx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.mult.EHCx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.circ.DOCUx` [ok] 200 1296ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.price.HUBSx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.circ.MGMx` [ok] 200 931ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.mult.DOCUx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.mult.AFGx` [ok] 200 589ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.circ.ARx` [ok] 200 1035ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.mult.MGMx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.price.GMEDx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.price.JKHYx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.ARx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.price.IESCx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.circ.JKHYx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.price.OCx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.circ.IESCx` [ok] 200 111ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.mult.JKHYx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.circ.WTRGx` [ok] 200 1119ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 427ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.price.CRx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.mult.IESCx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.circ.OCx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.mult.GMEDx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.price.JEFx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.mult.OCx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.circ.JEFx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.price.FIVEx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.circ.FIVEx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.price.BMRNx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.circ.CRx` [ok] 200 519ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.price.AMKRx` [ok] 200 1473ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.mult.FIVEx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.mult.CRx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.circ.BMRNx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.price.ITx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.circ.HUBSx` [ok] 200 1668ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.price.AMHx` [ok] 200 855ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.HALOx` [ok] 200 2277ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.mult.JEFx` [ok] 200 823ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.price.MDGLx` [ok] 200 556ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.mult.HALOx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.price.VNOMx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.circ.VNOMx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.price.UHALx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.circ.AMKRx` [ok] 200 1005ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.circ.MDGLx` [ok] 200 536ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.mult.AMKRx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.mult.BMRNx` [ok] 200 977ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.circ.ITx` [ok] 200 911ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.price.IVZx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.price.AHRx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.mult.HUBSx` [ok] 200 1096ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.mult.VNOMx` [ok] 200 702ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.circ.IVZx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.price.CORTx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.price.STRLx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.mult.IVZx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.mult.MDGLx` [ok] 200 610ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.price.NWSAx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.circ.CORTx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.price.AURx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.circ.NWSAx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.circ.AHRx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.circ.AMHx` [ok] 200 1578ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.circ.AURx` [ok] 200 109ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.mult.ITx` [ok] 200 836ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.AHRx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.circ.UHALx` [ok] 200 1310ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.mult.CORTx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.Hx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.price.ARWRx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.mult.NWSAx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.mult.UHALx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.circ.Hx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.price.GWREx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.circ.STRLx` [ok] 200 828ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.circ.ARWRx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.price.MANHx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.price.NWSx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.mult.Hx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.STRLx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.mult.AURx` [ok] 200 668ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.mult.AMHx` [ok] 200 709ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.price.BAXx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.mult.ARWRx` [ok] 200 431ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.price.CACIx` [ok] 200 725ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.circ.GWREx` [ok] 200 964ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.circ.MANHx` [ok] 200 1021ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.circ.BAXx` [ok] 200 948ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.circ.CACIx` [ok] 200 1039ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1574ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 159ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INDIx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 44ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 50ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.FLNCx` [ok] 200 47ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.BETRx` [ok] 200 69ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.XRXx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.PCTx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.WGSx` [ok] 200 56ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jito.tip_floor` [ok] 200 371ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 365ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 51ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 76ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 34ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 113ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 41ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 149ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
