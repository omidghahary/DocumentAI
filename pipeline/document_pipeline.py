from pipeline.base_pipeline import BasePipeline
from models.document_model import DocumentModel
from models.pipeline_result_model import PipelineResultModel

class DocumentPipeline(BasePipeline):

    def __init__(
        self,
        image_extractor,
        ocr,
        chunker,
        prompt_builder,
        llm,
    ):
        self.image_extractor = image_extractor
        self.ocr = ocr
        self.chunker = chunker
        self.prompt_builder = prompt_builder
        self.llm = llm
        
    def process(self, document: DocumentModel) -> PipelineResultModel:
        raise NotImplementedError