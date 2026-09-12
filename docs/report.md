# Borealis — Solana ecosystem report

**Generated** 2026-09-12T06:44:00Z · 2026-09-11 23:44:00 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-12T06:43:49Z · **RPC health** `ok`
**Health score** 89 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h +2.08%; DEX 24h $3.25B · 1d +11% · vs-7d-ago +73%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +19.78%. (threshold: `|1d %| >= 8`)
- **ALERT · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +67.66%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 967,396.00 is +21.7% vs 30d median 794,650.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +11.15%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +72.60%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 446,364,235 |
| Block height | 424,407,056 |
| Block time | 2026-09-12T06:43:49Z |
| Epoch | 1,033 (25.05% · slot 108,236/432,000) |
| Mean TPS (last ~3,600s) | 3,362.3 |
| Mean non-vote TPS | 1,243.8 |
| Median TPS (same window) | 3,346.4 |
| Mean slot time | 317.2 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 547,644,423,119 |
| Circulating supply | 586,633,093 SOL |
| Total supply | 633,924,368 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 672 |
| Delinquent | 17 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 434,536,905 SOL |
| Delinquent stake | 2,300,775.33 SOL (0.527%) |
| Nakamoto (33% / 50% / 67%) | 18 / 40 / 78 |
| Top 10 / 20 stake share | 24.53% / 35.91% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.56M SOL | 4.04% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.36M SOL | 3.76% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.52M SOL | 2.88% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.37M SOL | 2.62% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.67M SOL | 2.22% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.23M SOL | 2.13% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.02M SOL | 2.08% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.36M SOL | 1.69% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.94M SOL | 1.60% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.55M SOL | 1.51% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.13M SOL | 1.41% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.12M SOL | 1.41% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.37% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.62M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `pSo1KZXg…` · 1.64M SOL · commission 4% · lag 108208 slots
- `4vcmYPfL…` · 194.31K SOL · commission 5% · lag 835 slots
- `forb5u56…` · 158.43K SOL · commission 5% · lag 2408 slots
- `3Pfubj3y…` · 95.90K SOL · commission 0% · lag 1533 slots
- `Mwz8VgAE…` · 91.09K SOL · commission 0% · lag 3703 slots
- `9bkyxgYx…` · 60.76K SOL · commission 0% · lag 197 slots
- `EWARp8Sy…` · 31.93K SOL · commission 5% · lag 71940 slots
- `mrgn4atx…` · 19.58K SOL · commission 0% · lag 108208 slots
- `AYY1TCe3…` · 10.81K SOL · commission 0% · lag 108208 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 108208 slots
- `4GEEKSwu…` · 326.50 SOL · commission 5% · lag 554623 slots
- `inWVrrYJ…` · 14.05 SOL · commission 0% · lag 665138 slots

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
| **In-protocol fees 24h** | **$714.96K** (7,191.9 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-10 |
| **Solana REV** | **8,405.9 SOL** / **$835.65K** | MEASURED UTC calendar day 2026-09-10: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-10 · UTC day 2026-09-10 · SOL-USD date 2026-09-10 |
| Jito tip-floor run-rate (NOT REV) | $14.70K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 14700 USD; at p95 floor → 65577 USD. |
| Protocol fees 24h | $17.51M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9961 |
| p90 / p99 | 0.000010 / 0.000118 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $101.70 | coingecko.simple_price |
| 24h change | +2.08% | coingecko.simple_price |
| Market cap | $59.64B | coingecko.simple_price |
| 24h volume | $4.49B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.89B |
| TVL 1d / 7d / 30d | +2.41% / +0.31% / +21.83% |
| DEX volume 24h | $3.25B · 1d +11.15% · vs-7d-ago +72.60% |
| 7d DEX volume | $17.98B · +20.65% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $17.51M |
| Fees 1d / 7d | +19.78% / +67.66% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| Raydium AMM | $511.32M | +41.32% |
| BisonFi | $395.81M | 0.00% |
| Meteora DLMM | $363.04M | +64.69% |
| HumidiFi | $322.67M | 0.00% |
| PumpSwap | $294.17M | -37.16% |
| Orca DEX | $237.18M | +41.34% |
| Tessera V | $232.00M | 0.00% |
| Manifest Trade | $171.11M | +17.41% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.56B | +2.20% | +0.02% |
| Kamino Lend | Lending | $1.35B | +1.48% | +2.17% |
| Raydium AMM | Dexs | $1.14B | +2.46% | +3.10% |
| Jupiter Lend | Lending | $1.10B | +2.38% | +0.28% |
| Binance Staked SOL | Liquid Staking | $1.05B | +2.12% | -0.38% |
| Jito Liquid Staking | Liquid Staking | $1.04B | +2.32% | +0.24% |
| BlackRock BUIDL | RWA | $992.60M | -0.61% | -2.25% |
| Jupiter Perpetual Exchange | Derivatives | $747.79M | +1.20% | -0.39% |
| Jupiter Staked SOL | Liquid Staking | $525.91M | +2.46% | -0.20% |
| Sentora Curator | Risk Curators | $388.61M | +2.89% | -1.12% |

## Stablecoins

Solana circulating pegged-USD: **$16.13B**
(1d +1.20% · 7d -0.31%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.25B | +3.73% |
| USDT · Tether | $2.60B | -2.99% |
| USDGO · USDGO | $1.38B | -0.01% |
| USD1 · World Liberty Financial USD | $1.30B | +1.51% |
| BUIDL · BlackRock USD | $992.60M | +0.01% |
| PYUSD · PayPal USD | $707.33M | -5.25% |
| USDG · Global Dollar | $599.18M | +0.01% |
| USDe · Ethena USDe | $535.62M | -0.20% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 2 of 800 Solana-deployed listed symbols (multiplier ok 80/80; 800 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 800 · Solana deployments 800 · priced 2 · priced-subset mcap $59.02M (lower bound, not a census).
24h volume $107.64M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 2 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 800 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 800 unique underlyings among 800 Solana rows; not every tokenized equity on Solana). 800 of 800 listed xStocks have a Solana deployment (800 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$1.92B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $992.60M
- **OnRe** (RWA) — $294.85M
- **Huma Finance V2** (RWA) — $191.51M
- **Ondo Yield Assets** (RWA) — $179.67M
- **Hastra** (RWA) — $148.78M
- **Plume Vaults** (RWA) — $27.43M
- **Ondo Global Markets** (RWA) — $25.92M
- **Apollo Diversified Credit Securitize Fund** (RWA) — $18.35M

## Daily active addresses

967,396 (Allium, as of 2026-09-10). Provider range 482,447–988,015. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [63% of tokenized equity volume on Solana happens while Wall Street is asleep.](https://x.com/solana/status/2098639407884693541) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 12 Sep 2026 05:06:40 GMT
- [RT by @solana: Launch tokens paired with 100+ xStocks, including $AMZNx, $NFLXx, $PLTRx and more.

Powered by @xStocksFi, the largest tokenized equity issuer on @solana.

Now anyone can build new markets around the world’s biggest stocks on Meteora.](https://x.com/MeteoraAG/status/2098460479031271540) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 17:15:40 GMT
- [RT by @solana: Don't buy stocks. Earn them.

Now live on @solana.](https://x.com/apys_co/status/2098441509955678562) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 16:00:17 GMT
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
- [Step 2 of SIMD-0437 rent reduction is live.

How to reclaim excess SOL: https://x.com/a_milz/status/2095532192579661927?s=20](https://x.com/anza_xyz/status/2098519198783922184) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 21:09:00 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: 🚨JUST IN: The second wave of rent stimmy for @Solana users is on the way.

Rent reduction Step 2 goes live on mainnet in 7 hours, making another 612,000 $SOL reclaimable and bringing the total to 918,000 $SOL. 

Across all five steps, up to 3.06M $SOL ($319M) will become reclaimable.](https://x.com/SolanaFloor/status/2098406673874612536) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 13:41:52 GMT `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [63% of tokenized equity volume on Solana happens while Wall Street is asleep.](https://x.com/solana/status/2098639407884693541) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 12 Sep 2026 05:06:40 GMT
- [RT by @solana: Launch tokens paired with 100+ xStocks, including $AMZNx, $NFLXx, $PLTRx and more.

Powered by @xStocksFi, the largest tokenized equity issuer on @solana.

Now anyone can build new markets around the world’s biggest stocks on Meteora.](https://x.com/MeteoraAG/status/2098460479031271540) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 17:15:40 GMT
- [RT by @solana: Don't buy stocks. Earn them.

Now live on @solana.](https://x.com/apys_co/status/2098441509955678562) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 11 Sep 2026 16:00:17 GMT
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
- [Step 2 of SIMD-0437 rent reduction is live.

How to reclaim excess SOL: https://x.com/a_milz/status/2095532192579661927?s=20](https://x.com/anza_xyz/status/2098519198783922184) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 21:09:00 GMT `upgrade` `mainnet`
- [RT by @anza_xyz: 🚨JUST IN: The second wave of rent stimmy for @Solana users is on the way.

Rent reduction Step 2 goes live on mainnet in 7 hours, making another 612,000 $SOL reclaimable and bringing the total to 918,000 $SOL. 

Across all five steps, up to 3.06M $SOL ($319M) will become reclaimable.](https://x.com/SolanaFloor/status/2098406673874612536) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 11 Sep 2026 13:41:52 GMT `mainnet`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-12 (2026-09-11 23:44:00 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 136ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 32ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 54ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 109ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 38ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6194ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 103ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 84ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 35ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 134ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 23ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 25ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 29ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 63ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 247ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 49ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 73ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 270ms https://solana.com/data
- `solana.com.databricks` [ok] 200 145ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 456ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 130ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 44ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 74ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 196ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 500ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 84ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 292ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 79ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 305ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 681ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1438ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1885ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 191ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 115ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 33ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 200ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 246ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 337ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 317ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 332ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 244ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 108ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 756ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 367ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 250ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 268ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 233ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 233ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 399ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 245ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2579ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1284ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1194ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2796ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1172ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1390ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1221ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1695ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.SPYx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.SPYx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.COINx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/COINx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WGSx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.QQQx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.FLNCx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WRLDx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.INDIx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.XRXx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.QQQx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.WGSx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.price.PCTx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.COINx` [ok] 200 696ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.AIx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.INDIx` [ok] 200 1295ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 1306ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.INDIx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 981ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.mult.AIx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.METCx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/METCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.QUBTx` [FAIL]  12012ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WYFIx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BETRx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BETRx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.BETRx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.circ.QUBTx` [ok] 200 1143ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.price.DRSx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/DRSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.QUBTx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.SCIx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/SCIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.METCx` [ok] 200 1363ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.WYFIx` [ok] 200 1332ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.MPx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/MPx/price-data
- `xstocks.price.SAILx` [FAIL]  12016ms https://api.backed.fi/api/v2/public/assets/SAILx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.WYFIx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.BSYx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/BSYx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.METCx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.circ.BSYx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/BSYx/circulating-supply?format=object
- `xstocks.mult.BSYx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/BSYx/multiplier?network=Solana
- `xstocks.circ.MPx` [ok] 200 972ms https://api.backed.fi/api/v2/public/assets/MPx/circulating-supply?format=object
- `xstocks.circ.SAILx` [ok] 200 1002ms https://api.backed.fi/api/v2/public/assets/SAILx/circulating-supply?format=object
- `xstocks.circ.DRSx` [ok] 200 1419ms https://api.backed.fi/api/v2/public/assets/DRSx/circulating-supply?format=object
- `xstocks.mult.SAILx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/SAILx/multiplier?network=Solana
- `xstocks.circ.SCIx` [ok] 200 1373ms https://api.backed.fi/api/v2/public/assets/SCIx/circulating-supply?format=object
- `xstocks.mult.DRSx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/DRSx/multiplier?network=Solana
- `xstocks.price.RYANx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/RYANx/price-data
- `xstocks.mult.MPx` [ok] 200 719ms https://api.backed.fi/api/v2/public/assets/MPx/multiplier?network=Solana
- `xstocks.mult.SCIx` [ok] 200 582ms https://api.backed.fi/api/v2/public/assets/SCIx/multiplier?network=Solana
- `xstocks.price.DYx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/DYx/price-data
- `xstocks.circ.DYx` [ok] 200 816ms https://api.backed.fi/api/v2/public/assets/DYx/circulating-supply?format=object
- `xstocks.circ.RYANx` [ok] 200 1379ms https://api.backed.fi/api/v2/public/assets/RYANx/circulating-supply?format=object
- `xstocks.mult.RYANx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/RYANx/multiplier?network=Solana
- `xstocks.mult.DYx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/DYx/multiplier?network=Solana
- `xstocks.price.AMx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/AMx/price-data
- `xstocks.circ.AMx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/AMx/circulating-supply?format=object
- `xstocks.mult.AMx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/AMx/multiplier?network=Solana
- `xstocks.price.GSATx` [FAIL]  12016ms https://api.backed.fi/api/v2/public/assets/GSATx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DVAx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/DVAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DCIx` [FAIL]  12018ms https://api.backed.fi/api/v2/public/assets/DCIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DCIx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/DCIx/circulating-supply?format=object
- `xstocks.circ.GSATx` [ok] 200 1510ms https://api.backed.fi/api/v2/public/assets/GSATx/circulating-supply?format=object
- `xstocks.mult.DCIx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/DCIx/multiplier?network=Solana
- `xstocks.price.GDDYx` [FAIL]  12015ms https://api.backed.fi/api/v2/public/assets/GDDYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BXPx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/BXPx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DVAx` [ok] 200 1406ms https://api.backed.fi/api/v2/public/assets/DVAx/circulating-supply?format=object
- `xstocks.circ.BXPx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/BXPx/circulating-supply?format=object
- `xstocks.mult.DVAx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/DVAx/multiplier?network=Solana
- `xstocks.mult.GSATx` [ok] 200 1260ms https://api.backed.fi/api/v2/public/assets/GSATx/multiplier?network=Solana
- `xstocks.mult.BXPx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/BXPx/multiplier?network=Solana
- `xstocks.price.SFx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/SFx/price-data
- `xstocks.price.FRHCx` [FAIL]  12011ms https://api.backed.fi/api/v2/public/assets/FRHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.GDDYx` [ok] 200 1109ms https://api.backed.fi/api/v2/public/assets/GDDYx/circulating-supply?format=object
- `xstocks.mult.GDDYx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/GDDYx/multiplier?network=Solana
- `xstocks.circ.FRHCx` [ok] 200 1113ms https://api.backed.fi/api/v2/public/assets/FRHCx/circulating-supply?format=object
- `xstocks.circ.SFx` [ok] 200 1136ms https://api.backed.fi/api/v2/public/assets/SFx/circulating-supply?format=object
- `xstocks.price.WMSx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/WMSx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.FRHCx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/FRHCx/multiplier?network=Solana
- `xstocks.mult.SFx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/SFx/multiplier?network=Solana
- `xstocks.price.FDSx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/FDSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.FDSx` [ok] 200 1301ms https://api.backed.fi/api/v2/public/assets/FDSx/circulating-supply?format=object
- `xstocks.circ.WMSx` [ok] 200 2004ms https://api.backed.fi/api/v2/public/assets/WMSx/circulating-supply?format=object
- `xstocks.mult.FDSx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/FDSx/multiplier?network=Solana
- `xstocks.mult.WMSx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/WMSx/multiplier?network=Solana
- `xstocks.price.ALSNx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/ALSNx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ALSNx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/ALSNx/circulating-supply?format=object
- `xstocks.mult.ALSNx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/ALSNx/multiplier?network=Solana
- `xstocks.price.SMTCx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/SMTCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AXSMx` [FAIL]  12027ms https://api.backed.fi/api/v2/public/assets/AXSMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AXSMx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/AXSMx/circulating-supply?format=object
- `xstocks.price.EGPx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/EGPx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.EGPx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/EGPx/circulating-supply?format=object
- `xstocks.mult.EGPx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/EGPx/multiplier?network=Solana
- `xstocks.mult.AXSMx` [ok] 200 792ms https://api.backed.fi/api/v2/public/assets/AXSMx/multiplier?network=Solana
- `xstocks.price.PAGx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/PAGx/price-data
- `xstocks.circ.SMTCx` [ok] 200 1242ms https://api.backed.fi/api/v2/public/assets/SMTCx/circulating-supply?format=object
- `xstocks.mult.SMTCx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/SMTCx/multiplier?network=Solana
- `xstocks.price.BPOPx` [FAIL]  12010ms https://api.backed.fi/api/v2/public/assets/BPOPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.TTMIx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/TTMIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BPOPx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/BPOPx/circulating-supply?format=object
- `xstocks.mult.BPOPx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/BPOPx/multiplier?network=Solana
- `xstocks.price.HIIx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/HIIx/price-data
- `xstocks.circ.PAGx` [ok] 200 1225ms https://api.backed.fi/api/v2/public/assets/PAGx/circulating-supply?format=object
- `xstocks.circ.TTMIx` [ok] 200 919ms https://api.backed.fi/api/v2/public/assets/TTMIx/circulating-supply?format=object
- `xstocks.mult.PAGx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/PAGx/multiplier?network=Solana
- `xstocks.mult.TTMIx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/TTMIx/multiplier?network=Solana
- `xstocks.price.GFLx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/GFLx/price-data
- `xstocks.circ.GFLx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/GFLx/circulating-supply?format=object
- `xstocks.mult.GFLx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/GFLx/multiplier?network=Solana
- `xstocks.price.AEISx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/AEISx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DPZx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/DPZx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AEISx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/AEISx/circulating-supply?format=object
- `xstocks.circ.DPZx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/DPZx/circulating-supply?format=object
- `xstocks.mult.DPZx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/DPZx/multiplier?network=Solana
- `xstocks.mult.AEISx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/AEISx/multiplier?network=Solana
- `xstocks.circ.HIIx` [ok] 200 1919ms https://api.backed.fi/api/v2/public/assets/HIIx/circulating-supply?format=object
- `xstocks.mult.HIIx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/HIIx/multiplier?network=Solana
- `xstocks.price.HRLx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/HRLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.KTOSx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/KTOSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HRLx` [ok] 200 1334ms https://api.backed.fi/api/v2/public/assets/HRLx/circulating-supply?format=object
- `xstocks.mult.HRLx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/HRLx/multiplier?network=Solana
- `xstocks.price.SEICx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/SEICx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.KTOSx` [ok] 200 1197ms https://api.backed.fi/api/v2/public/assets/KTOSx/circulating-supply?format=object
- `xstocks.price.EHCx` [FAIL]  12012ms https://api.backed.fi/api/v2/public/assets/EHCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SEICx` [ok] 200 1117ms https://api.backed.fi/api/v2/public/assets/SEICx/circulating-supply?format=object
- `xstocks.circ.EHCx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/EHCx/circulating-supply?format=object
- `xstocks.mult.EHCx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/EHCx/multiplier?network=Solana
- `xstocks.mult.KTOSx` [ok] 200 1025ms https://api.backed.fi/api/v2/public/assets/KTOSx/multiplier?network=Solana
- `xstocks.price.ARx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/ARx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ARx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/ARx/circulating-supply?format=object
- `xstocks.mult.SEICx` [ok] 200 1307ms https://api.backed.fi/api/v2/public/assets/SEICx/multiplier?network=Solana
- `xstocks.mult.ARx` [ok] 200 487ms https://api.backed.fi/api/v2/public/assets/ARx/multiplier?network=Solana
- `xstocks.price.MGMx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/MGMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DOCUx` [FAIL]  12010ms https://api.backed.fi/api/v2/public/assets/DOCUx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.DOCUx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/DOCUx/circulating-supply?format=object
- `xstocks.price.HALOx` [FAIL]  12015ms https://api.backed.fi/api/v2/public/assets/HALOx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.DOCUx` [ok] 200 533ms https://api.backed.fi/api/v2/public/assets/DOCUx/multiplier?network=Solana
- `xstocks.circ.MGMx` [ok] 200 1406ms https://api.backed.fi/api/v2/public/assets/MGMx/circulating-supply?format=object
- `xstocks.mult.MGMx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/MGMx/multiplier?network=Solana
- `xstocks.circ.HALOx` [ok] 200 1430ms https://api.backed.fi/api/v2/public/assets/HALOx/circulating-supply?format=object
- `xstocks.mult.HALOx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/HALOx/multiplier?network=Solana
- `xstocks.price.WTRGx` [FAIL]  12019ms https://api.backed.fi/api/v2/public/assets/WTRGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WTRGx` [ok] 200 991ms https://api.backed.fi/api/v2/public/assets/WTRGx/circulating-supply?format=object
- `xstocks.mult.WTRGx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/WTRGx/multiplier?network=Solana
- `xstocks.price.CRx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/CRx/price-data
- `xstocks.circ.CRx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/CRx/circulating-supply?format=object
- `xstocks.mult.CRx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/CRx/multiplier?network=Solana
- `xstocks.price.AFGx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/AFGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HUBSx` [FAIL]  12012ms https://api.backed.fi/api/v2/public/assets/HUBSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AFGx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/AFGx/circulating-supply?format=object
- `xstocks.mult.AFGx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/AFGx/multiplier?network=Solana
- `xstocks.price.AMKRx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/AMKRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GMEDx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/GMEDx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AMKRx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/AMKRx/circulating-supply?format=object
- `xstocks.circ.GMEDx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/GMEDx/circulating-supply?format=object
- `xstocks.circ.HUBSx` [ok] 200 1165ms https://api.backed.fi/api/v2/public/assets/HUBSx/circulating-supply?format=object
- `xstocks.mult.AMKRx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/AMKRx/multiplier?network=Solana
- `xstocks.mult.GMEDx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/GMEDx/multiplier?network=Solana
- `xstocks.mult.HUBSx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/HUBSx/multiplier?network=Solana
- `xstocks.price.JKHYx` [FAIL]  12018ms https://api.backed.fi/api/v2/public/assets/JKHYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.IESCx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/IESCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.JKHYx` [ok] 200 1043ms https://api.backed.fi/api/v2/public/assets/JKHYx/circulating-supply?format=object
- `xstocks.mult.JKHYx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/JKHYx/multiplier?network=Solana
- `xstocks.price.OCx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/OCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.OCx` [ok] 200 794ms https://api.backed.fi/api/v2/public/assets/OCx/circulating-supply?format=object
- `xstocks.mult.OCx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/OCx/multiplier?network=Solana
- `xstocks.circ.IESCx` [ok] 200 1233ms https://api.backed.fi/api/v2/public/assets/IESCx/circulating-supply?format=object
- `xstocks.mult.IESCx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/IESCx/multiplier?network=Solana
- `xstocks.price.BMRNx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/BMRNx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BMRNx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/BMRNx/circulating-supply?format=object
- `xstocks.mult.BMRNx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/BMRNx/multiplier?network=Solana
- `xstocks.price.JEFx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/JEFx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AMHx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/AMHx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.FIVEx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/FIVEx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ITx` [FAIL]  12011ms https://api.backed.fi/api/v2/public/assets/ITx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AMHx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/AMHx/circulating-supply?format=object
- `xstocks.circ.FIVEx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/FIVEx/circulating-supply?format=object
- `xstocks.mult.AMHx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/AMHx/multiplier?network=Solana
- `xstocks.price.IVZx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/IVZx/price-data
- `xstocks.mult.FIVEx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/FIVEx/multiplier?network=Solana
- `xstocks.circ.ITx` [ok] 200 1013ms https://api.backed.fi/api/v2/public/assets/ITx/circulating-supply?format=object
- `xstocks.circ.JEFx` [ok] 200 1890ms https://api.backed.fi/api/v2/public/assets/JEFx/circulating-supply?format=object
- `xstocks.mult.JEFx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/JEFx/multiplier?network=Solana
- `xstocks.mult.ITx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/ITx/multiplier?network=Solana
- `xstocks.circ.IVZx` [ok] 200 1143ms https://api.backed.fi/api/v2/public/assets/IVZx/circulating-supply?format=object
- `xstocks.mult.IVZx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/IVZx/multiplier?network=Solana
- `xstocks.price.MDGLx` [FAIL]  12010ms https://api.backed.fi/api/v2/public/assets/MDGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MDGLx` [ok] 200 111ms https://api.backed.fi/api/v2/public/assets/MDGLx/circulating-supply?format=object
- `xstocks.mult.MDGLx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/MDGLx/multiplier?network=Solana
- `xstocks.price.VNOMx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/VNOMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.UHALx` [FAIL]  12011ms https://api.backed.fi/api/v2/public/assets/UHALx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.VNOMx` [ok] 200 1001ms https://api.backed.fi/api/v2/public/assets/VNOMx/circulating-supply?format=object
- `xstocks.mult.VNOMx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/VNOMx/multiplier?network=Solana
- `xstocks.circ.UHALx` [ok] 200 1145ms https://api.backed.fi/api/v2/public/assets/UHALx/circulating-supply?format=object
- `xstocks.mult.UHALx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/UHALx/multiplier?network=Solana
- `xstocks.price.GWREx` [ok] 200 662ms https://api.backed.fi/api/v2/public/assets/GWREx/price-data
- `xstocks.circ.GWREx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/GWREx/circulating-supply?format=object
- `xstocks.mult.GWREx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/GWREx/multiplier?network=Solana
- `xstocks.price.AHRx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/AHRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AHRx` [ok] 200 111ms https://api.backed.fi/api/v2/public/assets/AHRx/circulating-supply?format=object
- `xstocks.mult.AHRx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/AHRx/multiplier?network=Solana
- `xstocks.price.CORTx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/CORTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CORTx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/CORTx/circulating-supply?format=object
- `xstocks.mult.CORTx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/CORTx/multiplier?network=Solana
- `xstocks.price.CACIx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/CACIx/price-data
- `xstocks.circ.CACIx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/CACIx/circulating-supply?format=object
- `xstocks.mult.CACIx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/CACIx/multiplier?network=Solana
- `xstocks.price.STRLx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/STRLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.NWSAx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/NWSAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BAXx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/BAXx/price-data
- `xstocks.circ.BAXx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/BAXx/circulating-supply?format=object
- `xstocks.mult.BAXx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/BAXx/multiplier?network=Solana
- `xstocks.price.AURx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/AURx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AURx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/AURx/circulating-supply?format=object
- `xstocks.mult.AURx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/AURx/multiplier?network=Solana
- `xstocks.price.Hx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/Hx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.Hx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/Hx/circulating-supply?format=object
- `xstocks.mult.Hx` [ok] 200 113ms https://api.backed.fi/api/v2/public/assets/Hx/multiplier?network=Solana
- `xstocks.circ.NWSAx` [ok] 200 1244ms https://api.backed.fi/api/v2/public/assets/NWSAx/circulating-supply?format=object
- `xstocks.mult.NWSAx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/NWSAx/multiplier?network=Solana
- `xstocks.circ.STRLx` [ok] 200 1576ms https://api.backed.fi/api/v2/public/assets/STRLx/circulating-supply?format=object
- `xstocks.mult.STRLx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/STRLx/multiplier?network=Solana
- `xstocks.price.ARWRx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/ARWRx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.ARWRx` [ok] 200 112ms https://api.backed.fi/api/v2/public/assets/ARWRx/circulating-supply?format=object
- `xstocks.mult.ARWRx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/ARWRx/multiplier?network=Solana
- `xstocks.price.NWSx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/NWSx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.NWSx` [ok] 200 1176ms https://api.backed.fi/api/v2/public/assets/NWSx/circulating-supply?format=object
- `xstocks.mult.NWSx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/NWSx/multiplier?network=Solana
- `xstocks.price.MANHx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/MANHx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MANHx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/MANHx/circulating-supply?format=object
- `xstocks.mult.MANHx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/MANHx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 21ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 129ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.AIx` [ok] 200 41ms https://lite-api.jup.ag/tokens/v2/search?query=AIx
- `jup.tokens.search.FLNCx` [ok] 200 40ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.WGSx` [ok] 200 37ms https://lite-api.jup.ag/tokens/v2/search?query=WGSx
- `jup.tokens.search.WRLDx` [ok] 200 49ms https://lite-api.jup.ag/tokens/v2/search?query=WRLDx
- `jup.tokens.search.INDIx` [ok] 200 39ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.XRXx` [ok] 200 37ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.PCTx` [ok] 200 40ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.BETRx` [ok] 200 43ms https://lite-api.jup.ag/tokens/v2/search?query=BETRx
- `jito.tip_floor` [ok] 200 368ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 258ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 42ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 40ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 57ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 76ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 119ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 2829ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
