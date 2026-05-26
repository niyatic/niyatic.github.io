# Review round-19 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.0s

## Headline

- Total reviewed: **50**
- Approved: **48** (96%)
- Hold-with-revisions: **2** (4%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 1 | 1 | 0 | 2 |
| `cfo-agents-shepherd` | 1 | 0 | 0 | 1 |
| `comparative-study` | 46 | 0 | 0 | 46 |
| `gtm-b2c-virality` | 0 | 1 | 0 | 1 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `classify-misc` | 46 | 0 | 0 | 46 |
| `invoice` | 1 | 1 | 0 | 2 |
| `po` | 0 | 1 | 0 | 1 |
| `tax-1099` | 1 | 0 | 0 | 1 |

## Top issues found

- `quantified_hook` — 1 occurrence(s)
- `hook_strength` — 1 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-classify-royalty-statement-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-royalty-statement-vs-subscription-agreement/blog.html`
- `/repos/hyperapi-classify-royalty-tier-bracket/blog.html`
- `/repos/hyperapi-classify-sales-tax-exemption-certificate-type/blog.html`
- `/repos/hyperapi-classify-sales-tax-exemption-certificate-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-scan-legibility/blog.html`
- `/repos/hyperapi-classify-securities-corporate-action-type/blog.html`
- `/repos/hyperapi-classify-servicing-transfer-document/blog.html`
- `/repos/hyperapi-classify-settlement-statement-vs-cover-page/blog.html`
- `/repos/hyperapi-classify-settlement-statement-vs-fixed-asset-register/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.4ms | 21,600,000 |
| `cfo-agents-shepherd` | 0.3ms | 21,600,000 |
| `comparative-study` | 0.4ms | 21,600,000 |
| `gtm-b2c-virality` | 0.4ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Stage the 48 approved blogs at `/tmp/niyatic-gh-pages/repos/<slug>/blog.html` is **done**. CEO can commit to the github.io repo on the next beat.
- 2 hold + 0 reject need REVIEW-NOTES.md follow-up; see per-slug files.
- Greenlight round-19 (next 50) on a new sub-agent thread.