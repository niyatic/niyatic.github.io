# Human review queue — 10% stratified sample

- date: 2026-05-26
- total live: 1650 blogs (all passed rubric pre-filter)
- sample: **163 blogs** (10% stratified by bucket)
- target: 1 reviewer × ~30 min total (~10-12 sec/blog spot-check)
- verdict signals: ✅ approve (publishable as-is) · ⚠ minor fix (publish after small edit) · ❌ template-bug (re-emit batch)

## Per-bucket sample sizes

| Bucket | Live | Sample | What to check |
|---|---:|---:|---|
| classify-misc | 710 | 71 | Is the doc-type pair coherent? Any irrelevant filler? |
| extract-misc | 432 | 43 | Are the field-extraction examples plausible? No customer-leakage? |
| invoice | 163 | 16 | Does the math-derived hook ring true? Any fabricated specifics? |
| receipt | 142 | 14 | Receipt-specific framing (POS / restaurant / retail) sound? |
| remittance | 79 | 7 | Remittance-advice framing distinct from invoice? |
| tax-1099 | 30 | 3 | IRS-form specifics correct? No customer SSN/EIN-like leakage? |
| po | 17 | 1 | PO-specific terms (line items / vendor / amount) accurate? |
| cheque | 16 | 1 | Cheque-specific (MICR / amount-in-words) sound? Not cfo-product? |
| credit_note | 15 | 1 | Credit-note vs invoice/debit-note distinction crisp? |
| bank_statement | 15 | 1 | Bank-statement framing generic (not cfo-nanoclaw-product)? |
| debit_note | 13 | 1 | Debit-note vs credit-note clarity? |
| payroll | 9 | 1 | Payroll generic (not cfo-product)? |
| bol | 4 | 1 | BoL-specific (carrier / weight / consignee) accurate? |
| tax-w2 | 3 | 1 | W-2 specifics correct? |
| packing_slip | 2 | 1 | Packing-slip terms accurate? |

## Sample blogs to review

