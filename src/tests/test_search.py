# src/tests/test_search.py

import unittest
from aggregator.search.engine import search_papers

class TestSearch(unittest.TestCase):
    def test_search_papers(self):
        """Test that search returns papers matching the query.."""
        query = "deep learning"
        papers = search_papers(query, source="arxiv", year=2022)
        self.assertIsInstance(papers, list)
        self.assertGreater(len(papers), 0)

if __name__ == "__main__":
    unittest.main()