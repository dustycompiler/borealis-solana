# Borealis — Solana ecosystem report

**Generated** 2026-09-03T06:41:47Z · 2026-09-02 23:41:47 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-03T06:41:36Z · **RPC health** `ok`
**Health score** 96 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +0.87%; DEX 24h $2.33B · 1d +7% · vs-7d-ago -1%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -11.36%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is -26.46%. (threshold: `|7d %| >= 20`)
- **INFO · Daily active addresses vs 30d median** — Current 856,198.00 is +26.3% vs 30d median 677,709.00 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 100.89 USD is +21.9% vs 30d median 82.77 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,905,076 |
| Block height | 421,952,323 |
| Block time | 2026-09-03T06:41:36Z |
| Epoch | 1,027 (55.81% · slot 241,078/432,000) |
| Mean TPS (last ~3,600s) | 3,322.5 |
| Mean non-vote TPS | 1,183.0 |
| Median TPS (same window) | 3,297.9 |
| Mean slot time | 315.2 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 544,690,124,727 |
| Circulating supply | 585,275,060 SOL |
| Total supply | 633,361,091 SOL |
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

- `xLabscif…` · 84.41K SOL · commission 5% · lag 116703 slots
- `prt1st4R…` · 78.62K SOL · commission 5% · lag 418134 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 31943 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 556353 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 1118955 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 605420 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 466437 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1921322 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 1104725 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 1146239 slots
- `HFTcVVrX…` · 149.48 SOL · commission 100% · lag 1104619 slots
- `6pEtDovp…` · 131.86 SOL · commission 100% · lag 1119003 slots

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
| Jito tip-floor run-rate (NOT REV) | $69.52K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 69524 USD; at p95 floor → 3378321 USD. |
| Protocol fees 24h | $11.21M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9954 |
| p90 / p99 | 0.000009 / 0.000107 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $100.89 | coingecko.simple_price |
| 24h change | +0.87% | coingecko.simple_price |
| Market cap | $59.05B | coingecko.simple_price |
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
Listed 726 · Solana deployments 726 · priced 72 · priced-subset mcap $286.80M (lower bound, not a census).
24h volume $29.33M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
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

