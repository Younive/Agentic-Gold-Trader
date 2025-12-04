import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from firecrawl import FirecrawlApp

# Load environment variables from .env file
load_dotenv()

# Initialize the LLM client
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# Initialize the Firecrawl client
firecrawl_app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])
