"""PDF to text conversion logic."""

import os
from pathlib import Path
import pypdf

def is_pdf(file_path):
    """Check if the file is a valid PDF.
    
    Args:
        file_path (str): Path to the file to check.
        
    Returns:
        bool: True if the file is a valid PDF, False otherwise.
    """
    if not os.path.exists(file_path):
        return False
    
    if not file_path.lower().endswith('.pdf'):
        return False
    
    try:
        with open(file_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
            # If we can read the PDF file without errors, it's a valid PDF
            return len(reader.pages) > 0
    except Exception:
        return False

def pdf_to_text(pdf_path, output_path=None):
    """Convert PDF to text and save it to a file.
    
    Args:
        pdf_path (str): Path to the PDF file.
        output_path (str, optional): Path to save the text file. Defaults to the PDF filename with .txt extension.
        
    Returns:
        str: Path to the saved text file.
        
    Raises:
        ValueError: If the file is not a valid PDF.
    """
    if not is_pdf(pdf_path):
        raise ValueError(f"'{pdf_path}' is not a valid PDF file")
    
    # If output path is not specified, use the PDF filename with .txt extension
    if not output_path:
        output_path = str(Path(pdf_path).with_suffix('.txt'))
    
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)
    
    return output_path 