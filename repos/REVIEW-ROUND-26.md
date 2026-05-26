# Review round-26 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.0s

## Headline

- Total reviewed: **50**
- Approved: **20** (40%)
- Hold-with-revisions: **30** (60%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 20 | 2 | 0 | 22 |
| `comparative-study` | 0 | 28 | 0 | 28 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `extract-misc` | 20 | 2 | 0 | 22 |
| `remittance` | 0 | 28 | 0 | 28 |

## Top issues found

- `cross_vendor_framing` — 28 occurrence(s)
- `audience_clear` — 2 occurrence(s)
- `hook_strength` — 1 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-extract-escrow-statement-key-fields-ko/blog.html`
- `/repos/hyperapi-extract-escrow-statement-key-fields-nl/blog.html`
- `/repos/hyperapi-extract-escrow-statement-key-fields-pt/blog.html`
- `/repos/hyperapi-extract-escrow-statement-key-fields-ru/blog.html`
- `/repos/hyperapi-extract-escrow-statement-key-fields-tr/blog.html`
- `/repos/hyperapi-extract-escrow-statement-key-fields-zh-hans/blog.html`
- `/repos/hyperapi-extract-esg-emissions-scope-data/blog.html`
- `/repos/hyperapi-extract-expense-report-header-fields-ar/blog.html`
- `/repos/hyperapi-extract-expense-report-header-fields-de/blog.html`
- `/repos/hyperapi-extract-expense-report-header-fields-es/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.3ms | 21,600,000 |
| `comparative-study` | 0.4ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Approval rate is low (40%) — pause and review the rubric calibration with CEO before running round-26.