# Generative LLMs in Education

### Members: Arya Kumar, Krish Garg

## Abstract

As generative AI becomes embedded in higher education, concerns have emerged regarding its influence on students’ critical thinking. Critical thinking, defined as the ability to analyze information, make judgments, and form sound decisions, is a skill valued by universities, employers, and society at large, yet may be undermined by students’ reliance on AI for quick solutions. The first phase of this project investigates the extent to which AI usage affects critical thinking ability in STEM undergraduates, drawing from systematic literature reviews and empirical data collection. If findings confirm that generative AI poses risks to critical thinking development, we propose a targeted intervention: an AI tutor that uses chain-of-thought (CoT) prompting to elicit student self-explanations rather than simply revealing solutions. Prior work suggests that self-explanation fosters deeper cognitive processing, while Socratic dialogue models have shown promise in guiding learning. The second phase of the project will implement and evaluate such a tutor, testing whether adaptive, explanation-driven feedback can offset AI’s negative effects on critical thinking while simultaneously improving learning outcomes. By combining exploration of AI’s educational risks with the design of a potential solution, this project seeks to inform how universities can integrate AI in ways that promote both technical skill acquisition and the cultivation of lifelong critical thinking abilities.

## [Literature Review](https://github.com/arya-kumar1/Generative-LLMs-in-Education/blob/d2a163c46c2a645ca2f7730caebeec6aa2937281/literature-review.md)



## Research Questions

Among college STEM students, does a chain-of-thought LLM that prompts self-explanation result in greater learning gains than a solution-revealing LLM, and can such an approach mitigate the potential decline in critical thinking associated with AI use?

Is it the universities' role to make students better at critical thinking, or simply provide the technical skills needed for their intended career?

If it is the role of the University to help students improve their critical thinking skills, is it also their role to find a solution to the problem of students using generative AI or does that fall on the students to self regulate?

What are the future implications of a deterioration of critical thinking for individual students?

## Methodology

##### Track A – Investigating AI Use vs. Critical Thinking

Literature Review: Conduct a systematic scan of existing studies on how generative AI affects student reasoning, self-explanation, and critical thinking outcomes.

Secondary/Aggregate Data: Use only publicly available or de-identified course-level data (e.g., open benchmarks, published statistics) to look for trends in reasoning-intensive tasks before and after AI adoption.

Analysis: Summarize and synthesize findings to map where AI appears to help or harm critical thinking and under what conditions.

##### Track B – Developing the CoT-LLM Tutor

Design: Define the tutor’s behaviour (step-by-step reasoning visible to students, Socratic prompts before answers).

Implementation: Use prompt engineering and/or fine-tuning on open STEM problem sets with expert solutions to produce CoT-style explanations.

Evaluation:

Automated checks for accuracy of final answers and quality of reasoning steps.

Expert review of a sample of outputs for clarity and pedagogical soundness (using existing staff or public rubrics, no new student testing).

Iteratively refine prompts and data until the tutor meets predefined accuracy and explanation-quality benchmarks.

##### Integration

Use insights from Track A to prioritise which risks the CoT-LLM tutor should address (over-reliance on direct answers, lack of self-reflection).

##### Deliverables

Concise report mapping generative-AI use to critical thinking trends from existing literature and data
Functioning CoT-LLM tutor prototype

## test_wikipedia_api.py Function

