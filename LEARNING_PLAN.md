# RAG learning plan

Created: 2026-10-19  
Starting point: comfortable building Python projects  
Default pace: 5 sessions of about 1 hour per week for 8 weeks (about 40 hours). Adjust as needed; move on when you pass the readiness check.

## What you will be able to do

Explain a RAG pipeline, implement its main components, measure retrieval and answer quality separately, diagnose failures, and justify improvements using evidence.

RAG supplies retrieved information to a language model at answer time. Retrieval can help ground an answer, but it does not guarantee correctness. Begin with a simple pipeline before exploring agentic RAG, graph retrieval, fine-tuning, or complex orchestration.

## How each session works

- 10 minutes: recall the previous lesson and learn one concept.
- 35 minutes: implement or run one focused experiment.
- 10 minutes: inspect results and explain a failure.
- 5 minutes: write a short English summary and record evidence.

For each weekly stage, use five sessions: understand, build, inspect, experiment, and explain/review. Ask the coach for the next lesson after review.

## Roadmap

| Stage | Focus                          | Artifact                                                         | Ready to move on when...                                                                                                   |
| ----- | ------------------------------ | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 1     | RAG foundations and baseline   | Pipeline sketch, small document collection, keyword search       | You can trace one answer and explain retrieval versus generation failures.                                                 |
| 2     | Ingestion and chunking         | Deterministic chunker with source metadata                       | You can compare two chunking strategies and trace each chunk to its source.                                                |
| 3     | Embeddings and dense retrieval | In-memory semantic search with ranked results                    | You can explain cosine similarity and compare dense search with the keyword baseline.                                      |
| 4     | Grounded generation            | End-to-end question answering with source references             | You can demonstrate supported answers, insufficient-evidence responses, and a failure case.                                |
| 5     | Evaluation                     | Reproducible benchmark and baseline report                       | You can measure retrieval separately from answer quality and explain metric limitations.                                   |
| 6     | Retrieval improvements         | Controlled hybrid-search and reranking experiments               | You can show whether each change helps on development questions and verify the chosen configuration on held-out questions. |
| 7     | Reliability and operation      | Persistent index, update handling, safety checks, timing report  | You can restart the app, replace a document without stale chunks, and diagnose errors.                                     |
| 8     | Capstone and explanation       | Runnable assistant, demo, evaluation report, English walkthrough | Someone else can run it and you can defend its design and limitations.                                                     |

## Stage 1: Understand the pipeline and build a baseline

1. Complete [Lesson 01](lessons/01-rag-basics.md): manually retrieve evidence and answer with a source.
2. Choose one narrow topic and collect 10-20 public or synthetic text/Markdown documents. Record their source and reuse conditions.
3. Write down 10 representative questions before optimizing search, including 2 that the corpus cannot answer.
4. Implement a simple keyword-overlap ranking function. Return ranked document IDs, scores, and excerpts.
5. Explain three failures: missing information, retrieval missing existing evidence, and an answer contradicting retrieved evidence.

Deliverables: lesson answers, corpus manifest, initial questions, and a runnable keyword baseline.  
Checkpoint: show top results for three questions and explain why they are relevant or irrelevant. No LLM API is required yet.

## Stage 2: Ingestion, chunks, and metadata

1. Define document and chunk records with stable IDs, source paths, and heading or character-offset metadata.
2. Implement fixed-size chunking and a paragraph/heading-aware alternative. Start with text files; add PDFs later if useful.
3. Compare two chunk sizes and one overlap setting using the same questions.
4. Inspect boundary failures, duplicate passages, empty files, and long sections.
5. Save one experiment table and explain the quality/size tradeoff.

Deliverables: ingestion code, chunk inspection output, and experiment notes.  
Checkpoint: every retrieved chunk maps to an exact source passage. Add focused tests for boundary handling and metadata.

## Stage 3: Embeddings and semantic search

1. Learn vectors, dot products, cosine similarity, and the difference between lexical and semantic matching.
2. Choose a suitable embedding model using current documentation; record its name, version/revision where available, dimensions, language support, and license.
3. Embed chunks and queries, respecting model-specific query/document instructions.
4. Search in memory using NumPy or an equivalent simple implementation. Inspect the top 5 results and their scores.
5. Compare keyword and dense retrieval on identical questions, including paraphrases and exact identifiers.

Deliverables: semantic retriever, reusable embeddings, and a baseline comparison.  
Checkpoint: explain why a high similarity score is not a probability that an answer is correct, and demonstrate a dense-retrieval failure. A vector database is optional at this scale.

## Stage 4: Generate answers grounded in evidence

