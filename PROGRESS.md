# Learning progress

Last updated: 2026-10-20  
Current stage: 1 — RAG foundations  
Current assignment: [Lesson 01](lessons/01-rag-basics.md)  
Learning lessons completed: 0  
Pace: provisional, about 5 hours/week; weekly availability not yet confirmed.

## Lesson 01 当前进度（2026-10-20）

| 部分 | 状态 | 评审依据／下一步 |
| --- | --- | --- |
| A1–A4：依据资料回答 | 技术检查通过 | 来源选择、完整回答与证据不足判断已检查；英文修正见课程模块 4。 |
| B：错误原因解释 | 概念检查通过 | 已提交七点中文分析，覆盖分块、版本冲突、元数据、提示词、上下文、引用与模型理解。 |
| B：个人解释与流程图 | 技术检查通过 | 已检查新增英文解释与箭头流程；职责、检索后生成的顺序及误读证据风险正确。合并后的作答与技术评审见课程模块 2.3，开发问题和英语修正分别见模块 3、4。 |
| C：三种失败场景 | 需修订 | 已评审修订答案：C1/C2 诊断通过；C3 仍需区分资料缺失与检索失败。已在收到修订后公布参考答案，具体排查／改进动作待补全。 |

**本课状态：学习中。** A、B 的技术检查已通过；C 已提交但需修订。本课仅保留 A、B、C，练习 D 已取消。

**下一步：** 修正 C3，并补全具体排查／改进动作；通过后进入 Python 关键词检索基线练习。后续练习先评审与提示，收到学习者修订后再公布参考答案。详细证据见 [Lesson 01](lessons/01-rag-basics.md)。

## Milestones

| Stage | Status | Evidence | Next action |
| --- | --- | --- | --- |
| 1. Foundations and baseline | In progress | [Lesson 01 notes](lessons/01-rag-basics.md) | A and B passed the technical check. Revise C; Exercise D was removed at the learner’s request. |
| 2. Ingestion and chunking | Not started | — | Finish Stage 1 checkpoint. |
| 3. Dense retrieval | Not started | — | Finish Stage 2 checkpoint. |
| 4. Grounded generation | Not started | — | Finish Stage 3 checkpoint. |
| 5. Evaluation | Not started | — | Finish Stage 4 checkpoint. |
| 6. Retrieval improvements | Not started | — | Finish Stage 5 checkpoint. |
| 7. Reliability | Not started | — | Finish Stage 6 checkpoint. |
| 8. Capstone | Not started | — | Finish Stage 7 checkpoint. |

Status vocabulary: Not started / In progress / Needs revision / Blocked / Complete.
Evidence should link to code, notes, output, or a reviewed explanation. Do not count planned work as completed work.

## Session log

历史记录保留当时的课程安排；练习 D 现已取消，不再是待办或完成条件。

### 2026-10-19 — Learning setup

- Learner confirmed comfort building Python projects.
- Created an eight-stage learning plan, first assignment, and English practice notes.
- Study time is provisional; no technical exercise has been submitted or reviewed.
- Next: submit Lesson 01 answers A-D in English.

### 2026-10-20 — Lesson 01 started

- Teaching and technical explanations use Chinese, starting with the current lesson; everyday communication and learner answers use English.
- Lessons are saved as Markdown files with exercises, answers, and review records.
- Saved the Chinese Lesson 01 and blank answer sections. No exercise answers have been submitted or assessed.
- Next: submit Exercise A1; lesson completion remains 0.

### 2026-10-20 — First review of Lesson 01

- Reviewed learner answers A1–A4 and the draft explanation/pipeline in B. Original answers are preserved in the lesson file.
- A3 and A4 passed the technical check. A1 omitted the order-number requirement; A2 omitted the start of the delivery estimate.
- B needs revision: correct retrieval can still be followed by unsupported generation; keyword extraction is not mandatory in every RAG pipeline.
- Added Chinese feedback and English correction examples, with blank sections for independent revisions.
- C and D remain unanswered. Teacher examples do not count as learner revisions; completed lessons remain 0.
- Next: revise A1, A2, and B, then attempt C and D.

### 2026-10-20 — Reference answers filled on request

