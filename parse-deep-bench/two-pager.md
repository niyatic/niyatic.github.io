# Parse Deep Benchmark v1 — 2-page review brief

Date: 2026-06-11 · Status: BUILD-v0 (spec only · zero cells run · $0) · Bar: ParseBench / NeurIPS-paper, strictly above SAVIOR-Bench
Approval: PENDING build-v0 review (chief-research-scientist · chief-architect · docs-techwriter · benchmark-format-steward)
Companion: full spec at `PARSE-DEEP-BENCHMARK-FRAMEWORK-2026-06-11-v1.md` · dashboard at `parse-deep-build-v0/index.html`

---

## §1 — What this is, in one paragraph

A pre-registered, third-party-anchored, ensemble-aware framework to defensibly answer **"is the HyperAPI parse primitive the best general parsing primitive across finance documents."** 50 dimensions across image / text / doc-type / language / density / CV / enterprise / NLP / print / repro. A 60-row commercial-vs-OSS model panel. A 16-type × 50-dim matrix (800 cell-classes). Engineered to **succeed whether HyperAPI parse wins or loses on any dimension** — researcher-not-advocate. Inherits SAVIOR-Bench Appendix D 4-part cell contract; lifts the bar to ParseBench-style per-rule = per-doc score vectors, paired-bootstrap CIs, Holm-Bonferroni multiplicity correction, contamination + held-out audit, NeurIPS reproducibility checklist.

## §2 — The 50 dimensions (A–J)

