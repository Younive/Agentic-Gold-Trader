class PromptCollection:
    """Collection of prompts for the Agentic Gold Trader."""

    @staticmethod
    def TechnicalAnalysis(analysis: str) -> str:
        return f"""
        Analyze the following technical indicator data for Gold (GLD) and provide a concise interpretation.
        Based *only* on this data, what is the likely short-term trend?

        **Indicator Data:**
        {analysis}

        **Interpretation Guide:**
        - **Price vs EMA:** Is the price above or below the 50-day EMA? Above is generally bullish.
        - **MACD Histogram:** Is it positive or negative? Positive suggests bullish momentum.
        - **RSI:** Is it below 30 (oversold), above 70 (overbought), or neutral?
        - **ATR:** This represents volatility. Just state the value.
        - **ADX:** Is it above 25? If so, it indicates a strong trend (either up or down). If below 20, the trend is weak.
        """
    
    @staticmethod
    def FundamentalAnalysis(scraped_data: str) -> str:
        return f"""
        Analyze the following fundamental data for Gold (GLD) and provide a concise interpretation.
        Based *only* on this data, what is the likely short-term trend?

        **Fundamental Data:**
        {scraped_data}

        **Interpretation Guide:**
        - **Economic Indicators:** Focus on inflation rates, interest rates, and geopolitical events.
        - **Supply and Demand:** Are there any significant changes in gold supply or demand?
        - **Market Conditions:** Consider how these factors might influence gold prices in the short term.
        """
    
    @staticmethod
    def MarketSentimentAnalysis(news_summary: str, search_results: str) -> str:
        return f"""
        You are a market sentiment analyst. Your goal is to determine the net sentiment for gold (XAU/USD).

        You have two sources of information:
        1.  **News Summary:** A factual summary of recent major financial news.
        2.  **Web Search Results:** Current articles and discussions about gold market sentiment.

        Analyze both sources and synthesize them into a "Net Sentiment" score. State whether the overall sentiment is **Bullish**, **Bearish**, or **Neutral** and provide a brief justification for your conclusion based on the combined information.

        ---
        **Source 1: News Summary**
        {news_summary}
        ---
        **Source 2: Web Search Results**
        {search_results}
        ---
        """
    
    @staticmethod
    def RetailSentimentAnalysis(retail_sentiment: str) -> str:
        return f"""
        Analyze the following retail sentiment data for Gold (GLD) and provide a concise interpretation.
        Based *only* on this data, what is the likely short-term trend?

        **Retail Sentiment Data:**
        {retail_sentiment}

        **Interpretation Guide:**
        - **Retail Sentiment Score:** Is it positive, negative, or neutral? Positive suggests bullish sentiment.
        - **Volume of Retail Activity:** High volume with positive sentiment indicates strong retail interest.
        - **Recent Trends:** Are there any notable changes in retail sentiment over the past week?
        """
    
    @staticmethod
    def OpenInterestAnalysis(pdf_text: str) -> str:
        return f"""
        You are a data analyst. From the provided text of an Open Interest report, perform the following tasks:

        1.  **Find Total Calls OI:** Locate the "Calls" table and find the total "OPEN INTEREST" for all strike prices combined.
        2.  **Find Total Puts OI:** Locate the "Puts" table and find the total "OPEN INTEREST" for all strike prices combined.
        3.  **Calculate Total OI:** Sum the total Calls and Puts Open Interest together.
        4.  **Analyze and Interpret:** Based on the total open interest, provide a brief analysis. A high number of open interest contracts indicates high liquidity and trader attention.

        **Report Text:**
        ---
        {pdf_text}
        ---

        Provide the total OI number and your brief interpretation.
        """
    
    @staticmethod
    def CheifStatistician(fundamental_analysis: str, technical_analysis: str, sentiment_analysis: str, oi_analysis:str) -> str:
        return f"""
        You are the Chief Statistician for the Agentic Gold Trader. Your task is to analyze the provided data and provide a concise summary of the likely short-term trend for Gold (GLD).

        **Fundamental Analysis:**
        {fundamental_analysis}

        **Technical Analysis:**
        {technical_analysis}

        **Market Sentiment Analysis:**
        {sentiment_analysis}

        **Open Interest Analysis:**
        {oi_analysis}

        Based on this data, what is the likely short-term trend for Gold (GLD)? 
        Provide your final decision as one of these three options: GO LONG (BUY), GO SHORT (SELL), or STAY NEUTRAL (HOLD).
        """