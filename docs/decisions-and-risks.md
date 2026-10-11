# Decisions, risks, and unresolved questions

Date: 12 October 2026. Recommendations are provisional until reviewed.

## Decision record

| ID | Decision | Rationale | Revisit trigger |
|---|---|---|---|
| D01 | Preserve the six engineering entity types | Matches the supplied synopsis | Evidence that a domain cannot be modeled without changing the taxonomy |
| D02 | Use domain packs with a shared engine | Keeps the cross-industry ambition while bounding data | Second pack requires core-specific logic |
| D03 | Begin with manually reviewed knowledge | Isolates reasoning from extraction errors | Core reasoning is validated and extraction burden becomes limiting |
| D04 | Use model applications with explicit parameter bindings | Equations usually require multiple simultaneous inputs | A richer model signature is needed for coupled behavior |
| D05 | Separate review, applicability, and result states | Avoids calling a reviewed edge universally valid | Review workflow exposes additional distinctions |
| D06 | Local SQLite plus graph view first | Limits operational burden for a student prototype | Profiling shows traversal/concurrency limits |
| D07 | Private repository at creation | Retains patent-route options and contains team planning | Team/institution intentionally approve disclosure |
| D08 | Keep raw contact-bearing source local | Personal registration data is unrelated to shared research | A justified controlled institutional archival requirement |
| D09 | Test refusals and answer coverage together | Refusing everything must not count as good reasoning | Evaluation rubric revision |
| D10 | Treat novelty as a hypothesis | Adjacent prior work overlaps core ingredients | A verified specific implemented difference emerges |

## Risk register

| Risk | Likelihood / effect judgment | Mitigation | Early indicator |
|---|---|---|---|
| Contribution already covered by close work | High / high | Read R07/R09 against actual algorithm before broad implementation | Same condition/inverse behavior already described |
| Incorrect extracted equation or unit | High / high | Human review, exact locators, unit and model tests | OCR mismatch or unexplained numerical error |
| Unusable evidence corpus | Medium / high | Source permissions and known-answer cases before app expansion | Missing model inputs across most pilot cases |
| Domain overclaim | High / high | Report pack coverage and transfer effort | “Works for any industry” with one demonstration |
| Weak ground truth | Medium / high | Independent annotation and expert adjudication | Labels reflect the engine's own answers |
| Benchmark leakage | Medium / high | Split source/scenario families and isolate labels | Near-duplicate test questions or solution text in retrieval |
| Confident unsupported output | High / high | Blockers, context gates, false-support metric | Supported output despite missing inputs |
| Student workload underestimated | Medium / high | Complete a narrow workflow first, relative schedule, reduce UI breadth | No full scenario by the planned mid-point |
| Public disclosure before IP review | Medium / high | Private repo and disclosure record | Public demo or preprint before route decision |
| Cost outside prototype ceiling | Medium / medium | Local core and measured paid-call budget | Paid models or publication fees assumed affordable |

Risk levels are planning judgments, not measured probabilities.

## Open decisions

- Semester submission date and guide's minimum implementation expectations.
- Weekly team capacity and workstream ownership.
- First-domain evidence permissions and qualified reviewers.
- Whether LED thermal management is acceptable as the initial test case.
- Whether second-domain conduction provides sufficient transfer evidence or a mechanical pack is needed.
- Institutional IP ownership, previous public disclosures, and paper/patent priority.
- Affordable model, hosting, publication, and IP budgets as separate categories.
- Criteria for moving beyond a pilot and target venue after results.
