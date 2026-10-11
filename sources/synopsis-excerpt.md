# Privacy-safe synopsis excerpt

Source pages 3-12, excluding header-only page 11. This is extracted source text, not a new claim of approval.

## Source page 3

Vishwakarma Institute of Technology Issue 01 : Rev No. 00 : Dt. 05/02/26

 FF No 180

Project Synopsis
1. Introduction
ChainReaction of Innovation is a proposed research framework for representing and reasoning over engineering
knowledge across multiple levels of a technology. The central premise is to investigate how a change introduced at one
level of an engineering system may propagate through related components, materials, physical or chemical principles,
mathematical relationships, subsystems, and products, and how such propagation can be analysed to identify potential
technological impacts and candidate innovation opportunities.
The proposed framework organizes engineering knowledge into multiple interconnected layers, including products,
subsystems, components, materials, physical or chemical principles, and mathematical models. Rather than
representing these entities as isolated records, the framework will model explicit relationships among them, together
with relevant properties, operating conditions, constraints, equations, assumptions, and supporting evidence. This
representation is intended to provide a structured basis for analysing how changes in one entity may influence related
entities across different levels of abstraction.
For example, an improvement in a component may depend on a change in material properties, where the resulting
behaviour is governed by one or more physical principles and described quantitatively through an appropriate
mathematical relationship. The resulting change may influence a subsystem and subsequently affect one or more
products that incorporate that subsystem. Conversely, a limitation observed at the product level may be traced through
subsystems, components, materials, physical principles, and mathematical relationships to investigate possible lower-
level changes that could potentially address the identified limitation.
The project therefore considers two complementary forms of reasoning. Forward analysis will begin with a proposed
technological change and investigate its possible effects on related components, subsystems, products, or associated
technologies. Backward analysis will begin with a product limitation, performance requirement, or engineering
objective and investigate possible mechanisms, components, materials, or parameter changes that may contribute to
addressing it. Both forms of analysis will be constrained by the explicitly represented engineering conditions,
assumptions, and available evidence.
The framework will distinguish between structural relationships, scientific relationships, mathematical relationships,
and the evidence supporting those relationships. A graph connection alone will not be considered sufficient evidence
that a technological change will produce a particular outcome. Where a quantitative relationship is available, the
framework may apply an appropriate mathematical model subject to its documented assumptions, input requirements,
boundary conditions, and validity range. Where information is incomplete, uncertain, or contradictory, the framework
will preserve and represent such uncertainty rather than automatically inferring a positive technological impact.
The proposed system is intended as a research and engineering decision-support framework rather than an autonomous
invention-generation system. Its purpose is to assist researchers and engineers in exploring relationships, dependencies,
and possible consequences of technological changes while providing traceable reasoning paths and supporting
evidence that can be inspected and evaluated by a human reviewer.
The research will investigate whether a multi-layer representation of engineering knowledge can provide more useful,
explainable, and traceable technology-impact analysis than approaches based solely on document retrieval,
conventional graph traversal, or generated responses based on retrieved information. The proposed contribution will
therefore be evaluated experimentally using defined engineering scenarios, baseline methods, evidence sources,
engineering constraints, and measurable evaluation criteria.
The project will begin with a bounded set of documented technologies, engineering relationships, mathematical
models, and supporting evidence. The initial prototype will not attempt to model the entire engineering domain.
Instead, selected technical domains will be used as controlled settings for investigating the feasibility of the proposed
representation, reasoning mechanisms, mathematical relationships, evidence handling, uncertainty representation, and
the potential transferability of the framework to additional engineering domains.
Scope and intended users
The proposed framework is intended for researchers, engineering students, engineers, and technology-development
teams who need to investigate relationships between technological changes and existing products or engineering
systems. The system is intended to support exploration and analysis rather than replace engineering judgement or
expert validation.



## Source page 4

Vishwakarma Institute of Technology Issue 01 : Rev No. 00 : Dt. 05/02/26

                    FF No 180

