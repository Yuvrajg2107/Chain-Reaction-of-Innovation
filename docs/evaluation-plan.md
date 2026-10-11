# Evaluation protocol

Date: 12 October 2026. Prospective protocol; all counts and thresholds below are planning targets, not collected data or achieved results.

## What the experiment must establish

Separate representation quality, reasoning correctness, incomplete-evidence behavior, inverse feasibility, domain transfer, and reviewer usefulness. A favorable demonstration does not establish all of them.

## Dataset plan

Start with 12 development scenarios to debug the contract and rubric. After revision, freeze a proposed 60-scenario benchmark: 20 development, 10 validation, and 30 test cases. Spread test cases across the first and second packs. If time cannot support that size, reduce it openly and describe the study as a pilot.

Include valid forward chains, adverse or mixed effects, missing parameters, wrong units, out-of-range conditions, contradictory evidence, configuration mismatches, inverse feasible and infeasible targets, shared dependencies, and unsupported cycles. These categories can overlap; annotate each case rather than assigning it to exactly one bucket.

Maintain a separate historical blue-LED reconstruction case. It is a representation demonstration unless sources and model knowledge are restricted to a genuine pre-discovery cutoff. An LLM with later knowledge invalidates a historical prediction claim.

## Annotation and reference answers

Two reviewers independently label mechanism steps, applicable conditions, numerical answers/tolerances, result state, candidate feasibility, and required evidence. At least one reviewer needs relevant engineering expertise; recruit the guide or another qualified reviewer rather than claiming team consensus is expert validation. A third review/adjudication process resolves disagreements.

Label alternative valid paths and genuinely unknown cases. The reference set must include forbidden paths and appropriate abstentions, not only positive examples. Keep label origin and adjudication history. Report agreement and unresolved annotation disputes.

Split by source family, product configuration, and scenario family, not random near-duplicate rows. Keep answers and evaluation labels out of retrieval indexes. Models, equations, and allowed evidence may be shared consistently when the task is reasoning over known engineering knowledge, but reference solutions and answer text may not leak.

## Matched baselines

| ID | Method | Why it is necessary |
|---|---|---|
| B0 | Document retrieval with evidence snippets and structured answer extraction | Tests whether structured reasoning adds value over source finding |
| B1 | Plain graph traversal | Measures errors from connectivity without mechanisms |
| B2 | Typed engineering graph with fixed qualitative rules | Controls for good ontology and manual curation |
| B3 | Text RAG with a common LLM and fixed prompts | Tests retrieval-assisted explanation under the same evidence budget |
| B4 | Graph RAG with the same LLM | Separates graph retrieval from model execution |
| B5 | Expert-authored equations/constraint solver with the same inputs | Strong control: correct engineering arithmetic may explain the benefit |
| B6 | Patent similarity/link prediction, if a suitable patent opportunity set exists | Matches the synopsis's TOD comparison without pretending its task equals numerical reasoning |

Implement B0, B1, B2, and B5 before paid LLM comparisons. B3/B4 need reproducible service settings and a funded budget. B6 is a separate opportunity-retrieval task; do not score it unfairly on quantities it was never designed to compute.

Use the same frozen scenario inputs, corpus access, applicable source versions, and answer format. For different retrieval methods, report evidence retrieved and any indexing advantage. Record latency, hardware, manual preparation effort, and actual service costs.

## Metrics with denominators

| Metric | Definition | Guard against |
|---|---|---|
| Supported-path precision | Valid fully supported returned paths / all paths labeled supported by system | Counting one valid edge as a valid entire chain |
| Reference-path recall | Returned valid reference paths / annotated valid reference paths | Claiming exhaustive recall when alternatives are unknown |
| Full-chain correctness | Cases with every required step and result correct / cases with defined reference solutions | Ignoring wrong intermediate steps |
| Numerical error | Absolute and relative error against reference with quantity-specific tolerances | Comparing incompatible units or dividing by near-zero reference |
| Refusal correctness | Appropriate blocked/unresolved states / cases that require them | Refusing everything to maximize precision |
| False support rate | Supported answers on invalid or insufficient cases / all such cases | Hiding harmful conclusions in average scores |
| Answerable-case coverage | Answerable cases receiving correct supported output / all answerable cases | Treating abstention as a success on solvable cases |
| Backward feasibility precision | Forward-verified constraint-satisfying candidates / candidates labeled feasible | Mistaking graph reachability for a solution |
| Evidence completeness | Supported steps with required locators/context / all supported steps | Counting citations that do not support the actual claim |
| Domain onboarding effort | Logged person-hours, added model records, core changes, and review work per pack | Calling a rewritten engine portable |

Precision@K and Recall@K apply to a reviewed candidate set with known relevant options. Where relevance is incomplete, use judged precision and disclose that recall is undefined. Do not assign unknown options a false negative label automatically.

## Ablations

Remove context checks, model execution, contradiction handling, provenance display, or inverse forward-verification one at a time. Keep scenario inputs and curation fixed. Measure the effect and disclose whether removal changes the task. Provenance-display ablation belongs primarily in reviewer evaluation, not arithmetic correctness.

Add cases where individually plausible model steps have incompatible shared parameter bounds or configurations. Compare joint condition composition against ordinary per-model checks. For missing-evidence cases, independently annotate acceptable blocker sets and test whether the proposed AND/OR blocker propagation returns useful alternatives without claiming completeness beyond the represented graph.

## Analysis

Report per-domain and per-case-category results, denominators, effect sizes, and uncertainty intervals. Use paired comparisons on the same scenarios. Cluster uncertainty estimates by independent scenario/source family; avoid treating multiple variants of one case as independent evidence. Predeclare the primary metric as false support rate with answerable-case coverage reported alongside it. Small studies may support feasibility without strong significance claims.

## Reviewer study

Present outputs in randomized order with system identity hidden where practical. Ask reviewers to identify a wrong or missing step, judge feasibility, and record time and usefulness. Obtain consent, keep identifying details private, and report participant expertise. A convenient small group provides usability evidence, not broad industrial validation.

## Release gates

Require all deliberately invalid unit, missing-input, and out-of-range regression cases to refuse unsupported execution. Require replay of the initial accepted scenario within its declared tolerance. These are correctness gates, not publication thresholds. A paper decision requires comparison quality, credible annotation, and a clear effect beyond existing methods; no fixed score guarantees acceptance.
