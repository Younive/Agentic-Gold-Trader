from config import llm
from src.prompt import PromptCollection
import pypdf
import os
from scr.models import TradingState

def oi_analyst_agent(state):
    """
    Parses text from a PDF report to find and analyze Open Interest.
    """
    print("Agent: OI Analyst is running...")

    pdf_path = os.path.join(os.getcwd(), "Vol2Vol.pdf")
    
    if not os.path.exists(pdf_path):
        # Fallback to checking if it's just in the current directory if getcwd is different
        if os.path.exists("Vol2Vol.pdf"):
            pdf_path = "Vol2Vol.pdf"
        else:
            return {"oi_analysis": f"PDF file not found at {pdf_path}"}

    print(f"Reading PDF from: {pdf_path}")
    
    pdf_text = ""
    try:
        reader = pypdf.PdfReader(pdf_path)
        for page in reader.pages:
            pdf_text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return {"oi_analysis": f"Error reading PDF: {e}"}

    if not pdf_text.strip():
        return {"oi_analysis": "PDF content was empty or could not be read."}

    # New prompt designed to parse the structured text from the PDF
    prompt = PromptCollection.OpenInterestAnalysis(pdf_text)

    response = llm.invoke(prompt)
    
    state["oi_analysis"] = response.content
    return state