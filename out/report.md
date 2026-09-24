# Borealis — Solana ecosystem report

**Generated** 2026-09-24T08:36:26Z · 2026-09-24 01:36:26 PT
**Author** dustycompiler · **Version** 1.5.7 · **License** MIT
**Live demo** https://dustycompiler.github.io/borealis-solana/
**Cluster block time** 2026-09-24T08:36:18Z · **RPC health** `ok`
**Health score** 98 / 100 — `25×rpc_ok + 30×clamp(1 − max(0, slot_ms − 250)/250, 0, 1) + 25×clamp(1 − delinquent_stake_pct/2, 0, 1) + 20×clamp(tps / tps_baseline, 0, 1)`
**Network health** HEALTHY · **Ecosystem** CONTRACTION — SOL 24h -3.06%; DEX 24h $2.68B · 1d -16% · vs-7d-ago -4%; slot 265 ms
GitHub Actions snapshot (not a guaranteed 15-minute tick). STALE if snapshot age > 2 hours. The HTML dashboard also runs an on-page LIVE pulse (browser JSON-RPC, at most every 60s) for slot/epoch/TPS.

This file is produced by `python3 generate.py` from public endpoints. Every number
is timestamped in `out/report.json`. If a source fails, the tile is omitted rather
than filled with a guess.

## Anomalies

- **ALERT · Large Solana DEX volume 1d move** — DeFiLlama Solana DEX volume 1d change is -16.03%. (threshold: `|1d %| >= 8`)
- **ALERT · Last TPS sample outside 2.5σ of the 60-sample window** — Last sample 4,988 TPS is +4.27σ vs window mean 4,054 (n=60, σ=219). (threshold: `|last sample − window mean| > 2.5σ`)
- **WARN · Correlation: risk-off (SOL 24h ↓ + TVL 1d ↓ + DEX 1d ↓)** — SOL 24h -3.06%, DeFiLlama TVL 1d -2.12%, DEX 1d -16.03%. (threshold: `SOL 24h < 0 AND TVL 1d < 0 AND DEX 1d < 0`)

## Cluster

| Metric | Value |
| --- | ---: |
| Health | `ok` |
| Slot | 449,976,327 |
| Block height | 428,016,448 |
| Block time | 2026-09-24T08:36:18Z |
| Epoch | 1,041 (61.19% · slot 264,328/432,000) |
| Mean TPS (last ~3,600s) | 4,054.0 |
| Mean non-vote TPS | 1,515.2 |
| Median TPS (same window) | 3,992.2 |
| Mean slot time | 265.2 ms |
| Median slot time | 265.5 ms |
| Transaction count (cluster) | 552,027,749,695 |
| Circulating supply | 587,577,348 SOL |
| Total supply | 634,608,460 SOL |
| Burned SOL (incinerator getBalance) | 0.00 SOL |

Native SOL at the Foundation-documented burn address `1nc1nerator11111111111111111111111111111111`.
This is an inaccessible-account balance, not an SPL mint-supply burn.

TPS and slot time are derived from `getRecentPerformanceSamples` (60 × ~60s windows).
TPS = `numTransactions / samplePeriodSecs`. Slot time = `samplePeriodSecs / numSlots`.

## Validators

| Metric | Value |
| --- | ---: |
| Active vote accounts | 676 |
| Delinquent | 11 |
| Lagging current (>150 slots) | 0 |
| Activated stake | 439,764,444 SOL |
| Delinquent stake | 199,692.69 SOL (0.045%) |
| Nakamoto (33% / 50% / 67%) | 18 / 41 / 80 |
| Top 10 / 20 stake share | 24.39% / 35.68% |
| Commission min / median / max | 0% / 5.0% / 100% |

### Top validators by activated stake

| Rank | Node | Stake | Share | Commission | Last vote lag |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | `Fd7btgyS…` | 17.84M SOL | 4.06% | 7% | 0 |
| 2 | `HEL1USMZ…` | 15.84M SOL | 3.60% | 0% | 0 |
| 3 | `DRpbCBMx…` | 12.36M SOL | 2.81% | 0% | 0 |
| 4 | `JUPiTERr…` | 11.26M SOL | 2.56% | 5% | 0 |
| 5 | `E1r4Psq8…` | 10.34M SOL | 2.35% | 0% | 0 |
| 6 | `C8Bey3LK…` | 9.23M SOL | 2.10% | 7% | 0 |
| 7 | `CAo1dCGY…` | 9.16M SOL | 2.08% | 10% | 0 |
| 8 | `EvnRmnMr…` | 7.60M SOL | 1.73% | 7% | 0 |
| 9 | `9eGrDohd…` | 7.09M SOL | 1.61% | 5% | 0 |
| 10 | `Awes4Tr6…` | 6.56M SOL | 1.49% | 0% | 0 |
| 11 | `JD549Hsb…` | 6.22M SOL | 1.42% | 0% | 0 |
| 12 | `9jxgosAf…` | 6.13M SOL | 1.39% | 100% | 0 |
| 13 | `5pPRHnie…` | 5.94M SOL | 1.35% | 5% | 0 |
| 14 | `5Cchr1XG…` | 5.61M SOL | 1.27% | 100% | 0 |
| 15 | `GnC339vk…` | 4.83M SOL | 1.10% | 7% | 0 |

### Delinquency alerts

