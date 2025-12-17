from config import llm
from src.prompt import PromptCollection
from trading_journal_rag.vector_db_manager import get_vector_store
from langchain.schema import Document
from typing import List

def retrieve_vectordb(query: str, doc_type: str) -> List[Document]:
    """
    Search, filter and return information from the knowledge base.
    """
    try:
        # Load existing vector store (do not rebuild)
        vectorstore = get_vector_store()
        
        # filter by trade_log or system_crash
        docs = vectorstore.similarity_search(query, k=3, filter={"doc_type": doc_type})
        if not docs:
            return []
        return docs
    except Exception as e:
        print(f"Warning: Failed to retrieve from vector DB: {e}")
        return []

def format_rag_context(docs: List[Document]) -> str:
    if not docs:
        return "No relevant past record found."
    
    formatted = []
    for doc in docs:
        outcome = doc.metadata.get('outcome', 'Unknown')
        strategy = doc.metadata.get('strategy', 'Unknown')
        regime = doc.metadata.get('regime', 'Unknown')

        entry = f"[Outcome: {outcome}, Strategy: {strategy}, Regime: {regime}, Content: {doc.page_content}]"
        formatted.append(entry)
    
    return "\n".join(formatted)

def strategist_agent(state):
    print("Agent: Chief Strategist is making a decision...")

    tech_signal = state.get("technical_analysis", {}).get("signal", "NEUTRAL") 
    market_regime = state.get("technical_analysis", {}).get("regime", "General")

    trade_query = f"Losses using {tech_signal} strategy in {market_regime} market"
    past_trade = retrieve_vectordb(query=trade_query, doc_type="trade_log")

    health_query = f"System health warnings in {market_regime} market"
    system_health = retrieve_vectordb(query=health_query, doc_type="system_crash")

    rule_query = f"Rules about {tech_signal} trading"
    rule = retrieve_vectordb(query=rule_query, doc_type="rule_log")

    rag_context_str = f"""
    --- PAST TRADE PERFORMANCE (Learning from Mistakes) ---
    {format_rag_context(past_trade)}
    
    --- SYSTEM HEALTH WARNINGS (Circuit Breakers) ---
    {format_rag_context(system_health)}

    --- CONSTITUTIONAL RULES (Hard Limits) ---
    {format_rag_context(rule)}
    """
    
    print(f"RAG Context Loaded: {len(rag_context_str)} chars")

    prompt = PromptCollection.CheifStatistician(
        fundamental_analysis=state['fundamental_analysis'],
        technical_analysis=state['technical_analysis'],
        market_sentiment_analysis=state['market_sentiment_analysis'],
        oi_analysis=state['oi_analysis'],
        rag_data=rag_context_str
    )
    
    response = llm.invoke(prompt)
    state["final_decision"] = response.content
    return state