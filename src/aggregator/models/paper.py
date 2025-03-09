# src/aggregator/models/paper.py

class Paper:
    def __init__(self, title, authors, published_date, source):
        self.title = title
        self.authors = authors
        self.published_date = published_date
        self.source = source

    def __repr__(self):
        return f"<Paper(title='{self.title}', authors={self.authors}, published_date='{self.published_date}', source='{self.source}')>"