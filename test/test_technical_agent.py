import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent.technical_analyst_agent import technical_analyst_agent

mock_state = {}

result = technical_analyst_agent(mock_state)
print(result)