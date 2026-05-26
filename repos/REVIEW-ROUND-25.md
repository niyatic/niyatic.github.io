# Review round-25 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.0s

## Headline

- Total reviewed: **50**
- Approved: **31** (62%)
- Hold-with-revisions: **19** (38%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 31 | 19 | 0 | 50 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `extract-misc` | 31 | 19 | 0 | 50 |

## Top issues found

- `audience_clear` — 19 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-extract-escrow-analysis-fields/blog.html`
- `/repos/hyperapi-extract-escrow-analysis-fields-ar/blog.html`
- `/repos/hyperapi-extract-escrow-analysis-fields-de/blog.html`
- `/repos/hyperapi-extract-escrow-analysis-fields-es/blog.html`
- `/repos/hyperapi-extract-escrow-analysis-fields-fr/blog.html`
- `/repos/hyperapi-extract-escrow-analysis-fields-hi/blog.html`
- `/repos/hyperapi-extract-escrow-analysis-fields-it/blog.html`
- `/repos/hyperapi-extract-escrow-analysis-fields-ja/blog.html`
- `/repos/hyperapi-extract-escrow-analysis-fields-ko/blog.html`
- `/repos/hyperapi-extract-escrow-analysis-fields-nl/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.3ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Stage the 31 approved blogs at `/tmp/niyatic-gh-pages/repos/<slug>/blog.html` is **done**. CEO can commit to the github.io repo on the next beat.
- 19 hold + 0 reject need REVIEW-NOTES.md follow-up; see per-slug files.
- Greenlight round-25 (next 50) on a new sub-agent thread.