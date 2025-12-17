import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from firecrawl import FirecrawlApp

# Load environment variables from .env file
load_dotenv()

# Initialize the LLM client
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# Initialize the Firecrawl client
firecrawl_app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])

# Vector DB configuration
VECTOR_DB_DIR = os.path.join(os.path.dirname(__file__), "trading_journal_rag", "vector_db")

# Document Preprocessing
KNOWLEDGE_BASE_DIR = os.path.join(os.path.dirname(__file__), "trading_journal_rag", "knowledge_base")
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Initialize embedding model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
