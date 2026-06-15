# Parse Deep Benchmark v1 — 2-page review brief

Date: 2026-06-11 · Status: BUILD-v0 (spec only · zero cells run · $0) · Bar: ParseBench / NeurIPS-paper, strictly above SAVIOR-Bench
Approval: PENDING build-v0 review (chief-research-scientist · chief-architect · docs-techwriter · benchmark-format-steward)
Companion: full spec at `PARSE-DEEP-BENCHMARK-FRAMEWORK-2026-06-11-v1.md` · dashboard at `parse-deep-build-v0/index.html`

---

## §1 — What this is, in one paragraph

A pre-registered, third-party-anchored, ensemble-aware framework to defensibly answer **"is the HyperAPI parse primitive the best general parsing primitive across finance documents."** 50 dimensions across image / text / doc-type / language / density / CV / enterprise / NLP / print / repro. A 60-row commercial-vs-OSS model panel. A 16-type × 50-dim matrix (800 cell-classes). Engineered to **succeed whether HyperAPI parse wins or loses on any dimension** — researcher-not-advocate. Inherits SAVIOR-Bench Appendix D 4-part cell contract; lifts the bar to ParseBench-style per-rule = per-doc score vectors, paired-bootstrap CIs, Holm-Bonferroni multiplicity correction, contamination + held-out audit, NeurIPS reproducibility checklist.

## §2 — All 51 metrics (A–K · 50 v1 + D-51 UEM v1.1 amendment 2026-06-15)

| Dim | Cat | Name | Metric |
|---|---|---|---|
| D-01 | A-IMAGE | IMG-DPI | `effective_dpi + cer_delta_strat` |
| D-02 | A-IMAGE | IMG-MTF | `mtf_50_lp_mm + cer_delta` |
| D-03 | A-IMAGE | IMG-ILLUMINATION | `illumination_uniformity_pct + cer_delta + bbox_iou_delta` |
| D-04 | A-IMAGE | IMG-DEWARP | `dewarp_rmse_px + cer_delta` |
| D-05 | A-IMAGE | IMG-SKEW | `skew_recovery_pct_cer` |
| D-06 | A-IMAGE | IMG-JPEG-Q | `cer_delta_q40_vs_q90` |
| D-07 | B-TEXT | OCR-RECALL | `savior_word_recall` |
| D-08 | B-TEXT | OCR-PRECISION | `savior_word_precision + hallucinated_token_count` |
| D-09 | B-TEXT | OCR-EDIT-DISTANCE | `ocr_edit_distance_norm` |
| D-10 | B-TEXT | OCR-WER | `wer` |
| D-11 | B-TEXT | OCR-CER | `cer_per_script` |
| D-12 | B-TEXT | OCR-DIGIT-MICR-FIDELITY | `digit_micr_fidelity_f1` |
| D-13 | C-DOCTYPE | DT-AP-AR | `f1_per_type` |
| D-14 | C-DOCTYPE | DT-PAYMENTS | `f1_per_type + per_field` |
| D-15 | C-DOCTYPE | DT-CAPITAL-MARKETS | `f1_per_type` |
| D-16 | C-DOCTYPE | DT-ADJACENT | `f1_per_type` |
| D-17 | C-DOCTYPE | DT-DENSITY | `metric_per_density_stratum` |
| D-18 | C-DOCTYPE | DT-MULTI-COL | `multi_col_layout_f1 + column_count_err` |
| D-19 | C-DOCTYPE | DT-NESTED-TABLE | `nested_table_cell_f1` |
| D-20 | D-LANGUAGE | LANG-CER-PER-SCRIPT | `cer_per_script` |
| D-21 | D-LANGUAGE | LANG-KIE-XFUND | `kie_f1_per_language` |
| D-22 | D-LANGUAGE | LANG-MIXED-SCRIPT | `cer_mixed_script` |
| D-23 | E-DENSITY | LAYOUT-ELEM-ACCURACY | `layout_element_accuracy` |
| D-24 | E-DENSITY | LAYOUT-READING-ORDER | `reading_order_rank_correlation` |
| D-25 | E-DENSITY | LAYOUT-PAIRS | `pairs_layout_zeuclidean` |
| D-26 | F-CV | BBOX-IOU-TOKEN | `bbox_iou_token + match_rate` |
| D-27 | F-CV | BBOX-FIELD-TO-REGION | `field_to_region_grounding_acc_iou50` |
| D-28 | F-CV | LAYOUT-COCO-MAP | `coco_mAP_50_75_95 + per_class_AP` |
| D-29 | F-CV | SEG-IOU | `seg_pixel_iou` |
| D-30 | F-CV | VLM-PAGE-IMAGE-FIDELITY | `psnr + ssim` |
| D-31 | G-ENTERPRISE | TABLE-GTRM | `grits + tablerecordmatch + gtrm` |
| D-32 | G-ENTERPRISE | TABLE-TEDS | `teds` |
| D-33 | G-ENTERPRISE | TABLE-CELL-F1 | `cell_content_f1 + per_row_type` |
| D-34 | G-ENTERPRISE | KIE-FUNSD-F1 | `entity_f1` |
| D-35 | G-ENTERPRISE | KIE-CORD-F1 | `entity_f1` |
| D-36 | G-ENTERPRISE | DOWNSTREAM-LIFT | `parse_lift_paired_bootstrap` |
| D-37 | H-NLP | PARSE-INTENT-F1 | `parse_intent_f1 + wer` |
| D-38 | H-NLP | VQA-ANLS | `anls` |
| D-39 | H-NLP | SEMANTIC-BERTSCORE | `bertscore_f1` |
| D-40 | H-NLP | INTENT-CLASSIFICATION | `classify_accuracy_per_type` |
| D-41 | I-PRINT | LAT-P50 | `latency_p50_ms` |
| D-42 | I-PRINT | LAT-P95-P99 | `latency_p95_ms + latency_p99_ms` |
| D-43 | I-PRINT | COST-DOLLAR-PER-CORRECT | `dollars_per_correct_call` |
| D-44 | I-PRINT | FAILURE-RATE | `failure_rate_pct + per_mode_tally` |
| D-45 | I-PRINT | PAGE-SCALING | `cer_per_page_band + timeout_rate` |
| D-46 | J-REPRO | STAT-CI95 | `ci95_bootstrap_2000_seed_20260516` |
| D-47 | J-REPRO | STAT-PAIRED-CI | `paired_bootstrap_ci` |
| D-48 | J-REPRO | STAT-IAA | `cohens_kappa + krippendorff_alpha` |
| D-49 | J-REPRO | REPRO-FACTORY-GREEN | `factory_reproduced_bool` |
| D-50 | J-REPRO | REPRO-CONTAMINATION | `contamination_audit_pass_bool` |
| **D-51** | **K-UEM** | **UEM-UNIVERSAL-OCR-METRIC** | `uem_score` over {HOF · Markdown · HTML · Tokens+BB} · cross-format judge=GPT-5.4-mini (Azure) · same-format model-free |

