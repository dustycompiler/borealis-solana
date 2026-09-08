# Borealis — Solana ecosystem report

**Generated** 2026-09-08T09:53:38Z · 2026-09-08 02:53:38 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-08T09:53:28Z · **RPC health** `ok`
**Health score** 82 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** WATCH · **Ecosystem** NORMAL — SOL 24h -1.13%; DEX 24h $2.87B · 1d -1% · vs-7d-ago +15%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +9.17%. (threshold: `|1d %| >= 8`)
- **WARN · High validator delinquency** — 15 delinquent vote accounts, 1.166% of activated+delinquent stake. (threshold: `delinquent stake >= 1% or delinquent count >= 25`)
- **INFO · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -1.13%, DeFiLlama TVL 1d -2.07%, DEX 1d -1.12%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 445,309,019 |
| Block height | 423,353,102 |
| Block time | 2026-09-08T09:53:28Z |
| Epoch | 1,030 (80.79% · slot 349,022/432,000) |
| Mean TPS (last ~3,600s) | 3,476.2 |
| Mean non-vote TPS | 1,354.4 |
| Median TPS (same window) | 3,445.6 |
| Mean slot time | 315.4 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 546,294,275,702 |
| Circulating supply | 586,165,333 SOL |
| Total supply | 633,642,612 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 673 |
| Delinquent | 15 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 434,353,065 SOL |
| Delinquent stake | 5,124,923.37 SOL (1.166%) |
| Nakamoto (33% / 50% / 67%) | 18 / 40 / 79 |
| Top 10 / 20 stake share | 24.48% / 35.87% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 4.01% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.34M SOL | 3.76% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.52M SOL | 2.88% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.40M SOL | 2.62% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.56M SOL | 2.20% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.18M SOL | 2.11% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.08% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.38M SOL | 1.70% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.86M SOL | 1.58% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.60M SOL | 1.52% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.41% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.41% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.97M SOL | 1.37% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.64M SOL | 1.30% | 100% | 0 |
| 15 | `GnC339vk…` | 4.85M SOL | 1.12% | 7% | 0 |

### Delinquency alerts

