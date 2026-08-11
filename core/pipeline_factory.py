from chunk_scorers.keyword_chunk_scorer import KeywordChunkScorer
from chunk_scorers.simple_chunk_scorer import SimpleChunkScorer
from chunk_selection.top_score_chunk_selector import TopScoreChunkSelector
from chunk_selection.simple_chunk_selector import SimpleChunkSelector
from pipeline.document_pipeline import DocumentPipeline
from chunking.simple_chunker import SimpleChunker
from context.simple_context_builder import SimpleContextBuilder
from images.pymupdf_image_extractor import PyMuPDFImageExtractor
from ocr.tesseract_ocr import TesseractOCR
from prompting.simple_prompt_builder import SimplePromptBuilder
from prompting.simple_prompt_formatter import SimplePromptFormatter
from llm.mock_llm import MockLLM
from core.config import OCRConfig
from core.text_tokenizer import TextTokenizer

class PipelineFactory:

    @staticmethod
    def create_chunk_scorer(config):
        if config.chunk_scorer == "keyword":
            return KeywordChunkScorer(TextTokenizer())
        return SimpleChunkScorer()

    @staticmethod
    def create_chunk_selector(config):
        if config.chunk_selector == "top_score":
            return TopScoreChunkSelector(max_chunks=config.max_chunks)
        return SimpleChunkSelector()


    def create_document_pipeline(self, config):

        return DocumentPipeline(
            image_extractor=PyMuPDFImageExtractor(),
            ocr= TesseractOCR(OCRConfig()),
            chunker=SimpleChunker(),
            chunk_scorer=PipelineFactory.create_chunk_scorer(config),
            chunk_selector=PipelineFactory.create_chunk_selector(config),
            context_builder=SimpleContextBuilder(),
            prompt_builder=SimplePromptBuilder(),
            prompt_formatter=SimplePromptFormatter(),
            llm=MockLLM()
        )