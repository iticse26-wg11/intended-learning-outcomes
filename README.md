# Intended Learning Outcomes

Intended learning outcomes (ILOs) for **generative AI literacy for computing students in higher education**, developed and validated by ITiCSE 2026 Working Group 11.

Every outcome completes the stem:

> **At the end of the course, students should be able to …**

## Contents

| File | What it is |
|------|------------|
| [`ilos.yaml`](ilos.yaml) | Canonical, machine-readable list of all ILOs (id, area, sub-area, topic, statement). **Edit this**; every markdown file below is generated from it. |
| [`ilos/`](ilos/) | One page per ILO, `ilos/<ID>.md` — the stable link target (generated). |
| [`scripts/build-pages.py`](scripts/build-pages.py) | Regenerates `ilos/`, `areas/` and the quick index from `ilos.yaml`. |
| [`areas/history.md`](areas/history.md) | History (H01–H02) |
| [`areas/mental-models.md`](areas/mental-models.md) | Mental Models (MM01–MM08) |
| [`areas/ethics-policy-regulations.md`](areas/ethics-policy-regulations.md) | Ethics, Policy and Regulations (EPR01–EPR14) |
| [`areas/computer-science.md`](areas/computer-science.md) | Computer Science (CS01–CS07, with CS04 split into CS04a/CS04b) |

## Overview

32 ILOs across four topic areas.

| Area | ID prefix | Count | Sub-areas |
|------|-----------|-------|-----------|
| History | `H` | 2 | — |
| Mental Models | `MM` | 8 | How GenAI works · How models are trained · GenAI applications, use cases and user attitudes · Explainability |
| Ethics, Policy and Regulations | `EPR` | 14 | Resources and labor for GenAI · GenAI and Data · Limitations, Efficacy and Alignment · GenAI Use and Responsibility · GenAI in Social, Professional, and Regulatory Contexts |
| Computer Science | `CS` | 8 | Foundations of GenAI · Trust, Risk, Verification · Human-AI Collaboration |

## Quick index

<!-- BEGIN GENERATED -->
| ID | Area | Topic | Outcome |
|----|------|-------|---------|
| [H01](ilos/H01.md) | H | History | … identify key milestones (e.g. symbolic AI, rule-based systems, machine learning, transformers, …) in AI history and explain why the field experienced periods of rapid advancement and decline (AI winters) |
| [H02](ilos/H02.md) | H | History | … distinguish between earlier applications of AI (e.g., search algorithms and engines, recommendation systems, navigation systems) and GenAI |
| [MM01](ilos/MM01.md) | MM | How GenAI works | … explain how GenAI models generate output using a simplified "next-word prediction" process, recognising that real systems predict tokens and use contextual information from prompts and prior text to determine their responses. |
| [MM02](ilos/MM02.md) | MM | How models are trained: a very high-level overview | … explain, in high-level terms, the GenAI model development process, including data collection, pre-training, and alignment methods such as fine-tuning and RLHF, as well as limitations associated with these processes (e.g., biases related with data collection, dataset cutoff dates). |
| [MM03](ilos/MM03.md) | MM | How GenAI works | … evaluate technical, ethical and practical limitations of GenAI systems (e.g. hallucinations, computational cost, context window, lack of true understanding, biases, …) |
| [MM04](ilos/MM04.md) | MM | GenAI applications, use cases and user attitudes | … identify potential GenAI use cases, such as summarisation, augmented reasoning, generating content, evaluating content, ideation, and role playing, whilst recognising that these systems might make occasional mistakes. |
| [MM05](ilos/MM05.md) | MM | How GenAI works | … analyze existing misconceptions about GenAI, distinguishing between its actual capabilities and common myths / misinterpretations. |
| [MM06](ilos/MM06.md) | MM | GenAI applications, use cases and user attitudes | … evaluate whether GenAI is appropriate for use in specific scenarios, based on ethical, practical, and task-related considerations. |
| [MM07](ilos/MM07.md) | MM | Explainability | … articulate what explainability means in AI (i.e., XAI) and how it can improve user's trust when dealing with AI systems. |
| [MM08](ilos/MM08.md) | MM | Explainability | … discuss the limitations of explainability in GenAI, including why outputs can be difficult to interpret, and identify strategies to assess the model's responses (e.g., fact-checking against trusted sources and cross-checking outputs with alternative prompts) despite limited transparency. |
| [EPR01](ilos/EPR01.md) | EPR | Resources and Labor | … understand the origins of resources (e.g. water, minerals, human labor) required to train, deploy, and host large-scale AI models |
| [EPR02](ilos/EPR02.md) | EPR | Input Data, Bias | … identify data sources used to train GenAI models and describe how training data quality, consent, and representation shape GenAI model behaviors. |
| [EPR03](ilos/EPR03.md) | EPR | Data Control | … evaluate data management in GenAI systems in order to identify risks of misuse, manipulation, and threats to data sovereignty. |
| [EPR04](ilos/EPR04.md) | EPR | Output Data | … explain the shortcomings of GenAI outputs (e.g. accuracy, reliability) and recognise the need to follow the appropriate policies and regulations within the context where the outputs will be used. |
| [EPR05](ilos/EPR05.md) | EPR | Model Limitations | … recognize limitations in GenAI model outputs, including hallucination, misinformation, privacy leakage, harmful content, in the context of societal impacts. |
| [EPR06](ilos/EPR06.md) | EPR | Measures of Efficacy | … differentiate between reliable, trustworthy, and responsible GenAI systems. |
| [EPR07](ilos/EPR07.md) | EPR | Alignment Practices | … identify tools and procedures for evaluating and verifying model outputs, and apply these to assess AI-generated content. |
| [EPR08](ilos/EPR08.md) | EPR | Cognitive Debt | … explain how overreliance on GenAI can lead to cognitive debt. |
| [EPR09](ilos/EPR09.md) | EPR | Labor and Automation | … analyze the effects of GenAI automation on human labor, workplace expectations, and the labor market. |
| [EPR10](ilos/EPR10.md) | EPR | Evaluating AI Use | … evaluate (the use of) GenAI systems against relevant normative principles (e.g., fairness, transparency, accountability, safety, robustness, and human governance). |
| [EPR11](ilos/EPR11.md) | EPR | Responsible Use | … design a plan for the responsible and context-appropriate use of GenAI, including documenting of GenAI-related outputs and decisions |
| [EPR12](ilos/EPR12.md) | EPR | AI Policy | … identify and interpret relevant GenAI policies, assessing their applicability to and impacts on GenAI use in different contexts. |
| [EPR13](ilos/EPR13.md) | EPR | Societal Influences, Expectations | … discuss societal perceptions of and expectations around GenAI use, taking into consideration power dynamics in the adoption of GenAI tools. |
| [EPR14](ilos/EPR14.md) | EPR | Discipline-Specific AI Norms | … discuss frameworks for the fair and responsible use of GenAI in the student's particular discipline. |
| [CS01](ilos/CS01.md) | CS | Types of models (local vs API, chatbot vs coding agent) | … distinguish between different types of GenAI systems (e.g., web-based chatbots, coding assistants, local vs cloud-hosted models) and apply this knowledge to select an appropriate system for specific contexts. |
| [CS02](ilos/CS02.md) | CS | GenAI Core Concepts | … explain operational GenAI concepts (e.g., tokens, context windows, probability distributions, and non-determinism) and use these concepts to interpret system behavior, output variability, and prompt sensitivity. |
| [CS03](ilos/CS03.md) | CS | Open source AI models vs proprietary models | … compare open-source and proprietary GenAI models and identify their main advantages and disadvantages for a given context, for example in terms of data privacy. |
| [CS04a](ilos/CS04a.md) | CS | Explainability and interpretability of GenAI output | … demonstrate the understanding of the need to verify and review GenAI outputs for correctness, completeness, bias, and potential harm before integrating them into a final solution. |
| [CS04b](ilos/CS04b.md) | CS | Explainability and interpretability of GenAI output | … explain limitations of GenAI verification arising from non-determinism, incomplete model transparency, and probabilistic output generation. |
| [CS05](ilos/CS05.md) | CS | Plan vs. Code | … deconstruct (decompose) problems and determine appropriate subtasks to be undertaken by humans or GenAI systems. |
| [CS06](ilos/CS06.md) | CS | Vibe vs AI-Assisted vs Agentic vs AI-TDD | … distinguish between different levels of human oversight and automation in GenAI-supported development workflows (e.g., AI-assisted, agentic, or highly automated workflows) and select an appropriate workflow for a given scenario. |
| [CS07](ilos/CS07.md) | CS | Iterative Prompting and Refinement | … apply prompt refinement techniques and evaluate outputs iteratively in order to improve alignment between generated content and intended outcomes. |
<!-- END GENERATED -->

