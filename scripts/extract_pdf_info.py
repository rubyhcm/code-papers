#!/usr/bin/env python3
"""
Extract information from PDF papers
"""
import sys
from pypdf import PdfReader

def extract_paper_text(pdf_path):
    """Extract all text from PDF"""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_pdf_info.py <pdf_file>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    text = extract_paper_text(pdf_path)
    
    # Print first 10000 characters to analyze structure
    print(f"=== PDF: {pdf_path} ===")
    print(f"Total length: {len(text)} characters")
    print("\n=== First 10000 characters ===")
    print(text[:10000])
