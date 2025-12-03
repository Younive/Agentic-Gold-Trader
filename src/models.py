from typing import TypedDict, Annotated
from langchain_core.pydantic_v1 import BaseModel, Field

class AgentState(TypedDict):
    """The shared state for our gold trading agents."""
    
    # Input fields
    user_request: str
    pdf_content: str  # Content for the OI Analyst
    
    # Fields to hold the analysis from each agent
    fundamental_analysis: str
    technical_analysis: str
    market_sentiment_analysis: str
    oi_analysis: str
    retail_sentiment_analysis: str # Analysis from the Myfxbook agent
    
    # The final output field
    final_decision: str

class FundamentalAnalysisResult(BaseModel):
    sentiment_score: float = Field(description="Score between -1.0 (Bearish) and 1.0 (Bullish)")
    confidence_level: str = Field(description="Confidence Level: Low, Medium, or High")
    primary_driver: str = Field(description="The single most important factor driving this score")
    reasoning_summary: str = Field(description="Max 2 concise sentences explaining the decision")
    risk_factors: list[str] = Field(description="List 1-3 potential risks to this view")

class TechnicalAnalysisResult(BaseModel):
    market_regime: str = Field(description="Market regime: TRENDING_BULLISH, TRENDING_BEARISH, or RANGING_CHOPPY")
    suggested_trade: str = Field(description="BUY or SELL")
    confidence_level: str = Field(description="Confidence Level: Low, Medium, or High")
    reasoning: str = Field(description="Max 1 sentence summary")