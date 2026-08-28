# Borealis — Solana ecosystem report

**Generated** 2026-08-28T01:17:26Z · 2026-08-27 18:17:26 PT
**Author** dustycompiler · **Version** 1.5.6 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-28T01:17:13Z · **RPC health** `ok`
**Health score** 100 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 400)/400, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h +8.17%; DEX 24h $2.94B · 1d +25% · vs-7d-ago +6%; slot 366 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +40.93%. (threshold: `|7d %| >= 20`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 108.98 USD is +44.1% vs 30d median 75.65 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **WARN · Large SOL 24h price move** — SOL/USD 24h change is +8.17% (coingecko.simple_price). (threshold: `|24h %| >= 8`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +25.02%. (threshold: `|1d %| >= 8`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 442,228,979 |
| Block height | 420,277,155 |
| Block time | 2026-08-28T01:17:13Z |
| Epoch | 1,023 (67.82% · slot 292,980/432,000) |
| Mean TPS (last ~3,600s) | 3,973.0 |
| Mean non-vote TPS | 2,102.6 |
| Median TPS (same window) | 3,958.3 |
| Mean slot time | 366.2 ms |
| Median slot time | 365.9 ms |
| Transaction count (cluster) | 542,581,512,040 |
| Circulating supply | 584,062,210 SOL |
| Total supply | 632,969,021 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 688 |
| Delinquent | 9 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 436,840,782 SOL |
| Delinquent stake | 44,054.77 SOL (0.010%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 79 |
| Top 10 / 20 stake share | 24.28% / 35.57% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.06M SOL | 3.91% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.03M SOL | 3.67% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.31M SOL | 2.82% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.75M SOL | 2.69% | 5% | 0 |
| 5 | `C8Bey3LK…` | 9.22M SOL | 2.11% | 7% | 0 |
| 6 | `E1r4Psq8…` | 9.05M SOL | 2.07% | 0% | 0 |
| 7 | `CAo1dCGY…` | 8.90M SOL | 2.04% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.85M SOL | 1.80% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.30M SOL | 1.67% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.58M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.06M SOL | 1.39% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.93M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.64M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `mrgn4atx…` · 23.80K SOL · commission 0% · lag 124973 slots
- `gangtCrQ…` · 16.43K SOL · commission 0% · lag 976300 slots
- `ChaossRP…` · 1.42K SOL · commission 0% · lag 245225 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 1216613 slots
- `kom1oNHy…` · 1.06K SOL · commission 5% · lag 1592463 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 442228979 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 58180109 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 49624 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 1588980 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 36 | data/history.jsonl snapshot tape |
| TVL chart | 36 | data/history.jsonl snapshot tape |
| SOL chart | 35 | data/history.jsonl snapshot tape |
| history.jsonl rows | 36 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$930.30K** (9,612.4 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-26 |
| **Solana REV** | **12,104.8 SOL** / **$1.17M** | MEASURED UTC calendar day 2026-08-26: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-26 · UTC day 2026-08-26 · SOL-USD date 2026-08-26 |
| Jito tip-floor run-rate (NOT REV) | $238.36K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 238360 USD; at p95 floor → 18514787 USD. |
| Protocol fees 24h | $15.62M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9951 |
| p90 / p99 | 0.000014 / 0.000259 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $108.98 | coingecko.simple_price |
| 24h change | +8.17% | coingecko.simple_price |
| Market cap | $63.65B | coingecko.simple_price |
| 24h volume | $7.07B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.01B |
| TVL 1d / 7d / 30d | +7.17% / +14.97% / +24.71% |
| DEX volume 24h | $2.94B · 1d +25.02% · vs-7d-ago +6.26% |
| 7d DEX volume | $20.43B · +58.17% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $15.62M |
| Fees 1d / 7d | +2.68% / +40.93% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $765.13M | 0.00% |
| BisonFi | $416.99M | +65.84% |
| Orca DEX | $365.65M | +22.82% |
| Meteora DLMM | $245.52M | +32.85% |
| Raydium AMM | $180.41M | +8.50% |
| Manifest Trade | $179.83M | +49.65% |
| pump.fun | $144.47M | +127.22% |
| Axiom | $126.33M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.67B | +9.98% | +27.52% |
| Kamino Lend | Lending | $1.25B | +5.64% | +10.37% |
| Raydium AMM | Dexs | $1.18B | +11.13% | +22.99% |
| Binance Staked SOL | Liquid Staking | $1.13B | +9.26% | +27.38% |
| Jupiter Lend | Lending | $1.11B | +3.01% | +9.05% |
| Jito Liquid Staking | Liquid Staking | $1.10B | +9.52% | +25.19% |
| BlackRock BUIDL | RWA | $886.45M | -0.01% | +2.04% |
| Jupiter Perpetual Exchange | Derivatives | $793.69M | +4.04% | +10.22% |
| Jupiter Staked SOL | Liquid Staking | $568.37M | +9.99% | +24.96% |
| Marinade Native | Staking Pool | $444.80M | +14.20% | +75.27% |

## Stablecoins

Solana circulating pegged-USD: **$15.93B**
(1d -0.12% · 7d -0.23%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.06B | +0.25% |
| USDT · Tether | $2.84B | +0.00% |
| USDGO · USDGO | $1.25B | +0.80% |
| USD1 · World Liberty Financial USD | $1.14B | +2.57% |
| BUIDL · BlackRock USD | $886.45M | +1.15% |
| PYUSD · PayPal USD | $690.74M | +1.72% |
| USDG · Global Dollar | $620.81M | -1.31% |
| USDe · Ethena USDe | $537.76M | +0.10% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 80 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 80 · priced-subset mcap $285.83M (lower bound, not a census).
24h volume $27.73M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $441.84M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 80 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.45M
- **xStocks** (RWA) — $441.01M
- **OnRe** (RWA) — $283.36M
- **Ondo Yield Assets** (RWA) — $179.94M
- **Hastra** (RWA) — $159.00M
- **Theo Network thBill** (RWA) — $26.39M
- **Ondo Global Markets** (RWA) — $25.00M
- **Plume Vaults** (RWA) — $22.86M

## Daily active addresses

750,240 (Allium, as of 2026-08-26). Provider range 391,021–853,883. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: Spin Degenerately, Drink Responsibly. 🎰

👉🏻 https://vending.baxus.co

Only Possible On @Solana, with the support of @EYEKONSTUDIO and the @EcosystemCall](https://x.com/BAXUSco/status/2093024884381348012) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 17:16:33 GMT
- [RT by @solana: Reminder that as @solana’s infrastructure improves, so does its hard money.](https://x.com/ORE/status/2093077412808478881) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 20:45:17 GMT
- [RT by @solana: BREAKING: @xStocksFi passed $500M in assets under management on @Solana, becoming the network’s largest tokenized stock issuer with 700+ 1:1 backed assets.](https://x.com/tokens/status/2093024008581292477) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 17:13:04 GMT
- [From @readycards → @PSAcard Vault → eBay.

Only possible on Solana.](https://x.com/solana/status/2093027441195516020) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 17:26:43 GMT
- [RT by @solana: My country is going through a disaster right now; floods have taken lives and destroyed homes across Nepal.

The ecosystem wants to help, and it's our duty to make that possible. 

I am figuring out a way that enables direct stablecoin donations to the beneficiary bank account, tinkering my way around @altitude, @sphere_labs, and @Stablecoin to see what works best. Nth concrete yet; open to more options/help, 

As of now, the official portal for international donors by @PM_nepal_ accepts Visa and Mastercard. So anyone with access to @KASTxyz, @solflare, @RedotPay, etc can top up with stables and donate through that. This enables the whole crypto ecosystem to donate. 

We built rails for money to move anywhere on the internet. This is the moment they exist for. Any help around this is appreciated.](https://x.com/Ronak0010/status/2093006279891698123) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:02:37 GMT
- [RT by @solana: From 0 to half a billion in a year.

xStocks is now @Solana's leading tokenized stock issuer after crossing $500M in assets under management.

700+ assets. Always 1:1 backed. Live across DeFi.](https://x.com/xStocksFi/status/2093014909596361157) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:36:55 GMT
- [RT by @solana: Ansem explains why he’s bullish on Solana

"Solana is one of the only L1s, cycle over cycle that gets better and better infra wise and builder wise."](https://x.com/luminaries/status/2092998778475143635) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 15:32:49 GMT
- [RT by @solana: Live Now: Final Frontier Traders Showdown in Belgrade

Who will take the win?
https://x.com/i/broadcasts/1wxWjlDRZrkJQ](https://x.com/SolanaEvents/status/2093008774931910747) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:12:32 GMT
- [We keep shipping 👀](https://x.com/anza_xyz/status/2093126581690790223) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 00:00:40 GMT
- [Rent reduction is live on testnet.

Step 1 of SIMD-0437 just activated, the first of five feature gates cutting Solana's storage cost per byte by 90% overall.

End state after all five steps: lamports_per_byte drops 6,960 → 696. A token account's rent-exempt deposit goes from ~$0.16 to ~$0.016.

Cheaper accounts = cheaper deployments.](https://x.com/anza_xyz/status/2093038225443246227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 27 Aug 2026 18:09:34 GMT `upgrade`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: Spin Degenerately, Drink Responsibly. 🎰

👉🏻 https://vending.baxus.co

Only Possible On @Solana, with the support of @EYEKONSTUDIO and the @EcosystemCall](https://x.com/BAXUSco/status/2093024884381348012) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 17:16:33 GMT
- [RT by @solana: Reminder that as @solana’s infrastructure improves, so does its hard money.](https://x.com/ORE/status/2093077412808478881) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 20:45:17 GMT
- [RT by @solana: BREAKING: @xStocksFi passed $500M in assets under management on @Solana, becoming the network’s largest tokenized stock issuer with 700+ 1:1 backed assets.](https://x.com/tokens/status/2093024008581292477) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 17:13:04 GMT
- [From @readycards → @PSAcard Vault → eBay.

Only possible on Solana.](https://x.com/solana/status/2093027441195516020) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 17:26:43 GMT
- [RT by @solana: My country is going through a disaster right now; floods have taken lives and destroyed homes across Nepal.

The ecosystem wants to help, and it's our duty to make that possible. 

I am figuring out a way that enables direct stablecoin donations to the beneficiary bank account, tinkering my way around @altitude, @sphere_labs, and @Stablecoin to see what works best. Nth concrete yet; open to more options/help, 

As of now, the official portal for international donors by @PM_nepal_ accepts Visa and Mastercard. So anyone with access to @KASTxyz, @solflare, @RedotPay, etc can top up with stables and donate through that. This enables the whole crypto ecosystem to donate. 

We built rails for money to move anywhere on the internet. This is the moment they exist for. Any help around this is appreciated.](https://x.com/Ronak0010/status/2093006279891698123) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:02:37 GMT
- [RT by @solana: From 0 to half a billion in a year.

xStocks is now @Solana's leading tokenized stock issuer after crossing $500M in assets under management.

700+ assets. Always 1:1 backed. Live across DeFi.](https://x.com/xStocksFi/status/2093014909596361157) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:36:55 GMT
- [RT by @solana: Ansem explains why he’s bullish on Solana

"Solana is one of the only L1s, cycle over cycle that gets better and better infra wise and builder wise."](https://x.com/luminaries/status/2092998778475143635) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 15:32:49 GMT
- [RT by @solana: Live Now: Final Frontier Traders Showdown in Belgrade

Who will take the win?
https://x.com/i/broadcasts/1wxWjlDRZrkJQ](https://x.com/SolanaEvents/status/2093008774931910747) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:12:32 GMT
- [We keep shipping 👀](https://x.com/anza_xyz/status/2093126581690790223) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 00:00:40 GMT
- [Rent reduction is live on testnet.

Step 1 of SIMD-0437 just activated, the first of five feature gates cutting Solana's storage cost per byte by 90% overall.

End state after all five steps: lamports_per_byte drops 6,960 → 696. A token account's rent-exempt deposit goes from ~$0.16 to ~$0.016.

Cheaper accounts = cheaper deployments.](https://x.com/anza_xyz/status/2093038225443246227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 27 Aug 2026 18:09:34 GMT `upgrade`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-28 (2026-08-27 18:17:26 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=activated-not-yet-effective, 250ms=pending, 200ms=pending. Observed mean slot ~366 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `on-chain` — On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=activated-not-yet-effective, 250ms=pending, 200ms=pending.
- `observed` — Observed mean slot ~366 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **xStocks** — priced up to 80 of 715 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 288ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 164ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 248ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 200ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 188ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 8053ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 284ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 137ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 119ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 126ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 80ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 721ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1036ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 241ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 113ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 108ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 855ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 305ms https://solana.com/data
- `solana.com.databricks` [ok] 200 164ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 168ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 128ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 288ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 162ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 217ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 705ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 247ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 248ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 249ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 2255ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 266ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 278ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 270ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 175ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 140ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 141ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 678ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 714ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1023ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 849ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 801ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 843ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 839ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 803ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 787ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 929ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 677ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 640ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 772ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 801ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2493ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1227ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 3500ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 4057ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1796ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2921ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1876ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.SPYx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.AMZNx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.AAPLx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.GOOGLx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.METAx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.NVDAx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.SPYx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.MSFTx` [ok] 200 529ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.NVDAx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.AMZNx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.MSFTx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.price.QQQx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.MMGx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.COINx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.MSFTx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 432ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.price.SUOPTx` [ok] 200 521ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.COINx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.QQQx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 513ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.LAOPGx` [ok] 200 796ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.SNBIOx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 729ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.CTINSx` [ok] 200 1068ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.SZIGHx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.CTINSx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 1113ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 440ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 1183ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 933ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.JTGEXx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.CRESMx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.CMERPx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 528ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 1260ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.CSPCx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 403ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 1219ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.CSPCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.CRESMx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.MIXUx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 2535ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.circ.WXXDCx` [ok] 200 819ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.JDHLTx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.mult.WXXDCx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.PRADx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.ASMPTx` [ok] 200 831ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.CRESPx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 750ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.CTFJWx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.CRESPx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.CTFJWx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 786ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 879ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 1350ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 484ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 1103ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.SINOTx` [ok] 200 1019ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.PWAHLx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.WHGROx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 608ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 789ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.GENTEx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.SITCx` [ok] 200 1639ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 743ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 852ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.CTPCAx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.GENTEx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 1900ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 1474ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 615ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.KUAIx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.CKAHx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 1640ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 770ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.CKINFx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.COVELx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 365ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 1025ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 951ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.CHONGx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.NONGx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.GEELx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.MTRCPx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.COVELx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.MTRCPx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.COSCx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.COVELx` [ok] 200 542ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.COSCx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 622ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 931ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.COSCx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 977ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 1664ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.CITICx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.price.BOCOMx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.mult.CKHUTx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 847ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.price.CPETCx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.circ.BOCOMx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.price.ANTASx` [ok] 200 601ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.price.BOCHKx` [ok] 200 693ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.mult.BOCOMx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.price.CRESLx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.price.POPMTx` [ok] 200 1063ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.circ.CPETCx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.circ.BOCHKx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.price.HAIERx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.circ.ANTASx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.circ.CRESLx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.price.ZJGLDx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.mult.CPETCx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.circ.ZJGLDx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.circ.CITICx` [ok] 200 1027ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.price.PSBOCx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.mult.ZJGLDx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.mult.ANTASx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.circ.POPMTx` [ok] 200 848ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.mult.CITICx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.price.ICBCx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.mult.POPMTx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.mult.CRESLx` [ok] 200 1251ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.mult.BOCHKx` [ok] 200 1400ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.circ.HAIERx` [ok] 200 1609ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.mult.HAIERx` [ok] 200 736ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.circ.ICBCx` [ok] 200 1677ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.circ.PSBOCx` [ok] 200 2216ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.mult.ICBCx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `xstocks.mult.PSBOCx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1507ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 168ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 98ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 88ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 82ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.KUAIx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.MIXUx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.BANKCx` [ok] 200 90ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.HAIDLx` [ok] 200 110ms https://lite-api.jup.ag/tokens/v2/search?query=HAIDLx
- `jup.tokens.search.SINOTx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 159ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 288ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 188ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 148ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 153ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 153ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 151ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 487ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.6 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
