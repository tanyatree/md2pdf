# Markdown to PDF Converter 📄➡️📕

A simple and powerful CLI tool to convert Markdown files to beautifully formatted PDFs with full emoji support! 🎉

## Features ✨

- **Full Markdown Support**: Headers, lists, tables, code blocks, blockquotes, and more
- **Emoji Support**: Native emoji rendering 😊 🚀 ✅
- **Syntax Highlighting**: Beautiful code blocks with syntax highlighting
- **Custom Styling**: Apply custom CSS for personalized PDF styling
- **Clean Output**: Professional-looking PDFs with GitHub-inspired styling
- **Easy to Use**: Simple command-line interface

## Installation 🚀

### Option 1: Install from Source (Recommended)

1. **Clone this repository**:

```bash
git clone https://github.com/tanyatree/md2pdf.git
cd md2pdf
```

2. **Install the package**:

```bash
pip install -e .
```

This installs `md2pdf` as a global command that you can use from anywhere!

### Option 2: Install from PyPI (when published)

```bash
pip install md2pdf
```

### System Dependencies

WeasyPrint requires some system dependencies. On macOS, install them via Homebrew:

```bash
brew install python3 cairo pango gdk-pixbuf libffi
```

For other platforms, check the [WeasyPrint installation guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation).

## Usage 💻

### Basic Usage

Convert a markdown file to PDF (output will have the same name with `.pdf` extension):

```bash
md2pdf document.md
```

### Specify Output File

```bash
md2pdf document.md -o output.pdf
```

### Custom CSS Styling

Apply custom CSS from a file:

```bash
md2pdf document.md --css custom.css
```

Or provide CSS inline:

```bash
md2pdf document.md --css "body { font-size: 14pt; }"
```

### Verbose Output

```bash
md2pdf document.md -v
```

### All Options

```bash
md2pdf --help
```

## Examples 📝

### Example Markdown File

Create a file called `example.md`:

```markdown
# My Document 📚

This is a **bold** statement and this is *italic*.

## Features

- Bullet points work great ✅
- Emojis are fully supported 🎉
- Tables look professional

## Code Example

def hello_world():
    print("Hello, World! 🌍")

## Table

| Feature | Supported |
|---------|-----------|
| Emojis  | ✅ Yes    |
| Tables  | ✅ Yes    |
| Code    | ✅ Yes    |

> This is a blockquote with important information! 💡
```

Then convert it:

```bash
md2pdf example.md
```

This will create `example.pdf` in the same directory.

## Supported Markdown Features 📋

- ✅ Headers (H1-H6)
- ✅ Bold and italic text
- ✅ Lists (ordered and unordered)
- ✅ Links
- ✅ Images
- ✅ Code blocks with syntax highlighting
- ✅ Inline code
- ✅ Tables
- ✅ Blockquotes
- ✅ Horizontal rules
- ✅ Emojis and Unicode characters

## Custom Styling 🎨

You can customize the PDF appearance by providing your own CSS. Create a `custom.css` file:

```css
body {
    font-family: 'Georgia', serif;
    font-size: 12pt;
    color: #2c3e50;
}

h1 {
    color: #e74c3c;
    font-size: 2.5em;
}

code {
    background-color: #ecf0f1;
    color: #c0392b;
}
```

Then apply it:

```bash
md2pdf document.md --css custom.css
```

## Dependencies 📦

- **markdown**: Converts Markdown to HTML
- **weasyprint**: Converts HTML to PDF with excellent CSS support
- **pygments**: Provides syntax highlighting for code blocks
- **click**: Creates the command-line interface

## Troubleshooting 🔧

### WeasyPrint Installation Issues

If you encounter issues installing WeasyPrint on macOS, ensure you have the required system libraries:

```bash
brew install python3 cairo pango gdk-pixbuf libffi
```

For other platforms, check the [WeasyPrint installation guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation).

### Emoji Not Displaying

Emojis should work out of the box on most systems. If they don't appear, ensure your system has fonts that support emoji characters installed.

## License 📄

This project is open source and available for personal and commercial use.

## Contributing 🤝

Feel free to submit issues, fork the repository, and create pull requests for any improvements!

---

Made with ❤️ and Python by Tanya Tree
