# Review round-21 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.1s

## Headline

- Total reviewed: **50**
- Approved: **46** (92%)
- Hold-with-revisions: **4** (8%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 13 | 2 | 0 | 15 |
| `cfo-agents-shepherd` | 9 | 0 | 0 | 9 |
| `comparative-study` | 24 | 2 | 0 | 26 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `classify-misc` | 24 | 0 | 0 | 24 |
| `extract-misc` | 12 | 2 | 0 | 14 |
| `invoice` | 1 | 0 | 0 | 1 |
| `payroll` | 1 | 0 | 0 | 1 |
| `remittance` | 0 | 2 | 0 | 2 |
| `tax-1099` | 6 | 0 | 0 | 6 |
| `tax-w2` | 2 | 0 | 0 | 2 |

## Top issues found

- `hook_strength` — 2 occurrence(s)
- `cross_vendor_framing` — 2 occurrence(s)
- `audience_clear` — 1 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-classify-vendor-onboarding-form-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-vendor-onboarding-form-vs-debt-covenant-certificate/blog.html`
- `/repos/hyperapi-classify-vendor-onboarding-stage/blog.html`
- `/repos/hyperapi-classify-vendor-payment-block-reason/blog.html`
- `/repos/hyperapi-classify-vendor-risk-tier/blog.html`
- `/repos/hyperapi-classify-vendor-statement-vs-invoice/blog.html`
- `/repos/hyperapi-classify-vendor-tax-form-class/blog.html`
- `/repos/hyperapi-classify-w2-wage-statement-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-w2-wage-statement-vs-distribution-notice/blog.html`
- `/repos/hyperapi-classify-w8ben-form-vs-cover-page/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.3ms | 21,600,000 |
| `cfo-agents-shepherd` | 0.3ms | 21,600,000 |
| `comparative-study` | 0.4ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Stage the 46 approved blogs at `/tmp/niyatic-gh-pages/repos/<slug>/blog.html` is **done**. CEO can commit to the github.io repo on the next beat.
- 4 hold + 0 reject need REVIEW-NOTES.md follow-up; see per-slug files.
- Greenlight round-21 (next 50) on a new sub-agent thread.