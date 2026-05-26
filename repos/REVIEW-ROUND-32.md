# Review round-32 aggregate report

- date: 2026-05-26
- batch: next 50 (101-150) publish-ready (gate_pass=true) from queue-2026-05-25.jsonl
- wall-clock for round: 0.1s

## Headline

- Total reviewed: **50**
- Approved: **22** (44%)
- Hold-with-revisions: **28** (56%)
- Rejected: **0** (0%)

## Per-reviewer-persona breakdown

| Persona | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `abm-content-marketing` | 22 | 28 | 0 | 50 |

## Per-bucket breakdown

| Bucket | approve | hold | reject | total |
|---|---:|---:|---:|---:|
| `extract-misc` | 22 | 28 | 0 | 50 |

## Top issues found

- `audience_clear` — 16 occurrence(s)
- `hook_strength` — 13 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-extract-lease-termination-notice-fields/blog.html`
- `/repos/hyperapi-extract-lease-termination-notice-fields-ar/blog.html`
- `/repos/hyperapi-extract-lease-termination-notice-fields-de/blog.html`
- `/repos/hyperapi-extract-lease-termination-notice-fields-es/blog.html`
- `/repos/hyperapi-extract-lease-termination-notice-fields-fr/blog.html`
- `/repos/hyperapi-extract-lease-termination-notice-fields-hi/blog.html`
- `/repos/hyperapi-extract-lease-termination-notice-fields-it/blog.html`
- `/repos/hyperapi-extract-lease-termination-notice-fields-ja/blog.html`
- `/repos/hyperapi-extract-lease-termination-notice-fields-ko/blog.html`
- `/repos/hyperapi-extract-lease-termination-notice-fields-nl/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.4ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Approval rate is low (44%) — pause and review the rubric calibration with CEO before running round-32.