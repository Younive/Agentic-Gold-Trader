from config import llm
from src.prompt import PromptCollection
from src.firecrawl_service import FirecrawlService
from src.models import TradingState

def fundamental_analyst_agent(state):
    """
    Scrapes financial news and provides a summarized news report.
    """
    firecrawl_service = FirecrawlService()
    print("Agent: Fundamental Analyst is running...")
    
    urls = [
        'https://www.reuters.com/markets/gold/',
        'https://www.kitco.com/news/category/commodities/gold',
        'https://www.fxstreet.com/news?q=&hPP=17&idx=FxsIndexPro&p=0&dFR%5BCategory%5D%5B0%5D=News&dFR%5BTags%5D%5B0%5D=Commodities&dFR%5BTags%5D%5B1%5D=Gold'
    ]

    all_scraped_data = []

    for url in urls:
        print(f"Scraping {url}...")
        try:
            # Use the service to scrape with the correct keyword argument
            scraped_data = firecrawl_service.scrape(
                url=url, 
                only_main_content=True
            )
            if scraped_data:
                all_scraped_data.append(f"Source: {url}\nData: {scraped_data}")
        except Exception as e:
            print(f"Failed to scrape {url}: {e}")
    
    if not all_scraped_data:
        return {"fundamental_analysis": "Failed to scrape fundamental news from all sources."}

    combined_data = "\n\n".join(all_scraped_data)

    prompt = PromptCollection.FundamentalAnalysis(scraped_data=combined_data)

    response = llm.invoke(prompt)
    state["fundamental_analysis"] = response.content
    return state