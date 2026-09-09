# Borealis — Solana ecosystem report

**Generated** 2026-09-09T17:38:01Z · 2026-09-09 10:38:01 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-09T17:37:51Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h -0.40%; DEX 24h $2.71B · 1d -0% · vs-7d-ago +25%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +31.01%. (threshold: `|7d %| >= 20`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +24.83%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 445,669,619 |
| Block height | 423,713,170 |
| Block time | 2026-09-09T17:37:51Z |
| Epoch | 1,031 (64.26% · slot 277,619/432,000) |
| Mean TPS (last ~3,600s) | 4,195.0 |
| Mean non-vote TPS | 2,060.6 |
| Median TPS (same window) | 4,186.9 |
| Mean slot time | 316.2 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 546,765,095,521 |
| Circulating supply | 586,250,302 SOL |
| Total supply | 633,736,528 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 679 |
| Delinquent | 9 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 438,631,131 SOL |
| Delinquent stake | 22,373.50 SOL (0.005%) |
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

- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 2320896 slots
- `prt1st4R…` · 5.87K SOL · commission 5% · lag 2182677 slots
- `xLabscif…` · 4.17K SOL · commission 5% · lag 1881246 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 1703697 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 170863 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 342736 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 445669619 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 61620749 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 830608 slots

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
| Jito tip-floor run-rate (NOT REV) | $87.87K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 87866 USD; at p95 floor → 18796806 USD. |
| Protocol fees 24h | $16.56M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9977 |
| p90 / p99 | 0.000015 / 0.000295 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.51 | coingecko.simple_price |
| 24h change | -0.40% | coingecko.simple_price |
| Market cap | $60.68B | coingecko.simple_price |
| 24h volume | $2.94B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.94B |
| TVL 1d / 7d / 30d | +0.39% / +5.07% / +22.23% |
| DEX volume 24h | $2.71B · 1d -0.36% · vs-7d-ago +24.83% |
| 7d DEX volume | $16.83B · -0.50% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $16.56M |
| Fees 1d / 7d | +5.92% / +31.01% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $737.12M | -15.61% |
| Raydium AMM | $342.26M | +11.19% |
| BisonFi | $249.32M | +22.18% |
| Meteora DLMM | $237.76M | +21.71% |
| Tessera V | $156.31M | +4.56% |
| Orca DEX | $155.18M | -34.49% |
| HumidiFi | $153.40M | +58.34% |
| Manifest Trade | $147.98M | +8.30% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.58B | -0.50% | +4.50% |
| Kamino Lend | Lending | $1.35B | -0.58% | +9.93% |
| Raydium AMM | Dexs | $1.15B | +1.32% | +8.54% |
| Jupiter Lend | Lending | $1.10B | +2.00% | +3.45% |
| Binance Staked SOL | Liquid Staking | $1.07B | +0.50% | +4.58% |
| Jito Liquid Staking | Liquid Staking | $1.06B | +0.26% | +5.77% |
| BlackRock BUIDL | RWA | $987.67M | -0.43% | +1.37% |
| Jupiter Perpetual Exchange | Derivatives | $750.71M | -0.12% | +1.65% |
| Jupiter Staked SOL | Liquid Staking | $533.77M | -0.45% | +4.33% |
| xStocks | RWA | $438.64M | -1.33% | +1.55% |

## Stablecoins

Solana circulating pegged-USD: **$16.11B**
(1d -0.39% · 7d +4.94%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.02B | -4.13% |
| USDT · Tether | $2.77B | -0.00% |
| USDGO · USDGO | $1.37B | +0.18% |
| USD1 · World Liberty Financial USD | $1.28B | +1.58% |
| BUIDL · BlackRock USD | $987.67M | +1.00% |
| PYUSD · PayPal USD | $743.84M | +1.66% |
| USDG · Global Dollar | $604.96M | +5.79% |
| USDe · Ethena USDe | $535.74M | -0.00% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 79 of 737 Solana-deployed listed symbols (multiplier ok 80/80; 737 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 737 · Solana deployments 737 · priced 79 · priced-subset mcap $291.74M (lower bound, not a census).
24h volume $88.69M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $438.64M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 79 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 737 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 737 unique underlyings among 737 Solana rows; not every tokenized equity on Solana). 737 of 737 listed xStocks have a Solana deployment (737 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.35B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $987.67M
- **xStocks** (RWA) — $438.64M
- **OnRe** (RWA) — $305.80M
- **Ondo Yield Assets** (RWA) — $180.07M
- **Huma Finance V2** (RWA) — $172.11M
- **Hastra** (RWA) — $149.47M
- **Ondo Global Markets** (RWA) — $25.93M
- **Plume Vaults** (RWA) — $25.34M

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

- [RT by @anza_xyz: What is cool about transaction v1?
1) @multisig smart wallet being able to do everything onchain with big pqc based signatures 
2) two zkp root state transitions in one atomic tx, aka “based rollups”
3) routing to a bajilion markets at the same time](https://x.com/toly/status/2097345987937497491) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:27:04 GMT
- [Alpenglow is coming.](https://x.com/anza_xyz/status/2097352587817455967) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:53:18 GMT `upgrade`
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
- [Rent reduction is live on mainnet-beta.

Step 1 of SIMD-0437 activated at epoch 1028, the first of five feature gates on the road to cutting Solana's storage cost per byte by 90% overall.

Step 1 drops lamports per byte 6,960 → 6,333. Each remaining gate activates only after state growth checks out at the current level. We are stepping down to the final 696 safely, not on a fixed schedule. Follow here for an accurate timeline.

A safeguard gate (SIMD-0438) can restore the legacy value if state growth becomes a problem.](https://x.com/anza_xyz/status/2095654321350459648) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 23:25:00 GMT `upgrade` `mainnet`
- [Repo and benchmarks: https://github.com/anza-xyz/wincode

wincode is a drop-in replacement when layout and configuration match.](https://x.com/anza_xyz/status/2095612015192703481) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:53 GMT
- [wincode has surpassed 5M downloads 📦📈

Our Rust crate started as a fix for serialization performance in the Agave validator client.

RustSec now lists it as a recommended bincode replacement. Built to make Solana faster, now adopted across the Rust community.

Credit to Anza IBRL engineering culture who keep pushing the envelope on speed.

How it works by wincode creator @zbr0wn: https://www.anza.xyz/blog/wincode-bincode-compatible-rust-serializer](https://x.com/anza_xyz/status/2095611874142548262) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:20 GMT
- [IBRL](https://x.com/anza_xyz/status/2095605589548417152) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:11:21 GMT
- [Report: Stablecoins Are Reshaping Remittances](https://solana.com/news/report-stablecoins-are-reshaping-remittances) — solana.com/news · Tue, 08 Sep 2026 13:14:00 GMT
- [How BitRobot Crowdsources Real-World Data for Embodied AI, with Jonathan Victor](https://solana.com/news/bits-to-bricks-bitrobot-jonathan-victor) — solana.com/news · Mon, 07 Sep 2026 07:00:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @anza_xyz: What is cool about transaction v1?
1) @multisig smart wallet being able to do everything onchain with big pqc based signatures 
2) two zkp root state transitions in one atomic tx, aka “based rollups”
3) routing to a bajilion markets at the same time](https://x.com/toly/status/2097345987937497491) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:27:04 GMT
- [Alpenglow is coming.](https://x.com/anza_xyz/status/2097352587817455967) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 08 Sep 2026 15:53:18 GMT `upgrade`
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
- [Rent reduction is live on mainnet-beta.

Step 1 of SIMD-0437 activated at epoch 1028, the first of five feature gates on the road to cutting Solana's storage cost per byte by 90% overall.

Step 1 drops lamports per byte 6,960 → 6,333. Each remaining gate activates only after state growth checks out at the current level. We are stepping down to the final 696 safely, not on a fixed schedule. Follow here for an accurate timeline.

A safeguard gate (SIMD-0438) can restore the legacy value if state growth becomes a problem.](https://x.com/anza_xyz/status/2095654321350459648) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 23:25:00 GMT `upgrade` `mainnet`
- [Repo and benchmarks: https://github.com/anza-xyz/wincode

wincode is a drop-in replacement when layout and configuration match.](https://x.com/anza_xyz/status/2095612015192703481) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:53 GMT
- [wincode has surpassed 5M downloads 📦📈

Our Rust crate started as a fix for serialization performance in the Agave validator client.

RustSec now lists it as a recommended bincode replacement. Built to make Solana faster, now adopted across the Rust community.

Credit to Anza IBRL engineering culture who keep pushing the envelope on speed.

How it works by wincode creator @zbr0wn: https://www.anza.xyz/blog/wincode-bincode-compatible-rust-serializer](https://x.com/anza_xyz/status/2095611874142548262) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:36:20 GMT
- [IBRL](https://x.com/anza_xyz/status/2095605589548417152) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Thu, 03 Sep 2026 20:11:21 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-09 (2026-09-09 10:38:01 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 138ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 93ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 65ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 39ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 94ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6628ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 95ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 118ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 131ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 125ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 76ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 822ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1137ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 177ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 239ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 118ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 133ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 469ms https://solana.com/data
- `solana.com.databricks` [ok] 200 202ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 472ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 241ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 196ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 150ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 409ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 816ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 267ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 290ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 552ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [FAIL] 502 652ms https://nitter.perennialte.ch/solana/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_status` [ok] 200 208ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 12817ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [FAIL] 429 2942ms https://nitter.perennialte.ch/solana_devs/rss — HTTP 429 Too Many Requests
- `rss.rsshub.solana` [FAIL] 404 296ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 179ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 49ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 208ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 375ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 235ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 951ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 469ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 464ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 434ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 365ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 407ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 408ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 309ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 602ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 397ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 338ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 289ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1826ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1916ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1367ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1811ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1449ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2249ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1768ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1651ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AAPLx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.NVDAx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.METAx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.SPYx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.AAPLx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.MSFTx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.circ.NVDAx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.AMZNx` [ok] 200 530ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.GOOGLx` [ok] 200 561ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.METAx` [ok] 200 482ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 631ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 508ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 515ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 740ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.TSLAx` [ok] 200 1249ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.QQQx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.SPYx` [ok] 200 498ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.FLNCx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.price.COINx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.XRXx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.mult.AMZNx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 595ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.FLNCx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.circ.XRXx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 605ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.WGSx` [ok] 200 513ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.INDIx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.mult.QQQx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.WGSx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.circ.INDIx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.mult.XRXx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.price.WRLDx` [ok] 200 762ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.mult.INDIx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.circ.TSLAx` [ok] 200 1293ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.QUBTx` [ok] 200 354ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.circ.WRLDx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.price.BETRx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.price.PCTx` [ok] 200 601ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.circ.QUBTx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.price.AIx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.mult.WRLDx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.circ.BETRx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.PCTx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.AIx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.mult.QUBTx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.price.DRAMx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.mult.BETRx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.price.MVLLx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.MUUx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.mult.AIx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.price.METCx` [ok] 200 1294ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.circ.MVLLx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.WYFIx` [ok] 200 1327ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.MUUx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.AXTIx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.price.KORUx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.circ.WYFIx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.METCx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.AXTIx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.INTWx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.SNXXx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.DRAMx` [ok] 200 1156ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.MUUx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.SHEINx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.mult.WYFIx` [ok] 200 747ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 886ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.circ.SHEINx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.price.NWGx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.circ.KORUx` [ok] 200 1176ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.SOXSx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.NWGx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.SHEINx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.NWGx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.INTWx` [ok] 200 1398ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.MMGx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.KORUx` [ok] 200 627ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.mult.SNXXx` [ok] 200 1387ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 2165ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.TNGYIx` [ok] 200 529ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 406ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 773ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 1326ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.mult.DJTx` [ok] 200 697ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.HAIDLx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.CTINSx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.KUNLx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 900ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 499ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 1374ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.CMERPx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 503ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 708ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 997ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 687ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 1753ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.CMERPx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 567ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 490ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 762ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.BDWAPx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.CRESBx` [ok] 200 804ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 795ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.MIXUx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.ASMPTx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.CMENDx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.WXXDCx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 652ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 1355ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.CRESMx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 459ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 1425ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 1108ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.PRADx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.CRESPx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.JDHLTx` [ok] 200 790ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.SINOTx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.WXXDCx` [ok] 200 1015ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.CLONPx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.WHGROx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 427ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 872ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.PRADx` [ok] 200 1107ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 1180ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.SINOTx` [ok] 200 1202ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 687ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.SINOTx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 403ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 641ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.SWPRPx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.GENTEx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 1155ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 592ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.CRAUTx` [ok] 200 819ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 1146ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 1758ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 544ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 562ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 2702ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.HKCGAx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 1214ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.CKINFx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 550ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 1263ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 1106ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 860ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 1059ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 3686ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1381ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 323ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.INTWx` [ok] 200 150ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.MVLLx` [ok] 200 133ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SHEINx` [ok] 200 130ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.KORUx` [ok] 200 121ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.MUUx` [ok] 200 126ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.SNXXx` [ok] 200 131ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jup.tokens.search.DRAMx` [ok] 200 166ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.SOXSx` [ok] 200 130ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jito.tip_floor` [ok] 200 246ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 457ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 141ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 51ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 84ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 39ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 47ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 325ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
