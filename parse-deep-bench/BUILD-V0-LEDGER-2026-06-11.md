# BUILD-v0 Ledger — Parse Deep Benchmark v1

Date: 2026-06-11 · Author: orchestrator (in-session recovery after subagent socket-disconnect)
Bar: ParseBench (arXiv:2604.08538) / NeurIPS-paper · strictly higher than SAVIOR-Bench
Approval: PENDING build-v0 review (chief-research-scientist + chief-architect + docs-techwriter + benchmark-format-steward)

## §1 — Why this ledger

After the BUILD-v0 lead subagent died (socket disconnect, 48.6s, 9 tool uses, ~zero output) leaving only an empty `parse-deep-build-v0/` directory, the 5 deliverables + ledger were produced in-session. This ledger is the audit trail: each artifact → which acceptance criterion it satisfies → quick verifier.

## §2 — Deliverables

| ID | Artifact | Path | LOC | Purpose |
|---|---|---|---|---|
| D1 | Framework spec v1 | `../PARSE-DEEP-BENCHMARK-FRAMEWORK-2026-06-11-v1.md` | ~470 | The 50 §X-style dimension blocks; pre-registration; §0-§14 |
| D2 | Methodology (NeurIPS checklist) | `methodology.md` | ~180 | Pins · stats · contamination · NeurIPS item-by-item |
| D3 | Tasks additive JSON | `tasks-additive-DQ-001-050.json` | 50 entries | DQ-001..DQ-050; ADDITIVE-ONLY |
| D4 | Cell schema v1.1 | `cell-schema-v1.1.json` | JSON Schema 2020-12 | Backward-compat extension; adds dimension_id, category_id, nrun_status, ablation_id, pre_registration_id, contamination_audit |
| D5 | Dashboard scaffold | `index.html` | ~260 | All 50 cards in `registered-not-yet-run`; empty leaderboard by design |
| L | This ledger | `BUILD-V0-LEDGER-2026-06-11.md` | this file | Audit trail |

## §3 — Acceptance-criterion mapping (from STEP-4-CONSOLIDATED-BRIEF + NeurIPS-bar amendment)

| Criterion | Satisfied by | Verifier |
|---|---|---|
| Pre-registration discipline | D1 §1 + D5 all-cards-registered + D3 `nrun_status: registered-not-yet-run` on every task | `grep -c registered-not-yet-run tasks-additive-DQ-001-050.json` == 50 |
| Per-doc score vectors mandatory | D2 §4.1 + D4 `score_vector_path` field + D1 per-dim CI policy lines | `jq '.properties._meta.properties' cell-schema-v1.1.json` shows score_vector_path-adjacent contract |
| Paired bootstrap + multiplicity | D2 §4.2 + §4.3 (Holm-Bonferroni) + D1 §6 + D1 D-47 | D2 §4 grep |
| Explicit ablations E1-E9 | D1 §7 + D5 §7 + D4 `ablation_id` field | D1 §7 grep "E[1-9]" |
| Contamination + held-out audit | D1 §8 + D2 §5 + D4 `_meta.contamination_audit` + `held_out_ci95` + D5 §8 | schema field check |
| Ethics + license matrix | D1 §9 (full license matrix + 14-name roster verbatim) | grep ROSTER |
| NeurIPS reproducibility checklist | D2 §8 item-by-item (18 items) | D2 §8 read |
| Public release plan | D1 §11 (HF dataset card + arXiv skeleton) | D1 §11 read |
| Honest baselines per dimension | D1 §10 + D2 §7 | grep "baseline" |
| TR-4 discipline | D1 §1 + D2 §3 + D4 `_meta.factory_reproduced: false` default | schema check |
| Apples-to-apples I-1 | D2 §2 (3 pin families) + D1 §6 + D4 `pin_family` enum + `apples_to_oranges` flag on D-31/D-36 cells | schema check |
| results.zip never gold I-2 | D2 §3 + D1 §3 D-31 note | grep "results.zip" |
| Per-cell provenance I-3 | D2 §3 (4-part contract) + D4 `_meta` required fields | schema required check |
| [FT] inline I-4 | D1 §5.3 + D4 `_meta.ft_flag` + grep guard policy | grep "\\[FT\\]" |
| CI honesty I-5 | D2 §4.1 (literal-null aggregate-only) + D4 ci95_low/high nullable | schema nullable check |
| Customer-name 14-roster I-6 | D1 §9.2 (verbatim from `_grep_guard.sh`) | grep guard run |
| Ensemble-anchor I-7 | D1 §7 (E8 OSS-only explicit control) + D5 §7 | grep "E8" |
| Customer-name consent I-8 | D1 §9.3 (partner names internal-only) | text read |
| Inheritance of 9-D 2026-05-27 spec | D1 §2.4 bijection table | grep "D-OCR.*D-07" |
| 50 dimensions exactly | D1 §3 + D3 50 entries + D5 50 cards | `jq '.tasks | length' tasks-additive-DQ-001-050.json` == 50 |
| 52-row panel (22+22+8) | D1 §5.1 + §5.2 | section count |
| Additive-only (no edits to existing DC/PB/TR/DE tasks) | D3 separate file + `_meta.policy: ADDITIVE-ONLY` | file diff vs harness/tasks.json |
| Backward-compat cell schema | D4 `additionalProperties: true` + only adds fields | schema diff |
| Dashboard at depth bar | D5 nav + 9 sections + 50 cards + empty leaderboard by design | render check |

