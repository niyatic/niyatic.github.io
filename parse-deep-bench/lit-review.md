# Document AI literature review — Parse Deep Benchmark v1

Date: 2026-06-15 · Companion to `framework.md` (51 dimensions A–K · 130-row panel · ParseBench / NeurIPS-paper bar) and `two-pager.md`. Authored by the Hyperbots Research team building the framework — read §0 for declared conflicts.

---

## §0 — Honest framing

This is a literature review by the team that is also designing the benchmark it underpins. That is the explicit conflict: every framing choice we make here, downstream, helps decide whether HyperAPI parse looks good or bad on a given dimension. We have tried to control for that by writing a review that (a) succeeds whether HyperAPI wins or loses on any dimension, and (b) cites the most damaging-to-our-design work as prominently as the most flattering. Reviewers should still treat this document as advocacy-adjacent and weight the framework spec against an external second read.

We are not advocates for any single architecture, vendor, or metric. We are advocates for the position that **document-AI benchmarking in 2026 is overdue for pre-registered, per-doc-score-vector, paired-bootstrap, contamination-audited evaluation** — and that the existing benchmark literature has converged on individual ingredients of that recipe without anyone shipping all of them in one place. We owe the reader an honest map of how the field got here, what is broken about how it currently evaluates models, and what we are doing about it.

A note on the Hyperbots brand guardrail: we do not use the framing "HITL" or "human-in-the-loop" in this document or anywhere else in external content. Where the literature uses it, we paraphrase.

---

## §1 — Scope and method

### What we swept

- **arXiv** (cs.CV, cs.CL, cs.IR) — papers indexed through Q2 2026.
- **Major venue proceedings**: CVPR · ICCV · ECCV · NeurIPS · ICML · ICLR · ACL · EMNLP · NAACL · ICDAR · KDD · WWW (2018–2026, with emphasis on 2023–2026).
- **HuggingFace dataset cards and model cards** for benchmark and model lineage.
- **Vendor whitepapers and product docs** for the commercial IDP segment (ABBYY, Rossum, Hyperscience, Reducto, Extend, LandingAI, Mindee, Klippa, Unstructured.io, LlamaIndex / LlamaParse, Azure DI, AWS Textract, Google DocAI).
- **Internal Hyperbots research**: the 2026-05-27 9-D framework, F-B-STUDY (parse benchmark smoke), SAVIOR-Bench paper, the parse-x-research dossier, DOC-TYPE-GAPS.
- **Selected technical blogs** from labs (Allen AI, Microsoft Research, Google Research, Meta AI, OpenAI, Anthropic, Mistral, DeepSeek, Alibaba DAMO, Baidu, Zhipu) when they ship novel evaluation methodology not yet captured in a paper.

### Date cutoff and known gaps

Cutoff is early Q2 2026. Notable known gaps in our coverage:
- **Non-English-language venue work** beyond high-profile lab releases — we under-sample Chinese-language venues (CCF) and Japanese venues (PRMU) despite that being where some of the strongest OCR/VLM work originates today.
- **Industrial conference talks** (Snorkel · Databricks · LlamaCon · NVIDIA GTC) — partial coverage; we relied on published-paper artifacts rather than recorded sessions.
- **Vendor benchmarks** are by definition vendor-built; we treat them as evidence but never as ground truth (the comparative-study I-2 invariant: results.zip is never gold).

### Inclusion / exclusion criteria

- We include a work if it (a) introduces a benchmark or metric still used in 2026 evaluation, (b) defines an architectural paradigm we panel in the framework, or (c) sets a methodological bar (pre-registration, contamination audit, paired bootstrap) we explicitly emulate.
- We exclude work that is dominated by a later citation we already include (cluster the lineage).
- We exclude scene-text and natural-image OCR threads except where they cross-pollinate with document OCR. See §10 for the full exclusion list.

Where we cite without having verified a paper to the abstract level, we mark it as `[unverified]` so reviewers can flag it.

---

## §2 — The benchmark lineage

A benchmark earns its place by being run by more than its authors. The doc-AI benchmark lineage is roughly:

