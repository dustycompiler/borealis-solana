# Borealis competitor rediscovery — 2026-08-25

Scan window: **2026-08-26 01:59-02:05 UTC** (**2026-08-25 18:59-19:05 PT**).
Method: public HTTP only (GitHub HTML/raw, GitHub Pages, Vercel, Cloudflare tunnels, Dune pages/API, Superteam Earn Next data). No competitor code copied. `/workspace/canada-dashboard` was **not** edited.

Borealis live at scan: **v1.4.1** at https://dustycompiler.github.io/borealis-solana/ (`generated_at_utc` **2026-08-26T01:18:34Z** / **18:18:34 PT**). README and page both say 1.4.1; 1.5.0 is not live yet.

`0x-SquidSol/Heliostat` is **not a repo** (GitHub 404). Heliostat **0.1.0** is the engine name of `0x-SquidSol/Solana-Ecosystem-Auto-Updating-Report-Interactive-Dashboard`.

---

## Superteam listing (live, this window)

| Field | Live value |
|---|---|
| URL | https://superteam.fun/earn/listing/develop-solana-ecosystem-auto-updating-report-and-interactive-dashboard/ |
| Status | **OPEN** (`listing.status=OPEN`, `isWinnersAnnounced=false`) |
| Submissions | **14** (visible `14 SUBMISSIONS` + Next data `queryKey: submissionCount` `state.data: 14`) |
| Deadline | **2026-09-01T03:59:59.000Z** = **2026-08-31 20:59:59 PT** |
| Prizes | **500 / 300 / 200 USDG** (1,000 total) |
| Region | **Canada** |
| Agent access | **HUMAN_ONLY** |
| SIMD in listing body | **SIMD-525** only (not SIMD-0525, not SIMD-025) |
| Preferred stack | no API keys, Python stdlib + public RPC; live demo weighted |

Winners announcement scheduled **2026-09-15**. Unchanged vs the earlier 14-sub count.


---

## Comparison vs Borealis 1.4.1

Legend: live page or committed live artifact unless noted.

### Borealis (baseline)

- Live: https://dustycompiler.github.io/borealis-solana/
- Version **v1.4.1** generated **2026-08-26T01:18:34Z** (18:18 PT). Actions every **15 min**.
- REV **$1.16M 24h** = MEASURED in-protocol fees (9,162.1 SOL / $888.17K from solana.com/data) + ESTIMATED Jito tip-floor p50 ($271.96K). Protocol fees **$14.08M EXCLUDED**.
- Tokenized: 24h volume **$23.58M** (Jupiter subset); priced mcap **$276.69M** (80 of 715); Llama xStocks TVL **$430.26M**.
- Fees: p50 **0.000005 SOL**, n_tx=2240 / n_nonvote=1197, ~2.8h getBlock window, NOT a 24h census.
- SIMD: heading SIMD-525 + Alpenglow (SIMD-0326). Explicit: SIMD-525 is SIMD-0525, not SIMD-025.
- Tests: tests.yml badge passing. python3 -m unittest.

### Heliostat (0x-SquidSol long-named repo)

- Live: https://0x-squidsol.github.io/Solana-Ecosystem-Auto-Updating-Report-Interactive-Dashboard/
- heliostat **0.1.0**. JSON generated **2026-08-26T00:37:56Z** (17:37 PT), **~86 min old** vs claimed 15 min.
- REV **$1.14M** = Llama network fees $928.7K + Jito tips $213.5K. App fees **$14.62M kept separate**. Dune enabled: false.
- Tokenized: RWA TVL **$2.06B / 24 protocols** (not 24h equity volume). BUIDL $876.38M, xStocks $430.26M, OnRe $277.20M.
- Fees: median user fee **5,521 lamports (~$0.000533)**, votes excluded, sampled block.
- SIMD: no SIMD-525, no Alpenglow heading. Live SIMD Activity = 0340 / 0392 / 0433 / 0550 / 0553 GH Atom commits.
- Automation: report.yml passing, README every 15 min. Tests.yml passing.

### Orbit (Edgywol/Solana_Ecosystem)

- Live: https://dashboard-flame-gamma-14.vercel.app
- **v1.0.0** generated **2026-08-26T01:05:30Z** (18:05 PT). SPA loads /report.json.
- REV **$1,253,419.53** proxy (non-vote tx * fees + estimated Jito tips).
- Tokenized: honestly omitted (no free keyless API).
- Fees: median 0.000028 SOL / $0.0027. fee_source = **model fallback, no positive priority-fee samples**.
- SIMD: Alpenglow + SIMD-0096 / 0123. No SIMD-525. News last_updated 2026-08-18.
- Automation: README 6h to Vercel. **Actions badge this window: failing.**
- Tests: static "9 passing" badge; test_anomaly.py + test_pipeline.py. No tests.yml badge.

