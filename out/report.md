# Borealis — Solana ecosystem report

**Generated** 2026-09-09T12:55:01Z · 2026-09-09 05:55:01 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-09T12:54:50Z · **RPC health** `ok`
**Health score** 93 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 300)/300, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** ELEVATED — SOL 24h +1.54%; DEX 24h $2.71B · 1d -0% · vs-7d-ago +25%; slot 317 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **WARN · Large Solana protocol fees 7d move** — DeFiLlama Solana protocol fees 7d change is +31.04%. (threshold: `|7d %| >= 20`)
- **INFO · Large Solana DEX volume 7d move** — DeFiLlama Solana DEX volume 7d change is +24.83%. (threshold: `|7d %| >= 20`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 445,616,015 |
| Block height | 423,659,606 |
| Block time | 2026-09-09T12:54:50Z |
| Epoch | 1,031 (51.86% · slot 224,015/432,000) |
| Mean TPS (last ~3,600s) | 4,069.9 |
| Mean non-vote TPS | 1,949.5 |
| Median TPS (same window) | 4,084.2 |
| Mean slot time | 316.7 ms |
| Median slot time | 315.8 ms |
| Transaction count (cluster) | 546,691,062,322 |
| Circulating supply | 586,250,498 SOL |
| Total supply | 633,736,724 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 12 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 436,950,682 SOL |
| Delinquent stake | 1,702,823.14 SOL (0.388%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.34% / 35.67% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.44M SOL | 3.99% | 7% | 0 |
| 2 | `HEL1USMZ…` | 16.35M SOL | 3.74% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.53M SOL | 2.87% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.39M SOL | 2.61% | 5% | 0 |
| 5 | `E1r4Psq8…` | 9.57M SOL | 2.19% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.29M SOL | 2.13% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.03M SOL | 2.07% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.32M SOL | 1.68% | 7% | 0 |
| 9 | `9eGrDohd…` | 6.86M SOL | 1.57% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.60M SOL | 1.51% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.12M SOL | 1.40% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.12M SOL | 1.40% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.97M SOL | 1.37% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.63M SOL | 1.29% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.11% | 7% | 0 |

### Delinquency alerts

- `pSo1KZXg…` · 1.65M SOL · commission 4% · lag 15766 slots
- `mrgn4atx…` · 20.28K SOL · commission 0% · lag 15353 slots
- `inWVrrYJ…` · 9.89K SOL · commission 0% · lag 264986 slots
- `E4xNK4Uw…` · 6.26K SOL · commission 5% · lag 2267292 slots
- `prt1st4R…` · 5.87K SOL · commission 5% · lag 2129073 slots
- `xLabscif…` · 4.17K SOL · commission 5% · lag 1827642 slots
- `5ZjxMYBb…` · 3.21K SOL · commission 0% · lag 1650093 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 117259 slots
- `4GEEKSwu…` · 1.34K SOL · commission 5% · lag 289132 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 445616015 slots
- `R1parD2C…` · 1.63 SOL · commission 5% · lag 61567145 slots
- `Fb77sbwg…` · 1.08 SOL · commission 0% · lag 777004 slots

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
| **In-protocol fees 24h** | **$763.42K** (7,228.6 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-07 |
| **Solana REV** | **8,421.8 SOL** / **$889.43K** | MEASURED UTC calendar day 2026-09-07: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-07 · UTC day 2026-09-07 · SOL-USD date 2026-09-07 |
| Jito tip-floor run-rate (NOT REV) | $96.21K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 96209 USD; at p95 floor → 336667 USD. |
| Protocol fees 24h | $16.56M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | 0.000005 SOL ($0.0005) | NOT a 24h census · ~2.8h · n_tx=2240 window_seconds=9954 |
| p90 / p99 | 0.000015 / 0.000103 SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $104.74 | coingecko.simple_price |
| 24h change | +1.54% | coingecko.simple_price |
| Market cap | $61.41B | coingecko.simple_price |
| 24h volume | $2.88B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $5.96B |
| TVL 1d / 7d / 30d | +0.61% / +5.31% / +22.50% |
| DEX volume 24h | $2.71B · 1d -0.36% · vs-7d-ago +24.83% |
| 7d DEX volume | $16.83B · -0.50% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $16.56M |
| Fees 1d / 7d | +5.94% / +31.04% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| PumpSwap | $737.12M | -15.61% |
| Raydium AMM | $312.03M | +1.37% |
| BisonFi | $249.32M | +22.18% |
| Meteora DLMM | $237.76M | +21.71% |
| Tessera V | $156.31M | +4.56% |
| HumidiFi | $153.40M | +58.34% |
| Manifest Trade | $138.32M | +1.23% |
| pump.fun | $102.04M | +1.76% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.59B | +0.26% | +5.73% |
| Kamino Lend | Lending | $1.36B | +1.54% | +11.30% |
| Raydium AMM | Dexs | $1.15B | +1.61% | +5.92% |
| Jupiter Lend | Lending | $1.10B | +1.52% | +4.71% |
| Binance Staked SOL | Liquid Staking | $1.08B | +0.27% | +5.64% |
| Jito Liquid Staking | Liquid Staking | $1.06B | -0.07% | +7.25% |
| BlackRock BUIDL | RWA | $987.58M | -0.40% | +1.37% |
| Jupiter Perpetual Exchange | Derivatives | $753.84M | +0.41% | +2.37% |
| Jupiter Staked SOL | Liquid Staking | $536.88M | -0.04% | +5.39% |
| xStocks | RWA | $440.89M | -0.41% | +3.17% |

## Stablecoins

Solana circulating pegged-USD: **$16.19B**
(1d -0.39% · 7d +4.94%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.12B | -2.82% |
| USDT · Tether | $2.77B | -0.00% |
| USDGO · USDGO | $1.37B | +0.22% |
| USD1 · World Liberty Financial USD | $1.28B | +1.58% |
| BUIDL · BlackRock USD | $987.58M | +0.99% |
| PYUSD · PayPal USD | $752.35M | +2.83% |
| USDG · Global Dollar | $587.15M | +2.68% |
| USDe · Ethena USDe | $534.19M | -0.29% |

## Tokenized equities (xStocks)

Priced-subset lower bound: quote × circulating × live currentMultiplier over 78 of 737 Solana-deployed listed symbols (multiplier ok 80/80; 737 unique underlyings; attempted 80). Not a 715-name census, and not a census of every tokenized equity on Solana. Missing currentMultiplier → mcap omitted (never silent 1.0).
Listed 737 · Solana deployments 737 · priced 78 · priced-subset mcap $289.30M (lower bound, not a census).
24h volume $85.31M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL $440.89M — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 80 / mcap_computable 78 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 737 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 737 unique underlyings among 737 Solana rows; not every tokenized equity on Solana). 737 of 737 listed xStocks have a Solana deployment (737 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$2.35B** across 27 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **BlackRock BUIDL** (RWA) — $987.58M
- **xStocks** (RWA) — $440.89M
- **OnRe** (RWA) — $305.14M
- **Ondo Yield Assets** (RWA) — $180.05M
- **Huma Finance V2** (RWA) — $171.43M
- **Hastra** (RWA) — $149.48M
- **Ondo Global Markets** (RWA) — $25.71M
- **Plume Vaults** (RWA) — $25.28M

## Daily active addresses

867,112 (Allium, as of 2026-09-07). Provider range 478,831–936,187. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Did you pass the IQ test?](https://x.com/solana/status/2097667443585900979) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 12:44:25 GMT
- [RT by @solana: It’s Solana Summer.

0% swap fees are live now on Trust Wallet for USDT, USDC, EURC, USDS and DAI on @Solana

Now available on Trust Wallet.](https://x.com/TrustWallet/status/2097661271592128925) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 12:19:54 GMT
- [RT by @solana: Tokenizing Beehives on Solana ft. HiveBits https://x.com/i/broadcasts/1DGleVYXgvrJL](https://x.com/superteam/status/2097656326205981079) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 12:00:15 GMT
- [Solana is #1 for monthly @USDC senders: 6.2M in the last 30 days.

42% of everyone sending USDC, and 2.5x the next network.](https://x.com/solana/status/2097631542155870578) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 10:21:46 GMT
- [这个10月和我们@solana_zh 华语社区一起在中国相聚。 注册链接： 

10月16日 Accelerate Shanghai: https://luma.com/acc-shanghai-26
10月18日 18 Oct: Accelerate Hangzhou: https://luma.com/acc-hangzhou-26
10月20日Accelerate Shenzhen: https://luma.com/acc-shenzhen-26
10月22日 Accelerate Beijing: https://luma.com/acc-beijing-26](https://x.com/solana/status/2097604736786849932) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 08:35:15 GMT
- [Pinned: Solana 带着全新的Solana Accelerate China 回来了！一场为科技创造而来的四城巡回之旅 @solana_zh。

10 月 16 日至 22 日，上海、杭州、深圳、北京，Solana 隆重邀请开发者、创业者和投资人加入我们，一起交流、演示，探索中外科技新趋势](https://x.com/solana/status/2097604734027022813) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 08:35:14 GMT
- [RT by @solana: Meteora DBC now supports any token pair on @solana.

Stock tokens, RWAs, and other Token-2022 assets can now be used as quote tokens in DBC launch configurations.

If it’s on Solana, you can launch it on Meteora.](https://x.com/MeteoraAG/status/2097559327855034437) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 05:34:49 GMT
- [Join us on October 6th https://luma.com/solana-summit-singapore-2026](https://x.com/solana/status/2097552418582167824) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 05:07:21 GMT
- [Build with https://pay.sh](https://x.com/solana_devs/status/2097662127859171462) — X/Nitter-style RSS @solana_devs (not Twitter API) · Wed, 09 Sep 2026 12:23:18 GMT
- [1,000,000 payments per second with Solana Payment Channels.](https://x.com/solana_devs/status/2097502080655081892) — X/Nitter-style RSS @solana_devs (not Twitter API) · Wed, 09 Sep 2026 01:47:20 GMT

### X / announcements (public Nitter-style RSS, not Twitter API)

- [Did you pass the IQ test?](https://x.com/solana/status/2097667443585900979) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 12:44:25 GMT
- [RT by @solana: It’s Solana Summer.

0% swap fees are live now on Trust Wallet for USDT, USDC, EURC, USDS and DAI on @Solana

Now available on Trust Wallet.](https://x.com/TrustWallet/status/2097661271592128925) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 12:19:54 GMT
- [RT by @solana: Tokenizing Beehives on Solana ft. HiveBits https://x.com/i/broadcasts/1DGleVYXgvrJL](https://x.com/superteam/status/2097656326205981079) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 12:00:15 GMT
- [Solana is #1 for monthly @USDC senders: 6.2M in the last 30 days.

42% of everyone sending USDC, and 2.5x the next network.](https://x.com/solana/status/2097631542155870578) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 10:21:46 GMT
- [这个10月和我们@solana_zh 华语社区一起在中国相聚。 注册链接： 

10月16日 Accelerate Shanghai: https://luma.com/acc-shanghai-26
10月18日 18 Oct: Accelerate Hangzhou: https://luma.com/acc-hangzhou-26
10月20日Accelerate Shenzhen: https://luma.com/acc-shenzhen-26
10月22日 Accelerate Beijing: https://luma.com/acc-beijing-26](https://x.com/solana/status/2097604736786849932) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 08:35:15 GMT
- [Pinned: Solana 带着全新的Solana Accelerate China 回来了！一场为科技创造而来的四城巡回之旅 @solana_zh。

10 月 16 日至 22 日，上海、杭州、深圳、北京，Solana 隆重邀请开发者、创业者和投资人加入我们，一起交流、演示，探索中外科技新趋势](https://x.com/solana/status/2097604734027022813) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 08:35:14 GMT
- [RT by @solana: Meteora DBC now supports any token pair on @solana.

Stock tokens, RWAs, and other Token-2022 assets can now be used as quote tokens in DBC launch configurations.

If it’s on Solana, you can launch it on Meteora.](https://x.com/MeteoraAG/status/2097559327855034437) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 05:34:49 GMT
- [Join us on October 6th https://luma.com/solana-summit-singapore-2026](https://x.com/solana/status/2097552418582167824) — X/Nitter-style RSS @solana (not Twitter API) · Wed, 09 Sep 2026 05:07:21 GMT
- [Build with https://pay.sh](https://x.com/solana_devs/status/2097662127859171462) — X/Nitter-style RSS @solana_devs (not Twitter API) · Wed, 09 Sep 2026 12:23:18 GMT
- [1,000,000 payments per second with Solana Payment Channels.](https://x.com/solana_devs/status/2097502080655081892) — X/Nitter-style RSS @solana_devs (not Twitter API) · Wed, 09 Sep 2026 01:47:20 GMT

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-09 (2026-09-09 05:55:01 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

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

- **xStocks** — priced up to 80 of 737 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.

## Sources this run

- `rpc.getHealth` [ok] 200 116ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 126ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 72ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 71ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 68ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 6656ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 146ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 43ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 155ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 81ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 31ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 45ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 34ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 85ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 97ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 51ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 84ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 242ms https://solana.com/data
- `solana.com.databricks` [ok] 200 77ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 652ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 56ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 158ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 80ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 363ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [ok] 200 463ms https://xcancel.com/solana/rss
- `rss.xcancel.solana_status` [ok] 200 178ms https://xcancel.com/solana_status/rss
- `rss.xcancel.anza_xyz` [ok] 200 164ms https://xcancel.com/anza_xyz/rss
- `rss.xcancel.solana_devs` [ok] 200 179ms https://xcancel.com/solana_devs/rss
- `rss.nitter.solana` [ok] 200 211ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 184ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [FAIL] 502 942ms https://nitter.perennialte.ch/anza_xyz/rss — HTTP 502 Bad Gateway
- `rss.nitter.solana_devs` [ok] 200 2960ms https://nitter.perennialte.ch/solana_devs/rss
- `status.incidents` [ok] 200 211ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 201ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 109ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 569ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 498ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 466ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 489ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 503ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 780ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 468ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 480ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 482ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 570ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 453ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 396ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 492ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [ok] 200 646ms https://api.mainnet-beta.solana.com
- `xstocks.assets.p0` [ok] 200 1913ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 2540ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [ok] 200 1284ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2
- `xstocks.assets.p3` [ok] 200 1898ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=3
- `xstocks.assets.p4` [ok] 200 1332ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=4
- `xstocks.assets.p5` [ok] 200 4400ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=5
- `xstocks.assets.p6` [ok] 200 1212ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=6
- `xstocks.assets.p7` [ok] 200 762ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=7
- `xstocks.price.GOOGLx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/GOOGLx/price-data
- `xstocks.price.AAPLx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/AAPLx/price-data
- `xstocks.price.SPYx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/SPYx/price-data
- `xstocks.price.MSFTx` [ok] 200 226ms https://api.backed.fi/api/v2/public/assets/MSFTx/price-data
- `xstocks.price.NVDAx` [ok] 200 280ms https://api.backed.fi/api/v2/public/assets/NVDAx/price-data
- `xstocks.circ.GOOGLx` [ok] 200 146ms https://api.backed.fi/api/v2/public/assets/GOOGLx/circulating-supply?format=object
- `xstocks.price.TSLAx` [ok] 200 356ms https://api.backed.fi/api/v2/public/assets/TSLAx/price-data
- `xstocks.circ.NVDAx` [ok] 200 189ms https://api.backed.fi/api/v2/public/assets/NVDAx/circulating-supply?format=object
- `xstocks.price.AMZNx` [ok] 200 550ms https://api.backed.fi/api/v2/public/assets/AMZNx/price-data
- `xstocks.circ.AAPLx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/AAPLx/circulating-supply?format=object
- `xstocks.circ.SPYx` [ok] 200 433ms https://api.backed.fi/api/v2/public/assets/SPYx/circulating-supply?format=object
- `xstocks.mult.NVDAx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/NVDAx/multiplier?network=Solana
- `xstocks.circ.TSLAx` [ok] 200 304ms https://api.backed.fi/api/v2/public/assets/TSLAx/circulating-supply?format=object
- `xstocks.circ.MSFTx` [ok] 200 518ms https://api.backed.fi/api/v2/public/assets/MSFTx/circulating-supply?format=object
- `xstocks.mult.GOOGLx` [ok] 200 496ms https://api.backed.fi/api/v2/public/assets/GOOGLx/multiplier?network=Solana
- `xstocks.mult.AAPLx` [ok] 200 213ms https://api.backed.fi/api/v2/public/assets/AAPLx/multiplier?network=Solana
- `xstocks.circ.AMZNx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/AMZNx/circulating-supply?format=object
- `xstocks.mult.SPYx` [ok] 200 248ms https://api.backed.fi/api/v2/public/assets/SPYx/multiplier?network=Solana
- `xstocks.price.FLNCx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data
- `xstocks.mult.TSLAx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/TSLAx/multiplier?network=Solana
- `xstocks.price.COINx` [ok] 200 589ms https://api.backed.fi/api/v2/public/assets/COINx/price-data
- `xstocks.mult.MSFTx` [ok] 200 642ms https://api.backed.fi/api/v2/public/assets/MSFTx/multiplier?network=Solana
- `xstocks.mult.AMZNx` [ok] 200 639ms https://api.backed.fi/api/v2/public/assets/AMZNx/multiplier?network=Solana
- `xstocks.price.XRXx` [ok] 200 693ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data
- `xstocks.circ.COINx` [ok] 200 136ms https://api.backed.fi/api/v2/public/assets/COINx/circulating-supply?format=object
- `xstocks.price.WGSx` [ok] 200 458ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data
- `xstocks.price.INDIx` [ok] 200 200ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data
- `xstocks.circ.XRXx` [ok] 200 221ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.mult.COINx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/COINx/multiplier?network=Solana
- `xstocks.price.WRLDx` [ok] 200 320ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data
- `xstocks.circ.INDIx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.price.QQQx` [ok] 200 1254ms https://api.backed.fi/api/v2/public/assets/QQQx/price-data
- `xstocks.circ.QQQx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/QQQx/circulating-supply?format=object
- `xstocks.price.PCTx` [ok] 200 346ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data
- `xstocks.mult.XRXx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana
- `xstocks.mult.QQQx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/QQQx/multiplier?network=Solana
- `xstocks.mult.INDIx` [ok] 200 460ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana
- `xstocks.price.METCx` [ok] 200 201ms https://api.backed.fi/api/v2/public/assets/METCx/price-data
- `xstocks.price.QUBTx` [ok] 200 176ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data
- `xstocks.price.METAx` [ok] 200 2556ms https://api.backed.fi/api/v2/public/assets/METAx/price-data
- `xstocks.price.WYFIx` [ok] 200 314ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data
- `xstocks.circ.METAx` [ok] 200 219ms https://api.backed.fi/api/v2/public/assets/METAx/circulating-supply?format=object
- `xstocks.circ.FLNCx` [ok] 200 1873ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.METAx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/METAx/multiplier?network=Solana
- `xstocks.circ.WRLDx` [ok] 200 1529ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.price.BETRx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data
- `xstocks.circ.PCTx` [ok] 200 1396ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.circ.QUBTx` [ok] 200 1109ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 1304ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.circ.WGSx` [ok] 200 2032ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.METCx` [ok] 200 166ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana
- `xstocks.mult.QUBTx` [ok] 200 330ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana
- `xstocks.mult.WRLDx` [ok] 200 632ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana
- `xstocks.mult.FLNCx` [ok] 200 1024ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana
- `xstocks.mult.PCTx` [ok] 200 442ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana
- `xstocks.price.DRAMx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/DRAMx/price-data
- `xstocks.price.AIx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/AIx/price-data
- `xstocks.circ.WYFIx` [ok] 200 1433ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.AXTIx` [ok] 200 138ms https://api.backed.fi/api/v2/public/assets/AXTIx/price-data
- `xstocks.price.MUUx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/MUUx/price-data
- `xstocks.circ.AIx` [ok] 200 131ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object
- `xstocks.circ.DRAMx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/DRAMx/circulating-supply?format=object
- `xstocks.mult.WGSx` [ok] 200 657ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana
- `xstocks.circ.MUUx` [ok] 200 309ms https://api.backed.fi/api/v2/public/assets/MUUx/circulating-supply?format=object
- `xstocks.price.MVLLx` [ok] 200 539ms https://api.backed.fi/api/v2/public/assets/MVLLx/price-data
- `xstocks.mult.MUUx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/MUUx/multiplier?network=Solana
- `xstocks.mult.WYFIx` [ok] 200 641ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana
- `xstocks.price.DJTx` [ok] 200 355ms https://api.backed.fi/api/v2/public/assets/DJTx/price-data
- `xstocks.circ.MVLLx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/MVLLx/circulating-supply?format=object
- `xstocks.mult.MVLLx` [ok] 200 134ms https://api.backed.fi/api/v2/public/assets/MVLLx/multiplier?network=Solana
- `xstocks.mult.DRAMx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/DRAMx/multiplier?network=Solana
- `xstocks.price.KORUx` [ok] 200 466ms https://api.backed.fi/api/v2/public/assets/KORUx/price-data
- `xstocks.price.SOXSx` [ok] 200 246ms https://api.backed.fi/api/v2/public/assets/SOXSx/price-data
- `xstocks.mult.AIx` [ok] 200 1001ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana
- `xstocks.price.SNXXx` [ok] 200 305ms https://api.backed.fi/api/v2/public/assets/SNXXx/price-data
- `xstocks.price.INTWx` [ok] 200 589ms https://api.backed.fi/api/v2/public/assets/INTWx/price-data
- `xstocks.circ.AXTIx` [ok] 200 1366ms https://api.backed.fi/api/v2/public/assets/AXTIx/circulating-supply?format=object
- `xstocks.price.SHEINx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/SHEINx/price-data
- `xstocks.circ.SNXXx` [ok] 200 276ms https://api.backed.fi/api/v2/public/assets/SNXXx/circulating-supply?format=object
- `xstocks.mult.AXTIx` [ok] 200 151ms https://api.backed.fi/api/v2/public/assets/AXTIx/multiplier?network=Solana
- `xstocks.price.NWGx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/NWGx/price-data
- `xstocks.circ.DJTx` [ok] 200 1104ms https://api.backed.fi/api/v2/public/assets/DJTx/circulating-supply?format=object
- `xstocks.circ.SHEINx` [ok] 200 348ms https://api.backed.fi/api/v2/public/assets/SHEINx/circulating-supply?format=object
- `xstocks.mult.SNXXx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/SNXXx/multiplier?network=Solana
- `xstocks.mult.DJTx` [ok] 200 158ms https://api.backed.fi/api/v2/public/assets/DJTx/multiplier?network=Solana
- `xstocks.circ.NWGx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/NWGx/circulating-supply?format=object
- `xstocks.circ.KORUx` [ok] 200 1083ms https://api.backed.fi/api/v2/public/assets/KORUx/circulating-supply?format=object
- `xstocks.circ.SOXSx` [ok] 200 1211ms https://api.backed.fi/api/v2/public/assets/SOXSx/circulating-supply?format=object
- `xstocks.mult.KORUx` [ok] 200 204ms https://api.backed.fi/api/v2/public/assets/KORUx/multiplier?network=Solana
- `xstocks.price.SUOPTx` [ok] 200 377ms https://api.backed.fi/api/v2/public/assets/SUOPTx/price-data
- `xstocks.price.BANKCx` [ok] 200 521ms https://api.backed.fi/api/v2/public/assets/BANKCx/price-data
- `xstocks.circ.INTWx` [ok] 200 1123ms https://api.backed.fi/api/v2/public/assets/INTWx/circulating-supply?format=object
- `xstocks.price.MMGx` [ok] 200 187ms https://api.backed.fi/api/v2/public/assets/MMGx/price-data
- `xstocks.circ.SUOPTx` [ok] 200 152ms https://api.backed.fi/api/v2/public/assets/SUOPTx/circulating-supply?format=object
- `xstocks.mult.NWGx` [ok] 200 511ms https://api.backed.fi/api/v2/public/assets/NWGx/multiplier?network=Solana
- `xstocks.mult.INTWx` [ok] 200 123ms https://api.backed.fi/api/v2/public/assets/INTWx/multiplier?network=Solana
- `xstocks.mult.SOXSx` [ok] 200 241ms https://api.backed.fi/api/v2/public/assets/SOXSx/multiplier?network=Solana
- `xstocks.mult.SHEINx` [ok] 200 832ms https://api.backed.fi/api/v2/public/assets/SHEINx/multiplier?network=Solana
- `xstocks.mult.SUOPTx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/SUOPTx/multiplier?network=Solana
- `xstocks.price.JDLOGx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/JDLOGx/price-data
- `xstocks.price.CTINSx` [ok] 200 143ms https://api.backed.fi/api/v2/public/assets/CTINSx/price-data
- `xstocks.price.LAOPGx` [ok] 200 362ms https://api.backed.fi/api/v2/public/assets/LAOPGx/price-data
- `xstocks.price.TNGYIx` [ok] 200 408ms https://api.backed.fi/api/v2/public/assets/TNGYIx/price-data
- `xstocks.circ.MMGx` [ok] 200 503ms https://api.backed.fi/api/v2/public/assets/MMGx/circulating-supply?format=object
- `xstocks.circ.CTINSx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CTINSx/circulating-supply?format=object
- `xstocks.circ.BANKCx` [ok] 200 628ms https://api.backed.fi/api/v2/public/assets/BANKCx/circulating-supply?format=object
- `xstocks.circ.JDLOGx` [ok] 200 192ms https://api.backed.fi/api/v2/public/assets/JDLOGx/circulating-supply?format=object
- `xstocks.price.ZHAOMx` [ok] 200 527ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/price-data
- `xstocks.circ.TNGYIx` [ok] 200 150ms https://api.backed.fi/api/v2/public/assets/TNGYIx/circulating-supply?format=object
- `xstocks.mult.BANKCx` [ok] 200 130ms https://api.backed.fi/api/v2/public/assets/BANKCx/multiplier?network=Solana
- `xstocks.circ.ZHAOMx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/circulating-supply?format=object
- `xstocks.price.KUNLx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/KUNLx/price-data
- `xstocks.mult.JDLOGx` [ok] 200 268ms https://api.backed.fi/api/v2/public/assets/JDLOGx/multiplier?network=Solana
- `xstocks.circ.KUNLx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/KUNLx/circulating-supply?format=object
- `xstocks.circ.LAOPGx` [ok] 200 624ms https://api.backed.fi/api/v2/public/assets/LAOPGx/circulating-supply?format=object
- `xstocks.mult.MMGx` [ok] 200 537ms https://api.backed.fi/api/v2/public/assets/MMGx/multiplier?network=Solana
- `xstocks.price.WRFHDx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/WRFHDx/price-data
- `xstocks.mult.KUNLx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/KUNLx/multiplier?network=Solana
- `xstocks.circ.WRFHDx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/WRFHDx/circulating-supply?format=object
- `xstocks.price.SNBIOx` [ok] 200 210ms https://api.backed.fi/api/v2/public/assets/SNBIOx/price-data
- `xstocks.circ.BETRx` [ok] 200 4550ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object
- `xstocks.mult.WRFHDx` [ok] 200 222ms https://api.backed.fi/api/v2/public/assets/WRFHDx/multiplier?network=Solana
- `xstocks.mult.ZHAOMx` [ok] 200 752ms https://api.backed.fi/api/v2/public/assets/ZHAOMx/multiplier?network=Solana
- `xstocks.mult.TNGYIx` [ok] 200 987ms https://api.backed.fi/api/v2/public/assets/TNGYIx/multiplier?network=Solana
- `xstocks.price.ENNHLx` [ok] 200 195ms https://api.backed.fi/api/v2/public/assets/ENNHLx/price-data
- `xstocks.price.HAIDLx` [ok] 200 718ms https://api.backed.fi/api/v2/public/assets/HAIDLx/price-data
- `xstocks.mult.CTINSx` [ok] 200 1280ms https://api.backed.fi/api/v2/public/assets/CTINSx/multiplier?network=Solana
- `xstocks.price.SZIGHx` [ok] 200 413ms https://api.backed.fi/api/v2/public/assets/SZIGHx/price-data
- `xstocks.price.SMOIHx` [ok] 200 284ms https://api.backed.fi/api/v2/public/assets/SMOIHx/price-data
- `xstocks.circ.ENNHLx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/ENNHLx/circulating-supply?format=object
- `xstocks.circ.HAIDLx` [ok] 200 121ms https://api.backed.fi/api/v2/public/assets/HAIDLx/circulating-supply?format=object
- `xstocks.circ.SNBIOx` [ok] 200 530ms https://api.backed.fi/api/v2/public/assets/SNBIOx/circulating-supply?format=object
- `xstocks.circ.SMOIHx` [ok] 200 133ms https://api.backed.fi/api/v2/public/assets/SMOIHx/circulating-supply?format=object
- `xstocks.circ.SZIGHx` [ok] 200 185ms https://api.backed.fi/api/v2/public/assets/SZIGHx/circulating-supply?format=object
- `xstocks.price.HRZRBx` [ok] 200 360ms https://api.backed.fi/api/v2/public/assets/HRZRBx/price-data
- `xstocks.mult.SNBIOx` [ok] 200 266ms https://api.backed.fi/api/v2/public/assets/SNBIOx/multiplier?network=Solana
- `xstocks.mult.SZIGHx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/SZIGHx/multiplier?network=Solana
- `xstocks.mult.BETRx` [ok] 200 841ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana
- `xstocks.mult.SMOIHx` [ok] 200 307ms https://api.backed.fi/api/v2/public/assets/SMOIHx/multiplier?network=Solana
- `xstocks.mult.HAIDLx` [ok] 200 401ms https://api.backed.fi/api/v2/public/assets/HAIDLx/multiplier?network=Solana
- `xstocks.price.CRESBx` [ok] 200 181ms https://api.backed.fi/api/v2/public/assets/CRESBx/price-data
- `xstocks.circ.HRZRBx` [ok] 200 247ms https://api.backed.fi/api/v2/public/assets/HRZRBx/circulating-supply?format=object
- `xstocks.price.CMERPx` [ok] 200 251ms https://api.backed.fi/api/v2/public/assets/CMERPx/price-data
- `xstocks.price.JTGEXx` [ok] 200 215ms https://api.backed.fi/api/v2/public/assets/JTGEXx/price-data
- `xstocks.circ.JTGEXx` [ok] 200 157ms https://api.backed.fi/api/v2/public/assets/JTGEXx/circulating-supply?format=object
- `xstocks.mult.ENNHLx` [ok] 200 817ms https://api.backed.fi/api/v2/public/assets/ENNHLx/multiplier?network=Solana
- `xstocks.mult.HRZRBx` [ok] 200 325ms https://api.backed.fi/api/v2/public/assets/HRZRBx/multiplier?network=Solana
- `xstocks.circ.CRESBx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/CRESBx/circulating-supply?format=object
- `xstocks.circ.CMERPx` [ok] 200 321ms https://api.backed.fi/api/v2/public/assets/CMERPx/circulating-supply?format=object
- `xstocks.mult.LAOPGx` [ok] 200 1831ms https://api.backed.fi/api/v2/public/assets/LAOPGx/multiplier?network=Solana
- `xstocks.price.CRESMx` [ok] 200 591ms https://api.backed.fi/api/v2/public/assets/CRESMx/price-data
- `xstocks.price.WXXDCx` [ok] 200 244ms https://api.backed.fi/api/v2/public/assets/WXXDCx/price-data
- `xstocks.mult.CMERPx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CMERPx/multiplier?network=Solana
- `xstocks.price.CMENDx` [ok] 200 289ms https://api.backed.fi/api/v2/public/assets/CMENDx/price-data
- `xstocks.price.CSPCx` [ok] 200 783ms https://api.backed.fi/api/v2/public/assets/CSPCx/price-data
- `xstocks.price.MIXUx` [ok] 200 149ms https://api.backed.fi/api/v2/public/assets/MIXUx/price-data
- `xstocks.circ.CMENDx` [ok] 200 177ms https://api.backed.fi/api/v2/public/assets/CMENDx/circulating-supply?format=object
- `xstocks.circ.WXXDCx` [ok] 200 262ms https://api.backed.fi/api/v2/public/assets/WXXDCx/circulating-supply?format=object
- `xstocks.price.BDWAPx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/BDWAPx/price-data
- `xstocks.mult.JTGEXx` [ok] 200 648ms https://api.backed.fi/api/v2/public/assets/JTGEXx/multiplier?network=Solana
- `xstocks.circ.CRESMx` [ok] 200 464ms https://api.backed.fi/api/v2/public/assets/CRESMx/circulating-supply?format=object
- `xstocks.mult.WXXDCx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/WXXDCx/multiplier?network=Solana
- `xstocks.circ.CSPCx` [ok] 200 338ms https://api.backed.fi/api/v2/public/assets/CSPCx/circulating-supply?format=object
- `xstocks.circ.BDWAPx` [ok] 200 237ms https://api.backed.fi/api/v2/public/assets/BDWAPx/circulating-supply?format=object
- `xstocks.mult.CRESMx` [ok] 200 161ms https://api.backed.fi/api/v2/public/assets/CRESMx/multiplier?network=Solana
- `xstocks.mult.CMENDx` [ok] 200 448ms https://api.backed.fi/api/v2/public/assets/CMENDx/multiplier?network=Solana
- `xstocks.mult.CRESBx` [ok] 200 989ms https://api.backed.fi/api/v2/public/assets/CRESBx/multiplier?network=Solana
- `xstocks.mult.CSPCx` [ok] 200 373ms https://api.backed.fi/api/v2/public/assets/CSPCx/multiplier?network=Solana
- `xstocks.mult.BDWAPx` [ok] 200 369ms https://api.backed.fi/api/v2/public/assets/BDWAPx/multiplier?network=Solana
- `xstocks.price.JDHLTx` [ok] 200 232ms https://api.backed.fi/api/v2/public/assets/JDHLTx/price-data
- `xstocks.price.WHRFRx` [ok] 200 541ms https://api.backed.fi/api/v2/public/assets/WHRFRx/price-data
- `xstocks.circ.MIXUx` [ok] 200 868ms https://api.backed.fi/api/v2/public/assets/MIXUx/circulating-supply?format=object
- `xstocks.price.SITCx` [ok] 200 491ms https://api.backed.fi/api/v2/public/assets/SITCx/price-data
- `xstocks.price.PRADx` [ok] 200 196ms https://api.backed.fi/api/v2/public/assets/PRADx/price-data
- `xstocks.circ.WHRFRx` [ok] 200 267ms https://api.backed.fi/api/v2/public/assets/WHRFRx/circulating-supply?format=object
- `xstocks.circ.PRADx` [ok] 200 191ms https://api.backed.fi/api/v2/public/assets/PRADx/circulating-supply?format=object
- `xstocks.circ.JDHLTx` [ok] 200 483ms https://api.backed.fi/api/v2/public/assets/JDHLTx/circulating-supply?format=object
- `xstocks.mult.PRADx` [ok] 200 172ms https://api.backed.fi/api/v2/public/assets/PRADx/multiplier?network=Solana
- `xstocks.mult.WHRFRx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/WHRFRx/multiplier?network=Solana
- `xstocks.price.SINOTx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/SINOTx/price-data
- `xstocks.mult.JDHLTx` [ok] 200 173ms https://api.backed.fi/api/v2/public/assets/JDHLTx/multiplier?network=Solana
- `xstocks.price.CRESPx` [ok] 200 861ms https://api.backed.fi/api/v2/public/assets/CRESPx/price-data
- `xstocks.price.SNDSCx` [ok] 200 891ms https://api.backed.fi/api/v2/public/assets/SNDSCx/price-data
- `xstocks.circ.SINOTx` [ok] 200 227ms https://api.backed.fi/api/v2/public/assets/SINOTx/circulating-supply?format=object
- `xstocks.price.CTFJWx` [ok] 200 327ms https://api.backed.fi/api/v2/public/assets/CTFJWx/price-data
- `xstocks.price.ASMPTx` [ok] 200 1472ms https://api.backed.fi/api/v2/public/assets/ASMPTx/price-data
- `xstocks.price.CLONPx` [ok] 200 329ms https://api.backed.fi/api/v2/public/assets/CLONPx/price-data
- `xstocks.circ.SNDSCx` [ok] 200 256ms https://api.backed.fi/api/v2/public/assets/SNDSCx/circulating-supply?format=object
- `xstocks.circ.ASMPTx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/ASMPTx/circulating-supply?format=object
- `xstocks.mult.SINOTx` [ok] 200 171ms https://api.backed.fi/api/v2/public/assets/SINOTx/multiplier?network=Solana
- `xstocks.circ.CLONPx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/CLONPx/circulating-supply?format=object
- `xstocks.mult.MIXUx` [ok] 200 1159ms https://api.backed.fi/api/v2/public/assets/MIXUx/multiplier?network=Solana
- `xstocks.mult.SNDSCx` [ok] 200 288ms https://api.backed.fi/api/v2/public/assets/SNDSCx/multiplier?network=Solana
- `xstocks.circ.SITCx` [ok] 200 1203ms https://api.backed.fi/api/v2/public/assets/SITCx/circulating-supply?format=object
- `xstocks.mult.CLONPx` [ok] 200 328ms https://api.backed.fi/api/v2/public/assets/CLONPx/multiplier?network=Solana
- `xstocks.price.CTPCAx` [ok] 200 218ms https://api.backed.fi/api/v2/public/assets/CTPCAx/price-data
- `xstocks.price.WHGROx` [ok] 200 453ms https://api.backed.fi/api/v2/public/assets/WHGROx/price-data
- `xstocks.price.SINOx` [ok] 200 416ms https://api.backed.fi/api/v2/public/assets/SINOx/price-data
- `xstocks.mult.SITCx` [ok] 200 358ms https://api.backed.fi/api/v2/public/assets/SITCx/multiplier?network=Solana
- `xstocks.mult.ASMPTx` [ok] 200 656ms https://api.backed.fi/api/v2/public/assets/ASMPTx/multiplier?network=Solana
- `xstocks.circ.SINOx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/SINOx/circulating-supply?format=object
- `xstocks.circ.CTPCAx` [ok] 200 308ms https://api.backed.fi/api/v2/public/assets/CTPCAx/circulating-supply?format=object
- `xstocks.circ.CRESPx` [ok] 200 1081ms https://api.backed.fi/api/v2/public/assets/CRESPx/circulating-supply?format=object
- `xstocks.mult.CRESPx` [ok] 200 124ms https://api.backed.fi/api/v2/public/assets/CRESPx/multiplier?network=Solana
- `xstocks.mult.SINOx` [ok] 200 141ms https://api.backed.fi/api/v2/public/assets/SINOx/multiplier?network=Solana
- `xstocks.price.PWAHLx` [ok] 200 493ms https://api.backed.fi/api/v2/public/assets/PWAHLx/price-data
- `xstocks.circ.WHGROx` [ok] 200 444ms https://api.backed.fi/api/v2/public/assets/WHGROx/circulating-supply?format=object
- `xstocks.price.GENTEx` [ok] 200 263ms https://api.backed.fi/api/v2/public/assets/GENTEx/price-data
- `xstocks.price.CLPHDx` [ok] 200 287ms https://api.backed.fi/api/v2/public/assets/CLPHDx/price-data
- `xstocks.circ.CTFJWx` [ok] 200 1126ms https://api.backed.fi/api/v2/public/assets/CTFJWx/circulating-supply?format=object
- `xstocks.circ.PWAHLx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/PWAHLx/circulating-supply?format=object
- `xstocks.price.CRAUTx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/CRAUTx/price-data
- `xstocks.circ.CLPHDx` [ok] 200 122ms https://api.backed.fi/api/v2/public/assets/CLPHDx/circulating-supply?format=object
- `xstocks.circ.GENTEx` [ok] 200 162ms https://api.backed.fi/api/v2/public/assets/GENTEx/circulating-supply?format=object
- `xstocks.mult.WHGROx` [ok] 200 182ms https://api.backed.fi/api/v2/public/assets/WHGROx/multiplier?network=Solana
- `xstocks.mult.CTFJWx` [ok] 200 272ms https://api.backed.fi/api/v2/public/assets/CTFJWx/multiplier?network=Solana
- `xstocks.circ.CRAUTx` [ok] 200 240ms https://api.backed.fi/api/v2/public/assets/CRAUTx/circulating-supply?format=object
- `xstocks.mult.GENTEx` [ok] 200 214ms https://api.backed.fi/api/v2/public/assets/GENTEx/multiplier?network=Solana
- `xstocks.price.WUXIBx` [ok] 200 398ms https://api.backed.fi/api/v2/public/assets/WUXIBx/price-data
- `xstocks.price.SWPRPx` [ok] 200 220ms https://api.backed.fi/api/v2/public/assets/SWPRPx/price-data
- `xstocks.mult.PWAHLx` [ok] 200 335ms https://api.backed.fi/api/v2/public/assets/PWAHLx/multiplier?network=Solana
- `xstocks.circ.WUXIBx` [ok] 200 135ms https://api.backed.fi/api/v2/public/assets/WUXIBx/circulating-supply?format=object
- `xstocks.circ.SWPRPx` [ok] 200 228ms https://api.backed.fi/api/v2/public/assets/SWPRPx/circulating-supply?format=object
- `xstocks.mult.WUXIBx` [ok] 200 127ms https://api.backed.fi/api/v2/public/assets/WUXIBx/multiplier?network=Solana
- `xstocks.mult.CLPHDx` [ok] 200 531ms https://api.backed.fi/api/v2/public/assets/CLPHDx/multiplier?network=Solana
- `xstocks.mult.CTPCAx` [ok] 200 869ms https://api.backed.fi/api/v2/public/assets/CTPCAx/multiplier?network=Solana
- `xstocks.price.HKCGAx` [ok] 200 315ms https://api.backed.fi/api/v2/public/assets/HKCGAx/price-data
- `xstocks.mult.SWPRPx` [ok] 200 144ms https://api.backed.fi/api/v2/public/assets/SWPRPx/multiplier?network=Solana
- `xstocks.price.KUAIx` [ok] 200 132ms https://api.backed.fi/api/v2/public/assets/KUAIx/price-data
- `xstocks.circ.KUAIx` [ok] 200 120ms https://api.backed.fi/api/v2/public/assets/KUAIx/circulating-supply?format=object
- `xstocks.price.CKAHx` [ok] 200 577ms https://api.backed.fi/api/v2/public/assets/CKAHx/price-data
- `xstocks.circ.CKAHx` [ok] 200 126ms https://api.backed.fi/api/v2/public/assets/CKAHx/circulating-supply?format=object
- `xstocks.price.CKINFx` [ok] 200 658ms https://api.backed.fi/api/v2/public/assets/CKINFx/price-data
- `xstocks.mult.KUAIx` [ok] 200 145ms https://api.backed.fi/api/v2/public/assets/KUAIx/multiplier?network=Solana
- `xstocks.circ.CKINFx` [ok] 200 261ms https://api.backed.fi/api/v2/public/assets/CKINFx/circulating-supply?format=object
- `xstocks.mult.CKAHx` [ok] 200 368ms https://api.backed.fi/api/v2/public/assets/CKAHx/multiplier?network=Solana
- `xstocks.circ.HKCGAx` [ok] 200 1029ms https://api.backed.fi/api/v2/public/assets/HKCGAx/circulating-supply?format=object
- `xstocks.mult.HKCGAx` [ok] 200 300ms https://api.backed.fi/api/v2/public/assets/HKCGAx/multiplier?network=Solana
- `xstocks.mult.CRAUTx` [ok] 200 2684ms https://api.backed.fi/api/v2/public/assets/CRAUTx/multiplier?network=Solana
- `xstocks.mult.CKINFx` [ok] 200 1823ms https://api.backed.fi/api/v2/public/assets/CKINFx/multiplier?network=Solana
- `llama.protocol.xstocks` [ok] 200 1436ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 306ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.GOOGLx` [ok] 200 72ms https://lite-api.jup.ag/tokens/v2/search?query=GOOGLx
- `jup.tokens.search.AMZNx` [ok] 200 67ms https://lite-api.jup.ag/tokens/v2/search?query=AMZNx
- `jup.tokens.search.INTWx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=INTWx
- `jup.tokens.search.SHEINx` [ok] 200 79ms https://lite-api.jup.ag/tokens/v2/search?query=SHEINx
- `jup.tokens.search.KORUx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=KORUx
- `jup.tokens.search.MVLLx` [ok] 200 79ms https://lite-api.jup.ag/tokens/v2/search?query=MVLLx
- `jup.tokens.search.MUUx` [ok] 200 68ms https://lite-api.jup.ag/tokens/v2/search?query=MUUx
- `jup.tokens.search.DRAMx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=DRAMx
- `jito.tip_floor` [ok] 200 212ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 197ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 91ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 196ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 148ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 103ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 67ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 256ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
