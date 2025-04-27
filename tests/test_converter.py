"""Tests for the converter module."""

import os
import tempfile
import pytest
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock
from pdf_to_txt.converter import is_pdf, pdf_to_text

def test_is_pdf_with_nonexistent_file():
    """Test is_pdf with a nonexistent file."""
    assert not is_pdf('nonexistent_file.pdf')

def test_is_pdf_with_non_pdf_file():
    """Test is_pdf with a non-PDF file."""
    # Create a temporary file that is not a PDF
    with tempfile.NamedTemporaryFile(suffix='.txt') as tmp:
        tmp.write(b'This is not a PDF file')
        tmp.flush()
        assert not is_pdf(tmp.name)

def test_pdf_to_text_with_invalid_file():
    """Test pdf_to_text with an invalid file."""
    with pytest.raises(ValueError):
        pdf_to_text('nonexistent_file.pdf')

def test_pdf_to_text_output_path():
    """Test that pdf_to_text returns the correct output path when not specified."""
    sample_pdf = 'sample.pdf'
    expected_output = str(Path(sample_pdf).with_suffix('.txt'))
    
    # Create mock objects
    mock_reader = MagicMock()
    mock_page = MagicMock()
    mock_page.extract_text.return_value = "Sample text"
    mock_reader.pages = [mock_page]
    
    # Patch the necessary functions and classes
    with patch('pdf_to_txt.converter.is_pdf', return_value=True), \
         patch('builtins.open', mock_open()), \
         patch('pypdf.PdfReader', return_value=mock_reader):
        
        # Now test the function
        result = pdf_to_text(sample_pdf)
        assert result == expected_output 