import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent.retail_sentiment_agent import retail_sentiment_agent

mock_state = {}

result = retail_sentiment_agent(mock_state)
print(result.retail_sentiment_analysis)