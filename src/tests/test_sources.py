# src/tests/test_sources.py

import unittest
from aggregator.sources.arxiv import ArxivClient
from aggregator.sources.pubmed import PubmedClient

class TestSources(unittest.TestCase):
    def test_arxiv_client(self):
        """Test that Arxiv client fetches papers.."""
        client = ArxivClient()
        papers = client.fetch_papers("quantum computing", limit=3)
        self.assertIsInstance(papers, list)
        self.assertGreater(len(papers), 0)

    def test_pubmed_client(self):
        """Test that PubMed client fetches papers."""
        client = PubmedClient()
        papers = client.fetch_papers("neural networks", limit=3)
        self.assertIsInstance(papers, list)
        self.assertGreater(len(papers), 0)

if __name__ == "__main__":
    unittest.main()