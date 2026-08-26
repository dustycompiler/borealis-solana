# Borealis 1.5.2 — official Superteam rubric

Scored 2026-08-25 **21:29 PT** against the 1.5.2 snapshot
(`meta.version` **1.5.2**, `generated_at_utc` **2026-08-26T04:29:36Z**). Not a judge ranking. Do not inflate.

Official listing criteria only (earn.superteam.fun, listing token SIMD-525). Scale 0.0–5.0.
If uncertain, score lower. A 5.0 would survive a hostile grep with no remaining P0/P1.

| Criterion | Score / 5 | Why | What prevents 5.0 |
|---|---:|---|---|
| Comprehensiveness | 4.8 | Same coverage as 1.5.1 plus **REV USD on the same UTC day as the SOL legs**. This run: **10,941.3 SOL / $1.05M, UTC 2026-08-24**, SOL-USD **$96.18** from `solana.com/data` SOL Price (DexPaprika) that day — not the $97.07 snapshot. Gross Jito = `jito_tips + validator_tips` (Jito-paid/retained vs validator-distributed). | REV is a UTC **calendar day**, not rolling 24h; Fees can lag to T-2. xStocks mcap is 80 of 715. 7d equity volume does not exist no-key. Dune is an external embed. |
| Automation & Maintainability | 4.8 | `python3 generate.py`, stdlib-only, no secrets. GitHub Actions every 15 minutes. Pages tracks main. CoinGecko 429 is expected-unavailable. | GitHub cron drifts. CoinGecko 429 from shared IPs is standing. Screenshot step is best-effort Chrome. |
| Clarity & Presentation | 4.8 | Tile: **$1.05M · 10,941.3 SOL · UTC 2026-08-24 · SOL-USD 96.18 on 2026-08-24**. Spot equivalent at run price is labeled not-headline. Network Health separate from Ecosystem Activity. | Headline confidence cannot be HIGH while xStocks mcap is 80/715. Charts mix a short local tape with upstream 30d/90d — labeled. |
| Innovation | 4.7 | Network-vs-ecosystem classifier; live xStocks `currentMultiplier`; public no-key Jito daily MEV tape; same-day SOL-USD for REV; refuses a TipRouter fee-rate story the API does not prove. | Rule-based intelligence. No original Dune query. |
| Technical Implementation | 4.8 | 51 stdlib unittests including **REV USD price date equals `rev_utc_day`**, snapshot price rejected, skip incomplete today, refuse mixed dates, Llama and tip-floor excluded. | Full generate.py is network-bound; e2e is fixture-backed. |
| Originality | 4.8 | First-party generator. Pulse still labels Llama app fees as REV — Borealis does not. Dune iframe is External Reference. | Third-party Dune dashboard remains on Sources. |

Mean: **4.78 / 5**. Categories below 4.5: **none**.

## External blockers (not laziness)

1. **solana.com Fees lag** — this run aligned to UTC 2026-08-24 even though Jito had a complete 2026-08-25 row.
2. **xStocks HTTP budget** — 715 catalog names; 80 priced is a labeled lower bound.
3. **Dune API** — 401 without a key. Core stays zero-key.

## This cycle vs 1.5.1

1.5.1 converted Aug-24 SOL REV with the live snapshot (~$97). 1.5.2 uses that UTC day's `solana.com/data` SOL Price (DexPaprika $96.18 here). Headline SOL total is first-class. Spot equivalent is separate. Jito field copy is neutral: no "~5% TipRouter protocol fee" claim.