The initial scope will focus on a bounded set of technical domains for which sufficiently documented product
structures, component relationships, material properties, scientific principles, mathematical models, and supporting
evidence can be obtained. The framework will be designed so that additional domains can be incorporated through
domain-specific entities, relationships, constraints, and engineering models.
The project will investigate a common knowledge representation across the selected domains while allowing domain-
specific rules where required. A successful demonstration in selected domains will therefore be interpreted as evidence
of feasibility under the evaluated conditions rather than proof of universal applicability.
The framework will support two primary analysis directions. Forward analysis will investigate the possible
downstream effects of a specified technological change. Backward analysis will investigate candidate lower-level
changes that could potentially address a specified product limitation or engineering objective.
The output of an analysis will include the identified reasoning path, relevant relationships, applicable constraints,
mathematical models where available, supporting evidence, assumptions, and unresolved information. Candidate
innovation opportunities will be presented as research hypotheses or engineering options requiring further evaluation
rather than as automatically validated inventions.
Research focus
The research focuses on investigating how knowledge distributed across different levels of an engineering system can
be represented and reasoned over to understand the propagation of technological changes and identify potential
innovation opportunities.
The proposed framework will represent engineering knowledge through six interconnected layers: products,
subsystems, components, materials, physical or chemical principles, and mathematical models. Relationships within
and across these layers will be represented explicitly so that a change at one level can be investigated for its possible
effects on related levels.
The research will investigate two complementary reasoning directions. Forward reasoning will start from a
technological change and examine its possible effects on components, subsystems, products, and related technologies.
Backward reasoning will start from a product limitation, performance requirement, or engineering objective and
investigate possible lower-level changes that could potentially address it.
A key research focus is the integration of mathematical relationships and engineering constraints into this propagation
process. Where suitable equations and engineering models are available, they will be used to evaluate whether a
proposed relationship is quantitatively meaningful. Calculations will be subject to required parameters, units,
assumptions, operating conditions, and validity ranges.
The framework will also maintain evidence and provenance for the information used during reasoning. This will allow
the system to distinguish between established information, evidence-supported relationships, conditional calculations,
and unresolved hypotheses. Missing or contradictory information will be explicitly represented rather than converted
into unsupported conclusions.
The research will therefore investigate whether combining multi-layer engineering knowledge representation,
relationship-based reasoning, mathematical models, engineering constraints, and evidence can improve the
identification and explanation of technology impacts and candidate innovation opportunities compared with simpler
retrieval or graph-based approaches.
The proposed contribution will be established through implementation and evaluation on selected technical scenarios.
Candidate innovation opportunities produced by the framework will be treated as research hypotheses or engineering
options requiring further validation, rather than as automatically generated inventions.












## Source page 5

Vishwakarma Institute of Technology Issue 01 : Rev No. 00 : Dt. 05/02/26

            FF No 180

2. Review of Literature
Technology Opportunity Discovery (TOD) research investigates methods for identifying potential technological
opportunities from relationships among technologies, products, patents, and related knowledge. Recent studies have
progressively moved from similarity-based approaches toward knowledge networks, semantic relationships, and graph-
based learning. The following studies form the literature foundation for the proposed ChainReaction of Innovation
framework.
Lee et al. (2020) proposed a word2vec-based approach for navigating a product landscape using an integrated patent-
product database. The approach represents relationships between patent and product entities through vector-space
similarity and uses these relationships to identify potential technology opportunities. This work demonstrates the
usefulness of connecting patent information with product-level information for technology opportunity analysis.
However, the representation primarily captures relationships at the product and technology-concept level and does not
explicitly represent the physical, material, or mathematical mechanisms underlying those relationships.
Ren and Zhao (2021) proposed a technology opportunity discovery approach based on constructing, evaluating, and
searching knowledge networks. Their work demonstrates how technological relationships can be represented as a
network and searched to identify potential opportunities. This provides an important foundation for the use of
structured relationships in ChainReaction. However, the knowledge-network representation does not explicitly trace
how a technological relationship is realized through materials, components, physical principles, or mathematical
dependencies.
Liu et al. (2023) developed a technology opportunity analysis approach using hierarchical semantic networks and dual
link prediction. Their work introduces hierarchical semantic relationships and link prediction for identifying potential
technological opportunities. The study demonstrates that structured semantic relationships can improve the analysis of
technology connections. However, the predicted relationships remain primarily at the semantic or technology-concept
level and do not explicitly model the engineering mechanism through which a change propagates from a scientific
principle or material to components, subsystems, and products.
Honores-Marín et al. (2026) proposed an approach based on relational graph convolutional networks (R-GCNs),
PatentSBERTa, temporal analysis, and large language model-assisted interpretation for technological opportunity
discovery in converging industries. This represents a significant progression toward heterogeneous and temporal
graph-based technology analysis. The approach can learn relation-specific patterns among patents, inventors,
organizations, technologies, and classifications. However, the learned relationships and subsequent interpretation do
not explicitly trace the physical or mathematical mechanism responsible for a technology impact.
Research Gap
The reviewed studies demonstrate substantial progress in Technology Opportunity Discovery, from vector-space
similarity and knowledge networks to hierarchical semantic networks and heterogeneous graph neural networks.
However, within the four reviewed TOD studies, the relationships between technologies are primarily represented
through similarity, connectivity, semantic links, or learned graph patterns. The reviewed approaches do not jointly
represent the underlying engineering mechanism connecting scientific principles, materials, components, subsystems,
and products.
The first identified gap is the absence of an explicit science-to-engineering mechanism layer within the reviewed
TOD approaches. The proposed research therefore investigates a multi-layer representation connecting scientific or
physical/chemical principles, mathematical models, materials, components, subsystems, and products.
The second gap concerns forward multi-hop impact propagation. Existing approaches identify related technologies
or potential links, but the reviewed studies do not explicitly model a step-by-step engineering propagation path through
intermediate material, component, subsystem, and product levels. ChainReaction will investigate whether such multi-
hop propagation can provide a more interpretable explanation of how a technological change may influence
downstream systems.
The third gap is backward, bottleneck-driven reasoning. The reviewed approaches primarily operate in a forward
technology-discovery direction. They do not explicitly begin with a product limitation and trace upstream through
constrained parameters, components, materials, and scientific principles to identify candidate technological changes.
ChainReaction will investigate this reverse reasoning direction.



