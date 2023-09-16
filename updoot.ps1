function RunGenerateReadme {
    Set-Location -Path 'C:\Users\kade\projects\notebooks'
    conda activate notebook-env
    & 'C:\Users\kade\anaconda3\python.exe' '.\Scripts\generate-README.py'
    conda deactivate
}

RunGenerateReadme