# src/aggregator/search/filters.py

def filter_by_author(papers, author_name):
    """
    Filter papers by author name.
    
    Args:
        papers (list): List of Paper objects.
        author_name (str): The name of the author to filter by.
    
    Returns:
        list: A filtered list of Paper objects.
    """
    return [paper for paper in papers if any(author_name.lower() in author.lower() for author in paper.authors)]

def filter_by_year(papers, year):
    """
    Filter papers by publication year.
    
    Args:
        papers (list): List of Paper objects.
        year (int): The year to filter by.
    
    Returns:
        list: A filtered list of Paper objects.
    """
    return [paper for paper in papers if str(year) in paper.published_date]