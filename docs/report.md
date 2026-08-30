# Borealis — Solana ecosystem report

**Generated** 2026-08-30T20:18:40Z · 2026-08-30 13:18:40 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-30T20:18:29Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +0.49%; DEX 24h $1.67B · 1d -36% · vs-7d-ago -55%; slot 318 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -35.51%. (threshold: `|1d %| >= 8`)
- **ALERT · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -55.24%. (threshold: `|7d %| >= 20`)
- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -28.70%. (threshold: `|1d %| >= 8`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 105.82 USD is +38.6% vs 30d median 76.37 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 442,968,127 |
| Block height | 421,015,884 |
| Block time | 2026-08-30T20:18:29Z |
| Epoch | 1,025 (38.92% · slot 168,128/432,000) |
| Mean TPS (last ~3,600s) | 4,287.1 |
| Mean non-vote TPS | 2,160.4 |
| Median TPS (same window) | 4,220.9 |
| Mean slot time | 318.2 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 543,526,706,877 |
| Circulating supply | 585,121,719 SOL |
| Total supply | 633,173,402 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 680 |
| Delinquent | 17 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 437,104,291 SOL |
| Delinquent stake | 23,598.38 SOL (0.005%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.25% / 35.54% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.20M SOL | 3.94% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.09M SOL | 3.68% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.39M SOL | 2.83% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.48M SOL | 2.63% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.45M SOL | 2.16% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.13% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.02M SOL | 2.06% | 10% | 0 |
| 8 | `9eGrDohd…` | 7.30M SOL | 1.67% | 5% | 0 |
| 9 | `EvnRmnMr…` | 7.20M SOL | 1.65% | 7% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.11M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.60M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1715448 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 182006 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 48702 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 288289 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 984373 slots
- `CpdzCVza…` · 315.26 SOL · commission 100% · lag 167776 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 209290 slots
- `HFTcVVrX…` · 152.80 SOL · commission 100% · lag 167670 slots
- `6pEtDovp…` · 131.96 SOL · commission 100% · lag 182054 slots
- `7G4Rfctw…` · 75.85 SOL · commission 100% · lag 206428 slots
- `DZKTNGR3…` · 48.61 SOL · commission 100% · lag 213970 slots
- `As9NxA9b…` · 46.69 SOL · commission 100% · lag 167793 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 225 | data/history.jsonl snapshot tape |
| TVL chart | 225 | data/history.jsonl snapshot tape |
| SOL chart | 224 | data/history.jsonl snapshot tape |
| history.jsonl rows | 225 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$953.12K** (9,080.5 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-28 |
| **Solana REV** | **11,337.8 SOL** / **$1.19M** | MEASURED UTC calendar day 2026-08-28: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-28 · UTC day 2026-08-28 · SOL-USD date 2026-08-28 |
| Jito tip-floor run-rate (NOT REV) | $82.96K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 82959 USD; at p95 floor → 8625031 USD. |
| Protocol fees 24h | $11.21M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9952 |
| p90 / p99 | 0.000011 / 0.000105 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $105.82 | coingecko.simple_price |
| 24h change | +0.49% | coingecko.simple_price |
| Market cap | $61.94B | coingecko.simple_price |
| 24h volume | $2.40B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.96B |
| TVL 1d / 7d / 30d | +1.47% / +7.17% / +23.36% |
| DEX volume 24h | $1.67B · 1d -35.51% · vs-7d-ago -55.24% |
| 7d DEX volume | $19.18B · +9.50% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $11.21M |
| Fees 1d / 7d | -28.70% / -6.77% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $584.75M | +1.47% |
| BisonFi | $149.87M | -54.78% |
| Orca DEX | $144.51M | -57.35% |
| Meteora DLMM | $142.97M | -48.83% |
| pump.fun | $110.08M | -6.41% |
| Axiom | $103.65M | -16.61% |
| Raydium AMM | $99.61M | -42.89% |
| Manifest Trade | $87.78M | -37.89% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.63B | +1.42% | +14.28% |
| Kamino Lend | Lending | $1.27B | +1.12% | +6.17% |
| Raydium AMM | Dexs | $1.15B | +2.43% | +11.18% |
| Jupiter Lend | Lending | $1.10B | +0.80% | +3.98% |
| Binance Staked SOL | Liquid Staking | $1.10B | +1.48% | +13.98% |
| Jito Liquid Staking | Liquid Staking | $1.07B | +1.59% | +12.46% |
| BlackRock BUIDL | RWA | $886.54M | 0.00% | +6.05% |
| Jupiter Perpetual Exchange | Derivatives | $779.81M | +1.14% | +4.68% |
| Jupiter Staked SOL | Liquid Staking | $552.10M | +1.20% | +12.14% |
| Marinade Native | Staking Pool | $437.97M | +2.18% | +30.59% |

## Stablecoins

Solana circulating pegged-USD: **$15.78B**
(1d -0.29% · 7d -0.47%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.86B | -2.73% |
| USDT · Tether | $2.83B | -0.00% |
| USDGO · USDGO | $1.25B | 0.00% |
| USD1 · World Liberty Financial USD | $1.19B | +1.81% |
| BUIDL · BlackRock USD | $886.54M | 0.00% |
| PYUSD · PayPal USD | $692.66M | -0.12% |
| USDG · Global Dollar | $614.15M | -1.42% |
| USDe · Ethena USDe | $536.56M | +0.38% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 70 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 70 · priced-subset mcap $475.53K (lower bound, not a census).
24h volume $9.59M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $437.34M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 70 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.54M
- **xStocks** (RWA) — $437.34M
- **OnRe** (RWA) — $284.80M
- **Ondo Yield Assets** (RWA) — $179.85M
- **Hastra** (RWA) — $157.86M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $24.78M
- **Plume Vaults** (RWA) — $22.86M

## Daily active addresses

741,873 (Allium, as of 2026-08-29). Provider range 419,515–896,918. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: HUGE: @Solana is averaging roughly 2,100 transactions per second, up more than threefold since January.](https://x.com/tokens/status/2094109147839254873) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 17:05:02 GMT
- [RT by @solana: 21 founders. 2 minutes each.

@colosseum Demo Day. August 26, 2026.](https://x.com/solana_devs/status/2094112001517580707) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 17:16:22 GMT
- [Pinned: Solana's first binding onchain governance vote closed, and the network got 25% faster. 

From 300ms slots to fixed-rate credit to a tokenized 1997 manga debut, with Wall Street's largest retail brokerage clearing the path on the other side.

Here’s everything that shipped this week:

📰 Headline News

- @CharlesSchwab announced plans to add SOL to Schwab Crypto Direct

- @Bitwise's Solana Staking ETF surpassed $1B in AUM in 10 months

- @SolanaEvents revealed the first lineup of confirmed speakers for Breakpoint 2026 in London

- Solana validators passed the network Constitution and Double Disinflation, formalizing governance rules and reducing annual issuance

📰 Launches

- @kamino introduced Fixed Rates in private beta, bringing fixed-term, fixed-rate onchain borrowing and lending

- Marvell Technology ($MRVL) went live via @sunrise, issued by @Backpack Securities

- @solflare launched Solflare Perps powered by @PhoenixTrade

- @virtuals_io deployed AI agent tokenization on Solana

- @perena debuted BTC*, a yield-bearing Bitcoin token on Solana powered by Kestrel

- @NolusProtocol went live on Solana with asset-backed leverage, fixed rates, and no margin calls

- @traded_gg unveiled its unified exchange and digital binder for cross-vault collectible trading

- @phygitals tokenized the first manga in history, a graded 1997 magazine featuring Luffy's debut

- @reflectmoney opened pre-deposits for its first tranched credit market built on @maplefinance’s syrupUSDC

- @JupiterExchange added live 5-minute and 15-minute prediction markets for $SPCX

- @solscanofficial integrated network, staking, and DeFi metrics into Solana's data dashboard

- @PayBox integrated @kamino, enabling Claude and ChatGPT users to deploy USDC into yield strategies

- @rips_cards introduced the Private Gacha Machine powered by @Arcium and @Collector_Crypt

- @LaunchOnSF launched collectible-paired memecoins, debuting with solana:SV151D5pjygAKA8aJJcKzm4wFnRX5G92Fye94jQJk7g

- @ImperialPerps opened its collectible Gacha beta, with Perp Packs and borrowing against pulled cards

- @benchdotmarkets launched Hiring Markets to filter applicants using capital stakes and social proof

- @meleemarkets opened public beta for sub-minute permissionless prediction market creation

- @PlayKintara launched its play-to-earn MMO on the @solanamobile dApp Store

- @commonsmade kicked off a three-week hackathon with a $60K prize pool focused on AI waiting UX

- @solana_devs opened applications for the Solana University Ambassador Program

- @mtndao wrapped its month-long residency with 25 teams at Demo Day

- @cstldao opened doors for CastleDAO, a two-week founder residency in Ireland

- @SuperteamMY announced Startup Village Borneo, running September 5-9, 2026

📰 Milestones

- Solana RWA holders surpassed 350K

- @xStocksFi surpassed $500M in AUM across 700+ tokenized assets

- Cumulative Solana ETF inflows reached a record $1.22B, with a $60M single-day high in 2026

- Tokenized commodities supply on Solana crossed a record $50M

- Solana reduced its target slot time to 300ms, a 25% reduction in eight days

- Solana became the leading network by total x402 transaction volume

- @BlockRunAI settled 5.4M agentic payments on Solana over seven days via @PayAINetwork

- @jtx_trade reached a new all-time high daily volume exceeding $20M

- @Dominion_Market’s solana:SiLVFMgD3eD2rgK628NbTBq9MnuJF5FW2CRaVyTB35L on @sunrise logged $4M+ in 24-hour weekend volume

- @solanamobile wrapped Seeker Summer with 100M+ SKR earned and 300K+ badges across 16 apps

- Solana processed 1.32B non-vote transactions in a week, a new ATH

- Solana daily active addresses reached 5M

- Solana memecoins hit $5.2B in weekly spot volume, a 2026 high

If you enjoyed this week’s newsletter, please share it with an RT.

Artwork by @hubie 🔥](https://x.com/solana/status/2094062589743607937) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 14:00:01 GMT
- [RT by @solana: Almost a million traders on @solana yesterday.

On a Saturday.](https://x.com/vibhu/status/2093986629492806111) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 08:58:11 GMT
- [Vibhu on internet capital markets, on CNBC-TV18

"This is the beautiful thing about crypto networks. They are global. They are permissionless."

"As long as you can get money into crypto in the form of a stablecoin, you have access to global capital markets by default. And those markets are really liquid today. You can access borrow lend markets, private credit, treasuries, fixed yield."

"The story of crypto is about making finance truly global and borderless. And Solana is number one there."

@vibhu @CNBC_Awaaz](https://x.com/solana/status/2093987090342031630) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 09:00:01 GMT
- [RT by @solana: Solana 最近又在加速了，从网络速度到韩国传统金融机构入场，再到数千亿美元级别的资产管理能力开始拥抱链上，@Solana 海外生态最新动态尽在 Solar 资讯点👇](https://x.com/Solana_zh/status/2093977018006221266) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 08:19:59 GMT
- [Solana development will never be the same](https://x.com/solana/status/2093829689857220905) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 22:34:34 GMT `upgrade`
- [GM](https://x.com/solana/status/2093792801767240094) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 20:07:59 GMT
- [RT by @anza_xyz: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: HUGE: @Solana is averaging roughly 2,100 transactions per second, up more than threefold since January.](https://x.com/tokens/status/2094109147839254873) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 17:05:02 GMT
- [RT by @solana: 21 founders. 2 minutes each.

@colosseum Demo Day. August 26, 2026.](https://x.com/solana_devs/status/2094112001517580707) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 17:16:22 GMT
- [Pinned: Solana's first binding onchain governance vote closed, and the network got 25% faster. 

From 300ms slots to fixed-rate credit to a tokenized 1997 manga debut, with Wall Street's largest retail brokerage clearing the path on the other side.

Here’s everything that shipped this week:

📰 Headline News

- @CharlesSchwab announced plans to add SOL to Schwab Crypto Direct

- @Bitwise's Solana Staking ETF surpassed $1B in AUM in 10 months

- @SolanaEvents revealed the first lineup of confirmed speakers for Breakpoint 2026 in London

- Solana validators passed the network Constitution and Double Disinflation, formalizing governance rules and reducing annual issuance

📰 Launches

- @kamino introduced Fixed Rates in private beta, bringing fixed-term, fixed-rate onchain borrowing and lending

- Marvell Technology ($MRVL) went live via @sunrise, issued by @Backpack Securities

- @solflare launched Solflare Perps powered by @PhoenixTrade

- @virtuals_io deployed AI agent tokenization on Solana

- @perena debuted BTC*, a yield-bearing Bitcoin token on Solana powered by Kestrel

- @NolusProtocol went live on Solana with asset-backed leverage, fixed rates, and no margin calls

- @traded_gg unveiled its unified exchange and digital binder for cross-vault collectible trading

- @phygitals tokenized the first manga in history, a graded 1997 magazine featuring Luffy's debut

- @reflectmoney opened pre-deposits for its first tranched credit market built on @maplefinance’s syrupUSDC

- @JupiterExchange added live 5-minute and 15-minute prediction markets for $SPCX

- @solscanofficial integrated network, staking, and DeFi metrics into Solana's data dashboard

- @PayBox integrated @kamino, enabling Claude and ChatGPT users to deploy USDC into yield strategies

- @rips_cards introduced the Private Gacha Machine powered by @Arcium and @Collector_Crypt

- @LaunchOnSF launched collectible-paired memecoins, debuting with solana:SV151D5pjygAKA8aJJcKzm4wFnRX5G92Fye94jQJk7g

- @ImperialPerps opened its collectible Gacha beta, with Perp Packs and borrowing against pulled cards

- @benchdotmarkets launched Hiring Markets to filter applicants using capital stakes and social proof

- @meleemarkets opened public beta for sub-minute permissionless prediction market creation

- @PlayKintara launched its play-to-earn MMO on the @solanamobile dApp Store

- @commonsmade kicked off a three-week hackathon with a $60K prize pool focused on AI waiting UX

- @solana_devs opened applications for the Solana University Ambassador Program

- @mtndao wrapped its month-long residency with 25 teams at Demo Day

- @cstldao opened doors for CastleDAO, a two-week founder residency in Ireland

- @SuperteamMY announced Startup Village Borneo, running September 5-9, 2026

📰 Milestones

- Solana RWA holders surpassed 350K

- @xStocksFi surpassed $500M in AUM across 700+ tokenized assets

- Cumulative Solana ETF inflows reached a record $1.22B, with a $60M single-day high in 2026

- Tokenized commodities supply on Solana crossed a record $50M

- Solana reduced its target slot time to 300ms, a 25% reduction in eight days

- Solana became the leading network by total x402 transaction volume

- @BlockRunAI settled 5.4M agentic payments on Solana over seven days via @PayAINetwork

- @jtx_trade reached a new all-time high daily volume exceeding $20M

- @Dominion_Market’s solana:SiLVFMgD3eD2rgK628NbTBq9MnuJF5FW2CRaVyTB35L on @sunrise logged $4M+ in 24-hour weekend volume

- @solanamobile wrapped Seeker Summer with 100M+ SKR earned and 300K+ badges across 16 apps

- Solana processed 1.32B non-vote transactions in a week, a new ATH

- Solana daily active addresses reached 5M

- Solana memecoins hit $5.2B in weekly spot volume, a 2026 high

If you enjoyed this week’s newsletter, please share it with an RT.

Artwork by @hubie 🔥](https://x.com/solana/status/2094062589743607937) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 14:00:01 GMT
- [RT by @solana: Almost a million traders on @solana yesterday.

On a Saturday.](https://x.com/vibhu/status/2093986629492806111) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 08:58:11 GMT
- [Vibhu on internet capital markets, on CNBC-TV18

"This is the beautiful thing about crypto networks. They are global. They are permissionless."

"As long as you can get money into crypto in the form of a stablecoin, you have access to global capital markets by default. And those markets are really liquid today. You can access borrow lend markets, private credit, treasuries, fixed yield."

"The story of crypto is about making finance truly global and borderless. And Solana is number one there."

@vibhu @CNBC_Awaaz](https://x.com/solana/status/2093987090342031630) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 09:00:01 GMT
- [RT by @solana: Solana 最近又在加速了，从网络速度到韩国传统金融机构入场，再到数千亿美元级别的资产管理能力开始拥抱链上，@Solana 海外生态最新动态尽在 Solar 资讯点👇](https://x.com/Solana_zh/status/2093977018006221266) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 08:19:59 GMT
- [Solana development will never be the same](https://x.com/solana/status/2093829689857220905) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 22:34:34 GMT `upgrade`
- [GM](https://x.com/solana/status/2093792801767240094) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 20:07:59 GMT
- [RT by @anza_xyz: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-30 (2026-08-30 13:18:40 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~318 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~318 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 224ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 134ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 183ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 181ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 179ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6037ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 350ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 157ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 193ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 219ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 87ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 82ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1115ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 253ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 129ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 119ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 140ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 549ms https://solana.com/data
- `solana.com.databricks` [ok] 200 184ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 515ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 188ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 315ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 195ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 352ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 819ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 298ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 304ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 317ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 461ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2409ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1835ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 2133ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 127ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 180ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 131ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 652ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 972ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 1037ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 806ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 765ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 899ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 824ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 594ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 639ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 740ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 791ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 792ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 845ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 810ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1830ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1724ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2112ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1915ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 3742ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1350ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1613ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [FAIL]  12052ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AAPLx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AMZNx` [FAIL]  12051ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.NVDAx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GOOGLx` [FAIL]  12053ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SPYx` [FAIL]  12056ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METAx` [FAIL]  12056ms https://api.backed.fi/api/v2/public/assets/METAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MSFTx` [FAIL]  12062ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AAPLx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.METAx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 506ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 562ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 441ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 713ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.BANKCx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.price.SUOPTx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 797ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 1213ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 561ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 597ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.TNGYIx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 765ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.price.CTINSx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.KUNLx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.WRFHDx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.MMGx` [ok] 200 1614ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.KUNLx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 415ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.LAOPGx` [ok] 200 977ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.SZIGHx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 495ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.WRFHDx` [ok] 200 946ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.SNBIOx` [ok] 200 594ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.ENNHLx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 939ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 1665ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.SZIGHx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 739ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 2313ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.price.CRESBx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.price.CMERPx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.CRESBx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 712ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 1034ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.CSPCx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.CMERPx` [ok] 200 837ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.ENNHLx` [ok] 200 1785ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 385ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 749ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 729ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.CMENDx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 631ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.mult.WXXDCx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.MIXUx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 1030ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.ASMPTx` [ok] 200 457ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.SITCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.JDHLTx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.circ.BDWAPx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 239ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 655ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 1252ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.price.SINOTx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.PRADx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.SNDSCx` [ok] 200 1096ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.circ.SINOTx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 682ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 729ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 340ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.SINOTx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.CTFJWx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.WHGROx` [ok] 200 497ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.mult.CLONPx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 526ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 535ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.WHGROx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 755ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.PWAHLx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.GENTEx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.CLPHDx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.SINOx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.GENTEx` [ok] 200 533ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 757ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.price.WUXIBx` [ok] 200 463ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.CKAHx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.CRAUTx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 292ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 1313ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.WUXIBx` [ok] 200 797ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 1574ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 1266ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 580ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.HKEXCx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.SWPRPx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.KUAIx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.price.NONGx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.CKINFx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.SWPRPx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.NONGx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 1133ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.circ.CHONGx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.price.MTRCPx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.QQQx` [FAIL]  12059ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MEITx` [ok] 200 530ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.COINx` [FAIL]  12055ms https://api.backed.fi/api/v2/public/assets/COINx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.CHONGx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.COINx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.MEITx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.COVELx` [ok] 200 1447ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.MTRCPx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.price.POPMTx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.circ.COVELx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.POPMTx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.price.BOCOMx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.price.HNDLDx` [ok] 200 1115ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.price.CKHUTx` [ok] 200 503ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.COVELx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.CPETCx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.price.COSCx` [ok] 200 870ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.BOCOMx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.mult.POPMTx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.price.GEELx` [ok] 200 1792ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.BOCHKx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.circ.COSCx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.BOCOMx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.price.CITICx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.circ.HNDLDx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.BOCHKx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.price.ANTASx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.mult.HNDLDx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.BOCHKx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.circ.CITICx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 510ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.CRESLx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.price.HAIERx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.price.ZJGLDx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.mult.GEELx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.circ.CRESLx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.circ.HAIERx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.circ.ZJGLDx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.mult.CRESLx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.mult.HAIERx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.circ.CPETCx` [ok] 200 1178ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.price.PSBOCx` [ok] 200 484ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.circ.ANTASx` [ok] 200 855ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.mult.ZJGLDx` [ok] 200 353ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.price.ICBCx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.mult.CKHUTx` [ok] 200 1330ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.CPETCx` [ok] 200 381ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.mult.ANTASx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.circ.ICBCx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.mult.CITICx` [ok] 200 1222ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.mult.ICBCx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `xstocks.circ.PSBOCx` [ok] 200 869ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.mult.PSBOCx` [ok] 200 793ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1541ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 275ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 153ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 139ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 143ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 139ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 153ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 145ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 151ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.SINOTx` [ok] 200 159ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 324ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 303ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 139ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 140ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 141ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 139ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 146ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 352ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
