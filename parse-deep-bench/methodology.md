# Methodology — Parse Deep Benchmark v1 (BUILD-v0)

Version: v1 · 2026-06-11 · companion to `../PARSE-DEEP-BENCHMARK-FRAMEWORK-2026-06-11-v1.md`
Bar: NeurIPS reproducibility-checklist (paper-track) · strictly higher than SAVIOR-Bench

## §1 — Scope

Methodology for the 50-dimension parse benchmark framework. This document is the per-claim reproducibility contract: pins, seeds, statistical procedure, contamination protocol, license posture, and the NeurIPS-reproducibility-checklist item-by-item answer. No cells run in v0; BUILD-v1 cell execution inherits this contract verbatim.

## §2 — Decoding pins (3 families)

| Family | Used by dimensions | T | top_p | max_tokens | seed |
|---|---|---|---|---|---|
| parse-deep | D-01..D-30, D-32..D-50 (excluding D-31, D-36) | 0.1 | 0.9 | 2048 | 20260516 |
| TR-000 (host: D-31 GTRM) | D-31 only | 0.0 | 1.0 | 4096 | 20260516 |
| extract (host: D-36 lift) | D-36 only | 0.0 | 1.0 | 4096 | 20260516 |

Cross-family cells (D-31, D-36) are tagged `apples-to-oranges: true` per comparative-study I-1; they ship with the pin family named in the cell's `_meta.pin_family` field.

## §3 — Per-cell provenance contract (SAVIOR Appendix D 4-part)

Every published cell carries the verbatim 4-part contract:
- `provenance`: free-text + URL/path to the source-of-truth artifact (data card · model card · vendor-attested table)
- `pins`: `{ model_version, sdk_commit, harness_commit, prompt_id, pin_family, env_hash }`
- `rerun_command`: a single shell line that reproduces the cell when run from the repo root with the env in §6
- `factory_reproduced`: `false` at adapter emit time (TR-4 discipline); `true` only after `harness/repro_check.py --cell <path>` returns exit 0

`results.zip` is **never** ground truth (comparative-study I-2); a build-time grep guard forbids `results.zip`-derived gold cells.

## §4 — Statistical procedure

### §4.1 — Bootstrap
- Method: nonparametric bootstrap on per-doc score vector
- Resamples: 2000
- Seed: 20260516
- Interval: 95% percentile (low = 2.5th, high = 97.5th)
- Aggregate-only cells (no per-doc vector) → `ci95_low: null, ci95_high: null, n: <literal>` (never inferred per SAVIOR R3)

### §4.2 — Paired bootstrap (D-36 + paired comparisons)
- Stratification on `doc_id`; same resamples + seed
- Used for any "A vs B same doc" claim — primarily D-36 lift, also model-vs-baseline on the same panel

### §4.3 — Multiplicity correction
- Headline cross-dimension claims ("wins on N of 50") → Holm-Bonferroni
- Family-wise α = 0.05; per-dimension target α ≈ 0.05/50 ≈ 0.001
- Cells in their own dimension report uncorrected p; cross-dimension headline tables apply correction

### §4.4 — IAA (gold corpus quality)
- Method: Cohen κ (binary), Krippendorff α (ordinal / nominal)
- Reported per net-new gold corpus the framework curates (D-48 dimension)
- Double-annotation subset: 187 pairs (SAVIOR-Bench convention; extends to net-new corpora)
- SAVIOR baseline IAA 0.761 inherited but NOT silently extended to new corpora

## §5 — Contamination + held-out audit

### §5.1 — Per-FT-row protocol
Every row with `[FT]` in the Model name (today: O12 Qwen 3.6-35B-A3B `[FT]`, O13 Qwen 2.5-VL-7B `[FT]`, O14 Qwen 2.5-VL-3B `[FT]`, hyperapi-parse-intent) triggers:

1. `harness/contamination_check.py --model <m> --train savior-train --test <test-corpus>` for every test corpus the cell scores against
2. Output written to `contamination/<model>__<test>.json` with fields: `overlap_doc_count`, `overlap_pct`, `mitigation`, `audited_at`
3. Cell's `_meta.contamination_audit` field cites the contamination report path
4. Unresolved overlap (`mitigation = unresolved`) → cell stays `factory_reproduced: false` and renders red

### §5.2 — Held-out splits
Every test corpus declares a 10% random held-out subset, seed=20260516. Cells reported on the full corpus pair with held-out CIs in the cell's `_meta.held_out_ci95` block.

### §5.3 — Audit subdir
`contamination/` factory subdir. Each (train, test) pair gets one JSON. Auditable from CI by re-running `contamination_check.py` against pinned corpora.

## §6 — Environment + version pins

