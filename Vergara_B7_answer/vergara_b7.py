#VERGARA, IVYANN ROMIJN H. 
# 7. Transpose the contents such that the column headers become row headers.

import pandas as pd
# Open file
filename = 'Ivyann Romijn Vergara - Exam_Table.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(filename, skip_blank_lines=True).dropna()

# Read the CSV file into a DataFrame
df = pd.read_csv(filename)

transposed_data = df.transpose()

# Save the filtered data to a CSV file
transposed_data.to_csv('b7_output.csv', index=False)

print("Saved a new file.")