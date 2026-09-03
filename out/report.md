# Borealis — Solana ecosystem report

**Generated** 2026-09-03T14:39:15Z · 2026-09-03 07:39:15 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-03T14:39:05Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +3.37%; DEX 24h $2.29B · 1d +5% · vs-7d-ago -3%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -17.43%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -30.88%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 856,198.00 is +26.3% vs 30d median 677,709.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 102.42 USD is +23.7% vs 30d median 82.77 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,996,143 |
| Block height | 422,043,159 |
| Block time | 2026-09-03T14:39:05Z |
| Epoch | 1,027 (76.89% · slot 332,146/432,000) |
| Mean TPS (last ~3,600s) | 4,013.7 |
| Mean non-vote TPS | 1,885.7 |
| Median TPS (same window) | 4,000.8 |
| Mean slot time | 314.8 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 544,791,465,383 |
| Circulating supply | 585,274,785 SOL |
| Total supply | 633,360,822 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 19 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 438,202,194 SOL |
| Delinquent stake | 220,162.83 SOL (0.050%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.25% / 35.53% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.35M SOL | 3.96% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.33M SOL | 3.73% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.46M SOL | 2.84% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.30M SOL | 2.58% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.18% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.12% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.22M SOL | 1.65% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.13M SOL | 1.63% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.50% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.95M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.61M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `xLabscif…` · 84.41K SOL · commission 5% · lag 207770 slots
- `prt1st4R…` · 78.62K SOL · commission 5% · lag 509201 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 30858 slots
- `5ZjxMYBb…` · 18.18K SOL · commission 0% · lag 30221 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 647420 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1210022 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 696487 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 557504 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 2012389 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1195792 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1237306 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 1195686 slots

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
| **In-protocol fees 24h** | **$915.85K** (9,030.4 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-01 |
| **Solana REV** | **10,924.9 SOL** / **$1.11M** | MEASURED UTC calendar day 2026-09-01: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-01 · UTC day 2026-09-01 · SOL-USD date 2026-09-01 |
| Jito tip-floor run-rate (NOT REV) | $62.08K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 62076 USD; at p95 floor → 5485563 USD. |
| Protocol fees 24h | $10.54M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9963 |
| p90 / p99 | 0.000010 / 0.000104 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $102.42 | coingecko.simple_price |
| 24h change | +3.37% | coingecko.simple_price |
| Market cap | $59.95B | coingecko.simple_price |
| 24h volume | $3.29B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.78B |
| TVL 1d / 7d / 30d | +2.98% / +0.73% / +22.06% |
| DEX volume 24h | $2.29B · 1d +5.42% · vs-7d-ago -2.65% |
| 7d DEX volume | $16.85B · -21.10% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $10.54M |
| Fees 1d / 7d | -17.43% / -30.88% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $1.02B | +23.42% |
| Orca DEX | $223.81M | +2.21% |
| BisonFi | $194.35M | -5.12% |
| Manifest Trade | $194.25M | +32.08% |
| Meteora DLMM | $137.83M | -1.54% |
| Raydium AMM | $114.99M | -24.61% |
| pump.fun | $83.17M | +50.90% |
| Axiom | $60.26M | -38.49% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.55B | +3.66% | -2.14% |
| Kamino Lend | Lending | $1.28B | +5.29% | +4.30% |
| Raydium AMM | Dexs | $1.09B | +0.53% | -1.44% |
| Jupiter Lend | Lending | $1.08B | +3.16% | -2.57% |
| Binance Staked SOL | Liquid Staking | $1.05B | +3.57% | -1.56% |
| Jito Liquid Staking | Liquid Staking | $1.02B | +3.67% | -2.27% |
| BlackRock BUIDL | RWA | $890.69M | +0.11% | -1.06% |
| Jupiter Perpetual Exchange | Derivatives | $750.17M | +2.21% | -4.00% |
| Jupiter Staked SOL | Liquid Staking | $524.96M | +3.54% | -2.84% |
| xStocks | RWA | $436.04M | +2.07% | +1.21% |

## Stablecoins

Solana circulating pegged-USD: **$15.89B**
(1d +1.59% · 7d -0.19%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.82B | +2.79% |
| USDT · Tether | $2.94B | +3.90% |
| USDGO · USDGO | $1.32B | +5.62% |
| USD1 · World Liberty Financial USD | $1.21B | -0.00% |
| BUIDL · BlackRock USD | $890.69M | +0.42% |
| PYUSD · PayPal USD | $810.33M | +9.77% |
| USDG · Global Dollar | $596.76M | -2.73% |
| USDe · Ethena USDe | $535.98M | -0.23% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 73 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 73 · priced-subset mcap $292.50M (lower bound, not a census).
24h volume $31.97M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $438.92M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 73 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $890.69M
- **xStocks** (RWA) — $436.04M
- **OnRe** (RWA) — $293.04M
- **Ondo Yield Assets** (RWA) — $179.96M
- **Hastra** (RWA) — $153.00M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $24.90M
- **Plume Vaults** (RWA) — $22.89M

## Daily active addresses

856,198 (Allium, as of 2026-09-02). Provider range 446,040–917,329. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: 📊 @Solana ETFs ended August at all-time highs of $1.44B net assets, up 45% YTD.

This growth came after 7 consecutive days of net flows exceeding $10M.](https://x.com/TokenRelations/status/2095513176485839199) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 14:04:08 GMT
- [RT by @solana: xStocks are here!

XPlace now supports @xStocksFi tokenized equities as collateral.

Borrow against tokenized stocks like Apple, Tesla, Nvidia, and Google - alongside BTC, ETH, and SOL without selling your assets - powered by @kamino 

✓ Earn yield on eligible assets while you spend
✓ Switch between crypto and stock collateral in one tap
✓ No fixed repayment schedule

The future of credit is asset-backed.

Access to xStocks is subject to regional eligibility and is not available to U.S. persons or certain restricted jurisdictions. Terms apply.](https://x.com/xplaceapp/status/2095514271216009289) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 14:08:29 GMT
- [BREAKING: Birkins are coming to Solana via @Beezie 

Partnering with The Luxury Closet to bring authenticated luxury onchain.](https://x.com/solana/status/2095492290576052692) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 12:41:09 GMT
- [Listen to the pod: https://solana.com/podcasts/house-of-sol-with-ben-brophy/episodes/7-trillion-a-month-in-stablecoins-with-geoff-kendrick-of-standard-chartered-e3nvgtn](https://x.com/solana/status/2095458499400704060) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 10:26:52 GMT
- [One of the world's largest banks on where Solana fits:

"Solana's particular niche is ultra low cost, ultra fast. That opens up things like micropayments, particularly as we move towards agentic AI."

– Geoff Kendrick, Global Head of Digital Assets Research, @StanChart](https://x.com/solana/status/2095458487585399200) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 10:26:49 GMT
- [Solana's flagship event, gathering the leaders, builders and institutions driving the token supercycle.

Get your ticket: https://solana.com/breakpoint](https://x.com/solana/status/2095434370194784712) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 08:50:59 GMT
- [Consider this your official invite to Breakpoint 2026](https://x.com/solana/status/2095434367921483926) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 08:50:59 GMT
- [RT by @solana: “Solana is the financial infra powering the token supercycle.”

That line from @calilyliu’s new op-ed is not a bull case. It’s a framing: money, assets, and ownership moving onto always-on internet infrastructure.

Read it as a rally and you miss the point. The internet capital market it produces becomes the largest capital market.

The core claim: distribution is valuation.

Legacy markets still price assets through old frictions: geography, ticket size, jurisdictional walls. Tokenization removes those gates. An asset issued anywhere can reach capital everywhere, at any hour. The ADR already proved this. Tokenization scales it.

The early evidence is onchain.

Hundreds of billions in RWAs have traded across @solana. More than $4.7T in stablecoins moved across the network in the past year. @Visa, @PayPal, @MoneyGram, and @WesternUnion use the same rails.

That loop compounds: more issuers → more assets → more investors → deeper liquidity. Payments, settlement, issuance, and markets run on one venue. Any app can become a superapp. AI agents accelerate the same loop.

We are still in the early innings. Tokenized Treasuries are the “newspapers going online” phase: useful, not the endpoint. The system that captures this shift will not be an upgrade of the old one. It is being built now, one token at a time.

Full op-ed in the comments.](https://x.com/solana_stream/status/2095428231017238840) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 08:26:36 GMT `upgrade`
- [RT by @anza_xyz: 🚨ATTENTION: large transactions have hit the testnet

https://explorer.solana.com/tx/5KxbxQxkqv2gPjRArDeFJSmfhG6X1vAbEjZFn5zGPsmLvsb4FYKbYTm7BBDSNarkEt2jL5878wmJ4cTYyvURPLnK?cluster=testnet](https://x.com/bw_solana/status/2095199360724431064) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 17:17:09 GMT `upgrade`
- [RT by @anza_xyz: Solana is the financial infra powering the token supercycle. 

We're building toward a future where the internet capital market becomes the biggest capital market.

More thoughts here:

https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/calilyliu/status/2095179874839462349) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 15:59:43 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: 📊 @Solana ETFs ended August at all-time highs of $1.44B net assets, up 45% YTD.

This growth came after 7 consecutive days of net flows exceeding $10M.](https://x.com/TokenRelations/status/2095513176485839199) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 14:04:08 GMT
- [RT by @solana: xStocks are here!

XPlace now supports @xStocksFi tokenized equities as collateral.

Borrow against tokenized stocks like Apple, Tesla, Nvidia, and Google - alongside BTC, ETH, and SOL without selling your assets - powered by @kamino 

✓ Earn yield on eligible assets while you spend
✓ Switch between crypto and stock collateral in one tap
✓ No fixed repayment schedule

The future of credit is asset-backed.

Access to xStocks is subject to regional eligibility and is not available to U.S. persons or certain restricted jurisdictions. Terms apply.](https://x.com/xplaceapp/status/2095514271216009289) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 14:08:29 GMT
- [BREAKING: Birkins are coming to Solana via @Beezie 

Partnering with The Luxury Closet to bring authenticated luxury onchain.](https://x.com/solana/status/2095492290576052692) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 12:41:09 GMT
- [Listen to the pod: https://solana.com/podcasts/house-of-sol-with-ben-brophy/episodes/7-trillion-a-month-in-stablecoins-with-geoff-kendrick-of-standard-chartered-e3nvgtn](https://x.com/solana/status/2095458499400704060) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 10:26:52 GMT
- [One of the world's largest banks on where Solana fits:

"Solana's particular niche is ultra low cost, ultra fast. That opens up things like micropayments, particularly as we move towards agentic AI."

– Geoff Kendrick, Global Head of Digital Assets Research, @StanChart](https://x.com/solana/status/2095458487585399200) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 10:26:49 GMT
- [Solana's flagship event, gathering the leaders, builders and institutions driving the token supercycle.

Get your ticket: https://solana.com/breakpoint](https://x.com/solana/status/2095434370194784712) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 08:50:59 GMT
- [Consider this your official invite to Breakpoint 2026](https://x.com/solana/status/2095434367921483926) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 08:50:59 GMT
- [RT by @solana: “Solana is the financial infra powering the token supercycle.”

That line from @calilyliu’s new op-ed is not a bull case. It’s a framing: money, assets, and ownership moving onto always-on internet infrastructure.

Read it as a rally and you miss the point. The internet capital market it produces becomes the largest capital market.

The core claim: distribution is valuation.

Legacy markets still price assets through old frictions: geography, ticket size, jurisdictional walls. Tokenization removes those gates. An asset issued anywhere can reach capital everywhere, at any hour. The ADR already proved this. Tokenization scales it.

The early evidence is onchain.

Hundreds of billions in RWAs have traded across @solana. More than $4.7T in stablecoins moved across the network in the past year. @Visa, @PayPal, @MoneyGram, and @WesternUnion use the same rails.

That loop compounds: more issuers → more assets → more investors → deeper liquidity. Payments, settlement, issuance, and markets run on one venue. Any app can become a superapp. AI agents accelerate the same loop.

We are still in the early innings. Tokenized Treasuries are the “newspapers going online” phase: useful, not the endpoint. The system that captures this shift will not be an upgrade of the old one. It is being built now, one token at a time.

Full op-ed in the comments.](https://x.com/solana_stream/status/2095428231017238840) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 08:26:36 GMT `upgrade`
- [RT by @anza_xyz: 🚨ATTENTION: large transactions have hit the testnet

https://explorer.solana.com/tx/5KxbxQxkqv2gPjRArDeFJSmfhG6X1vAbEjZFn5zGPsmLvsb4FYKbYTm7BBDSNarkEt2jL5878wmJ4cTYyvURPLnK?cluster=testnet](https://x.com/bw_solana/status/2095199360724431064) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 17:17:09 GMT `upgrade`
- [RT by @anza_xyz: Solana is the financial infra powering the token supercycle. 

We're building toward a future where the internet capital market becomes the biggest capital market.

More thoughts here:

https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/calilyliu/status/2095179874839462349) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 15:59:43 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-03 (2026-09-03 07:39:15 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 747ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 534ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 616ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 518ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 513ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6841ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1419ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 145ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 63ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 37ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 27ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 27ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 29ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 70ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 233ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 60ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 93ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 300ms https://solana.com/data
- `solana.com.databricks` [ok] 200 72ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 382ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 136ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 25ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 79ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 171ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 429ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 77ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 72ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 75ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 469ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1729ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2711ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1051ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 270ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 650ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 525ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2474ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2315ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2089ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2350ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2135ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1829ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2163ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2072ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2050ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2666ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2043ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2193ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2201ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2117ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1608ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2864ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1393ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1297ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1316ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1215ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 934ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1396ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.MSFTx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.GOOGLx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.SPYx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.NVDAx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.AMZNx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.NVDAx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.MVLLx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.QQQx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.mult.MSFTx` [ok] 200 499ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.price.MUUx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.price.COINx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.COINx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.AAPLx` [ok] 200 1341ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.QQQx` [ok] 200 298ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.MVLLx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.mult.QQQx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.MVLLx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.DJTx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.mult.COINx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.price.INTWx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.circ.AAPLx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.KORUx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.DJTx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.KORUx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.DRAMx` [ok] 200 1350ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.mult.KORUx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.circ.MUUx` [ok] 200 1150ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.NWGx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.price.BANKCx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.SOXSx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.SNXXx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.price.SHEINx` [ok] 200 627ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.mult.MUUx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.BANKCx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.BANKCx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.SHEINx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.SHEINx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.price.LAOPGx` [ok] 200 623ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.NWGx` [ok] 200 1369ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 1144ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.NWGx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.circ.DRAMx` [ok] 200 1737ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 1046ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 1549ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.MMGx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 2273ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 835ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 1585ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 1631ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.ENNHLx` [ok] 200 745ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.SMOIHx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 1118ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 1506ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 987ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 1492ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.KUNLx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.CMERPx` [ok] 200 118ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.CSPCx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 1272ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.SMOIHx` [ok] 200 1068ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 1217ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 1281ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 1094ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 869ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 430ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.circ.CMERPx` [ok] 200 1010ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.CMENDx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.BDWAPx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.CRESBx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 1440ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 685ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 301ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.price.SITCx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.CRESMx` [ok] 200 931ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.ASMPTx` [ok] 200 891ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.CMENDx` [ok] 200 1448ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 944ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 1189ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 128ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.SNDSCx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.CRESMx` [ok] 200 1076ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 2365ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 1196ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.SITCx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 1089ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.SINOTx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.SINOx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 1198ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 979ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.CTFJWx` [ok] 200 1098ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 1911ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 686ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.CLPHDx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.CLONPx` [ok] 200 1476ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 1677ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.CLONPx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.SINOx` [ok] 200 1588ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 1224ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 1098ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 1202ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 957ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 1472ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 117ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.price.CKINFx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 1437ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 1758ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.SWPRPx` [ok] 200 550ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.HKCGAx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.GENTEx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 698ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.HKEXCx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.price.NONGx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 1021ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 954ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 1289ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 1565ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.COVELx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.CHONGx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.CKAHx` [ok] 200 139ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.MEITx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.NONGx` [ok] 200 932ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.GEELx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.KUAIx` [ok] 200 868ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 1115ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 129ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.COSCx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.HNDLDx` [ok] 200 675ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.COSCx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 999ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.COVELx` [ok] 200 1174ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.circ.CHONGx` [ok] 200 1177ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 1105ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.CHONGx` [ok] 200 437ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 1538ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 1697ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 116ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 4161ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.MIXUx` [ok] 200 11592ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.MIXUx` [ok] 200 938ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 1431ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 790ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 249ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.MEITx` [ok] 200 66ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 42ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.HKEXCx` [ok] 200 81ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 50ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.SHEINx` [ok] 200 43ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.BANKCx` [ok] 200 51ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.PRADx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=PRADx
- `jup.tokens.search.HKCGAx` [ok] 200 46ms https://lite-api.jup.ag/tokens/v2/search?query=HKCGAx
- `jito.tip_floor` [ok] 200 273ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 274ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 12ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 658ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 525ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 545ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 507ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 1439ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