| ✓ | # | Slug | Bucket | Reviewer-persona | Blog URL |
|:---:|---:|---|---|---|---|
| ☐ | 1 | `hyperapi-classify-1099-int-vs-dividend-notice` | tax-1099 | cfo-agents-shepherd | [open](https://niyatic.github.io/repos/hyperapi-classify-1099-int-vs-dividend-notice/blog.html) |
| ☐ | 2 | `hyperapi-classify-ach-return-vs-certificate-of-origin-ar` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-ach-return-vs-certificate-of-origin-ar/blog.html) |
| ☐ | 3 | `hyperapi-classify-commercial-invoice-vs-cover-page-hi` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-classify-commercial-invoice-vs-cover-page-hi/blog.html) |
| ☐ | 4 | `hyperapi-classify-commercial-invoice-vs-k1-schedule` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-classify-commercial-invoice-vs-k1-schedule/blog.html) |
| ☐ | 5 | `hyperapi-classify-construction-billing-document-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-construction-billing-document-type/blog.html) |
| ☐ | 6 | `hyperapi-classify-construction-lien-waiver-type-zh-hans` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-construction-lien-waiver-type-zh-hans/blog.html) |
| ☐ | 7 | `hyperapi-classify-contract-subtype-tr` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-contract-subtype-tr/blog.html) |
| ☐ | 8 | `hyperapi-classify-credit-note-vs-debit-note-zh-hans` | credit_note | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-credit-note-vs-debit-note-zh-hans/blog.html) |
| ☐ | 9 | `hyperapi-classify-debit-note-vs-bank-statement-it` | bank_statement | cfo-agents-shepherd | [open](https://niyatic.github.io/repos/hyperapi-classify-debit-note-vs-bank-statement-it/blog.html) |
| ☐ | 10 | `hyperapi-classify-debit-note-vs-cover-page-nl` | debit_note | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-debit-note-vs-cover-page-nl/blog.html) |
| ☐ | 11 | `hyperapi-classify-delivery-challan-vs-cover-page-it` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-delivery-challan-vs-cover-page-it/blog.html) |
| ☐ | 12 | `hyperapi-classify-delivery-challan-vs-cover-page-pt` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-delivery-challan-vs-cover-page-pt/blog.html) |
| ☐ | 13 | `hyperapi-classify-delivery-challan-vs-wire-confirmation-hi` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-delivery-challan-vs-wire-confirmation-hi/blog.html) |
| ☐ | 14 | `hyperapi-classify-delivery-challan-vs-wire-confirmation-it` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-delivery-challan-vs-wire-confirmation-it/blog.html) |
| ☐ | 15 | `hyperapi-classify-demurrage-vs-detention-charge` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-demurrage-vs-detention-charge/blog.html) |
| ☐ | 16 | `hyperapi-classify-derivative-confirmation-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-derivative-confirmation-type/blog.html) |
| ☐ | 17 | `hyperapi-classify-derivative-contract-type-ja` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-derivative-contract-type-ja/blog.html) |
| ☐ | 18 | `hyperapi-classify-derivative-contract-type-zh-hans` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-derivative-contract-type-zh-hans/blog.html) |
| ☐ | 19 | `hyperapi-classify-dividend-notice-vs-escrow-statement-ja` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-dividend-notice-vs-escrow-statement-ja/blog.html) |
| ☐ | 20 | `hyperapi-classify-document-fiscal-period` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-document-fiscal-period/blog.html) |
| ☐ | 21 | `hyperapi-classify-escrow-instruction-type-ru` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-escrow-instruction-type-ru/blog.html) |
| ☐ | 22 | `hyperapi-classify-escrow-release-condition-type-pt` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-escrow-release-condition-type-pt/blog.html) |
| ☐ | 23 | `hyperapi-classify-escrow-release-condition-type-ru` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-escrow-release-condition-type-ru/blog.html) |
| ☐ | 24 | `hyperapi-classify-escrow-statement-event-type-zh-hans` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-escrow-statement-event-type-zh-hans/blog.html) |
| ☐ | 25 | `hyperapi-classify-escrow-statement-period-ru` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-escrow-statement-period-ru/blog.html) |
| ☐ | 26 | `hyperapi-classify-escrow-statement-purpose-fr` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-escrow-statement-purpose-fr/blog.html) |
| ☐ | 27 | `hyperapi-classify-escrow-statement-vs-cover-page-it` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-escrow-statement-vs-cover-page-it/blog.html) |
| ☐ | 28 | `hyperapi-classify-escrow-statement-vs-cover-page-ru` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-escrow-statement-vs-cover-page-ru/blog.html) |
| ☐ | 29 | `hyperapi-classify-esg-disclosure-document-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-esg-disclosure-document-type/blog.html) |
| ☐ | 30 | `hyperapi-classify-expense-receipt-completeness-de` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-expense-receipt-completeness-de/blog.html) |
| ☐ | 31 | `hyperapi-classify-expense-receipt-completeness-ja` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-expense-receipt-completeness-ja/blog.html) |
| ☐ | 32 | `hyperapi-classify-expense-receipt-vs-statement-ar` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-expense-receipt-vs-statement-ar/blog.html) |
| ☐ | 33 | `hyperapi-classify-expense-receipt-vs-statement-ja` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-expense-receipt-vs-statement-ja/blog.html) |
| ☐ | 34 | `hyperapi-classify-expense-reimbursable-status-ar` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-expense-reimbursable-status-ar/blog.html) |
| ☐ | 35 | `hyperapi-classify-expense-report-vs-check-deposit-ar` | cheque | cfo-agents-shepherd | [open](https://niyatic.github.io/repos/hyperapi-classify-expense-report-vs-check-deposit-ar/blog.html) |
| ☐ | 36 | `hyperapi-classify-expense-travel-vs-nontravel` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-expense-travel-vs-nontravel/blog.html) |
| ☐ | 37 | `hyperapi-classify-expense-travel-vs-nontravel-ko` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-expense-travel-vs-nontravel-ko/blog.html) |
| ☐ | 38 | `hyperapi-classify-factoring-agreement-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-factoring-agreement-type/blog.html) |
| ☐ | 39 | `hyperapi-classify-fixed-asset-event-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-fixed-asset-event-type/blog.html) |
| ☐ | 40 | `hyperapi-classify-franchise-disclosure-section` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-franchise-disclosure-section/blog.html) |
| ☐ | 41 | `hyperapi-classify-freight-invoice-vs-lease-agreement-ar` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-classify-freight-invoice-vs-lease-agreement-ar/blog.html) |
| ☐ | 42 | `hyperapi-classify-fx-contract-type-de` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-fx-contract-type-de/blog.html) |
| ☐ | 43 | `hyperapi-classify-goods-receipt-condition-ja` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-goods-receipt-condition-ja/blog.html) |
| ☐ | 44 | `hyperapi-classify-goods-receipt-note-vs-delivery-challan-hi` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-goods-receipt-note-vs-delivery-challan-hi/blog.html) |
| ☐ | 45 | `hyperapi-classify-grain-contract-pricing-type-es` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-grain-contract-pricing-type-es/blog.html) |
| ☐ | 46 | `hyperapi-classify-grain-contract-pricing-type-fr` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-grain-contract-pricing-type-fr/blog.html) |
| ☐ | 47 | `hyperapi-classify-grain-contract-pricing-type-hi` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-grain-contract-pricing-type-hi/blog.html) |
| ☐ | 48 | `hyperapi-classify-grant-funding-document-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-grant-funding-document-type/blog.html) |
| ☐ | 49 | `hyperapi-classify-grant-letter-funding-stage` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-grant-letter-funding-stage/blog.html) |
| ☐ | 50 | `hyperapi-classify-grant-restriction-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-grant-restriction-type/blog.html) |
| ☐ | 51 | `hyperapi-classify-insurance-premium-document-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-insurance-premium-document-type/blog.html) |
| ☐ | 52 | `hyperapi-classify-intercompany-invoice-vs-cover-page` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-classify-intercompany-invoice-vs-cover-page/blog.html) |
| ☐ | 53 | `hyperapi-classify-invoice-subtype` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-classify-invoice-subtype/blog.html) |
| ☐ | 54 | `hyperapi-classify-invoice-vs-quote` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-classify-invoice-vs-quote/blog.html) |
| ☐ | 55 | `hyperapi-classify-journal-entry-vs-statement-of-account-ar` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-journal-entry-vs-statement-of-account-ar/blog.html) |
| ☐ | 56 | `hyperapi-classify-journal-entry-vs-statement-of-account-pt` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-journal-entry-vs-statement-of-account-pt/blog.html) |
| ☐ | 57 | `hyperapi-classify-lease-accounting-treatment` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-lease-accounting-treatment/blog.html) |
| ☐ | 58 | `hyperapi-classify-lease-agreement-vs-1099-int-ar` | tax-1099 | cfo-agents-shepherd | [open](https://niyatic.github.io/repos/hyperapi-classify-lease-agreement-vs-1099-int-ar/blog.html) |
| ☐ | 59 | `hyperapi-classify-lease-agreement-vs-1099-int-ko` | tax-1099 | cfo-agents-shepherd | [open](https://niyatic.github.io/repos/hyperapi-classify-lease-agreement-vs-1099-int-ko/blog.html) |
| ☐ | 60 | `hyperapi-classify-lease-agreement-vs-cover-page-ko` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-lease-agreement-vs-cover-page-ko/blog.html) |
| ☐ | 61 | `hyperapi-classify-lease-classification-finance-vs-operating-de` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-lease-classification-finance-vs-operating-de/blog.html) |
| ☐ | 62 | `hyperapi-classify-lease-incentive-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-lease-incentive-type/blog.html) |
| ☐ | 63 | `hyperapi-classify-ledger-account-normal-balance` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-ledger-account-normal-balance/blog.html) |
| ☐ | 64 | `hyperapi-classify-loan-collateral-status` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-loan-collateral-status/blog.html) |
| ☐ | 65 | `hyperapi-classify-loan-covenant-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-loan-covenant-type/blog.html) |
| ☐ | 66 | `hyperapi-classify-loan-repayment-structure` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-loan-repayment-structure/blog.html) |
| ☐ | 67 | `hyperapi-classify-margin-call-urgency` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-margin-call-urgency/blog.html) |
| ☐ | 68 | `hyperapi-classify-meter-reading-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-meter-reading-type/blog.html) |
| ☐ | 69 | `hyperapi-classify-packing-slip-vs-cover-page` | packing_slip | gtm-b2c-virality | [open](https://niyatic.github.io/repos/hyperapi-classify-packing-slip-vs-cover-page/blog.html) |
| ☐ | 70 | `hyperapi-classify-payment-run-priority` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-payment-run-priority/blog.html) |
| ☐ | 71 | `hyperapi-classify-payroll-register-vs-trade-confirmation` | payroll | cfo-agents-shepherd | [open](https://niyatic.github.io/repos/hyperapi-classify-payroll-register-vs-trade-confirmation/blog.html) |
| ☐ | 72 | `hyperapi-classify-pension-plan-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-pension-plan-type/blog.html) |
| ☐ | 73 | `hyperapi-classify-procurement-document-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-procurement-document-type/blog.html) |
| ☐ | 74 | `hyperapi-classify-promissory-note-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-promissory-note-type/blog.html) |
| ☐ | 75 | `hyperapi-classify-promissory-note-vs-cover-page` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-promissory-note-vs-cover-page/blog.html) |
| ☐ | 76 | `hyperapi-classify-purchase-order-vs-bill-of-lading` | bol | gtm-b2c-virality | [open](https://niyatic.github.io/repos/hyperapi-classify-purchase-order-vs-bill-of-lading/blog.html) |
| ☐ | 77 | `hyperapi-classify-receipt-merchant-category` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-receipt-merchant-category/blog.html) |
| ☐ | 78 | `hyperapi-classify-reinsurance-cession-document-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-reinsurance-cession-document-type/blog.html) |
| ☐ | 79 | `hyperapi-classify-revenue-arrangement-performance-obligation` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-revenue-arrangement-performance-obligation/blog.html) |
| ☐ | 80 | `hyperapi-classify-royalty-deduction-category` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-royalty-deduction-category/blog.html) |
| ☐ | 81 | `hyperapi-classify-royalty-statement-payer-role` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-royalty-statement-payer-role/blog.html) |
| ☐ | 82 | `hyperapi-classify-sales-tax-exemption-certificate-vs-blanket-po-release` | po | gtm-b2c-virality | [open](https://niyatic.github.io/repos/hyperapi-classify-sales-tax-exemption-certificate-vs-blanket-po-release/blog.html) |
| ☐ | 83 | `hyperapi-classify-scan-legibility` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-scan-legibility/blog.html) |
| ☐ | 84 | `hyperapi-classify-securities-corporate-action-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-securities-corporate-action-type/blog.html) |
| ☐ | 85 | `hyperapi-classify-statement-period-frequency` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-statement-period-frequency/blog.html) |
| ☐ | 86 | `hyperapi-classify-statement-period-monthly-quarterly` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-statement-period-monthly-quarterly/blog.html) |
| ☐ | 87 | `hyperapi-classify-tax-form-variant-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-tax-form-variant-type/blog.html) |
| ☐ | 88 | `hyperapi-classify-tax-invoice-vs-proforma` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-classify-tax-invoice-vs-proforma/blog.html) |
| ☐ | 89 | `hyperapi-classify-timesheet-vs-cover-page` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-timesheet-vs-cover-page/blog.html) |
| ☐ | 90 | `hyperapi-classify-title-commitment-vs-cover-page` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-title-commitment-vs-cover-page/blog.html) |
| ☐ | 91 | `hyperapi-classify-trade-finance-instrument-stage` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-trade-finance-instrument-stage/blog.html) |
| ☐ | 92 | `hyperapi-classify-treasury-confirmation-instrument-class` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-treasury-confirmation-instrument-class/blog.html) |
| ☐ | 93 | `hyperapi-classify-treasury-confirmation-product` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-treasury-confirmation-product/blog.html) |
| ☐ | 94 | `hyperapi-classify-vendor-onboarding-form-vs-cover-page` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-vendor-onboarding-form-vs-cover-page/blog.html) |
| ☐ | 95 | `hyperapi-classify-w2-wage-statement-vs-cover-page` | tax-w2 | cfo-agents-shepherd | [open](https://niyatic.github.io/repos/hyperapi-classify-w2-wage-statement-vs-cover-page/blog.html) |
| ☐ | 96 | `hyperapi-classify-warehouse-document-type` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-warehouse-document-type/blog.html) |
| ☐ | 97 | `hyperapi-classify-wire-transfer-purpose` | classify-misc | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-classify-wire-transfer-purpose/blog.html) |
| ☐ | 98 | `hyperapi-extract-1003-application-fields` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-1003-application-fields/blog.html) |
| ☐ | 99 | `hyperapi-extract-cash-pooling-statement-fields` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-cash-pooling-statement-fields/blog.html) |
| ☐ | 100 | `hyperapi-extract-certificate-of-origin-header-fields-it` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-certificate-of-origin-header-fields-it/blog.html) |
| ☐ | 101 | `hyperapi-extract-certificate-of-origin-remittance-fields-de` | remittance | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-certificate-of-origin-remittance-fields-de/blog.html) |
| ☐ | 102 | `hyperapi-extract-claims-bordereau-line-items` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-claims-bordereau-line-items/blog.html) |
| ☐ | 103 | `hyperapi-extract-closing-disclosure-fields-it` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-closing-disclosure-fields-it/blog.html) |
| ☐ | 104 | `hyperapi-extract-closing-disclosure-trid-fields-de` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-closing-disclosure-trid-fields-de/blog.html) |
| ☐ | 105 | `hyperapi-extract-closing-disclosure-trid-fields-ja` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-closing-disclosure-trid-fields-ja/blog.html) |
| ☐ | 106 | `hyperapi-extract-closing-disclosure-trid-fields-nl` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-closing-disclosure-trid-fields-nl/blog.html) |
| ☐ | 107 | `hyperapi-extract-cms-1500-claim-fields-ja` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-cms-1500-claim-fields-ja/blog.html) |
| ☐ | 108 | `hyperapi-extract-commercial-invoice-header-fields-ru` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-commercial-invoice-header-fields-ru/blog.html) |
| ☐ | 109 | `hyperapi-extract-commercial-lease-fields-es` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-commercial-lease-fields-es/blog.html) |
| ☐ | 110 | `hyperapi-extract-commercial-lease-fields-ko` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-commercial-lease-fields-ko/blog.html) |
| ☐ | 111 | `hyperapi-extract-equipment-lease-schedule-fields-it` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-equipment-lease-schedule-fields-it/blog.html) |
| ☐ | 112 | `hyperapi-extract-equipment-lease-schedule-fields-ko` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-equipment-lease-schedule-fields-ko/blog.html) |
| ☐ | 113 | `hyperapi-extract-escrow-analysis-amounts-ja` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-escrow-analysis-amounts-ja/blog.html) |
| ☐ | 114 | `hyperapi-extract-escrow-analysis-fields-es` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-escrow-analysis-fields-es/blog.html) |
| ☐ | 115 | `hyperapi-extract-escrow-analysis-fields-fr` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-escrow-analysis-fields-fr/blog.html) |
| ☐ | 116 | `hyperapi-extract-escrow-statement-key-fields-ar` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-escrow-statement-key-fields-ar/blog.html) |
| ☐ | 117 | `hyperapi-extract-escrow-statement-remittance-fields-it` | remittance | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-escrow-statement-remittance-fields-it/blog.html) |
| ☐ | 118 | `hyperapi-extract-escrow-statement-remittance-fields-zh-hans` | remittance | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-escrow-statement-remittance-fields-zh-hans/blog.html) |
| ☐ | 119 | `hyperapi-extract-expense-report-header-fields-pt` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-expense-report-header-fields-pt/blog.html) |
| ☐ | 120 | `hyperapi-extract-factoring-advance-fields` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-factoring-advance-fields/blog.html) |
| ☐ | 121 | `hyperapi-extract-freight-invoice-accessorials-ja` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-freight-invoice-accessorials-ja/blog.html) |
| ☐ | 122 | `hyperapi-extract-freight-invoice-accessorials-nl` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-freight-invoice-accessorials-nl/blog.html) |
| ☐ | 123 | `hyperapi-extract-freight-invoice-fields` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-freight-invoice-fields/blog.html) |
| ☐ | 124 | `hyperapi-extract-freight-invoice-header-fields` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-freight-invoice-header-fields/blog.html) |
| ☐ | 125 | `hyperapi-extract-freight-invoice-header-fields-de` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-freight-invoice-header-fields-de/blog.html) |
| ☐ | 126 | `hyperapi-extract-freight-invoice-header-fields-hi` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-freight-invoice-header-fields-hi/blog.html) |
| ☐ | 127 | `hyperapi-extract-freight-invoice-header-fields-ko` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-freight-invoice-header-fields-ko/blog.html) |
| ☐ | 128 | `hyperapi-extract-freight-invoice-remittance-fields-zh-hans` | invoice | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-freight-invoice-remittance-fields-zh-hans/blog.html) |
| ☐ | 129 | `hyperapi-extract-general-ledger-export-header-fields` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-general-ledger-export-header-fields/blog.html) |
| ☐ | 130 | `hyperapi-extract-general-ledger-export-remittance-fields` | remittance | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-general-ledger-export-remittance-fields/blog.html) |
| ☐ | 131 | `hyperapi-extract-goods-receipt-note-header-fields-de` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-goods-receipt-note-header-fields-de/blog.html) |
| ☐ | 132 | `hyperapi-extract-goods-receipt-note-header-fields-it` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-goods-receipt-note-header-fields-it/blog.html) |
| ☐ | 133 | `hyperapi-extract-goods-receipt-note-header-fields-nl` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-goods-receipt-note-header-fields-nl/blog.html) |
| ☐ | 134 | `hyperapi-extract-goods-receipt-note-header-fields-pt` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-goods-receipt-note-header-fields-pt/blog.html) |
| ☐ | 135 | `hyperapi-extract-goods-receipt-note-remittance-fields-ar` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-goods-receipt-note-remittance-fields-ar/blog.html) |
| ☐ | 136 | `hyperapi-extract-goods-receipt-note-remittance-fields-tr` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-goods-receipt-note-remittance-fields-tr/blog.html) |
| ☐ | 137 | `hyperapi-extract-goods-receipt-note-remittance-fields-zh-hans` | receipt | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-goods-receipt-note-remittance-fields-zh-hans/blog.html) |
| ☐ | 138 | `hyperapi-extract-indenture-redemption-terms` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-indenture-redemption-terms/blog.html) |
| ☐ | 139 | `hyperapi-extract-installment-loan-schedule-fields` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-installment-loan-schedule-fields/blog.html) |
| ☐ | 140 | `hyperapi-extract-insurance-binder-remittance-fields` | remittance | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-insurance-binder-remittance-fields/blog.html) |
| ☐ | 141 | `hyperapi-extract-interest-rate-swap-economics` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-interest-rate-swap-economics/blog.html) |
| ☐ | 142 | `hyperapi-extract-journal-entry-remittance-fields` | remittance | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-journal-entry-remittance-fields/blog.html) |
| ☐ | 143 | `hyperapi-extract-k1-partner-allocations` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-k1-partner-allocations/blog.html) |
| ☐ | 144 | `hyperapi-extract-lease-abstract-fields-ar` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-lease-abstract-fields-ar/blog.html) |
| ☐ | 145 | `hyperapi-extract-lease-agreement-header-fields-ru` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-lease-agreement-header-fields-ru/blog.html) |
| ☐ | 146 | `hyperapi-extract-lease-agreement-remittance-fields-it` | remittance | comparative-study | [open](https://niyatic.github.io/repos/hyperapi-extract-lease-agreement-remittance-fields-it/blog.html) |
| ☐ | 147 | `hyperapi-extract-lease-agreement-rent-escalation` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-lease-agreement-rent-escalation/blog.html) |
| ☐ | 148 | `hyperapi-extract-lease-agreement-rent-escalation-es` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-lease-agreement-rent-escalation-es/blog.html) |
| ☐ | 149 | `hyperapi-extract-lease-agreement-rent-escalation-fr` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-lease-agreement-rent-escalation-fr/blog.html) |
| ☐ | 150 | `hyperapi-extract-lease-cam-reconciliation-charges-fr` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-lease-cam-reconciliation-charges-fr/blog.html) |
| ☐ | 151 | `hyperapi-extract-lease-cam-reconciliation-charges-nl` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-lease-cam-reconciliation-charges-nl/blog.html) |
| ☐ | 152 | `hyperapi-extract-lease-escalation-schedule-es` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-lease-escalation-schedule-es/blog.html) |
| ☐ | 153 | `hyperapi-extract-lease-escalation-schedule-pt` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-lease-escalation-schedule-pt/blog.html) |
| ☐ | 154 | `hyperapi-extract-lease-incentive-schedule-fields-hi` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-lease-incentive-schedule-fields-hi/blog.html) |
| ☐ | 155 | `hyperapi-extract-lease-incentive-schedule-fields-ja` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-lease-incentive-schedule-fields-ja/blog.html) |
| ☐ | 156 | `hyperapi-extract-lease-termination-notice-fields-nl` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-lease-termination-notice-fields-nl/blog.html) |
| ☐ | 157 | `hyperapi-extract-letter-of-credit-terms` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-letter-of-credit-terms/blog.html) |
| ☐ | 158 | `hyperapi-extract-letter-of-indemnity-obligations` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-letter-of-indemnity-obligations/blog.html) |
| ☐ | 159 | `hyperapi-extract-loan-amortization-schedule` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-loan-amortization-schedule/blog.html) |
| ☐ | 160 | `hyperapi-extract-loan-payoff-figures` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-loan-payoff-figures/blog.html) |
| ☐ | 161 | `hyperapi-extract-money-market-confirmation` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-money-market-confirmation/blog.html) |
| ☐ | 162 | `hyperapi-extract-packing-list-net-gross-weight-tr` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-packing-list-net-gross-weight-tr/blog.html) |
| ☐ | 163 | `hyperapi-extract-pledge-agreement-collateral` | extract-misc | abm-content-marketing | [open](https://niyatic.github.io/repos/hyperapi-extract-pledge-agreement-collateral/blog.html) |

## Process

1. Click each [open] link; passphrase `hypercontent26`.
2. Spot-check the blog: does the math-derived hook make sense? Is the audience tag right? Is the cross-vendor framing accurate (without naming competitors)? Any factual oddities?
3. Check the ✓ box if approve, edit the row to `⚠` or `❌` if not.
4. Aggregate verdicts into a closing block at the bottom of this doc.

## Honest scope
- The rubric is **structural pre-filter** (presence/absence of patterns), not LLM editorial judgment.
- This 10% sample is the FIRST human gate before any of the 1,650 ship to external surfaces (LinkedIn, Hyperbots marketing site).
- If <5% of the sample fails → ship the batch. If >5% fails → revise rubric and re-run.

## Aggregate verdict
_(reviewer fills in)_
- approve: ___
- minor fix: ___
- template-bug: ___
- decision: SHIP / HOLD / REVISE-RUBRIC