_As of 2026-09-03 (2026-09-02 23:41:47 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 230ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 213ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 278ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 270ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 205ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6815ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 417ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 146ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 25ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 190ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 71ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 26ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 33ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 71ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 40ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 60ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 85ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 401ms https://solana.com/data
- `solana.com.databricks` [ok] 200 48ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 445ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 97ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 88ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 43ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 302ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 828ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 439ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 441ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 430ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1454ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1294ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1672ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 177ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 249ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 217ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 218ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 877ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 893ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1137ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 927ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 792ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 860ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 906ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 966ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 817ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 915ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 734ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 930ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 853ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 863ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 4383ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 6779ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 4319ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 2363ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 3291ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2215ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2479ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 821ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [ok] 200 337ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.AAPLx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.SPYx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.TSLAx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 825ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.mult.TSLAx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 748ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.GOOGLx` [ok] 200 1470ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.mult.SPYx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 1195ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.NVDAx` [ok] 200 1909ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.AMZNx` [ok] 200 1967ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.METAx` [ok] 200 1510ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 431ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 876ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 938ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 374ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 631ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 764ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.MUUx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.price.MSFTx` [ok] 200 3184ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.DJTx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.price.MVLLx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.circ.MUUx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 2091ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.price.DRAMx` [ok] 200 1134ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.circ.DJTx` [ok] 200 687ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 966ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.KORUx` [ok] 200 597ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.mult.DJTx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.mult.MUUx` [ok] 200 1078ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.INTWx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.price.COINx` [ok] 200 3040ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.MSFTx` [ok] 200 485ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.KORUx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.price.SNXXx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.mult.COINx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.circ.SNXXx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 627ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.MVLLx` [ok] 200 1921ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.price.SOXSx` [ok] 200 789ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.SHEINx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.SOXSx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 2688ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.mult.INTWx` [ok] 200 670ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 296ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.mult.SHEINx` [ok] 200 994ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.SNXXx` [ok] 200 1673ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.TNGYIx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 522ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 806ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.MVLLx` [ok] 200 2482ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.BANKCx` [ok] 200 2275ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 845ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 4252ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 903ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 490ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 939ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.SOXSx` [ok] 200 3540ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 770ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.mult.MMGx` [ok] 200 675ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 2456ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 561ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.CTINSx` [ok] 200 678ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.JDLOGx` [ok] 200 627ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 569ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.WRFHDx` [ok] 200 1219ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.KUNLx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.SZIGHx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 1768ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 1243ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 452ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 3091ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.SMOIHx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 1169ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.HAIDLx` [ok] 200 2639ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 1082ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.ENNHLx` [ok] 200 2420ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 1173ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 1874ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 1819ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.price.CSPCx` [ok] 200 461ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 3595ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 1307ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 1673ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.CRESBx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 706ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.SNBIOx` [ok] 200 5709ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 294ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 1072ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.CMERPx` [ok] 200 3086ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.CRESMx` [ok] 200 1882ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.NWGx` [FAIL]  12022ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.SNBIOx` [ok] 200 1169ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 2685ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 2869ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.MIXUx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 1533ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 367ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 3739ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 939ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.NWGx` [ok] 200 1366ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 910ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.CMENDx` [ok] 200 925ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 1630ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 2509ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 1360ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.NWGx` [ok] 200 1161ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 1685ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.BDWAPx` [ok] 200 2455ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.MIXUx` [ok] 200 830ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 635ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 1151ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.mult.CMERPx` [ok] 200 1530ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 811ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 1210ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.JDHLTx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.SNDSCx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 2130ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 1611ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 770ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.PRADx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 1258ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 455ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.SNDSCx` [ok] 200 1168ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 1327ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.PRADx` [ok] 200 895ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 1695ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.CRESPx` [ok] 200 2034ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.CLONPx` [ok] 200 688ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.SINOTx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 718ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 1493ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.WHRFRx` [ok] 200 4589ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 1012ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.CTPCAx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 1706ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.SINOx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 703ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 1565ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 976ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 2409ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 1667ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 1555ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 2197ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 1627ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.GENTEx` [ok] 200 1106ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.HKCGAx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.WUXIBx` [ok] 200 601ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.CRAUTx` [ok] 200 1155ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.GENTEx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 575ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.KUAIx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 752ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.WUXIBx` [ok] 200 967ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 1560ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.CKAHx` [ok] 200 1585ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 190ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 1712ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 2641ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.SINOTx` [ok] 200 5584ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.CKAHx` [ok] 200 1436ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.MEITx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.NONGx` [ok] 200 1279ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.CKINFx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 1190ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.GEELx` [ok] 200 724ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.COVELx` [ok] 200 2021ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.NONGx` [ok] 200 499ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 766ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.mult.CKINFx` [ok] 200 1533ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.HNDLDx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 2527ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 2413ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.COVELx` [ok] 200 1939ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 551ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 3762ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.price.PICCx` [ok] 200 1940ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 533ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 1302ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.circ.CHONGx` [ok] 200 593ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 2500ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 861ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.mult.COVELx` [ok] 200 1388ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 868ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 690ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.CKHUTx` [ok] 200 1767ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 37ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 203ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.MEITx` [ok] 200 110ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 103ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.HKEXCx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 106ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.SHEINx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.BANKCx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.PRADx` [ok] 200 107ms https://lite-api.jup.ag/tokens/v2/search?query=PRADx
- `jup.tokens.search.HKCGAx` [ok] 200 103ms https://lite-api.jup.ag/tokens/v2/search?query=HKCGAx
- `jito.tip_floor` [ok] 200 103ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 422ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 121ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 493ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 442ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 417ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 461ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 141ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
