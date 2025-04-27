"""Tests for the CLI module."""

import sys
import os
from unittest.mock import patch, MagicMock
import pytest
from pdf_to_txt.cli import main

def test_cli_with_invalid_path():
    """Test CLI with an invalid path."""
    with patch('sys.argv', ['pdf-to-txt', 'nonexistent_file.pdf']), \
         patch('pdf_to_txt.cli.pdf_to_text', side_effect=ValueError("Invalid file")), \
         patch('sys.stdout', MagicMock()), \
         patch('sys.stderr', MagicMock()):
        
        assert main() == 1

def test_cli_with_directory_path():
    """Test CLI with a directory path."""
    with patch('sys.argv', ['pdf-to-txt', '/tmp']), \
         patch('os.path.isdir', return_value=True), \
         patch('sys.stdout', MagicMock()), \
         patch('sys.stderr', MagicMock()):
        
        assert main() == 1

def test_cli_with_valid_pdf_path():
    """Test CLI with a valid PDF path."""
    test_pdf = 'test.pdf'
    test_txt = 'test.txt'
    
    with patch('sys.argv', ['pdf-to-txt', test_pdf]), \
         patch('os.path.isdir', return_value=False), \
         patch('pdf_to_txt.cli.pdf_to_text', return_value=test_txt) as mock_pdf_to_text, \
         patch('sys.stdout', MagicMock()), \
         patch('sys.stderr', MagicMock()):
        
        assert main() == 0
        mock_pdf_to_text.assert_called_once_with(test_pdf, None)

def test_cli_with_output_option():
    """Test CLI with an output option."""
    test_pdf = 'test.pdf'
    test_txt = 'custom.txt'
    
    with patch('sys.argv', ['pdf-to-txt', test_pdf, '-o', test_txt]), \
         patch('os.path.isdir', return_value=False), \
         patch('pdf_to_txt.cli.pdf_to_text', return_value=test_txt) as mock_pdf_to_text, \
         patch('sys.stdout', MagicMock()), \
         patch('sys.stderr', MagicMock()):
        
        assert main() == 0
        mock_pdf_to_text.assert_called_once_with(test_pdf, test_txt) 