- `GSTampk6…` · 2.50M SOL · commission 100% · lag 2432 slots
- `AEHqTB2R…` · 2.08M SOL · commission 100% · lag 2432 slots
- `3YVoK8UN…` · 489.64K SOL · commission 5% · lag 25616 slots
- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 81171 slots
- `xLabscif…` · 8.89K SOL · commission 5% · lag 1520646 slots
- `prt1st4R…` · 7.04K SOL · commission 5% · lag 1822077 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 1960296 slots
- `5ZjxMYBb…` · 3.79K SOL · commission 0% · lag 1343097 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 769828 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 1870380 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 2508668 slots
- `HFTcVVrX…` · 148.42 SOL · commission 100% · lag 2508562 slots

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
| **In-protocol fees 24h** | **$658.16K** (6,158.9 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-06 |
| **Solana REV** | **7,251.8 SOL** / **$774.94K** | MEASURED UTC calendar day 2026-09-06: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-06 · UTC day 2026-09-06 · SOL-USD date 2026-09-06 |
| Jito tip-floor run-rate (NOT REV) | $38.68K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 38679 USD; at p95 floor → 174077 USD. |
| Protocol fees 24h | $16.00M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9987 |
| p90 / p99 | 0.000010 / 0.000108 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.63 | coingecko.simple_price |
| 24h change | -1.13% | coingecko.simple_price |
| Market cap | $60.74B | coingecko.simple_price |
| 24h volume | $2.90B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.87B |
| TVL 1d / 7d / 30d | -2.07% / -1.93% / +22.06% |
| DEX volume 24h | $2.87B · 1d -1.12% · vs-7d-ago +14.81% |
| 7d DEX volume | $15.45B · -12.59% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $16.00M |
| Fees 1d / 7d | +9.17% / +19.86% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $873.43M | +28.85% |
| Raydium AMM | $291.98M | -25.55% |
| BisonFi | $241.45M | 0.00% |
| Orca DEX | $226.62M | -30.64% |
| Tessera V | $206.39M | 0.00% |
| Meteora DLMM | $195.35M | -12.44% |
| HumidiFi | $143.21M | 0.00% |
| Manifest Trade | $143.09M | +8.98% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.57B | -1.75% | -0.34% |
| Kamino Lend | Lending | $1.33B | -0.88% | +6.00% |
| Raydium AMM | Dexs | $1.13B | -1.82% | +1.20% |
| Jupiter Lend | Lending | $1.09B | -1.86% | -0.16% |
| Binance Staked SOL | Liquid Staking | $1.07B | -1.49% | +0.41% |
| Jito Liquid Staking | Liquid Staking | $1.06B | -1.41% | +1.48% |
| BlackRock BUIDL | RWA | $977.90M | +0.00% | +0.38% |
| Jupiter Perpetual Exchange | Derivatives | $748.36M | -1.59% | -2.09% |
| Jupiter Staked SOL | Liquid Staking | $532.92M | -2.23% | -0.53% |
| xStocks | RWA | $441.65M | -2.30% | -0.24% |

## Stablecoins

Solana circulating pegged-USD: **$16.26B**
(1d -0.28% · 7d +4.53%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.27B | -1.19% |
| USDT · Tether | $2.77B | +0.00% |
| USDGO · USDGO | $1.37B | +0.74% |
| USD1 · World Liberty Financial USD | $1.26B | +0.48% |
| BUIDL · BlackRock USD | $977.90M | 0.00% |
| PYUSD · PayPal USD | $731.85M | -2.21% |
| USDG · Global Dollar | $578.15M | -1.53% |
| USDe · Ethena USDe | $536.33M | +0.23% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 79 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 79 · priced-subset mcap $288.23M (lower bound, not a census).
24h volume $67.83M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $441.65M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 79 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.35B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $977.90M
- **xStocks** (RWA) — $441.65M
- **OnRe** (RWA) — $302.84M
- **Huma Finance V2** (RWA) — $186.50M
- **Ondo Yield Assets** (RWA) — $179.63M
- **Hastra** (RWA) — $151.55M
- **Ondo Global Markets** (RWA) — $25.88M
- **Plume Vaults** (RWA) — $24.10M

## Daily active addresses

858,456 (Allium, as of 2026-09-06). Provider range 418,160–928,010. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Register to Crypto World’s Fair, runs Sept 14 to Oct 12:  https://x.com/colosseum/status/2095574551841112180](https://x.com/solana/status/2097232159799234960) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 07:54:46 GMT
- [We asked @colosseum founders one question: what would you tell someone considering applying?](https://x.com/solana/status/2097232157186121877) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 07:54:45 GMT
- [JUST IN: Solana RWA holders cross 400K for the first time

400K+ holders, up from under 10K in January 2025](https://x.com/solana/status/2097196979243901335) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 05:34:58 GMT
- [RT by @solana: Sanctum on the @Blockworks @0xResearch newsletter today by @Kunallegendd: 

"On Solana, one stat is difficult to square: the network’s largest protocol by TVL has an FDV of just $32M. It is not Jupiter, Kamino or Jito. It is Sanctum, a protocol that has stayed out of the spotlight despite quietly becoming one of Solana’s most important pieces of infrastructure."

Full article: https://blockworks-research.beehiiv.com/p/sanctum-flips-jupiter?_bhlid=4b496bee66de52c6cc2e45a413a8cd63974e50bd](https://x.com/sanctumIR/status/2096980608262209943) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 15:15:11 GMT
- [RT by @solana: Introducing: ✦ Abstract Markets https://x.com/i/article/2093297250650796032](https://x.com/kar888l/status/2096990586297290924) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 15:54:50 GMT
- [RT by @solana: ZEC-backed credit is now live on Solana.

Introducing the ZCASH Market on Kamino, curated by @AllezLabs.

ZEC holders can supply ZEC as collateral and borrow USDC against their position in a fully isolated market on Kamino.](https://x.com/kamino/status/2097066296592777447) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 20:55:41 GMT
- [RT by @solana: We built the end-to-end CLI for funding and growing a startup.

"Claude, launch a fundraise and give my top referrers 1% of my business."

One command opens your round. The next one puts ownership in your users' hands.](https://x.com/stardotfun/status/2097057882814734547) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 20:22:15 GMT
- [Start the week with @WSOP poker https://x.com/i/broadcasts/1dKrPrNNAwwJX](https://x.com/solana/status/2097063901279997970) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 20:46:10 GMT
- [# How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — solana.com/news · Mon, 07 Sep 2026 07:00:00 GMT
- [Solana Ecosystem Roundup: August 2026](https://solana.com/news/solana-ecosystem-roundup-august-2026) — solana.com/news · Fri, 04 Sep 2026 04:18:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [Register to Crypto World’s Fair, runs Sept 14 to Oct 12:  https://x.com/colosseum/status/2095574551841112180](https://x.com/solana/status/2097232159799234960) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 07:54:46 GMT
- [We asked @colosseum founders one question: what would you tell someone considering applying?](https://x.com/solana/status/2097232157186121877) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 07:54:45 GMT
- [JUST IN: Solana RWA holders cross 400K for the first time

400K+ holders, up from under 10K in January 2025](https://x.com/solana/status/2097196979243901335) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 08 Sep 2026 05:34:58 GMT
- [RT by @solana: Sanctum on the @Blockworks @0xResearch newsletter today by @Kunallegendd: 

"On Solana, one stat is difficult to square: the network’s largest protocol by TVL has an FDV of just $32M. It is not Jupiter, Kamino or Jito. It is Sanctum, a protocol that has stayed out of the spotlight despite quietly becoming one of Solana’s most important pieces of infrastructure."

Full article: https://blockworks-research.beehiiv.com/p/sanctum-flips-jupiter?_bhlid=4b496bee66de52c6cc2e45a413a8cd63974e50bd](https://x.com/sanctumIR/status/2096980608262209943) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 15:15:11 GMT
- [RT by @solana: Introducing: ✦ Abstract Markets https://x.com/i/article/2093297250650796032](https://x.com/kar888l/status/2096990586297290924) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 15:54:50 GMT
- [RT by @solana: ZEC-backed credit is now live on Solana.

Introducing the ZCASH Market on Kamino, curated by @AllezLabs.

ZEC holders can supply ZEC as collateral and borrow USDC against their position in a fully isolated market on Kamino.](https://x.com/kamino/status/2097066296592777447) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 20:55:41 GMT
- [RT by @solana: We built the end-to-end CLI for funding and growing a startup.

"Claude, launch a fundraise and give my top referrers 1% of my business."

One command opens your round. The next one puts ownership in your users' hands.](https://x.com/stardotfun/status/2097057882814734547) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 20:22:15 GMT
- [Start the week with @WSOP poker https://x.com/i/broadcasts/1dKrPrNNAwwJX](https://x.com/solana/status/2097063901279997970) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 20:46:10 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-08 (2026-09-08 02:53:38 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 726 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 431ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 497ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 486ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 369ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 361ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6142ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 836ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 126ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 123ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 424ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 49ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 51ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 64ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 151ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 86ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 652ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 125ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 448ms https://solana.com/data
- `solana.com.databricks` [ok] 200 161ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 891ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 163ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 185ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 109ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 372ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 753ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 443ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 391ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 370ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 5123ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [FAIL] 502 361ms https://nitter.perennialte.ch/solana_status/rss — HTTP 502 Bad Gateway
- `rss.nitter.anza_xyz` [FAIL] 502 219ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_devs` [FAIL] 502 194ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 502 Bad Gateway
- `status.incidents` [ok] 200 188ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 396ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 434ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1864ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1789ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1361ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1796ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1598ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1753ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2359ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1870ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1372ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1386ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1479ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1681ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1870ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1835ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1916ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1912ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1597ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 3441ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1886ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1980ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1713ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1169ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.MSFTx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.SPYx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.NVDAx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.AMZNx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.AAPLx` [ok] 200 400ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.GOOGLx` [ok] 200 411ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.SPYx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.TSLAx` [ok] 200 651ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 864ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.TSLAx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 653ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.NVDAx` [ok] 200 1094ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 928ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.DRAMx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.mult.TSLAx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.MUUx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.mult.NVDAx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.MVLLx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.circ.MUUx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.price.KORUx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.circ.MVLLx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 806ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.AXTIx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.mult.MUUx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.DJTx` [ok] 200 616ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.KORUx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 1110ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.DRAMx` [ok] 200 520ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.DJTx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.SNXXx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.price.INTWx` [ok] 200 496ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.mult.DJTx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.AXTIx` [ok] 200 637ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 499ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.SHEINx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.INTWx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.circ.SOXSx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.price.NWGx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.mult.QQQx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.SHEINx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.circ.NWGx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.SOXSx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.mult.SNXXx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.mult.SHEINx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.NWGx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.mult.INTWx` [ok] 200 938ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.MMGx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.BANKCx` [ok] 200 996ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.CTINSx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 565ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.KUNLx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.SMOIHx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 588ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.CRESBx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 2796ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 507ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.CRESBx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 1987ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.JTGEXx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.CSPCx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.CMERPx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.CRESMx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 751ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.WXXDCx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.mult.CRESMx` [ok] 200 538ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 618ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.ASMPTx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.CMENDx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 950ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.JDHLTx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.JTGEXx` [ok] 200 1552ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 1013ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 734ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.SINOTx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 601ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 651ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.SINOTx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.CRESPx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.SINOx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.CTPCAx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.SINOx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.PRADx` [ok] 200 1625ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.PRADx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 2339ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 779ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.GENTEx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.WHGROx` [ok] 200 923ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.SITCx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.GENTEx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 726ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.price.CKAHx` [ok] 200 687ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 847ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.HKCGAx` [ok] 200 644ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.KUAIx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 1022ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 454ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.COVELx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 803ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 869ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 820ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 852ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 885ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.circ.COVELx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.GEELx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.HNDLDx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.price.MTRCPx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.CHONGx` [ok] 200 703ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.NONGx` [ok] 200 528ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.COVELx` [ok] 200 723ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.MTRCPx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 431ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.COSCx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 12266ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 1118ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1706ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 205ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INTWx` [ok] 200 127ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.MUUx` [ok] 200 91ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.KORUx` [ok] 200 133ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.SHEINx` [ok] 200 88ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.MVLLx` [ok] 200 132ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SNXXx` [ok] 200 91ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jup.tokens.search.DRAMx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.SOXSx` [ok] 200 132ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jito.tip_floor` [ok] 200 79ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 455ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 150ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 367ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 388ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 499ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 548ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 2278ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
