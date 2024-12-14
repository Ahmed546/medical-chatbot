import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "reqirements.txt",
    "setup.py",
    "app.py",
    "research/trails.ipynb",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html",
    "model/abc.txt",
    ""
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object
    filedir = filepath.parent  # Get the directory of the file
    filename = filepath.name   # Get the file name

    if filedir != "":  # Ensure there's a directory to create
        filedir.mkdir(parents=True, exist_ok=True)  # Create the directory
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if not filepath.exists() or filepath.stat().st_size == 0:  # Check if file doesn't exist or is empty
        with filepath.open("w") as f:  # Open file safely with Path object
            pass  # Create the empty file
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")