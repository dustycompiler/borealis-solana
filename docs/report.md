# Borealis — Solana ecosystem report

**Generated** 2026-09-06T05:22:45Z · 2026-09-05 22:22:45 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-06T05:22:35Z · **RPC health** `ok`
**Health score** 96 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +4.02%; DEX 24h $1.96B · 1d +4% · vs-7d-ago +17%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

No flags vs rolling baseline (60 samples / llama 7d). Watching.

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 444,712,087 |
| Block height | 422,756,473 |
| Block time | 2026-09-06T05:22:35Z |
| Epoch | 1,029 (42.61% · slot 184,091/432,000) |
| Mean TPS (last ~3,600s) | 3,552.0 |
| Mean non-vote TPS | 1,431.1 |
| Median TPS (same window) | 3,475.1 |
| Mean slot time | 316.8 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 545,589,045,652 |
| Circulating supply | 585,445,396 SOL |
| Total supply | 633,549,271 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 18 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 438,854,866 SOL |
| Delinquent stake | 393,953.69 SOL (0.090%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.28% / 35.56% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.42M SOL | 3.97% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.32M SOL | 3.72% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.51M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.37M SOL | 2.59% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.56M SOL | 2.18% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.27M SOL | 2.11% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.35M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.13M SOL | 1.62% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.50% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.39% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.64M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.85M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `D1Vbgkrh…` · 314.95K SOL · commission 0% · lag 2458 slots
- `xLabscif…` · 28.57K SOL · commission 5% · lag 923714 slots
- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 87129 slots
- `prt1st4R…` · 13.11K SOL · commission 5% · lag 1225145 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 1363364 slots
- `5ZjxMYBb…` · 4.06K SOL · commission 0% · lag 746165 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1925966 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 172896 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 1273448 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1911736 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1953250 slots
- `HFTcVVrX…` · 148.42 SOL · commission 100% · lag 1911630 slots

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
| **In-protocol fees 24h** | **$528.86K** (5,211.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-04 |
| **Solana REV** | **6,254.6 SOL** / **$634.77K** | MEASURED UTC calendar day 2026-09-04: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-04 · UTC day 2026-09-04 · SOL-USD date 2026-09-04 |
| Jito tip-floor run-rate (NOT REV) | $159.06K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 159058 USD; at p95 floor → 2090284 USD. |
| Protocol fees 24h | $10.48M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9966 |
| p90 / p99 | 0.000010 / 0.000099 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $105.78 | coingecko.simple_price |
| 24h change | +4.02% | coingecko.simple_price |
| Market cap | $61.86B | coingecko.simple_price |
| 24h volume | $3.01B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.92B |
| TVL 1d / 7d / 30d | +1.11% / +0.23% / +25.46% |
| DEX volume 24h | $1.96B · 1d +4.20% · vs-7d-ago +17.35% |
| 7d DEX volume | $14.51B · -24.36% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $10.48M |
| Fees 1d / 7d | +0.44% / -6.19% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $693.23M | +123.14% |
| BisonFi | $251.95M | 0.00% |
| Orca DEX | $129.40M | -48.31% |
| Raydium AMM | $125.28M | -19.51% |
| Manifest Trade | $123.28M | -24.20% |
| Meteora DLMM | $122.38M | -32.26% |
| Jupiterz | $64.61M | 0.00% |
| Scorch | $63.08M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.59B | +2.42% | -0.69% |
| Kamino Lend | Lending | $1.33B | +0.86% | +6.19% |
| Raydium AMM | Dexs | $1.12B | +1.46% | -1.37% |
| Jupiter Lend | Lending | $1.11B | +1.53% | +1.16% |
| Binance Staked SOL | Liquid Staking | $1.08B | +1.65% | -0.68% |
| Jito Liquid Staking | Liquid Staking | $1.07B | +3.06% | +1.01% |
| BlackRock BUIDL | RWA | $977.90M | -0.00% | +0.60% |
| Jupiter Perpetual Exchange | Derivatives | $758.00M | +0.84% | -1.93% |
| Jupiter Staked SOL | Liquid Staking | $540.36M | +2.55% | -1.14% |
| xStocks | RWA | $450.35M | +0.68% | +4.28% |

## Stablecoins

Solana circulating pegged-USD: **$16.35B**
(1d +0.48% · 7d +3.38%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.36B | +1.24% |
| USDT · Tether | $2.77B | -0.00% |
| USDGO · USDGO | $1.36B | 0.00% |
| USD1 · World Liberty Financial USD | $1.26B | +0.62% |
| BUIDL · BlackRock USD | $977.90M | 0.00% |
| PYUSD · PayPal USD | $752.07M | +4.47% |
| USDG · Global Dollar | $579.49M | +0.02% |
| USDe · Ethena USDe | $536.37M | +0.56% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 78 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 78 · priced-subset mcap $287.63M (lower bound, not a census).
24h volume $43.79M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $450.35M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 78 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.36B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $977.90M
- **xStocks** (RWA) — $450.35M
- **OnRe** (RWA) — $299.20M
- **Huma Finance V2** (RWA) — $191.37M
- **Ondo Yield Assets** (RWA) — $180.01M
- **Hastra** (RWA) — $150.50M
- **Ondo Global Markets** (RWA) — $25.94M
- **Plume Vaults** (RWA) — $24.03M

## Daily active addresses

855,572 (Allium, as of 2026-09-04). Provider range 443,957–880,805. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Encrypt the memes](https://x.com/solana/status/2096403741947613380) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 01:02:56 GMT
- [Solana handled 5 billion transactions in August, an unfathomable level of activity that exceeded all other networks combined.

That's more than 100,000 every minute.

And it did this while keeping fees orders of magnitude lower than other chains.](https://x.com/solana/status/2096360656597369132) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 22:11:43 GMT
- [Are the aces in their favor? 

World Series of Poker (@WSOP) Super Circuit Canada continues  https://x.com/i/broadcasts/1YGNrbEXXPNGw](https://x.com/solana/status/2096339948035031463) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 20:49:26 GMT
- [RT by @solana: StonkFun is now live on @Raydium LaunchLab.

All new StonkFun deployments now launch through LaunchLab, with cheaper deployment costs, reduced sniper risk, and compounding liquidity after bonding.

https://stonkfun.xyz/launch](https://x.com/LaunchOnSF/status/2096315023731675202) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 19:10:23 GMT
- [RT by @solana: Want to host an event at your school with @Solana? 🎓

Solana Across Campuses is a global initiative powered by http://College.xyz and @SolanaFndn, bringing events to universities around the world over one week.

The goal is simple: onboard more students into crypto.

Hosts will receive USDC stipends to seed wallets, order pizza, and bring their campus together 🍕

Apply to host an event at your school ↓
https://luma.com/295pf7k7?tk=xxDvFB](https://x.com/college_xyz/status/2096282255270543436) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 17:00:11 GMT
- [Fast, cheap and reliable. Solana.](https://x.com/solana/status/2096267114998886657) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 16:00:01 GMT
- [RT by @solana: 200ms
8k txs (40k TPS)
300M CUs (1.5B CUPS)
5.5k shreds (27.5k SPS)

this is the block 🔳 Agave can handle](https://x.com/bw_solana/status/2096250616351965576) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 14:54:28 GMT
- [x.com/i/article/209620676578…](https://x.com/solana/status/2096206771232923652) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 12:00:14 GMT
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

- [Encrypt the memes](https://x.com/solana/status/2096403741947613380) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 01:02:56 GMT
- [Solana handled 5 billion transactions in August, an unfathomable level of activity that exceeded all other networks combined.

That's more than 100,000 every minute.

And it did this while keeping fees orders of magnitude lower than other chains.](https://x.com/solana/status/2096360656597369132) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 22:11:43 GMT
- [Are the aces in their favor? 

World Series of Poker (@WSOP) Super Circuit Canada continues  https://x.com/i/broadcasts/1YGNrbEXXPNGw](https://x.com/solana/status/2096339948035031463) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 20:49:26 GMT
- [RT by @solana: StonkFun is now live on @Raydium LaunchLab.

All new StonkFun deployments now launch through LaunchLab, with cheaper deployment costs, reduced sniper risk, and compounding liquidity after bonding.

https://stonkfun.xyz/launch](https://x.com/LaunchOnSF/status/2096315023731675202) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 19:10:23 GMT
- [RT by @solana: Want to host an event at your school with @Solana? 🎓

Solana Across Campuses is a global initiative powered by http://College.xyz and @SolanaFndn, bringing events to universities around the world over one week.

The goal is simple: onboard more students into crypto.

Hosts will receive USDC stipends to seed wallets, order pizza, and bring their campus together 🍕

Apply to host an event at your school ↓
https://luma.com/295pf7k7?tk=xxDvFB](https://x.com/college_xyz/status/2096282255270543436) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 17:00:11 GMT
- [Fast, cheap and reliable. Solana.](https://x.com/solana/status/2096267114998886657) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 16:00:01 GMT
- [RT by @solana: 200ms
8k txs (40k TPS)
300M CUs (1.5B CUPS)
5.5k shreds (27.5k SPS)

this is the block 🔳 Agave can handle](https://x.com/bw_solana/status/2096250616351965576) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 14:54:28 GMT
- [x.com/i/article/209620676578…](https://x.com/solana/status/2096206771232923652) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 12:00:14 GMT
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

_As of 2026-09-06 (2026-09-05 22:22:45 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 726 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 542ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 726ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 641ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 523ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 623ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6545ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1063ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 46ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 66ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 47ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 31ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 27ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 2016ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 79ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 41ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 50ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 77ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 318ms https://solana.com/data
- `solana.com.databricks` [ok] 200 89ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 450ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 234ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 47ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 123ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 346ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 735ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 155ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 150ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 159ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 231ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1756ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1832ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 815ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 278ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 554ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 721ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2278ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2619ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2359ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2072ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1977ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2689ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2561ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2139ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1878ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2386ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2023ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2338ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1825ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1960ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 3831ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1348ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1736ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1483ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 4154ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2363ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1381ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1376ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.NVDAx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.METAx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.TSLAx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.AMZNx` [ok] 200 456ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.NVDAx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.AAPLx` [ok] 200 755ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.TSLAx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.price.SPYx` [ok] 200 937ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.AAPLx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.QQQx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.COINx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.SPYx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 1023ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 689ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.GOOGLx` [ok] 200 1483ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.MSFTx` [ok] 200 1511ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.mult.QQQx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.MVLLx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.mult.COINx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.GOOGLx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.MUUx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.mult.METAx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.DJTx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.MSFTx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.AXTIx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.circ.AXTIx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.INTWx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.KORUx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.circ.INTWx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 1292ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 653ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 867ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.price.SOXSx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.mult.AXTIx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.INTWx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.SOXSx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.price.SNXXx` [ok] 200 656ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.price.SHEINx` [ok] 200 776ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.mult.SOXSx` [ok] 200 675ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 911ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.MUUx` [ok] 200 2550ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 554ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.MUUx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.circ.SNXXx` [ok] 200 1323ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.circ.BANKCx` [ok] 200 1530ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.MVLLx` [ok] 200 3186ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 1288ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.LAOPGx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 1589ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.SHEINx` [ok] 200 912ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.SNXXx` [ok] 200 1180ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 1145ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 2045ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 606ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 971ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 710ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.SNBIOx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 754ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.KUNLx` [ok] 200 999ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.KUNLx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 528ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 1538ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 631ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 1391ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 695ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 1091ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.SMOIHx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 2089ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 4564ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 1320ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 5526ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 1457ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.HRZRBx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.CRESBx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 1098ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 394ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.CSPCx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 1136ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 1848ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.CMERPx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 2094ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.CMERPx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 1612ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 583ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.TNGYIx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 973ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.CSPCx` [ok] 200 319ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.ASMPTx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.BDWAPx` [ok] 200 731ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.WHRFRx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 1016ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.MIXUx` [ok] 200 873ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 1511ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 2299ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 1580ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 2168ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.SNDSCx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.JDHLTx` [ok] 200 692ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 1953ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 1297ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 530ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.PRADx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.CLONPx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.CTFJWx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.NWGx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SINOTx` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.CRESPx` [ok] 200 1199ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 1187ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 1630ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 503ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 2328ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 1523ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.NWGx` [ok] 200 1587ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.PRADx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 2472ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.NWGx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.CLPHDx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.CTPCAx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.SNDSCx` [ok] 200 952ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 842ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 1165ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 1191ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 886ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.GENTEx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.SINOx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.circ.CTPCAx` [ok] 200 1057ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 1283ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 3388ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 680ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 361ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.CKAHx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.CRAUTx` [ok] 200 1138ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.CKAHx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 551ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.GENTEx` [ok] 200 1085ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.HKCGAx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 1206ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 618ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 2142ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 878ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 993ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 1292ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.COVELx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.CHONGx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 760ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 1128ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.GEELx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.mult.CKINFx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.KUAIx` [ok] 200 1178ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.NONGx` [ok] 200 1286ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.HNDLDx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 1883ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 1754ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 1281ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 1602ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.MEITx` [ok] 200 2044ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 820ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.PICCx` [ok] 200 1348ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 1227ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 1317ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.circ.COVELx` [ok] 200 3284ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 498ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 1531ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 2829ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 4993ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 1121ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1297ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 118ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.MUUx` [ok] 200 56ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.KORUx` [ok] 200 61ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.INTWx` [ok] 200 54ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.MVLLx` [ok] 200 68ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SNXXx` [ok] 200 55ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jup.tokens.search.DRAMx` [ok] 200 55ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.SHEINx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.SOXSx` [ok] 200 75ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jito.tip_floor` [ok] 200 126ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 220ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 96ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 504ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 784ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 541ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 526ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 140ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
