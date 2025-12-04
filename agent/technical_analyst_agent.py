import pandas_ta as ta
import numpy as np
from config import llm
from src.prompt import PromptCollection
from src.fetch_mt5_data import get_data
from src.models import TradingState
from smartmoneyconcepts import smc
from scipy.signal import find_peaks

def technical_analyst_agent(state):
    """
    Fetches gold price data and performs comprehensive technical analysis
    using various indicators.
    """
    print("Agent: Technical Analyst is running...")
    
    try:
        
        print("Fetching data...")
        data = get_data(timeframe_str='H1')
        
        print("Calculating indicators...")
        # Calculate indicators
        data.ta.ema(length=100, append=True)  # Exponential Moving Average
        data.ta.ema(length=50, append=True)   # Exponential Moving Average
        data.ta.macd(append=True)             # Moving Average Convergence Divergence
        data.ta.rsi(append=True)              # Relative Strength Index
        data.ta.atr(length=14,append=True)              # Average True Range
        data.ta.adx(append=True)              # Average Directional Index
        data.ta.stoch(k=9, d=3, ksmooth=3, append=True)   # Stochastic Oscillator

        # find support and resistance
        resistance_idx, _ = find_peaks(data['high'], distance=20)
        support_idx, _ = find_peaks(-data['low'], distance=20)
        
        current_support = data.iloc[support_idx]['low'].tail(3).values.tolist()
        current_resistance = data.iloc[resistance_idx]['high'].tail(3).values.tolist()

        # calculate order blocks
        swings = smc.swing_highs_lows(data, swing_length=1)
        ob = smc.ob(data, swings)
        last_ob = ob[ob['OB'].notna()].iloc[-1]
        ob_info = {
            "ob": "BULLISH" if last_ob['OB'] == 1 else "BEARISH",
            "top": last_ob['Top'],
            "bottom": last_ob['Bottom'],
            "ob_volume": last_ob['OBVolume'],
            "percentage": last_ob['Percentage']
        }

        # calculate fibonacci level
        lookback = data.tail(100)
        swing_high = lookback['high'].max()
        swing_low = lookback['low'].min()
        diff = swing_high - swing_low
        
        fib_levels = {
            "0.0": swing_high,
            "0.236": swing_high - 0.236 * diff,
            "0.382": swing_high - 0.382 * diff,
            "0.5": swing_high - 0.5 * diff,
            "0.618": swing_high - 0.618 * diff,
            "0.764": swing_high - 0.764 * diff,
            "0.886": swing_high - 0.886 * diff,
            "1.0": swing_low
        }

        # recent data for llm
        recent_data = data.tail(10).to_dict(orient='records')

        combine_data = {
            "recent_data": recent_data,
            "ob_info": ob_info,
            "support": current_support,
            "resistance": current_resistance,
            "fib_levels": fib_levels
        }

        # Use the LLM for a qualitative interpretation
        prompt = PromptCollection.TechnicalAnalysis(combine_data)
        
        response = llm.invoke(prompt)

        state["technical_analysis"] = response.content

    except Exception as e:
         print(f"Could not perform technical analysis: {e}")

    return state