### Pulse (ChaosAIVision/solana-pulse)

- Live: https://chaosaivision.github.io/solana-pulse/
- Generated 2026-08-26T01:58:28Z (18:58 PT). Freshest rival. No semver.
- Hero Fees/REV 24h $13.80M. JSON rev equals fees (13800650). Llama app fees, not network REV.
- No tokenized equities, no median fee, no SIMD, no tests.
- pulse.yml passing, every 2h.

### HIS (HIS-AliKarasneh)

- Live: https://his-alikarasneh.github.io/solana-ecosystem-report/
- HTML generated 2026-08-26T00:56:10Z (17:56 PT).
- Missing REV, tokenized equities, median fee, and SIMD.
- Pages cron every 2 hours. unittest suite present.
- DEX 24h $9.90B vs about $3.0B on Borealis/Pulse/Squid/Orbit.

### jonschwadron/solpulse (stale)

- Live: https://jonschwadron.github.io/solpulse/ v1.0.0 dated 2026-08-14T12:45:58Z (11 days stale).
- REV proxy about $10.08M (Llama fees, labeled). Names SIMD-0525 plus Alpenglow notes. Host not refreshing.

### Solstice (quetzalforge)

- Hosted demo returned HTTP 200. Snapshot timestamp 2026-08-26T02:04:24Z.
- On-chain network and validator metrics were blank this window. Off-chain Llama economics still populate.
- Node stack, not stdlib-only. No REV, tokenized, or SIMD.

### Not live (repo exists, no clickable dashboard)

- nandy-technologies: GH Pages 404. Cloudflare tunnel NXDOMAIN. Hourly cron claimed.
- jojo2a/solpulse: GH Pages 404. README on master claims REV, tokenized volumes, and tests. No demo.
- Carl0ss100/solarium: GH Pages is the Jekyll README, not the dashboard.
- liushazyy: GH Pages is README. Sample dated 2026-08-06.
- chaintail: GH Pages 404.
- mamenesia: claimed demo 404. README deadline 2026-08-18 (past).
- devyeyostellar: README 404 on main.
- 0x-SquidSol/Heliostat as a repo: GitHub 404. Alias of the long-named Squid repo.

GitHub search HTML returned 429 this window. No new Vercel/Netlify live dashboard under obvious name guesses.

---

## Who might beat Borealis (1.4.1 to 1.5.0)

Ranked by judge-visible risk.

### 1. Heliostat (Squid) — only live peer on the same checklist

Why it can take 1st: same stdlib / no-keys / HTML+MD+JSON / 15-min Actions story. Prints a REV dollar of the same order ($1.14M vs Borealis $1.16M) with app fees $14.6M held out. Broader RWA (24 protocols, $2.06B, BUIDL on the hero). Validator skyline, Agave/Firedancer split, tests.yml passing.

Why Borealis still wins if 1.5.0 holds: listing says Alpenglow, SIMD-525. Heliostat JSON has no Alpenglow string. Borealis greps clean. Borealis also has 24h tokenized-equity DEX volume ($23.58M). Heliostat xStocks $430M is Llama TVL, not volume. This scan Heliostat was ~86 min stale vs claimed 15 min.

1.5.0 watch: keep SIMD-525 / Alpenglow headings; keep REV definition; keep Jupiter 24h equity volume; stay inside 15 min.

### 2. Pulse — checklist trap, not a better report

Why it can steal a scorebox: live, dark, stdlib, 2h Actions passing, hero says Fees / REV 24h $13.80M. A time-pressed judge matching the listing word REV will see a big number. 1.4.1 already closed the empty-REV hole from 1.3.0.

Why it should not win: rev equals fees. That is application fees, not network REV. No median fee, no tokenized equities, no SIMD, no tests.

### 3. Orbit — product polish, currently tripping on ops

Why it can still place: Vercel, Chart.js, health pentagon, SQLite timeseries, DAA model, keyless RSS, honest tokenized omission, in-repo tests, REV proxy ~$1.25M.

Why weaker tonight: Actions badge failing; median fee is a model fallback; Dune cache dated 2026-08-20; SIMD ledger has Alpenglow + 0096/0123 but not SIMD-525; 6h cadence; news frozen 2026-08-18.

Do not copy Orbit Dune queries or cache.

### 4. Everyone else is unlikely to beat a live 1.4.1/1.5.0

HIS is live and 2h with tests but missing REV/fees/tokenized/SIMD. jonschwadron names SIMD-0525 but is 11 days stale. jojo2a has claims plus tests but no live demo. Solstice on-chain metrics were blank. nandy/solarium/liusha/chaintail/mamenesia have no clickable dashboard.

