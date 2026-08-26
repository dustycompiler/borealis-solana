# Borealis 1.5.1 — official Superteam rubric

Scored 2026-08-25 **20:56 PT** against the 1.5.1 snapshot
(`meta.version` **1.5.1**, `generated_at_utc` **2026-08-26T03:56:06Z**). Not a judge ranking. Do not inflate.

Official listing criteria only (earn.superteam.fun, listing token SIMD-525). Scale 0.0–5.0.
If uncertain, score lower. A 5.0 would survive a hostile grep with no remaining P0/P1.

| Criterion | Score / 5 | Why | What prevents 5.0 |
|---|---:|---|---|
| Comprehensiveness | 4.8 | Live page covers TPS, slot, height, epoch, active/delinquent validators, stake, commissions, delinquency alerts, news + public X/Nitter RSS, SOL 24h, stables, DEX (24h and 7d totals with correct Llama semantics), **measured Solana REV on the latest common complete UTC day** (in-protocol fees + gross Jito MEV `jito_tips + validator_tips`), median tx fee (stratified getBlock, labeled not a census), tokenized-equity **volume** (Jupiter xStocks subset), DAA (Allium via solana.com/data), Alpenglow SIMD-0326, SIMD-525, anomalies, HTML+MD+JSON, 15-min Action, live demo. This run: **$1.06M REV, UTC 2026-08-24** ($889k fees + $173k Jito). | REV is a UTC **calendar day**, not rolling 24h; solana.com Fees can lag so the common day may be T-2. xStocks mcap is 80 of 715 names. 7d equity volume does not exist on no-key Jupiter/Llama. Dune is an external embed, not a Borealis query. |
| Automation & Maintainability | 4.8 | `python3 generate.py`, stdlib-only, no secrets. GitHub Actions every 15 minutes (tests.yml then update). Pages tracks main. Failure of CoinGecko 429 is expected-unavailable, not a crash. | GitHub cron drifts; do not claim hard realtime. CoinGecko 429 from shared IPs is a standing external. Screenshot step is best-effort Chrome. |
| Clarity & Presentation | 4.8 | 30-second hero: Network Health separate from Ecosystem Activity. Solana REV tile shows **$1.06M · UTC calendar day 2026-08-24**, not a ghost "incomplete". DEX line labels Llama `change_7d` as 24h vs 24h from 7d ago. Multipliers are live `?network=Solana`. | Headline confidence is **MED** (CoinGecko 429 → Coinbase) and cannot be HIGH while xStocks mcap is 80/715. Charts still mix a short local tape with upstream 30d/90d — labeled, but easy to misread. |
| Innovation | 4.7 | Network-vs-ecosystem classifier; biggest-risk bound to the same model; evidence-linked insights; source provenance; live xStocks currentMultiplier (capital-S `network=Solana`); **public no-key Jito daily MEV tape** (`kobe.mainnet.jito.network/api/v1/daily_mev_rewards`) with explicit 5%/95% component accounting instead of a fake tip-floor product. | Intelligence is rule-based, not a deep multi-source causal model. No original Dune query (API is 401 without a key). |
| Technical Implementation | 4.8 | 49 stdlib unittests (gross = jito+validator, skip incomplete today, refuse mixed dates, Llama and tip-floor excluded from REV, WATCH+delinquency is the risk, multiplier route fetched, DEX labels). RPC 429→publicnode. Escaping of feed text. `write_outputs` is the HTML/MD/JSON sink. | Full generate.py is still network-bound; e2e is fixture-backed via `write_outputs`, not a recorded RPC cassette of every source. JSON schema_version is not a separate product field. |
| Originality | 4.8 | First-party generator, not a restyle of Orbit/Pulse/Heliostat. Pulse still labels Llama app fees as REV — Borealis does not. Dune iframe is labeled public embed, not our query. README states the SolPulse *idea* inspiration. | Third-party Dune dashboard is still on the Sources tab; must stay External Reference. |

Mean: **4.78 / 5**. Categories below 4.5: **none**.

## External blockers (not laziness)

1. **solana.com Fees lag** — this run aligned to UTC 2026-08-24 even though Jito already published a complete 2026-08-25 row. Mixing those dates is forbidden. Label the day.
2. **xStocks HTTP budget** — 715 unique catalog names with a Solana mint; pricing 80 is a labeled lower bound.
3. **Dune API** — results/CSV 401 without a key. Core architecture stays zero-key.

## This cycle vs 1.5.0

1.5.0 refused a REV product because only `tip_floor` was wired. 1.5.1 uses Jito's public daily MEV tape. Gross user-paid tips = `jito_tips + validator_tips` (empirically 5% + 95%). Today's incomplete Jito row is skipped. Llama `/overview/fees/Solana` stays excluded. Tip-floor × nvTPS × 86400 stays `jito_runrate_not_rev` with `included_in_headline=false`.
