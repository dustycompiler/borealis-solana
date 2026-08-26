# Official requirement matrix — Borealis 1.5.0

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
| Real Economic Value (REV) | partial | Measured in-protocol fees 24h. Full REV incomplete. | solana.com/data Fees; Jito tip_floor as distribution only | yes | yes | yes | yes | No zero-key 24h Jito tape. Llama app fees excluded. |
| Median transaction fees | yes | getBlock meta.fee p50, time-stratified ~2–3h | RPC getBlock | yes | yes | yes | yes | Not a 24h census; window_seconds labeled. |
| Tokenized asset volumes (equities) | yes | Jupiter stats24h buy+sell on matched xStock mints | lite-api.jup.ag | yes | yes | yes | helper | Subset, not all 715, not all Solana DEX. |
| Daily active addresses | yes | Allium series via solana.com/data | solana.com/api/databricks | yes | yes | yes | helper | Vendors disagree; not averaged. |
| Alpenglow | yes | SIMD-0326 editorial + status | SIMD docs / solana.com | yes | yes | yes | yes | Not claimed activated from slot time. |
| SIMD-525 | yes | Listing token SIMD-525 = SIMD-0525 slot-time stages | solana.com/news + SIMD-0525 | yes | yes | yes | yes | Observed slot is INFERRED corroboration, not a feature-gate RPC. |
| Automation / configurable refresh | yes | Actions every 15 minutes; local `--` flags | GitHub Actions | yes | yes | yes | workflow | Cron can drift. |
| Anomaly detection | yes | TPS/slot/delinquency/TVL/DEX/price vs baselines | derived | yes | yes | yes | yes | Optional in the listing; present. |
| Interactive HTML | yes | dark dashboard | htmlout.py | yes | — | — | yes | |
| Markdown report | yes | report.md | render_md | — | yes | — | yes | |
| Structured JSON | yes | report.json | generate.py | — | — | yes | yes | schema_version not a separate top-level product field. |
| No API keys / stdlib | yes | urllib + ThreadPoolExecutor | — | yes | yes | yes | yes | Preferred by listing. |
| Live demo | yes | GitHub Pages | dustycompiler.github.io/borealis-solana | yes | — | — | live curl | |
| Dune Analytics | partial | Public embed, labeled External Reference | cryptoonchain/solana-explorer iframe | yes | yes | yes | — | Dune API 401 without key. Not a Borealis query. Not copied from Orbit. |
| README / sources / anomaly write-up | yes | README + SCORE + this matrix | repo | — | yes | — | — | |

All explicit "key metrics to include" cells are yes except REV (partial, honest incomplete) and X (partial, public mirrors). No RWA TVL pretending to be equity volume. No protocol fees pretending to be REV. No Alpenglow pretending to be SIMD-525.
