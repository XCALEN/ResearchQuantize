# src/aggregator/utils/logger.py

import logging
from rich.logging import RichHandler

def setup_logger():
    """Set up a logger with rich formatting."""
    logger = logging.getLogger("ResearchQuantize")
    logger.setLevel(logging.DEBUG)

    # Create a console handler with rich formatting
    ch = RichHandler(rich_tracebacks=True, markup=True)
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(message)s')
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    return logger