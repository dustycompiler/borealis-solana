# Borealis 1.5.4 — official Superteam rubric

Scored 2026-08-27 **09:45 PT** against the 1.5.4 ship
(`meta.version` **1.5.4**). Not a judge ranking. Do not inflate.

Official listing criteria only (earn.superteam.fun, listing token SIMD-525). Scale 0.0–5.0.
If uncertain, score lower. A 5.0 would survive a hostile grep with no remaining P0/P1.

| Criterion | Score / 5 | Why | What prevents 5.0 |
|---|---:|---|---|
| Comprehensiveness | 4.8 | Same coverage as 1.5.3 (REV calendar-day, Jupiter xStocks subset volume, fees sample, incinerator, DAA) plus **on-chain SIMD-0525 Feature-gate labels** instead of inferred slot-ms. Changelog 2026-08-20 is the first-party 350 ms quote. | REV is a UTC **calendar day**, not rolling 24h. xStocks mcap is 80 of 715. Volume is a Jupiter subset. 7d equity volume does not exist no-key. Dune is an external embed. |
| Automation & Maintainability | 4.2 | Still one command, stdlib-only, no secrets, `workflow_dispatch` kept. **Honesty patch:** copy no longer claims 15-minute updates; **STALE banner when `generated_at` age > 2 hours**. | GitHub `*/15` cron drifted to ~2h on Aug 26 then went **silent ~26h**. STALE banner is honesty, not reliability. CoinGecko/Jupiter 429 from shared IPs is standing. |
| Clarity & Presentation | 4.8 | SIMD stages render as `live` / `activated-not-yet-effective` / `pending`. STALE banner is explicit. HEALTHY + CONTRACTION no longer paints DEX −19.9% as Biggest risk. | Headline confidence cannot be HIGH while xStocks mcap is 80/715. Charts mix a short local tape with upstream 30d/90d — labeled. |
| Innovation | 4.7 | Feature-account decode (Option&lt;u64&gt; activated_slot → effective epoch + 1) on public RPC, zero keys. Network-vs-ecosystem classifier. Keyless Jito daily MEV + same-day SOL-USD for REV. | Rule-based intelligence. No original Dune query. |
| Technical Implementation | 4.8 | Stdlib unittests cover gate labels at epoch 1023 (350 live, 300 not-yet-effective, 250/200 pending), epoch 1024 → 300 live, observed 367 ms is **not** gate proof, STALE threshold, HEALTHY+CONTRACTION risk None. | Full generate.py is network-bound; e2e is fixture-backed. |
| Originality | 4.8 | First-party generator. Pulse still labels Llama app fees as REV — Borealis does not. Gate labels are Feature accounts, not a copied upgrades-page “still 400ms”. Dune iframe is External Reference. | Third-party Dune dashboard remains on Sources. |

Mean: **4.68 / 5**. Category below 4.5: **Automation & Maintainability (4.2)** — the 15-minute claim was false; GitHub cron is not a clock.

## This cycle vs 1.5.3

1.5.3 claimed “updates every 15 min” while Actions drifted then went silent, and labeled 350 ms `consistent-with-observed` from ~367 ms slot time. 1.5.4 stops both leaks: honest cadence + STALE banner; SIMD labels from `getAccountInfo` Feature accounts (changelog quote for 350 ms live). Observed slot remains corroboration only.

## External blockers (not laziness)

1. **GitHub hosted cron** — cannot guarantee a 15-minute tick. Do not add a second in-repo cron we already know is dead.
2. **solana.com Fees lag** — REV is the latest common complete UTC day, not rolling 24h.
3. **xStocks HTTP budget** — 715 catalog names; priced subset is a labeled lower bound.
4. **Dune API** — 401 without a key. Core stays zero-key. Did not invent MEV/REV/volume to close SolVitals gaps.
