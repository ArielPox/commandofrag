"""Lesson 02 exercise scaffold. Implement the two functions marked TODO.

Run from the repository root:
    python exercises/lesson02_keyword_search.py
Standard library only. Source data is synthetic.
"""

import json
import re
from pathlib import Path


STOP_WORDS = {
    "a", "an", "the", "is", "are", "i", "my", "can", "does",
    "how", "what", "when", "do", "to", "of", "and", "in",
}

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "sample" / "northstar.json"


def tokenize(text):
    """Return unique English/number tokens, with fixed stop words removed."""
    return set(re.findall(r"[a-z0-9]+", text.lower())) - STOP_WORDS


def score_document(query_tokens, document_tokens):
    """Return query-token coverage; return 0.0 for an empty query set."""
    # TODO: implement the scoring rule described in Lesson 02.
    raise NotImplementedError("Implement score_document first.")


def retrieve(query, documents, top_k=3):
    """Return at most top_k positive-score results.

    Validate integer top_k > 0 (integer input is assumed for this lesson).
    Score text only. Break score ties by document id ascending.
    Every result must contain:
        id, source, score, matched_tokens, excerpt
    matched_tokens must be sorted; excerpt is text[:160].
    Do not modify the input documents.
    """
    # TODO: tokenize, score, filter, rank, and construct result records.
    raise NotImplementedError("Implement retrieve after score_document.")


def main():
    documents = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    queries = [
        "Can I return an unused product?",
        "How long does express shipping take?",
        "Does the warranty cover accidental damage?",
    ]
    for query in queries:
        print(json.dumps(
            {"query": query, "results": retrieve(query, documents, top_k=3)},
            ensure_ascii=False,
            indent=2,
        ))


if __name__ == "__main__":
    main()