## Source page 6

Vishwakarma Institute of Technology Issue 01 : Rev No. 00 : Dt. 05/02/26

FF No 180

The fourth gap concerns quantitative, parameter-level dependencies. Existing approaches use similarity scores,
network connectivity, link-prediction probabilities, or learned graph relationships. These do not directly represent
engineering quantities such as the affected parameter, direction of effect, sensitivity, or validity range. The proposed
framework will investigate whether representing such engineering attributes can improve the interpretability of
technology-impact relationships where suitable evidence and mathematical models are available.
The fifth gap concerns structured evidence and validation. The reviewed approaches primarily derive relationships
from similarity, network structure, prediction models, or learned representations. The proposed research will
investigate attaching evidence sources and validation states to relationships so that identified technology-impact paths
can be examined and assessed rather than treated as automatically established facts.
Therefore, the proposed research will investigate whether a mechanism-aware, evidence-grounded technology
dependency graph spanning scientific principles, materials, components, subsystems, and products can improve
the discovery and explanation of multi-hop technology impact chains in both forward and backward directions,
compared with conventional patent-based similarity, network, and link-prediction approaches.
The identified gaps are treated as research hypotheses and proposed directions rather than claims of guaranteed
novelty. The scope of the gap is specifically based on the four TOD papers reviewed from 2020 to 2026. Related work
in other areas, such as materials-science knowledge graphs or engineering knowledge representation, will need to be
considered during further research.
3. Problem Statement and Objectives
Existing Technology Opportunity Discovery (TOD) approaches have progressed from vector-space similarity and
knowledge networks to hierarchical semantic networks and heterogeneous graph-based learning. However, the four
reviewed studies primarily represent technological relationships through similarity, network connectivity, semantic
links, or learned graph patterns. They do not explicitly represent the underlying engineering mechanisms connecting
scientific principles, mathematical models, materials, components, subsystems, and products.
As a result, existing approaches do not explicitly support step-by-step forward propagation of technological
impacts through intermediate engineering levels. They also do not explicitly provide backward, bottleneck-driven
reasoning, where a product limitation can be traced upstream to a constrained parameter, component, material, or
scientific principle. Furthermore, the reviewed approaches do not directly represent engineering-interpretable
quantitative dependencies such as parameter, direction of effect, sensitivity, and validity range, nor do they provide a
structured evidence and validation state for each relationship.
Therefore, the proposed ChainReaction of Innovation framework investigates whether a mechanism-aware and
evidence-grounded technology dependency graph can represent these engineering relationships and support both
forward and backward reasoning for discovering and explaining potential technology impact chains and candidate
innovation opportunities. The proposed framework is intended as a research prototype and does not assume that every
identified relationship represents a validated invention or engineering solution.
Objectives
To design a multi-layer engineering knowledge representation connecting scientific or physical/chemical
principles, mathematical models, materials, components, subsystems, product features, and products.
To develop a knowledge-graph prototype capable of representing relationships within and across the different
engineering layers.
To implement forward reasoning for tracing how a proposed technological or material/component change may
propagate through components and subsystems toward potential product-level impacts.
To implement backward, bottleneck-driven reasoning that starts from a product limitation or engineering
requirement and traces upstream toward candidate components, materials, scientific principles, or technological
changes.
To represent quantitative engineering dependencies using attributes such as affected parameter, direction of effect,
sensitivity, confidence, and validity range wherever suitable mathematical or engineering evidence is available.
To associate evidence and validation information with relationships by recording evidence sources, confidence
scores, and validation states such as candidate, predicted, verified, expert-approved, or rejected.