- Filled the English reference answers for revised A1/A2, B, C, and D while preserving learner originals and review notes.
- D uses the synthetic Northstar policy assistant as an example; the learner has not confirmed this topic.
- Next: review the examples, explain retrieval failure versus generation failure versus missing evidence, and confirm or change the topic.
- Reference answers are supplied, but independent understanding has not been checked; completed lessons remain 0.

### 2026-10-20 — Second review of latest Lesson 01 file

- Reviewed new learner revisions for A1/A2 and the notes stored in an HTML comment. All original learner text was preserved.
- A1/A2 now include the required information; all A answers pass the technical check. Added spelling, punctuation, and missing-verb corrections.
- Added visible corrected notes and clarified that generation must use retrieved evidence and citations require claim-level support checks.
- The latest lesson file does not contain the previously supplied filled reference-answer sections; B revision slots and C/D remain blank in this version. Current progress follows the file actually reviewed.
- Next: revise B, including why correct retrieval can still lead to a wrong answer, and complete C/D. Completed lessons remain 0.

### 2026-10-20 — B failure explanation reviewed

- Recorded the learner’s seven-point Chinese explanation of RAG failures and stage-specific feedback.
- The concept check for why correct evidence can still lead to an incorrect answer passed. Clarified chunking versus retrieval, version applicability, context omission versus underuse, and citation limitations.
- Added an assistant-written English rendering, distinguished from the learner’s original answer.
- The learner’s pipeline and exercises C/D remain pending; completed lessons remain 0.

### 2026-10-20 — B English explanation and pipeline reviewed

- Reviewed the learner's new English explanation and pipeline stored in HTML comments; preserved the original text.
- B passed the technical check: component responsibilities, retrieval followed by generation, and the possibility of misinterpreting correct evidence are understood.
- Added an assistant-edited English version, a fuller pipeline example, and focused grammar corrections. Clarified retrieving chunks from a corpus and checking claims against sources.
- Next: complete C and D. Completed lessons remain 0.

### 2026-10-20 — C first submission reviewed

- Reviewed all three newly submitted C answers and preserved learner originals.
- Clarified retrieval failure, generation error, and missing evidence; distinguished stored documents, retrieval results, and the actual model input.
- C needs revision: identify each failure type and give a concrete investigation or improvement action.
- Reviewed the new B wording about too many chunks: this is a possible risk, not a sufficient explanation by itself. Earlier B concept checks remain passed.
- Next: revise C, then complete D. Completed lessons remain 0.

### 2026-10-20 — Exercise D removed

- Removed the project-topic exercise at the learner’s request. Lesson 01 now requires only A, B, and C.
- A and B remain passed. C still needs revision; removing D does not mark C or the lesson complete.
- Next: revise C, then proceed to the Python keyword-retrieval baseline after review.

### 2026-10-20 — Revised C answers and feedback order

- Reviewed the learner's three revised C diagnoses. C1 and C2 now pass the diagnosis check; C3 still confuses missing evidence with retrieval failure.
- Published a reference comparison after receiving the learner's revision. Concrete investigation or improvement actions remain incomplete, so C and the lesson are not marked complete.
- Saved the requested teaching sequence: initial answer, review and hints, learner revision, then reference answers. Do not reveal reference answers during the initial review of future exercises.
- Next: revise C3 and supply concrete actions.

### 2026-10-20 — Lesson reorganized into four modules

- Reorganized Lesson 01 into lesson knowledge; exercises, reviews, revisions and published answers; development precautions and direct Q&A; English supplements.
- Preserved learner answer wording, including text formerly hidden in HTML comments, and consolidated repeated technical reviews and outdated status summaries.
- Recorded the four-module format for future lessons. A/B remain passed; C needs revision; completed lessons remain 0.

### Template for the next session

- Date:
- Lesson/stage:
- What I attempted:
- Artifact or commit:
- Result and failure observed:
- My explanation:
- Review outcome:
- English correction:
- Next action:

## How to request an update

Say: "I completed Lesson 01. Here are my answers..." or "I am stuck on..."
Share the actual work or results. During that chat, the coach can review the evidence and update this file. Repository updates are made when we work together; progress is not inferred from elapsed time.
