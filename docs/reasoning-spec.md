# Proposed reasoning method

Date: 12 October 2026. Design specification; no performance results.

## Research question

Does explicit checking of context and model inputs across mechanism paths reduce unsupported impact conclusions while retaining useful coverage, compared with retrieval, graph traversal, and established engineering calculation workflows?

## Forward reasoning

```text
validate scenario, pack revision, and product configuration
initialize changed parameters with explicit origin and uncertainty
plan bounded candidate paths using permitted relation categories
for each model application in dependency order:
    verify reviewed model and exact input/output bindings
    evaluate context predicates as true, false, or unknown
    if any required condition is false: record blocked branch
    if any required condition or input is unknown: record unresolved branch
    check units and physical/model bounds
    execute registered model with its declared numerical policy
    record outputs, assumptions, evidence, conversions, and limits
merge output branches without double-counting shared mechanisms
return conditional results plus all material blockers
```

Structural and semantic edges help locate relevant entities. Only an explicit mechanism or approved model application can support a physical-effect step. A path reaching a product does not by itself quantify that product's behavior.

## Proposed condition-composition algorithm

For an application `a`, define its contract as input/output quantity kinds, configuration binding, required predicates, model version, and evidence IDs. A chain is supported only if every required application contract is satisfied under one consistent scenario assignment. Checking each edge against a different convenient operating condition is invalid.

Bind repeated parameters by canonical configuration-specific IDs. Normalize compatible units, then intersect admissible bounds for shared quantities. An empty intersection blocks the chain; an unknown required predicate leaves it unresolved. Apply all relevant hard constraints to the resulting assignment. A nonlinear feasible region may require an approved solver rather than independent interval intersections. The initial pilot can restrict itself to scalar bounds and explicitly decline more complex regions.

Keep model applications as an AND-dependency: all required inputs and conditions must be available. Alternative applicable models or mechanisms form OR-branches, and each branch retains separate evidence and assumptions. Do not combine an input from one alternative with the assumptions of another merely to obtain a result.

For each unresolved target, propagate a blocker set backward through these AND/OR dependencies. An AND-branch needs the union of its missing requirements; an OR-branch can report alternative requirement sets. Remove duplicate requirements and strict supersets only when they refer to the same configuration and would establish the same target. These are minimal missing-input sets within the represented graph, not a claim that a new experiment is sufficient to prove physical causation.

Retain all condition checks in the run certificate. The proposed study should compare the extra consistency/blocker-set work with ordinary per-model checking and an expert-authored constraint solver. If these behaviors are already covered by the closest work, this specification provides no new algorithmic novelty by itself.

## Backward investigation

Start from a target parameter and inequality or allowable interval. Find model applications that produce it. Identify upstream controllable variables and allowable interventions. Solve an approved inverse relation when one exists, otherwise enumerate a bounded candidate set or use an approved optimizer. Non-invertible and underdetermined models require multiple candidates or an unresolved result.

Forward-evaluate every candidate through the same model graph. Reject hard constraint violations before ranking. Return the search bounds and termination reason. A failed search means no candidate was found in that search, not that no solution exists.

If sensitivity analysis is used, record the evaluation point and range. A local derivative cannot justify extrapolating a trend over a large operating change. Distinguish interventions the engineer can control from properties merely observed in the evidence.

## Illustrative calculation, not experimental evidence

For a simplified steady conduction path, use `R = L / (k A)` and `Delta T = Q R`. All numbers below are invented for illustrating the contract. They are not material measurements or product specifications.

Assume thickness `L = 0.001 m`, area `A = 0.001 m^2`, conductivity `k = 1 W/(m K)`, and heat flow `Q = 2 W`. The layer resistance is `1 K/W`, giving a `2 K` temperature difference across that layer. If conductivity becomes `2 W/(m K)` under the same valid model conditions, resistance is `0.5 K/W` and the layer temperature difference is `1 K`.

This is a temperature drop across an idealized layer. It is not a prediction of full LED junction temperature, efficiency, lifetime, or lamp performance. A real thermal network needs contact, package, heat-sink, and ambient conditions with applicable data. The source relationship and its assumptions must be verified before using this equation in an accepted engineering pack.

For the illustrative inverse target `Delta T <= 1 K`, holding `L`, `A`, and `Q` fixed implies `k >= 2 W/(m K)`. This becomes a candidate property requirement. It does not identify a compatible purchasable material; that step needs evidence for electrical insulation, interface compatibility, degradation, and other specified constraints.

## Quantitative uncertainty

Use bounded intervals first when the sources justify ranges. Maintain dependencies between reused quantities; repeated use of one uncertain input is not independent evidence. Interval bounds can overestimate uncertainty, so document the arithmetic policy. Monte Carlo is optional only when distributions and correlations are justified and a seed/sample budget is recorded.

Keep extraction confidence, evidence quality, numerical uncertainty, and candidate ranking separate. Do not multiply arbitrary edge confidence scores and call the result a probability of physical success. Do not add outputs from overlapping paths unless the registered model defines an additive aggregation.

## Contradictions

First compare configurations, measurement methods, dates, and operating conditions. Different-context values can coexist. Conflicting same-context values remain unresolved or become alternate scenario branches pending review. Source prestige alone does not select the correct engineering value. Preserve the discarded claim and adjudication reason when a reviewer resolves a conflict.

## Missing evidence and next investigations

A blocker record identifies the desired conclusion, the failed model or relation, required input/condition, and a specific evidence request. For example: obtain thermal conductivity at the operating temperature, or measure contact resistance for the specified interface. Rank these investigations by relevance to the user target and acquisition burden only when that burden is known. This stays within evidence-gap analysis; it is not a separate autonomous experimentation product.

## Candidate ranking

Use feasibility tiers first: conditional feasible, qualitative only, unresolved, blocked. Within the supported tier, compare target effect, constraint margins, evidence coverage, and measured or supplied acquisition cost. Display a Pareto set when objectives conflict. If using weighted scores, expose the weights and unknown criteria. Ranking cannot establish innovation novelty.

## Termination and failure

Bound graph depth, model applications, inverse candidates, solver steps, and total runtime. Flag truncation and unsupported coupled models. Do not return a polished final answer when computation failed. Store enough context to reproduce the failure and inspect the first meaningful blocker.
