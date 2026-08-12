# DocumentAI Architecture

## 1. Project Overview

DocumentAI is an AI-powered document analysis framework designed to process documents, extract meaningful information, prepare contextual prompts, and use Large Language Models (LLMs) to generate intelligent responses.

The project is designed with a modular architecture where each processing stage is implemented as an independent component. The main objective is to keep the system extensible, testable, and ready for future AI capabilities such as Retrieval-Augmented Generation (RAG), knowledge bases, and multimodal document analysis.

## 2. Main Goal

The primary goal of DocumentAI is to provide a flexible pipeline for intelligent document processing.

The initial version focuses on PDF document analysis:

- Extracting document content
- Extracting images from documents
- Performing OCR
- Splitting content into manageable chunks
- Building prompts for LLMs
- Sending requests to LLM providers
- Returning structured AI-generated responses

Future versions may extend the system to support additional document formats, knowledge bases, and multimodal AI analysis.

## 3. High-Level Architecture

DocumentAI follows a modular pipeline-based architecture.

The system is composed of independent components where each component has a specific responsibility. The DocumentPipeline acts as the main orchestrator and controls the execution flow between different processing stages.

High-level data flow:

User Document
    ↓
DocumentPipeline
    ↓
ImageExtractor
    ↓
OCR
    ↓
Chunker
    ↓
Retrieval Layer
    ↓
ContextBuilder
    ↓
PromptBuilder
    ↓
LLM Provider
    ↓
PipelineResultModel

Each component can be replaced or extended independently without affecting other parts of the system.

## 4. Processing Pipeline

The DocumentAI processing pipeline is responsible for transforming a user document into an AI-generated response.

The pipeline executes a sequence of independent processing stages. Each stage receives a defined input, performs a specific operation, and produces an output that is consumed by the next stage.

Current pipeline flow:

DocumentModel
    ↓
ImageExtractor
    ↓
DocumentModel (with extracted images)
    ↓
OCR Processor
    ↓
DocumentModel (with extracted text)
    ↓
Chunker
    ↓
List[ChunkModel]
    ↓
Retrieval Layer
    ↓
List[ScoredChunkModel]
    ↓
Selected Chunks
    ↓
ContextBuilder
    ↓
List[Prompt]
    ↓
LLM Provider
    ↓
List[LLMResponseModel]
    ↓
PipelineResultModel

## Pipeline Components

### 4.1 Image Extraction

Responsibility:
- Extract embedded images from documents.
- Attach extracted image information to the document model.

Input:
- DocumentModel

Output:
- DocumentModel containing extracted images.


### 4.2 OCR Processing

Responsibility:
- Extract textual content from document pages.
- Support conversion of scanned documents into machine-readable text.

Input:
- DocumentModel

Output:
- DocumentModel containing extracted text.


### 4.3 Document Chunking

Responsibility:
- Split document content into smaller logical units.
- Prepare content for prompt generation and LLM processing.

Input:
- DocumentModel

Output:
- List of ChunkModel objects.

### 4.4 Retrieval

Responsibility:

* Identify the most relevant document chunks for a given query.
* Calculate relevance scores for chunks.
* Select the most relevant scored chunks for context construction.

The Retrieval layer is composed of:

* TextTokenizer
* ChunkScorer
* ScoredChunkModel
* ChunkSelector

Supported chunk scoring strategies:

* SimpleChunkScorer
* KeywordChunkScorer
* TfIdfChunkScorer

Supported chunk selection strategies:

* SimpleChunkSelector
* TopScoreChunkSelector

TopScoreChunkSelector supports:

* `min_score` — minimum score required for a chunk to be selected.
* `max_chunks` — maximum number of chunks that can be selected.

Retrieval behavior is configured through `RetrievalConfig` and constructed by `PipelineFactory`.

Input:

* List of ChunkModel objects
* Query

Output:

* List of selected ScoredChunkModel objects

### 4.5 Prompt Construction

Responsibility:
- Convert selected document chunks into LLM-ready prompts.
- Apply prompt templates and processing instructions.

Input:
- ChunkModel

Output:
- LLM prompt messages.


### 4.6 LLM Processing

