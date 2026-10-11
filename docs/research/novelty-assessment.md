# Novelty assessment

Date: 12 October 2026. Verdict applies to the proposal, not an implemented system.

## Direct verdict

**Proceed as a research project. Do not yet call it a novel invention or a high-rank publication-ready contribution.** The broad combination has substantial prior-work overlap. A publishable result is plausible if the team defines a specific method, builds it, and demonstrates a meaningful advantage. Patent strength is currently unestablished.

No search can guarantee that an idea does not exist. This pass located disconfirming work rather than proving an empty research gap.

## Claims we can and cannot make

| Claim | Current assessment | Evidence or needed work |
|---|---|---|
| Multi-layer engineering representation is new | Not defensible as stated | Layered semantic and engineering models already exist; see R03, R06, R09. |
| Forward engineering change propagation is new | Not defensible | R05 predates this project. |
| Backward requirements-driven impact analysis is new | Not established | R07 is a close comparator. |
| Equations, validity regimes, and evidence in a KG are new | Not defensible as ingredients | R09 and R11 cover important pieces. |
| The proposed context-composition and refusal method is distinct | Candidate hypothesis | Needs algorithm specification, closest-work comparison, and implementation. |
| One engine can transfer between industry packs | Design ambition | Requires actual onboarding and held-out transfer evaluation. |
| System outputs are patentable innovations | Unsupported | Each output needs independent technical validation and a separate novelty search. |
| The engine itself is patentable | Unresolved | Needs concrete inventive method, claim analysis, technical effect, and jurisdiction review. |

References: [literature and direct sources](literature-review.md).

## Recommended contribution to investigate

Working research title: **Context-Checked Engineering Impact Propagation with Evidence-Grounded Backward Intervention Search**.

The method would check compatible conditions across linked model applications, retain incomplete branches as structured blockers, and re-evaluate inverse candidates forward under product constraints. The system would export a reproducible certificate identifying sources, inputs, model versions, conditions, and failure reasons. This certificate is a useful interface artifact, not an asserted formal proof or a novelty claim by itself.

The research target is whether these mechanisms jointly improve valid impact-path precision, refusal correctness, and reviewer usefulness at comparable answer coverage. A gain caused solely by better manual annotations is a curation gain; measure it separately from the reasoning algorithm.

The concrete method under investigation is configuration-consistent condition composition over multi-input model applications, with alternative missing-input sets and bounded inverse candidates. Its contract is detailed in the reasoning specification. This is a more precise target for prior-work comparison than a general claim about six layers. It remains a hypothesis about a useful contribution, not a declaration that the algorithm is unprecedented.

## Testable hypotheses

| ID | Hypothesis | Falsifying observation |
|---|---|---|
| H1 | Applicability checks reduce invalid supported paths | No advantage over equally informed typed-graph or engineering-solver baselines |
| H2 | Explicit blockers improve handling of incomplete cases | The engine hides errors by refusing most answerable scenarios |
| H3 | Forward verification improves backward candidate feasibility | Equally bounded inverse solver matches or exceeds it with less effort |
| H4 | Domain packs permit meaningful engine reuse | Second pack requires substantial core-specific logic or fails basic cases |
| H5 | Evidence inspection helps reviewers find failure points | Blinded reviewers gain no accuracy or time benefit at comparable information |

All hypotheses are prospective. Do not write a results section using expected benefits.

## Avoid novelty traps

Counting six layers is not a technical contribution. Using an LLM or graph database is not sufficient. Predicting absent edges is not proof of scientific causation. A historical chain demonstrates representation, not future forecasting. Readable explanations can still be incorrect. A system with perfect precision from answering almost nothing is not useful.

## Decision gates

1. Compare the written algorithm with the closest primary work, especially R07 and R09. If equivalent, revise the claim before building a large system.
2. Build a manually reviewed complete scenario and meaningful failure cases. If model binding is unreliable, fix the representation first.
3. Run matched baselines and ablations. If the new method has no clear advantage, report that outcome and consider a benchmark or engineering-tool contribution.
4. Seek domain-expert review of both accepted and rejected paths. Team agreement alone is not external validation.
5. After evidence exists, choose paper and IP routes. Neither publication nor filing should be promised beforehand.
