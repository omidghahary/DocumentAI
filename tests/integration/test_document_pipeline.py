from unittest.mock import Mock
from pipeline.document_pipeline import DocumentPipeline
from models.prompt_model import PromptModel
from models.llm_response_model import LLMResponseModel

def test_document_pipeline_calls_context_builder_after_chunker():
    image_extractor = Mock()
    ocr = Mock()
    chunker = Mock()
    chunk_scorer = Mock()
    chunk_selector = Mock()
    context_builder = Mock()
    prompt_builder = Mock()
    prompt_formatter = Mock()
    llm = Mock()
    expected_messages = [
        {
            "role": "system",
            "content": "You are a document analysis assistant."
        },
        {
            "role": "user",
            "content": "fake_prompt"
        }
    ]
    fake_response = LLMResponseModel(
        text="fake_response",
        prompt_tokens=10,
        completion_tokens=5,
        model="mock"
    )
    image_extractor.extract_images.return_value = "fake_images"
    ocr.extract_document_text.return_value = "fake_text"
    chunker.chunk.return_value = "fake_chunks"
    chunk_scorer.score.return_value = "fake_scored_chunks"
    chunk_selector.select.return_value = "fake_selected_chunks"
    context_builder.build.return_value = "fake_context"
    prompt_builder.build.return_value = PromptModel(text="fake_prompt")
    prompt_formatter.format.return_value = expected_messages
    llm.generate.return_value = fake_response
    pipeline = DocumentPipeline(
        image_extractor=image_extractor,
        ocr=ocr,
        chunker=chunker,
        chunk_scorer=chunk_scorer,
        chunk_selector=chunk_selector,
        context_builder=context_builder,
        prompt_builder=prompt_builder,
        prompt_formatter=prompt_formatter,
        llm=llm,
    )

    result = pipeline.process("document")
    messages = llm.generate.call_args.args[0]

    image_extractor.extract_images.assert_called_once_with("document")
    ocr.extract_document_text.assert_called_once_with("fake_images")
    chunker.chunk.assert_called_once_with("fake_text")
    chunk_scorer.score.assert_called_once_with("fake_chunks","")
    chunk_selector.select.assert_called_once_with("fake_scored_chunks")
    context_builder.build.assert_called_once_with("fake_selected_chunks")
    prompt_builder.build.assert_called_once_with("fake_context")
    prompt_formatter.format.assert_called_once_with(PromptModel(text="fake_prompt"))
    llm.generate.assert_called_once_with(expected_messages)

    assert result.chunks == "fake_chunks"
    assert result.context == "fake_context"
    assert result.selected_chunks == "fake_selected_chunks"
    assert result.prompt == PromptModel(text="fake_prompt")
    assert result.response == fake_response
    assert isinstance(messages, list)
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