| Year | Benchmark | Measures | n (test) | Why still cited in 2026 |
|---|---|---|---|---|
| 2003–2017 | ICDAR robust reading challenges | scene + doc text detection / recognition | varies | foundational; OCR taxonomy still inherited |
| 2019 | **FUNSD** (Jaume et al.) | form KIE: entity-F1 over header/question/answer/other | 50 | the canonical Western-form KIE benchmark; still the FT-vs-zero-shot dividing line |
| 2019 | **CORD** (Park et al.) | receipt entity-F1; canonical receipt schema | ~1,000 | the receipts canonical schema; widely-overlapped with FT training sets — contamination risk high |
| 2020 | **PubTabNet → TEDS** (IBM, Zhong et al.) | table-structure recognition; HTML emission; TEDS metric | ~9k | TEDS is the dominant table-structure metric still in 2026 |
| 2021 | **DocVQA** (Mathew et al.) | extractive doc-VQA; ANLS metric | 5k+ | ANLS is the dominant VQA metric; the benchmark itself shows ceiling effects |
| 2022 | **DocLayNet** (Pfitzmann et al., IBM) | layout COCO-mAP over 6 element classes (text, title, list, table, figure, page-header) | 80k pages | DocLayNet is the layout-mAP anchor for any panel claiming layout-awareness |
| 2022 | **XFUND** (Microsoft) | multilingual FUNSD across 7 languages | ~50/lang | the multilingual-KIE anchor; calls out the EN-overfit problem |
| 2022 | **ChartQA** (Masry et al.) | chart-data-point match accuracy | ~1.5k | chart understanding split out from doc-VQA; small-n but still used |
| 2023 | **DUDE** (Van Landeghem et al.) | document understanding benchmark; multi-task | ~5k | combines extraction + reasoning + summarization |
| 2024 | **OCRBench** (Liu et al.) | broad OCR capability over 29 sub-benchmarks | ~1k each | the broadest single OCR-eval-aggregator for VLMs |
| 2024 | **OmniDocBench** (Ouyang et al.) | document parsing over 9 types and 4 languages | ~1k | the most heterogeneous doc-parsing benchmark; per-language CER breakouts |
| 2025 | **olmOCR-Bench** (Allen AI) | open-license OCR benchmark accompanying olmOCR | ~1k | first benchmark to ship with open-license commitments end-to-end |
| 2025 | **OCRBench v2** (Liu et al.) | OCRBench successor; better task balance, harder layout tasks | ~3k | the de-facto VLM-OCR leaderboard in 2025–2026 |
| 2026 | **ParseBench** (run-llama, arXiv:2604.08538) | 5 splits (chart 4,864 · layout 16,325 · table 503 · text_content 141,322 · text_formatting 5,997 = 169,011 rules) with **per-rule pass/fail** | ~7k docs | the publishability anchor for our work — per-rule = per-doc score vector makes CIs computable for free; Apache-2.0 |
| 2026 | **RealDocBench** (Extend, internal-leaning) | 1,500 layout samples + 1,359 Q&A | mixed | vendor-built; Extend leads on its own bench (0.847 layout / 95.7% Q&A); we contrast but never head-to-head |
| 2026 | **SAVIOR-Bench v1** (Hyperbots, internal) | 3-facet decoupling (transcription / extract / layout); F1–F10 failure taxonomy; n=509; IAA 0.761 | 509 | our discipline anchor; Appendix D 4-part provenance contract; honestly attests "ci95=null" where per-doc vectors are unavailable |

### Lineage commentary

The honest story of the field is that **benchmarks have grown wide and shallow.** OCRBench v2 spans many sub-tasks but at n≈3k per task you cannot compute CIs that distinguish two top models. DocVQA hit ceiling effects on extractive tasks around 2023 — most frontier VLMs sit within 1–2 ANLS of each other. ChartQA has small-n known-error labels. The 2025–2026 inflection — ParseBench, OmniDocBench, OCRBench v2 — is the field starting to say *we need many more rules per doc to get statistical power*, and ParseBench is the cleanest expression of that idea: tens of thousands of pass/fail rules over a smaller doc corpus.

What ParseBench gets right and we inherit: **per-rule scoring is per-doc score vector**. That makes CIs computable without changing the metric. Cross-dimension claims still need multiplicity correction (Holm-Bonferroni or equivalent), which to our knowledge no current public benchmark enforces.

What SAVIOR-Bench (our in-house) gets right that the public lineage does not: the 4-part Appendix D cell contract (`provenance · pins · rerun_command · factory_reproduced`) makes every published cell rerunnable. The drift mode in public benchmarks today is *attested* numbers from a vendor that no third party can re-produce. SAVIOR is honestly attested-not-reproduced where the per-doc vectors are off the per-cell artifact.

What everyone is still bad at: **contamination audit on FT models** (CORD overlap with Donut/LayoutLM FT splits is well-known but under-reported in headline tables); **per-language stratification** (XFUND helps but ZH-Hans/JA/AR finance docs are partner-gated); **long-doc evaluation** (most benchmarks cap at 10–50 pages; 10-Q is 200–600pp).

---

## §3 — Evaluation metric lineage

Metrics are where the field has the most accumulated technical debt. Most published rankings depend on the metric choice, and most papers do not run the cross-metric correlation check. The lineage:

### §3.1 — Text fidelity

- **CER / WER** (1990s ASR roots → applied to OCR) — character/word error rate. CER is normalized by gold-text length; standard for character-script languages (ZH/JA/KO). WER is the Western-script default. The two disagree on rank order on dense pages because insert/delete cost asymmetry matters more there. We measure both (D-10 + D-11) precisely because they disagree.
- **Levenshtein-normalized edit distance** — same family, different normalization. Most papers report one or the other; few report both. Our D-09 reports edit-distance specifically for rank-correlation calibration against attested baselines.
- **ANLS** (Average Normalized Levenshtein Similarity, Biten et al. for ST-VQA / DocVQA, 2019) — the VQA-style answer-similarity metric. Saturates around 0.85–0.90 on DocVQA for frontier VLMs.
- **Word recall / precision** (multiset matching) — SAVIOR-Bench-style. Differentiates hallucinating VLMs from transcription-faithful pipelines; the gap between best-VLM and Tesseract on precision is often >0.15 because VLMs hallucinate plausible-but-wrong text.
- **BERTScore** (Zhang et al., 2020) — semantic similarity for free-text; gives credit for paraphrase. Used downstream in summary/extraction evaluation but rarely on OCR transcripts.

### §3.2 — Table structure

- **TEDS** (Tree-Edit-Distance over Structure, Zhong et al., 2020, with PubTabNet) — the dominant table-structure metric. Computes edit distance over the HTML tree representation; can be variants (TEDS-Struct vs TEDS-Content).
- **GriTS** (Smock et al., 2023, with Table Transformer / TATR) — Grid Table Similarity; cell-content-aware, less sensitive to representational choices than TEDS.
- **GTRM / GTRM-combined** (per ParseBench README, 2026) — combined GriTS + TableRecordMatch; the metric our D-31 measures. Buyer-relevant: it asks whether the table content as a record set matches gold.
- **Cell-content F1** — per-cell match with row-type stratification (header / data / total). Differentiates content-faithful from structurally-impressive emissions.

Cross-metric reality: TEDS and GriTS rank-correlate around 0.85 in published comparisons, but where they disagree is where the model is doing something structurally clever (or structurally cheating). Always report both.

