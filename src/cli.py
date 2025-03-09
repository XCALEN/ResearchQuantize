#!/usr/bin/env python3

import argparse
from rich.console import Console
from rich.table import Table
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.aggregator.core import aggregate_papers
from src.aggregator.search.engine import search_papers
from src.aggregator.utils.logger import setup_logger

# Initialize Rich console and logger
console = Console()
logger = setup_logger()

def display_results(papers):
    """Display search results in a beautiful table format."""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Title", style="dim", width=50)
    table.add_column("Authors", style="cyan")
    table.add_column("Published", style="green")
    table.add_column("Source", style="yellow")

    for paper in papers:
        table.add_row(
            paper.title,
            ", ".join([author for author in paper.authors]),
            paper.published_date,
            paper.source
        )

    console.print(table)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="ResearchQuantize: Aggregate and Search Research Papers")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Aggregation command
    aggregate_parser = subparsers.add_parser('aggregate', help='Aggregate research papers from multiple sources')
    aggregate_parser.add_argument('--query', required=True, help='Search query for papers')
    aggregate_parser.add_argument('--limit', type=int, default=10, help='Limit the number of results')

    # Search command
    search_parser = subparsers.add_parser('search', help='Search for specific papers')
    search_parser.add_argument('--query', required=True, help='Search query for papers')
    search_parser.add_argument('--source', choices=['arxiv', 'pubmed', 'semantic_scholar', 'google_scholar'], help='Filter by source')
    search_parser.add_argument('--year', type=int, help='Filter by publication year')

    # Parse arguments
    args = parser.parse_args()

    if args.command == 'aggregate':
        logger.info(f"Aggregating papers for query: {args.query}")
        papers = aggregate_papers(args.query, limit=args.limit)
        display_results(papers)

    elif args.command == 'search':
        logger.info(f"Searching papers for query: {args.query}")
        papers = search_papers(args.query, source=args.source, year=args.year)
        display_results(papers)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()