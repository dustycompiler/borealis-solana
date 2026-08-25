# Borealis

Live Solana cluster & ecosystem report. One command, **no API keys**, Python stdlib only (`urllib`).

**Live demo:** https://dustycompiler.github.io/borealis-solana/

**Repo:** https://github.com/dustycompiler/borealis-solana

```bash
python3 generate.py
```

Writes:

| Path | What |
| --- | --- |
| `out/index.html` | Interactive dark dashboard (self-contained) |
| `out/report.md` | Human-readable report |
| `out/report.json` | Structured metrics + per-source timestamps |
| `docs/` | Static copy for GitHub Pages (including `favicon.svg`) |
| `data/history.jsonl` | Rolling baseline used by the anomaly strip |

Author: **dustycompiler**. License: MIT.

Original work for Superteam Canada's auto-updating Solana report bounty. Inspired by the *idea* of a live pulse dashboard — not a clone of any existing codebase (including SolPulse).

---

## Run

Requires Python 3.9+ (3.12/3.13 fine). No `pip install`.

```bash
git clone https://github.com/dustycompiler/borealis-solana
cd borealis-solana
python3 generate.py
```

Open `out/index.html` locally, or the live demo above.

Flags:

```
python3 generate.py --out out --docs docs --history data/history.jsonl
```

Each run **appends** a compact row to `data/history.jsonl` and charts it. The first run already has in-window RPC samples + DeFiLlama daily history, so the anomaly strip is useful immediately.

---

## What is measured

Live JSON-RPC against `https://api.mainnet-beta.solana.com`, falling back to `https://solana-rpc.publicnode.com` on HTTP 429 / 5xx / parse errors.

| Call | Used for |
| --- | --- |
| `getHealth` | Cluster health + health-score RPC term |
| `getSlot` + `getBlockTime` | Slot, block timestamp |
| `getEpochInfo` | Epoch, slot index, block height, epoch % |
| `getRecentPerformanceSamples(60)` | TPS, non-vote TPS, slot time (last sample vs window) |
| `getVoteAccounts` | Active vs delinquent, stake, commission, lag |
| `getSupply` | Circulating / total SOL (also used for derived market cap) |

**Derived (not fetched as a named RPC field):**

- TPS = `numTransactions / samplePeriodSecs`
- Non-vote TPS = `numNonVoteTransactions / samplePeriodSecs`
- Slot time = `samplePeriodSecs / numSlots`
- Nakamoto coefficient = fewest current validators whose activated stake exceeds 33% / 50% / 67%
- Lag slots = `getSlot − lastVote`

### Market & DeFi (no keys)

- **CoinGecko** `simple/price?ids=solana` — tried first with `Retry-After`. Often 429 from shared CI IPs.
- **Coinbase Exchange** `https://api.exchange.coinbase.com/products/SOL-USD/stats` — **primary 24h** on this project: `last`, `open`, `volume`. 24h % = `(last − open) / open`. Quote volume = `last × base volume`. CORS `*` so the page can also tick live in the browser, labeled **browser live vs snapshot**.
- **Kraken** `https://api.kraken.com/0/public/Ticker?pair=SOLUSD` — fallback 24h using last `c[0]` and 24h open `o`.
- **DeFiLlama coins** `coins.llama.fi/prices/current/coingecko:solana` — price-only fill (no 24h). CORS `*`.
- **solana.com/data** SOL Price 30d series — day-over-day 24h only if the tape above has no change. Labeled as DoD, not a rolling 24h.
- **Binance** is not called (HTTP 451 from this network).
- Market cap: CoinGecko when present, otherwise **derived: price × RPC circulating supply**, labeled as such. Never invented.
- **DeFiLlama** `/v2/chains`, `/v2/historicalChainTvl/Solana`, `/overview/dexs/Solana`, `/overview/fees/Solana`, `/protocols`
- **stablecoins.llama.fi** chain circulating + per-asset Solana supply + 90-day chart
- **RWA** = sum of `chainTvls.Solana` for protocols whose DeFiLlama category is `RWA` or `RWA Lending`. Labeled protocol TVL, not a tokenized-equities census (those Llama routes are Pro-only).

**REV** is shown as **DeFiLlama Solana fees 24h (REV proxy)**. Network fees in SOL come from `solana.com/data` Fees (Allium). **Median tx fee is not published** on these public feeds and is not inferred from an average.

### solana.com/data

- `https://solana.com/api/databricks/data?days=30` — Active Addresses, SOL price, fees, tx count, application revenue, …
- `https://solana.com/api/rpc/data` — public RPC latency / error rate by provider

Daily active addresses: headline = Allium, plus the min–max across vendors. Vendor series disagree; Borealis does **not** average them. 30d medians of TPS (tx count / 86400), DAA, and price are used for anomaly flags.

### News / X (no Twitter API key)

Probes live public RSS and keeps what works:

