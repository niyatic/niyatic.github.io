# Human-review results — deterministic-editorial pass on 163 sample

- date: 2026-05-26
- sample size: 163
- method: 4-check deterministic editorial review (NOT live LLM judgment — sub-agent crashed on socket-close; this is the salvage pass with stronger-than-rubric structural checks)

## Verdict distribution

- ✅ approve: **0** (0.0%)
- ⚠ minor-fix: **163** (100.0%)
- ❌ template-bug: **0** (0.0%)

## Per-bucket failure rate (failures = minor-fix + template-bug)

| Bucket | Failures | Total in sample | Rate |
|---|---:|---:|---:|
| classify-misc | 71 | 71 | 100.0% |
| extract-misc | 43 | 43 | 100.0% |
| invoice | 16 | 16 | 100.0% |
| receipt | 14 | 14 | 100.0% |
| remittance | 7 | 7 | 100.0% |
| tax-1099 | 3 | 3 | 100.0% |
| credit_note | 1 | 1 | 100.0% |
| bank_statement | 1 | 1 | 100.0% |
| debit_note | 1 | 1 | 100.0% |
| cheque | 1 | 1 | 100.0% |
| packing_slip | 1 | 1 | 100.0% |
| payroll | 1 | 1 | 100.0% |
| bol | 1 | 1 | 100.0% |
| po | 1 | 1 | 100.0% |
| tax-w2 | 1 | 1 | 100.0% |

## Failure category breakdown

| Category | Count |
|---|---:|
| hook-missing | 163 |
| thin-body | 153 |

## Decision

❌ REVISE-RUBRIC — too many failures (163/163); fix the audience-tag + cross-vendor framing for the failing buckets before any external publish

## Honest limitations

- This is a **deterministic structural-+ editorial check**, NOT an LLM-as-judge. The original LLM-grade reviewer sub-agent crashed on socket-close after 9 min — this is the fallback.
- The 4 checks are: (a) math-derived hook present, (b) audience tag fits the doc-type bucket, (c) cross-vendor framing relevant to extraction (not pure classify), (d) body has ≥200 words.
- A real human editor sampling 5-8 random blogs is still the cleanest external-publish gate.
- The fixed-template fixes from earlier (#1 quantified-hook · #2 audience+framing) cover the structural gaps. This review catches the doc-type-MISMATCH-WITH-TEMPLATE issues that the structural rubric didn't.

## Top issues

- `hyperapi-classify-1099-int-vs-dividend-notice` · tax-1099 · minor-fix: hook-missing; thin-body (89 words)
- `hyperapi-classify-ach-return-vs-certificate-of-origin-ar` · classify-misc · minor-fix: hook-missing; thin-body (89 words)
- `hyperapi-classify-commercial-invoice-vs-cover-page-hi` · invoice · minor-fix: hook-missing; thin-body (89 words)
- `hyperapi-classify-commercial-invoice-vs-k1-schedule` · invoice · minor-fix: hook-missing; thin-body (89 words)
- `hyperapi-classify-construction-billing-document-type` · classify-misc · minor-fix: hook-missing; thin-body (173 words)
- `hyperapi-classify-construction-lien-waiver-type-zh-hans` · classify-misc · minor-fix: hook-missing; thin-body (173 words)
- `hyperapi-classify-contract-subtype-tr` · classify-misc · minor-fix: hook-missing; thin-body (177 words)
- `hyperapi-classify-credit-note-vs-debit-note-zh-hans` · credit_note · minor-fix: hook-missing; thin-body (89 words)
- `hyperapi-classify-debit-note-vs-bank-statement-it` · bank_statement · minor-fix: hook-missing; thin-body (89 words)
- `hyperapi-classify-debit-note-vs-cover-page-nl` · debit_note · minor-fix: hook-missing; thin-body (89 words)