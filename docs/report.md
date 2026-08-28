# Borealis — Solana ecosystem report

**Generated** 2026-08-28T16:23:30Z · 2026-08-28 09:23:30 PT
**Author** dustycompiler · **Version** 1.5.6 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-28T16:23:18Z · **RPC health** `ok`
**Health score** 100 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 400)/400, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** SURGE — SOL 24h -3.44%; DEX 24h $3.70B · 1d +57% · vs-7d-ago +34%; slot 323 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +47.11%. (threshold: `|7d %| >= 20`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 104.01 USD is +36.8% vs 30d median 76.00 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **WARN · TPS vs 30d median (solana.com/data tx/86400)** — Current 5,140.82 TPS is +43.4% vs 30d median 3,584.53 TPS (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Daily active addresses vs 30d median** — Current 786,740.00 is +20.3% vs 30d median 653,923.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +57.34%. (threshold: `|1d %| >= 8`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +33.73%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 442,378,878 |
| Block height | 420,427,009 |
| Block time | 2026-08-28T16:23:18Z |
| Epoch | 1,024 (2.52% · slot 10,879/432,000) |
| Mean TPS (last ~3,600s) | 5,140.8 |
| Mean non-vote TPS | 3,027.2 |
| Median TPS (same window) | 5,093.8 |
| Mean slot time | 323.3 ms |
| Median slot time | 320.9 ms |
| Transaction count (cluster) | 542,787,735,098 |
| Circulating supply | 584,162,702 SOL |
| Total supply | 633,079,891 SOL |
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
| Activated stake | 436,095,791 SOL |
| Delinquent stake | 38,497.86 SOL (0.009%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.15% / 35.47% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 16.99M SOL | 3.90% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.04M SOL | 3.68% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.39M SOL | 2.84% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.46M SOL | 2.63% | 5% | 0 |
| 5 | `C8Bey3LK…` | 9.29M SOL | 2.13% | 7% | 0 |
| 6 | `E1r4Psq8…` | 9.08M SOL | 2.08% | 0% | 0 |
| 7 | `CAo1dCGY…` | 9.00M SOL | 2.06% | 10% | 0 |
| 8 | `9eGrDohd…` | 7.29M SOL | 1.67% | 5% | 0 |
| 9 | `EvnRmnMr…` | 7.19M SOL | 1.65% | 7% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.10M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.60M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `mrgn4atx…` · 20.33K SOL · commission 0% · lag 61714 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1126199 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 32177 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 395124 slots
- `kom1oNHy…` · 662.86 SOL · commission 5% · lag 1742362 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 442378878 slots
- `pSo1KZXg…` · 2.00 SOL · commission 4% · lag 41037 slots
- `7Dvp5zCF…` · 1.07 SOL · commission 100% · lag 199523 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 1738879 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 37 | data/history.jsonl snapshot tape |
| TVL chart | 37 | data/history.jsonl snapshot tape |
| SOL chart | 36 | data/history.jsonl snapshot tape |
| history.jsonl rows | 37 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$1.14M** (10,859.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 |
| **Solana REV** | **13,424.0 SOL** / **$1.40M** | MEASURED UTC calendar day 2026-08-27: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-27 · UTC day 2026-08-27 · SOL-USD date 2026-08-27 |
| Jito tip-floor run-rate (NOT REV) | $68.99K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 68989 USD; at p95 floor → 2872228 USD. |
| Protocol fees 24h | $16.30M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~3.0h · n_tx=2240 window_seconds=10834 |
| p90 / p99 | 0.000018 / 0.000314 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $104.01 | coingecko.simple_price |
| 24h change | -3.44% | coingecko.simple_price |
| Market cap | $60.74B | coingecko.simple_price |
| 24h volume | $6.15B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.87B |
| TVL 1d / 7d / 30d | +1.63% / +10.05% / +22.41% |
| DEX volume 24h | $3.70B · 1d +57.34% · vs-7d-ago +33.73% |
| 7d DEX volume | $22.25B · +72.25% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $16.30M |
| Fees 1d / 7d | +7.19% / +47.11% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $1.46B | +90.88% |
| BisonFi | $416.99M | +65.84% |
| Orca DEX | $317.30M | +6.58% |
| Meteora DLMM | $245.52M | +32.85% |
| Raydium AMM | $170.42M | +2.49% |
| Axiom | $165.79M | +31.24% |
| Manifest Trade | $160.72M | +33.75% |
| pump.fun | $144.47M | +127.22% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.61B | +1.73% | +18.57% |
| Kamino Lend | Lending | $1.23B | -0.20% | +5.54% |
| Raydium AMM | Dexs | $1.14B | +0.05% | +12.78% |
| Binance Staked SOL | Liquid Staking | $1.08B | +0.80% | +18.36% |
| Jupiter Lend | Lending | $1.08B | -3.29% | +3.08% |
| Jito Liquid Staking | Liquid Staking | $1.06B | +0.77% | +16.39% |
| BlackRock BUIDL | RWA | $886.54M | -0.01% | +2.04% |
| Jupiter Perpetual Exchange | Derivatives | $784.94M | +0.68% | +6.14% |
| Jupiter Staked SOL | Liquid Staking | $555.25M | -0.36% | +16.18% |
| xStocks | RWA | $438.22M | -0.27% | +4.31% |

## Stablecoins

Solana circulating pegged-USD: **$15.82B**
(1d +0.55% · 7d -0.84%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.96B | -0.34% |
| USDT · Tether | $2.84B | +0.00% |
| USDGO · USDGO | $1.25B | -0.01% |
| USD1 · World Liberty Financial USD | $1.14B | +0.44% |
| BUIDL · BlackRock USD | $886.52M | +0.02% |
| PYUSD · PayPal USD | $681.47M | -0.47% |
| USDG · Global Dollar | $619.58M | +0.95% |
| USDe · Ethena USDe | $535.04M | -0.40% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 80 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 80 · priced-subset mcap $283.57M (lower bound, not a census).
24h volume $37.82M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $438.22M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 80 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.54M
- **xStocks** (RWA) — $438.22M
- **OnRe** (RWA) — $283.72M
- **Ondo Yield Assets** (RWA) — $179.89M
- **Hastra** (RWA) — $158.06M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $25.15M
- **Plume Vaults** (RWA) — $22.85M

## Daily active addresses

786,740 (Allium, as of 2026-08-27). Provider range 387,557–903,429. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Details: https://governance.solana.com/proposals](https://x.com/solana/status/2093367687661371720) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 15:58:44 GMT
- [Solana Validator Governance has concluded.

Results:

✅ SGP-0001: The Solana Constitution 
✅ SGP-0002: Double Disinflation
❌ SGP-0003: Resource and Inclusion Fee](https://x.com/solana/status/2093367686017245668) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 15:58:43 GMT
- [30 million hours a day. 

Go get them back in the @commonsmade hackathon.](https://x.com/solana/status/2093363055510069747) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 15:40:19 GMT
- [solana.com/200ms](https://x.com/solana/status/2093362857996120269) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 15:39:32 GMT
- [300ms](https://x.com/solana/status/2093362625606554051) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 15:38:37 GMT `mainnet`
- [New episode of The Privacy Show today @ 2 PM ET

@catmcgee sits down with @gegelz and @Maxwolfj to talk all things privacy.](https://x.com/solana/status/2093343106636607926) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 14:21:03 GMT
- [1 hour and 40 minutes left

It’s time to vote:

https://governance.solana.com](https://x.com/solana/status/2093334736643244113) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 13:47:48 GMT
- [0 to $500M on Solana in 12 months. 

@xStocksFi 🤝 @solana](https://x.com/solana/status/2093325148552380769) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 13:09:42 GMT
- [300ms slots just activated on mainnet.

400 → 350 → 300ms

2 more steps to 200ms.](https://x.com/anza_xyz/status/2093361495442911713) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 15:34:07 GMT `mainnet`
- [300ms going effective in about 12 hours boys](https://x.com/anza_xyz/status/2093176749643403549) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 03:20:01 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [Details: https://governance.solana.com/proposals](https://x.com/solana/status/2093367687661371720) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 15:58:44 GMT
- [Solana Validator Governance has concluded.

Results:

✅ SGP-0001: The Solana Constitution 
✅ SGP-0002: Double Disinflation
❌ SGP-0003: Resource and Inclusion Fee](https://x.com/solana/status/2093367686017245668) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 15:58:43 GMT
- [30 million hours a day. 

Go get them back in the @commonsmade hackathon.](https://x.com/solana/status/2093363055510069747) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 15:40:19 GMT
- [solana.com/200ms](https://x.com/solana/status/2093362857996120269) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 15:39:32 GMT
- [300ms](https://x.com/solana/status/2093362625606554051) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 15:38:37 GMT `mainnet`
- [New episode of The Privacy Show today @ 2 PM ET

@catmcgee sits down with @gegelz and @Maxwolfj to talk all things privacy.](https://x.com/solana/status/2093343106636607926) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 14:21:03 GMT
- [1 hour and 40 minutes left

It’s time to vote:

https://governance.solana.com](https://x.com/solana/status/2093334736643244113) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 13:47:48 GMT
- [0 to $500M on Solana in 12 months. 

@xStocksFi 🤝 @solana](https://x.com/solana/status/2093325148552380769) — X/Nitter-style RSS @solana (not Twitter API) · Fri, 28 Aug 2026 13:09:42 GMT
- [300ms slots just activated on mainnet.

400 → 350 → 300ms

2 more steps to 200ms.](https://x.com/anza_xyz/status/2093361495442911713) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 15:34:07 GMT `mainnet`
- [300ms going effective in about 12 hours boys](https://x.com/anza_xyz/status/2093176749643403549) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 03:20:01 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-28 (2026-08-28 09:23:30 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~323 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~323 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 128ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 127ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 74ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 101ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 140ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7411ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 177ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 191ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 48ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 342ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 79ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 80ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 3268ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 276ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 102ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 184ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 152ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 361ms https://solana.com/data
- `solana.com.databricks` [ok] 200 239ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 488ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 146ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 260ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 178ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 307ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 542ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 191ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 155ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 187ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 367ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1696ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1679ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1524ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 194ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 106ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 108ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 518ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 594ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 656ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 654ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1049ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 782ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 892ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 854ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 876ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 598ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 720ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 609ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 662ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 621ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 3851ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 3510ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2422ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1285ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2139ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 4390ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1934ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 904ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.METAx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.TSLAx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.MSFTx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.AAPLx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.NVDAx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.SPYx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.MSFTx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.price.GOOGLx` [ok] 200 871ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.COINx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.QQQx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.COINx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 1275ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 768ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.AMZNx` [ok] 200 1579ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.SUOPTx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.AMZNx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.NVDAx` [ok] 200 1505ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.BANKCx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 1426ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.TSLAx` [ok] 200 838ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.MMGx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.QQQx` [ok] 200 1472ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.price.KUNLx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 800ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 712ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 684ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 1048ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.WRFHDx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 745ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.SZIGHx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 570ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.CMERPx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.CMERPx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.CSPCx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.JTGEXx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.WXXDCx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.CRESMx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.CMENDx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 1215ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 1465ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.circ.WXXDCx` [ok] 200 1018ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 556ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 1841ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.WXXDCx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.ASMPTx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 5705ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 431ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.CRESPx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 784ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 968ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.CRESPx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 3577ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.PRADx` [ok] 200 630ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.SINOTx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 2626ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.PRADx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 1135ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.CLONPx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.SINOx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.WHGROx` [ok] 200 575ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 621ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.WHGROx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 6370ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.MIXUx` [ok] 200 4129ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 830ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.CKAHx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.HKEXCx` [ok] 200 397ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.price.KUAIx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.price.CHONGx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 1360ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.KUAIx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.mult.CKINFx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.COVELx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.HNDLDx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.COSCx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.PICCx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.COSCx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 705ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.price.BOCOMx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.circ.CKHUTx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.price.CPETCx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.price.BOCHKx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.circ.BOCOMx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.circ.CPETCx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.circ.BOCHKx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.BOCOMx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.mult.CPETCx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.price.CITICx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.price.POPMTx` [ok] 200 710ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.mult.BOCHKx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.price.CRESLx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.price.ANTASx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.price.HAIERx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.circ.POPMTx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.circ.ANTASx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.circ.CRESLx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.circ.HAIERx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.mult.POPMTx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.mult.CRESLx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.mult.HAIERx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.price.ZJGLDx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.circ.ZJGLDx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.price.ICBCx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.mult.ZJGLDx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.price.PSBOCx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.circ.ICBCx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.mult.CHONGx` [ok] 200 2614ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.PSBOCx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.mult.ICBCx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `xstocks.mult.ANTASx` [ok] 200 890ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.circ.CITICx` [ok] 200 1315ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 4560ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.PSBOCx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.CITICx` [ok] 200 742ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 4880ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.GEELx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1295ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 71ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 53ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 55ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 54ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.SINOTx` [ok] 200 62ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 240ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 366ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 89ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 106ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 77ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 77ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 213ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 196ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.6 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