## Source page 7

Vishwakarma Institute of Technology Issue 01 : Rev No. 00 : Dt. 05/02/26

FF No 180

Proposed evaluation
The proposed ChainReaction of Innovation framework will be evaluated to determine whether a mechanism-aware and
evidence-grounded technology dependency graph can improve the discovery and explanation of multi-hop technology
impact chains.
The evaluation will consider both forward reasoning and backward reasoning using selected engineering and
technology scenarios. For forward reasoning, the system will begin with a proposed technological, material, or
component-level change and evaluate whether it can trace the possible effects through relevant engineering
relationships toward components, subsystems, and products. For backward reasoning, the system will begin with a
product limitation or engineering requirement and evaluate whether it can trace possible upstream dependencies
toward components, materials, scientific principles, and relevant technological changes.
The proposed framework will be evaluated against suitable baseline approaches, including conventional patent-based
similarity, network-based relationships, and link-prediction-based approaches. The comparison will investigate
whether explicit engineering mechanisms and multi-hop reasoning provide more interpretable and useful technology-
impact paths.
Evaluation measures will include Precision@K, Recall@K, path accuracy, and expert evaluation. Precision@K
and Recall@K will be used to evaluate the relevance of identified technology opportunities where suitable reference
results are available. Path accuracy will assess whether the intermediate relationships in an identified technology-
impact chain are correct. Expert evaluation will assess the relevance, engineering plausibility, interpretability, and
usefulness of the generated paths.
At least one historically known technology chain will be used as an evaluation case, such as the progression from blue
LED technology to efficient white lighting and related display applications. Additional scenarios may be included
subject to the availability of reliable technical evidence and suitable reference information.
Results will be reported separately for the evaluated scenarios and domains, including successful paths, incorrect paths,
unresolved cases, and failures. The evaluation will be treated as an empirical investigation of the proposed framework
rather than evidence that the system can automatically generate or validate inventions.
4. System Architecture
The proposed ChainReaction of Innovation architecture consists of an evidence ingestion layer, a multi-layer
engineering knowledge representation, a relationship and evidence layer, a reasoning engine, and an evaluation/output
layer.
Technical sources such as research papers, patents, product specifications, engineering documents, and other permitted
technical sources will provide the information required to construct the knowledge representation. Extracted
information will be associated with its source and relevant evidence so that relationships can be traced back to their
supporting information.
The core knowledge representation will organize engineering knowledge into six interconnected layers:
Product Layer
Subsystem Layer
Component Layer
Material Layer
Physical/Chemical Principle Layer
Mathematical Model Layer
These layers will not be treated as a strictly linear hierarchy. Relationships may exist within the same layer as well as
across different layers. The mathematical model layer will represent applicable equations and parameter relationships
where sufficient information is available.






## Source page 8

Vishwakarma Institute of Technology Issue 01 : Rev No. 00 : Dt. 05/02/26

FF No 180

A relationship layer will represent dependencies between entities and may include attributes such as the affected
parameter, direction of effect, sensitivity, confidence, validity range, and supporting evidence, where such information
is available. Each relationship will also maintain a validation state such as candidate, predicted, verified, expert-
approved, or rejected.
The reasoning engine will support two complementary analysis directions. Forward reasoning will investigate how a
technological change may propagate through relevant engineering dependencies toward component, subsystem, and
product-level effects. Backward reasoning will begin with a product limitation or requirement and trace upstream
dependencies toward components, materials, scientific principles, and mathematical parameters that may provide
candidate solutions.
Mathematical calculations will be performed only when the required inputs, units, assumptions, operating conditions,
and validity conditions are available. Relationships for which sufficient information is unavailable or contradictory will
be represented as unresolved rather than being treated as established engineering facts.
The proposed implementation may use Python for data processing and reasoning, together with an appropriate graph-
oriented data store and a user interface for entering scenarios and inspecting relationships and supporting evidence.
These implementation choices will be finalized according to project resources and feasibility.



