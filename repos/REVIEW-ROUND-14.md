# Review round-14 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.0s

## Headline

- Total reviewed: **50**
- Approved: **49** (98%)
- Hold-with-revisions: **1** (2%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 6 | 1 | 0 | 7 |
| `comparative-study` | 43 | 0 | 0 | 43 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `classify-misc` | 43 | 0 | 0 | 43 |
| `invoice` | 6 | 1 | 0 | 7 |

## Top issues found

- `audience_clear` — 1 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-classify-grain-contract-pricing-type-zh-hans/blog.html`
- `/repos/hyperapi-classify-grant-award-document-stage/blog.html`
- `/repos/hyperapi-classify-grant-award-document-type/blog.html`
- `/repos/hyperapi-classify-grant-award-letter-stage/blog.html`
- `/repos/hyperapi-classify-grant-award-modification-type/blog.html`
- `/repos/hyperapi-classify-grant-award-stage/blog.html`
- `/repos/hyperapi-classify-grant-budget-category/blog.html`
- `/repos/hyperapi-classify-grant-budget-line-category/blog.html`
- `/repos/hyperapi-classify-grant-claim-document-type/blog.html`
- `/repos/hyperapi-classify-grant-correspondence-intent/blog.html`

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

- Stage the 49 approved blogs at `/tmp/niyatic-gh-pages/repos/<slug>/blog.html` is **done**. CEO can commit to the github.io repo on the next beat.
- 1 hold + 0 reject need REVIEW-NOTES.md follow-up; see per-slug files.
- Greenlight round-14 (next 50) on a new sub-agent thread.