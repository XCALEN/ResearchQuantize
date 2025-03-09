# src/aggregator/core.py

from aggregator.sources.arxiv import ArxivClient
from aggregator.sources.pubmed import PubmedClient
from aggregator.sources.semantic_scholar import SemanticScholarClient
from aggregator.sources.google_scholar import GoogleScholarClient
from aggregator.models.paper import Paper
from aggregator.utils.logger import setup_logger

logger = setup_logger()

def aggregate_papers(query, limit=10):
    """
    Aggregate papers from multiple sources based on the query.
    
    Args:
        query (str): The search query.
        limit (int): Maximum number of papers to retrieve from each source.
    
    Returns:
        list: A list of aggregated Paper objects.
    """
    logger.info(f"Starting aggregation for query: {query}")
    
    # Initialize API clients
    arxiv_client = ArxivClient()
    pubmed_client = PubmedClient()
    semantic_scholar_client = SemanticScholarClient()
    google_scholar_client = GoogleScholarClient()

    # Fetch papers from each source
    arxiv_papers = arxiv_client.fetch_papers(query, limit)
    pubmed_papers = pubmed_client.fetch_papers(query, limit)
    semantic_scholar_papers = semantic_scholar_client.fetch_papers(query, limit)

    # Temporarily disable Google Scholar by commenting out its usage
    # google_scholar_papers = google_scholar_client.fetch_papers(query, limit)
    google_scholar_papers = []  # Return an empty list instead

    # Combine all papers into one list
    aggregated_papers = arxiv_papers + pubmed_papers + semantic_scholar_papers + google_scholar_papers

    logger.info(f"Aggregated {len(aggregated_papers)} papers.")
    return aggregated_papers