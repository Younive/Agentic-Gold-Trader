import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from firecrawl import FirecrawlApp
from alpha_vantage.timeseries import TimeSeries

# Load environment variables from .env file
load_dotenv()

# Initialize the LLM client
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Initialize the Firecrawl client
firecrawl_app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])

# Initialize the Alpha Vantage client
alpha_vantage_ts = TimeSeries(key=os.environ["ALPHA_VANTAGE_API_KEY"], output_format='pandas')