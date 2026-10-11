# Team guide

Date: 12 October 2026. This is a proposed allocation of work, not an assignment to named people.

## First meeting

Read the project brief together. Confirm the first case, reviewer, deadline, available effort, budget, IP ownership route, and who owns each workstream. The goal is that everyone can explain both what the system does and when it should refuse to answer.

## Workstreams

| Workstream | Deliverable | Paired reviewer |
|---|---|---|
| Knowledge and domain curation | Source registry, reviewed claims, first and second packs | Reasoning owner plus engineering reviewer |
| Shared engine | Model execution, applicability, forward/backward workflows, certificates | Evaluation owner |
| Interface and integration | Scenario entry, evidence/path inspection, review screen, export | Curation owner |
| Evaluation and research | Frozen cases, baselines, metrics, literature/IP updates, report | Engine owner plus guide |

Every member should understand the end-to-end scenario. Avoid one person owning all scientific correctness while others only build screens.

## Working agreement

Use GitHub branches with a scoped change and review. A schema change requires agreement from engine, curation, and evaluation workstreams because it affects their contracts. Review mechanisms against sources, and review code against acceptance cases. Keep issues small enough to finish and inspect.

At the weekly meeting, demonstrate one actual behavior, one failure, and the next dependency. Record what was implemented, what was checked, and what remains proposed. A screenshot is not evidence that the calculation is correct.

## Evidence collection checklist

For each source record, save the citation, accessible locator, reuse conditions, relevant context, model or relation claim, and reviewer decision. Separate primary measurements from repeated summaries. Do not upload paywalled or proprietary full texts merely because someone can access them.

For figures and tables, preserve the figure/table ID and units. If an equation is recovered with OCR, compare it with the original before approval. If a diagram lacks a labeled relation, do not invent one to complete a path.

## Definition of an implementation-ready task

A task states the user behavior, input/output contract, evidence needed, failure conditions, and acceptance cases. Example: add forward execution for a reviewed conduction model, including wrong units and missing conductivity. “Build AI reasoning” is too vague to assign.

## Review and authorship

Discuss authorship based on actual contribution and venue rules with the guide. Registration membership does not by itself establish inventorship. Review the institution's student-project IP policy before filing or public disclosure. Record decisions without including private contact information in the repository.
