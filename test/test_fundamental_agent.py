import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent.fundamental_agent import fundamental_analyst_agent

mock_state = {}

result = fundamental_analyst_agent(mock_state)
print(result)