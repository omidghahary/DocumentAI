# import pytest
from unittest.mock import Mock
from pipeline.document_pipeline import DocumentPipeline
from models.pipeline_result_model import PipelineResultModel
# from images.pymupdf_image_extractor import PyMuPDFImageExtractor
# from ocr.tesseract_document_ocr import TesseractDocumentOCR
# from chunking.simple_chunker import SimpleChunker
# from prompting.simple_prompt_builder import SimplePromptBuilder
# from llm.ollama_llm import OllamaLLM
# from pipeline.base_pipeline import BasePipeline
# from core.config import OCRConfig, LLMConfig
# from ocr.tesseract_ocr import TesseractOCR

# @pytest.fixture
# def ocr_config():
#     return OCRConfig

# @pytest.fixture
# def ocr_engine(ocr_config):
#     return TesseractOCR(ocr_config)

# @pytest.fixture
# def llm_config():
#     return LLMConfig(
#         provider="ollama",
#         base_url="http://localhost:11434",
#         model_name="qwen2.5:3b",
#         temperature=0.1,
#         timeout=120
#     )

# @pytest.fixture
# def pipeline(ocr_engine, llm_config):
#     image_extractor = PyMuPDFImageExtractor()
#     ocr = TesseractDocumentOCR(ocr_engine)
#     chunker = SimpleChunker()
#     prompt_builder = SimplePromptBuilder()
#     llm = OllamaLLM(llm_config)
#     return DocumentPipeline(
#         image_extractor=image_extractor,
#         ocr=ocr,
#         chunker=chunker,
#         prompt_builder=prompt_builder,
#         llm=llm
#     )

# def test_document_pipeline_can_be_instantiated(pipeline):
#     assert pipeline is not None

# def test_document_pipeline_is_base_pipeline(pipeline):
#     assert isinstance(pipeline, BasePipeline)

# def test_document_pipeline_hold_dependencies(pipeline):
    # assert isinstance(pipeline.image_extractor, PyMuPDFImageExtractor)
    # assert isinstance(pipeline.ocr, TesseractDocumentOCR)
    # assert isinstance(pipeline.chunker, SimpleChunker)
    # assert isinstance(pipeline.prompt_builder, SimplePromptBuilder)
    # assert isinstance(pipeline.llm, OllamaLLM)

# def test_document_pipeline_process_calls_image_extractor():
#     image_extractor = Mock()
#     ocr = Mock()
#     image_extractor.extract_images.return_value = "document_with_images"
#     ocr.extract_document_text.return_value = "document_after_ocr"
#     pipeline = DocumentPipeline(
#         image_extractor=image_extractor,
#         ocr=ocr,
#         chunker=Mock(),
#         prompt_builder=Mock(),
#         llm=Mock()
#     )
#     result = pipeline.process("document")
#     image_extractor.extract_images.assert_called_once_with("document")
#     ocr.extract_document_text.assert_called_once_with("document_with_images")
#     assert result == "document_after_ocr"

# def test_document_pipeline_process_calls_ocr_after_image_extractor():

#     image_extractor = Mock()
#     ocr = Mock()
#     image_extractor.extract_images.return_value = "document_with_images"
#     ocr.extract_document_text.return_value = "document_with_text"
#     pipeline = DocumentPipeline(
#         image_extractor=image_extractor,
#         ocr=ocr,
#         chunker=Mock(),
#         prompt_builder=Mock(),
#         llm=Mock()
#     )
#     result = pipeline.process("document")
#     image_extractor.extract_images.assert_called_once_with("document")
#     ocr.extract_document_text.assert_called_once_with("document_with_images")
#     assert result == "document_with_text"

# def test_document_pipeline_process_calls_chunker_after_ocr():
#     image_extractor = Mock()
#     ocr = Mock()
#     chunker = Mock()
#     prompt_builder = Mock()
#     image_extractor.extract_images.return_value = "document_with_images"
#     ocr.extract_document_text.return_value = "document_with_text"
#     chunker.chunk.return_value = "fake_chunk"
#     chunk1 = Mock()
#     chunk2 = Mock()
#     chunks = [chunk1, chunk2]
#     chunker.chunk.return_value = chunks
#     prompt_builder.build.side_effect = ["prompt1", "prompt2"]
#     llm = Mock()
#     llm.generate.side_effect = ["response1", "response2"]
#     pipeline = DocumentPipeline(
#         image_extractor=image_extractor,
#         ocr=ocr,
#         chunker=chunker,
#         prompt_builder=prompt_builder,
#         llm=llm
#     )
#     result = pipeline.process("document")
#     image_extractor.extract_images.assert_called_once_with("document")
#     ocr.extract_document_text.assert_called_once_with("document_with_images")
#     chunker.chunk.assert_called_once_with("document_with_text")
#     prompt_builder.build.assert_any_call(chunk1)
#     prompt_builder.build.assert_any_call(chunk2)
#     assert prompt_builder.build.call_count == 2
#     assert llm.generate.call_count == 2
#     llm.generate.assert_any_call("prompt1")
#     llm.generate.assert_any_call("prompt2")
#     assert isinstance(result, PipelineResultModel)

def test_document_pipeline_calls_context_builder_after_chunker():
    image_extractor = Mock()
    ocr = Mock()
    chunker = Mock()
    context_builder = Mock()
    prompt_builder = Mock()
    llm = Mock()

    image_extractor.extract_images.return_value = "fake_images"
    ocr.extract_document_text.return_value = "fake_text"
    chunker.chunk.return_value = "fake_chunks"
    context_builder.build.return_value = "fake_context"
    prompt_builder.build.return_value = "fake_prompt"
    llm.generate.return_value = "fake_response"

    pipeline = DocumentPipeline(
        image_extractor=image_extractor,
        ocr=ocr,
        chunker=chunker,
        context_builder=context_builder,
        prompt_builder=prompt_builder,
        llm=llm,
    )

    result = pipeline.process("document")

    image_extractor.extract_images.assert_called_once_with("document")
    ocr.extract_document_text.assert_called_once_with("fake_images")
    chunker.chunk.assert_called_once_with("fake_text")
    context_builder.build.assert_called_once_with("fake_chunks")
    prompt_builder.build.assert_called_once_with("fake_context")
    llm.generate.assert_called_once_with("fake_prompt")

    assert result.chunks == "fake_chunks"
    assert result.context == "fake_context"
    assert result.prompt == "fake_prompt"
    assert result.response == "fake_response"
