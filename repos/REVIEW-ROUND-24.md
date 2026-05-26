# Review round-24 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.1s

## Headline

- Total reviewed: **50**
- Approved: **18** (36%)
- Hold-with-revisions: **32** (64%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 17 | 30 | 0 | 47 |
| `comparative-study` | 1 | 2 | 0 | 3 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `credit_note` | 1 | 0 | 0 | 1 |
| `extract-misc` | 16 | 30 | 0 | 46 |
| `invoice` | 1 | 0 | 0 | 1 |
| `remittance` | 0 | 2 | 0 | 2 |

## Top issues found

- `audience_clear` — 29 occurrence(s)
- `hook_strength` — 19 occurrence(s)
- `cross_vendor_framing` — 2 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-extract-commercial-invoice-remittance-fields-zh-hans/blog.html`
- `/repos/hyperapi-extract-commission-statement-header-fields/blog.html`
- `/repos/hyperapi-extract-construction-draw-fields/blog.html`
- `/repos/hyperapi-extract-corporate-card-fields/blog.html`
- `/repos/hyperapi-extract-credit-memo-header-fields/blog.html`
- `/repos/hyperapi-extract-credit-note-fields/blog.html`
- `/repos/hyperapi-extract-crypto-cost-basis-lots/blog.html`
- `/repos/hyperapi-extract-crypto-exchange-transaction-statement-fields/blog.html`
- `/repos/hyperapi-extract-customs-bond-coverage-fields/blog.html`
- `/repos/hyperapi-extract-derivative-margin-call-amounts/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.4ms | 21,600,000 |
| `comparative-study` | 0.5ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Approval rate is low (36%) — pause and review the rubric calibration with CEO before running round-24.