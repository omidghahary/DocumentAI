# DocumentAI — Project Checkpoint & Roadmap

**Checkpoint:** Retrieval milestone / post-v0.12.0  
**Purpose:** Portable context for continuing the project in a new chat  
**Repository:** `E:\AI-Projects\DocumentAI`  
**Latest official tag:** `v0.12.0`  
**Current state:** All tests green after the latest Retrieval integration work.

---

## 1. Project Goal

DocumentAI is being developed as a modular document-processing and Retrieval pipeline.

The project direction is intentionally incremental:

- implement the smallest useful capability;
- write focused tests for the main behavior;
- keep the architecture modular;
- commit/tag at meaningful milestones;
- avoid overengineering and unnecessary abstractions;
- progressively move from basic Retrieval toward more intelligent Retrieval and multi-document reasoning.

A key working rule is:

> Test important behavior, not every conceivable implementation detail.

After a feature's main behavior is verified and the test suite is green, move forward unless there is a meaningful boundary or regression risk.

---

# 2. Current Architecture

Current high-level flow:

```text
Document
   ↓
Document Processing / OCR
   ↓
Chunker
   ↓
TextTokenizer
   ↓
Chunk Scorer
   ├── SimpleChunkScorer
   ├── KeywordChunkScorer
   └── TfIdfChunkScorer
   ↓
ScoredChunkModel
   ↓
Chunk Selector
   ├── SimpleChunkSelector
   └── TopScoreChunkSelector
          ├── min_score
          └── max_chunks
   ↓
Document Pipeline
   ↓
Context Builder
   ↓
Prompt / LLM layers
```

The exact downstream ContextBuilder/Prompt architecture exists in the project and should not be unnecessarily redesigned while implementing the next Retrieval milestones.

---

# 3. Retrieval Components Completed

## 3.1 TextTokenizer

A dedicated tokenizer was introduced so tokenization behavior is not duplicated inside individual scorers.

Current responsibilities include:

- removing punctuation;
- converting text to lowercase;
- splitting into tokens;
- handling punctuation attached to tokens.

This component was introduced after tests exposed problems with punctuation and version-like strings such as `3.11.9`.

The tokenizer is now reused by Retrieval scorers.

---

## 3.2 SimpleChunkScorer

Baseline scorer retained for simple/default behavior.

---

## 3.3 KeywordChunkScorer

Keyword-based scoring is implemented.

Current conceptual behavior:

```text
query
  ↓
TextTokenizer
  ↓
unique keywords
  ↓
compare against chunk tokens
  ↓
keyword occurrence score
```

Important design decision:

- duplicate query keywords are treated as unique keywords;
- punctuation is normalized through `TextTokenizer`;
- scoring is token-based rather than naïve substring matching.

---

## 3.4 TfIdfChunkScorer

TF-IDF scoring has been implemented and tested.

A meaningful Integration Test now verifies:

```text
TfIdfChunkScorer
      ↓
ScoredChunkModel
      ↓
TopScoreChunkSelector
      ↓
most relevant chunk
```

The test confirms that a more specific/relevant chunk can rank above less relevant chunks.

This is the current main Information Retrieval mechanism beyond simple keyword matching.

---

# 4. ScoredChunkModel

Scoring is separated from the original Chunk model.

Conceptually:

```python
ScoredChunkModel(
    chunk=ChunkModel(...),
    score=float(...)
)
```

This distinction is important.

Selectors return `ScoredChunkModel` objects, not bare `ChunkModel` objects.

When writing integration assertions, compare the underlying chunk when appropriate:

```python
selected_chunks[0].chunk == expected_chunk
```

rather than:

```python
selected_chunks[0] == expected_chunk
```

---

# 5. Chunk Selectors

## 5.1 SimpleChunkSelector

Baseline selector.

## 5.2 TopScoreChunkSelector

Current behavior:

```text
Scored Chunks
      ↓
min_score filtering
      ↓
sort descending by score
      ↓
max_chunks
      ↓
selected chunks
```

Threshold condition:

```python
score >= min_score
```

Default:

```python
min_score = 0.0
```

Important: `min_score` filtering occurs **before** `max_chunks`.

Example:

```text
scores = [10, 8, 2, 1]
min_score = 5
max_chunks = 2
```

Result:

```text
[10, 8]
```

---

# 6. Retrieval Configuration

`core/config.py` contains configuration dataclasses including:

- `OCRConfig`
- `LLMConfig`
- `RetrievalConfig`

`RetrievalConfig` now supports the Retrieval strategy configuration:

```text
chunk_scorer
chunk_selector
max_chunks
min_score
```

The important architectural goal is that the Pipeline does not hard-code which Retrieval implementation must be used.

---

# 7. PipelineFactory

`PipelineFactory` is responsible for constructing the configured Retrieval components.

Current conceptual mapping:

```text
chunk_scorer:
    "simple"  → SimpleChunkScorer
    "keyword" → KeywordChunkScorer
    "tfidf"   → TfIdfChunkScorer

chunk_selector:
    "simple"    → SimpleChunkSelector
    "top_score" → TopScoreChunkSelector
```

For `top_score`, configuration is passed through:

```python
TopScoreChunkSelector(
    max_chunks=config.max_chunks,
    min_score=config.min_score,
)
```

Invalid configuration values should not silently select an unrelated implementation.

---

# 8. Retrieval Integration Already Verified

The following behaviors have been verified with focused tests:

### Keyword + TopScore

```text
KeywordChunkScorer
        ↓
TopScoreChunkSelector
```

