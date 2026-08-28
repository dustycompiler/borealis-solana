# Borealis 1.5.6 — official Superteam rubric

Scored 2026-08-27 **18:13 PT** against the 1.5.6 ship
(`meta.version` **1.5.6**). Not a judge ranking. Do not inflate.

Official listing criteria only (earn.superteam.fun, listing token SIMD-525). Scale 0.0–5.0.
If uncertain, score lower. A 5.0 would survive a hostile grep with no remaining P0/P1.

| Criterion | Score / 5 | Why | What prevents 5.0 |
|---|---:|---|---|
| Comprehensiveness | 4.8 | Same coverage as 1.5.5. In-protocol fee USD now uses the same UTC-day SOL-USD as REV (not a new metric). Live pulse is still cluster slot/epoch/TPS only. | REV is a UTC **calendar day**, not rolling 24h. xStocks mcap is 80 of 715. Volume is a Jupiter subset. 7d equity volume does not exist no-key. Dune is an external embed. |
| Automation & Maintainability | 4.4 | Unchanged: one command, stdlib-only, no secrets, `workflow_dispatch` kept. On-page LIVE pulse (browser JSON-RPC, ≤60s) plus STALE banner if snapshot age > 2 hours. No new in-repo cron. This patch does not add a snapshot cadence. | GitHub `*/15` cron still is not a clock for the full snapshot. Pulse is cluster-only (slot/epoch/TPS), not REV/DEX/xStocks. CoinGecko/Jupiter 429 from shared IPs is standing. |
| Clarity & Presentation | 4.8 | Fee tile now labels the UTC-day SOL-USD next to REV's. LIVE / on-page-now vs snapshot `generated_at`. RPC fail → last snapshot values, **NOT LIVE**, never invented. SIMD stages still `live` / `activated-not-yet-effective` / `pending`. STALE banner explicit. | Headline confidence cannot be HIGH while xStocks mcap is 80/715. Charts mix a short local tape with upstream 30d/90d — labeled. |
| Innovation | 4.7 | Same as 1.5.5. This is a consistency fix, not a new oracle. | Rule-based intelligence. No original Dune query. |
| Technical Implementation | 4.8 | Stdlib tests now pin `network_fees_usd_24h` to the fee UTC day's solana.com/data SOL Price (rejects live/spot when that series exists; falls back only if the day is missing). Gate-label and STALE tests unchanged. | Full generate.py is network-bound; e2e is fixture-backed. Browser CORS: mainnet-beta 403s GitHub Pages Origin, so pulse tries publicnode first. 1.5.5 shipped a real FX inconsistency; closing it is the job, not extra credit. |
| Originality | 4.8 | First-party generator. Pulse still labels Llama app fees as REV — Borealis does not. Gate labels are Feature accounts, not a copied upgrades-page “still 400ms”. Dune iframe is External Reference. | Third-party Dune dashboard remains on Sources. |

Mean: **4.72 / 5**. Category below 4.5: **Automation & Maintainability (4.4)** — GitHub cron is still not a clock for the comprehensive snapshot; the live pulse only keeps cluster time honest. Scores are not raised for a bugfix.

## This cycle vs 1.5.5

1.5.5's `network_fees_usd_24h` converted the UTC-day Allium fee SOL total at the **live snapshot** SOL-USD while headline REV used that day's solana.com/data SOL Price. Same SOL quantity, two USD numbers. Superteam can ding that. 1.5.6 uses the same UTC-day FX for in-protocol fee USD as the rest of the REV stack. Spot remains labeled on `rev_spot_usd` only. Not a new snapshot cadence. STALE banner + live pulse unchanged. No Superteam Earn reopen. No withdraw.

## External blockers (not laziness)

1. **GitHub hosted cron** — cannot guarantee a 15-minute tick. Do not add a second in-repo cron we already know is dead. The page itself pulses instead.
2. **solana.com Fees lag** — REV is the latest common complete UTC day, not rolling 24h.
3. **xStocks HTTP budget** — 715 catalog names; priced subset is a labeled lower bound.
4. **Dune API** — 401 without a key. Core stays zero-key. Did not invent MEV/REV/volume to close SolVitals gaps.
5. **Browser RPC** — `api.mainnet-beta.solana.com` 403s the GitHub Pages Origin; pulse uses `solana-rpc.publicnode.com` first (CORS *), same two keyless endpoints as generate.py.
