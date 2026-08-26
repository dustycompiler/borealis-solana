# Borealis 1.5.0 — official Superteam rubric

Scored 2026-08-25 **19:15 PT** against live https://dustycompiler.github.io/borealis-solana/
(`meta.version` **1.5.0**, `generated_at_utc` **2026-08-26T02:13:17Z**, commit **e97fc69** plus
the Action refresh that kept 1.5.0 semantics). Not a judge ranking. Do not inflate.

Official listing criteria only (earn.superteam.fun, listing token SIMD-525). Scale 0.0–5.0.
If uncertain, score lower. A 5.0 would survive a hostile grep with no remaining P0/P1.

| Criterion | Score / 5 | Why | What prevents 5.0 |
|---|---:|---|---|
| Comprehensiveness | 4.7 | Live page covers TPS, slot, height, epoch, active/delinquent validators, stake, commissions, delinquency alerts, news + public X/Nitter RSS, SOL 24h, stables, DEX (24h and 7d totals with correct Llama semantics), **measured** in-protocol fees, median tx fee (stratified getBlock, labeled not a census), tokenized-equity **volume** (Jupiter xStocks subset), DAA (Allium via solana.com/data), Alpenglow SIMD-0326, SIMD-525, anomalies, HTML+MD+JSON, 15-min Action, live demo. | Full REV is **honestly incomplete** (no zero-key 24h Jito tape). xStocks mcap is 80 of 715 names. 7d equity volume does not exist on no-key Jupiter/Llama. Dune is an external embed, not a Borealis query. |
| Automation & Maintainability | 4.8 | `python3 generate.py`, stdlib-only, no secrets. GitHub Actions every 15 minutes (tests.yml then update). Pages tracks main. Failure of CoinGecko 429 is expected-unavailable, not a crash. | GitHub cron drifts; do not claim hard realtime. CoinGecko 429 from shared IPs is a standing external. Screenshot step is best-effort Chrome. |
| Clarity & Presentation | 4.7 | 30-second hero: Network Health separate from Ecosystem Activity. This live run: **HEALTHY** + **SURGE**. DEX line is `24h $2.95B · 1d −2% · vs-7d-ago +60%` (Llama `change_7d` is 24h vs 24h from 7d ago, not 7d-total). Full REV reads **incomplete**. Multipliers are live `?network=Solana`. | JSON version lives under `meta`, not the top-level key a judge might grep first. Charts still mix a short local tape with upstream 30d/90d — labeled, but easy to misread. |
| Innovation | 4.6 | Network-vs-ecosystem classifier; biggest-risk bound to the same model; evidence-linked insights; source provenance; live xStocks currentMultiplier (capital-S `network=Solana`); refusing a fake REV product when the tape does not exist. | Intelligence is rule-based, not a deep multi-source causal model. No original Dune query (API is 401 without a key). |
| Technical Implementation | 4.7 | 41 stdlib unittests (REV product forbidden, WATCH+delinquency is the risk, multiplier route fetched, DEX labels). RPC 429→publicnode. Escaping of feed text. `write_outputs` is the HTML/MD/JSON sink. | Full generate.py is still network-bound; e2e is fixture-backed via `write_outputs`, not a recorded RPC cassette of every source. JSON schema_version is not a separate product field. |
| Originality | 4.8 | First-party generator, not a restyle of Orbit/Pulse/Heliostat. Pulse still labels Llama app fees as REV — Borealis does not. Dune iframe is labeled public embed, not our query. README states the SolPulse *idea* inspiration. | Third-party Dune dashboard is still on the Sources tab; must stay External Reference. |

Mean: **4.72 / 5**. Categories below 4.5: **none**.

## External blockers (not laziness)

1. **24h Jito tip tape** — Blockworks REV = in-protocol fees + actual Jito tips. Public `tip_floor` is a landed *bundle* percentile. Scanning eight tip accounts on public RPC is not a reliable 24h census. Headline stays incomplete.
2. **xStocks HTTP budget** — 715 unique catalog names with a Solana mint; pricing 80 is a labeled lower bound.
3. **Dune API** — results/CSV 401 without a key. Core architecture stays zero-key.

## This cycle vs 1.4.1

Falsified and removed: `tip_floor p50 × non-vote TPS × 86400` as "Borealis REV 24h"; silent multiplier=1.0; WATCH with Biggest risk None; "DEX 7d +60%" as if it were 7d-total vs prior 7d.
