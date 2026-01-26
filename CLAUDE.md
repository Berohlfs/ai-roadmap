# CLAUDE.md

## Project Overview

Educational Python notebooks for learning AI/ML fundamentals. Structured curriculum with interactive Jupyter notebooks.

## Tech Stack

- Python 3.14
- Jupyter Notebooks
- NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn
- UV package manager

## Project Structure

```
notebooks/
├── src/
│   ├── welcome.ipynb              # Environment setup verification
│   ├── chapter-1-python-basics/   # Python fundamentals
│   └── playground/                # Practice area
├── data/                          # Datasets (CSV files)
└── pyproject.toml                 # Dependencies
md/                                # Documentation
```

## Commands

```bash
cd notebooks
uv sync          # Install dependencies
uv run python    # Run Python in venv
```

## Conventions

- Notebook naming: `number-topic-name.ipynb` (e.g., `1-data-types.ipynb`)
- Each notebook starts with a markdown title cell, followed by sections
- Use f-strings for output
- Progress from simple to complex concepts within each notebook