- Python: `>=3.11,<3.13`
- Package manager: `uv` (lockfile-pinned)
- Key pins (verbatim from `pyproject.toml`):
  - `vlm_ocr`: commit `1fbbc334824d0a0d4fb9c3afdcb9e514d963e093` (PaIRS + WordRecall vendoring source)
  - ParseBench upstream: commit `a0b10dd75b70d4917b6cc946de7f03129888ff46`
  - HyperAPI SDK: commit `0fc4bada0cf8a190df95d53cf7d56e24b5c13f5e`
- `env_hash`: `sha256(pyproject.toml + uv.lock + harness/_pin_manifest.json)` — recomputed per cell, written to `_meta.env_hash`
- All seeds for bootstrap / held-out splits / synthetic image renders: 20260516

## §7 — Honest baselines per dimension

Inherits §10 of the framework spec verbatim. Baseline names are pre-registered (not chosen post-hoc to make the FT row look better):
- text dimensions: best-zero-shot OCR + Tesseract floor
- layout: best zero-shot layout-emitter (today: Chandra)
- table: best zero-shot table-emitter + PubTabNet-trained control
- KIE: FUNSD-trained model + best zero-shot KIE-prompt model
- parse-intent / NLP: best documented zero-shot = GPT-4o (SAVIOR §5.1.1 modesty anchor)
- downstream lift: no-parse direct-extract baseline = pinned Qwen-3.6 image→extract
- cost / latency: cheapest baseline + production-grade-floor

## §8 — NeurIPS 2024 paper-checklist item-by-item

| # | Item | Status | Where |
|---|---|---|---|
| 1 | Claims scope matches paper | ✓ | Framework §0 + §1 |
| 2 | Limitations | ✓ | Framework §12 |
| 3 | Theoretical assumptions / proofs | n/a | empirical framework |
| 4 | Reproducibility of results | ✓ | this doc §6 + §4 + per-cell `rerun_command` |
| 5 | Open access to data + code | ◐ | partial: ParseBench Apache-2.0 (open); SAVIOR / partner gated (per §9.1 framework license matrix) |
| 6 | Experimental setting / details | ✓ | this doc §2 (pins) + §4 (stats) |
| 7 | Error bars / statistical significance | ✓ | this doc §4 |
| 8 | Compute resources | ◐ | per-cell `_meta.compute` block to be populated at BUILD-v1 (model + GPU + wall-clock) |
| 9 | Code-of-conduct compliance | ✓ | NeurIPS CoC adhered; researcher-not-advocate framing |
| 10 | Broader impacts | ✓ | Framework §9 + §12 |
| 11 | Safeguards | ✓ | Customer-name grep guard (§9.2); PII gate (§9.3); contamination audit (§5) |
| 12 | License + terms of use respected | ✓ | Framework §9.1 license matrix |
| 13 | Assets attribution | ✓ | Framework §13 sources; per-cell `provenance` |
| 14 | Documentation for assets | ✓ | this doc + framework spec + HF dataset card (§11.1 framework) |
| 15 | Human subjects | n/a (synthetic / public + consented partner corpora) | §5.3 framework |
| 16 | IRB / institutional review | n/a | per-partner consent gate |
| 17 | Risks to participants | n/a (no live human subjects) | — |
| 18 | LLMs used as part of methodology | ✓ disclosed | the 52-row panel IS the methodology subject; no editorial-LLM use beyond panel members |

Items marked ◐ are tracked open issues in `BUILD-V0-LEDGER-2026-06-11.md`; resolved at BUILD-v1.

## §9 — Comparative-study 8 invariants — per-claim enforcement

- I-1 apples-to-apples: same pin family per dimension; cross-family cells (D-31, D-36) tagged `apples-to-oranges: true` machine-readably
- I-2 results.zip never gold: build-time grep guard
- I-3 per-cell provenance: §3 above (4-part contract)
- I-4 FT inline + abstract-first: `[FT]` mandatory in Model name; FT? column in panel; modesty-anchor baseline named per dimension
- I-5 CI honesty: §4 above; never-inferred `n`; literal `null` on aggregate-only
- I-6 named-competitor scope per-surface: customer-name 14-roster (framework §9.2) word-boundary-grep-guarded; SAVIOR §1 naming-exception 4-surface ✓/✗ matrix cited at framework §7
- I-7 ensemble-anchor: ship-claim ensembles include HyperAPI parse; E8 OSS-only is the explicit control
- I-8 customer-name consent: partner names internal-only without externalization consent (per `[[hyperapi-fde-agent-ga-and-partners]]`)

## §10 — Drift policy + amendment procedure

Drift policy: stop-and-ask. Adding a 51st dimension after v1 publishes requires a v1.1 amendment with its own pre-registration. Removing a dimension requires written rationale + chief-research-scientist sign-off. Renumbering forbidden after v1 ships.

Amendment file: `methodology-amendment-v1.X-<date>.md` adjacent to this file; references this doc by section number.

## §11 — Approval

PENDING build-v0 review (chief-research-scientist + chief-architect + docs-techwriter + benchmark-format-steward). NOT self-approved.
