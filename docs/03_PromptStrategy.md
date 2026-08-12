Prompt Types or Prompt Categories

Summary

Extraction

Question Answering

Table Analysis

Chart Analysis

Image Description

Comparison

Classification

Reasoning

## Retrieval and Context Flow

Prompt generation occurs after Retrieval and Context Construction.

The Retrieval layer identifies relevant document chunks first.
The ContextBuilder then constructs the context supplied to the
PromptBuilder.

Conceptually:

Query
  ↓
Retrieval
  ↓
Relevant Chunks
  ↓
ContextBuilder
  ↓
PromptBuilder
  ↓
LLM