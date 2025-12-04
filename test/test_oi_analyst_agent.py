import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent.oi_analyst_agent import oi_analyst_agent

mock_state = {}

result = oi_analyst_agent(mock_state)
print(result.oi_analysis)