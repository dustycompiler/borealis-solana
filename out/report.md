# Borealis — Solana ecosystem report

**Generated** 2026-08-26T10:08:35Z · 2026-08-26 03:08:35 PT
**Author** dustycompiler · **Version** 1.5.3 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-26T10:08:23Z · **RPC health** `ok`
**Health score** 95 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 400)/400, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -3.60%; DEX 24h $2.95B · 1d -2% · vs-7d-ago +60%; slot 364 ms
Updates every 15 min via GitHub Action.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +48.46%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -10.11%. (threshold: `|1d %| >= 8`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -3.60%, DeFiLlama TVL 1d -2.40%, DEX 1d -1.58%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **INFO · Daily active addresses vs 30d median** — Current 794,650.00 is +24.5% vs 30d median 638,326.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +60.42%. (threshold: `|7d %| >= 20`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 96.11 USD is +27.3% vs 30d median 75.47 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 441,843,930 |
| Block height | 419,892,454 |
| Block time | 2026-08-26T10:08:23Z |
| Epoch | 1,022 (78.69% · slot 339,933/432,000) |
| Mean TPS (last ~3,600s) | 3,514.2 |
| Mean non-vote TPS | 1,640.6 |
| Median TPS (same window) | 3,490.7 |
| Mean slot time | 364.2 ms |
| Median slot time | 365.9 ms |
| Transaction count (cluster) | 541,992,632,884 |
| Circulating supply | 583,375,229 SOL |
| Total supply | 632,859,090 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 683 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 433,634,445 SOL |
| Delinquent stake | 1,483,659.17 SOL (0.341%) |
| Nakamoto (33% / 50% / 67%) | 18 / 40 / 78 |
| Top 10 / 20 stake share | 24.36% / 35.74% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.07M SOL | 3.94% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.04M SOL | 3.70% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.27M SOL | 2.83% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.74M SOL | 2.71% | 5% | 0 |
| 5 | `C8Bey3LK…` | 9.20M SOL | 2.12% | 7% | 0 |
| 6 | `CAo1dCGY…` | 8.92M SOL | 2.06% | 10% | 0 |
| 7 | `E1r4Psq8…` | 8.58M SOL | 1.98% | 0% | 0 |
| 8 | `EvnRmnMr…` | 7.95M SOL | 1.83% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.30M SOL | 1.68% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.57M SOL | 1.52% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.41% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.02M SOL | 1.39% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.93M SOL | 1.37% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.67M SOL | 1.31% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `BXAxLMMM…` · 819.32K SOL · commission 2% · lag 2201 slots
- `EfPYQ4BU…` · 338.00K SOL · commission 8% · lag 2395 slots
- `BGAjnivV…` · 226.29K SOL · commission 1% · lag 603 slots
- `2bpfa8Jb…` · 29.73K SOL · commission 5% · lag 1203931 slots
- `mrgn4atx…` · 26.11K SOL · commission 0% · lag 78701 slots
- `5P35CJVK…` · 24.00K SOL · commission 100% · lag 1203931 slots
- `gangtCrQ…` · 16.66K SOL · commission 0% · lag 591251 slots
- `kom1oNHy…` · 2.19K SOL · commission 5% · lag 1207414 slots
- `4GEEKSwu…` · 1.35K SOL · commission 5% · lag 831564 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 441843930 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 123259 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 1203931 slots

## Trends

15-min Borealis tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 25 | data/history.jsonl 15-min tape |
| TVL chart | 25 | data/history.jsonl 15-min tape |
| SOL chart | 24 | data/history.jsonl 15-min tape |
| history.jsonl rows | 25 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$881.73K** (9,174.2 SOL) | solana.com/data Fees (Allium) MEASURED |
| **Solana REV** | **11,440.0 SOL** / **$1.12M** | MEASURED UTC calendar day 2026-08-25: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-25 · UTC day 2026-08-25 · SOL-USD date 2026-08-25 |
| Jito tip-floor run-rate (NOT REV) | $50.95K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 50952 USD; at p95 floor → 8760708 USD. |
| Protocol fees 24h | $13.03M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9972 |
| p90 / p99 | 0.000010 / 0.000105 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $96.11 | coingecko.simple_price |
| 24h change | -3.60% | coingecko.simple_price |
| Market cap | $56.05B | coingecko.simple_price |
| 24h volume | $3.47B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.60B |
| TVL 1d / 7d / 30d | -2.40% / +14.36% / +13.79% |
| DEX volume 24h | $2.95B · 1d -1.58% · vs-7d-ago +60.42% |
| 7d DEX volume | $21.60B · +100.14% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $13.03M |
| Fees 1d / 7d | -10.11% / +48.46% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $567.89M | -18.27% |
| BisonFi | $411.40M | +0.55% |
| Orca DEX | $307.24M | -29.47% |
| Meteora DLMM | $246.36M | -11.40% |
| Scorch | $218.92M | 0.00% |
| Raydium AMM | $158.37M | -13.74% |
| Manifest Trade | $140.32M | -20.00% |
| pump.fun | $112.18M | +17.58% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.48B | -3.60% | +28.48% |
| Kamino Lend | Lending | $1.18B | -4.22% | +10.53% |
| Raydium AMM | Dexs | $1.06B | -3.81% | +24.48% |
| Jupiter Lend | Lending | $1.06B | -3.69% | +10.84% |
| Binance Staked SOL | Liquid Staking | $996.04M | -3.71% | +28.35% |
| Jito Liquid Staking | Liquid Staking | $974.41M | -4.32% | +26.79% |
| BlackRock BUIDL | RWA | $876.38M | +4.14% | +1.16% |
| Jupiter Perpetual Exchange | Derivatives | $750.10M | -3.20% | +9.28% |
| Jupiter Staked SOL | Liquid Staking | $503.23M | -4.33% | +26.33% |
| xStocks | RWA | $429.19M | +0.55% | +12.80% |

## Stablecoins

Solana circulating pegged-USD: **$15.86B**
(1d -0.69% · 7d +1.86%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.06B | -1.52% |
| USDT · Tether | $2.84B | -0.00% |
| USDGO · USDGO | $1.24B | +3.77% |
| USD1 · World Liberty Financial USD | $1.11B | +1.70% |
| BUIDL · BlackRock USD | $876.38M | +5.75% |
| PYUSD · PayPal USD | $687.99M | +1.92% |
| USDG · Global Dollar | $616.53M | -2.83% |
| USDe · Ethena USDe | $537.06M | +0.07% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 80 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 80 · priced-subset mcap $277.93M (lower bound, not a census).
24h volume $21.91M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $429.19M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 80 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.06B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $876.38M
- **xStocks** (RWA) — $429.19M
- **OnRe** (RWA) — $277.42M
- **Ondo Yield Assets** (RWA) — $179.28M
- **Hastra** (RWA) — $162.66M
- **Theo Network thBill** (RWA) — $26.39M
- **Ondo Global Markets** (RWA) — $24.81M
- **Plume Vaults** (RWA) — $22.70M

## Daily active addresses

794,650 (Allium, as of 2026-08-25). Provider range 389,101–854,284. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: Janamat has now crossed 10,000 users🇳🇵

We're building Nepal's governance infrastructure on @Solana.

If you're a Nepali, your voice deserves to be heard.

Still day 1.](https://x.com/janamatnp/status/2092525575999303959) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 26 Aug 2026 08:12:29 GMT
- [Pinned: Demos, talks, and special appearances 👀

Watch Solana Summit Serbia @SuperteamBLKN  from home
https://x.com/i/broadcasts/1qxvveWBlOqxB](https://x.com/solana/status/2092533152275202224) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 26 Aug 2026 08:42:35 GMT
- [gm](https://x.com/solana/status/2092529144378917213) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 26 Aug 2026 08:26:39 GMT
- [RT by @solana: Memecoins paired with anything.

Memes have traditionally been paired with $SOL, meaning you would trade coins directly against Solana.

Now, there’s a new way to launch & trade anything.

You can launch coins paired with a broad list of custom quote assets, such as RWAs, commodities, currencies, memes, and more to come.

Get airdropped rewards for holding coins while trading against anything.

http://stonkfun.xyz

Powered by @Raydium](https://x.com/LaunchOnSF/status/2092432236389806146) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 26 Aug 2026 02:01:35 GMT
- [chat, are we back](https://x.com/solana/status/2092414366180151641) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 26 Aug 2026 00:50:34 GMT
- [RT by @solana: Home of the only interesting interviews happening on Solana.

@blknoiz06 and @Banks, fully unboxed.

Thursday 2pm UTC 👇](https://x.com/EcosystemCall/status/2092366326329168044) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 21:39:41 GMT
- [BREAKING: Solana ETF cumulative inflows hit a record $1.22B. $33.5M came in Monday alone.

The biggest single day of 2026, capping five straight days of inflows.](https://x.com/solana/status/2092333691338887672) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 19:30:00 GMT
- [RT by @solana: The king is in town.  

Earn 3.5-5% on top of your BTC holdings. 

Introducing BTC*, a token giving you market exposure while compounding.  

Powered by Kestrel, managed by Perena.](https://x.com/perena/status/2092315290323333197) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 18:16:53 GMT
- [RT by @anza_xyz: 300ms now pending on Solana mainnet 👀
effective start of epoch 1024 (~3 days)](https://x.com/bw_solana/status/2092259551659831608) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 25 Aug 2026 14:35:24 GMT `mainnet`
- [We're aware of today's arrayref crate supply-chain attack: https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/

Agave and Anza's software are not affected.

If you ran cargo update today, check your machine against indicators in the writeup. Stay safe out there.](https://x.com/anza_xyz/status/2090608013891813501) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 21 Aug 2026 01:12:46 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: Janamat has now crossed 10,000 users🇳🇵

We're building Nepal's governance infrastructure on @Solana.

If you're a Nepali, your voice deserves to be heard.

Still day 1.](https://x.com/janamatnp/status/2092525575999303959) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 26 Aug 2026 08:12:29 GMT
- [Pinned: Demos, talks, and special appearances 👀

Watch Solana Summit Serbia @SuperteamBLKN  from home
https://x.com/i/broadcasts/1qxvveWBlOqxB](https://x.com/solana/status/2092533152275202224) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 26 Aug 2026 08:42:35 GMT
- [gm](https://x.com/solana/status/2092529144378917213) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 26 Aug 2026 08:26:39 GMT
- [RT by @solana: Memecoins paired with anything.

Memes have traditionally been paired with $SOL, meaning you would trade coins directly against Solana.

Now, there’s a new way to launch & trade anything.

You can launch coins paired with a broad list of custom quote assets, such as RWAs, commodities, currencies, memes, and more to come.

Get airdropped rewards for holding coins while trading against anything.

http://stonkfun.xyz

Powered by @Raydium](https://x.com/LaunchOnSF/status/2092432236389806146) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 26 Aug 2026 02:01:35 GMT
- [chat, are we back](https://x.com/solana/status/2092414366180151641) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 26 Aug 2026 00:50:34 GMT
- [RT by @solana: Home of the only interesting interviews happening on Solana.

@blknoiz06 and @Banks, fully unboxed.

Thursday 2pm UTC 👇](https://x.com/EcosystemCall/status/2092366326329168044) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 21:39:41 GMT
- [BREAKING: Solana ETF cumulative inflows hit a record $1.22B. $33.5M came in Monday alone.

The biggest single day of 2026, capping five straight days of inflows.](https://x.com/solana/status/2092333691338887672) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 19:30:00 GMT
- [RT by @solana: The king is in town.  

Earn 3.5-5% on top of your BTC holdings. 

Introducing BTC*, a token giving you market exposure while compounding.  

Powered by Kestrel, managed by Perena.](https://x.com/perena/status/2092315290323333197) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 25 Aug 2026 18:16:53 GMT
- [RT by @anza_xyz: 300ms now pending on Solana mainnet 👀
effective start of epoch 1024 (~3 days)](https://x.com/bw_solana/status/2092259551659831608) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 25 Aug 2026 14:35:24 GMT `mainnet`
- [We're aware of today's arrayref crate supply-chain attack: https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/

Agave and Anza's software are not affected.

If you ran cargo update today, check your machine against indicators in the writeup. Stay safe out there.](https://x.com/anza_xyz/status/2090608013891813501) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 21 Aug 2026 01:12:46 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-26 (2026-08-26 03:08:35 PT). Editorial. Listing token SIMD-525 cites solana.com/news “Lowering Slot Time and Validators Economic”. Observed slot time is INFERRED corroboration, not a feature-gate RPC. Activation dates move. None of this is a live consensus metric._

Primary source for the listing token SIMD-525: solana.com/news “Lowering Slot Time and Validators Economic” (SIMD-0525 staged 400→350→300→250→200 ms). Observed mean slot ~364 ms is corroboration, labeled inferred — not a feature-gate RPC. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

_Listing token SIMD-525 is SIMD-0525. Not SIMD-025._

- **SIMD-525** — Reduce Slot Times (400→350→300→250→200 ms)
- **SIMD-0326** — Alpenglow Consensus Protocol (Votor)
- **SIMD-0337** — Markers for Alpenglow Fast Leader Handover
- **SIMD-0357** — Alpenglow Validator Admission Ticket (VAT)
- **SIMD-0384** — Alpenglow Migration
- **SIMD-0387** — BLS Pubkey Management in Vote Account

### Public timeline (editorial)

- `source` — solana.com/news “Lowering Slot Time and Validators Economic” is the primary public write-up for the SIMD-525 listing token (SIMD-0525).
- `2026-05-01` — SIMD-0525 created (Anza). Four feature gates: 350/300/250/200 ms.
- `2026-Q3` — Agave v4.2 schedule targeted the four SIMD-0525 steps on mainnet one epoch apart; schedule is tentative. First step is 400→350 ms.
- `observed` — Observed mean slot 364 ms is consistent with the 350 ms SIMD-0525 target (staged 400→350→300→250→200). INFERRED corroboration, not a feature-gate RPC.
- `2026-07-08` — SIMD-0387 (BLS pubkey in vote account) activated on mainnet.
- `2026-07-22` — SIMD-0357 VAT activated. VAT does not itself turn on Alpenglow consensus.

### What to watch

- Whether observed slot time stays near the inferred SIMD-0525 target after the next epoch.
- Skip rate / skipped slots as later 50 ms steps (300/250/200) are considered.
- Agave 4.2 / 4.3 stake rollout vs the published (tentative) schedule.
- Firedancer / Frankendancer Votor parity before a full Alpenswitch.

- https://solana.com/news/lowering-slot-time-and-validators-economic
- https://solana.com/upgrades/reduced-slot-times
- https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0525-reduce-slot-times.md
- https://solana.com/upgrades/alpenglow
- https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0326-alpenglow.md

## Omissions

- **xStocks** — priced up to 80 of 715 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 551ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 512ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 533ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 482ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 482ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 8628ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 999ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 109ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 74ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 114ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 848ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 2389ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 41ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 105ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 104ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 63ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 110ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 558ms https://solana.com/data
- `solana.com.databricks` [ok] 200 101ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 260ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 214ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 204ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 75ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 437ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 821ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 443ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 443ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 444ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1152ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1793ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1657ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1889ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 585ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 494ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 472ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2205ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2284ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1869ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2064ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2646ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL]  2314ms https://api.mainnet-beta.solana.com — URLError: <urlopen error [Errno 111] Connection refused>
- `rpc.getBlock.fallback` [ok] 200 977ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 2058ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2032ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2020ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2053ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1763ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2087ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2484ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2059ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1969ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1849ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1172ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1877ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1778ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1214ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1773ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 619ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.GOOGLx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.AAPLx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.AMZNx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.TSLAx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.NVDAx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.SPYx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.METAx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.MSFTx` [ok] 200 578ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.mult.GOOGLx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.AAPLx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.TSLAx` [ok] 200 840ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 636ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 893ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 532ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.SPYx` [ok] 200 758ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 592ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 507ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.COINx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.TNGYIx` [ok] 200 537ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.price.BANKCx` [ok] 200 858ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.MMGx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 1116ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 787ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.BANKCx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.SUOPTx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 658ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.MMGx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 747ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.KUNLx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.CTINSx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.SZIGHx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 666ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.KUNLx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 860ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 1147ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 752ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 754ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.SMOIHx` [ok] 200 799ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.CSPCx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 622ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 529ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 885ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 549ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.CRESBx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.CMERPx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.MIXUx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.CMENDx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.price.SITCx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.mult.MIXUx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.SITCx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 925ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.JDHLTx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.CRESPx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.SNDSCx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 1084ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 454ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.WHRFRx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.PRADx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 1075ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 651ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.PWAHLx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.SINOTx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 738ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.GENTEx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.CTPCAx` [ok] 200 682ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 387ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 869ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.HKCGAx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.mult.CTFJWx` [ok] 200 1307ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.price.COVELx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.CKAHx` [ok] 200 834ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 727ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.NONGx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.CHONGx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.COVELx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 754ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.CHONGx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.MEITx` [ok] 200 692ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.GEELx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 732ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.GEELx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 810ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.HNDLDx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.POPMTx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.mult.HNDLDx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 865ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.BOCOMx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.price.CPETCx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.circ.POPMTx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 629ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.CPETCx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.circ.BOCOMx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.price.BOCHKx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.circ.COSCx` [ok] 200 615ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.POPMTx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.price.CITICx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.mult.PICCx` [ok] 200 878ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.BOCHKx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.mult.BOCOMx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.circ.CITICx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.mult.BOCHKx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.price.ANTASx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.price.ZJGLDx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.mult.CITICx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.price.PSBOCx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.circ.ANTASx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.circ.ZJGLDx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.price.HAIERx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.mult.ANTASx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.circ.HAIERx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.price.CRESLx` [ok] 200 840ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.mult.COSCx` [ok] 200 1033ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.price.ICBCx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.circ.CRESLx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.mult.HAIERx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.circ.PSBOCx` [ok] 200 571ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.mult.ZJGLDx` [ok] 200 611ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.mult.PSBOCx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `xstocks.circ.ICBCx` [ok] 200 623ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.mult.CRESLx` [ok] 200 578ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.mult.ICBCx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `xstocks.mult.CPETCx` [ok] 200 1989ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1683ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 350ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 117ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 152ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 129ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.KUAIx` [ok] 200 124ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.MIXUx` [ok] 200 115ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.BANKCx` [ok] 200 113ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.HAIDLx` [ok] 200 114ms https://lite-api.jup.ag/tokens/v2/search?query=HAIDLx
- `jup.tokens.search.KUNLx` [ok] 200 115ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jito.tip_floor` [ok] 200 309ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 426ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 183ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `jito.daily_mev_rewards` [ok] 200 182ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.3 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
