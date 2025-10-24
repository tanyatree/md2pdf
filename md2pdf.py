#!/usr/bin/env python3
"""
Markdown to PDF Converter CLI Tool
Converts markdown files to PDF with full emoji and formatting support.
"""

import click
import markdown
from weasyprint import HTML, CSS
from pathlib import Path
import sys


def get_default_css():
    """Return default CSS styling for the PDF."""
    return """
    @page {
        size: A4;
        margin: 2cm;
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #333;
        max-width: 100%;
    }

    h1, h2, h3, h4, h5, h6 {
        margin-top: 1.5em;
        margin-bottom: 0.5em;
        font-weight: 600;
        line-height: 1.25;
        color: #1a1a1a;
    }

    h1 {
        font-size: 2em;
        border-bottom: 2px solid #e1e4e8;
        padding-bottom: 0.3em;
    }

    h2 {
        font-size: 1.5em;
        border-bottom: 1px solid #e1e4e8;
        padding-bottom: 0.3em;
    }

    h3 { font-size: 1.25em; }
    h4 { font-size: 1em; }
    h5 { font-size: 0.875em; }
    h6 { font-size: 0.85em; color: #6a737d; }

    p {
        margin-top: 0;
        margin-bottom: 1em;
    }

    a {
        color: #0366d6;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    code {
        background-color: #f6f8fa;
        border-radius: 3px;
        font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
        font-size: 85%;
        padding: 0.2em 0.4em;
    }

    pre {
        background-color: #f6f8fa;
        border-radius: 6px;
        padding: 16px;
        overflow: auto;
        font-size: 85%;
        line-height: 1.45;
    }

    pre code {
        background-color: transparent;
        padding: 0;
        font-size: 100%;
    }

    blockquote {
        border-left: 4px solid #dfe2e5;
        color: #6a737d;
        padding-left: 1em;
        margin-left: 0;
        margin-right: 0;
    }

    ul, ol {
        padding-left: 2em;
        margin-top: 0;
        margin-bottom: 1em;
    }

    li {
        margin-bottom: 0.25em;
    }

    table {
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 1em;
    }

    table th,
    table td {
        border: 1px solid #dfe2e5;
        padding: 6px 13px;
    }

    table th {
        background-color: #f6f8fa;
        font-weight: 600;
    }

    table tr:nth-child(2n) {
        background-color: #f6f8fa;
    }

    hr {
        border: 0;
        border-top: 2px solid #e1e4e8;
        margin: 1.5em 0;
    }

    img {
        max-width: 100%;
        height: auto;
    }

    strong {
        font-weight: 600;
    }

    em {
        font-style: italic;
    }
    """


def convert_markdown_to_pdf(input_file, output_file, custom_css=None):
    """
    Convert a markdown file to PDF.

    Args:
        input_file: Path to the input markdown file
        output_file: Path to the output PDF file
        custom_css: Optional custom CSS string or file path
    """
    # Read the markdown file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    except FileNotFoundError:
        click.echo(f"Error: File '{input_file}' not found.", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Error reading file: {e}", err=True)
        sys.exit(1)

    # Convert markdown to HTML with extensions for better support
    md = markdown.Markdown(extensions=[
        'extra',          # Tables, fenced code blocks, etc.
        'codehilite',     # Syntax highlighting
        'nl2br',          # Newline to <br>
        'sane_lists',     # Better list handling
        'toc',            # Table of contents
    ])

    html_content = md.convert(markdown_content)

    # Wrap in a complete HTML document
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Converted PDF</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Prepare CSS
    css_list = [CSS(string=get_default_css())]

    if custom_css:
        css_path = Path(custom_css)
        if css_path.exists() and css_path.is_file():
            css_list.append(CSS(filename=str(css_path)))
        else:
            css_list.append(CSS(string=custom_css))

    # Convert to PDF
    try:
        html = HTML(string=full_html)
        pdf = html.write_pdf(stylesheets=css_list)
        with open(output_file, 'wb') as f:
            f.write(pdf)
        click.echo(f"✅ Successfully converted '{input_file}' to '{output_file}'")
    except Exception as e:
        click.echo(f"Error converting to PDF: {e}", err=True)
        sys.exit(1)


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('-o', '--output', 'output_file',
              help='Output PDF file path (default: same name as input with .pdf extension)')
@click.option('-c', '--css', 'custom_css',
              help='Custom CSS file or CSS string to style the PDF')
@click.option('-v', '--verbose', is_flag=True,
              help='Enable verbose output')
def main(input_file, output_file, custom_css, verbose):
    """
    Convert a Markdown file to PDF.

    INPUT_FILE: Path to the markdown file to convert

    Examples:

        md2pdf document.md

        md2pdf document.md -o output.pdf

        md2pdf document.md --css custom.css

        md2pdf document.md --css "body { font-size: 14pt; }"
    """
    # Determine output file name
    if not output_file:
        input_path = Path(input_file)
        output_file = input_path.with_suffix('.pdf')

    if verbose:
        click.echo(f"Input file: {input_file}")
        click.echo(f"Output file: {output_file}")
        if custom_css:
            click.echo(f"Custom CSS: {custom_css}")

    # Convert the file
    convert_markdown_to_pdf(input_file, output_file, custom_css)


if __name__ == '__main__':
    main()
