import pytest
from core.config import RetrievalConfig
from core.pipeline_factory import PipelineFactory
from chunk_scorers.keyword_chunk_scorer import KeywordChunkScorer
from chunk_selection.top_score_chunk_selector import TopScoreChunkSelector
from chunk_scorers.tfidf_chunk_scorer import TfIdfChunkScorer
from chunk_scorers.simple_chunk_scorer import SimpleChunkScorer
from chunk_selection.simple_chunk_selector import SimpleChunkSelector

@pytest.fixture 
def config():
    return RetrievalConfig(
    chunk_scorer="keyword", 
    chunk_selector="top_score",
    )

@pytest.fixture
def pipline_factory():
    return PipelineFactory()

def test_document_pipeline_factory_creation(pipline_factory):
    assert pipline_factory is not None

def test_document_pipeline_factory_create_pipline(pipline_factory, config):
    pipeline = pipline_factory.create_document_pipeline(config)
    assert pipeline is not None
    assert isinstance(pipeline.chunk_scorer, KeywordChunkScorer)
    assert isinstance(pipeline.chunk_selector, TopScoreChunkSelector)    

def test_document_pipeline_factory_creates_tfidf_scorer(pipline_factory):
    config = RetrievalConfig(
        chunk_scorer="tfidf",
        chunk_selector="top_score",
    )
    pipeline = pipline_factory.create_document_pipeline(config)
    assert isinstance(pipeline.chunk_scorer, TfIdfChunkScorer)
    assert isinstance(pipeline.chunk_selector, TopScoreChunkSelector)

def test_document_pipeline_factory_rejects_unknown_chunk_scorer(pipline_factory):
    config = RetrievalConfig(
        chunk_scorer="unknown",
        chunk_selector="top_score",
    )
    with pytest.raises(ValueError):
        pipline_factory.create_document_pipeline(config)

def test_document_pipeline_factory_rejects_unknown_chunk_selector(pipline_factory):
    config = RetrievalConfig(
        chunk_scorer="keyword",
        chunk_selector="unknown",
    )
    with pytest.raises(ValueError):
        pipline_factory.create_document_pipeline(config)

def test_document_pipeline_factory_creates_simple_chunk_scorer(pipline_factory):
    config = RetrievalConfig(
        chunk_scorer="simple",
        chunk_selector="top_score",
    )
    pipeline = pipline_factory.create_document_pipeline(config)
    assert isinstance(pipeline.chunk_scorer, SimpleChunkScorer)

def test_document_pipeline_factory_creates_simple_chunk_selector(pipline_factory):
    config = RetrievalConfig(
        chunk_scorer="keyword",
        chunk_selector="simple",
    )
    pipeline = pipline_factory.create_document_pipeline(config)
    assert isinstance(pipeline.chunk_selector, SimpleChunkSelector)