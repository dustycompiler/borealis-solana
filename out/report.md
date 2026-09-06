# Borealis — Solana ecosystem report

**Generated** 2026-09-06T00:55:16Z · 2026-09-05 17:55:16 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-06T00:55:05Z · **RPC health** `ok`
**Health score** 96 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** NORMAL — SOL 24h +1.38%; DEX 24h $1.65B · 1d -12% · vs-7d-ago -1%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -12.08%. (threshold: `|1d %| >= 8`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 444,661,411 |
| Block height | 422,705,809 |
| Block time | 2026-09-06T00:55:05Z |
| Epoch | 1,029 (30.88% · slot 133,411/432,000) |
| Mean TPS (last ~3,600s) | 3,420.0 |
| Mean non-vote TPS | 1,288.7 |
| Median TPS (same window) | 3,345.8 |
| Mean slot time | 315.4 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 545,531,864,593 |
| Circulating supply | 585,445,547 SOL |
| Total supply | 633,549,422 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 17 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,169,820 SOL |
| Delinquent stake | 78,999.56 SOL (0.018%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.27% / 35.53% |
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
| 8 | `EvnRmnMr…` | 7.35M SOL | 1.67% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.13M SOL | 1.62% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.50% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.39% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.39% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.64M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.85M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `xLabscif…` · 28.57K SOL · commission 5% · lag 873038 slots
- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 36453 slots
- `prt1st4R…` · 13.11K SOL · commission 5% · lag 1174469 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 1312688 slots
- `5ZjxMYBb…` · 4.06K SOL · commission 0% · lag 695489 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1875290 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 122220 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 1222772 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1861060 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1902574 slots
- `HFTcVVrX…` · 148.42 SOL · commission 100% · lag 1860954 slots
- `6pEtDovp…` · 131.86 SOL · commission 100% · lag 1875338 slots

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
| Jito tip-floor run-rate (NOT REV) | $30.15K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 30153 USD; at p95 floor → 69190156 USD. |
| Protocol fees 24h | $10.37M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9959 |
| p90 / p99 | 0.000010 / 0.000105 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.40 | coingecko.simple_price |
| 24h change | +1.38% | coingecko.simple_price |
| Market cap | $60.54B | coingecko.simple_price |
| 24h volume | $2.42B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.89B |
| TVL 1d / 7d / 30d | -0.52% / +0.33% / +22.54% |
| DEX volume 24h | $1.65B · 1d -12.08% · vs-7d-ago -0.98% |
| 7d DEX volume | $13.66B · -28.81% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $10.37M |
| Fees 1d / 7d | -0.65% / -7.21% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $310.67M | 0.00% |
| BisonFi | $251.95M | 0.00% |
| Meteora DLMM | $180.66M | 0.00% |
| Orca DEX | $126.38M | -49.51% |
| Manifest Trade | $120.63M | -25.83% |
| Raydium AMM | $110.91M | -28.74% |
| Jupiterz | $64.61M | 0.00% |
| Scorch | $63.08M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.58B | +1.74% | -1.43% |
| Kamino Lend | Lending | $1.33B | +0.56% | +5.71% |
| Raydium AMM | Dexs | $1.12B | +1.46% | -1.37% |
| Jupiter Lend | Lending | $1.10B | +0.78% | +2.56% |
| Binance Staked SOL | Liquid Staking | $1.07B | +1.42% | -1.30% |
| Jito Liquid Staking | Liquid Staking | $1.06B | +2.03% | -0.46% |
| BlackRock BUIDL | RWA | $977.90M | -0.00% | +0.60% |
| Jupiter Perpetual Exchange | Derivatives | $756.25M | +0.70% | -2.26% |
| Jupiter Staked SOL | Liquid Staking | $535.00M | +1.78% | -1.80% |
| xStocks | RWA | $449.76M | +0.37% | +3.78% |

## Stablecoins

Solana circulating pegged-USD: **$16.33B**
(1d -0.25% · 7d +2.58%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.33B | +3.06% |
| USDT · Tether | $2.77B | -6.11% |
| USDGO · USDGO | $1.36B | +3.04% |
| USD1 · World Liberty Financial USD | $1.26B | +2.88% |
| BUIDL · BlackRock USD | $977.90M | +4.27% |
| PYUSD · PayPal USD | $753.44M | -12.39% |
| USDG · Global Dollar | $586.06M | +4.24% |
| USDe · Ethena USDe | $536.43M | +0.04% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 78 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 78 · priced-subset mcap $287.63M (lower bound, not a census).
24h volume $18.38M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $449.76M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 78 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.36B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $977.90M
- **xStocks** (RWA) — $449.76M
- **OnRe** (RWA) — $299.10M
- **Huma Finance V2** (RWA) — $190.42M
- **Ondo Yield Assets** (RWA) — $179.34M
- **Hastra** (RWA) — $150.50M
- **Ondo Global Markets** (RWA) — $25.91M
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
- [IBRL was never a meme. It's the reason Solana exists.

"With some very difficult but clever engineering, you can make a blockchain function as one giant computer that syncs all the financial information in the world at the speed of light."

"Alpenglow is a consensus improvement that will bring finality down to 100 milliseconds. It's going to feel like you're using any traditional system."

"This is us trying to, in a single unified environment, scale everything up so all of the world's markets, everything, could fit in one spot."](https://x.com/solana/status/2096115815397638649) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 05:58:48 GMT `upgrade`
- [Payment Channels: 1 Million Payments Per Second](https://solana.com/news/payment-channels-1-million-payments-per-second) — solana.com/news · Thu, 03 Sep 2026 16:26:00 GMT
- [How to Reclaim Excess SOL After Rent Reduction](https://solana.com/news/how-to-reclaim-excess-sol-after-rent-reduction) — solana.com/news · Thu, 03 Sep 2026 15:15:00 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

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
- [IBRL was never a meme. It's the reason Solana exists.

"With some very difficult but clever engineering, you can make a blockchain function as one giant computer that syncs all the financial information in the world at the speed of light."

"Alpenglow is a consensus improvement that will bring finality down to 100 milliseconds. It's going to feel like you're using any traditional system."

"This is us trying to, in a single unified environment, scale everything up so all of the world's markets, everything, could fit in one spot."](https://x.com/solana/status/2096115815397638649) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 05 Sep 2026 05:58:48 GMT `upgrade`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-06 (2026-09-05 17:55:16 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 175ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 155ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 155ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 171ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 170ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5916ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 278ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 107ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 73ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 324ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 44ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 1001ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1394ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 106ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 932ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 67ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 112ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 402ms https://solana.com/data
- `solana.com.databricks` [ok] 200 181ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 406ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 271ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 237ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 139ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 352ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 1072ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 458ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 454ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 449ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 879ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [FAIL] 502 6253ms https://nitter.perennialte.ch/solana_status/rss — HTTP 502 Bad Gateway
- `rss.nitter.anza_xyz` [FAIL] 502 193ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_devs` [ok] 200 703ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 267ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 112ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 112ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 472ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 588ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 512ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 747ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 580ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 560ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 542ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 513ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 455ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 542ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 505ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 644ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 479ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 482ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1980ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2155ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1590ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1786ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1567ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1832ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1462ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AAPLx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.SPYx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.TSLAx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.GOOGLx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.NVDAx` [ok] 200 594ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.AMZNx` [ok] 200 609ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.MSFTx` [ok] 200 623ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.METAx` [ok] 200 682ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.NVDAx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 629ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.GOOGLx` [ok] 200 516ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 482ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 475ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.MSFTx` [ok] 200 862ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.circ.AAPLx` [ok] 200 1342ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 583ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 779ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.AAPLx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.AXTIx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.DJTx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.DRAMx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.price.MVLLx` [ok] 200 864ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.circ.AXTIx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 984ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.MUUx` [ok] 200 918ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.price.KORUx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.AXTIx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.DJTx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.price.INTWx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.SHEINx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.price.SOXSx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.SNXXx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.MUUx` [ok] 200 664ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 725ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 685ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.circ.SNXXx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.mult.MUUx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.circ.SOXSx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.SHEINx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 530ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.SNXXx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.SUOPTx` [ok] 200 685ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.SOXSx` [ok] 200 674ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.KORUx` [ok] 200 1686ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 517ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 662ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.KUNLx` [ok] 200 347ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 906ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 1846ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.CTINSx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 639ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 906ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.LAOPGx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.HAIDLx` [ok] 200 612ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.MMGx` [ok] 200 694ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.JDLOGx` [ok] 200 712ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 645ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.WRFHDx` [ok] 200 1132ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 547ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.CMERPx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.SMOIHx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.SZIGHx` [ok] 200 1253ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.CMERPx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 841ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.CSPCx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.CRESBx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 549ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.WXXDCx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 629ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 1081ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.MIXUx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 1161ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.SNDSCx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.CRESMx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.mult.WHRFRx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.ASMPTx` [ok] 200 1236ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.PRADx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.CRESPx` [ok] 200 506ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.PRADx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 614ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 626ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 828ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 599ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.CTFJWx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.SITCx` [ok] 200 1123ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 893ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.WHGROx` [ok] 200 807ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.SINOTx` [ok] 200 1080ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.CTPCAx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.CLONPx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.CLONPx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 3985ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.SINOTx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.CMENDx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 565ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 556ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.SWPRPx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.GENTEx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.CKINFx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.price.CKAHx` [ok] 200 731ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.mult.CKINFx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 488ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.CKAHx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.COVELx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.CHONGx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.KUAIx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.COVELx` [ok] 200 422ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.mult.CHONGx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.COVELx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 283ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.PICCx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.price.GEELx` [ok] 200 878ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.COSCx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 602ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 882ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 1240ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.COSCx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.price.NWGx` [FAIL]  12029ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.NWGx` [ok] 200 370ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.NWGx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1636ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 310ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.MUUx` [ok] 200 117ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.KORUx` [ok] 200 117ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.INTWx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.MVLLx` [ok] 200 122ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.SNXXx` [ok] 200 119ms https://lite-api.jup.ag/tokens/v2/search?query=SNXXx
- `jup.tokens.search.DRAMx` [ok] 200 127ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.SHEINx` [ok] 200 118ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.SOXSx` [ok] 200 121ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jito.tip_floor` [ok] 200 118ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 477ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 141ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 125ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 163ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 100ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 136ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 2069ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
