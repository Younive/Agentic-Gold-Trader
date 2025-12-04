from config import firecrawl_app

class FirecrawlService:
    def __init__(self):
        self.app = firecrawl_app

    def search(self, query: str):
        """
        Performs a generic search using Firecrawl.
        """
        try:
            results = self.app.search(query=query, num_results=5)
            return results
        except Exception as e:
            print(f"Error during Firecrawl search for '{query}': {e}")
            return []
        
    def scrape(self, url: str, **kwargs):
        """
        Performs a scrape using Firecrawl, accepting flexible keyword arguments.
        """
        try:
            results = self.app.scrape_url(url=url, **kwargs)
            return results
        except Exception as e:
            print(f"Error during Firecrawl scrape for '{url}': {e}")
            return None