from pipeline.base_pipeline import BasePipeline
from models.document_model import DocumentModel
from models.pipeline_result_model import PipelineResultModel
from images.base_image_extractor import BaseImageExtractor
from ocr.base_document_ocr import BaseDocumentOCR
from chunking.base_chunker import BaseChunker
from prompting.base_prompt_builder import BasePromptBuilder
from llm.base_llm import BaseLLM
from context.base_context_builder import BaseContextBuilder
from prompting.base_prompt_formatter import BasePromptFormatter
from chunk_selection.base_chunk_selector import BaseChunkSelector

class DocumentPipeline(BasePipeline):

    def __init__(
        self,
        image_extractor: BaseImageExtractor,
        ocr: BaseDocumentOCR,
        chunker: BaseChunker,
        chunk_selector: BaseChunkSelector,
        context_builder: BaseContextBuilder,
        prompt_builder: BasePromptBuilder,
        prompt_formatter: BasePromptFormatter,
        llm: BaseLLM,
        ):
        self.image_extractor = image_extractor
        self.ocr = ocr
        self.chunker = chunker
        self.chunk_selector = chunk_selector
        self.context_builder = context_builder
        self.prompt_builder = prompt_builder
        self.prompt_formatter = prompt_formatter
        self.llm = llm
        
    def process(self, document: DocumentModel) -> PipelineResultModel:
        document = self.image_extractor.extract_images(document)
        document = self.ocr.extract_document_text(document)
        chunks = self.chunker.chunk(document)
        selected_chunks = self.chunk_selector.select(chunks)
        context = self.context_builder.build(selected_chunks)
        prompt = self.prompt_builder.build(context)
        messages = self.prompt_formatter.format(prompt)
        response = self.llm.generate(messages)
        return PipelineResultModel(
            document=document,
            chunks=chunks,
            selected_chunks=selected_chunks,
            context=context,
            prompt=prompt,
            response=response,
        )