# Borealis — Solana ecosystem report

**Generated** 2026-09-03T06:20:28Z · 2026-09-02 23:20:28 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-03T06:20:18Z · **RPC health** `ok`
**Health score** 96 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +0.77%; DEX 24h $2.33B · 1d +7% · vs-7d-ago -1%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -11.36%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -26.46%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 856,198.00 is +26.3% vs 30d median 677,709.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 100.63 USD is +21.6% vs 30d median 82.77 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,901,022 |
| Block height | 421,948,271 |
| Block time | 2026-09-03T06:20:18Z |
| Epoch | 1,027 (54.87% · slot 237,026/432,000) |
| Mean TPS (last ~3,600s) | 3,398.3 |
| Mean non-vote TPS | 1,258.1 |
| Median TPS (same window) | 3,393.2 |
| Mean slot time | 315.1 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 544,685,903,913 |
| Circulating supply | 585,275,071 SOL |
| Total supply | 633,361,102 SOL |
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

- `xLabscif…` · 84.41K SOL · commission 5% · lag 112649 slots
- `prt1st4R…` · 78.62K SOL · commission 5% · lag 414080 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 27889 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 552299 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1114901 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 601366 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 462383 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1917268 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1100671 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1142185 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 1100565 slots
- `6pEtDovp…` · 131.86 SOL · commission 100% · lag 1114949 slots

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
| Jito tip-floor run-rate (NOT REV) | $61.53K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 61527 USD; at p95 floor → 6114399 USD. |
| Protocol fees 24h | $11.21M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9953 |
| p90 / p99 | 0.000010 / 0.000104 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $100.63 | coingecko.simple_price |
| 24h change | +0.77% | coingecko.simple_price |
| Market cap | $58.89B | coingecko.simple_price |
| 24h volume | $3.13B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.73B |
| TVL 1d / 7d / 30d | +1.49% / -0.73% / +20.29% |
| DEX volume 24h | $2.33B · 1d +7.16% · vs-7d-ago -1.05% |
| 7d DEX volume | $16.71B · -21.77% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $11.21M |
| Fees 1d / 7d | -11.36% / -26.46% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $1.02B | +23.42% |
| Orca DEX | $206.25M | -5.81% |
| BisonFi | $194.35M | -5.12% |
| Manifest Trade | $166.19M | +13.00% |
| Meteora DLMM | $137.83M | -1.54% |
| Raydium AMM | $110.82M | -27.34% |
| Axiom | $97.98M | 0.00% |
| pump.fun | $83.17M | +50.90% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.53B | +0.39% | -0.32% |
| Kamino Lend | Lending | $1.25B | +1.48% | +3.45% |
| Raydium AMM | Dexs | $1.08B | +0.23% | -2.15% |
| Jupiter Lend | Lending | $1.07B | +0.52% | -1.81% |
| Binance Staked SOL | Liquid Staking | $1.04B | +0.48% | +0.54% |
| Jito Liquid Staking | Liquid Staking | $1.01B | +0.60% | -0.34% |
| BlackRock BUIDL | RWA | $890.69M | +0.11% | -1.06% |
| Jupiter Perpetual Exchange | Derivatives | $746.13M | +0.12% | -2.75% |
| Jupiter Staked SOL | Liquid Staking | $519.16M | +0.16% | -0.85% |
| xStocks | RWA | $435.63M | +0.94% | +1.66% |

## Stablecoins

