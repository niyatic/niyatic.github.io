---
team: hyperapi-documentapi-benchmark-factory
kind: framework-spec
version: v1 (BUILD-v0)
date: 2026-06-11
bar: ParseBench (arXiv:2604.08538) / NeurIPS-paper bar — strictly higher than SAVIOR-Bench
predecessor: PARSE-DEEP-BENCHMARK-FRAMEWORK-2026-05-27.md (9 dimensions)
pre_registration: this document IS the pre-registration; per §1
approval: PENDING build-v0 review (chief-research-scientist + chief-architect + docs-techwriter + benchmark-format-steward)
plan_of_record: ../hyperapi-parse-x-research/command-center/plans/PARSE-FRAMEWORK-PLAN-2026-06-11.md
---

# Parse Deep Benchmark Framework — v1 (50 dimensions)

## §0 — Honest framing

We are researchers, not advocates. This framework is engineered to defensibly answer "is the HyperAPI parse primitive the best general parsing primitive across finance documents, on every measurement dimension that matters" — and to do so in a way that **succeeds whether parse wins or loses** on any given dimension. Manufacturing a positive result is forbidden; that is what the SAVIOR-Bench Appendix D 4-part cell contract (`provenance` · `pins` · `rerun_command` · `factory_reproduced`) and the comparative-study 8 invariants exist to prevent.

The bar is **ParseBench (arXiv:2604.08538) / NeurIPS-paper level**, strictly higher than SAVIOR-Bench. Concretely: pre-registration before any cell runs; per-doc score vectors for every CI; paired-bootstrap with Holm-Bonferroni multiplicity correction for cross-dimension claims; named ablations per ensemble; contamination + held-out audit per FT row; NeurIPS reproducibility checklist on every claim → rerunnable command. Cells that cannot be measured today stay PENDING-KEY / PENDING-SDK / PENDING-CORPUS — never fabricated, never silently filled.

Inheritance: this document **extends** `PARSE-DEEP-BENCHMARK-FRAMEWORK-2026-05-27.md` (9 dimensions D-OCR..D-COST-LATENCY) by adding 41 dimensions and renumbering all 50 into the D-01..D-50 namespace. No dimension from the 2026-05-27 spec is dropped; the bijection is preserved at §2.4.

## §1 — Pre-registration statement

This document **is** the pre-registration. The 50 per-dimension blocks in §3 each name a hypothesis (the directional claim the cell will be tested against), an acceptance criterion (the deterministic check that the cell meets the bar), and a rerunnable command stub (the canonical invocation). **No cell is reported as factory-reproduced until that command runs green under `repro_check.py`.** Every cell in the v0 leaderboard ships with one of three states: `registered-not-yet-run`, `running`, `green` (or `red` with the failure reason).

Pre-registration cuts off two failure modes that vendor benchmarks routinely commit: (a) silently tuning the metric to make the headline look better after the cells run, and (b) reporting the dimensions where the home team wins and quietly omitting the ones where it loses. Neither is possible here: the dimension list is fixed at 50 before any cell executes; the per-dimension headline winner is whoever the data names; and the comparative-study I-1 invariant (apples-to-apples) forces the same prompt + decoding-pin set across the panel for any dimension.

Drift policy: adding a 51st dimension after this document publishes requires a v1.1 amendment with its own pre-registration. Removing a dimension requires a written rationale + chief-research-scientist sign-off. Renumbering is forbidden after v1 ships.

## §2 — Reference benchmarks

### §2.1 — What we read

| Reference | What we take | Path |
|---|---|---|
| **ParseBench** (run-llama, arXiv:2604.08538, Apache-2.0) | Per-rule = per-doc-score-vector → CI computable; 5 splits / 169,011 rules; the publishability anchor | `command-center/PARSEBENCH-RECREATE-PLAN-2026-05-26.md`; `F-B-STUDY.html` |
| **SAVIOR-Bench v1** (Hyperbots, 2026) | 3-facet decoupling (transcription / extract / layout); F1–F10 failure taxonomy; non-waivable `[FT]` disclosure; Appendix D provenance contract; R1–R9 gap list | `paper/SAVIOR-Bench.md` (n=509, IAA 0.761) |
| **Azure DI invoice study** (Hyperbots, 2026) | Section depth + per-dimension block template + cell-level provenance display | `comparative/azure-di/azure-di-invoice-study.html` (1,842 LOC) |
| **Extend Parse 2.0 / RealDocBench** (Extend, 2026) | Vendor-schema-fidelity framing; ablation discipline; contrast (not head-to-head) | `comparative/parse-bench/gap-report-2026-05-27.md` |
| **OmniDocBench, OCRBench v2** (2024-2025) | Multi-format OCR; per-language stratification template | cited only |
| **DocVQA / DocVQA-NL** (Mathew et al., 2021) | ANLS metric for VQA-style extraction | cited |
| **FUNSD** (Adobe + Stanford, 2019) | KIE F1 + per-token bbox upstream | cited |
| **CORD** (Park et al., 2019) | Entity-level F1 + receipts canonical schema | cited |
| **PubTabNet → TEDS** (IBM, 2020) | Tree-Edit-Distance over Structure for tables | cited (existing TR-000 host) |
| **DocLayNet** (IBM, 2022) | Layout COCO-style mAP for 6 element classes | cited |
| **ChartQA** (Masry et al., 2022) | Chart-data-point-match accuracy | cited |
| **OLM-OCR / olmOCR-Bench** (AI2, 2025) | Open-license OCR baseline; mid-2025 vendor-attested | cited |
| **DewarpNet** (Das et al., 2019) | Dewarping quality benchmark | cited |
| **XFUND** (Microsoft, 2022) | Multilingual FUNSD (7 languages) | cited |
| **PARSE-DEEP-BENCHMARK-FRAMEWORK-2026-05-27.md** (ours) | The 9 base dimensions — extended not duplicated | benchmark-factory root |
| **DEEP-RESEARCH-PLAN.md** (ours) | 16-type doc taxonomy (T-01..T-16); A1–A10 axes; ensemble E1–E9 catalogue | `command-center/DEEP-RESEARCH-PLAN.md` |
| **CONSOLIDATED-150** (ours) | Cell schema (the per-cell JSON contract we inherit) | `leaderboard/CONSOLIDATED-150/CONSOLIDATED-150.md` |

### §2.2 — What we measure vs ParseBench / SAVIOR / RealDocBench

ParseBench is the **dataset-publishability anchor** (Apache-2.0, public, per-rule scoring → CIs). SAVIOR-Bench is the **discipline anchor** (3-facet, F1–F10, Appendix D, R8/R9 honest "not yet measured"). RealDocBench is the **contrast** — Extend's vendor-built benchmark, never run head-to-head from our harness because we hold no Extend API key (`PENDING-KEY` per `gap-report-2026-05-27.md`). The 50 dimensions in §3 cover and extend all three.

### §2.3 — Bar above SAVIOR

SAVIOR-Bench was attested-not-factory-reproduced (`ci95=null`, `n` null on parse-intent, corpus off-machine for the OCR panel). This framework lifts that bar: (1) every cell that ships a CI ships its per-doc score vector OR honest `null`; (2) every claim is rerunnable from a pinned command + seed; (3) every FT row passes a contamination audit before the leaderboard renders it green; (4) every ensemble claim is paired with the named ablation that isolates the lift. SAVIOR-Bench's R1–R9 gap list is treated as a punch-list, not a footnote — see §8 (contamination + held-out) and §10 (honest baselines).

### §2.4 — Bijection: the 9 D-* from 2026-05-27 → the 50 D-XX in this spec

| 2026-05-27 dimension | 2026-06-11 dimension(s) | Note |
|---|---|---|
| D-OCR | D-07 (OCR-RECALL) | renamed; metric unchanged |
| D-PARSE-INTENT | D-37 (PARSE-INTENT-F1) | renamed; metric unchanged |
| D-LAYOUT | D-23 (LAYOUT-ELEM-ACCURACY) | renamed; metric unchanged |
| D-BBOX | D-26 (BBOX-IOU-TOKEN) | renamed; metric unchanged |
| D-TABLE | D-31 (TABLE-GTRM) | renamed; metric unchanged |
| D-DOC-QUALITY | D-06 (IMG-JPEG-Q) + D-17 (DT-DENSITY) | split into two finer dimensions |
| D-LANG | D-20 (LANG-CER-PER-SCRIPT) | renamed; per-script extended to 10 scripts |
| D-DOWNSTREAM | D-36 (DOWNSTREAM-LIFT) | renamed; paired-bootstrap CI added per D-47 |
| D-COST-LATENCY | D-41 + D-42 + D-43 | split into LAT-P50 + LAT-P95-P99 + COST-DOLLAR-PER-CORRECT |

No 2026-05-27 dimension is dropped. Reviewers can verify by `grep -E 'D-OCR|D-PARSE-INTENT|D-LAYOUT|D-BBOX|D-TABLE|D-DOC-QUALITY|D-LANG|D-DOWNSTREAM|D-COST-LATENCY' PARSE-DEEP-BENCHMARK-FRAMEWORK-2026-05-27.md` and checking each lands at the named D-XX above.

## §3 — The 50 dimensions

