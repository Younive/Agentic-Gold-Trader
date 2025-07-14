from config import llm
from src.prompt import PromptCollection
from src.firecrawl import FirecrawlService

def fundamental_analyst_agent(state):
    """
    Scrapes financial news and provides a summarized news report.
    """
    firecrawl_service = FirecrawlService()
    print("Agent: Fundamental Analyst is running...")
    
    # Use the service to scrape with the correct keyword argument
    scraped_data = firecrawl_service.scrape(
        url='https://www.reuters.com/markets/gold/', 
        only_main_content=True
    )
    
    if not scraped_data:
        return {"fundamental_analysis": "Failed to scrape fundamental news."}

    prompt = PromptCollection.FundamentalAnalysis(
        scraped_data=scraped_data,
    )
    
    response = llm.invoke(prompt)
    return {"fundamental_analysis": response.content}