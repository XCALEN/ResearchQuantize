# src/aggregator/utils/helpers.py

from datetime import datetime

def format_date(date_str):
    """
    Format a date string into a more readable format.
    
    Args:
        date_str (str): The date string to format.
    
    Returns:
        str: The formatted date string.
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%B %d, %Y")
    except ValueError:
        return date_str

def clean_string(text):
    """
    Clean a string by removing extra whitespace and special characters.
    
    Args:
        text (str): The string to clean.
    
    Returns:
        str: The cleaned string.
    """
    import re
    return re.sub(r'\s+', ' ', text.strip())