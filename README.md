# Intended Learning Outcomes

Intended learning outcomes (ILOs) for **generative AI literacy for computing students in higher education**, developed and validated by ITiCSE 2026 Working Group 11.

Every outcome completes the stem:

> **At the end of the course, students should be able to …**

## Contents

| File | What it is |
|------|------------|
| [`ilos.yaml`](ilos.yaml) | Canonical, machine-readable list of all ILOs (id, area, sub-area, topic, statement). Edit this first; the markdown files are the human-readable view. |
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

| ID | Topic | Outcome (abridged) |
|----|-------|--------------------|
| H01 | History | identify key milestones in AI history and explain AI booms/winters |
| H02 | History | distinguish earlier AI applications from GenAI |
| MM01 | How GenAI works | explain output generation as simplified next-token prediction |
| MM02 | How models are trained | explain the development pipeline (data, pre-training, alignment) and its limitations |
| MM03 | How GenAI works | evaluate technical, ethical and practical limitations of GenAI |
| MM04 | Applications & use cases | identify GenAI use cases while recognising occasional mistakes |
| MM05 | How GenAI works | analyze misconceptions vs. actual capabilities |
| MM06 | Applications & use cases | evaluate whether GenAI is appropriate for a scenario |
| MM07 | Explainability | articulate what XAI means and how it affects trust |
| MM08 | Explainability | discuss limits of explainability and strategies to assess responses |
| EPR01 | Resources and Labor | understand the origins of resources needed for large-scale AI |
| EPR02 | Input Data, Bias | identify training data sources and how quality/consent/representation shape behaviour |
| EPR03 | Data Control | evaluate data management risks: misuse, manipulation, data sovereignty |
| EPR04 | Output Data | explain output shortcomings and the need to follow policies/regulations |
| EPR05 | Model Limitations | recognize output limitations (hallucination, misinformation, leakage, harm) in societal context |
| EPR06 | Measures of Efficacy | differentiate reliable, trustworthy and responsible GenAI systems |
| EPR07 | Alignment Practices | identify and apply tools/procedures for verifying model outputs |
| EPR08 | Cognitive Debt | explain how overreliance leads to cognitive debt |
| EPR09 | Labor and Automation | analyze effects of GenAI automation on labor and the labor market |
| EPR10 | Evaluating AI Use | evaluate GenAI (use) against normative principles |
| EPR11 | Responsible Use | design a plan for responsible, context-appropriate use incl. documentation |
| EPR12 | AI Policy | identify and interpret relevant GenAI policies |
| EPR13 | Societal Influences | discuss societal perceptions, expectations and power dynamics |
| EPR14 | Discipline-Specific Norms | discuss frameworks for fair and responsible use in the student's discipline |
| CS01 | Types of models | distinguish types of GenAI systems and select one for a context |
| CS02 | Core Concepts | explain tokens, context windows, probability, non-determinism and use them to interpret behaviour |
| CS03 | Open source vs proprietary | compare open-source and proprietary models for a context |
| CS04a | Verification | demonstrate the need to verify and review GenAI outputs before integration |
| CS04b | Verification | explain limits of verification due to non-determinism and opacity |
| CS05 | Plan vs. Code | decompose problems and allocate subtasks to humans or GenAI |
| CS06 | Workflows | distinguish levels of oversight/automation in AI-supported development and select a workflow |
| CS07 | Iterative Prompting | apply prompt refinement and evaluate outputs iteratively |

Full wording is in `ilos.yaml` and the `areas/` files.

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
