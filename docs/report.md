# Borealis — Solana ecosystem report

**Generated** 2026-09-03T10:07:19Z · 2026-09-03 03:07:19 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-03T10:07:09Z · **RPC health** `ok`
**Health score** 99 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +1.90%; DEX 24h $2.33B · 1d +7% · vs-7d-ago -1%; slot 305 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -11.36%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -26.46%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 856,198.00 is +26.3% vs 30d median 677,709.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 100.15 USD is +21.0% vs 30d median 82.77 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,944,291 |
| Block height | 421,991,505 |
| Block time | 2026-09-03T10:07:09Z |
| Epoch | 1,027 (64.88% · slot 280,292/432,000) |
| Mean TPS (last ~3,600s) | 3,926.7 |
| Mean non-vote TPS | 1,497.1 |
| Median TPS (same window) | 3,475.2 |
| Mean slot time | 305.1 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 544,732,431,019 |
| Circulating supply | 585,274,941 SOL |
| Total supply | 633,360,978 SOL |
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

- `xLabscif…` · 84.41K SOL · commission 5% · lag 155918 slots
- `prt1st4R…` · 78.62K SOL · commission 5% · lag 457349 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 71158 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 595568 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1158170 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 644635 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 505652 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1960537 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1143940 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1185454 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 1143834 slots
- `6pEtDovp…` · 131.86 SOL · commission 100% · lag 1158218 slots

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
| Jito tip-floor run-rate (NOT REV) | $77.72K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 77724 USD; at p95 floor → 9609549 USD. |
| Protocol fees 24h | $11.21M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.9h · n_tx=2240 window_seconds=10279 |
| p90 / p99 | 0.000010 / 0.000091 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $100.15 | coingecko.simple_price |
| 24h change | +1.90% | coingecko.simple_price |
| Market cap | $58.61B | coingecko.simple_price |
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

Priced-subset lower bound: quote × circulating × live currentMultiplier over 2 of 100 Solana-deployed listed symbols (multiplier ok 14/80; 100 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 100 · Solana deployments 100 · priced 2 · priced-subset mcap $121.90 (lower bound, not a census).
24h volume $28.79M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $436.72M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 14 / mcap_computable 2 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 100 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 100 unique underlyings among 100 Solana rows; not every tokenized equity on Solana). 100 of 100 listed xStocks have a Solana deployment (100 unique underlyings). Count share, not market-cap share.

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