### Keyword + Threshold

```text
KeywordChunkScorer
        ↓
min_score
        ↓
TopScoreChunkSelector
```

### Keyword + Threshold + max_chunks

Verified.

### TF-IDF + TopScore

Verified through an Integration Test.

The current Retrieval path therefore supports:

```text
Query
  ↓
Tokenization
  ↓
Scoring
  ↓
Ranking
  ↓
Threshold
  ↓
Top-K
```

---

# 9. Testing Philosophy

The project previously spent significant time adding many small tests around Retrieval behavior.

This has now been deliberately corrected.

Current rule:

> Write enough tests to establish the important behavior and protect against meaningful regressions, then move to the next feature.

Do NOT continue adding tests for every theoretical combination when the core behavior is already covered.

Current state:

```text
All tests green
```

At the latest point, the project had **121+ tests**, plus the newer Retrieval tests added afterward.

The exact current count should be obtained by running `pytest`; do not assume a fixed number if the suite has changed.

---

# 10. Git / Versioning Status

Latest official tag:

```text
v0.12.0
```

Several Retrieval improvements have been committed after that tag.

The latest work includes:

- configurable Retrieval scorer;
- configurable selector;
- TextTokenizer;
- TF-IDF Retrieval integration;
- TopScore threshold;
- Retrieval integration tests.

The latest Integration commit has been committed successfully.

Do not create a new tag automatically.

A new tag should be created only when a meaningful milestone is completed.

---

# 11. Roadmap

The original roadmap/checkpoint identified the remaining important Retrieval/document-intelligence work.

## Completed / substantially completed

```text
✓ Chunk processing foundation
✓ TextTokenizer
✓ Simple scoring
✓ Keyword scoring
✓ TF-IDF scoring
✓ ScoredChunkModel
✓ Simple selector
✓ TopScore selector
✓ max_chunks
✓ min_score
✓ RetrievalConfig
✓ PipelineFactory
✓ Configurable scorer
✓ Configurable selector
✓ Keyword Retrieval integration
✓ TF-IDF Retrieval integration
```

The **Better Chunk Selection / basic intelligent Retrieval** portion is now sufficiently mature for the next architectural step.

---

# 12. NEXT STEP — Multi-document Reasoning

This is the next planned feature.

Do NOT immediately jump to Embeddings, Vector DB, FAISS, Rerankers, or Hybrid Retrieval.

First implement a minimal, clean Multi-document Retrieval capability using the components already built.

Target concept:

```text
Document A ─┐
Document B ─┼──→ Chunks
Document C ─┘
              ↓
         Retrieval
              ↓
      Relevant Chunks
              ↓
        ContextBuilder
              ↓
             LLM
```

The first implementation should focus on:

1. allowing Retrieval to operate over chunks originating from multiple documents;
2. preserving document/chunk identity;
3. reusing the existing Scorers;
4. reusing the existing Selectors;
5. avoiding a new abstraction unless it is actually required;
6. adding one focused Integration Test for the main Multi-document behavior.

The first goal is NOT sophisticated multi-document reasoning by the LLM.

The first goal is:

> Retrieve the relevant chunks across multiple documents and preserve enough provenance to build a correct combined context.

---

# 13. After Multi-document Retrieval

Next planned area:

## Persian Optimization

Focus areas should be practical and evidence-driven, such as:

- Persian tokenization;
- Persian punctuation;
- Arabic/Persian character normalization;
- mixed Persian/English text;
- Retrieval quality for Persian queries/documents.

Do not prematurely build a complex Persian NLP stack.

---

# 14. Later / Advanced Retrieval

Only after the above stages are stable:

```text
Multi-document Retrieval
        ↓
Persian Optimization
        ↓
Semantic / Embedding Retrieval
        ↓
Hybrid Retrieval
        ↓
(optional) Reranking
```

Potential future technologies:

- embeddings;
- vector index/database;
- semantic similarity;
- hybrid lexical + semantic Retrieval;
- reranking.

These are explicitly deferred to avoid premature complexity.

---

# 15. Important Design Constraints

Maintain these principles throughout the next phases:

### Minimal viable architecture

Do not add infrastructure or abstractions before they are required.

### Reuse existing components

Prefer:

```text
existing Scorer
existing Selector
existing Pipeline
existing ContextBuilder
```

over creating parallel implementations.

### Configuration-driven behavior

Retrieval strategy should remain configurable rather than hard-coded.

### Test the contract

Tests should describe observable behavior, not implementation details.

### Incremental commits

Use:

```text
implement
  ↓
focused test
  ↓
pytest
  ↓
green
  ↓
commit
```

Tag only at meaningful milestones.

---

# 16. Immediate Continuation Instruction

If this checkpoint is pasted into a new chat, continue from:

> **NEXT STEP: Multi-document Retrieval / Multi-document reasoning**

Start by examining the existing document/chunk models and current DocumentPipeline/ContextBuilder interfaces.

Do not redesign the entire architecture.

First identify the smallest change needed to allow multiple documents to participate in the same Retrieval operation.

Then write **one focused test for the main behavior** before implementing the change.

---

# 17. Current Project Principle

The project is intentionally moving from:

```text
Basic document processing
```

toward:

```text
Configurable Retrieval
        ↓
Multi-document Retrieval
        ↓
Persian-aware Retrieval
        ↓
Semantic / Hybrid Retrieval
        ↓
Intelligent DocumentAI
```

The priority is **useful intelligence**, not increasing the number of classes, tests, or abstractions.
