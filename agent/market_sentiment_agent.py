from config import llm, firecrawl_app
from src.prompt import PromptCollection

def market_sentiment_analyst_agent(state):
    """
    Calculates the net sentiment for gold by combining a news summary
    with fresh web search results.
    """
    print("Agent: General Sentiment Analyst is running...")
    
    # Perform a fresh web search for current sentiment
    search_results = firecrawl_app.search("gold market sentiment today")
    
    # The news summary comes from the previous agent's output
    news_summary = state['fundamental_analysis']
    
    # New prompt to synthesize both sources into a net sentiment score
    prompt = PromptCollection.MarketSentimentAnalysis(news_summary, search_results)
    
    response = llm.invoke(prompt)
    
    return {"market_sentiment_analysis": response.content}