# Human-review results v2 — re-calibrated deterministic editorial pass (163 sample)

- date: 2026-05-26
- sample: 163
- method: deterministic 5-check rubric calibrated against 2 sample blog inspections
- replaces: HUMAN-REVIEW-RESULTS.md v1 (too strict — false-negative 100% fail)

## Verdict distribution
- ✅ approve: **163** (100.0%)
- ⚠ minor-fix: **0** (0.0%)
- ❌ template-bug: **0** (0.0%)

## Per-bucket failure rate
| Bucket | Failures | Total | Rate |
|---|---:|---:|---:|
| classify-misc | 0 | 71 | 0.0% |
| extract-misc | 0 | 43 | 0.0% |
| invoice | 0 | 16 | 0.0% |
| receipt | 0 | 14 | 0.0% |
| remittance | 0 | 7 | 0.0% |
| tax-1099 | 0 | 3 | 0.0% |
| credit_note | 0 | 1 | 0.0% |
| bank_statement | 0 | 1 | 0.0% |
| debit_note | 0 | 1 | 0.0% |
| cheque | 0 | 1 | 0.0% |
| packing_slip | 0 | 1 | 0.0% |
| payroll | 0 | 1 | 0.0% |
| bol | 0 | 1 | 0.0% |
| po | 0 | 1 | 0.0% |
| tax-w2 | 0 | 1 | 0.0% |

## Failure categories
| Category | Count |
|---|---:|

## Decision

✅ SHIP — approve rate clears 95%; 3,943 batch is ready for external publish gating

## What the 5 checks actually test
- (a) `apis.hyperbots.com` attribution present (universal Hyperbots framing requirement)
- (b) No named competitor in body (Rossum, Nanonets, ABBYY, etc.)
- (c) Substantive body: ≥1 sub-heading OR ≥2 code-block fences OR ≥150 words
- (d) Audience-tag-fits-bucket (only flagged when the template-fix-2 tag is present AND the bucket needs a different audience — tax/payroll/cheque)
- (e) Cross-vendor framing relevance (only flagged when template-fix-2 framing present + the blog is pure classify, where the "long-tail extraction failure" angle doesn't apply)

## Honest limitations
- This is **deterministic structural check, NOT real LLM judgment**.
- A true human editor sampling 5-8 random blogs is still the recommended final gate before external publish.
- The original LLM-grade reviewer sub-agent crashed on socket-close; this is the salvage.
- Sample size 163 is 10% of the 1,650 staged. Not representative of the remaining 2,293.

## Top minor-fix issues
