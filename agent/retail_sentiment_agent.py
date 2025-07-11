from config import llm, firecrawl_app
from src.prompt import PromptCollection

def retail_sentiment_agent(state):
    """
    Scrapes Myfxbook for retail sentiment on XAUUSD and provides a contrarian analysis.
    """
    print("Agent: Retail Sentiment Analyst is running...")
    
    # The public outlook page for XAUUSD on Myfxbook
    url = "https://www.myfxbook.com/community/outlook/XAUUSD"
    
    try:
        # Scrape the page using Firecrawl
        scraped_data = firecrawl_app.scrape_url(
            url=url, 
            params={'pageOptions': {'onlyMainContent': True}}
        )
        
        # Use the LLM to find the key data and provide a contrarian interpretation
        prompt = PromptCollection.RetailSentimentAnalysis(
            scraped_data=scraped_data,
        )
        
        response = llm.invoke(prompt)
        analysis = response.content

    except Exception as e:
        analysis = f"Could not analyze retail sentiment: {e}"

    return {"retail_sentiment_analysis": analysis}