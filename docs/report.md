# Borealis — Solana ecosystem report

**Generated** 2026-09-07T23:23:02Z · 2026-09-07 16:23:02 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-07T23:22:52Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -2.52%; DEX 24h $2.90B · 1d +56% · vs-7d-ago +51%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +44.97%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +55.76%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +50.52%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 445,189,310 |
| Block height | 423,233,476 |
| Block time | 2026-09-07T23:22:52Z |
| Epoch | 1,030 (53.08% · slot 229,312/432,000) |
| Mean TPS (last ~3,600s) | 3,827.1 |
| Mean non-vote TPS | 1,697.0 |
| Median TPS (same window) | 3,823.3 |
| Mean slot time | 315.4 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 546,158,030,278 |
| Circulating supply | 586,165,692 SOL |
| Total supply | 633,642,972 SOL |
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
| Activated stake | 439,428,459 SOL |
| Delinquent stake | 49,528.97 SOL (0.011%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.19% / 35.46% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 3.97% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.34M SOL | 3.72% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.52M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.40M SOL | 2.59% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.56M SOL | 2.18% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.18M SOL | 2.09% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.38M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.86M SOL | 1.56% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.60M SOL | 1.50% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.39% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.39% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.97M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.64M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.85M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 142280 slots
- `xLabscif…` · 8.89K SOL · commission 5% · lag 1400937 slots
- `prt1st4R…` · 7.04K SOL · commission 5% · lag 1702368 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 1840587 slots
- `5ZjxMYBb…` · 3.79K SOL · commission 0% · lag 1223388 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 650119 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 1750671 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 2388959 slots
- `HFTcVVrX…` · 148.42 SOL · commission 100% · lag 2388853 slots
- `As9NxA9b…` · 46.58 SOL · commission 100% · lag 2388976 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 445189310 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 350299 slots

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
| Jito tip-floor run-rate (NOT REV) | $38.18K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 38178 USD; at p95 floor → 2886317 USD. |
| Protocol fees 24h | $14.66M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9990 |
| p90 / p99 | 0.000012 / 0.000157 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.74 | coingecko.simple_price |
| 24h change | -2.52% | coingecko.simple_price |
| Market cap | $60.81B | coingecko.simple_price |
| 24h volume | $3.21B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.91B |
| TVL 1d / 7d / 30d | +0.02% / +2.08% / +24.40% |
| DEX volume 24h | $2.90B · 1d +55.76% · vs-7d-ago +50.52% |
| 7d DEX volume | $16.07B · -11.56% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $14.66M |
| Fees 1d / 7d | +44.97% / +18.04% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $677.89M | -2.21% |
| Raydium AMM | $309.46M | +179.01% |
| BisonFi | $241.45M | +32.54% |
| Orca DEX | $238.90M | +89.04% |
| Meteora DLMM | $223.09M | +82.29% |
| Tessera V | $206.39M | +139.77% |
| HumidiFi | $143.21M | +123.80% |
| Manifest Trade | $133.94M | +14.29% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.59B | -1.46% | +0.65% |
| Kamino Lend | Lending | $1.34B | -0.91% | +5.69% |
| Raydium AMM | Dexs | $1.14B | -1.59% | +2.50% |
| Jupiter Lend | Lending | $1.09B | -2.27% | +1.08% |
| Binance Staked SOL | Liquid Staking | $1.08B | -1.89% | +0.95% |
| Jito Liquid Staking | Liquid Staking | $1.06B | -3.15% | +1.94% |
| BlackRock BUIDL | RWA | $977.90M | +0.00% | +0.38% |
| Jupiter Perpetual Exchange | Derivatives | $753.48M | -1.54% | -1.88% |
| Jupiter Staked SOL | Liquid Staking | $538.95M | -2.11% | -0.08% |
| xStocks | RWA | $447.01M | -1.09% | +1.05% |

## Stablecoins

Solana circulating pegged-USD: **$16.30B**
(1d +0.34% · 7d +4.87%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.35B | +0.62% |
| USDT · Tether | $2.77B | +0.00% |
| USDGO · USDGO | $1.37B | +1.11% |
| USD1 · World Liberty Financial USD | $1.26B | +0.64% |
| BUIDL · BlackRock USD | $977.90M | 0.00% |
| PYUSD · PayPal USD | $731.61M | -2.76% |
| USDG · Global Dollar | $574.81M | -1.29% |
| USDe · Ethena USDe | $535.69M | -0.11% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 79 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 79 · priced-subset mcap $287.53M (lower bound, not a census).
24h volume $66.90M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $447.01M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 79 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.36B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $977.90M
- **xStocks** (RWA) — $447.01M
- **OnRe** (RWA) — $302.62M
- **Huma Finance V2** (RWA) — $186.52M
- **Ondo Yield Assets** (RWA) — $180.02M
- **Hastra** (RWA) — $154.70M
- **Ondo Global Markets** (RWA) — $26.13M
- **Plume Vaults** (RWA) — $24.03M

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

- [RT by @solana: Introducing: ✦ Abstract Markets https://x.com/i/article/2093297250650796032](https://x.com/kar888l/status/2096990586297290924) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 15:54:50 GMT
- [RT by @solana: ZEC-backed credit is now live on Solana.

Introducing the ZCASH Market on Kamino, curated by @AllezLabs.

ZEC holders can supply ZEC as collateral and borrow USDC against their position in a fully isolated market on Kamino.](https://x.com/kamino/status/2097066296592777447) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 20:55:41 GMT
- [RT by @solana: We built the end-to-end CLI for funding and growing a startup.

"Claude, launch a fundraise and give my top referrers 1% of my business."

One command opens your round. The next one puts ownership in your users' hands.](https://x.com/stardotfun/status/2097057882814734547) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 20:22:15 GMT
- [Start the week with @WSOP poker https://x.com/i/broadcasts/1dKrPrNNAwwJX](https://x.com/solana/status/2097063901279997970) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 20:46:10 GMT
- [Video](https://x.com/solana/status/2097037299435585682) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 19:00:27 GMT
- [RT by @solana: make a confidential transfer. on Solana. Right now.

live on https://helius.dev/docs/privacy](https://x.com/tilo_cpn/status/2097015389448183872) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 17:33:24 GMT
- [Real estate on Solana with @GetStake](https://x.com/solana/status/2097019704355516800) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 17:50:32 GMT
- [.@kamino is now available as a source of liquidity for onchain yield for @veda_labs 

https://x.com/veda_labs/status/2096992133324611869](https://x.com/solana/status/2097009524469022775) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 17:10:05 GMT
- [RT by @anza_xyz: 200ms
8k txs (40k TPS)
300M CUs (1.5B CUPS)
5.5k shreds (27.5k SPS)

this is the block 🔳 Agave can handle](https://x.com/bw_solana/status/2096250616351965576) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 05 Sep 2026 14:54:28 GMT
- [RT by @anza_xyz: more users
→ more activity
→ problems exposed
→ IBRL
→ more capacity
→ more resilience
→ better products
→ more users

usage & execution is the moat](https://x.com/bw_solana/status/2095876304805740662) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 04 Sep 2026 14:07:05 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: Introducing: ✦ Abstract Markets https://x.com/i/article/2093297250650796032](https://x.com/kar888l/status/2096990586297290924) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 15:54:50 GMT
- [RT by @solana: ZEC-backed credit is now live on Solana.

Introducing the ZCASH Market on Kamino, curated by @AllezLabs.

ZEC holders can supply ZEC as collateral and borrow USDC against their position in a fully isolated market on Kamino.](https://x.com/kamino/status/2097066296592777447) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 20:55:41 GMT
- [RT by @solana: We built the end-to-end CLI for funding and growing a startup.

"Claude, launch a fundraise and give my top referrers 1% of my business."

One command opens your round. The next one puts ownership in your users' hands.](https://x.com/stardotfun/status/2097057882814734547) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 20:22:15 GMT
- [Start the week with @WSOP poker https://x.com/i/broadcasts/1dKrPrNNAwwJX](https://x.com/solana/status/2097063901279997970) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 20:46:10 GMT
- [Video](https://x.com/solana/status/2097037299435585682) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 19:00:27 GMT
- [RT by @solana: make a confidential transfer. on Solana. Right now.

live on https://helius.dev/docs/privacy](https://x.com/tilo_cpn/status/2097015389448183872) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 17:33:24 GMT
- [Real estate on Solana with @GetStake](https://x.com/solana/status/2097019704355516800) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 17:50:32 GMT
- [.@kamino is now available as a source of liquidity for onchain yield for @veda_labs 

https://x.com/veda_labs/status/2096992133324611869](https://x.com/solana/status/2097009524469022775) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 07 Sep 2026 17:10:05 GMT
- [RT by @anza_xyz: 200ms
8k txs (40k TPS)
300M CUs (1.5B CUPS)
5.5k shreds (27.5k SPS)

this is the block 🔳 Agave can handle](https://x.com/bw_solana/status/2096250616351965576) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 05 Sep 2026 14:54:28 GMT
- [RT by @anza_xyz: more users
→ more activity
→ problems exposed
→ IBRL
→ more capacity
→ more resilience
→ better products
→ more users

usage & execution is the moat](https://x.com/bw_solana/status/2095876304805740662) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 04 Sep 2026 14:07:05 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-07 (2026-09-07 16:23:02 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 1050ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 371ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 388ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 386ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 512ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6317ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1023ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 163ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 101ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 149ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 116ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 67ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 71ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 331ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 92ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 92ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 152ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 448ms https://solana.com/data
- `solana.com.databricks` [ok] 200 426ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 531ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 146ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 272ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 138ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 297ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 857ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 546ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 370ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 375ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 365ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1421ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1765ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 198ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 65ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 493ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 400ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1532ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1642ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1832ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2083ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2275ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1660ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1746ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1493ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1974ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2143ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1522ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1589ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1668ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1455ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1710ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1950ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1574ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1728ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2062ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1502ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1793ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 875ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.SPYx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.GOOGLx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.SPYx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.TSLAx` [ok] 200 605ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.AAPLx` [ok] 200 687ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.AMZNx` [ok] 200 723ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.NVDAx` [ok] 200 838ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.TSLAx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.MSFTx` [ok] 200 914ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.AAPLx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 1022ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.mult.SPYx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.NVDAx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.MUUx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.circ.MSFTx` [ok] 200 881ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.GOOGLx` [ok] 200 1374ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 954ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.MSFTx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 510ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.DRAMx` [ok] 200 1217ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.DJTx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.mult.QQQx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 801ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.MVLLx` [ok] 200 1414ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.INTWx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.KORUx` [ok] 200 616ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.MUUx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.KORUx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 891ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.price.SOXSx` [ok] 200 679ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.circ.SNXXx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 2132ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.circ.SOXSx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.AXTIx` [ok] 200 1699ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.mult.SNXXx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.NWGx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.mult.SOXSx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 594ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.SHEINx` [ok] 200 727ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.price.BANKCx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.AXTIx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 1860ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.INTWx` [ok] 200 1973ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.MVLLx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.SHEINx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.INTWx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 815ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 1199ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.NWGx` [ok] 200 1320ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 888ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.LAOPGx` [ok] 200 869ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 608ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.BANKCx` [ok] 200 1988ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 1583ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 392ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.NWGx` [ok] 200 1349ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.SNBIOx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.BANKCx` [ok] 200 877ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 868ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 1240ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 1670ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 1824ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 556ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.HAIDLx` [ok] 200 1394ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.CRESBx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 711ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.KUNLx` [ok] 200 672ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 1438ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 839ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 1104ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 950ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 722ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.KUNLx` [ok] 200 1495ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 855ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 1953ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 1807ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 406ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 1265ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.circ.WXXDCx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.WXXDCx` [ok] 200 666ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 3093ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 1434ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.CSPCx` [ok] 200 1552ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 997ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.MIXUx` [ok] 200 909ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.ASMPTx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 1979ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.MIXUx` [ok] 200 516ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 720ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 1455ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.JTGEXx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.CMENDx` [ok] 200 975ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 875ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.SITCx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.mult.MIXUx` [ok] 200 698ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 431ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.CMENDx` [ok] 200 643ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 499ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.CRESPx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 1889ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.SINOTx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 403ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.CRESMx` [ok] 200 638ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 1184ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.PRADx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 710ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.CTFJWx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 2754ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 2158ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 685ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 714ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 1580ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 743ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.CLPHDx` [ok] 200 693ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.CLONPx` [ok] 200 2387ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 400ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 4818ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 1127ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.CKAHx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 504ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 682ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 1688ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 1269ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 1373ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 733ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.GENTEx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 1409ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 611ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 2049ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.HKEXCx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.mult.CKINFx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.CHONGx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 1170ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.CHONGx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.HNDLDx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 1026ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.PICCx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.COSCx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.NONGx` [ok] 200 1282ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.HNDLDx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 711ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.COVELx` [ok] 200 1392ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 519ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 1531ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.mult.PICCx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.COVELx` [ok] 200 519ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 675ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.HNDLDx` [ok] 200 1015ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 1186ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 1676ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 872ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 516ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 482ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1404ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 330ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.METAx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=METAx
- `jup.tokens.search.MUUx` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.KORUx` [ok] 200 146ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.INTWx` [ok] 200 176ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.MVLLx` [ok] 200 142ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SHEINx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.SNXXx` [ok] 200 92ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jup.tokens.search.DRAMx` [ok] 200 101ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jito.tip_floor` [ok] 200 522ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 309ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 403ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 490ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 366ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 364ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 359ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 257ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