### §3.3 — Layout

- **COCO-style mAP** (over DocLayNet element classes, mAP@.5/.75/.95) — the canonical layout-detection metric.
- **Reading-order rank correlation** — normalized rank correlation between predicted and gold reading orders. Decorrelates from element-detection on multi-column documents (you can detect every element and still misorder them).
- **Layout-element accuracy** (ParseBench) — per-element pass/fail against gold tree.
- **PaIRS** (pairwise spatial relationship, z-euclidean, vlm_ocr@1fbbc334 vendor code) — the only published cross-vendor layout-fidelity metric with attested SAVIOR numbers. Strictly "prompt-controlled" cells only; never cross-compare PC and NPC.

### §3.4 — Field-grounding / bbox

- **IoU** (per matched token, IoU ≥ 0.5 threshold for grounding "hit") — standard.
- **Field-to-region grounding accuracy** — downstream-extract-conditional. Some models with weak grounding still produce strong extract F1 because the extractor compensates; the grounding metric matters when the downstream consumer needs the box, not the value.

### §3.5 — Latency / cost

- **p50 / p95 / p99 latency** — per-page; the tail-latency metric (p99) surfaces outliers.
- **$/correct call** — cost-per-page × inverse-accuracy. Re-ranks the panel vs raw accuracy; OSS dominates ROI even when frontier rows lead accuracy. Underreported in headline tables.

### §3.6 — Reliability / reproducibility

- **CI95 bootstrap** with explicit n and per-doc score vector.
- **Paired bootstrap** for "A vs B same doc" claims (D-36 lift, model-vs-baseline).
- **Holm-Bonferroni multiplicity** for cross-dimension headline claims.
- **Cohen κ / Krippendorff α** for IAA on annotated corpora.
- **Factory-reproduced gate** — `repro_check.py`-style binary gate per cell. SAVIOR introduced this; the public benchmark literature has not converged on it.

### §3.7 — The universal eval-metric problem

In 2026 the field has more output formats than ever (HOF, Markdown, HTML, Tokens+BB, JSON-schema, structured data classes). No single metric works across all four. The Hyperbots-internal **UEM** proposal (our D-51, v1.1 amendment) is one cut: judge-LLM-derived diff features for cross-format comparisons, model-free diff features for same-format. Related public work: structured-output evaluation (Chen et al., 2024 — JSON-schema matching), schema-grounded F1 (Extend-style), and the Allen AI olmOCR-Bench multi-format harness. None solve the cross-format problem at scale; UEM is our attempt and we register the gates K-1..K-4 honestly before running any cell.

---

## §4 — Architectures: OCR pipelines → VLMs → unified doc-converters

### §4.1 — The pre-deep-learning baseline

**Tesseract** (Smith, 2007 → 4.x with LSTM, 2017 → 5.x current) and **OCRopus** (Breuel, 2008) — heuristic + CTC pipelines. Still production-grade-floor and the cheapest cost baseline in 2026. On digit-MICR fidelity, Tesseract 5.x **beats** Chandra and most VLMs at fraction of cost — a finding we replicated in our F-B smoke (Tesseract 0.793 vs Chandra 0.455 on `bag_of_digit_percent`). The lesson: "frontier" does not mean "best on every dimension."

### §4.2 — CNN + CTC OCR

**CRNN** (Shi et al., 2017) and the broader CTC-loss-trained CNN family. Largely superseded by transformer OCR for end-to-end document reading but still common as a component (Surya uses a recognition head of this family). Solid CER baselines.

### §4.3 — Transformer OCR

**TrOCR** (Li et al., Microsoft, 2021) — encoder-decoder transformer over patches → text. The first widely-cited transformer OCR; still a strong reproducible baseline. The two-stage detect-then-recognize pipeline (e.g. Surya = detect-then-recognize + layout) remains competitive when the inputs are clean-scan.

### §4.4 — OCR-free document reading

**Donut** (Kim et al., Naver Clova, 2021) — encoder-decoder VLM trained directly on doc-image → structured-output. Skips the OCR stage. Strong on receipts (CORD-FT) but contamination-prone on CORD; honest evaluation requires held-out splits.

**Pix2Struct** (Lee et al., Google, 2022) — pretrained on screenshot→HTML; transferable to many downstream doc tasks. Now superseded by larger VLMs but the screenshot-as-pretraining-signal idea recurs in later VLM pretraining.

**Kosmos-2.5** (Microsoft, 2023) — OCR-free reading model with explicit bbox emission. The bbox-emission capability matters for the D-26/D-27 dimensions; many later VLMs lost this and have to be coaxed back via prompting.

### §4.5 — Layout-aware document language models

**LayoutLM** (Xu et al., Microsoft, 2019) → **LayoutLMv2** (2020) → **LayoutLMv3** (2022) — joint text + layout pretraining. The defining family for KIE benchmarks (FUNSD, CORD) in the pre-VLM era.

**LiLT** (Wang et al., 2022) — language-independent layout transformer; reduces the EN-overfit problem in LayoutLM. Still a strong multilingual KIE baseline.

**UDOP** (Tang et al., Microsoft, 2022) — unified document processing; vision + text + layout in one transformer.

**ERNIE-Layout** (Peng et al., Baidu, 2022) — layout-pretrained with strong ZH support; underrated outside Chinese-language venues.

**LayoutXLM** (Microsoft, 2022) — multilingual extension of LayoutLM; the XFUND-companion model.

**DocFormer / DocFormerV2** (Appalaraju et al., Amazon, 2021/2023) — multi-modal document transformer; recurrent strong baseline on FUNSD-family.

### §4.6 — Table-specialized

**Table Transformer / TATR** (Smock et al., Microsoft, 2023) — DETR-style table detection + structure recognition. The most reproducible OSS table baseline; trained on PubTables-1M.

