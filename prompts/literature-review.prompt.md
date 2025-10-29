---
type: agent-workflow
version: 1.0
author: Arya Kumar & Krish Garg
created: 2025-10-28
updated: 2025-10-28
description: Automated literature review workflow for Generative LLMs evaluating the educational quality of Wikipedia content.
prerequisites:
  - pdftotext installed (Poppler utils)
  - PDF papers stored in literature/
  - paper/references.bib exists (or will be created)
  - AI agent has file read/write access
---

# Literature Review Agent Workflow

## Overview
This workflow automates a structured literature review for research investigating how **Wikipedia articles support learning** and how **LLMs can evaluate their educational effectiveness**. The agent processes relevant PDFs, extracts metadata and findings connected to our research questions, and maintains both a structured review file and a curated bibliography.

Target research themes:
- Educational psychology influencing instructional text quality (coherence, cognitive load, scaffolding)
- NLP/AI models used for educational assessment or content evaluation
- Research analyzing Wikipedia’s role in learning
- Metrics for text difficulty, clarity, readability, and conceptual structure
- LLM evaluation reliability (alignment with human expert judgments)

## Inputs
- All new PDF files in `literature/`

## Outputs
- Update `literature/literature-review.md` with structured article notes
- Update `paper/references.bib` with minimal valid BibTeX entries

## Relevance Criteria
A paper is **relevant** if ≥1 applies:
1. Studies Wikipedia as an educational source
2. Evaluates instructional text quality or design principles
3. Analyzes readability, structure, or conceptual clarity in educational materials
4. Uses AI/LLMs for educational assessment or feedback generation
5. Provides metrics or insights applicable to Wikipedia article classification

## Article Processing Steps

For each **new** PDF in `literature/`:

### Step 1 — Convert PDF to text
```bash
pdftotext -layout name.pdf name.txt