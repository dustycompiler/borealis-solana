# Borealis — Solana ecosystem report

**Generated** 2026-09-03T09:39:33Z · 2026-09-03 02:39:33 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-03T09:39:22Z · **RPC health** `ok`
**Health score** 99 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +1.71%; DEX 24h $2.33B · 1d +7% · vs-7d-ago -1%; slot 303 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -11.36%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -26.46%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 856,198.00 is +26.3% vs 30d median 677,709.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 100.31 USD is +21.2% vs 30d median 82.77 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,938,994 |
| Block height | 421,986,216 |
| Block time | 2026-09-03T09:39:22Z |
| Epoch | 1,027 (63.66% · slot 274,995/432,000) |
| Mean TPS (last ~3,600s) | 3,930.8 |
| Mean non-vote TPS | 1,490.5 |
| Median TPS (same window) | 3,418.2 |
| Mean slot time | 303.5 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 544,726,749,426 |
| Circulating supply | 585,274,957 SOL |
| Total supply | 633,360,993 SOL |
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

- `xLabscif…` · 84.41K SOL · commission 5% · lag 150621 slots
- `prt1st4R…` · 78.62K SOL · commission 5% · lag 452052 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 65861 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 590271 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1152873 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 639338 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 500355 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1955240 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1138643 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1180157 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 1138537 slots
- `6pEtDovp…` · 131.86 SOL · commission 100% · lag 1152921 slots

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
| Jito tip-floor run-rate (NOT REV) | $129.18K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 129182 USD; at p95 floor → 12993769 USD. |
| Protocol fees 24h | $11.21M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.9h · n_tx=2240 window_seconds=10329 |
| p90 / p99 | 0.000010 / 0.000110 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $100.31 | coingecko.simple_price |
| 24h change | +1.71% | coingecko.simple_price |
| Market cap | $58.71B | coingecko.simple_price |
| 24h volume | $3.17B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.75B |
| TVL 1d / 7d / 30d | +1.88% / -0.34% / +20.76% |
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
| Sanctum Validator LSTs | Liquid Staking | $1.53B | +0.38% | +0.13% |
| Kamino Lend | Lending | $1.27B | +2.92% | +4.89% |
| Raydium AMM | Dexs | $1.08B | +0.23% | -2.15% |
| Jupiter Lend | Lending | $1.07B | +1.01% | -1.87% |
| Binance Staked SOL | Liquid Staking | $1.04B | +0.77% | +0.75% |
| Jito Liquid Staking | Liquid Staking | $1.01B | +1.63% | -0.46% |
| BlackRock BUIDL | RWA | $890.69M | +0.11% | -1.06% |
| Jupiter Perpetual Exchange | Derivatives | $749.90M | +0.53% | -2.29% |
| Jupiter Staked SOL | Liquid Staking | $522.84M | +0.80% | -0.38% |
| xStocks | RWA | $436.72M | +1.29% | +1.30% |

## Stablecoins

