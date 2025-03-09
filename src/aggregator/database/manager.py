# src/aggregator/database/manager.py

import sqlite3
from aggregator.models.paper import Paper
from aggregator.utils.logger import setup_logger

logger = setup_logger()

class DatabaseManager:
    def __init__(self, db_path="papers.db"):
        self.db_path = db_path
        self.conn = None
        self._initialize_db()

    def _initialize_db(self):
        """Initialize the database and create tables if they don't exist."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS papers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    authors TEXT,
                    published_date TEXT,
                    source TEXT
                )
            """)
            self.conn.commit()
        except Exception as e:
            logger.error(f"Error initializing database: {e}")

    def save_paper(self, paper):
        """
        Save a paper to the database.
        
        Args:
            paper (Paper): The Paper object to save.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO papers (title, authors, published_date, source)
                VALUES (?, ?, ?, ?)
            """, (paper.title, ", ".join(paper.authors), paper.published_date, paper.source))
            self.conn.commit()
            logger.info(f"Saved paper '{paper.title}' to the database.")
        except Exception as e:
            logger.error(f"Error saving paper to database: {e}")

    def get_all_papers(self):
        """
        Retrieve all papers from the database.
        
        Returns:
            list: A list of Paper objects.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT title, authors, published_date, source FROM papers")
            rows = cursor.fetchall()
            papers = []
            for row in rows:
                title, authors, published_date, source = row
                papers.append(Paper(title=title, authors=authors.split(", "), published_date=published_date, source=source))
            return papers
        except Exception as e:
            logger.error(f"Error retrieving papers from database: {e}")
            return []

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()