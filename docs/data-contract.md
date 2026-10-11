# Knowledge and domain-pack contract

Date: 12 October 2026. Proposed contract. See `schemas/domain-pack.schema.json` and synthetic fixtures in `examples/`.

## Entities and quantities

Each entity has an immutable ID, label, one of six layer types, domain ID, version, and optional aliases. Layers are `product`, `subsystem`, `component`, `material`, `principle`, and `model`. Supporting records for parameters, configurations, evidence, constraints, and reviews are not additional engineering layers.

A parameter has a canonical ID, owning entity, quantity kind, unit, and optional admissible bounds. A value assertion belongs to a configuration and operating context; it is never a global property of every instance of that material or component. Store uncertainty as a declared interval or a justified distribution with its origin. Do not label a missing uncertainty estimate as zero.

## Relationship categories

| Category | Examples | Computational meaning |
|---|---|---|
| Structural | `part_of`, `made_of`, `contains` | Navigates product structure; no numerical effect implied |
| Scientific | `governed_by`, `qualitatively_influences` | Enables conditional qualitative explanation with evidence |
| Model dependency | `input_to`, `output_of`, `models` | Refers to an explicit multi-input model application |
| Evidence | `supported_by`, `contradicted_by` | Connects a claim to a location and review |
| Association | `similar_to`, `co_occurs_with` | Discovery aid; excluded from supported physical propagation |

A model application references one reviewed model, all bound input parameters, output parameters, context, and evidence. This captures dependencies that a bare triple cannot represent. The equation definition is separate from its use in a particular product.

## Separate states

| Axis | Values | Meaning |
|---|---|---|
| Origin | manual, extracted, predicted | How a record was proposed |
| Review | unreviewed, accepted, rejected | Human judgment on the record in its stated context |
| Applicability | satisfied, failed, unknown | Whether a scenario satisfies conditions |
| Evidence | reported, modeled, measured, corroborated | Nature of support, with source independence recorded |
| Run result | conditional_supported, qualitative_only, unresolved, blocked, infeasible_within_search | What the analysis can conclude |

An accepted review does not make a model applicable everywhere. A predicted record remains a candidate until supported and reviewed. `Corroborated` requires independent evidence, not duplicate reports of the same experiment.

## Evidence record

Store title, source type, URL/DOI or local reference, publication date if verified, observed date, source version or hash, locator, access level, permitted reuse, and extraction settings. A claim's locator specifies page and section/equation/table/figure when available; web content needs a stable heading or archived permitted record. Full-text unavailable must remain explicit.

PROV-O already supplies an established provenance vocabulary. Where exchange is useful, map our source records to entities, extraction/review runs to activities, and authors/reviewers/software to agents. This mapping is an implementation choice, not research novelty. [W3C PROV-O](https://www.w3.org/TR/prov-o/)

## Context predicates

Use typed predicates: equality for configuration or regime labels, inclusive or exclusive numeric bounds with compatible units, membership in reviewed materials/interfaces, and named Boolean assumptions whose values are explicit. Three-valued evaluation is required: true, false, unknown. Unknown must not become true.

Record which conditions are essential to execute a model. If a qualitative source lacks a validity range, expose that omission; do not invent a numeric bound.

## Versioning and identity

Pack IDs and semantic versions identify released knowledge snapshots. Review decisions refer to exact claim versions. A changed source value invalidates dependent results for new runs without silently changing old run records. Same-name components are not merged unless identifiers and context establish equivalence.

## What the JSON Schema validates

The supplied schema defines entity types, parameter declarations, evidence metadata, typed relation categories, model-application bindings, scenario values, and result-state fixtures. `validate_bundle.py` also checks references and model-binding completeness.

It does not establish truth, dimensional consistency, solver correctness, reviewer expertise, source permissions, or model applicability. Those checks belong to the future engine and curation process. The example data is synthetic and has no standing as an engineering dataset.
