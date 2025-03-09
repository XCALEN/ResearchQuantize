# src/aggregator/sources/arxiv.py

import requests
from aggregator.models.paper import Paper
from aggregator.utils.logger import setup_logger

logger = setup_logger()

class ArxivClient:
    BASE_URL = "http://export.arxiv.org/api/query"

    def fetch_papers(self, query, limit=10):
        """
        Fetch papers from Arxiv based on the query.
        
        Args:
            query (str): The search query.
            limit (int): Maximum number of papers to retrieve.
        
        Returns:
            list: A list of Paper objects.
        """
        logger.info(f"Fetching papers from Arxiv for query: {query}")
        params = {
            'search_query': query,
            'start': 0,
            'max_results': limit
        }

        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()

        # Parse the XML response (for simplicity, assume we have a helper function)
        papers = self._parse_response(response.text)
        logger.info(f"Fetched {len(papers)} papers from Arxiv.")
        return papers

    def _parse_response(self, xml_data):
        """
        Parse the Arxiv API response and return a list of Paper objects.
        
        Args:
            xml_data (str): The XML response from Arxiv.
        
        Returns:
            list: A list of Paper objects.
        """
        # Simplified parsing logic (you can use an XML parser like lxml or xml.etree.ElementTree)
        papers = []
        # Example: Assume we parse the XML and extract title, authors, etc.
        for entry in xml_data.split('<entry>')[1:]:
            title = entry.split('<title>')[1].split('</title>')[0]
            authors = [author.split('<name>')[1].split('</name>')[0] for author in entry.split('<author>')[1:]]
            published_date = entry.split('<published>')[1].split('</published>')[0]
            papers.append(Paper(title=title, authors=authors, published_date=published_date, source="Arxiv"))
        
        return papers