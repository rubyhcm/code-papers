#!/usr/bin/env python3
"""
Extract text from PDF files for analysis
"""
import sys
from pypdf import PdfReader

def extract_pdf_text(pdf_path, output_path=None, max_pages=None):
    """Extract text from PDF"""
    try:
        reader = PdfReader(pdf_path)
        
        total_pages = len(reader.pages)
        print(f"Total pages: {total_pages}")
        
        pages_to_extract = max_pages if max_pages else total_pages
        
        text_content = []
        for i in range(min(pages_to_extract, total_pages)):
            page = reader.pages[i]
            text = page.extract_text()
            text_content.append(f"=== PAGE {i+1} ===\n{text}\n")
        
        full_text = "\n".join(text_content)
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_text)
            print(f"Extracted text saved to: {output_path}")
        
        return full_text
    
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf_text.py <pdf_file> [output_file] [max_pages]")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    max_pages = int(sys.argv[3]) if len(sys.argv) > 3 else None
    
    extract_pdf_text(pdf_file, output_file, max_pages)
