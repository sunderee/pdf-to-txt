# PDF to TXT

A simple command-line tool to convert PDF files to plain text.

## Features

- Validate that the input file is a valid PDF
- Convert PDF files to plain text
- Specify custom output file name and location
- Simple and easy to use CLI

## Setup

1. Clone the repository:
```bash
git clone https://github.com/sunderee/pdf-to-txt.git
cd pdf-to-txt
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Make the script executable:
```bash
chmod +x pdf2txt.py
```

5. Create an alias for easy access from anywhere (add to your ~/.bashrc or ~/.zshrc):
```bash
alias pdf2txt='/path/to/pdf-to-txt/pdf2txt.py'
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

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output filename (defaults to input filename with .txt extension)
```

## Development

### Running tests

```bash
python3 -m pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 