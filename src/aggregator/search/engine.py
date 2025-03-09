# src/aggregator/search/engine.py

from aggregator.sources.arxiv import ArxivClient
from aggregator.sources.pubmed import PubmedClient
from aggregator.sources.semantic_scholar import SemanticScholarClient
from aggregator.sources.google_scholar import GoogleScholarClient
from aggregator.utils.logger import setup_logger

logger = setup_logger()

def search_papers(query, source=None, year=None):
    """
    Search for papers across multiple sources with optional filters.
    
    Args:
        query (str): The search query.
        source (str): Filter by source (arxiv, pubmed, semantic_scholar, google_scholar).
        year (int): Filter by publication year.
    
    Returns:
        list: A list of Paper objects matching the search criteria.
    """
    logger.info(f"Searching papers for query: {query}, source: {source}, year: {year}")

    clients = {
        'arxiv': ArxivClient(),
        'pubmed': PubmedClient(),
        'semantic_scholar': SemanticScholarClient(),
        'google_scholar': GoogleScholarClient()
    }

    if source:
        # Search only in the specified source
        client = clients.get(source)
        if not client:
            raise ValueError(f"Invalid source: {source}")
        papers = client.fetch_papers(query, limit=10)
    else:
        # Search across all sources
        papers = []
        for client in clients.values():
            papers.extend(client.fetch_papers(query, limit=5))

    # Apply year filter if provided
    if year:
        papers = [paper for paper in papers if str(year) in paper.published_date]

    logger.info(f"Found {len(papers)} papers matching the search criteria.")
    return papers