# Review round-28 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.0s

## Headline

- Total reviewed: **50**
- Approved: **16** (32%)
- Hold-with-revisions: **34** (68%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 15 | 6 | 0 | 21 |
| `comparative-study` | 1 | 28 | 0 | 29 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `extract-misc` | 5 | 6 | 0 | 11 |
| `invoice` | 10 | 0 | 0 | 10 |
| `receipt` | 1 | 27 | 0 | 28 |
| `remittance` | 0 | 1 | 0 | 1 |

## Top issues found

- `cross_vendor_framing` — 28 occurrence(s)
- `audience_clear` — 6 occurrence(s)
- `hook_strength` — 3 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-extract-freight-invoice-remittance-fields-fr/blog.html`
- `/repos/hyperapi-extract-freight-invoice-remittance-fields-hi/blog.html`
- `/repos/hyperapi-extract-freight-invoice-remittance-fields-it/blog.html`
- `/repos/hyperapi-extract-freight-invoice-remittance-fields-ja/blog.html`
- `/repos/hyperapi-extract-freight-invoice-remittance-fields-ko/blog.html`
- `/repos/hyperapi-extract-freight-invoice-remittance-fields-nl/blog.html`
- `/repos/hyperapi-extract-freight-invoice-remittance-fields-pt/blog.html`
- `/repos/hyperapi-extract-freight-invoice-remittance-fields-ru/blog.html`
- `/repos/hyperapi-extract-freight-invoice-remittance-fields-tr/blog.html`
- `/repos/hyperapi-extract-freight-invoice-remittance-fields-zh-hans/blog.html`

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

- Approval rate is low (32%) — pause and review the rubric calibration with CEO before running round-28.