- `6DTkuiey…` · 89.15K SOL · commission 100% · lag 449976327 slots
- `HDRqPft5…` · 71.15K SOL · commission 100% · lag 449976327 slots
- `t23p8aBQ…` · 14.37K SOL · commission 0% · lag 2381091 slots
- `AYY1TCe3…` · 10.70K SOL · commission 0% · lag 44486 slots
- `NWY18yrP…` · 9.76K SOL · commission 10% · lag 1177617 slots
- `mrgn4atx…` · 2.21K SOL · commission 0% · lag 1378922 slots
- `pSoLoZx5…` · 1.51K SOL · commission 4% · lag 2101575 slots
- `Hgozywot…` · 797.43 SOL · commission 100% · lag 1483456 slots
- `9fTWmMqV…` · 23.86 SOL · commission 0% · lag 1213952 slots
- `R1parD2C…` · 2.87 SOL · commission 5% · lag 65927457 slots
- `6mygxmZx…` · 2.00 SOL · commission 100% · lag 71819 slots

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
| **In-protocol fees 24h** | **$1.09M** (9,201.0 SOL) | solana.com/data Fees (Allium) MEASURED · USD at solana.com/data SOL Price (DexPaprika) UTC 2026-09-22 |
| **Solana REV** | **11,385.8 SOL** / **$1.34M** | MEASURED UTC calendar day 2026-09-22: in-protocol fees + gross Jito MEV tips (jito_tips + validator_tips; not a rolling 24h); USD uses solana.com/data SOL Price (DexPaprika) UTC 2026-09-22 · UTC day 2026-09-22 · SOL-USD date 2026-09-22 |
| Jito tip-floor run-rate (NOT REV) | $53.08K | INVALID as a 24h aggregate · included_in_headline=false · sensitivity (NOT a 24h aggregate, NOT headline REV): invalid run-rate at p50 floor → 53080 USD; at p95 floor → 302603 USD. |
| Protocol fees 24h | $16.52M | EXCLUDED from REV — DeFiLlama Solana protocol fees 24h (not REV) |
| Median tx fee p50 | — SOL (—) | NOT a 24h census · ~2–3h target · n_tx=0 window_seconds=None |
| p90 / p99 | — / — SOL | same sample |
| Burned SOL | 0.00 SOL | incinerator getBalance |

## Market

| Metric | Value | Source |
| --- | ---: | --- |
| SOL/USD | $114.41 | coingecko.simple_price |
| 24h change | -3.06% | coingecko.simple_price |
| Market cap | $67.22B | coingecko.simple_price |
| 24h volume | $4.80B | coingecko.simple_price |

## DeFi (DeFiLlama)

| Metric | Value |
| --- | ---: |
| Solana TVL | $6.40B |
| TVL 1d / 7d / 30d | -2.12% / +10.62% / +11.23% |
| DEX volume 24h | $2.68B · 1d -16.03% · vs-7d-ago -4.17% |
| 7d DEX volume | $19.96B · +11.85% vs prior 7d |
| DEX change_7d meaning | percent change of 24h DEX volume vs the 24h from 7 days ago (not 7d-total vs prior 7d) |
| Protocol fees 24h (DeFiLlama, not REV) | $16.52M |
| Fees 1d / 7d | -7.58% / +10.91% |

### Top DEX venues (24h)

| DEX | 24h volume | 1d |
| --- | ---: | ---: |
| Raydium AMM | $370.01M | -22.25% |
| BisonFi | $368.17M | 0.00% |
| Orca DEX | $355.43M | -3.31% |
| PumpSwap | $270.19M | -57.39% |
| Meteora DLMM | $233.66M | -12.43% |
| Scorch | $129.41M | 0.00% |
| fomo Wallet | $125.97M | -14.79% |
| pump.fun | $121.03M | 0.00% |

### Top Solana protocols by chain TVL

| Protocol | Category | Solana TVL | 1d | 7d |
| --- | --- | ---: | ---: | ---: |
| Sanctum Validator LSTs | Liquid Staking | $1.85B | -1.76% | +16.83% |
| Kamino Lend | Lending | $1.41B | -1.28% | +5.11% |
| Raydium AMM | Dexs | $1.31B | -2.67% | +17.47% |
| Jito Liquid Staking | Liquid Staking | $1.19B | -2.75% | +15.98% |
| Binance Staked SOL | Liquid Staking | $1.18B | -3.26% | +14.34% |
| Jupiter Lend | Lending | $1.17B | -2.44% | +7.87% |
| Jupiter Perpetual Exchange | Derivatives | $804.09M | -2.19% | +8.45% |
| Jupiter Staked SOL | Liquid Staking | $596.60M | -2.63% | +15.78% |
| Marinade Native | Staking Pool | $442.46M | -2.76% | +16.52% |
| PumpSwap | Dexs | $376.74M | -1.35% | +17.40% |

## Stablecoins

Solana circulating pegged-USD: **$16.13B**
(1d -2.70% · 7d +4.21%)

| Asset | Solana circulating | 1d |
| --- | ---: | ---: |
| USDC · USD Coin | $7.55B | -5.07% |
| USDT · Tether | $2.14B | +0.00% |
| USDGO · USDGO | $1.42B | +1.00% |
| USD1 · World Liberty Financial USD | $1.38B | +0.73% |
| BUIDL · BlackRock USD | $987.68M | +0.01% |
| PYUSD · PayPal USD | $735.44M | -0.47% |
| USDG · Global Dollar | $631.44M | +0.30% |
| USDe · Ethena USDe | $496.72M | -1.17% |

## Tokenized equities (xStocks)


Listed 200 · Solana deployments 200 · priced 0 · priced-subset mcap — (lower bound, not a census).
24h volume $151.58M — Jupiter-reported xStocks subset 24h activity (stats24h buy+sell per mint; a swap is buy XOR sell of that mint, not a double-count; not all 715, not all Solana DEX) · 7d volume omitted (no no-key Jupiter/DeFiLlama series).
DeFiLlama protocol/xstocks Solana TVL — — liquidity census, not mcap, not 24h volume.
Formula: `quote * circulating * multiplier` with live currentMultiplier (coverage: multiplier_ok 0 / mcap_computable 0 of attempted 80; missing multiplier → mcap omitted, never silent 1.0). 200 unique xStocks names with a Solana deployment (catalog; 1:1 with unique underlyings in current API; 200 unique underlyings among 200 Solana rows; not every tokenized equity on Solana). 200 of 200 listed xStocks have a Solana deployment (200 unique underlyings). Count share, not market-cap share.

## Real-world assets

Sum of DeFiLlama `chainTvls.Solana` for protocols tagged **RWA** or **RWA Lending**:
**$543.25M** across 16 protocols.
This is protocol TVL, not a full on-chain RWA market-cap census (those Llama endpoints are Pro-only).

- **OnRe** (RWA) — $301.16M
- **Huma** (RWA) — $196.70M
- **Plume Vaults** (RWA) — $28.21M
- **Invesco USTB** (RWA) — $3.91M
- **Mansory** (RWA) — $2.98M
- **VNX** (RWA) — $2.70M
- **Oro Finance** (RWA) — $2.49M
- **International Stable Currency** (RWA) — $2.42M

