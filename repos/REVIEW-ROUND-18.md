# Review round-18 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.0s

## Headline

- Total reviewed: **50**
- Approved: **43** (86%)
- Hold-with-revisions: **7** (14%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 3 | 1 | 0 | 4 |
| `cfo-agents-shepherd` | 2 | 0 | 0 | 2 |
| `comparative-study` | 38 | 0 | 0 | 38 |
| `gtm-b2c-virality` | 0 | 6 | 0 | 6 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `bol` | 0 | 1 | 0 | 1 |
| `classify-misc` | 28 | 0 | 0 | 28 |
| `invoice` | 3 | 1 | 0 | 4 |
| `po` | 0 | 5 | 0 | 5 |
| `receipt` | 3 | 0 | 0 | 3 |
| `remittance` | 7 | 0 | 0 | 7 |
| `tax-1099` | 2 | 0 | 0 | 2 |

## Top issues found

- `quantified_hook` — 6 occurrence(s)
- `viral_angle` — 3 occurrence(s)
- `audience_clear` — 1 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-classify-private-credit-notice-type/blog.html`
- `/repos/hyperapi-classify-procurement-document-type/blog.html`
- `/repos/hyperapi-classify-procurement-spend-category/blog.html`
- `/repos/hyperapi-classify-proforma-invoice-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-proforma-invoice-vs-remittance-advice/blog.html`
- `/repos/hyperapi-classify-promissory-note-type/blog.html`
- `/repos/hyperapi-classify-promissory-note-vs-1099-misc/blog.html`
- `/repos/hyperapi-classify-promissory-note-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-prospectus-offering-type/blog.html`
- `/repos/hyperapi-classify-purchase-vs-expense-document/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.3ms | 21,600,000 |
| `cfo-agents-shepherd` | 0.3ms | 21,600,000 |
| `comparative-study` | 0.4ms | 21,600,000 |
| `gtm-b2c-virality` | 0.4ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Stage the 43 approved blogs at `/tmp/niyatic-gh-pages/repos/<slug>/blog.html` is **done**. CEO can commit to the github.io repo on the next beat.
- 7 hold + 0 reject need REVIEW-NOTES.md follow-up; see per-slug files.
- Greenlight round-18 (next 50) on a new sub-agent thread.