**TableFormer** (IBM) — encoder-decoder approach to table structure.

**StructEqTable** (OpenDataLab) — structured-equation tables; niche but relevant for 10-Q financial-schedule extraction.

### §4.7 — Document-converter VLMs (2024–2026 wave)

**Marker** (datalab-to, 2024) — markdown-converter VLM pipeline with layout + OCR stages.

**MinerU** (OpenDataLab, 2024 → 2.5 → 2.5-Pro → Pro hosted, 2026) — layout-aware doc converter; strong on academic-PDF parsing.

**Chandra (chandra-ocr-2)** (datalab-to, 2026) — vLLM-served VLM; emits structured HTML with `<div data-bbox=… data-label=…>` and `<table>` natively. The only engine in our panel that emits all four ParseBench primary metrics directly. Wins ParseBench-table GriTS in our F-B smoke (0.800 at n=10) — re-anchored at n=100 in BUILD-v1.

**MonkeyOCR / MonkeyOCR-Pro-3B** (Yuliang-Liu et al., 2025–2026) — structure-respecting OCR; the Pro-3B variant pushes parameter-efficiency.

**DOTS-OCR (dots.ocr)** (rednote-hilab, 2025) — layout-emitting OCR; strong on tables.

**GOT-OCR 2.0** (StepFun, 2024) — general OCR text recognition; reads from screenshots.

**GLM-OCR** (Zhipu, 2025) — OCR variant of GLM-4V family; among the best edit-distance results on attested rankings.

**PaddleOCR-VL 1.5 / 1.6** (PaddlePaddle, 2025–2026) — the largest open-source production OCR family; pipeline + VL extensions.

**Logics-Parsing v2** (Logics, 2025) — newer entry; layout + table.

**Surya** (datalab-to, 2024) — layout + OCR + reading-order; widely panel-included.

**Docling** (IBM, 2025) — IBM's open-source doc converter; layout-aware, table-aware.

**Nougat** (Meta AI, 2023) — scientific-PDF specialist; LaTeX-aware.

**FireRed-OCR** (Xiaohongshu, 2025) — newer entry; ZH-strong.

**olmOCR / olmOCR-2** (Allen AI, 2025–2026) — open-license open-data OCR; the most rigorous about reproducibility.

**RolmOCR** (Reducto, 2025) — open-weights distill of Reducto's hosted model; rare in being an enterprise-vendor open-weight release.

**SmolDocling** (HuggingFace, 2025) — 256M-parameter doc converter; demonstrates that small models can be competitive at the parsing task when targeted.

### §4.8 — Frontier multimodal closed-source

**Anthropic Claude family** — Opus 4.x / Sonnet 4.x / Haiku 4.x. Strong general doc QA; weaker explicit bbox emission than purpose-built OCR.

**OpenAI GPT family** — GPT-4o → GPT-5.4 → GPT-5.5 (via Azure OpenAI Service per our internal directive). Strong VQA; cost-per-correct rarely competitive against OSS on transcription-heavy tasks.

**Google Gemini** — Gemini 2.5 Pro → Gemini 3 Flash → Gemini 3 Pro. The Flash tier shifted the cost-per-correct curve in 2026.

**xAI Grok-4 vision** (2026) — frontier multimodal entrant.

**Cohere Command R+ vision** (2026) — frontier multimodal with enterprise-RAG focus.

**Mistral OCR / Mistral OCR 2** — Mistral's purpose-built OCR; a notable shift for a frontier-lab to ship a non-general-VLM endpoint.

**Reka Core vision** (2026) — frontier multimodal with smaller-than-leader scale.

### §4.9 — Frontier multimodal open-weight

**Qwen-VL family** — Qwen 2.5-VL → Qwen 3-VL-235B. Strong all-round; Hyperbots fine-tunes on Qwen 3.6-35B-A3B and Qwen 2.5-VL-7B-F/3B-F under our `[FT]` discipline.

**InternVL2 → InternVL3** (Shanghai AI Lab, 2024–2025) — leaderboard-top on many VLM benchmarks; the 78B variant is the heaviest open-weight competitive panel member.

**Llama-3.2-Vision** (11B / 90B, Meta, 2024) — Meta's first vision-instruct family.

**Llama-4-Maverick** (Meta, 2025) — large MoE multimodal.

**DeepSeek-VL2** (DeepSeek, 2024) — MoE multimodal; small efficient model.

**DeepSeek-Janus-Pro 7B** (DeepSeek, 2025) — unified multimodal (understanding + generation).

**MiniCPM-V 2.6 / MiniCPM-o 2.6** (OpenBMB) — efficient 8B-class VLMs.

**Idefics3** (HuggingFace, 2024) — open vision-language model with the openness norms HuggingFace insists on.

**CogVLM2** (Zhipu, 2024) — strong on doc-VQA.

**InternLM-XComposer 2.5** (Shanghai AI Lab, 2024) — long-context multimodal.

**Phi-4-multimodal** (Microsoft, 2025) — small but strong; on-device-feasible.

**Pixtral 12B** (Mistral, 2024) — Mistral's first open-weight multimodal.

**Molmo (1B / 7B / 72B)** (Allen AI, 2024) — open multimodal with pointer-grounding (rare and useful for doc-AI).

**Aria** (Rhymes AI, 2024) — MoE multimodal.

**Cambrian-1** (NYU, 2024) — vision-centric multimodal tuning study.

**NVIDIA VILA** (2024) — long-context multimodal.

**Mini-Gemini** (Li et al., 2024) — efficient dual-encoder.

**MAmmoTH-VL** (2024) — math + chart heavy specialist.

**Apple OpenELM-VL** (Apple, 2025) — on-device baseline.

**LG EXAONE 3.5 VL** (LG AI Research, 2025) — KO-strong VLM.

