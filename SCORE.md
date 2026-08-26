# Borealis 1.5.3 — official Superteam rubric

Scored 2026-08-25 **21:50 PT** against the 1.5.3 snapshot
(`meta.version` **1.5.3**, `generated_at_utc` **2026-08-26T04:48:50Z**). Not a judge ranking. Do not inflate.

Official listing criteria only (earn.superteam.fun, listing token SIMD-525). Scale 0.0–5.0.
If uncertain, score lower. A 5.0 would survive a hostile grep with no remaining P0/P1.

| Criterion | Score / 5 | Why | What prevents 5.0 |
|---|---:|---|---|
| Comprehensiveness | 4.8 | Same coverage as 1.5.2 plus **numeric tokenized-equity 24h volume**. This run: **$22.31M** Jupiter `stats24h` subset (query=`xStock` first, 8 priced-symbol misses throttled at ≤0.5 RPS, not a 25-call burst). REV still **10,941.3 SOL / $1.05M, UTC 2026-08-24**, SOL-USD **$96.18** DexPaprika that day. | REV is a UTC **calendar day**, not rolling 24h. xStocks mcap is 80 of 715. Volume is a Jupiter subset, not all 715, not all Solana DEX. 7d equity volume does not exist no-key. Dune is an external embed. |
| Automation & Maintainability | 4.8 | `python3 generate.py`, stdlib-only, no secrets. GitHub Actions every 15 minutes. Pages tracks main. Jupiter 429 uses Retry-After/backoff + committed last-known-good cache (STALE ≤24h, never presented as current). | GitHub cron drifts. CoinGecko/Jupiter 429 from shared IPs is standing. Screenshot step is best-effort Chrome. |
| Clarity & Presentation | 4.8 | xStocks vol tile **$22.31M** (MED). STALE path would show the number plus `STALE · last successful X ago` at LOW, not a ghost em dash. REV tile unchanged: **$1.05M · 10,941.3 SOL · UTC 2026-08-24 · SOL-USD 96.18**. | Headline confidence cannot be HIGH while xStocks mcap is 80/715. Charts mix a short local tape with upstream 30d/90d — labeled. |
| Innovation | 4.7 | Network-vs-ecosystem classifier; live xStocks `currentMultiplier`; public no-key Jito daily MEV tape; same-day SOL-USD for REV; keyless Jupiter volume that degrades to labeled STALE instead of bursting the 0.5 RPS cap. | Rule-based intelligence. No original Dune query. |
| Technical Implementation | 4.8 | 57 stdlib unittests including broad xStock skips per-symbol burst, Retry-After bound, rate limiter ≤0.5 RPS, valid cache → STALE, expired cache → unavailable, fresh fetch replaces cache. REV USD price-date tests still pass. | Full generate.py is network-bound; e2e is fixture-backed. |
| Originality | 4.8 | First-party generator. Pulse still labels Llama app fees as REV — Borealis does not. Dune iframe is External Reference. | Third-party Dune dashboard remains on Sources. |

Mean: **4.78 / 5**. Categories below 4.5: **none**.

## External blockers (not laziness)

1. **solana.com Fees lag** — this run aligned to UTC 2026-08-24 even though Jito had a complete 2026-08-25 row.
2. **xStocks HTTP budget** — 715 catalog names; 80 priced is a labeled lower bound. Volume is Jupiter-matched subset.
3. **Dune API** — 401 without a key. Core stays zero-key.

## This cycle vs 1.5.2

1.5.2 shipped REV same-day SOL-USD but left tokenized-equity 24h volume `null` after a 25-call Jupiter burst 429'd. 1.5.3 queries `xStock` first, falls back per missing priced symbol only (cap 8), throttles ≤0.5 RPS, and persists `data/xstocks-volume-cache.json`. This run replaced the cache with a **fresh** `$22.31M` at 2026-08-26T04:50:06Z. Comprehensiveness 4.8 is honest only because that number is on the page.
