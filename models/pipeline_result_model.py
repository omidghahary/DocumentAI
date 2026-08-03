from dataclasses import dataclass
from models.document_model import DocumentModel
from models.chunk_model import ChunkModel
from models.context_model import ContextModel
from models.prompt_model import PromptModel
from models.llm_response_model import LLMResponseModel

@dataclass
class PipelineResultModel:
    document: DocumentModel
    chunks: list[ChunkModel]
    context: ContextModel
    prompt: PromptModel
    response: LLMResponseModel