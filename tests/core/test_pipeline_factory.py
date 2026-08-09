from core.config import RetrievalConfig
from core.pipeline_factory import PipelineFactory
from chunk_scorers.keyword_chunk_scorer import KeywordChunkScorer
from chunk_selection.top_score_chunk_selector import TopScoreChunkSelector

def test_create_keyword_scorer():
    config = RetrievalConfig(chunk_scorer="keyword")
    scorer = PipelineFactory.create_chunk_scorer(config)
    assert isinstance(scorer, KeywordChunkScorer)

def test_create_top_score_selector():
    config = RetrievalConfig(chunk_selector="top_score")
    selector = PipelineFactory.create_chunk_selector(config)
    assert isinstance(selector, TopScoreChunkSelector)