# DocumentAI Roadmap

1. Vision

2. Mission

3. Core Principles

4. Current Status

5. Development Phases

6. Version Roadmap

7. Future Research

8. Out of Scope


Every release must deliver a meaningful improvement in document intelligence, not just additional functionality.


## 1. Vision

To become an enterprise AI assistant that understands, analyzes, and reasons over organizational documents.

## 2. Mission

Help organizations transform unstructured documents into reliable, explainable, and actionable knowledge using artificial intelligence.

## 3. Core Principles

- Accuracy over speed
- Intelligence over automation
- Modular architecture
- Testability by design
- Local-first deployment
- Enterprise-ready scalability

## 4. Current Status

Current milestone:

✔ Modular architecture

✔ Pipeline implementation

✔ OCR integration

✔ Local LLM integration (Ollama)

✔ Test-driven development

✔ Architecture documentation

The project now has a stable software foundation and has entered the AI capability development stage.

The current focus is improving document Retrieval, context construction,
and reasoning quality.

## 5. Development Phases

### Phase 1 — Foundation ✅

Goal

Build a stable, modular, and testable software foundation.

Completed

- Core data models
- OCR
- Image extraction
- Chunking
- Prompt generation
- Local LLM integration
- Processing pipeline
- Architecture documentation

---

### Phase 2 — Building Intelligence 🔄

Goal

Improve the quality of AI reasoning over documents by improving
context construction and document Retrieval.

Completed

* Context Builder foundation
* Prompt Engineering foundation
* TextTokenizer
* Configurable chunk scoring
* Keyword-based Retrieval
* TF-IDF Retrieval
* Configurable chunk selection
* Top-score selection
* Minimum score threshold
* Top-K selection
* Retrieval configuration through RetrievalConfig
* Retrieval component construction through PipelineFactory

Next

* Multi-document Retrieval and reasoning
* Persian-aware Retrieval optimization

Future

* Semantic Retrieval
* Hybrid Retrieval
* Retrieval quality evaluation

The project should not move to the next phase before the goals of
the current phase have been completed.

### Phase 3 — Knowledge Integration

Goal

Enable the assistant to combine user documents with external knowledge.

Main topics

- Knowledge Base
- RAG
- Vector database
- Semantic retrieval
- Citation support
The project should never move to the next phase before the goals of the current phase have been completed.
---

### Phase 4 — Enterprise Platform

Goal

Transform DocumentAI into an enterprise-ready platform.

Main topics

- GUI
- API
- Authentication
- User management
- Background processing
- Monitoring
- Deployment

## 6. Version Roadmap

---

Every version is organized around one primary objective.
Additional features may be implemented only if they directly support that objective.

### v0.12 — Configurable Retrieval

Primary Goal

Introduce configurable and testable document Retrieval.

Completed

* TextTokenizer
* KeywordChunkScorer
* TfIdfChunkScorer
* ScoredChunkModel
* SimpleChunkSelector
* TopScoreChunkSelector
* `min_score` threshold
* `max_chunks` top-K selection
* RetrievalConfig
* PipelineFactory integration
* Keyword Retrieval integration
* TF-IDF Retrieval integration

Definition of Done

The system can score document chunks using configurable Retrieval
strategies and select relevant chunks using configurable ranking,
threshold, and top-K policies.

### Next Milestone — Multi-document Retrieval

Primary Goal

Enable Retrieval across multiple documents while preserving
document and chunk provenance.

Key Deliverables

* Multi-document chunk collection
* Document-aware Retrieval
* Provenance preservation
* Retrieval across multiple documents
* Integration with ContextBuilder

Definition of Done

The system can retrieve relevant chunks from multiple documents
and construct a combined context while preserving the source
document of each selected chunk.

### v0.8 — Context Intelligence

Primary Goal

Introduce intelligent context construction for document analysis.

Key Deliverables

- Context Builder
- Context selection strategy
- Multi-chunk context generation
- Token-aware context construction

Definition of Done

The system is able to intelligently construct optimized context from multiple document chunks before prompt generation.

---

### v0.9 — Prompt Intelligence

Primary Goal

Improve reasoning quality through advanced prompt engineering.

Key Deliverables

- Prompt templates
- Dynamic prompt generation
- Persian prompt optimization
- Prompt evaluation

Definition of Done

Prompt generation becomes configurable, reusable, and optimized for document understanding.

---

### v1.0 — First Product Release

Primary Goal

Deliver the first usable version of DocumentAI.

Key Deliverables

- Desktop GUI
- Multi-document support
- User configuration
- Export results

Definition of Done

Users can analyze one or more documents through a graphical interface without interacting with internal components.

---

### v1.1 — Knowledge Integration

Primary Goal

Enable external knowledge to improve document analysis.

Key Deliverables

- Knowledge Base
- Retrieval-Augmented Generation (RAG)
- Citation support

Definition of Done

The assistant is able to combine user documents with external organizational knowledge.

---

### v1.2 — Enterprise Readiness

Primary Goal

Prepare the platform for enterprise deployment.

Key Deliverables

- Authentication
- User management
- Background jobs
- Monitoring
- Configuration management

Definition of Done

The platform is ready for organizational deployment and long-term maintenance.