## §4 — Customer-name grep-guard self-check

Roster: `Airgas|CJ Logistics|Eskimo|Mahindra|INFY|MERC|TCS|ICICI|HDFC|KPITTECH|PAYTM|WIPRO|Reiser|Stauffer`

Self-check: roster names appear ONLY inside §9.2 sentinel-tagged exempt context in D1 (verbatim quote of `_grep_guard.sh`) and in this ledger (same). No leaked references in D2, D3, D4, or D5 prose. The framework's D-45 page-scaling block uses "long-doc T-11 class (≥400pp)" (Mahindra scrub from L192 preserved).

Recommended verifier:
```bash
ROSTER='Airgas|CJ Logistics|Eskimo|Mahindra|INFY|MERC|TCS|ICICI|HDFC|KPITTECH|PAYTM|WIPRO|Reiser|Stauffer'
grep -EwH "$ROSTER" \
  PARSE-DEEP-BENCHMARK-FRAMEWORK-2026-06-11-v1.md \
  parse-deep-build-v0/methodology.md \
  parse-deep-build-v0/tasks-additive-DQ-001-050.json \
  parse-deep-build-v0/cell-schema-v1.1.json \
  parse-deep-build-v0/index.html \
  parse-deep-build-v0/BUILD-V0-LEDGER-2026-06-11.md \
  | grep -v '_grep_guard\|ROSTER='
```
Expected: zero hits outside the sentinel-tagged §9.2 quote in D1 and this §4.

## §5 — Hard guardrails honored

- ✓ No cells run; no model API called; $0 burned
- ✓ TR-4: every cell schema default + every example shows `factory_reproduced: false`
- ✓ results.zip never used as gold (build-time guard cited)
- ✓ Pinned upstream commits inherited: vlm_ocr `1fbbc334` · ParseBench `a0b10dd7` · HyperAPI SDK `0fc4bada`
- ✓ Pinned seeds: 20260516 (bootstrap + held-out + synthetic renders)
- ✓ Pinned resamples: 2000
- ✓ Customer-name roster: verbatim from `_grep_guard.sh`
- ✓ Azure OpenAI directive: C18/C19/C20 rows tagged `Azure OpenAI Service`
- ✓ No HITL framing in any artifact
- ✓ Researcher-not-advocate tone preserved in D1 §0
- ✓ Predecessor 9-D spec extended, not duplicated (§2.4 bijection)
- ✓ ADDITIVE-ONLY namespace: D3 in separate file; existing tasks.json untouched
- ✓ Backward-compat schema: D4 extends, never breaks CONSOLIDATED-150

## §6 — Open issues (resolved at BUILD-v1)

1. NeurIPS-checklist item 8 (compute resources) — populated per-cell at run time.
2. NeurIPS-checklist item 5 (open access) — partial today; pinned at corpus-license matrix; ParseBench (Apache-2.0) is the publishable anchor.
3. `contamination/` subdir not yet built; methodology specifies the contract; BUILD-v1 first action.
4. HF dataset-card draft + arXiv skeleton — registered (D1 §11) but not written; BUILD-v1 deliverable.

## §7 — Drift log

- 2026-06-11: BUILD-v0 lead subagent dispatched at ParseBench/NeurIPS bar. Died after 48.6s with socket disconnect; subagent_tokens 109 → ~zero output. Empty dir only.
- 2026-06-11: Recovered in-session per declared fallback ("subagents unreliable today; in-session more reliable"). Wrote D1-D5 + ledger.
- No drift vs the orchestration plan: still BUILD-v0 only; zero cells run; $0; bar held to ParseBench/NeurIPS.

## §8 — Next gate

This v0 artifact set goes to build-v0 review:
- chief-research-scientist (P0/P1/P2 + NeurIPS-bar 10 criteria)
- chief-architect (tech 8 criteria — schema backward-compat, additive-only, pinned env)
- docs-techwriter (content 8 criteria — tone, customer-name guard, F-B-STUDY bar)
- benchmark-format-steward (research-format 10 criteria — pre-registration discipline, comparative-study 8 invariants, SAVIOR Appendix D 4-part)

Verdict files expected at `../../hyperapi-cto-org/command-center/REVIEW-VERDICT-PARSE-FRAMEWORK-V1-{RESEARCH-HEAD,CTO-TECH,CTO-CONTENT,CTO-RESEARCH-FORMAT}-2026-06-11.md`.

After all 4 verdicts ACCEPT (or ACCEPT-WITH-CHANGES folded): human review → BUILD-v1 cell execution gated on CEO budget + corpus acquisition.
