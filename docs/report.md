# Borealis — Solana ecosystem report

**Generated** 2026-09-03T10:26:06Z · 2026-09-03 03:26:06 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-03T10:25:56Z · **RPC health** `ok`
**Health score** 96 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +1.95%; DEX 24h $2.33B · 1d +7% · vs-7d-ago -1%; slot 314 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -11.36%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -26.46%. (threshold: `|7d %| >= 20`)
- **WARN · Last slot-time sample outside 2.5σ of the 60-sample window** — Last sample 326 ms is +2.91σ vs window mean 314 ms (n=60). (threshold: `|last sample − window mean| > 2.5σ`)
- **INFO · Daily active addresses vs 30d median** — Current 856,198.00 is +26.3% vs 30d median 677,709.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 100.25 USD is +21.1% vs 30d median 82.77 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,947,874 |
| Block height | 421,995,088 |
| Block time | 2026-09-03T10:25:56Z |
| Epoch | 1,027 (65.71% · slot 283,875/432,000) |
| Mean TPS (last ~3,600s) | 3,462.8 |
| Mean non-vote TPS | 1,319.5 |
| Median TPS (same window) | 3,458.1 |
| Mean slot time | 314.3 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 544,736,328,675 |
| Circulating supply | 585,274,931 SOL |
| Total supply | 633,360,967 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 677 |
| Delinquent | 18 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 438,220,370 SOL |
| Delinquent stake | 201,987.05 SOL (0.046%) |
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

- `xLabscif…` · 84.41K SOL · commission 5% · lag 159501 slots
- `prt1st4R…` · 78.62K SOL · commission 5% · lag 460932 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 74741 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 599151 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1161753 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 648218 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 509235 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1964120 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1147523 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1189037 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 1147417 slots
- `6pEtDovp…` · 131.86 SOL · commission 100% · lag 1161801 slots

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
| Jito tip-floor run-rate (NOT REV) | $16.35K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 16354 USD; at p95 floor → 172378 USD. |
| Protocol fees 24h | $11.21M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9979 |
| p90 / p99 | 0.000010 / 0.000115 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $100.25 | coingecko.simple_price |
| 24h change | +1.95% | coingecko.simple_price |
| Market cap | $58.70B | coingecko.simple_price |
| 24h volume | $3.12B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.76B |
| TVL 1d / 7d / 30d | +2.06% / -0.16% / +20.98% |
| DEX volume 24h | $2.33B · 1d +7.16% · vs-7d-ago -1.05% |
| 7d DEX volume | $16.71B · -21.77% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $11.21M |
| Fees 1d / 7d | -11.36% / -26.46% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $1.02B | +23.42% |
| Orca DEX | $218.27M | -0.32% |
| BisonFi | $194.35M | -5.12% |
| Manifest Trade | $164.29M | +11.71% |
| Meteora DLMM | $137.83M | -1.54% |
| Raydium AMM | $111.69M | -26.78% |
| Axiom | $97.98M | 0.00% |
| pump.fun | $83.17M | +50.90% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.54B | +1.61% | -0.28% |
| Kamino Lend | Lending | $1.28B | +3.65% | +5.24% |
| Raydium AMM | Dexs | $1.09B | +0.53% | -1.44% |
| Jupiter Lend | Lending | $1.07B | +1.01% | -1.87% |
| Binance Staked SOL | Liquid Staking | $1.04B | +0.77% | +0.75% |
| Jito Liquid Staking | Liquid Staking | $1.01B | +1.63% | -0.46% |
| BlackRock BUIDL | RWA | $890.69M | +0.11% | -1.06% |
| Jupiter Perpetual Exchange | Derivatives | $748.28M | +0.86% | -2.67% |
| Jupiter Staked SOL | Liquid Staking | $521.03M | +1.28% | -0.89% |
| xStocks | RWA | $436.72M | +1.29% | +1.30% |

## Stablecoins

