from config import llm
from src.prompt import PromptCollection

def strategist_agent(state):
    print("Agent: Chief Strategist is making a decision...")
    
    prompt = PromptCollection.CheifStatistician(
        fundamental_analysis=state['fundamental_analysis'],
        technical_analysis=state['technical_analysis'],
        market_sentiment_analysis=state['market_sentiment_analysis'],
        oi_analysis=state['oi_analysis']
    )
    
    response = llm.invoke(prompt)
    state["final_decision"] = response.content
    return state