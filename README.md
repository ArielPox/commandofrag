# Command of RAG

A hands-on learning journal for mastering retrieval-augmented generation (RAG), with English practice alongside technical work.

## Start here

1. Read [the learning plan](LEARNING_PLAN.md).
2. Complete [Lesson 01: Trace a RAG answer](lessons/01-rag-basics.md).
3. Share your exercise and explanation in our chat for review.
4. Record reviewed work in [the progress tracker](PROGRESS.md).

## Learning agreement

- Starting level: comfortable building Python projects.
- Suggested pace: 8 weeks, about 5 hours per week; adjust to your schedule. These are learning stages, not deadlines.
- Build one document question-answering project throughout the course.
- Explain decisions in English. The coach answers the technical question and briefly corrects useful grammar and word-choice mistakes.
- Work through one lesson at a time. Attempt the exercise before requesting a complete solution.
- Completion requires an artifact, an explanation, and review. Creating this plan does not count as completing a lesson.
- Updates happen during our chats when work is shared or reviewed; there is no automatic monitoring.

## Project goal

Build a document assistant that retrieves useful passages, answers with verifiable source references, recognizes insufficient evidence, and has a reproducible evaluation report.

Start with Python, Markdown/text documents, a keyword baseline, and an in-memory dense search implementation. Add persistence, reranking, and an interface only as the project needs them. Select specific models and providers when you reach those lessons, based on hardware, budget, language, and current documentation.

## Repository guide

- [LEARNING_PLAN.md](LEARNING_PLAN.md): milestones, exercises, and readiness checks.
- [PROGRESS.md](PROGRESS.md): current status, evidence, and session notes.
- [lessons/01-rag-basics.md](lessons/01-rag-basics.md): your first assignment.
- [ENGLISH_PRACTICE.md](ENGLISH_PRACTICE.md): corrections and a short writing routine.

Later, add `src/`, `tests/`, `data/sample/`, `eval/`, and `experiments/` as you build them. Use public or synthetic documents in this public repository. Keep credentials in environment variables and exclude secrets and private datasets from Git.
# commandofrag
