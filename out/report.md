# Borealis — Solana ecosystem report

**Generated** 2026-08-31T09:33:37Z · 2026-08-31 02:33:37 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-08-31T09:33:27Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -1.44%; DEX 24h $1.87B · 1d +12% · vs-7d-ago -36%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -36.38%. (threshold: `|7d %| >= 20`)
- **WARN · SOL price vs 30d median (solana.com/data)** — Current 103.17 USD is +35.1% vs 30d median 76.37 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is +11.91%. (threshold: `|1d %| >= 8`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,118,232 |
| Block height | 421,165,907 |
| Block time | 2026-08-31T09:33:27Z |
| Epoch | 1,025 (73.67% · slot 318,233/432,000) |
| Mean TPS (last ~3,600s) | 3,534.5 |
| Mean non-vote TPS | 1,403.0 |
| Median TPS (same window) | 3,519.3 |
| Mean slot time | 316.6 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 543,719,531,659 |
| Circulating supply | 585,121,214 SOL |
| Total supply | 633,172,897 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 679 |
| Delinquent | 18 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 437,082,504 SOL |
| Delinquent stake | 45,385.49 SOL (0.010%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.26% / 35.54% |
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

- `mrgn4atx…` · 21.79K SOL · commission 0% · lag 136449 slots
- `gangtCrQ…` · 15.32K SOL · commission 0% · lag 1865553 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 332111 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 198807 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 438394 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1134478 slots
- `CpdzCVza…` · 315.26 SOL · commission 100% · lag 317881 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 359395 slots
- `HFTcVVrX…` · 152.80 SOL · commission 100% · lag 317775 slots
- `6pEtDovp…` · 131.96 SOL · commission 100% · lag 332159 slots
- `7G4Rfctw…` · 75.85 SOL · commission 100% · lag 356533 slots
- `DZKTNGR3…` · 48.61 SOL · commission 100% · lag 364075 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 278 | data/history.jsonl snapshot tape |
| TVL chart | 278 | data/history.jsonl snapshot tape |
| SOL chart | 277 | data/history.jsonl snapshot tape |
| history.jsonl rows | 278 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$814.10K** (7,855.5 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-29 |
| **Solana REV** | **9,341.6 SOL** / **$968.12K** | MEASURED UTC calendar day 2026-08-29: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-29 · UTC day 2026-08-29 · SOL-USD date 2026-08-29 |
| Jito tip-floor run-rate (NOT REV) | $28.70K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 28703 USD; at p95 floor → 967425 USD. |
| Protocol fees 24h | $12.01M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9983 |
| p90 / p99 | 0.000010 / 0.000111 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $103.17 | coingecko.simple_price |
| 24h change | -1.44% | coingecko.simple_price |
| Market cap | $60.37B | coingecko.simple_price |
| 24h volume | $3.68B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.79B |
| TVL 1d / 7d / 30d | -1.97% / +4.19% / +21.96% |
| DEX volume 24h | $1.87B · 1d +11.91% · vs-7d-ago -36.38% |
| 7d DEX volume | $17.96B · -7.42% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $12.01M |
| Fees 1d / 7d | +7.12% / -5.28% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $732.11M | +25.20% |
| Orca DEX | $247.90M | +70.57% |
| BisonFi | $184.51M | +23.11% |
| Meteora DLMM | $142.67M | -0.21% |
| Manifest Trade | $121.29M | +39.86% |
| Raydium AMM | $116.01M | -4.99% |
| Axiom | $103.65M | 0.00% |
| pump.fun | $91.65M | -16.74% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.57B | -2.12% | +11.57% |
| Kamino Lend | Lending | $1.24B | -0.97% | +4.51% |
| Raydium AMM | Dexs | $1.10B | -3.30% | +4.42% |
| Jupiter Lend | Lending | $1.08B | -1.52% | +2.59% |
| Binance Staked SOL | Liquid Staking | $1.06B | -1.96% | +10.16% |
| Jito Liquid Staking | Liquid Staking | $1.03B | -2.27% | +8.42% |
| BlackRock BUIDL | RWA | $886.54M | 0.00% | +6.05% |
| Jupiter Perpetual Exchange | Derivatives | $760.17M | -1.44% | +2.97% |
| Jupiter Staked SOL | Liquid Staking | $531.10M | -2.17% | +8.17% |
| xStocks | RWA | $432.20M | +1.15% | +3.37% |

## Stablecoins

Solana circulating pegged-USD: **$15.79B**
(1d -1.07% · 7d -2.03%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.87B | -1.89% |
| USDT · Tether | $2.84B | -0.00% |
| USDGO · USDGO | $1.24B | -0.40% |
| USD1 · World Liberty Financial USD | $1.21B | +2.55% |
| BUIDL · BlackRock USD | $886.54M | 0.00% |
| PYUSD · PayPal USD | $693.60M | -0.13% |
| USDG · Global Dollar | $609.36M | -0.84% |
| USDe · Ethena USDe | $537.41M | +0.55% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 80 of 715 Solana-deployed listed symbols (multiplier ok 80/80; 715 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 715 · Solana deployments 715 · priced 80 · priced-subset mcap $285.14M (lower bound, not a census).
24h volume $12.89M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $432.20M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 80 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 715 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 715 unique underlyings among 715 Solana rows; not every tokenized equity on Solana). 715 of 715 listed xStocks have a Solana deployment (715 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $886.54M
- **xStocks** (RWA) — $432.20M
- **OnRe** (RWA) — $284.91M
- **Ondo Yield Assets** (RWA) — $180.00M
- **Hastra** (RWA) — $154.87M
- **Theo Network thBill** (RWA) — $26.40M
- **Ondo Global Markets** (RWA) — $24.75M
- **Plume Vaults** (RWA) — $22.86M

## Daily active addresses

741,873 (Allium, as of 2026-08-29). Provider range 419,515–768,976. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: New Solana jobs just dropped on the Superteam Talent Portal

Check out the job board below!](https://x.com/SuperteamTalent/status/2094347126755205387) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 08:50:40 GMT
- [RT by @solana: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT
- [Pinned:](https://x.com/solana/status/2094258208844255589) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 02:57:21 GMT
- [RT by @solana: BREAKPOINT](https://x.com/platis_e/status/2094171000266977774) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 21:10:48 GMT
- [RT by @solana: 🔥 Solaris AI Copilot is now open & free for everyone.

No more LLM keys.

Tell Copilot what you want to automate on @solana in plain language.

It builds, validates, and dry-runs the workflow against live data before you execute.

16 integrations are live across swaps, perps, onchain + market data, indicators, memecoins, smart money, RWAs, stocks, alerts, privacy, x402 and more.

Built in:
• Multi-run automations
• Duplicate-trade protection
• Failure recovery
• Execution proofs
• Pre-execution safety checks

Next: turning workflows into standalone apps.](https://x.com/SolarisAI_fun/status/2094111080423579977) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 17:12:42 GMT
- [RT by @solana: HUGE: @Solana is averaging roughly 2,100 transactions per second, up more than threefold since January.](https://x.com/tokens/status/2094109147839254873) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 17:05:02 GMT
- [RT by @solana: 21 founders. 2 minutes each.

@colosseum Demo Day. August 26, 2026.](https://x.com/solana_devs/status/2094112001517580707) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 17:16:22 GMT
- [Solana's first binding onchain governance vote closed, and the network got 25% faster. 

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

- [RT by @solana: New Solana jobs just dropped on the Superteam Talent Portal

Check out the job board below!](https://x.com/SuperteamTalent/status/2094347126755205387) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 08:50:40 GMT
- [RT by @solana: we love larger txs
we love higher TPS
we love lower slot times
we love lower rent
we love shorter finality
we love more expressivity
we love @solana 
we love @anza_xyz](https://x.com/bw_solana/status/2094145668294332669) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 19:30:09 GMT
- [Pinned:](https://x.com/solana/status/2094258208844255589) — X/Nitter-style RSS @solana (not Twitter API) · Mon, 31 Aug 2026 02:57:21 GMT
- [RT by @solana: BREAKPOINT](https://x.com/platis_e/status/2094171000266977774) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 21:10:48 GMT
- [RT by @solana: 🔥 Solaris AI Copilot is now open & free for everyone.

No more LLM keys.

Tell Copilot what you want to automate on @solana in plain language.

It builds, validates, and dry-runs the workflow against live data before you execute.

16 integrations are live across swaps, perps, onchain + market data, indicators, memecoins, smart money, RWAs, stocks, alerts, privacy, x402 and more.

Built in:
• Multi-run automations
• Duplicate-trade protection
• Failure recovery
• Execution proofs
• Pre-execution safety checks

Next: turning workflows into standalone apps.](https://x.com/SolarisAI_fun/status/2094111080423579977) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 17:12:42 GMT
- [RT by @solana: HUGE: @Solana is averaging roughly 2,100 transactions per second, up more than threefold since January.](https://x.com/tokens/status/2094109147839254873) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 17:05:02 GMT
- [RT by @solana: 21 founders. 2 minutes each.

@colosseum Demo Day. August 26, 2026.](https://x.com/solana_devs/status/2094112001517580707) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 30 Aug 2026 17:16:22 GMT
- [Solana's first binding onchain governance vote closed, and the network got 25% faster. 

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

_As of 2026-08-31 (2026-08-31 02:33:37 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~317 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~317 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 199ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 194ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 128ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 281ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 162ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 7116ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 308ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 86ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 134ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 93ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 69ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 81ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 7995ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 174ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 106ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 111ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 124ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 430ms https://solana.com/data
- `solana.com.databricks` [ok] 200 231ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 532ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 143ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 121ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 150ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 187ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 848ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 243ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 246ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 247ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1740ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2149ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1282ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 2069ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 263ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 188ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 186ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 609ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 630ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 634ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 732ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 823ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 711ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 598ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 743ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 690ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 668ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 586ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 694ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 912ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 635ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1545ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1204ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 878ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 854ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1005ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1709ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 995ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.MSFTx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.GOOGLx` [ok] 200 393ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.TSLAx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.price.AAPLx` [ok] 200 407ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.SPYx` [ok] 200 439ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.TSLAx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 633ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.circ.METAx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.MSFTx` [ok] 200 670ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.circ.SPYx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.price.NVDAx` [ok] 200 1019ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.mult.SPYx` [ok] 200 253ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.price.BANKCx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.price.SUOPTx` [ok] 200 203ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.circ.NVDAx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.MSFTx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.price.AMZNx` [ok] 200 1263ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.COINx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.BANKCx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 197ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.TNGYIx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.mult.BANKCx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.COINx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.QQQx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 271ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.SUOPTx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.LAOPGx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.COINx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.mult.MMGx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.AMZNx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 202ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.JDLOGx` [ok] 200 349ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.mult.QQQx` [ok] 200 419ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.CTINSx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.ZHAOMx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 465ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 427ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.LAOPGx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.circ.HAIDLx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 585ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 306ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 625ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 759ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.SMOIHx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.SZIGHx` [ok] 200 780ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 188ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.SMOIHx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 418ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 1251ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 1143ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.CMERPx` [ok] 200 600ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 602ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.CSPCx` [ok] 200 589ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.CMENDx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.CMERPx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.circ.CSPCx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.CMENDx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 688ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.mult.CMENDx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.SITCx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.MIXUx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.JDHLTx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.WHRFRx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.MIXUx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.JDHLTx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 1028ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.SNDSCx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.circ.SITCx` [ok] 200 692ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 549ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 1148ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.circ.WHRFRx` [ok] 200 945ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 2324ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.WHRFRx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.circ.BDWAPx` [ok] 200 1111ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.mult.BDWAPx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 339ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 216ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 810ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 2224ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.CRESPx` [ok] 200 1142ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.PRADx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.CLONPx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.SITCx` [ok] 200 1421ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.CTFJWx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 179ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.SNDSCx` [ok] 200 1324ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 344ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.SINOTx` [ok] 200 693ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.price.SINOx` [ok] 200 451ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.WHGROx` [ok] 200 169ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.SINOTx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.mult.CTFJWx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 1002ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.PWAHLx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.CLPHDx` [ok] 200 199ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.GENTEx` [ok] 200 206ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.WUXIBx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.circ.GENTEx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.PWAHLx` [ok] 200 318ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 175ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 875ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.SWPRPx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 509ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.mult.GENTEx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.CRAUTx` [ok] 200 815ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.SINOx` [ok] 200 1077ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 449ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.price.KUAIx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.price.HKEXCx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.price.CKINFx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.KUAIx` [ok] 200 170ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.circ.HKEXCx` [ok] 200 217ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.HKCGAx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 364ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.COVELx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.HKCGAx` [ok] 200 269ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.HKEXCx` [ok] 200 575ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 2615ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.MEITx` [ok] 200 331ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.COVELx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.price.GEELx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.mult.CHONGx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.circ.GEELx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 2155ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.GEELx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.price.NONGx` [ok] 200 1482ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 597ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.circ.PICCx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 2529ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 492ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.price.HNDLDx` [ok] 200 1211ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.price.CKHUTx` [ok] 200 633ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.mult.COVELx` [ok] 200 1718ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 1551ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.circ.HNDLDx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.circ.CKHUTx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.COSCx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.circ.MTRCPx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.price.BOCOMx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/BOCOMx/price-data
- `xstocks.mult.MTRCPx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 2123ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.price.POPMTx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.price.CPETCx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/CPETCx/price-data
- `xstocks.price.BOCHKx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/BOCHKx/price-data
- `xstocks.mult.MEITx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.circ.POPMTx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 1488ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 1926ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.mult.HNDLDx` [ok] 200 666ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.POPMTx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.circ.BOCHKx` [ok] 200 186ms https://api.backed.fi/api/v2/public/assets/BOCHKx/circulating-supply?format=object
- `xstocks.price.ANTASx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/ANTASx/price-data
- `xstocks.mult.NONGx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.CPETCx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/CPETCx/circulating-supply?format=object
- `xstocks.price.ZJGLDx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/price-data
- `xstocks.price.CRESLx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/CRESLx/price-data
- `xstocks.price.HAIERx` [ok] 200 345ms https://api.backed.fi/api/v2/public/assets/HAIERx/price-data
- `xstocks.price.CITICx` [ok] 200 617ms https://api.backed.fi/api/v2/public/assets/CITICx/price-data
- `xstocks.circ.ZJGLDx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/circulating-supply?format=object
- `xstocks.mult.BOCHKx` [ok] 200 592ms https://api.backed.fi/api/v2/public/assets/BOCHKx/multiplier?network=Solana
- `xstocks.circ.CRESLx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/CRESLx/circulating-supply?format=object
- `xstocks.mult.CPETCx` [ok] 200 532ms https://api.backed.fi/api/v2/public/assets/CPETCx/multiplier?network=Solana
- `xstocks.mult.CRESLx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/CRESLx/multiplier?network=Solana
- `xstocks.circ.CITICx` [ok] 200 379ms https://api.backed.fi/api/v2/public/assets/CITICx/circulating-supply?format=object
- `xstocks.circ.HAIERx` [ok] 200 519ms https://api.backed.fi/api/v2/public/assets/HAIERx/circulating-supply?format=object
- `xstocks.circ.BOCOMx` [ok] 200 1358ms https://api.backed.fi/api/v2/public/assets/BOCOMx/circulating-supply?format=object
- `xstocks.mult.ZJGLDx` [ok] 200 489ms https://api.backed.fi/api/v2/public/assets/ZJGLDx/multiplier?network=Solana
- `xstocks.mult.HAIERx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/HAIERx/multiplier?network=Solana
- `xstocks.price.ICBCx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/ICBCx/price-data
- `xstocks.mult.BOCOMx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/BOCOMx/multiplier?network=Solana
- `xstocks.price.PSBOCx` [ok] 200 592ms https://api.backed.fi/api/v2/public/assets/PSBOCx/price-data
- `xstocks.circ.ICBCx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/ICBCx/circulating-supply?format=object
- `xstocks.circ.ANTASx` [ok] 200 1449ms https://api.backed.fi/api/v2/public/assets/ANTASx/circulating-supply?format=object
- `xstocks.mult.ICBCx` [ok] 200 205ms https://api.backed.fi/api/v2/public/assets/ICBCx/multiplier?network=Solana
- `xstocks.circ.PSBOCx` [ok] 200 445ms https://api.backed.fi/api/v2/public/assets/PSBOCx/circulating-supply?format=object
- `xstocks.mult.CITICx` [ok] 200 885ms https://api.backed.fi/api/v2/public/assets/CITICx/multiplier?network=Solana
- `xstocks.mult.PSBOCx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/PSBOCx/multiplier?network=Solana
- `xstocks.mult.ANTASx` [ok] 200 1104ms https://api.backed.fi/api/v2/public/assets/ANTASx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1298ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 309ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 79ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.MEITx` [ok] 200 111ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.HKEXCx` [ok] 200 108ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 80ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.KUAIx` [ok] 200 104ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.BANKCx` [ok] 200 105ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.CPETCx` [ok] 200 122ms https://lite-api.jup.ag/tokens/v2/search?query=CPETCx
- `jup.tokens.search.KUNLx` [ok] 200 89ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jito.tip_floor` [ok] 200 121ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 289ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 129ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 142ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 120ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 121ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 115ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 150ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
