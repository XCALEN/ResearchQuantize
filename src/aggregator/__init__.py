# src/aggregator/__init__.py

from .core import aggregate_papers
from .search.engine import search_papers
from .database.manager import DatabaseManager

__all__ = ['aggregate_papers', 'search_papers', 'DatabaseManager']