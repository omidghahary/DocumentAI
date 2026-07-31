from pipeline.base_pipeline import BasePipeline
from models.document_model import DocumentModel
from models.pipeline_result_model import PipelineResultModel
from images.base_image_extractor import BaseImageExtractor
from ocr.base_document_ocr import BaseDocumentOCR
from chunking.base_chunker import BaseChunker
from prompting.base_prompt_builder import BasePromptBuilder
from llm.base_llm import BaseLLM

class DocumentPipeline(BasePipeline):

    def __init__(
        self,
        image_extractor: BaseImageExtractor,
        ocr: BaseDocumentOCR,
        chunker: BaseChunker,
        prompt_builder: BasePromptBuilder,
        llm: BaseLLM,
        ):
        self.image_extractor = image_extractor
        self.ocr = ocr
        self.chunker = chunker
        self.prompt_builder = prompt_builder
        self.llm = llm
        
    def process(self, document: DocumentModel) -> PipelineResultModel:
        document = self.image_extractor.extract_images(document)
        document = self.ocr.extract_document_text(document)
        chunks = self.chunker.chunk(document)
        prompts = [
            self.prompt_builder.build(chunk)
            for chunk in chunks
        ]
        responses = [
            self.llm.generate(prompt)
            for prompt in prompts
        ]
        return PipelineResultModel(
            document= document,
            chunks= chunks,
            prompts= prompts,
            responses= responses
        )