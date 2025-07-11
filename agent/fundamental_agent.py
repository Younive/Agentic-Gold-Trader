from config import llm, firecrawl_app
from src.prompt import PromptCollection

def fundamental_analyst_agent(state):
    """
    Scrapes financial news, filters out noise, and calculates the net sentiment for gold.
    """
    print("Agent: Fundamental Analyst is running...")
    
    scraped_data = firecrawl_app.scrape_url(
        url='https://www.reuters.com/markets/commodities/', 
        params={'pageOptions': {'onlyMainContent': True}}
    )
    
    # New prompt for filtered net sentiment analysis
    prompt = PromptCollection.FundamentalAnalysis(
        scraped_data=scraped_data,
    )
    
    response = llm.invoke(prompt)
    return {"fundamental_analysis": response.content}