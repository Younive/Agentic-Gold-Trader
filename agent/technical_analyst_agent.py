import pandas_ta as ta
from config import alpha_vantage_ts, llm
from src.prompt import PromptCollection

def technical_analyst_agent(state):
    """
    Fetches gold price data and performs comprehensive technical analysis
    using various indicators.
    """
    print("Agent: Technical Analyst is running...")
    
    try:
        
        data, _ = alpha_vantage_ts.get_intraday(symbol="GLD", outputsize='full')
        
        # Alpha Vantage data comes in reverse chronological order, so we sort it
        data = data.sort_index(ascending=True)
        data.columns = [col.split('. ')[1] if '. ' in col else col for col in data.columns]
        
        # Calculate indicators
        data.ta.ema(length=200, append=True)  # Exponential Moving Average
        data.ta.ema(length=50, append=True)   # Exponential Moving Average
        data.ta.macd(append=True)             # Moving Average Convergence Divergence
        data.ta.rsi(append=True)              # Relative Strength Index
        data.ta.atr(append=True)              # Average True Range
        data.ta.adx(append=True)              # Average Directional Index
        
        # Get the latest row of data with all indicators
        latest_data = data.iloc[-1]
        # Prepare a summary of the technical indicators for the LLM
        analysis = f"""
        **Gold (GLD) Technical Analysis Report:**

        * **Price:** ${latest_data.get('4. close', 0):.2f}
        * **EMA (50):** ${latest_data.get('EMA_50', 0):.2f}
        * **EMA (200):** ${latest_data.get('EMA_200', 0):.2f}
        * **MACD (12,26,9):** {latest_data.get('MACD_12_26_9', 0):.2f}
        * **MACD Histogram:** {latest_data.get('MACDh_12_26_9', 0):.2f}
        * **RSI (14):** {latest_data.get('RSI_14', 0):.2f}
        * **ATR (14):** {latest_data.get('ATRr_14', 0):.2f}
        * **ADX (14):** {latest_data.get('ADX_14', 0):.2f}
        """

        # 5. Use the LLM for a qualitative interpretation
        prompt = PromptCollection.TechnicalAnalysis(analysis)
        
        response = llm.invoke(prompt)
        
        # Combine the raw data summary with the LLM's interpretation
        full_analysis = f"{analysis}\n**Interpretation:**\n{response.content}"

    except Exception as e:
        full_analysis = f"Could not perform technical analysis: {e}"

    return {"technical_analysis": full_analysis}