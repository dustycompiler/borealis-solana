# Borealis build notes

Written 2026-08-25 15:21 PT (2026-08-25 22:21 UTC) after a live `python3 generate.py` run against public endpoints. Author: dustycompiler. No GitHub repo was created and nothing was submitted to Superteam.

## How to run

Python 3.9+ (this box: 3.13.5). Stdlib only. No `pip install`, no API keys.

```bash
cd borealis-solana
python3 generate.py
```

Writes `out/index.html`, `out/report.md`, `out/report.json`, then copies those three files to `docs/` for GitHub Pages. Appends one row to `data/history.jsonl`.

Optional flags: `--out`, `--docs`, `--history`. Cron sample: `crontab.example`. GitHub Action: `.github/workflows/update.yml` (commits as dustycompiler; enable Actions yourself).

Open `out/index.html` in a browser, or point Pages at `/docs`.

## What works (this live run)

23 of 24 fetches succeeded. Sample snapshot:

| Metric | Live value | Source |
| --- | --- | --- |
| RPC health | ok | `getHealth` on api.mainnet-beta.solana.com |
| Slot / height | 441,727,561-class / 419,776,193-class | `getSlot` + `getEpochInfo` |
| Epoch | 1022, ~51.7% | `getEpochInfo` |
| Mean TPS / non-vote TPS | ~4,083 / ~2,212 | derived from `getRecentPerformanceSamples(60)` |
| Mean slot time | ~365 ms | same samples |
| Vote accounts | 686 active, 9 delinquent | `getVoteAccounts` |
| Activated stake | ~435.0M SOL | same |
| Nakamoto 33/50/67 | 18 / 41 / 79 | derived |
| Solana DeFi TVL | ~$5.63B | DeFiLlama `/v2/chains` |
| DEX 24h | ~$3.00B | DeFiLlama `/overview/dexs/Solana` |
| Fees 24h | ~$14.5M | DeFiLlama `/overview/fees/Solana` |
| Stablecoin circulating (pegged-USD) | ~$15.85B | stablecoins.llama.fi |
| RWA protocol TVL on Solana | ~$2.06B (26 protocols) | DeFiLlama `/protocols` category RWA / RWA Lending |
| Daily active addresses | Allium 749,721 on 2026-08-24; vendor range 361,127–854,284 | `solana.com/api/databricks/data?days=30` |
| SOL/USD | $97.63 | DeFiLlama coins `coingecko:solana` **fallback** (see below) |
| Status | All Systems Operational | status.solana.com/api/v2/summary.json |
| News | 18 RSS/Atom items | status atom + solana.com/news/rss.xml + medium.com/feed/anza-xyz |

RPC fallback `https://solana-rpc.publicnode.com` was **not needed** this run (primary answered every method). `getSupply` is the slow call (~7s).

`solana.com/data` HTML is fetchable but client-rendered. The useful public JSON is:

- `https://solana.com/api/databricks/data?days=30` (network/vendor metrics, including DAA)
- `https://solana.com/api/rpc/data` (public RPC latency / error rate)

Anomaly detector ran. Zero flags this run: TPS and slot time were inside the last-hour sample band, delinquent stake 0.023%, TVL 1d +1.2% (7d +16% is under the 20% 7-day threshold), status operational. Quiet is the correct result.

## What failed / was omitted

**CoinGecko public API** (`api.coingecko.com/api/v3/simple/price?ids=solana`) returned **HTTP 429** on every attempt from this IP, with `Retry-After` of 20–50s. Borealis does not invent a price. It then called `https://coins.llama.fi/prices/current/coingecko:solana` (public, no key) and labeled the tile `defillama-coins (coingecko:solana id; CoinGecko public API 429)`. 24h change / market cap / volume from CoinGecko are therefore blank this snapshot. `omissions[]` records that. If Llama coins also failed, the next fallback is the dated `solana.com/data` SOL Price vendor series.

**DeFiLlama Pro `/rwa/*` endpoints** require a key. Not used. RWA is the public protocol-TVL rollup described above, labeled as such.

**Daily active addresses** from Flipside/Dune/Allium APIs need keys. Not used. DAA comes from the public solana.com/data databricks JSON, with the vendor spread shown instead of a fake average.

No Twitter API (by design).

## Editorial name check

Bounty brief said “Alpenglow / SIMD-025”. Current public docs:

- **Alpenglow consensus = SIMD-0326 (Votor)**, plus SIMD-0337 / 0357 / 0384 / 0387
- **SIMD-0256** (2025) is a 50M→60M block CU limit, not consensus

The Overview editorial is dated 2026-08-25 and sourced to solana.com/upgrades/alpenglow and the SIMD repo. VAT (0357) and BLS (0387) mainnet activations in July 2026 are noted. Agave 4.3 / ~28 Sep 2026 is marked tentative.

## Integrity

Every fetch is in `out/report.json` → `sources[]` (URL, HTTP status, bytes, ms, UTC). Failed tiles are dashed. MIT license, author `dustycompiler`, no personal names.
