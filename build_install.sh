#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Check if venv is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
  echo "Virtual environment not activated. Exiting."
  exit 1
fi

# Build the executable
echo "Building standalone executable with PyInstaller..."
pyinstaller --onefile pdf2txt.py

# Check if the build was successful
if [ ! -f "dist/pdf2txt" ]; then
  echo "Build failed. Executable not found."
  exit 1
fi

echo "Build successful! Executable created at dist/pdf2txt"

# Ask if user wants to install to local bin
read -p "Do you want to install the executable to ~/bin? (y/n): " install_choice

if [[ "$install_choice" == "y" || "$install_choice" == "Y" ]]; then
  # Create bin directory if it doesn't exist
  mkdir -p ~/bin
  
  # Copy the executable
  cp dist/pdf2txt ~/bin/
  chmod +x ~/bin/pdf2txt
  
  # Check if ~/bin is in PATH
  if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
    echo "~/bin is not in your PATH. Add the following line to your ~/.bashrc or ~/.zshrc:"
    echo 'export PATH="$HOME/bin:$PATH"'
  else
    echo "Executable installed to ~/bin/pdf2txt"
    echo "You can now run 'pdf2txt' from anywhere."
  fi
else
  echo "Skipping installation. You can manually copy the executable from dist/pdf2txt"
fi

echo "Done!" 