**Bijection** to the 2026-05-27 9-D spec preserved (every D-OCR/D-PARSE-INTENT/D-LAYOUT/D-BBOX/D-TABLE/D-DOC-QUALITY/D-LANG/D-DOWNSTREAM/D-COST-LATENCY maps to a D-XX). No dimension dropped.

## §3 — The 130-row model panel

**56 commercial · 66 OSS · 8 stretch OSS = 130 rows.** Floor cleared by ~5×.

| Bucket | Count | Examples |
|---|---|---|
| Frontier closed-source LLM/VLM | 13 | Claude Opus 4.8 / Sonnet 4.6 / Haiku 4.5 · GPT-5.5/5.4/4.1/o3 (via Azure) · Gemini 3 Pro/Flash + 2.5 Pro · xAI Grok-4 · Cohere CR+ vision · Reka Core |
| Doc-AI / IDP commercial | 33 | Azure DI · AWS Textract · Google DocAI · LlamaParse · Reducto · **Extend Parse 2.0 (C10)** · Nanonets · Mistral OCR 2 · ABBYY · Rossum · Hyperscience · Klippa · Mindee · Veryfi · Affinda · Sensible · Instabase · Indico · IBM Watson · Oracle · Adobe · Foxit · Konfuzio · HyperVerge · Eden AI · OCR.space · Scribe · Iron OCR · Aspose · A2iA |
| Frontier OSS VLM-OCR | 21 | Chandra · MonkeyOCR + Pro-3B · PaddleOCR-VL 1.5/1.6 · MinerU 2.5/2.5-Pro/Pro · DOTS-OCR · GLM-OCR · GOT-OCR 2.0 · Qwen 3-VL-235B · Marker · Surya · Docling · Nougat · FireRed · PP-StructureV3 |
| OSS doc-AI classics | 11 | TrOCR · Donut · LayoutLMv3 · LiLT · Pix2Struct · Kosmos-2.5 · Florence-2 · UDOP · DocFormerV2 · ERNIE-Layout · LayoutXLM |
| OSS open-weight VLMs (sweep) | 21 | Vary-toy · MiniCPM-V/o 2.6 · Idefics3 · CogVLM2 · InternLM-XC 2.5 · DeepSeek-VL2 · Phi-4-mm · Pixtral 12B · Molmo 72B · Aria · Llama-3.2-11B-Vision · Janus-Pro · GLM-4V · InternVL3 · Cambrian-1 · VILA · Mini-Gemini · MAmmoTH-VL · OpenELM-VL · EXAONE 3.5 VL |
| Table / structure / open-OCR | 7 | TATR · SmolDocling · olmOCR-2 · RolmOCR · TextMonkey · StructEqTable · Kraken |
| Hyperbots-IP `[FT]` | 4 | Qwen 3.6-35B-A3B `[FT]` (D-36 extractor pin) · Qwen 2.5-VL-7B/3B-F `[FT]` · hyperapi-parse-intent `[FT]` |
| Stretch | 8 | mPLUG-DocOwl 1.5 · DeepSeek-OCR-2 · Nanonets-OCR-s · LLaVA-1.6-34B · InternVL2 · Llama-3.2-90B-V · Llama-4-Maverick · Youtu-Parsing |

