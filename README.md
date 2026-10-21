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
- 练习按“首次作答 → 评审与提示 → 学习者提交修订 → 公布参考答案并对照评审”的顺序进行。首次评审只指出问题和给出必要提示，不提前公布正确答案；提交修订后才公布。后续新题继续遵守此顺序。
- 课程文档统一使用四个模块：本节课知识；练习、评审、修订与答案公布；注意事项与开发常见问题（直接问答）；英文知识补充。保留学习者原始作答，合并重复评审，当前进度只保留一处。
- Completion requires an artifact, an explanation, and review. Creating this plan does not count as completing a lesson.
- Updates happen during our chats when work is shared or reviewed; there is no automatic monitoring.

## Project goal

Build a document assistant that retrieves useful passages, answers with verifiable source references, recognizes insufficient evidence, and has a reproducible evaluation report.

Start with Python, Markdown/text documents, a keyword baseline, and an in-memory dense search implementation. Add persistence, reranking, and an interface only as the project needs them. Select specific models and providers when you reach those lessons, based on hardware, budget, language, and current documentation.

## Current lesson

- [Lesson 02: Keyword retrieval](lessons/02-keyword-retrieval.md) — started 2026-10-21; Python exercise and corpus linked inside.
- Lesson 01 A/B passed; C remains a warm-up revision.

## Repository guide

- [LEARNING_PLAN.md](LEARNING_PLAN.md): milestones, exercises, and readiness checks.
- [PROGRESS.md](PROGRESS.md): current status, evidence, and session notes.
- [lessons/01-rag-basics.md](lessons/01-rag-basics.md): your first assignment.
- [ENGLISH_PRACTICE.md](ENGLISH_PRACTICE.md): corrections and a short writing routine.

Later, add `src/`, `tests/`, `data/sample/`, `eval/`, and `experiments/` as you build them. Use public or synthetic documents in this public repository. Keep credentials in environment variables and exclude secrets and private datasets from Git.
# commandofrag
