# src/aggregator/sources/semantic_scholar.py

import requests
from aggregator.models.paper import Paper
from aggregator.utils.logger import setup_logger

logger = setup_logger()

class SemanticScholarClient:
    BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

    def fetch_papers(self, query, limit=10):
        """
        Fetch papers from Semantic Scholar based on the query.
        
        Args:
            query (str): The search query.
            limit (int): Maximum number of papers to retrieve.
        
        Returns:
            list: A list of Paper objects.
        """
        logger.info(f"Fetching papers from Semantic Scholar for query: {query}")
        params = {
            'query': query,
            'limit': limit,
            'fields': 'title,authors,year,publicationDate'
        }

        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()
        papers = self._parse_response(data)
        logger.info(f"Fetched {len(papers)} papers from Semantic Scholar.")
        return papers

    def _parse_response(self, data):
        """
        Parse the Semantic Scholar API response and return a list of Paper objects.
        
        Args:
            data (dict): The JSON response from Semantic Scholar.
        
        Returns:
            list: A list of Paper objects.
        """
        papers = []
        for paper_data in data.get('data', []):
            title = paper_data.get('title', 'No Title')
            authors = [author['name'] for author in paper_data.get('authors', [])]
            published_date = paper_data.get('publicationDate', 'Unknown')
            papers.append(Paper(title=title, authors=authors, published_date=published_date, source="Semantic Scholar"))
        
        return papers