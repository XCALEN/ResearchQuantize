# ResearchQuantize

**ResearchQuantize** is a  command-line tool that aggregates and searches research papers from multiple sources, like **Arxiv**, **PubMed**, and **Semantic Scholar**. (Google Scholar is temporarily disabled but can be re-enabled easily.)

It is easy to discover, filter, and save academic papers for your research needs.

## Installation

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package manager)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/Arcoson/ResearchQuantize.git
   cd ResearchQuantize
   ```
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Not Required (Really not needed unless you want to surpass ratelimits)- Set up environment variables:

   - Create a `.env` file in the root directory and add any required API keys:
     ```env
     ARXIV_API_KEY=  # Not required
     PUBMED_API_KEY=your_pubmed_api_key # only if >100 requests (check with pubmed)
     SEMANTIC_SCHOLAR_API_KEY=  # Not required
     GOOGLE_SCHOLAR_API_KEY=  # Temporarily disabled
     DATABASE_PATH=papers.db
     ```

## Usage

### Aggregate Papers

Aggregate papers from multiple sources based on a query:

```bash
python3 src/cli.py aggregate --query "machine learning" --limit 10
```

### Search Papers

Search for specific papers with optional filters:

```bash
python3 src/cli.py search --query "neural networks" --source arxiv
```

### View Saved Papers

All fetched papers are saved to an SQLite database (`papers.db`). You can view them using the SQLite CLI:

```bash
sqlite3 papers.db "SELECT * FROM papers;"
```

---

## Configuration

You can customize the behavior of PaperEngine by modifying the following files:

- **`src/config/preferences.json`**: User preferences such as default query limits and themes.
- **`.env`**: Environment variables for API keys and database paths.

Example `preferences.json`:

```json
{
    "default_query_limit": 10,
    "default_source": "arxiv",
    "default_year_filter": null,
    "theme": "dark",
    "show_advanced_options": false
}
```

---

## Database

ResearchQuantize uses an SQLite database (`papers.db`) to store fetched papers. The database schema includes the following fields:

- `title`: Title of the paper.
- `authors`: Comma-separated list of authors.
- `published_date`: Publication date of the paper.
- `source`: Source of the paper (e.g., Arxiv, PubMed).

You can query the database directly using SQLite commands or integrate it into other tools.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Notes

- **Google Scholar**: Temporarily disabled due to potential scraping issues. To re-enable it, uncomment the relevant lines in `src/aggregator/core.py`:
  ```python
  # google_scholar_papers = google_scholar_client.fetch_papers(query, limit)
  google_scholar_papers = google_scholar_client.fetch_papers(query, limit) # this might not work as google scholar does not have offical API, might need to implement web scraping
  ```
