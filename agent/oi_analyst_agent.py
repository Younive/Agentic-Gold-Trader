from config import llm
from src.prompt import PromptCollection

def oi_analyst_agent(state):
    """
    Parses text from a PDF report to find and analyze Open Interest.
    """
    print("Agent: OI Analyst is running...")

    pdf_text = state.get("pdf_content", "")

    if not pdf_text:
        return {"oi_analysis": "PDF content was not provided."}

    # New prompt designed to parse the structured text from the PDF
    prompt = PromptCollection.OpenInterestAnalysis(pdf_text)

    response = llm.invoke(prompt)
    
    return {"oi_analysis": response.content}