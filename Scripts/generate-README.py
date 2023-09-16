import os
import nbformat
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Define the README file path
readme_file = "README.md"

# Define the GitHub repository base URL
github_base_url = "https://github.com/ka-de/notebooks/blob/main/"

# Define the table header
table_header = """# 🪐 Jupyter Notebooks 🪐

I'm attempting to rectify my failing brain's fatal mistake of learning Python too late in life. Feel free to use this repository to study the behavior of chimpanzees.

![Jupiter, in all its glory.](https://github.com/ka-de/notebooks/raw/main/Data/jupiter.jpg)
Credit: NASA, ESA, CSA, Jupiter ERS Team; image processing by Ricardo Hueso (UPV/EHU) and Judy Schmidt.

Name | What does it do?
:---|:---
"""

# Create a new README.md file with the table header
with open(readme_file, "w", encoding="utf-8") as readme:
    readme.write(table_header)

print("README.md created with table header.")

# Function to extract title from a Jupyter notebook
def extract_title_from_notebook(notebook_path):
    try:
        with open(notebook_path, "r", encoding="utf-8") as notebook_file:
            notebook_content = nbformat.read(notebook_file, as_version=4)
            cells = notebook_content.cells
            for cell in cells:
                if cell.cell_type == "markdown":
                    lines = cell.source.split("\n")
                    for line in lines:
                        if line.startswith("# "):
                            return line[2:].strip()
    except Exception as e:
        print(f"Error extracting title from {notebook_path}: {e}")
    return None

# Walk through the current directory and its subdirectories
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".ipynb"):
            notebook_path = os.path.join(root, file)
            title = extract_title_from_notebook(notebook_path)
            if title:
                relative_path = os.path.relpath(notebook_path, start=".")
                subdirectory = os.path.dirname(relative_path)
                # Normalize the notebook path by replacing backslashes with forward slashes
                notebook_path = notebook_path.replace("\\", "/")
                # Remove leading "./" from the notebook path
                notebook_path = notebook_path.lstrip("./")
                # Create the URL for the notebook
                notebook_url = f"[{notebook_path}]({github_base_url}{notebook_path.replace(' ', '%20')})"
                # Create the "What does it do" line
                what_does_it_do = f"**{subdirectory}** - {title}"
                line = f"{notebook_url} | {what_does_it_do}"
                print(f"Adding: {line}")
                with open(readme_file, "a", encoding="utf-8") as readme:
                    readme.write(line + "\n")
            else:
                print(f"Skipped: {notebook_path}")

print("Table of Contents updated in README.md.")