**Audit gap closed**: Extend Parse 2.0 is **C10** (PENDING-KEY, gap-report contrast per Extend RealDocBench). Adapter wires fall into 3 contract shapes (class-based image-input vLLM · hosted REST multipart · OpenAI-shape chat); 7 REGISTRY entries today vs ~123 to wire at BUILD-v1.

## §4 — Methodology highlights (NeurIPS-bar)

- **Pre-registration**: this framework IS the pre-registration. Every cell ships with hypothesis · acceptance · rerunnable command · `nrun_status` (default `registered-not-yet-run`) before any number lands.
- **Decoding pins** — 3 named families, machine-readable per cell:
  - `parse-deep` (T=0.1, top_p=0.9, max_tokens=2048) — 48 dimensions
  - `TR-000` (T=0, top_p=1, 4096) — D-31 GTRM, flagged `apples-to-oranges` per I-1
  - `extract` (T=0, top_p=1, 4096) — D-36 lift, flagged `apples-to-oranges`
- **Stats**: nonparametric bootstrap, resamples=2000, seed=20260516. Paired-bootstrap on D-36 lift. Holm-Bonferroni for cross-dimension headlines (family-wise α=0.05; per-dim α≈0.001).
- **Contamination**: every `[FT]=y` row is audited vs SAVIOR-Train; unresolved overlap → cell stays `factory_reproduced=false` and renders red. Held-out 10% split per corpus.
- **Provenance**: SAVIOR-Bench Appendix D 4-part contract — `provenance · pins · rerun_command · factory_reproduced` — on every cell. `factory_reproduced=false` at adapter emit time (TR-4); only `repro_check.py` flips it true.
- **Reproducibility checklist**: 18 NeurIPS-2024 items answered item-by-item in `methodology.md §8`.
- **Comparative-study 8 invariants** (I-1 apples-to-apples ... I-8 customer-name consent): per-claim enforced; machine-greppable.

## §5 — License + customer-name discipline

License matrix (framework §9.1): ParseBench Apache-2.0 (the publishability anchor) · FUNSD/CORD/PubTabNet/DocLayNet/ChartQA permissive (public) · DocVQA CC-BY-NC (internal-only) · Hyperbots-internal corpora (no customer names) · SAVIOR partial (aggregate publishable per Appendix D). Customer-name 14-roster (verbatim from `_grep_guard.sh`) build-time-grep-guarded across every artifact. PII corpora synthetic-fill or partner-consent-gated.

## §6 — What's in BUILD-v0 (this package)

1. `PARSE-DEEP-BENCHMARK-FRAMEWORK-2026-06-11-v1.md` — full spec (~500 LOC, §0–§14)
2. `parse-deep-build-v0/methodology.md` — NeurIPS reproducibility checklist
3. `parse-deep-build-v0/tasks-additive-DQ-001-050.json` — 50 task entries, ADDITIVE-ONLY
4. `parse-deep-build-v0/cell-schema-v1.1.json` — JSON Schema 2020-12, backward-compat
5. `parse-deep-build-v0/index.html` — dashboard scaffold (registered-not-yet-run state)
6. `parse-deep-build-v0/BUILD-V0-LEDGER-2026-06-11.md` — acceptance-criterion mapping + grep-guard self-check

Zero cells run · $0 burned · no quota touched · no broadcasts fired.

## §7 — Decisions requested from reviewer

1. **APPROVE / APPROVE-WITH-CHANGES / REJECT** on the 50-dim list — anything missing? anything to cut?
2. **Panel completeness sign-off** — 110 rows after the 2026-06-15 lit-sweep (+50 across enterprise IDP, frontier multimodal hosted, OSS doc-AI, open-weight VLMs, and table specialists). Any further additions / cuts before BUILD-v1 wires adapters?
3. **Q-DR-5** (CEO): for D-15 capital-markets — restrict HyperAPI scope to AP/AR + payments + forms, OR fund a capital-markets fine-tune to bring T-11/T-12 into the doc-type set?
4. **BLK-16 Option A (wait reset) vs Option B (paid-tier upgrade)** for HyperAPI quota — blocks the HyperAPI parse + classify columns.
5. **Greenlight BUILD-v1?** — cell execution, gated on (3) + (4) + partner-corpus consent.

---

*Researcher-not-advocate · Hyperbots Research · 2026-06-11 · DRAFT INTERNAL until build-v0 reviewers verdict.*
