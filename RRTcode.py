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
# Filter rows where the Outcome column contains the word 'Active'
if outcome_column in df.columns:
    active_cases = df[df[outcome_column].str.contains('Active', case=False, na=False)]
    print(active_cases)
    #DataFrame to a CSV file
    active_cases.to_csv('active_cases.csv', index=False)

    # Extract inactive cases
    inactive_cases = df[~df[outcome_column].str.contains('Active', case=False, na=False)]
    print(inactive_cases)
    # Save inactive cases to CSV
    inactive_cases.to_csv('inactive_cases.csv', index=False)

else:
    print(f"Column'{outcome_column}' does not exist. Available columns are:",df.columns)
#Drop duplicate
No_Duplicates = df.drop_duplicates()
print(No_Duplicates)
#Dataframe to a csv file
No_Duplicates.to_csv('No_Duplicates.csv', index=False)

# Calculate the age of the file as the difference between 'Audit date' and 'Registered'
df['Age of File'] = (df['Audit Date'] - df['Registered']).dt.days

# Display the first few rows of the dataframe to check the result
print("\nData with 'Age of File' column:")
Age_of_File=df[['Code/Year','Registered', 'Audit Date', 'Age of File']]
print(Age_of_File)
Age_of_File.to_csv(('Age_of_File.csv'), index=False)