Solana circulating pegged-USD: **$15.69B**
(1d +1.58% · 7d -0.20%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.73B | +1.41% |
| USDT · Tether | $2.90B | +2.49% |
| USDGO · USDGO | $1.25B | +0.72% |
| USD1 · World Liberty Financial USD | $1.21B | -0.00% |
| BUIDL · BlackRock USD | $890.69M | +0.42% |
| PYUSD · PayPal USD | $800.60M | +8.45% |
| USDG · Global Dollar | $603.28M | -1.67% |
| USDe · Ethena USDe | $535.98M | -0.22% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 72 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 72 · priced-subset mcap $286.71M (lower bound, not a census).
24h volume $29.42M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $433.40M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 72 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $890.69M
- **xStocks** (RWA) — $435.63M
- **OnRe** (RWA) — $288.88M
- **Ondo Yield Assets** (RWA) — $179.52M
- **Hastra** (RWA) — $153.70M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $25.01M
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
- [The long tail has never had its own markets. @arqentrade is live on Solana with the infrastructure to change that.](https://x.com/solana/status/2095229262353838352) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 19:15:58 GMT
- [Read more on @CoinDesk : https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/solana/status/2095210145227616641) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 18:00:00 GMT
- [5.5 billion people on the internet. All of them use money. @calilyliu on the token supercycle.

"What we're in the midst of right now is the token supercycle. Everything of value is becoming programmable." 

"Money, assets, ownership, and markets are always going to move towards the largest market, and that largest market is the internet capital market." 

"This is not just a market rally or a near-term narrative. It's a structural transformation of global capital markets."](https://x.com/solana/status/2095210144514687362) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 18:00:00 GMT
- [RT by @anza_xyz: 🚨ATTENTION: large transactions have hit the testnet

https://explorer.solana.com/tx/5KxbxQxkqv2gPjRArDeFJSmfhG6X1vAbEjZFn5zGPsmLvsb4FYKbYTm7BBDSNarkEt2jL5878wmJ4cTYyvURPLnK?cluster=testnet](https://x.com/bw_solana/status/2095199360724431064) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 17:17:09 GMT `upgrade`
- [RT by @anza_xyz: Solana is the financial infra powering the token supercycle. 

We're building toward a future where the internet capital market becomes the biggest capital market.

More thoughts here:

https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/calilyliu/status/2095179874839462349) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 15:59:43 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

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
- [The long tail has never had its own markets. @arqentrade is live on Solana with the infrastructure to change that.](https://x.com/solana/status/2095229262353838352) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 19:15:58 GMT
- [Read more on @CoinDesk : https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/solana/status/2095210145227616641) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 18:00:00 GMT
- [5.5 billion people on the internet. All of them use money. @calilyliu on the token supercycle.

"What we're in the midst of right now is the token supercycle. Everything of value is becoming programmable." 

"Money, assets, ownership, and markets are always going to move towards the largest market, and that largest market is the internet capital market." 

"This is not just a market rally or a near-term narrative. It's a structural transformation of global capital markets."](https://x.com/solana/status/2095210144514687362) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 18:00:00 GMT
- [RT by @anza_xyz: 🚨ATTENTION: large transactions have hit the testnet

https://explorer.solana.com/tx/5KxbxQxkqv2gPjRArDeFJSmfhG6X1vAbEjZFn5zGPsmLvsb4FYKbYTm7BBDSNarkEt2jL5878wmJ4cTYyvURPLnK?cluster=testnet](https://x.com/bw_solana/status/2095199360724431064) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 17:17:09 GMT `upgrade`
- [RT by @anza_xyz: Solana is the financial infra powering the token supercycle. 

We're building toward a future where the internet capital market becomes the biggest capital market.

More thoughts here:

https://www.coindesk.com/opinion/2026/09/02/the-token-supercycle-everything-of-value-is-becoming-programmable](https://x.com/calilyliu/status/2095179874839462349) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Wed, 02 Sep 2026 15:59:43 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-03 (2026-09-02 23:20:28 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 634ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 545ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 548ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 531ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 538ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7045ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 1164ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 88ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 91ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 88ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 36ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 66ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 29ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 73ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 92ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 46ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 76ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 472ms https://solana.com/data
- `solana.com.databricks` [ok] 200 105ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 523ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 161ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 83ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 54ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 402ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 790ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 442ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 443ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 438ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 247ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1517ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1251ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 186ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 210ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 537ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 530ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2061ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1936ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1992ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2232ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1967ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1920ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2082ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2185ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2177ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2180ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1963ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2158ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 2098ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1765ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 3601ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2005ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 5446ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 4325ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1531ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1229ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 5150ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 2351ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.NVDAx` [ok] 200 490ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.METAx` [ok] 200 514ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.SPYx` [ok] 200 602ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.AAPLx` [ok] 200 719ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.AMZNx` [ok] 200 1083ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.TSLAx` [ok] 200 1380ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.SPYx` [ok] 200 806ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 972ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 913ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 712ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 607ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 484ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.MSFTx` [ok] 200 2178ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.mult.TSLAx` [ok] 200 623ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.NVDAx` [ok] 200 1801ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.MSFTx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 640ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.MVLLx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.mult.METAx` [ok] 200 1370ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.DRAMx` [ok] 200 644ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.GOOGLx` [ok] 200 3167ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.mult.QQQx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.circ.MVLLx` [ok] 200 782ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.MUUx` [ok] 200 608ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.mult.MSFTx` [ok] 200 1185ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.MVLLx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 1500ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.KORUx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 732ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.KORUx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 1441ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 765ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.DJTx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 1659ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 770ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.price.INTWx` [ok] 200 913ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.mult.DJTx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 740ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 993ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 534ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.SHEINx` [ok] 200 577ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.SOXSx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 734ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 1144ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 1284ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.mult.INTWx` [ok] 200 648ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.SHEINx` [ok] 200 768ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.MMGx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.SHEINx` [ok] 200 605ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 519ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 1344ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.SNXXx` [ok] 200 1173ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.circ.MUUx` [ok] 200 3893ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.SNXXx` [ok] 200 446ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.mult.MUUx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.TNGYIx` [ok] 200 1682ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 1541ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.CTINSx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.BANKCx` [ok] 200 1759ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 5849ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.mult.CTINSx` [ok] 200 1111ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 1031ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 2115ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.price.KUNLx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.BANKCx` [ok] 200 1102ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 760ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 1003ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 3256ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 1956ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.WRFHDx` [ok] 200 2161ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.TNGYIx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 2892ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 624ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 5344ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 867ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 937ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 2123ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [ok] 200 2422ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.HRZRBx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 1083ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 1572ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 797ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.SMOIHx` [ok] 200 724ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 1582ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 487ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 796ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 1695ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.CSPCx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.CRESMx` [ok] 200 384ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.CMERPx` [ok] 200 1079ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 494ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 496ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 549ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.SZIGHx` [ok] 200 566ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.CSPCx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 462ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 858ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 1220ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 1389ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 902ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 575ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.NWGx` [FAIL]  12023ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.CRESBx` [ok] 200 3550ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.WHRFRx` [ok] 200 616ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.price.CMENDx` [ok] 200 2345ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.CRESBx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 290ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 785ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.CRESBx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.NWGx` [ok] 200 1553ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 3366ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.CMENDx` [ok] 200 1105ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 790ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 1255ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.SITCx` [ok] 200 2514ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.CRESPx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 3304ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.SITCx` [ok] 200 651ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 810ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.circ.CRESPx` [ok] 200 909ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 1169ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.mult.CRESPx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.NWGx` [ok] 200 1904ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.price.JDHLTx` [ok] 200 3810ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.mult.SITCx` [ok] 200 869ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 618ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.SINOx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.SINOTx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 989ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 420ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 3220ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.PWAHLx` [ok] 200 411ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 1167ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 1697ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 807ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.SNDSCx` [ok] 200 973ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.GENTEx` [ok] 200 599ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 2002ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 1645ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 1532ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.CKAHx` [ok] 200 554ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 943ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.GENTEx` [ok] 200 842ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 313ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 278ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.CKAHx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 1841ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.CRAUTx` [ok] 200 273ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 1132ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 667ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 801ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 5236ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 984ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.CKINFx` [ok] 200 1568ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.KUAIx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.COVELx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 1448ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.price.CHONGx` [ok] 200 503ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.PRADx` [ok] 200 1100ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.circ.CHONGx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 759ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 5159ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 1570ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.price.MTRCPx` [ok] 200 1078ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.GEELx` [ok] 200 1313ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.circ.MEITx` [ok] 200 1718ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.HNDLDx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 3109ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.MTRCPx` [ok] 200 487ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.COSCx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 834ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.MEITx` [ok] 200 1201ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.price.CKHUTx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.COSCx` [ok] 200 763ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 2207ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 8305ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 7285ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 7206ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 5401ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 1531ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 6524ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 279ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.MEITx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 131ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.HKEXCx` [ok] 200 107ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 148ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.SHEINx` [ok] 200 145ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.BANKCx` [ok] 200 131ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.PRADx` [ok] 200 142ms https://lite-api.jup.ag/tokens/v2/search?query=PRADx
- `jup.tokens.search.HKCGAx` [ok] 200 122ms https://lite-api.jup.ag/tokens/v2/search?query=HKCGAx
- `jito.tip_floor` [ok] 200 101ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 454ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 161ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 524ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 528ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 529ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 530ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 3185ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