### §4.10 — Architecture commentary

The trajectory is clear: OCR-as-a-pipeline → end-to-end doc-converter VLMs → general multimodal frontier models. Each step **gains** generality and **loses** something the prior step did well:

- Heuristic OCR → CNN+CTC: gained accuracy on dense pages, lost interpretability of glyph-level confidence.
- CNN+CTC → transformer OCR: gained long-range context, lost per-character locality.
- Transformer OCR → OCR-free reading: gained schema-aware emission, lost the ability to ship a CER on raw text.
- OCR-free reading → doc-converter VLM: gained layout-aware emission, lost stable bbox grounding.
- Doc-converter VLM → frontier multimodal: gained reasoning and instruction-following, lost cheap inference and (often) the bbox emission entirely.

The right architecture is **per dimension**. Our framework explicitly avoids declaring a single winner. The most likely 2026 production system is an **ensemble**: a frontier VLM for reasoning + a doc-converter VLM for structure + a CNN+CTC fallback for digit fidelity + a heuristic for layout silver gold. The ensemble ablations E1–E9 in the framework spec are how we test that claim.

---

## §5 — The finance-document subfield

### §5.1 — Why finance docs are hard

- **Dense tables** with merged cells, nested headers, multi-row totals — 10-Q financial schedules are the worst case. Most doc-converter VLMs lose structure on nested tables.
- **MICR lines on cheques** require precise digit fidelity; Tesseract still beats most VLMs because the VLMs hallucinate digit shapes they have seen in training.
- **Multi-column 10-Q and investor-presentation layouts** — reading order is the failure mode; the model can detect every element and still emit them in the wrong order.
- **Long-doc tail** — 10-Qs are 200–600 pages; tax forms can be longer with appendices. Most VLMs have a 32k–128k token context and cost scales linearly.
- **Mixed numeric + free-text** — "Net income of $4.2B vs $3.8B prior year (10% growth)" mixes structured and unstructured signal; extractors that handle one cleanly often fumble the other.
- **PII gates** — pay-stubs, wire/ACH receipts, tax forms, insurance, loan packages cannot be publicly shared without redaction. This is a structural barrier to public benchmarks for the application area where doc-AI revenue actually sits.

### §5.2 — Enterprise IDP vendors

- **ABBYY** — FineReader Engine + Vantage. The incumbent. Strong on European-language IDs and forms; weaker on frontier-VLM-style schemas.
- **Rossum** — transactional-doc IDP; strongest on invoice + remittance flows. RossumCloud APIs are the production benchmark to beat for AP/AR.
- **Hyperscience** — DocLayNet-era leader; classification + extraction; enterprise on-prem.
- **Reducto** — newer entrant; ships RolmOCR open-weights; doc-AI-focused.
- **Extend** — Extend Parse 2.0 + RealDocBench (vendor-built). Leads on its own benchmark; we never run head-to-head from our harness because we hold no Extend API key.
- **Hyperbots** — our team; HyperAPI parse + parse-intent + classify + extract primitives; SAVIOR-Bench attests the in-house numbers.
- **Klippa · Mindee · Veryfi · Affinda** — receipts / IDs / payslip specialists; strong cost-per-correct at low end.
- **Sensible · Instabase · Indico** — long-doc / configurable schema players.
- **IBM Watson Discovery · Oracle Document Understanding** — enterprise platform tier.
- **Adobe Acrobat AI Extract · Foxit AI Document Intelligence** — the PDF-vendor incumbents joining the IDP race.
- **A2iA (Mitek)** — handwriting + cheque specialist; the unsexy but production-grade incumbent.

The honest commentary: enterprise IDP vendors are **measured by their customers, not by public benchmarks**. RossumCloud's actual accuracy on a specific AP customer's invoice stream is the number that matters; the public-benchmark numbers are marketing.

### §5.3 — KYC / AML adjacency

KYC OCR is a parallel subfield (HyperVerge, Onfido, Jumio, Veriff) optimized for ID-card extraction with strong PII safeguards. The architectures look like miniature doc-AI; the evaluation rigor is generally lower because the buyers care about end-to-end fraud-prevention, not parse F1.

---

## §6 — Evaluation rigor: pre-registration, paired bootstrap, multiplicity, contamination

### §6.1 — Why this matters

Document-AI vendor benchmarks routinely commit two failure modes: **(a)** silently tuning the metric to make the headline look better after the cells run, and **(b)** reporting the dimensions where the home team wins and quietly omitting the ones where it loses. Pre-registration cuts off both. Our framework spec is the pre-registration: dimensions fixed at 51 before any cell executes, baselines named per dimension, headline winner is whoever the data names.

### §6.2 — SAVIOR-Bench Appendix D 4-part contract as a model

`provenance · pins · rerun_command · factory_reproduced` per cell. Provenance is free-text + URL/path to the source-of-truth artifact. Pins is the (model_version, sdk_commit, harness_commit, prompt_id, env_hash) tuple. Rerun_command is a single shell line that reproduces the cell from the repo root. Factory_reproduced is `false` at adapter emit time and only flips to `true` after `repro_check.py` exits 0.

This is what the public-benchmark literature has not converged on. Most public leaderboards have provenance (a citation) and rerun_command (a repo link) but no pins (the env / prompt / version that produced the number is usually under-specified) and no factory_reproduced gate (you trust the author's number, you don't re-verify).

### §6.3 — NeurIPS reproducibility checklist

NeurIPS 2024+ requires a reproducibility-checklist answer per paper: scope-match, limitations, reproducibility, open-access, statistical significance, compute resources, code-of-conduct, broader impacts, safeguards, license, attribution, asset documentation, human-subjects, IRB. Our methodology answers all 18 items in `methodology.md §8`.

### §6.4 — The contamination problem

