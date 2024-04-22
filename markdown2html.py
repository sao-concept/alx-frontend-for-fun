#!/usr/bin/env python3

import argparse
import sys
import markdown

def convert_markdown_to_html(input_file: str, output_file: str) -> None:
    """
    Convert Markdown file to HTML file.

    Args:
        input_file (str): Name of the Markdown file.
        output_file (str): Name of the output HTML file.

    Raises:
        FileNotFoundError: If the Markdown file doesn't exist.
    """
    try:
        # Read Markdown content
        with open(input_file, 'r') as md_file:
            markdown_content = md_file.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)

        # Write HTML content to output file
        with open(output_file, 'w') as html_file:
            html_file.write(html_content)
    except FileNotFoundError:
        # Print error message if Markdown file doesn't exist
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

def main() -> None:
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Convert Markdown file to HTML file")
    parser.add_argument("input_file", help="Name of the Markdown file")
    parser.add_argument("output_file", help="Name of the output HTML file")
    args = parser.parse_args()

    # Convert Markdown to HTML
    convert_markdown_to_html(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
