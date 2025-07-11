import os
from firecrawl import FirecrawlApp, ScrapeOptions
from config import firecrawl_app

class FirecrawlService:
    def __init__(self):
        self.app = firecrawl_app

    def search_fundamental(self, query: str):
        try:
            options = ScrapeOptions(
                query=query,
                num_results=5,
                include_images=False,
                include_videos=False,
                include_news=False
            )
            results = self.app.search(options)
            return results
        except Exception as e:
            print(f"Error during Firecrawl search: {e}")
            return []
        
    def search_oi(self, query: str):
        try:
            options = ScrapeOptions(
                query=query,
                num_results=5,
                include_images=False,
                include_videos=False,
                include_news=False
            )
            results = self.app.search(options)
            return results
        except Exception as e:
            print(f"Error during Firecrawl search: {e}")
            return []
        
    def search_retail_sentiment(self, query: str):
        try:
            options = ScrapeOptions(
                query=query,
                num_results=5,
                include_images=False,
                include_videos=False,
                include_news=False
            )
            results = self.app.search(options)
            return results
        except Exception as e:
            print(f"Error during Firecrawl search: {e}")
            return []