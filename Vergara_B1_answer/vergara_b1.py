#VERGARA, IVYANN ROMIJN H. 
# 1. Extract only rows where the ‘Interval’ is 30-0 and save to a new file. (3 points)

import pandas as pd

# open file
filename = 'Ivyann Romijn Vergara - Exam_Table.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(filename)

# Filter rows where 'Interval' is '30-0'
new_df = df[df['Interval'] == '30-0']

# Save the filtered data to a CSV file 
new_df.to_csv('b1_output.csv', index=False)

print("Saved a new file.")