- `xcancel.com/{solana,solana_status,anza_xyz,solana_devs}/rss` (skip whitelist/403)
- Nitter-style `nitter.perennialte.ch/{handle}/rss` as a working public mirror
- `rsshub.app/twitter/user/solana` (often 403 — skipped)
- `status.solana.com/history.atom`, `solana.com/news/rss.xml`, `medium.com/feed/anza-xyz`

Labeled **public X/Nitter-style RSS, not the official Twitter API**. Lightweight keyword tags (`upgrade`, `outage`, `incident`, `mainnet`, `halt`) — not ML.

---

## Health score (0–100)

Shown in the hero. Not a mystery number.

```
25×rpc_ok
+ 30×clamp(1 − max(0, slot_ms − 400)/400, 0, 1)
+ 25×clamp(1 − delinquent_stake_pct/2, 0, 1)
+ 20×clamp(tps / tps_baseline, 0, 1)
```

| Term | Max | Meaning |
| --- | --- | --- |
| `rpc_ok` | 25 | 25 if `getHealth == ok`, or if getHealth 429s but slot + TPS RPC succeeded; 0 if RPC unreachable |
| slot | 30 | 400 ms → 30, 800 ms → 0 (faster than 400 still 30) |
| delinquency | 25 | 0% delinquent stake → 25, 2%+ → 0 |
| TPS | 20 | current mean TPS vs 30d median from solana.com/data `Transaction Count / 86400`; falls back to the in-window sample median |

---

## Anomaly detection

Useful **on run 1** (no history.jsonl required). Empty strip copy:

> No flags vs rolling baseline (N samples / llama 7d). Watching.

| Flag | Window | Threshold |
| --- | --- | --- |
| `tps_last_sigma` / `slot_time_last_sigma` | 60 × ~60s samples | last sample vs window mean, \|z\| ≥ 2.5 |
| `slow_slots_500ms` | same | last or mean slot time > 500 ms |
| `high_delinquency` | `getVoteAccounts` | delinquent stake ≥ 1% **or** count ≥ 25 |
| `tvl_move_1d` / `_7d` | DeFiLlama daily TVL | \|1d\| ≥ 8% or \|7d\| ≥ 20% |
| `dex_move_1d` / `_7d` | DeFiLlama DEX | same |
| `fees_move_1d` / `_7d` | DeFiLlama fees (REV proxy) | same |
| `sol_price_move` | Coinbase/Kraken/CoinGecko 24h | \|24h\| ≥ 8% |
| `tps_vs_30d` / `daa_vs_30d` / `price_vs_30d` | solana.com/data 30d | \|current − median\| / median ≥ 20% |
| `corr_congestion` | multi-source | elevated slot time **and** depressed non-vote TPS **and** fees 1d ≥ 8% |
| `corr_risk_off` | multi-source | SOL 24h < 0 **and** TVL 1d < 0 **and** DEX 1d < 0 |
| `corr_validator_stress` | multi-source | delinquency up **and** lagging vote accounts |
| `rpc_unhealthy` / `status_degraded` | RPC / status.solana.com | not ok |
| `tps_vs_run_history` | `data/history.jsonl` (n ≥ 8) | outside 3σ of prior snapshots |

`history.jsonl` is persisted and charted on the Overview / Anomalies tabs.

---

## Editorial: Alpenglow / SIMD numbering

The bounty brief mentioned “Alpenglow / SIMD-025”. **Current public documents name the consensus rewrite Alpenglow, specified as SIMD-0326.** SIMD-0256 (2025) raised the block compute-unit limit 50M → 60M and is a different proposal.

The Overview tab carries a dated, sourced editorial (VAT / BLS activation dates, Agave 4.3 window). It is **not** a live metric. See `editorial` in `report.json`.

---

## Automation

### GitHub Action (every 15 minutes)

`.github/workflows/update.yml` runs `python3 generate.py` on `*/15 * * * *` and on `workflow_dispatch`, then commits `out/`, `docs/`, and `data/history.jsonl` as **dustycompiler** (`dustycompiler@users.noreply.github.com`). Enable Actions on the repo. No secrets required. GitHub cron can drift by a few minutes.

### GitHub Pages

Settings → Pages → Deploy from branch → `/docs`. `docs/index.html` is the dashboard. `docs/.nojekyll` is included so GitHub does not run Jekyll. Favicon + Open Graph tags ship with the snapshot.

### cron

See `crontab.example` (`*/15 * * * *`).

---

## Integrity rules

- No API keys, no scraping of authenticated dashboards.
- If a source 429s or 5xxs after retries, the tile is omitted and `omissions[]` explains why.
- Every fetch is logged in `report.json` → `sources[]` with URL, HTTP status, bytes, milliseconds, UTC timestamp — including failures.
- User-Agent: `BorealisReport/1.1 (Solana ecosystem dashboard; stdlib urllib; no API key)`.

## Layout

```
generate.py          orchestrator (RPC, HTTP, anomalies, markdown, json)
htmlout.py           dark dashboard renderer (inline CSS/JS, SVG sparklines)
out/                 latest generated artifacts
docs/                GitHub Pages snapshot (copy of out/)
data/history.jsonl   rolling baselines
.github/workflows/update.yml
crontab.example
```
