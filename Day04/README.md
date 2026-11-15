# Day 4: Protein Calculator Web Application

## Project Overview

In Day03, I developed a Python program that calculates the theoretical molecular weight and amino acid composition of protein sequences.

In Day04, I extended the project by converting it into a web application using Flask.

## Main Features

- Upload protein sequences using FASTA files.
- Calculate theoretical protein molecular weight.
- Calculate amino acid composition and percentages.
- Display results in a web interface.
- Handle invalid protein sequences.

## Project Structure

- `main.py` – Original command-line application.
- `app.py` – Flask web application.
- `protein_logic.py` – Shared biological calculation functions.
- `proteins.fasta` – Example protein sequences.
- `templates/index.html` – HTML web interface.

## Technologies

- Python
- Flask
- HTML
- CSS
- VS Code
- Git and GitHub

## Implementation

The biological computation functions were separated into `protein_logic.py`.

Both the original command-line application and the Flask web application use the same business logic.

The Flask application allows users to upload FASTA files and view protein analysis results through a browser.

## Testing

- Tested the original Day03 Python application.
- Tested the Day04 command-line application.
- Tested the Flask web application.
- Tested valid and invalid FASTA files.

## AI Assistance

AI tools were used during development to understand Python functions, implement the Flask application, debug errors, and improve the code.