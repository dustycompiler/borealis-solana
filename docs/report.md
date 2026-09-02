# Borealis — Solana ecosystem report

**Generated** 2026-09-02T10:50:50Z · 2026-09-02 03:50:50 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-02T10:50:40Z · **RPC health** `ok`
**Health score** 94 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -4.61%; DEX 24h $2.25B · 1d -10% · vs-7d-ago -23%; slot 315 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -4.61%, DeFiLlama TVL 1d -4.79%, DEX 1d -10.19%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)
- **WARN · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -10.19%. (threshold: `|1d %| >= 8`)
- **WARN · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is -23.45%. (threshold: `|7d %| >= 20`)
- **WARN · Large Solana protocol fees 1d move** — DeFiLlama Solana protocol fees 1d change is -9.19%. (threshold: `|1d %| >= 8`)
- **WARN · Last TPS sample outside 2.5σ of the 60-sample window** — Last sample 3,647 TPS is +3.12σ vs window mean 2,993 (n=60, σ=210). (threshold: `|last sample − window mean| > 2.5σ`)
- **INFO · Daily active addresses vs 30d median** — Current 840,200.00 is +26.5% vs 30d median 664,014.50 (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)
- **INFO · SOL price vs 30d median (solana.com/data)** — Current 97.79 USD is +26.2% vs 30d median 77.46 USD (solana.com/data). (threshold: `|current − 30d median| / median >= 20%`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 443,678,152 |
| Block height | 421,725,598 |
| Block time | 2026-09-02T10:50:40Z |
| Epoch | 1,027 (3.28% · slot 14,153/432,000) |
| Mean TPS (last ~3,600s) | 2,993.4 |
| Mean non-vote TPS | 863.0 |
| Median TPS (same window) | 3,010.0 |
| Mean slot time | 314.6 ms |
| Median slot time | 314.1 ms |
| Transaction count (cluster) | 544,420,334,065 |
| Circulating supply | 585,292,437 SOL |
| Total supply | 633,361,802 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 675 |
| Delinquent | 20 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 437,996,555 SOL |
| Delinquent stake | 425,801.93 SOL (0.097%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.26% / 35.54% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.35M SOL | 3.96% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.33M SOL | 3.73% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.46M SOL | 2.85% | 0% | 0 |
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

- `SLAY6uN1…` · 183.29K SOL · commission 5% · lag 14153 slots
- `nymsGg7Z…` · 91.62K SOL · commission 0% · lag 14154 slots
- `prt1st4R…` · 78.62K SOL · commission 5% · lag 191210 slots
- `omeg2wso…` · 33.32K SOL · commission 0% · lag 34234 slots
- `mrgn4atx…` · 20.34K SOL · commission 0% · lag 13902 slots
- `E4xNK4Uw…` · 10.45K SOL · commission 5% · lag 329429 slots
- `FSyAsxcE…` · 3.02K SOL · commission 100% · lag 892031 slots
- `Fb77sbwg…` · 2.13K SOL · commission 0% · lag 378496 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 239513 slots
- `ChaossRP…` · 827.71 SOL · commission 0% · lag 1694398 slots
- `CpdzCVza…` · 193.38 SOL · commission 100% · lag 877801 slots
- `7ZjHeeYE…` · 176.10 SOL · commission 5% · lag 919315 slots

## Trends

Borealis snapshot tape (data/history.jsonl) with daily DeFiLlama / solana.com/data context.

| Series | Points | Source |
| --- | ---: | --- |
| TPS chart | 464 | data/history.jsonl snapshot tape |
| TVL chart | 464 | data/history.jsonl snapshot tape |
| SOL chart | 463 | data/history.jsonl snapshot tape |
| history.jsonl rows | 464 | data/history.jsonl |

## Economics — Solana REV (UTC calendar day)

Full network REV (Blockworks/Helius) is in-protocol transaction fees (vote + base + priority) plus out-of-protocol Jito MEV tips. Jito tape: GET kobe.mainnet.jito.network/api/v1/daily_mev_rewards (no key). Gross tips = jito_tips + validator_tips (Jito-paid/retained vs validator-distributed; not inclusive; split is not a TipRouter fee rate). UTC calendar day, aligned to solana.com/data Fees date. REV USD uses that same day's solana.com/data SOL Price, not the live snapshot. Never mix dates. tip_floor × TPS is NOT REV. DeFiLlama protocol/application fees are NOT REV.

| Metric | Value | Source |
| --- | ---: | --- |
| **In-protocol fees 24h** | **$832.18K** (8,091.7 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-08-31 |
| **Solana REV** | **9,754.9 SOL** / **$1.00M** | MEASURED UTC calendar day 2026-08-31: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-08-31 · UTC day 2026-08-31 · SOL-USD date 2026-08-31 |
| Jito tip-floor run-rate (NOT REV) | $363.08K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 363084 USD; at p95 floor → 2876418 USD. |
| Protocol fees 24h | $12.26M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9971 |
| p90 / p99 | 0.000008 / 0.000097 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $97.79 | coingecko.simple_price |
| 24h change | -4.61% | coingecko.simple_price |
| Market cap | $57.23B | coingecko.simple_price |
| 24h volume | $3.35B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.70B |
| TVL 1d / 7d / 30d | -4.79% / +1.63% / +20.16% |
| DEX volume 24h | $2.25B · 1d -10.19% · vs-7d-ago -23.45% |
| 7d DEX volume | $16.74B · -23.99% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $12.26M |
| Fees 1d / 7d | -9.19% / -7.47% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $827.37M | -11.91% |
| Orca DEX | $211.42M | -16.98% |
| BisonFi | $204.83M | -12.03% |
| Meteora DLMM | $139.98M | -6.26% |
| Manifest Trade | $136.58M | +4.40% |
| Raydium AMM | $128.25M | -9.18% |
| Axiom | $113.58M | 0.00% |
| Jupiterz | $101.70M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.51B | -4.10% | +2.42% |
| Kamino Lend | Lending | $1.23B | -1.81% | +4.22% |
| Raydium AMM | Dexs | $1.08B | -2.92% | +1.79% |
| Jupiter Lend | Lending | $1.06B | -2.04% | +0.78% |
| Binance Staked SOL | Liquid Staking | $1.03B | -2.67% | +3.19% |
| Jito Liquid Staking | Liquid Staking | $998.27M | -2.91% | +2.45% |
| BlackRock BUIDL | RWA | $887.01M | -1.38% | -0.87% |
| Jupiter Perpetual Exchange | Derivatives | $741.89M | -2.01% | -1.09% |
| Jupiter Staked SOL | Liquid Staking | $514.46M | -2.75% | +2.23% |
| xStocks | RWA | $431.15M | -1.81% | +0.46% |

## Stablecoins

Solana circulating pegged-USD: **$15.47B**
(1d -0.78% · 7d -1.86%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $6.65B | -1.09% |
| USDT · Tether | $2.83B | +0.00% |
| USDGO · USDGO | $1.25B | +0.81% |
| USD1 · World Liberty Financial USD | $1.21B | -0.00% |
| BUIDL · BlackRock USD | $887.01M | +0.01% |
| PYUSD · PayPal USD | $737.50M | -4.74% |
| USDG · Global Dollar | $608.78M | -0.44% |
| USDe · Ethena USDe | $537.17M | -0.01% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 73 of 725 Solana-deployed listed symbols (multiplier ok 80/80; 725 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 725 · Solana deployments 725 · priced 73 · priced-subset mcap $283.63M (lower bound, not a census).
24h volume $23.27M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $427.35M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 73 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 725 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 725 unique underlyings among 725 Solana rows; not every tokenized equity on Solana). 725 of 725 listed xStocks have a Solana deployment (725 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.07B** across 26 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $887.01M
- **xStocks** (RWA) — $431.15M
- **OnRe** (RWA) — $288.02M
- **Ondo Yield Assets** (RWA) — $179.86M
- **Hastra** (RWA) — $153.95M
- **Theo Network thBill** (RWA) — $26.41M
- **Ondo Global Markets** (RWA) — $24.36M
- **Plume Vaults** (RWA) — $22.88M

## Daily active addresses

840,200 (Allium, as of 2026-09-01). Provider range 397,651–840,200. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [RT by @solana: bee's on solana 🐝 (@hivebits_io) 
dino's on solana 🦖 (@Claynosaurz / @JurassicFi) 
pengu's on solana 🐧 (@pudgypenguins)
monke's on solana 🐵 (@MonkeDAO)

welcome to the solana animal kingdom.](https://x.com/superteam/status/2095091546798617014) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 10:08:44 GMT
- [the _ _ _ _ _ supercycle](https://x.com/solana/status/2095077638977310961) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 09:13:28 GMT
- [150k raised so far for Nepal flood relief.

9 hours left to go on @mallowdotart 

👉 https://nepal.mallow.art](https://x.com/solana/status/2094999141881610259) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 04:01:33 GMT
- [BREAKING: SHEIN is live on Solana via @xStocksFi.

The world’s largest online fashion retailer debuts on the Hong Kong Stock Exchange and gets tokenized the same day.](https://x.com/solana/status/2094980455884026053) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 02:47:18 GMT
- [RT by @solana: IP Supercycle (real)

Collector sentiment is starting to pick up again, and @opensea is right at the centre of it.

With the Collector Park coming up during NFT NYC, bringing together some of the biggest IPs in the space.

And now, Solana NFTs are officially coming to OpenSea.

The attention is shifting back onchain.

Pivot to NFTs.](https://x.com/shivst3r/status/2094856142123896872) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 18:33:19 GMT
- [RT by @solana: Green Candle Cup https://x.com/i/broadcasts/1rxmqpzvNqwxy](https://x.com/doublezero/status/2094878026781905186) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 20:00:17 GMT
- [RT by @solana: The Green Candle Cup is here, and we’re putting @Solana’s best traders head to head on a live leaderboard.

@solana_sailor just took the 1st place at the @PhoenixTrade competition, but @aut3z wants a rematch. We’ve given them their very own leaderboard for the GCC.

Remember, if you’re not first, you’re last.

Turn notifications on 🔔](https://x.com/doublezero/status/2094871289525649888) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 19:33:30 GMT
- [RT by @solana: Introducing the solmF-ONE Market, curated by @SteakhouseFi.

Tokenized private credit from Fasanara Capital, a London-based, FCA-regulated manager with $5B+ in AUM and a decade-long track record in SME lending, issued by Midas.

Kamino is the home of institutional credit markets.](https://x.com/kamino/status/2094837639346352498) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 17:19:48 GMT
- [Max transaction size is growing by more than 3x

A new transaction format, Transaction V1 (SIMD-0385), activates on testnet at epoch 1025 raising the transaction size limit from 1,232 to 4,096 bytes.

Use cases like ZK proofs, large multisigs, BLS signatures, and confidential transfers that required multiple transactions now fit in one atomic operation.

In addition to larger max transaction size, Transaction V1 configures transaction resource requests (such as priority fee) in the new V1 header instead of using compute budget instructions.

Transaction V1 is opt-in. Legacy (the original format) and V0 (the format that added address lookup tables) remain supported. Existing apps continue working as is, and can adopt V1 on their own timeline.

RPC operators: update to v4.2.2 or v4.3.0-beta.3 to serve the larger size.](https://x.com/anza_xyz/status/2094913006123761886) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 01 Sep 2026 22:19:16 GMT `upgrade`
- [We're removing floating-point math from Solana's core protocol. Layer by layer.

Layer one: SIMD-0391, activated on mainnet-beta at epoch 1026. It replaces all floating-point (floats) arithmetic in the Stake Program and validator client’s warmup and cooldown logic with fixed-point math.

Layer two: SIMD-0607, now proposed and in review. It targets the runtime itself, removing floats from the inflation rewards and rent calculation path.

Floats can round differently across different hardware, validator clients, and compilers, introducing the possibility of consensus divergence and liveness risk. SIMD-0391 and SIMD-0607 eliminates this by standardizing on fixed-point.

These two improvements aren't the end. Floating-point lives in other, less urgent paths that will transition to fixed-point eventually.](https://x.com/anza_xyz/status/2094509053687091401) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 31 Aug 2026 19:34:07 GMT `upgrade` `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- [RT by @solana: bee's on solana 🐝 (@hivebits_io) 
dino's on solana 🦖 (@Claynosaurz / @JurassicFi) 
pengu's on solana 🐧 (@pudgypenguins)
monke's on solana 🐵 (@MonkeDAO)

welcome to the solana animal kingdom.](https://x.com/superteam/status/2095091546798617014) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 10:08:44 GMT
- [the _ _ _ _ _ supercycle](https://x.com/solana/status/2095077638977310961) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 09:13:28 GMT
- [150k raised so far for Nepal flood relief.

9 hours left to go on @mallowdotart 

👉 https://nepal.mallow.art](https://x.com/solana/status/2094999141881610259) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 04:01:33 GMT
- [BREAKING: SHEIN is live on Solana via @xStocksFi.

The world’s largest online fashion retailer debuts on the Hong Kong Stock Exchange and gets tokenized the same day.](https://x.com/solana/status/2094980455884026053) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 02 Sep 2026 02:47:18 GMT
- [RT by @solana: IP Supercycle (real)

Collector sentiment is starting to pick up again, and @opensea is right at the centre of it.

With the Collector Park coming up during NFT NYC, bringing together some of the biggest IPs in the space.

And now, Solana NFTs are officially coming to OpenSea.

The attention is shifting back onchain.

Pivot to NFTs.](https://x.com/shivst3r/status/2094856142123896872) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 18:33:19 GMT
- [RT by @solana: Green Candle Cup https://x.com/i/broadcasts/1rxmqpzvNqwxy](https://x.com/doublezero/status/2094878026781905186) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 20:00:17 GMT
- [RT by @solana: The Green Candle Cup is here, and we’re putting @Solana’s best traders head to head on a live leaderboard.

@solana_sailor just took the 1st place at the @PhoenixTrade competition, but @aut3z wants a rematch. We’ve given them their very own leaderboard for the GCC.

Remember, if you’re not first, you’re last.

Turn notifications on 🔔](https://x.com/doublezero/status/2094871289525649888) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 19:33:30 GMT
- [RT by @solana: Introducing the solmF-ONE Market, curated by @SteakhouseFi.

Tokenized private credit from Fasanara Capital, a London-based, FCA-regulated manager with $5B+ in AUM and a decade-long track record in SME lending, issued by Midas.

Kamino is the home of institutional credit markets.](https://x.com/kamino/status/2094837639346352498) — X/Nitter-style RSS @solana (not Twitter API) · Tue, 01 Sep 2026 17:19:48 GMT
- [Max transaction size is growing by more than 3x

A new transaction format, Transaction V1 (SIMD-0385), activates on testnet at epoch 1025 raising the transaction size limit from 1,232 to 4,096 bytes.

Use cases like ZK proofs, large multisigs, BLS signatures, and confidential transfers that required multiple transactions now fit in one atomic operation.

In addition to larger max transaction size, Transaction V1 configures transaction resource requests (such as priority fee) in the new V1 header instead of using compute budget instructions.

Transaction V1 is opt-in. Legacy (the original format) and V0 (the format that added address lookup tables) remain supported. Existing apps continue working as is, and can adopt V1 on their own timeline.

RPC operators: update to v4.2.2 or v4.3.0-beta.3 to serve the larger size.](https://x.com/anza_xyz/status/2094913006123761886) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Tue, 01 Sep 2026 22:19:16 GMT `upgrade`
- [We're removing floating-point math from Solana's core protocol. Layer by layer.

Layer one: SIMD-0391, activated on mainnet-beta at epoch 1026. It replaces all floating-point (floats) arithmetic in the Stake Program and validator client’s warmup and cooldown logic with fixed-point math.

Layer two: SIMD-0607, now proposed and in review. It targets the runtime itself, removing floats from the inflation rewards and rent calculation path.

Floats can round differently across different hardware, validator clients, and compilers, introducing the possibility of consensus divergence and liveness risk. SIMD-0391 and SIMD-0607 eliminates this by standardizing on fixed-point.

These two improvements aren't the end. Floating-point lives in other, less urgent paths that will transition to fixed-point eventually.](https://x.com/anza_xyz/status/2094509053687091401) — X/Nitter-style RSS @anza_xyz (not Twitter API) · Mon, 31 Aug 2026 19:34:07 GMT `upgrade` `mainnet`

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-02 (2026-09-02 03:50:50 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 725 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 667ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 122ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 77ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 195ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 100ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6484ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 243ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 42ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 33ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 75ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 22ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 5249ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 992ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 74ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 151ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 47ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 75ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 324ms https://solana.com/data
- `solana.com.databricks` [ok] 200 93ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 251ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 141ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 47ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 128ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 156ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 590ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 153ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 175ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 155ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 253ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 2020ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 1334ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1315ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 103ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 104ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 105ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 497ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 469ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 495ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 392ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 570ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 457ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 429 83ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [ok] 200 546ms https://solana-rpc.publicnode.com
- `rpc.getBlock` [ok] 200 614ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 444ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 356ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 364ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 302ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 469ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 326ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1948ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1676ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 2857ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 3613ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1931ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 1643ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1283ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 832ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.AMZNx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.price.AAPLx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.TSLAx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.TSLAx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.price.SPYx` [ok] 200 561ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.circ.AMZNx` [ok] 200 523ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.TSLAx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.circ.AAPLx` [ok] 200 821ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.price.GOOGLx` [ok] 200 1016ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.circ.SPYx` [ok] 200 568ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.price.METAx` [ok] 200 1197ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.MSFTx` [ok] 200 1266ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.mult.AMZNx` [ok] 200 646ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.price.QQQx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 351ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.COINx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.circ.METAx` [ok] 200 410ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.price.NVDAx` [ok] 200 1640ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.QQQx` [ok] 200 312ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.circ.NVDAx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 324ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 378ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 1154ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.mult.GOOGLx` [ok] 200 878ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.NVDAx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.price.DRAMx` [ok] 200 664ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.circ.COINx` [ok] 200 1234ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 477ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.mult.SPYx` [ok] 200 1654ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.circ.AXTIx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.KORUx` [ok] 200 164ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.circ.MSFTx` [ok] 200 1700ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 391ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.MUUx` [ok] 200 1059ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.price.INTWx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.mult.MSFTx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 879ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.circ.KORUx` [ok] 200 632ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.INTWx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.DJTx` [ok] 200 1423ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.mult.AXTIx` [ok] 200 784ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.SOXSx` [ok] 200 424ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.price.MVLLx` [ok] 200 1804ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.circ.SOXSx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.INTWx` [ok] 200 474ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.mult.KORUx` [ok] 200 532ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.BANKCx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.MVLLx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.mult.SOXSx` [ok] 200 620ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.circ.DJTx` [ok] 200 888ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.mult.DJTx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.mult.MUUx` [ok] 200 1504ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.circ.BANKCx` [ok] 200 584ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.price.SHEINx` [ok] 200 774ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 168ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.price.SNXXx` [ok] 200 1263ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.price.TNGYIx` [ok] 200 303ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.SHEINx` [ok] 200 250ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 579ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.DRAMx` [ok] 200 1964ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.circ.MMGx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.mult.TNGYIx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.mult.MVLLx` [ok] 200 1539ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.SHEINx` [ok] 200 737ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 1031ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.mult.BANKCx` [ok] 200 1236ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.price.CTINSx` [ok] 200 245ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.ZHAOMx` [ok] 200 729ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.price.WRFHDx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.price.LAOPGx` [ok] 200 665ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.JDLOGx` [ok] 200 607ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.circ.LAOPGx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.circ.WRFHDx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 529ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.ZHAOMx` [ok] 200 502ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 703ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.WRFHDx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.CTINSx` [ok] 200 184ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.circ.JDLOGx` [ok] 200 417ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.HAIDLx` [ok] 200 178ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.circ.SNXXx` [ok] 200 1989ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 1292ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.SNBIOx` [ok] 200 183ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.mult.SNXXx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 702ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.mult.ZHAOMx` [ok] 200 711ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.price.SMOIHx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.HAIDLx` [ok] 200 644ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 311ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 1358ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 1160ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 1338ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.price.HRZRBx` [ok] 200 357ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.circ.SNBIOx` [ok] 200 1315ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.HRZRBx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.mult.SNBIOx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.circ.SZIGHx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.ENNHLx` [ok] 200 1497ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.mult.SMOIHx` [ok] 200 971ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 436ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 302ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.KUNLx` [ok] 200 1545ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.price.JTGEXx` [ok] 200 174ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.mult.HAIDLx` [ok] 200 1477ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.WXXDCx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.price.CRESMx` [ok] 200 257ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.CMERPx` [ok] 200 718ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.CRESBx` [ok] 200 1045ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.WXXDCx` [ok] 200 165ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.CMENDx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.circ.CRESBx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.mult.JTGEXx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.price.BDWAPx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.circ.CMENDx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.price.CSPCx` [ok] 200 1074ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.mult.CRESBx` [ok] 200 619ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 156ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.mult.BDWAPx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.price.WHRFRx` [ok] 200 160ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.price.SITCx` [ok] 200 147ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 1212ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.circ.CRESMx` [ok] 200 1285ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.circ.ENNHLx` [ok] 200 1825ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.mult.CMERPx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.mult.CRESMx` [ok] 200 231ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 553ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.SITCx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.price.MIXUx` [ok] 200 2158ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.MIXUx` [ok] 200 125ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 1971ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 2234ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 1647ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.SINOTx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.CMENDx` [ok] 200 3222ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.MIXUx` [ok] 200 1209ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.circ.SINOTx` [ok] 200 238ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.JDHLTx` [ok] 200 2508ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.PRADx` [ok] 200 668ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 153ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.price.SNDSCx` [ok] 200 2499ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.price.ASMPTx` [ok] 200 3202ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.circ.JDHLTx` [ok] 200 371ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 748ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.circ.SNDSCx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.price.CLONPx` [ok] 200 643ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.mult.PRADx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.JDHLTx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.mult.SINOTx` [ok] 200 731ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 682ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.circ.ASMPTx` [ok] 200 745ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.ASMPTx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 521ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.price.PWAHLx` [ok] 200 282ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.price.SINOx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.price.WHGROx` [ok] 200 789ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.circ.SINOx` [ok] 200 468ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 1799ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.price.GENTEx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.circ.WHGROx` [ok] 200 1060ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.CTPCAx` [ok] 200 1869ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.circ.CTPCAx` [ok] 200 119ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.mult.CTPCAx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 1229ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.circ.GENTEx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.price.CLPHDx` [ok] 200 1867ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.price.CRAUTx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.PWAHLx` [ok] 200 1890ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.circ.CRAUTx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.price.WUXIBx` [ok] 200 326ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.mult.SNDSCx` [ok] 200 2789ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 2330ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.CKAHx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 668ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.mult.WUXIBx` [ok] 200 409ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.WHGROx` [ok] 200 1320ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.circ.CLPHDx` [ok] 200 856ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.price.SWPRPx` [ok] 200 514ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.price.KUAIx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.price.HKCGAx` [ok] 200 291ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.circ.CKAHx` [ok] 200 561ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.mult.CLPHDx` [ok] 200 388ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 137ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 1414ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.circ.KUAIx` [ok] 200 529ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 405ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.price.COVELx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/COVELx/price-data
- `xstocks.price.HKEXCx` [ok] 200 695ms https://api.backed.fi/api/v2/public/assets/HKEXCx/price-data
- `xstocks.circ.COVELx` [ok] 200 423ms https://api.backed.fi/api/v2/public/assets/COVELx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 1534ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.circ.HKEXCx` [ok] 200 376ms https://api.backed.fi/api/v2/public/assets/HKEXCx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 1354ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.mult.KUAIx` [ok] 200 920ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.mult.HKEXCx` [ok] 200 252ms https://api.backed.fi/api/v2/public/assets/HKEXCx/multiplier?network=Solana
- `xstocks.mult.SWPRPx` [ok] 200 1431ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 486ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.CRAUTx` [ok] 200 2629ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.COVELx` [ok] 200 582ms https://api.backed.fi/api/v2/public/assets/COVELx/multiplier?network=Solana
- `xstocks.price.GEELx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/GEELx/price-data
- `xstocks.price.HNDLDx` [ok] 200 140ms https://api.backed.fi/api/v2/public/assets/HNDLDx/price-data
- `xstocks.price.PICCx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/PICCx/price-data
- `xstocks.mult.CKINFx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `xstocks.price.CHONGx` [ok] 200 571ms https://api.backed.fi/api/v2/public/assets/CHONGx/price-data
- `xstocks.circ.GEELx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/GEELx/circulating-supply?format=object
- `xstocks.circ.PICCx` [ok] 200 223ms https://api.backed.fi/api/v2/public/assets/PICCx/circulating-supply?format=object
- `xstocks.mult.GEELx` [ok] 200 142ms https://api.backed.fi/api/v2/public/assets/GEELx/multiplier?network=Solana
- `xstocks.circ.HNDLDx` [ok] 200 352ms https://api.backed.fi/api/v2/public/assets/HNDLDx/circulating-supply?format=object
- `xstocks.price.CKHUTx` [ok] 200 193ms https://api.backed.fi/api/v2/public/assets/CKHUTx/price-data
- `xstocks.price.NONGx` [ok] 200 2137ms https://api.backed.fi/api/v2/public/assets/NONGx/price-data
- `xstocks.mult.HNDLDx` [ok] 200 230ms https://api.backed.fi/api/v2/public/assets/HNDLDx/multiplier?network=Solana
- `xstocks.mult.PICCx` [ok] 200 341ms https://api.backed.fi/api/v2/public/assets/PICCx/multiplier?network=Solana
- `xstocks.circ.NONGx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/NONGx/circulating-supply?format=object
- `xstocks.price.COSCx` [ok] 200 557ms https://api.backed.fi/api/v2/public/assets/COSCx/price-data
- `xstocks.circ.CHONGx` [ok] 200 645ms https://api.backed.fi/api/v2/public/assets/CHONGx/circulating-supply?format=object
- `xstocks.mult.NONGx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/NONGx/multiplier?network=Solana
- `xstocks.price.MTRCPx` [ok] 200 1065ms https://api.backed.fi/api/v2/public/assets/MTRCPx/price-data
- `xstocks.price.MEITx` [ok] 200 1345ms https://api.backed.fi/api/v2/public/assets/MEITx/price-data
- `xstocks.circ.MTRCPx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/MTRCPx/circulating-supply?format=object
- `xstocks.circ.COSCx` [ok] 200 366ms https://api.backed.fi/api/v2/public/assets/COSCx/circulating-supply?format=object
- `xstocks.price.POPMTx` [ok] 200 559ms https://api.backed.fi/api/v2/public/assets/POPMTx/price-data
- `xstocks.circ.CKHUTx` [ok] 200 643ms https://api.backed.fi/api/v2/public/assets/CKHUTx/circulating-supply?format=object
- `xstocks.mult.CKHUTx` [ok] 200 148ms https://api.backed.fi/api/v2/public/assets/CKHUTx/multiplier?network=Solana
- `xstocks.circ.POPMTx` [ok] 200 260ms https://api.backed.fi/api/v2/public/assets/POPMTx/circulating-supply?format=object
- `xstocks.circ.MEITx` [ok] 200 543ms https://api.backed.fi/api/v2/public/assets/MEITx/circulating-supply?format=object
- `xstocks.mult.MEITx` [ok] 200 211ms https://api.backed.fi/api/v2/public/assets/MEITx/multiplier?network=Solana
- `xstocks.mult.CHONGx` [ok] 200 1035ms https://api.backed.fi/api/v2/public/assets/CHONGx/multiplier?network=Solana
- `xstocks.mult.POPMTx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/POPMTx/multiplier?network=Solana
- `xstocks.mult.COSCx` [ok] 200 1275ms https://api.backed.fi/api/v2/public/assets/COSCx/multiplier?network=Solana
- `xstocks.mult.MTRCPx` [ok] 200 1816ms https://api.backed.fi/api/v2/public/assets/MTRCPx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1228ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 117ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.POPMTx` [ok] 200 53ms https://lite-api.jup.ag/tokens/v2/search?query=POPMTx
- `jup.tokens.search.HKEXCx` [ok] 200 54ms https://lite-api.jup.ag/tokens/v2/search?query=HKEXCx
- `jup.tokens.search.MEITx` [ok] 200 52ms https://lite-api.jup.ag/tokens/v2/search?query=MEITx
- `jup.tokens.search.KUAIx` [ok] 200 52ms https://lite-api.jup.ag/tokens/v2/search?query=KUAIx
- `jup.tokens.search.MIXUx` [ok] 200 51ms https://lite-api.jup.ag/tokens/v2/search?query=MIXUx
- `jup.tokens.search.BANKCx` [ok] 200 53ms https://lite-api.jup.ag/tokens/v2/search?query=BANKCx
- `jup.tokens.search.AXTIx` [ok] 200 50ms https://lite-api.jup.ag/tokens/v2/search?query=AXTIx
- `jup.tokens.search.KUNLx` [ok] 200 52ms https://lite-api.jup.ag/tokens/v2/search?query=KUNLx
- `jito.tip_floor` [ok] 200 241ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 377ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 71ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 104ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 72ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 78ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 72ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 394ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