Solana circulating pegged-USD: **$15.69B**
(1d +1.57% · 7d -0.21%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.70B | +1.04% |
| USDT · Tether | $2.90B | +2.49% |
| USDGO · USDGO | $1.28B | +2.41% |
| USD1 · World Liberty Financial USD | $1.21B | -0.00% |
| BUIDL · BlackRock USD | $890.69M | +0.42% |
| PYUSD · PayPal USD | $811.93M | +9.99% |
| USDG · Global Dollar | $598.61M | -2.43% |
| USDe · Ethena USDe | $535.91M | -0.22% |

## Tokenized equities (xStocks)

HTTP 503 Service Unavailable
Listed 0 · Solana deployments 0 · priced 0 · priced-subset mcap — (lower bound, not a census).
24h volume $28.75M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $436.72M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok None / mcap_computable None of attempted None; missing multiplier → mcap omitted, never silent 1.0).  

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $890.69M
- **xStocks** (RWA) — $436.72M
- **OnRe** (RWA) — $288.99M
- **Ondo Yield Assets** (RWA) — $179.13M
- **Hastra** (RWA) — $153.73M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $24.98M
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
- [Source: @DefiLlama](https://x.com/solana/status/2095379851003978119) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 05:14:21 GMT
- [BREAKING: Solana ranks #1 for app revenue in August with $143M. 38% of all onchain app revenue.](https://x.com/solana/status/2095379848709677207) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 05:14:20 GMT
- [RT by @solana: Introducing Titan Pro

Custom layouts, and advanced order types, including our all-new Conditional Orders.

Everything you need to trade with an edge on @solana.](https://x.com/Titan_Exchange/status/2095167528049971267) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 15:10:39 GMT
- [RT by @solana: 📁 @superteam 
┃
┣ 📁 Global
┃ ┣ 📁 @SuperteamBlack 
┃ ┣ 📁 @SuperteamTalent 
┃ ┗ 📁 @SuperteamEarn 
┃
┣ 📁 Chapters — Americas
┃ ┣ 📁 @SuperteamUSA 
┃ ┣ 📁 @SuperteamCAN 
┃ ┣ 📁 @SuperteamBR 
┃ ┗ 📁 @SuperteamAR 
┃
┣ 📁 Chapters — Europe
┃ ┣ 📁 @LaFamilia_so 
┃ ┣ 📁 @SuperteamUK 
┃ ┣ 📁 @SuperteamDE 
┃ ┣ 📁 @SuperteamTR  
┃ ┣ 📁 @SuperteamUKR 
┃ ┣ 📁 @SuperteamBLKN 
┃ ┣ 📁 @SuperteamPOL 
┃ ┣ 📁 @superteamIE 
┃ ┣ 📁 @SuperteamNL 
┃ ┗ 📁 @SuperteamGEO 
┃
┣ 📁 Chapters — Asia
┃ ┣ 📁 @SuperteamVN 
┃ ┣ 📁 @SuperteamMY 
┃ ┣ 📁 @SuperteamTH 
┃ ┣ 📁 @SuperteamAE 
┃ ┣ 📁 @SuperteamIN 
┃ ┣ 📁 @SuperteamSG 
┃ ┣ 📁 @SuperteamJapan  
┃ ┣ 📁 @SuperteamKorea 
┃ ┣ 📁 @SuperteamINDO 
┃ ┗ 📁 @SuperteamKZ 
┃
┣ 📁 Chapters — Africa
┃ ┗ 📁 @SuperteamNG 
┃
┣ 📁 Chapters — Oceania
┃ ┗ 📁 @SuperteamAU 
┃
┣ 📁 Ecosystem
┃ ┣ 📁 Solana
┃ ┣ 📁 Partners
┃ ┣ 📁 Grants
┃ ┗ 📁 Opportunities
┃
┣ 📁 @vibhu Memes
┃  ┗ 📁 http://unhinged.zip
┃
┗ 📁 Mission
  ┣ 📁 Grow Together
  ┣ 📁 Ship Together
  ┣ 📁 Create Opportunities
  ┗ 📁 Win Together](https://x.com/SuperteamAR/status/2095246522841809022) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 20:24:33 GMT
- [solmF-ONE brings @FasanaraCapital's private credit strategy onchain through @MidasRWA 

Use it in DeFi across Solana: 
solmF-ONE is integrated on @kamino in @RockawayX RWA USDC market and @SteakhouseFi USDG High Yield market](https://x.com/solana/status/2095248912487477256) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 20:34:03 GMT
- [RT by @anza_xyz: 🚨ATTENTION: large transactions have hit the testnet

https://explorer.solana.com/tx/5KxbxQxkqv2gPjRArDeFJSmfhG6X1vAbEjZFn5zGPsmLvsb4FYKbYTm7BBDSNarkEt2jL5878wmJ4cTYyvURPLnK?cluster=testnet](https://x.com/bw_solana/status/2095199360724431064) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 17:17:09 GMT `upgrade`
- [RT by @anza_xyz: Solana is the financial infra powering the token supercycle. 

We're building toward a future where the internet capital market becomes the biggest capital market.

More thoughts here:

https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/calilyliu/status/2095179874839462349) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 15:59:43 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

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
- [Source: @DefiLlama](https://x.com/solana/status/2095379851003978119) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 05:14:21 GMT
- [BREAKING: Solana ranks #1 for app revenue in August with $143M. 38% of all onchain app revenue.](https://x.com/solana/status/2095379848709677207) — X/Nitter-style RSS @solana (not Twitter API) · Thu, 03 Sep 2026 05:14:20 GMT
- [RT by @solana: Introducing Titan Pro

Custom layouts, and advanced order types, including our all-new Conditional Orders.

Everything you need to trade with an edge on @solana.](https://x.com/Titan_Exchange/status/2095167528049971267) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 15:10:39 GMT
- [RT by @solana: 📁 @superteam 
┃
┣ 📁 Global
┃ ┣ 📁 @SuperteamBlack 
┃ ┣ 📁 @SuperteamTalent 
┃ ┗ 📁 @SuperteamEarn 
┃
┣ 📁 Chapters — Americas
┃ ┣ 📁 @SuperteamUSA 
┃ ┣ 📁 @SuperteamCAN 
┃ ┣ 📁 @SuperteamBR 
┃ ┗ 📁 @SuperteamAR 
┃
┣ 📁 Chapters — Europe
┃ ┣ 📁 @LaFamilia_so 
┃ ┣ 📁 @SuperteamUK 
┃ ┣ 📁 @SuperteamDE 
┃ ┣ 📁 @SuperteamTR  
┃ ┣ 📁 @SuperteamUKR 
┃ ┣ 📁 @SuperteamBLKN 
┃ ┣ 📁 @SuperteamPOL 
┃ ┣ 📁 @superteamIE 
┃ ┣ 📁 @SuperteamNL 
┃ ┗ 📁 @SuperteamGEO 
┃
┣ 📁 Chapters — Asia
┃ ┣ 📁 @SuperteamVN 
┃ ┣ 📁 @SuperteamMY 
┃ ┣ 📁 @SuperteamTH 
┃ ┣ 📁 @SuperteamAE 
┃ ┣ 📁 @SuperteamIN 
┃ ┣ 📁 @SuperteamSG 
┃ ┣ 📁 @SuperteamJapan  
┃ ┣ 📁 @SuperteamKorea 
┃ ┣ 📁 @SuperteamINDO 
┃ ┗ 📁 @SuperteamKZ 
┃
┣ 📁 Chapters — Africa
┃ ┗ 📁 @SuperteamNG 
┃
┣ 📁 Chapters — Oceania
┃ ┗ 📁 @SuperteamAU 
┃
┣ 📁 Ecosystem
┃ ┣ 📁 Solana
┃ ┣ 📁 Partners
┃ ┣ 📁 Grants
┃ ┗ 📁 Opportunities
┃
┣ 📁 @vibhu Memes
┃  ┗ 📁 http://unhinged.zip
┃
┗ 📁 Mission
  ┣ 📁 Grow Together
  ┣ 📁 Ship Together
  ┣ 📁 Create Opportunities
  ┗ 📁 Win Together](https://x.com/SuperteamAR/status/2095246522841809022) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 20:24:33 GMT
- [solmF-ONE brings @FasanaraCapital's private credit strategy onchain through @MidasRWA 

Use it in DeFi across Solana: 
solmF-ONE is integrated on @kamino in @RockawayX RWA USDC market and @SteakhouseFi USDG High Yield market](https://x.com/solana/status/2095248912487477256) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 20:34:03 GMT
- [RT by @anza_xyz: 🚨ATTENTION: large transactions have hit the testnet

https://explorer.solana.com/tx/5KxbxQxkqv2gPjRArDeFJSmfhG6X1vAbEjZFn5zGPsmLvsb4FYKbYTm7BBDSNarkEt2jL5878wmJ4cTYyvURPLnK?cluster=testnet](https://x.com/bw_solana/status/2095199360724431064) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 17:17:09 GMT `upgrade`
- [RT by @anza_xyz: Solana is the financial infra powering the token supercycle. 

We're building toward a future where the internet capital market becomes the biggest capital market.

More thoughts here:

https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/calilyliu/status/2095179874839462349) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 15:59:43 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-03 (2026-09-03 03:26:06 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~314 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~314 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **Tokenized equities (xStocks)** — HTTP 503 Service Unavailable
- **xStocks** — asset list failed on backed.fi and xstocks.fi

## Sources this run

- `rpc.getHealth` [ok] 200 203ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 165ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 189ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 173ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 154ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6049ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 366ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 54ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 34ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 141ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 19ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 25ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 30ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 65ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 27ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 59ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 78ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 188ms https://solana.com/data
- `solana.com.databricks` [ok] 200 60ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 399ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 172ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 35ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 84ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 350ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 406ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 71ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 68ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 71ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1125ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1928ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1323ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 940ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 24ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 180ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 162ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 760ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 790ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 674ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 788ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 808ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 908ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 782ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 643ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 969ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 755ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 770ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 764ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 597ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 781ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [FAIL] 503 142ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0 — HTTP 503 Service Unavailable
- `xstocks.assets.p0` [FAIL] 503 109ms https://api.xstocks.fi/api/v2/public/assets?pageSize=100&page=0 — HTTP 503 Service Unavailable
- `llama.protocol.xstocks` [ok] 200 9834ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 202ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jito.tip_floor` [ok] 200 304ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 200ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 39ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 180ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 156ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 230ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 248ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 119ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
