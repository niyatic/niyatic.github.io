# Review round-17 aggregate report

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
| `abm-content-marketing` | 1 | 0 | 0 | 1 |
| `cfo-agents-shepherd` | 8 | 0 | 0 | 8 |
| `comparative-study` | 37 | 0 | 0 | 37 |
| `gtm-b2c-virality` | 0 | 4 | 0 | 4 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `classify-misc` | 34 | 0 | 0 | 34 |
| `invoice` | 1 | 0 | 0 | 1 |
| `packing_slip` | 0 | 2 | 0 | 2 |
| `payroll` | 8 | 0 | 0 | 8 |
| `po` | 0 | 2 | 0 | 2 |
| `remittance` | 3 | 0 | 0 | 3 |

## Top issues found

- `quantified_hook` — 4 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-classify-lockbox-batch-document-type/blog.html`
- `/repos/hyperapi-classify-lockbox-batch-type/blog.html`
- `/repos/hyperapi-classify-lockbox-batch-vs-commercial-invoice/blog.html`
- `/repos/hyperapi-classify-lockbox-batch-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-lockbox-remittance-type/blog.html`
- `/repos/hyperapi-classify-margin-call-urgency/blog.html`
- `/repos/hyperapi-classify-marine-insurance-certificate-type/blog.html`
- `/repos/hyperapi-classify-meter-reading-type/blog.html`
- `/repos/hyperapi-classify-mortgage-package-page-type/blog.html`
- `/repos/hyperapi-classify-municipal-filing-form-type/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.3ms | 21,600,000 |
| `cfo-agents-shepherd` | 0.4ms | 21,600,000 |
| `comparative-study` | 0.4ms | 21,600,000 |
| `gtm-b2c-virality` | 0.3ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Stage the 46 approved blogs at `/tmp/niyatic-gh-pages/repos/<slug>/blog.html` is **done**. CEO can commit to the github.io repo on the next beat.
- 4 hold + 0 reject need REVIEW-NOTES.md follow-up; see per-slug files.
- Greenlight round-17 (next 50) on a new sub-agent thread.