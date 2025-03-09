# src/aggregator/sources/google_scholar.py

import requests
from aggregator.models.paper import Paper
from aggregator.utils.logger import setup_logger

logger = setup_logger()

class GoogleScholarClient:
    BASE_URL = "https://scholar.google.com/scholar"

    def fetch_papers(self, query, limit=10):
        """
        Fetch papers from Google Scholar based on the query.
        
        Args:
            query (str): The search query.
            limit (int): Maximum number of papers to retrieve.
        
        Returns:
            list: A list of Paper objects.
        """
        logger.info(f"Fetching papers from Google Scholar for query: {query}")
        params = {
            'q': query,
            'num': limit
        }

        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()

        # Parse the HTML response (you can use BeautifulSoup or another HTML parser)
        papers = self._parse_response(response.text)
        logger.info(f"Fetched {len(papers)} papers from Google Scholar.")
        return papers

    def _parse_response(self, html_data):
        """
        Parse the Google Scholar HTML response and return a list of Paper objects.
        
        Args:
            html_data (str): The HTML response from Google Scholar.
        
        Returns:
            list: A list of Paper objects.
        """
        # Simplified parsing logic (you can use BeautifulSoup for more robust parsing)
        papers = []
        # Example: Assume we parse the HTML and extract title, authors, etc.
        for entry in html_data.split('<div class="gs_ri">')[1:]:
            title = entry.split('<h3><a href="')[1].split('">')[1].split('</a>')[0]
            authors = entry.split('<div class="gs_a">')[1].split(' - ')[0].split(', ')
            published_date = entry.split('<div class="gs_a">')[1].split(' - ')[1].split(',')[0]
            papers.append(Paper(title=title, authors=authors, published_date=published_date, source="Google Scholar"))
        
        return papers