function RunGenerateReadme {
    Set-Location -Path 'C:\Users\kade\projects\notebooks'
    conda activate C:\Users\kade\projects\.venv
    & 'C:\Users\kade\miniconda3\python.exe' '.\Scripts\generate-README.py'
    conda deactivate
}

RunGenerateReadme
