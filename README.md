# Generative LLMs in Education

### Members: Arya Kumar, Krish Garg

## Abstract

As generative AI continues to integrate into digital learning environments, questions have emerged about how effectively online information sources—particularly Wikipedia—support meaningful learning. While Wikipedia is widely used by students, the educational quality of its articles varies significantly. This project investigates how large language models (LLMs) can be trained to evaluate and classify Wikipedia articles based on their pedagogical value. Drawing from research on instructional design, text coherence, and cognitive load theory, the first phase examines which linguistic and structural features make educational materials effective for learning. The second phase applies these insights to train an LLM that diagnoses whether a given Wikipedia article facilitates understanding or promotes misconceptions. Using the Wikipedia API and OpenAI’s Apps SDK, the system will allow real-time interaction between Wikipedia content and ChatGPT, enabling dynamic analysis and feedback on article quality. By combining educational theory with AI-driven analysis, this project aims to create a tool that not only identifies high-quality learning resources but also informs how AI can enhance open-access educational ecosystems.

## [Literature Review](https://github.com/arya-kumar1/Generative-LLMs-in-Education/blob/d2a163c46c2a645ca2f7730caebeec6aa2937281/literature-review.md)



## Research Questions

Which textual and structural characteristics make Wikipedia articles effective for learning according to established educational psychology research?

Can an LLM be trained to accurately diagnose the quality of a Wikipedia article using these characteristics?

How does the model’s assessment compare to human expert judgments of article quality?

What are the broader implications for AI-assisted learning and the reliability of open educational resources?

## Methodology

##### Track A – Investigating AI Use vs. Critical Thinking

Literature Review: Conduct a systematic review of studies on instructional text design, including coherence, scaffolding, conceptual density, and explanatory depth.

Data Extraction: Compile a labeled dataset of Wikipedia articles rated for educational quality by prior research or expert evaluators.

Feature Analysis: Identify linguistic and structural variables (e.g., readability, hierarchical structure, example density) correlated with effective learning outcomes.

##### Track B – Developing the CoT-LLM Tutor

Design: Configure a model that connects to the Wikipedia API via the OpenAI Apps SDK to fetch article content dynamically.

Implementation: Use prompt engineering and fine-tuning to train the model on annotated examples, teaching it to classify articles as educationally effective, neutral, or ineffective.

Evaluation:

Automated metrics: Compare model outputs against expert-labeled datasets using accuracy, precision, and F1 scores.

Human review: Expert educators will qualitatively assess a subset of model predictions for validity and reasoning clarity.

Iterative refinement: Adjust prompts and fine-tuning parameters based on performance feedback.

##### Integration

Combine insights from Track A’s educational text analysis with Track B’s LLM outputs to produce interpretable explanations for why an article is or isn’t effective for learning.

##### Deliverables

Comprehensive report summarizing the linguistic and educational features that define high-quality instructional writing.

Functional prototype of the Wiki Diagnostic LLM connected to the Wikipedia API via Apps SDK.

## test_wikipedia_api.py Function
To run:
1. python -m venv .venv
2. source .venv/bin/activate
3. python -m pip install requests
4. python wiki_summarizer.py

## Research Question Week 7

What aspects of Wikipedia articles specifically categorize them as a reliable source of learning?



