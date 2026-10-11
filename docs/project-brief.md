# Project brief

Date: 12 October 2026. Status: proposed design, awaiting team and guide review.

## Plain explanation

ChainReaction helps an engineer investigate two questions: what could change downstream if a technology improves, and what could be changed upstream to meet a product requirement? It connects product structure to material properties, scientific principles, and mathematical models. Every answer should expose the conditions and evidence that make it credible.

It helps people investigate possible innovations. It does not certify that an idea is new, feasible in a real product, or patentable.

## Why this project matters

A useful engineering answer needs more than related documents. A material property measured at one temperature may not apply at another. A change that improves one component may violate a product's space or compatibility requirement. A quantitative result may depend on a parameter the user has not supplied. The project will test whether representing these conditions explicitly improves impact analysis.

This is a research question. We have not demonstrated that the proposed representation outperforms established methods.

## Intended users and their jobs

| User | Job | Useful output |
|---|---|---|
| Engineering student | Explain a known change chain | Inspectable path with equations and sources |
| Researcher | Identify where evidence is missing | A bounded hypothesis and required investigation |
| Product engineer | Check a candidate improvement | Conditional impact plus constraint conflicts |
| Technology-development team | Compare candidate changes | Feasibility tiers and tradeoffs, with provenance |

## What stays constant across industries

The shared framework handles entity identity, parameter values and units, evidence locators, context conditions, model bindings, scenario inputs, result states, and reproducible run records. Domain packs supply the actual engineering vocabulary, allowed relationships, materials, product structures, models, and validity rules.

The six entity types are a common organization scheme. They are not six mandatory steps in every impact path. Equations relate several parameters at once; they should be represented as model applications with explicit inputs and outputs, rather than a chain of unrelated pairwise arrows.

## First domain, then transfer

The recommended first pack is LED lighting with a tightly bounded thermal-management scenario. This remains within the synopsis's lighting example but is easier to check numerically than the full history of LED development. The historical blue-LED chain stays as an explanatory case, not a forecast experiment.

A second pack, proposed for a transfer test, models steady conduction through a simple insulation assembly. It tests reuse of the engine in a building-envelope context. Shared thermal equations alone would be weak evidence of broad transfer, so a later mechanical-stiffness pack should test different equations and constraints if resources permit. Neither pack commits the product permanently to those industries.

## Success means

The team can demonstrate a correct, conditional forward calculation; derive and recheck a feasible backward candidate; refuse an invalid model application; show evidence for each accepted mechanism; and load a second domain without changing core logic. The research succeeds if controlled experiments then establish a useful advantage over strong baselines, including a conventional engineering solver.

## Decisions still needed

Confirm the semester deadline, available weekly effort, access to engineering reviewers, affordable operating budget, first-domain source permissions, and institution IP rules. These affect delivery pace and publication strategy; they do not change the project's central purpose.
