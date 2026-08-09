import pytest
from core.config import RetrievalConfig
from core.pipeline_factory import PipelineFactory
from chunk_scorers.keyword_chunk_scorer import KeywordChunkScorer
from chunk_selection.top_score_chunk_selector import TopScoreChunkSelector
from core.pipeline_factory import PipelineFactory

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
