import uuid
from datetime import datetime
from trading_journal_rag.vector_db_manager import get_vector_store
import json

# initialize vector store
vectorstore = get_vector_store()

def journalist_agent(state):
    print("Agent: Journalist is Recording Trading Result...")

    trade_result = state['trading_result']

    log_content = f"Trade Result: \
        {'WIN' if trade_result['pnl'] > 0 else 'LOSS'} \
             (${trade_result['pnl']}). \
                Strategy: {trade_result['strategy']}. \
                    Context: {state['technical_analysis']}."

    trade_id = str(uuid.uuid4())

    metadata = {
        'doc_type': 'trade_log',
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'strategy': trade_result['strategy'],
        'regime': state['technical_analysis']['regime'],
        'outcome': 'WIN' if trade_result['pnl'] > 0 else 'LOSS'
    }

    vectorstore.add_documents(
        documents=[Document(page_content=log_content, metadata=metadata)],
        ids=[trade_id]
    )

    #TODO: save json as backup
    