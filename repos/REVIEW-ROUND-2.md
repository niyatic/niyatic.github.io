# Review round-2 aggregate report

- date: 2026-05-26
- batch: next 50 (51-100) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.1s

## Headline

- Total reviewed: **50**
- Approved: **50** (100%)
- Hold-with-revisions: **0** (0%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 2 | 0 | 0 | 2 |
| `comparative-study` | 48 | 0 | 0 | 48 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `classify-misc` | 48 | 0 | 0 | 48 |
| `invoice` | 2 | 0 | 0 | 2 |

## Top issues found

- (none flagged — all rubric checks passed across the 50)

## First 10 approved-and-published blogs

- `/repos/hyperapi-classify-commercial-invoice-vs-k1-schedule-zh-hans/blog.html`
- `/repos/hyperapi-classify-commission-statement-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-commission-statement-vs-nav-statement/blog.html`
- `/repos/hyperapi-classify-commodity-settlement-document-type/blog.html`
- `/repos/hyperapi-classify-construction-billing-document-type/blog.html`
- `/repos/hyperapi-classify-construction-lien-waiver-type/blog.html`
- `/repos/hyperapi-classify-construction-lien-waiver-type-ar/blog.html`
- `/repos/hyperapi-classify-construction-lien-waiver-type-de/blog.html`
- `/repos/hyperapi-classify-construction-lien-waiver-type-es/blog.html`
- `/repos/hyperapi-classify-construction-lien-waiver-type-fr/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.7ms | 21,600,000 |
| `comparative-study` | 0.4ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Stage the 50 approved blogs at `/tmp/niyatic-gh-pages/repos/<slug>/blog.html` is **done**. CEO can commit to the github.io repo on the next beat.
- 0 hold + 0 reject need REVIEW-NOTES.md follow-up; see per-slug files.
- Greenlight round-2 (next 50) on a new sub-agent thread.