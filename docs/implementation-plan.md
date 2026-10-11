# Implementation plan and feasibility

Date: 12 October 2026. Proposed sequence. Relative weeks assume a four-person student team with regular weekly availability; the actual deadline and effort are not yet known.

## Feasibility verdict

Build the reusable architecture directly, but grow its knowledge and validation in stages. A direct jump to all products and industries is not credible with the current evidence, resources, or prototype status. A complete bounded workflow can be built first without reducing the project's final scope to one industry.

| Goal | Assessment now | Reason |
|---|---|---|
| Shared schema for the six entity types | Feasible early | Requires a clear contract and reviewed examples |
| One conditional forward and backward workflow | Feasible pilot | Small approved model set and manageable reference answers |
| More than one industry domain pack | Feasible after first gate | Needs new evidence, reviewers, and transfer tests |
| Reliable automatic extraction of all engineering knowledge | Not established | Equations, figures, negation, units, and context need review |
| Coverage of every product or industry | Not feasible as an initial deliverable | Knowledge acquisition and validation dominate effort |
| Guaranteed high-rank publication or patent | Cannot be promised | Depends on contribution, evidence, prior art, and external review |

## Proposed 12-week schedule

| Phase | Relative time | Work | Exit evidence |
|---|---|---|---|
| 0: sharpen question | Week 1 | Read closest papers, obtain reviewer access, confirm source permissions and budget | Written novelty comparison and first case approved by guide/team |
| 1: contract | Weeks 2-3 | Implement schema, IDs, units, context, review history; curate first pack | Pack validation, manually checked model bindings, known-answer fixtures |
| 2: full workflow | Weeks 4-5 | Forward execution, blockers, inverse candidate search, forward recheck, export | One complete scenario plus invalid/missing cases replayed correctly |
| 3: inspection UI | Week 6 | Scenario input, path details, source viewing, review records | Teammate can diagnose a failure without reading engine code |
| 4: baselines and freeze | Weeks 7-8 | B0/B1/B2/B5, annotation rubric, separate splits, benchmark freeze | Reproducible baseline run and signed-off evaluation protocol |
| 5: transfer | Weeks 9-10 | Second pack, onboarding logs, held-out evaluation and ablations | Transfer results, including core changes and failures |
| 6: research decision | Weeks 11-12 | Error analysis, reviewer feedback, paper outline, IP disclosure review | Evidence-based publication/IP recommendation and final EDI demonstration |

These durations are estimates. A semester deadline may require fewer scenarios, less UI, or deferring LLM extraction. Reduce breadth before removing evidence checks.

## First ten backlog items

| Item | Acceptance | Depends on |
|---|---|---|
| Define context and configuration IDs | Same-name parts in different revisions stay separate | Phase 0 case selection |
| Implement domain-pack import | Reject dangling references and malformed records | Contract |
| Add evidence and review records | Source locators and immutable decisions retained | Import |
| Add units and approved model registry | Invalid dimensions and source code strings rejected | Parameters/model signatures |
| Curate one complete thermal case | Reviewer checks values, assumptions, and reference outputs | Permitted sources |
| Build forward planner/executor | Only mechanism/model relations update values | Registry and reviewed case |
| Add blocker certificates | Missing input identifies what to obtain next | Forward executor |
| Add bounded inverse workflow | Candidate forward-checks target and hard constraints | Forward executor |
| Build inspection/export interface | User can inspect and replay one run | Run records |
| Freeze benchmark and run baselines | Labels separated from retrieval and development | Review rubric and baseline adapters |

## Fast path

In a compressed deadline, target the shared core, one reviewed domain pack, forward/backward scenarios, refusal behavior, replay, B1/B2/B5, and a small blinded test set. Keep the second-domain pack as a limited transfer attempt. This yields a meaningful EDI prototype; it would provide less support for a general research claim.

Starting with a manually reviewed pack is deliberate. It isolates reasoning errors from extraction errors. Once reasoning is valid, introduce assisted extraction and measure it separately. Do not spend the semester training a GNN on an unvalidated graph.

## Resource plan

Use existing machines and local storage initially. The source PDF proposes INR 4,200, including contingency, as an illustrative ceiling. Treat it as unapproved and exclude publication charges, patent expenses, paid data, expert compensation, new hardware, and student time. Confirm affordability before paid calls.

Log actual API, storage, compute, and review costs. Prefer a zero-paid-service core. A local model has device and runtime costs; it is not automatically cost-free. Separate prototype operating cost from publication/IP costs.

## When to stop or reshape

If experts cannot validate the first case, replace the case rather than fabricating a reference. If inverse suggestions violate constraints, fix forward verification before adding domains. If transfer needs core special cases, revise the abstraction. If closest work already implements the contribution, reposition around a verified difference or honest benchmark study.
