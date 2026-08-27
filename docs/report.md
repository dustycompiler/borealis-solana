# Borealis — Solana ecosystem report

**Generated** 2026-08-27T16:53:35Z · 2026-08-27 09:53:35 PT
**Author** dustycompiler · **Version** 1.5.4 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-27T16:53:23Z · **RPC health** `ok`
**Health score** 88 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 400)/400, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +13.52%; DEX 24h $2.35B · 1d -20% · vs-7d-ago -22%; slot 367 ms
Auto-refresh on a GitHub Actions schedule (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -19.87%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -21.87%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is +14.62%. (threshold: `|1d %| >= 8`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 108.84 USD is +43.9% vs 30d median 75.65 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **WARN · Large SOL 24h price move** — SOL/USD 24h change is +13.52% (coingecko.simple_price). (threshold: `|24h %| >= 8`)
- **INFO · TPS vs 30d median (solana.com/data tx/86400)** — Current 4,729.27 TPS is +32.2% vs 30d median 3,577.41 TPS (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 442,146,598 |
| Block height | 420,194,858 |
| Block time | 2026-08-27T16:53:23Z |
| Epoch | 1,023 (48.75% · slot 210,599/432,000) |
| Mean TPS (last ~3,600s) | 4,729.3 |
| Mean non-vote TPS | 2,866.1 |
| Median TPS (same window) | 4,769.9 |
| Mean slot time | 367.0 ms |
| Median slot time | 365.9 ms |
| Transaction count (cluster) | 542,446,944,034 |
| Circulating supply | 584,062,559 SOL |
| Total supply | 632,969,375 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 685 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 432,684,178 SOL |
| Delinquent stake | 4,200,658.33 SOL (0.962%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 79 |
| Top 10 / 20 stake share | 24.51% / 35.92% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.06M SOL | 3.94% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.03M SOL | 3.70% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.31M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.75M SOL | 2.72% | 5% | 0 |
| 5 | `C8Bey3LK…` | 9.22M SOL | 2.13% | 7% | 0 |
| 6 | `E1r4Psq8…` | 9.05M SOL | 2.09% | 0% | 0 |
| 7 | `CAo1dCGY…` | 8.90M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.85M SOL | 1.81% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.30M SOL | 1.69% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.58M SOL | 1.52% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.42% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.06M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.93M SOL | 1.37% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.64M SOL | 1.30% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `87CcUxpy…` · 3.90M SOL · commission 0% · lag 10804 slots
- `2Gfd4mkM…` · 139.16K SOL · commission 0% · lag 398 slots
- `mrgn2vUP…` · 90.76K SOL · commission 0% · lag 1373 slots
- `7ZjHeeYE…` · 31.34K SOL · commission 5% · lag 66195 slots
- `mrgn4atx…` · 23.80K SOL · commission 0% · lag 42592 slots
- `gangtCrQ…` · 16.43K SOL · commission 0% · lag 893919 slots
- `ChaossRP…` · 1.42K SOL · commission 0% · lag 162844 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 1134232 slots
- `kom1oNHy…` · 1.06K SOL · commission 5% · lag 1510082 slots
- `6adw3JVB…` · 2.00 SOL · commission 100% · lag 442146598 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 58097728 slots
- `bcZxRSoz…` · 0.00 SOL · commission 0% · lag 1506599 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 30 | data/history.jsonl snapshot tape |
| TVL chart | 30 | data/history.jsonl snapshot tape |
| SOL chart | 29 | data/history.jsonl snapshot tape |
| history.jsonl rows | 30 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$998.52K** (9,174.2 SOL) | solana.com/data Fees (Allium) MEASURED |
| **Solana REV** | **11,440.0 SOL** / **$1.12M** | MEASURED UTC calendar day 2026-08-25: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-25 · UTC day 2026-08-25 · SOL-USD date 2026-08-25 |
| Jito tip-floor run-rate (NOT REV) | $186.74K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 186736 USD; at p95 floor → 32342153 USD. |
| Protocol fees 24h | $15.17M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9948 |
| p90 / p99 | 0.000017 / 0.000384 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $108.84 | coingecko.simple_price |
| 24h change | +13.52% | coingecko.simple_price |
| Market cap | $63.57B | coingecko.simple_price |
| 24h volume | $6.69B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.97B |
| TVL 1d / 7d / 30d | +6.51% / +14.26% / +23.94% |
| DEX volume 24h | $2.35B · 1d -19.87% · vs-7d-ago -21.87% |
| 7d DEX volume | $21.32B · +76.41% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $15.17M |
| Fees 1d / 7d | +14.62% / +10.85% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $765.13M | +34.73% |
| Orca DEX | $363.48M | -20.90% |
| BisonFi | $251.44M | -38.88% |
| Meteora DLMM | $184.81M | -24.98% |
| Raydium AMM | $165.75M | -14.17% |
| Manifest Trade | $153.11M | -22.39% |
| Axiom | $126.33M | +42.08% |
| Jupiterz | $78.00M | -1.65% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.63B | +12.15% | +26.46% |
| Kamino Lend | Lending | $1.26B | +7.48% | +11.14% |
| Raydium AMM | Dexs | $1.14B | +7.23% | +19.18% |
| Jupiter Lend | Lending | $1.13B | +7.91% | +10.41% |
| Binance Staked SOL | Liquid Staking | $1.10B | +12.51% | +26.12% |
| Jito Liquid Staking | Liquid Staking | $1.08B | +12.37% | +24.92% |
| BlackRock BUIDL | RWA | $886.45M | +0.29% | +1.62% |
| Jupiter Perpetual Exchange | Derivatives | $791.35M | +6.71% | +7.03% |
| Jupiter Staked SOL | Liquid Staking | $557.28M | +12.66% | +24.20% |
| xStocks | RWA | $439.42M | +3.06% | +9.26% |

## Stablecoins

Solana circulating pegged-USD: **$15.81B**
(1d -0.12% · 7d -0.23%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.94B | -1.34% |
| USDT · Tether | $2.84B | +0.00% |
| USDGO · USDGO | $1.25B | +0.80% |
| USD1 · World Liberty Financial USD | $1.13B | +2.12% |
| BUIDL · BlackRock USD | $886.45M | +1.15% |
| PYUSD · PayPal USD | $685.41M | +0.96% |
| USDG · Global Dollar | $624.00M | -0.80% |
| USDe · Ethena USDe | $537.65M | +0.09% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 80 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 80 · priced-subset mcap $286.01M (lower bound, not a census).
24h volume $39.25M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $439.42M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 80 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.45M
- **xStocks** (RWA) — $439.42M
- **OnRe** (RWA) — $278.02M
- **Ondo Yield Assets** (RWA) — $178.52M
- **Hastra** (RWA) — $161.01M
- **Theo Network thBill** (RWA) — $26.39M
- **Ondo Global Markets** (RWA) — $25.00M
- **Plume Vaults** (RWA) — $22.86M

## Daily active addresses

750,240 (Allium, as of 2026-08-26). Provider range 399,997–882,844. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: From 0 to half a billion in a year.

xStocks is now @Solana's leading tokenized stock issuer after crossing $500M in assets under management.

700+ assets. Always 1:1 backed. Live across DeFi.](https://x.com/xStocksFi/status/2093014909596361157) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:36:55 GMT
- [RT by @solana: Ansem explains why he’s bullish on Solana

"Solana is one of the only L1s, cycle over cycle that gets better and better infra wise and builder wise."](https://x.com/luminaries/status/2092998778475143635) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 15:32:49 GMT
- [RT by @solana: Live Now: Final Frontier Traders Showdown in Belgrade

Who will take the win?
https://x.com/i/broadcasts/1wxWjlDRZrkJQ](https://x.com/SolanaEvents/status/2093008774931910747) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:12:32 GMT
- [luma.com/summerhouse2026](https://x.com/solana/status/2093005906347000313) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:01:08 GMT
- [Saturday, Aug 29th. Solana Summer House is taken over by @gmgnai, @spenders_club, & @solanaspaces

Live trading battles, pack rips, basketball, DJs, food and drinks, 8+ exclusive drops.

Catch the livestream right here on @solana.](https://x.com/solana/status/2093005893759816030) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:01:05 GMT
- [Pinned: Solana now processes more x402 transactions than any other network.](https://x.com/solana/status/2092990785398645224) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 15:01:03 GMT
- [RT by @solana: 🚀 NOLUS IS LIVE ON @solana 

Asset-backed leverage with:
→ No margin calls
→ Fixed rates for the life of the position
→ Liquidations that trim instead of erase

So you can stay on Solana instead of moving to a CEX margin desk

Up to 5x on SOL → https://app.nolus.io](https://x.com/NolusProtocol/status/2092972910830846375) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 13:50:02 GMT
- [RT by @solana: Every prediction market you've ever used has a gatekeeper. Not anymore.

The era of creator-made prediction markets starts now.

Sign up below to secure beta access, claim your first badge, and start earning your Melee Score.

https://www.melee.markets/](https://x.com/meleemarkets/status/2092975483822469335) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 14:00:15 GMT
- [RT by @anza_xyz: best bug bounty program in the biz.
most battle tested client software](https://x.com/bw_solana/status/2092757428010139894) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 26 Aug 2026 23:33:47 GMT `upgrade`
- [Alpenglow bug bounty is now closed, thank you to everyone who took part! We had over 300 submissions and will distribute over 25,000 SOL as bounties.

Next steps for valid reports will begin shortly. Make sure to follow us to stay tuned for future competitions.](https://x.com/anza_xyz/status/2092745018041917496) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 26 Aug 2026 22:44:28 GMT `upgrade`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: From 0 to half a billion in a year.

xStocks is now @Solana's leading tokenized stock issuer after crossing $500M in assets under management.

700+ assets. Always 1:1 backed. Live across DeFi.](https://x.com/xStocksFi/status/2093014909596361157) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:36:55 GMT
- [RT by @solana: Ansem explains why he’s bullish on Solana

"Solana is one of the only L1s, cycle over cycle that gets better and better infra wise and builder wise."](https://x.com/luminaries/status/2092998778475143635) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 15:32:49 GMT
- [RT by @solana: Live Now: Final Frontier Traders Showdown in Belgrade

Who will take the win?
https://x.com/i/broadcasts/1wxWjlDRZrkJQ](https://x.com/SolanaEvents/status/2093008774931910747) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:12:32 GMT
- [luma.com/summerhouse2026](https://x.com/solana/status/2093005906347000313) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:01:08 GMT
- [Saturday, Aug 29th. Solana Summer House is taken over by @gmgnai, @spenders_club, & @solanaspaces

Live trading battles, pack rips, basketball, DJs, food and drinks, 8+ exclusive drops.

Catch the livestream right here on @solana.](https://x.com/solana/status/2093005893759816030) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 16:01:05 GMT
- [Pinned: Solana now processes more x402 transactions than any other network.](https://x.com/solana/status/2092990785398645224) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 15:01:03 GMT
- [RT by @solana: 🚀 NOLUS IS LIVE ON @solana 

Asset-backed leverage with:
→ No margin calls
→ Fixed rates for the life of the position
→ Liquidations that trim instead of erase

So you can stay on Solana instead of moving to a CEX margin desk

Up to 5x on SOL → https://app.nolus.io](https://x.com/NolusProtocol/status/2092972910830846375) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 13:50:02 GMT
- [RT by @solana: Every prediction market you've ever used has a gatekeeper. Not anymore.

The era of creator-made prediction markets starts now.

Sign up below to secure beta access, claim your first badge, and start earning your Melee Score.

https://www.melee.markets/](https://x.com/meleemarkets/status/2092975483822469335) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 27 Aug 2026 14:00:15 GMT
- [RT by @anza_xyz: best bug bounty program in the biz.
most battle tested client software](https://x.com/bw_solana/status/2092757428010139894) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 26 Aug 2026 23:33:47 GMT `upgrade`
- [Alpenglow bug bounty is now closed, thank you to everyone who took part! We had over 300 submissions and will distribute over 25,000 SOL as bounties.

Next steps for valid reports will begin shortly. Make sure to follow us to stay tuned for future competitions.](https://x.com/anza_xyz/status/2092745018041917496) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 26 Aug 2026 22:44:28 GMT `upgrade`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-27 (2026-08-27 09:53:35 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=activated-not-yet-effective, 250ms=pending, 200ms=pending. Observed mean slot ~367 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~367 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 174ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 124ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 121ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 208ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 131ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6939ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 255ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 82ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 28ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 41ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 25ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 34ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 871ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 78ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 33ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 64ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 80ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 269ms https://solana.com/data
- `solana.com.databricks` [ok] 200 59ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 284ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 135ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 31ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 62ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 100ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 376ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 75ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 76ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 85ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 389ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 279ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1097ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 324ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 190ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 120ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 132ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 809ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 865ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 886ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 995ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 976ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 954ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 796ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 769ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1231ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 869ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 765ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 801ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 887ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 784ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 2040ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1505ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1256ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1299ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1078ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 4143ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1832ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 471ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.MSFTx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.AAPLx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.NVDAx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.AMZNx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.SPYx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.SPYx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.GOOGLx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.METAx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.MSFTx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 333ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.SPYx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.GOOGLx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 154ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.GOOGLx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.MMGx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.BANKCx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 481ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.TSLAx` [ok] 200 974ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.QQQx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.TSLAx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.TSLAx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 729ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.BANKCx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.COINx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.HAIDLx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.CTINSx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 668ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.SZIGHx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.price.ENNHLx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.KUNLx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 581ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.SMOIHx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.CSPCx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.circ.CRESBx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.CMERPx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 917ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.CSPCx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.BDWAPx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.MIXUx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.ASMPTx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.CRESPx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.SITCx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.JDHLTx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.SNDSCx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.SINOTx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.WHRFRx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.circ.CRESPx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 1106ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.CRESPx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 115ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.PRADx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.CTFJWx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.CLONPx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.CLONPx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 728ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.mult.WHGROx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.WUXIBx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 640ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.GENTEx` [ok] 200 774ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.GENTEx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.CKAHx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 677ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.KUAIx` [ok] 200 114ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 835ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 1103ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 1091ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.KUAIx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 679ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.COVELx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.CHONGx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.price.MEITx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.HKEXCx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 657ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.MEITx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 742ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.NONGx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.GEELx` [ok] 200 548ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.CKINFx` [ok] 200 1405ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.POPMTx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.price.CKHUTx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.CKINFx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.price.BOCOMx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.price.HNDLDx` [ok] 200 619ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.PICCx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.price.CPETCx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.circ.BOCOMx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.circ.HNDLDx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.price.BOCHKx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.mult.CKHUTx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.price.CITICx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.circ.CPETCx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.mult.BOCOMx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.circ.CITICx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.mult.CPETCx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.price.CRESLx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.price.ANTASx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.mult.PICCx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.POPMTx` [ok] 200 607ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.mult.CITICx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.circ.CRESLx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.price.ZJGLDx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.mult.POPMTx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.price.PSBOCx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.circ.ANTASx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.circ.ZJGLDx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.price.ICBCx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.circ.BOCHKx` [ok] 200 609ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.circ.PSBOCx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.mult.ANTASx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.mult.CRESLx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.mult.ZJGLDx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.mult.BOCHKx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.mult.PSBOCx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `xstocks.price.HAIERx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.circ.ICBCx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.circ.HAIERx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.mult.HAIERx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.mult.ICBCx` [ok] 200 814ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 34ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 98ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 44ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 47ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.KUAIx` [ok] 200 45ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.MIXUx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.BANKCx` [ok] 200 47ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.HAIDLx` [ok] 200 40ms https://lite-api.jup.ag/tokens/v2/search?query=HAIDLx
- `jup.tokens.search.SINOTx` [ok] 200 73ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 173ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 244ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 61ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 122ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 118ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 124ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 115ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 2153ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.4 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