_As of 2026-09-03 (2026-09-03 03:07:19 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~305 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~305 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **xStocks** — priced up to 80 of 100 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.
- **xStocks** — MUUx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SOXSx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MVLLx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — KORUx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — DJTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — INTWx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SNXXx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SHEINx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — LAOPGx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MMGx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — ZHAOMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — BANKCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SUOPTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — JDLOGx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CTINSx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SNBIOx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — WRFHDx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SZIGHx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — ENNHLx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — HAIDLx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SMOIHx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CRESBx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — HRZRBx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CMERPx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — JTGEXx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CRESMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — WXXDCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CSPCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CMENDx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — ASMPTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — JDHLTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SNDSCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CRESPx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — PRADx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SINOTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CLONPx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CTFJWx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — WHGROx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — WUXIBx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — PWAHLx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CLPHDx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — GENTEx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CRAUTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SWPRPx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CKINFx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — HKCGAx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — KUAIx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — HKEXCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — NONGx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — COVELx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CHONGx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MEITx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — BOCOMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CPETCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MTRCPx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — POPMTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CKHUTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — PICCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — HNDLDx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — COSCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CRESLx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — HAIERx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — BOCHKx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CITICx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — ZJGLDx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — PSBOCx multiplier missing — mcap omitted (never assumed 1.0)

## Sources this run

- `rpc.getHealth` [ok] 200 125ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 86ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 103ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 86ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 80ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5684ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 236ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 91ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 22ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 547ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 28ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 22ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 28ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 63ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 218ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 62ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 77ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 430ms https://solana.com/data
- `solana.com.databricks` [ok] 200 61ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 471ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 101ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 1148ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 94ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 228ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 888ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 437ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 435ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 444ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 2301ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1607ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1177ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 171ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 14ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 84ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 110ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 405ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 499ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 427ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 480ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 428ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 396ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 400ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 453ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 390ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 423ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 354ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 499ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 374ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 376ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [FAIL]  15043ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0 — TimeoutError: The read operation timed out
- `xstocks.assets.p0` [ok] 200 11345ms https://api.xstocks.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [FAIL]  15011ms https://api.xstocks.fi/api/v2/public/assets?pageSize=100&page=1 — TimeoutError: The read operation timed out
- `xstocks.price.AXTIx` [ok] 200 600ms https://api.xstocks.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.MVLLx` [FAIL]  12013ms https://api.xstocks.fi/api/v2/public/assets/MVLLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DRAMx` [FAIL]  12014ms https://api.xstocks.fi/api/v2/public/assets/DRAMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.KORUx` [FAIL]  12012ms https://api.xstocks.fi/api/v2/public/assets/KORUx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MUUx` [FAIL]  12014ms https://api.xstocks.fi/api/v2/public/assets/MUUx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SOXSx` [FAIL]  12023ms https://api.xstocks.fi/api/v2/public/assets/SOXSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.INTWx` [FAIL]  12024ms https://api.xstocks.fi/api/v2/public/assets/INTWx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DJTx` [FAIL]  12025ms https://api.xstocks.fi/api/v2/public/assets/DJTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AXTIx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.AXTIx` [ok] 200 2801ms https://api.xstocks.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 2929ms https://api.xstocks.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.circ.DRAMx` [ok] 200 6958ms https://api.xstocks.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.circ.KORUx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/KORUx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.MVLLx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.SOXSx` [FAIL]  12010ms https://api.xstocks.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.MUUx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/MUUx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.DJTx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/DJTx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.INTWx` [FAIL]  12023ms https://api.xstocks.fi/api/v2/public/assets/INTWx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.DRAMx` [ok] 200 9168ms https://api.xstocks.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.SNXXx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.MUUx` [FAIL]  12013ms https://api.xstocks.fi/api/v2/public/assets/MUUx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.SOXSx` [FAIL]  12017ms https://api.xstocks.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.MVLLx` [FAIL]  12018ms https://api.xstocks.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.KORUx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/KORUx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.DJTx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/DJTx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.INTWx` [FAIL]  12018ms https://api.xstocks.fi/api/v2/public/assets/INTWx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.NWGx` [ok] 200 3662ms https://api.xstocks.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.price.SHEINx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/SHEINx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SNXXx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.BANKCx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/BANKCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SUOPTx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/SUOPTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MMGx` [FAIL]  12018ms https://api.xstocks.fi/api/v2/public/assets/MMGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ZHAOMx` [FAIL]  12013ms https://api.xstocks.fi/api/v2/public/assets/ZHAOMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.TNGYIx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/TNGYIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.NWGx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/NWGx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.SHEINx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.NWGx` [ok] 200 2407ms https://api.xstocks.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [FAIL]  12010ms https://api.xstocks.fi/api/v2/public/assets/LAOPGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.LAOPGx` [ok] 200 1556ms https://api.xstocks.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.BANKCx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.SUOPTx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.MMGx` [FAIL]  12023ms https://api.xstocks.fi/api/v2/public/assets/MMGx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.ZHAOMx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.TNGYIx` [FAIL]  12018ms https://api.xstocks.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.TNGYIx` [ok] 200 3575ms https://api.xstocks.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.SHEINx` [FAIL]  12015ms https://api.xstocks.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.JDLOGx` [FAIL]  12023ms https://api.xstocks.fi/api/v2/public/assets/JDLOGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CTINSx` [ok] 200 2758ms https://api.xstocks.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.LAOPGx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.MMGx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/MMGx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.ZHAOMx` [FAIL]  12014ms https://api.xstocks.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.BANKCx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.SUOPTx` [FAIL]  12025ms https://api.xstocks.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.SNBIOx` [ok] 200 2718ms https://api.xstocks.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.KUNLx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/KUNLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.JDLOGx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.CTINSx` [FAIL]  12017ms https://api.xstocks.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.WRFHDx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/WRFHDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HAIDLx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/HAIDLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.ENNHLx` [FAIL]  12016ms https://api.xstocks.fi/api/v2/public/assets/ENNHLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SZIGHx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/SZIGHx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.SNBIOx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.KUNLx` [FAIL]  12017ms https://api.xstocks.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.JDLOGx` [FAIL]  12014ms https://api.xstocks.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.CTINSx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.KUNLx` [ok] 200 2247ms https://api.xstocks.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [FAIL]  12010ms https://api.xstocks.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.SZIGHx` [ok] 200 8738ms https://api.xstocks.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.HAIDLx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.SNBIOx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.SMOIHx` [FAIL]  12008ms https://api.xstocks.fi/api/v2/public/assets/SMOIHx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CRESBx` [FAIL]  12012ms https://api.xstocks.fi/api/v2/public/assets/CRESBx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HRZRBx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/HRZRBx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.WRFHDx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.SZIGHx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.SMOIHx` [ok] 200 5306ms https://api.xstocks.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.HAIDLx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.JTGEXx` [ok] 200 5785ms https://api.xstocks.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.CMERPx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/CMERPx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CRESBx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.HRZRBx` [FAIL]  12016ms https://api.xstocks.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.CSPCx` [FAIL]  12010ms https://api.xstocks.fi/api/v2/public/assets/CSPCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SMOIHx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.WXXDCx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/WXXDCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CRESMx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/CRESMx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CMERPx` [ok] 200 10036ms https://api.xstocks.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.JTGEXx` [FAIL]  12014ms https://api.xstocks.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.CRESMx` [ok] 200 2985ms https://api.xstocks.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 6256ms https://api.xstocks.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.HRZRBx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.CSPCx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.CMENDx` [FAIL]  12009ms https://api.xstocks.fi/api/v2/public/assets/CMENDx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CMERPx` [FAIL]  12018ms https://api.xstocks.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.JTGEXx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.CRESMx` [FAIL]  12023ms https://api.xstocks.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.WXXDCx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.BDWAPx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/BDWAPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MIXUx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/MIXUx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CSPCx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.CMENDx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.ASMPTx` [FAIL]  12015ms https://api.xstocks.fi/api/v2/public/assets/ASMPTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WHRFRx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/WHRFRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SITCx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/SITCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WHRFRx` [ok] 200 816ms https://api.xstocks.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 886ms https://api.xstocks.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/JDHLTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MIXUx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.BDWAPx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.SNDSCx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/SNDSCx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SITCx` [ok] 200 4109ms https://api.xstocks.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 2194ms https://api.xstocks.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 5241ms https://api.xstocks.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [FAIL]  12017ms https://api.xstocks.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.ASMPTx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.MIXUx` [ok] 200 8722ms https://api.xstocks.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 9243ms https://api.xstocks.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.CRESPx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/CRESPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PRADx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/PRADx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SINOTx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/SINOTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CLONPx` [ok] 200 5742ms https://api.xstocks.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.CTFJWx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/CTFJWx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.ASMPTx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.JDHLTx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.SNDSCx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.CRESPx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.PRADx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/PRADx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.SINOTx` [FAIL]  12010ms https://api.xstocks.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.CLONPx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.CTFJWx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.WHGROx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/WHGROx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SINOx` [ok] 200 10007ms https://api.xstocks.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.SINOx` [ok] 200 2564ms https://api.xstocks.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 9774ms https://api.xstocks.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.CRESPx` [FAIL]  12011ms https://api.xstocks.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.PRADx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/PRADx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.SINOTx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.CLONPx` [FAIL]  12018ms https://api.xstocks.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.CTFJWx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.WHGROx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.CTPCAx` [ok] 200 7416ms https://api.xstocks.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 10299ms https://api.xstocks.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 2980ms https://api.xstocks.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [FAIL]  12014ms https://api.xstocks.fi/api/v2/public/assets/PWAHLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CLPHDx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/CLPHDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GENTEx` [FAIL]  12016ms https://api.xstocks.fi/api/v2/public/assets/GENTEx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CRAUTx` [FAIL]  12013ms https://api.xstocks.fi/api/v2/public/assets/CRAUTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WUXIBx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/WUXIBx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.WHGROx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.WUXIBx` [ok] 200 2189ms https://api.xstocks.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/SWPRPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CKAHx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/CKAHx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.PWAHLx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.CLPHDx` [FAIL]  12014ms https://api.xstocks.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.GENTEx` [FAIL]  12010ms https://api.xstocks.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.CRAUTx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.SWPRPx` [ok] 200 7724ms https://api.xstocks.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.CKINFx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/CKINFx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.WUXIBx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.CKAHx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.CKAHx` [ok] 200 2184ms https://api.xstocks.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.CLPHDx` [FAIL]  12015ms https://api.xstocks.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.GENTEx` [FAIL]  12023ms https://api.xstocks.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.CRAUTx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.SWPRPx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.CKINFx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.HKCGAx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/HKCGAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.KUAIx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/KUAIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.HKEXCx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/HKEXCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.NONGx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/NONGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.COVELx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/COVELx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CHONGx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/CHONGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MEITx` [FAIL]  12009ms https://api.xstocks.fi/api/v2/public/assets/MEITx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CKINFx` [FAIL]  12018ms https://api.xstocks.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.HKCGAx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.price.GEELx` [ok] 200 3023ms https://api.xstocks.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.KUAIx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.HKEXCx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.NONGx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/NONGx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.COVELx` [FAIL]  12014ms https://api.xstocks.fi/api/v2/public/assets/COVELx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.CHONGx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.MEITx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/MEITx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.HKCGAx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.GEELx` [FAIL]  12017ms https://api.xstocks.fi/api/v2/public/assets/GEELx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.KUAIx` [FAIL]  12009ms https://api.xstocks.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.HKEXCx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.NONGx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/NONGx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.COVELx` [FAIL]  12025ms https://api.xstocks.fi/api/v2/public/assets/COVELx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.CHONGx` [FAIL]  12011ms https://api.xstocks.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.MEITx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/MEITx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.GEELx` [ok] 200 6882ms https://api.xstocks.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/MTRCPx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.BOCOMx` [ok] 200 3808ms https://api.xstocks.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.price.CPETCx` [ok] 200 4742ms https://api.xstocks.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.price.PICCx` [ok] 200 9793ms https://api.xstocks.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.HNDLDx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/HNDLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.COSCx` [FAIL]  12018ms https://api.xstocks.fi/api/v2/public/assets/COSCx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CKHUTx` [FAIL]  12008ms https://api.xstocks.fi/api/v2/public/assets/CKHUTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.POPMTx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/POPMTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BOCOMx` [ok] 200 8894ms https://api.xstocks.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.circ.CPETCx` [ok] 200 8565ms https://api.xstocks.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.POPMTx` [ok] 200 6888ms https://api.xstocks.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 7573ms https://api.xstocks.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.circ.PICCx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/PICCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.HNDLDx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.COSCx` [FAIL]  12011ms https://api.xstocks.fi/api/v2/public/assets/COSCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.BOCOMx` [FAIL]  12030ms https://api.xstocks.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.CPETCx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.MTRCPx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.POPMTx` [FAIL]  12023ms https://api.xstocks.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.CKHUTx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.PICCx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/PICCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.HNDLDx` [FAIL]  12022ms https://api.xstocks.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.COSCx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/COSCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.HAIERx` [ok] 200 6013ms https://api.xstocks.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.price.BOCHKx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/BOCHKx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CITICx` [ok] 200 11140ms https://api.xstocks.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.price.CRESLx` [ok] 200 8962ms https://api.xstocks.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.price.ANTASx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/ANTASx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CRESLx` [ok] 200 1808ms https://api.xstocks.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.price.ZJGLDx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/ZJGLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.PSBOCx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/PSBOCx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.HAIERx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.BOCHKx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.CITICx` [FAIL]  12026ms https://api.xstocks.fi/api/v2/public/assets/CITICx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.ANTASx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.CRESLx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.ZJGLDx` [FAIL]  12019ms https://api.xstocks.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.circ.PSBOCx` [FAIL]  12017ms https://api.xstocks.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object — TimeoutError: The read operation timed out
- `xstocks.mult.ANTASx` [ok] 200 5953ms https://api.xstocks.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.mult.HAIERx` [FAIL]  12014ms https://api.xstocks.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.BOCHKx` [FAIL]  12021ms https://api.xstocks.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.CITICx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/CITICx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.ZJGLDx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.PSBOCx` [FAIL]  12020ms https://api.xstocks.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `llama.protocol.xstocks` [ok] 200 49ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 430ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.CTPCAx` [ok] 200 101ms https://lite-api.jup.ag/tokens/v2/search?query=CTPCAx
- `jup.tokens.search.SINOx` [ok] 200 102ms https://lite-api.jup.ag/tokens/v2/search?query=SINOx
- `jup.tokens.search.AXTIx` [ok] 200 100ms https://lite-api.jup.ag/tokens/v2/search?query=AXTIx
- `jup.tokens.search.DRAMx` [ok] 200 107ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jup.tokens.search.MUUx` [ok] 200 99ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.SOXSx` [ok] 200 97ms https://lite-api.jup.ag/tokens/v2/search?query=SOXSx
- `jup.tokens.search.MVLLx` [ok] 200 107ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.KORUx` [ok] 200 110ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jito.tip_floor` [ok] 200 429ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 373ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 123ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 441ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 327ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 328ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 328ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 214ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
