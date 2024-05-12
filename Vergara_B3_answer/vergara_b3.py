#VERGARA, IVYANN ROMIJN H. 
# 3. Get all unique scientific names and save them to a new file. (4 points)

import pandas as pd

# open file
filename = 'Ivyann Romijn Vergara - Exam_Table.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(filename, skip_blank_lines=True).dropna()

new_df = unique_names = df['Scientific Name'].unique()  

new_df = pd.DataFrame({"Scientific Names": new_df})
# Save the filtered data to a CSV file 
new_df.to_csv('./b3_output.csv', index=False)

print("Saved a new file.")
