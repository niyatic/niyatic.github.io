# Review round-1 aggregate report

- date: 2026-05-26
- batch: first 50 publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.0s

## Headline

- Total reviewed: **50**
- Approved: **39** (78%)
- Hold-with-revisions: **11** (22%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 21 | 0 | 0 | 21 |
| `cfo-agents-shepherd` | 9 | 0 | 0 | 9 |
| `comparative-study` | 9 | 0 | 0 | 9 |
| `gtm-b2c-virality` | 0 | 11 | 0 | 11 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `bol` | 0 | 3 | 0 | 3 |
| `classify-misc` | 8 | 0 | 0 | 8 |
| `invoice` | 21 | 0 | 0 | 21 |
| `po` | 0 | 8 | 0 | 8 |
| `receipt` | 1 | 0 | 0 | 1 |
| `tax-1099` | 9 | 0 | 0 | 9 |

## Top issues found

- `quantified_hook` — 11 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-classify-1099-div-vs-capital-call-notice/blog.html`
- `/repos/hyperapi-classify-1099-div-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-1099-int-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-1099-int-vs-dividend-notice/blog.html`
- `/repos/hyperapi-classify-1099-misc-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-1099-misc-vs-royalty-statement/blog.html`
- `/repos/hyperapi-classify-1099-nec-vs-commission-statement/blog.html`
- `/repos/hyperapi-classify-1099-nec-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-1099-variant-type/blog.html`
- `/repos/hyperapi-classify-accrual-vs-prepaid/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.3ms | 21,600,000 |
| `cfo-agents-shepherd` | 0.3ms | 21,600,000 |
| `comparative-study` | 0.4ms | 21,600,000 |
| `gtm-b2c-virality` | 0.3ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Stage the 39 approved blogs at `/tmp/niyatic-gh-pages/repos/<slug>/blog.html` is **done**. CEO can commit to the github.io repo on the next beat.
- 11 hold + 0 reject need REVIEW-NOTES.md follow-up; see per-slug files.
- Greenlight round-2 (next 50) on a new sub-agent thread.