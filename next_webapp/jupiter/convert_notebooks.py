import os
import sys
from pathlib import Path
import nbformat
from nbconvert import HTMLExporter
 
def read_notebook_file(notebook_path: Path):
    """Read a Jupyter notebook file and return the notebook object."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        return nbformat.read(f, as_version=4)
 
def convert_notebook_to_html(notebook) -> str:
    """Convert a notebook object to HTML string."""
    html_exporter = HTMLExporter()
    html_exporter.exclude_input_prompt = True
    html_exporter.exclude_output_prompt = True
    body, _ = html_exporter.from_notebook_node(notebook)
    return body
 
def write_html_file(html_content: str, output_path: Path):
    """Write HTML content to a file."""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)