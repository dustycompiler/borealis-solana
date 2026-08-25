# Borealis

Live Solana cluster & ecosystem report. One command, **no API keys**, Python stdlib only (`urllib`).

```bash
python3 generate.py
```

Writes:

| Path | What |
| --- | --- |
| `out/index.html` | Interactive dark dashboard (self-contained) |
| `out/report.md` | Human-readable report |
| `out/report.json` | Structured metrics + per-source timestamps |
| `docs/` | Static copy of the three files, ready for GitHub Pages |

Author: **hardest-worker**. License: MIT. No personal names in the repo.

This is an original build for Superteam Canada's auto-updating Solana report bounty. Inspired by the *idea* of a live pulse dashboard — not a clone of any existing codebase.

---

## Run

Requires Python 3.9+ (3.12/3.13 fine). No `pip install`.

```bash
git clone <this-repo>
cd canada-dashboard
python3 generate.py
```

Open `out/index.html` locally, or serve `docs/` however you host static files.

Flags:

```
python3 generate.py --out out --docs docs --history data/history.jsonl
```

Each run **appends** a compact row to `data/history.jsonl` so later runs can flag TPS/price vs a rolling cross-run baseline. The first run uses in-window RPC samples + DeFiLlama daily history only.

---

## What is measured

Live JSON-RPC against `https://api.mainnet-beta.solana.com`, falling back to `https://solana-rpc.publicnode.com` on HTTP 429 / 5xx / parse errors.

| Call | Used for |
| --- | --- |
| `getHealth` | Cluster health pill |
| `getSlot` + `getBlockTime` | Slot, block timestamp |
| `getEpochInfo` | Epoch, slot index, block height, epoch % |
| `getRecentPerformanceSamples(60)` | TPS, non-vote TPS, slot time |
| `getVoteAccounts` | Active vs delinquent, stake, commission, lag |
| `getSupply` | Circulating / total SOL |

**Derived (not fetched as a named RPC field):**

- TPS = `numTransactions / samplePeriodSecs`
- Non-vote TPS = `numNonVoteTransactions / samplePeriodSecs`
- Slot time = `samplePeriodSecs / numSlots`
- Nakamoto coefficient = fewest current validators whose activated stake exceeds 33% / 50% / 67%
- Lag slots = `getSlot − lastVote`

### Market & DeFi (no keys)

- **CoinGecko** `simple/price?ids=solana` — SOL/USD, 24h change, market cap, 24h volume. Honors `Retry-After` on 429. If CoinGecko still 429s, Borealis falls back to `coins.llama.fi/prices/current/coingecko:solana`, then to `solana.com/data` SOL Price, and **labels the source**. It never invents a price.
- **DeFiLlama** ` /v2/chains`, `/v2/historicalChainTvl/Solana`, `/overview/dexs/Solana`, `/overview/fees/Solana`, `/protocols`
- **stablecoins.llama.fi** chain circulating + per-asset Solana supply + 90-day chart
- **RWA** = sum of `chainTvls.Solana` for protocols whose DeFiLlama category is `RWA` or `RWA Lending`. The dedicated `/rwa/*` Llama routes are Pro-only; this rollup is the public substitute and is labeled as such.

### solana.com/data

The marketing page is a client-rendered Next app. The **same dashboard is backed by public JSON**:

- `https://solana.com/api/databricks/data?days=30` — Active Addresses, SOL price vendor series, DEX volume, fees, …
- `https://solana.com/api/rpc/data` — public RPC latency / error rate by provider

**Daily active addresses** are taken from that databricks feed (headline = Allium, plus the min–max across vendors). Vendor series disagree; Borealis does **not** average them.

### News (no Twitter)

- `https://status.solana.com/api/v2/summary.json`
- `https://status.solana.com/history.atom`
- `https://solana.com/news/rss.xml`
- `https://medium.com/feed/anza-xyz`

---

## Anomaly detection

Shown on the HTML strip, in `report.md`, and as `anomalies[]` in `report.json`.

| Flag | Window | Threshold |
| --- | --- | --- |
| `tps_spike` | 60 × ~60s performance samples | mean > median + 2.5σ **and** > 1.35× median |
| `tps_drop` | same | mean < 0.55× median, or < median − 2.5σ and < 0.75× median |
| `slow_slots` | same | mean > 0.60s, max > 0.80s, or mean > 1.5× median |
| `high_delinquency` | `getVoteAccounts` | delinquent stake ≥ 1% **or** count ≥ 25 |
| `tvl_move_1d` / `_7d` | DeFiLlama daily TVL | \|1d\| ≥ 8% or \|7d\| ≥ 20% |
| `sol_price_move` | CoinGecko 24h | \|24h\| ≥ 8% |
| `rpc_unhealthy` | `getHealth` | not `ok` |
| `status_degraded` | status.solana.com | indicator not `none` |
| `tps_vs_run_history` | `data/history.jsonl` (n ≥ 8) | outside 3σ of prior snapshots |
| `sol_price_vs_last_run` | history n ≥ 5 | ≥ 8% vs last snapshot |

A quiet hour produces **zero** flags. That is success, not a missing feature.

---

## Editorial: Alpenglow / SIMD numbering

The bounty brief mentioned “Alpenglow / SIMD-025”. **Current public documents name the consensus rewrite Alpenglow, specified as SIMD-0326.** SIMD-0256 (2025) raised the block compute-unit limit 50M → 60M and is a different proposal.

The Overview tab carries a dated, sourced editorial (VAT / BLS activation dates, Agave 4.3 window). It is **not** a live metric. See `editorial` in `report.json`.

---

## Automation

### cron

See `crontab.example`. Hourly is enough; public RPC does not want a tight loop.

### GitHub Action

`.github/workflows/update.yml` runs `python3 generate.py` on an hourly schedule and on `workflow_dispatch`, then commits `out/`, `docs/`, and `data/history.jsonl` as **hardest-worker**. Enable Actions on the repo. No secrets required.

### GitHub Pages

Settings → Pages → Deploy from branch → `/docs`. After the first successful Action run (or a local `generate.py`), `docs/index.html` is the dashboard. `docs/.nojekyll` is included so GitHub does not run Jekyll on the snapshot.

---

## Integrity rules

- No API keys, no scraping of authenticated dashboards.
- If a source 429s or 5xxs after retries, the tile is omitted and `omissions[]` explains why.
- Every fetch is logged in `report.json` → `sources[]` with URL, HTTP status, bytes, milliseconds, UTC timestamp.
- User-Agent: `BorealisReport/1.0 (Solana ecosystem dashboard; stdlib urllib; no API key)`.

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
