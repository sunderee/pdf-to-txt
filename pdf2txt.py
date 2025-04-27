#!/usr/bin/env python3
"""PDF to text converter CLI script."""

import os
import sys

# Add the parent directory to sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from pdf_to_txt.cli import main

if __name__ == "__main__":
    main() 