1. Choose a hosted or local generation model based on budget and hardware; record the choice and configuration.
2. Build context from retrieved chunks within a token budget and include stable source IDs.
3. Prompt the model to answer from the supplied evidence, reference source IDs, and state when evidence is insufficient.
4. Validate that cited IDs exist and manually check that citations support the claims. Valid IDs alone do not establish support.
5. Compare generation with and without retrieval on the same examples. Inspect missing, conflicting, and irrelevant evidence.

Deliverables: end-to-end command-line assistant and examples of supported answers and appropriate abstentions.  
Checkpoint: demonstrate three answerable questions and two unanswerable ones. Explain why prompting cannot guarantee grounding. Set a usage budget before paid API experiments.

## Stage 5: Evaluate before optimizing

1. Expand the question set to 30 questions: 20 answerable and 10 unanswerable, with expected facts and supporting chunk/document references.
2. Split once into a 20-question development set and a 10-question held-out set, keeping both categories represented. Keep near-duplicate questions in the same split.
3. Compute retrieval hit rate@k (at least one gold passage retrieved) and recall@k (fraction of all labeled relevant passages retrieved) on answerable questions. State which metric you report.
4. Manually score answer correctness, evidence support, citation support, and abstention using a written rubric; report the denominators. Automated judging is optional and should be calibrated against manual review.
5. Record corpus version, chunking, model configuration, query timing, and API usage/cost if applicable. Classify failures as ingestion, retrieval, context assembly, or generation.

Deliverables: evaluation dataset, runner, rubric, and baseline report.  
Checkpoint: another run can reproduce the setup and metrics. Treat a small benchmark as diagnostic evidence, not proof of broad quality.

## Stage 6: Improve retrieval with controlled experiments

1. Add a stronger lexical baseline such as BM25.
2. Combine lexical and dense rankings using reciprocal rank fusion.
3. Retrieve more candidates and rerank them with a suitable cross-encoder.
4. Change one factor at a time. Compare development-set retrieval quality, answer quality, and latency; retain the simpler method if improvements are unclear.
5. Freeze your chosen configuration and check it on the held-out set. If you tune after seeing those results, create fresh held-out questions before making a new generalization claim.

Deliverables: experiment table with baseline, hybrid, and reranked configurations, plus your recommendation.  
Checkpoint: explain when exact keyword matching wins, when semantic search wins, and whether reranking earns its added latency.

## Stage 7: Make the system dependable

1. Persist chunks, metadata, embeddings, and configuration. Detect incompatible embedding/index versions.
2. Support adding, updating, and deleting documents without duplicates or stale chunks.
3. Treat retrieved documents as untrusted input. Test a document containing instructions to ignore the user's request or expose secrets.
4. Add clear errors, timeouts/retries where applicable, and logs that help diagnose failures without recording credentials or private data.
5. Measure ingestion time and median/p95 query latency over a stated sample. Check retrieval filters before context assembly if the corpus has access restrictions.

Deliverables: persistent index, lifecycle tests, adversarial examples, and timing/error notes.  
Checkpoint: restart successfully, update one source, delete another, and show correct retrieval after both operations. Describe remaining security limits.

## Stage 8: Finish and teach it back

1. Provide one documented install path and commands for ingestion, asking a question, and evaluation.
2. Add a simple interface only if useful; a command-line app is sufficient.
3. Run the final benchmark with a frozen configuration. Publish limitations and representative failures alongside successes.
4. Create a five-minute English walkthrough: problem, pipeline, evidence, tradeoffs, and next improvements.
5. Rebuild a small pipeline component without copying, then explain what you would change for a larger corpus.

Deliverables: runnable capstone, setup instructions, architecture sketch, experiment report, and walkthrough notes.  
Completion: demonstrate reproducibility and explain at least three design tradeoffs and three remaining failure modes.

## Resources by stage

Read the relevant sections when you need them; do not try to read everything first.

- Stages 1 and 4: [Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401). Start with the abstract and pipeline description; the original training setup is optional.
- Stages 1, 5, and 6: [Stanford, Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/). Focus on ranked retrieval, evaluation, and probabilistic retrieval.


- Stage 3: [Sentence Transformers: Semantic Search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html).
- Stage 6: [Sentence Transformers: Retrieve & Re-Rank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html).

Use current official documentation when selecting packages and model APIs; record versions when implementing each stage.

## Review and progress rules

For each lesson, share your code or written artifact, one result, one failure, and a 3-5 sentence English explanation. The coach reviews correctness, gives a next exercise, corrects a small number of useful language issues, and updates the tracker based on evidence. Mark blocked work with a specific obstacle; mark completion only after the readiness check passes.
