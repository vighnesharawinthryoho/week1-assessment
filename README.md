# Week 1 Assessment

## Setup Steps
1. Open week1-assessment in VS Code or PowerShell.
2. Create and activate the virtual environment: python -m venv .venv and .\.venv\Scripts\Activate.ps1.
3. Install dependencies with pip install -r requirements.txt and add API_KEY to .env.
4. Run scripts in src/ or open 
otebooks/analysis.ipynb to run the analysis and %timeit check.

## Summary of Findings
1. Across 8 employees in employees.csv, 5 earn above 50,000 and 4 are based in Chennai.
2. Removing duplicate rows and filling missing salaries with the median keeps cleaned data consistent.
3. groupby().agg() shows differences in headcount, average pay, and top salary across departments.
4. An outer merge with departments.csv highlights departments that currently have zero employees.
5. NumPy broadcasting and 
p.dot compute grace marks, subject averages, and weighted scores cleanly.