FT models trained on doc benchmarks contaminate their own evaluation. CORD overlap with Donut-FT is well-known. FUNSD overlap with LayoutLM-FT is well-known. SAVIOR-Train overlap with our `[FT]` rows must be audited per-row, with `mitigation = held-out / re-scored / accepted-with-flag / unresolved` and unresolved → cell stays `factory_reproduced = false`.

The field is bad at this. Most benchmark papers do not audit contamination at all; the assumption is "if it's a test split, it's clean." But test splits are absorbed into pretraining corpora when those corpora are web-scale, and the contamination is silent. We treat the contamination audit as non-waivable per the comparative-study I-4 invariant.

### §6.5 — Paired bootstrap and multiplicity

For "A vs B same doc" claims (parse-lift D-36, model-vs-baseline on the same panel), paired bootstrap on `doc_id` strata is the right procedure. Independent bootstrap is wasteful — paired CIs are often 30%+ tighter because per-doc correlation between conditions is high.

For cross-dimension headline claims ("wins on N of 50"), naive p-values do not control family-wise error rate. Holm-Bonferroni or Benjamini-Hochberg are the standard corrections. Public benchmarks rarely apply either; we make it explicit (per-dim α ≈ 0.001 = 0.05/50) so we do not embarrass ourselves at NeurIPS review.

---

## §7 — Open problems (2026)

### §7.1 — Bbox emission inconsistency

Frontier VLMs (Claude, GPT, Gemini) have inconsistent and prompt-dependent bbox emission. They can be coaxed to emit boxes but the boxes are often pixel-shifted by quantization artifacts of the patch encoder. Purpose-built OCR (Chandra, Tesseract, Surya) emits stable boxes natively. The field has not converged on a single bbox-emission protocol.

### §7.2 — Long-doc tail

10-Q (200–600pp), 10-K (300–800pp), tax-form appendix-heavy filings. Most VLMs hit context limits or cost ceilings. The 300s server-side extract timeout is a cross-vendor production bottleneck (BLK-4 in our internal blocker registry). E6 page-chunked long-doc ensemble is one fix; whether it preserves cross-page reading order is an open question.

### §7.3 — Multilingual finance docs

XFUND covers 7 languages but not in finance-doc-specific form. ZH-Hans/JA/AR finance docs are partner-gated by structurally — banks do not release real customer documents. Synthetic-fill is a partial mitigation but synthetic-vs-real gap remains a research direction. SAVIOR-Bench residual F9 (multilingual + very-dense cluster persists post-FT) is the empirical name of this open problem.

### §7.4 — Contamination of FT rows

See §6.4. Both the metric (per-row contamination audit) and the protocol (`mitigation` enum) are under-converged in the public literature.

### §7.5 — Agentic vs non-agentic

LlamaParse Agentic vs LlamaParse non-agentic, Chandra agentic prompting vs zero-shot, Reducto's agentic doc-parsing — these are different *systems* with different latencies, costs, and failure modes. The field has not converged on whether to evaluate them in the same panel cell or in separate cells. Our framework treats agentic-vs-non-agentic as a property of systems (folded into D-36 lift + paired bootstrap), not a separate dimension; that is one defensible call but not the only one.

### §7.6 — The universal eval-metric problem

Cross-format comparison (HOF↔Markdown↔HTML↔Tokens+BB) — no single public metric does it cleanly. Our D-51 UEM is a proposal; whether judge-LLM-derived diff features survive cross-LLM judge variance is the K-3 calibration question we have registered but not yet answered.

### §7.7 — Cost-per-correct vs accuracy

Most leaderboards do not publish $/correct. Buyers care about it more than they care about the top-line accuracy. The Pareto front of cost vs accuracy is the most undervalued artifact a benchmark can ship. Our E5 cost-cascade ablation is explicit; the public literature lacks an equivalent norm.

### §7.8 — Partner-gated PII

Pay-stubs, wire/ACH, tax forms, insurance, loan packages cannot be publicly shared. This caps the public-benchmark surface for the application area where doc-AI revenue lives. Federated evaluation (run-locally, ship-the-numbers) is one proposed direction; we don't yet endorse it because the protocols for ensuring no model-update-via-leakage are immature.

### §7.9 — Streaming / online evaluation

Production doc-AI systems serve streams, not one-shot batches. Drift detection, online-recalibration, model-version-rollover — none of these are in any public benchmark we cite. Our D-46/D-49 gates are static; this is honest scope.

### §7.10 — Adversarial robustness

Adversarial perturbations on doc images (printed adversarial patches, fonts designed to fool OCR) are an emergent threat. The field is younger than scene-text adversarial work and we do not include it in v1.

---

## §8 — How this framework engages each open problem

| Open problem | Framework engagement |
|---|---|
| §7.1 bbox inconsistency | D-26 BBOX-IOU-TOKEN + D-27 BBOX-FIELD-TO-REGION with match-rate reported per cell; engines that don't emit boxes get `n/a`, not zero |
| §7.2 long-doc tail | D-45 PAGE-SCALING binned at {1pp, 10pp, 50pp, 200pp+} + E6 page-chunk ensemble ablation |
| §7.3 multilingual finance | D-20 LANG-CER-PER-SCRIPT over 10 scripts + D-22 mixed-script; partner-gated cells honestly flagged PENDING-CORPUS |
| §7.4 contamination | D-50 REPRO-CONTAMINATION as a binary gate; methodology §5 protocol; mitigation enum; honest red flag on unresolved |
| §7.5 agentic-vs-non-agentic | Folded into D-36 paired-bootstrap lift + ensemble ablations; explicit acknowledgement in §12 of the framework |
| §7.6 universal eval-metric | D-51 UEM v1.1 amendment with K-1..K-4 gates registered before cells run |
| §7.7 cost-per-correct | D-43 COST-DOLLAR-PER-CORRECT + E5 cost-cascade Pareto |
| §7.8 partner-gated PII | Honest PENDING-CORPUS / partner-consent flags; framework §9 license matrix; no fabrication |
| §7.9 streaming / online | Out of scope for v1; methodology §10 amendment procedure documents the way in for v1.x |
| §7.10 adversarial | Out of scope; not registered; future v2 work |