Responsibility:
- Send prepared prompts to the configured Large Language Model provider.
- Receive generated responses.

Input:
- LLM prompts

Output:
- LLMResponseModel


### 4.7 Pipeline Result

The final output of the pipeline is a PipelineResultModel containing the processed document information, generated chunks, prompts, and LLM responses.

## 5. Core Components

The system is composed of loosely coupled components. Each component has a single responsibility and communicates with other components only through well-defined interfaces.

Component           | Responsibility
------------------- | ----------------------------------------------------------------------
DocumentPipeline    | Orchestrates the complete document processing workflow.
ImageExtractor      | Extracts embedded images from document pages.
OCR Processor       | Extracts machine-readable text from document pages.
Chunker             | Splits document text into logical chunks.
TextTokenizer       | Normalizes and tokenizes query and chunk text for Retrieval.
ChunkScorer         | Calculates relevance scores for document chunks.
ScoredChunkModel    | Associates a ChunkModel with its calculated relevance score.
ChunkSelector       | Selects relevant scored chunks according to a selection strategy.
RetrievalConfig     | Defines the configured Retrieval scorer, selector, and selection limits.
PipelineFactory     | Constructs the configured Retrieval components.
ContextBuilder      | Builds context from selected document chunks.
PromptBuilder       | Converts selected context into prompts suitable for LLMs.
LLM Provider        | Sends prompts to the configured LLM and receives responses.
PipelineResultModel | Stores the final output of the complete processing pipeline.

### Design Philosophy

Each component is designed around the Single Responsibility Principle (SRP).

Components do not communicate directly with each other.

The DocumentPipeline is the only class responsible for orchestrating the execution order.

This design allows every component to be independently tested, replaced, or extended without affecting the remaining parts of the system.

## 6. External Dependencies

The current implementation relies on a small set of external technologies.

| Dependency              | Purpose                                              |
|-------------------------|------------------------------------------------------|
| PyMuPDF                 | PDF parsing and image extraction.                    |
| Tesseract OCR           | Optical Character Recognition for scanned documents. |
| Ollama                  | Local LLM runtime for AI inference.                  |
| Python Standard Library | Core language features and utilities.                |
| pytest                  | Unit testing framework.                              |
| unittest.mock           | Dependency isolation during testing.                 |

The architecture intentionally isolates these dependencies behind abstraction layers. This allows individual implementations to be replaced without affecting the remaining system.

Examples:

- PyMuPDF may be replaced by another PDF parser.
- Tesseract may be replaced by PaddleOCR or EasyOCR.
- Ollama may be replaced by OpenAI, Azure OpenAI, or another LLM provider.

## 7. Design Principles

The architecture of DocumentAI follows a small set of design principles.

### Single Responsibility Principle

Each component is responsible for only one task.

Examples:

- OCR extracts text.
- Chunker creates chunks.
- TextTokenizer tokenizes Retrieval input.
- ChunkScorer calculates chunk relevance.
- ChunkSelector selects relevant chunks.
- ContextBuilder constructs context from selected chunks.
- PromptBuilder creates prompts.
- LLMProvider communicates with language models.

---

### Loose Coupling

Components communicate only through data models and interfaces.

No component directly depends on the implementation details of another component.

---

### Dependency Injection

External services are injected into the pipeline.

This makes every component replaceable and easy to test.

---

### Testability

Every processing stage should be testable in isolation.

External systems such as OCR engines or LLM providers should always be mocked during unit testing.

---

### Extensibility

The architecture should support future extensions without requiring major refactoring.

Examples include:

- New OCR engines
- Additional LLM providers
- Knowledge bases
- Retrieval-Augmented Generation (RAG)
- Additional document formats
- Multimodal AI processing

---

### Pipeline-Oriented Design

The DocumentPipeline orchestrates the execution order.

Business logic remains inside individual components.

Retrieval strategy and component selection are configured through
RetrievalConfig and constructed by PipelineFactory.

The pipeline should not contain document-processing or Retrieval
business logic itself.


## Summary

DocumentAI is designed as a modular, extensible, and testable AI document processing framework.

The current implementation focuses on PDF document analysis, while the architecture has been prepared for future AI capabilities including RAG, multimodal processing, and additional document sources.