Solana circulating pegged-USD: **$15.70B**
(1d +1.57% · 7d -0.21%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.71B | +1.15% |
| USDT · Tether | $2.90B | +2.49% |
| USDGO · USDGO | $1.28B | +2.41% |
| USD1 · World Liberty Financial USD | $1.21B | -0.00% |
| BUIDL · BlackRock USD | $890.69M | +0.42% |
| PYUSD · PayPal USD | $810.95M | +9.86% |
| USDG · Global Dollar | $603.19M | -1.67% |
| USDe · Ethena USDe | $535.96M | -0.22% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 73 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 73 · priced-subset mcap $287.17M (lower bound, not a census).
24h volume $28.74M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $436.72M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 73 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $890.69M
- **xStocks** (RWA) — $436.72M
- **OnRe** (RWA) — $288.99M
- **Ondo Yield Assets** (RWA) — $179.13M
- **Hastra** (RWA) — $153.74M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $25.02M
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

_As of 2026-09-03 (2026-09-03 02:39:33 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~304 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~304 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 139ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 82ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 124ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 74ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 182ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6417ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 179ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 241ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 141ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 102ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 740ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 39ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1058ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 132ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 298ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 92ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 108ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 355ms https://solana.com/data
- `solana.com.databricks` [ok] 200 156ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 506ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 154ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 85ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 113ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 328ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 604ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 264ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 263ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 253ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 547ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1398ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1416ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 274ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 181ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 81ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 75ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 261ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 323ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 363ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 480ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 492ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 623ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 65ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 635ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 438ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 549ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 529ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 412ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 455ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 304ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 313ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 5065ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 3758ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 3142ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2228ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 3486ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2874ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 3890ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 907ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AAPLx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.MSFTx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.NVDAx` [ok] 200 549ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.MSFTx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.GOOGLx` [ok] 200 644ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.METAx` [ok] 200 671ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.NVDAx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.AMZNx` [ok] 200 748ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.mult.MSFTx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.price.TSLAx` [ok] 200 928ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.mult.NVDAx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.AMZNx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 508ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.METAx` [ok] 200 594ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.SPYx` [ok] 200 1362ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.mult.METAx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 588ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.AXTIx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.circ.COINx` [ok] 200 729ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.MUUx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.circ.SPYx` [ok] 200 686ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.MUUx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 544ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.MVLLx` [ok] 200 1101ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.price.INTWx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.DJTx` [ok] 200 962ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.mult.AAPLx` [ok] 200 2055ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.KORUx` [ok] 200 746ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.price.DRAMx` [ok] 200 2040ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.circ.INTWx` [ok] 200 567ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 414ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.DJTx` [ok] 200 721ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 530ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.price.SHEINx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.KORUx` [ok] 200 1003ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 522ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.circ.SHEINx` [ok] 200 254ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.SHEINx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 3712ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.NWGx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.circ.AXTIx` [ok] 200 2796ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.BANKCx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.QQQx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.SOXSx` [ok] 200 1730ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.circ.BANKCx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.SNXXx` [ok] 200 1114ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.mult.KORUx` [ok] 200 888ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 2397ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.AXTIx` [ok] 200 497ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.SNXXx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 510ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.SOXSx` [ok] 200 905ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.SUOPTx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.SNXXx` [ok] 200 609ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 1073ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.MMGx` [ok] 200 1011ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.SOXSx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 1373ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 839ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.MMGx` [ok] 200 747ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 1258ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 1142ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 945ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.JDLOGx` [ok] 200 1842ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.NWGx` [ok] 200 3405ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.CTINSx` [ok] 200 1934ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 1035ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 1072ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.CTINSx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.HRZRBx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 1521ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 616ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 608ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 1169ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 454ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 2255ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.NWGx` [ok] 200 1975ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 1239ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 530ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 621ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 884ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 641ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.circ.CRESBx` [ok] 200 1072ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.JTGEXx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 1422ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.CRESMx` [ok] 200 1147ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.circ.CMENDx` [ok] 200 793ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 1402ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 159ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 1428ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 1376ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.CRESBx` [ok] 200 1785ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 2410ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.CRESMx` [ok] 200 1224ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 564ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 2695ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 1304ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 925ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.mult.SITCx` [ok] 200 552ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.ASMPTx` [ok] 200 1022ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.JDHLTx` [ok] 200 771ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 1084ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 550ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.PRADx` [ok] 200 1051ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.SINOTx` [ok] 200 650ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.PRADx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 2171ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 537ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 674ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 2592ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.SINOTx` [ok] 200 776ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 2708ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.WHGROx` [ok] 200 650ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.PRADx` [ok] 200 2103ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 1351ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.WHGROx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 704ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.CLPHDx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 958ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 2518ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.CRAUTx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 3793ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 958ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 1541ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.CLONPx` [ok] 200 1649ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.MIXUx` [ok] 200 5399ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 753ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 412ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 1132ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 1027ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.CLONPx` [ok] 200 916ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 995ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.COVELx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.HKEXCx` [ok] 200 619ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.COVELx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 643ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 1266ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.mult.NONGx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.CKAHx` [ok] 200 1035ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 1691ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 867ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.CHONGx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 1025ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 576ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 1469ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 1367ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.GENTEx` [ok] 200 4088ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 669ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 1711ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.GEELx` [ok] 200 2253ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 1331ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 691ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.price.HNDLDx` [ok] 200 2405ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.MEITx` [ok] 200 657ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.COSCx` [ok] 200 2016ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.CKHUTx` [ok] 200 709ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 1703ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.CHONGx` [ok] 200 5837ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 1923ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 7638ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 6532ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.KUAIx` [ok] 200 690ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 4366ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 391ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.MEITx` [ok] 200 88ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 85ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.HKEXCx` [ok] 200 88ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.SHEINx` [ok] 200 96ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.BANKCx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.PRADx` [ok] 200 84ms https://lite-api.jup.ag/tokens/v2/search?query=PRADx
- `jup.tokens.search.HKCGAx` [ok] 200 86ms https://lite-api.jup.ag/tokens/v2/search?query=HKCGAx
- `jito.tip_floor` [ok] 200 134ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 337ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 138ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 63ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 52ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 71ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 96ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 346ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
