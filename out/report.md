# Borealis — Solana ecosystem report

**Generated** 2026-09-11T21:34:30Z · 2026-09-11 14:34:30 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-11T21:34:20Z · **RPC health** `ok`
**Health score** 89 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +2.85%; DEX 24h $2.92B · 1d -3% · vs-7d-ago +19%; slot 317 ms
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
| Slot | 446,260,198 |
| Block height | 424,303,200 |
| Block time | 2026-09-11T21:34:20Z |
| Epoch | 1,033 (0.97% · slot 4,200/432,000) |
| Mean TPS (last ~3,600s) | 4,437.4 |
| Mean non-vote TPS | 2,320.0 |
| Median TPS (same window) | 4,487.8 |
| Mean slot time | 317.4 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 547,518,347,412 |
| Circulating supply | 586,623,416 SOL |
| Total supply | 633,924,703 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 14 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 433,575,779 SOL |
| Delinquent stake | 3,261,901.53 SOL (0.747%) |
| Nakamoto (33% / 50% / 67%) | 18 / 40 / 78 |
| Top 10 / 20 stake share | 24.58% / 35.99% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.56M SOL | 4.05% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.36M SOL | 3.77% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.52M SOL | 2.89% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.37M SOL | 2.62% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.67M SOL | 2.23% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.23M SOL | 2.13% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.02M SOL | 2.08% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.36M SOL | 1.70% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.94M SOL | 1.60% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.55M SOL | 1.51% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.13M SOL | 1.41% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.12M SOL | 1.41% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.38% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.62M SOL | 1.30% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `pSo1KZXg…` · 1.64M SOL · commission 4% · lag 4171 slots
- `HSDTxfgr…` · 1.27M SOL · commission 5% · lag 1602 slots
- `BoNKmNCG…` · 290.50K SOL · commission 0% · lag 1495 slots
- `EWARp8Sy…` · 31.93K SOL · commission 5% · lag 2707 slots
- `mrgn4atx…` · 19.58K SOL · commission 0% · lag 4171 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 4171 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 4171 slots
- `4GEEKSwu…` · 326.50 SOL · commission 5% · lag 450586 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 561101 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 446260198 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 62211328 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 4171 slots

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
| Jito tip-floor run-rate (NOT REV) | $108.28K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 108285 USD; at p95 floor → 1029423 USD. |
| Protocol fees 24h | $14.61M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9957 |
| p90 / p99 | 0.000015 / 0.000410 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $102.79 | coingecko.simple_price |
| 24h change | +2.85% | coingecko.simple_price |
| Market cap | $60.34B | coingecko.simple_price |
| 24h volume | $4.58B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.87B |
| TVL 1d / 7d / 30d | +0.21% / -1.06% / +20.39% |
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

Solana circulating pegged-USD: **$16.13B**
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
Listed 800 · Solana deployments 800 · priced 14 · priced-subset mcap $107.15M (lower bound, not a census).
24h volume $121.15M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
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

