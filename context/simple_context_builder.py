from context.base_context_builder import BaseContextBuilder
from models.context_model import ContextModel
from models.chunk_model import ChunkModel

class SimpleContextBuilder(BaseContextBuilder):

    def build(self, chunks: list[ChunkModel]) -> ContextModel:
        text = "\n\n".join(chunk.text for chunk in chunks)
        source_chunks = [chunk.chunk_id for chunk in chunks]
        return ContextModel(
            text=text,
            source_chunks=source_chunks,
            token_count=0,
        )