Where this framework will fail: any dimension whose gold cannot be reproduced from public corpora ends up partner-gated or PENDING-CORPUS, which means we will publish honest "not measured" rather than fake "great." That is the price of researcher-not-advocate.

---

## §9 — Annotated bibliography

### §9.1 — Benchmarks

1. Jaume, G., Ekenel, H. K., & Thiran, J.-P. (2019). *FUNSD: A Dataset for Form Understanding in Noisy Scanned Documents.* ICDAR-OST. — Foundational form-KIE benchmark; the entity-F1 protocol still inherited.
2. Park, S. et al. (2019). *CORD: A Consolidated Receipt Dataset for Post-OCR Parsing.* NeurIPS Doc Intelligence Workshop. — Canonical receipt schema; contamination-prone with FT models.
3. Zhong, X., ShafieiBavani, E., & Jimeno-Yepes, A. (2020). *Image-based Table Recognition: Data, Model, and Evaluation.* ECCV. — PubTabNet + TEDS metric.
4. Mathew, M., Karatzas, D., & Jawahar, C. V. (2021). *DocVQA: A Dataset for VQA on Document Images.* WACV. — The ANLS-anchored doc-VQA benchmark.
5. Pfitzmann, B. et al. (2022). *DocLayNet: A Large Human-Annotated Dataset for Document-Layout Analysis.* KDD. — Layout COCO-mAP gold standard.
6. Xu, Y. et al. (2022). *XFUND: A Multilingual Dataset for Form Understanding.* ACL. — Multilingual KIE anchor.
7. Masry, A. et al. (2022). *ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning.* ACL Findings. — Chart-data-point match.
8. Van Landeghem, J. et al. (2023). *Document Understanding Dataset and Evaluation (DUDE).* ICCV. — Multi-task doc-understanding benchmark.
9. Liu, Y. et al. (2024). *OCRBench: On the Hidden Mystery of OCR in Large Multimodal Models.* arXiv:2305.07895. — Broad VLM-OCR aggregator.
10. Ouyang, L. et al. (2024). *OmniDocBench: Benchmarking Diverse PDF Document Parsing.* arXiv. [unverified — confirm exact citation] — Heterogeneous doc parsing.
11. Liu, Y. et al. (2025). *OCRBench v2.* arXiv. [unverified] — Successor benchmark.
12. Allen AI (2025). *olmOCR and olmOCR-Bench.* HuggingFace dataset card; technical report. — First end-to-end-open-license OCR benchmark.
13. run-llama (2026). *ParseBench: Per-Rule Evaluation of Document Parsers.* arXiv:2604.08538. — Per-rule pass/fail; 169,011 rules; Apache-2.0; our publishability anchor.
14. Extend (2026). *RealDocBench and Extend Parse 2.0.* Vendor-published. — The vendor-built contrast benchmark; never head-to-head.
15. Hyperbots Research (2026). *SAVIOR-Bench v1.* Internal paper; Appendix D 4-part cell contract; n=509; IAA 0.761. — Our discipline anchor.

### §9.2 — Metrics

16. Biten, A. F. et al. (2019). *Scene Text Visual Question Answering.* ICCV. — Introduced ANLS for VQA.
17. Smock, B., Pesala, R., & Abraham, R. (2023). *Aligning Benchmark Datasets for Table Structure Recognition.* ICDAR. — GriTS metric.
18. Zhang, T. et al. (2020). *BERTScore: Evaluating Text Generation with BERT.* ICLR. — Semantic-similarity metric for free text.
19. Hyperbots vlm_ocr team (2026). *PaIRS metric (pairwise spatial relationship z-euclidean).* Internal vendor code, commit 1fbbc334. — Layout-fidelity metric we vendor.
20. Smith, R. (2007). *An Overview of the Tesseract OCR Engine.* ICDAR. — Tesseract foundational paper; CER/WER baseline.

### §9.3 — Architectures

