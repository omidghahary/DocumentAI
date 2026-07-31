import pytest
from pipeline.document_pipeline import DocumentPipeline
from images.pymupdf_image_extractor import PyMuPDFImageExtractor
from ocr.tesseract_document_ocr import TesseractDocumentOCR
from chunking.simple_chunker import SimpleChunker
from prompting.simple_prompt_builder import SimplePromptBuilder
from llm.ollama_llm import OllamaLLM
from pipeline.base_pipeline import BasePipeline
from core.config import OCRConfig, LLMConfig
from ocr.tesseract_ocr import TesseractOCR

@pytest.fixture
def ocr_config():
    return OCRConfig

@pytest.fixture
def ocr_engine(ocr_config):
    return TesseractOCR(ocr_config)

@pytest.fixture
def llm_config():
    return LLMConfig(
        provider="ollama",
        base_url="http://localhost:11434",
        model_name="qwen2.5:3b",
        temperature=0.1,
        timeout=120
    )

@pytest.fixture
def pipeline(ocr_engine, llm_config):
    image_extractor = PyMuPDFImageExtractor()
    ocr = TesseractDocumentOCR(ocr_engine)
    chunker = SimpleChunker()
    prompt_builder = SimplePromptBuilder()
    llm = OllamaLLM(llm_config)
    return DocumentPipeline(
        image_extractor=image_extractor,
        ocr=ocr,
        chunker=chunker,
        prompt_builder=prompt_builder,
        llm=llm
    )

def test_document_pipeline_can_be_instantiated(pipeline):
    assert pipeline is not None

def test_document_pipeline_is_base_pipeline(pipeline):
    assert isinstance(pipeline, BasePipeline)

def test_document_pipeline_hold_dependencies(pipeline):
    assert isinstance(pipeline.image_extractor, PyMuPDFImageExtractor)
    assert isinstance(pipeline.ocr, TesseractDocumentOCR)
    assert isinstance(pipeline.chunker, SimpleChunker)
    assert isinstance(pipeline.prompt_builder, SimplePromptBuilder)
    assert isinstance(pipeline.llm, OllamaLLM)

