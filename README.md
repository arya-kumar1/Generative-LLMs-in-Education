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

The program fetches a summary of the wikipedia article the user is interested in reading. This is the first step as now the user is able to choose which article they are interested in and eventually our program will tell them whether the article they choose is good for learning

## Research Question Week 7
### Question:
How effectively do Wikipedia article summaries communicate educational content that supports student understanding?

### Methodology
Purpose: Evaluate whether the lead summaries returned by the script are clear, accurate, and informative enough to serve as effective learning resources.
Data collection:
	1.	Run wiki_summarizer.py for 5–10 educational topics (e.g., “Neural network,” “Overfitting,” “Photosynthesis”).
	2.	Record each printed summary output.

### Output Rubric:
- Clarity: Is the summary understandable to a non-expert?
- Comprehensiveness: Does it define the concept and mention key ideas or applications?
- Readability: Is the language concise and free of heavy jargon?
- Educational Value Score: Rate each 1–5 and compute an average across topics.

### Running the Program:
1. python -m venv .venv
2. source .venv/bin/activate
3. python -m pip install requests
4. python wiki_summarizer.py

### Results:
1. AI: Artificial intelligence (AI) is the capability of computational systems to perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making. It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals.

Clarity: 5, Comprehensiveness: 5, Readability: 4, Average: 4.7, Category: high

3. ML: Machine learning (ML) is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can learn from data and generalise to unseen data, and thus perform tasks without explicit instructions. Within a subdiscipline in machine learning, advances in the field of deep learning have allowed neural networks, a class of statistical algorithms, to surpass many previous machine learning approaches in performance.

Clarity: 5, Comprehensiveness: 4, Readability: 4, Average: 4.3, Category: high

4. Neural network: A neural network is a group of interconnected units called neurons that send signals to one another. Neurons can be either biological cells or signal pathways. While individual neurons are simple, many of them together in a network can perform complex tasks. There are two main types of neural networks.In neuroscience, a biological neural network is a physical structure found in brains and complex nervous systems – a population of nerve cells connected by synapses.
In machine learning, an artificial neural network is a mathematical model used to approximate nonlinear functions. Artificial neural networks are used to solve artificial intelligence problems.

Clarity: 4, Comprehensiveness: 4, Readability: 3, Average: 3.7, Category: Medium-high

5. Overfitting: In mathematical modeling, overfitting is "the production of an analysis that corresponds too closely or exactly to a particular set of data, and may therefore fail to fit to additional data or predict future observations reliably". An overfitted model is a mathematical model that contains more parameters than can be justified by the data. In the special case of a model that consists of a polynomial function, these parameters represent the degree of a polynomial. The essence of overfitting is to unknowingly extract some of the residual variation as if that variation represents the underlying model structure.

Clarity: 4, Comprehensiveness: 3, Readability: 3, Average: 3.3, Category: Medium

6. Photosynthesis: Photosynthesis is a system of biological processes by which photopigment-bearing autotrophic organisms, such as most plants, algae and cyanobacteria, convert light energy — typically from sunlight — into the chemical energy necessary to fuel their metabolism. The term photosynthesis usually refers to oxygenic photosynthesis, a process that releases oxygen as a byproduct of water splitting. Photosynthetic organisms store the converted chemical energy within the bonds of intracellular organic compounds, typically carbohydrates like sugars, starches, phytoglycogen and cellulose. When needing to use this stored energy, an organism's cells then metabolize the organic compounds through cellular respiration. Photosynthesis plays a critical role in producing and maintaining the oxygen content of the Earth's atmosphere, and it supplies most of the biological energy necessary for complex life on Earth.

Clarity: 5, Comprehensiveness: 5, Readability: 4, Average: 4.7, Category: high


### Interpretation: 
Overall, the Wikipedia REST API summaries retrieved via wiki_summarizer.py are educationally effective for introductory learning:
- Average score across all topics ≈ 4.1/5 → “High learning suitability.”
- Summaries balance conciseness with completeness.
- The clearest summaries use definition + application structures (AI, Photosynthesis).

### Using these Results:
These results serve as a baseline dataset for our project:
- They demonstrate that the lead summaries themselves often reflect educational quality.
- We can now train or prompt an LLM evaluator to analyze future articles using similar criteria (clarity, completeness, readability) automatically.
- This manual scoring provides labeled examples for our next research phase: AI-based classification of article educational quality.