| Cat | # | Theme | Notable dims |
|---|---|---|---|
| A | 6 | Image / scan quality | D-01 DPI · D-02 MTF · D-04 dewarp · D-06 JPEG-Q |
| B | 6 | Text / transcription | D-07 recall · D-08 precision · D-11 CER · **D-12 digit-MICR-fidelity** (validates the "dumb-tool-wins-on-digits" F-B finding at scale) |
| C | 7 | Doc-type strat | D-13 AP/AR · D-14 payments · **D-15 capital-markets** (HyperAPI declared out-of-set per Q-DR-5 — honest fail expected) |
| D | 3 | Language / script | D-20 CER per script (EN/DE/FR/ES/ZH/JA/KO/AR/HI) · D-22 mixed-script |
| E | 3 | Density / layout | **D-23 layout-elem-accuracy** (Chandra's native HTML lead) · D-25 PaIRS (PC-only secondary) |
| F | 5 | Computer vision | D-26 bbox-IoU · D-28 DocLayNet COCO-mAP · D-29 seg-IoU |
| G | 6 | Enterprise doc AI | **D-31 TABLE-GTRM** (Chandra's F-B lead 0.800 re-anchored) · D-32 TEDS · D-34/35 KIE FUNSD/CORD · **D-36 DOWNSTREAM-LIFT** (CEO-required; paired-bootstrap on parse→extract chain) |
| H | 4 | NLP / semantic | D-37 parse-intent F1 · D-38 VQA-ANLS · D-40 classify |
| I | 5 | Print / production | D-41/42 lat-P50/P95-P99 · D-43 $/correct · D-45 page-scaling on ≥400pp T-11 class |
| J | 5 | Repro / stat | D-46 CI95 · D-47 paired-CI · D-48 IAA · **D-49 factory-green gate** · **D-50 contamination-audit gate** |

**Bijection** to the 2026-05-27 9-D spec preserved (every D-OCR/D-PARSE-INTENT/D-LAYOUT/D-BBOX/D-TABLE/D-DOC-QUALITY/D-LANG/D-DOWNSTREAM/D-COST-LATENCY maps to a D-XX). No dimension dropped.

## §3 — The 60-row model panel (current-frontier-complete, 2026-Q2)

**26 commercial** + **26 OSS** + **8 stretch OSS** = 60 rows. Floor (≥15 each, ≥30 total) cleared comfortably.

- **Frontier closed-source**: Anthropic Claude Opus 4.8 · Sonnet 4.6 · Haiku 4.5 · OpenAI GPT-5.5 thinking + GPT-5.4 + GPT-4.1 + o3 (all via Azure OpenAI Service per `[[azure-openai-preferred]]`) · Google Gemini 3 Pro + Gemini 3 Flash + Gemini 2.5 Pro · Mistral OCR 2.
- **Doc-AI commercial**: Azure DI prebuilt-{layout,document,invoice} · AWS Textract · Google DocAI (form parser + OCR) · LlamaParse Agentic + non-agentic · Reducto · Extend Parse 2.0 · LandingAI · Unstructured.io · Nanonets.
- **Frontier OSS / VLM-OCR**: Chandra (datalab-to/chandra-ocr-2 @ self-hosted vLLM) · MonkeyOCR + MonkeyOCR-Pro-3B (new) · PaddleOCR-VL 1.5 + 1.6 (new) · MinerU 2.5 + 2.5-Pro (new) + MinerU Pro hosted-OSS · DOTS-OCR · GLM-OCR · GOT-OCR 2.0 · Qwen 3-VL-235B · Marker 1.0 · Surya · Docling · Nougat · FireRed-OCR · Logics-Parsing-v2 · Tesseract 5.x · PaddleOCR v4 · EasyOCR · OpenOCR.
- **Hyperbots-IP `[FT]`** (modesty-anchored, contamination-audited): Qwen 3.6-35B-A3B `[FT]` (also pinned as D-36 extractor) · Qwen 2.5-VL-7B-F `[FT]` · Qwen 2.5-VL-3B-F `[FT]` · hyperapi-parse-intent `[FT]`.
- **Stretch (8)**: mPLUG-DocOwl 1.5 · DeepSeek-OCR-2 · Nanonets-OCR-s · LLaVA-1.6-34B · InternVL2-26B/76B · Llama-3.2-90B-Vision · Llama-4-Maverick · Youtu-Parsing.

Adapter wires fall into 3 contract shapes (class-based image-input vLLM · hosted REST multipart · OpenAI-shape chat); 7 REGISTRY entries today vs ~53 to wire at BUILD-v1 — explicitly budgeted.

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

## §5 — Honesty register (cannot-measure-today)

- **BLK-16** HyperAPI quota exhausted → blocks HyperAPI parse + classify columns until reset OR CEO Option B (paid-tier upgrade).
- **BLK-17** Chandra vLLM host `:8847` flaky → blocks Chandra cells; watcher armed.
- **BLK-18** SAVIOR-Bench gold corpus off-disk → blocks SAVIOR-anchored D-07/08/25 rows until corpus obtained.
- **Partner consent** required for T-09 pay stub · T-10 wire/ACH · T-13 tax form · T-14 insurance · T-15 loan · ZH/JA/KO/AR/HI scripts.
- **Structurally out-of-reach today**: T-11 10-Q / T-12 investor-presentation — HyperAPI IDP doc-type set excludes; D-15 is an *expected fail* dimension; Q-DR-5 open to CEO (restrict scope vs fund capmkts FT).

## §6 — License + customer-name discipline

License matrix (framework §9.1): ParseBench Apache-2.0 (the publishability anchor) · FUNSD/CORD/PubTabNet/DocLayNet/ChartQA permissive (public) · DocVQA CC-BY-NC (internal-only) · Hyperbots-internal corpora (no customer names) · SAVIOR partial (aggregate publishable per Appendix D). Customer-name 14-roster (verbatim from `_grep_guard.sh`) build-time-grep-guarded across every artifact. PII corpora synthetic-fill or partner-consent-gated.

## §7 — What's in BUILD-v0 (this package)

1. `PARSE-DEEP-BENCHMARK-FRAMEWORK-2026-06-11-v1.md` — full spec (~500 LOC, §0–§14)
2. `parse-deep-build-v0/methodology.md` — NeurIPS reproducibility checklist
3. `parse-deep-build-v0/tasks-additive-DQ-001-050.json` — 50 task entries, ADDITIVE-ONLY
4. `parse-deep-build-v0/cell-schema-v1.1.json` — JSON Schema 2020-12, backward-compat
5. `parse-deep-build-v0/index.html` — dashboard scaffold (registered-not-yet-run state)
6. `parse-deep-build-v0/BUILD-V0-LEDGER-2026-06-11.md` — acceptance-criterion mapping + grep-guard self-check

Zero cells run · $0 burned · no quota touched · no broadcasts fired.

## §8 — Decisions requested from reviewer

1. **APPROVE / APPROVE-WITH-CHANGES / REJECT** on the 50-dim list — anything missing? anything to cut?
2. **Panel completeness sign-off** — the 60 rows now include Opus 4.8, GPT-5.5, Gemini 3 Pro, Mistral OCR 2, PaddleOCR-VL 1.6, MinerU 2.5-Pro, MonkeyOCR + MonkeyOCR-Pro-3B per 2026-06-11 feedback; any further additions?
3. **Q-DR-5** (CEO): for D-15 capital-markets — restrict HyperAPI scope to AP/AR + payments + forms, OR fund a capital-markets fine-tune to bring T-11/T-12 into the doc-type set?
4. **BLK-16 Option A (wait reset) vs Option B (paid-tier upgrade)** for HyperAPI quota — blocks the HyperAPI parse + classify columns.
5. **Greenlight BUILD-v1?** — cell execution, gated on (3) + (4) + partner-corpus consent.

---

*Researcher-not-advocate · Hyperbots Research · 2026-06-11 · DRAFT INTERNAL until build-v0 reviewers verdict.*
