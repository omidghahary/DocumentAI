Project Title:
# DocumentAI

Tagline:
AI-powered modular document intelligence pipeline.

Project Overview:
DocumentAI is a modular document intelligence pipeline designed to transform raw documents into high-quality AI-ready knowledge.
The project combines document preprocessing, OCR, chunking, context engineering, prompt engineering, and local Large Language Model (LLM) integration into a clean, extensible architecture.
Instead of treating OCR, prompting, and LLM interaction as isolated components, DocumentAI organizes them into a structured processing pipeline where every stage has a single responsibility and can be independently tested, replaced, or extended.
The primary objective of this project is to provide a production-oriented foundation for AI-powered document analysis while demonstrating modern software architecture, clean code practices, automated testing, and modular design.


## Features

### 📄 Document Processing

- Image extraction from document pages
- OCR-based text extraction
- Modular document chunking pipeline

### 🧠 Context Engineering

- Context Builder abstraction
- Context generation from document chunks
- Immutable context model

### ✍️ Prompt Engineering

- Prompt Builder abstraction
- Prompt Model
- Prompt Formatter for LLM providers

### 🤖 LLM Integration

- Local LLM integration using Ollama
- Provider-independent LLM interface
- Structured LLM response model

### 🏗️ Software Architecture

- Modular pipeline architecture
- Dependency injection across components
- Replaceable implementations through abstract interfaces
- Strong separation of responsibilities

### ✅ Quality Assurance

- Extensive unit test coverage
- Version-driven development
- Roadmap-driven architecture evolution


## Architecture

DocumentAI is designed as a modular processing pipeline where every stage has a single responsibility and communicates through well-defined abstractions.

The system follows a layered architecture that makes each component independently testable, replaceable, and easy to extend without affecting the rest of the pipeline.

### Processing Flow

```mermaid
flowchart TD
    A[Document] --> B[Image Extraction]
    B --> C[OCR]
    C --> D[Chunking]
    D --> E[Context Builder]
    E --> F[Prompt Builder]
    F --> G[Prompt Formatter]
    G --> H[Local LLM]
    H --> I[Pipeline Result]
```

### Software Architecture

```mermaid
classDiagram
    BaseImageExtractor <|-- PyMuPDFImageExtractor
    BaseDocumentOCR <|-- EasyOCR
    BaseChunker <|-- SimpleChunker
    BaseContextBuilder <|-- SimpleContextBuilder
    BasePromptBuilder <|-- SimplePromptBuilder
    BasePromptFormatter <|-- SimplePromptFormatter
    BaseLLM <|-- OllamaLLM
```

The processing pipeline depends only on abstract interfaces rather than concrete implementations. This design enables components to be replaced, extended, or tested independently while keeping the overall architecture stable.

