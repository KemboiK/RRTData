# RRTData
# Legal Case Data Processing Script
## Overview
This Python script is designed to process legal case data from an Excel file. It performs various data transformations and analyses, including date conversions, categorization of case ages, and filtering cases based on their status. The script outputs CSV and Excel files that categorize cases into active, inactive, and based on the age of the case.

## Features
1. Date Conversion: Converts various date columns to datetime formats.
2. Data Cleaning: Removes duplicate records to ensure data integrity.
3. Case Filtering: Separates cases into active and inactive based on specific keywords in the 'Outcome' column.
4. Age Calculation: Calculates the age of each case from the registered date to the audit date.
5. Categorization: Categorizes cases based on their age and outputs separate files for each category.
## Prerequisites
Before running this script, ensure you have these installed:
Python 3.x
Pandas library
NumPy library
Matplotlib library
An Excel file with legal case data named RRT data.xlsx located in the /content/ directory.

You can install the necessary Python libraries using pip:
pip install pandas numpy matplotlib
## Setup
Place your Excel file with the name RRT data.xlsx in the /content/ directory.
Ensure the Excel file has the necessary columns formatted correctly as per the script requirements.
Usage
Run the script using Python from your terminal:

python legal_case_processing.py
## Output
The script will generate the following files in the current directory:

- No_Duplicates.csv and No_Duplicates.xlsx: Data without duplicates.
- active_cases.csv and active_cases.xlsx: Cases filtered by active status.
- inactive_cases.csv and inactive_cases.xlsx: Cases filtered by inactive status.
- Files for each age category of cases, e.g., Less_than_1_year_cases.csv.
## Contributing
Feel free to fork this repository and submit pull requests. You can also open issues for any bugs found or enhancements proposed.
