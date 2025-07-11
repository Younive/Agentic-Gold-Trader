from langgraph.graph import StateGraph, END
from langgraph.graph.state import AgentState
from agent.fundamental_agent import fundamental_analyst_agent
from agent.technical_analyst_agent import technical_analyst_agent
from agent.market_sentiment_agent import market_sentiment_analyst_agent
from agent.oi_analyst_agent import oi_analyst_agent
from agent.retail_sentiment_agent import retail_sentiment_agent
from agent.strategist_agent import chief_strategist_agent

# Define the workflow graph
workflow = StateGraph(AgentState)

# Add the nodes
workflow.add_node("fundamental_analyst", fundamental_analyst_agent)
workflow.add_node("technical_analyst", technical_analyst_agent)
workflow.add_node("sentiment_analyst", market_sentiment_analyst_agent)
workflow.add_node("oi_analyst", oi_analyst_agent)
workflow.add_node("retail_sentiment_agent", retail_sentiment_agent) # <-- ADD NEW NODE
workflow.add_node("chief_strategist", chief_strategist_agent)

# Define the edges
workflow.set_entry_point("fundamental_analyst")
workflow.add_edge("fundamental_analyst", "technical_analyst")
workflow.add_edge("technical_analyst", "sentiment_analyst")
workflow.add_edge("sentiment_analyst", "oi_analyst")
workflow.add_edge("oi_analyst", "retail_sentiment_agent") # <-- ADD NEW EDGE
workflow.add_edge("retail_sentiment_agent", "chief_strategist") # <-- ADD NEW EDGE
workflow.add_edge("chief_strategist", END)

# Compile the graph
app = workflow.compile()