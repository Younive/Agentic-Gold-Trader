from typing import TypedDict, Annotated
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.messages import BaseMessage
from typing import List, Dict

class TradingState(TypedDict):
    # --- CONVERSATION MEMORY (Standard) ---
    messages: List[BaseMessage]
    
    # --- DATA LAYER (Window Memory) ---
    ticker: str
    current_price: float
    price_history: List[Dict]  # Last 100 candles for calculating indicators
    raw_news: List[str]        # Last 24h news headlines
    
    # --- INTELLIGENCE LAYER (Agent Outputs) ---
    # Python-calculated levels (Support, Res, OrderBlocks)
    technical_analysis: Dict 
    # LLM-synthesized sentiment (Bullish/Bearish + Reasoning)
    fundamental_analysis: Dict 
    
    # --- DECISION LAYER ---
    supervisor_decision: str   # "BUY", "SELL", "WAIT"
    supervisor_reasoning: str
    
    # --- EXECUTION LAYER (Calculated by Python, not LLM) ---
    entry_price: float
    stop_loss: float
    take_profit: float