## Daily active addresses

867,560 (Allium, as of 2026-09-22). Provider range 489,457–895,781. solana.com/data publishes several vendor series for the same label. Values disagree; Borealis does not average them.

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

- [Stocks Go Onchain: What the SEC's Innovation Exemption Means for Solana](https://solana.com/news/stocks-sec-innovation-exemption) — solana.com/news · Wed, 23 Sep 2026 14:06:00 GMT
- [Solana Changelog: September 18, 2026](https://solana.com/news/solana-changelog-september-18-2026) — solana.com/news · Sat, 19 Sep 2026 11:28:00 GMT `mainnet`
- [How AI Is Reshaping Crypto Security, with Michael Coates](https://solana.com/news/bits-to-bricks-crypto-security-michael-coates) — solana.com/news · Sat, 19 Sep 2026 10:00:00 GMT
- [Project Harmonia Brings Institutional Tokenized Funds to Solana](https://solana.com/news/project-harmonia-brings-institutional-tokenized-funds-to-solana) — solana.com/news · Wed, 16 Sep 2026 00:56:00 GMT
- [Solana: Building, Proving and Earning Trust in Public](https://solana.com/news/solana-building-trust-in-public) — solana.com/news · Mon, 14 Sep 2026 11:00:00 GMT
- [Solana Changelog: September 10, 2026](https://solana.com/news/solana-changelog-september-10-2026) — solana.com/news · Thu, 10 Sep 2026 20:16:00 GMT
- [Solana Changelog: September 3, 2026](https://solana.com/news/solana-changelog-september-3-2026) — solana.com/news · Thu, 10 Sep 2026 20:16:00 GMT `mainnet`

### X / announcements (public Nitter-style RSS, not Twitter API)

- No public X/Nitter-style RSS items this run.

Public X/Nitter-style RSS (xcancel.com, nitter mirrors, rsshub). Not the official Twitter API. 403/gated routes are skipped.

## Editorial — SIMD-525 reduced slot times + Alpenglow (SIMD-0326)

_As of 2026-09-24 (2026-09-24 01:36:26 PT). Editorial. Gate labels come from getAccountInfo Feature accounts (effective epoch = activation epoch + 1). Observed slot ms is INFERRED corroboration, not proof. Ignore solana.com/upgrades/reduced-slot-times if it lists 400 ms as current._

First-party Solana Changelog: August 20, 2026: “Feature gates reduced mainnet slot times from 400ms to 350ms, while Testnet moved from 250ms to 200ms.” On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=live, 200ms=pending. Observed mean slot ~265 ms is corroboration only — not feature-gate proof. Alpenglow (SIMD-0326) remains the consensus rewrite (Votor / Rotor); it is a separate track from the slot-time feature gates.

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
- `on-chain` — On-chain Feature accounts: 400ms=superseded, 350ms=live, 300ms=live, 250ms=live, 200ms=pending.
- `observed` — Observed mean slot ~265 ms is corroboration only — not feature-gate proof. INFERRED corroboration, not a feature-gate RPC.
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

- **X / Twitter RSS** — Public X/Nitter-style RSS yielded no usable items this run (403/gated skipped). xcancel.solana 451, xcancel.solana_status 451, xcancel.anza_xyz 451, xcancel.solana_devs 451, nitter.solana 200, nitter.solana_status empty-or-gated
- **Median tx fee** — no getBlock samples
- **xStocks market cap** — Listed Solana-deployed xStocks but quote and/or circulating missing. Mcap omitted.
- **xStocks** — priced up to 80 of 200 Solana-deployed symbols (HTTP budget). Priced-subset lower bound, not a census.
- **xStocks** — FLNCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — QUBTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — PCTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — METCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — WYFIx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — INDIx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — XRXx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — RITMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — RNGx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — WHx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MIDDx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — WRLDx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — VSNTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — REYNx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CARx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — BETRx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — IRDMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — GXOx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — AIx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — WGSx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — ALMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — FBINx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — OZKx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — AMTMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — PSNx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — PEGAx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MTNx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — EXLSx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CRUSx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — EPAMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SAICx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — ELFx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SNDRx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — VNOx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — EXPx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — VIRTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — Mx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MKTXx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — HXLx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CPBx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — VFCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — NXSTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — ADTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — BCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — ACIx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — GTESx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — KRMNx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — HRBx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — DLBx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — AXSx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — RYNx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — POOLx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — TFXx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — LWx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — AAONx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SONx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — INGMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — TTDx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — HRx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — RLIx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CLFx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — STWDx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CZRx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MSMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — OMFx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CROXx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CHEx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — Gx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — ALGMx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MTDRx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — BEPCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — INGRx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MTGx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — BYDx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — LYFTx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — STAGx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — FNBx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — MBGLx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — CACCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — SHCx multiplier missing — mcap omitted (never assumed 1.0)
- **xStocks** — price, circulating-supply, and/or currentMultiplier missing — market cap omitted (never assumed multiplier=1.0)

## Sources this run

- `rpc.getHealth` [ok] 200 287ms https://api.mainnet-beta.solana.com
- `rpc.getSlot` [ok] 200 111ms https://api.mainnet-beta.solana.com
- `rpc.getBlockTime` [ok] 200 115ms https://api.mainnet-beta.solana.com
- `rpc.getEpochInfo` [ok] 200 210ms https://api.mainnet-beta.solana.com
- `rpc.getRecentPerformanceSamples` [ok] 200 113ms https://api.mainnet-beta.solana.com
- `rpc.getSupply` [ok] 200 5975ms https://api.mainnet-beta.solana.com
- `rpc.getVoteAccounts` [ok] 200 188ms https://api.mainnet-beta.solana.com
- `coingecko.simple_price` [ok] 200 36ms https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd&include_24hr_change=true&include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true
- `coinbase.solusd.stats` [ok] 200 68ms https://api.exchange.coinbase.com/products/SOL-USD/stats
- `llama.chains` [ok] 200 66ms https://api.llama.fi/v2/chains
- `llama.historical_tvl` [ok] 200 33ms https://api.llama.fi/v2/historicalChainTvl/Solana
- `llama.dexs` [ok] 200 26ms https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.fees` [ok] 200 1027ms https://api.llama.fi/overview/fees/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true
- `llama.protocols` [ok] 200 91ms https://api.llama.fi/protocols
- `llama.stablecoinchains` [ok] 200 47ms https://stablecoins.llama.fi/stablecoinchains
- `llama.stablecoins` [ok] 200 56ms https://stablecoins.llama.fi/stablecoins?includePrices=true
- `llama.stablecoincharts` [ok] 200 104ms https://stablecoins.llama.fi/stablecoincharts/Solana
- `solana.com.data_page` [ok] 200 347ms https://solana.com/data
- `solana.com.databricks` [ok] 200 1340ms https://solana.com/api/databricks/data?days=30
- `solana.com.rpc_data` [ok] 200 184ms https://solana.com/api/rpc/data
- `status.summary` [ok] 200 93ms https://status.solana.com/api/v2/summary.json
- `rss.status.atom` [ok] 200 54ms https://status.solana.com/history.atom
- `rss.news.rss` [ok] 200 83ms https://solana.com/news/rss.xml
- `rss.anza.medium` [ok] 200 157ms https://medium.com/feed/anza-xyz
- `rss.xcancel.solana` [FAIL] 451 213ms https://xcancel.com/solana/rss — HTTP 451 
- `rss.xcancel.solana_status` [FAIL] 451 89ms https://xcancel.com/solana_status/rss — HTTP 451 
- `rss.xcancel.anza_xyz` [FAIL] 451 101ms https://xcancel.com/anza_xyz/rss — HTTP 451 
- `rss.xcancel.solana_devs` [FAIL] 451 97ms https://xcancel.com/solana_devs/rss — HTTP 451 
- `rss.nitter.solana` [ok] 200 137ms https://nitter.perennialte.ch/solana/rss
- `rss.nitter.solana_status` [ok] 200 60ms https://nitter.perennialte.ch/solana_status/rss
- `rss.nitter.anza_xyz` [ok] 200 50ms https://nitter.perennialte.ch/anza_xyz/rss
- `rss.nitter.solana_devs` [ok] 200 1732ms https://nitter.perennialte.ch/solana_devs/rss
- `rss.rsshub.solana` [FAIL] 404 198ms https://rsshub.app/twitter/user/solana — HTTP 404 Not Found
- `status.incidents` [ok] 200 109ms https://status.solana.com/api/v2/incidents.json
- `rpc.getBalance` [ok] 200 88ms https://api.mainnet-beta.solana.com
- `rpc.getBlocks` [ok] 200 211ms https://api.mainnet-beta.solana.com
- `rpc.getBlock` [FAIL] 200 138ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 105ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 103ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 56ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 358ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 234ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 255ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 249ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 204ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 188ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 208ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 183ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 429 88ms https://api.mainnet-beta.solana.com — HTTP 429 Too Many Requests
- `rpc.getBlock.fallback` [FAIL] 200 152ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 319ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 212ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 284ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 147ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 209ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 111ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 141ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 102ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 131ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 141ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 132ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 135ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock` [FAIL] 200 127ms https://api.mainnet-beta.solana.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `rpc.getBlock.fallback` [FAIL] 200 100ms https://solana-rpc.publicnode.com — {'code': -32015, 'message': 'Transaction version (1) is not supported by the requesting client. Please try the request again with the following configuration parameter: "maxSupportedTransactionVersion": 1'}
- `xstocks.assets.p0` [ok] 200 1413ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=0
- `xstocks.assets.p1` [ok] 200 1348ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=1
- `xstocks.assets.p2` [FAIL] 502 325ms https://api.backed.fi/api/v2/public/assets?pageSize=100&page=2 — HTTP 502 Bad Gateway
- `xstocks.price.METCx` [FAIL] 502 310ms https://api.backed.fi/api/v2/public/assets/METCx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.QUBTx` [FAIL] 502 322ms https://api.backed.fi/api/v2/public/assets/QUBTx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.FLNCx` [FAIL] 502 442ms https://api.backed.fi/api/v2/public/assets/FLNCx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.FLNCx` [ok] 200 155ms https://api.backed.fi/api/v2/public/assets/FLNCx/circulating-supply?format=object
- `xstocks.mult.FLNCx` [FAIL] 502 137ms https://api.backed.fi/api/v2/public/assets/FLNCx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.QUBTx` [ok] 200 434ms https://api.backed.fi/api/v2/public/assets/QUBTx/circulating-supply?format=object
- `xstocks.circ.METCx` [ok] 200 571ms https://api.backed.fi/api/v2/public/assets/METCx/circulating-supply?format=object
- `xstocks.price.PCTx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/PCTx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.INDIx` [FAIL]  12025ms https://api.backed.fi/api/v2/public/assets/INDIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WRLDx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/WRLDx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.WGSx` [FAIL]  12026ms https://api.backed.fi/api/v2/public/assets/WGSx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.XRXx` [FAIL]  12028ms https://api.backed.fi/api/v2/public/assets/XRXx/price-data — TimeoutError: The read operation timed out
- `xstocks.circ.XRXx` [ok] 200 163ms https://api.backed.fi/api/v2/public/assets/XRXx/circulating-supply?format=object
- `xstocks.circ.WRLDx` [ok] 200 167ms https://api.backed.fi/api/v2/public/assets/WRLDx/circulating-supply?format=object
- `xstocks.circ.INDIx` [ok] 200 342ms https://api.backed.fi/api/v2/public/assets/INDIx/circulating-supply?format=object
- `xstocks.circ.PCTx` [ok] 200 716ms https://api.backed.fi/api/v2/public/assets/PCTx/circulating-supply?format=object
- `xstocks.price.WYFIx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/WYFIx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.QUBTx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/QUBTx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.PCTx` [FAIL] 502 112ms https://api.backed.fi/api/v2/public/assets/PCTx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.METCx` [FAIL]  12024ms https://api.backed.fi/api/v2/public/assets/METCx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.circ.WYFIx` [ok] 200 180ms https://api.backed.fi/api/v2/public/assets/WYFIx/circulating-supply?format=object
- `xstocks.price.MIDDx` [FAIL] 502 128ms https://api.backed.fi/api/v2/public/assets/MIDDx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.WYFIx` [FAIL] 502 114ms https://api.backed.fi/api/v2/public/assets/WYFIx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.MIDDx` [FAIL] 502 127ms https://api.backed.fi/api/v2/public/assets/MIDDx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.WGSx` [ok] 200 1275ms https://api.backed.fi/api/v2/public/assets/WGSx/circulating-supply?format=object
- `xstocks.mult.INDIx` [FAIL] 502 10965ms https://api.backed.fi/api/v2/public/assets/INDIx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.XRXx` [FAIL] 502 11244ms https://api.backed.fi/api/v2/public/assets/XRXx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.RITMx` [FAIL] 502 113ms https://api.backed.fi/api/v2/public/assets/RITMx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.RITMx` [FAIL] 502 111ms https://api.backed.fi/api/v2/public/assets/RITMx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.RNGx` [FAIL] 502 128ms https://api.backed.fi/api/v2/public/assets/RNGx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.RNGx` [FAIL] 502 117ms https://api.backed.fi/api/v2/public/assets/RNGx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.RITMx` [FAIL] 502 125ms https://api.backed.fi/api/v2/public/assets/RITMx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.RNGx` [FAIL] 502 124ms https://api.backed.fi/api/v2/public/assets/RNGx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.WHx` [FAIL] 502 114ms https://api.backed.fi/api/v2/public/assets/WHx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.WHx` [FAIL] 502 112ms https://api.backed.fi/api/v2/public/assets/WHx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.WHx` [FAIL] 502 107ms https://api.backed.fi/api/v2/public/assets/WHx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.MIDDx` [FAIL] 502 10984ms https://api.backed.fi/api/v2/public/assets/MIDDx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.WRLDx` [FAIL]  12021ms https://api.backed.fi/api/v2/public/assets/WRLDx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.price.VSNTx` [FAIL] 502 109ms https://api.backed.fi/api/v2/public/assets/VSNTx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.REYNx` [FAIL] 502 121ms https://api.backed.fi/api/v2/public/assets/REYNx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.REYNx` [FAIL] 502 121ms https://api.backed.fi/api/v2/public/assets/REYNx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.VSNTx` [FAIL] 502 127ms https://api.backed.fi/api/v2/public/assets/VSNTx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.CARx` [FAIL] 502 322ms https://api.backed.fi/api/v2/public/assets/CARx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.CARx` [FAIL] 502 126ms https://api.backed.fi/api/v2/public/assets/CARx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.VSNTx` [FAIL] 502 293ms https://api.backed.fi/api/v2/public/assets/VSNTx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.REYNx` [FAIL] 502 330ms https://api.backed.fi/api/v2/public/assets/REYNx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.CARx` [FAIL] 502 117ms https://api.backed.fi/api/v2/public/assets/CARx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.BETRx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/BETRx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.OZKx` [FAIL] 502 124ms https://api.backed.fi/api/v2/public/assets/OZKx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.IRDMx` [FAIL] 502 135ms https://api.backed.fi/api/v2/public/assets/IRDMx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.AIx` [FAIL]  12017ms https://api.backed.fi/api/v2/public/assets/AIx/price-data — TimeoutError: The read operation timed out
- `xstocks.price.GXOx` [FAIL] 502 120ms https://api.backed.fi/api/v2/public/assets/GXOx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.BETRx` [FAIL] 502 118ms https://api.backed.fi/api/v2/public/assets/BETRx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.IRDMx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/IRDMx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.AIx` [FAIL] 502 119ms https://api.backed.fi/api/v2/public/assets/AIx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.GXOx` [FAIL] 502 129ms https://api.backed.fi/api/v2/public/assets/GXOx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.BETRx` [FAIL] 502 116ms https://api.backed.fi/api/v2/public/assets/BETRx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.ALMx` [FAIL]  12020ms https://api.backed.fi/api/v2/public/assets/ALMx/price-data — TimeoutError: The read operation timed out
- `xstocks.mult.IRDMx` [FAIL] 502 125ms https://api.backed.fi/api/v2/public/assets/IRDMx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.OZKx` [FAIL] 502 323ms https://api.backed.fi/api/v2/public/assets/OZKx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.GXOx` [FAIL] 502 125ms https://api.backed.fi/api/v2/public/assets/GXOx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.FBINx` [FAIL] 502 125ms https://api.backed.fi/api/v2/public/assets/FBINx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.ALMx` [FAIL] 502 124ms https://api.backed.fi/api/v2/public/assets/ALMx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.AMTMx` [FAIL] 502 132ms https://api.backed.fi/api/v2/public/assets/AMTMx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.MTNx` [FAIL] 502 122ms https://api.backed.fi/api/v2/public/assets/MTNx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.FBINx` [FAIL] 502 122ms https://api.backed.fi/api/v2/public/assets/FBINx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.AIx` [FAIL] 502 326ms https://api.backed.fi/api/v2/public/assets/AIx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.WGSx` [FAIL]  12016ms https://api.backed.fi/api/v2/public/assets/WGSx/multiplier?network=Solana — TimeoutError: The read operation timed out
- `xstocks.mult.ALMx` [FAIL] 502 122ms https://api.backed.fi/api/v2/public/assets/ALMx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.AMTMx` [FAIL] 502 120ms https://api.backed.fi/api/v2/public/assets/AMTMx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.FBINx` [FAIL] 502 130ms https://api.backed.fi/api/v2/public/assets/FBINx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.PSNx` [FAIL] 502 121ms https://api.backed.fi/api/v2/public/assets/PSNx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.PEGAx` [FAIL] 502 128ms https://api.backed.fi/api/v2/public/assets/PEGAx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.OZKx` [FAIL] 502 337ms https://api.backed.fi/api/v2/public/assets/OZKx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.AMTMx` [FAIL] 502 116ms https://api.backed.fi/api/v2/public/assets/AMTMx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.EXLSx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/EXLSx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.PSNx` [FAIL] 502 116ms https://api.backed.fi/api/v2/public/assets/PSNx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.PEGAx` [FAIL] 502 126ms https://api.backed.fi/api/v2/public/assets/PEGAx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.EPAMx` [FAIL] 502 118ms https://api.backed.fi/api/v2/public/assets/EPAMx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.MTNx` [FAIL] 502 307ms https://api.backed.fi/api/v2/public/assets/MTNx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.CRUSx` [FAIL] 502 122ms https://api.backed.fi/api/v2/public/assets/CRUSx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.SAICx` [FAIL] 502 327ms https://api.backed.fi/api/v2/public/assets/SAICx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.EXLSx` [FAIL] 502 124ms https://api.backed.fi/api/v2/public/assets/EXLSx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.PSNx` [FAIL] 502 119ms https://api.backed.fi/api/v2/public/assets/PSNx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.PEGAx` [FAIL] 502 124ms https://api.backed.fi/api/v2/public/assets/PEGAx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.CRUSx` [FAIL] 502 110ms https://api.backed.fi/api/v2/public/assets/CRUSx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.MTNx` [FAIL] 502 116ms https://api.backed.fi/api/v2/public/assets/MTNx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.EPAMx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/EPAMx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.SAICx` [FAIL] 502 135ms https://api.backed.fi/api/v2/public/assets/SAICx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.EXLSx` [FAIL] 502 118ms https://api.backed.fi/api/v2/public/assets/EXLSx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.Mx` [FAIL] 502 114ms https://api.backed.fi/api/v2/public/assets/Mx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.ELFx` [FAIL] 502 124ms https://api.backed.fi/api/v2/public/assets/ELFx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.CRUSx` [FAIL] 502 122ms https://api.backed.fi/api/v2/public/assets/CRUSx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.EPAMx` [FAIL] 502 126ms https://api.backed.fi/api/v2/public/assets/EPAMx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.SNDRx` [FAIL] 502 134ms https://api.backed.fi/api/v2/public/assets/SNDRx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.SAICx` [FAIL] 502 113ms https://api.backed.fi/api/v2/public/assets/SAICx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.VNOx` [FAIL] 502 132ms https://api.backed.fi/api/v2/public/assets/VNOx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.EXPx` [FAIL] 502 118ms https://api.backed.fi/api/v2/public/assets/EXPx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.ELFx` [FAIL] 502 121ms https://api.backed.fi/api/v2/public/assets/ELFx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.VIRTx` [FAIL] 502 113ms https://api.backed.fi/api/v2/public/assets/VIRTx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.SNDRx` [FAIL] 502 112ms https://api.backed.fi/api/v2/public/assets/SNDRx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.MKTXx` [FAIL] 502 126ms https://api.backed.fi/api/v2/public/assets/MKTXx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.VNOx` [FAIL] 502 129ms https://api.backed.fi/api/v2/public/assets/VNOx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.EXPx` [FAIL] 502 124ms https://api.backed.fi/api/v2/public/assets/EXPx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.VIRTx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/VIRTx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.ELFx` [FAIL] 502 125ms https://api.backed.fi/api/v2/public/assets/ELFx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.SNDRx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/SNDRx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.Mx` [FAIL] 502 316ms https://api.backed.fi/api/v2/public/assets/Mx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.MKTXx` [FAIL] 502 121ms https://api.backed.fi/api/v2/public/assets/MKTXx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.VNOx` [FAIL] 502 115ms https://api.backed.fi/api/v2/public/assets/VNOx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.EXPx` [FAIL] 502 115ms https://api.backed.fi/api/v2/public/assets/EXPx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.VIRTx` [FAIL] 502 122ms https://api.backed.fi/api/v2/public/assets/VIRTx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.HXLx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/HXLx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.CPBx` [FAIL] 502 140ms https://api.backed.fi/api/v2/public/assets/CPBx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.Mx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/Mx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.MKTXx` [FAIL] 502 130ms https://api.backed.fi/api/v2/public/assets/MKTXx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.VFCx` [FAIL] 502 117ms https://api.backed.fi/api/v2/public/assets/VFCx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.ADTx` [FAIL] 502 120ms https://api.backed.fi/api/v2/public/assets/ADTx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.NXSTx` [FAIL] 502 130ms https://api.backed.fi/api/v2/public/assets/NXSTx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.HXLx` [FAIL] 502 129ms https://api.backed.fi/api/v2/public/assets/HXLx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.CPBx` [FAIL] 502 120ms https://api.backed.fi/api/v2/public/assets/CPBx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.BCx` [FAIL] 502 118ms https://api.backed.fi/api/v2/public/assets/BCx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.ACIx` [FAIL] 502 115ms https://api.backed.fi/api/v2/public/assets/ACIx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.VFCx` [FAIL] 502 119ms https://api.backed.fi/api/v2/public/assets/VFCx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.NXSTx` [FAIL] 502 121ms https://api.backed.fi/api/v2/public/assets/NXSTx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.ADTx` [FAIL] 502 127ms https://api.backed.fi/api/v2/public/assets/ADTx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.HXLx` [FAIL] 502 117ms https://api.backed.fi/api/v2/public/assets/HXLx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.CPBx` [FAIL] 502 119ms https://api.backed.fi/api/v2/public/assets/CPBx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.BCx` [FAIL] 502 111ms https://api.backed.fi/api/v2/public/assets/BCx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.ACIx` [FAIL] 502 127ms https://api.backed.fi/api/v2/public/assets/ACIx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.VFCx` [FAIL] 502 127ms https://api.backed.fi/api/v2/public/assets/VFCx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.KRMNx` [FAIL] 502 118ms https://api.backed.fi/api/v2/public/assets/KRMNx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.NXSTx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/NXSTx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.ADTx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/ADTx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.GTESx` [FAIL] 502 120ms https://api.backed.fi/api/v2/public/assets/GTESx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.BCx` [FAIL] 502 120ms https://api.backed.fi/api/v2/public/assets/BCx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.HRBx` [FAIL] 502 116ms https://api.backed.fi/api/v2/public/assets/HRBx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.ACIx` [FAIL] 502 126ms https://api.backed.fi/api/v2/public/assets/ACIx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.AXSx` [FAIL] 502 119ms https://api.backed.fi/api/v2/public/assets/AXSx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.DLBx` [FAIL] 502 121ms https://api.backed.fi/api/v2/public/assets/DLBx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.KRMNx` [FAIL] 502 126ms https://api.backed.fi/api/v2/public/assets/KRMNx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.GTESx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/GTESx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.RYNx` [FAIL] 502 127ms https://api.backed.fi/api/v2/public/assets/RYNx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.HRBx` [FAIL] 502 139ms https://api.backed.fi/api/v2/public/assets/HRBx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.POOLx` [FAIL] 502 139ms https://api.backed.fi/api/v2/public/assets/POOLx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.AXSx` [FAIL] 502 115ms https://api.backed.fi/api/v2/public/assets/AXSx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.DLBx` [FAIL] 502 119ms https://api.backed.fi/api/v2/public/assets/DLBx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.GTESx` [FAIL] 502 107ms https://api.backed.fi/api/v2/public/assets/GTESx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.KRMNx` [FAIL] 502 134ms https://api.backed.fi/api/v2/public/assets/KRMNx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.RYNx` [FAIL] 502 114ms https://api.backed.fi/api/v2/public/assets/RYNx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.HRBx` [FAIL] 502 116ms https://api.backed.fi/api/v2/public/assets/HRBx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.POOLx` [FAIL] 502 122ms https://api.backed.fi/api/v2/public/assets/POOLx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.DLBx` [FAIL] 502 117ms https://api.backed.fi/api/v2/public/assets/DLBx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.TFXx` [FAIL] 502 121ms https://api.backed.fi/api/v2/public/assets/TFXx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.AXSx` [FAIL] 502 136ms https://api.backed.fi/api/v2/public/assets/AXSx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.LWx` [FAIL] 502 116ms https://api.backed.fi/api/v2/public/assets/LWx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.RYNx` [FAIL] 502 122ms https://api.backed.fi/api/v2/public/assets/RYNx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.AAONx` [FAIL] 502 121ms https://api.backed.fi/api/v2/public/assets/AAONx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.POOLx` [FAIL] 502 125ms https://api.backed.fi/api/v2/public/assets/POOLx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.SONx` [FAIL] 502 116ms https://api.backed.fi/api/v2/public/assets/SONx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.TFXx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/TFXx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.INGMx` [FAIL] 502 127ms https://api.backed.fi/api/v2/public/assets/INGMx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.LWx` [FAIL] 502 128ms https://api.backed.fi/api/v2/public/assets/LWx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.TTDx` [FAIL] 502 126ms https://api.backed.fi/api/v2/public/assets/TTDx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.AAONx` [FAIL] 502 119ms https://api.backed.fi/api/v2/public/assets/AAONx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.HRx` [FAIL] 502 122ms https://api.backed.fi/api/v2/public/assets/HRx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.SONx` [FAIL] 502 128ms https://api.backed.fi/api/v2/public/assets/SONx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.INGMx` [FAIL] 502 111ms https://api.backed.fi/api/v2/public/assets/INGMx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.TFXx` [FAIL] 502 125ms https://api.backed.fi/api/v2/public/assets/TFXx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.LWx` [FAIL] 502 113ms https://api.backed.fi/api/v2/public/assets/LWx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.TTDx` [FAIL] 502 120ms https://api.backed.fi/api/v2/public/assets/TTDx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.AAONx` [FAIL] 502 120ms https://api.backed.fi/api/v2/public/assets/AAONx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.HRx` [FAIL] 502 125ms https://api.backed.fi/api/v2/public/assets/HRx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.SONx` [FAIL] 502 121ms https://api.backed.fi/api/v2/public/assets/SONx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.INGMx` [FAIL] 502 120ms https://api.backed.fi/api/v2/public/assets/INGMx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.RLIx` [FAIL] 502 120ms https://api.backed.fi/api/v2/public/assets/RLIx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.CLFx` [FAIL] 502 136ms https://api.backed.fi/api/v2/public/assets/CLFx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.TTDx` [FAIL] 502 130ms https://api.backed.fi/api/v2/public/assets/TTDx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.STWDx` [FAIL] 502 125ms https://api.backed.fi/api/v2/public/assets/STWDx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.HRx` [FAIL] 502 122ms https://api.backed.fi/api/v2/public/assets/HRx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.RLIx` [FAIL] 502 109ms https://api.backed.fi/api/v2/public/assets/RLIx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.MSMx` [FAIL] 502 127ms https://api.backed.fi/api/v2/public/assets/MSMx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.CZRx` [FAIL] 502 127ms https://api.backed.fi/api/v2/public/assets/CZRx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.CLFx` [FAIL] 502 125ms https://api.backed.fi/api/v2/public/assets/CLFx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.OMFx` [FAIL] 502 119ms https://api.backed.fi/api/v2/public/assets/OMFx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.STWDx` [FAIL] 502 116ms https://api.backed.fi/api/v2/public/assets/STWDx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.CROXx` [FAIL] 502 108ms https://api.backed.fi/api/v2/public/assets/CROXx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.CZRx` [FAIL] 502 114ms https://api.backed.fi/api/v2/public/assets/CZRx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.RLIx` [FAIL] 502 130ms https://api.backed.fi/api/v2/public/assets/RLIx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.MSMx` [FAIL] 502 128ms https://api.backed.fi/api/v2/public/assets/MSMx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.CLFx` [FAIL] 502 113ms https://api.backed.fi/api/v2/public/assets/CLFx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.OMFx` [FAIL] 502 119ms https://api.backed.fi/api/v2/public/assets/OMFx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.STWDx` [FAIL] 502 120ms https://api.backed.fi/api/v2/public/assets/STWDx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.CROXx` [FAIL] 502 127ms https://api.backed.fi/api/v2/public/assets/CROXx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.CHEx` [FAIL] 502 119ms https://api.backed.fi/api/v2/public/assets/CHEx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.CZRx` [FAIL] 502 133ms https://api.backed.fi/api/v2/public/assets/CZRx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.Gx` [FAIL] 502 113ms https://api.backed.fi/api/v2/public/assets/Gx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.MSMx` [FAIL] 502 126ms https://api.backed.fi/api/v2/public/assets/MSMx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.OMFx` [FAIL] 502 120ms https://api.backed.fi/api/v2/public/assets/OMFx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.ALGMx` [FAIL] 502 127ms https://api.backed.fi/api/v2/public/assets/ALGMx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.CROXx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/CROXx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.CHEx` [FAIL] 502 117ms https://api.backed.fi/api/v2/public/assets/CHEx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.Gx` [FAIL] 502 114ms https://api.backed.fi/api/v2/public/assets/Gx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.MTDRx` [FAIL] 502 115ms https://api.backed.fi/api/v2/public/assets/MTDRx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.BEPCx` [FAIL] 502 129ms https://api.backed.fi/api/v2/public/assets/BEPCx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.ALGMx` [FAIL] 502 130ms https://api.backed.fi/api/v2/public/assets/ALGMx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.INGRx` [FAIL] 502 131ms https://api.backed.fi/api/v2/public/assets/INGRx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.CHEx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/CHEx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.Gx` [FAIL] 502 124ms https://api.backed.fi/api/v2/public/assets/Gx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.MTDRx` [FAIL] 502 113ms https://api.backed.fi/api/v2/public/assets/MTDRx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.BEPCx` [FAIL] 502 121ms https://api.backed.fi/api/v2/public/assets/BEPCx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.MTGx` [FAIL] 502 301ms https://api.backed.fi/api/v2/public/assets/MTGx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.ALGMx` [FAIL] 502 122ms https://api.backed.fi/api/v2/public/assets/ALGMx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.INGRx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/INGRx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.LYFTx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/LYFTx/price-data — HTTP 502 Bad Gateway
- `xstocks.price.BYDx` [FAIL] 502 126ms https://api.backed.fi/api/v2/public/assets/BYDx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.MTDRx` [FAIL] 502 131ms https://api.backed.fi/api/v2/public/assets/MTDRx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.BEPCx` [FAIL] 502 129ms https://api.backed.fi/api/v2/public/assets/BEPCx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.MTGx` [FAIL] 502 123ms https://api.backed.fi/api/v2/public/assets/MTGx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.STAGx` [FAIL] 502 111ms https://api.backed.fi/api/v2/public/assets/STAGx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.BYDx` [FAIL] 502 113ms https://api.backed.fi/api/v2/public/assets/BYDx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.INGRx` [FAIL] 502 128ms https://api.backed.fi/api/v2/public/assets/INGRx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.FNBx` [FAIL] 502 110ms https://api.backed.fi/api/v2/public/assets/FNBx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.LYFTx` [FAIL] 502 133ms https://api.backed.fi/api/v2/public/assets/LYFTx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.price.MBGLx` [FAIL] 502 124ms https://api.backed.fi/api/v2/public/assets/MBGLx/price-data — HTTP 502 Bad Gateway
- `xstocks.mult.MTGx` [FAIL] 502 115ms https://api.backed.fi/api/v2/public/assets/MTGx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.STAGx` [FAIL] 502 125ms https://api.backed.fi/api/v2/public/assets/STAGx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.circ.FNBx` [FAIL] 502 112ms https://api.backed.fi/api/v2/public/assets/FNBx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.BYDx` [FAIL] 502 122ms https://api.backed.fi/api/v2/public/assets/BYDx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.LYFTx` [FAIL] 502 115ms https://api.backed.fi/api/v2/public/assets/LYFTx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.CACCx` [FAIL] 502 125ms https://api.backed.fi/api/v2/public/assets/CACCx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.MBGLx` [FAIL] 502 109ms https://api.backed.fi/api/v2/public/assets/MBGLx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.STAGx` [FAIL] 502 132ms https://api.backed.fi/api/v2/public/assets/STAGx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.circ.CACCx` [FAIL] 502 124ms https://api.backed.fi/api/v2/public/assets/CACCx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.FNBx` [FAIL] 502 137ms https://api.backed.fi/api/v2/public/assets/FNBx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.MBGLx` [FAIL] 502 138ms https://api.backed.fi/api/v2/public/assets/MBGLx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.mult.CACCx` [FAIL] 502 134ms https://api.backed.fi/api/v2/public/assets/CACCx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `xstocks.price.SHCx` [FAIL] 502 10597ms https://api.backed.fi/api/v2/public/assets/SHCx/price-data — HTTP 502 Bad Gateway
- `xstocks.circ.SHCx` [FAIL] 502 127ms https://api.backed.fi/api/v2/public/assets/SHCx/circulating-supply?format=object — HTTP 502 Bad Gateway
- `xstocks.mult.SHCx` [FAIL] 502 124ms https://api.backed.fi/api/v2/public/assets/SHCx/multiplier?network=Solana — HTTP 502 Bad Gateway
- `llama.protocol.xstocks` [ok] 200 589ms https://api.llama.fi/protocol/xstocks
- `jup.tokens.search.xStock` [ok] 200 288ms https://lite-api.jup.ag/tokens/v2/search?query=xStock
- `jup.tokens.search.FLNCx` [ok] 200 57ms https://lite-api.jup.ag/tokens/v2/search?query=FLNCx
- `jup.tokens.search.QUBTx` [ok] 200 53ms https://lite-api.jup.ag/tokens/v2/search?query=QUBTx
- `jup.tokens.search.PCTx` [ok] 200 53ms https://lite-api.jup.ag/tokens/v2/search?query=PCTx
- `jup.tokens.search.METCx` [ok] 200 50ms https://lite-api.jup.ag/tokens/v2/search?query=METCx
- `jup.tokens.search.WYFIx` [ok] 200 63ms https://lite-api.jup.ag/tokens/v2/search?query=WYFIx
- `jup.tokens.search.INDIx` [ok] 200 52ms https://lite-api.jup.ag/tokens/v2/search?query=INDIx
- `jup.tokens.search.XRXx` [ok] 200 50ms https://lite-api.jup.ag/tokens/v2/search?query=XRXx
- `jup.tokens.search.RITMx` [ok] 200 53ms https://lite-api.jup.ag/tokens/v2/search?query=RITMx
- `jito.tip_floor` [ok] 200 150ms https://bundles.jito.wtf/api/v1/bundles/tip_floor
- `dune.public_embed` [ok] 200 237ms https://dune.com/embeds/dashboard/cryptoonchain/solana-explorer
- `simd.0525.raw` [ok] 200 116ms https://raw.githubusercontent.com/solana-foundation/solana-improvement-documents/main/proposals/0525-reduce-slot-times.md
- `rpc.getAccountInfo` [ok] 200 88ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 88ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 244ms https://api.mainnet-beta.solana.com
- `rpc.getAccountInfo` [ok] 200 87ms https://api.mainnet-beta.solana.com
- `jito.daily_mev_rewards` [ok] 200 379ms https://kobe.mainnet.jito.network/api/v1/daily_mev_rewards

---

Borealis 1.5.7 · MIT · author `dustycompiler` · regenerate with `python3 generate.py`
