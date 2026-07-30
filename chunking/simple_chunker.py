from models.document_model import DocumentModel
from models.chunk_model import ChunkModel
from chunking.base_chunker import BaseChunker

class SimpleChunker(BaseChunker):
    def chunk(self, document: DocumentModel) -> list[ChunkModel]:
        chunks = []
        for page in document.pages:
            chunk = ChunkModel(
                chunk_id=page.page_number,
                text=page.text,
                page_numbers=[page.page_number],
                metadata={}
            )
            chunks.append(chunk)
        return chunks