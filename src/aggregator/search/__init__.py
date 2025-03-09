# src/aggregator/search/__init__.py

from .engine import search_papers
from .filters import filter_by_author, filter_by_year

__all__ = ['search_papers', 'filter_by_author', 'filter_by_year']