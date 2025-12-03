import pandas_ta as ta
from config import llm
from src.prompt import PromptCollection
from src.fetch_mt5_data import get_data
from src.models import TechnicalAnalysisResult

def technical_analyst_agent(state):
    """
    Fetches gold price data and performs comprehensive technical analysis
    using various indicators.
    """
    print("Agent: Technical Analyst is running...")
    
    try:
        
        data = get_data()
        
        # Calculate indicators
        data.ta.ema(length=100, append=True)  # Exponential Moving Average
        data.ta.ema(length=50, append=True)   # Exponential Moving Average
        data.ta.macd(append=True)             # Moving Average Convergence Divergence
        data.ta.rsi(append=True)              # Relative Strength Index
        data.ta.atr(append=True)              # Average True Range
        data.ta.adx(append=True)              # Average Directional Index

        # recent data for llm
        recent_data = data.tail(5).to_dict(orient='records')

        # Use the LLM for a qualitative interpretation
        prompt = PromptCollection.TechnicalAnalysis(recent_data)
        
        technical_analysis = llm.with_structured_output(TechnicalAnalysisResult)
        response = technical_analysis.invoke(prompt)

    except Exception as e:
         print(f"Could not perform technical analysis: {e}")

    return response