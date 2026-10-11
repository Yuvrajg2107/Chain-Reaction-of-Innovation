# Chain Reaction of Innovation

An engineering decision-support research project: trace how a change in a material, component, or design could affect products, and work backward from a product limitation to candidate changes.

**Status: research and implementation plan, 12 October 2026.** This repository contains the reviewed project definition, literature assessment, product requirements, technical contracts, and evaluation plan. The application has not been built or experimentally validated. Publication and patentability remain unproven.

## What we are building

Engineering knowledge sits across papers and product specifications, mathematical equations, and product structures. ChainReaction connects that knowledge through six types of engineering entities: products, subsystems, components, materials, physical or chemical principles, and mathematical models. A reasoning result must show the evidence and conditions behind each step.

The intended framework can accept different industry domain packs. The first experiments will use bounded engineering cases so that we can check whether its reasoning is correct. A reusable engine does not imply that we already have knowledge of every industry.

The proposed research contribution is **context-checked impact propagation and constrained backward analysis with explicit unresolved results**. Merely combining a knowledge graph, six layers, and an LLM is insufficient as a novelty claim. See the [research assessment](docs/research/novelty-assessment.md).

![Proposed architecture](assets/diagrams/architecture.png)

## Read this first

| Reader | Start here | Then read |
|---|---|---|
| New teammate | [Project brief](docs/project-brief.md) | [PRD](docs/PRD.md), [roadmap](docs/implementation-plan.md) |
| Developer | [Architecture](docs/architecture.md) | [Data contract](docs/data-contract.md), [reasoning](docs/reasoning-spec.md) |
| Research lead or guide | [Source review](docs/source-review.md) | [Literature](docs/research/literature-review.md), [evaluation](docs/evaluation-plan.md) |
| Publication or IP discussion | [Novelty assessment](docs/research/novelty-assessment.md) | [Publication and IP plan](docs/publication-and-ip.md) |
| Coding agent | [AGENTS.md](AGENTS.md) | [Agent handoff](docs/agent-handoff.md) |

The [planning report](reports/ChainReaction_Analysis_and_Plan.pdf) collects the main decisions in a printable format. The individual Markdown documents are the editable source of truth.

The [verification record](reports/verification.md) explains what was checked and the limits of those checks.

## One concrete example

A lighting designer asks whether a different thermal-interface material would lower an LED's operating temperature. The system identifies the relevant thermal path, checks material properties and geometry, evaluates an approved model if inputs are available, and shows which product requirement might be affected. It must stop before predicting lifetime or brightness unless it has an applicable, evidenced relationship for that step.

The reverse query starts with a temperature limit and searches approved changes subject to geometry and interface compatibility, as well as operating constraints. It rechecks each candidate through the forward model. Traversing the graph backward cannot establish that a candidate works.

## Repository contents

- `docs/`: product and technical plans, team guidance, and research protocols.
- `schemas/`: proposed machine-readable domain-pack contract.
- `examples/`: synthetic contract fixtures, explicitly excluded from research results.
- `assets/source/`: the supplied technical diagrams, retained for comparison.
- `assets/diagrams/`: readable planning diagrams with editable SVG sources.
- `reports/`: printable report and document-verification record.
- `scripts/`: tools for validating documents and generating the report and fixtures.
- `sources/`: source manifest and privacy-safe synopsis excerpt.

## Current checks

Run `python scripts/validate_bundle.py` after installing `jsonschema` and `pypdf`. To regenerate the PDF and diagrams, install the versions recorded in `requirements-docs.txt`, then run `python scripts/build_report.py`. These are documentation checks, not application or engineering validation.

## Team workflow

Use small branches and review changes to the shared schema before implementing domain-specific logic. The [team guide](docs/team-guide.md) proposes workstreams; individual assignments are pending team agreement. Do not upload private specifications, credentials, institutional contact lists, or copyrighted full texts without permission.

The repository starts private while the team decides its publication and patent route. The unmodified FF180 PDF stays local because it contains personal contact details. Its permitted technical content is summarized here; the report does not fill signatures or claim institutional approval.

## First implementation milestone

Build one complete forward-and-backward scenario using a manually reviewed domain pack, with evidence inspection and missing-input behavior. Then compare it with graph traversal and retrieval baselines before extending to a second domain. See [acceptance gates](docs/implementation-plan.md).
