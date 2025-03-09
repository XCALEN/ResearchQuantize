# src/aggregator/models/author.py

class Author:
    def __init__(self, name, affiliation=None, email=None):
        self.name = name
        self.affiliation = affiliation
        self.email = email

    def __repr__(self):
        return f"<Author(name='{self.name}', affiliation='{self.affiliation}', email='{self.email}')>"