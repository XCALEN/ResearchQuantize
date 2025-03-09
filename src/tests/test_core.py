# src/tests/test_core.py

import unittest
from aggregator.core import aggregate_papers

class TestCore(unittest.TestCase):
    def test_aggregate_papers(self):
        """Test that aggregation returns a list of papers.."""
        query = "machine learning"
        limit = 5
        papers = aggregate_papers(query, limit)
        self.assertIsInstance(papers, list)
        self.assertLessEqual(len(papers), limit)

if __name__ == "__main__":
    unittest.main()