## Source page 9

Vishwakarma Institute of Technology Issue 01 : Rev No. 00 : Dt. 05/02/26

FF No 180
Forward and backward analysis
Forward reasoning will start from a proposed technological, material, or component-level change and trace its
potential effects through connected engineering relationships. A representative reasoning path may be:
Technology Change → Material/Component Effect → Subsystem Effect → Product Impact
The reasoning process will examine the relevant physical or chemical principles and mathematical relationships
wherever sufficient evidence and applicable models are available.
Backward reasoning will start from a product limitation, performance requirement, or engineering objective and trace
relevant dependencies upstream. A representative path may be:
Product Limitation → Subsystem/Component Constraint → Material Property → Physical/Chemical Principle
→ Mathematical Parameter
The two directions will use the same underlying engineering knowledge representation and evidence. Reversing a
graph relationship alone will not be considered sufficient for backward reasoning; the resulting relationship must be
supported by appropriate engineering evidence and constraints.

Illustrative scenario
Consider an engineering improvement introduced at a lower level of a technology. For example, an improvement in a
material or component property may change the behaviour of a subsystem and subsequently influence the performance
or design possibilities of a product.
The system would represent the relevant entities and relationships across the six layers and investigate the resulting
impact path. Where an applicable mathematical relationship is available, the system would use the relevant parameters,
assumptions, units, and operating conditions to determine whether the proposed dependency can be quantitatively
evaluated.
For example, a change in a component property may influence a subsystem parameter, which may subsequently affect
a product-level performance characteristic. The system would retain the supporting evidence and reasoning path for
each identified relationship. If a required parameter or relationship cannot be established from available evidence, the
corresponding conclusion would remain unresolved.
A historically documented technology chain, such as blue LED technology → efficient white lighting → display
applications, may be used as an evaluation case. This represents a proposed evaluation scenario rather than a claimed
experimental result.


## Source page 10

Vishwakarma Institute of Technology Issue 01 : Rev No. 00 : Dt. 05/02/26

FF No 180

5. Environment
The main environmental considerations of the proposed system are computational processing, document storage, and
network usage. The initial prototype will use existing computing resources where practical, and large-scale model
training is not part of the proposed initial implementation.
The system will use bounded datasets and selected technical sources for experimentation. Where practical, caching and
reuse of processed information will be used to reduce unnecessary repeated computation and data transfer.
During evaluation, computational requirements such as execution time, storage requirements, and resource usage may
be recorded to understand the practical resource requirements of the prototype. No environmental benefit or carbon-
emission reduction will be claimed without appropriate measurement and comparison.
6. Sustainability
The system may help users investigate relationships between technological changes, engineering components,
materials, principles, and products using a structured and traceable knowledge representation. Extending product life is
a possible application, but any benefit would depend on a real engineering decision and its outcome. The project would
not equate recommending a replacement with reducing electronic waste. A future assessment would need the old and
proposed configurations, expected service life, repair requirements, and relevant material or energy data.
Software maintainability is also a practical concern. Domain rules would be stored separately from the shared engine
so that changes can be reviewed and tested. Source versions and extraction settings would be recorded to make results
reproducible. Exportable data and documented schemas would reduce dependence on a single database
implementation. The team would track annotation and maintenance effort because a system that requires repeated
manual reconstruction is difficult to sustain.
7. Safety
The prototype will provide research and decision-support information and will not directly control physical equipment.
However, an incorrect engineering dependency or technology-impact conclusion could lead to an inappropriate design
decision if interpreted without expert review. Therefore, unsupported or incomplete relationships will be represented as
unresolved rather than automatically accepted. Mathematical results will include their applicable assumptions,
operating conditions, and validity limitations. Safety-critical engineering decisions will require qualified expert review
before implementation.
8. Ethics
Every displayed technical claim should retain a source location and a clear status: reported claim, reviewed
observation, conditional calculation, or unresolved hypothesis. Repeated publications describing the same experiment
would not count as independent confirmation. The interface should make gaps in product coverage visible so users do
not interpret an absent result as proof that no effect exists.
The team would use documents under suitable access and reuse terms. Public availability does not automatically
permit redistribution. Private organizational configurations would require authorization, access restrictions, and a
controlled export process. Personal contact details collected for project registration would not become part of the
research dataset. Evaluation reports would describe coverage differences between domains and disclose remaining
limitations.
9. Cost
The following is an illustrative, unapproved planning budget for a student prototype, not a vendor quotation. It
assumes existing computers and access to permitted documents. Incremental device purchase is budgeted at INR 0; a
model-API spending cap is INR 2,000; hosting and storage allowance is INR 1,000; and documentation allowance is
INR 500. The subtotal is INR 3,500. A 20% contingency adds INR 700, giving a proposed ceiling of INR 4,200. The
team must confirm affordability and actual service prices before spending.
This ceiling excludes paid datasets, new hardware, expert compensation, and the value of student development time.
Any such requirement would need a revised budget. Local processing may reduce API expenditure while increasing
device runtime. The prototype would therefore log both usage and monetary charges. Cost per scenario would be
calculated from actual service charges divided by completed analyses, with unresolved analyses reported separately.
Free software would be selected only after checking its licence and deployment conditions.


