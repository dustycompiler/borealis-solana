# Official requirement matrix — Borealis 1.5.6

Source: live Superteam Canada listing
https://earn.superteam.fun/listing/develop-solana-ecosystem-auto-updating-report-and-interactive-dashboard
Deadline 2026-09-01T03:59:59Z. Judging: Comprehensiveness, Automation & Maintainability, Clarity & Presentation, Innovation, Technical Implementation, Originality.

Green = implemented as specified. Partial = related metric present, limitation named. No checkbox substitutions.

| Official requirement | Implemented | Exact metric/feature | Source | HTML | MD | JSON | Test | Limitation |
|---|---|---|---|---|---|---|---|---|
| Network TPS | yes | `cluster.tps_total` from getRecentPerformanceSamples | Solana RPC | yes | yes | yes | yes | Vote+nonvote. Non-vote shown separately. |
| Slot time | yes | `cluster.slot_time_sec` | RPC samples | yes | yes | yes | yes | Mean of sample window, not every slot. |
| Block height | yes | `cluster.absolute_slot` / epoch info | getEpochInfo | yes | yes | yes | helper | |
| Epoch progress | yes | epoch, slot index, % | getEpochInfo | yes | yes | yes | helper | |
| Active validators | yes | current vote accounts | getVoteAccounts | yes | yes | yes | helper | |
| Delinquent validators | yes | delinquent list + count | getVoteAccounts | yes | yes | yes | yes | |
| Stake distribution | yes | top by activated stake, Nakamoto 33/50/67 | getVoteAccounts | yes | yes | yes | helper | |
| Top validators by stake | yes | ranked current | getVoteAccounts | yes | yes | yes | helper | |
| Commission tracking | yes | commission on rows | getVoteAccounts | yes | yes | yes | helper | |
| Delinquency alerts | yes | `high_delinquency` flag; WATCH when stake ≥1% | derived | yes | yes | yes | yes | Biggest risk uses the same classifier. |
| Ecosystem news | yes | RSS buckets after recency filter | solana.com/news, status, medium | yes | yes | yes | yes | 2022–2024 status incidents are archive. |
| Twitter/X signals | partial | public Nitter-style RSS, not Twitter API | xcancel / nitter mirrors | yes | yes | yes | recency | Mirrors 403 often; labeled not official API. |
| SOL price movements | yes | last/open 24h % | Coinbase (Gecko 429 → Coinbase) | yes | yes | yes | yes | Gecko 429 expected-unavailable. |
| Stablecoin supply | yes | Solana circulating USD | stablecoins.llama.fi | yes | yes | yes | helper | |
| DEX volume | yes | 24h, 7d total, change_1d, change_7d (24h vs 7d-ago), change_7dover7d | DeFiLlama /overview/dexs/Solana | yes | yes | yes | yes | Labels distinguish change_7d vs 7d-total. |
| Real Economic Value (REV) | yes | Same completed UTC day: in-protocol fees + gross Jito MEV (`jito_tips + validator_tips`); USD at that day's solana.com/data SOL Price; `network_fees_usd_24h` uses the same FX | solana.com/data Fees + SOL Price + kobe.mainnet.jito.network/api/v1/daily_mev_rewards | yes | yes | yes | yes | UTC calendar day, not rolling 24h. Dates never mixed. Today's Jito row skipped. Llama app fees excluded. Tip-floor × TPS is not REV. Split is not a TipRouter fee rate. Fee USD is not live/spot (1.5.6). |
| Median transaction fees | yes | getBlock meta.fee p50, time-stratified ~2–3h | RPC getBlock | yes | yes | yes | yes | Not a 24h census; window_seconds labeled. |
| Tokenized asset volumes (equities) | yes | Jupiter stats24h buy+sell; query=xStock first, per-symbol only for misses, <=0.5 RPS; STALE cache <=24h | lite-api.jup.ag | yes | yes | yes | yes | Subset, not all 715, not all Solana DEX. STALE labeled, never presented as current. |
| Daily active addresses | yes | Allium series via solana.com/data | solana.com/api/databricks | yes | yes | yes | helper | Vendors disagree; not averaged. |
| Alpenglow | yes | SIMD-0326 editorial + status | SIMD docs / solana.com | yes | yes | yes | yes | Not claimed activated from slot time. |
| SIMD-525 | yes | Listing token SIMD-525 = SIMD-0525; per-stage live/activated-not-yet-effective/pending from Feature accounts | changelog 2026-08-20 + getAccountInfo | yes | yes | yes | yes | Observed slot is INFERRED corroboration, never gate proof. Upgrades page 400 ms ignored if stale. |
| Automation / configurable refresh | yes | GitHub Actions schedule + workflow_dispatch; STALE banner if snapshot age > 2h; on-page LIVE pulse (browser JSON-RPC, ≤60s) for slot/epoch/TPS; local `--` flags | GitHub Actions + page JS | yes | yes | yes | workflow + pulse test | GitHub cron can drift or pause; 15-minute tick is not claimed. Pulse is cluster-only. |
| Anomaly detection | yes | TPS/slot/delinquency/TVL/DEX/price vs baselines | derived | yes | yes | yes | yes | Optional in the listing; present. |
| Interactive HTML | yes | dark dashboard | htmlout.py | yes | — | — | yes | |
| Markdown report | yes | report.md | render_md | — | yes | — | yes | |
| Structured JSON | yes | report.json | generate.py | — | — | yes | yes | schema_version not a separate top-level product field. |
| No API keys / stdlib | yes | urllib + ThreadPoolExecutor | — | yes | yes | yes | yes | Preferred by listing. |
| Live demo | yes | GitHub Pages | dustycompiler.github.io/borealis-solana | yes | — | — | live curl | |
| Dune Analytics | partial | Public embed, labeled External Reference | cryptoonchain/solana-explorer iframe | yes | yes | yes | — | Dune API 401 without key. Not a Borealis query. Not copied from Orbit. |
| README / sources / anomaly write-up | yes | README + SCORE + this matrix | repo | — | yes | — | — | |

All explicit "key metrics to include" cells are yes except X (partial, public mirrors). REV is the latest common complete UTC day of solana.com Fees + Jito daily gross tips, labeled as a calendar day (not rolling 24h). No RWA TVL pretending to be equity volume. No protocol fees pretending to be REV. No Alpenglow pretending to be SIMD-525.
