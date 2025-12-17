import sys
import os
from process_documents import load_and_tag_documents
from vector_db_manager import create_vector_store

def main():
    print("--- RAG Setup & Initialization ---")
    
    # Always rebuild DB when running setup manually to ensure consistency
    rebuild = True
    
    print("Loading and processing documents...")
    documents = load_and_tag_documents()
    
    if not documents:
        print("No documents to process. Exiting.")
        return

    print(f"Creating Vector DB with {len(documents)} chunks...")
    try:
        vectorstore = create_vector_store(documents, rebuild_db=rebuild)
        print("Success! Knowledge Base is ready.")
        
        # Optional: Test query
        print("-" * 30)
        print("Testing retrieval (doc_type: trading_log)...")
        # Note: Chroma filters syntax depends on version, usually accepts dict
        results = vectorstore.similarity_search("Losses trading", k=1, filter={"doc_type": "trading_log"})
        if results:
            print(f"Retrieved: {results[0].page_content[:100]}...")
        else:
            print("No results found for test query.")
            
    except Exception as e:
        print(f"FAILED to update Vector DB: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