---

## Dune: no-key public query/result?

Question: is there a no-key public Dune query/result for Solana REV or fees we could cite as OPTIONAL EXTERNAL, not core?

What we hit this window:

- Dune API query results: 401 Unauthorized (key required). CSV export also 401.
- dune.com query and embed pages: 200 HTML shell with Loading, no SSR result rows.
- Public dashboards exist (ilemi solana-compute, lily212 solana-fee-tracker, cryptoonchain solana-explorer). They are JS apps, not JSON.
- Jito DAO revenue dashboard is not network REV.
- Orbit live dune object is cached, cached_at 2026-08-20, refreshes only when a key is supplied.
- Heliostat dune section enabled: false unless DUNE_API_KEY plus query ids.

There is no original, no-key, machine-readable Dune query result we can ingest as a core number. Blockworks Network REV is a public definition page, not Dune. Borealis already uses solana.com/data for the fees leg (vendor series, labeled). That is not running a Dune query.

### Recommendation

Keep Dune as a clearly labeled External Reference. Do not make it core. Do not copy Orbit queries or Orbit cached rows.

Practical 1.5.0 shape:

1. Core REV stays 1.4.1: solana.com/data in-protocol fees (MEASURED) + public Jito tip-floor estimate (ESTIMATED, p50 headline, p95 sensitivity). Llama app fees stay excluded.
2. Sources tab may keep a public iframe with copy: external Dune dashboard, not our query, not required to render this report.
3. Optional one-liner links, not numbers: Blockworks Network REV definition; ilemi compute; lily212 fee tracker.
4. If a Dune key is ever added, gate it off (never failed) so the no-keys preference still holds.

Orbit Dune cache going stale on 2026-08-20 shows why keyed Dune cannot be core on this bounty.

---

## Compact comparison (live only)

| Project | Ver / freshness | REV | Tokenized equities | Fees | SIMD | Auto | Tests |
|---|---|---|---|---|---|---|---|
| Borealis | 1.4.1 / 01:18Z / 15m | $1.16M measured+est tips; $14.08M app fees excluded | $23.58M 24h vol; $276.69M mcap 80/715; $430.26M TVL | p50 0.000005 SOL ~2.8h | SIMD-525 + Alpenglow 0326 | 15m Actions | tests.yml passing |
| Heliostat | 0.1.0 / 00:37Z (~86m lag) | $1.14M fees+tips; $14.62M app separate | RWA $2.06B / 24 proto; xStocks TVL $430M | 5521 lamports sampled | no 525 / no Alpenglow | 15m claimed | tests.yml passing |
| Orbit | 1.0.0 / 01:05Z / 6h | $1.25M proxy | omitted (honest) | model fallback 0.000028 SOL | Alpenglow + 0096/0123; no 525 | Actions failing | 9 tests claimed |
| Pulse | none / 01:58Z / 2h | $13.80M = Llama app fees | no | no | no | 2h passing | none |
| HIS | none / 00:56Z / 2h | no | no | no | no | 2h Pages | unittest yes |
| jonsch | 1.0.0 / Aug 14 stale | $10.08M fees proxy | no | no p50 | SIMD-0525 yes | not refreshing | no |
| Solstice | snapshot 02:04Z degraded | no | no | no | no | host 200, RPC blank | Node CI |

---

## Borealis 1.4.1 live snapshot (baseline for 1.5.0)

Fetched 2026-08-26T01:59Z, 189260 bytes. Embedded snapshot:

- Health score 82 (rpc 25 + slot 30 + delinquency 7.2 + tps 20). Delinquent stake 1.424%. Verdict WATCH now matches delinquency (unlike 1.3.0's 100/WATCH).
- REV 24h $1.16M. Median fee p50 0.000005 SOL. xStocks 24h vol $23.58M.
- SIMD-525 + Alpenglow present. Tests passing. Cadence 15 min.

1.3.0 holes closed: empty REV cell; missing SIMD-525; xStocks volume. Remaining nits: tokenized mcap is 80/715 lower bound (labeled); Heliostat still looks bigger on RWA TVL.

---

## Sources (this pass)

Superteam listing Next data; Borealis homepage + README + tests badge; Squid Pages + report.json + badges; Orbit Vercel report.json + README + failing refresh badge; Pulse Pages + report.json; HIS Pages + workflow + tests; jonschwadron Pages; Solstice snapshot; nandy/jojo/solarium/liusha/chaintail/mamenesia 404s; Dune API 401s and public dashboard shells.

No files under /workspace/canada-dashboard were written.
