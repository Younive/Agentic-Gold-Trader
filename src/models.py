from typing import TypedDict, Annotated

class AgentState(TypedDict):
    """The shared state for our gold trading agents."""
    
    # Input fields
    user_request: str
    pdf_content: str  # Content for the OI Analyst
    
    # This field accumulates messages, but isn't used by our current agents
    messages: Annotated[list, lambda x, y: x + y]
    
    # Fields to hold the analysis from each agent
    fundamental_analysis: str
    technical_analysis: str
    market_sentiment_analysis: str
    oi_analysis: str
    retail_sentiment_analysis: str # Analysis from the Myfxbook agent
    
    # The final output field
    final_decision: str