Each block carries: **name · metric · hypothesis · acceptance criterion · gold needed · model-panel applicability · rerunnable command · CI policy · status**. The status `registered-not-yet-run` is the v0 default; cells flip to `green` only on `repro_check.py` pass.

### Category A — Image / scan quality (D-01..D-06)

#### D-01 — IMG-DPI
- **Metric**: `effective_dpi` (pixels-per-inch over text glyphs)
- **Hypothesis**: Models degrade non-linearly below 150 DPI; the 150/200/300 DPI strata produce statistically distinguishable CER deltas (paired-bootstrap, α=0.05/50).
- **Acceptance**: per-cell `effective_dpi` reported; CER delta vs 300 DPI baseline cited with CI.
- **Gold needed**: DPI-known scans (synthetic re-renders at 100/150/200/300 DPI).
- **Panel applicability**: all C* (with PDF rasterization) + all O* (local rasterization).
- **Rerunnable command**: `python harness/run.py --task DQ-001 --dataset img-dpi-strat-v1 --model <m> --seed 20260516`.
- **CI policy**: per-doc CER vector → bootstrap (resamples=2000, seed=20260516).
- **Status**: `registered-not-yet-run`.

#### D-02 — IMG-MTF
- **Metric**: `mtf_50_lp_mm` (line-pairs per mm at 50% modulation).
- **Hypothesis**: MTF below 6 lp/mm correlates with >5% CER inflation.
- **Acceptance**: per-cell MTF derived from glyph-edge spectrum.
- **Gold**: MTF chart insets per ISO 12233 OR synthetic Gaussian-blur strata.
- **Panel**: all OCR/VLM rows.
- **Command**: `python harness/run.py --task DQ-002 --dataset img-mtf-v1 --model <m> --seed 20260516`.
- **CI**: per-doc CER vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-03 — IMG-ILLUMINATION
- **Metric**: `illumination_uniformity_pct` (gradient-flatness).
- **Hypothesis**: Mobile-capture vignetting + uneven lighting degrade VLM bbox emission more than OCR pipeline transcription.
- **Acceptance**: per-cell illumination measured pre-OCR; CER + bbox-IoU delta reported per stratum.
- **Gold**: synthetic vignette renders + real mobile captures (partner-gated).
- **Panel**: VLM rows (Chandra, Qwen 3.6, Qwen 2.5-VL family) + OCR baseline (Tesseract).
- **Command**: `python harness/run.py --task DQ-003 --dataset img-illum-v1 --model <m> --seed 20260516`.
- **CI**: per-doc vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-04 — IMG-DEWARP
- **Metric**: `dewarp_rmse` (px, after engine's dewarp output vs gold flat).
- **Hypothesis**: Engines without explicit dewarp emission (Tesseract, raw OCR) degrade on curved-page scans more than VLMs.
- **Acceptance**: CER on raw curved-input vs after-dewarp reported separately; dewarp-residual RMSE cited.
- **Gold**: DewarpNet test split.
- **Panel**: Chandra, Marker, MinerU, Paddle-VL, all C* with explicit pre-process; Tesseract as baseline.
- **Command**: `python harness/run.py --task DQ-004 --dataset dewarpnet-test --model <m> --seed 20260516`.
- **CI**: per-doc RMSE vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-05 — IMG-SKEW
- **Metric**: `skew_recovery_pct` (CER delta after derotation at ±5°/±10°).
- **Hypothesis**: All models tolerate ±5° skew with <2% CER inflation; ±10° splits the panel.
- **Acceptance**: 0°/±5°/±10° triples reported per doc; deskew implicit or explicit noted.
- **Gold**: SAVIOR-Bench §10 R4 protocol (synthetic rotation).
- **Panel**: all OCR/VLM rows.
- **Command**: `python harness/run.py --task DQ-005 --dataset skew-strat-v1 --model <m> --seed 20260516`.
- **CI**: per-doc CER vector at each strata → bootstrap; paired-test 0° vs ±10°.
- **Status**: `registered-not-yet-run`.

#### D-06 — IMG-JPEG-Q (inherits D-DOC-QUALITY portion 1)
- **Metric**: `cer_delta_q40_vs_q90` (JPEG-Q degradation tolerance).
- **Hypothesis**: Q40 degradation > 5% CER inflation differentiates production-grade OCR from research VLMs.
- **Acceptance**: Q40/Q60/Q90 triples per doc; "Hyperbots-IP fine-tunes degrade gracefully" claim tested or refuted.
- **Gold**: synthetic Q-LOW/MED/HIGH renders over ParseBench docs (Apache-2.0-clean).
- **Panel**: all rows.
- **Command**: `python harness/run.py --task DQ-006 --dataset jpeg-q-strat-v1 --model <m> --seed 20260516`.
- **CI**: per-doc CER vector per Q-stratum → bootstrap.
- **Status**: `registered-not-yet-run`.

### Category B — Text / transcription (D-07..D-12)

#### D-07 — OCR-RECALL (inherits D-OCR)
- **Metric**: `savior_word_recall` (multiset; refactored from vlm_ocr@1fbbc334).
- **Hypothesis**: Recall on the SAVIOR-Bench corpus correlates with downstream extract F1 (per D-36); Pearson ≥ 0.6.
- **Acceptance**: per-cell recall computed; correlation tested at 95% CI.
- **Gold**: SAVIOR-Bench 509-doc corpus (BLK-18: corpus off-disk; PENDING) + ParseBench text_content where gold transcript reconstructable.
- **Panel**: all OCR/VLM rows. **SAVIOR-Train rows are `[FT]` per I-4** (modesty anchor: best documented zero-shot).
- **Command**: `python harness/run_pairs_allmodels.py --metric recall --dataset savior-v1 --model <m> --seed 20260516`.
- **CI**: per-doc recall vector → bootstrap (resamples=2000, seed=20260516).
- **Status**: `registered-not-yet-run` (corpus-blocked; see BLK-18).

#### D-08 — OCR-PRECISION
- **Metric**: `savior_word_precision` (multiset).
- **Hypothesis**: Precision differentiates hallucinating VLMs from transcription-faithful OCR pipelines; gap ≥ 0.15 between worst-VLM and Tesseract.
- **Acceptance**: per-cell precision computed + hallucinated-token count reported.
- **Gold**: SAVIOR-Bench corpus (PENDING per BLK-18).
- **Panel**: all OCR/VLM rows.
- **Command**: `python harness/run_pairs_allmodels.py --metric precision --dataset savior-v1 --model <m>`.
- **CI**: per-doc precision vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-09 — OCR-EDIT-DISTANCE
- **Metric**: `ocr_edit_distance` (Levenshtein-normalized, ↓ better).
- **Hypothesis**: Edit-distance ranking on a held-out set within ±2 ranks of the SAVIOR-Bench 31-system attested ranking (validates the panel is well-formed).
- **Acceptance**: rank-correlation (Spearman) ≥ 0.85 vs the attested ranking.
- **Gold**: 31-system attested SAVIOR + held-out 50-doc augmentation.
- **Panel**: all OCR/VLM rows.
- **Command**: `python harness/run.py --task DQ-009 --dataset ocr-edit-dist-v1 --model <m>`.
- **CI**: per-doc edit-distance vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-10 — OCR-WER
- **Metric**: `wer` (word-error rate).
- **Hypothesis**: WER and edit-distance disagree on rank order on dense pages (insert/delete cost asymmetry).
- **Acceptance**: per-doc WER + rank deviation vs D-09 reported.
- **Gold**: same as D-09.
- **Panel**: all OCR/VLM rows.
- **Command**: `python harness/run.py --task DQ-010 --dataset ocr-wer-v1 --model <m>`.
- **CI**: per-doc WER vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-11 — OCR-CER
- **Metric**: `cer` (character-error rate; primary for ZH/JA/KO/AR).
- **Hypothesis**: CER ranks differ from WER for non-EN scripts; the gap widens for character-script languages.
- **Acceptance**: per-script CER table; ZH/JA/KO/AR explicitly broken out.
- **Gold**: XFUND + native partner corpora (D-21 gated).
- **Panel**: all OCR/VLM rows.
- **Command**: `python harness/run.py --task DQ-011 --dataset ocr-cer-multiscript --model <m>`.
- **CI**: per-doc CER vector per script → bootstrap.
- **Status**: `registered-not-yet-run` (partner-corpus-gated for ZH/JA/AR).

#### D-12 — OCR-DIGIT-MICR-FIDELITY
- **Metric**: `digit_micr_fidelity_f1`.
- **Hypothesis**: F-B smoke (2026-05-28) finding holds at n=100: literal OCR (Tesseract 0.793) + Qwen 3.6 (0.859) beat structure-busy Chandra (0.455) on `bag_of_digit_percent`. **The dumb-tool-wins finding survives scaling.**
- **Acceptance**: per-cell `bag_of_digit_percent` reported; the Chandra-vs-Tesseract gap explicitly cited.
- **Gold**: ParseBench text_content `bag_of_digit_percent` rules + tough-bench bank-statement + cheque + invoice.
- **Panel**: all OCR/VLM rows. **Headline-finding-validation dimension.**
- **Command**: `python harness/run.py --task DQ-012 --dataset digit-fidelity-v1 --model <m> --seed 20260516`.
- **CI**: per-doc fidelity vector → bootstrap; paired-test Chandra vs Tesseract.
- **Status**: `registered-not-yet-run`.

### Category C — Document type stratification (D-13..D-19)

Each is a per-type stratification contract: every leaderboard row reports the primary metric stratified by these doc-types (not a separate scoring rule). The hypothesis is per-type-specific; the acceptance is per-cell-row reporting.

#### D-13 — DT-AP-AR
- **Metric**: per-type F1 over {T-01 invoice, T-02 credit note, T-03 PO, T-04 packing slip, T-05 BoL, T-06 remittance}.
- **Hypothesis**: AP/AR is HyperAPI's home turf; the HyperAPI parse row's per-type F1 on T-01/T-02/T-05/T-06 ≥ best zero-shot non-Hyperbots row.
- **Acceptance**: per-type F1 table per row; HyperAPI-vs-best-zero-shot gap reported with CI; honest if HyperAPI loses.
- **Gold**: tough-bench {T-02, T-05, T-06, T-07, T-08} + dataset_95 (T-01) + financepss-205 (mixed AP).
- **Panel**: all rows.
- **Command**: `python harness/run.py --task DQ-013 --dataset ap-ar-v1 --model <m>`.
- **CI**: per-doc field-F1 vector per type → bootstrap.
- **Status**: `registered-not-yet-run` (T-09/T-10 partner-gated; reported separately).

#### D-14 — DT-PAYMENTS
- **Metric**: per-type F1 over {T-07 bank statement, T-08 cheque, T-09 pay stub, T-10 wire/ACH}.
- **Hypothesis**: MICR + digit-fidelity (D-12) dominates payments dimension; Tesseract competitive with VLMs on T-07/T-08.
- **Acceptance**: per-type F1 + per-field accuracy (MICR-line, account-number, routing) reported.
- **Gold**: tough-bench {T-07, T-08} + partner (T-09, T-10).
- **Panel**: all rows.
- **Command**: `python harness/run.py --task DQ-014 --dataset payments-v1 --model <m>`.
- **CI**: per-doc vector → bootstrap.
- **Status**: `registered-not-yet-run` (T-09/T-10 partner-gated).

#### D-15 — DT-CAPITAL-MARKETS
- **Metric**: per-type F1 over {T-11 10-Q, T-12 investor presentation, T-13 tax form}.
- **Hypothesis**: HyperAPI IDP doc-type set excludes T-11/T-12 → HyperAPI's per-type F1 on T-11 is expected-fail (Q-DR-5 to CEO); the framework honestly reports the gap rather than skip the dimension.
- **Acceptance**: per-type F1 reported even where HyperAPI's column is null (with `_status: out-of-doc-type-set`).
- **Gold**: EDGAR-pulled 10-Q (Apache-2.0-equivalent public-domain) + IRS blank tax forms + synthetic-fill.
- **Panel**: all rows; HyperAPI parse declared out-of-set per Q-DR-5.
- **Command**: `python harness/run.py --task DQ-015 --dataset capmkts-v1 --model <m>`.
- **CI**: per-doc vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-16 — DT-ADJACENT
- **Metric**: per-type F1 over {T-14 insurance, T-15 loan, T-16 form/FUNSD}.
- **Hypothesis**: FUNSD-trained KIE models outperform general VLMs on T-16; T-14/T-15 partner-gated.
- **Acceptance**: per-type F1; KIE-trained-vs-general split reported.
- **Gold**: FUNSD upstream (T-16) + partner (T-14, T-15).
- **Panel**: all rows.
- **Command**: `python harness/run.py --task DQ-016 --dataset adjacent-v1 --model <m>`.
- **CI**: per-doc vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-17 — DT-DENSITY (inherits D-DOC-QUALITY portion 2)
- **Metric**: per-density-slice metric over {P-DENSE, P-NORMAL, P-SPARSE}.
- **Hypothesis**: Dense layouts (P-DENSE) widen the Chandra-vs-Qwen gap on layout/table dimensions and narrow it on text dimensions.
- **Acceptance**: per-doc token-density computed; per-density-stratum metric reported.
- **Gold**: ParseBench corpus binned by measured density.
- **Panel**: all rows.
- **Command**: `python harness/run.py --task DQ-017 --dataset density-strat-v1 --model <m>`.
- **CI**: per-doc vector per density → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-18 — DT-MULTI-COL
- **Metric**: multi-column layout F1.
- **Hypothesis**: Column-recovery is the long-doc T-11 failure mode; engines without explicit column detection score < 0.5.
- **Acceptance**: per-doc column-recovery F1; column-count error rate reported.
- **Gold**: 10-Q + investor-presentation pages (manually-annotated 50-doc seed).
- **Panel**: all rows.
- **Command**: `python harness/run.py --task DQ-018 --dataset multicol-v1 --model <m>`.
- **CI**: per-doc vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-19 — DT-NESTED-TABLE
- **Metric**: nested-table cell-F1.
- **Hypothesis**: Nested tables (table-in-table) are sub-1% baseline-prevalence but dominant in 10-Q financial schedules; Chandra's HTML emission gives it the largest single-model lead.
- **Acceptance**: per-doc nested-cell F1; the 10-Q + ParseBench-table-split nested subset reported.
- **Gold**: ParseBench table split + manually-annotated 10-Q financial schedules.
- **Panel**: all rows.
- **Command**: `python harness/run.py --task DQ-019 --dataset nested-table-v1 --model <m>`.
- **CI**: per-doc vector → bootstrap.
- **Status**: `registered-not-yet-run`.

### Category D — Language / script (D-20..D-22)

#### D-20 — LANG-CER-PER-SCRIPT (inherits D-LANG)
- **Metric**: per-script CER over {EN, DE, FR, ES, ZH-Hans, ZH-Hant, JA, KO, AR, HI}.
- **Hypothesis**: SAVIOR-Bench residual F9 (multilingual + very-dense cluster persists post-FT) holds at our scale; Hyperbots-IP `[FT]` rows do not close the ZH-Hans / JA / AR gap.
- **Acceptance**: per-script CER with CI; the F9 cluster persistence claim either confirmed or refuted.
- **Gold**: XFUND public (EN/DE/FR/ES/ZH/JA) + native partner annotation (KO/AR/HI).
- **Panel**: all rows.
- **Command**: `python harness/run.py --task DQ-020 --dataset lang-cer-multiscript --model <m>`.
- **CI**: per-doc CER vector per script → bootstrap.
- **Status**: `registered-not-yet-run` (KO/AR/HI partner-gated).

#### D-21 — LANG-KIE-XFUND
- **Metric**: KIE F1 on XFUND (7 languages).
- **Hypothesis**: XFUND F1 correlates with CER per script (D-20) but only after structural-OCR threshold; below it F1 is noise.
- **Acceptance**: per-language F1 + the F1-vs-CER correlation reported.
- **Gold**: XFUND public.
- **Panel**: all KIE-capable rows.
- **Command**: `python harness/run.py --task DQ-021 --dataset xfund-v1 --model <m>`.
- **CI**: per-doc F1 vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-22 — LANG-MIXED-SCRIPT
- **Metric**: CER on code-switch pages (EN+ZH, EN+AR).
- **Hypothesis**: Code-switch CER > single-script CER for both scripts (worse than the harder of the two).
- **Acceptance**: per-doc mixed-script CER; the "worse than both" claim tested.
- **Gold**: partner-curated mixed-script corpus (50-doc seed).
- **Panel**: all rows.
- **Command**: `python harness/run.py --task DQ-022 --dataset mixed-script-v1 --model <m>`.
- **CI**: per-doc CER vector → bootstrap.
- **Status**: `registered-not-yet-run` (partner-gated).

### Category E — Density / layout complexity (D-23..D-25)

#### D-23 — LAYOUT-ELEM-ACCURACY (inherits D-LAYOUT)
- **Metric**: `layout_element_accuracy` (per-element class match against gold tree).
- **Hypothesis**: Chandra's native `data-label` emission gives it the per-element accuracy lead; Qwen + Tesseract floor.
- **Acceptance**: per-doc element-F1 + per-class breakdown; F-B smoke (2026-05-28) finding (Chandra 0.100 / Qwen 0.000 / Tesseract 0.000 at n=10) re-anchored at n=100.
- **Gold**: ParseBench layout split (16,325 rules).
- **Panel**: all rows; only Chandra + Surya + DOTS + Paddle-VL expected non-zero by construction.
- **Command**: `python3.11 harness/run_parsebench.py --split layout --model <m> --n 100`.
- **CI**: per-rule pass vector → bootstrap (per-rule = per-doc here).
- **Status**: `registered-not-yet-run`.

#### D-24 — LAYOUT-READING-ORDER
- **Metric**: `reading_order_accuracy` (normalized rank correlation).
- **Hypothesis**: Reading-order accuracy is the secondary layout signal; on multi-column docs (D-18) it decorrelates from element accuracy.
- **Acceptance**: per-doc reading-order rank-correlation; D-23 vs D-24 decorrelation reported on multi-column subset.
- **Gold**: ParseBench layout split + READ benchmark subset.
- **Panel**: all bbox-emitting rows.
- **Command**: `python harness/run.py --task DQ-024 --dataset reading-order-v1 --model <m>`.
- **CI**: per-doc rank-correlation vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-25 — LAYOUT-PAIRS (PC-only secondary)
- **Metric**: `pairs_layout` z-euclidean (vendored from vlm_ocr@1fbbc334 → `harness/metrics/vlm_ocr/pairs.py`).
- **Hypothesis**: PaIRS rank order on the PC subset (prompt-controlled models only) tracks D-23 within ±2 ranks.
- **Acceptance**: per-doc PaIRS reported with `pairs_cat: PC | NPC` flag; PC-only rank comparison cited.
- **Gold**: SAVIOR-Bench corpus (BLK-18 PENDING) + ParseBench table split (gold expected_markdown available).
- **Panel**: PC subset of all OCR/VLM rows. **Label PC vs NPC machine-readably; never cross-compare.**
- **Command**: `python3.11 harness/run_pairs_allmodels.py 100` (ParseBench table) + `harness/run_pairs_savior.py --root <SAVIOR>` (when BLK-18 clears).
- **CI**: per-doc PaIRS vector per category → bootstrap.
- **Status**: `registered-not-yet-run` (BLK-17 Chandra-host + BLK-18 corpus blockers).

### Category F — Computer-vision metrics (D-26..D-30)

#### D-26 — BBOX-IOU-TOKEN (inherits D-BBOX)
- **Metric**: `bbox_iou` mean over matched tokens (matched-token alignment first, then IoU on bounding regions).
- **Hypothesis**: Token-bbox IoU separates engines that emit per-token boxes (Chandra, Tesseract, Surya) from those that don't (Qwen 3.6, Claude). The latter floor at 0.
- **Acceptance**: per-doc mean IoU + match-rate (tokens-matched/tokens-gold).
- **Gold**: Inv3D upstream + FUNSD upstream + PyMuPDF silver on digital PDFs (per `BBOX-SILVER-PIPELINE-SPEC.md`).
- **Panel**: all bbox-emitting rows.
- **Command**: `python harness/run.py --task DQ-026 --dataset bbox-iou-token-v1 --model <m>`.
- **CI**: per-doc IoU vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-27 — BBOX-FIELD-TO-REGION
- **Metric**: `field_to_region_grounding_accuracy` at IoU ≥ 0.5.
- **Hypothesis**: Field-to-region grounding is downstream-extract-conditional; models with high D-07 recall but low D-27 grounding still produce strong D-36 lift because the extractor compensates.
- **Acceptance**: per-doc grounding accuracy; D-36 lift conditional on D-27 reported.
- **Gold**: ParseBench layout split + FUNSD.
- **Panel**: all bbox + field-emitting rows.
- **Command**: `python harness/run.py --task DQ-027 --dataset field-region-v1 --model <m>`.
- **CI**: per-doc accuracy vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-28 — LAYOUT-COCO-mAP
- **Metric**: COCO-style mAP@.5/.75/.95 over the 6 DocLayNet classes.
- **Hypothesis**: COCO-mAP differentiates models trained on DocLayNet (Surya, MinerU) from general VLMs.
- **Acceptance**: per-class AP table; mAP-overall + per-area-AP-S/M/L reported.
- **Gold**: DocLayNet public test split.
- **Panel**: all layout-emitting rows.
- **Command**: `python harness/run.py --task DQ-028 --dataset doclaynet-v1 --model <m>`.
- **CI**: per-doc AP vector → bootstrap; class-stratified.
- **Status**: `registered-not-yet-run`.

#### D-29 — SEG-IOU
- **Metric**: pixel-IoU on figure + table region segmentation.
- **Hypothesis**: Segmentation IoU is a stricter signal than bbox-IoU; ranks differ on docs with curved tables.
- **Acceptance**: per-doc seg-IoU; the bbox-vs-seg rank-deviation reported.
- **Gold**: DocLayNet seg masks (public).
- **Panel**: layout-emitting + seg-capable rows.
- **Command**: `python harness/run.py --task DQ-029 --dataset seg-iou-v1 --model <m>`.
- **CI**: per-doc IoU vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-30 — VLM-PAGE-IMAGE-FIDELITY
- **Metric**: pixel-level reconstruction quality when the engine emits a rendered page (PSNR + SSIM).
- **Hypothesis**: Engines that emit synthesized renders (some VLM pipelines) trade fidelity for structure; the trade is measurable and cell-specific.
- **Acceptance**: PSNR + SSIM reported only when engine outputs an image; "did-not-emit" cells flagged `n/a` not zero.
- **Gold**: digital PDF render-compare (deterministic).
- **Panel**: only engines that emit a rendered surface (subset of C* + O*).
- **Command**: `python harness/run.py --task DQ-030 --dataset page-render-fidelity-v1 --model <m>`.
- **CI**: per-doc PSNR + SSIM vectors → bootstrap.
- **Status**: `registered-not-yet-run`.

### Category G — Enterprise document AI (D-31..D-36)

#### D-31 — TABLE-GTRM (inherits D-TABLE; CROSS-FAMILY: TR-000 pin)
- **Metric**: GTRM (GriTS + TableRecordMatch combined, per ParseBench README).
- **Hypothesis**: Chandra wins GriTS on ParseBench table (F-B smoke 0.800 at n=10) — re-anchored at n=100 with CI.
- **Acceptance**: per-rule GriTS + TableRecordMatch + the combined GTRM reported; Chandra-vs-others gap with CI.
- **Gold**: ParseBench table split (503 rules) + PubTabNet test.
- **Panel**: all table-emitting rows. **NOTE: D-31 runs under TR-000 family pins (T=0.0, top_p=1.0, max_tokens=4096), not parse-deep pins → cell row tagged `apples-to-oranges` per I-1.**
- **Command**: `python3.11 harness/run_parsebench.py --split table --model <m> --n 100`.
- **CI**: per-rule GriTS vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-32 — TABLE-TEDS
- **Metric**: Tree-Edit-Distance over Structure (TEDS).
- **Hypothesis**: TEDS and GTRM rank-correlate ≥ 0.85; disagreement isolates structural-only failures.
- **Acceptance**: per-table TEDS + rank-correlation reported.
- **Gold**: PubTabNet public.
- **Panel**: all table-emitting rows.
- **Command**: `python harness/run.py --task DQ-032 --dataset pubtabnet-v1 --model <m>`.
- **CI**: per-table TEDS vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-33 — TABLE-CELL-F1
- **Metric**: per-cell content F1 (cells matched first, then content compared).
- **Hypothesis**: Content-cell-F1 is more buyer-relevant than structural metrics; differentiates the Hyperbots-IP fine-tune.
- **Acceptance**: per-cell F1 + per-row-type breakdown (header / data / total).
- **Gold**: financepss-205 + tough-bench bank statement.
- **Panel**: all table-emitting rows.
- **Command**: `python harness/run.py --task DQ-033 --dataset table-cell-f1-v1 --model <m>`.
- **CI**: per-doc F1 vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-34 — KIE-FUNSD-F1
- **Metric**: entity-level F1 on FUNSD.
- **Hypothesis**: FUNSD-trained KIE models lead; general VLMs catch up via prompt engineering on header/question/answer/other entities.
- **Acceptance**: per-entity F1; prompt-engineering vs trained-KIE gap reported.
- **Gold**: FUNSD public.
- **Panel**: all KIE-capable rows.
- **Command**: `python harness/run.py --task DQ-034 --dataset funsd-v1 --model <m>`.
- **CI**: per-doc F1 vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-35 — KIE-CORD-F1
- **Metric**: entity-level F1 on CORD receipts.
- **Hypothesis**: CORD is the receipt-canonical-schema test; Hyperbots `[FT]` rows benefit from receipt overlap with SAVIOR-Train.
- **Acceptance**: per-doc F1; contamination-audit citation per D-50.
- **Gold**: CORD public.
- **Panel**: all KIE-capable rows.
- **Command**: `python harness/run.py --task DQ-035 --dataset cord-v1 --model <m>`.
- **CI**: per-doc F1 vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-36 — DOWNSTREAM-LIFT (inherits D-DOWNSTREAM; CEO-required dimension; CROSS-FAMILY: extract pin)
- **Metric**: `parse_lift = downstream_extract_micro_f1(parse + extract) − no_parse_extract_micro_f1(image → extract)`.
- **Hypothesis**: HyperAPI parse contributes positive lift on T-01 (invoice) when the downstream extractor is fixed (Qwen 3.6-35B-A3B); the lift collapses on T-11 (10-Q) — the doc-type out-of-set boundary.
- **Acceptance**: paired-bootstrap CI on lift (per D-47); per-doc lift vector; `extractor_pin` named in cell.
- **Gold**: dataset_95 + tough-bench + financepss-205; extractor pinned at Qwen 3.6-35B-A3B (Hyperbots-IP `[FT]`).
- **Panel**: all parse-capable rows; downstream extractor pinned cross-row for apples-to-apples lift.
- **Command**: `python harness/run.py --task DQ-036 --dataset downstream-lift-v1 --model <m> --extractor qwen36-a3b`.
- **CI**: paired-bootstrap on per-doc lift vector (resamples=2000, seed=20260516).
- **Status**: `registered-not-yet-run`. **CROSS-FAMILY apples-to-oranges flag per I-1; extractor pin documented in cell.**

### Category H — NLP / semantic (D-37..D-40)

#### D-37 — PARSE-INTENT-F1 (inherits D-PARSE-INTENT)
- **Metric**: `parse_intent_f1`.
- **Hypothesis**: hyperapi-parse-intent `[FT]` row ranks ≥ best documented zero-shot (per SAVIOR-Bench §5.1.1 attested 0.8328 vs GPT-4o 0.8052 modesty anchor); factory-reproduction restores per-doc score vector + CI.
- **Acceptance**: per-doc parse-intent F1 + WER; modesty-anchor explicitly cited; FT-vs-zero-shot delta with CI.
- **Gold**: parse-intent-inhouse-v1 (corpus-restoration PENDING).
- **Panel**: all parse-intent-capable rows.
- **Command**: `python harness/run.py --task DQ-037 --dataset parse-intent-v1 --model <m>`.
- **CI**: per-doc F1 + WER vector → bootstrap.
- **Status**: `registered-not-yet-run` (per-doc vector recovery PENDING per BLK-3).

#### D-38 — VQA-ANLS
- **Metric**: ANLS on DocVQA.
- **Hypothesis**: VLM rows lead ANLS; OCR pipelines floor; the gap is a buyer-signal for VQA-style workloads.
- **Acceptance**: per-question ANLS; question-type breakdown (extractive / numeric / lookup).
- **Gold**: DocVQA public test.
- **Panel**: all rows.
- **Command**: `python harness/run.py --task DQ-038 --dataset docvqa-v1 --model <m>`.
- **CI**: per-question ANLS vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-39 — SEMANTIC-BERTSCORE
- **Metric**: BERTScore on free-text / summary outputs.
- **Hypothesis**: BERTScore differentiates content-faithful vs hallucinating engines beyond what CER/recall capture.
- **Acceptance**: per-doc BERTScore F1 + content-faithfulness correlation.
- **Gold**: 10-Q section summaries (synthetic baseline) + dataset_95 vendor-name reformulations.
- **Panel**: all summary-capable rows.
- **Command**: `python harness/run.py --task DQ-039 --dataset bertscore-v1 --model <m>`.
- **CI**: per-doc BERTScore vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-40 — INTENT-CLASSIFICATION
- **Metric**: per-doc-type classification F1 (the `classify` primitive's accuracy).
- **Hypothesis**: HyperAPI `classify` (already at 100% on tough-cheque, 96.7% on credit-note, 87.1% on remittance per Subagent A landings) holds at scale; the 87.1% remittance score is the loose end.
- **Acceptance**: per-doc-type classification F1 with CI; the remittance ceiling explicitly tested.
- **Gold**: tough-bench + dataset_95 type-labels.
- **Panel**: all classify-capable rows.
- **Command**: `python harness/run.py --task DQ-040 --dataset classify-v1 --model <m>`.
- **CI**: per-doc accuracy vector → bootstrap.
- **Status**: `registered-not-yet-run` (BLK-16: HyperAPI quota — gated for HyperAPI column).

### Category I — Print / production (D-41..D-45)

#### D-41 — LAT-P50 (inherits D-COST-LATENCY portion 1)
- **Metric**: `latency_p50_ms` (median per-page latency).
- **Hypothesis**: Chandra (~8–22s) and Qwen (~5–15s) latencies are the buyer-bottleneck for ensemble routing; the latency tax is 2–3× single-model.
- **Acceptance**: per-cell p50 + the ensemble latency budget (single + chained) reported.
- **Gold**: observed per-cell.
- **Panel**: all rows.
- **Command**: emitted per-cell from `_meta.mean_latency_ms`.
- **CI**: per-cell distribution → bootstrap on p50.
- **Status**: `registered-not-yet-run`.

#### D-42 — LAT-P95-P99 (inherits D-COST-LATENCY portion 2)
- **Metric**: `latency_p95_ms`, `latency_p99_ms` (tail latency).
- **Hypothesis**: Tail-latency surfaces page-shape outliers (Eskimo 140pp class); D-45 page-scaling correlates.
- **Acceptance**: p95/p99 per cell; the outlier-doc-IDs cited.
- **Gold**: observed.
- **Panel**: all rows.
- **Command**: emitted per-cell.
- **CI**: bootstrap on tail quantiles.
- **Status**: `registered-not-yet-run`.

#### D-43 — COST-DOLLAR-PER-CORRECT (inherits D-COST-LATENCY portion 3)
- **Metric**: `dollars_per_correct_call` (cost-per-page × inverse-accuracy).
- **Hypothesis**: Cost-per-correct re-ranks the panel vs raw accuracy; OSS rows dominate ROI even when frontier rows lead accuracy.
- **Acceptance**: per-cell $/correct; ROI table per dimension.
- **Gold**: price-list-pinned per vendor (vendor pricing pages, fetched + cited).
- **Panel**: all rows.
- **Command**: derived per-cell from observed accuracy + pinned price-list.
- **CI**: propagated through accuracy CI.
- **Status**: `registered-not-yet-run`.

#### D-44 — FAILURE-RATE
- **Metric**: `failure_rate_pct` (engine-error, timeout, malformed-output).
- **Hypothesis**: F-B smoke (0 socket failures over 150 cells for self-hosted) is the production-grade-floor; vendor APIs hit ≥ 1% transient failures at scale.
- **Acceptance**: per-cell failure-mode tally + counts; F11-DICT-LITERAL (Chandra-specific) tracked separately.
- **Gold**: observed per-cell.
- **Panel**: all rows.
- **Command**: emitted per-cell.
- **CI**: per-doc binary failure vector → bootstrap.
- **Status**: `registered-not-yet-run`.

#### D-45 — PAGE-SCALING
- **Metric**: CER-by-pages curve at {1pp, 10pp, 50pp, 200pp+}.
- **Hypothesis**: 300s server-side extract timeout (BLK-4 cross-vendor) inflates the long-doc-T-11 class (≥400pp) tail; E6 page-chunk ensemble is the named fix.
- **Acceptance**: per-page-count CER + timeout-rate; long-doc T-11 class (≥400pp) reported separately.
- **Gold**: parsing-dataset (Mahindra-era 10-Q class, internal-only filename — renamed to "long-doc T-11 class").
- **Panel**: all rows.
- **Command**: `python harness/run.py --task DQ-045 --dataset page-scaling-v1 --model <m>`.
- **CI**: per-doc CER vector per page-band → bootstrap.
- **Status**: `registered-not-yet-run`.

### Category J — Reproducibility / statistical (D-46..D-50)

#### D-46 — STAT-CI95
- **Metric**: CI95 honesty + explicit `n` disclosure on every cell.
- **Hypothesis**: Cells with per-doc score vectors yield CI widths < ±0.05 at n=100 for most dimensions; the dimensions where they don't are the ones needing n≥200 sample sizes.
- **Acceptance**: bootstrap pinned at resamples=2000, seed=20260516; `n` never inferred; aggregate-only cells carry literal `null`.
- **Gold**: per-cell score vector.
- **Panel**: every cell.
- **Command**: `python harness/run.py --task DQ-046 --aggregate <task> --bootstrap-seed 20260516 --resamples 2000`.
- **CI**: 95% bootstrap percentile; Holm-Bonferroni multiplicity correction for cross-dimension headline claims (alpha = 0.05/50 = 0.001 per dimension to control family-wise error).
- **Status**: `registered-not-yet-run` (gauge: enforced by `repro_check.py` policy).

#### D-47 — STAT-PAIRED-CI
- **Metric**: paired-bootstrap CI for D-36 lift + any other paired comparison.
- **Hypothesis**: Paired-bootstrap CIs are tighter than independent-bootstrap by ≥30% for D-36 (high per-doc correlation between conditions).
- **Acceptance**: paired-bootstrap-CI width vs independent-bootstrap-CI width reported per paired dimension.
- **Gold**: per-doc paired vector.
- **Panel**: D-36 + any paired-comparison cell.
- **Command**: `python harness/run.py --task DQ-047 --paired-aggregate <task>`.
- **CI**: paired-bootstrap percentile.
- **Status**: `registered-not-yet-run`.

#### D-48 — STAT-IAA
- **Metric**: annotator IAA (Cohen κ for binary, Krippendorff α for ordinal/nominal) for gold corpora used.
- **Hypothesis**: SAVIOR-Bench IAA 0.761 inherited baseline; net-new gold corpora must report their own IAA — no silent inheritance.
- **Acceptance**: per net-new gold corpus (partner-gated L-ZH/L-JA/L-AR per D-20–D-22; bbox silver-vs-gold per D-26–D-28) → computed-and-reported IAA in `_meta.iaa` field; no IAA inferred when no double-annotation pairs exist.
- **Gold**: double-annotation 187-pair subset (SAVIOR convention).
- **Panel**: gold-curation dimension; not a model-comparison metric.
- **Command**: `python harness/iaa.py --corpus <corpus> --double-pairs <pairs.jsonl>`.
- **CI**: Bootstrap on per-pair Kappa vector.
- **Status**: `registered-not-yet-run`.

#### D-49 — REPRO-FACTORY-GREEN
- **Metric**: `factory_reproduced=true` only on green `repro_check.py` (per SAVIOR-Bench Appendix D 4-part cell contract: `provenance` · `pins` · `rerun_command` · `factory_reproduced`).
- **Hypothesis**: 100% of v1-published cells pass `repro_check.py` green; cells that fail stay `factory_reproduced=false` and visibly flagged.
- **Acceptance**: every published cell carries the 4-part contract; status box renders the green/red state.
- **Gold**: per-cell rerunnable command.
- **Panel**: every cell.
- **Command**: `python harness/repro_check.py --cell <path-to-cell-json>`.
- **CI**: n/a (binary gate).
- **Status**: `registered-not-yet-run`.

#### D-50 — REPRO-CONTAMINATION
- **Metric**: contamination-audit pass on test-set vs FT training set.
- **Hypothesis**: Hyperbots-IP `[FT]` rows (O12/O13/O14 + hyperapi-parse-intent) have measurable SAVIOR-Train overlap on T-01/T-02 (invoice + credit note); the audit is non-waivable per I-4.
- **Acceptance**: every `[FT]=y` row declares overlap; cells with unresolved overlap stay `factory_reproduced=false` and visibly flagged in the cell `_meta.contamination_audit` field.
- **Gold**: `contamination/` factory subdir (registered-not-yet-built).
- **Panel**: all `[FT]=y` rows + a self-audit on the corpus mix.
- **Command**: `python harness/contamination_check.py --model <m> --test-corpus <c> --train-corpus savior-train`.
- **CI**: n/a (binary gate).
- **Status**: `registered-not-yet-run`.

### Category tally + integrity

A=6, B=6, C=7, D=3, E=3, F=5, G=6, H=4, I=5, J=5 — **total 50.** Every category represented; every dimension cites at least one reference from §2; every D-* from `PARSE-DEEP-BENCHMARK-FRAMEWORK-2026-05-27.md` is present per the §2.4 bijection.

## §4 — Doc-type × dimension matrix

16 doc-types (T-01..T-16) × 50 dimensions = **800 cell-classes**. Density-priors inherited from `DOC-TYPE-GAPS.json` + the 2026-05-27 spec:

- **G subset (gold available today)**: ~150 cell-classes — concentrated on T-01 invoice, T-04 packing slip, T-06 remittance, T-07 bank statement, T-16 form/FUNSD × categories B/E/F/G/I.
- **S subset (silver via PyMuPDF / Q-* synthetic renders / Inv3D upstream)**: ~200 cell-classes — mostly categories A and F.
- **P subset (partner-gated)**: ~450 cell-classes — T-09 pay stub, T-10 wire/ACH, T-13 tax form, T-14 insurance, T-15 loan + L-non-EN (ZH/JA/KO/AR/HI scripts).

**No cell is fabricated to fill a P cell** (inherits the 2026-05-27 honesty discipline + the NeurIPS-bar pre-registration). The matrix shape is the contract; per-cell gold availability is auditable from `DOC-TYPE-GAPS.json`.

## §5 — Model panel

**Total**: 26 commercial + 26 OSS + 8 stretch OSS = **60 rows.** Floor (≥15 each, ≥30 total) cleared. Current-frontier 2026-Q2 rows added: Claude Opus 4.8, GPT-5.5 thinking, Gemini 3 Pro, Mistral OCR 2, PaddleOCR-VL 1.6, MinerU 2.5-Pro, MonkeyOCR, MonkeyOCR-Pro-3B.

### §5.1 — Commercial (n=22)

| # | Model | Vendor | Access | Surface | FT? | Adapter shape | Status |
|---|---|---|---|---|---|---|---|
| C1 | Azure DI prebuilt-layout | Microsoft | Azure REST | L T Tx B F | n | hosted-REST | Have cell |
| C2 | Azure DI prebuilt-document | Microsoft | Azure REST | L T Tx B F | n | hosted-REST | PENDING-KEY |
| C3 | Azure DI prebuilt-invoice | Microsoft | Azure REST | T Tx F | n | hosted-REST | Have cell |
| C4 | AWS Textract | AWS | AWS SDK | L T Tx B | n | AWS SDK | PENDING-KEY |
| C5 | Google Document AI (form parser) | Google | GCP REST | L T Tx B F | n | hosted-REST | PENDING-KEY |
| C6 | Google Document AI (OCR) | Google | GCP REST | Tx B | n | hosted-REST | PENDING-KEY |
| C7 | LlamaParse Agentic | run-llama | hosted | L T Tx F | n | hosted-REST | PENDING-KEY |
| C8 | LlamaParse non-agentic | run-llama | hosted | Tx F | n | hosted-REST | PENDING-KEY |
| C9 | Reducto | Reducto | hosted | L T Tx | n | hosted-REST | PENDING-KEY |
| C10 | Extend Parse 2.0 | Extend | hosted | L T Tx F | n | hosted-REST | PENDING-KEY (gap-report contrast only) |
| C11 | LandingAI Document Extract | LandingAI | hosted | T Tx F | n | hosted-REST | PENDING-KEY |
| C12 | Unstructured.io API | Unstructured | hosted | L Tx | n | hosted-REST | PENDING-KEY |
| C13 | Nanonets | Nanonets | hosted | T Tx F | n | hosted-REST | PENDING-KEY |
| C14 | Mistral OCR API | Mistral | hosted | Tx F | n | hosted-REST | PENDING-KEY |
| C15 | Anthropic Claude Opus 4.7 | Anthropic | native API | Tx F | n | OpenAI-shape chat | PENDING-KEY |
| C16 | Anthropic Claude Sonnet 4.6 | Anthropic | native API | Tx F | n | OpenAI-shape chat | PENDING-KEY |
| C17 | Anthropic Claude Haiku 4.5 | Anthropic | native API | Tx F | n | OpenAI-shape chat | PENDING-KEY |
| C18 | OpenAI GPT-5.4 thinking (via Azure) | OpenAI/Azure | Azure OpenAI Service | Tx F | n | Azure OpenAI | PENDING-KEY |
| C19 | OpenAI GPT-4.1 (via Azure) | OpenAI/Azure | Azure OpenAI Service | Tx F | n | Azure OpenAI | PENDING-KEY |
| C20 | OpenAI o3 (via Azure) | OpenAI/Azure | Azure OpenAI Service | Tx F | n | Azure OpenAI | PENDING-KEY |
| C21 | Google Gemini 2.5 Pro | Google | Vertex / native | Tx F | n | hosted-REST | PENDING-KEY |
| C22 | Google Gemini 3 Flash | Google | Vertex / native | Tx F | n | hosted-REST | PENDING-KEY |
| C23 | Anthropic Claude Opus 4.8 | Anthropic | native API | Tx F | n | OpenAI-shape chat | PENDING-KEY · current-frontier-Anthropic |
| C24 | OpenAI GPT-5.5 thinking (via Azure) | OpenAI/Azure | Azure OpenAI Service | Tx F | n | Azure OpenAI | PENDING-KEY · current-frontier-OpenAI |
| C25 | Google Gemini 3 Pro | Google | Vertex / native | Tx F | n | hosted-REST | PENDING-KEY · current-frontier-Google |
| C26 | Mistral OCR 2 (latest) | Mistral | hosted | Tx F | n | hosted-REST | PENDING-KEY |

### §5.2 — OSS / specialist (n=26 + 8 stretch)

| # | Model | Origin | Access | Surface | FT? | Adapter shape | Status |
|---|---|---|---|---|---|---|---|
| O1 | Tesseract 5.x | Google OSS | local | Tx B | n | class-based (pytesseract) | Have adapter |
| O2 | PaddleOCR v4 | PaddlePaddle | local | L T Tx B | n | class-based | Have attested |
| O3 | PaddleOCR-VL-1.5 | PaddlePaddle | local | L T Tx B F | n | class-based vLLM | Have attested |
| O4 | MinerU 0.9 | OpenDataLab | local | L T Tx | n | class-based | Have attested |
| O5 | MinerU 2.5 | OpenDataLab | local | L T Tx B | n | class-based | Have attested |
| O6 | MinerU Pro | OpenDataLab | hosted-OSS | L T Tx B | n | class-based | NEW-install |
| O7 | Marker 1.0 | datalab-to | local | L T Tx | n | class-based | Have attested |
| O8 | Nougat 0.1 | Meta | local | Tx F (scientific) | n | class-based | Have attested |
| O9 | DOTS-OCR (dots.ocr) | rednote-hilab | local | L Tx B | n | class-based | Have attested |
| O10 | Docling | IBM | local | L T Tx | n | class-based | NEW-install |
| O11 | Chandra (`datalab-to/chandra-ocr-2`) | datalab-to | self-hosted vLLM `54.185.174.140:8847` | L T Tx B (native) | n | class-based vLLM | Have adapter |
| O12 | Qwen 3.6-35B-A3B `[FT]` | Hyperbots-IP | self-hosted `135.233.113.234:6006` | Tx F | **y** | class-based vLLM | Runnable; $0; D-36 extractor pin |
| O13 | Qwen 2.5-VL-7B-F `[FT]` | Hyperbots-IP | local weights | Tx F | **y** | class-based vLLM | Have attested (recall #1 FT) |
| O14 | Qwen 2.5-VL-3B-F `[FT]` | Hyperbots-IP | local weights | Tx F | **y** | class-based vLLM | Have attested |
| O15 | Qwen 3-VL-235B | Alibaba OSS | local (heavy) | Tx F | n | class-based vLLM | Have attested |
| O16 | GLM-OCR | Zhipu | local | Tx F | n | class-based vLLM | Have attested (#1 edit-dist) |
| O17 | GOT-OCR-2.0 | StepFun | local | Tx F | n | class-based vLLM | Have attested |
| O18 | Surya | datalab-to | local | L Tx B | n | class-based | Have attested |
| O19 | EasyOCR | JaidedAI | local | Tx B | n | class-based | Have attested |
| O20 | OpenOCR | OpenDataLab | local | Tx B | n | class-based | Have attested |
| O21 | Logics-Parsing-v2 | Logics | local | L T Tx | n | class-based | NEW |
| O22 | FireRed-OCR | Xiaohongshu | local | Tx F | n | class-based vLLM | NEW |
| O23 | PaddleOCR-VL-1.6 | PaddlePaddle | local | L T Tx B F | n | class-based vLLM | NEW · supersedes O3 for current-frontier |
| O24 | MinerU 2.5-Pro | OpenDataLab | local | L T Tx B | n | class-based | NEW · supersedes O5 for current-frontier |
| O25 | MonkeyOCR | Yuliang-Liu | local | L T Tx B F | n | class-based vLLM | NEW |
| O26 | MonkeyOCR-Pro-3B | Yuliang-Liu | local | L T Tx B F | n | class-based vLLM | NEW · 3B-param Pro variant |

**Total panel = 26 commercial + 26 OSS + 8 stretch = 60 rows (floor cleared).**

**Stretch OSS (n=8)** → O27 mPLUG-DocOwl 1.5 · O28 DeepSeek-OCR-2 · O29 Nanonets-OCR-s (open weights) · O30 LLaVA-1.6-34B · O31 InternVL2-26B/76B · O32 Llama-3.2-90B-Vision · O33 Llama-4-Maverick · O34 Youtu-Parsing.

### §5.3 — FT? column convention (I-4 machine-checkability)

`y` for rows whose Model name carries `[FT]` (today: O12/O13/O14 + the hyperapi-parse-intent row when it joins). All other rows are `n` (zero-shot, vendor-native). Machine-greppable; the I-4 invariant is enforced by `repro_check.py` (D-49) rejecting any cell with a missing or wrong `[FT]` tag on a Model name carrying `[FT]`.

### §5.4 — Adapter contract (3 shapes)

Of the 52 panel rows, REGISTRY currently holds 7 adapter entries. The remaining ~45 fall into 3 contract shapes — all dispatched class-based via the 2026-05-27 fix-pass orchestrator:

(a) **class-based image-input** (`chandra`-style `.call_page(image_bytes, prompt) -> dict`): self-hosted vLLMs — Qwen 2.5-VL family, GLM-OCR, GOT-OCR, Surya, DOTS-OCR, MinerU, Marker, Nougat, Docling, EasyOCR, OpenOCR, Logics-Parsing-v2, FireRed-OCR, stretch tier.

(b) **hosted REST file-upload**: LlamaParse, Reducto, Extend, LandingAI, Unstructured, Nanonets, Mistral OCR — multipart-form wrappers around `RealQAClient`-style rate-limited adapters.

(c) **OpenAI / Azure chat-completions**: Anthropic Claude family, OpenAI via Azure GPT-5.4/4.1/o3, Gemini 2.5/3 family, Azure DI prebuilt-* via SDK.

BUILD-v1 deliverable item budgets ~45 new adapter wires under these 3 shapes; the harness contract scales because the dispatch lane was made class-based-detection-aware in the 2026-05-27 fix-pass. No silent overload of existing adapters.

## §6 — Methodology (NeurIPS reproducibility — summary; full checklist in `parse-deep-build-v0/methodology.md`)

- **Decoding pins (3 family sets)**:
  - **parse-deep family** (D-01..D-30, D-32..D-50 except as noted): `T=0.1, top_p=0.9, max_tokens=2048, seed=20260516`.
  - **TR-000 family** (D-31 table-GTRM host): `T=0.0, top_p=1.0, max_tokens=4096`. **D-31 cells are `apples-to-oranges`-flagged per I-1.**
  - **extract family** (D-36 downstream-lift host): `T=0.0, top_p=1.0, max_tokens=4096`. **D-36 cells are `apples-to-oranges`-flagged per I-1.**

- **CI methodology**: bootstrap (resamples=2000, seed=20260516) over per-doc score vector. Aggregate-only cells stay `ci95_low: null, ci95_high: null` with `n` literally reported (never inferred). Multiplicity: cross-dimension headline claims use **Holm-Bonferroni** with family-wise alpha = 0.05; per-dimension target alpha ≈ 0.001 (= 0.05/50). Paired-bootstrap on D-36 lift and any paired comparison.

- **Reproducibility checklist** (NeurIPS 2024 paper-checklist alignment): every claim → rerunnable command; pinned env via `pyproject.toml` (`requires-python>=3.11,<3.13`); pinned commits (vlm_ocr `1fbbc334`, ParseBench `a0b10dd7`); seeds disclosed (20260516); model-checkpoint pins per row in §5.

- **The 8 comparative-study invariants applied per-dimension**: see §7 in the plan-of-record (`PARSE-FRAMEWORK-PLAN-2026-06-11.md`); each D-XX block above implicitly inherits all 8.

## §7 — Ablations (E1–E9)

For each ensemble in `DEEP-RESEARCH-PLAN §6` + this spec §5, the BUILD-v1 panel will name the ablation explicitly:

- **E1 (production parse→extract chain)**: with-HyperAPI-parse vs without (replaced by Qwen-3.6 parse only). Lift = E1-with vs E1-without; if lift CI95 excludes 0 → HyperAPI parse contributes; if not → ensemble is not HyperAPI-anchored on this dimension.
- **E2 (doc-type router)**: with router vs uniform-routing (random / round-robin); router-uplift CI per type.
- **E3 (field-level confidence-weighted vote)**: with vote vs single-best; vote-uplift CI per field-type.
- **E4 (OCR + LLM reconciler)**: with reconciler vs raw OCR; reconciler-uplift CI per dimension.
- **E5 (cost-cascade)**: cascade vs cheapest-only and frontier-only; cascade Pareto front (cost vs accuracy).
- **E6 (page-chunked long-doc)**: chunked vs single-page; D-45 page-scaling lift on long-doc-T-11 class.
- **E7 (layout-aware tri-engine)**: 3-engine vs each single-engine + each-pair; component-contribution attribution.
- **E8 (OSS-only control)**: OSS-only ensemble — the **explicit baseline** for "what HyperAPI-anchored adds." If E8 matches E1/E3/E7 within CI, HyperAPI-anchored claim fails honestly.
- **E9 (Chandra-anchored layout-aware)**: Chandra + Qwen 3.6 + chart specialist; ablation = drop each component in turn.

No ensemble claim ships without its named ablation. Comparative-study I-7 ensemble-anchor rule: ship-claim ensembles must include HyperAPI parse as a member; E8 is the explicit OSS control.

## §8 — Contamination + held-out audit

Per the NeurIPS bar and SAVIOR-Bench R1–R9 honesty discipline:

- **Per FT row (`[FT]=y`)**: contamination audit between the row's training corpus (SAVIOR-Train for Hyperbots-IP rows) and every test corpus the cell is scored against. Output: `_meta.contamination_audit` block with `train_corpus_id`, `test_corpus_id`, `overlap_doc_count`, `overlap_pct`, `mitigation` (held-out / re-scored / accepted-with-flag).
- **Unresolved overlap** = cells stay `factory_reproduced=false` and visibly flagged in the dashboard.
- **Held-out splits**: every test corpus declares a held-out subset (default: 10% random, seed=20260516); cells published on the full-corpus are paired with held-out-CIs.
- **Audit subdir**: `contamination/` factory subdir holds per-(train,test) pair overlap reports. Auditable by `python harness/contamination_check.py --train <c> --test <c>`.

## §9 — Ethics + license + customer-name policy

### §9.1 — License matrix per corpus

| Corpus | License | Publishable? | Notes |
|---|---|---|---|
| ParseBench (run-llama) | Apache-2.0 | ✓ public | Anchor for HF dataset-card publish |
| FUNSD | CC-BY-SA-4.0 (XFUND mixed) | ✓ public | Per-entity |
| CORD | CC-BY-4.0 | ✓ public | Receipts |
| PubTabNet | CDLA-Permissive-2.0 | ✓ public | Tables |
| DocLayNet | CDLA-Permissive-1.0 | ✓ public | Layout |
| DocVQA | CC-BY-NC-4.0 | ◐ internal | NC restricts external publish |
| ChartQA | CC-BY-4.0 | ✓ public | Charts |
| dataset_95_granular | Hyperbots-internal | ✗ internal-only | No customer names per §9.2 |
| financepss-205 | Hyperbots-internal | ✗ internal-only | Same |
| tough-bench | Hyperbots-internal | ✗ internal-only | Same |
| SAVIOR-Bench v1 | mixed (UCSF / FUNSD / Inv3D / Hyperbots-IP) | ◐ partial; aggregate publishable per Appendix D | Per-doc not redistributable |
| Partner corpora (L-ZH/JA/AR; T-09/T-10/T-13/T-14/T-15) | per-partner | per-partner | Consent gate required |

### §9.2 — Customer-name policy (the 14-name roster verbatim)

Build-time grep guard against the canonical 14-name roster (from `parse-deep-benchmark-draft/_grep_guard.sh`):

```
ROSTER='Airgas|CJ Logistics|Eskimo|Mahindra|INFY|MERC|TCS|ICICI|HDFC|KPITTECH|PAYTM|WIPRO|Reiser|Stauffer'
```

Any artifact (spec, dashboard, methodology, JSON cell file, HTML render) that contains a roster match outside a sentinel-tagged exempt line fails the grep guard (`exit 1`) and cannot publish. The 4 false-positive overlaps with non-roster terms (e.g. `MERC` inside `commercial`) are sentinel-managed; the guard uses word-boundary regex.

### §9.3 — PII + partner data

Per `[[hyperapi-fde-agent-ga-and-partners]]`: partner names internal-only without externalization consent. PII corpora (T-09 pay stub, T-10 wire/ACH, T-13 tax form) require synthetic-fill or PII-redacted consented samples; no real PII in published cells.

## §10 — Honest baselines per dimension

Every dimension names the **single-model baseline** that an ensemble claim must beat to be reported as ship-claim:

- **Text dimensions (D-07..D-12)**: best zero-shot OCR baseline = Tesseract floor + best zero-shot VLM modesty anchor.
- **Layout / bbox (D-23..D-29)**: best zero-shot layout-emitter baseline = Chandra (sole native layout-emitter today).
- **Table (D-31..D-33)**: best zero-shot table-emitter = Chandra (GriTS lead) + PubTabNet-trained models as control.
- **KIE (D-34..D-35)**: FUNSD-trained model + best zero-shot KIE-prompt model.
- **Parse-intent / NLP (D-37..D-40)**: best documented zero-shot = GPT-4o per SAVIOR-Bench §5.1.1 modesty-anchor convention.
- **Downstream lift (D-36)**: no-parse direct-extract baseline = pinned Qwen-3.6 image→extract.
- **Cost / latency (D-41..D-44)**: cheapest baseline + production-grade-floor (Tesseract for cost; the self-hosted Qwen 3.6 for latency).
- **All FT claims**: best documented zero-shot baseline named inline (SAVIOR convention).

Honesty principle: the cell that beats its baseline ships with the delta + CI; the cell that doesn't ships the honest tie/loss. No "modesty anchor" cherry-picking — the anchor is named in the dimension block before cells run.

## §11 — Public release plan (HF + arXiv skeleton)

### §11.1 — HuggingFace dataset card

When the BUILD-v1 panel ships green:
- HF dataset card at `huggingface.co/datasets/hyprbots/parse-deep-benchmark-v1` (assuming approval).
- License = composite per §9.1 (per-split notice; non-redistributable splits clearly tagged).
- Card includes: §0 honest framing, §2 reference benchmarks, §3 dimension list, §4 matrix, §5 panel, §6 methodology, §8 contamination, §9 license, §11.2 paper link.

### §11.2 — arXiv preprint skeleton

Title: *"A 50-dimension parse-benchmark framework for finance documents — pre-registered, third-party-anchored, ensemble-aware"*. Section structure:

1. Introduction — problem statement (the vendor-benchmark integrity problem, F-B-STUDY-style)
2. Related work — ParseBench, RealDocBench, SAVIOR-Bench, OmniDocBench, OCRBench v2, FUNSD/CORD/PubTabNet/DocLayNet/DocVQA tradition
3. Framework design — the 50 dimensions, the 16-type matrix, the 52-row panel, the 9 ensembles + ablations
4. Methodology — pin sets, bootstrap, Holm-Bonferroni, paired-bootstrap, contamination audit, NeurIPS reproducibility checklist
5. Results — once cells run (BUILD-v1; not v0)
6. Discussion — per-dimension winners, the facet-decoupling thesis, ensemble lift
7. Limitations — partner-gated dimensions, BLK-16/17/18, the structurally-out-of-reach T-11/T-12 caveat
8. Ethics — the §9 license matrix; partner-PII gate; customer-name policy
9. Reproducibility appendix — every claim → rerunnable command; pinned versions; seeds
10. Appendix A — per-dimension tables; Appendix B — per-ensemble ablation tables; Appendix C — contamination audit reports

Status: **DRAFT 0 — not yet written; preprint authored after BUILD-v1 cells land green.**

## §12 — Limitations + risks

Inherited from `PARSE-FRAMEWORK-PLAN-2026-06-11.md §9 + §9.1`:

**Cannot measure today (PENDING-*)**:
- BLK-16 (HyperAPI quota exhausted) → C18/C19/C20/HyperAPI parse rows wait
- BLK-17 (Chandra vLLM host down) → Chandra cells wait
- BLK-18 (SAVIOR-Bench gold corpus off-disk) → D-07 / D-08 / D-25 SAVIOR-anchored rows wait
- Per-doc score vector recovery for the 21 SAVIOR OCR + 23 parse-intent attested cells → D-46 CI on those rows waits

**Requires partner data**: T-09 / T-10 / T-13 / T-14 / T-15 + L-ZH/L-JA/L-AR partner-gated.

**Structurally out-of-reach today**: T-11 / T-12 (HyperAPI IDP doc-type set excludes); Q-DR-5 to CEO ("restrict scope to AP/AR + payments + forms" vs "fund capital-markets fine-tune"). D-15 honest-fail expected.

**Top-3 hardest cut-vs-kept calls** (inherited from plan §9.1):
1. D-04 IMG-DEWARP — KEPT (distinct from D-05 skew; different gold, different remediation).
2. D-25 LAYOUT-PAIRS — KEPT, as PC-only secondary; PaIRS is the only published cross-vendor layout-fidelity metric with attested SAVIOR numbers.
3. Agentic-loop dimension — CUT; folded into D-36 lift + paired-bootstrap; agentic-vs-non-agentic is a property of systems, not dimensions.

## §13 — Sources + provenance trail

- Plan-of-record: `../hyperapi-parse-x-research/command-center/plans/PARSE-FRAMEWORK-PLAN-2026-06-11.md`
- All 4 review verdicts (chief-research-scientist + chief-architect + docs-techwriter + benchmark-format-steward): `../hyperapi-cto-org/command-center/REVIEW-VERDICT-PARSE-FRAMEWORK-*-2026-06-11.md`
- Predecessor (9-D spec): `PARSE-DEEP-BENCHMARK-FRAMEWORK-2026-05-27.md` (507 LOC)
- Depth-bar reference (invoice study): `comparative/azure-di/azure-di-invoice-study.html` (1,842 LOC)
- SAVIOR-Bench paper: `paper/SAVIOR-Bench.md` (1,119 LOC; Appendix D provenance contract)
- ParseBench arXiv: arXiv:2604.08538, repo `github.com/run-llama/ParseBench`, dataset Apache-2.0, commit pinned `a0b10dd7`
- vlm_ocr metric vendor: `hyprbots/vlm_ocr@eval` commit `1fbbc334` (PaIRS + WordRecall)
- Comparative-study skill: `../hyperapi-cto-org/.claude/skills/comparative-study/SKILL.md` (8 invariants)
- 14-name customer-name roster: `parse-deep-benchmark-draft/_grep_guard.sh`
- DOC-TYPE-GAPS machine-readable: `../hyperapi-parse-x-research/command-center/DOC-TYPE-GAPS.json`
- F-B study (the methodology bar to beat): `../hyperapi-parse-x-research/command-center/F-B-STUDY.html` + `command-center/F-B-SMOKE-2026-05-28.md`
- BLK-16 escalation: `../hyperapi-parse-x-research/command-center/BLK-16-ESCALATION-2026-05-27.md`
- Auto-memory: `azure-openai-preferred.md`, `openai-default-gpt-5-4-thinking.md`, `no-hitl-framing.md`, `teams-broadcast-explicit-ask-only.md`.

## §14 — Approval

**APPROVAL — PENDING build-v0 review** (chief-research-scientist + chief-architect + docs-techwriter + benchmark-format-steward). This spec is **NOT self-approved**.

Reviewers will apply the 8 P0 / 6 P1 / 3 P2 (research-head) + 8 (tech) + 8 (content) + 10 (research-format) criteria from the 2026-06-11 review chain to this v1 artifact. Plus the 10-item NeurIPS-bar amendment from `STEP-4-CONSOLIDATED-BRIEF-2026-06-11.md`.

Until the verdict files land at `../hyperapi-cto-org/command-center/REVIEW-VERDICT-PARSE-FRAMEWORK-V1-*-2026-06-11.md`, this document is **DRAFT INTERNAL ONLY**.
