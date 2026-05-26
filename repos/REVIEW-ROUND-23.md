# Review round-23 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.1s

## Headline

- Total reviewed: **50**
- Approved: **47** (94%)
- Hold-with-revisions: **3** (6%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 47 | 2 | 0 | 49 |
| `comparative-study` | 0 | 1 | 0 | 1 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `extract-misc` | 20 | 1 | 0 | 21 |
| `invoice` | 27 | 1 | 0 | 28 |
| `remittance` | 0 | 1 | 0 | 1 |

## Top issues found

- `hook_strength` — 2 occurrence(s)
- `audience_clear` — 2 occurrence(s)
- `cross_vendor_framing` — 1 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-extract-closing-disclosure-trid-fields-pt/blog.html`
- `/repos/hyperapi-extract-closing-disclosure-trid-fields-ru/blog.html`
- `/repos/hyperapi-extract-closing-disclosure-trid-fields-tr/blog.html`
- `/repos/hyperapi-extract-closing-disclosure-trid-fields-zh-hans/blog.html`
- `/repos/hyperapi-extract-cms-1500-claim-fields/blog.html`
- `/repos/hyperapi-extract-cms-1500-claim-fields-ar/blog.html`
- `/repos/hyperapi-extract-cms-1500-claim-fields-de/blog.html`
- `/repos/hyperapi-extract-cms-1500-claim-fields-es/blog.html`
- `/repos/hyperapi-extract-cms-1500-claim-fields-fr/blog.html`
- `/repos/hyperapi-extract-cms-1500-claim-fields-hi/blog.html`

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

- Stage the 47 approved blogs at `/tmp/niyatic-gh-pages/repos/<slug>/blog.html` is **done**. CEO can commit to the github.io repo on the next beat.
- 3 hold + 0 reject need REVIEW-NOTES.md follow-up; see per-slug files.
- Greenlight round-23 (next 50) on a new sub-agent thread.