## Source page 12

Vishwakarma Institute of Technology Issue 01 : Rev No. 00 : Dt. 05/02/26

       FF No 180

The final budget will be determined based on the selected APIs, storage requirements, computing resources, and
available institutional resources.
10. SDG Goal
The primary alignment is SDG 9: Industry, Innovation and Infrastructure. The proposed system could support
research and industrial innovation by making the evidence behind technology-impact analysis and engineering
innovation decisions easier to inspect.
The secondary alignment is SDG 7: Affordable and Clean Energy. The system could support the identification of
potential energy-efficiency improvements by tracing relationships between materials, components, physical principles,
mathematical models, and energy-related products, such as LED lighting and other energy-consuming technologies.
These are intended contributions, not measured changes in official SDG indicators. Relevant project measures would
include traceable impact records, review effort, the fraction of decisions supported by adequate engineering evidence,
the number of energy-related impact pathways identified, and estimated changes in energy consumption under clearly
specified operating conditions.
Technology readiness and expected outcome
Using the supplied TRL reference, the present self-assessment is TRL 2: the concept and intended application have
been formulated. No working prototype or experimental validation is claimed. Progress toward TRL 3 would require
an implemented proof of concept with reproducible examples and documented evaluation results. The guide should
review this assessment.
The expected outcome is a prototype that helps users inspect possible product impacts, understand compatibility
conditions, and identify useful next investigations. A research paper or patent application would depend on the
contribution demonstrated after implementation and comparison with prior work. This synopsis does not assert patent
eligibility, publication acceptance, or industrial readiness.
References and Implementation Plan
[1] S. Lee, D. Jeon, J. Ahn, and O. Kwon, “Navigating a product landscape for technology opportunity analysis: A
word2vec approach using an integrated patent-product database,” Technovation, vol. 96–97, art. 102140, 2020.
[2] H. Ren and Y. Zhao, “Technology opportunity discovery based on constructing, evaluating, and searching
knowledge networks,” Technovation, vol. 101, art. 102196, 2021.
[3] Z. Liu, J. Feng, and L. Uden, “Technology opportunity analysis using hierarchical semantic networks and dual link
prediction,” Technovation, vol. 128, art. 102872, 2023.
[4] G. Honores-Marín, S. Hashemkhani Zolfani, and M. Chipulu, “From patents to predictive analytics: Leveraging R-
GCNs for technological opportunity discovery in converging industries,” Technological Forecasting and Social
Change, vol. 227, art. 124613, 2026.
Planned development sequence
Stage 1: Define the six-layer engineering knowledge representation and relationship schema based on the identified
research gaps.
Stage 2: Collect and organize a bounded set of technical evidence covering products, subsystems, components,
materials, physical/chemical principles, and mathematical relationships.
Stage 3: Implement the knowledge-graph prototype and evidence/provenance representation.
Stage 4: Implement forward and backward reasoning for selected technology-impact scenarios.
Stage 5: Incorporate quantitative dependencies and mathematical relationships where sufficient engineering
information is available.
Stage 6: Evaluate the prototype using selected technology scenarios and a historically known technology chain using
Precision@K, Recall@K, path accuracy, and expert evaluation.
Stage 7: Analyze failures, unresolved relationships, limitations, and possible improvements.
