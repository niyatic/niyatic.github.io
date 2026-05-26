# Review round-15 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.1s

## Headline

- Total reviewed: **50**
- Approved: **45** (90%)
- Hold-with-revisions: **5** (10%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 6 | 5 | 0 | 11 |
| `cfo-agents-shepherd` | 11 | 0 | 0 | 11 |
| `comparative-study` | 28 | 0 | 0 | 28 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `classify-misc` | 27 | 0 | 0 | 27 |
| `credit_note` | 1 | 0 | 0 | 1 |
| `invoice` | 6 | 5 | 0 | 11 |
| `tax-1099` | 10 | 0 | 0 | 10 |
| `tax-w2` | 1 | 0 | 0 | 1 |

## Top issues found

- `audience_clear` — 3 occurrence(s)
- `hook_strength` — 2 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-classify-invoice-freight-treatment/blog.html`
- `/repos/hyperapi-classify-invoice-gross-vs-net/blog.html`
- `/repos/hyperapi-classify-invoice-line-type/blog.html`
- `/repos/hyperapi-classify-invoice-rebill-vs-original/blog.html`
- `/repos/hyperapi-classify-invoice-recurring-vs-onetime/blog.html`
- `/repos/hyperapi-classify-invoice-rounding-treatment/blog.html`
- `/repos/hyperapi-classify-invoice-vs-credit-note/blog.html`
- `/repos/hyperapi-classify-journal-entry-type/blog.html`
- `/repos/hyperapi-classify-journal-entry-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-journal-entry-vs-statement-of-account/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.4ms | 21,600,000 |
| `cfo-agents-shepherd` | 0.3ms | 21,600,000 |
| `comparative-study` | 0.6ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Stage the 45 approved blogs at `/tmp/niyatic-gh-pages/repos/<slug>/blog.html` is **done**. CEO can commit to the github.io repo on the next beat.
- 5 hold + 0 reject need REVIEW-NOTES.md follow-up; see per-slug files.
- Greenlight round-15 (next 50) on a new sub-agent thread.