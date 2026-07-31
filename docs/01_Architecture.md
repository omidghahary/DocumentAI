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
      |
      v
DocumentPipeline
      |
      v
ImageExtractor
      |
      v
OCR
      |
      v
Chunker
      |
      v
PromptBuilder
      |
      v
LLM Provider
      |
      v
PipelineResultModel

Each component can be replaced or extended independently without affecting other parts of the system.

## 4. Processing Pipeline

The DocumentAI processing pipeline is responsible for transforming a user document into an AI-generated response.

The pipeline executes a sequence of independent processing stages. Each stage receives a defined input, performs a specific operation, and produces an output that is consumed by the next stage.

Current pipeline flow:
DocumentModel
     |
     v
ImageExtractor
     |
     v
DocumentModel (with extracted images)
     |
     v
OCR Processor
     |
     v
DocumentModel (with extracted text)
     |
     v
Chunker
     |
     v
List[ChunkModel]
     |
     v
PromptBuilder
     |
     v
List[Prompt]
     |
     v
LLM Provider
     |
     v
List[LLMResponseModel]
     |
     v
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


### 4.4 Prompt Construction

Responsibility:
- Convert document chunks into LLM-ready prompts.
- Apply prompt templates and processing instructions.

Input:
- ChunkModel

Output:
- LLM prompt messages.


### 4.5 LLM Processing

Responsibility:
- Send prepared prompts to the configured Large Language Model provider.
- Receive generated responses.

Input:
- LLM prompts

Output:
- LLMResponseModel


### 4.6 Pipeline Result

The final output of the pipeline is a PipelineResultModel containing the processed document information, generated chunks, prompts, and LLM responses.

## 5. Core Components

The system is composed of loosely coupled components. Each component has a single responsibility and communicates with other components only through well-defined interfaces.

| Component           | Responsibility                                               |
|---------------------|--------------------------------------------------------------|
| DocumentPipeline    | Orchestrates the complete document processing workflow.      |
| ImageExtractor      | Extracts embedded images from document pages.                |
| OCR Processor       | Extracts machine-readable text from document pages.          |
| Chunker             | Splits document text into logical chunks.                    |
| PromptBuilder       | Converts chunks into prompts suitable for LLMs.              |
| LLM Provider        | Sends prompts to the configured LLM and receives responses.  |
| PipelineResultModel | Stores the final output of the complete processing pipeline. |

## 6. Data Models

## 7. External Dependencies

## 8. Design Principles

## 9. Future Extension Points

