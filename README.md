# PDF to TXT

A simple command-line tool to convert PDF files to plain text.

> [!NOTE]  
> This tool was developed on macOS. If you're on Linux, on paper everything should work, but please raise an issue in case you're experiencing problems. If you're on Windows, I'm terribly sorry, but I have zero experience with Python development on that operating system. Please contribute if you feel like it. I'd love to learn.

## Features

- Validate that the input file is a valid PDF
- Convert PDF files to plain text
- Specify custom output file name and location
- Simple and easy to use CLI

## Setup and Installation

### Setting up the development environment

1. Clone the repository:
```bash
git clone https://github.com/username/pdf-to-txt.git
cd pdf-to-txt
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Building a standalone executable

#### Option 1: Using the provided build script

The easiest way to build and install the executable is to use the provided script:

```bash
# Make the script executable
chmod +x build_install.sh

# Run the script
./build_install.sh
```

The script will:
1. Build the executable
2. Ask if you want to install it to your `~/bin` directory
3. Check if `~/bin` is in your PATH and provide instructions if it's not

#### Option 2: Manual build

To create a standalone executable that can be run from anywhere without Python dependencies:

```bash
# Make sure you're in the virtual environment
source venv/bin/activate

# Build the executable
pyinstaller --onefile pdf2txt.py
```

This will create a standalone executable in the `dist` directory. You can copy this executable anywhere on your system and run it without needing Python or any dependencies installed.

### Installing the executable manually

1. Copy the executable to a directory in your PATH, for example:
```bash
# Provide the executable to all users on your machine
sudo cp dist/pdf2txt /usr/local/bin/

# Alternatively, install it to current user's bin directory
cp dist/pdf2txt ~/bin/
```

2. Make it executable (on macOS/Linux):
```bash
# If you copied to common /usr/local/bin, use this command
sudo chmod +x /usr/local/bin/pdf2txt

# If you copied to user bin, use this command instead
chmod +x ~/bin/pdf2txt
```

## Usage

### Basic usage

```bash
pdf2txt path/to/your/file.pdf
```

This will convert the PDF file to plain text and save it as `file.txt` in the same directory.

### Specify output file

```bash
pdf2txt path/to/your/file.pdf -o output.txt
```

This will save the text as `output.txt` instead of using the default name.

### CLI Options

```
usage: pdf2txt [-h] [-o OUTPUT] [path]

Convert PDF files to plain text.

positional arguments:
  path                  Path to the PDF file or directory (defaults to current directory)

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output filename (defaults to input filename with .txt extension)
```

## Development

### Running tests

```bash
python -m pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 