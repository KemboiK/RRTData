import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
#import the data
df = pd.read_excel("RRT data.xlsx")
# Adjust the column name according to your actual data

# Convert the 'Audit Date' column to datetime format
df['Audit Date'] = '2024/05/31'
# Convert both 'Audit Date' and 'Registered' columns to pd.Timestamp
df['Audit Date'] = pd.to_datetime(df['Audit Date'], format="%Y/%m/%d")
# Combine 'Day', 'Month.1', and 'Year.1' into a single datetime column for 'Registered'
df['Registered'] = pd.to_datetime(df[['Year.1', 'Month.1', 'Day']]
                                  .rename(columns={'Year.1': 'Year', 'Month.1': 'Month'}), errors='coerce')
#Combine Day.2, Month.2, Year.2 into a single datatime column for Date Last in court
df['Date_Last_in_Court']= pd.to_datetime(df[['Year.2','Month.2','Day.1']]
                                         .rename(columns={'Year.2': 'Year', 'Month.2': 'Month', 'Day.1': 'Day'}), format='%d/%m/%Y', errors='coerce')
#Combine Code and Year with a slash
df['Code/Year']= df['No'].astype(str)+'/'+df['Year.1'].astype(str)
outcome_column = 'Outcome'
#Drop duplicate
No_Duplicates = df.drop_duplicates()
print(No_Duplicates)
#Dataframe to a csv file
No_Duplicates.to_csv('No_Duplicates.csv', index=False)
No_Duplicates.to_excel('No_Duplicates.xlsx', index=False)
# Filter rows where the Outcome column contains the word 'Active'
if outcome_column in df.columns:
    active_cases = No_Duplicates[No_Duplicates[outcome_column].str.contains('Active|activity|Adjourned|Pleadings|Parties|Plaintiff|Matters|distress|Respondent|Decreed|Recover|Pending|Dormant|served|Defendant|Interparties|Court|Hearing', case=False, na=False)]
    print(active_cases)
    #DataFrame to a CSV file
    active_cases.to_csv('active_cases.csv', index=False)
    active_cases.to_excel('active_cases.xlsx', index=False)

    # Extract inactive cases
    inactive_cases = No_Duplicates[~No_Duplicates[outcome_column].str.contains('Active|activity|Adjourned|Pleadings|Parties|Plaintiff|Matters|distress|Respondent|Decreed|Recover|Pending|Dormant|served|Defendant|Interparties|Court|Hearing', case=False, na=False)]
    print(inactive_cases)
    # Save inactive cases to CSV
    inactive_cases.to_csv('inactive_cases.csv', index=False)
    inactive_cases.to_excel('inactive_cases.xlsx', index=False)

else:
    print(f"Column'{outcome_column}' does not exist. Available columns are:",df.columns)


# Calculate the age of the file as the difference between 'Audit date' and 'Registered'
No_Duplicates['Age of File'] = (No_Duplicates['Audit Date'] - No_Duplicates['Registered']).dt.days/ 365.2425

# Display the first few rows of the dataframe to check the result
print("\nData with 'Age of File' column:")
print(No_Duplicates[['Code/Year', 'Registered', 'Audit Date', 'Age of File']].head())

Age_of_File_column= 'Age of File'
def categorize_age(Age_of_File_column):
  if Age_of_File_column < 1:
    return 'Less than 1 year'
  elif Age_of_File_column<=3:
    return "1 to 3"
  else:
    return 'Over 3'
#Apply the function to the age column
No_Duplicates['age_category']=No_Duplicates['Age of File'].apply(categorize_age)

# Filter and save data based on categories
categories = No_Duplicates['age_category'].unique()
for category in categories:
    subset = No_Duplicates[No_Duplicates['age_category'] == category]
    subset.to_csv(f'{category.replace(" ", "_")}_cases.csv', index=False)  # Save as CSV
    subset.to_excel(f'{category.replace(" ", "_")}_cases.xlsx', index=False)  # Save as Excel

# Display the first few rows of the dataframe to check the result
print("\nData with 'Age of File' column:")
print(No_Duplicates[['Code/Year', 'Registered', 'Audit Date', 'Age of File', 'age_category']].head())









