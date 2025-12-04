from config import llm, firecrawl_app
from src.prompt import PromptCollection
from src.firecrawl_service import FirecrawlService

def retail_sentiment_agent(state):
    """
    Scrapes Myfxbook for retail sentiment on XAUUSD and provides a contrarian analysis.
    """
    firecrawl_service = FirecrawlService()
    print("Agent: Retail Sentiment Analyst is running...")
    
    # Use the service to scrape with the correct keyword argument
    scraped_data = firecrawl_service.scrape(
        url = "https://www.myfxbook.com/community/outlook/XAUUSD", 
        only_main_content=True
    )
    
    if not scraped_data:
        return {"retail sentiment": "Failed to scrape retail sentiment."}
    
    # Use the LLM to find the key data and provide a contrarian interpretation
    prompt = PromptCollection.RetailSentimentAnalysis(
        scraped_data=scraped_data,
    )
    
    response = llm.invoke(prompt)
    analysis = response.content

    state["retail_sentiment_analysis"] = analysis
    return state