21. Shi, B., Bai, X., & Yao, C. (2017). *An End-to-End Trainable Neural Network for Image-based Sequence Recognition (CRNN).* IEEE TPAMI. — CNN+CTC OCR.
22. Li, M. et al. (2021). *TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models.* AAAI 2023. — Transformer OCR baseline.
23. Kim, G. et al. (2021). *Donut: Document Understanding Transformer without OCR.* ECCV 2022. — OCR-free reading; CORD-FT contamination-prone.
24. Lee, K. et al. (2022). *Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding.* ICML 2023. — Screenshot-as-pretraining-signal.
25. Lv, T. et al. (2023). *Kosmos-2.5: A Multimodal Literate Model.* arXiv. — OCR-free with bbox emission.
26. Xu, Y. et al. (2019/2020/2022). *LayoutLM / LayoutLMv2 / LayoutLMv3.* KDD / ACL / ACM MM. — The layout-aware language-model family.
27. Wang, J. et al. (2022). *LiLT: A Simple yet Effective Language-independent Layout Transformer.* ACL. — Multilingual layout.
28. Tang, Z. et al. (2022). *Unifying Vision, Text, and Layout for Universal Document Processing (UDOP).* CVPR 2023. — Unified doc processing.
29. Peng, Q. et al. (2022). *ERNIE-Layout.* EMNLP Findings. — ZH-strong layout.
30. Xu, Y. et al. (2022). *LayoutXLM.* arXiv. — Multilingual LayoutLM.
31. Appalaraju, S. et al. (2021/2023). *DocFormer / DocFormerV2.* ICCV / AAAI. — Multimodal doc transformer.
32. Smock, B. et al. (2023). *Table Transformer (TATR) and PubTables-1M.* CVPR 2022/2023. — Table detection + structure.
33. Blecher, L. et al. (2023). *Nougat: Neural Optical Understanding for Academic Documents.* arXiv. — Scientific-PDF OCR.
34. datalab-to (2024–2026). *Marker, Surya, Chandra-ocr-2.* Repo + model cards. — Doc-converter VLM family.
35. OpenDataLab (2024–2026). *MinerU and MinerU 2.5 / 2.5-Pro / Pro.* Repo + model cards. — Layout-aware doc converter.
36. PaddlePaddle (2025–2026). *PaddleOCR-VL 1.5 and 1.6.* Repo + technical report. — Largest open-source production OCR family.
37. Yuliang-Liu et al. (2025–2026). *MonkeyOCR and MonkeyOCR-Pro-3B.* arXiv + repo. — Structure-respecting OCR.
38. Microsoft Research (2025). *Phi-4-multimodal.* Technical report. — Small-but-strong VLM.
39. Allen AI (2024). *Molmo.* Technical report. — Open multimodal with pointer-grounding.
40. Mistral (2024). *Pixtral 12B.* Technical report. — Mistral's first open-weight multimodal.
41. OpenBMB (2024). *MiniCPM-V 2.6 and MiniCPM-o 2.6.* Repo + technical report. — Efficient 8B VLM.
42. Shanghai AI Lab (2024–2025). *InternVL series.* Technical reports. — Leaderboard-top open-weight VLM.
43. DeepSeek (2024–2025). *DeepSeek-VL2 and Janus-Pro 7B.* Repo + technical report. — MoE multimodal.
44. Anthropic (2024–2026). *Claude 3 → Claude 4.x family.* Model cards. — Frontier closed-source.
45. OpenAI (2024–2026). *GPT-4o → GPT-5.x family.* Model cards. — Frontier closed-source.
46. Google (2024–2026). *Gemini 1.5 → Gemini 3 family.* Model cards. — Frontier closed-source.

### §9.4 — Finance-doc applications and IDP

47. Hyperbots (2026). *HyperAPI: parse, parse-intent, classify, extract primitives.* Vendor documentation. — Our team.
48. Rossum (2024–2026). *RossumCloud Document AI.* Vendor whitepapers. — Transactional-doc IDP incumbent.
49. ABBYY (2024–2026). *FineReader Engine and Vantage.* Vendor product documentation. — Enterprise IDP incumbent.
50. Reducto (2025–2026). *Reducto and RolmOCR.* Vendor blog + open-weights release. — Reducto open-weight distill.

### §9.5 — Evaluation rigor and reproducibility

51. NeurIPS Reproducibility Committee (2024). *NeurIPS 2024 paper checklist.* — The 18-item reproducibility checklist; our methodology §8 answers item-by-item.
52. Holm, S. (1979). *A Simple Sequentially Rejective Multiple Test Procedure.* Scandinavian Journal of Statistics. — Holm-Bonferroni multiplicity correction.
53. Efron, B. & Tibshirani, R. J. (1993). *An Introduction to the Bootstrap.* Chapman & Hall. — Bootstrap CI; the basis for paired-bootstrap on doc-strata.
54. Krippendorff, K. (2004). *Content Analysis: An Introduction to Its Methodology.* Sage. — Krippendorff α IAA.
55. Cohen, J. (1960). *A Coefficient of Agreement for Nominal Scales.* Educational and Psychological Measurement. — Cohen κ IAA.

---

## §10 — What we deliberately did NOT include and why

1. **Handwritten-only historical OCR** (Kraken, READ benchmarks beyond reading-order) — out of scope for finance docs; we panel Kraken as a baseline but do not engage the historical-OCR literature.
2. **Scene-text OCR** (ICDAR Robust Reading challenges on scene images, CRAFT, TextSnake) — different task; cross-pollination is limited.
3. **Natural-image OCR / visual question answering on natural images** (VQA, VQAv2) — different task; ChartQA is the doc-AI cross-pollination point.
4. **ASR / speech recognition analogies** — the metric-lineage (CER/WER) crosses over but the architecture and benchmark literature are disjoint.
5. **Math OCR** (im2latex, ChromeBook math-handwriting) — niche; we cite Nougat as the doc-AI cross-pollination point and stop.
6. **Code OCR** (screenshot-to-code, design-to-code) — different downstream goal; Pix2Struct is the cross-pollination point.
7. **Image-to-image document restoration** (DocUNet, super-resolution OCR pre-processing) — relevant to our D-04 dewarp dimension but we cite only DewarpNet and stop short of the broader literature.
8. **Document forgery detection** — adjacent but different problem; out of scope for parse evaluation.
9. **Document summarization beyond extraction** — D-39 BERTScore touches it; we do not engage the broader summarization literature (BART, PEGASUS, T5 fine-tunes).
10. **Vision-language alignment / CLIP-family** — foundational for most VLMs but the alignment literature itself is not where doc-AI specifics live.
11. **Audio OCR / scanned-form audio-readback for accessibility** — out of scope.
12. **Document-image generation / synthesis** — generative side; the synthetic-fill discussion in §5 touches it but the broader generation literature is out of scope.
13. **Diff-privacy and PII redaction** — adjacent; we cite the partner-PII gate but not the diff-privacy literature.

---

*Researcher-not-advocate. Hyperbots Research. 2026-06-15. DRAFT INTERNAL until reviewers' verdict at `hyperapi-cto-org/command-center/REVIEW-VERDICT-LIT-REVIEW-*-2026-06-15.md`.*
