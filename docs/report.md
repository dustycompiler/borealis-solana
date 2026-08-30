# Borealis — Solana ecosystem report

**Generated** 2026-08-30T18:03:40Z · 2026-08-30 11:03:40 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-30T18:03:29Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h +1.37%; DEX 24h $1.67B · 1d -36% · vs-7d-ago -55%; slot 318 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -35.51%. (threshold: `|1d %| >= 8`)
- **ALERT · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -55.24%. (threshold: `|7d %| >= 20`)
- **ALERT · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -28.70%. (threshold: `|1d %| >= 8`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 106.41 USD is +39.3% vs 30d median 76.37 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 442,942,630 |
| Block height | 420,990,400 |
| Block time | 2026-08-30T18:03:29Z |
| Epoch | 1,025 (33.02% · slot 142,631/432,000) |
| Mean TPS (last ~3,600s) | 4,192.2 |
| Mean non-vote TPS | 2,068.2 |
| Median TPS (same window) | 4,202.9 |
| Mean slot time | 318.0 ms |
| Median slot time | 317.5 ms |
| Transaction count (cluster) | 543,491,891,033 |
| Circulating supply | 585,121,810 SOL |
| Total supply | 633,173,493 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 678 |
| Delinquent | 19 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 436,966,070 SOL |
| Delinquent stake | 161,820.05 SOL (0.037%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.26% / 35.55% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.20M SOL | 3.94% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.09M SOL | 3.68% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.39M SOL | 2.84% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.48M SOL | 2.63% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.45M SOL | 2.16% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.13% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.02M SOL | 2.07% | 10% | 0 |
| 8 | `9eGrDohd…` | 7.30M SOL | 1.67% | 5% | 0 |
| 9 | `EvnRmnMr…` | 7.20M SOL | 1.65% | 7% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.51% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.11M SOL | 1.40% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.60M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.82M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `nymsGg7Z…` · 116.43K SOL · commission 0% · lag 23029 slots
- `mrgn4atx…` · 21.79K SOL · commission 0% · lag 138893 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1689951 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 156509 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 23205 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 262792 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 958876 slots
- `CpdzCVza…` · 315.26 SOL · commission 100% · lag 142279 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 183793 slots
- `HFTcVVrX…` · 152.80 SOL · commission 100% · lag 142173 slots
- `6pEtDovp…` · 131.96 SOL · commission 100% · lag 156557 slots
- `7G4Rfctw…` · 75.85 SOL · commission 100% · lag 180931 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 216 | data/history.jsonl snapshot tape |
| TVL chart | 216 | data/history.jsonl snapshot tape |
| SOL chart | 215 | data/history.jsonl snapshot tape |
| history.jsonl rows | 216 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$953.12K** (9,080.5 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-28 |
| **Solana REV** | **11,337.8 SOL** / **$1.19M** | MEASURED UTC calendar day 2026-08-28: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-28 · UTC day 2026-08-28 · SOL-USD date 2026-08-28 |
| Jito tip-floor run-rate (NOT REV) | $67.32K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 67321 USD; at p95 floor → 1901444 USD. |
| Protocol fees 24h | $11.21M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9941 |
| p90 / p99 | 0.000012 / 0.000182 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $106.41 | coingecko.simple_price |
| 24h change | +1.37% | coingecko.simple_price |
| Market cap | $62.27B | coingecko.simple_price |
| 24h volume | $2.44B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.95B |
| TVL 1d / 7d / 30d | +1.46% / +7.16% / +23.35% |
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
| Raydium AMM | $96.58M | -44.63% |
| Manifest Trade | $86.32M | -38.93% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.62B | +1.33% | +14.69% |
| Kamino Lend | Lending | $1.27B | +1.08% | +6.41% |
| Raydium AMM | Dexs | $1.15B | +2.43% | +11.18% |
| Jupiter Lend | Lending | $1.10B | +0.34% | +3.60% |
| Binance Staked SOL | Liquid Staking | $1.10B | +1.48% | +13.58% |
| Jito Liquid Staking | Liquid Staking | $1.07B | +1.46% | +12.75% |
| BlackRock BUIDL | RWA | $886.54M | 0.00% | +6.05% |
| Jupiter Perpetual Exchange | Derivatives | $779.58M | +1.13% | +4.51% |
| Jupiter Staked SOL | Liquid Staking | $550.87M | +1.04% | +13.40% |
| xStocks | RWA | $436.76M | +0.86% | +3.85% |

## Stablecoins

Solana circulating pegged-USD: **$15.80B**
(1d -0.30% · 7d -0.47%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.88B | -2.35% |
| USDT · Tether | $2.83B | -0.00% |
| USDGO · USDGO | $1.25B | 0.00% |
| USD1 · World Liberty Financial USD | $1.19B | +1.81% |
| BUIDL · BlackRock USD | $886.54M | 0.00% |
| PYUSD · PayPal USD | $692.47M | -0.15% |
| USDG · Global Dollar | $614.64M | -1.32% |
| USDe · Ethena USDe | $536.58M | +0.38% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 80 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 80 · priced-subset mcap $285.10M (lower bound, not a census).
24h volume $9.21M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $436.76M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 80 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.08B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.54M
- **xStocks** (RWA) — $436.76M
- **OnRe** (RWA) — $284.71M
- **Ondo Yield Assets** (RWA) — $179.84M
- **Hastra** (RWA) — $157.85M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $24.77M
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
- [x.com/i/broadcasts/1kKzDPlap…](https://x.com/solana/status/2093875265894273410) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 01:35:40 GMT
- [Solana development will never be the same](https://x.com/solana/status/2093829689857220905) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 22:34:34 GMT `upgrade`
- [GM](https://x.com/solana/status/2093792801767240094) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 20:07:59 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`
- [7/
Solana's first stake-weighted vote drew participation from hundreds of millions of SOL on each proposal, well above the one-third quorum.

Proposals: https://governance.solana.com

SIMD-0550: https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0550-double-disinflation.md

SIMD-0607: https://github.com/solana-foundation/solana-improvement-documents/pull/607](https://x.com/anza_xyz/status/2093445419502272913) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:37 GMT `upgrade`

### X / announcements (public Nitter-style RSS, not Twitter API)

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
- [x.com/i/broadcasts/1kKzDPlap…](https://x.com/solana/status/2093875265894273410) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 01:35:40 GMT
- [Solana development will never be the same](https://x.com/solana/status/2093829689857220905) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 22:34:34 GMT `upgrade`
- [GM](https://x.com/solana/status/2093792801767240094) — X/Nitter-style RSS @solana (not Twitter API) · Sat, 29 Aug 2026 20:07:59 GMT
- [RT by @anza_xyz: Solana development will never be the same](https://x.com/bw_solana/status/2093754130573701227) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 29 Aug 2026 17:34:19 GMT `upgrade`
- [7/
Solana's first stake-weighted vote drew participation from hundreds of millions of SOL on each proposal, well above the one-third quorum.

Proposals: https://governance.solana.com

SIMD-0550: https://github.com/solana-foundation/solana-improvement-documents/blob/main/proposals/0550-double-disinflation.md

SIMD-0607: https://github.com/solana-foundation/solana-improvement-documents/pull/607](https://x.com/anza_xyz/status/2093445419502272913) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 28 Aug 2026 21:07:37 GMT `upgrade`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-08-30 (2026-08-30 11:03:40 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- `rpc.getHealth` [ok] 200 258ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 178ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 198ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 138ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 173ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6207ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 412ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 218ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 114ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 163ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 74ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 905ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 767ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 250ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 155ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 110ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 1094ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 914ms https://solana.com/data
- `solana.com.databricks` [ok] 200 243ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 511ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 234ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 192ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 155ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 300ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 1014ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 296ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 304ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 305ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 3040ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 6058ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 2581ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 2073ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 257ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 188ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 181ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 906ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 869ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 569ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 788ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 846ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 780ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 894ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 868ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 778ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 806ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 731ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 820ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 751ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 584ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1849ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2895ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1757ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1632ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 2093ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1431ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1737ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 1282ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.TSLAx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.SPYx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.NVDAx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.price.METAx` [ok] 200 316ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.TSLAx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.GOOGLx` [ok] 200 547ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.MSFTx` [ok] 200 728ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.AAPLx` [ok] 200 743ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.circ.METAx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.AMZNx` [ok] 200 1017ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 473ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 787ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 595ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 447ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 532ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.price.QQQx` [ok] 200 560ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.MSFTx` [ok] 200 806ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.METAx` [ok] 200 786ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.AAPLx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 454ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.LAOPGx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.BANKCx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.QQQx` [ok] 200 598ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.QQQx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 479ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.TNGYIx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.MMGx` [ok] 200 1144ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.price.KUNLx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.price.JDLOGx` [ok] 200 874ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 544ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.CTINSx` [ok] 200 673ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.price.HAIDLx` [ok] 200 690ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.KUNLx` [ok] 200 508ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.MMGx` [ok] 200 386ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 675ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 667ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.KUNLx` [ok] 200 738ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.mult.ENNHLx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.SNBIOx` [ok] 200 454ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 1029ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 1314ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.CRESBx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 700ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.circ.CRESBx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 249ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 270ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.CSPCx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.CMERPx` [ok] 200 758ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 659ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 745ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.price.MIXUx` [ok] 200 382ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.mult.WXXDCx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.HRZRBx` [ok] 200 1097ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.CRESMx` [ok] 200 733ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.JTGEXx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 969ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.mult.CRESMx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 521ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.WHRFRx` [ok] 200 592ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.price.SNDSCx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.circ.MIXUx` [ok] 200 913ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 1367ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.JDHLTx` [ok] 200 627ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.mult.ASMPTx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 277ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 556ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.price.CRESPx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 551ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 426ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.CRESPx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.price.SINOTx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.SITCx` [ok] 200 275ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.CLONPx` [ok] 200 235ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.PRADx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 590ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 723ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 651ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.circ.WHGROx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.mult.CTFJWx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 279ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.GENTEx` [ok] 200 359ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.mult.WHGROx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.CTPCAx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 467ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.CRAUTx` [ok] 200 363ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.mult.CLONPx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.circ.GENTEx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.GENTEx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.SINOx` [ok] 200 1281ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.CLPHDx` [ok] 200 1235ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.HKCGAx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.WUXIBx` [ok] 200 443ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.KUAIx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.price.CKAHx` [ok] 200 747ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.SINOx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.CLPHDx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.HKEXCx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.mult.SINOx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 243ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 1059ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.KUAIx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.price.NONGx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.mult.CKAHx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 808ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.HNDLDx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.price.MTRCPx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 1285ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 868ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.circ.HNDLDx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.MTRCPx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.CHONGx` [ok] 200 977ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.COVELx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.GEELx` [ok] 200 512ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.circ.CHONGx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 450ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.price.PICCx` [ok] 200 255ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.price.MEITx` [ok] 200 1290ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.price.CKHUTx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.price.COSCx` [ok] 200 421ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.price.POPMTx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.mult.COVELx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.circ.POPMTx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 1754ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.CHONGx` [ok] 200 818ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.BOCOMx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.mult.MEITx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.NONGx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.mult.POPMTx` [ok] 200 334ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.price.CPETCx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.circ.CKHUTx` [ok] 200 703ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.price.BOCHKx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.price.CITICx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.circ.PICCx` [ok] 200 997ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.price.ANTASx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.circ.BOCHKx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.circ.BOCOMx` [ok] 200 470ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.circ.CPETCx` [ok] 200 274ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.circ.CITICx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.circ.ANTASx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.price.CRESLx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.mult.BOCOMx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.mult.CPETCx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.price.HAIERx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.circ.CRESLx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.price.ZJGLDx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.mult.ANTASx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 1156ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.circ.HAIERx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.mult.CRESLx` [ok] 200 242ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.circ.ZJGLDx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.price.PSBOCx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.mult.ZJGLDx` [ok] 200 236ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.mult.CITICx` [ok] 200 838ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.circ.PSBOCx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.price.ICBCx` [ok] 200 507ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.mult.BOCHKx` [ok] 200 986ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.mult.HAIERx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.mult.PSBOCx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `xstocks.circ.ICBCx` [ok] 200 1061ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.mult.ICBCx` [ok] 200 478ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 996ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 505ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 143ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 141ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 139ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 141ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 145ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 149ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.KUNLx` [ok] 200 140ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jup.tokens.search.SINOTx` [ok] 200 149ms https://lite-api.jup.ag/tokens/v2/search?query=SINOTx
- `jito.tip_floor` [ok] 200 289ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 321ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 125ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 201ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 186ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 184ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 169ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 261ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
