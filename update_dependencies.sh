#!/usr/bin/env bash

# Activate virtual environment
source venv/bin/activate

# Check if venv is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
  echo "Virtual environment not activated. Exiting."
  exit 1
fi

# Update all dependencies
echo "Updating dependencies..."
pip install -U pypdf pytest

# Generate new requirements.txt
echo "Generating new requirements.txt file..."
pip freeze > requirements.txt

echo "Dependencies updated and requirements.txt refreshed!"
echo "Current versions:"
cat requirements.txt 