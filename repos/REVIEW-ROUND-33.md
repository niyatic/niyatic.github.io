# Review round-33 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.1s

## Headline

- Total reviewed: **50**
- Approved: **28** (56%)
- Hold-with-revisions: **22** (44%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 28 | 16 | 0 | 44 |
| `comparative-study` | 0 | 6 | 0 | 6 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `extract-misc` | 28 | 16 | 0 | 44 |
| `remittance` | 0 | 6 | 0 | 6 |

## Top issues found

- `audience_clear` — 16 occurrence(s)
- `hook_strength` — 8 occurrence(s)
- `cross_vendor_framing` — 6 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-extract-loan-amortization-schedule-header-fields/blog.html`
- `/repos/hyperapi-extract-loan-paydown-allocation/blog.html`
- `/repos/hyperapi-extract-loan-payoff-figures/blog.html`
- `/repos/hyperapi-extract-loan-payoff-quote-fields/blog.html`
- `/repos/hyperapi-extract-loan-payoff-statement-fields/blog.html`
- `/repos/hyperapi-extract-loan-repayment-holiday-terms/blog.html`
- `/repos/hyperapi-extract-loan-repayment-schedule-rows/blog.html`
- `/repos/hyperapi-extract-lockbox-batch-header-fields/blog.html`
- `/repos/hyperapi-extract-margin-call-notice-fields/blog.html`
- `/repos/hyperapi-extract-mineral-rights-division-order/blog.html`

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

- Approval rate is low (56%) — pause and review the rubric calibration with CEO before running round-33.