_As of 2026-09-11 (2026-09-11 14:34:30 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 299ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 276ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 391ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 279ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 284ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6145ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 541ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 170ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 131ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 72ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 41ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 1171ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 3209ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 112ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 133ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 88ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 104ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 370ms https://solana.com/data
- `solana.com.databricks` [ok] 200 129ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 458ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 145ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 136ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 78ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 361ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 839ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 543ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 714ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 1080ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 931ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 440ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2050ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1346ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 265ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 236ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 235ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1142ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1078ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1201ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1465ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1428ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1245ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1140ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1485ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1382ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1082ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1088ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1166ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1341ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1420ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2227ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2095ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1786ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 3079ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2034ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1797ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1259ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1835ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.INDIx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.price.SPYx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.QQQx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.COINx` [ok] 200 529ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.WRLDx` [ok] 200 578ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.price.FLNCx` [ok] 200 610ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.XRXx` [ok] 200 668ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.price.WGSx` [ok] 200 691ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.circ.QQQx` [ok] 200 496ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 543ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 497ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.PCTx` [ok] 200 638ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.INDIx` [ok] 200 1540ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.price.METCx` [ok] 200 607ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.mult.INDIx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.price.QUBTx` [ok] 200 768ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.circ.XRXx` [ok] 200 1352ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 1524ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.price.WYFIx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.WGSx` [ok] 200 1521ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.circ.WRLDx` [ok] 200 1780ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.WYFIx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.AIx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.price.DRSx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data
- `xstocks.mult.WRLDx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.price.SCIx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data
- `xstocks.circ.AIx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.DRSx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 1198ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.SCIx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.mult.BETRx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 1319ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.price.SAILx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data
- `xstocks.mult.METCx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.DRSx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.GSATx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data
- `xstocks.price.BSYx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data
- `xstocks.mult.PCTx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 639ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.circ.SAILx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.circ.GSATx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.price.MPx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.circ.BSYx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.price.DCIx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data
- `xstocks.mult.SCIx` [ok] 200 599ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.DVAx` [ok] 200 411ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data
- `xstocks.price.GDDYx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data
- `xstocks.mult.BSYx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.circ.DCIx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.mult.GSATx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.circ.DVAx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.mult.SAILx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.price.BXPx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data
- `xstocks.circ.GDDYx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.mult.DVAx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.mult.DCIx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.price.FRHCx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data
- `xstocks.circ.RYANx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.price.DYx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.mult.GDDYx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.price.AMx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.BXPx` [ok] 200 544ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.mult.RYANx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.price.WMSx` [ok] 200 516ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data
- `xstocks.circ.AMx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.price.FDSx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data
- `xstocks.circ.DYx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.mult.BXPx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.circ.MPx` [ok] 200 1487ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.mult.DYx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.mult.AMx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.price.ALSNx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data
- `xstocks.circ.FRHCx` [ok] 200 1146ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.price.SFx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.circ.ALSNx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.price.SMTCx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data
- `xstocks.mult.MPx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.price.AXSMx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data
- `xstocks.mult.ALSNx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.mult.FRHCx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.price.EGPx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data
- `xstocks.circ.AXSMx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.price.BPOPx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data
- `xstocks.circ.FDSx` [ok] 200 1158ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.price.TTMIx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data
- `xstocks.circ.BPOPx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.mult.AXSMx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.circ.WMSx` [ok] 200 1514ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.price.AEISx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data
- `xstocks.circ.SFx` [ok] 200 1105ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.mult.BPOPx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.mult.WMSx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.DPZx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data
- `xstocks.circ.AEISx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.price.HRLx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data
- `xstocks.mult.SFx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.circ.DPZx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.circ.HRLx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.circ.EGPx` [ok] 200 1168ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.circ.SMTCx` [ok] 200 1452ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.mult.DPZx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.price.PAGx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.mult.HRLx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.KTOSx` [ok] 200 648ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data
- `xstocks.mult.AEISx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.circ.TTMIx` [ok] 200 1147ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.SMTCx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.mult.EGPx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.price.SEICx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data
- `xstocks.circ.PAGx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.price.HIIx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.price.GFLx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.circ.SEICx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.price.ARx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/ARx/price-data
- `xstocks.price.EHCx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data
- `xstocks.mult.TTMIx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.mult.SEICx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.circ.EHCx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.circ.ARx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.circ.KTOSx` [ok] 200 610ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.circ.GFLx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.PAGx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.price.MGMx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data
- `xstocks.mult.HIIx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.price.DOCUx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data
- `xstocks.mult.EHCx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.price.HALOx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data
- `xstocks.mult.GFLx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.mult.KTOSx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.circ.MGMx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.price.AFGx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data
- `xstocks.circ.DOCUx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.mult.ARx` [ok] 200 406ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.price.WTRGx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data
- `xstocks.price.AMKRx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data
- `xstocks.price.HUBSx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data
- `xstocks.mult.MGMx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.circ.AFGx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.price.GMEDx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data
- `xstocks.circ.WTRGx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.circ.HUBSx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.price.JKHYx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data
- `xstocks.mult.DOCUx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.circ.GMEDx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.mult.AFGx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.circ.AMKRx` [ok] 200 547ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.price.IESCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data
- `xstocks.mult.GMEDx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.mult.HUBSx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.mult.AMKRx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.circ.HALOx` [ok] 200 1047ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.circ.IESCx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.price.OCx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/OCx/price-data
- `xstocks.price.CRx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.price.JEFx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data
- `xstocks.price.BMRNx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data
- `xstocks.mult.HALOx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.mult.WTRGx` [ok] 200 926ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.circ.BMRNx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.circ.JEFx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.price.FIVEx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data
- `xstocks.circ.CRx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.mult.BMRNx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.mult.IESCx` [ok] 200 632ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.mult.JEFx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.price.ITx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/ITx/price-data
- `xstocks.mult.CRx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.circ.JKHYx` [ok] 200 1457ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.price.UHALx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data
- `xstocks.price.AMHx` [ok] 200 884ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data
- `xstocks.circ.ITx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.circ.OCx` [ok] 200 1105ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.price.VNOMx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data
- `xstocks.price.MDGLx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data
- `xstocks.circ.UHALx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.circ.AMHx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.mult.ITx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.mult.OCx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.mult.JKHYx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.circ.VNOMx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.mult.UHALx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.price.CORTx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data
- `xstocks.mult.VNOMx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.price.IVZx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.circ.FIVEx` [ok] 200 1273ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.price.STRLx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data
- `xstocks.circ.CORTx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.price.AHRx` [ok] 200 596ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data
- `xstocks.price.NWSAx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data
- `xstocks.circ.STRLx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.circ.IVZx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.circ.NWSAx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.mult.STRLx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.mult.CORTx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.AURx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/AURx/price-data
- `xstocks.mult.NWSAx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.mult.AMHx` [ok] 200 1187ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.price.Hx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/Hx/price-data
- `xstocks.mult.IVZx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.circ.AURx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.price.GWREx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.circ.Hx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.price.ARWRx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data
- `xstocks.price.NWSx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data
- `xstocks.mult.Hx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.circ.GWREx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.mult.AURx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.mult.GWREx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.circ.AHRx` [ok] 200 1397ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.circ.MDGLx` [ok] 200 2199ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.price.BAXx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.price.CACIx` [ok] 200 406ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.mult.AHRx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.MANHx` [ok] 200 776ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data
- `xstocks.mult.MDGLx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.circ.BAXx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.circ.CACIx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.circ.MANHx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.circ.ARWRx` [ok] 200 1215ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.mult.FIVEx` [ok] 200 2118ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.mult.CACIx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.circ.NWSx` [ok] 200 1291ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `xstocks.mult.BAXx` [ok] 200 1016ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.mult.ARWRx` [ok] 200 836ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.mult.NWSx` [ok] 200 743ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 59ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 247ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INDIx` [ok] 200 124ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.QUBTx` [ok] 200 117ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.WRLDx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.FLNCx` [ok] 200 115ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.BETRx` [ok] 200 126ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jup.tokens.search.XRXx` [ok] 200 115ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.PCTx` [ok] 200 118ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.WGSx` [ok] 200 116ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jito.tip_floor` [ok] 200 442ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 301ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 146ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 236ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 245ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 266ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 236ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 449ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
