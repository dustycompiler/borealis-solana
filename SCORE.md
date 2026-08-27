# Borealis 1.5.5 — official Superteam rubric

Scored 2026-08-27 **11:20 PT** against the 1.5.5 ship
(`meta.version` **1.5.5**). Not a judge ranking. Do not inflate.

Official listing criteria only (earn.superteam.fun, listing token SIMD-525). Scale 0.0–5.0.
If uncertain, score lower. A 5.0 would survive a hostile grep with no remaining P0/P1.

| Criterion | Score / 5 | Why | What prevents 5.0 |
|---|---:|---|---|
| Comprehensiveness | 4.8 | Same coverage as 1.5.4 (REV calendar-day, Jupiter xStocks subset volume, fees sample, incinerator, DAA, Feature-gate SIMD labels). Live pulse is cluster slot/epoch/TPS only — not a second census. | REV is a UTC **calendar day**, not rolling 24h. xStocks mcap is 80 of 715. Volume is a Jupiter subset. 7d equity volume does not exist no-key. Dune is an external embed. |
| Automation & Maintainability | 4.4 | One command, stdlib-only, no secrets, `workflow_dispatch` kept. **On-page LIVE pulse** (browser JSON-RPC to publicnode, mainnet-beta fallback, at most every 60s) is the automation answer to GitHub cron unreliability: the comprehensive snapshot can sit idle; judges still see current cluster time. STALE banner remains for `generated_at` age > 2 hours. No new in-repo cron. | GitHub `*/15` cron still is not a clock for the full snapshot. Pulse is cluster-only (slot/epoch/TPS), not REV/DEX/xStocks. CoinGecko/Jupiter 429 from shared IPs is standing. |
| Clarity & Presentation | 4.8 | LIVE / on-page-now vs snapshot `generated_at`. RPC fail → last snapshot values, **NOT LIVE**, never invented. SIMD stages still `live` / `activated-not-yet-effective` / `pending`. STALE banner explicit. | Headline confidence cannot be HIGH while xStocks mcap is 80/715. Charts mix a short local tape with upstream 30d/90d — labeled. |
| Innovation | 4.7 | Same as 1.5.4 (Feature-account decode, network-vs-ecosystem classifier, keyless Jito daily MEV). Pulse is a small CORS-aware reuse of existing public RPC, not a new oracle. | Rule-based intelligence. No original Dune query. |
| Technical Implementation | 4.8 | Stdlib unittests cover gate labels at epoch 1023 (350 live, 300 not-yet-effective, 250/200 pending), epoch 1024 → 300 live, observed 367 ms is **not** gate proof, STALE threshold, HEALTHY+CONTRACTION risk None, live-pulse HTML/RPC fallbacks. | Full generate.py is network-bound; e2e is fixture-backed. Browser CORS: mainnet-beta 403s GitHub Pages Origin, so pulse tries publicnode first. |
| Originality | 4.8 | First-party generator. Pulse still labels Llama app fees as REV — Borealis does not. Gate labels are Feature accounts, not a copied upgrades-page “still 400ms”. Dune iframe is External Reference. | Third-party Dune dashboard remains on Sources. |

Mean: **4.72 / 5**. Category below 4.5: **Automation & Maintainability (4.4)** — GitHub cron is still not a clock for the comprehensive snapshot; the live pulse only keeps cluster time honest.

## This cycle vs 1.5.4

1.5.4 stopped claiming 15-minute GitHub ticks and labeled SIMD from Feature accounts. 1.5.5 keeps both, and adds a judged-visible **on-page LIVE pulse** so cluster slot/epoch/TPS stay current when Actions is idle. No second cron. Observed slot ms is still not gate proof.

Ship-time chain check (epoch **1023**): 350 **live**, 300 **activated-not-yet-effective** (effective epoch 1024), 250/200 **pending**.

## External blockers (not laziness)

1. **GitHub hosted cron** — cannot guarantee a 15-minute tick. Do not add a second in-repo cron we already know is dead. The page itself pulses instead.
2. **solana.com Fees lag** — REV is the latest common complete UTC day, not rolling 24h.
3. **xStocks HTTP budget** — 715 catalog names; priced subset is a labeled lower bound.
4. **Dune API** — 401 without a key. Core stays zero-key. Did not invent MEV/REV/volume to close SolVitals gaps.
5. **Browser RPC** — `api.mainnet-beta.solana.com` 403s the GitHub Pages Origin; pulse uses `solana-rpc.publicnode.com` first (CORS *), same two keyless endpoints as generate.py.
