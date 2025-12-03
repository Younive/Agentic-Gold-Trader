import MetaTrader5 as mt5
import pandas as pd
import datetime as dt
import pytz

import pandas as pd
import MetaTrader5 as mt5
import datetime as dt
import pytz

def get_data(symbol: str = 'XAUUSD', timeframe_str: str = 'H1', num_candles: int = 250) -> pd.DataFrame:
    """
    Fetches data from MT5.
    
    Args:
        symbol: Symbol name (e.g., 'XAUUSD').
        timeframe_str: Timeframe string ('H1', 'M15', etc.).
        num_candles: Number of candles to fetch.
        
    Returns:
        DataFrame with OHLCV data.
    """
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        return pd.DataFrame()

    # Map timeframe string to MT5 constant
    tf_map = {
        'M1': mt5.TIMEFRAME_M1,
        'M5': mt5.TIMEFRAME_M5,
        'M15': mt5.TIMEFRAME_M15,
        'M30': mt5.TIMEFRAME_M30,
        'H1': mt5.TIMEFRAME_H1,
        'H4': mt5.TIMEFRAME_H4,
        'D1': mt5.TIMEFRAME_D1,
    }
    
    tf = tf_map.get(timeframe_str, mt5.TIMEFRAME_H1)
    
    # Fetch data
    data = mt5.copy_rates_from_pos(symbol, tf, 0, num_candles)
        
    if data is None:
        print(f"No data received for {symbol}")
        return pd.DataFrame()
        
    df = pd.DataFrame(data)
    df['time'] = pd.to_datetime(df['time'], unit='s') # Keep UTC for simplicity in backtest
    df.rename(columns={
        'time':'Date', 
        'tick_volume':'volume'}, inplace=True)
    df.set_index('Date', inplace=True)
    return df

    