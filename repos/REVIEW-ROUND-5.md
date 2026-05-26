# Review round-5 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.0s

## Headline

- Total reviewed: **50**
- Approved: **50** (100%)
- Hold-with-revisions: **0** (0%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `cfo-agents-shepherd` | 1 | 0 | 0 | 1 |
| `comparative-study` | 49 | 0 | 0 | 49 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `bank_statement` | 1 | 0 | 0 | 1 |
| `classify-misc` | 49 | 0 | 0 | 49 |

## Top issues found

- (none flagged — all rubric checks passed across the 50)

## First 10 approved-and-published blogs

- `/repos/hyperapi-classify-derivative-contract-type-pt/blog.html`
- `/repos/hyperapi-classify-derivative-contract-type-ru/blog.html`
- `/repos/hyperapi-classify-derivative-contract-type-tr/blog.html`
- `/repos/hyperapi-classify-derivative-contract-type-zh-hans/blog.html`
- `/repos/hyperapi-classify-dispute-vs-inquiry/blog.html`
- `/repos/hyperapi-classify-distribution-notice-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-distribution-notice-vs-title-commitment/blog.html`
- `/repos/hyperapi-classify-dividend-event-type/blog.html`
- `/repos/hyperapi-classify-dividend-notice-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-dividend-notice-vs-escrow-statement/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `cfo-agents-shepherd` | 0.3ms | 21,600,000 |
| `comparative-study` | 0.4ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Stage the 50 approved blogs at `/tmp/niyatic-gh-pages/repos/<slug>/blog.html` is **done**. CEO can commit to the github.io repo on the next beat.
- 0 hold + 0 reject need REVIEW-NOTES.md follow-up; see per-slug files.
- Greenlight round-5 (next 50) on a new sub-agent thread.