# Agentic-Gold-Trader

> *__Note:__ This project is for educational purposes only and is not financial advice. Financial markets are highly unpredictable, and using an automated system for trading carries significant risk. Do not use this system for live trading without extensive backtesting and a complete understanding of the risks involved.

An advanced AI-powered trading assistant that uses a team of specialized agents to perform a multi-faceted analysis of the gold market (XAU/USD). This project leverages modern agentic AI frameworks to provide a synthesized trading suggestion based on fundamental, technical, sentiment, and institutional data.

## 📋 Features

* **Multi-Agent System:** Utilizes a team of agents, each with a specific role, orchestrated by `LangGraph`.
* **Fundamental News Analysis:** Summarizes key financial news relevant to gold.
* **Net Sentiment Analysis:** Combines news summaries with live web search results to gauge overall market sentiment.
* **Retail Sentiment Analysis:** Scrapes Myfxbook to use retail trader positioning as a contrarian indicator.
* **Comprehensive Technical Analysis:** Calculates and interprets a wide range of indicators (EMA, MACD, RSI, ATR, ADX) using `pandas-ta`.
* **Institutional Sentiment:** Parses `Open Interest (OI)` data from PDF reports to understand institutional positioning.
* **Dynamic PDF Processing:**  Accepts and analyzes data directly from user-provided PDF files.

## 🛠️ Technology Stack

* **Orchestration:** LangGraph
* **LLM:** Google Gemini (via langchain_google_genai)
* **Web Scraping & Search:** Firecrawl
* **Technical Analysis:** pandas-ta
* **Chart Data:** Alpha Vantage
* **PDF Processing:** pdfplumber

## 📂 Project Structure

```
Agentic-Gold-Trader/
├── .env
├── requirements.txt
├── README.md
├── main.py
├── config.py
├── src/
│   ├── __init__.py
│   ├── firecrawl.py
│   ├── models.py    # contain AgentState
│   └── prompt.py
├── agent/
│   ├── __init__.py
│   ├── fundamental_agent.py
│   ├── technical_agent.py
│   ├── sentiment_agent.py
│   ├── oi_agent.py
│   ├── retail_sentiment_agent.py
│   └── strategist_agent.py
├── Notebook/
|   └── experiments.ipynb
└── graph/
    ├── __init__.py
    └── workflow.py
```

## 🚀 Getting Started

**1. Prerequisites**
* Python 3.8+
* API Keys for:
  * Google AI Studio (for Gemini)
  * Firecrawl
  * Alpha Vantage
 
**2. Installation**

1. Clone the repository (or set up your project folder):
```
git clone git@github.com:Younive/Agentic-Gold-Trader.git
cd Agentic-Gold-Trader
```

2. Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```
pip install -r requirements.txt
```

**3. Configuration**

1. Create a file named `.env` in the root of the project directory.
2. Add your API keys to this file:
```
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
FIRECRAWL_API_KEY="YOUR_FIRECRAWL_API_KEY"
ALPHA_VANTAGE_API_KEY="YOUR_ALPHA_VANTAGE_API_KEY"
```

**4. Running the Application**
The application requires the path to a PDF file containing `Open Interest (OI)` data to be passed as a command-line argument.
You can get `Open Interest (OI)` report via https://www.cmegroup.com/tools-information/quikstrike/options-open-interest-profile.html product: Gold

```
python main.py "/path/to/your/OpenInterest.pdf"
```

## 💡 Improvement Suggestions

* **Conditional Agent Workflow**
Introduce conditional edges in the LangGraph workflow. For example, if the Fundamental and Technical agents strongly disagree, the graph could route to a special "Conflict Resolution" agent that performs a deeper analysis before presenting the data to the Chief Strategist.

* **Consider Switching LLM**
Switching to a large language model (LLM) that has been specifically fine-tuned for financial trading can work, often leading to significant improvements in specific tasks. E.g. Improved Sentiment Analysis: A general LLM might see "strong Q2 report" as positive. A fine-tuned model would understand that a "strong dollar report" is often a bearish signal for gold. It can capture these complex, inverse relationships more reliably.

* **Persistent State and Memory**
Integrate a database (like SQLite or a vector database) to store the results of each run. This would give the agents a "memory," allowing them to analyze trends over time (e.g., "Retail sentiment has become increasingly bullish over the last 7 days").

* **Backtesting**
Build a framework to run the agent against historical data. This would involve feeding it historical news, price data, and sentiment for a specific day in the past and recording its decision. Running this over months or years of data is the only way to statistically evaluate the strategy's performance.

* **Interactive Frontend**
Create a web interface using Streamlit or Flask. This would allow you to visualize the output from each agent, see the final decision in a clean dashboard, and potentially input parameters without using the command line.

* **Real-Time Data Integration**
For a more serious application, replace the end-of-day REST APIs with real-time data feeds using WebSockets for price data and a paid news API (like NewsAPI or Alpaca) for instant news analysis.

## ⚠️ Disclaimer
This project is for educational purposes only. Financial markets are highly unpredictable, and using an automated system for trading carries significant risk. The author is not responsible for any financial losses incurred. Do not use this system for live trading without extensive backtesting and a complete understanding of the risks involved.
