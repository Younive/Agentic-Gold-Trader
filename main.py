import argparse
import pdfplumber
from graph.workflow import app

def extract_text_from_pdf(file_path):
    """Opens and extracts all text from a PDF file."""
    try:
        with pdfplumber.open(file_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                # extract_text() is a method from pdfplumber
                page_text = page.extract_text()
                if page_text:
                    full_text += page_text + "\n"
            return full_text
    except Exception as e:
        print(f"Error reading or processing PDF file: {e}")
        return None

def main():
    """Main function to run the gold trading assistant."""
    
    # set up command line argument parsing
    parser = argparse.ArgumentParser(description="Agentic Gold Trading Assistant")
    parser.add_argument("pdf_path", help="The full path to the Open Interest PDF file.")
    args = parser.parse_args()

    print("Starting Gold Trading Assistant...")
    print(f"Loading PDF from: {args.pdf_path}")

    # extract text from the provided PDF file
    pdf_text_content = extract_text_from_pdf(args.pdf_path)
    
    if not pdf_text_content:
        print("Could not extract text from PDF. Exiting.")
        return

    # set the initial state for the agentic workflow
    initial_state = {
        "user_request": "Analyze the gold market based on the provided PDF.",
        "messages": [],
        "pdf_content": pdf_text_content  # Use the dynamically extracted text
    }
    
    # run the graph
    final_state = app.invoke(initial_state)
    
    # print the final report
    print("\n--- Gold Trading Assistant Final Report ---")
    print(final_state.get('final_decision', 'No decision was reached.'))
    print("-----------------------------------------")

if __name__ == "__main__":
    main()