Full wording is in `ilos.yaml`; each ID above links to the ILO's own page.

## Identifiers and links

- **Ids are permanent.** `<AREA><NN>` (`H01`, `MM01`, `EPR01`, `CS01` …) is an opaque label, not a rank: an id is never renumbered or reused. A new ILO takes the next free number in its area; a split adds a letter suffix (as `CS04a`/`CS04b`); a retired ILO keeps its id and gains `status: retired` in `ilos.yaml`.
- **Links use only the id.** The stable URL for an ILO is  
  `https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/<ID>.md`  
  (e.g. [MM01](ilos/MM01.md)). Wording, topic and sub-area may change; the path does not.
- **Edit `ilos.yaml`, then run `scripts/build-pages.py`.** It regenerates `ilos/*.md`, `areas/*.md` and the index above, and (when `../learning-activities` is checked out) lists on each ILO page the activities that address it. `--check` reports stale files or malformed ids.

## Source and extraction notes

Extracted from `wg11-ilos.pdf` (*Appendix. Full list of intended learning outcomes*, 3 pages). Wording is reproduced verbatim, with these deliberate exceptions:

- **CS04a / CS04b** — the source shows a single combined row labelled "CS04a + CS04b" with two statements; they are listed here as two separate ILOs sharing the same topic.
- **Section heading typo** — "GenA**U** in Social, Professional, and Regulatory Contexts" corrected to "GenA**I**".
- **H01** — "experienced period of rapid advancement" → "periods".
- **CS04a** — "reviewGenAI" (missing space in the PDF text) → "review GenAI".
- **EPR08 / EPR09** — inconsistent ellipsis formatting ("…explain", "…. analyze") normalised.
- Ligatures (e.g. "reﬁnement") normalised to plain ASCII.

Items the working group may wish to look at (left as in the source):

- **EPR01** is the only ILO whose verb is *understand*, which is not directly observable/assessable; the other outcomes use Bloom-style verbs (identify, explain, evaluate, …).
- **MM01/MM03/MM05** share the topic label "How GenAI works" and **MM04/MM06** share "GenAI applications, use cases and user attitudes"; the Mental Models area has no explicit sub-area headings, unlike EPR and CS.
- Spelling mixes UK and US conventions (recognising / recognize, summarisation / analyze).
