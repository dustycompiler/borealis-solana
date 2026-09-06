# Borealis — Solana ecosystem report

**Generated** 2026-09-06T19:48:55Z · 2026-09-06 12:48:55 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-06T19:48:44Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +1.90%; DEX 24h $1.96B · 1d +4% · vs-7d-ago +17%; slot 316 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

No flags vs rolling baseline (60 samples / llama 7d). Watching.

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 444,876,055 |
| Block height | 422,920,376 |
| Block time | 2026-09-06T19:48:44Z |
| Epoch | 1,029 (80.57% · slot 348,055/432,000) |
| Mean TPS (last ~3,600s) | 3,823.1 |
| Mean non-vote TPS | 1,695.6 |
| Median TPS (same window) | 3,832.8 |
| Mean slot time | 316.0 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 545,781,283,711 |
| Circulating supply | 585,444,889 SOL |
| Total supply | 633,548,765 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 17 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,169,820 SOL |
| Delinquent stake | 78,999.56 SOL (0.018%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.27% / 35.53% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.42M SOL | 3.97% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.32M SOL | 3.72% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.51M SOL | 2.85% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.37M SOL | 2.59% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.56M SOL | 2.18% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.27M SOL | 2.11% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.04M SOL | 2.06% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.35M SOL | 1.67% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.13M SOL | 1.62% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.59M SOL | 1.50% | 0% | 0 |
| 11 | `9jxgosAf…` | 6.12M SOL | 1.39% | 100% | 0 |
| 12 | `JD549Hsb…` | 6.12M SOL | 1.39% | 0% | 0 |
| 13 | `5pPRHnie…` | 5.96M SOL | 1.36% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.64M SOL | 1.28% | 100% | 0 |
| 15 | `GnC339vk…` | 4.85M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `xLabscif…` · 28.57K SOL · commission 5% · lag 1087682 slots
- `mrgn4atx…` · 20.30K SOL · commission 0% · lag 111945 slots
- `prt1st4R…` · 13.11K SOL · commission 5% · lag 1389113 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 1527332 slots
- `5ZjxMYBb…` · 4.06K SOL · commission 0% · lag 910133 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 2089934 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 336864 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 1437416 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 2075704 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 2117218 slots
- `HFTcVVrX…` · 148.42 SOL · commission 100% · lag 2075598 slots
- `6pEtDovp…` · 131.86 SOL · commission 100% · lag 2089982 slots

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
| **In-protocol fees 24h** | **$380.48K** (3,686.2 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-05 |
| **Solana REV** | **4,278.6 SOL** / **$441.64K** | MEASURED UTC calendar day 2026-09-05: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-05 · UTC day 2026-09-05 · SOL-USD date 2026-09-05 |
| Jito tip-floor run-rate (NOT REV) | $27.36K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 27357 USD; at p95 floor → 154472 USD. |
| Protocol fees 24h | $10.48M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9997 |
| p90 / p99 | 0.000010 / 0.000307 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $105.50 | coingecko.simple_price |
| 24h change | +1.90% | coingecko.simple_price |
| Market cap | $61.73B | coingecko.simple_price |
| 24h volume | $3.71B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.92B |
| TVL 1d / 7d / 30d | +1.11% / +0.23% / +25.46% |
| DEX volume 24h | $1.96B · 1d +4.20% · vs-7d-ago +17.35% |
| 7d DEX volume | $14.51B · -24.36% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $10.48M |
| Fees 1d / 7d | +0.44% / -6.19% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $693.23M | +123.14% |
| BisonFi | $251.95M | 0.00% |
| Orca DEX | $129.40M | -48.31% |
| Raydium AMM | $125.28M | -19.51% |
| Manifest Trade | $123.28M | -24.20% |
| Meteora DLMM | $122.38M | -32.26% |
| Jupiterz | $64.61M | 0.00% |
| Scorch | $63.08M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.59B | +2.42% | -0.69% |
| Kamino Lend | Lending | $1.33B | +0.86% | +6.19% |
| Raydium AMM | Dexs | $1.12B | +1.46% | -1.37% |
| Jupiter Lend | Lending | $1.11B | +1.53% | +1.16% |
| Binance Staked SOL | Liquid Staking | $1.08B | +1.65% | -0.68% |
| Jito Liquid Staking | Liquid Staking | $1.07B | +3.06% | +1.01% |
| BlackRock BUIDL | RWA | $977.90M | -0.00% | +0.60% |
| Jupiter Perpetual Exchange | Derivatives | $758.00M | +0.84% | -1.93% |
| Jupiter Staked SOL | Liquid Staking | $540.36M | +2.55% | -1.14% |
| xStocks | RWA | $450.35M | +0.68% | +4.28% |

## Stablecoins

Solana circulating pegged-USD: **$16.35B**
(1d +0.47% · 7d +3.37%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.36B | +1.24% |
| USDT · Tether | $2.77B | -0.00% |
| USDGO · USDGO | $1.36B | 0.00% |
| USD1 · World Liberty Financial USD | $1.26B | +0.62% |
| BUIDL · BlackRock USD | $977.90M | 0.00% |
| PYUSD · PayPal USD | $751.09M | +4.35% |
| USDG · Global Dollar | $580.47M | +0.20% |
| USDe · Ethena USDe | $535.69M | +0.44% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 60 of 726 Solana-deployed listed symbols (multiplier ok 80/80; 726 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 726 · Solana deployments 726 · priced 60 · priced-subset mcap $283.31K (lower bound, not a census).
24h volume $99.69M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $450.87M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 60 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 726 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 726 unique underlyings among 726 Solana rows; not every tokenized equity on Solana). 726 of 726 listed xStocks have a Solana deployment (726 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.36B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $977.90M
- **xStocks** (RWA) — $450.35M
- **OnRe** (RWA) — $299.20M
- **Huma Finance V2** (RWA) — $191.37M
- **Ondo Yield Assets** (RWA) — $180.01M
- **Hastra** (RWA) — $150.50M
- **Ondo Global Markets** (RWA) — $25.94M
- **Plume Vaults** (RWA) — $24.03M

## Daily active addresses

795,694 (Allium, as of 2026-09-05). Provider range 422,399–795,694. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: BREAKING: $143M+ in 24h tokenized equity volume on @solana](https://x.com/tokens/status/2096652407166165096) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 17:31:02 GMT
- [$ARB is available in your favorite Solana apps

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2096629700479344804) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 16:00:48 GMT
- [Arbitrum ($ARB) is a Layer 2 scaling network, processing transactions at lower cost while inheriting the security of the underlying settlement layer.

Verify the address on @tokens:
https://tokens.xyz/arb?solana=ARBzQTYDCW2KnVEjs1Mc81LekB1ibVFZKbSVmorkoT9d](https://x.com/solana/status/2096629688764674209) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 16:00:45 GMT
- [BREAKING: $ARB is now on Solana via @sunrise

Same asset, better spread and lower fees. By 10x. https://x.com/toly/status/2096599463339127059?s=46](https://x.com/solana/status/2096629676127166873) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 16:00:42 GMT
- [RT by @solana: Startup Village Borneo: Amazing Race Day + our First Connect in Kuching with @RedotsClub recap is out 🤝

Powered by @solana and @socoe_s 🐈](https://x.com/SuperteamMY/status/2096574351240048670) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 12:20:52 GMT
- [No summer slowdown. August wrapped at $143M in app revenue and 5.2B transactions, and September opened with rails built for AI agents.

From SHEIN's listing-day debut to Birkins coming onchain, here's everything that shipped this week:

📰 Headline News

- Solana Payment Channels went live for x402 and MPP, enabling 1M agent payments/sec with batched settlement

- Solana’s logo ad auction raised $167K for Nepal flood relief via @mallowdotart

- @opensea expanded its marketplace to include Solana NFTs

📰 Launches

- SHEIN landed on Solana via @xStocksFi the day it listed in Hong Kong

- @JupiterExchange deployed Universal Deposit, automating cross-chain routing and swapping directly into Solana USDC

- @moonpay introduced PayBox for @grok users to trade, shop and spend through conversation on Solana

- @MidasRWA launched solmF-ONE, bringing @FasanaraCapital's asset-backed credit strategy onchain

- @gmtrade_xyz enabled 24/7 gold and WTI perps with @chainlink Data Streams

- @Beezie partnered with The Luxury Closet to bring authenticated Birkins onchain

- Neuberger Securitize High Income Tokenized Fund (HINC) by @Securitize went live as collateral on @Loopscale

- $AMC and $GPRO tokenized shares went live on Solana via @sunrise, issued by @Backpack Securities

- @arqentrade launched isolated-margin perps across 20 long-tail markets

- @colosseum announced the Crypto World’s Fair hackathon running Sept 14-Oct 12

- @solanamobile scheduled the CLOCK IN hackathon with @RadiantsDAO for Sept 8-Oct 8

- @SuperteamAU joined the Buy Australian AI Partnership as a founding partner alongside major national banks

- @WSOP returned with the 2026 WSOP Super Circuit Canada Main Event

- @M3LEE_LIVE teased social shopping for Solana collectibles

📰 Milestones

- Solana hit a record 5.2B non-vote transactions in August

- Tokenized equity supply reached a new all-time high of $683M

- Solana led August app revenue across chains with $143M, a 38% share

- @onrefinance topped $250M, becoming @kamino’s largest RWA market

- @jtx_trade passed $100M in cumulative trading volume

- Solana's share of x402 transactions rose to 81% in August

- Solana crypto card spending hit a record $100M+ in August

- @Beezie recorded a new all-time high of $2.2M in daily volume

- @fomo achieved a new daily revenue record of $1.2M

If you enjoyed this week’s newsletter, please share it with an RT.

Artwork by @grizzle_art](https://x.com/solana/status/2096584206360969439) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 13:00:02 GMT
- [3](https://x.com/solana/status/2096566100930535617) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 11:48:05 GMT
- [Track all Solana upgrades here: https://solana.com/upgrades](https://x.com/solana/status/2096501152493822052) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 07:30:00 GMT `upgrade`
- [RT by @anza_xyz: 200ms
8k txs (40k TPS)
300M CUs (1.5B CUPS)
5.5k shreds (27.5k SPS)

this is the block 🔳 Agave can handle](https://x.com/bw_solana/status/2096250616351965576) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 05 Sep 2026 14:54:28 GMT
- [RT by @anza_xyz: more users
→ more activity
→ problems exposed
→ IBRL
→ more capacity
→ more resilience
→ better products
→ more users

usage & execution is the moat](https://x.com/bw_solana/status/2095876304805740662) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 04 Sep 2026 14:07:05 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: BREAKING: $143M+ in 24h tokenized equity volume on @solana](https://x.com/tokens/status/2096652407166165096) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 17:31:02 GMT
- [$ARB is available in your favorite Solana apps

@Backpack, @tryfomo, @dflow, @Titan_Exchange, @phantom, @JupiterExchange, @solflare, @kamino_swap, @Raydium, @mayan and more](https://x.com/solana/status/2096629700479344804) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 16:00:48 GMT
- [Arbitrum ($ARB) is a Layer 2 scaling network, processing transactions at lower cost while inheriting the security of the underlying settlement layer.

Verify the address on @tokens:
https://tokens.xyz/arb?solana=ARBzQTYDCW2KnVEjs1Mc81LekB1ibVFZKbSVmorkoT9d](https://x.com/solana/status/2096629688764674209) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 16:00:45 GMT
- [BREAKING: $ARB is now on Solana via @sunrise

Same asset, better spread and lower fees. By 10x. https://x.com/toly/status/2096599463339127059?s=46](https://x.com/solana/status/2096629676127166873) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 16:00:42 GMT
- [RT by @solana: Startup Village Borneo: Amazing Race Day + our First Connect in Kuching with @RedotsClub recap is out 🤝

Powered by @solana and @socoe_s 🐈](https://x.com/SuperteamMY/status/2096574351240048670) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 12:20:52 GMT
- [No summer slowdown. August wrapped at $143M in app revenue and 5.2B transactions, and September opened with rails built for AI agents.

From SHEIN's listing-day debut to Birkins coming onchain, here's everything that shipped this week:

📰 Headline News

- Solana Payment Channels went live for x402 and MPP, enabling 1M agent payments/sec with batched settlement

- Solana’s logo ad auction raised $167K for Nepal flood relief via @mallowdotart

- @opensea expanded its marketplace to include Solana NFTs

📰 Launches

- SHEIN landed on Solana via @xStocksFi the day it listed in Hong Kong

- @JupiterExchange deployed Universal Deposit, automating cross-chain routing and swapping directly into Solana USDC

- @moonpay introduced PayBox for @grok users to trade, shop and spend through conversation on Solana

- @MidasRWA launched solmF-ONE, bringing @FasanaraCapital's asset-backed credit strategy onchain

- @gmtrade_xyz enabled 24/7 gold and WTI perps with @chainlink Data Streams

- @Beezie partnered with The Luxury Closet to bring authenticated Birkins onchain

- Neuberger Securitize High Income Tokenized Fund (HINC) by @Securitize went live as collateral on @Loopscale

- $AMC and $GPRO tokenized shares went live on Solana via @sunrise, issued by @Backpack Securities

- @arqentrade launched isolated-margin perps across 20 long-tail markets

- @colosseum announced the Crypto World’s Fair hackathon running Sept 14-Oct 12

- @solanamobile scheduled the CLOCK IN hackathon with @RadiantsDAO for Sept 8-Oct 8

- @SuperteamAU joined the Buy Australian AI Partnership as a founding partner alongside major national banks

- @WSOP returned with the 2026 WSOP Super Circuit Canada Main Event

- @M3LEE_LIVE teased social shopping for Solana collectibles

📰 Milestones

- Solana hit a record 5.2B non-vote transactions in August

- Tokenized equity supply reached a new all-time high of $683M

- Solana led August app revenue across chains with $143M, a 38% share

- @onrefinance topped $250M, becoming @kamino’s largest RWA market

- @jtx_trade passed $100M in cumulative trading volume

- Solana's share of x402 transactions rose to 81% in August

- Solana crypto card spending hit a record $100M+ in August

- @Beezie recorded a new all-time high of $2.2M in daily volume

- @fomo achieved a new daily revenue record of $1.2M

If you enjoyed this week’s newsletter, please share it with an RT.

Artwork by @grizzle_art](https://x.com/solana/status/2096584206360969439) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 13:00:02 GMT
- [3](https://x.com/solana/status/2096566100930535617) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 11:48:05 GMT
- [Track all Solana upgrades here: https://solana.com/upgrades](https://x.com/solana/status/2096501152493822052) — X/Nitter-style RSS @solana (not Twitter API) · Sun, 06 Sep 2026 07:30:00 GMT `upgrade`
- [RT by @anza_xyz: 200ms
8k txs (40k TPS)
300M CUs (1.5B CUPS)
5.5k shreds (27.5k SPS)

this is the block 🔳 Agave can handle](https://x.com/bw_solana/status/2096250616351965576) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Sat, 05 Sep 2026 14:54:28 GMT
- [RT by @anza_xyz: more users
→ more activity
→ problems exposed
→ IBRL
→ more capacity
→ more resilience
→ better products
→ more users

usage & execution is the moat](https://x.com/bw_solana/status/2095876304805740662) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Fri, 04 Sep 2026 14:07:05 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-06 (2026-09-06 12:48:55 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=pending, 200ms=pending. Observed mean slot ~316 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `observed` — Observed mean slot ~316 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- `rpc.getHealth` [ok] 200 101ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 61ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 69ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 72ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 84ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5930ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 119ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 196ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 160ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 125ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 54ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 55ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 72ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 149ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 98ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 91ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 125ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 506ms https://solana.com/data
- `solana.com.databricks` [ok] 200 122ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 448ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 196ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 108ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 106ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 485ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 772ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 367ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 370ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 370ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 1688ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 1572ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1583ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 203ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 255ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 75ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 63ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 332ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 354ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 477ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 578ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 336ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 573ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 74ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 928ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 368ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 381ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 456ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 353ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 520ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 369ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 382ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1674ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1628ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2246ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1724ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1482ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 2075ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 2237ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 790ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AMZNx` [FAIL]  12032ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SPYx` [FAIL]  12034ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.AAPLx` [FAIL]  12033ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MSFTx` [FAIL]  12035ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.TSLAx` [FAIL]  12039ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.NVDAx` [FAIL]  12039ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.METAx` [FAIL]  12040ms https://api.backed.fi/api/v2/public/assets/METAx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GOOGLx` [FAIL]  12047ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.TSLAx` [ok] 200 224ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.circ.METAx` [ok] 200 258ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 281ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.circ.AAPLx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.GOOGLx` [ok] 200 572ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.circ.AMZNx` [ok] 200 645ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.AAPLx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.mult.METAx` [ok] 200 702ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.TSLAx` [ok] 200 862ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.mult.MSFTx` [ok] 200 949ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 1045ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.mult.SPYx` [ok] 200 1369ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.QQQx` [FAIL]  12038ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.COINx` [FAIL]  12040ms https://api.backed.fi/api/v2/public/assets/COINx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.DRAMx` [FAIL]  12056ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MVLLx` [FAIL]  12045ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.MUUx` [FAIL]  12039ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.QQQx` [ok] 200 390ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.AXTIx` [FAIL]  12032ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.COINx` [ok] 200 435ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.price.DJTx` [FAIL]  12040ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.MVLLx` [ok] 200 399ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.circ.MUUx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.price.KORUx` [FAIL]  12040ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.AXTIx` [ok] 200 561ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 480ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 772ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.COINx` [ok] 200 723ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.circ.KORUx` [ok] 200 775ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.DJTx` [ok] 200 1092ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 899ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 1696ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.mult.MUUx` [ok] 200 1684ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.mult.DJTx` [ok] 200 908ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.SUOPTx` [ok] 200 556ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.BANKCx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.SUOPTx` [ok] 200 675ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 1040ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.mult.SUOPTx` [ok] 200 299ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.ZHAOMx` [ok] 200 551ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.SHEINx` [ok] 200 2656ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.ZHAOMx` [ok] 200 225ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.circ.MMGx` [ok] 200 1017ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.price.TNGYIx` [ok] 200 1575ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.SHEINx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 649ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.LAOPGx` [ok] 200 505ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.mult.SHEINx` [ok] 200 864ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.circ.TNGYIx` [ok] 200 995ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 380ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.price.KUNLx` [ok] 200 229ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 903ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.KUNLx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 469ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 510ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 640ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.HAIDLx` [ok] 200 375ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.price.CTINSx` [ok] 200 1843ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.circ.WRFHDx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 198ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.mult.CTINSx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 2952ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.price.SNBIOx` [ok] 200 404ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 714ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 234ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.mult.HAIDLx` [ok] 200 975ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.mult.JDLOGx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.price.SZIGHx` [ok] 200 682ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.price.ENNHLx` [ok] 200 438ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.circ.SZIGHx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 737ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.ENNHLx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 1280ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 829ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.CRESBx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 372ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.circ.CMERPx` [ok] 200 396ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.SMOIHx` [ok] 200 1890ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 2285ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.CRESBx` [ok] 200 764ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.mult.CMERPx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.circ.HRZRBx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.JTGEXx` [ok] 200 295ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.price.CSPCx` [ok] 200 654ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.HRZRBx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 233ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.price.WXXDCx` [ok] 200 521ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.price.CRESMx` [ok] 200 1110ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.mult.CSPCx` [ok] 200 799ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.circ.JTGEXx` [ok] 200 1095ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.INTWx` [FAIL]  12039ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.CRESMx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.price.SOXSx` [FAIL]  12037ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.SNXXx` [FAIL]  12042ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.WXXDCx` [ok] 200 695ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.INTWx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.circ.SNXXx` [ok] 200 194ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 501ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.CMENDx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 293ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.price.MIXUx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.price.NWGx` [FAIL]  12040ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.BDWAPx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.circ.MIXUx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.SNXXx` [ok] 200 611ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.INTWx` [ok] 200 683ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.circ.SOXSx` [ok] 200 964ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.WXXDCx` [ok] 200 1026ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 336ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.price.ASMPTx` [ok] 200 389ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.JDHLTx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.CRESPx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.SITCx` [ok] 200 621ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.ASMPTx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.price.WHRFRx` [ok] 200 900ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.mult.SOXSx` [ok] 200 919ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.CRESPx` [ok] 200 425ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.SITCx` [ok] 200 525ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 844ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.price.PRADx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.price.SNDSCx` [ok] 200 1044ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.mult.CRESPx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.SITCx` [ok] 200 264ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.circ.PRADx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 798ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.PRADx` [ok] 200 265ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.price.CTFJWx` [ok] 200 285ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 594ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.CLONPx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 286ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.CLONPx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.SINOx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 1345ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.NWGx` [ok] 200 2416ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.circ.SINOx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 1226ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.mult.WHRFRx` [ok] 200 322ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.mult.NWGx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.mult.SINOx` [ok] 200 472ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.mult.CLONPx` [ok] 200 899ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 395ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.SINOTx` [ok] 200 1620ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 429ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 625ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 773ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.WUXIBx` [ok] 200 208ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.CTPCAx` [ok] 200 317ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 1881ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.price.WHGROx` [ok] 200 2178ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.GENTEx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 1409ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.CKAHx` [ok] 200 507ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 1534ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 626ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 888ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.mult.PWAHLx` [ok] 200 310ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.price.CKINFx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.price.SWPRPx` [ok] 200 1237ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.HKCGAx` [ok] 200 350ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.CLPHDx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 1548ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.CKINFx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.circ.WHGROx` [ok] 200 1715ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.circ.CKAHx` [ok] 200 1269ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.CKINFx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 857ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.price.NONGx` [ok] 200 323ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.price.HKEXCx` [ok] 200 730ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.HKCGAx` [ok] 200 851ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.KUAIx` [ok] 200 343ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 546ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.circ.HKEXCx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.circ.NONGx` [ok] 200 402ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.COVELx` [ok] 200 672ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.mult.KUAIx` [ok] 200 332ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.mult.NONGx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.circ.COVELx` [ok] 200 476ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.circ.CHONGx` [ok] 200 500ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.HKEXCx` [ok] 200 694ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.HKCGAx` [ok] 200 1274ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 411ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.GEELx` [ok] 200 818ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.MEITx` [ok] 200 1166ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.mult.WHGROx` [ok] 200 1980ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 725ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.price.HNDLDx` [ok] 200 383ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.circ.GEELx` [ok] 200 297ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.price.PICCx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.GEELx` [ok] 200 259ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.circ.SWPRPx` [ok] 200 2980ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 209ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.circ.HNDLDx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 207ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.price.COSCx` [ok] 200 577ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.CKHUTx` [ok] 200 212ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.COVELx` [ok] 200 1672ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.mult.HNDLDx` [ok] 200 537ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.circ.MEITx` [ok] 200 1091ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.PICCx` [ok] 200 573ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.COSCx` [ok] 200 589ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 563ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.MEITx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.circ.MTRCPx` [ok] 200 2025ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.mult.MTRCPx` [ok] 200 528ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1842ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 239ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.SHEINx` [ok] 200 90ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.MEITx` [ok] 200 93ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 134ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.HKEXCx` [ok] 200 122ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MIXUx` [ok] 200 92ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.BANKCx` [ok] 200 92ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.SUOPTx` [ok] 200 115ms https://lite-api.jup.ag/tokens/v2/search?query=SUOPTx
- `jup.tokens.search.CTINSx` [ok] 200 97ms https://lite-api.jup.ag/tokens/v2/search?query=CTINSx
- `jito.tip_floor` [ok] 200 90ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 336ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 140ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 54ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 55ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 89ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 128ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 237ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
