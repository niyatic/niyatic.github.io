# Review round-31 aggregate report

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

- `audience_clear` — 14 occurrence(s)
- `cross_vendor_framing` — 6 occurrence(s)
- `hook_strength` — 2 occurrence(s)

## First 10 approved-and-published blogs

- `/repos/hyperapi-extract-lease-agreement-rent-escalation/blog.html`
- `/repos/hyperapi-extract-lease-agreement-rent-escalation-ar/blog.html`
- `/repos/hyperapi-extract-lease-agreement-rent-escalation-de/blog.html`
- `/repos/hyperapi-extract-lease-agreement-rent-escalation-es/blog.html`
- `/repos/hyperapi-extract-lease-agreement-rent-escalation-fr/blog.html`
- `/repos/hyperapi-extract-lease-agreement-rent-escalation-hi/blog.html`
- `/repos/hyperapi-extract-lease-agreement-rent-escalation-it/blog.html`
- `/repos/hyperapi-extract-lease-agreement-rent-escalation-ja/blog.html`
- `/repos/hyperapi-extract-lease-agreement-rent-escalation-ko/blog.html`
- `/repos/hyperapi-extract-lease-agreement-rent-escalation-nl/blog.html`

## Per-persona time-per-blog (measured)

| Persona | avg s/blog | projected daily capacity (6h day) |
|---|---:|---:|
| `abm-content-marketing` | 0.3ms | 21,600,000 |
| `comparative-study` | 0.5ms | 21,600,000 |

## Honest framing

- Per-blog evaluation is rubric-deterministic and runs in milliseconds — the throughput ceiling is rubric-design + human spot-checks, not compute.
- The measured per-blog times above describe the rubric pass only; a human spot-check at ~10% sample is still recommended before any external publish.
- The competitor list used for the editorial double-check is representative, not exhaustive; partner-PII customer list is intentionally empty per v1.

## Recommended next action

- Approval rate is low (56%) — pause and review the rubric calibration with CEO before running round-31.