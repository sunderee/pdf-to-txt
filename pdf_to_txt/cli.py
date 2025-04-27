"""Command-line interface for the PDF to text converter."""

import os
import sys
import argparse
from pdf_to_txt.converter import pdf_to_text

def main():
    """
    Main entry point for the PDF to text converter CLI.
    
    Returns:
        int: 0 for success, 1 for failure.
    """
    parser = argparse.ArgumentParser(description='Convert PDF files to plain text.')
    parser.add_argument('path', nargs='?', default=os.getcwd(), 
                        help='Path to the PDF file or directory (defaults to current directory)')
    parser.add_argument('-o', '--output', help='Output filename (defaults to input filename with .txt extension)')
    
    args = parser.parse_args()
    path = args.path
    
    if os.path.isdir(path):
        print(f"'{path}' is a directory. Please provide a PDF file.")
        return 1
    
    try:
        output_file = pdf_to_text(path, args.output)
        print(f"Successfully converted '{path}' to '{output_file}'")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 