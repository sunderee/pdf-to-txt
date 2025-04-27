# PDF to TXT

A simple command-line tool to convert PDF files to plain text.

> [!NOTE]  
> This tool was developed on macOS. If you're on Linux, on paper everything should work, but please raise an issue in case you're experiencing problems. If you're on Windows, I'm terribly sorry, but I have zero experience with Python development on that operating system. Please contribute if you feel like it. I'd love to learn.

## Features

- Validate that the input file is a valid PDF
- Convert PDF files to plain text
- Specify custom output file name and location
- Simple and easy to use CLI

## Installation Options

You have two ways to use this tool:

### Option 1: Install as a standalone executable (recommended for most users)

This option allows you to run the tool without needing Python or any dependencies installed.

#### Using the provided build script

The easiest way to install the executable is to use the provided script:

```bash
# Clone the repository
git clone git@github.com:sunderee/pdf-to-txt.git
cd pdf-to-txt

# Make the script executable
chmod +x build_install.sh

# Run the script
./build_install.sh
```

The script will:
1. Build the executable
2. Ask if you want to install it to your `~/bin` directory
3. Check if `~/bin` is in your PATH and provide instructions if it's not

#### Manual installation

If you prefer to build and install manually:

1. Build the executable:
```bash
git clone git@github.com:sunderee/pdf-to-txt.git
cd pdf-to-txt
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pyinstaller --onefile pdf2txt.py
```

2. Install the executable:
```bash
# Install for all users on your machine
sudo cp dist/pdf2txt /usr/local/bin/
sudo chmod +x /usr/local/bin/pdf2txt

# OR install for current user only
cp dist/pdf2txt ~/bin/
chmod +x ~/bin/pdf2txt
```

### Option 2: Set up for development

If you want to modify the tool or contribute to its development:

1. Clone the repository:
```bash
git clone git@github.com:sunderee/pdf-to-txt.git
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

4. Run the tool directly:
```bash
python pdf2txt.py path/to/your/file.pdf
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
# Make sure you're in the virtual environment
source venv/bin/activate

# Run tests
python -m pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
