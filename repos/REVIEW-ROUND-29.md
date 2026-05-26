# Review round-29 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.1s

## Headline

- Total reviewed: **50**
- Approved: **31** (62%)
- Hold-with-revisions: **19** (38%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 31 | 16 | 0 | 47 |
| `comparative-study` | 0 | 3 | 0 | 3 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `extract-misc` | 24 | 13 | 0 | 37 |
| `invoice` | 7 | 3 | 0 | 10 |
| `receipt` | 0 | 1 | 0 | 1 |
| `remittance` | 0 | 2 | 0 | 2 |

## Top issues found

- `audience_clear` — 14 occurrence(s)
- `hook_strength` — 7 occurrence(s)
- `cross_vendor_framing` — 3 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-extract-grant-budget-line-items/blog.html`
- `/repos/hyperapi-extract-grant-budget-modification-fields/blog.html`
- `/repos/hyperapi-extract-grant-budget-narrative-fields/blog.html`
- `/repos/hyperapi-extract-grant-disbursement-milestones/blog.html`
- `/repos/hyperapi-extract-grant-financial-report-fields/blog.html`
- `/repos/hyperapi-extract-grant-subaward-agreement-fields/blog.html`
- `/repos/hyperapi-extract-gst-tax-invoice-lines/blog.html`
- `/repos/hyperapi-extract-guarantee-letter-fields/blog.html`
- `/repos/hyperapi-extract-holdback-amount/blog.html`
- `/repos/hyperapi-extract-iata-sis-interline-invoice-fields/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.4ms | 21,600,000 |
| `comparative-study` | 0.4ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Stage the 31 approved blogs at `/tmp/niyatic-gh-pages/repos/<slug>/blog.html` is **done**. CEO can commit to the github.io repo on the next beat.
- 19 hold + 0 reject need REVIEW-NOTES.md follow-up; see per-slug files.
- Greenlight round-29 (next 50) on a new sub-agent thread.