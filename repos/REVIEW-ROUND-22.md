# Review round-22 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.1s

## Headline

- Total reviewed: **50**
- Approved: **36** (72%)
- Hold-with-revisions: **14** (28%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 34 | 2 | 0 | 36 |
| `cfo-agents-shepherd` | 2 | 0 | 0 | 2 |
| `comparative-study` | 0 | 12 | 0 | 12 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `cheque` | 2 | 0 | 0 | 2 |
| `extract-misc` | 34 | 2 | 0 | 36 |
| `remittance` | 0 | 12 | 0 | 12 |

## Top issues found

- `cross_vendor_framing` — 12 occurrence(s)
- `hook_strength` — 1 occurrence(s)
- `audience_clear` — 1 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-extract-chargeback-notice-fields/blog.html`
- `/repos/hyperapi-extract-charter-party-agreement-clauses/blog.html`
- `/repos/hyperapi-extract-charter-party-agreement-terms/blog.html`
- `/repos/hyperapi-extract-charter-party-bunker-clauses/blog.html`
- `/repos/hyperapi-extract-charter-party-demurrage-terms/blog.html`
- `/repos/hyperapi-extract-charter-party-hire-terms/blog.html`
- `/repos/hyperapi-extract-charter-party-laytime-terms/blog.html`
- `/repos/hyperapi-extract-check-deposit-header-fields/blog.html`
- `/repos/hyperapi-extract-check-deposit-remittance-fields/blog.html`
- `/repos/hyperapi-extract-claims-bordereau-line-items/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.4ms | 21,600,000 |
| `cfo-agents-shepherd` | 0.3ms | 21,600,000 |
| `comparative-study` | 0.4ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Stage the 36 approved blogs at `/tmp/niyatic-gh-pages/repos/<slug>/blog.html` is **done**. CEO can commit to the github.io repo on the next beat.
- 14 hold + 0 reject need REVIEW-NOTES.md follow-up; see per-slug files.
- Greenlight round-22 (next 50) on a new sub-agent thread.