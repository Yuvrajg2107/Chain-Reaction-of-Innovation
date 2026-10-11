# Product requirements document

Version 0.1, 12 October 2026. Proposed requirements for team review. Application status: not implemented.

## Product purpose

Give engineers a traceable account of how a specified change might affect a configured product, and help identify bounded changes that could address a requirement. Support different industries through domain packs rather than hardcoded workflows.

The initial product is a research prototype for mechanism reasoning. The final ambition is an extensible engineering-analysis framework. It will not claim exhaustive knowledge or dependable predictions for unmodeled industries.

## User journeys

### Forward analysis

Select an installed domain pack and product configuration. Specify a parameter change and operating conditions. The system validates the input, identifies applicable mechanism paths, requests missing values, computes eligible models, and presents impacts with evidence and limits. The user inspects an impact and exports a reproducible run record.

### Backward investigation

Select a product requirement, target value, allowed interventions, and hard constraints. The system identifies upstream parameters and candidate interventions. It evaluates candidates through the forward model and returns feasible conditional options, unresolved options requiring evidence, and reasons for exclusion. The user decides which option deserves engineering investigation.

### Evidence review

A curator proposes a relation or model from a permitted source. A reviewer inspects the exact source location, context, parameter interpretation, and model assumptions. Approval creates a versioned record. Conflicting claims remain separate until adjudicated in a matching context.

### Domain onboarding

A contributor supplies entities, relationships, units, models, evidence, constraints, and known-answer cases. Validation rejects malformed references and incomplete model bindings. The new pack runs through the shared engine and regression suite before being considered supported.

## Functional requirements and acceptance

| ID | Priority | Requirement | Acceptance evidence |
|---|---|---|---|
| FR-01 | P0 | Retain the six engineering entity types | A domain pack can represent every type without forcing a linear path. |
| FR-02 | P0 | Store product configuration and typed parameter bindings | A model cannot borrow a value from a different product revision silently. |
| FR-03 | P0 | Attach provenance to mechanism claims | Every accepted mechanism shows source ID, locator, review state, and applicability conditions. |
| FR-04 | P0 | Distinguish structure, association, qualitative influence, and executable dependence | `part_of` and `similar_to` edges never authorize a numerical update. |
| FR-05 | P0 | Check inputs, units, bounds, and assumptions before calculation | Deliberate missing-input, wrong-unit, and out-of-range cases return the specified refusal states. |
| FR-06 | P0 | Propagate applicable changes across multiple model applications | A known-answer case reproduces intermediate and final values within model-specific tolerances. |
| FR-07 | P0 | Investigate a requirement backward | At least one bounded inverse case is solved and forward-checked; an infeasible target is rejected. |
| FR-08 | P0 | Preserve uncertainty, conflict, and missing knowledge | Missing inputs cannot produce a supported value; incompatible same-context evidence cannot be silently averaged. |
| FR-09 | P0 | Show path explanations and unresolved steps | Results identify the first blocker, affected output, required information, and source locations. |
| FR-10 | P0 | Export reproducible runs | A stored run identifies input, pack, model, source, and engine versions and can be replayed. |
| FR-11 | P0 | Load domain packs independently of the shared engine | Adding the second evaluation pack does not require domain-specific branches in core code. |
| FR-12 | P0 | Bound computation | Hop, candidate, time, and solver limits are logged; truncation is explicit. |
| FR-13 | P1 | Assist extraction from PDFs and documents | Draft extractions retain spans and enter a review queue. They cannot auto-approve themselves. |
| FR-14 | P1 | Rank candidate changes | Hard violations are filtered first; remaining tradeoffs and unknown values remain visible. |
| FR-15 | P1 | Compare baselines on a frozen benchmark | The same scenario inputs and evidence budget apply across methods. |
| FR-16 | P2 | Assist literature and opportunity exploration | Retrieved suggestions remain candidate hypotheses and never gain mechanism status from similarity. |

P0 defines the first complete research workflow. P1 supports a stronger study. P2 is optional after the reasoning result is useful.

## Result requirements

Each result includes scenario and configuration IDs, changed inputs or requested target, mechanism/model application IDs, intermediate outputs, applicable conditions, evidence locations, unresolved inputs, conflicts, numerical uncertainty when justified, and run/version information.

Use these result states: `conditional_supported`, `qualitative_only`, `unresolved`, `blocked`, and `infeasible_within_search`. The last state refers to the declared search space, not all possible innovations. Reviewed information remains conditional on model applicability.

## Nonfunctional requirements

- Operate locally for the initial pilot, with no mandatory paid model or cloud database.
- Keep input data private unless the team deliberately supplies it to an approved service.
- Separate read-only analysis from knowledge editing; record review and revision history.
- Never evaluate executable code from uploaded documents. Apply parser, file-size, page-count, and time limits.
- Make evidence and result states understandable without knowing database terminology.
- Log runtime, model calls, token usage when available, and actual spend. Do not assume free services remain free.
- Preserve a machine-readable export format to avoid dependence on one graph vendor.
- Meet a provisional interactive goal of completing pilot cases within 10 seconds on the recorded team machine. This is a proposed target, not measured performance; long jobs must expose their status.

## Scope exclusions

No autonomous invention certification, patent filing, manufacturing control, whole-industry web crawling, production digital twin, automatic safety approval, new large-model training, enterprise billing, supplier marketplace, or full CAD integration in the initial project. These do not help test the central hypothesis within the available student project.

## Definition of done

Complete P0 behavior, a reviewed first pack, an independently reviewed test set, matching baselines, documented failure analysis, reproducible exports, and a second-pack transfer attempt. A failed or partial transfer is still a result and must be reported.

## Open requirements

Team capacity, deadline, first-domain reviewers, UI preference, institutional IP ownership, language support, and real deployment requirements remain unknown. The proposed stack and milestones are recommendations, not approved commitments.
