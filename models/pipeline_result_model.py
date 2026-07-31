from dataclasses import dataclass
from models.document_model import DocumentModel
from models.chunk_model import ChunkModel
from models.llm_response_model import LLMResponseModel

@dataclass
class PipelineResultModel:
    document: DocumentModel
    chunks: list[ChunkModel]
    prompts: list[list[dict]]
    responses: list[LLMResponseModel]