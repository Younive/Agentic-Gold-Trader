import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from typing import List
from langchain_core.documents import Document
from config import KNOWLEDGE_BASE_DIR

def load_and_tag_documents():
    documents = []
    
    for filename in os.listdir(KNOWLEDGE_BASE_DIR):
        file_path = os.path.join(KNOWLEDGE_BASE_DIR, filename)
        
        if 'constitution' in filename:
            assign_type = 'constitution'
        elif 'system_health' in filename:
            assign_type = 'system_crash'
        elif 'trading_log' in filename:
            assign_type = 'trading_log'
        elif 'seed_mistakes' in filename:
            assign_type = 'trading_log'
        else:
            print(f'skipping unknown file: {filename}')
            continue
        
        with open(file_path, 'r') as file:
            data = json.load(file)

        for entry in data:
            final_metadata = entry.get('metadata', {}).copy()
            final_metadata['doc_type'] = assign_type
            
            doc = Document(page_content=entry['page_content'], metadata=final_metadata)
            documents.append(doc)
    
    return documents