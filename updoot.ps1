function RunGenerateReadme {
    Set-Location -Path 'C:\Users\kade\projects\notebooks'
    conda activate C:\Users\kade\projects\notebooks\.venv
    & 'C:\Users\kade\anaconda3\python.exe' '.\Scripts\generate-README.py'
    conda deactivate
}

RunGenerateReadme
